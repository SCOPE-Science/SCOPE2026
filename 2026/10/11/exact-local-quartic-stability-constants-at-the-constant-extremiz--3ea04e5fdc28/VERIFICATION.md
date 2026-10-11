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

The proof was replayed from the cited source identities rather than from cached numerical output. The following checks were performed:

1. The focal source date is October 4, 2026, and its primary MSC is 46E35.
2. The admissible classes, normalized nearest-neighbor and circle heat energies, word-length energy, deficits, and distance agree with the source definitions.
3. The exact identities \(d^2=2(1-a)\), \(s=1-a^2\), the high-frequency excess form, and the cubic-deficit decomposition were checked in the focal full text.
4. For \(n\ge5\) and the circle, a normalized first harmonic satisfies \(\|e^2-1\|_2^2=1/2\), and \(e^2-1\) lies in the second harmonic. Its excess eigenvalue is \(q_n\) for nearest-neighbor or heat energy and \(1\) for word-length energy.
5. The localization estimate was checked algebraically: if the normalized deficit remains bounded as \(d\to0\), the cubic interaction terms imply \(Q(z)=O(d^4)\); this is the step that rules out hidden high-frequency competitors in the local limit.
6. Completing the positive quadratic form gives the cubic fourth-order coefficient \(1/4-1/(8p)\), and the scalar remainder contributes \(1/4\), yielding \(3/4-1/(4p)\).
7. The explicit source family has second-harmonic amplitude \(\varepsilon^2/(2\sqrt2 p)\) and realizes the same limit, proving sharpness of the local lower bound.
8. Direct finite-cycle evaluations for several small and moderate cycle lengths approached the stated constants; these evaluations were sanity checks only.

Limits: this verification establishes only the local constants stated in the finding. It does not establish the unknown global constants, and it does not perform an independent audit.
