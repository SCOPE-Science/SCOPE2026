# Colored-gap orbit profiles for minimal chain ultrametric expansions
## Finding
For an integer \(d\ge1\), let
\[
\Lambda_d=\{\lambda_0<\lambda_1<\cdots<\lambda_d\}
\]
be a chain. Let \(M_d\) be Braunfeld's minimal generic expansion of the generic \(\Lambda_d\)-ultrametric space: for every \(i=0,\ldots,d-1\), add one generic subquotient order from \(E_{\lambda_i}\) to its cover \(E_{\lambda_{i+1}}\). If \(a_d(n)\) is the number of \(\operatorname{Aut}(M_d)\)-orbits on injective ordered \(n\)-tuples, then
\[
\boxed{a_d(n)=n!\,d^{\,n-1}}\qquad(n\ge1).
\]
More precisely, the orbit of an injective labeled \(n\)-tuple is encoded by a permutation of its \(n\) labels together with a word of length \(n-1\) over \(\{1,\ldots,d\}\). The letter at a gap records the first equivalence level at which the two adjacent points become equivalent.

If \(b_d(n)\) counts all ordered \(n\)-tuple orbits, repetitions allowed, then
\[
b_d(n)=\sum_{k=1}^{n}{n\brace k}\,k!\,d^{k-1}
       =\frac{1}{d}\,\mathcal F_n(d),
\]
where \(\mathcal F_n(x)=\sum_{k=1}^{n}k!{n\brace k}x^k\) is the ordered-Bell/Fubini polynomial. Hence
\[
\sum_{n\ge1}b_d(n)\frac{x^n}{n!}
 =\frac{e^x-1}{1-d(e^x-1)}.
\]
In particular, the chain height parameter is already recovered in arity two by \(d=a_d(2)/2\), and the injective profile satisfies the exact recurrence \(a_d(n+1)=d(n+1)a_d(n)\).

The first six injective profiles are
\[
\begin{aligned}
d=1:&\quad 1,2,6,24,120,720,\\
d=2:&\quad 1,4,24,192,1920,23040,\\
d=3:&\quad 1,6,54,648,9720,174960.
\end{aligned}
\]
The first six all-tuple profiles are
\[
\begin{aligned}
d=1:&\quad 1,3,13,75,541,4683,\\
d=2:&\quad 1,5,37,365,4501,66605,\\
d=3:&\quad 1,7,73,1015,17641,367927.
\end{aligned}
\]

## Assumptions and scope
Braunfeld defines \(\Lambda\)-ultrametric spaces as structures carrying the equivalence relations associated with a finite lattice and, for a finite distributive \(\Lambda\), defines the minimal expansion by one subquotient order from each meet-irreducible relation to a chosen cover. In a finite chain, every non-top element is meet-irreducible and has a unique cover, so the minimal expansion has exactly the \(d\) adjacent-level subquotient orders used above. Braunfeld proves that this minimal class is a Ramsey class with the expansion property, and the later Braunfeld--Simon classification places such generic subquotient-order expansions in the catalog of homogeneous finite-dimensional permutation structures.

The formula concerns the automorphism group of the full minimal expansion \(M_d\), not the reduct obtained by forgetting its subquotient orders. The finite equivalence relations are allowed to coincide on a finite induced substructure, exactly as in the standard \(\Lambda\)-ultrametric presentation.

## Proof
Because \(M_d\) is homogeneous, injective ordered \(n\)-tuple orbits are the isomorphism types of induced structures on \(n\) labeled distinct points. Consider one such finite structure.

Inside each \(E_{\lambda_i}\)-class, the subquotient order from \(E_{\lambda_{i-1}}\) to \(E_{\lambda_i}\) linearly orders its child \(E_{\lambda_{i-1}}\)-classes. Reading these local orders recursively from the top level down gives a unique global left-to-right order of the \(n\) labeled points. Thus the first datum is a permutation \(\pi\in S_n\).

For each adjacent pair \(\pi_j,\pi_{j+1}\), let \(c_j\in\{1,\ldots,d\}\) be the least index such that the pair is \(E_{\lambda_{c_j}}\)-equivalent. This produces a gap word
\[
(c_1,\ldots,c_{n-1})\in\{1,\ldots,d\}^{n-1}.
\]
The pair \((\pi,c)\) reconstructs the whole finite structure. Indeed, for every \(i\), the \(E_{\lambda_i}\)-classes are exactly the maximal consecutive intervals in the \(\pi\)-order whose internal gaps all have color at most \(i\). These interval partitions are nested, and the order of the child intervals is inherited from \(\pi\), recovering every adjacent-level subquotient order.

