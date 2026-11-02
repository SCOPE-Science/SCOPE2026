# A 24-point \(7\)-rank-one stratum in a bielliptic cyclic trigonal family of genus four

## Finding

Let \(k=\overline{\mathbb F}_7\) and let \(C_{a,b}\) be the smooth projective model of
\[
y^3=x^6+a x^4+b x^2+1,\qquad (a,b)\in k^2.
\]
Put
\[
\Delta=a^2b^2+3a^3+3b^3-3ab+1,\qquad H=ab+1,
\]
and define the degree-eight polynomial
\[
q(z)=z^8+3z^7+3z^6+3z^5+5z^4+4z^3+3z^2+4z+1
\quad\text{in }\mathbb F_7[z].
\]
The curve is smooth of genus four precisely when \(\Delta\ne0\). For every such coefficient-marked parameter, its Jacobian \(a\)-number and \(7\)-rank satisfy
\[
\boxed{(a(C_{a,b}),f_7(C_{a,b}))=
\begin{cases}
(0,4),&H\ne0,\\
(2,2),&H=0\text{ and }q(b^3)\ne0,\\
(2,1),&H=0\text{ and }q(b^3)=0.
\end{cases}}
\]
There are exactly 24 smooth geometric coefficient-marked parameters of \(7\)-rank one. Their \(b\)-coordinates are the distinct roots of eight irreducible cubic polynomials over \(\mathbb F_7\), so they form eight Frobenius orbits of degree three. In particular no smooth curve in this family has \(7\)-rank zero or three, and no such curve has \(a\)-number one, three, or four. The coefficient-normalized Hasse determinant is \(3H^2\Delta^2\); consequently, on the smooth coefficient parameter space the nonordinary Hasse divisor is exactly twice the reduced smooth hyperbola \(H=0\).

## Assumptions and scope

All polynomial identities are in characteristic seven. All parameter counts refer to distinct pairs \((a,b)\), not geometric isomorphism classes. The family has a natural involution \((x,y)\mapsto(-x,y)\), whose quotient is the genus-one cubic cover \(y^3=t^3+at^2+bt+1\), with \(t=x^2\). This makes the family a natural bielliptic subfamily of genus-four cyclic trigonal curves. The order-three symmetry \(y\mapsto\zeta_3y\) commutes with the involution.

The cubic \(t^3+at^2+bt+1\) has discriminant \(\Delta\). Its constant coefficient is nonzero, so its roots are nonzero, and \(x^6+ax^4+bx^2+1\) has six distinct roots exactly when \(\Delta\ne0\). The degree-three morphism to the \(x\)-line is totally ramified at these six roots and unramified above infinity; Riemann–Hurwitz gives \(2g-2=3(-2)+6(3-1)=6\), hence \(g=4\).

## Proof

For this family, regular differentials have basis
\[
\omega_0=\frac{dx}{y},\quad
\omega_1=\frac{dx}{y^2},\quad
\omega_2=\frac{x\,dx}{y^2},\quad
\omega_3=\frac{x^2dx}{y^2}.
\]
Indeed these forms are regular at the six finite branch points (use \(y\) as a local parameter), and at the three points above infinity they have nonnegative orders \(0,2,1,0\), respectively. Their number equals the genus.

