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

# Reproducibility and limits

Run `python3 verify.py` with Python 3's standard library only. The script independently builds counts via composition sums and first-return recurrences, then checks them against direct enumeration of all labeled words. Both *short-border return multiplicities* and the full number of distinct proper Abelian-border lengths are verified.

The checker enumerates all words for \(q=2\) through paired length \(m=6\), \(q=3\) through \(m=5\), and \(q=4\) through \(m=4\). It additionally verifies odd lengths through \(m=3\), the exact binary formula already known from earlier literature, the first five ternary return-multiplicity rows, and the approach of the ternary local-return factor to \(3\sqrt3/(4\pi)\) at three finite indices. A successful execution prints `VERIFY_OK`.

These are finite corroborations. Correctness for arbitrary length and the asymptotic distributional limits rests on the analytic argument in `RESULT.md`, including the unique first-return decomposition, multinomial local limit, and factorial-moment calculations. No independent scientific audit has been performed.
