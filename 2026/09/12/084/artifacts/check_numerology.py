"""Sanity check of numerical inputs for the Cartan-group topological lemma.

Verifies:
  - free step-3 rank-2 layer dimensions (2,1,2) sum to topological dim 5;
  - homogeneous dimension Q = 1*2 + 2*1 + 3*2 = 10;
  - ambient dimension n=5 satisfies n>=3, so exterior U ~= S^{n-1}
    is simply connected (pi_1(S^{k})=0 for k>=2) and complement-of-compact
    has exactly one unbounded component.
"""
layer_dims = {1: 2, 2: 1, 3: 2}
top_dim = sum(layer_dims.values())
Q = sum(i * d for i, d in layer_dims.items())
n = top_dim
sphere_dim = n - 1
simply_connected_regime = sphere_dim >= 2  # pi_1(S^k)=0 for k>=2
print(f"layer_dims={layer_dims} top_dim={top_dim} Q={Q} n={n} "
      f"sphere_dim={sphere_dim} simply_connected={simply_connected_regime}")
assert top_dim == 5, top_dim
assert Q == 10, Q
assert n >= 3, n
assert simply_connected_regime
print("OK: Cartan numerology (dim 5, Q 10, n>=3 simply-connected exterior).")
