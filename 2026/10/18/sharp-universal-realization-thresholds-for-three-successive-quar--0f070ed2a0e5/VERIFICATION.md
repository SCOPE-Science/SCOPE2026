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

# Verification record

Run `python3 verify.py` using any Python 3 interpreter with its standard library. The program deterministically constructs all primes \(p<6724\), filters to \(p\equiv1\pmod4\), certifies a primitive root for each, and enumerates all three-consecutive quartic coset patterns. A second fourth-power-character implementation validates every label at every finite prime, rather than assuming the discrete-log table. The run completed successfully and printed `VERIFY_OK`, reporting 427 eligible primes, 38 exceptions, and sharp thresholds 733 and 1181. The exceptional list is a complete finite-range census, not a statistical sample.

The uniform infinite-range inequality \(64N_p(e)\ge p-81\sqrt p-48\) was separately proved by character orthogonality and the standard Weil bound for products of up to three distinct linear factors. It guarantees every pattern for \(p\ge6724\). The computation does not establish this analytic inequality or infinite claims by sampling.

The definition depends on a choice of primitive root only up to automorphism of \(\mathbb Z/4\mathbb Z\). Consequently all-pattern realization and the zero/nonzero distinction are intrinsic. This verification does not provide individual word frequencies beyond enumerated primes, nor independent audit or exhaustive global priority checking.
