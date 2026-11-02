# A six-component ceiling for nearly free smooth-conic arrangements with \(A_1,A_3,D_4,A_5,A_7\) singularities

## Finding
Let \(\mathcal C\subset\mathbb P^2_{\mathbb C}\) be a reduced union of \(k\ge2\) **distinct smooth conics**. Assume that every singularity of the union is a node \(A_1\), a tacnode \(A_3\), an ordinary triple point \(D_4\), a two-branch \(A_5\) point, or a two-branch \(A_7\) point. If the union is nearly free in the sense of the Jacobian-syzygy definition of [1], then
\[
\boxed{k\le 6.}
\]
Thus nearly free arrangements of seven or eight smooth conics in this singularity class do not exist. This improves the previously established necessary bound \(k\le8\) [1, Remark 2.7] and rules out two of the four sizes \(k=5,6,7,8\) identified there as having no known nearly free example. It neither constructs arrangements for five or six conics nor asserts that such arrangements exist.

## Assumptions and scope
Work throughout over \(\mathbb C\). Let \(f\) be a reduced homogeneous equation for the union, of degree \(d=2k\). Put \(r=\operatorname{mdr}(f)\), the smallest degree of a nonzero relation among the three partial derivatives of \(f\). For a nearly free curve, the standard numerical identity in [1, Definition 1.3] is
\[
\tau(\mathcal C)=(d-1)^2-r(d-r-1)-1,
\]
where \(\tau\) is the total Tjurina number; the syzygy exponents give \(r\le d/2=k\). Let \(n\) count nodes, \(s\) tacnodes, \(q\) ordinary triple points, \(u\) singularities of type \(A_5\), and \(v\) singularities of type \(A_7\). All these quantities are nonnegative integers. The local Tjurina contributions are, respectively, \(1,3,4,5,7\).

The two nontrivial inputs already established in the literature are: (i) Pokora's \(k\le8\) necessary bound and the Dimca--Sernesi estimate \(r\ge\alpha_{\mathcal C}d-2\) in [1, Theorem 2.3 and Remark 2.7]; (ii) Zieliński's orbifold BMY inequality [2, Theorem 1.1]. They apply to exactly the above collection of conic arrangements. Each prescribed singularity has log canonical threshold at least \(5/8\), hence \(\alpha_{\mathcal C}\ge5/8\). The tacnode variable \(s\) is denoted \(t_3\) in [1] and \(t_2\) in [2]; both mean the number of \(A_3\) points.

## Proof
Suppose \(\mathcal C\) is nearly free and has at least seven conics. By [1, Remark 2.7], we may assume \(k\in\{7,8\}\). From the Dimca--Sernesi lower bound and near-freeness we obtain
\[
 k\ge r\ge (5/8)(2k)-2=5k/4-2.
\]
For \(k=7\) the right-hand side is \(27/4\), and for \(k=8\) it is \(8\). Since \(r\) is integral, necessarily \(r=k\) in both cases. Substituting in the nearly-free Tjurina identity gives
\[
 \tau(\mathcal C)=(2k-1)^2-k(k-1)-1=3k(k-1).
\]
Write \(K=k(k-1)\). Pairwise Bézout counting and the preceding Tjurina identity are
\[
\begin{aligned}
2K&=n+2s+3q+3u+4v,\\
3K&=n+3s+4q+5u+7v.
\end{aligned}
\]
Their difference yields \(K=s+q+2u+3v\). Eliminating \(q\) and \(n\) gives two useful identities,
\[
q=u+2v-n,\qquad 3u+5v=K+n-s.
\]
Zieliński's theorem [2, Theorem 1.1], with its tacnode notation translated, asserts
\[
560k+100n+75q\ge184s+404u+608v.
\]
Insert \(q=u+2v-n\) to obtain
\[
560k+25n\ge184s+329u+458v.
\]
Using the other identity to eliminate \(v\), multiply by five and rearrange. This gives the **necessary nonnegative-integer inequality**
\[
\boxed{271u+333n+462s\le2800k-458k(k-1).}\tag{*}
\]
For \(k=8\) the right-hand side is \(-3248\), while the left-hand side is nonnegative: contradiction.

