---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

All assumptions are explicit: n≥1, nontrivial finite C with d(C)≤n inside an existentially closed exponent-three group; class at most three and finite local freeness. The first defect rank r₂=dim((C∩γ₂(G))/γ₂(C))≤dim gr₁(C)≤n, so q₂(n) fresh rank supplies r₂ independent degree-two wedges. In the PRIMARY source Lemma 4.7 proof, Claim B uses only independence to force all degree-two relation coefficients to zero, and Claim C uses the direct-sum V_G⊗Λ²V_F component and independence to force all old-side commutator coefficients to zero; overlap of pairs within the fresh basis does not affect either argument. Lemma 4.8 then obtains degree-two strictness. With N=n+q₂(n), the second defect r₃≤dim gr₂(D₁)≤binom(N,2). Independent triple-wedge basis classes in F_{q₃(N)} ensure central relations give G∩L=1 by the exact argument of primary Lemma 4.9. The intersection computations in Lemma 4.10 need only that each central defect is represented by a degree-three generator; a shared fresh factor suffices. Primary Lemma 4.6 adds exactly two generators, and finite exponent-three groups are locally finite, allowing e.c. transfer into M. Theorems 3.3 and Proposition 4.13 then give B(s(m)). Independent reimplementation computed q₂,q₃,B for n=1,2,3,4,5,10,100,1000,10000,100000 and s(m),B(s(m)) for m=1,2,3,5,10,20,40,100; no numerical contradiction. The universal bound rests on the symbolic proof, not a finite sample.

## originality

PASS

Best-of-knowledge originality survives, narrowly: the source paper explicitly supplies the general exterior-power structure and a 4-defect packing example, and even states the trick works for the first repair, but its printed quantified strict-envelope theorem remains 15n^2. No inspected independent prior work states or already provides the full all-n inverse-binomial envelope B(n) and propagated O(m^4) bound. The novelty is executing the hinted packing simultaneously and deriving explicit all-n quantitative consequences, NOT discovering the packing idea. The closeness to Remark 4.11 is a substantive residual priority/value risk.

## value

PASS

The object is the natural strict finite envelope of a finite subgroup of an existentially closed exponent-three group, a central quantitative input in the primary model-companion proof. Existing constructions use distinct commutator blocks and a quadratic generator bound; the independently motivated invariant is the number of new generators required to cure first- and second-layer defects. Packing through Λ² and Λ³ systematically improves the asymptotic generator bound from 15n² to n+O(n^(2/3)), and the concrete downstream finite-amalgamation obstruction witness from O(m⁸) to O(m⁴). The improvement is structural and asymptotic, not a renaming or tiny-table computation. The source itself explicitly highlights nonoptimality, but does not present this uniform propagation. No optimality or complexity lower bound is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
