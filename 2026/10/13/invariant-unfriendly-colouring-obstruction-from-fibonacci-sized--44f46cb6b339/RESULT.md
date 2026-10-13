# Invariant unfriendly-colouring obstruction from Fibonacci-sized majority fibres
## Finding

There is a **closed, locally finite, bipartite Borel graph** \(G\) on a zero-dimensional Polish space \(Y\) with all components one-ended and with hyperfinite connectedness equivalence relation, such that:

1. every vertex has odd degree at least \(3\), and degree \(3\) occurs; degrees are unbounded in every component;
2. \(G\) preserves an atomless, fully supported Borel **probability measure** \(\nu\), but no \(\nu\)-measurable two-colouring is unfriendly almost everywhere (nor can a Baire measurable colouring be unfriendly on a comeager set);
3. \(\int_Y\deg_G(y)\,d\nu(y)=\infty\);
4. the rank-homogeneous odd fibre multiplicities used below are pointwise minimal among those with leaf multiplicity \(1\), minimum degree at least \(3\), and the **strict-parent-majority certificate** specified below. They grow at the Fibonacci rate \(\Theta(\varphi^k)\), where \(\varphi=(1+\sqrt5)/2\), in place of the cubic-base exponential weights in the reference construction.

In particular, finite average degree is an essential hypothesis in the Conley–Tamuz theorem asserting almost-everywhere Borel unfriendly colourability of probability-measure-preserving, locally finite Borel graphs. This is an existence counterexample under an invariant probability; it does **not** address the bounded-maximum-degree version of the Borel question.

## Assumptions and scope

A colouring \(c:Y\to\{0,1\}\) is *unfriendly* at \(y\) when at least half of the finitely many neighbours of \(y\) have colour different from \(c(y)\). A Borel probability \(\nu\) is *invariant for the connectedness relation* when every Borel partial bijection whose graph lies in that equivalence relation preserves \(\nu\). This implies the graph is \(\nu\)-preserving in the sense of Conley–Tamuz.

Let \(X\subseteq2^{\mathbb N}\) be the sequences having infinitely many \(1\)'s, carrying the restriction \(\mu\) of the fair Bernoulli product probability. Write \(k(x)\) for the position of its first \(1\), and let \(p(x)\) erase that first \(1\). The undirected graph \(T\) of \(p\) has precisely the eventual-equality components, with one end per component and \(k\) children at a vertex of first-one rank \(k\). These elementary facts are reconstructed below; the underlying tree is from Pelayo-Gómez.

Set \(\varepsilon_k=1\) for odd \(k\), and \(0\) for even \(k\). Add one leaf to each vertex of \(T\) whose rank is odd. Call the resulting forest \(F\), with base vertices \((x,0)\) and leaves \((x,1)\) where defined. Every base vertex has \(k(x)+\varepsilon_{k(x)}\) children and one parent.

Define odd positive integers
\[
M_0=1,\qquad M_1=3,\qquad
M_{k+1}=1+\sum_{j=0}^{k-1}M_j+\varepsilon_k\quad(k\ge1).
\]
Replace each base vertex \((x,0)\) by a fibre of \(M_{k(x)}\) vertices, each added leaf by a fibre of one vertex, and each \(F\)-edge by all cross-edges between its two fibres. Write \(r:Y\to V(F)\) for the fibre projection. The construction makes no edges inside fibres.

## Proof

**1. Recurrence, parity, and dominance.** The first fibre sizes are \(1,3,3,5,9,13,23,35,59\). For every \(k\ge1\), subtracting successive defining equations gives
\[
M_{k+2}=M_{k+1}+M_k+(-1)^k.
\]
Thus \(N_k=M_k-(-1)^k\) satisfies the Fibonacci recurrence from \(k=1\) onwards, with \(N_1=4\), \(N_2=2\). It follows that \(M_k=\Theta(\varphi^k)\), and in particular \(\sum_k2^{-k}M_k<\infty\). The defining recurrence inductively gives all \(M_k\) odd. It also gives a nondecreasing sequence: \(M_0<M_1=M_2\), and \(M_{k+2}-M_{k+1}=M_k+(-1)^k>0\) for \(k\ge1\).

For a base vertex of rank \(k\), the sum of the multiplicities of its children is
\[
S_k=\sum_{j<k}M_j+\varepsilon_k.
\]
The number \(k+\varepsilon_k\) of child fibres is even, so \(S_k\) is even. If the parent's first-one rank is \(\ell>k\), then \(M_\ell\ge M_{k+1}>S_k\): for \(k=0\) the inequality is \(3>0\), while for \(k\ge1\) it is the defining equality \(M_{k+1}=S_k+1\). At an added leaf, its parent's weight is positive and its child-weight sum is zero. We call this property *strict parent majority*.

