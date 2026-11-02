# Elliptic-trace profiles and exact variance for squarefree cubic pairs under quadratic shifts

## Finding
Fix any odd prime power \(q\). For \(u\in\mathbb F_q^\times\), \(v,w\in\mathbb F_q\), put
\[
h(T)=uT^2+vT+w,\qquad \Delta=v^2-4uw,\qquad t=\frac{4\Delta}{u^4}.
\]
Let \(C_q(h)\) be the number of monic cubics \(f\in\mathbb F_q[T]\) for which both \(f\) and \(f+h\) are squarefree; let \(B_q(h)=C_q(h)-q^3+2q^2\), the number for which **both** are non-squarefree. With \(\chi\) the quadratic character extended by \(\chi(0)=0\), the following exact profile holds:
\[
B_q(h)=q-1+\sum_{z\in\mathbb F_q^\times}\chi(z^3+z^2+t)+q\mathbf 1_{t=0}.
\tag{1}
\]
Consequently \(C_q(h)=q^3-2q^2+B_q(h)\). In particular \(B_q(h)\) depends only on the normalized discriminant \(t\), not separately on the three coefficients of \(h\).

For \(t=0\), \(B_q(h)=2q-2\). When the characteristic is not three and \(t=-4/27\),
\[
B_q(h)=q-1-\chi(-1)-\chi(-3).
\tag{2}
\]
For every other \(t\), the smooth elliptic curve \(E_t:y^2=z^3+z^2+t\) has Frobenius trace \(a_q(E_t)=q+1-\#E_t(\mathbb F_q)\), and
\[
B_q(h)=q-1-\chi(t)-a_q(E_t),
\qquad \bigl|B_q(h)-(q-1-\chi(t))\bigr|\le2\sqrt q.
\tag{3}
\]
The exclusion \(t=-4/27\) in (3) is needed only when three is invertible. In characteristic three, all \(t\ne0\) yield smooth curves.

There is also an exact shift-distribution law. For each fixed \(u\ne0\) and \(v\), when \(w\) ranges uniformly over \(\mathbb F_q\),
\[
\frac1q\sum_{w\in\mathbb F_q}B_q(uT^2+vT+w)=q,
\tag{4}
\]
\[
\frac1q\sum_{w\in\mathbb F_q}\bigl(B_q(uT^2+vT+w)-q\bigr)^2
=2q-6-\chi(-3)+\mathbf1_{\operatorname{char}\mathbb F_q=3}-\frac1q.
\tag{5}
\]
In particular the mean squarefree-pair count is exactly \(q(q-1)^2\), its independent-marginals benchmark, although individual quadratic shifts have nontrivial elliptic fluctuations and a larger singular-discriminant contribution.

## Assumptions and scope
All assertions concern arbitrary odd prime powers, including nonprime fields and characteristic three, monic cubics, and shifts of **exactly degree two** with \(u\ne0\). A polynomial is squarefree if no nonconstant polynomial square divides it. The character \(\chi\) is defined on all of \(\mathbb F_q\); positive integer cardinalities include all monic cubics \(T^3+aT^2+bT+c\). In (4) and (5) the population is the \(q\) shifts obtained by varying \(w\), rather than the population of cubics \(f\).

## Proof
**1. Counting the simultaneous nonsquarefree locus.** Every non-squarefree monic cubic over a field is uniquely \((T-r)^2(T-s)\), where \(r,s\in\mathbb F_q\). Indeed a repeated irreducible factor of degree at least two would have total degree at least four. The repeated root \(r\) is unique even if \(r=s\). Thus there are exactly \(q^2\) such cubics.

Suppose \(f=(T-r)^2(T-s)\) and \(f+h\) has repeated root \(x\). Put \(d=x-r\). If \(d=0\), then \(h(x)=h'(x)=0\). Since \(u\ne0\) and the characteristic is odd, this happens at a unique \(x\) exactly when \(\Delta=0\). For that \(x\), any \(s\) works, giving \(q\mathbf1_{\Delta=0}\) cubics.

If \(d\ne0\), the two equations \((f+h)(x)=(f+h)'(x)=0\) read
\[
d^2(x-s)=-h(x),\qquad 2d(x-s)+d^2=-h'(x).
\]
The first determines \(s\) uniquely and the second is equivalent to
\[
d^3+d h'(x)-2h(x)=0.
\]
After inserting \(h(x)=ux^2+vx+w\), this is a quadratic equation in \(x\) with nonzero leading coefficient \(-2u\) and discriminant
\[
4\bigl(2ud^3+u^2d^2+v^2-4uw\bigr).
\]
The number of \(x\) is therefore \(1+\chi(2ud^3+u^2d^2+\Delta)\). Summing over \(d\ne0\) and adding the \(d=0\) class gives \(B_q\). Set \(d=uz/2\): the factor \(u^4/4\) is a square, yielding (1). Inclusion–exclusion of the two \(q^2\)-element nonsquarefree loci yields the stated formula for \(C_q\). There is no uncounted overlap, because each nonsquarefree cubic has a unique repeated root.

**2. Singular and elliptic cases.** Put \(P_t(z)=z^3+z^2+t\) and \(A_q(t)=\sum_z\chi(P_t(z))\). Formula (1) is
\[
B_q(t)=q-1+A_q(t)-\chi(t)+q\mathbf1_{t=0}.
\tag{6}
\]
When \(t=0\), \(P_0(z)=z^2(z+1)\) and \(A_q(0)=\sum_{z\ne0}\chi(z+1)=-1\), so \(B_q(0)=2q-2\).

If three is invertible and \(t=-4/27\), then \(P_t(z)=(z+2/3)^2(z-1/3)\). Thus \(A_q(t)=-\chi(-1)\) and \(\chi(t)=\chi(-3)\), giving (2).

The discriminant of \(P_t\) is \(-t(4+27t)\). In odd characteristic it vanishes precisely for \(t=0\), and additionally for \(t=-4/27\) if the characteristic is not three. Otherwise the projective completion of \(y^2=P_t(z)\) is an elliptic curve with exactly one point at infinity and
\[
\#E_t(\mathbb F_q)=q+1+A_q(t).
\]
Substituting \(A_q(t)=-a_q(E_t)\) into (6) proves (3); the inequality is Hasse's bound.

**3. First and second shift moments.** Since \(w\mapsto t=4(v^2-4uw)/u^4\) is a bijection of \(\mathbb F_q\), it suffices to average (6) over \(t\). Put \(a(z)=z^2(z+1)\), \(z\ne0\), and \(H(t)=\sum_{z\ne0}\chi(t+a(z))\). Then
\[
B_q(t)=q-1+H(t)+q\mathbf1_{t=0},\quad \sum_tH(t)=0,\quad H(0)=-1.
\]
Summing gives (4). The standard quadratic-character correlation identity, valid in every odd finite field, is
\[
\sum_t\chi((t+\alpha)(t+\beta))=
\begin{cases}q-1,&\alpha=\beta,\\-1,&\alpha\ne\beta.\end{cases}
\]
For distinct \(\alpha,\beta\), translating and scaling reduces the sum to \(\sum_s\chi(s(s+1))=-1\): the affine conic \(y^2=s(s+1)\) has exactly \(q-1\) points because \((2s+1-2y)(2s+1+2y)=1\) parametrizes them by nonzero field elements. For equal parameters there are \(q-1\) nonzero squares.
Let \(M\) count ordered pairs \((z_1,z_2)\in(\mathbb F_q^\times)^2\) with \(a(z_1)=a(z_2)\). It follows that
\[
\sum_t H(t)^2=qM-(q-1)^2,\qquad
\sum_t(B_q(t)-q)^2=qM-q-1.
\tag{7}
\]
To calculate \(M\), factor
\[
a(z_1)-a(z_2)=(z_1-z_2)(z_1^2+z_1z_2+z_2^2+z_1+z_2).
\]
The diagonal contributes \(q-1\). For the second factor use \(s=z_1+z_2\), \(d=z_1-z_2\), a bijective change of coordinates in odd characteristic. Its zero locus is
\[
d^2=-3s^2-4s,
\]
which has \(q-\chi(-3)\) affine points: a nondegenerate quadratic-character sum when the characteristic is not three (complete the square and apply the immediately preceding character identity), and exactly \(q\) points from the linear right-hand side in characteristic three. Remove three points with either \(z_i=0\), namely \((0,0),(0,-1),(-1,0)\), and the additional diagonal point \(z_1=z_2=-2/3\) if the characteristic is not three. This gives
\[
M=(q-1)+(q-\chi(-3)-4+\mathbf1_{\operatorname{char}=3})
=2q-5-\chi(-3)+\mathbf1_{\operatorname{char}=3}.
\]
Insert into (7), divide by \(q\), and obtain (5). This completes the proof.

## Verification
Run `python verify.py` using Python 3 and no third-party libraries. It constructs finite fields of orders \(3,5,7,9,11,13,25,27,49\) using explicit monic irreducible moduli; directly enumerates all \(q^2\) nonsquarefree monic cubics by their repeated linear factors; and tests intersection counts against (1), including all \(w\) for each selected nonzero \(u\) and \(v\). It separately recomputes the mean and variance of each complete shift profile. The successful run returned `VERIFY_OK fields=9 shifts=293 independent_repeated_cubic_sets=yes means_variances=exact`. This verifies 293 finite configurations and does not constitute the proof for all prime powers; the proof above is algebraic.

## Relationship to prior work
Carmon and Rudnick (arXiv:1205.1599, first posted 2012-05-08) prove asymptotic Möbius correlations for distinct polynomial shifts as the field grows, not an exact finite-field joint squarefree cubic count. Keating and Rudnick (arXiv:1504.03444, first posted 2015-04-14), notably Appendix A, Theorem A.2, give a singular-series asymptotic for simultaneous squarefreeness when the **degree of the counted polynomial grows**, not a degree-three exact elliptic profile and a second moment over quadratic shifts. Almousa and Wood (arXiv:1210.0472) count single-polynomial root multiplicity partitions without imposing a simultaneous translated constraint. Rosenberg (arXiv:1410.7449) treats squarefree polynomial values in sparse families asymptotically. Exact cubic pair calculations for affine (degree at most one) shifts do not imply the degree-two profile: the new conic intersection has a genus-one character sum and singular strata. No independent originality certification is asserted.

## Limitations
The statements do not cover characteristic two, degree-one or constant shifts, nonlinear shifts of degree greater than two, monic polynomial degrees greater than three, or joint irreducibility rather than squarefreeness. For smooth parameters (3) is an elliptic-trace expression, not an elementary closed expression in \(q\) and the quadratic character alone. The exact first two moments do not determine the full distribution of elliptic traces, and equivalent coverage in historical literature not located in the searches remains possible.

## References
- D. Carmon and Z. Rudnick, *The autocorrelation of the Möbius function and Chowla's conjecture for the rational function field*, arXiv:1205.1599v1 (2012-05-08), https://arxiv.org/abs/1205.1599.
- A. Almousa and M. M. Wood, *Counting polynomials over finite fields with given root multiplicities*, arXiv:1210.0472v1 (2012-10-01), https://arxiv.org/abs/1210.0472.
- S. Rosenberg, *Square-free values of multivariate polynomials over function fields in linear sparse sets*, arXiv:1410.7449v1 (2014-10-27), https://arxiv.org/abs/1410.7449.
- J. P. Keating and Z. Rudnick, *Squarefree polynomials and Möbius values in short intervals and arithmetic progressions*, arXiv:1504.03444v1 (2015-04-14), https://arxiv.org/abs/1504.03444, especially Appendix A.
