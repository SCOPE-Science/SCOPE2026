# Sharp seven-measure upper bound for the three-state Potts model on the order-three Cayley tree
## Finding
Consider the ferromagnetic three-state Potts model with constant external field on the Cayley tree of order \(k=3\), in the notation and normalization of Bogachev and Rozikov. Let \(\nu(\theta,\alpha)\) denote the number of positive completely homogeneous boundary-law solutions of their system (2.31). Then, for every \(\theta\ge 1\) and \(\alpha\in\mathbb R\),
\[
\nu(\theta,\alpha)\le 7=2^3-1.
\]
The bound is sharp: when \(\alpha=0\), the source proves that exactly seven solutions occur for all sufficiently large \(\theta\).

The new part is the arbitrary-field case \(\theta>1\), \(\alpha\ne0\). For \(q=3\) and \(k=3\), every mixed solution is governed by the source function \(K_1(v;\theta)\). Put
\[
x=v+v^{-1}.
\]
On its positive domain, \(x<\theta\). For \(v>1\), differentiation gives
\[
\operatorname{sgn} K_1'(v;\theta)
=
\operatorname{sgn}R_\theta(x),
\qquad
R_\theta(x)=-2x^2+(2\theta-6)x+5\theta-1.
\]
The quadratic \(R_\theta\) has at most one zero on \(2<x<\theta\). Hence every positive horizontal level of \(K_1\) has at most two roots with \(v>1\), and reciprocal symmetry gives at most four admissible roots \(v\ne1\) in total. The remaining single-colour branch has at most three positive solutions by the source's Theorem 2.8. Thus \(\nu(\theta,\alpha)\le3+4=7\).

This proves Conjecture 2.2 of the motivating paper for the first arbitrary-field tree order beyond its \(k=2\) theorem, namely \(q=3\), \(k=3\).

## Assumptions and scope
The interaction is ferromagnetic and nearest-neighbour, the field is the constant field parameterized by \(\alpha\) in Bogachev--Rozikov, and only completely homogeneous splitting Gibbs measures represented by positive normalized boundary laws are counted. The Cayley tree has order \(k=3\), so each vertex has degree four. The statement does not classify nonhomogeneous splitting measures, periodic measures, weakly periodic measures, or arbitrary Gibbs measures outside the source's completely homogeneous reduction.

The endpoint \(\theta=1\) is included because Lemma 5.1(a) of the source gives the unique normalized positive solution. The zero-field case \(\alpha=0\) is not reproved: Theorem 2.11(b) of the source already establishes the bound \(2^q-1\) for every tree order and shows sharpness at sufficiently large \(\theta\). The proof below therefore addresses \(\theta>1\) and \(\alpha\ne0\).

## Proof
For \(q=3\), Lemma 5.1(c) of the source splits every positive solution into two disjoint types. The single-colour type has boundary law \(z_1=u\), \(z_2=1\), with \(u\) solving the scalar equation (5.4). By Theorem 2.8, this scalar equation has at most three positive roots.

For the mixed type, there is only one possible subset index, \(m=1\), because \(q-2=1\). The source reduction (5.22)--(5.25) is reversible on positive solutions and gives
\[
\theta^\alpha=K_1(v;\theta),
\qquad
u=\frac{p(v)+L(v;\theta)}{p(v)+1},
\]
where, for \(k=3\),
\[
p(v)=v+v^2,
\qquad
L(v;\theta)=(\theta-1)(v+v^2)-v^3-1.
\]
Factor \(L\) exactly:
\[
L(v;\theta)=(v+1)(\theta v-v^2-1)
=v(v+1)\bigl(\theta-(v+v^{-1})\bigr).
\]
Hence the physical mixed-branch domain \(L>0\) is nonempty exactly when \(\theta>2\), and on that domain
\[
2\le x:=v+v^{-1}<\theta.
\]
At \(v=1\) the mixed system is inadmissible, so only \(x>2\) matters for mixed solutions.

