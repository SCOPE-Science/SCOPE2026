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

Keep `verify.py`, `rule_catalog.csv`, and `class_recurrences.csv` together; run `python verify.py`. No optional libraries or external data are required.

The verifier constructs all 256 four-pair labeled predecessor graphs from the neighborhood bits of their Wolfram rule numbers. It closes the Boolean relations under both output labels, marks exactly those relations with directed cycles, and counts the labeled output words of each length by integer state propagation. For each rule with \(N\) reachable relations and recurrence order \(d\), it verifies the claimed recurrence for \(N\) consecutive indices after the degree threshold. Cayley–Hamilton extends this exact certificate to every subsequent period. It independently checks all output words of lengths one through eight in eight-phase graphs, and checks that exactly 31 class fingerprints occur and that the period-eight witness is sharp.

Successful test output:

```
VERIFY_OK: 256 exact complete-state recurrence certificates;
31 pairwise distinct all-period spectra separated by periods <=8;
sharp period-8 witness: Rule 7 versus Rule 25 (P8=148 versus 156);
max relation states=2375; max recurrence degree=56;
2048 independent expanded-phase periodic-word checks (periods 1..8)
```

## Limits

The code certifies a finite-dimensional mathematical recurrence rather than inferring an infinite result from experiments. A failure of this script would not imply the claimed classification is impossible; the certificate would need investigation. The computation does not address temporal orbits, conjugacy, or historical-priority uniqueness. Independent mathematical verification has not been performed.
