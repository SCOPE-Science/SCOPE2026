# Sharp large-field rigidity and transposition dominance in full-support evolution algebras

## Finding

Fix an integer \(n\ge5\). For each prime power \(q\ge5\), let \(A=(a_{ij})\) be chosen uniformly among invertible \(n\times n\) matrices over \(\mathbb F_q\) whose entries are all nonzero. Equip the vector space with natural basis \(e_1,\ldots,e_n\) and evolution-algebra multiplication \(e_i e_j=0\) for \(i\ne j\), and \(e_i^2=\sum_j a_{ij}e_j\). Write \(E_A\) for this algebra. As \(q\to\infty\) through prime powers, with \(n\) fixed,

\[
\Pr\bigl(\operatorname{Aut}_{\mathbb F_q}(E_A)\ne\{1\}\bigr)
=\binom n2(q-1)^{3-2n}\bigl(1+O_n(q^{-1})\bigr).
\]

Conditionally on a nontrivial automorphism, with probability \(1-O_n(q^{-1})\), the *entire* automorphism group is cyclic of order two and its nonidentity member exchanges exactly two lines of the natural basis. For \(n\ge6\), the conditional error improves to \(O_n(q^{-2})\).

There is also an exact precursor: if \(A\) is uniform among *all*, not necessarily invertible, full-support matrices, then for each prescribed transposition \(\tau\), the probability that some monomial algebra automorphism of \(E_A\) induces \(\tau\) is exactly \((q-1)^{3-2n}\). This last statement concerns monomial automorphisms only when \(A\) is singular.

## Assumptions and scope

An evolution algebra is a commutative, generally nonassociative algebra with a basis whose distinct vectors multiply to zero. An algebra is *idempotent/perfect* here when \(E^2=E\), equivalent to invertibility of its structure matrix. Full support means \(a_{ij}\ne0\) for every ordered pair of indices, including the diagonal. For invertible structure matrices, every algebra automorphism is monomial in a natural basis. In particular, its induced permutation of the natural-basis lines is intrinsic up to simultaneous relabeling. The sampling measure is uniform on labeled full-support invertible structure matrices, *not* uniform on algebra isomorphism classes.

The asymptotic is the large-field limit at fixed dimension \(n\ge5\), not a dimension-growing limit at fixed field. All implied constants may depend on \(n\), never on \(q\). Every sufficiently large prime power is permitted, in either characteristic. The support-complete property is preserved by rescaling and permuting natural basis vectors.

## Proof

**1. Monomial automorphisms and their kernel.** Since \(A\) is invertible, the vectors \(e_i^2\) form a basis. If an automorphism \(g\) has matrix \(P\), then \(g(e_i)g(e_j)=0\) for distinct \(i,j\). Expanding in the basis \(e_k^2\) gives \(P_{ki}P_{kj}=0\) for every \(k\), so invertibility of \(P\) forces exactly one nonzero entry in each row and column. Hence

\[
g(e_i)=c_i e_{\sigma(i)},\qquad c_i\in\mathbb F_q^\times,\quad \sigma\in S_n.
\]

The multiplication rule is preserved precisely when

\[
a_{\sigma(i),\sigma(j)}=\frac{c_j}{c_i^2}a_{ij}
\quad\text{for all }1\le i,j\le n.\tag{1}
\]

For \(\sigma=1\), the diagonal equations \(a_{ii}\ne0\) force \(c_i=c_i^2\), hence \(c_i=1\). Thus the map from the automorphism group to \(S_n\) is injective; in particular, for a given \(\sigma\), at most one scaling vector can work for a fixed full-support matrix. Equation (1) also applies to monomial automorphisms without assuming \(A\) invertible.

**2. Exact transposition stratum before conditioning on invertibility.** Fix \(\tau=(1\ 2)\), and put \(b=q-1\). All indices \(j\ge3\) are fixed by \(\tau\), so their diagonal equations imply \(c_j=1\). Applying (1) successively to \((j,1)\) and \((j,2)\) gives \(c_1c_2=1\). Conversely, for every \(t\in\mathbb F_q^\times\), the vector

