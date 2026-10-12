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
The self-contained `checker.py` requires Python 3 and the standard library only. Run `python3 checker.py` from the folder containing the file. It prints `VERIFY_OK` on success and aborts on any failed assertion.

The program directly enumerates all images of two generators in the four-dimensional algebra, including scalar components, for skew parameters \(c=2,3\) over \(\mathbb F_4\) and \(\mathbb F_5\). It constructs the multiplication table, tests the Leibniz identity on each basis pair, tests \(D^2=D\), computes linear rank, and checks a concrete shear normalization. Observed rank histograms are \(\{0:1,2:24\}\) over \(\mathbb F_4\) and \(\{0:1,2:10\}\) over \(\mathbb F_5\), independent of the two tested values of \(c\). For \(2\le n\le6\) and \(q\in\{4,5,7\}\), a distinct enumeration of all diagonal supports and permitted free quadratic coefficients reproduces the theorem's closed polynomial.

These finite enumerations cannot establish an arbitrary-field or unbounded-generator theorem by themselves. The theoretical derivation, invertible shear normalization, and orbit comparisons in RESULT.md provide those implications. No external or independent assessment is asserted.
