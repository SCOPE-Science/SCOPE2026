# Exact Floquet stability of BDF3 on every positive three-periodic grid

## Finding

Let the positive step lengths of a variable-coefficient third-order backward differentiation formula (BDF3) repeat in the order \(x,y,z,x,y,z,\ldots\), where \(x,y,z>0\). For the homogeneous equation \(y'=0\), let \(F(x,y,z)\) be the propagation matrix over three consecutive steps on the two-dimensional space of successive solution differences. Then both eigenvalues of \(F(x,y,z)\) lie strictly inside the unit disk, for **every** positive triple:

\[
\rho(F(x,y,z))<1\qquad(x,y,z>0).
\]

Nevertheless, the bound is sharp without being attained:

\[
\sup_{x,y,z>0}\rho(F(x,y,z))=1.
\]

Along the explicitly nonuniform family \((x,y,z)=(t,1,t^{-1})\),

\[
\rho(F(t,1,t^{-1}))=1-\frac{16}{3t}+O(t^{-2})\qquad(t\to+\infty).
\]

Consequently, each **fixed** positive three-periodic pattern has decaying parasitic modes and is zero-stable under common scaling of its three steps, although no uniform spectral gap exists over the full family of patterns.

## Assumptions and scope

BDF3 here means that the derivative at the current node is the derivative of the cubic interpolant through the four latest variable-grid nodes, set equal to zero. The step lengths are strictly positive and periodically repeat exactly with period three. The starting values are arbitrary and finite. No forcing, nonlinear dynamics, or nonperiodic step sequence is considered. The Floquet multipliers are eigenvalues of the three-step **difference** propagator; the full four-value recurrence separately preserves a constant solution, corresponding to the neutral multiplier \(1\).

The stability assertion is for each fixed positive triple. The constant in a uniform-in-time bound on the solution may depend on the triple. The statement does not assert a stability constant uniform over triples whose ratios are allowed to degenerate as the mesh is refined.

## Proof

**1. Exact difference reduction.** Write \(d_j=y_j-y_{j-1}\). For current and two preceding step lengths \(u,v,w>0\), cubic interpolation uses the local node coordinates

\[
0,\quad-u,\quad -(u+v),\quad -(u+v+w).
\]

Differentiating their cardinal Lagrange polynomials at \(0\) and setting the BDF3 derivative to zero gives

\[
\begin{pmatrix}d_j\\d_{j-1}\end{pmatrix}=
M(u,v,w)\begin{pmatrix}d_{j-1}\\d_{j-2}\end{pmatrix},
\qquad M(u,v,w)=\begin{pmatrix}a(u,v,w)&-c(u,v,w)\\1&0\end{pmatrix},
\]

where, defining

\[
\begin{aligned}
H(u,v,w)&=3u^2+4uv+2uw+v^2+vw,\\
K(u,v,w)&=u^2+4uv+2uw+3v^2+3vw+w^2,
\end{aligned}
\]

one has

\[
a(u,v,w)=\frac{u^2K(u,v,w)}{v(v+w)H(u,v,w)},\qquad
c(u,v,w)=\frac{u^2(u+v)^2}{w(v+w)H(u,v,w)}.
\]

All denominators and numerators are strictly positive. These identities follow by collecting the three older interpolation values into the differences; the supplied symbolic verifier checks the original differentiated Lagrange polynomials, rather than assuming the recurrence.

**2. Three-step trace and determinant.** Put

\[
A(u,v,w)=wu^2K(u,v,w),\quad C(u,v,w)=vu^2(u+v)^2,\quad D(u,v,w)=vw(v+w)H(u,v,w).
\]

For \(i=1,2,3\), evaluate \((A_i,C_i,D_i)\) at the ordered triples \((x,z,y)\), \((y,x,z)\), \((z,y,x)\), respectively. The period matrix is

\[
F=M(z,y,x)M(y,x,z)M(x,z,y).
\]

Direct multiplication yields \(\operatorname{tr}F=U/P\) and \(\det F=V/P\), where

\[
\begin{aligned}
P&=D_1D_2D_3,\\
U&=A_1A_2A_3-A_3C_2D_1-A_1C_3D_2-A_2C_1D_3,\\
V&=C_1C_2C_3.
\end{aligned}
\]

In particular \(P,V>0\). The characteristic polynomial is \(\lambda^2-(U/P)\lambda+V/P\).

**3. Exact positive Schur certificates.** For a real monic quadratic \(\lambda^2-T\lambda+\Delta\), both roots lie strictly inside the unit circle if and only if \(1-T+\Delta>0\), \(1+T+\Delta>0\), and \(1-\Delta>0\). We establish all three inequalities by positive-polynomial identities.

Define \(s=x+y+z\), \(q_2=xy+xz+yz\), and the strictly positive factor

\[
X=x^2y^2z^2(x+y)(x+z)(y+z).
\]

For nonnegative integer indices, write the ordinary cyclic monomial sum

\[
\mathcal C_{abc}=x^ay^bz^c+y^az^bx^c+z^ax^by^c.
\]

Exact polynomial expansion gives

\[
P-U+V=6Xs^4q_2.
\]

The other two expressions satisfy \(P+U+V=XH_+\), \(P-V=XH_d\), with the **fully explicit** positive-coefficient polynomials

\[
\begin{aligned}
H_+={}&6\mathcal C_{501}+10\mathcal C_{420}+40\mathcal C_{411}+22\mathcal C_{402}\\
&+26\mathcal C_{330}+114\mathcal C_{321}+120\mathcal C_{312}+206x^2y^2z^2,\\[2pt]
H_d={}&3\mathcal C_{510}+6\mathcal C_{501}+17\mathcal C_{420}+47\mathcal C_{411}\\
&+23\mathcal C_{402}+31\mathcal C_{330}+121\mathcal C_{321}\\
&+124\mathcal C_{312}+207x^2y^2z^2.
\end{aligned}
\]

Every cyclic sum displayed is strictly positive when \(x,y,z>0\). These polynomial identities are exact, with no numerical or asymptotic hypotheses. After division by \(P>0\), all three strict Schur inequalities hold; hence \(\rho(F)<1\).

**4. Sharpness and near-neutral degeneration.** Substitute \((x,y,z)=(t,1,t^{-1})\) into the rational formulas for trace and determinant. Exact rational expansion at infinity gives

\[
\operatorname{tr}F=-1+\frac{16}{3t}+O(t^{-2}),\qquad
\det F=\frac1{3t^3}+O(t^{-4}).
\]

The characteristic roots are therefore \(-1+16/(3t)+O(t^{-2})\) and \(O(t^{-3})\). For sufficiently large \(t\), the first root is negative and has the larger modulus, proving the stated spectral-radius expansion. Since the strict bound already holds for every finite positive triple and this family approaches \(1\), the global supremum equals \(1\) and is not attained.

**5. Interpretation for solution values.** For any fixed positive triple, the difference vector after \(k\) periods is \(F^k\) times its initial difference vector, and thus decays geometrically by the strict spectral-radius result. Summing the intervening differences shows that the values \(y_j\) remain bounded and converge to a constant. A common rescaling of all three step lengths leaves the matrices unchanged, giving zero-stability for the fixed periodic ratio pattern.

## Verification

The accompanying Python 3 program `verify_period3.py` uses SymPy to derive the BDF3 recurrence from differentiated cubic Lagrange cardinal polynomials, construct \(P,U,V\), and check the three polynomial identities exactly. It verifies that the three reduced Schur polynomials have respectively 25, 22, and 25 strictly positive monomial coefficients; these counts are supplementary to the explicit expressions above. It also evaluates the trace/determinant degeneration symbolically and makes 1,200 independent numerical comparisons against a fresh cardinal-polynomial implementation. The saved checker output records all checks passing. A finite numerical comparison is not used as proof of the universal statement.

Reproduction: with Python 3, NumPy and SymPy installed, execute `python verify_period3.py` from the directory containing the embedded files. All arguments and random draws are fixed in the supplied source.

## Relationship to prior work

Guglielmi and Zennaro [1] study spectral-radius techniques for variable-step BDF3 zero stability. The publisher's accessible abstract describes a general step-ratio-bound program, not an explicit unrestricted three-periodic classification. Their complete article was not accessible here, so potential equivalent special results within that article remain a material priority risk. Calvo, Grande and Grigorieff [2] give classical step-ratio restrictions. Li and Liao [3], whose complete public preprint was inspected, prove stability subject to a bound of approximately \(2.553\) on almost all adjacent ratios; the patterns considered here can violate that restriction on every period. Söderlind, Fekete and Faragó [4] consider smooth grids with adjacent ratios \(1+O(N^{-1})\), which exclude fixed extreme periodic ratios in the refinement regime. These known sufficient-condition theorems do not by themselves imply the all-triples result.

## Limitations

The claim concerns linear homogeneous zero-stability of fixed exactly three-periodic BDF3 patterns only, not absolute stability for \(y'=\lambda y\), nonlinear convergence, arbitrary nonperiodic meshes, or uniform stability over degenerating ratio families. The earlier primary full text [1] was not inspected despite alternative access attempts, and unlocated equivalent specialist literature remains possible. The result has not undergone independent mathematical audit.

## References

[1] N. Guglielmi and M. Zennaro, *On the zero-stability of variable stepsize multistep methods: the spectral radius approach*, Numerische Mathematik 88 (2001), 445–458. First online 2000-11-08. https://doi.org/10.1007/s211-001-8010-0

[2] M. P. Calvo, T. Grande, and R. D. Grigorieff, *On zero stability of variable order variable stepsize BDF formulas*, Numerische Mathematik 57 (1990), 39–50. https://doi.org/10.1007/BF01386395

[3] Z. Li and H. Liao, *Stability of Variable-Step BDF2 and BDF3 Methods*, SIAM Journal on Numerical Analysis 60 (2022), 2253–2272. Public preprint https://arxiv.org/abs/2201.00527; DOI https://doi.org/10.1137/21M1462398

[4] G. Söderlind, I. Fekete, and I. Faragó, *On the zero-stability of multistep methods on smooth nonuniform grids*, BIT Numerical Mathematics 58 (2018), 1125–1143. https://doi.org/10.1007/s10543-018-0716-y
