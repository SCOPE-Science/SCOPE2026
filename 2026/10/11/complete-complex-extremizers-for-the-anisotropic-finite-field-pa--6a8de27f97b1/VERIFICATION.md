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

The extension is normalized by \(q^{-2}\), the target carries counting measure and the source carries normalized counting measure. The published sharp constant is \(1+q^{-1}-q^{-2}\) at fourth-power level. This normalization was checked against [1, Theorem 1.1] and with direct sums.

The phase classification follows from the explicit orthogonal parallelogram identity, including zero and collinear increments. Every nonzero maximizer is nowhere zero by the published constant-modulus equality condition. For independent increments, mixed difference depends separately on two independent field coordinates and hence must be constant. Collinear increments are reduced to independent increments by decomposing one of them into two noncollinear components. The resulting symmetric bicharacter is forced to be a single trace character of the dot product and integrates to the claimed quadratic chirp plus a linear character. The proof handles all odd prime powers with \(q\equiv3\pmod4\).

Execute `python verify.py` in the same directory. The script performs exact prime-field linear algebra of noncritical pair-sum constraint rows for \(p=3,7,11\), yielding respective ranks \(5,45,117\), and tests several chirps. Direct fourth-moment evaluations of the normalized extension agree with the constant-input optimal moment for each of those primes to numerical tolerance \(3\times10^{-9}\). These computations are finite corroborations and do not independently establish the result for arbitrary prime powers.

The initial sharp inequality and constant-modulus necessary condition are credited to González-Riquelme–Oliveira e Silva, arXiv:2405.16647. The phase classification for the anisotropic congruence class and the projective count are proved in `RESULT.md`. Originality remains subject to possible unindexed equivalent sources. Independent mathematical review has not been performed.
