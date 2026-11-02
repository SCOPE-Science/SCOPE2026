# Twenty-five rank-zero fibers in a characteristic-eleven genus-four cyclic trigonal pencil

## Finding

Let \(k\) be an algebraically closed field of characteristic \(11\), and let \(C_a\) be the smooth projective model of
\[
 C_a:\quad y^3=x^5+a x^2+1,\qquad a\in k,\quad a^5\ne6.
\]
Every such curve has genus \(4\). Put
\[
 T(a)=2a^{25}-3a^5-3\in\mathbb F_{11}[a].
\]
Its Jacobian has \(a\)-number exactly \(2\) for every smooth parameter, whereas the Jacobian \(11\)-rank satisfies
\[
 f_{11}(C_a)=\begin{cases}0,&T(a)=0,\\2,&T(a)\ne0.\end{cases}
\]
The polynomial \(T\) is separable and factors over \(\mathbb F_{11}\) as
\[
 T(a)=2(a^5-2)\bigl(a^{20}+2a^{15}+4a^{10}-3a^5-2\bigr).
\]
Both displayed factors are irreducible over \(\mathbb F_{11}\). Hence there are precisely \(25\) distinct smooth geometric rank-zero *marked parameters*: their Frobenius orbit lengths are \(5\) and \(20\), with no rank-zero parameter defined over \(\mathbb F_{11}\). More precisely, over \(\mathbb F_{11^m}\) their number is
\[
 5\mathbf 1_{5\mid m}+20\mathbf 1_{20\mid m}.
\]
The fivefold parameter symmetry \(a\mapsto\zeta^2a\), for \(\zeta^5=1\), preserves the curve's geometric isomorphism class; the result counts coefficient-marked parameters, not distinct isomorphism classes.

## Assumptions and scope

All quantities concern the Jacobian of the smooth projective normalization over an algebraically closed field of characteristic \(11\). Here \(f_{11}\) is the stable Frobenius rank (equivalently the Jacobian \(11\)-rank), and the \(a\)-number is \(\dim_k\operatorname{Hom}(\alpha_{11},J[11])\), equivalently \(4\) minus the Cartier rank. Singular parameters are excluded. The threefold cover is tame, and the exponent pair \((3,5)\) is coprime.

## Proof

**1. Smoothness and genus.** Write \(F=x^5+ax^2+1\). Its ordinary characteristic-zero discriminant is \(108a^5+3125\). Reducing modulo \(11\) gives
\[
 \operatorname{disc}_x(F)=1-2a^5=-2(a^5+5).
\]
It vanishes exactly when \(a^5=6\). Otherwise the tame cyclic degree-three cover of the \(x\)-line is totally ramified over the five finite simple roots and infinity. Riemann–Hurwitz gives
\[
 2g-2=3(-2)+6(3-1)=6,\quad g=4.
\]

**2. Cartier basis and matrix.** At the unique place over infinity, \(\operatorname{ord}_{\infty}(x)=-3\), \(\operatorname{ord}_{\infty}(y)=-5\), and \(\operatorname{ord}_{\infty}(dx)=-4\). Thus a regular differential basis is
\[
 \omega_0=\frac{dx}{y},\quad \omega_1=\frac{dx}{y^2},\quad
 \omega_2=\frac{x\,dx}{y^2},\quad \omega_3=\frac{x^2\,dx}{y^2}.
\]
For the Cartier operator \(\mathcal C\), the rule on powers of the separating coordinate is
\[
 \mathcal C(x^n dx)=0\ \text{unless }n\equiv10\pmod{11},\qquad
 \mathcal C(x^{11j+10}dx)=x^j dx.
\]
Since \(y^{-1}=F^7y^{-22}\) and \(y^{-2}=F^3y^{-11}\), coefficient extraction from \(F^7\) at degrees \(10,21,32\), and from \(F^3\) at degrees \(10,9,8\), respectively yields
\[
 A=(-a^5-1,-3a^3,-4a)^t,\qquad B=(3,3a^2,0).
\]
Specifically,
\[
 \mathcal C(\omega_0)=\sum_{j=0}^{2}A_j^{1/11}\omega_{j+1},\qquad
 \mathcal C(\omega_{j+1})=B_j^{1/11}\omega_0.
\]
Both \(A\) and \(B\) are nonzero for all \(a\): \(B_0=3\), and \(A_0\ne0\) if \(a=0\) while \(A_2\ne0\) if \(a\ne0\). Therefore the Cartier rank is always exactly \(2\), and the \(a\)-number is exactly \(4-2=2\).

**3. Correct semilinear iteration.** The Hasse–Witt operator is \(11\)-linear; in the dual basis one may use the matrix
\[
 H=\begin{pmatrix}
 0&A_0&A_1&A_2\\
 B_0&0&0&0\\
 B_1&0&0&0\\
 B_2&0&0&0
 \end{pmatrix}.
\]
Its iterates are products \(H H^{(11)}\cdots H^{(11^r)}\), with Frobenius applied *entrywise*. The upper-left entry of \(H H^{(11)}\) is
\[
 \sum_{j=0}^{2}A_j B_j^{11}
 =3(-a^5-1)+(-3a^3)(3a^2)^{11}
 =2a^{25}-3a^5-3=T(a).
\]
The other nonzero diagonal block of \(H H^{(11)}\) is the rank-one matrix \(B(A^{(11)})^t\). Consequently, if \(T(a)\ne0\), both cyclic eigenspace channels survive under every iteration and the stable rank is \(2\). If \(T(a)=0\), then \(H H^{(11)}H^{(11^2)}=0\): its two potentially nonzero blocks involve \(T\) and \(T^{11}\), respectively. Thus the stable rank is \(0\). In particular, a single untwisted matrix square would be inadequate.

