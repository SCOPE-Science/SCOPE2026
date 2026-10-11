---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

With \(s=1-q\), set \(X=s^{T_0}\) and \(\phi(x)=x\log x/\log s\). The lattice points satisfy \(\phi(s^t)=ts^t\), and their piecewise-linear interpolant through \((0,0)\) is concave because \(\phi\) is strictly concave. Therefore at fixed \(E X=p\), Jensen gives the sharp maximum \(M_+=L(p)\), attained exactly by the two adjacent lattice points \(s^k,s^{k+1}\). Pointwise \(T_0s^{T_0}\ge s^{T_0}\) gives \(M\ge p\), with equality only at the boundary \(T_0=1\); a law on \(\{1,N\}\) with its mixing weight chosen to preserve \(p\) makes \(M\downarrow p\). Convex mixing of fixed-p laws fills the interval. Substitution into the published affine variance identity reverses the endpoints and gives the complete variance envelope.

## originality

PASS

The accessible Wang--Lu primary record establishes the same memoryless-catastrophe setting and advertises distributional/PGF formulas; the assigned theorem uses its exact variance identity but solves an additional discrete moment problem at fixed success probability. Targeted Resultary search found no earlier exact feasible interval for \(sg'(s)\), adjacent-support minimizer or nonattained opposite endpoint. Full text of Wang--Lu was unavailable after ordinary arXiv/open-access attempts, and the authorized institutional retrieval returned an operational error, so any hidden equivalent optimization in that paper is retained explicitly as a residual risk rather than converted into failure.

## value

PASS

Fixing one-attempt success probability fixes the mean but not the variance, so the exact remaining fluctuation range is a natural question for restart/catastrophe models. The theorem solves that support-constrained moment problem completely, identifies both extremal mechanisms and shows the discrete lattice changes the Jensen envelope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
