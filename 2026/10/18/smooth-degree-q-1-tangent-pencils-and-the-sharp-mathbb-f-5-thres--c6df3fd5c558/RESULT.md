# Smooth degree-\(q-1\) tangent pencils and the sharp \(\mathbb F_5\) threshold

## Finding
For every prime power \(q=p^e\) of characteristic \(p>3\), the smooth plane curve
\[
 C_q:\quad F_q(X,Y,Z)=X^{q-1}+X^{q-2}Y+Y^{q-2}Z-Z^{q-1}=0
\]
has degree \(q-1\), genus \((q-2)(q-3)/2\), and is tangent-filling over \(\mathbb F_q\). Indeed every rational line through the external point \(P=[1:1:0]\) is tangent to \(C_q\) at a distinct smooth rational point.

For \(q=5\), the quartic \(X^4+X^3Y+Y^3Z-Z^4=0\) is a minimum-degree geometrically integral tangent-filling curve: the minimum is exactly \(4\). Exhaustive enumeration of all \((5^{10}-1)/4=2{,}441{,}406\) projective cubic forms over \(\mathbb F_5\), including singular and reducible forms, gives a largest tangent-line coverage of \(29\) of the \(31\) rational projective points. Thus no cubic can be tangent-filling.

## Assumptions and scope
Work over the finite field \(\mathbb F_q\), where \(q=p^e\) and \(p>3\). All assertions about smoothness and irreducibility are geometric (over the algebraic closure). A rational tangent is the tangent line at a nonsingular \(\mathbb F_q\)-rational point; a curve is tangent-filling if these tangent lines cover all of \(\mathbb P^2(\mathbb F_q)\). For the minimum-degree statement, geometric integrality is required; the exhaustive cubic obstruction actually applies to every nonzero cubic form, including reducible and singular ones.

## Proof
**1. Geometric smoothness.** In characteristic \(p\), with \(q\equiv0\pmod p\), the derivatives of \(F_q\) are
\[
 (F_X,F_Y,F_Z)=\left(-X^{q-3}(X+2Y),\ X^{q-2}-2Y^{q-3}Z,\ Y^{q-2}+Z^{q-2}\right).
\]
If \(X=0\), the last two partials cannot simultaneously vanish at a projective point: when \(Y\) or \(Z\) vanishes, \(F_Z\ne0\), whereas if \(YZ\ne0\), then \(F_Y=-2Y^{q-3}Z\ne0\). If \(X\ne0\), put \(X=1\). Vanishing of \(F_X\) forces \(Y=-1/2\); vanishing of \(F_Y\) forces \(Z=1/8\), because \((-1/2)^{q-3}=4\) in the prime field. But then \(F_Z=(-1/2)^{q-2}+(1/8)^{q-2}=-2+8=6\ne0\) since \(p>3\). No geometric common zero of the partial derivatives exists. Thus the curve is smooth. A positive-degree smooth plane curve cannot have two geometric components by Bézout; it is geometrically integral, with the usual plane-curve genus.

**2. A full rational tangent pencil.** At \(Q_{\infty}=[0:1:0]\), the tangent is \(Z=0\). At \(Q_z=[1:0:z]\) for every \(z\in\mathbb F_q^{\times}\), the equation holds and the gradient is \((-1,1,z^{-1})\), giving tangent \(-X+Y+z^{-1}Z=0\). Finally \(Q_0=[1:1:-1]\) is on the curve, has gradient \((-3,3,0)\), and tangent \(-X+Y=0\). These \(q+1\) curve points are pairwise distinct, and their tangents are precisely the rational pencil \(Z=0\) and \(-X+Y+tZ=0\) for \(t\in\mathbb F_q\). Every rational point of the plane lies on exactly one line of this pencil, since the lines run through \(P=[1:1:0]\). The tangent-filling property follows. The point \(P\) is external to the curve because \(F_q(P)=2\ne0\).

**3. Sharpness at \(q=5\).** A line supplies only itself as a tangent. A smooth conic over \(\mathbb F_5\) has six rational tangent lines, no three of which are concurrent, so their union contains \(6\cdot6-\binom62=21\) rational points, fewer than \(31\). If a conic is reducible, its smooth rational tangents lie on at most its two component lines and cover at most \(11\) rational points; an irreducible but geometrically split conic has no smooth rational points away from the conjugate-component intersection. Therefore degree one or two cannot be tangent-filling.

For cubics, enumerate the \(10\) monomials of degree \(3\), and normalize every nonzero coefficient vector in \(\mathbb F_5^{10}\) by scaling its first nonzero coefficient to \(1\); there are precisely \((5^{10}-1)/4=2{,}441{,}406\) such vectors. Enumerate the \(31\) rational projective points by taking representatives whose first nonzero coordinate is \(1\). For each cubic, take every rational zero with nonzero gradient; form its tangent line from that gradient, and OR the exact \(31\)-bit incidence mask of that line. Every tangent used in the definition is included and no other line is counted. The resulting maximum population count is exactly \(29\); zero of the cubic forms has population count \(31\). The standalone `verify.cpp` provides the complete reproducible enumeration, without random sampling or irreducibility assumptions. This excludes all cubics, while \(C_5\) is a smooth tangent-filling quartic, so the minimum is \(4\).

## Verification
Compile `verify.cpp` using `g++ -std=c++17 -O3 verify.cpp -o verify` and execute `./verify`. It enumerates exactly \(2{,}441{,}406\) normalized cubic coefficient vectors, and prints `tangent_cover=0 max_cover=29`. It also checks that the displayed quartic has \(11\) rational points and that its rational tangent lines cover all \(31\) projective points. The infinite-family proof is symbolic and does not extrapolate from this finite enumeration.

## Relationship to prior work
Asgarli–Ghioca, *Tangent-filling plane curves over finite fields* (arXiv:2302.13420, first posted 2023-02-26), introduced and studied the tangent-filling property and posed the minimum-degree problem. Their Theorem 1.3 constructs a distinct, geometrically irreducible degree-\(q-1\) tangent-filling example for sufficiently large \(q\) in characteristic greater than three; that construction is singular. The smooth family here has an explicit full pencil of rational tangents and already works for \(q=5\). The complete \(\mathbb F_5\) lower bound addresses the smallest odd characteristic in that range. The prior construction does not imply geometric smoothness or the new explicit pencil, and the general existence statement does not determine the exact \(\mathbb F_5\) minimum. More general plane-filling constructions address a different incidence property.

## Limitations
The minimum is proved only for \(q=5\), not for every prime power. The infinite family excludes characteristics \(2\) and \(3\); no lower bound for general \(q\) is claimed. The cubic obstruction is a finite, exhaustive, independently reproducible computation rather than a compact theoretical classification of individual cubic orbits. An earlier equivalent construction under a different name cannot be ruled out by database searches alone. The verifications are self-review; independent mathematical review has not been performed.

## References
1. S. Asgarli and D. Ghioca, *Tangent-filling plane curves over finite fields*, arXiv:2302.13420v1 (2023-02-26), https://arxiv.org/abs/2302.13420 ; published in *Bulletin of the Australian Mathematical Society* 109 (2024), 301–315, DOI:10.1017/S0004972723000382.
2. S. Asgarli and D. Ghioca, *Plane-filling curves of small degree over finite fields*, arXiv:2307.03072 (2023), https://arxiv.org/abs/2307.03072 (different plane-filling incidence problem).
