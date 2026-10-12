---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
For connected simple graphs on a fixed number \(n\) of vertices, the homogeneous threshold
\[
\tau_{\mathrm{avg}}=\frac1{\bar d}
\]
is ordered exactly by edge count, while the spectral threshold
\[
\tau_{\mathrm{spec}}=\frac1{\rho(A)}
\]
is ordered exactly by adjacency spectral radius.

The embedded `verify_epidemic_density_spectral_boundary.py` generates all
\[
2^{\binom n2}
\]
labeled simple graphs for each
\[
2\le n\le5,
\]
filters for connectivity, and then removes only label duplicates by exact permutation canonicalization.

It recovers connected unlabeled class counts
\[
1,2,6,21.
\]

For each class it computes the integer adjacency characteristic polynomial and uses exact rational real-root isolation to bound the largest eigenvalue. Every pair with different edge counts is checked, and no pair with fewer edges has strictly larger spectral radius.

The six-vertex witness is symbolic:
\[
\bar d(K_{1,5})=\frac53,
\qquad
\rho(K_{1,5})=\sqrt5,
\]
while
\[
\bar d(C_6)=2,
\qquad
\rho(C_6)=2.
\]

The persistent family follows from
\[
\frac{2(n-1)}n<2
\]
and
\[
\sqrt{n-1}>2
\]
for every integer
\[
n\ge6.
\]

Run:

`python3 verify_epidemic_density_spectral_boundary.py`

The first output line must be:

`VERIFY_OK`

The verifier reports the SymPy version and installed package path actually used for exact characteristic polynomials and rational root isolation.
