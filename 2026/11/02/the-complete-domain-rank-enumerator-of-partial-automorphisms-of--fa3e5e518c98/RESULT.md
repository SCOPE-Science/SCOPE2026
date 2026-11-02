# The complete domain-rank enumerator of partial automorphisms of finite crown posets

## Finding

For each integer \(n\ge2\), write \(\mathcal C_{2n}\) for the finite crown poset on \(V=\mathbb Z/(2n)\mathbb Z\): every even vertex is minimal and lies below exactly its two neighboring odd vertices; there are no other strict comparisons. Let \(\mathcal I_n\) be the inverse monoid of all order isomorphisms between two induced subposets, including the empty partial map, and put
\[
R_n(z)=\sum_{f\in\mathcal I_n}z^{|\operatorname{dom}f|}.
\]
All its coefficients admit a finite multivariate coefficient formula, valid uniformly for every \(n\ge2\). Set
\[
E=\sum_{j=1}^{n-1}a_j(xy)^{2j},\qquad
O_p=u xy+\sum_{j=1}^{n-1}b_{j,p}(xy)^{2j+1},\quad p\in\{0,1\},
\]
\[
G_0=\frac{y^2}{1-y^2},\qquad G_1=\frac y{1-y^2},
\]
and introduce a formal \(2\times2\) matrix
\[
M_{pp}=EG_0+O_pG_1,\qquad M_{p,1-p}=EG_1+O_pG_0.
\]
Define the finite polynomial
\[
F_n(x;u,\mathbf a,\mathbf b)
=1+n[y^{2n}]\sum_{t=1}^{n}\frac{\operatorname{tr}(M^t)}t.
\]
Equivalently, in formal power series, \(F_n=1-n[y^{2n}]\log\det(I-M)\). Let \(c_{\mathbf m}\) be the coefficient of
\(u^{m_1}x^k\prod_{j=1}^{n-1}a_j^{e_j}\prod_{j=1}^{n-1}\prod_{p=0}^{1}b_{j,p}^{o_{j,p}}\)
in \(F_n\), with \(k=m_1+\sum_j2je_j+\sum_{j,p}(2j+1)o_{j,p}\). Then
\[
\boxed{R_n(z)=2nz^{2n}+
\sum_{\mathbf m}c_{\mathbf m}^2\,m_1!\,
\prod_je_j!\prod_{j,p}\bigl(2^{o_{j,p}}o_{j,p}!\bigr)z^{k}.}
\]
The sum is over the finite set of occurring monomials, including the constant monomial. In particular,
\[
[z^{2n}]R_n=2n,\quad [z^{2n-1}]R_n=4n^2\quad(n\ge2),
\]
\[
[z^{2n-2}]R_n=n^2(6n-8)\quad(n\ge3).
\]
The last coefficient equals \(24\), rather than the displayed stable formula, when \(n=2\). The monoid orders \(R_n(1)\) at \(n=2,3,4,5,6,7,8\) are
\[
61,\quad571,\quad6889,\quad101041,\quad1723621,\quad33233943,\quad711242001.
\]

## Assumptions and scope

Here \(n\) is an integer at least two. The domain and image of a partial map carry the **induced order** (both preservation and reflection are required); an injective map preserving only existing comparisons is not sufficient. The variable \(x\) marks selected vertices, \(y\) marks all vertices, and \(u,a_j,b_{j,p}\) mark connected-component types. A run is a maximal nonempty string of consecutive selected vertices in the underlying cyclic order. An isolated selected vertex is type \(u\); a run of even length \(2j\) is type \(a_j\); a run of odd length \(2j+1\ge3\) has type \(b_{j,p}\), where \(p=0\) means both endpoints are minimal and \(p=1\) means both endpoints are maximal. The sum defining \(F_n\) includes only proper vertex subsets; the full crown is handled separately.

## Proof

**1. Classification of proper induced subposets.** Every proper subset of the cycle is a disjoint union of runs. Each run is an alternating path poset. A singleton loses its ambient minimal/maximal label because it has no comparable elements. A nontrivial even run is a path of even cardinality with one minimal and one maximal endpoint, and its isomorphism type is independent of initial parity. A nontrivial odd run has both endpoints minimal or both maximal, distinguishing two nonisomorphic types. These are all the connected component types: the comparability graph is exactly the induced path and an isomorphism preserves the bipartition into minimal and maximal vertices on every nonsingleton component.

Each even-length run has one automorphism as a poset: reversal interchanges minimal and maximal elements and hence is forbidden. Each odd-length nonsingleton run has exactly two automorphisms, identity and reversal. A singleton has one. Components of an identical type may be permuted freely; components of distinct types cannot be interchanged. Thus for a profile \(\mathbf m=(m_1,(e_j),(o_{j,p}))\) the number of isomorphisms between **any two fixed** induced subposets of that profile is
\[
A(\mathbf m)=m_1!\prod_je_j!\prod_{j,p}(2^{o_{j,p}}o_{j,p}!).
\]

**2. Enumeration of component profiles on the cycle.** For a proper nonempty subset with \(t\) selected runs, choose a distinguished run start, specify positive run lengths \(r_1,\ldots,r_t\), positive gap lengths \(g_1,\ldots,g_t\), and initial vertex parity. The lengths sum to \(2n\). If a run starts at parity \(p\), then the next starts at parity \(p+r+g\pmod2\). For even runs the weight is \(E\), for odd runs the weight is \(O_p\). The generating functions for positive even and positive odd gaps are respectively \(G_0\) and \(G_1\). Summing over the next start parity gives precisely the matrix \(M\).