Write \(F(x)=x^6+ax^4+bx^2+1=q_0(x^2)\), where \(q_0(t)=t^3+at^2+bt+1\). For \(j=1,2\), the Cartier coefficient rule is
\[
\mathcal C\left(\frac{x^i dx}{y^j}\right)=
\sum_{r\ge0}\left([x^{7r+6-i}]F^{2j}\right)^{1/7}
\frac{x^r dx}{y^j}.
\]
Let \(c_r=[t^r]q_0(t)^4\). In the ordered differential basis above, the seventh powers of the Cartier matrix coefficients form a block matrix: a scalar \(d=[t^3]q_0(t)^2=2H\), and the \(3\)-by-\(3\) matrix
\[
M_2=\begin{pmatrix}
c_3&0&c_2\\
0&c_6&0\\
c_{10}&0&c_9
\end{pmatrix}.
\]
Direct expansion in \(\mathbb F_7[a,b]\) yields
\[
\begin{aligned}
c_2&=-3a-b^2,\\
c_3&=-2ab-3b^3-3,\\
c_6&=-\Delta,\\
c_9&=-3a^3-2ab-3,\\
c_{10}&=-a^2-3b,
\end{aligned}
\qquad
c_3c_9-c_2c_{10}=2H\Delta.
\]
Thus the determinant of the coefficient matrix is
\[
d\,c_6(c_3c_9-c_2c_{10})=3H^2\Delta^2.
\]
If \(\Delta H\ne0\), the Cartier operator has rank four and the curve is ordinary, with \(a\)-number zero and \(7\)-rank four.

Suppose \(H=0\) and \(\Delta\ne0\). Then \(b\ne0\) and \(a=-b^{-1}\). The scalar \(d\) is zero, the isolated scalar \(c_6=-\Delta\) is invertible, and the remaining \(2\)-by-\(2\) coefficient block is exactly
\[
B=\begin{pmatrix}
c_3&c_2\\c_{10}&c_9
\end{pmatrix}
=\begin{pmatrix}1\\ b^{-2}\end{pmatrix}
\begin{pmatrix}A&C/b\end{pmatrix},
\qquad A=-3b^3-1,\quad C=3-b^3.
\]
The row \((A,C/b)\) cannot vanish: \(C=0\) implies \(b^3=3\), which gives \(A=-3\ne0\). Thus \(B\) has rank one, the full Cartier rank equals two, and the \(a\)-number is exactly two.

For the \(7\)-rank, it is crucial to respect semilinearity. The Frobenius matrix on cohomology is the transpose of this coefficient Cartier matrix. Its second iterate on the two-dimensional block has matrix \((B^{[7]}B)^T\), not \((BB^{[7]})^T\). Write \(B=uv\) with \(u=(1,b^{-2})^T\) and \(v=(A,C/b)\). Then
\[
B^{[7]}B=u^{[7]}(v^{[7]}u)v,
\qquad v^{[7]}u=A^7+\frac{C^7}{b^9}.
\]
The scalar is zero exactly when
\[
P(b):=b^9A^7+C^7=-3b^{30}-b^{21}-b^9+3=0.
\]
If it is nonzero, every successive Frobenius-twisted factor is a seventh-power conjugate of a nonzero scalar, so the stable rank of the \(2\)-by-\(2\) block is one. If it is zero, the second iterate already vanishes, so its stable rank is zero. The permanently invertible \(1\)-by-\(1\) block \(c_6\) contributes exactly one, and the zero block \(d\) contributes zero. Thus \(f_7=2\) or \(1\), respectively.

Put \(D(b)=b^6+4b^3-1\). Two exact identities in \(\mathbb F_7[b,b^{-1}]\) are
\[
\left.\Delta\right|_{a=-b^{-1}}=\frac{3D(b)}{b^3},
\qquad P(b)=-3D(b)q(b^3).
\]
Since smoothness excludes \(D(b)=0\), the stable rank drops precisely when \(q(b^3)=0\). Finally, \(q(b^3)\) is the product, in \(\mathbb F_7[b]\), of the following eight monic cubic factors:
\[
\begin{aligned}
&b^3+2,\quad b^3+3,\quad b^3+3b-2,\quad b^3-2b-2,\\
&b^3-b-2,\quad b^3+3b^2-3,\quad b^3-2b^2-3,\quad b^3-b^2-3.
\end{aligned}
\]
Each has no root in \(\mathbb F_7\), so each is irreducible of degree three. They are pairwise distinct, their product is squarefree, and \(\gcd(D,q(b^3))=1\). Hence exactly 24 distinct smooth geometric marked parameters satisfy the deepest rank equation, arranged in eight degree-three Frobenius orbits. This proves the classification.

