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

The exact proof reduces every \(mab=ax+by\) to \((x,y)=(bj,a(m-j))\) and proves the universal sharp classification by complete elementary case splits. For the finite auxiliary check, run `python3 verify.py` with Python 3 and no third-party packages.

The actual execution returned `VERIFY_OK state_assignments=729 coprime_pairs=13416 diagonal_range=2..16`. In the prime-state check, each prime at most \(13\) is independently assigned to divide only the first generator, only the second, or neither. All 729 mutually exclusive patterns were checked at every multiplier from 2 through 16. This is exhaustive for the finite-index obstruction pattern; it does **not** independently prove the infinite arithmetic theorem without the reduction in the proof. A separate direct-integer gcd comparison checked 13,416 coprime ordered generator pairs within \(2\le a,b\le150\) and the exceptional pair \((55,273)\).

The classification makes no claim about multipliers beyond 16, general non-diagonal numbers, or exact values of the full primitive Frobenius function. No independent mathematical audit has been performed.
