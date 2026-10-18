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

# Verification and reproducibility

Run `python3 verify.py` with the packages described in `requirements.txt`. The executed checker returned `VERIFY_OK rank_cases=45 radial_cases=116 physical_cases=2`.

The first check reconstructs every Fourier restriction matrix between the Hamming shell of weight two and every Fourier level, for dimensions four through nine, and computes exact ranks over the prime field of size 1000003. The analytic proof works over characteristic zero; prime-field agreement is an independent finite check, not a proof of the infinite rank theorem. The second check tests exact integer Krawtchouk recurrences and zeros for all levels in square dimensions four, nine, sixteen and twenty-five. The third propagates the finite Lindblad semigroup for dimensions four and five, using ordinary unit dephasing rates, and compares the corner return with the claimed large-time formula at explicitly chosen finite times and tolerances.

The proof covers all dimensions at least four and all positive monitored-site rates; numerical tests cover a finite range only. These checks do not independently validate originality, prove uniform convergence rates, or establish publication-level priority. A separate independent scientific audit has not been performed.