## Verification

The standalone script `verify_symbolic.py` reconstructs the coefficient identities from \(q_0(t)^2\) and \(q_0(t)^4\), checks the Hasse determinant and correct Frobenius-order rank-one scalar, confirms the degree-24 factorization, tests the eight cubics for irreducibility, and checks disjointness from the discriminant. It prints `SYMBOLIC_GF7_HASSE_DETERMINANT_AND_24_P_RANK_EXCEPTIONAL_PARAMETERS_OK` on success.

The independent script `verify_fields.py` performs direct polynomial convolution for \(F(x)^2\) and \(F(x)^4\), without importing the symbolic verifier, and independently forms the Frobenius-twisted block products over \(\mathbb F_7\), \(\mathbb F_{49}\), and \(\mathbb F_{343}\). In these three fields respectively, it finds smooth counts \((37,6,0)\), \((2311,42,0)\), and \((116965,318,24)\) in the three strata (ordinary, \(7\)-rank two, \(7\)-rank one), with singular-model counts \(6\), \(48\), and \(342\). These finite enumerations corroborate, but do not replace, the unrestricted symbolic argument.

To reproduce, execute `python3 verify_symbolic.py` (requires SymPy) and `python3 verify_fields.py` (Python standard library only) from the directory containing the files.

## Relationship to prior work

Ogasawara, Ohashi, Sakata, and Harashita study genus-four double covers of elliptic curves, their smoothness conditions and superspecial cases (arXiv:2403.08139v1, first public version March 12, 2024). That work motivates this bielliptic subfamily but does not provide the 24-point \(7\)-rank-one classification; the present quotient elliptic curves are ordinary, so superspecial enumeration is not equivalent. The Frobenius-versus-Cartier transpose and semilinear iteration follow the conventions clarified by Achter and Howe (arXiv:1710.10726).

Borges and Gonçalves (arXiv:2212.03987) analyze \(p\)-ranks of Fermat-type curves and several related families; the inspected full arXiv paper (its main Fermat-type theorem and Section 6 examples) does not cover the present two-parameter full stratification. Sohn's 2025 article on \(a\)-numbers of genus-four superelliptic curves (DOI:10.23091/japm.2025.059) is a plausible overlap source for the \(a\)-number portion, but its full text could not be accessed for a decisive comparison; this is an explicit priority risk, especially for auxiliary statements about Cartier ranks. The exact 24-point stable-rank classification is not claimed to be independent of all unpublished or unindexed calculations.

## Limitations

The result is a classification of coefficient-marked smooth fibers over an algebraic closure, not a classification of geometric isomorphism classes. It establishes the \(a\)-number and \(7\)-rank but not the full Ekedahl–Oort types or Newton polygons. The nonordinary Hasse divisor identity is part of the proof and not independently claimed as novel beyond previous general methods. An inaccessible 2025 source and possible unindexed studies leave residual literature-priority risk. No independent external audit or validation is claimed.

## References

1. T. Ogasawara, R. Ohashi, K. Sakata, and S. Harashita, *Superspecial genus-4 double covers of elliptic curves*, arXiv:2403.08139v1 (2024), https://arxiv.org/abs/2403.08139.
2. J. D. Achter and E. W. Howe, *Hasse–Witt and Cartier–Manin matrices: A warning and a request*, arXiv:1710.10726 (2017), https://arxiv.org/abs/1710.10726.
3. H. Borges and C. Gonçalves, *The p-rank of curves of Fermat type*, arXiv:2212.03987, https://arxiv.org/abs/2212.03987.
4. G. Sohn, *The a-number of superelliptic curves of genus four*, Journal of Applied and Pure Mathematics 7 (2025), 59–66, DOI:10.23091/japm.2025.059.
