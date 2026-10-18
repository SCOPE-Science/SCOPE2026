# Duality-twisted homology characters of all Kneser neighborhood complexes

## Finding
For integers \(k\geq1\) and \(n\geq2k\), let \(G=\mathrm{KG}(n,k)\), whose vertices are the \(k\)-subsets of \([n]\), with disjointness adjacency, and let \(X=\mathcal N(G)\) be the **open** neighborhood complex. Set \(r=n-2k\). The natural coordinate-permutation action of \(\mathfrak S_n\) on \(\widetilde H_r(X;\mathbb Q)\) commutes with the homological involution \(c_*\) induced by the Lovász neighborhood duality operator. The resulting \(\mathfrak S_n\times C_2\) character is completely determined by the following two formulas.

For \(\sigma\in\mathfrak S_n\), the untwisted character is
\[
 \operatorname{tr}(\sigma\mid\widetilde H_r(X;\mathbb Q))
 =\sum_{j=1}^{k}\chi^{(2k-j,j,1^r)}(\sigma),
\]
where \(\chi^\lambda\) denotes the irreducible symmetric-group character of partition \(\lambda\), and \(1^0\) indicates an empty tail. Thus the ordinary action is multiplicity-free, with exactly \(k\) constituents.

To specify the **duality-twisted** character, write the even cycles of \(\sigma\) as having lengths \(2w_1,\ldots,2w_e\), and let \(\delta_\sigma=1\) if **every** cycle of \(\sigma\) is even, and \(0\) otherwise. Define the finite poset \(Q_{\sigma,k}\) of strings \(a\in\{0,+,-\}^e\) of weight \(\mathrm{wt}(a)=\sum_{i:a_i\ne0}w_i\) satisfying \(k\leq\mathrm{wt}(a)<n/2\). It is ordered coordinatewise by \(0<+\), \(0<-\), with \(+\) and \(-\) incomparable. Define the finite poset \(B_{\sigma,k}\) of subsets \(I\subseteq[e]\) for which \(k\leq\sum_{i\in I}w_i<n/2\), ordered by inclusion. For any finite poset \(P\) put \(\chi(P)=\sum_{m\geq1}(-1)^{m-1}c_m(P)\), where \(c_m(P)\) is the number of strict \(m\)-element chains and \(\chi(\varnothing)=0\). Then
\[
 \boxed{\operatorname{tr}(c_*\sigma\mid\widetilde H_r(X;\mathbb Q))
 =(-1)^r\left[-1+\chi(Q_{\sigma,k})
 +\delta_\sigma2^e\bigl(1-\chi(B_{\sigma,k})\bigr)\right].}
\]
The formula involves at most \(3^e\) signed-half-cycle configurations, rather than the faces of the original (potentially enormous) neighborhood complex. In particular, for \(\sigma=1\),
\[
 \operatorname{tr}(c_*\mid\widetilde H_r(X;\mathbb Q))=(-1)^{r+1}.
\]
Consequently, if \(b=\dim_{\mathbb Q}\widetilde H_r(X;\mathbb Q)\), the positive and negative eigenspaces of duality have dimensions \(\bigl(b+(-1)^{r+1}\bigr)/2\) and \(\bigl(b-(-1)^{r+1}\bigr)/2\), respectively. All other reduced rational homology groups vanish. The preceding equations specify the character for every element of \(\mathfrak S_n\times C_2\).

## Assumptions and scope
The theorem concerns finite simple Kneser graphs with \(k\ge1\), \(n\ge2k\), the ordinary open neighborhood complex (not its clique complex), and **reduced rational** homology. The case \(r=0\) means reduced zeroth homology. The duality operator is **not** asserted to be a permutation of Kneser-graph vertices. Instead, for every nonempty face \(F\) of \(X\) it sends \(F\) to the common-neighbor face \(N(F)\), reversing inclusion; it induces a simplicial self-map on the barycentric subdivision, hence a well-defined map on homology. Its square is homotopic to the identity in this setting.