Every vertex in a fibre over \(v\in F\) has exactly \(\sum_{w\sim_Fv}m(w)\) neighbours, where \(m(v)\) is the fibre multiplicity. The original forest has odd degrees (at a base vertex the degree is \(k+1+\varepsilon_k\)); all fibre multiplicities are odd. Hence every degree in \(G\) is odd. For a base point whose first two \(1\)'s occur at \(k<\ell\), its degree is \(M_\ell+S_k\ge3\); at a leaf of odd rank \(k\), the degree is \(M_k\ge3\). The base vertices with first two \(1\)'s at ranks \(0,1\), and leaves of rank \(1\), have degree exactly \(3\). Since ranks along the parent ray tend to infinity and \(M_k\to\infty\), each component has unbounded degrees.

**2. Rigidity of unfriendly colourings.** Consider a colouring unfriendly at every vertex. All vertices of a fibre have the identical neighbourhood, of odd cardinality. The colour opposite to the unique strict majority in that neighbourhood is forced; therefore the fibre is monochromatic. Write its colour as \(b(v)\). Strict parent majority shows the majority colour among the neighbours of the fibre over \(v\) is always \(b(P(v))\), regardless of its children's colours. Consequently \(b(v)\ne b(P(v))\) on every parent edge of \(F\). Thus \(b\) is a proper two-colouring of \(F\), and the original colouring is proper on \(G\). Conversely every proper two-colouring of the forest \(F\) lifts to an unfriendly colouring of \(G\). These conclusions also hold after restriction to any union of connected components.

**3. Topology and hyperfiniteness.** The first-one rank is locally constant on \(X\), and the parent map \(p\) is continuous. Each vertex of \(T\) has a finite descendant set, consisting of its \(2^{k(x)}\) variations on the initial \(k(x)\) positions. Its parent ray is infinite; hence \(T\) is a locally finite closed one-ended forest. The added-leaf set is clopen, as are the fibre sections, since \(M_{k(x)}\) is locally constant. Thus \(Y\) is a clopen subset of \(X\times\{0,1\}\times\mathbb N\) and is zero-dimensional Polish. The inverse image under \(r\times r\) of the closed relation \(F\) is \(G\), so \(G\) is closed and locally finite. Finite positive fibre replacements preserve one-endedness and bipartiteness. The connectedness relation of \(G\) is precisely equality of the base sequences modulo finite coordinate changes. Equating coordinates after position \(n\) therefore gives an increasing Borel exhaustion by finite equivalence classes, proving hyperfiniteness.

**4. An invariant probability with exact total mass.** For Borel \(A\subseteq Y\), define the counting lift
\[
\eta(A)=\int_X\sum_{t:\,(x,t)\in F}\sum_{0\le i<m(x,t)}
\mathbf1_A(x,t,i)\,d\mu(x).
\]
Every Borel partial bijection within connectedness can be Borel-partitioned into restrictions of countably many maps \((x,t,i)\mapsto(\sigma_Dx,u,j)\), where \(D\subset\mathbb N\) is finite and \(\sigma_D\) flips precisely those coordinates. Each such map preserves \(\eta\), since \(\mu\) is invariant under \(\sigma_D\); therefore \(\eta\) is invariant for the full connectedness relation. In particular, countably many Borel partial matchings cover the locally finite edge relation; extending each to an involution by the identity outside its endpoints exhibits the graph as probability-measure-preserving after normalization.

For \(|z|\) sufficiently small the multiplicity generating function is
\[
A(z)=\sum_{k\ge0}M_kz^k
=\frac{1+3z+z^2-2z^3}{(1+z)(1-z-z^2)}.
\]
In particular \(A(1/2)=20/3\). Since \(\mu\{k(x)=k\}=2^{-k-1}\) and \(\int\varepsilon_{k(x)}\,d\mu=1/3\),
\[
\eta(Y)=\sum_{k\ge0}2^{-k-1}(M_k+\varepsilon_k)
=\frac{10}{3}+\frac13=\frac{11}{3}.
\]
Thus \(\nu=(3/11)\eta\) is an atomless, fully supported, connectedness-invariant Borel **probability**. It is not merely quasi-invariant.

**5. No measurable or Baire almost-everywhere unfriendly colouring.** Suppose a \(\nu\)-measurable colouring is unfriendly on a conull set. Enclose its failure set in a Borel null set and remove that set's connectedness saturation. Invariance of \(\nu\) makes the remainder an invariant conull Borel set. By Step 2, the surviving colouring induces a proper two-colouring \(b\) of \(T\) on an eventual-equality-invariant \(\mu\)-conull subset of \(X\). The section \(x\mapsto(x,0,0)\) pulls \(\nu\) back to \((3/11)\mu\), ensuring the required measurability.

If \(\sigma_j\) flips coordinate \(j\), any such proper colouring has \(b(\sigma_jx)=1-b(x)\) on its invariant domain, since \(T\) is a tree and each of its edges flips one bit. But for every \(\mu\)-measurable two-colouring, \(\mu\{b(\sigma_jx)\ne b(x)\}\to0\) as \(j\to\infty\): approximate its colour class by a cylinder set depending on finitely many coordinates, and use invariance of \(\mu\). This contradicts the required probability one, proving nonexistence.

