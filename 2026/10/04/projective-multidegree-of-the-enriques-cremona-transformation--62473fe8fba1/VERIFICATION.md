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

The verifier is `artifacts/verify_multidegree.py`. It uses only Python's standard library and exact integers.

It checks the quoted source intersection data
\[
H^5=1,\quad H^4E=H^3E^2=0,\quad H^2E^3=10,\quad HE^4=60,\quad E^5=222,
\]
then expands \(D=5H-2E\) to obtain
\[
(b_0,\ldots,b_5)=(1,5,25,45,-15,21).
\]
For a single residual plane it uses
\[
H|_\Pi=l,\qquad D|_\Pi=-l,\qquad N_{\Pi/P^-}\simeq\mathcal O_{\mathbf P^2}(-1)^{\oplus3},
\]
and the codimension-three blowup pushforwards to compute the corrections. Twenty disjoint planes give
\[
(0,0,0,-20,20,-20).
\]
The script asserts that their sum is
\[
(1,5,25,25,5,1)
\]
and prints `MULTIDEGREE_OK` on success.

The verification is exact, finite, and exhaustive for the displayed intersection calculation. It does not independently reconstruct the Enriques surface, the twenty planes, or their normal bundles from defining equations; those geometric inputs are taken from arXiv:2609.10353.
