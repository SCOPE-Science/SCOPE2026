---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For the sign pair, put t_i=x_i y_i. The rank-one projector gives the error −a_i t_i Σ_{l≠i}a_l²t_l/T in either order. The t_i are independent signs, so a covariance term survives exactly for l=m on the diagonal or the crossed pair (l,m)=(j,i) off it. Summing the diagonal yields the claimed risk; with w_i=a_i²/T, its normalized value is the w_i-weighted average of w_i(1−w_i). Equality forces both positive weights to be 1/2. For Gaussian probes the endpoint ranks give exactness. In the middle phase, rotation invariance of the independent omitted sketch gives P_ii strictly between 0 and 1 almost surely, so the off-diagonal row of P has positive squared norm P_ii(1−P_ii). Its contraction with the other coordinates of the omitted probe has a nondegenerate Gaussian law conditional on P. When its i-th coordinate s tends to zero the other leave-one-out terms stay bounded: at zero their sketch contains one almost surely nonzero vector in the coordinate hyperplane and k−2 independent full Gaussians, hence is full column rank, and continuity holds nearby. Thus the pole cannot cancel and the conditional absolute moment diverges for p≥1. For p<1, subadditivity and the absolute moment of a Gaussian ratio suffice. For n=k=2 the Cauchy pair reduces the error to −aF/2 with F=UV[(1+U²)⁻¹+(1+V²)⁻¹]. On |U|≥|V| at fixed V=v the limiting one-signed coefficient is |v|/[π(1+v²)], and a constant multiple of this bounds the scaled tail uniformly by the Cauchy tail inequality. Integrating against the Cauchy density gives 1/π² per region, hence a/π² in each tail after scaling and sign symmetry.

## originality

PASS

The established contributions are the exact sign-probe all-diagonal covariance and sharp risk with zero component dissent, and the scalar Gaussian moment phase and smallest-case signed tails for the literal estimator. The XDiag definition, standard Gaussian-ratio moments, and normalized-probe scalar exactness are not new. Whether any specific software implementation accepts Gaussian probes was not checked and is not needed by the theorem.

## value

PASS

The sharp sign example separates zero component disagreement from true risk, and even shows that moving from one probe to two need not improve this estimator. The Gaussian calculation identifies a real rank-dependent failure of a natural but formal probe-law substitution: nonintegrability persists for every intermediate count and disappears at full omitted-sketch rank. These can be used as exact estimator and diagnostic benchmarks without claims about software or performance outside the stated model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
