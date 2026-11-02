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

# Verification of the matching-chain reversibility theorem

Run `python verify_matching_chain.py` with Python 3.10 or newer; no third-party dependencies are required.

The program independently enumerates all partial matchings for \(N=4,5,6\) (respectively 10, 26, 76 matchings) and builds the exact stochastic transition kernel by applying each possible single-site or Bell-pair measurement. It confirms all row sums equal one; checks pairwise detailed balance against the proposed product measure for positive vertex-additive reciprocal weights and also when an individual vertex potential is negative; and detects nonzero detailed-balance residuals for distance exponents one and two. The five-state Kolmogorov ratio is verified exactly as \(1/2\) and \(1/4\), respectively, at each tested size. All performed checks passed.

The proof in `RESULT.md` establishes the infinite parameter family and all finite sizes. Finite enumeration alone would not establish those general conclusions. In particular, the assertion about the full quantum trajectory or any thermodynamic-limit rate is not made. The primary 2026 model and its supplement were compared, as were general monomer–dimer weights and the classical cycle criterion; a more general published result might subsume the classification.
