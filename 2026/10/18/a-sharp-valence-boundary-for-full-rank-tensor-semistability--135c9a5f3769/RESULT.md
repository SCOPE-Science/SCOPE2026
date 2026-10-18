# A sharp valence boundary for full-rank tensor semistability

## Finding

Let \(d\ge2\) and \(m\ge2\) be integers. Consider \(V_{d,m}=(\mathbb C^d)^{\otimes m}\) with the factorwise action of \(G=\prod_{j=1}^m\mathrm{GL}_d(\mathbb C)\), and the standard positive central moment parameter used for the one-hyperedge Kähler hyperquiver quotient in [1, Section 3]. Write \(U_{d,m}\subset V_{d,m}\) for the open locus of tensors whose flattening in each of the \(m\) tensor modes has rank \(d\). Call such tensors *concise* or *of full multilinear rank*.

**Theorem (exact valence boundary).** For every \(d\ge2\):

1. If \(m=2\), every member of \(U_{d,2}\) is semistable (indeed polystable) for this central parameter.
2. If \(m\ge3\), there is an explicit symmetric member \(T_{d,m}\in U_{d,m}\) whose orbit closure under \(H=\prod_{j=1}^m\mathrm{SL}_d(\mathbb C)\) contains \(0\). Consequently, \(T_{d,m}\) is **not semistable** for the positive central character.

For \(m\ge3\), one choice is the symmetric polarization of the homogeneous polynomial
\[
 F_{d,m}(x_0,\ldots,x_{d-1})=
 x_0^{m-1}x_{d-1}+x_0^{m-2}\sum_{i=1}^{d-2}x_i^2.
\]
The summation is empty when \(d=2\). Thus equality between the full-rank locus and the semistable locus holds throughout the equal-dimension **bilinear** family but fails for every equal-dimension **multilinear** family of valence at least three. In particular, the criterion asserted in [1, Proposition 3.3] does not hold in these formats. It fails even in the finite-generic-stabilizer range \(2d<d^{m-1}\) of [1, Proposition 3.4].

## Assumptions and scope

Work over \(\mathbb C\), use the usual diagonal action of \(\prod \mathrm{GL}_d\) on tensor factors, and use the Kähler/GIT linearization corresponding to the positive central level \(c^j(T,T)=I_d\) in [1, Equation (3.1)]. Quotienting the ineffective central subtorus does not change the orbits or the following null-cone obstruction. Semistability here is relative to that specific central linearization, not an unqualified statement about arbitrary choices of weights or character.

A tensor is of full multilinear rank if each linear map \((\mathbb C^d)^*\to(\mathbb C^d)^{\otimes(m-1)}\), formed by contraction in one mode, is injective.

## Proof

**1. A family with full multilinear rank.** For \(m\ge3\), let \(T_{d,m}\) be the unique symmetric tensor whose diagonal contraction is \(F_{d,m}\). The vector spaces of slices of a symmetric tensor are identified, up to the harmless nonzero scalar \(m\), with the span of the first partial derivatives of its diagonal polynomial. Here these derivatives are
\[
 \begin{aligned}
 \partial_{x_{d-1}}F_{d,m}&=x_0^{m-1},\\
 \partial_{x_i}F_{d,m}&=2x_0^{m-2}x_i \quad(1\le i\le d-2),\\
 \partial_{x_0}F_{d,m}&=(m-1)x_0^{m-2}x_{d-1}
 +(m-2)x_0^{m-3}\sum_{i=1}^{d-2}x_i^2.
 \end{aligned}
\]
They are linearly independent: the last derivative is the only one involving \(x_{d-1}\), and the remaining derivatives are distinct monomials. Therefore every flattening has rank \(d\). The same argument covers the empty sum at \(d=2\).

**2. A strictly positive one-parameter weight in all dimensions.** For \((d,m)\ne(3,3)\), set
\[
 \lambda_d(t)=\operatorname{diag}(t^{d-1},t^{-1},\ldots,t^{-1})\in\mathrm{SL}_d(\mathbb C)
\]
and act by \(\lambda_d(t)\) in **every** tensor factor. The first monomial of \(F_{d,m}\) has weight \((m-1)(d-1)-1\), which is positive. Each monomial in the sum has weight \((m-2)(d-1)-2\). For \(d=2\) the sum is empty; for \(d\ge4,m\ge3\) the second weight is at least \(1\); and for \(d=3,m\ge4\) it is at least \(2\). Thus all nonzero coordinates of \(T_{d,m}\) have strictly positive weights.