Conversely, start from any permutation \(\pi\in S_n\) and any word \(c\in\{1,\ldots,d\}^{n-1}\). For each \(i\), declare the \(E_{\lambda_i}\)-classes to be the maximal consecutive intervals separated only by gaps with colors at most \(i\), and order the children of each class from left to right. This gives a valid finite member of Braunfeld's minimal chain expansion. The two constructions are inverse. Hence the labeled finite structures, and therefore the injective tuple orbits, are in bijection with
\[
S_n\times\{1,\ldots,d\}^{n-1},
\]
which proves \(a_d(n)=n!d^{n-1}\).

For an arbitrary ordered \(n\)-tuple, first choose its equality partition. If it has \(k\) blocks, order the distinct values canonically by the least coordinate in each block. There are \({n\brace k}\) equality patterns and \(a_d(k)\) possible injective orbits of the distinct values. Therefore
\[
b_d(n)=\sum_{k=1}^{n}{n\brace k}a_d(k).
\]
Substituting the injective formula yields the displayed Fubini-polynomial identity. Finally, using
\[
\sum_{n\ge k}{n\brace k}\frac{x^n}{n!}=\frac{(e^x-1)^k}{k!}
\]
and summing the resulting geometric series gives the exponential generating function.

## Verification
The bundled `verify.py` independently generates the finite structures as recursively ordered nested set partitions, rather than from the closed formula. For every \(1\le d\le3\) and \(1\le n\le5\), it checks that the generated structures are in bijection with all pairs consisting of a label permutation and a length-\(n-1\) word over \(\{1,\ldots,d\}\), and that encoding followed by decoding is the identity. It also checks the Stirling transform and the ordered-Bell/Fubini-polynomial identity through \(d\le5\), \(n\le8\). A successful replay ends with `VERIFY_OK`.

## Relationship to prior work
Braunfeld's 2017 paper defines the minimal expansion \(\widetilde{\mathcal A}^{\min}_{\Lambda}\): one subquotient order from each meet-irreducible relation to a cover, and proves that its Fraïssé limit is a Ramsey expansion with the expansion property. The paper explicitly notes that when \(\Lambda\) is a chain, the underlying generic \(\Lambda\)-ultrametric is the usual homogeneous ultrametric space. Braunfeld and Simon later classify homogeneous finite-dimensional permutation structures via generic distributive-lattice ultrametrics with generic subquotient orders.

The ordered Bell/Fubini numbers and polynomials are classical; in particular OEIS A000670 records the ordered-partition interpretation and \(\sum k!{n\brace k}\) formula, while Guo and Zhu use the ordered Bell polynomial \(\sum k!{n\brace k}q^k\) and its exponential generating function. The new point here is the exact identification of the chain minimal-expansion tuple orbits with colored gaps between a labeled permutation, yielding the closed orbit profiles and parameter recovery. Targeted exact-formula searches, semantic published-finding corpus searches, the Braunfeld papers, the Braunfeld thesis, and the current research ledger did not locate this orbit-profile statement.

## Limitations
The claim is specific to the minimal successor-order expansion of a chain. Adding extra subquotient orders, choosing a non-chain distributive lattice, or forgetting part of the expansion changes the finite types and generally changes the orbit profile. The Fubini-polynomial identity itself is classical combinatorics; originality is claimed only for its appearance as the repeated-tuple profile of this model-theoretic family and for the colored-gap bijection. Unindexed notes or folklore about these particularly simple chain expansions remain a residual originality risk.

## References
1. Samuel Braunfeld, *Ramsey expansions of \(\Lambda\)-ultrametric spaces*, arXiv:1710.01193, submitted 3 October 2017. Definition 7.7 defines the minimal successor-order expansion; Theorem 7.11 proves its Ramsey and expansion properties. The arXiv record lists MSC 03C13, 03C15, 03C50, 05D10, 37B05.
2. Samuel Braunfeld and Pierre Simon, *The classification of homogeneous finite-dimensional permutation structures*, arXiv:1807.07110; Electronic Journal of Combinatorics 27(1) (2020), P1.38, DOI 10.37236/8321. The paper defines subquotient orders, identifies \(\Lambda\)-ultrametrics with lattice-indexed equivalence relations, and proves the catalog is complete.
3. Samuel Braunfeld, *Infinite Limits of Finite-Dimensional Permutation Structures, and their Automorphism Groups: Between Model Theory and Combinatorics*, arXiv:1805.04219, 2018. The thesis presents the minimal successor-order expansion and the surrounding finite-dimensional permutation-structure catalog.
4. OEIS A000670, Fubini numbers / ordered Bell numbers, including the interpretation as ordered partitions and the formula \(\sum_k k!{n\brace k}\).
5. Wan-Ming Guo and Bao-Xuan Zhu, *A generalized ordered Bell polynomial*, Linear Algebra and its Applications 588 (2020), 458--470, DOI 10.1016/j.laa.2019.12.006.
