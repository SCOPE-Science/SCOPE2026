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

The standalone `verify.py` depends only on Python's standard library. Run `python verify.py` after extracting the package entry. The program enumerates *literal* factors and their overlapping occurrence counts for every quadruple \(1\le a,b,c,d\le7\) and compares the entire set of minimal unique factors against the structural classification. It also enumerates all four-run words of lengths four through twenty-two, compares all coefficient counts for one through five factors against a separately implemented finite-pair expansion of the proposed rational generating function, and checks the five-factor extremal formula.

Observed result: `VERIFY_OK complete_quadruples=2401 literal_mus=9457 length_coefficients=95 max_length=22 maximum=5 first_attainment=8`.

These computations are finite consistency tests, not a substitute for the general proof. They do not establish originality or independent external validation. The all-length theorem and its phase boundaries are justified by the factor-by-factor proof in `RESULT.md`.
