---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Let q=2^m with m odd and 1<=k<=q pairwise distinct constant shifts. Translation of monic cubic T³+aT²+bT+c by T↦T+a gives T³+uT+d with u=a²+b, d=ab+c; each (u,d) has q lifts. The depressed cubic is nonsquarefree iff d=0 (with shifts d+c_i=0); for squarefree cubics Carmon’s Berlekamp expression 1+u³/(d+c_i)² and characteristic-two Pellet sign yield mu=ψ(u³/(d+c_i)²) since Tr(1)=1. Multiplication over shifts gives additive character at u³(P’(d)/P(d))². Since gcd(3,q-1)=1 the cube map permutes K, making the u-sum q when P’(d)=0 and 0 otherwise. P separable excludes shift roots; summing gives exactly q² times number of K-roots of P’, whose square-polynomial structure bounds it by floor((k-1)/2). Checks k=1,2,3,4 and q=2 apply. Independent direct root-factor-sign enumeration over GF(8) for five representative shift subsets agrees: totals 0,64,0,64,0; the square-root counts match. Finite tests do not establish all odd m.

## originality

PASS

PASS for exact all-constant-shift cubic correlations in odd-degree binary extensions. Carmon (2015) provides both the precise cubic Berlekamp/Pellet identities and Chowla-type q→∞ estimates; these ingredients are prior, but its stated theorem is a bound rather than the exact nonnegative integer correlation for every fixed field and shift set. Carmon–Rudnick addresses odd characteristic. The derivative-root reduction and four-shift dichotomy are a motivated arithmetic classification. A hidden specialization of Carmon’s counting machinery could imply the identity, so priority remains conditional.

## value

PASS

This is an all-k fixed-degree exact evaluation of Chowla-type correlations, not a generic restatement of the underlying discriminant identity. Positivity and divisibility by q² plus a four-shift vanishing criterion are precise natural arithmetic invariants; the odd-extension boundary is sharp and GF(4) obstructs naive extension.

The dated certificate retains the supplied scientific assessment, sources and limitations.
