# Review

## Correctness

**PASS.** The only new analytic input beyond the Langharst--Wang characterization is continuity of the special-test defect. For Hausdorff-convergent convex pairs \(A_j\to A\), \(B_j\to B\) with a common interior point, the intersections \(A_j\cap B_j\) converge to \(A\cap B\). The proof in RESULT.md supplies a common interior ball, contracts every point of the limiting intersection toward its center to gain a uniform interior margin, and uses uniform convergence of support functions to place those contracted points in both approximating bodies. This gives the required inner approximation; the outer approximation follows directly from compactness and Hausdorff convergence.

For \(x\in\operatorname{int}(K-K)\), the bodies \(K\) and \(K-x\) have intersecting interiors, so the lemma applies jointly when both \(K\) and \(x\) vary. Hence
\[
(K,x)\mapsto K\cap(K-x)
\]
is Hausdorff-continuous on the stated incidence domain. The segment \([0,x]\), volume, and every mixed-volume factor in the defect are continuous as well. The strict witness set is therefore open.

Langharst--Wang Theorem 1.2 gives the exact logical input: a non-simplex fails at least one of these special tests. Failure of a non-strict inequality is strict positivity of the displayed defect. Openness then supplies a rational witness, and joint continuity supplies a positive violation margin on a Hausdorff neighborhood. The converse direction uses the known fact that simplices satisfy the Bézout inequality for all convex test bodies. The unit-square calculation independently checks the sign convention and gives defect \(s^2/4>0\).

## Originality

**PASS, to the best of our knowledge.** The current v1 of arXiv:2609.20380 was inspected at Theorem 1.2 and the proof of (iii)\(\Rightarrow\)(iv). It states the special-pair test for every nonzero \(x\in\operatorname{int}(K-K)\), but no countable test family or perturbation-stable witness theorem was located. Full-text searches of that version for “rational”, “countable”, “dense”, “robust”, and “stable” found no matching formulation.

External searches combined “Bézout inequality”, mixed volumes, simplex characterization, rational directions/displacements, dense test sets, countable tests, robustness, and witnesses. They returned the original Soprunov--Zvavitch program, the Saroglou--Soprunov--Zvavitch work, the new Langharst--Wang solution, and neighboring mixed-volume inequalities, but no statement matching (2)--(5). The continuity of mixed volumes and the interior-intersection lemma are standard/elementary ingredients; originality is claimed only for their use to extract open strict-witness sets, a universal countable rational certification, and a single rational witness stable on a Hausdorff neighborhood from the new special-test characterization.

An archive overlap search against the current SCOPE repository for Bézout/mixed-volume/simplex and rational/countable/dense-witness terminology found no matching record. The principal residual risk is that the motivating preprint is extremely recent and the refinement is a short consequence of its theorem; a later revision, author note, or unindexed parallel observation could contain the same certification statement. No specifically identified inaccessible paper gives concrete evidence of prior coverage.

## Value

**PASS.** Langharst--Wang reduce the full Bézout conjecture to a continuum of highly structured translations. The present result removes the remaining uncountability at the level of exact certification: one fixed dense set, in particular \(\mathbb Q^n\), is sufficient for every convex body. More importantly, a failure is never isolated. Every non-simplex has a strict witness that persists with a positive margin under Hausdorff perturbation of the body, so the same rational displacement certifies an entire open neighborhood of convex bodies.

This gives a useful bridge from a universal geometric characterization to discretized or sampled testing. It also cleanly separates what continuity provides from what would require new quantitative geometry: detection is positive-probability for every fixed non-simplex, but no uniform success probability or dimension-only margin is asserted.

## Limitations

The result depends on the Langharst--Wang simplex characterization and does not replace its geometric proof. No quantitative lower bound is obtained for the measure of the witness set, the violation margin, or the Hausdorff radius of stability. The intersection-continuity argument is restricted to interior difference-body shifts; boundary shifts can undergo dimension loss. The motivating theorem is very recent, so later revisions or unindexed parallel observations remain a real originality risk.

**Same-model review: passed. Independent audit: not yet performed.**
