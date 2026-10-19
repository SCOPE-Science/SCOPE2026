# Square-zero resonance strata of a twelve-dimensional quantum complete intersection

## Finding

Let \(k\) be any field and \(\lambda\in k^\times\). Consider the twelve-dimensional quantum complete intersection
\[
\mathcal A_\lambda=k\langle x,y\rangle/(x^3,y^4,yx-\lambda xy)
\]
and its **reduced** square-zero variety \(X_\lambda=\{z\in\mathcal A_\lambda:z^2=0\}_{\mathrm{red}}\). Put \(u_j=1+\lambda^j\) for \(j=2,4,6\). The following five mutually exclusive cases exhaust all characteristics and nonzero parameters:

| Condition | Geometrically irreducible components (dimensions) | Grothendieck class \([X_\lambda]\) |
| --- | --- | --- |
| \(u_2u_4u_6\ne0\) | Three, all dimension \(6\) | \(\mathbb L^5(3\mathbb L-2)\) |
| \(u_2u_4\ne0,\ u_6=0\) | Two, dimensions \(7\) and \(6\) | \(\mathbb L^5(\mathbb L^2+\mathbb L-1)\) |
| \(u_4=0,\ u_2\ne0\) | Two, both dimension \(7\) | \(2\mathbb L^7-\mathbb L^6\) |
| \(u_2=0,\operatorname{char}k\ne2\) | Two, both dimension \(7\) | \(2\mathbb L^7-\mathbb L^6\) |
| \(\operatorname{char}k=2,\lambda=1\) | One, dimension \(8\), isomorphic to \(\mathbb A^8\) | \(\mathbb L^8\) |

Here \(\mathbb L=[\mathbb A^1_k]\) in \(K_0(\operatorname{Var}_k)\). Thus the generic dimension is \(6\), rises to \(7\) at the indicated fourth-, eighth-, or twelfth-root resonances (as allowed by the characteristic), and reaches \(8\) in characteristic two at the commutative parameter. In characteristic two a nontrivial third root gives the second row, not the final row. All asserted components are geometrically irreducible over \(k\); no algebraic-closure hypothesis is needed.

For a finite field \(k=\mathbb F_Q\), evaluation \(\mathbb L\mapsto Q\) gives the exact square-zero element count in every row. The formulas also hold over all finite extensions of \(\mathbb F_Q\) with the same parameter.

## Assumptions and scope

The relation is \(yx=\lambda xy\), so multiplication in the standard basis is
\[
(x^iy^j)(x^ry^s)=
\begin{cases}
\lambda^{jr}x^{i+r}y^{j+s},&i+r<3,\ j+s<4,\\
0,&\text{otherwise},
\end{cases}
\quad 0\le i,r<3,\quad 0\le j,s<4.
\]
The basis comprises twelve monomials. The assertion classifies the reduced geometric locus; it does **not** assert scheme-theoretic reducedness of the displayed square equations. A scalar coefficient in a square-zero element must vanish, and the coefficients of \(x\) and \(y\) also vanish because their squares have independent nonzero basis coordinates. Every candidate therefore has the unique form
\[
z=ax^2+bxy+cy^2+dx^2y+exy^2+fy^3
+ux^2y^2+vxy^3+w x^2y^3.
\]
All nine coordinates range freely over \(k\) subject to the three equations derived next. No restriction is made on whether \(\lambda\) is a root of unity, except those stated in the case distinctions.

## Proof

**1. Exact equations and a rank-one fiber reduction.** Multiplication of the nine displayed monomials gives
\[
\begin{aligned}
P&=\lambda b^2+(1+\lambda^4)ac=0,\\
R&=(1+\lambda^2)bc=0,\\
S&=(1+\lambda^4)cd+\lambda(1+\lambda)be+(1+\lambda^6)af=0.
\end{aligned}
\tag{1}
\]
These are exactly the coefficients of \(x^2y^2\), \(xy^3\), and \(x^2y^3\) in \(z^2\). No other coefficient can survive the truncations. The variables \(u,v,w\) are completely free.