\[
(c_1,c_2,c_3,\ldots,c_n)=(t,t^{-1},1,\ldots,1)
\]

satisfies all cycle-consistency conditions for (1). The simultaneous action \((i,j)\mapsto(\tau(i),\tau(j))\) has exactly \(n^2-2n+2\) orbits on ordered pairs: \(2n-2\) of those orbits have length two and all others have length one. Choosing an arbitrary nonzero coefficient at one representative of every orbit, and then extending uniquely by (1), gives exactly \(b^{n^2-2n+2}\) solutions for any fixed \(t\). Different choices of \(t\) cannot describe the same matrix, by the injective-permutation property in step 1. Thus the exact number of full-support matrices with a monomial automorphism projecting to \(\tau\) is

\[
b^{n^2-2n+3},
\]

and the exact probability in the unrestricted full-support model is \(b^{3-2n}\).

**3. Invertibility changes only a relative \(O_n(q^{-1})\).** The determinant is a nonzero polynomial of total degree \(n\) on the coordinate torus of all full-support matrices. It is also a nonzero polynomial on every transposition stratum. To see the latter, first rescale the natural basis by nonzero scalars so that the automorphism of step 2 becomes the pure permutation \(e_1\leftrightarrow e_2\); this rescaling multiplies rows and columns of the structure matrix by units and preserves its rank and full support. On the pure-permutation stratum, the matrix \(I_n+uJ_n\), with \(J_n\) the all-ones matrix, is a full-support witness of invertibility whenever \(u\ne0,-1\) and \(1+nu\ne0\). Such a \(u\) exists for every \(q\ge5\). Therefore the determinant restricted to the free nonzero orbit coordinates is not identically zero. The elementary polynomial zero bound on a product of \(\mathbb F_q^\times\) sets now gives, uniformly over the transposition scalings,

\[
\Pr(\det A=0)=O_n(q^{-1}),\qquad
\Pr(\det A=0\mid\tau\text{ appears})=O_n(q^{-1}).
\]

It follows that for a uniformly selected full-support *invertible* matrix,

\[
\Pr(\tau\text{ appears})=b^{3-2n}\bigl(1+O_n(q^{-1})\bigr).\tag{2}
\]

**4. Every other permutation is negligible.** Suppose a nonidentity \(\sigma\) moves exactly \(k\) indices, \(3\le k\le n\). The diagonal equations for fixed indices force all their scaling factors to one, leaving at most \(b^k\) possible scaling vectors. Let \(d(\sigma)\) be the number of ordered-pair positions minus the number of their orbits under simultaneous \(\sigma\). The \(2k(n-k)\) positions with exactly one moved index have no fixed points, giving orbit deficit at least \(k(n-k)\). The \(k^2\) positions with both indices moved likewise have no fixed points, giving another deficit at least \(k^2/2\). Hence

\[
d(\sigma)\ge nk-k^2/2.
\]

For each fixed scaling vector, equation (1) constrains at least \(d(\sigma)\) independent nonzero coordinate choices. Therefore, before invertibility conditioning,

\[
\Pr(\sigma\text{ appears})\le b^{k-d(\sigma)}.
\]

The integer \(d(\sigma)-k\) is at least \(2n-2\) for every \(n\ge5\) and \(3\le k\le n\). For \(n\ge6\), it is at least \(2n-1\). Indeed, the concave quadratic \(k(n-1-k/2)\) is minimized on \([3,n]\) at an endpoint; the two endpoint bounds, together with integrality, give the stated inequalities. Conditioning on invertibility increases probabilities by at most \(1+O_n(q^{-1})\). A union bound over the finitely many permutations proves

