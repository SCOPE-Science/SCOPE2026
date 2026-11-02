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

# Reproducible finite checks

Run `python3 verify.py` with standard Python 3. The script exhausts all divisor-poset upper-set tests for \(3,751\) two-shift parameter triples \((n,a,b)\), with \(1\leq n\leq31\) and \(-5\leq a,b\leq5\). It matches the complete arithmetic criterion, including positive-covariance forbidden cases.

It also checks \(1,250\) three-shift triples with \(1\leq n\leq10\). In cases satisfying the criterion it tests \(62,484\) exact inequalities for all upper-set indicators on all pairs of disjoint nonempty coordinate groups; in cases failing the criterion it identifies at least one forbidden coordinate pair. A final direct sum computes \(\mathbb E[\gcd(U-1,n)\gcd(U+1,n)]\) for every \(1\leq n<200\), comparing the explicit local-factor formula.

The test command returned: `VERIFY_OK: 3751 two-shift parameter triples; 1250 three-shift triples; 62484 full-NA event inequalities; 199 opposite-shift exact moments`.

The finite computation is not an infinite certificate. The general classification is established in the analytic proof using CRT independence, local disjoint departures and necessity witnesses. The opposite-shift expectation is a known/elementary corollary and not an asserted novel result.
