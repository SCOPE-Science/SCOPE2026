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

# Computational reproduction and limits

Run `python3 verify.py` using Python 3 and the standard library only. The program constructs each commuting endomorphism as an explicit matrix and tests commutation, square-zero multiplication, and ordinary rank by finite-field elimination. It does not assume the structural square-zero equation or rank enumerator in its matrix tests; the predicted enumerator is evaluated separately for comparison.

The tested dimensions are \(n=2,3,4,5,6,7,8\) over \(\mathbb F_2\), \(n=2,3,4,5\) over \(\mathbb F_3\), \(n=2,3,4\) over \(\mathbb F_4\), and \(n=2,3\) over \(\mathbb F_5\). The code also enumerates every ambient matrix for \((q,n)=(2,2),(2,3),(3,2)\), independently recovering the complete centralizer size and the square-zero rank distribution. Its final success marker is `VERIFY_OK_SQUARE_ZERO_ALMOST_REGULAR`.

The extension-field arithmetic for \(\mathbb F_4\) uses the polynomial \(z^2+z+1\) over \(\mathbb F_2\). Matrix arithmetic and ranking are direct, separate from the valuation proof. The general all-characteristics and all-dimensions conclusions require the symbolic module calculation in `RESULT.md`; finite samples alone do not prove them. This is a computational reproduction, not an independent mathematical audit.
