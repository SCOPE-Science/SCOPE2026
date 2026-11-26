---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The frozen sign, scaled-node and amplification claims are correct, but its unconditional assertion (RESULT.md lines 54 and 77, also in REVIEW.md and METADATA.json) that constant normalization destroys kernel-translate exactness is false. At ell=sqrt(3) and a²=24 log(5/4), t=(4/5)^4, u=(4/5)^3 and c=sqrt(3)/2. Substitution in S=c[1+2(u-t)/((1-t)(1+t)^2)] gives S²=113167253586821281/109369216915761708>1 by exact rational arithmetic. As a tends to infinity at the same ell, S tends to c<1, so some finite spacing has S=1 and normalization does nothing. /workspace/repairs/3/ replaces the three affected files and preserves the frozen source. Reassessment of the repaired claim: subtracting t times the center row from the outer row leaves (1-t²)^2 w=c(u-t)>0. The sign of v is that of log cosh(y)-y/[2(1+ell²)]; y tanh(y)-log cosh(y) grows from zero, so the scaled logarithm increases from 0 to 2 and crosses exactly once. Integrating tanh(y)>y/(1+y) gives h(y)>y/(1+y) and hence a_*<1; also h(2)>1 gives y_*<2. At ell²>=1/2 the scaled GH radius squared is at least 1, and at ell²<=1/2 it is at least 2ell², so positivity is strict in both cases. Solving the monotone node-scale relation gives the stated alpha cutoff. The Gram system tensorizes; rescaling multiplies each strictly positive exact kernel mean by S^(-d), hence preserves exactness iff S=1. The absolute-mass/total-mass ratio to the d-th power is attained by the signs of the weights. Taylor expansion gives w~c³/(2a²) and S→c+c³/(2ell²), verifying the amplification prefactor. The limits of the sign frontier follow from h(y)=y+O(y³) at zero and continuity at its level 1. Frozen verify.py was inspected, not executed; the universal checks are algebraic. This is a three-node fixed-target result, not an RKHS error or higher-order positivity theorem.

## originality

PASS

Only the exact fixed-target sign boundary and the all-bandwidth natural three-node guarantee with their quantitative consequences receive credit. Prior work observed positivity numerically and proved formulas for a different, Mercer-truncated rule. A later generalization does cover the spacing boundary; its indexed date is later, not evidence of prior coverage. Tensor factorization, absolute-mass norm and the elementary normalization qualification are not independent originality claims.

## value

PASS

Three symmetric nodes are the first symmetric grid capable of a negative weight. They supply a necessary-and-sufficient spacing rule for stable mass-one nodal integration and rigorously settle the first nontrivial symmetric case of the empirical scaled-GH observation. The exact coalescence coefficient explains when tensor products amplify bounded nodal perturbations, without claiming anything about RKHS error or matrix conditioning. The normalization repair preserves all of this; the exception itself is not assigned separate value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
