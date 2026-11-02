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

# Reproduction and verification

Run `python3 verify_ideals.py` with Python 3.8 or newer; no third-party libraries are needed. The output must match `verification_output.txt` exactly and end with `BIPARTITE_GRAPH_LIE_IDEALS_OK 7_EXHAUSTIVE_CONFIGURATIONS`.

The checker generates **all** reduced-row-echelon subspaces independently of the proposed ideal classification. It evaluates the original bracket, verifies Lie closure against every horizontal basis generator, and counts ideals by subspace dimension. The comparison formula is evaluated separately using Gaussian coefficients and general linear-group cardinalities. A genuine polynomial-basis model of \(\mathbb F_4\) using \(u^2+u+1=0\) checks extension-field arithmetic. Its largest case exhausts all \(417199\) subspaces of \(\mathbb F_2^8\).

The arbitrary-field result is proved by projecting any ideal onto \(A\oplus B\), identifying the mandatory central bracket image \(P\otimes B+A\otimes Q\), recovering the unique lift map, and applying the linear Goursat lemma to the horizontal subspace. This proof does not depend on testing a finite set of parameters. Geometry follows from a locally trivial isomorphism bundle, a relative Grassmannian and a vector bundle.

Unproved limits: the original ideal scheme may be nonreduced and its global components are not classified. Exhaustive tests cover only the seven stated finite-field configurations. Publication priority and any independent mathematical validation are not established.
