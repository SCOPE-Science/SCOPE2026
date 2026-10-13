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
The exact proof has two components. First, component intersections show that the only singular points are \(q=[0:0:1]\) and \(p_j=V(z,\ell_j)\), and a local unit-root change reduces the latter germ to \(uv(u^{k_j}-v^d)=0\). Second, weighted homogeneity gives the local numerical invariants and threshold.

The supplied `verify.py` checks the weighted Euler identity and, for every \((d,k)\) with \(2\le d\le8\) and \(1\le k\le d\), computes a Gröbner basis of the Jacobian ideal and counts standard monomials, obtaining \((d+1)(k+1)\). It also verifies the symbolic global Tjurina identity, the derivative
\[
-\frac{d^2}{(dk+d+k)^2},
\]
and the examples \(2/5\) and \(5/17\). This finite grid is a replay check, not the proof of the universally quantified statement; the proof is the weighted-homogeneous calculation in `RESULT.md`.
