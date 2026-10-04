# Tie-collision phase transition for ordered Boolean full products

## Finding
For a fixed integer \(d\ge 1\), let \(P_d\) have universe \(\mathbb Q^d\). For each coordinate \(i\), name the equivalence relation \(E_i\) of equality in the \(i\)-th coordinate and the subquotient order \(<_i\) from \(E_i\) to the universal relation induced by the usual order on the \(i\)-th coordinate. For \(d=2\), this is exactly Braunfeld's full product \(\mathbb Q^2\); for general \(d\), it is the Boolean-lattice version of the same generic subquotient-order construction.

Let \(T_d(n)\) be the number of automorphism orbits on all ordered \(n\)-tuples of \(P_d\), and \(I_d(n)\) the number on injective ordered \(n\)-tuples. If \(F_n\) is the \(n\)-th ordered Bell/Fubini number and \(s(n,k)\) is the signed Stirling number of the first kind, then
\[
T_d(n)=F_n^d,
\qquad
I_d(n)=\sum_{k=1}^n s(n,k)F_k^d.
\]
These exact product-action formulas are classical. The additional conclusion is a sharp dimension-dependent collision law. Writing \(L=\log 2\), for fixed \(d\) and \(n\to\infty\),
\[
\frac{I_d(n)}{T_d(n)}=
\begin{cases}
2L^{n+1}(1+o(1)),&d=1,\\[2mm]
e^{-L^2/2}+o(1),&d=2,\\[2mm]
1-\dfrac{L^d}{2n^{d-2}}+o\!\left(n^{2-d}\right),&d\ge3.
\end{cases}
\]
Thus dimension \(2\) is the critical product dimension: a positive limiting fraction \(e^{-(\log 2)^2/2}\) of all tuple orbits is injective; from dimension \(3\) onward almost every tuple orbit is injective, with the first deficit term explicitly \((\log 2)^d/(2n^{d-2})\). In particular,
\[
\frac{I_3(n)}{T_3(n)}=1-\frac{(\log2)^3}{2n}+o(n^{-1}).
\]

## Assumptions and scope
The coordinate equivalence relations are named, so coordinate permutations are not automorphisms. The quotient orders are also named and oriented. The dimension \(d\) is fixed while \(n\) tends to infinity. Braunfeld's source explicitly presents \(d=2\), and its general finite-distributive-lattice theorem supplies the generic setting in which the Boolean \(d\)-coordinate construction sits. The first public arXiv version of the primary source appeared on 2017-10-14; the journal paper lists MSC 03C13 and 03C50.

## Proof
First identify the automorphism group. Every automorphism of \(P_d\) induces an order automorphism of each quotient \(P_d/E_i\cong(\mathbb Q,<)\). Since
\[
E_1\wedge\cdots\wedge E_d
\]
is equality, a point is determined by its \(d\) quotient classes. Hence every automorphism acts coordinatewise, and conversely every \(d\)-tuple of order automorphisms acts on \(P_d\). Therefore
\[
\operatorname{Aut}(P_d)\cong\operatorname{Aut}(\mathbb Q,<)^d.
\]
The same observation proves homogeneity directly: a finite partial isomorphism induces a finite order-preserving partial bijection on each coordinate quotient, and each extends to an automorphism of \((\mathbb Q,<)\).

An orbit of \(\operatorname{Aut}(\mathbb Q,<)\) on an arbitrary ordered \(n\)-tuple is exactly a weak order on the index set \([n]\): indices are tied precisely when their coordinates are equal, and the tie blocks inherit their linear order from \(\mathbb Q\). There are \(F_n\) such weak orders. Coordinate independence therefore gives
\[
T_d(n)=F_n^d.
\]
An \(n\)-tuple in \(P_d\) is injective exactly when no pair of indices is tied in all \(d\) coordinate weak orders. Equivalently, the meet of their \(d\) tie partitions is discrete. Decomposing arbitrary tuples by their equality kernel gives
\[
T_d(n)=\sum_{k=1}^n {n\brace k}I_d(k),
\]
and Stirling inversion yields the exact formula for \(I_d(n)\).

For the asymptotics, use the standard ordered-Bell estimate
\[
F_n\sim \frac{n!}{2L^{n+1}}.
\]
When \(d=1\), injectivity forces a strict total order, so \(I_1(n)=n!\), giving the first line.

For \(d=2\), Cameron, Prellberg, and Stark's incidence-matrix asymptotic applies exactly. Indeed \(I_2(n)/n!\) is the number of zero-one matrices with exactly \(n\) ones and no zero row or column: the two ordered weak-order block systems index the rows and columns and injectivity puts at most one label in each cell. Their theorem gives
\[
\frac{I_2(n)}{F_n^2}\longrightarrow e^{-L^2/2}.
\]
This critical constant is prior work.

