# Five tips are the sharp threshold for common-risk phylogenetic conservation-priority switching

## Finding

**Theorem (sharp five-tip conservation-priority boundary and complete five-tip classification).** Let \(T\) be a rooted, fully binary, ultrametric phylogenetic tree with \(n\ge2\) labeled extant tips, all branch lengths strictly positive and common root-to-tip distance \(H>0\). Each taxon independently becomes extinct with the same probability \(q\in(0,1)\). At equal cost, choose exactly one tip and force its survival; maximize the resulting expected rooted Faith phylogenetic diversity.

1. If \(n\le4\), some *fixed tip*, independent of \(q\), is optimal for every \(q\in(0,1)\).
2. If \(n=5\), the identity of an optimal tip depends on \(q\) (equivalently, no fixed tip is optimal for every \(q\)) **if and only if** the root split is \(2+3\) and the root-to-crown lengths \(a,b\) of the two-tip and three-tip subtrees, respectively, obey

\[
b<a<2b.
\]

Here both crown edges have positive lengths less than \(H\); the two-tip crown has tips \(A,B\), and the three-tip crown has an outgroup tip \(C\) and a nested cherry \(D,E\) at root-depth \(t\in(b,H)\). Under the strict inequality above the unique threshold is

\[
q_*=\frac{a}{b}-1\in(0,1).
\]

For \(0<q<q_*\), \(C\) is the unique optimal tip; for \(q_*<q<1\), precisely \(A,B\) tie as optimal; and at \(q=q_*\), precisely \(A,B,C\) tie. The tips \(D,E\) are never optimal for \(0<q<1\). If \(a\le b\), the two-tip leaves \(A,B\) remain optimal for every \(q\); if \(a\ge2b\), \(C\) remains optimal for every \(q\). The \(1+4\) root split likewise has a universally optimal singleton child.

In particular, the minimum number of tips for a change in the *globally optimal* single-taxon conservation intervention as common extinction risk varies is exactly **five**.

## Assumptions and scope

A rooted fully binary tree has exactly two children at each internal vertex and no zero-length edges. An ultrametric tree has an equal root-to-tip path length \(H\). For an arbitrary set \(S\) of surviving tips, rooted Faith phylogenetic diversity \(\operatorname{PD}(S)\) is the sum of lengths of all branches on paths from the root to leaves in \(S\), and \(\operatorname{PD}(\varnothing)=0\). All other taxa retain their independent extinction probabilities when a single selected focal taxon is made certain to survive. Every intervention has the same cost. The optimization compares the **expected increase in PD** over the unprotected baseline, not estimated population persistence, biodiversity utility with heterogeneous weights, or standardized per-taxon scores.

For each tip \(i\), let \(S_i\) denote the random set of surviving tips other than \(i\) under common risk \(q\). Set

\[
\Psi_i(q)=\mathbb E\!\left[\operatorname{PD}(S_i\cup\{i\})-\operatorname{PD}(S_i)\right].
\]

The actual improvement from making \(i\) certain to survive rather than leaving it exposed to risk \(q\) is

\[
\Delta_i(q)=q\Psi_i(q).
\]

Because the factor \(q>0\) is common across taxa, maximizing \(\Delta_i(q)\) is equivalent to maximizing \(\Psi_i(q)\). The latter is the previously established rooted HED score; neither that index nor its general branch formula is asserted to be new.

## Proof

**1. Marginal-gain identity and branch formula.** Consider any edge \(e\) on the unique root-to-tip path for \(i\); let \(C(e)\) be its set of descendant tips and \(\ell_e\) its length. Protecting \(i\) adds \(e\) to the surviving rooted subtree exactly when all other members of \(C(e)\) go extinct. Since those events are independent, that has probability \(q^{|C(e)|-1}\). Summing the edge contributions gives the established HED identity

\[
\Psi_i(q)=\sum_{e\in P(\mathrm{root},i)}\ell_e q^{|C(e)|-1}.
\tag{1}
\]

Without protection the edge is gained only when \(i\) survives as well; with protection it is gained whenever no other descendant survives. Equivalently, the change in baseline expectation is \(\mathbb E[\mathbf1_{\{i\text{ extinct}\}}\,(\operatorname{PD}(S_i\cup\{i\})-\operatorname{PD}(S_i))]\), which is \(q\Psi_i(q)\) because survival/extinction of \(i\) is independent of \(S_i\). This proves the intervention identity exactly, without conditioning on any negligible events.

**2. A singleton root child is always optimal.** Suppose one child of the root is a single tip \(i\). The sole root-to-tip branch for \(i\) has length \(H\), so \(\Psi_i(q)=H\). For any other tip \(j\), its root-to-tip path has total length \(H\), and at least one strictly positive edge on that path subtends at least two descendant tips. Formula (1) weights that edge by \(q^{m-1}<1\) with \(m\ge2\), hence \(\Psi_j(q)<H\) for all \(0<q<1\). Thus \(i\) is uniquely and uniformly optimal.

**3. No switching with at most four tips.** Every fully binary rooted topology on \(n=2\) or \(n=3\) has a singleton root child. Among four-tip trees, the only root split not covered by Step 2 is \(2+2\). Write \(a,b\in(0,H)\) for the two root-to-cherry edge lengths. By ultrametricity, either tip in the first cherry has score \(H-a+aq\), and either tip in the second has score \(H-b+bq\). Their difference is \((b-a)(1-q)\), which has constant sign for \(0<q<1\). Consequently one entire cherry is optimal for all \(q\). This includes \(a=b\), where all four tips tie at all risks.

