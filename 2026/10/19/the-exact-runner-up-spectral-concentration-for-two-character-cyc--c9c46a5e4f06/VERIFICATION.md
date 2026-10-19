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

The proof relies on the strict adjacent-swap compression lemma for cosine weights on a regular polygon, a geometric-sum identity, and an exact two-by-two Fourier restriction Gram-matrix calculation. The exceptional zero case at \((N,k)=(4,2)\) is handled separately.

The standalone script `verify.py` uses Python 3 and the standard library only. It enumerates all noninterval subsets for 120 parameter pairs, verifies that the exact runner-up norm is attained **if and only if** the mask is a one-gap arc, and checks the unrestricted interval norm. Run `python3 verify.py` and compare the resulting one-line report with `verification_output.txt`.

The finite enumeration is a sanity check and does not replace the all-order strict-compression proof. No independent audit, external formal verification, noise stability, or result outside the stated hypotheses is claimed.
