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

# Reproducibility and evidence

Run `python verify.py` with the dependency listed in `requirements.txt`. The script uses characteristic-three Gröbner bases for all ten pairwise intersections, saturating away from the smoothness boundary \(\Delta=uv(u-1)(v-1)(u-v)\), and checks the five Legendre supersingularity equations. It then enumerates every allowed ordered parameter over the explicitly constructed finite fields \(\mathbb F_3\), \(\mathbb F_9\), and \(\mathbb F_{27}\), evaluating the five elliptic Hasse conditions independently of the saturated divisor formulas.

Actual output is included in `verification_output.txt` and ends in `VERIFY_OK`. The observed rank-four/rank-five counts are \((0,0)\) for \(q=3\), \((30,12)\) for \(q=9\), and \((120,480)\) for \(q=27\).

**Limits.** These are exact finite algebraic and enumerative checks, but finite-field enumeration alone is not evidence for arbitrary extensions. The all-extension counts follow from the proven disjointness and the explicit \(\mathbb A^1\setminus\{0,1,-1\}\) parametrizations. The \(3\)-rank, \(a\)-number and Newton conclusions depend on the algebraic tame-group character decomposition, not on numerical observation. The supplied code does not attempt independent literature certification.
