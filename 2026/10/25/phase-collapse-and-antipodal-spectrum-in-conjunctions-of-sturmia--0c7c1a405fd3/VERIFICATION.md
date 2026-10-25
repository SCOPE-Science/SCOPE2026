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

# Verification evidence and limits

The proof in `RESULT.md` establishes the unrestricted invariant-measure and Koopman-spectrum statements. Its critical steps are: (i) almost-everywhere equivalence of Sturmian codings with circle rotations, (ii) ergodic decomposition on fixed phase-difference cosets, (iii) direct circular-interval intersection calculations, (iv) absolute convergence of the correlation Fourier expansion, (v) trivial/half-turn classification of the translation stabilizer, and (vi) affine extension by ergodic decomposition.

To repeat finite computational checks, run `python3 verify.py`. The script has no external dependencies, uses a deterministic pseudorandom seed, tests overlap lengths and Fourier magnitudes with exact fractions for 2,980 rational configurations, verifies four exact half-turn identities, and tests 14 finite irrational-orbit frequencies. A passing numerical run neither establishes an arbitrary irrational statement nor proves uniqueness of ergodic measures; those statements rely on the mathematical proof. No external independent audit has been performed.
