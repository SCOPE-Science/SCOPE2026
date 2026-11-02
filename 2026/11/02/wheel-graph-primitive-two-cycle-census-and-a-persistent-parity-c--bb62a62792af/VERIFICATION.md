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

The first program `wheel_period_two_verify.py` uses the graph's actual neighbor lists and explicitly evaluates the chip-firing update twice. Every state satisfying \(0\le c(v)<2d(v)\) was tested for rim sizes \(3,4,5,6\). This box contains all possible primitive two-cycles by the height-interval proof. Exact orbit totals were \(60,276,1125,4476\), respectively. Across \(n=3,\ldots,15\), an independently implemented sum over every binary cut and a separate cyclic rim-word sum agreed with the proposed recurrence. The program printed `WHEEL_TWO_CYCLE_EXACT_VERIFY_OK`.

The second program `wheel_transfer_symbolic.py` uses SymPy to verify the displayed four-by-four characteristic polynomial, determinant and rational logarithmic-derivative generating function. It independently checked the weighted orbit polynomial for rim sizes \(3\) through \(9\), printing `WHEEL_TRANSFER_SYMBOLIC_VERIFY_OK`. For instance \(B_3(z)=9z+48z^2+3z^3\) and \(B_4(z)=176z^2+96z^3+4z^4\).

To reproduce from this package, execute `python wheel_period_two_verify.py` with standard-library Python 3, and `python wheel_transfer_symbolic.py` with Python 3 and SymPy installed. The recorded outputs are included. Finite experiments do not certify claims for untested sizes. The general proof is self-contained in `RESULT.md`. No independent external audit or validation is claimed.
