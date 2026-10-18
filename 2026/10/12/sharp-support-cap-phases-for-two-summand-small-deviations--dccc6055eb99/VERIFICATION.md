---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Exact claim: for independent 0<=X,Y<=L with E X=E Y=1 and inclusive event X+Y>=3, F(L)=0 when 1<=L<3/2; 1/[L(3-L)] for 3/2<=L<=2; 1/2 for 2<=L<=2+1/sqrt(2); [2t+3t^2]/(1+2t)^2, t=L-2, for 2+1/sqrt(2)<=L<=3; 5/9 for L>=3. Read the complete proof: each mean-one [0,L] marginal is a mixture of degenerate one or mean-one two-atom laws, preserving cap and independence on product mixtures. Each elementary pair has low-low impossible, high-high only bound, one-cross bound<=1/2, or both crosses with b=3-c,d=3-a and H(A,B) monotone on 0<A,B<=min(1,L-2). Explicit two-atom extremizers attain each branch, including the discontinuity at L=3/2 and plateau transition; end points agree. Independently enumerated exact rational two-atom grids across L=3/2,9/5,2,5/2,14/5,3,4 and checked the required branch values. Grid is supporting evidence only; complete moment-mixture argument proves arbitrary distributions.

## originality

PASS

Ling proves the uncapped optimum 5/9 and a general two-atom reduction. The complete support-dependent envelope and its internal phase boundaries are not implied by the uncapped scalar bound, nor by standard exponential Chernoff bounds. Full-text inspection of Ling separates known mixture lemma from the new finite-cap optimization. An older differently indexed exact cap result remains a priority risk.

## value

PASS

A natural, useful support-capped extension of the unrestricted two-variable Feige/Samuels small-deviation extremum with exact attained phases, a discontinuous threshold, a plateau and a nontrivial algebraic switching cap. The cap is a meaningful probabilistic constraint, and the exact bound is not a routine single application of Markov or Hoeffding; it distinguishes sharp event probabilities from surrogate exponential inequalities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
