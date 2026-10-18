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

# Mathematical verification

The full statement and proof are in `RESULT.md`. The core check is the equivalence between \(K\sim4p\) and integrality of the unique harmonic potential for \(4v_2-4p\). The existence and uniqueness of the real potential follow from the connected positive-conductance Laplacian (one zero eigenvalue). Away from the support of its divisor it cannot bend at unmarked interior points.

For \(p\) on the variable edge, the exact slope calculation yields

\[
k=\frac{4t-3\lambda-1}{2(\lambda+1)},\qquad
\text{slopes}=(k-1,k,-k-2,-k-1,1,1-2k,-3-2k).
\]

The list is integral exactly when \(k\) is integral. The allowed open interval for \(k\) contains no integers other than \(-1,0\), which produce the two points stated in the finding only when \(\lambda>1\). For points in the interiors of the other five edges, the respective unavoidable noninteger slopes are \(1-t,1-t,1+t,1+t,-t\). The variable-edge endpoint test gives \(\lambda=1\) exactly.

To reproduce independent exact-rational spot checks, execute `python3 verify.py`. This checks several rational choices of \(\lambda\) and every point of a finite \(1/16\)-spaced grid in each open edge by fraction-preserving Gaussian elimination. A finite grid is **not** an exhaustive search over all real points or irrational lengths; only the symbolic argument certifies those.
