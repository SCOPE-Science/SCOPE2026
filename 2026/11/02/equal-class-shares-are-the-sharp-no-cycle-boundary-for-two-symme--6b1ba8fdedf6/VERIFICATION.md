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

# Scientific verification

The proof in `RESULT.md` covers all finite alternative sets of size at least three and all continuous strictly increasing symmetric links with the stated endpoint limits. The crucial identity is odd-monotonicity of \(F-1/2\); the existence argument uses the inverse link at a cutoff strictly above \(1/2\) and a finite, sufficiently large first-class score spread. Boundary equality, ties, extreme shares and the strict-cycle construction are addressed separately.

To reproduce the exact arithmetic checks, run `python3 checker.py` in the directory containing that script. It requires only the Python standard library and outputs `PASS: 25215 exact rational assertions; analytic universal proof is in RESULT.md`. These checks separately verify a rational three-alternative strict cycle, the explicit construction at both orientations of 127 imbalanced rational weight values, and the full \(4^6\) configurations of worth configurations for the 50:50 product ranking including tied products. These finite calculations test, but do not prove, the continuum theorem.

The numerical consequence does not assert identifiability from samples or that every score assignment cycles at imbalanced weights. Historical novelty remains provisional against unlocated equivalent results. No external independent scientific audit has been performed.
