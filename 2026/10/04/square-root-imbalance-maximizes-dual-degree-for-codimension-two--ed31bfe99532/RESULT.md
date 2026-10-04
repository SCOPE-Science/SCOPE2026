# Square-root imbalance maximizes dual degree for codimension-two complete-intersection threefolds
## Finding
Let \(X_{d,e}\subset \mathbb P^5_\mathbb C\) be a smooth complete-intersection threefold cut out by hypersurfaces of degrees \(2\le d\le e\). Write
\[
q=d+e-2,\qquad s=e-d.
\]
Then \(s\equiv q\pmod 2\) and \(0\le s\le q-2\). The projective dual \(X_{d,e}^\vee\) is a hypersurface, and
\[
\deg X_{d,e}^\vee
=de\bigl((d-1)^3+(d-1)^2(e-1)+(d-1)(e-1)^2+(e-1)^3\bigr)
=\frac q8\bigl(((q+2)^2-s^2)(q^2+s^2)\bigr).
\]
For each fixed \(q\), the maximum is attained exactly by those admissible \(s\) that minimize
\[
\left|s^2-2(q+1)\right|.
\]
There is a unique maximizing bidegree except when
\[
q=2k(k+1),\qquad k\ge2.
\]
In that exceptional case exactly two bidegrees tie:
\[
(d,e)=\bigl(k^2+1,(k+1)^2\bigr),\qquad
(d,e)=\bigl(k^2,(k+1)^2+1\bigr).
\]
Moreover, along any sequence of maximizing bidegrees with \(q\to\infty\),
\[
\frac{e-d}{\sqrt{2(d+e-2)}}\longrightarrow1.
\]
Thus the dual-degree maximizer at fixed adjunction coefficient is asymptotically close to balanced in relative terms, but has a systematic square-root-sized degree gap.

## Assumptions and scope
The ground field is \(\mathbb C\). The variety is assumed smooth and nondegenerate, with codimension two and dimension three in \(\mathbb P^5\). The lower bounds \(d,e\ge2\) exclude redundant hyperplane factors. Fixing \(q=d+e-2\) fixes the coefficient in the adjunction identity
\[
K_{X_{d,e}}\cong \mathcal O_{X_{d,e}}(q-4).
\]
The theorem compares all smooth complete-intersection types with that fixed degree sum; it does not assert that their canonical volumes or Hilbert polynomials agree.

## Proof
Let \(H=c_1(\mathcal O_X(1))\), and set \(x=d-1\), \(y=e-1\). For a smooth complete intersection,
\[
N^*_{X/\mathbb P^5}(1)\cong \mathcal O_X(-x)\oplus\mathcal O_X(-y).
\]
The Katz--Kleiman dual-degree formula, in the normal-bundle form recorded by Kleiman and by Tevelev, gives
\[
\deg X^\vee=\int_X\frac1{c(N^*_{X/\mathbb P^5}(1))}.
\]
Kleiman also notes directly that a nonlinear smooth complete intersection has nonzero dual class, hence dual hypersurface. Expanding only through degree three,
\[
\frac1{(1-xH)(1-yH)}
=1+(x+y)H+(x^2+xy+y^2)H^2+(x^3+x^2y+xy^2+y^3)H^3+\cdots.
\]
Since \(\int_X H^3=de=(x+1)(y+1)\),
\[
\deg X^\vee=(x+1)(y+1)(x^3+x^2y+xy^2+y^3).
\]
Put \(q=x+y\), \(p=xy\), and \(s=y-x\). Then
\[
x^3+x^2y+xy^2+y^3=q(q^2-2p),\qquad (x+1)(y+1)=p+q+1,
\]
and \(p=(q^2-s^2)/4\). Substitution yields
\[
\deg X^\vee
=\frac q8\bigl(((q+2)^2-s^2)(q^2+s^2)\bigr).
\]
A second expansion gives the decisive completed square:
\[
\deg X^\vee
=\frac q8\left(q^2(q+2)^2+4(q+1)^2-\bigl(s^2-2(q+1)\bigr)^2\right).
\]
For fixed \(q\), every term except the final square is constant, so maximization is equivalent to minimizing \(\lvert s^2-2(q+1)\rvert\) on the parity lattice \(s\equiv q\pmod2\), \(0\le s\le q-2\).