\[
\Pr(\exists\text{ an automorphism inducing a permutation of support}\ge3)
=\begin{cases}O_n(b^{-(2n-2)}),&n=5,\\
O_n(b^{-(2n-1)}),&n\ge6.
\end{cases}\tag{3}
\]

**5. Union of the transposition events.** If two distinct transpositions are represented, their product in the automorphism group induces either a three-cycle or two disjoint transpositions, hence a permutation moving at least three points. Thus all overlaps between distinct transposition events are contained in the event bounded in (3). Summing (2) over the \(\binom n2\) transpositions and applying this overlap bound gives the asserted rare-symmetry probability. Moreover, outside (3), a nontrivial automorphism group can contain only the identity and one transposition, since its projection into \(S_n\) is injective. Dividing (3) by the leading probability of nontrivial symmetry proves the conditional \(O_n(q^{-1})\) error for \(n=5\) and \(O_n(q^{-2})\) for \(n\ge6\). This completes the proof.

## Verification

The standalone file `evolution_fullsupport_checker.py` exhaustively enumerates \(328192\) full-support matrices in three small prime-field cases and verifies the exact prescribed-transposition count by direct substitution in (1). It independently tests matrix invertibility and whether compatible scaling factors are unique. A separate exhaustive permutation-orbit check runs through \(5877\) nonidentity permutations in dimensions five, six, and seven, checking the deficit inequalities used in step 4. Run `python evolution_fullsupport_checker.py`; expected output is in `evolution_fullsupport_checker_output.txt`. The executable computations verify finite instances, not the asymptotic theorem; the asymptotic proof uses the polynomial zero bound and the uniform orbit-deficit argument.

## Relationship to prior work

The monomial-automorphism principle and the structure-matrix equation are standard in the theory of idempotent evolution algebras, especially Sriwongsa–Zou (2022). Wei–Zou (2023) formulate the monomial-group action and apply Burnside's lemma to count all isomorphism classes in fixed dimensions, explicitly through dimension four. Those results are credited; neither an automorphism-group description nor a Burnside first moment by itself supplies the probability of a nontrivial automorphism or the conditional *complete* group law in the full-support, large-field regime. Costoya–Mayorga–Viruel (2024) address realizability of permutation representations rather than this random-model distribution. The 2020 universal-finiteness result demonstrates range of possible groups, not their sampling frequencies. The distinctive result here is the large-field leading exponent and constant, together with transposition dominance despite the associated complete support graph.

## Limitations

The results concern uniform labeled full-support *invertible* matrices and therefore are not assertions for all invertible evolution algebras or for uniformly sampled isomorphism classes. Dimension is fixed before the field size grows; the estimates are not uniform in increasing dimension. The improved \(O_n(q^{-2})\) conditional error is proved only for \(n\ge6\). The manuscript does not give a closed exact formula for the nonsingular count in each transposition stratum at finite \(q\). The baseline monomial action and finite-dimensional Burnside method are known; the novelty assessment is limited to the newly derived sharp random-model law and conditional group classification, subject to possible unindexed prior work. No independent review has been performed.

## References

1. S. Sriwongsa and Y. M. Zou, *On Automorphism Groups of Idempotent Evolution Algebras*, arXiv:2202.01333, first submitted 2022-02-02. https://arxiv.org/abs/2202.01333
2. Y. Wei and Y. M. Zou, *Isomorphism Classes of Idempotent Evolution Algebras*, arXiv:2310.12368, first submitted 2023-10-18; Linear Algebra and its Applications 675 (2023). https://arxiv.org/abs/2310.12368
3. C. Costoya, P. Mayorga and A. Viruel, *Permutation representations and automorphisms of evolution algebras*, arXiv:2401.05924, first submitted 2024-01-11. https://arxiv.org/abs/2401.05924
4. C. Costoya, P. Ligouras, A. Tocino and A. Viruel, *Regular evolution algebras are universally finite*, arXiv:2002.03338, first submitted 2020-02-09. https://arxiv.org/abs/2002.03338
