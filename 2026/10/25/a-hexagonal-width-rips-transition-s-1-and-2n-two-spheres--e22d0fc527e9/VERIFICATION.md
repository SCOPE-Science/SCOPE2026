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

# Reproducibility and scope

The complete translation-orbit certificate is `artifacts/certificate.json`. Run `python3 -S artifacts/verify.py` in an environment with Python 3. The verifier uses only standard-library modules. With no arguments it checks every integer period \(7\le n\le20\); passing explicit integers checks those periods instead.

The checker independently constructs every simplex from the inclusive graph-distance rule. It verifies exact face vectors; replays all \(53n\) free-face collapse pairs; checks every selected edge/triangle pair and strict orbit-order acyclicity; and checks the five transverse tree edge orbits and one longitudinal cycle edge orbit that permit a complete lower-dimensional acyclic matching. It reports \(2n\) critical triangles, one critical edge and one critical vertex.

The actual successful output for periods \(7\) through \(20\) is included in `artifacts/verification_output.txt`, ending with `VERIFY_OK_C6_CN_RIPS2_WEDGE`. These are finite repeatability tests. The uniform mathematical proof is the three-consecutive-column locality and orbit-incidence argument in RESULT.md, together with the projection to a longitudinal \(S^1\), which rules out nonzero integral two-cell attaching degrees.

Scientific limitations: the result applies to \(C_6\square C_n\) with \(n\ge7\) at graph-metric radius two only. The checks do not constitute an external independent scientific audit.
