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
# Reproducibility and limitations

The pure-Python file `verify.py` is standalone and requires no third-party packages. From the folder containing it, run `python3 verify.py`; the final output is `VERIFY_OK`. The program uses exact polynomial quotient fields \(\mathbb F_3\), \(\mathbb F_3[u]/(u^2+1)\), and \(\mathbb F_3[t]/(t^3-t-1)\), and does not use floating-point numerical approximations.

It verifies that \(t\) has multiplicative order \(13\), that \(t^2\) supplies a normal basis, and that the coefficientwise trace expands to the nine-term quartic printed in the proof. A separate symbolic polynomial implementation substitutes the displayed invertible matrix and checks every coefficient of the identity with the Klein quartic modulo three. Independent exhaustive projective evaluations of both forms over the three finite fields give counts \((4,10,28)\). It then checks that the thirteen characteristic-three parameter curves have distinct four-point subsets, each rational plane point lies on four of them, and each pair of blocks or points has precisely one common incident counterpart. Newton identities and the genus-three functional equation give the \(1+27T^6\) numerator. The program prints an additional `VERIFY_DESIGN_OK` marker for the incidence checks.

These are finite exact computations, not a substitute for the general-field proof. General smoothness and parameter independence follow from the displayed Moore/diagonal argument, general Singer orbit counts from the cyclic group quotient, and the projective design from the nondegenerate trace pairing and the bijective power map. No assertion is made about all projective linear systems, the full automorphism-group orbit partition in the noncoprime case, or the zeta functions of the general \(q\)-family. The literature novelty comparison is incomplete against potentially unindexed specialized sources. No independent audit or independent validation has been performed.