The term \(\operatorname{tr}(M^t)\) records all cyclically consistent lists of \(t\) runs and gaps, with the initial start parity distinguished. For each parity there are exactly \(n\) choices of the starting vertex, whereas every nonempty proper subset with \(t\) selected runs has precisely \(t\) possible distinguished runs. Therefore multiplication by \(n/t\) counts each labeled subset once. At most \(n\) runs fit on the \(2n\) vertices, since each needs at least one selected and one omitted vertex. This proves that the coefficient \(c_{\mathbf m}\) in \(F_n\) counts proper induced subposets of profile \(\mathbf m\) exactly. The constant coefficient 1 accounts for the empty subset. The formal log-determinant identity follows from \(-\log\det(I-M)=\sum_{t\ge1}\operatorname{tr}(M^t)/t\), valid here because every entry of \(M\) has positive \(y\)-degree.

**3. Counting partial isomorphisms.** Fix the domain and image component profiles. An isomorphism exists precisely when their profiles agree, and in that case the number of isomorphisms is \(A(\mathbf m)\). There are \(c_{\mathbf m}\) possible domains and independently \(c_{\mathbf m}\) possible images. This yields the finite sum in the theorem. The full domain is necessarily mapped to the entire crown. For \(n\ge3\), its automorphisms are exactly the \(n\) even rotations and \(n\) color-preserving reflections, for a total of \(2n\); at \(n=2\), the full crown is the four-element complete height-two poset, also with \(4=2n\) automorphisms. This proves the formula for every coefficient and all boundary cases.

**4. High-domain-rank coefficients.** The full-domain case gives \(2n\). Deleting an even vertex leaves a path on \(2n-1\) vertices with both endpoints maximal; deleting an odd vertex leaves a path with both endpoints minimal. These are distinct component types, with \(n\) possible domains and \(n\) possible images for each type. Each odd path admits exactly two order automorphisms, identity and reversal, yielding \(2\cdot n^2\cdot2=4n^2\).

For two deleted vertices and \(n\ge3\), classify their cyclic separation by the smaller distance \(d\). An adjacent deletion gives \(2n\) domains of a single even run with no internal symmetry, contributing \(4n^2\). Distance \(d=2\) gives two parity-distinct profiles of \(n\) domains each, with a single odd path whose reversal is allowed, contributing \(4n^2\). For \(3\le d<n\) odd, each profile consists of two unequal even runs, with \(2n\) possible domains and no internal symmetry, contributing \(4n^2\) at that distance. For \(4\le d<n\) even, the omitted pair has common parity, giving two endpoint-color profiles of \(n\) domains each and two odd runs admitting independent reversals; the contribution is \(8n^2\) at that distance. Finally, opposite deletions \(d=n\) contribute \(2n^2\) for odd \(n\), and \(4n^2\) for even \(n\), using the component-swap symmetry when the two remaining runs are isomorphic. Summing these distance classes and adding the adjacent case yields \(n^2(6n-8)\). When \(n=2\), opposite deletions leave two isolated vertices whose additional permutations give the exceptional coefficient \(24\). This completes the proof.

## Verification

The included standalone `verify.py` independently enumerates positive run-gap compositions rather than using the transfer matrix symbolically, and separately examines all proper labeled subsets to check their exact component profiles for \(2\le n\le8\). For \(n=2,3,4\), it also exhaustively checks every partial injection for preservation **and reflection** of each comparison, directly obtaining the entire rank polynomial. It checks high-rank formulas and the displayed total orders. Execute with `python3 verify.py` from the package directory; success prints `VERIFY_OK`. Exhaustive checks for small crowns support but cannot replace the all-\(n\) proof above.

## Relationship to prior work

Dimitrova and Koppitz (2022), arXiv:2204.13961, study precisely the inverse semigroup of partial automorphisms of a finite crown. Their result provides a minimum generating set and the corresponding *semigroup generating rank*. Their membership characterization (Proposition 2.1) is compatible with the present induced-order definition. The result here instead determines the complete distribution of **individual elements by domain cardinality**, hence the monoid order, for all crown sizes. Neither the generating rank nor a characterization of individual admissible maps determines these counts directly.

Dimitrova, Fernandes, Koppitz and Quinteiro (2021), arXiv:2101.12468, calculate cardinalities for partial automorphism monoids of **undirected paths**. Separate known cycle-graph enumerations concern undirected induced-subgraph automorphisms, which allow interchanging the two color classes of a connected path. They cannot be substituted for partial order isomorphisms of the crown: already at rank \(2n-1\), the graph-cycle count is \(8n^2\), while the crown-poset count is \(4n^2\). The present parity-sensitive odd-run inventory is essential. Earlier work does not establish the stated complete crown-poset enumerator on the sources inspected here.

## Limitations

This is a finite exact formula, not an elementary closed form for \(R_n(1)\) in a single exponent. It concerns partial *isomorphisms* between induced subposets, not all order-preserving partial injections, nor general comparability graphs or arbitrary fence/crown variants. The coefficient formula is finite at each \(n\) and the proof applies for every integer \(n\ge2\). Independent mathematical verification and exhaustive priority assessment are not claimed; unlocated general finite-poset inverse-semigroup enumeration principles remain a residual literature risk.

## References

1. I. Dimitrova and J. Koppitz, *The rank of the inverse semigroup of all partial automorphisms on a finite crown* (2022), arXiv:2204.13961, first public April 29, 2022; https://arxiv.org/abs/2204.13961.
2. I. Dimitrova, V. H. Fernandes, J. Koppitz and T. M. Quinteiro, *Partial Automorphisms and Injective Partial Endomorphisms of a Finite Undirected Path* (2021), arXiv:2101.12468; https://arxiv.org/abs/2101.12468.
