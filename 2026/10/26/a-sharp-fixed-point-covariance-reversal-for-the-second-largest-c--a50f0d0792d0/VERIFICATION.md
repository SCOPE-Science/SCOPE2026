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

# Reproducibility and verification
Run `python3 verify.py` in a directory containing the enclosed standalone script. Python's standard library suffices. Cycle-index partition enumeration and cycle-length threshold recursion compute separately every rational second-cycle expectation through order \(14\). Direct enumeration covers all \(46{,}232\) individual permutations from sizes \(2\) to \(8\), comparing the mixed fixed-point/second-cycle moment with the marked-cycle formula. The script also checks the insertion identity through order \(15\), and checks the strict harmonic lower bound and its parity monotonicity through size \(300\).

The finite assertions are consistency checks, not proofs beyond their tested ranges. The exact sign for all sizes follows instead from the partition-family harmonic inequality and the listed rational boundary cases in RESULT.md. The limiting result invokes the cited classical ranked-cycle distribution and long-cycle tie bound. No independent audit or external validation is claimed.
