# Uniform symmetric-group characters of Kneser neighborhood homology

## Finding
For every integer \(n\ge7\), consider the ordinary open-neighborhood complex \(K_n=\mathcal N(\mathrm{KG}(n,2))\) of the Kneser graph on unordered pairs of the ground set \([n]=\{1,\ldots,n\}\). The natural coordinate action of \(S_n\) has **the following complete rational homology character**:
\[
\boxed{\operatorname{tr}\!\left(\sigma\mid\widetilde H_{n-4}(K_n;\mathbb Q)\right)
=\operatorname{sgn}(\sigma)\left(f_1(\sigma)^2-3f_1(\sigma)+1\right),}
\]
where \(f_1(\sigma)=|\{i\in[n]:\sigma(i)=i\}|\). All other reduced rational homology is zero. Equivalently, as rational representations,
\[
\boxed{\widetilde H_{n-4}(K_n;\mathbb Q)
\cong S^{(2,2,1^{n-4})}\oplus S^{(3,1^{n-3})}.}
\]
Here \(S^\lambda\) denotes the Specht representation indexed by a partition \(\lambda\) of \(n\). The respective dimensions are \(n(n-3)/2\) and \((n-1)(n-2)/2\), totaling \(n^2-3n+1\). In particular no nonzero rational class is fixed by \(S_n\) or its alternating subgroup \(A_n\).

## Assumptions and scope
All graphs are finite and simple. A simplex of the open-neighborhood complex is a finite set of graph vertices admitting at least one common graph neighbor. Thus its nonempty simplices are collections \(F\) of two-element subsets of \([n]\) whose endpoint union misses **at least two** ground points. Equivalently, \(F\) is the edge set of a simple graph on \([n]\) having at least two isolated vertices. The empty face is retained in the augmented simplicial chain complex. The action permutes ground-point labels, hence the two-element subsets and oriented simplices. Coefficients in the representation theorem are rational; the known underlying homotopy type is an integral statement. The new theorem covers every \(n\ge7\), not an extrapolation from finitely many examples.

Nilakantan and Singh proved that for every integer \(n\ge4\) this complex is homotopy equivalent to a wedge of \(n^2-3n+1\) spheres of dimension \(n-4\) (their parameter is \(k=n-4\)); that previously known theorem supplies homology concentration. This work does **not** claim the wedge decomposition as new and does not posit an equivariant homotopy equivalence.

## Proof
**Step 1: augmented Lefschetz trace.** Fix \(n\ge7\) and \(\sigma\in S_n\). Let \(c=c(\sigma)\) be its number of cycles on \([n]\), including fixed points, and let \(f=f_1(\sigma)\). A face \(F\) is fixed setwise by \(\sigma\) exactly when it is a union of orbits of \(\sigma\) on the ground-pair set \(E=\binom{[n]}2\). If \(q(F)\) is its number of selected pair-orbits, then the signed contribution of \(F\) to the augmented simplicial Euler trace is \(-(-1)^{q(F)}\), including the empty face: for a nonempty face with \(|F|=m\), the permutation sign on its oriented \((m-1)\)-simplex is \((-1)^{m-q(F)}\), while the chain-degree sign is \((-1)^{m-1}\). Therefore
\[
\widetilde L(\sigma)=-\sum_{\substack{F=\sigma F\\|I(F)|\ge2}}(-1)^{q(F)},
\]
where \(I(F)=[n]\setminus\bigcup_{e\in F}e\) is the set of isolated ground vertices. No equivariant Morse collapse is presumed.

**Step 2: count exactly zero or one isolated vertex.** For each \(\sigma\)-invariant subset \(U\subseteq[n]\), set
\[
g(U)=\sum_{\substack{F=\sigma F\\U\subseteq I(F)}}(-1)^{q(F)}.
\]
The permitted edges are exactly the pairs contained in \([n]\setminus U\), and every orbit of such pairs may be selected independently. Consequently \(g(U)=(1-1)^t\), where \(t\) counts these pair-orbits. Explicitly, \(g(U)=1\) when \(|[n]\setminus U|\le1\) and \(g(U)=0\) otherwise. Let
\[
h(W)=\sum_{\substack{F=\sigma F\\I(F)=W}}(-1)^{q(F)}
\]
for a \(\sigma\)-invariant subset \(W\). Inversion on the Boolean lattice of the \(c\) ground-set cycles (not on all subsets) gives
\[
h(\varnothing)=(-1)^c(1-f).
\]
For a singleton \(\{i\}\) fixed by \(\sigma\), the only invariant supersets \(U\supseteq\{i\}\) with \(g(U)\ne0\) are all of \([n]\), and \([n]\setminus\{j\}\) for each of the \(f-1\) other fixed points \(j\). Thus
\[
h(\{i\})=(-1)^{c-1}(2-f).
\]
The sum of \((-1)^{q(F)}\) over *all* \(\sigma\)-invariant edge sets \(F\) is zero because \(E\ne\varnothing\). Subtracting the excluded cases of zero or one isolated vertex from this zero sum, and substituting into the augmented Lefschetz trace, yields
\[
\widetilde L(\sigma)=h(\varnothing)+\sum_{\sigma(i)=i}h(\{i\})
=(-1)^c(f^2-3f+1).
\]
This identity is symbolic and valid for every \(n\ge2\), independently of any numerical enumeration.

