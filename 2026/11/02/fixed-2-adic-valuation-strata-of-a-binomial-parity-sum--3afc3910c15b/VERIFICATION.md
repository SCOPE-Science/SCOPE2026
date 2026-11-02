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

Run `python3 verify.py` with Python 3.9 or newer. The script is self-contained and uses only the standard library; success prints `VERIFY_OK binomial=2000 binary_words=262143 depths=0..17`.

The executable checks: the defining fourth-order integer recurrence and its initial values; repeated companion states modulo two at distance five and modulo four at distance ten; the resulting modular patterns; positivity of the first 256 recurrence values; direct Lucas-parity evaluation of the binomial sum for indices zero through 1999 versus a separately evaluated run-length product; the rational generating functions for valuation zero and one by exact integer polynomial recurrences; and complete valuation histograms for every binary word of each length zero through 17. The latter checks visit 262,143 binary words across all lengths and verify each histogram totals the correct power of two.

These are finite checks, not a proof of periodicity or of the asymptotic law. Invertibility of the recurrence shift plus the explicit returning states supplies infinite periodicity; formal decomposition of arbitrary binary words supplies the generating functions; and the dominant-pole argument supplies the infinite asymptotics. The binomial-sum/run-length equality for all indices is the cited published Theorem 13 of Rampersad and Wiebe (2023). The proof does not assume that numeric checks certify that earlier result.

The overlap comparison identifies the known OEIS A124312 zero-valuation baseline and the non-covering OEIS A118898 table. No independent scientific audit or external proof certification is represented by this report.
