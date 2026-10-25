---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For n>=3, a=2^n+1, generators g_i=(a+1)(2^i-1)+a, the cited Liu–Xin–Ye–Yin Apéry formula applies for gcd(a,1)=1 and a>=m-1 with m=n-1: w(r)=(a+1)r+a t_m(r), t_m the greedy coin count using c_i=2^i-1. Direct semigroup-order comparison gives no-upward-jump condition t_m(r+c_i)<=t_m(r) on nonwrap, while wrapped jumps are automatically nonmaximal restrictions because the w difference has positive multiple of a. The induction on h for jump-maximal residues on [0,2(2^h-1)] identifies exactly the final h consecutive positions, with t_h(R_h-q)=q+2; its h=1 boundary and above-largest-coin reduction are explicit. At the actual cutoff a-1=2(2^m-1)+2 the top three coin counts 2,3,4 eliminate all but residue a-1 and tail residues a-1-j for 4<=j<=n; the apparent j=3 candidate fails because jump +3 reaches a-1 with larger count. Translation w(r)-a yields PF={a²+3a-1} ∪ {a²-a-1-j :4<=j<=n} and type n-2, including symmetric n=3. Independently reconstructed all Apéry shortest paths and full PF spectra for n=3..8, separately from greedy formulas.

## originality

PASS

The 2023 generalized repunit source includes the needed generic greedy/Apéry description but its explicit pseudo-Frobenius theorem assumes a repunit multiplicity (b^n−1)/(b−1); present a=2^n+1 is not that family. Other generalized repunit results likewise use repunit multiplicity. The full isolated-largest-gap plus (n−3)-block PF spectrum and type n−2 for all n>=3 require the new jump-maxima argument; no equivalent same-parameter theorem found in Resultary/primary-source comparisons.

## value

PASS

A complete PF spectrum and type of a natural Fermat-shaped companion to the well-studied Mersenne/repunit semigroups gives an infinite-family structural contrast. The isolated Frobenius gap plus consecutive lower gap block and linear type n−2 are useful exact invariants, not inferred from known Frobenius values alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