For \(k=7\), inequality \((*)\) reads \(271u+333n+462s\le364\). Hence \(s=0\), and the only possible pairs \((u,n)\) are \((0,0),(1,0),(0,1)\). The exact Bézout--Tjurina identity above becomes
\[
3u+5v=42+n.
\]
Reducing modulo five yields \(3u\equiv42+n\pmod5\), but this fails for each of the three allowed pairs: their residues \(3u\pmod5\) are \(0,3,0\), whereas \((42+n)\pmod5\) are \(2,2,3\). This is another contradiction. Consequently the original assumption \(k\ge7\) is impossible, proving \(k\le6\). \(\square\)

## Verification
The certificate is the exact algebraic elimination leading to \((*)\) and the three-case modular contradiction for \(k=7\). These steps prove the assertion for all arrangements in the stated domain without sampling curves.

Run the self-contained standard-library script with `python3 verify_cutoff.py`. It independently enumerates all nonnegative weak singularity-count vectors satisfying the Bézout equation, required nearly-free Tjurina value, and Zieliński inequality for \(k=7,8\), and checks the explicit arithmetic obstruction. Expected terminal marker: `CONIC_CEILING_EXACT_OK`. The finite census is exhaustive **only of the necessary integer weak-combinatorics** for these two component counts; it is not a general classification of geometric realizability or a substitute for the analytic proof.

## Relationship to prior work
Pokora [1, Remark 2.7] proved a bound of eight conics for precisely this near-freeness class and explicitly noted the lack of examples at \(k=5,6,7,8\). Zieliński [2, Theorem 1.1] independently proved the orbifold inequality for the same five singularity types, but did not make the above near-freeness exclusion. Their conjunction alone does not transparently state the result: the new observation is the forced equality \(r=k\) at seven and eight conics, the elimination \((*)\), and the final modulo-five obstruction that removes the borderline seven-conic case.

Bromboszcz--Jarosławski--Pokora [3, Theorem 3.4] subsequently obtained another Hirzebruch-type inequality \(32k+4n+3q\ge10s+20u+29v\) when restricted to this singularity class. It concerns a broader plus-one-generated framework and is not asserted here as the new argument; the decisive numerical coefficient in \((*)\) comes from the sharper applicable inequality in [2]. The 2026 inequality by itself does not eliminate every numerically conceivable seven-conic nearly-free weak type.

The result concerns **only pure smooth-conic arrangements** with the listed ADE types. Earlier conclusions on conic-line arrangements, arbitrary conic pencils with higher multiplicities, or free (as opposed to nearly free) curves do not subsume it.

## Limitations
The result is a necessary bound, not a sharp existence theorem: the cases of five and six smooth conics are left open. Other singularity types, singular irreducible components, and mixed conic-line arrangements are excluded from the hypotheses. The proof relies on the stated published theorems of Pokora, Dimca--Sernesi and Zieliński. An unindexed equivalent proof in other literature is a remaining priority risk; the research comparison does not establish absolute uniqueness. No independent external validation is claimed.

## References
[1] P. Pokora, *On free and nearly free arrangements of conics admitting certain ADE singularities*, arXiv:2303.08584 (public v1 March 15, 2023); Annali dell'Università di Ferrara **70** (2024), 593--606. https://arxiv.org/html/2303.08584v5 ; https://doi.org/10.1007/s11565-023-00481-6 . Relevant: Definition 1.3, Assumption 1.6, Theorem 2.3, Remark 2.7.

[2] M. Zieliński, *On plane conic arrangements with A5 and A7 singularities*, Rendiconti del Circolo Matematico di Palermo **73** (2024), 57--63 (first published May 17, 2023). https://doi.org/10.1007/s12215-023-00890-8 . Relevant: Bézout identity (1), Theorem 1.1.

[3] A. Bromboszcz, B. Jarosławski, P. Pokora, *On plus-one generated arrangements of plane conics*, Geometriae Dedicata **220** (2026), article 10. https://doi.org/10.1007/s10711-025-01063-w . Relevant: Theorem 3.4.
