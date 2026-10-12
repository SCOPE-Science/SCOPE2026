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
The theorem is proved symbolically in `RESULT.md`. The executable check is deliberately narrower: it verifies exact algebraic identities and exponent boundary conditions so that implementation output is not mistaken for an infinite proof.

The critical exact identity checked is
\[
(xz+n)(yw+n)-(xw+n)(yz+n)=n(y-x)(w-z).
\]
The boundary exponent comparisons checked are the three-tail cases \(k=4,5\) and the two-tail threshold beginning at \(k=6\). The program also verifies \(k^2-6k+4\ge0\) over a broad finite diagnostic range after the symbolic reduction; the proof that it persists for all larger integers is the monotonicity argument in `RESULT.md`.

The computation does not search for extremal sets, does not establish existence at the bounds, and does not certify novelty.
