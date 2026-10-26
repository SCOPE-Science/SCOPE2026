"""Reproducible checks for three-component weak-edge Grover transport.

Requires Python 3 and NumPy. Run: python verification_three_bridge.py
The theorem's infinite-parameter and asymptotic assertions require its analytic proof.
"""
import math
import numpy as np


def reduced_laplacian(masses, bridges):
    a, b, c = map(float, masses)
    k, h = map(float, bridges)
    lap = np.array([[k, -k, 0.0], [-k, k+h, -h], [0.0, -h, h]], dtype=float)
    d = np.sqrt(np.array([a, b, c]))
    return lap / np.outer(d, d)


def cosine_amplitude(lap, tau):
    eigenvalues, vectors = np.linalg.eigh(lap)
    assert np.min(eigenvalues) > -1e-10
    factors = np.cos(tau * np.sqrt(np.maximum(eigenvalues, 0.0)))
    return float(((vectors * factors) @ vectors.T)[2, 0])


def symmetric_amplitude(m_outer, m_middle, k, tau):
    omega_a = math.sqrt(k / m_outer)
    omega_s = math.sqrt(k / m_outer + 2*k / m_middle)
    return (m_outer / (2*m_outer+m_middle)
            - 0.5 * math.cos(omega_a*tau)
            + m_middle/(2*(2*m_outer+m_middle)) * math.cos(omega_s*tau))


def original_grover(block_edge_counts, epsilon):
    """Take three path-shaped connected components and two weak bridges."""
    sizes = [e + 1 for e in block_edge_counts]
    offsets = np.cumsum([0] + sizes[:-1]).tolist()
    undirected = []
    for off, count in zip(offsets, block_edge_counts):
        for j in range(count):
            undirected.append((off+j, off+j+1, 1.0))
    undirected += [(offsets[0], offsets[1], epsilon),
                   (offsets[1]+sizes[1]-1, offsets[2], epsilon)]
    directed = []
    for u, v, w in undirected:
        directed.extend([(u,v,w), (v,u,w)])
    arc = [(u,v) for u,v,_ in directed]
    weight = {(u,v):w for u,v,w in directed}
    degree = np.zeros(sum(sizes))
    for u,v,w in directed:
        degree[u] += w
    inv = {edge:i for i,edge in enumerate(arc)}
    N = len(arc)
    U = np.zeros((N,N),dtype=complex)
    for i,(u,v) in enumerate(arc):
        for j,(s,t) in enumerate(arc):
            if v == t:
                val = 2*math.sqrt(weight[(v,u)]*weight[(t,s)])/degree[v]
                if i == j:
                    val -= 1
                U[inv[(v,u)], j] = val
    initial = np.zeros(N,complex)
    initial_arcs = [(i,u,v) for i,(u,v) in enumerate(arc)
                    if u < sizes[0] and v < sizes[0]]
    for i,u,v in initial_arcs:
        initial[i] = 1/math.sqrt(len(initial_arcs))
    target_start = offsets[2]
    target_indices = [i for i,(u,v) in enumerate(arc)
                      if u >= target_start and v >= target_start]
    assert np.linalg.norm(U.conj().T @ U - np.eye(N)) < 2e-12
    assert abs(np.linalg.norm(initial)-1)<1e-12
    return U,initial,target_indices


def run_checks():
    count=0
    rng = np.random.default_rng(987123)
    for _ in range(160):
        M=int(rng.integers(1,20))*2
        m=int(rng.integers(1,20))*2
        K=int(rng.integers(1,6))
        tau=float(rng.uniform(0,70))
        reduced = cosine_amplitude(reduced_laplacian([M,m,M],[K,K]),tau)
        exact = symmetric_amplitude(M,m,K,tau)
        assert abs(reduced-exact)<4e-12, (M,m,K,tau,reduced,exact)
        count += 1
    # A true resonant case: ratio sqrt(1+2*M/m) = 2.
    tau=math.pi*math.sqrt(6)
    assert abs(symmetric_amplitude(6,4,1,tau)-1)<1e-14
    count+=1
    # A rational parity obstruction: ratio 3 has no perfect three-mode alignment.
    L=reduced_laplacian([8,2,8],[1,1])
    times=np.linspace(0,2*math.pi*math.sqrt(8),1001)
    maximum=max(cosine_amplitude(L,float(t))**2 for t in times)
    assert maximum < 0.999
    count+=1
    # The zero-mode mismatch bound applies at every sampled time.
    masses=(6,4,12)
    S=sum(masses)
    cap=(math.sqrt(masses[0]*masses[2])+math.sqrt((masses[0]+masses[1])*(masses[1]+masses[2])))/S
    assert cap < 1
    L=reduced_laplacian(masses,[1,1])
    for t in np.linspace(0,150,125):
        assert abs(cosine_amplitude(L,float(t))) <= cap+1e-12
        count+=1
    # Pell witnesses, norm and explicit upper bounds.
    x,q=2,1
    for _ in range(4):
        assert x*x-3*q*q == 1 and x%2==0 and q%2==1
        tau=math.pi*q*math.sqrt(12)
        p=symmetric_amplitude(12,12,1,tau)**2
        assert p>1-math.pi**2/(72*q*q)-1e-12
        count+=2
        x,q=7*x+12*q,4*x+7*q
    # An independently built full arc-space walk approaches its reduced prediction.
    for blocks,eps,q in [([3,2,3],0.0001,1),
                          ([6,6,6],0.0001,1),
                          ([6,6,6],0.000001,15),
                          ([6,6,6],0.00000001,15)]:
        M=2*blocks[0]; m=2*blocks[1]
        U,initial,target=original_grover(blocks,eps)
        tau=math.pi*q*math.sqrt(M)
        t=round(tau/math.sqrt(2*eps))
        actual=np.linalg.matrix_power(U,t)@initial
        probability=float(np.sum(np.abs(actual[target])**2))
        predicted=symmetric_amplitude(M,m,1,t*math.sqrt(2*eps))**2
        assert abs(probability-predicted)<0.03,(blocks,eps,t,probability,predicted)
        count+=3
    print(f"PASS: {count} finite checks; no claim of exhaustive/infinite computational verification")


if __name__=='__main__':
    run_checks()
