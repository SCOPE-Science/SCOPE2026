# Sharp generic automorphism rigidity for binary perfect evolution algebras

## Finding
Let \(A\) be uniformly distributed over \(\operatorname{GL}_n(\mathbb F_2)\). Give \(E_A=\mathbb F_2^n\) the evolution-algebra multiplication \(e_i e_j=0\) for \(i\ne j\) and \(e_i^2=\sum_j A_{ij}e_j\). As \(n\to\infty\),
\[
\Pr\{\operatorname{Aut}_{\mathbb F_2}(E_A)\ne\{1\}\}
\sim n(n-1)2^{-2n}.
\]
Conditioned on the event of nontrivial automorphisms, the automorphism group is cyclic of order two with probability tending to one; moreover its generator acts by a transposition of two natural basis vectors, with conditional probability tending to one. For any prescribed transposition \(\tau\) and \(n\ge2\), the exact probability of \(\tau\) acting as an algebra automorphism is
\[
\Pr\{\tau\in\operatorname{Aut}_{\mathbb F_2}(E_A)\}
=\frac{2^{-2n+1}}{(1-2^{-(n-1)})(1-2^{-n})}.
\]
These statements use the uniform distribution on invertible *labelled structure matrices*, not the uniform distribution on algebra isomorphism classes.

## Assumptions and scope
The field is exactly \(\mathbb F_2\); dimension \(n\) is any positive integer for the algebra construction and at least two for the prescribed-transposition identity. The structure matrix is invertible, equivalently \(E_A^2=E_A\), so the evolution algebra is perfect (also called idempotent in the cited literature). Automorphisms are linear, bijective, multiplication-preserving maps over \(\mathbb F_2\), and probabilities refer to uniform sampling of \(\operatorname{GL}_n(\mathbb F_2)\). The asymptotics have \(n\to\infty\) with the field fixed.

## Proof
**Reduction to permutation stabilizers.** For distinct \(i,j\), the products \(e_ie_j\) vanish. Let \(\varphi\) be an algebra automorphism with coefficient matrix \(P=(p_{ij})\), its \(i\)-th row giving \(\varphi(e_i)\). For \(i\ne j\),
\[
0=\varphi(e_i)\varphi(e_j)=\sum_{k=1}^n p_{ik}p_{jk}e_k^2.
\]
Since invertibility of \(A\) makes the \(e_k^2\) a basis, every product \(p_{ik}p_{jk}\) vanishes. Thus each column of \(P\) has at most one nonzero entry; invertibility forces exactly one in each row and column. Hence \(P\) is monomial. Over \(\mathbb F_2\), every nonzero scalar is one, so \(P\) is a permutation matrix. Preservation of squares is equivalent to \(P A=A P\) (up to the harmless convention exchanging \(P\) with its inverse). Therefore
\[
\operatorname{Aut}_{\mathbb F_2}(E_A)
\cong\{\pi\in S_n:P_\pi A=A P_\pi\}.
\]

**A single transposition, exactly.** Fix \(\tau=(1\ 2)\). The permutation operator on \(\mathbb F_2^n\) is \(I+N\), where \(N^2=0\), \(\operatorname{rank}N=1\). Choose a basis \(u=e_1+e_2\), \(v=e_1\), and \(w_3,\ldots,w_n\) such that \(Nv=u\) and \(N\) annihilates the other basis elements. A linear operator \(T\) commutes with \(N\) precisely when, writing \(W=\langle w_3,\ldots,w_n\rangle\), it has
\[
T(u)=a u,\quad T(v)=b u+a v+w,\quad
T(x)=\lambda(x)u+D(x)\quad(x\in W),
\]
where \(a,b\in\mathbb F_2\), \(w\in W\), \(\lambda\in W^*\), and \(D\in\operatorname{End}(W)\). Such a \(T\) is invertible exactly when \(a=1\) and \(D\in\operatorname{GL}(W)\). Consequently the number of invertible matrices commuting with \(\tau\) equals
\[
2^{1+(n-2)+(n-2)}|\operatorname{GL}_{n-2}(2)|
=2^{2n-3}|\operatorname{GL}_{n-2}(2)|.
\]
Using \(|\operatorname{GL}_n(2)|=2^{n^2}\prod_{j=1}^n(1-2^{-j})\), division gives the asserted exact probability, including \(n=2\) under the convention \(|\operatorname{GL}_0(2)|=1\).

