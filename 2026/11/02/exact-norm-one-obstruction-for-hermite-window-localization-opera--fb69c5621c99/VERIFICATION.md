---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The displayed Weyl action multiplies with phase exp(−iσ(z,w)/2), so conjugation of W_xi and of the character Toeplitz operator has the same eigencharacter. Irreducibility gives scalar proportionality. With the radial unit vector L_{k−1}(|w|²) and real a=|xi|, pairing with its shift leaves the tilt exp(a w) after multiplying the character. In the two-variable Laguerre generating integral the Gaussian quadratic coefficient is (1−st)/[(1−s)(1−t)], the linear coefficients are a/(1−t) and at/(1−t), and the constant is −a²t/(1−t). Gaussian integration gives (1−st)^−1 exp(−a²st/(1−st)), establishing every diagonal coefficient and the stated zero without a Fourier convention ambiguity. The phase-weighted Weyl matrix average has norm at most 1 and equals 1 on W_xi. Covariance and the translated disk substitution leave a bounded scalar times the zero character operator, plus an error tending to zero by dominated convergence: the disk symmetric-difference fraction tends to zero pointwise and is bounded by 2, and the test-vector product is integrable. This works for each fixed bounded symbol with no uniform symbol bound needed. Thus the lower bound is 1 for the full range, and the zero symbol attains it. Distance is unchanged under norm closure; norm continuity of Weyl conjugation on this shift follows from the eigencharacter. For BUC symbols the Toeplitz range lies in C_1 by covariance and the symbol sup-norm bound, so the proper-subset conclusion is valid. The Hermite STFT/Bargmann unitary in Abreu–Speckbacher Eq. (6.2) identifies the mask and Toeplitz sesquilinear forms by coordinate reflection/rescaling; the phase cancels. Time-frequency shifts correspond to Weyl shifts up to unimodular factors, which do not affect distance to the complex linear range. The argument requires the irreducible true level and a Laguerre root, not the full reducible sum or arbitrary frequencies.

## originality

PASS

The supported new content is the exact distance to the full L-infinity linear range and its norm closure, not the Laguerre-zero kernel or the lack of exact representation. Fulsche–Hagger explicitly leave uniform-closure membership open. The distinction is about norm density, not weak-* density or C*-generation. The printed first clause of Question 2 lacks a closure bar; the preceding sentence expressly poses the uniform-closure issue meant here. No equivalent norm-gap statement was found in the inspected sources, not a guarantee of priority.

## value

PASS

The sharp norm obstruction answers the stated norm-closure problem for every higher true level and for the full bounded-mask range. It pinpoints a genuine distinction between weak-* and norm density and uses an explicit contractive separation at each forbidden frequency. It is stronger than identifying a null symbol or an operator with no exact representation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