**4. The complete five-tip calculation.** Every fully binary rooted five-tip tree has root split \(1+4\) or \(2+3\). The former is covered by Step 2. For \(2+3\), assign labels and lengths as in the theorem. Ultrametricity fixes the pendant lengths, so formula (1) gives

\[
\begin{aligned}
\Psi_A(q)=\Psi_B(q)&=H-a+aq,\\
\Psi_C(q)&=H-b+bq^2,\\
\Psi_D(q)=\Psi_E(q)&=H-t+(t-b)q+bq^2.
\end{aligned}
\tag{2}
\]

Because \(t>b\),

\[
\Psi_C(q)-\Psi_D(q)=(t-b)(1-q)>0\qquad(0<q<1).
\tag{3}
\]

Thus the only possible global optimal taxa are \(A,B,C\). Their decisive comparison factors as

\[
\Psi_C(q)-\Psi_A(q)=(1-q)\bigl(a-b(1+q)\bigr).
\tag{4}
\]

The first factor is positive for \(0<q<1\). If \(a\le b\), then \(a-b(1+q)<0\), so \(A,B\) are always best. If \(a\ge2b\), then \(a-b(1+q)>0\) for every \(q<1\), so \(C\) is always best. If \(b<a<2b\), the affine second factor has its unique zero at \(q_*=a/b-1\in(0,1)\); it is positive before and negative after the zero. Equations (2)-(4) identify the winners strictly and show that there is no taxon common to all optimal sets. The parameter regimes are exhaustive, giving both necessity and sufficiency, and Step 3 proves the asserted sharp minimum. \(\square\)

**Exact five-tip witness.** Take \(H=4\), \(a=3\), \(b=2\), and \(t=3\). The eight positive edges are: root to \(\{A,B\}\) of length \(3\); its two terminal edges of length \(1\); root to \(\{C,D,E\}\) of length \(2\); its terminal edge to \(C\) of length \(2\); its inner edge to \(\{D,E\}\) of length \(1\); and its two terminal edges of length \(1\). Then

\[
\Psi_A=\Psi_B=1+3q,\qquad
\Psi_C=2+2q^2,\qquad
\Psi_D=\Psi_E=1+q+2q^2,
\]

and \(\Psi_C-\Psi_A=(1-q)(1-2q)\). The optimal taxon is \(C\) for \(q<1/2\), changes at \(q=1/2\), and is either \(A\) or \(B\) for \(q>1/2\).

## Verification

The accompanying self-contained `verify.py` uses Python standard-library exact rational arithmetic. It constructs the eight-edge tree above and computes rooted PD directly from descending edge sets; for each of five distinct rational extinction probabilities it checks the 16 independent survival scenarios for each of five focal taxa against equation (1), verifies exact score profiles and all optimal-taxon sets, and checks the two symbolic comparison factorizations by coefficient and rational evaluations. It also tests equation (4) at several other rational branch lengths, including boundary cases. Run `python3 verify.py` from the directory containing this report and script. Its success signal begins `VERIFY_OK`.

These finite calculations verify the witness and algebra but are **not** substitutes for the universal arbitrary-length proof in Steps 1-4. The proof does not rely on a sampling simulation or any finite search for a general statement.

## Relationship to prior work

The rooted HED index and its general edge-sum formula are Theorem 3.1 of Steel, Mimoto and Mooers (2007); the fact that protecting a focal taxon improves expected PD by its extinction probability times its HED score follows from their Theorem 4.1. These expressions are used here as acknowledged premises, and the present claim is *only* the fully binary, ultrametric, common-risk sharp minimum and five-tip global-optimum classification.

Mooers, Faith and Maddison (2008) exhibit risk-transformation sensitivity of HEDGE and EDGE rankings on a four-species tree; their illustrative risk probabilities differ across species, rather than being the single common parameter analyzed here. Their result therefore neither contradicts nor implies the uniform-risk four-tip impossibility established in Step 3. Fischer, Francis and Wicke (2021) study robustness of the Fair Proportion index after extinction and re-ranking, a distinct index and comparison mechanism. The texts examined do not state the theorem or the five-tip iff condition; the existence of an unexamined stronger result remains a possible prior-art risk.

## Limitations

The theorem assumes rooted phylogenetic diversity, binary topology, strictly positive edges, an ultrametric clock, independently identical extinction probabilities, one perfectly protected species, and equal protection costs. Heterogeneous threats, nonultrametric phylogenies, nonbinary trees, joint multiple protections, conservation costs, and probabilistic intervention success are outside its conclusion. The result is an exact mathematical ranking property, not empirical support for any particular species priority or estimate of real-world extinction probability. The underlying HED formula is pre-existing; the classification follows by specializing it and should not be interpreted as a new general HED method. No independent scientific audit or empirical validation is claimed.

## References

1. Steel, M., Mimoto, A., and Mooers, A. Ø. (2007). *Hedging our bets: the expected contribution of species to future phylogenetic diversity*. arXiv:0704.2649v1 (first public 20 April 2007), Theorems 3.1 and 4.1, Appendix. https://arxiv.org/abs/0704.2649 .
2. Mooers, A. Ø., Faith, D. P., and Maddison, W. P. (2008). *Converting Endangered Species Categories to Probabilities of Extinction for Phylogenetic Conservation Prioritization*. PLOS ONE 3(11): e3700. DOI 10.1371/journal.pone.0003700. https://doi.org/10.1371/journal.pone.0003700 .
3. Fischer, M., Francis, A., and Wicke, K. (2021). *Phylogenetic Diversity Rankings in the Face of Extinctions: the Robustness of the Fair Proportion Index*. arXiv:2107.00748v1. https://arxiv.org/abs/2107.00748 .
