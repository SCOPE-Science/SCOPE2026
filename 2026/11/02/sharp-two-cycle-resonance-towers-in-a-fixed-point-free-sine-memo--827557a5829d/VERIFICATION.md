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

# Verification and limits

Run `python verify.py` with Python 3 and `mpmath` installed. The program uses 75 decimal digits and approximately 300 bisection iterations on each side of even resonances for each of four parameter pairs. For 32 representatives it reconstructs the real-plane two-cycle points, verifies the two exact map returns to high numerical precision, and checks the leading \(n^{-1}\) location formula against an explicit loose \(n^{-2}\) envelope. It prints a PASS line for each parameter pair and a PASS total. The original published FPFM3 values \(\alpha=0.05\), \(\beta=1.82\) are included.

These are nonexhaustive finite calculations, not proof that infinitely many orbits exist or that other orbits do not. The exhaustive statements in RESULT.md are established by algebraic elimination, a sharp gain inequality, the intermediate value theorem, a strictly increasing resonance equation for sufficiently large integers, and uniform Taylor estimates. No calculation or experiment certifies stability, entropy or basin size; none is claimed.
