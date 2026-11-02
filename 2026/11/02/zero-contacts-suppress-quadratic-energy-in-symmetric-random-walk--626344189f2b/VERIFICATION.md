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
# Reproducible checks

Execute `python3 verify_bridge_energy.py` in the same directory as this document. Python 3 standard library is sufficient.

The program independently enumerates all \(66{,}194\) balanced step sequences of semilength \(2\) through \(9\). For each it directly computes all path squares and interior zero times; it compares raw empirical rational moments with the five displayed formulas, and conditional energy with one or two prescribed zero times. It separately verifies the central-binomial coefficient convolution through semilength \(100\), and the weighted-pair sums used in the fourth-moment calculation through total length \(60\).

Actual execution output:

```
PASS exact enumeration of 66194 bridges for n=2..9;
PASS 346 exact arithmetic assertions including prescribed-contact energies,
convolution identities through n=100, and fourth-moment coefficient sums.
```

This run requires no random seed or external data. Exact enumeration at bounded sizes cannot establish an all-size theorem; the full proof appears in `RESULT.md`. The fourth-moment identity is additionally justified there from balanced-sign exchangeability rather than solely from the verifier. Independent audit has not been performed.