**Step 3: isolate the actual homology.** The cited non-equivariant homotopy theorem gives reduced homology only in degree \(n-4\). The augmented Hopf trace theorem therefore gives
\[
\widetilde L(\sigma)=(-1)^{n-4}
\operatorname{tr}(\sigma\mid\widetilde H_{n-4}(K_n;\mathbb Q)).
\]
Because \(\operatorname{sgn}(\sigma)=(-1)^{n-c}\), the claimed homology character follows, for every permutation and every \(n\ge7\).

**Step 4: identify both irreducibles.** The permutation representation on \(n(n-1)\) ordered pairs of distinct ground points has character \(f(f-1)\). For \(n\ge4\), Young's rule decomposes it as
\[
\mathbb Q[\{(i,j):i\ne j\}]
\cong\mathbf1\oplus2S^{(n-1,1)}\oplus S^{(n-2,2)}\oplus S^{(n-2,1,1)}.
\]
The point-permutation module is \(\mathbf1\oplus S^{(n-1,1)}\), so the sum of the last two characters is \(f(f-1)-2f+1=f^2-3f+1\). Tensoring with the sign representation transposes Specht diagrams: \(S^{(n-2,2)}\otimes\operatorname{sgn}\cong S^{(2,2,1^{n-4})}\) and \(S^{(n-2,1,1)}\otimes\operatorname{sgn}\cong S^{(3,1^{n-3})}\). Semisimplicity of rational symmetric-group representations establishes the displayed isomorphism. Both partitions differ from \((n)\) and \((1^n)\) for \(n\ge7\); hence the representation has neither trivial nor sign summands. Taking \(A_n\)-invariants agrees with testing these two one-dimensional constituents, proving the final assertion.

## Verification
The complete all-\(n\) proof is the alternating orbit-sum and cycle-lattice inversion above, coupled to the published homotopy theorem; it does not rely on any finite pattern. Run `python3 verify.py` using the Python standard library. This standalone program independently enumerates every edge-orbit selection for each permutation cycle type at \(n=4,5,6,7\), checks its valid-face criterion directly, computes the augmented signed Euler trace, and compares the result to the closed formula and to the two Specht character polynomials. The checks cover all \(5,7,11,15\) cycle types respectively and return `VERIFY_OK`; they corroborate but do not replace the symbolic argument. For \(n=7\), the dimension is \(29=14+15\); for \(n=8\), the theorem gives \(41=20+21\).

## Relationship to prior work
Schultz's 2010 work on the *equivariant topology of stable Kneser graphs* motivates asking for permutation-group actions on Kneser-related neighborhood complexes; it addresses **stable** Kneser subgraphs and principally dihedral symmetry, not the full \(S_n\)-homology of ordinary \(\mathrm{KG}(n,2)\). Nilakantan and Singh's 2018 Theorem 1.3 proves the exact wedge-of-spheres homotopy type for this ordinary family, with an explicitly non-equivariant discrete-Morse proof. Their theorem gives the dimension and concentration used here, but not the \(S_n\)-character.

A published finite calculation, *Rational symmetry decomposition of the Kneser neighborhood complex on six points* (2026), determines \(S^{(3,1,1,1)}\oplus S^{(2,2,1,1)}\) at **\(n=6\)**. That case agrees with the uniform expression, is credited and is **excluded from the new theorem's domain**. A fixed case cannot imply the all-size character formula or the two Specht families for \(n\ge7\); the cycle-orbit proof is an independent infinite-family argument. Jonsson's bounded-vertex-cover graph complexes are related but not identical: allowing an independent pair of ground vertices does not require them both to be isolated in the edge-set graph. No result about that distinct complex is transferred without proof.

## Limitations
Only the action on rational homology is classified. An integral \(\mathbb Z[S_n]\)-lattice decomposition, an equivariant homotopy classification, and explicit geometric bases of homology are not supplied. The symbolic trace calculation is valid without the published homotopy theorem, but the deduction of a **single** homology representation uses that theorem. The closest finite \(n=6\) representation is previously published; it is not a separate new claim. More general or differently named literature might independently imply this character, and an inaccessible full text on bounded-cover complexes was not certified as not covering the result. Independent scientific validation has not been performed.

## References
1. C. Schultz, *The Equivariant Topology of Stable Kneser Graphs*, arXiv:1003.5688v1, posted 2010-03-29. https://arxiv.org/abs/1003.5688
2. N. Nilakantan and A. Singh, *Homotopy Type of Neighborhood Complexes of Kneser Graphs, KG_{2,k}*, arXiv:1802.05848v1, posted 2018-02-16, Theorem 1.3. https://arxiv.org/abs/1802.05848
3. *Rational symmetry decomposition of the Kneser neighborhood complex on six points*, public finite-case calculation (2026-10-11), published-finding corpus record `2026/10/11/SCOPE-rational-symmetry-decomposition-of-the-kneser-neighborhood-compl--6890383e239b`.
4. J. Jonsson, *Simplicial Complexes of Graphs and Hypergraphs with a Bounded Covering Number*, SIAM J. Discrete Math. 19 (2005), 633–650, DOI:10.1137/S0895480104443680.
