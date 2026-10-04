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
# Verification

The source equation for the unilateral lower-threshold impulse is \(\Delta x=p_1x\), \(\Delta y=-\tau_1\) at \(x=h_1\). Thus, if the continuous flow reaches \(B=(h_1,y_B)\), the post-impulse point has predator coordinate \(y_B-\tau_1\), and the successor value relative to \(A\) is \(y_B-\tau_1-y_A\).

Theorem 3.1's proof is checked in the following order:

1. The theorem condition \(y_B-\tau_1\ge y_A\) is consistent with a nonnegative model-consistent successor value at \(A\).
2. In the strict case, the proof says a second point with negative successor value is required.
3. The next displayed calculation concludes \(f(A_1)=y_{B_1}-y_B>0\).
4. Therefore the displayed endpoint values do not straddle zero, so continuity does not justify the asserted fixed point.

`verify_successor.py` checks the reset substitution with exact rational arithmetic and confirms that the model-consistent and printed multiplicative formulas can differ. It also verifies a concrete same-sign pair compatible with the proof's displayed inequalities. Running the script prints `VERIFY_OK`.

Limit: the checker does not decide whether Theorem 3.1 is true by some other argument. The verified claim is only that the published proof, as written, lacks the required successor-function sign change and uses a successor expression inconsistent with the stated reset.
