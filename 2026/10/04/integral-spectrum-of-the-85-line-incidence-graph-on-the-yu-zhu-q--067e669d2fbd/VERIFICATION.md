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
# Verification

`verify_incidence.py` uses exact rational arithmetic in the basis of \(\mathbb Q(a,b,i)\), with reductions \(a^4=2\), \(b^4=3\), and \(i^2=-1\). It reconstructs the explicit line equations from Yu--Zhu Section 3 and checks all \(3570\) unordered pairs by exact \(4\times4\) determinants.

The replay certifies \(85\) lines, degree \(20\) at every graph vertex, \(850\) edges, the adjacent-pair common-neighbor census, the annihilating polynomial
\[
(z-20)(z-3)(z+1)(z+3)(z+5)(z+9),
\]
and traces through the fifth power. Since the adjacency matrix is symmetric and the roots are distinct, these exact checks determine the stated eigenvalue multiplicities. The shifted matrix \(A-3I\) is then checked to have rank \(39\) and inertia \((1,38,46)\).

The recorded `verify_output.txt` ends with `VERIFY_OK`. The verification does not reprove the source theorem that the displayed equations exhaust every line on the surface; it verifies the incidence and spectral conclusions for that complete source list.
