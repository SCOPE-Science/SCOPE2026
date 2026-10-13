# Complete \(p\)-rank and \(a\)-number stratification of an extremal genus-two fibration

## Finding
Let \(k\) be an algebraically closed field of characteristic \(5\). For each finite parameter \(t\in k\setminus\{0,1,3\}\), let \(C_t\) be the smooth projective model of the genus-two curve
\[
y^2=4t x(x-1)^5+\bigl(x(x-1)+t(x^4-(x-1)^4)\bigr)^2.
\]
This is the generic smooth-family equation for the four-singular-fiber genus-two fibration of Sun–Xu [1]. Define its \(5\)-rank \(f(C_t)\) by \(\#\operatorname{Jac}(C_t)[5](k)=5^{f(C_t)}\). Then
\[
\begin{aligned}
f(C_t)=0&\iff t^2+2=0,\\
f(C_t)=1&\iff (t-2)(t+1)(t^2-2t-2)=0,\\
f(C_t)=2&\text{ otherwise.}
\end{aligned}
\]
The two roots of \(t^2+2\) are the **only smooth superspecial members**, with \(a\)-number two; exactly four smooth members have \(5\)-rank one and \(a\)-number one, and every other smooth member is ordinary with \(a\)-number zero. All six exceptional parameters are distinct, lie away from the four singular-fiber parameters, and are geometrically simple.

## Assumptions and scope
All polynomial identities, discriminants and Hasse invariants below are in characteristic \(5\). The base point \(t=\infty\), along with \(t=0,1,3\), is excluded: these are exactly the four singular fibers proved in [1, Theorem 1.5 and Section 5]. The six exceptional counts are **geometric counts** over \(k\), not counts of rational parameters over \(\mathbb F_5\). The word supersingular refers to the Newton polygon of the genus-two Jacobian, with all slopes \(1/2\), and the stronger word superspecial means that the Jacobian has \(a\)-number two.

## Proof
**1. Two elliptic quotients.** Set \(z=x(x-1)\). Expansion in characteristic \(5\) gives the exact identity
\[
4t x(x-1)^5+\bigl(x(x-1)+t(x^4-(x-1)^4)\bigr)^2=F_t(z),
\]
where
\[
F_t(z)=t(t-1)z^3+(1-2t)z^2+2t(1-t)z+t^2.
\]
The involution \(\sigma:(x,y)\mapsto(1-x,y)\) is different from the hyperelliptic involution \(\iota:(x,y)\mapsto(x,-y)\), and they commute. Their quotient equations are
\[
E_{+,t}:Y^2=F_t(z),\qquad E_{-,t}:V^2=(4z+1)F_t(z),
\]
with \(Y=y\) and \(V=(2x-1)y\). The respective fixed fields are \(k(z,y)\) and \(k(z,(2x-1)y)\), since \((2x-1)^2=4z+1\). Thus both quotient maps have separable degree two. For \(t\notin\{0,1,3\}\), the cubic and quartic have nonzero leading coefficients and distinct roots: one may calculate
\[
\operatorname{disc}_z(F_t)=-2t^6(t+2),\qquad
\operatorname{disc}_z((4z+1)F_t)=-2t^6(t-1)^2(t+2).
\]
Hence both smooth quotients have genus one (and rational points over \(k\)), so they are elliptic curves.

**2. Splitting the Jacobian.** The two elliptic involutions differ by the hyperelliptic involution. On the two-dimensional space of regular differentials of \(C_t\), the \(\sigma\)-invariant and anti-invariant lines are distinct: in the basis \(dx/y,x\,dx/y\), the pullback satisfies \(\sigma^*(dx/y)=-dx/y\) and \(\sigma^*(x\,dx/y)=x\,dx/y-dx/y\). The pullback homomorphism
\[
E_{+,t}\times E_{-,t}\longrightarrow\operatorname{Jac}(C_t)
\]
therefore has an isomorphism on tangent spaces and finite kernel: it is the standard separable \((2,2)\)-isogeny of a genus-two curve with two elliptic quotients [2]. In particular, \(5\)-ranks add:
\[
f(C_t)=f(E_{+,t})+f(E_{-,t}).
\]

**3. Hasse factors.** For an elliptic curve in characteristic \(5\) presented as \(v^2=h(z)\) with squarefree polynomial \(h\) of degree three or four, the Hasse invariant is, up to a nonzero scalar, the coefficient of \(z^{4}\) in \(h(z)^{(5-1)/2}=h(z)^2\). This vanishes precisely for supersingular elliptic curves. Direct coefficient extraction yields
\[
\begin{aligned}
H_+(t)&=[z^4]F_t(z)^2=(t^2+2)(t^2-2t-2),\\
H_-(t)&=[z^4]\bigl((4z+1)F_t(z)\bigr)^2
=(t-2)(t+1)(t^2+2).
\end{aligned}
\]
The factors of \(H_+\) and \(H_-\) have exactly the common factor \(t^2+2\). The factors \(t-2\), \(t+1\), \(t^2-2t-2\), and \(t^2+2\) are pairwise coprime, and none vanishes at \(0,1,3\); the two quadratic factors are separable. Consequently, both elliptic quotients are supersingular precisely at the two roots of \(t^2+2\), exactly one elliptic quotient is supersingular at the other four listed parameters, and both are ordinary otherwise. Additivity of \(5\)-rank proves the trichotomy. At the two common roots the Jacobian is isogenous to a product of two supersingular elliptic curves, hence is supersingular.

**4. The full \(a\)-number stratification.** To distinguish superspecial from merely supersingular points, compute the genus-two Hasse–Witt (equivalently, transposed Cartier–Manin) matrix. For \(P_t(x)=F_t(x(x-1))\), let \(c_j=[x^j]P_t(x)^2\). In the standard basis \(dx/y,x\,dx/y\), its matrix is
\[
M_t=\begin{pmatrix}c_4&c_3\\c_9&c_8\end{pmatrix}
=\begin{pmatrix}
(t-2)(t+1)(t^2+2)&-2t(t^2+2)\\
0&(t^2+2)(t^2-2t-2)
\end{pmatrix}.
\]
These identities hold in \(\mathbb F_5[t]\). The \(a\)-number is \(a(C_t)=2-\operatorname{rank}M_t\). At the two roots of \(t^2+2\), **all four matrix entries vanish**; thus \(a(C_t)=2\), and the genus-two Jacobian is superspecial. At the other four nonordinary parameters, exactly one diagonal factor vanishes, the other does not, and \(\operatorname{rank}M_t=1\), giving \(a(C_t)=1\). Everywhere else \(M_t\) is invertible, giving \(a(C_t)=0\). Thus this is also the complete \(a\)-number classification.

## Verification
The supplied `verify.py` uses Python's standard library only. Run `python3 verify.py` from the package directory. It computes exact polynomial identities over \(\mathbb F_5[t,z]\) (not numerical sampling), reconstructs the sextic as a polynomial in \(x(x-1)\), compares both genus-one Hasse polynomials against the stated factors, independently reconstructs all four entries of the genus-two Cartier–Manin matrix, and checks polynomial coprimality and separability for all exceptional parameters. It prints `VERIFY_OK` upon success. The general isogeny and \(5\)-rank statements follow from the geometric proof above, not from a finite-field point count.

## Relationship to prior work
Sun and Xu [1, equations (34)–(37), Theorem 1.5] give the genus-two pencil and prove that it has exactly four singular fibers, at \(0,1,3,\infty\), as well as sharp Arakelov invariants. They do not state its elliptic quotient equations or classify its ordinary, intermediate-\(5\)-rank, and supersingular smooth fibers. Degree-two elliptic subcovers and split genus-two Jacobians have an extensive preexisting theory, illustrated by Shaska [2]; the abstract quotient and splitting principles are therefore **not** claimed as new. The contribution here is the exact characteristic-five parameter stratification for the particular extremal fibration [1], including the two superspecial smooth fibers and four additional nonordinary smooth fibers, including their exact \(a\)-numbers.

## Limitations
The classification applies to the smooth fibers of this specific characteristic-five pencil, not all genus-two fibrations or their singular fibers. It classifies \(5\)-rank, \(a\)-number, and superspeciality, but does not classify the full isomorphism classes of the special Jacobians or their polarizations. Independent checking of bibliographic completeness beyond the named searched sources is not asserted.

## References
[1] H. M. Sun and W.-Y. Xu, *Arakelov inequalities for fibered surfaces in positive characteristic*, arXiv:2610.02760v1 (first public 2026-10-02), Theorem 1.5 and Section 5, https://arxiv.org/html/2610.02760v1.

[2] T. Shaska, *Genus two curves covering elliptic curves: a computational approach*, arXiv:1209.3187v1 (2012), https://arxiv.org/html/1209.3187v1. General reference for elliptic subcovers; its characteristic-zero discussion does not supply the present characteristic-five Hasse locus.
