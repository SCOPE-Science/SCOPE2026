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
The universal proof uses only finite-field linear algebra and does not depend on enumeration.

For
\[
x=(a,v,c),\qquad y=(d,w,f),
\]
the direct multiplication law gives
\[
[x,y]=(0,(a-c)w-(d-f)v,0).
\]
The center, centralizers, and commutator fibers all follow from this equation.

The packaged checker `artifacts/verify.py` independently constructs the multiplication and enumerates all ordered pairs for
\[
(q,r)=(2,1),(2,2),(2,3),(3,1),(3,2),(4,1),(4,2).
\]
For \(\mathbf F_4\), it implements
\[
\mathbf F_2[t]/(t^2+t+1)
\]
directly.

For every test case the checker verifies:

- exactly \(q^r+2\) distinct element-centralizers;
- the predicted centralizer-size multiset;
- the exact zero commutator fiber;
- the common size of every nonzero radical commutator fiber;
- the commuting-probability formula.

It additionally verifies that \(A_{2,2}\) and \(A_{1,4}\) both have six centralizers while their commuting probabilities are \(7/16\) and \(19/64\).

The checker returns `VERIFY_OK`.

Finite enumeration is not used to prove the theorem.