The category analogue follows by first deleting the connectedness saturation of the meager failure set. Such saturations are meager because connectedness is covered by the countably many clopen partial homeomorphisms used in Step 4. A Baire measurable colouring is continuous on a comeager relative subspace, while \(\sigma_jx\to x\), contradicting the parity-flip identity there. Thus even comeager-set Baire measurable unfriendly colourings do not exist.

**6. Infinite mean degree.** Restrict the degree integral against \(\eta\) to base points whose first two \(1\)'s occur at consecutive ranks \(k,k+1\). This cylinder has \(\mu\)-measure \(2^{-k-2}\), contains \(M_k\) base fibre points, and each such point has degree at least \(M_{k+1}\). Therefore
\[
\int_Y\deg_G(y)\,d\eta(y)
\ \ge\sum_{k\ge0}2^{-k-2}M_kM_{k+1}=\infty,
\]
because the summands grow on the scale \((\varphi^2/2)^k\) and \(\varphi^2/2>1\). Normalization to \(\nu\) preserves divergence. This independently verifies that the counterexample lies outside the finite-average-degree theorem's hypothesis.

**7. Sharpness within the certificate class.** Consider any positive odd, rank-homogeneous base weights \(U_k\), with added-leaf weights \(1\), that give degree at least \(3\) and satisfy the strict-parent-majority inequality at every base vertex. The rank-\(1\) leaf has degree \(U_1\), so \(U_1\ge3\), and \(U_0\ge1\). Base vertices whose first two \(1\)'s are at \(k,k+1\) require
\[
U_{k+1}>\sum_{j<k}U_j+\varepsilon_k.
\]
The right-hand side is even; hence the odd number \(U_{k+1}\) must be at least its value plus \(1\). Induction yields \(U_k\ge M_k\) for every \(k\). Our weights attain the bound simultaneously. This proves pointwise minimality of the explicit **certificate**, not a universal lower bound for all possible counterexample graphs or all possible rigidity proofs.

## Verification

The standalone file `verify_optimal_fibres.py` checks the recurrence and parity, all eligible parent ranks through the indicated finite cutoff, exhaustive assignments of child-fibre colours for small ranks, the minimum-degree bound on those instances, the generating-function normalization \(\eta(Y)=11/3\), and increasing finite partial sums for the infinite-cost lower bound. It reports `VERIFY_OK` and `NORMALIZATION_OK`. The infinite recurrence argument, invariance, one-endedness, and non-colourability are proved above rather than inferred from experiments.

## Relationship to prior work

Pelayo-Gómez, *Unfriendly partitions of locally finite Borel graphs* (arXiv:2609.11919v1), constructs the same underlying first-one tree and odd-degree added-leaf forest but uses \(M_k=(3^{k+1}-(-1)^k)/2\). In that construction the lifted invariant counting measure has infinite total mass and the connectedness relation admits no invariant probability (Proposition 4.4); instead the author constructs an equivalent **quasi-invariant** probability with finite mean degree. The present rank weights are neither those multiplicities nor a corollary of the published existence theorem: summability of the lifted counting measure changes the measure-preservation regime. The source's rigidity and topology ideas remain applicable after independently checking the sharp parent-majority inequality.

Conley and Tamuz, *Unfriendly colorings of graphs with finite average degree* (arXiv:1903.05268; Proceedings of the London Mathematical Society), prove existence of almost-everywhere Borel unfriendly colourings in the invariant **finite-average-degree** setting (Theorem 1). The example above demonstrates that their integrability assumption cannot be dropped, even for a hyperfinite equivalence relation and a closed bipartite graph. It is not covered by their bounded-degree or small-cocycle theorems because the degrees are unbounded and the invariant mean degree is infinite.

## Limitations

The result does **not** produce a bounded-maximum-degree counterexample. Its optimality statement is restricted to odd rank-homogeneous fibre weights, unit leaf weights, minimum degree three, and the pointwise strict-parent-majority certificate; other gadgets may use fewer points. Invariant probability does not imply integrable degrees, as the explicit divergent series shows. The reduction to a nonmeasurable parity colouring is for two colours; no claim is made about three-colourings. The source preprints are not independent validations of this new argument.

## References

1. José de Jesús Pelayo-Gómez, *Unfriendly partitions of locally finite Borel graphs*, arXiv:2609.11919v1, first posted 2026-09-10. https://arxiv.org/pdf/2609.11919
2. Clinton T. Conley and Omer Tamuz, *Unfriendly colorings of graphs with finite average degree*, arXiv:1903.05268, first posted 2019-03-12; Proceedings of the London Mathematical Society 122 (2021), 229–233. https://arxiv.org/pdf/1903.05268