Because \(s^2\) is strictly increasing for \(s\ge0\), there can be at most two minimizers, and two occur only for adjacent admissible values \(s,s+2\). They tie exactly when
\[
2(q+1)=\frac{s^2+(s+2)^2}2,
\]
which reduces to \(2q=s(s+2)\). Integrality forces \(s=2k\), and then \(q=2k(k+1)\). The second adjacent value is admissible exactly for \(k\ge2\). Converting back from \((q,s)\) to \((d,e)\) gives the two displayed bidegrees.

Finally, for large \(q\), the upper endpoint \(q-2\) lies beyond \(\sqrt{2(q+1)}\), and the parity lattice has mesh two. Hence every minimizing \(s\) satisfies
\[
s=\sqrt{2(q+1)}+O(1),
\]
which implies the stated asymptotic ratio.

## Verification
The standalone exact-arithmetic program `artifacts/verify_dual_degree_mode.py` checks, for every \(2\le q\le2000\), all one million admissible pairs \((q,s)\). It independently compares the direct Chern-class formula with the factored formula, verifies that the degree maximizers are exactly the minimizers of \(\lvert s^2-2(q+1)\rvert\), and checks the complete tie classification \(q=2k(k+1)\), \(k\ge2\). It also checks \(\deg X_{2,2}^\vee=16\), \(\deg X_{2,4}^\vee=320>288=\deg X_{3,3}^\vee\), and the first tie at \(q=12\), namely \((5,9)\) and \((4,10)\). The finite computation is regression evidence only; the theorem for all \(q\) is proved symbolically above.

## Relationship to prior work
Kleiman develops the projective-duality class formula and derives
\[
d^\vee=\int_X\frac1{c(N(1))},
\]
with the relevant convention for the conormal bundle, and explicitly states that nonlinear smooth complete intersections have nonzero dual class. Tevelev restates the Katz--Kleiman--Holme formula as
\[
\deg\Delta_X=\int_X\frac1{c(N^*_{X/\mathbb P^N}(1))}
\]
and notes that nondegenerate smooth complete intersections have dual hypersurfaces. These sources determine the degree for each fixed bidegree. The new statement is the exact cross-bidegree optimization at fixed \(d+e\): the completed-square reduction, the square-root imbalance law, and the exceptional two-maximizer sequence \(q=2k(k+1)\). Searches for complete-intersection dual degrees, discriminant degrees, fixed degree sums, and imbalance/extremal formulations did not locate a source stating or implying this optimization theorem.

## Limitations
The theorem is restricted to smooth complex codimension-two complete-intersection threefolds in \(\mathbb P^5\). It does not cover singular complete intersections, degree-one factors, higher codimension, or other dimensions. The originality assessment is bounded by the inspected primary literature and the recorded semantic and web searches; an equivalent extremal statement could exist under terminology not encountered there. The verification program samples a large finite range but is not used to infer the infinite theorem.

## References
1. S. L. Kleiman, *The Enumerative Theory of Singularities*, in *Real and Complex Singularities, Oslo 1976*, Sijthoff and Noordhoff, 1977, pp. 297--396. DOI: 10.1007/978-94-010-1289-8_10. See Chapter IV.D, especially formulas (IV,63)--(IV,70) and the complete-intersection discussion on p. 362.
2. E. A. Tevelev, *Projectively Dual Varieties*, arXiv:math/0112028, first submitted 3 December 2001. See §7.1, Theorem 7.2 and Examples 7.3--7.4.
