---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

For all m>=3, with binary base fixed at 2 and t_m(j)=s_2(j) mod m, the exact carry identity d_j=1-v_2(j+1) mod m forces at least one +1 among every adjacent pair. If both a triple and its reverse occur, its consecutive differences must contain +1 and -1, hence are exactly (1,-1) or (-1,1) (since +1!=-1 mod m); the triple is a palindrome. If a length-four factor and its reversal both occur, its overlapping triples must be palindromes, forcing alternating letters. An alternating quadruple with differences (-1,1,-1) is impossible: its start is odd, j+1,j+3 are consecutive even integers and exactly one has v_2=1, forcing a zero increment. Hence an alternating quadruple can begin with +1 only, while its reverse would have to begin with -1. The local contradiction implies all n>=4; for n=3 all reversal-identified factors are already identical. Constructions j=2^v(2k+1)-2 or -1 realize every triple with first or second increment +1 and each initial residue, establishing 2m^2-m triples, 2m palindromic triples, all m^2 pairs, and r(2)=m(m+1)/2. Independent bounded prefix checks and independent exact constructed witnesses corroborate but are not used to infer the infinite conclusion.

## originality

PASS

Best-of-knowledge new all-modulus ordinary-reversal exclusion at factor length four, hence reflection-complexity equality for m>=4, answering the explicit extension question in Allouche et al. (2024). Existing earlier literature has already proved the m=3 equality, described palindromes of these words, and (Starosta 2011) classified short factor languages/ordinary factor complexity and D_m twisted-reflection invariance. Those prior facts are NOT claimed as new; the new obstruction concerns ordinary reversal R, which is different from antimorphisms Psi_x over m>=3. No inspected primary theorem or published-record result implies the uniform no-reversed-pair length-four conclusion. Historical synonymous prior art remains possible.

## value

PASS

Answers a specifically posed and natural reflection-complexity extension for all binary-digit-sum residue words m>=4 with a sharp constant local obstruction; length-three palindromes persist, yet all length-four reflected pairs are excluded. The theorem reduces entire infinite-family reflection counting to ordinary factor counting for n>=3 and identifies the precise obstruction, not a simple parameter substitution or an arbitrary finite census. Previously known short ordinary complexity counts are explicitly not treated as novel.

The dated certificate retains the supplied scientific assessment, sources and limitations.
