# The irregular characteristic-two Fano fourfold has a cubic-fourfold zeta function

## Finding
Let \(\theta\in\mathbf F_{128}\) have degree seven over \(\mathbf F_2\), and let \(X/\mathbf F_{128}\) be the smooth projective Fano fourfold obtained by the Waldron--Witaszek rank-one foliation quotient of the complete intersection \(H\subset\mathbf P^6\) described below. Put
\[
Y=\left\{\sum_{j=0}^{2}\bigl(x_{2j}^{2}x_{2j+1}+x_{2j}x_{2j+1}^{2}\bigr)=0\right\}\subset\mathbf P^5_{\mathbf F_2}.
\]
There are finite flat universal homeomorphisms of degree two
\[
X\xleftarrow{\,\pi\,}H\xrightarrow{\,\rho\,}Y_{\mathbf F_{128}}.
\]
The cubic fourfold \(Y\) is smooth. Consequently, for every prime \(\ell\ne2\), this span identifies the graded \(\ell\)-adic cohomology rings of \(X_{\overline{\mathbf F}_2}\) and \(Y_{\overline{\mathbf F}_2}\), compatibly with geometric Frobenius for the field \(\mathbf F_{128}\); it matches the anticanonical class on \(X\) with the hyperplane class on \(Y\). The Betti numbers of \(X\) are
\[
(b_0,b_1,\ldots,b_8)=(1,0,1,0,23,0,1,0,1).
\]
Writing \(q=128\), for every integer \(n\ge1\),
\[
\#X(\mathbf F_{q^n})=1+q^n+q^{2n}+q^{3n}+q^{4n}+
\begin{cases}8q^{2n},&n\text{ odd},\\22q^{2n},&n\text{ even}.\end{cases}
\]
Equivalently, its Hasse--Weil zeta function is
\[
Z(X/\mathbf F_q,T)=\frac{1}{(1-T)(1-qT)(1-q^3T)(1-q^4T)(1-q^2T)^{16}(1+q^2T)^7}.
\]
In particular, the characteristic-two Fano fourfold has \(27\) as its \(\ell\)-adic Euler characteristic. Moreover, finite-flat radicial pullback and pushforward through \(H\) identify the rational Chow groups of \(X\) and \(Y\) in every codimension. By the Tate theorem for characteristic-two smooth cubic fourfolds, over \(\mathbf F_{q^2}\) all \(23\) dimensions of the fourth \(\ell\)-adic cohomology of \(X\) are spanned by codimension-two algebraic cycle classes.

## Assumptions and scope
The construction is the one in Waldron--Witaszek, arXiv:2609.29924v1, with coefficients in \(\mathbf F_{128}\). Let \(S=\mathbf F_{128}[x_0,\ldots,x_5,t]\) with the usual degree-one grading and set
\[
\begin{aligned}
C&=\sum_{j=0}^{2}(x_{2j}^{2}x_{2j+1}+x_{2j}x_{2j+1}^{2}),\\
Q_6&=x_0x_1+x_2x_3+x_4x_5+\sum_{i=0}^5\theta^{i+1}x_i^2,\\
H&=V(C,Q_6+t^2)\subset\mathbf P^6_{\mathbf F_{128}}.
\end{aligned}
\]
The source constructs an invariant open neighborhood of \(H\) in \(V(C)\) with a regular rank-one foliation whose quotient contains a smooth Cartier divisor \(X\). Its restriction \(\pi:H\to X\) is finite flat radicial of degree two; this construction is defined over \(\mathbf F_{128}\). The source also proves \(\pi^*\omega_X^{-1}\cong\mathcal O_H(1)\). The assertion about Chow groups means ordinary codimension-indexed Chow groups tensored with \(\mathbf Q\), not integral Chow-group isomorphisms and not an isomorphism of Hodge cohomology. All \(\ell\)-adic assertions assume \(\ell\ne2\).

