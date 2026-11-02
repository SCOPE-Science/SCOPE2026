# A partition-Möbius orbit formula for finite subsets of rational chain products

## Finding
Let \(L_r=(\mathbb Q,\min,\max)^r\), as a distributive lattice, and let \(a_{r,n}\) count \(\operatorname{Aut}(L_r)\)-orbits on \(n\)-element subsets. The following formula gives these orbits for all positive integers \(n\) and \(r\ge3\):
\[
a_{r,n}=\frac{1}{n!\,r!}\sum_{g\in S_n}\sum_{\pi\in S_r}\sum_{P\in\Pi_n}\mu(P)\prod_{c\in\operatorname{Cyc}(\pi)}F_{b(g,P,|c|)}.
\]
Here \(\Pi_n\) is the lattice of partitions of \([n]\), ordered by refinement, and \(\mu(P)=\prod_{B\in P}(-1)^{|B|-1}(|B|-1)!\). The number \(F_k=\sum_{j=1}^k j!S(k,j)\) is the number of total preorders on \(k\) labelled objects; \(F_0=1\). For \(g\in S_n\), a partition \(P\), and an integer \(\ell\ge1\), define \(E(g,P,\ell)\) as the smallest equivalence relation containing the equivalence relations \(g^j(P)\) for \(0\le j<\ell\) and containing every pair \((i,g^\ell(i))\). Let \(b(g,P,\ell)\) be the number of its classes.

For three factors the first five values are
\[
(a_{3,1},a_{3,2},a_{3,3},a_{3,4},a_{3,5})=(1,5,80,3053,216879).
\]
The dimensional restriction identifies the new higher-product classification: the two-factor case and its matrix-transposition interpretation were previously established.

## Assumptions and scope
All coordinates carry the order \((\mathbb Q,<)\). An automorphism means a lattice automorphism preserving coordinatewise minimum and maximum; coordinate permutations are allowed. The set size \(n\) is finite and positive. Distinct points need only differ in at least one coordinate: ties are permitted in any particular coordinate. No claim is made for non-isomorphic factors, infinite sets of points, or transformations that reverse a coordinate order.

## Proof
**Step 1 (the automorphism group).** Every lattice automorphism of a finite direct power of a nontrivial linear order permutes the chain factors and acts through order automorphisms on the factors. In this special case this gives \(\operatorname{Aut}(L_r)=\operatorname{Aut}(\mathbb Q,<)^r\rtimes S_r\), consistent with the factor uniqueness of Kurilić's Theorem 1.1(a). This also follows directly by recovering factors from the lattice structure.

**Step 2 (rank profiles).** Label \(n\) different points by \([n]\). In each coordinate, record the total preorder \(W_j\) induced on \([n]\) by the coordinate values. Every total preorder can be realized in \(\mathbb Q\), and two ordered labelled configurations are carried into one another by coordinatewise increasing bijections if and only if all their coordinate preorders coincide. The labelled points are distinct exactly when \(\bigwedge_{j=1}^{r}\ker W_j=\Delta_n\) in the partition lattice. Relabelling the points and permuting lattice coordinates gives a finite action of \(S_n\times S_r\) on these admissible \(r\)-tuples of preorders. The desired orbit count is the number of orbits of this action.

**Step 3 (exclude collisions).** For any partition \(K\) the partition lattice identity is \(\mathbf 1_{K=\Delta_n}=\sum_{P\le K}\mu(P)\). Thus when counting tuples fixed by \((g,\pi)\), the distinctness indicator can be replaced by the sum over all partitions \(P\) such that every coordinate preorder is constant on the blocks of \(P\). The order of this sum is finite, so the substitution is exact. Here \(P\le K\) means \(P\) refines \(K\).

**Step 4 (fixed tuples).** Take one cycle \(c\) of \(\pi\) of length \(\ell\). Fixedness under \((g,\pi)\) forces its \(\ell\) coordinate preorders to be successive relabelled copies of one initial preorder \(W\), and forces \(W\) to be invariant under \(g^\ell\). A finite-order automorphism of a finite chain fixes each chain position. Consequently \(W\), if invariant under \(g^\ell\), must tie every \(g^\ell\)-orbit. Requiring all \(\ell\) preorders to be constant on \(P\) additionally forces \(W\) to tie the classes of every \(g^j(P)\), for \(0\le j<\ell\). Hence the allowable initial preorders are **exactly** the total preorders of the \(b(g,P,\ell)\) classes of \(E(g,P,\ell)\), counted by \(F_{b(g,P,\ell)}\). Every choice determines all other preorders in the cycle uniquely. Different cycles of \(\pi\) impose independent choices, giving the product in the formula.

**Step 5 (average).** Möbius-weight these fixed counts to remove all collisions, sum over the partitions \(P\), and average over \(S_n\times S_r\) by Burnside's lemma. This yields the displayed formula for all stated \(r,n\). No computational exhaustiveness assumption enters the argument.

## Verification
The standalone `checker.py` computes the finite sum independently of orbit-generation enumeration, and cross-checks it against direct enumeration of admissible preorder tuples and their \(S_n\times S_r\)-orbits in small cases, including \((n,r)=(3,3)\) and \((3,4)\). It also reproduces the known two-coordinate row/column transposition counts as a negative control and checks the first five three-coordinate values. Run with `python3 checker.py`; its success line is `ALL_CHECKS_OK`. Direct enumeration is exhaustive only for the small listed inputs; the proof is uniform.

## Relationship to prior work
Kurilić, *Model Theory of Products of Chains* (arXiv:2610.24683v1, first posted 2026-10-17), establishes the uniqueness of chain factors in lattice products, motivating this finite-set orbit question but not computing its orbit profile. Cameron–Prellberg–Stark, *Asymptotics for Incidence Matrix Classes* (arXiv:math/0510155v2, 2006, Section 1 and Table 1), completely cover \(r=2\): their transpose-identified incidence-matrix counts are \(1,3,15,108,1045,\ldots\). That covered case is explicitly excluded from the novelty claim. Chen–Fang–Kitaev–Zhang, *Patterns in Multi-dimensional Permutations* (2025, Sections 1–2), work with coordinate-injective multidimensional permutations and pattern statistics; the collision-retaining orbit formula is not implied by their displayed framework. Standard Burnside and partition-Möbius methods are prior techniques; their joint specialized fixed-point reduction is what yields the new complete higher-dimensional invariant.

## Limitations
The result counts orbits, not an asymptotic growth rate or explicit canonical representatives. Complete historical priority has not been independently certified; an equivalent higher-dimensional incidence-array formula under other terminology remains a risk. A closely related published result on collision probabilities for ordered tuple profiles was identified from its summary, but its complete text could not be inspected. Such tuple probabilities do not by themselves supply the unlabeled coordinate-symmetric orbit formula, although an uninspected appendix could conceivably do so. No independent mathematical audit has been performed.

## References
1. M. S. Kurilić, *Model Theory of Products of Chains*, arXiv:2610.24683v1, 2026-10-17. https://arxiv.org/abs/2610.24683
2. P. J. Cameron, T. Prellberg, D. Stark, *Asymptotics for Incidence Matrix Classes*, Electronic Journal of Combinatorics 13 (2006), R85; arXiv:math/0510155v2. https://arxiv.org/abs/math/0510155
3. S. Chen, H. Fang, S. Kitaev, C. X. T. Zhang, *Patterns in Multi-dimensional Permutations*, European Journal of Combinatorics 130 (2025), 104203. https://strathprints.strath.ac.uk/93412/
4. Standard finite permutation-group orbit counting (Burnside's lemma) and partition-lattice Möbius inversion.
