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

# Verification record

The exact theorem and analytic proof are given in `RESULT.md`. The residue-class identity is obtained by substituting \(n=pk+a\), with \(\xi_j=z_j^{rp}\), into the canonical Carleson frame coefficients. A family of normalized Szegő kernels indexed by the **distinct** powered points is Riesz because those points form a Carleson interpolating sequence. The same finite-fiber reduction gives the exact minimal repair period: its maximum fiber cardinality cannot exceed the period. The remaining frame question is precisely finite-fiber injectivity.

`CHECKER.py` is standalone Python using only the standard library. Run `python CHECKER.py`. It checks an exact power collision, the fiber decomposition, and quantitative first- and second-order singular-value vanishing on representative finite collision groups. The analytic proof handles every admissible infinite spectrum, every prescribed spacing and every sufficiently small positive jitter; numerical tests do not replace these quantifiers.

Scientific restrictions: the period depends on the spectrum and spacing, the Stolz assumption matters, and no explicit leading constant for the optimal lower frame bound is claimed. Independent mathematical audit and publication-priority certification have not been performed.
