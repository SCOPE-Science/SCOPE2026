# Complete \(S_n\)-homology representations of two-subset Kneser neighborhood complexes

## Finding
For every integer \(n\ge4\), let \(G_n=\operatorname{KG}(n,2)\) be the graph whose vertices are the two-element subsets of \([n]\), with two vertices adjacent precisely when they are disjoint. Let \(X_n=\mathcal N(G_n)\) be its ordinary *open-neighborhood complex*: a set of graph vertices spans a simplex if the vertices have a common neighbor. The group \(S_n\) acts by permuting \([n]\).

Write \(U_n=\ker(\mathbb Q^n\xrightarrow{\mathrm{sum}}\mathbb Q)\) for the standard permutation-augmentation representation, \(\operatorname{sgn}_n\) for the sign representation, and \(S^{(n-2,2)}\) for the rational Specht module of the indicated two-row partition. Then
\[
\boxed{\widetilde H_{n-4}(X_n;\mathbb Q)\cong_{\mathbb Q[S_n]}\operatorname{sgn}_n\otimes\left(\bigwedge^2 U_n\oplus S^{(n-2,2)}\right).}
\]
All other reduced rational homology groups vanish. Equivalently, for any \(\sigma\in S_n\), if \(f\) is the number of fixed elements of \([n]\), then
\[
\boxed{\operatorname{tr}\!\left(\sigma\mid\widetilde H_{n-4}(X_n;\mathbb Q)\right)=\operatorname{sgn}(\sigma)\left(f^2-3f+1\right).}
\]
Thus the complete character depends only on permutation parity and its number of fixed ground elements. It has dimension \(n^2-3n+1\), and there is no nonzero \(S_n\)-invariant reduced rational homology class.

## Assumptions and scope
The graph is the ordinary loopless Kneser graph of two-subsets and the complex uses **open**, not closed, neighborhoods. The domain is all integers \(n\ge4\), including the disconnected zero-dimensional case \(n=4\). Each simplex \(F\) is an edge set of a graph on \([n]\) whose endpoint support \(V(F)\) omits at least two ground vertices, because a common neighbor is precisely a disjoint two-subset. Use the augmented oriented simplicial chain complex with the empty simplex in degree \(-1\). All representation statements are over \(\mathbb Q\); integral representations and equivariant homotopy type are not asserted.

## Proof
**1. The existing homology-concentration input.** Nilakantan and Singh, Theorem 1.3 [1], prove that, for \(k\ge0\), the open-neighborhood complex of their \(\operatorname{KG}_{2,k}\), namely the two-subset Kneser graph on \(k+4\) ground elements, is homotopy equivalent to a wedge of \(k^2+5k+5\) spheres of dimension \(k\). Substituting \(k=n-4\) gives
\[
X_n\simeq\bigvee^{n^2-3n+1}S^{n-4}.
\]
The prior result is nonequivariant; we use it only to concentrate the reduced homology in one degree. The symmetry character is established independently below.

