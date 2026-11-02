# A genus and elliptic-rank transition for rationally scaled quadratic shifts

## Finding

Fix a squarefree integer \(d>1\). For a positive integer \(k\ge2\), let \(\mathcal S_{k,d}\) consist of rational pairs \((u,\lambda)\) with \(\lambda>0\) for which
\[
r=u-\lambda\sqrt d,\qquad r+\lambda\sqrt d\in\mathbb Q,\qquad r^k+\lambda\sqrt d\in\mathbb Q.
\]
Then the following complete genus-and-cardinality reduction holds.

* For \(k=2\), \(\mathcal S_{2,d}=\{(1/2,\lambda):\lambda\in\mathbb Q_{>0}\}\), which is infinite.
* For \(k=3\), \(\mathcal S_{3,d}\) is either empty or infinite. It is nonempty precisely when the rational conic \(3u^2+d\lambda^2=1\) has a rational point. In particular, \(\mathcal S_{3,6}\) is infinite.
* For \(k=4\), \(\mathcal S_{4,d}\) is infinite exactly when the Mordell–Weil rank of \(E_d:\ Y^2=X^3-4d^3\) is positive. In particular, \(\mathcal S_{4,15}\) is infinite.
* For every fixed \(d>1\) squarefree and every fixed \(k\ge5\), \(\mathcal S_{k,d}\) is finite.

Thus allowing the coefficient of a quadratic irrational shift to vary rationally changes the existence landscape from the fixed-unit-coefficient problem, but the high-exponent case retains a precise finiteness obstruction. The reduction determines whether infinitude can occur; it does not compute the sets of rational points in arbitrary genus or rank-zero cases.

## Assumptions and scope

All fields have characteristic zero; \(d>1\) is a positive squarefree integer, \(k\) is a fixed integer at least two, \(u\in\mathbb Q\), and \(\lambda\in\mathbb Q_{>0}\). We require the same irrational shift \(\lambda\sqrt d\) at exponents \(1\) and \(k\). We do not require \(r>0\). The radical is genuinely irrational because \(d\) is not a square and \(\lambda\ne0\).

Define a homogeneous integer binary form of degree \(k-1\) by
\[
F_{k,d}(U,V)=\sum_{\substack{1\le j\le k\\j\ \mathrm{odd}}}
\binom{k}{j}d^{(j-1)/2}U^{k-j}V^{j-1}.
\]
For \(V\ne0\), it is the divided difference
\[
F_{k,d}(U,V)=\frac{(U+\sqrt d\,V)^k-(U-\sqrt d\,V)^k}{2\sqrt d\,V}.
\]
The polynomial extends at \(V=0\) with value \(kU^{k-1}\). The associated projective curve is
\[
C_{k,d}:\quad F_{k,d}(U,V)=W^{k-1}\subset\mathbb P^2_{\mathbb Q}.
\]

## Proof

**1. Exact rationality reduction.** By the binomial theorem, the coefficient of \(\sqrt d\) in \((u-\lambda\sqrt d)^k\) is
\[
-\lambda F_{k,d}(u,\lambda).
\]
Thus the second rationality condition is equivalent to \(\lambda[1-F_{k,d}(u,\lambda)]=0\). Since \(\lambda>0\), it is exactly \(F_{k,d}(u,\lambda)=1\). Every affine pair is uniquely the projective point \([u:\lambda:1]\), and conversely every rational point with \(W\ne0\) and \(V/W>0\) recovers a unique pair. The case \(k=2\) has \(F_{2,d}=2U\), yielding the asserted entire infinite solution family.

**2. Separability and genus.** Let \(k\ge3\), and work over \(\mathbb C\). For a zero \([U:V]\) of \(F_{k,d}\) in \(\mathbb P^1\), \(V=0\) is impossible since \(F_{k,d}(U,0)=kU^{k-1}\). Moreover \(U-\sqrt d\,V\ne0\): otherwise the numerator of the divided difference is nonzero. Therefore
\[
\frac{U+\sqrt d\,V}{U-\sqrt d\,V}=\zeta
\]
for some nontrivial \(k\)-th root of unity \(\zeta\). Conversely, each of the \(k-1\) nontrivial roots gives a zero. The displayed fraction is a Möbius coordinate on \(\mathbb P^1\); these \(k-1\) points are distinct. As \(F_{k,d}\) has degree \(k-1\), all these zeros are simple.

At every point of \(C_{k,d}\) with \(W\ne0\), the derivative of \(F_{k,d}-W^{k-1}\) with respect to \(W\) equals \(-(k-1)W^{k-2}\ne0\). At a point with \(W=0\), simplicity of the corresponding binary-form root ensures that the gradient in \(U,V\) is nonzero. Thus \(C_{k,d}\) is a smooth projective geometrically integral plane curve of degree \(k-1\). The plane-curve genus formula gives
\[
g(C_{k,d})=\frac{(k-2)(k-3)}2.
\]
In particular \(g\ge3\) for \(k\ge5\). Faltings' theorem then makes \(C_{k,d}(\mathbb Q)\), and hence \(\mathcal S_{k,d}\), finite for each fixed \(d,k\) in this range. This argument is not effective and does not assert that the set is empty.

**3. The genus-zero boundary.** For \(k=3\) the equation is
\[
3u^2+d\lambda^2=1.
\]
A smooth rational conic with a rational point admits a rational parametrization and hence infinitely many rational points. No rational point on this conic can have \(\lambda=0\), because then \(u^2=1/3\). Changing the sign of \(\lambda\) if needed makes it positive. Consequently either there are no rational points or there are infinitely many admissible rational pairs.