Now suppose \(d\ge3\). Choose \(d\) weak orders independently and uniformly from the \(F_n\) weak orders on \([n]\). Let \(X\) count unordered pairs \(\{i,j\}\) tied in every coordinate. Contracting one prescribed tied pair gives a bijection with weak orders on \(n-1\) points, so
\[
\mathbb E X={n\choose2}\left(\frac{F_{n-1}}{F_n}\right)^d
\sim \frac{L^d}{2}n^{2-d}.
\]
For two distinct pair-collision events, whether the two pairs are disjoint or share one vertex, imposing both ties contracts exactly two degrees of freedom in each weak order. Thus their joint probability is
\[
\left(\frac{F_{n-2}}{F_n}\right)^d=O(n^{-2d}).
\]
There are \(O(n^4)\) pairs of pair-events, hence
\[
\mathbb E {X\choose2}=O(n^{4-2d})=o(n^{2-d}).
\]
Bonferroni's inequalities now give
\[
\Pr(X=0)=1-\mathbb E X+o(n^{2-d})
=1-\frac{L^d}{2n^{d-2}}+o(n^{2-d}).
\]
But \(\Pr(X=0)=I_d(n)/T_d(n)\), proving the last line and the phase transition.

## Verification
The bundled `verify.py` computes ordered Bell numbers and both Stirling transforms exactly through nontrivial ranges. It checks \(T_d(n)=\sum_k {n\brace k}I_d(k)\) for \(d\le5\), verifies \(I_1(n)=n!\), and reproduces the known incidence-matrix sequence A101370 from \(I_2(n)/n!\). It also records the previously unindexed-looking \(d=3\) set-orbit / three-dimensional support counts
\[
1,13,353,17041,1284977,139389925,20564986865,\ldots.
\]
Independently of the Stirling calculation, the verifier explicitly generates every weak order through \(n=4\), takes Cartesian powers for \(d\le3\), tests the no-common-tie condition pair by pair, and recovers the exact injective counts. Finally it prints numerical scaled deficits showing convergence toward \((\log2)^d/2\) for \(d=3,4,5\). These numerical checks are sanity tests; the asymptotic proof is the Bonferroni argument above.

## Relationship to prior work
Braunfeld supplies the homogeneous full product \(\mathbb Q^2\) as Example 16 and the general finite-distributive-lattice generic subquotient-order theorem. Cameron, Gewurz, and Merola already treat the product action of \(A=\operatorname{Aut}(\mathbb Q,<)\), explicitly discuss \(A\times A\), \(A\times A\times A,\ldots\), and derive the weak-order/Stirling enumeration; the exact formulas \(T_d(n)=F_n^d\) and \(I_d(n)=\sum_k s(n,k)F_k^d\) are therefore not claimed as new. They also identify the \(d=2\) binary-matrix model. Cameron, Prellberg, and Stark prove the \(d=2\) incidence-matrix asymptotic, which is exactly the critical constant \(e^{-(\log2)^2/2}\).

The contribution isolated here is the sharp higher-dimensional collision asymptotic
\[
1-\frac{I_d(n)}{T_d(n)}\sim\frac{(\log2)^d}{2n^{d-2}}\qquad(d\ge3),
\]
together with its interpretation as a dimension-\(2\) phase transition for the ordered Boolean full-product Fraïssé family. Targeted literature, exact-sequence, higher-dimensional-incidence-array, weak-order-meet, and semantic published-finding corpus searches did not locate this higher-dimensional asymptotic or phase statement. Exact searches for the \(d=3\) initial sequence likewise returned no matching enumerative source.

## Limitations
The novelty assessment is search-based and cannot exclude an unindexed note or folklore generalization of the product-action calculations. The exact orbit formulas and the \(d=2\) asymptotic are prior work; novelty is asserted only for the \(d\ge3\) first-order collision asymptotic and the resulting full-product phase interpretation. The theorem keeps \(d\) fixed; it does not analyze a regime in which the number of coordinates grows with \(n\). Braunfeld explicitly names only the two-coordinate full product, while the \(d\)-coordinate version is derived from his general theorem and verified directly.

## References
1. Samuel Braunfeld, *Homogeneous 3-Dimensional Permutation Structures*, arXiv:1710.05138, first submitted 2017-10-14; *Electronic Journal of Combinatorics* 25(2) (2018), #P2.52, DOI 10.37236/7506.
2. Peter J. Cameron, Daniele A. Gewurz, Francesca Merola, *Product action*, *Discrete Mathematics* 308 (2008), 386–394, DOI 10.1016/j.disc.2006.11.054.
3. Peter J. Cameron, Thomas Prellberg, Dudley Stark, *Asymptotics for Incidence Matrix Classes*, *Electronic Journal of Combinatorics* 13 (2006), #R85, DOI 10.37236/1111.
4. OEIS A101370, number of zero-one matrices with \(n\) ones and no zero rows or columns.