**2. Exact signed chain trace.** Fix \(\sigma\in S_n\), with \(c\) cycles on \([n]\), of which \(f\) are fixed-point cycles. The permutation induces an action on the graph vertices, which are the \(\binom n2\) unordered ground-element pairs. An invariant simplex is a union of complete orbits of pairs. In the alternating trace of the **augmented** oriented chain complex, a selected orbit containing \(r\) pair-vertices contributes the factor \((-1)^r(-1)^{r-1}=-1\) to \((-1)^{|F|}\operatorname{sgn}(\sigma|_F)\). Consequently the reduced Lefschetz number equals
\[
\widetilde L(\sigma)=-\sum_{F\in X_n,\ \sigma F=F}(-1)^{\#\text{selected pair-orbits}},
\]
where \(F=\varnothing\) is included in the sum. This is an equality of finite signed traces, not an assumption about fixed geometric points.

**3. Möbius cancellation on vertex cycles.** Let \(\mathscr C\) be the set of the \(c\) disjoint cycles of \(\sigma\). For \(S\subseteq\mathscr C\), write \(B_S\subseteq[n]\) for the union of its cycles, and \(f_S\) for the number of singleton cycles in \(S\). Define \(a(S)\) as the signed sum above restricted to invariant pair-edge sets whose endpoint support is **exactly** \(B_S\). For the cumulative sum over support contained in \(B_S\), selecting any pair-orbit inside \(\binom{B_S}2\) gives a factor \(1-1\). It follows that
\[
\sum_{T\subseteq S}a(T)=\begin{cases}1,&|B_S|\le1,\\0,&|B_S|\ge2.\end{cases}
\]
Möbius inversion on the Boolean lattice of vertex cycles therefore gives the exact identity
\[
a(S)=\sum_{T\subseteq S}(-1)^{|S|-|T|}\mathbf 1_{\{|B_T|\le1\}}=(-1)^{|S|}(1-f_S).
\]
This step covers cycles of every length and uses no genericity assumption on \(\sigma\).

**4. The two missing ground elements.** Because \(n\ge4\), the sum \(\sum_{S\subseteq\mathscr C}a(S)\) vanishes: it is the signed sum over all pair-orbit choices, and at least one pair-orbit exists. A simplex of \(X_n\) must have endpoint support of cardinality at most \(n-2\). The excluded cycle subsets, whose support omits at most one ground element, are exactly \(S=\mathscr C\), together with \(S=\mathscr C\setminus\{C_i\}\) for each singleton ground-element cycle \(C_i\). Their signed sum is
\[
\begin{aligned}
E(\sigma)&=(-1)^c(1-f)+f(-1)^{c-1}(2-f)\\
&=(-1)^c(f^2-3f+1).
\end{aligned}
\]
The admissible signed sum is \(-E(\sigma)\). From the minus sign in the augmented chain Lefschetz formula, \(\widetilde L(\sigma)=E(\sigma)\). By Step 1 the only reduced homology is in degree \(n-4\), so the Hopf trace identity yields
\[
\operatorname{tr}(\sigma\mid\widetilde H_{n-4})=(-1)^{n-4+c}(f^2-3f+1)=\operatorname{sgn}(\sigma)(f^2-3f+1),
\]
since \(\operatorname{sgn}(\sigma)=(-1)^{n-c}\).

**5. Identifying the rational module.** Let \(t\) be the number of two-cycles in \(\sigma\). The permutation representation \(\mathbb Q^n\) has character \(f\), and its augmentation summand \(U_n\) has character \(f-1\). Therefore
\[
\chi_{\bigwedge^2U_n}(\sigma)=\frac{(f-1)^2-(f+2t-1)}2.
\]
The two-subset permutation module is \(\mathbb Q^{\binom{[n]}2}\cong\mathbf1\oplus U_n\oplus S^{(n-2,2)}\) for every \(n\ge4\). It has character \(\binom f2+t\), whence
\[
\chi_{S^{(n-2,2)}}(\sigma)=\binom f2+t-f.
\]
Adding the last two equations gives \(f^2-3f+1\). Tensoring with \(\operatorname{sgn}_n\) matches the previously computed homology character on every permutation. The rational group algebra of \(S_n\) is semisimple, and all its irreducible ordinary Specht representations are defined over \(\mathbb Q\), so equality of characters proves the displayed representation isomorphism. Neither summand is the sign representation before twisting, for \(n\ge4\); hence there is no trivial constituent after twisting. The dimensions \(\binom{n-1}{2}\) and \(n(n-3)/2\) sum to \(n^2-3n+1\), checking the identity trace. This completes the proof.

## Verification
Run `python3 verify_kneser_character.py` using Python 3 standard library only. Its independent routines enumerate invariant pair-orbit selections for a representative of every conjugacy class of \(S_n\), \(4\le n\le7\), and compare the resulting augmented-chain Lefschetz numbers with the theorem. For \(4\le n\le6\), a second routine separately enumerates every labeled edge subset, directly tests its invariant face condition and calculates its oriented simplex permutation sign, without using the edge-orbit recurrence. The script also checks the two constituent character identities and dimension formulas. The 38 conjugacy-class tests pass. These are finite consistency checks; the arbitrary-\(n\) statement rests on Steps 1–5 above.

## Relationship to prior work
Nilakantan and Singh [1, Theorem 1.3] give the homotopy type and the rank \(n^2-3n+1\) but do not describe the \(S_n\)-action. Their separate work [2] on three-subset Kneser graphs addresses a different family and gives nonequivariant homotopy. Schultz [3] studies the smaller **stable** Kneser graphs under natural dihedral actions rather than the full \(S_n\)-action on the ordinary graph. A previously reported six-point calculation [4] already gives the two constituents \(S^{(3,1,1,1)}\oplus S^{(2,2,1,1)}\); that isolated \(n=6\) specialization is **not claimed to be new**. At \(n=6\), the present uniform formula specializes to precisely those constituents. The new assertion is the explicit all-parameter character and rational module decomposition, including arbitrary \(n\ge7\). The different bounded-vertex-cover graph complexes of Jonsson [5] allow graph edge sets with two independent vertices but not necessarily two isolated vertices, so those objects do not have the face condition used here.

## Limitations
The argument requires the published nonequivariant sphere-wedge classification [1]; it does not independently reprove that classification or supply an explicit integral \(S_n\)-lattice, a preferred top-homology basis, or an equivariant homotopy equivalence. Equality of rational characters does not imply an integral representation isomorphism. An equivalent all-parameter character in unindexed prior work cannot be excluded by finite search. The exact \(n=6\) case has already been separately reported [4].

## References
1. N. Nilakantan and A. Singh, *Homotopy Type of Neighborhood Complexes of Kneser Graphs, \(KG_{2,k}\)*, arXiv:1802.05848v1, publicly dated 2018-02-16, especially Theorem 1.3 and Section 5. https://arxiv.org/abs/1802.05848
2. N. Nilakantan and A. Singh, *Neighborhood Complexes of Kneser Graphs, \(KG_{3,k}\)*, arXiv:1807.11732v1, publicly dated 2018-07-31. https://arxiv.org/abs/1807.11732
3. C. Schultz, *The Equivariant Topology of Stable Kneser Graphs*, arXiv:1003.5688v1, 2010-03-29. https://arxiv.org/abs/1003.5688
4. *Rational symmetry decomposition of the Kneser neighborhood complex on six points*, published mathematical-result record (opaque identifier `6890383e239b`), 2026.
5. J. Jonsson, *Simplicial Complexes of Graphs and Hypergraphs with a Bounded Covering Number*, SIAM J. Discrete Math. 19 (2005), 633–650, DOI:10.1137/S0895480104443680.
