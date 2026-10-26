# An exact dimension-free generation law for reversible finite tense algebras

## Finding
Let \(n\ge2\) and \(k\ge1\), and put \(q=2^k\). Choose a permutation \(\sigma\) uniformly from \(S_n\). Form the full finite tense Boolean algebra \(\mathcal A_\sigma=\mathcal P([n])\), with the ordinary Boolean operations, future operator \(F(U)=\sigma^{-1}(U)\), and past operator \(P(U)=\sigma(U)\). Independently choose \(k\) subsets \(U_1,\ldots,U_k\subseteq[n]\), each uniformly from the power set. Then the probability that those subsets generate \(\mathcal A_\sigma\) under the entire tense-Boolean signature is **exactly**

\[
\Pr\bigl(\langle U_1,\ldots,U_k\rangle_{\mathcal A_\sigma}=\mathcal A_\sigma\bigr)=1-2^{-k}.
\]

The identity holds for every \(n\ge2\), without an asymptotic limit. In particular, among all \(n!\,q^n\) pairs consisting of a permutation and an ordered \(k\)-tuple of subsets, precisely \(n!\,(q^n-q^{n-1})\) generate. For \(n=1\), all \(q\) tuples generate.

The proof also gives an exact conditional census. If \(c_\ell\) is the number of cycles of length \(\ell\) in \(\sigma\), define
\[
L_\ell(q)=\frac1\ell\sum_{d\mid\ell}\mu(d)q^{\ell/d},\qquad
(a)_{\underline m}=a(a-1)\cdots(a-m+1).
\]
The number of ordered \(k\)-tuples generating \(\mathcal A_\sigma\) is
\[
G_k(\sigma)=\prod_{\ell\ge1}\ell^{c_\ell}\bigl(L_\ell(q)\bigr)_{\underline{c_\ell}}.
\]
When \(c_\ell>L_\ell(q)\), its factor and the entire product are zero. This census is part of the derivation, not a separate claim of an unrelated invariant.

## Assumptions and scope
All sets and algebras are finite. The future and past operators are induced by one **bijective** accessibility map; they act as inverse Boolean automorphisms. A generating tuple means generation using finite Boolean operations, constants, and both tense operators, not merely Boolean generation. Sampling is uniform and independent: first \(\sigma\in S_n\), then all membership bits for the \(k\) subsets. The theorem is not asserted for nonbijective maps, nonuniform distributions, or arbitrary binary relations. No independence or external certification is claimed.

## Proof
**1. Iterated observations.** Each ordered \(k\)-tuple assigns a symbol in an alphabet of size \(q\) to each vertex: its vector of membership bits. For a vertex \(v\), its two-sided itinerary is the bi-infinite string of symbols read along the orbit \(\{\sigma^t(v):t\in\mathbb Z\}\). The generated algebra is exactly the collection of unions of equivalence classes of vertices sharing the same itinerary. Indeed, the generators and all their tense translates distinguish exactly these classes. Since \([n]\) is finite, Boolean combinations of translated coordinates realize each class; conversely, every generated element is constant on classes. Thus the tuple generates the whole power set if and only if all \(n\) itineraries are pairwise different.

**2. Primitive-necklace criterion.** For each \(\ell\)-cycle, read the cyclic \(q\)-ary word of length \(\ell\). Its \(\ell\) vertices have distinct itineraries exactly when the word is primitive, meaning no nonidentity cyclic rotation fixes it. For different cycles, primitive cyclic words yield coincident itineraries if and only if they have the same length and belong to the same necklace (rotation) class. The number of primitive necklaces of length \(\ell\) over \(q\) symbols is \(L_\ell(q)\), by Möbius inversion from \(q^\ell=\sum_{d\mid\ell}dL_d(q)\). On the \(c_\ell\) labelled cycles, choose distinct primitive necklace classes and one of \(\ell\) rotations for each. This produces the formula for \(G_k(\sigma)\) above.

**3. Averaging over permutations.** The number of permutations having cycle counts \((c_\ell)\) is \(n!/\prod_\ell\ell^{c_\ell}c_\ell!\), under \(\sum_\ell\ell c_\ell=n\). Consequently the total number \(T_{n,q}\) of generating permutation-colouring pairs satisfies the formal power series identity
\[
\sum_{n\ge0}\frac{T_{n,q}}{n!}z^n
=\prod_{\ell\ge1}\sum_{m=0}^{L_\ell(q)}\binom{L_\ell(q)}m z^{\ell m}
=\prod_{\ell\ge1}(1+z^\ell)^{L_\ell(q)}.
\]
Here \(T_{0,q}=1\) is a formal empty-object convention.