## Proof
**1. A second inseparable cover.** The point \([0:\cdots:0:1]\) does not lie on \(H\), because \(Q_6+t^2\) is nonzero there. Projection away from this point therefore gives a morphism
\[
\rho:H\longrightarrow Y_{\mathbf F_{128}},\qquad [x_0:\cdots:x_5:t]\longmapsto[x_0:\cdots:x_5].
\]
On each standard chart of \(\mathbf P^5\) where an \(x_i\) is nonzero, the coordinate \(t/x_i\) satisfies a monic quadratic equation of the form \(z^2=a\). The coordinate ring of its inverse image is free of rank two over the coordinate ring of \(Y\), with basis \(1,z\). Hence \(\rho\) is finite flat of degree two. In characteristic two, \(z^2=a\) has exactly one geometric root over any algebraically closed field, and the induced residue extensions are purely inseparable. Thus \(\rho\) is surjective and radicial, hence a universal homeomorphism. The same properties for \(\pi\) are proved in the source. Differentiating \(C\) gives
\[
\nabla C=(x_1^2,x_0^2,x_3^2,x_2^2,x_5^2,x_4^2),
\]
which cannot vanish at a projective point, so \(Y\) is smooth.

**2. Cohomology and polarizations.** A universal homeomorphism induces an equivalence on small étale topoi. Accordingly, \(\pi^*\) and \(\rho^*\) are ring isomorphisms on \(\ell\)-adic cohomology, commute with the \(\mathbf F_{128}\)-Frobenius, and preserve cup products. The identities \(\rho^*\mathcal O_Y(1)=\mathcal O_H(1)=\pi^*\omega_X^{-1}\) match the two polarization classes. The étale Lefschetz theorem and Poincaré duality for a smooth cubic fourfold give one-dimensional cohomology in degrees \(0,2,6,8\), no odd cohomology, and the remaining fourth Betti number \(23\) (the Euler characteristic is \(27\), computed from \(c_4(T_Y)=9h^4\) and \(\int_Yh^4=3\)). This proves the Betti assertion and the Euler characteristic.

