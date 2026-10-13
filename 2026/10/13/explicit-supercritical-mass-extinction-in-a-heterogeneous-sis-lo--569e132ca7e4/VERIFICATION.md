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
# Reproducibility and limits

Run `python verify_cosine_sis.py` from the directory containing that file. It uses only the Python standard library. The observed completion message starts `VERIFY_OK`.

The checker verifies exact polynomial multiplication and the cosine moments \(\int_0^1\cos(\pi x)=0\), \(\int_0^1\cos^2(\pi x)=1/2\). It checks that the negative-potential Rayleigh estimate is \(-1/16\), the perturbed estimate is \(-9/200<-1/25\), and the threshold witness has potential upper bound \(-17/400\). It verifies the strictly positive gap \(7/1280<1/100\) in the nonlinear comparison and the mass gap \(9/4+1/10000<9/4+1/800\).

What is established **mathematically**, rather than by this checker: the Neumann Poincare inequality in the full \(H^1(0,1)\) space, the Rayleigh variational principle, the simplicity and strict positivity of the principal eigenfunction, global well-posedness/positivity, the parabolic comparison principle, and the continuity bootstrap. Those standard inputs and their exact use are given in RESULT.md. No claimed infinite-dimensional proof is based on a numerical mesh, truncated eigenbasis, finite experiment, or solver success alone.

There has been no independent audit or external validation. The exact value of the supremal threshold \(N^*_{S_0,r}\) is not computed; an admissible lower-bound witness suffices. Possible equivalent statements in inaccessible or unindexed sources remain an originality risk.
