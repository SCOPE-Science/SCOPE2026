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

# Reproduction and scope

Use Python 3 with no third-party dependencies. Run `python3 check_spectrum.py` in this directory. The checker constructs the finite rings explicitly, exhausts every \(2\times2\) matrix in each chosen ring, evaluates all four entries of its square, and enumerates the additive image set directly for every square-zero matrix. The observed image-cardinality logarithm is compared with the theorem's complete finite sum for each rank, not merely with the total and maximal-rank formulas.

The checker covers twelve complete test configurations: \(\mathbb F_2[t]/(t^n)\) for \(1\le n\le4\), \(\mathbb F_3[t]/(t^n)\) for \(1\le n\le2\), \(\mathbb F_4[t]/(t^n)\) for \(1\le n\le2\), and the mixed-characteristic rings \(\mathbb Z/2^n\mathbb Z\) for \(2\le n\le4\) and \(\mathbb Z/9\mathbb Z\). The length-one cases are harmless checks of the formula beyond its stated \(n\ge2\) scope.

Recorded success marker: `SQUAREZERO_TWO_BLOCK_CHAIN_CENSUS_OK 12`. The theorem is an infinite-family statement established by the proof; finite experiments cannot establish its general quantifiers. Independent review of the mathematical proof and historical priority has not occurred.
