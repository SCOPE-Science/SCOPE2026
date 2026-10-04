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

The decisive published input is the exact non-torsion elliptic ruled-surface formula
\[
arepsilon(A,x)=rac{2n(n+1)b+a}{2n+1},
\qquad
n=\left\lfloor\sqrt{rac{a}{2b}}ightfloor,
\]
for a point away from the two distinguished sections. The same source gives the corresponding chamber structure and the general upper bound by \(\sqrt{A^2}\).

The proof in `RESULT.md` is purely algebraic once that theorem is fixed. It rewrites \(A^2-arepsilon(A,x)^2\), factors the numerator, and then minimizes the exact normalized ratio on each chamber. This establishes the infinite statement without relying on finite computation.

The standalone checker `artifacts/verify_seshadri_gap.py` uses exact rational arithmetic. It verifies the factorization, the equality-with-volume criterion, and the chamber lower-bound equality condition for every integer pair \(1\le a,b\le 200\). A successful replay prints `VERIFY_OK 40000 integer classes`.

The finite replay is a regression test, not an exhaustive proof for all real or integral ample classes. No independent audit or external certification has been performed.
