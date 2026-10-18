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

# Finite verification

Run `python3 CHECKER.py` using Python 3 with its standard library. The program constructs the complete 32-edge de Bruijn digraph and independently enumerates de Bruijn cycles through (i) all 65,536 local incoming-to-outgoing bijections and (ii) recursive edge-avoiding tours. Each enumeration yields 2,048 distinct normalized cyclic words; the two sets coincide exactly.

For every cycle it directly evaluates signed periodic autocorrelations over all 31 nonzero shifts and independently tabulates their squared-sum energy. Exact integer tests compare the entire 47-value distribution, all extremal and symmetry-orbit counts, and the two energy moments. The checker also tests low-lag zero correlations. For external normalization cross-checks, it reproduces the published peak-cutoff cardinalities 12 and 784 and the rounded average normalized RMS sidelobe values 0.146, 0.123, 0.078 (Spinsante et al., 2011, Table 3).

The result for order five follows from exhaustive coverage proved in the mathematical argument, not from a numerical sample. Two algorithms in the same package are cross-checks and do not constitute an independently commissioned audit. No inference for larger de Bruijn orders is made.
