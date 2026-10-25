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

# Reproducible exact checks

Run `python check_loewner.py` with Python 3 and SymPy. This reconstructs the divided-difference polynomial and its squared kernel using rational arithmetic; divides the three-node determinants by the squared Vandermonde; and checks (i) positivity of the two-node principal minors uniformly for all nodes below \(1/100\), (ii) the negative sign of all 44 coefficient terms of the original three-node determinant quotient, (iii) the positive constant and 680 negative nonconstant coefficient terms of the squared-kernel quotient, and (iv) an exact strict lower bound greater than \(3/100\) on a cube containing all ordered triple configurations. It also evaluates a distinct-node rational witness.

A result from this script is an exact polynomial identity plus a finite rational coefficient certificate, **not** an empirical substitution for a universal statement. The proof in `RESULT.md` supplies the order-congruence argument extending the interval result to the entire positive half-line and the finite-order Loewner implication.

The work does not check positivity for fourth and higher Loewner-matrix orders and does not prove any full radial-convexity statement. No independent audit has been conducted.
