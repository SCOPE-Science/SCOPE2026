# Maximal hidden-interaction fibers in the universal homogeneous stochastic process

## Finding
Fix a finite state set \(S\) with \(q=|S|\ge 2\), and let \(\mathbf U_S\) be the separable universal ultrahomogeneous non-degenerate \(S\)-valued stochastic process of Bryant, Nies, and Tupper. For every \(n\ge 3\), consider injective ordered \(n\)-tuples and forget their full automorphism orbit while retaining the automorphism orbit of every proper coordinate subtuple.

The fiber over the datum in which every proper subtuple has the independent uniform law is naturally identified with
\[
\mathcal P_{q,n}=\left\{p\in\Delta(S^n):\text{ every }(n-1)\text{-coordinate marginal is uniform on }S^{n-1}\right\}.
\]
Its affine dimension is exactly
\[
\dim \mathcal P_{q,n}=(q-1)^n.
\]
Consequently this single proper-subtuple orbit profile has \(2^{\aleph_0}\) distinct full \(n\)-tuple orbits above it. This is the largest possible cardinality of such a fiber because the index set of \(\mathbf U_S\) is separable metric and therefore has cardinality at most \(2^{\aleph_0}\).

For \(q=2\), an explicit one-parameter subfamily is
\[
p_\theta(x_1,\ldots,x_n)=2^{-n}\left(1+\theta(-1)^{x_1+\cdots+x_n}\right),\qquad -1<\theta<1.
\]
All proper marginals are independent fair bits, while distinct values of \(\theta\) give distinct full tuple orbits.

## Assumptions and scope
The state space \(S\) is finite, with \(q\ge2\), and \(\mathbf U_S\) denotes the universal ultrahomogeneous process supplied by the cited Fraïssé-limit construction. Tuples are injective ordered tuples of indices. The claim concerns reconstruction of a full tuple orbit from the collection of all proper coordinate-subtuple orbits. It does not assert that the linear-algebra fact about fixed-marginal probability tables is itself new.

The restriction \(n\ge3\) keeps the intended “all proper subtuples” interpretation nontrivial and guarantees immediately that every pair marginal in the displayed fiber is independent uniform. The same tensor-kernel calculation is valid already for \(n=2\).

## Proof
Bryant, Nies, and Tupper encode an \(S\)-valued process as a relational metric structure whose predicates are its finite-dimensional probabilities. Their notion of embedding is equality of the finite-dimensional distributions after relabeling indices, and their limit is universal and ultrahomogeneous. Therefore two injective ordered finite tuples of \(\mathbf U_S\) are in the same automorphism orbit exactly when their full joint \(S\)-valued laws agree: equality of the full joint law gives equality of all lower-dimensional predicates by marginalization, hence a finite partial isomorphism, which ultrahomogeneity extends to an automorphism; the converse is immediate from preservation of predicates.

Now fix \(n\) and the independent uniform law \(u\) on \(S^n\). Write a candidate law as \(p=u+h\). Let
\[
V=\mathbb R^S=\mathbb R\mathbf 1\oplus W,
\qquad
W=\left\{v\in\mathbb R^S:\sum_{s\in S}v(s)=0\right\},
\]
so \(\dim W=q-1\). Identify real arrays on \(S^n\) with \(V^{\otimes n}\). Requiring the marginal obtained by summing out coordinate \(i\) to agree with the corresponding uniform marginal is precisely the condition that \(h\) lie in the kernel of contraction by the all-ones functional in the \(i\)-th tensor factor. That kernel is
\[
V^{\otimes(i-1)}\otimes W\otimes V^{\otimes(n-i)}.
\]
Intersecting these kernels over all coordinates gives
\[
W^{\otimes n},
\]
because in the direct-sum expansion of \((\mathbb R\mathbf1\oplus W)^{\otimes n}\), surviving every coordinate-sum constraint requires a \(W\) factor in every position. Hence the affine solution space has dimension
\[
\dim W^{\otimes n}=(q-1)^n.
\]