Set \(B_\lambda=\{(a,b,c):P=R=0\}_{\mathrm{red}}\), and let \(Z_\lambda\subseteq B_\lambda\) be the zero locus of the three coefficients of \(d,e,f\) in \(S\):
\[
(1+\lambda^4)c=0,\qquad \lambda(1+\lambda)b=0,
\qquad(1+\lambda^6)a=0.
\]
Over \(B_\lambda\setminus Z_\lambda\), the equation \(S=0\) has a rank-two vector-bundle fiber in \(\mathbb A^3_{d,e,f}\); over \(Z_\lambda\) the fiber is \(\mathbb A^3\). The free \(u,v,w\) supply an additional \(\mathbb A^3\). Therefore
\[
[X_\lambda]=\mathbb L^5\bigl([B_\lambda]+(\mathbb L-1)[Z_\lambda]\bigr).
\tag{2}
\]
The bundle statement follows by solving for a coordinate of \(d,e,f\) wherever its coefficient is nonzero. It is Zariski-local and valid over an arbitrary field.

**2. Generic and twelfth-root regimes.** Suppose \(u_2u_4\ne0\). The equations \(P=R=0\) force \(b=0\), because \(bc=0\) and \(c=0\Rightarrow \lambda b^2=0\). Then \(ac=0\), giving the union of the two coordinate axes with \([B_\lambda]=2\mathbb L-1\). If \(u_6\ne0\), the fiber-rank-zero locus is the origin, \([Z_\lambda]=1\), and (2) yields \(\mathbb L^5(3\mathbb L-2)\). The three complete irreducible components, in coordinates \((a,b,c,d,e,f,u,v,w)\), are
\[
V(b,c,f),\qquad V(a,b,d),\qquad V(a,b,c),
\]
each an affine six-space. If \(u_6=0\), then \(Z_\lambda=V(b,c)\cong\mathbb A^1\), and (2) gives \(\mathbb L^5(\mathbb L^2+\mathbb L-1)\). The two components are \(V(b,c)\cong\mathbb A^7\) and \(V(a,b,d)\cong\mathbb A^6\). In this case the origin-fiber component of the preceding regime is contained in \(V(b,c)\).

**3. Eighth-root regime.** Suppose \(u_4=0\) and \(u_2\ne0\). The equation \(P=\lambda b^2=0\) forces \(b=0\) on the reduced variety. The base is the plane \(B_\lambda=V(b)\) and \(1+\lambda^6=1-\lambda^2\ne0\) (otherwise \(\lambda^2=1\) and \(u_4\ne0\) in this regime). Thus \(Z_\lambda=V(a,b)\cong\mathbb A^1\), and (2) gives \(2\mathbb L^7-\mathbb L^6\). The two affine seven-space components are \(V(a,b)\) and \(V(b,f)\).

**4. Fourth-root regime in odd characteristic.** Suppose \(u_2=0\) and \(\operatorname{char}k\ne2\). Then \(\lambda^2=-1\), \(u_4=2\), \(u_6=0\), and \(\beta:=\lambda(1+\lambda)\ne0\). The base is the nondegenerate split quadratic cone
\[
B_\lambda=V(\lambda b^2+2ac)\subseteq\mathbb A^3,
\]
whose projectivization is a smooth conic with the rational point \([1:0:0]\). Hence \([B_\lambda]=\mathbb L^2\). The coefficient vector in \(S=2cd+\beta be\) vanishes precisely on \(Z_\lambda=V(b,c)\cong\mathbb A^1\), so (2) again gives \(2\mathbb L^7-\mathbb L^6\).

For completeness, the two geometrically irreducible components are the linear \(V(b,c)\cong\mathbb A^7\) and the closure \(T\) of the open set \(c\ne0\) in \(X_\lambda\). On \(c\ne0\), the equations uniquely solve
\[
a=-\frac{\lambda b^2}{2c},\qquad
 d=-\frac{\beta be}{2c};
\]
therefore the open set is \(\mathbb G_m\times\mathbb A^6\) and \(T\) is geometrically irreducible of dimension seven. Every point outside it lies in \(V(b,c)\), since \(c=0\) forces \(b=0\) by the quadratic equation. To see that the linear component is not swallowed by \(T\), observe that \(\lambda bd-\beta ae\) vanishes identically on \(c\ne0\) (and hence on \(T\)), but not at \(a=e=1,b=c=0\) on the linear component. Thus these are exactly the two components.

