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

# Reproducibility and verification

Run `python verify.py` in this package's directory with the pinned dependency from `requirements.txt` (`sympy==1.14.0`). No downloaded inputs, external services or additional package files are required. The program builds its own six-vertex weighted Laplacian for several exact positive rational parameters, grounds the candidate leader pairs, and inverts the follower matrices using exact rational arithmetic.

The script also symbolically reconstructs the Fourier-mode resistance and biharmonic formulas, the resistance crossing function, the quartic-controlled coherence crossing, and the exact difference factorizations against the cyclic-distance-one class. It checks monotonicity of the quartic derivative for positive weights and the endpoint signs at \(c=4\) and \(c=5\). The six tested conductances are \(1\), \(3\), \(4\), \(17/4\), \(5\) and \(10\); each includes all three pair-separation classes. The exact integer-witness checks include \(d_2-d_3=1/3696\) and \(C_2-C_3=241/216216\) at \(c=4\).

The strict ordering over every real \(c>0\) is proved in `RESULT.md` by exact algebra, rational denominator signs and a monotone quartic. The finite direct inversions are verification evidence, not an exhaustive proof over the parameter continuum. Independent mathematical audit has not been performed.
