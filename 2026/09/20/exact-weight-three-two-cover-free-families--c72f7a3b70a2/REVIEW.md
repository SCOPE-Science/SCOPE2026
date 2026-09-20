# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The key repeated-pair lemma is exact: if two distinct triples share a pair \(xy\), then the third point of either triple cannot occur in any other block, since that other block together with the other \(xy\)-triple would cover the target triple. Thus a repeated pair of codegree \(s\) contributes \(s\) degree-one leaves and gives the valid reduction
\[
|\mathcal F|\le s+F_3(v-s).
\]

The linear case is exactly a \(2\)-\((v,3,1)\) packing, and every such packing is 2-cover-free because each of two other triples intersects a target triple in at most one point. The small cases \(v=3,4,5,6\) were checked separately. The induction for \(v\ge7\) uses only the classical exact table for \(D(v,3,2)\) and the residue-class consequences \(D(t+1)\ge D(t)+1\) and \(D(t+2)\ge D(t)+3\) for \(t\ge6\). These inequalities were checked directly from all six residue classes. They make the non-linear reduction strict for \(v\ge7\), proving both the exact maximum and extremal linearity.

As a finite independent sanity check, the included integer program optimizes the defining cover-free constraints exactly for \(v=3,\ldots,9\), producing \(1,2,3,4,7,8,12\), all matching the theorem. The finite computation is supplementary and is not used as a substitute for the proof.

## Originality

**PASS, to the best of our knowledge.** The primary 1982 Erdős--Frankl--Füredi paper formulates this exact uniform cover-free problem. For weight three, its theorem gives the pair-count upper bound with equality in Steiner-system cases, and its stated general conclusion is \(F_3(v)=v^2/6+O(v)\); the checked text does not state the all-orders exact formula proved here.

The exact values of \(D(v,3,2)\) are classical: Bailey--Burgess explicitly attribute the maximum \(2\)-\((v,3,1)\) packing table to Schönheim (1966). Recent CFF literature also explicitly knows the forward construction: Idalino--Moura (2026), Section 6.2, states that a \(2\)-\((v,k,1)\) packing with \(k\ge3\) yields a 2-CFF. The checked current source does not state that every maximum weight-three 2-CFF is a maximum packing from \(v=6\), nor the stronger extremal-linearity theorem from \(v=7\).

Searches under cover-free family, 2-disjunct matrix, superimposed code, constant column weight, partial Steiner triple system, and packing terminology did not locate the same exact theorem. Li--van Rees--Wei (2006) is directly relevant but its accessible abstract emphasizes explicit constructions and unrestricted optimal 2-CFFs on 9, 10, and 11 points; its full text was not fully inspected. Yu--Wang--Ji (2025) is also relevant; its accessible abstract treats row-weight-limited optimal 2-disjunct matrices and an asymptotic bound for column weights \(r+1\le w\le2r\), but its full text was not fully inspected. These are residual originality risks. Because the proof is short and its ingredients are classical, prior appearance under alternative terminology remains plausible and the originality claim is deliberately limited to the best of our knowledge.

## Value

**PASS.** The result closes the exact weight-three case of a classical uniform cover-free extremal problem for every ground-set size. It converts a general upper bound/asymptotic statement into a complete residue-class formula, and the structural theorem shows that for \(v\ge7\) every optimum automatically collapses to a classical maximum packing. In group-testing language, it gives the exact item capacity of binary 2-disjunct matrices with column weight three and classifies the structural form of every optimum for all sufficiently large row counts (indeed, every \(v\ge7\)).

## Scientific limitations

The argument is special to uniformity three and disjunctness two. It does not directly determine higher constant column weights or \(d\)-disjunct matrices for \(d>2\). The exact numerical formula depends on the classical maximum partial-Steiner-triple packing theorem. Residual originality uncertainty is concentrated in relevant sources whose full texts were not completely inspected and in the possibility of an equivalent result stated in different terminology.