## Proof
**Step 1 (canonical Boolean model and duality).** A nonempty collection \(F\) of \(k\)-subsets is a face of \(X\) exactly when \(k\leq|\bigcup F|\leq n-k\). Write \(F_U\) for the family of all \(k\)-subsets contained in a fixed \(U\subseteq[n]\), \(k\leq|U|\leq n-k\). The common-neighbor map satisfies \(N(F)=F_{[n]\setminus\bigcup F}\) and \(N^2(F)=F_{\bigcup F}\). Thus \(N^2\) is an ascending closure operator on the face poset, with image the subposet of all \(F_U\). Its barycentric subdivision is homotopy equivalent to \(X\), with an \(\mathfrak S_n\)-equivariant equivalence. On this image, the map \(N\) becomes the order-reversing involution \(U\mapsto U^c\), and it commutes with \(\mathfrak S_n\). Therefore the full homological action is the action of coordinate permutations and complementation on the order complex \(\Delta P_{n,k}\), where \(P_{n,k}=\{U\subseteq[n]:k\leq|U|\leq n-k\}\).

**Step 2 (homology concentration and untwisted character).** The poset \(P_{n,k}\) is a consecutive-rank selection of the Boolean lattice with \(r+1\) ranks. Rank-selected Boolean shellability gives reduced homology only in degree \(r\), free integrally. In the rational representation ring, the alternating augmented chain complex has Frobenius characteristic
\[
 \sum_{\beta\succeq(k,1^r,k)}(-1)^{r+2-\ell(\beta)}h_{\beta_1}\cdots h_{\beta_{\ell(\beta)}},
\]
where \(\beta\) runs over coarsenings (merging adjacent parts) of the indicated composition. This is the classical ribbon Schur characteristic \(s_{(k,1^r,k)}\). The Littlewood–Richardson/Pieri expansion for this two-long-row ribbon is
\[
 s_{(k,1^r,k)}=\sum_{j=1}^{k}s_{(2k-j,j,1^r)}.
\]
One way to verify the identity is to apply the skew Jacobi–Trudi determinant and Pieri's horizontal-strip rule: the alternating coarsenings cancel except the two-row heads \((2k-j,j)\) followed by \(r\) singleton rows, each with coefficient one. The complete-homogeneous expansion and its cancellation can also be checked by the included standalone verifier. This proves the untwisted character for all parameters; finite checks are corroboration, not its proof.

**Step 3 (classification of fixed chains under duality).** Let \(t\geq1\). A simplex of \(\Delta P_{n,k}\) is a strict chain \(U_1\subset\cdots\subset U_t\). Applying \(c\sigma\) reverses its order. If the simplex is preserved setwise, then \((c\sigma)^2=\sigma^2\) fixes each member, and \(U_i=c\sigma(U_{t+1-i})\). Orientation reversal on an invariant chain has sign \((-1)^{t(t-1)/2}\).

For even \(t=2m\), the lower half of the chain is a strict \(m\)-chain of sets \(A\) with \(k\leq|A|<n/2\), invariant under \(\sigma^2\), and satisfying \(A\cap\sigma(A)=\varnothing\). On an odd cycle of \(\sigma\), such a set contains nothing. On an even cycle of length \(2w_i\), it contains either neither parity orbit or exactly one of the two \(\sigma^2\)-orbits of size \(w_i\). Therefore the number of invariant \(2m\)-chains equals \(c_m(Q_{\sigma,k})\).

For odd \(t=2m+1\), there must additionally be a central set \(M=c\sigma(M)\). Such a set exists exactly when all \(\sigma\)-cycles are even, and then there are \(2^e\) choices of \(M\), one parity orbit on each cycle. Below each \(M\), a lower chain is exactly an \(m\)-chain in the weighted Boolean subposet \(B_{\sigma,k}\). For \(m=0\), the empty lower chain is counted once per central set.

