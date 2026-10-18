---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For nonzero diagonal U=diag(a_i), V=diag(b_i), the first row update sets x_i to y_i/a_i, and the second sees this same-iteration x_j and hence sets z_j to z_j^*=y_j/(a_j b_j) precisely after a J=i selection has preceded or coincided with a stage-two I=i selection. This two-event waiting-time decomposition gives the exact unfinished probability (1-p_i)^t+(p_i-pi_ii)*sum_{s=1}^t(1-p_i)^{s-1}(1-q_i)^{t-s} for every t>=0, with zero horizon correctly giving 1. The coefficient on pi_ii is nonpositive and strictly negative for t>=1, so optimizing all nonzero coordinate targets is equivalent to attaining the Fréchet diagonal bound min(p_i,q_i). The transport construction with residuals p_i-c_i and q_j-c_j is a valid nonnegative coupling; their supports are disjoint at each coordinate, hence it has exactly the proposed diagonal. Independent sampling has pi_ii=p_i q_i<min(p_i,q_i) for positive interior marginals. In balanced p=q=1/m, the risk reduces to m(1-1/m)^t[1+(1-theta)t/m], and uniform log-expansion about the unique solution c_m-log(1+(1-theta)c_m)=log m gives e^{-s} limit at t=floor(m(c_m+s)); synchronization theta=1 eliminates the loglog m correction. Independent exact enumeration of all two-coordinate row-pair paths for 0<=t<=4 and two distinct rational marginals matched every finite-horizon formula; algebra, not enumeration, establishes the universal assertions.

## originality

PASS

The source two-stage RK-RK algorithm updates the intermediate vector before the second-stage selection, but its convergence bound assumes separately randomized rows; it does not optimize their within-step joint law. The assessed coordinatewise first-completion representation, globally optimal fixed-marginal coupling, and finite-size synchronization window have not been located in the examined source or closely related published work. Fréchet maximal coupling itself is classical and not claimed as newly invented; the new result is its exact role in this coordinated iterative algorithm and the associated threshold.

## value

PASS

The pairing law is a natural algorithmic control variable when stage-wise row sampling distributions are prescribed and cannot be changed. The exact all-horizon optimizer and explicit sharp delayed-versus-synchronized threshold supply mathematically motivated performance information beyond a renaming of a familiar coupling inequality. The diagonal subclass is intentionally a solvable structural benchmark, not an unmotivated numerical slice; it exposes a logarithmic-logarithmic delay absent at full synchronization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