The source defines
\[
K_1(v;\theta)
=
\frac{L(v;\theta)(p(v)+1)^3}{(p(v)+L(v;\theta))^3}.
\]
Because \(q=3\) has \(m=m'=1\), Lemma 6.6 gives the reciprocal identity
\[
K_1(v;\theta)=K_1(v^{-1};\theta).
\]
Using the source derivative formula (6.23), direct expansion of its numerator gives
\[
(\theta+2)(v-1)(v+1)v^2R_\theta(v+v^{-1}),
\]
where
\[
R_\theta(x)=-2x^2+(2\theta-6)x+5\theta-1.
\]
All omitted factors in (6.23) are strictly positive on \(L>0\). Thus, for \(v>1\), the sign of \(K_1'(v;\theta)\) is exactly the sign of \(R_\theta(x)\).

It remains to count zeros of \(R_\theta\) on \(2<x<\theta\). At the endpoints,
\[
R_\theta(2)=3(3\theta-7),
\qquad
R_\theta(\theta)=-(\theta+1)<0.
\]
Also
\[
R_\theta'(x)=-4x+2\theta-6,
\]
so its vertex is at \(x_0=(\theta-3)/2\). If \(2<\theta\le7/3\), then \(R_\theta(2)\le0\) and \(R_\theta\) is strictly decreasing for \(x\ge2\), hence there is no zero in the physical interval. If \(7/3<\theta\le7\), the vertex lies at or to the left of \(2\), so \(R_\theta\) is strictly decreasing on \(x>2\) and has exactly one zero before \(x=\theta\). If \(\theta>7\), the quadratic first increases from the positive value \(R_\theta(2)\), reaches its maximum at \(x_0>2\), and then decreases to the negative value \(R_\theta(\theta)\); again it has exactly one zero in \(2<x<\theta\).

Therefore \(K_1\) is either strictly decreasing on the \(v>1\) half of the physical interval or increases once and then decreases once. A positive horizontal level \(K_1(v;\theta)=\theta^\alpha\) consequently has at most two roots with \(v>1\). Reciprocal symmetry pairs every such root with a root in \(0<v<1\), so the mixed branch contributes at most four admissible roots. Formula (5.24) determines \(u\) uniquely from each such \(v\); the additional source restrictions \(u\ne1\), \(u\ne v\), and \(v\ne1\) can only reduce the count.

Combining the at-most-three single-colour roots with the at-most-four mixed roots yields
\[
\nu(\theta,\alpha)\le 7.
\]
Together with the source's zero-field theorem and its sharpness statement, this proves the claimed all-field bound for \(q=3\), \(k=3\).

## Verification
The proof is analytic on the full parameter domain. The only nontrivial new algebra is the factorization of \(L\) and of the numerator in the derivative formula (6.23), followed by a complete sign analysis of one quadratic on the interval \(2<x<\theta\). The bundled `verify.py` uses only the Python standard library and replays the polynomial identities exactly with integer-coefficient bivariate polynomial arithmetic. Its finite rational spot checks are supplementary and are not used to infer the global zero count.

A fresh replay from the packaged path must print `VERIFY_OK`. The global step is proved in the text from the exact endpoint values, vertex location, and concavity of \(R_\theta\), not from numerical sampling.

## Relationship to prior work
Bogachev and Rozikov prove the universal bound \(2^q-1\) for zero field at every order and for arbitrary field when \(k=2\), then state Conjecture 2.2 that the same upper bound is universal. Their proof of the arbitrary-field \(k=2\) case uses only that equation (5.25) is quartic, giving at most four mixed roots. For \(q=3\), \(k=3\), equation (5.25) is no longer covered by that degree-four argument. The present proof instead exploits the special reciprocal structure of the three-state mixed branch and shows that its derivative has only one possible turning point on each reciprocal half-domain.

Khakimov and Khaidarov treat the ferromagnetic three-state Potts model on the Cayley tree of order three and give explicit translation-invariant measures in the zero-field setting. That result is consistent with, but does not imply, the arbitrary constant-field bound proved here. Rozikov's later survey likewise reviews the zero-field Potts classification and the Bogachev--Rozikov external-field problem; no all-field \(q=3\), \(k=3\) seven-solution theorem was located in the inspected literature or database searches.

## Limitations
The theorem resolves only the \(q=3\), \(k=3\) instance of the source's universal upper-bound conjecture. It does not prove Conjecture 2.2 for \(k\ge4\) with nonzero field or for \(q\ge4\) outside the cases already covered by the source. It counts completely homogeneous splitting solutions in the source normalization, not all Gibbs measures on the tree. The originality search cannot exclude a weakly indexed equivalent proof under different fixed-point notation; this remains the principal residual literature risk.

## References
1. L. V. Bogachev and U. A. Rozikov, *On the uniqueness of Gibbs measure in the Potts model on a Cayley tree with external field*, arXiv:1903.11440v1; J. Stat. Mech. Theory Exp. (2019) 073205, DOI:10.1088/1742-5468/ab270b.
2. R. M. Khakimov and F. Kh. Khaidarov, *Translation-invariant and periodic Gibbs measures for the Potts model on a Cayley tree*, Theoret. Math. Phys. 189 (2016), 1651--1659, DOI:10.1134/S004057791611009X.
3. U. A. Rozikov, *Gibbs measures of Potts model on Cayley trees: a survey and applications*, Rev. Math. Phys. 33 (2021), 2130007, arXiv:2103.07391v1.
