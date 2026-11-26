---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

With peak counts (a,b,c), exactly the a left-peak voters prefer L to C and exactly the c right-peak voters prefer R to C. Hence C is the Condorcet winner precisely when both a,c≤r=(n−1)/2; outside that region the majority extreme wins IRV outright. When C is the Condorcet winner, eliminating either extreme first elects C in the two-candidate majority contest. Thus failure under every legal elimination requires C to be the unique first-round minimum, b<a and b<c; ties with an extreme cannot qualify. The independent peak probabilities (1/4,1/2,1/4) now give the exact multinomial sum. For a separate derivation of the sharp asymptotic, set u=a−b≥1, v=c−b≥1, d=u+v; then b=(n−d)/3, and the exact ratio of its peak mass to the multinomial with uniform peak probabilities is (27/32)^(n/3)·2^(−d/3). For each fixed u,v compatible with the residue, the count vector is at fixed offsets from n/3 and eventually satisfies both majority restrictions. Stirling shows that its uniform-peak mass times n tends to 3√3/(2π). A uniform bound on n times this mass follows since transferring a unit from a count exceeding another by at least two increases the multinomial mass; hence a maximizer has all counts differing by at most one, where the bound follows from Stirling. Summability of (d−1)2^(−d/3) proves dominated convergence along each residue. Summing (d−1)2^(−d/3) for d≥2 and d≡s mod 3 gives 5, 6·2^(−1/3), and 8·2^(−2/3), establishing the claimed sharp prefactor and logarithmic rate. Independently enumerating all 4^n ordered profiles, checking every pairwise majority and every legal first-round minimum, then comparing to the multinomial gave counts 0, 0, 60, 280, 11340 at n=1,3,5,7,9. The furnished code and certificate were inspected, not run; they only cover prescribed finite sizes and truncated coefficient sums. No claim for other ballot cultures or arbitrary tie-breaking probabilities follows.

## originality

PASS

The strict center-squeeze mechanism and the uniform fixed-axis culture are both prior. The finite sum is the direct probabilistic translation of that mechanism and is not credited as a substantial standalone novelty. The supported distinct result is the sharp large-electorate risk of unavoidable failure, including its residue-dependent prefactors, within the stated culture.

## value

PASS

The known center-squeeze mechanism by itself does not say how its unavoidable risk scales with electorate size. This fixed-axis benchmark yields not just exponential rarity but a sharp 1/n prefactor and a genuine three-class dependence from strict ties and integer counts. It allows precise checks of finite voting-risk approximations without relying on arbitrary tie resolution. Its scope is not a claim about real electorate frequencies or other cultures.

The dated certificate retains the supplied scientific assessment, sources and limitations.
