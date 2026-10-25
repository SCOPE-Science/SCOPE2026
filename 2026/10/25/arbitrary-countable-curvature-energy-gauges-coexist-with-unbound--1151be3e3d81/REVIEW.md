# Scientific review: countable curvature-energy gauges

## Correctness — PASS
The construction fixes the curvature height \(a_j\log(1/\varepsilon_j)=j\) exactly while forcing the volume of each high-curvature core to become arbitrarily small. In the new dominated-convergence lemma, for fixed index \(j\), the upper envelope at every positive radius tends to zero as the amplitude tends to zero but remains uniformly bounded by \(2C_1(j+1)\). This is a valid integrable dominator for each finite continuous gauge on a finite ball. Selecting the amplitude to meet the first \(j\) inequalities produces convergence for every fixed gauge. The symbolic checker independently recomputes the center's algebraic tensor norm and zero Ricci contraction. Cheng's uniform estimates supply the full Ricci and injectivity claims; the note makes explicit that injectivity is **not** deduced from bilipschitz equivalence. The Gauss and scalar equations give the stated coefficient \(3/8\). Remaining dependency: correctness of the cited geodesic estimate from the inspected primary paper.

## Originality — PASS, subject to literature risk
Cheng's full primary text [1] includes variable-amplitude curvature peaks and the mean-curvature obstruction but not a theorem imposing arbitrary countable curvature-integrability gauges. Cheeger–Naber [2] concerns automatic local polynomial curvature integrability under two-sided Ricci bounds/noncollapsing and does not imply a global existence construction for every countable family of gauges. Results searches included equivalence terms (Orlicz, all exponential moments, global integrability, curvature concentration, and bounded-mean-curvature isometric immersion), both in scholarly literature and relevant result records. No equivalent or stronger-covered claim was identified in the inspected material. An unindexed variation of the Cheng example could still be prior art; the claim is not that all alternative constructions have been ruled out.

## Value — PASS
The result separates two natural geometric hypotheses that can appear superficially similar: control by arbitrarily many integral curvature observables, even rapidly growing ones, versus a uniform pointwise curvature bound. The simultaneous diagonal theorem shows no *specified countable* package of such global energy assumptions alone can replace the pointwise curvature requirement for bounded-mean-curvature Euclidean immersions, while preserving a positive injectivity radius and exceptionally mild Ricci geometry. Countable quantification and global moment finiteness are not consequences of the source's variable-amplitude claim without an additional construction and proof.

## Principal sources and limitations
[1] H. Cheng, *A counterexample to Yau's bounded-mean-curvature embedding question*, arXiv:2610.00153v1, §§3–6 (primary construction and global injectivity argument).
[2] J. Cheeger and A. Naber, *Regularity of Einstein manifolds and the codimension 4 conjecture*, arXiv:1406.6534v10 (local curvature integrability comparison).
The metric depends on the chosen **countable** gauge family; there is no single metric integrating every gauge. The source's analytical injectivity estimates remain a cited dependency. A possible unindexed parallel concentration construction is the main originality risk.

Self-review: passed. Independent audit: not yet performed.
