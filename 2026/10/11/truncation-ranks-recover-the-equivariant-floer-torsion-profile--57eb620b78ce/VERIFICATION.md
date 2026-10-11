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

The proof uses no numerical experiment. Its algebraic checks are as follows.

For \(R=\mathbb F_2[[q]]\) and \(A_N=R/(q^N)\), a cyclic summand \(R/(q^a)\) satisfies
\[
(R/(q^a))\otimes_R A_N\cong R/(q^{\min(a,N)})
\]
and
\[
\operatorname{Tor}_1^R(R/(q^a),A_N)\cong R/(q^{\min(a,N)}).
\]
Thus its total contribution to the truncated homology dimension is exactly \(2\min(a,N)\). A free summand contributes \(N\) and has zero first Tor.

After summing the universal-coefficient short exact sequences over homological degrees, this yields
\[
h_N=rN+2\sum_j\min(N,a_j).
\]
The localization input is \(r=2^{c-1}\). Taking differences gives
\[
h_N-h_{N-1}=r+2\#\{j:a_j\ge N\}
\]
and hence
\[
(h_N-h_{N-1})-(h_{N+1}-h_N)=2\#\{j:a_j=N\}.
\]
These equalities prove reconstruction of the ungraded module and also show the stated parity, concavity, and stabilization constraints.

The verification does not assert recovery of grading positions or any link-specific torsion exponents not computed in the cited literature.