**4. The exceptional points.** In \(\mathbb F_{11}[z]\) let
\[
 Q(z)=2z^5-3z-3=2(z-2)G(z),\qquad
 G(z)=z^4+2z^3+4z^2-3z-2.
\]
Then \(T(a)=Q(a^5)\). The polynomial \(G\) is irreducible: Euclidean reduction gives
\[
 z^{121}-z\equiv -5z^3+4z^2+3z+1\pmod{G},
 \qquad\gcd(G,z^{121}-z)=1.
\]
A reducible quartic over \(\mathbb F_{11}\) has an irreducible factor of degree at most \(2\), so this gcd suffices. The fifth powers in \(\mathbb F_{11}^{\times}\) are \(\{1,-1\}\); therefore \(z^5-2\) is irreducible by the finite-field Kummer criterion (\(\mu_5\subset\mathbb F_{11}\)). For a root \(\eta\) of \(G\), its norm from \(\mathbb F_{11^4}\) to \(\mathbb F_{11}\) equals \(G(0)=-2=9\), which is not a fifth power in \(\mathbb F_{11}\). Hence \(\eta\) is not a fifth power in \(\mathbb F_{11^4}\); the polynomial \(X^5-\eta\) is irreducible there. It follows that \(G(a^5)\) is irreducible of degree \(20\) over \(\mathbb F_{11}\).

Every irreducible polynomial over a finite field is separable, so the two factors exhibit exactly \(5+20\) distinct geometric roots and the claimed two Frobenius orbits. At the singular parameter value \(a^5=6\) one has \(Q(6)=10\ne0\), so all \(25\) exceptional points are smooth. Finally, an element of degree \(d\) over \(\mathbb F_{11}\) belongs to \(\mathbb F_{11^m}\) precisely when \(d\mid m\), proving the counting formula.

**5. Marking symmetry.** If \(\zeta\) is a fifth root of unity then the coordinate replacement \(x\mapsto\zeta x\) transforms \(x^5+a x^2+1\) into \(x^5+(\zeta^2a)x^2+1\). Thus the coefficient-marked roots may represent fewer isomorphism classes than \(25\). No stronger isomorphism classification is used.

## Verification

Run `python3 verify_symbolic.py` (requires SymPy) and `python3 verify_fields.py` (standard library only) in the same directory. The first reconstructs all necessary coefficients, discriminant, factorization, coprimality, separability, and irreducibility tests. The second independently implements finite fields \(\mathbb F_{11}\), \(\mathbb F_{11^5}\), and \(\mathbb F_{11^{20}}\), and computes four successive Frobenius-twisted Hasse–Witt products on the two exceptional field generators and all eleven base-field parameters. Its rank sequences at either exceptional generator are \((2,1,0,0,0)\), while the base-field sequences are constantly \(2\). The finite calculations corroborate, but do not substitute for, the symbolic proof of exhaustiveness over the algebraic closure.

## Relationship to prior work

The general Cartier–Manin coefficient method and caution about the orientation of semilinear products are established by Sutherland and Achter–Howe. Camacho-Navarro studies genus-four \(a\)-numbers, \(p\)-ranks, and Cartier points, including a sample over \(\mathbb F_{11}\), but does not state this geometric-parameter classification. Sohn studies genus-four superelliptic \(a\)-numbers; only the abstract of that later paper was accessible, so its complete coverage of individual families cannot be excluded here. An earlier calculation of the related characteristic-eleven family \(y^3=x^5+Ax+B\) does not by itself give the stated degeneration polynomial for the different marked pencil \(y^3=x^5+ax^2+1\). The evaluated contribution is the exact stable-rank locus and its degree-five/degree-twenty Frobenius splitting, rather than the general coefficient algorithm or the standalone constant \(a\)-number.

## Limitations

The theorem makes no claim that these are all genus-four trigonal curves with \(11\)-rank zero, no claim that rank-zero Jacobians are supersingular, and no count of geometric isomorphism classes. Parameters refer to the displayed coefficient-normalized pencil. A potentially relevant 2025 paper could be compared only at the abstract level, and earlier unindexed equivalent formulations could exist; no independent external audit has been performed.

## References

1. J. D. Achter and E. W. Howe, *Hasse–Witt and Cartier–Manin matrices: a warning and a request*, arXiv:1710.10726, first public 2017-10-30.
2. A. V. Sutherland, *Counting points on superelliptic curves in average polynomial time*, arXiv:2004.10189, first public 2020-04-21.
3. C. Camacho-Navarro, *The \(a\)-number, \(p\)-rank and Cartier points of genus \(4\) curves*, arXiv:2012.08705, 2020-12-17.
4. G. Sohn, *The \(a\)-number of superelliptic curves of genus four*, Journal of Applied and Pure Mathematics 7 (2025), 59–66, DOI:10.23091/japm.2025.059. Abstract inspected; full text unavailable at review.
