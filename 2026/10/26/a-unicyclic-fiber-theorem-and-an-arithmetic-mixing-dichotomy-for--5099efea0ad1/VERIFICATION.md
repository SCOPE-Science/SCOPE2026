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
# Verification and limits

The mathematical proof uses the original four-branch Feres transition law for \(\alpha=m\pi/n\), \(\gcd(m,n)=1\), \(n>6m\), and nongrid fiber offsets \(t\in(0,\pi/n)\). The critical steps are: (i) identify all positive shift and reflection edges, (ii) prove residue-class connectivity, (iii) remove the \(2m\) pendant vertices to expose the unique cycle, (iv) apply detailed balance with sine weights, and (v) apply the finite irreducible Markov convergence theorem. No numerical assertion replaces an infinite quantifier.

Run `python3 verify.py` with Python 3 (standard library only). The program explicitly reconstructs the graph by integer formulas and independently obtains its positive edges from the original probability law. It covers every coprime pair \((m,n)\) with \(7\le n\le100\), \(n>6m\), and offsets \(t/(\pi/n)\in\{0.137,0.381,0.5,0.769\}\), totaling 2,024 cases. The graph checks use exact integer arithmetic; comparisons of trigonometric weights and probabilities use floating-point tolerances printed in source.

The test is finite and cannot prove the universal claim. Exact spectral gaps are not calculated. Boundary angles are intentionally excluded because branch activation there can differ. The conditional stationary distributions do not imply mixing of the full billiard position/angle system.