**Step 4 (oriented Lefschetz signs).** The reduced Lefschetz number includes the augmented empty-chain contribution \(-1\). Summing \((-1)^{t-1+t(t-1)/2}\) over invariant \(t\)-chains gives
\[
 \widetilde L(c\sigma)=-1+\sum_{m\ge1}(-1)^{m+1}c_m(Q_{\sigma,k})
 +\delta_\sigma2^e\sum_{m\ge0}(-1)^m c_m(B_{\sigma,k}),
\]
with \(c_0(B)=1\). By definition of \(\chi\), this simplifies to the bracketed formula in the finding. Homology is concentrated in degree \(r\), hence \(\widetilde L(c\sigma)=(-1)^r\operatorname{tr}(c\sigma\mid\widetilde H_r)\), proving the claimed character. For \(\sigma=1\) there are no even cycles, so both posets are empty and \(\delta_\sigma=0\), giving the stated duality trace and eigenspace dimensions.

## Verification
Run `python3 verify.py` using Python's standard library. The verifier independently constructs the actual rank-selected Boolean order complexes and enumerates **every** conjugacy class of \(\mathfrak S_n\) for parameter pairs \((n,k)=(4,2),(5,2),(6,2),(7,3),(8,3),(9,4)\), totaling 90 cases. It computes oriented fixed chains of \(c\sigma\) directly, without using the weighted-poset counting method, and compares all traces. It also expands the relevant ribbon characteristics in the Schur basis independently via Pieri's horizontal-strip rule for 25 additional parameter pairs. The expected terminal output is `VERIFY_OK 90` and `RIBBON_OK 25`. At \((n,k)=(9,4)\), the four ordinary irreducible dimensions are \(28,105,162,84\) and the duality trace is \(+1\); for \(\sigma\) of cycle type \((2,2,2,2,1)\), the duality-twisted trace is \(-15\). The finite program does **not** replace the all-parameter proofs in Steps 1–4.

## Relationship to prior work
Kozlov's *Combinatorial Algebraic Topology* (2008), especially Proposition 17.28 and the neighborhood involution discussion in Section 17.3, already constructs the rank-selected Boolean model and proves the nonequivariant wedge-of-spheres homotopy type. These are not new claims. The classical theory of ribbon Schur functions, including McNamara and van Willigenburg's multiplicity-free ribbon classification, accounts for the ordinary symmetric-group part. Nilakantan and Singh treat the ordinary homotopy types of the two- and three-subset Kneser families. The distinctive result here is the **simultaneous mixed trace of every coordinate permutation composed with neighborhood duality**, computed by the even-cycle weighted-poset formula, including the nonidentity mixed elements invisible to ordinary Betti numbers and ordinary \(\mathfrak S_n\)-characters. The result is not a classification of graph automorphisms or of all graph-Hom symmetries.

## Limitations
Only the rational homology **character** of the canonical duality action is classified, not an explicit integral decomposition into \(\mathfrak S_n\times C_2\) lattices or an equivariant homotopy equivalence for arbitrary additional symmetries. The formula is a finite exact combinatorial expression, not a closed polynomial in a fixed number of short-cycle counts. The exterior literature comparison has residual risk from less-indexed publications on equivariant poset topology. Independent audit has not been performed.

## References
1. D. Kozlov, *Combinatorial Algebraic Topology*, Springer, 2008, Section 17.3, especially Propositions 17.23, 17.25, and 17.28; lawful author-hosted PDF: https://webhomes.maths.ed.ac.uk/~v1ranick/papers/kozlov.pdf .
2. P. R. W. McNamara and S. van Willigenburg, *Positivity results on ribbon Schur function differences*, European Journal of Combinatorics 30 (2009), 1352–1369; original preprint arXiv:0712.2424 (2007-12-14), https://arxiv.org/abs/0712.2424 .
3. N. Nilakantan and A. Singh, *Homotopy Type of Neighborhood Complexes of Kneser Graphs*, arXiv:1802.05848 (2018-02-16), https://arxiv.org/abs/1802.05848 .
4. N. Nilakantan and A. Singh, *Neighborhood Complexes of Kneser Graphs*, arXiv:1807.11732 (2018-07-31), https://arxiv.org/abs/1807.11732 .
