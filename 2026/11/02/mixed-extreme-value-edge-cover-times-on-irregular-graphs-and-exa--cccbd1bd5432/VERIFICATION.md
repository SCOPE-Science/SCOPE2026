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

# Reproduction and limits

The accompanying `checker.py` is standalone source code requiring Python 3 and SymPy; invoke `python3 checker.py` after installing SymPy. Its deterministic exact-rational checks exhaust every binary edge-status subset for the listed small balanced spiders, independently compute discrete edge-draw state counts for the first eight draw times, and verify the no-consecutive-absent recurrence using direct binary word enumeration. It additionally checks illustrative convergence on larger spiders numerically. At packaging, the program passed 105 assertions.

The finite checks validate the stated special-case algebra and help catch indexing and normalization mistakes; they do not prove results for arbitrary graph orders or asymptotic regimes. The analytic proof uses joint factorial moments, negligible high-degree coverage tails, exponential-clock coupling, and an explicitly evaluated arm recurrence. The displayed asymptotic statements are mathematical arguments, not machine-certified theorems.

The primary preprint motivating the contextual comparison was first public on 2018-03-26, arXiv:1803.09601. Historical work includes Tauraso (2008) and Falgas-Ravry et al. (2016). General finite edge-cover transforms are known. Independent validation has not been performed.
