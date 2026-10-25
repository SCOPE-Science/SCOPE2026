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

PASS: The directed order-four binary de Bruijn graph has sixteen vertices and thirty-two labeled edges. Every Euler tour gives exactly one incoming→outgoing perfect pairing at every 4-bit vertex, encoded by sixteen switches, and vice versa; successor permutation T_s(e)=2(e mod16)+(floor(e/16) xor s_(e mod16)) is a single 32-cycle iff it represents one rooted Euler tour. Exhausting 2^16=65536 pairings is both complete and duplicate-free on rotation classes. The local indicator for the six-letter factor a x1 x2 x3 x4 b is [a+x1+x2=x3+x4+b]; with b=a xor s_x, summing both arriving edges gives X(B_s)=sum_x h(x,s_x). Independent switch/permutation enumeration recovered exact frequencies {4:32,5:96,6:288,7:384,8:448,9:416,10:224,11:128,12:32}, total 2048. Independently generated cyclic words by Hamilton/Euler DFS and computed each six-letter factor and reversal/complement orbits, recovering size-two/size-four orbit counts (4,6),(0,24),(8,68),(0,96),(8,108),(0,104),(8,52),(0,32),(4,6), total 528 orbits; mean 8 and variance 23/8. Exhaustiveness follows from bijection plus exhaustive loops, not from sampling or a timeout.

## originality

PASS

PASS best of knowledge: actual general-framework primary source text and result-set searches were checked against each exact claim, with the four distinct prior-implication tests documented. No examined theorem has a stronger statement whose direct specialization is the reported exact frequency and symmetry table. The finite exhaustive switch proof contributes a logically additional distribution. Historical priority is not guaranteed. No failed search is equated to a novelty proof; unaccessed primary material is named explicitly.

## value

PASS

PASS: A de Bruijn cycle fixes the occurrence of every length-five factor but leaves the length-six neighbor relation variable. The length-six Abelian-square count is thus a natural first unconstrained Parikh-repetition statistic. The exact nine-value distribution and symmetry-orbit profile over all 2048 rotation classes are an independently useful natural finite classification, not a randomly sliced data subset.

The dated certificate retains the supplied scientific assessment, sources and limitations.