**3. Two finite-field counts.** The defining cubic is over \(\mathbf F_2\). For \((x,y)\in\mathbf F_2^2\), \(xy(x+y)=0\), so every point of \(\mathbf P^5(\mathbf F_2)\) lies on \(Y\): \(\#Y(\mathbf F_2)=63\). Over \(\mathbf F_4\), a pair \((x,y)\) has \(xy(x+y)=0\) at exactly \(10\) of the \(16\) pairs; each of the six other pairs has \(xy(x+y)=1\). Indeed, if \(x,y\ne0\) and \(x\ne y\), then \((y/x)^2+(y/x)+1=0\) and \(x^3=1\). Among three independent pairs of coordinates, the cubic sum is zero exactly when either zero or two pairs contribute \(1\). Consequently
\[
\#Y(\mathbf F_4)=\frac{10^3+3\cdot6^2\cdot10-1}{4-1}=693.
\]

**4. Frobenius and the zeta function.** The fourth cohomology of a smooth cubic fourfold has one Tate summand with Frobenius eigenvalue \(4\) over \(\mathbf F_2\), and a primitive summand of dimension \(22\). Its eigenvalues \(\alpha_j\) satisfy \(|\alpha_j|=4\) under every complex embedding, by the Weil conjectures. The Lefschetz trace formula and the two counts yield
\[
\sum_j\alpha_j=63-(1+2+2^2+2^3+2^4)=32
\]
and
\[
\sum_j\alpha_j^2=693-(1+4+4^2+4^3+4^4)=352=22\cdot16.
\]
The second equality saturates the triangle-inequality bound \(\bigl|\sum_j\alpha_j^2\bigr|\le22\cdot16\). Thus each \(\alpha_j^2=16\), so every \(\alpha_j\in\{4,-4\}\). The first equality forces multiplicities \(15\) and \(7\), respectively. Including the Tate summand, the fourth-cohomology eigenvalues over \(\mathbf F_2\) are \(4\) with multiplicity \(16\) and \(-4\) with multiplicity \(7\). Raising them to the seventh power gives the eigenvalues \(q^2\) (multiplicity \(16\)) and \(-q^2\) (multiplicity \(7\)) over \(\mathbf F_q\). The remaining eigenvalues are \(1,q,q^3,q^4\). The trace formula gives the asserted point counts and zeta function for \(X\) via the universal-homeomorphism span.

**5. Algebraic cycles.** For a finite flat radicial morphism of degree two, flat pullback and proper pushforward on Chow groups compose to multiplication by two in either order: over each irreducible cycle there is one irreducible preimage, and the residue-field degree times its scheme-theoretic multiplicity is two. Therefore both \(\pi\) and \(\rho\) induce isomorphisms of codimension-indexed Chow groups with \(\mathbf Q\)-coefficients, giving the stated correspondence between \(X\) and \(Y\). All fourth-cohomology eigenvalues of \(Y\) over \(\mathbf F_{q^2}\) are \(q^4\); after the Tate twist by two they are \(1\). The characteristic-two Tate theorem for smooth cubic fourfolds (Auel--Kulkarni--Petok--Weinbaum, Theorem 4.10) then supplies \(23\) independent codimension-two cycle classes spanning \(H^4(Y_{\overline{\mathbf F}_2},\mathbf Q_\ell(2))\); finite-flat radicial transfer gives the same conclusion for \(X\).

## Verification
The standalone `verify.py` implements arithmetic in \(\mathbf F_2\), \(\mathbf F_4\), \(\mathbf F_8\), and \(\mathbf F_{16}\), enumerates the values of the binary cubic \(xy(x+y)\), convolves three independent copies, and counts projective points of \(Y\). It checks the formula for the first four extensions of \(\mathbf F_2\) and returns `CUBIC_ZETA_CHECKS_OK`. The infinite extension formula instead follows from the Weil bounds and the two exact small-field counts, as proved above. Finite checks do not substitute for the universal-homeomorphism and eigenvalue arguments.

## Relationship to prior work
Waldron and Witaszek construct the Fano fourfold, the singular \((2,3)\) cover \(H\), and the finite flat radicial quotient \(\pi\), and prove its irregularity and absence of free rational curves. Their inspected complete article does not identify the second radicial projection onto the smooth cubic \(Y\), the cohomological comparison, or the zeta function. An earlier mathematical note concerning the same fourfold determines its bi-anticanonical morphism to \(H^{(2)}\), but not this smooth cubic comparison or the finite-field zeta function. The earlier census of cubic fourfolds over \(\mathbf F_2\) computes the zeta functions of all such cubic fourfolds, so the cubic-side arithmetic is not claimed as new; the new conclusion is the exact arithmetic and cycle-theoretic transfer to the recently constructed irregular Fano fourfold. The census also establishes the Tate theorem used in Step 5. A contemporaneous note on the exceptional vector bundle of \(X\) addresses derived-category structure rather than these arithmetic invariants.

## Limitations
The connection is through finite flat universal homeomorphisms, not an isomorphism of the algebraic varieties. It does not identify Hodge or coherent cohomology, and indeed \(H^1(X,\mathcal O_X)\ne0\) while this cohomology vanishes on the smooth cubic. The Chow-group comparison is rational and makes no integral-torsion assertion. The zeta formula concerns the displayed model over \(\mathbf F_{128}\), with the stated choice of degree-seven parameter, and all its finite-field extensions; it does not classify other forms of the fourfold. The originality assessment is best-of-knowledge rather than an assertion that every unpublished treatment was found.

## References
1. J. Waldron and J. Witaszek, *An irregular smooth Fano fourfold in positive characteristic*, arXiv:2609.29924v1, first submitted 24 September 2026, especially Theorem A and Propositions 3.2--3.6.
2. A. Auel, A. Kulkarni, J. Petok and J. Weinbaum, *A census of cubic fourfolds over the field with two elements*, Mathematics of Computation 94 (2025), 2089--2112, DOI:10.1090/mcom/4010, especially Section 4 and Theorem 4.10.
3. P. Belmans, *An exceptional object for the irregular Waldron--Witaszek Fano fourfold*, 25 September 2026.
4. *The bi-anticanonical map of the irregular Fano fourfold has degree \(8\)*, mathematical research note, 4 October 2026.
