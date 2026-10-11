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

# Verification of the Desargues independence-complex calculation

The complete graph definition, matching, and signed incidence computations are in `verification/verify_integral_morse.py`; a separately implemented independent-set enumerator, edge-deletion polynomial recurrence, explicit \(H(5,2)\) model and complete mod-two boundary reductions are in `verification/verify_independent_homology.py`.

From the directory containing `RESULT.md`, run:

```
python3 verification/verify_integral_morse.py
python3 verification/verify_independent_homology.py
```

Both programs require only Python 3's standard library. They terminate with assertion errors if any expected exact count or rank differs. The first expects `DESARGUES_INTEGRAL_MORSE_OK`, 6212 augmented faces, 3103 matched pairs, six critical augmented faces, a complete 30380-arc acyclicity check and five zero **integer** boundary coefficients. The second expects `DESARGUES_H52_HOMOLOGY_OK`, the independent face counts \((1,20,160,660,1510,1924,1320,480,115,20,2)\), the mod-two boundary ranks \((1,19,141,519,991,932,383,97,18,2)\), and reduced Betti numbers one in degree four and five in degree five. The independent polynomial gives Euler characteristic \(-3\), matching \(1+1-5\).

The integral conclusion uses the acyclic Morse theorem and the classification \(\pi_4(S^4)\cong\mathbb Z\) by degree. Binary ranks and Euler characteristic independently check the finite face combinatorics but cannot establish vanishing integer attaching maps on their own. The proof does not extrapolate from a finite sample to an infinite family. An external independent audit has not been performed.
