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

The proof has an analytic infinite part and a finite exact part. The analytic reductions force any hypothetical configuration with maximal center-to-vertex radius at most \(\sqrt5\) to have area \(11/2\) or \(6\), and force every squared side length into the finite set
\[
\{1,2,4,5,8,9,10,13,16,17,18,20\}.
\]
The checker exhausts unordered triples from this complete set using the squared-length form of Heron's identity. It returns exactly five triples and confirms that each contains a squared side length at least \(16\). The final contradiction is analytic because strict disk containment gives side-line distance greater than \(1\).

The same checker also verifies rational inequalities for a member of the explicit sharpness family. The limiting step \(\delta\to0^+\) is elementary and is not inferred from sampling.

Reproduction command:

`python3 artifacts/verify.py`

Expected terminal line: `VERIFY_OK`.