For \(d=6\), a concrete infinite subfamily, for every rational \(t\) with \(-1/5<t<1/5\), is
\[
 u(t)=\frac{2t^2-4t-1}{3(2t^2+1)},\qquad
 \lambda(t)=\frac{1-2t-2t^2}{3(2t^2+1)}.
\]
Direct expansion gives \(3u(t)^2+6\lambda(t)^2=1\), and \(\lambda(t)>0\) throughout the indicated range. The pairs are distinct as \(t\) varies: the slope of the line from \((3u,3\lambda)=(1,1)\) recovers \(t\), and none of these points is \((1,1)\).

**4. The genus-one boundary and non-torsion example.** For \(k=4\) the equation becomes
\[
4u(u^2+d\lambda^2)=1.
\]
In particular \(u\ne0\). Put
\[
 X=\frac d u,\qquad Y=\frac{2d^2\lambda}u.
\]
Then exactly \(Y^2=X^3-4d^3\). Conversely, any finite rational point \((X,Y)\) of \(E_d\) has \(X>0\) (since \(X^3=Y^2+4d^3>0\)), and \(Y\ne0\) because \(4d^3\) is not a rational cube. The reverse transformation is
\[
 u=\frac dX,\qquad \lambda=\frac Y{2dX}.
\]
Exactly one of each pair of opposite points \((X,Y)\) and \((X,-Y)\) yields \(\lambda>0\). Thus admissible pairs are in bijection with nonidentity rational points of \(E_d\) modulo \(P\sim-P\). By the Mordell–Weil theorem, the set is infinite if and only if \(E_d(\mathbb Q)\) has positive rank.

For \(d=15\), \(E_{15}\) is \(Y^2=X^3-13500\) and has the rational point \(P=(60,450)\). The exact chord-and-tangent group law yields
\[
2P=(24,-18),\quad 3P=(85,-775),\quad
5P=\left(\frac{167460}{3721},\frac{63249750}{226981}\right).
\]
The elliptic curve has an integral nonsingular Weierstrass equation. By the Nagell–Lutz theorem, every finite-order rational point has integral coordinates; \(5P\) has nonintegral first coordinate. Therefore \(5P\), and hence \(P\), has infinite order. Its infinitely many nonzero multiples (taken modulo sign) give distinct admissible positive rational scales. The first pair is \((u,\lambda)=(1/4,1/4)\).

## Verification

Run `python3 verify.py` in a directory containing the standalone included file. It uses only the Python standard library and exact `Fraction` arithmetic. The checked output is

```
VERIFY_OK conic_points=41 elliptic_multiples=7 nonintegral_5P_x=167460/3721 binomial_checks=51 rational_arithmetic=yes
```

These checks verify 41 explicit conic pairs, seven exact elliptic multiples, the nonintegral \(5P\) coordinate, and 51 independent coefficient identities across exponents two through eighteen. The smoothness and Faltings steps are mathematical proofs, not consequences of those finite checks.

## Relationship to prior work

Anthony Pisani's *On the Open Problem in the 2023 Simon Marais Mathematics Competition* (arXiv:2610.30658; first public posting 22 October 2026) resolves the simultaneous-rationality problem with a fixed radical \(\sqrt n\) for a nonsquare **integer** \(n\). His Section 4 writes the same unscaled binomial divided difference for exponent pairs involving one and uses integral valuations to exclude all exponents greater than two in that fixed-integer setting. We instead allow the multiplier \(\lambda\) to vary over positive rationals, so the radicand \(d\lambda^2\) need not be an integer. This exposes the complete genus hierarchy and, crucially, a positive-rank elliptic example at exponent four that is impossible in the original integer-radicand problem.

The genus formula for smooth plane curves, Faltings' theorem, the Mordell–Weil theorem, and Nagell–Lutz are established background results. The contribution is the precise arithmetic-geometric reduction for this scaled simultaneous-rationality problem, the resulting sharp finiteness boundary, and the explicit positive-rank witness. The underlying superelliptic and elliptic facts are not claimed as new.

## Limitations

The result is **pointwise in both \(d\) and \(k\)**: it supplies no uniform upper bound over changing parameters. Faltings' theorem here does not enumerate rational points or give an effective height cutoff. Deciding the rank of \(E_d\) for arbitrary \(d\), or finding all rational points on \(C_{k,d}\) for \(k\ge5\), lies outside this result. The work does not treat two independently chosen exponents greater than one, positive \(r\) as an additional constraint, or arbitrary irrational shifts. Historical priority for a potentially equivalent formulation in classical superelliptic-curve literature requires independent review.

## References

1. Anthony Pisani, *On the Open Problem in the 2023 Simon Marais Mathematics Competition*, arXiv:2610.30658v1 (2026-10-22); revised v2 (2026-10-24). https://arxiv.org/html/2610.30658v2
2. Gerd Faltings, *Endlichkeitssätze für abelsche Varietäten über Zahlkörpern*, Inventiones Mathematicae 73 (1983), 349–366 (Mordell finiteness theorem).
3. Joseph H. Silverman, *The Arithmetic of Elliptic Curves*, Springer (1986), in particular the Mordell–Weil and Nagell–Lutz theorems.
4. A. A. Swaminathan, *Most odd-degree binary forms fail to primitively represent a square*, Compositio Mathematica (2024), for context on broader superelliptic finiteness techniques; its quadratic-square setting is not used as a proof here.