For the sole remaining pair \((d,m)=(3,3)\), use
\[
 \lambda_3(t)=\operatorname{diag}(t^2,1,t^{-2}).
\]
Both terms of \(F_{3,3}=x_0^2x_2+x_0x_1^2\) then have weight \(2\). In every case,
\[
 \lim_{t\to0}\lambda_d(t)^{\otimes m}T_{d,m}=0.
\]
This is an algebraic one-parameter subgroup inside \(\prod_j\mathrm{SL}_d\), and proves that the origin lies in the \(H\)-orbit closure of a full-rank tensor.

**3. Why this excludes the positive-central semistable locus.** Every semi-invariant section defining semistability for the stated positive central linearization restricts to an \(H\)-invariant homogeneous polynomial, because every character of \(G\) is trivial on \(H\). An \(H\)-invariant homogeneous polynomial of positive degree must vanish at \(T_{d,m}\), since its value is constant on the \(H\)-orbit and therefore, by the displayed degeneration, equals its value at the origin, namely zero. Hence no positive-character semi-invariant is nonzero at \(T_{d,m}\); by the usual affine GIT semistability criterion, \(T_{d,m}\) is not semistable. Equivalently, a tensor admitting \(0\) in its \(H\)-orbit closure cannot have a \(G\)-translate satisfying the prescribed balanced moment-map equations (Kempf--Ness).

**4. Sharpness at two factors.** For \(m=2\), full multilinear rank means an invertible \(d\times d\) matrix. The factorwise \(\mathrm{GL}_d\times\mathrm{GL}_d\) action carries every invertible matrix to \(I_d\). The latter has \(c^1(I_d,I_d)=c^2(I_d,I_d)=I_d\) and hence belongs to the central moment level. Thus every full-rank bilinear tensor is polystable. The threshold from valence \(2\) to valence \(3\) is exact.

## Verification

The accompanying `verify_hyperquiver_valence.py` constructs symmetric coefficient arrays over the integers for \(16\) pairs of small dimensions and valences. For every tested pair it checks that all \(m\) flattenings have rank \(d\), that the specified one-parameter subgroup has determinant one, and that every nonzero tensor coefficient has strictly positive weight. Its expected output is `HYPERQUIVER_FULL_RANK_NULLCONE_EXACT_OK 16 test_formats`. The infinite-family proof is the polynomial derivative calculation and weight inequality above; finite checks are only independent consistency tests.

## Relationship to prior work

Bielawski [1, Proposition 3.3] asserts that for balanced dimension vectors the semistable and polystable loci coincide with the tensors of maximal multilinear rank. The counterexamples above directly test that statement for the equal-dimension balanced vectors. Proposition 3.4 there separately gives a generic finite-stabilizer criterion; this criterion does not remove the counterexamples. Muller, Nanda and Seigal [2] introduce the hyperquiver representation formalism and study singular vectors, not this sharp GIT valence criterion. The familiar three-qubit W/GHZ distinction and hyperdeterminant classification [3] already show a dimension-two trivalent instability phenomenon; they are **not** claimed as new here. The contribution here is the complete all-\(d\), all-\(m\) sharp boundary for sufficiency of full multilinear rank in the balanced one-hyperedge GIT problem, with one uniform algebraic witness family.

## Limitations

The theorem says neither that every full-rank tensor is unstable for \(m\ge3\) nor that the Kähler quotient is empty. Its conclusion concerns sufficiency of the rank criterion, not the complete GIT stability classification or the geometry of the actual quotient. General null-cone criteria in invariant theory may imply related examples; possible historical implicit coverage remains a literature risk. The exact first public date supplied for the motivating paper is from the dated arXiv version.

## References

1. R. Bielawski, *Hyperquiver varieties*, arXiv:2610.12261v1 (first public 2026-10-08), Section 3, Propositions 3.3 and 3.4. https://arxiv.org/html/2610.12261v1
2. T. Muller, V. Nanda and A. Seigal, *Multilinear Hyperquiver Representations*, arXiv:2305.05622v3, especially the introduction and its main theorem. https://arxiv.org/html/2305.05622v3
3. A. Miyake, *Classification of multipartite entangled states by multidimensional determinants*, arXiv:quant-ph/0206111 (2002). https://arxiv.org/abs/quant-ph/0206111
4. H. Jaffali, F. Holweck and L. Oeding, *Maximally entangled real states and SLOCC invariants: the 3-qutrit case*, J. Phys. A 57 (2024), 145301, doi:10.1088/1751-8121/ad3193.
