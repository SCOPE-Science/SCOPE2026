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

The proof was checked symbolically over an arbitrary ground field \(F\). No finite experiment is used to establish an infinite statement.

For split local \(B\) and \(C\), direct multiplication verifies that
\[
J(B\otimes C)=J(B)\otimes C+B\otimes J(C)
\]
and
\[
J(B\otimes C)^2=J(B)^2\otimes C+J(B)\otimes J(C)+B\otimes J(C)^2.
\]
Taking the quotient therefore gives the direct sum of the two cotangent spaces and proves additivity of \(e\).

For the equality case, if \(e(P)=1\), a lift \(x\) of a cotangent basis generates every nonzero radical layer: multiplication maps \((J/J^2)^{\otimes q}\) onto \(J^q/J^{q+1}\), so the latter has dimension at most one. A nonzero layer cannot equal the next layer because the radical is nilpotent. Hence \(1,x,\ldots,x^{m-1}\) is a basis up to the radical nilpotency index \(m\), proving \(P\cong F[t]/(t^m)\). The converse tensor-irreducibility of this algebra follows immediately from cotangent additivity.

The only external theorem used for the final uniqueness statement is Sakurai's unique irreducible tensor factorization theorem for finite-dimensional local algebras over a splitting field. The proof does not claim results for nonsplit local algebras or nonlocal algebras. Historical full-text coverage remains incomplete for some older uniqueness/cancellation sources; that is a novelty-risk limitation, not a gap in the proof.
