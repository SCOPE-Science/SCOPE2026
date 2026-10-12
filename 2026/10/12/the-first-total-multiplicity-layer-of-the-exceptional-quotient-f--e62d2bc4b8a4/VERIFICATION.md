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

The proof in `RESULT.md` is complete and does not rely on bounded computation.

The attached checker factors every integer
\[
2\le n<200000
\]
by exact integer arithmetic. It computes
\[
\Omega(n),
\qquad
\sigma(n),
\qquad
\varphi(n),
\]
filters to even integers satisfying
\[
\Omega(n)\le3,
\]
and asserts that the complete observed solution set of
\[
\sigma(n)=4\varphi(n)
\]
is
\[
\{14,418\}.
\]

It separately checks the symbolic boundary reduction for squarefree three-support integers by enumerating the positive factor pairs of
\[
48
\]
and verifying that only
\[
(4,12)
\]
becomes a prime pair after adding \(7\).

The finite replay is corroborative. The universal result follows from the exhaustive factorization-type proof.
