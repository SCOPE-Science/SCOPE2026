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

Re-audited the repaired Finding and proof. For P(cos t)=f(t), the interior chord zero c=−φ/2 forces a double root since P is nonnegative on [−1,1]. At degree ≤3, P=(x−c)^2(A+B x); the third cosine coefficient B/4 must be nonnegative. Comparing x=d=η/2 to x=1 makes the ratio at most ((d−c)/(1−c))²=η², with equality forcing B=0. The normalized square belongs to the class and uniquely attains the bound. The five-point sample is I+q A(C5); explicit adjacent nonnegative rank-one terms plus (1−2q)I give complete positivity up to 1/2, including the full lower-degree range. The negative eigenvalue threshold 1−φq≥0 bounds arbitrary degree. For sharpness, the prior N=4 polynomial divided by sqrt(5) is exactly F. An independent symbolic replay solves for weights u,v,w in u+v x+w T4(x) from P(1)=1, P(c)=P'(c)=0, recovering the stated F; exact division by (x−c)^2 gives the displayed positive quadratic and exact evaluations give F(d)=η and the two Horn pairings 10−5sqrt(5), 10+5sqrt(5) for F and 1+cos 2t. Copositivity follows from mass transfer at nonadjacent vertices, reducing a triangle-free graph to a clique; the pairing is strictly negative at F. For the illustrative perturbation, the summands' zero sets do not meet, and strictly positive weights on all Fourier residues give full sample rank. Its Horn bound is sufficient only. The frozen verification script was inspected, not run.

## originality

PASS

PASS only for the repaired degree-three inequality, unique equality case, and the resulting sharp zero-chord bandwidth threshold. The frozen identification of the quartic interpolation as part of the contribution is not supported: a prior paper supplies literally the same polynomial after normalization, so quartic and unrestricted attainment are now expressly prior consequences. In the inspected comparisons, the prior extremal objective and matrix results do not supply the sharp exclusion or equality analysis for degree ≤3.

## value

PASS

The antipodal chord class is dictated by the sparsity graph of the classical five-cycle obstruction. The useful new boundary is not the old quartic formula but a necessary bandwidth theorem with unique lower-degree extremizer: it quantifies how much complete positivity is forced by a global nonnegativity constraint and three Fourier harmonics, although it fails at four. This is a motivated exact finite interpolation invariant not supplied by the cone example or the older sparse support optimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
