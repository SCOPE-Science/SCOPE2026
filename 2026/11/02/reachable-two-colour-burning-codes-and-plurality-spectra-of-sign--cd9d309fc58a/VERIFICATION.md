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

# Reproducibility and scope

Run `python3 verify_signed_star.py` in the directory containing that source. The script is standalone and uses only Python standard-library facilities.

Its first checker simulates each round of the exact signed process, including simultaneous spread, zero-influence ties, an optional ignition after spread, and termination upon fully coloured states. It enumerates all complete colourings for every labelled signing and every \(3\le n\le8\); it then tests the claimed switched code, its cardinality, plurality and full weight distribution. Its second checker directly computes binary Hamming distances to the proposed positive-star code for all normalized words with \(9\le n\le15\), without using the asserted closed distance formula in that distance computation.

Observed output:

```
VERIFY_OK full_signed_dynamics_star_n=3..8 signings=504 terminal_colorings_checked=8160 direct_code_distances_n=9..15 all_signings
```

These checks cover finite ranges only. The general classification, covering-radius formula, and the complete signing census for every size are established by the proof in `RESULT.md`, not by extrapolation. Independent audit: not performed.
