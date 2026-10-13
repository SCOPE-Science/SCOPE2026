import itertools
import numpy as np

def unique_permutations(x):
    return np.array(sorted(set(itertools.permutations(x))), dtype=float)

def population_cov(X):
    mu = X.mean(axis=0)
    Y = X - mu
    return (Y.T @ Y) / len(X)

def check_law(weights, grads):
    T = weights.shape[1]
    assert np.max(np.abs(weights.sum(axis=1) - 1.0)) < 1e-13
    assert np.min(weights) >= -1e-14

    mean_w = weights.mean(axis=0)
    assert np.max(np.abs(mean_w - 1.0/T)) < 1e-13
    Cw = population_cov(weights)
    v = Cw[0,0]
    P = np.eye(T) - np.ones((T,T))/T
    target_w = v*T/(T-1)*P
    assert np.max(np.abs(Cw-target_w)) < 2e-13

    Z = weights @ grads
    Cz = population_cov(Z)
    gbar = grads.mean(axis=0)
    centered = grads - gbar
    scatter = centered.T @ centered
    target_z = v*T/(T-1)*scatter
    assert np.max(np.abs(Cz-target_z)) < 3e-12

    energy = np.trace(Cz)
    pair = 0.0
    for i in range(T):
        for j in range(i+1,T):
            pair += np.sum((grads[i]-grads[j])**2)
    assert abs(energy - v/(T-1)*pair) < 3e-12

    if v > 1e-14:
        assert np.linalg.matrix_rank(Cz, tol=1e-10) == np.linalg.matrix_rank(centered, tol=1e-10)

# Exact finite exchangeable laws obtained from all coordinate permutations.
laws = [
    unique_permutations((0.7,0.2,0.1)),
    unique_permutations((0.5,0.3,0.15,0.05)),
    unique_permutations((0.4,0.4,0.1,0.1)),
]
grad_sets = [
    np.array([[1.0,2.0],[-2.0,1.0],[0.5,-1.0]]),
    np.array([[1.0,0.0,2.0],[-1.0,3.0,0.0],[2.0,-2.0,1.0],[0.0,1.0,-3.0]]),
    np.array([[1.0,0.0],[0.0,1.0],[-1.0,0.0],[0.0,-1.0]]),
]
for W,G in zip(laws,grad_sets):
    check_law(W,G)

# Uniform one-hot is the sharp variance endpoint.
for T in range(2,9):
    W = np.eye(T)
    Cw = population_cov(W)
    v = Cw[0,0]
    assert abs(v - (T-1)/T**2) < 2e-15
    # Every sampled simplex coordinate obeys x^2 <= x, giving the universal endpoint.
    for law in [unique_permutations(tuple([0.55]+[(0.45/(T-1))]*(T-1))) if T > 2
                else unique_permutations((0.65,0.35))]:
        vv = population_cov(law)[0,0]
        assert vv < (T-1)/T**2 + 1e-14

# Two-task specialization: covariance is v times the outer product of the disagreement.
W = unique_permutations((0.8,0.2))
G = np.array([[2.0,-1.0,4.0],[-3.0,5.0,1.0]])
Cz = population_cov(W @ G)
v = population_cov(W)[0,0]
d = G[0]-G[1]
assert np.max(np.abs(Cz - v*np.outer(d,d))) < 2e-13

# Consensus gradients give zero weight-induced noise for every law.
W = unique_permutations((0.7,0.2,0.1))
G = np.tile(np.array([2.0,-4.0,1.5]), (3,1))
assert np.max(np.abs(population_cov(W @ G))) < 2e-13

print("verification passed")