**4. Witt-product cancellation.** Unique decomposition of every nonempty word into a power of one primitive necklace, equivalently Möbius inversion above and a formal logarithm, gives the classical Witt identity
\[
\prod_{\ell\ge1}(1-z^\ell)^{-L_\ell(q)}=\frac1{1-qz}.
\]
Applying it at \(z\) and at \(z^2\) gives
\[
\prod_{\ell\ge1}(1+z^\ell)^{L_\ell(q)}
=\frac{1-qz^2}{1-qz}.
\]
Therefore \(T_{1,q}=q\), and for every \(n\ge2\), \(T_{n,q}=n!(q^n-q^{n-1})\). Divide by the exactly \(n!q^n\) equally likely permutation-colouring pairs. Since the color alphabet is the \(k\)-bit vector alphabet, \(q^{-1}=2^{-k}\). This proves the claim.

## Verification
The standalone Python 3 checker in `checker.py` performs independent direct enumeration of membership vectors and their complete temporal itineraries against the closed-form conditional count: all permutations of sizes \(1\) through \(6\) for \(q=2\), and sizes \(1\) through \(4\) for \(q=4\). It directly counts primitive words for lengths \(1\) through \(7\) and alphabet sizes \(1\) through \(6\), verifies formal coefficients for \(q\in\{2,4,8,16\}\) through degree \(18\), and checks aggregate permutation sums. The reported success strings are `PERMUTATION_TENSE_GENERATORS_EXACT_OK` and `GENERATION_SQUAREFREE_IDENTITY_OK`. Finite computation supports but does not replace the all-size formal-series proof.

## Relationship to prior work
Figallo, Sarmiento and Pezzini (2026) establish algebraic completeness for minimal tense logic, with tense Boolean algebras as semantics; Bezhanishvili and Kornell (2025) develop duality and structure of tense operators. These supply the setting, but their inspected results are not an enumeration of random generating tuples. Primitive-necklace counts, the Witt identity and the squarefree-polynomial generating series are classical. Indeed, for prime-power \(q\), the right-hand product in step 3 is the standard generating series for monic squarefree polynomials over \(\mathbb F_q\); the cardinality \(q^n-q^{n-1}\) is not claimed as a new arithmetic fact. The substantive identification here is that **generation of the full reversible tense algebra** is the exact temporal-itinerary condition counted by this squarefree series. Krieger-type embedding criteria for finite dynamical systems concern the existence of a sufficiently rich labelling, not this uniform average of all labellings and permutations. Relevant symbolic necklace combinatorics also appears in Gessel, Restivo and Reutenauer (2012).

## Limitations
The result concerns the joint uniform distribution over bijective frames and uniform generating predicates. It does not say that the conditional probability is \(1-2^{-k}\) for each fixed permutation; for example, the identity permutation on \(n\) atoms needs distinct initial bit colours and can have probability zero if \(n>2^k\). The arithmetic side and necklace theory predate this result. The specific tense-algebra generation interpretation and exact joint probability are the assessed contribution; possible unlocated historical equivalent combinatorial formulations are a residual priority risk. No independently conducted audit is asserted.

## References
1. M. Figallo, J. Sarmiento and L. Pezzini, *Tense Logic via Truth Degrees: An Algebraic Completeness Result for Kashima's Calculus*, arXiv:2610.01547v1, posted 2026-10-01, https://arxiv.org/abs/2610.01547.
2. G. Bezhanishvili and A. Kornell, *On the structure of modal and tense operators on a boolean algebra*, arXiv:2308.08664v2, https://arxiv.org/html/2308.08664v2.
3. T. Meyerovitch, *An embedding theorem for multidimensional subshifts*, Ergodic Theory and Dynamical Systems (online 2025), Theorem 1.1 describing Krieger's classical periodic-point embedding criterion, https://www.cambridge.org/core/journals/ergodic-theory-and-dynamical-systems/article/an-embedding-theorem-for-multidimensional-subshifts/4447D094B3ABD6A61BB90AC430EA18D3.
4. I. M. Gessel, A. Restivo and C. Reutenauer, *A bijection between words and multisets of necklaces*, European Journal of Combinatorics 33 (2012), 1537–1546, doi:10.1016/j.ejc.2012.03.016.
5. D. Adamson, A. Deligkas, V. V. Gusev and I. Potapov, *Combinatorial Algorithms for Multidimensional Necklaces*, arXiv:2108.01990, https://arxiv.org/abs/2108.01990.