**Other permutations have negligible contribution.** Draw first a uniformly random matrix \(B\in M_n(\mathbb F_2)\), without imposing invertibility. For \(\pi\in S_n\), invariance under simultaneous row and column permutation forces \(B\) to be constant on the orbits of \(\langle\pi\rangle\) acting on ordered pairs. If \(o(\pi)\) is the number of such orbits, then
\[
\Pr\{P_\pi B=B P_\pi\}=2^{-\Delta(\pi)},
\qquad \Delta(\pi)=n^2-o(\pi).
\]
Suppose \(\pi\) moves \(k\) letters, has \(s\le\lfloor k/2\rfloor\) nontrivial cycles, and fixes \(f=n-k\) letters. On the pairs of fixed letters there are \(f^2\) orbits; pairs with one moved and one fixed letter give \(2fs\) orbits. On the \(k^2\) remaining pairs every orbit has at least two elements, hence at most \(k^2/2\) orbits. Therefore
\[
\Delta(\pi)\ge2(n-k)(k-s)+\frac{k^2}{2}
\ge (n-k)k+\frac{k^2}{2}.
\]
For \(3\le k\le n/2\) this is at least \(3kn/4\). For \(k>n/2\) it is at least \(n^2/8\). The number of permutations moving exactly \(k\) letters is at most \(n^k\). It follows that the total *unconditioned* probability, summed over all nonidentity nontranspositions, is bounded by
\[
\sum_{k=3}^{\lfloor n/2\rfloor}n^k2^{-3kn/4}
+n!2^{-n^2/8}
=o\bigl(n^2 2^{-2n}\bigr).
\]
For all sufficiently large \(n\), the first sum is dominated by its \(k=3\) term. Furthermore, \(\Pr\{B\in\operatorname{GL}_n(2)\}=\prod_{j=1}^n(1-2^{-j})\) is bounded below by the positive constant \(\prod_{j\ge1}(1-2^{-j})\). Conditioning on invertibility therefore changes this negligible bound by at most a fixed factor.

**Transposition intersections and the group law.** Two distinct transpositions generate a subgroup containing either a three-cycle or a product of two disjoint transpositions. The ordered-pair orbit codimensions of these permutations are, respectively, \(4n-6\) and \(4n-8\); direct counting gives these values. Hence the intersection probability of the events for two distinct transpositions, after conditioning on invertibility, is \(O(2^{-4n+8})\). Summing over \(O(n^4)\) transposition pairs is negligible against \(n^2 2^{-2n}\). Bonferroni and the exact single-transposition probability give
\[
\Pr\{\text{some transposition is an automorphism}\}
\sim {n\choose2}2^{-2n+1}=n(n-1)2^{-2n}.
\]
The preceding bound on all other permutations shows that this is also the leading probability of a nontrivial automorphism group. Except for a relative-probability-o(1) event, there is exactly one nonidentity automorphism, a transposition, which proves the final conditional statement.

## Verification
The standalone `verify.py` uses only the Python standard library. It enumerates every binary matrix of dimensions \(1\) through \(4\), retains precisely the invertible ones by direct binary elimination, computes permutation stabilizers independently by comparing matrix entries, and verifies the exact number fixed by each transposition. In dimensions \(1\) through \(3\), it also enumerates all invertible linear transformations and tests multiplication preservation directly, verifying the permutation reduction without assuming it. The complete finite checks include \(20{,}160\) invertible matrices in dimension four. Run `python verify.py` to reproduce. Exhaustion at small dimensions checks only finite instances; the asymptotic estimates above are the mathematical proof.

## Relationship to prior work
Elduque and Labra (arXiv:1902.02191, first publicly posted 2019-02-06) identify the automorphism group scheme of a perfect evolution algebra through its associated directed graph. Over the binary field, this prior structure directly gives its graph-automorphism reduction. Sriwongsa and Zou (arXiv:2202.01333, first publicly posted 2022-02-02) establish structural results about automorphism groups of idempotent evolution algebras, including monomial constraints and prescribed group realizations. Wei and Zou (arXiv:2310.12368, first publicly posted 2023-10-18) count isomorphism classes via the symmetric-group/torus orbit action. Costoya, Mayorga and Viruel (arXiv:2401.05924) study permutation representations realized by automorphisms. These give broader foundations, and the monomial constraint is prior work. The contribution claimed here is the sharp random-*invertible*-binary asymptotic, the exact transposition-stabilizer probability, and typical symmetry-group identification, not the structural reduction itself. Prior studies of almost surely asymmetric random graphs and directed graphs are relevant analogues; the conditioning on invertible binary matrices affects the leading constant.

## Limitations
The theorem is restricted to characteristic-two field of order two, invertible structure matrices, and matrix-uniform sampling. It does not give the analogous constants for larger fields or for isomorphism-class-uniform sampling. Searches of relevant publications and research records cannot establish unique historical priority; an asymptotic statement buried in older binary-matrix or random-directed-graph literature might overlap. In particular, elementary consequences of existing orbit-count formulas should not be claimed as new without a statement-level comparison.

## References
- A. Elduque and A. Labra, *Evolution algebras, automorphisms, and graphs*, arXiv:1902.02191v1 (2019), https://arxiv.org/abs/1902.02191.
- S. Sriwongsa and Y. M. Zou, *On Automorphism Groups of Idempotent Evolution Algebras*, arXiv:2202.01333v1 (2022), https://arxiv.org/abs/2202.01333.
- Y. Wei and Y. M. Zou, *Isomorphism Classes of Idempotent Evolution Algebras*, arXiv:2310.12368v1 (2023), https://arxiv.org/abs/2310.12368.
- C. Costoya, P. Mayorga and A. Viruel, *Permutation representations and automorphisms of evolution algebras*, arXiv:2401.05924v1 (2024), https://arxiv.org/abs/2401.05924.
