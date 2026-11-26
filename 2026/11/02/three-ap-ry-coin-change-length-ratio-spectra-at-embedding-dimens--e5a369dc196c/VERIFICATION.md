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

Each atom except m is an Apéry minimum (otherwise subtracting m decomposes it); there are exactly three nonzero composite minima. Every positive partial sum of an Apéry factorization also lies in the Apéry set, or subtracting m there would allow it at the whole sum. The increasing length-2 through length-k partial sums give k≤4. If a four-term factorization contains two unequal atoms b,c, take a third summand a: a+b, a+c, a+b+c and the full sum are four distinct composite minima, impossible. So the composites must then be 2a,3a,4a. A triple for 4a would have every pair sum in {2a,3a}; a pair at 2a forces a nonatom complement 2a, while a pair at 3a forces complement a and the other two pair sums then both 2a (else a summand is the nonatom 2a). This would give three copies of a, also impossible. A double for 3a would give such a triple for 4a. Thus 2 is the only possible nonunit ratio with any length four; without it, 3/2 is the only one. For realization, m,m+1 ensure cofiniteness and multiplicity m. Omitting m in minima, in (a) a high generator plus any positive summand exceeds the largest proposed minimum; pure copies of m+1 cover residues 1–4 uniquely and are dearer in larger residues. In (b), a high generator with copies of m+1 that reaches residue 1–4 must wrap, using at least two copies and costing above those minima. Two highs with residue sum m+j reach 3m+j, tying the triple at j=3 and beating four copies at j=4; (5,m−2) and (5,m−1) realize these for m≥7. Other high pairs cannot improve a minimum, and three highs cost at least 3m+15. In (c), two ordinary highs or any three highs exceed 4m+4; two special generators cost 4m−2 at residue m−2, more than its minimum. An ordinary high plus the special costs 4m+j−1, tying only at j=5. An ordinary high plus one m+1 has a larger cost than the minimum at residue j+1, and plus at least two exceeds 4m+4. The special plus one m+1 reaches residue zero, plus two reaches residue one above its minimum, and plus at least three exceeds 4m+4. These comparisons verify minimality, atomicity of the displayed generators, and the claimed lengths for all m≥7. Independent increasing-amount enumeration confirms all three spectra, atom counts, and the precise exceptional length sets for 279 instances.

## originality

PASS

The closest primary paper explicitly treats the adjacent near-maximal case e=m−2 and leaves the next cases open. Its unconstrained realization result does not force fixed e=m−3 or realization at each m. The closest indexed coin/Apéry results concern different quantities. This supports the distinct fixed-defect classification and uniform realization, not priority for individual spectra.

## value

PASS

This is the next natural case at the explicit near-maximal boundary in the motivating elasticity paper, not an arbitrary fixed parameter slice. It also identifies a structural obstruction: a four-term ladder rules out a coexisting 3/2 ratio, and the three spectra remain attainable at every eligible multiplicity. The precise exclusion and realization are useful for the research question of what elasticity data are possible at constrained embedding dimension.

The dated certificate retains the supplied scientific assessment, sources and limitations.