The uniform law is strictly positive. Therefore a sufficiently small neighborhood of \(u\) inside the affine space \(u+W^{\otimes n}\) remains inside the probability simplex. Thus \(\mathcal P_{q,n}\) has nonempty relative interior and cardinality continuum.

Every law in \(\mathcal P_{q,n}\) has independent uniform pair marginals, so for distinct coordinates \(i\ne j\),
\[
\Pr[X_i\ne X_j]=1-\frac1q>0.
\]
It is therefore a finite non-degenerate process. Universality embeds it into \(\mathbf U_S\). Distinct laws give distinct full tuple orbits by the orbit-law criterion above, whereas every proper subtuple has the independent uniform law and therefore the same proper-subtuple orbit. This proves that the stated fiber is exactly \(\mathcal P_{q,n}\) and has continuum many full orbits.

Finally, a separable metric space has cardinality at most continuum, so its set of ordered \(n\)-tuples, and hence any orbit fiber, has cardinality at most \(2^{\aleph_0}\). The constructed fiber is therefore cardinally maximal.

## Verification
A standalone exact-arithmetic checker accompanies this note. It forms the linear system saying that every one-coordinate marginal perturbation vanishes and computes its nullity over the rationals for several \((q,n)\) pairs. The observed nullities are \(1,1,8,16,27\) for \((2,3),(2,4),(3,3),(3,4),(4,3)\), respectively, matching \((q-1)^n\). It also checks the binary parity family exactly for several arities and rational values of \(\theta\). The checker ends with `VERIFY_OK`.

These computations are sanity checks only. The general result follows from the tensor decomposition and the universal-ultrahomogeneous property, not from finite enumeration.

## Relationship to prior work
Bryant, Nies, and Tupper construct the unique separable universal ultrahomogeneous stochastic process on any fixed finite state set. They explicitly encode finite-dimensional distributions as predicates, prove that the class of finite non-degenerate processes has a unique Fraïssé limit, and state the resulting universal ultrahomogeneous process. Those ingredients make the finite joint law a complete invariant of an injective tuple orbit.

The probability-theoretic phenomenon that a highest-order interaction can vary while all proper marginals stay fixed is classical and appears in many forms, including parity constructions. The additional conclusion here is model-theoretic: in this canonical homogeneous process the entire fixed-marginal polytope is realized as one fiber of the proper-subtuple orbit map, with exact affine dimension \((q-1)^n\) and maximal possible orbit-cardinality \(2^{\aleph_0}\).

Targeted searches for formulations in terms of automorphism orbits, proper-subtuple reconstruction, hidden interactions, and the universal ultrahomogeneous stochastic process did not locate this orbit-fiber statement. The nearest indexed findings concerned statistical consequences of pure higher-order dependence or exact orbit profiles of unrelated homogeneous structures; neither implies this theorem.

## Limitations
The originality conclusion is search-based, not a proof of priority. The tensor dimension of the fixed-marginal family is standard linear algebra and may also be recorded in contingency-table or hierarchical-model literature. The potentially new content is the exact identification of that family with a maximal automorphism-orbit fiber in the universal homogeneous stochastic process. A short version of this corollary may exist as folklore or in literature not captured by the searches performed.

No claim is made here about fibers over arbitrary nonuniform proper-marginal data, about classification of all tuple-orbit fibers, or about infinite state spaces.

## References
1. David Bryant, André Nies, and Paul Tupper, “Fraïssé Limits for Relational Metric Structures,” arXiv:1901.02122, first posted 8 January 2019; *The Journal of Symbolic Logic* 86(3) (2021), 913–934, DOI 10.1017/jsl.2021.65. See the stochastic-process construction, especially Definition 18, Theorem 19, and Corollary 20.
2. Standard finite-dimensional probability and tensor-product linear algebra for marginalization; used here only for the kernel calculation \(\bigcap_i\ker M_i=W^{\otimes n}\).
