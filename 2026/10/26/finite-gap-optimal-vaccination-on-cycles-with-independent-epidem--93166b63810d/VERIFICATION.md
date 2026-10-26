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

# Reproduction and scope

Run `python3 verify.py` in the same directory; it needs only standard-library exact `fractions.Fraction` and `itertools.combinations` and does not require external data.

The checker independently enumerates undirected open-bond configurations on the surviving cycle after each possible two-vertex immunization, computes each open connected component and its probability of containing an initial infection seed, weights configurations exactly using rational bond probabilities, and compares its expected final infected count with the closed-form path objective. It checked 385 cycle/vaccinee/parameter instances up to 11 cycle vertices (including some n=3 boundary tests not required by the theorem). It separately tested the path curvature and difference identities through positive path length 74 at three rational parameter settings; the whole finite p=q=1/2 optimum for n=4 through 71; and the eventual optimum in four parameter settings for n=302 and n=352. All checks passed.

These are finite experiments. The proof that the formula holds for every cycle size, that vaccination gaps are nonzero in any optimum, and that the optimal shorter gap is eventually fixed is the algebraic and coupling proof in RESULT.md. Neither the code nor these checks constitute independent audit or complete novelty certification.
