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

## Reproduction

Run `python verify.py` with Python 3.8 or later. Expected final line:

`VERIFY_OK general_m=199 proth_pairs=68 popcount_thresholds=128`

The checker computes residue-graph shortest paths independently of the Mersenne-coin formula, checks the equality of the resulting Apéry sets, enumerates actual isolated gaps, compares with the two-valued prediction, checks Proth binary-weight criteria for \(68\) pairs, and checks threshold equivalences for \(128\) Hamming weights.

## Proof dependencies and limits

Finite verification is supplementary. The universal result uses the exact Apéry calculation, parity-forced adjacent coin length changes, the one-residue characterization of isolated gaps, and a no-carry binary weight calculation. It uses no conjectural mathematical input. The bibliographic search cannot establish absolute novelty; no independent scientific audit has been performed.