**5. Characteristic two.** If \(\operatorname{char}k=2\) and \(\lambda=1\), equations (1) reduce to \(b^2=0\) and two zero equations. The reduced variety is the linear eight-space \(V(b)\). If \(\lambda\ne1\), then \(u_2=(1+\lambda)^2\ne0\) and \(u_4=(1+\lambda)^4\ne0\), reducing to case 2. The remaining coefficient \(u_6\) vanishes precisely when \(\lambda^3=1\), because \(1+\lambda^6=(1+\lambda^3)^2\). This accounts for the characteristic-two third-root resonance and completes the exhaustive case split.

**6. Finite fields.** Formula (2) is an equality of classes of varieties, so the ring homomorphism \([V]\mapsto |V(\mathbb F_Q)|\) specializes each displayed motivic formula to an exact finite-field count. All components and bundle charts in the proof are defined over the original field; no point-count correction is needed for nontrivial Galois orbits.

## Verification

The standalone C11 file `verify_qci_squarezero.c` enumerates all six degree-two/degree-three coefficients and evaluates the square by independent multiplication of the monomial basis using \((x^iy^j)(x^ry^s)=\lambda^{jr}x^{i+r}y^{j+s}\). The three higher-degree coefficients are handled by the exact free factor \(Q^3\). It compares the resulting full counts with the five-case formulas, for prime fields of sizes \(2,3,5,13,17\) and the four-element field. In particular, parameters of orders three, four, eight, and twelve occur. Compile with `cc -O3 -std=c11 verify_qci_squarezero.c -o verify_qci_squarezero` and execute `./verify_qci_squarezero`; it prints `VERIFY_OK` only when all exhaustive cases pass. These are finite checks, not a substitute for the uniform proofs above.

## Relationship to prior work

Two-generator quantum complete intersections and their monomial bases are classical. Bergh and Erdmann (2007, arXiv:0709.3029) construct a minimal projective bimodule resolution and calculate Hochschild (co)homology for this algebra family. Their root-of-unity transition concerns Hochschild cohomology; it is not the internal square-zero element locus. Bergh and Oppermann (2007, arXiv:0710.2606) derive bounds on representation dimension, again for the larger family. Bergh and Erdmann (2008, arXiv:0810.3308) compare rank and support varieties **of modules**, rather than reduced varieties of square-zero elements **in the algebra**; those varieties have different definitions and are not used as substitutes here. None of these inspected results yields the five-case component or motivic formula. This is a claim of noncoverage by the examined statements, not a proof of absolute literature uniqueness.

## Limitations

The result concerns the reduced variety, not the possibly nonreduced square-equation scheme or its singular scheme. It classifies one natural asymmetric truncation \((3,4)\) and does not assert a comparable formula for arbitrary exponents. The fourth- and eighth-root regimes have identical Grothendieck classes despite different explicit component geometry; equality of classes does not imply variety isomorphism. Literature not located by the searches could contain equivalent component classifications. No independent mathematical audit has been performed.

## References

1. P. A. Bergh and K. Erdmann, *(Co)homology of quantum complete intersections*, arXiv:0709.3029, first posted 19 September 2007; see the algebra definition in Section 2 and Theorems 3.1–3.3. https://arxiv.org/abs/0709.3029
2. P. A. Bergh and S. Oppermann, *The representation dimension of quantum complete intersections*, arXiv:0710.2606, first posted 13 October 2007; see Section 3 and Theorems 3.1–3.2. https://arxiv.org/abs/0710.2606
3. P. A. Bergh and K. Erdmann, *The Avrunin–Scott theorem for quantum complete intersections*, arXiv:0810.3308, first posted 18 October 2008; see Sections 2–3 and Corollary 3.7. https://arxiv.org/abs/0810.3308
