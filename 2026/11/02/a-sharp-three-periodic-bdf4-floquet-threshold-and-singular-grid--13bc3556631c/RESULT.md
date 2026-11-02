# A sharp three-periodic BDF4 Floquet threshold and singular-grid stability frontier

## Finding

Consider the genuine variable-coefficient four-step backward differentiation formula (BDF4) for the homogeneous differential equation \(y'=0\), with a positive step sequence that repeats as \((1,R,3)\) up to a common positive scale, where \(R>0\). Write \(T_R\) for the three-step monodromy of the three-dimensional *difference* recurrence (the constant solution mode has already been removed). Define

\[
\begin{aligned}
P(R)={}&R^7-38R^6-1120R^5-10170R^4-42193R^3\\
&-81856R^2-60496R-3104.
\end{aligned}
\]

This polynomial has exactly one positive zero, \(R_*=59.7836545406779490\ldots\). The exact classification is

\[
\rho(T_R)<1\quad(0<R<R_*),\qquad
-1\in\sigma(T_{R_*}),\qquad
\rho(T_R)>1\quad(R>R_*).
\]

At \(R=R_*\), the multiplier \(-1\) is simple and the other two parasitic multipliers lie strictly inside the unit disk. For every \(R>R_*\), there is a real parasitic multiplier strictly below \(-1\). Hence the periodic homogeneous recurrence is power-bounded, including at the neutral boundary, precisely when \(0<R\le R_*\), and is exponentially unstable for \(R>R_*\).

The finite threshold at \(s=3\), the smallest integer above the singular instability boundary \(s=2\), is a natural representative of a larger singular-grid transition: for any fixed \(s>0\), the three parasitic multipliers for steps \((1,R,s)\), as \(R\to\infty\), converge as a multiset to the roots of

\[
z\left[z^2+\frac{2(8s-1)}{7(s+2)}z+\frac{s}{7(s+2)}\right]=0.
\]

The limiting parasitic spectrum lies strictly inside the unit disk for \(0<s<2\), has one simple multiplier \(-1\) for \(s=2\), and contains one real multiplier less than \(-1\) for \(s>2\). Consequently, sufficiently large \(R\) is strictly damping for each fixed \(0<s<2\) and is unstable for each fixed \(s>2\). No assertion of strict damping at finite \(R\) when \(s=2\) is needed for this singular-limit claim.

## Assumptions and scope

For any current index \(j\), let its four preceding positive step lengths be \(h_j,h_{j-1},h_{j-2},h_{j-3}\). Form interpolation nodes

\[
x_0=0,\qquad x_\ell=-\sum_{k=0}^{\ell-1}h_{j-k}\quad(1\le\ell\le4),
\]

and let \(a_\ell\) be the derivative at zero of the \(\ell\)-th Lagrange cardinal polynomial on these five nodes. The genuine variable-coefficient BDF4 recurrence on \(y'=0\) is \(\sum_{\ell=0}^4 a_\ell y_{j-\ell}=0\). This is not the fixed-coefficient Nordsieck interpolation variant. All steps are strictly positive, the pattern repeats indefinitely, and stability means bounded powers of its exact Floquet monodromy for arbitrary starting differences. A common multiplication of every step leaves these homogeneous coefficients unchanged.

## Proof

Set \(d_j=y_j-y_{j-1}\). Since \(\sum_{\ell=0}^4 a_\ell=0\), the state \((d_j,d_{j-1},d_{j-2})^\mathsf T\) is propagated by the companion matrix

\[
M_j=\begin{pmatrix}
(a_2+a_3+a_4)/a_0&(a_3+a_4)/a_0&a_4/a_0\\
1&0&0\\0&1&0
\end{pmatrix}.
\]

For \((h_0,h_1,h_2)=(1,R,3)\), define \(T_R=M_2M_1M_0\), taking earlier step indices modulo three. Direct rational interpolation and multiplication give

\[
\det(zI-T_R)=z^3+\frac{2U(R)}{D(R)}z^2+
\frac{V(R)}{D(R)}z-\frac{W(R)}{D(R)},
\]

where all the following are explicit integer polynomials:

\[
\begin{aligned}
D={}&(5R^2+53R+136)(R^3+23R^2+145R+267)\\
&\quad\cdot(7R^3+37R^2+52R+16),\\
U={}&23R^8+569R^7+5833R^6+32661R^5+112864R^4\\
&+264082R^3+443584R^2+497504R+267072,\\
V={}&3R^8+57R^7+490R^6+2558R^5+8743R^4\\
&+19753R^3+31676R^2+39280R+27648,\\
W={}&12R(R+1)(R+3)(R+4)^3.
\end{aligned}
\]

For a real monic cubic \(z^3+az^2+bz+c\), the strict Schur–Jury conditions are \(|c|<1\), \(1+a+b+c>0\), \(1-a+b-c>0\), and \(1-b+ac-c^2>0\). Here they reduce to

\[
\begin{gathered}
D-W>0,\qquad D+2U+V-W>0,\\
D-2U+V+W>0,\\
Q:=D^2-DV-2UW-W^2>0.
\end{gathered}
\]

These inequalities are certified *for all positive* \(R\), not merely sampled numerically, as follows. The polynomials \(D-W\), \(D+2U+V-W\), and \(Q\) have exclusively strictly positive coefficients. For an explicit certificate of the largest one, its coefficients \((q_0,\ldots,q_{16})\) in \(Q(R)=\sum_{k=0}^{16}q_kR^k\) are

```text
321488437248, 2732565940224, 9529361608704,
18272643316608, 22095231300320, 18208250085888,
10720450858830, 4642890653484, 1504428362552,
367538058524, 67663326556, 9302439340,
936646120, 66726436, 3166454, 89192, 1120
```

The remaining condition factors exactly as

\[
D-2U+V+W=-8(R+3)P(R).
\]

The coefficient sequence of \(P\), descending in degree, has one sign change, and \(P(0)<0\), \(P(R)\to+\infty\). Descartes' rule and continuity yield a unique positive zero \(R_*\), with \(59<R_*<60\). Thus all three strict Schur conditions hold for \(R<R_*\), while for \(R>R_*\) one has \(\det(-I-T_R)=8(R+3)P(R)/D>0\). Since the characteristic polynomial tends to \(-\infty\) on the negative real axis, it has a real root \(z<-1\). At equality, the other strict Jury inequalities imply that the remaining quadratic factor has both roots strictly inside the disk: in particular, at \(z=-1\) its \(1+a+b+c\) and \(1-b+ac-c^2\) inequalities give the necessary positive quadratic endpoint tests. Hence \(-1\) is simple and neutral.

For the more general pattern \((1,R,s)\), let \((u_i,v_i,w_i)\) denote the first row of each \(M_i\) for \(i=0,1,2\). Exact rational differentiation gives, for fixed \(s>0\),

\[
\begin{aligned}
(u_0,v_0,w_0)&=\left(\frac1{s(s+2)}+O(R^{-1}),\ -\frac{4(s+1)^2}{s+2}R^{-3}+O(R^{-4}),\ \frac{(s+1)^2}{s+2}R^{-2}+O(R^{-3})\right),\\
(u_1,v_1,w_1)&=\left(\frac{4R^2}{7(s+1)}+O(R),\ -\frac{4R^2}{7s(s+1)}+O(R),\ \frac17+O(R^{-1})\right),\\
(u_2,v_2,w_2)&=\left(6s^2R^{-2}+O(R^{-3}),\ -\frac{s^2}{s+1}+O(R^{-1}),\ \frac{s}{s+1}+O(R^{-1})\right).
\end{aligned}
\]

A product of three companion matrices has trace \(u_0u_1u_2+u_0v_2+u_1v_0+u_2v_1+w_0+w_1+w_2\), second elementary spectral symmetric function \(u_0v_2w_1+u_1v_0w_2+u_2v_1w_0-v_0v_1v_2+w_0w_1+w_0w_2+w_1w_2\), and determinant \(w_0w_1w_2\). Substitution gives respectively

\[
-\frac{2(8s-1)}{7(s+2)}+O(R^{-1}),\quad
\frac{s}{7(s+2)}+O(R^{-1}),\quad O(R^{-2}).
\]

For the limiting quadratic \(z^2+az+b\), \(b=s/[7(s+2)]\in(0,1)\), and

\[
1+a+b=\frac{24s+12}{7(s+2)}>0,\qquad
1-a+b=\frac{8(2-s)}{7(s+2)}.
\]

The quadratic Schur criterion proves the stated sharp singular frontier. At \(s=2\), its roots are exactly \(-1\) and \(-1/14\), along with the limiting zero root.

## Verification

The standalone `verify.py` independently constructs the Lagrange weights and three transfer matrices, checks the exact cubic characteristic coefficients and the factorization by \(P\), expands all three strictly positive polynomial certificates including the 17-coefficient degree-sixteen identity, proves the unique positive threshold by signs, verifies all nine general-\(s\) asymptotic terms symbolically, and cross-checks seven rational sample ratios by direct matrix characteristic polynomials. It passed in the delivered package using Python 3 and SymPy. The symbolic identities, not the finite samples, support the universal claim.

## Relationship to prior work

Skeel's *Construction of Variable-Stepsize Multistep Formulas* (1986, DOI 10.1090/S0025-5718-1986-0856699-X) establishes the actual variable-coefficient construction, not the present three-periodic Floquet threshold. Calvo, Grande and Grigorieff's *On the zero stability of the variable order variable stepsize BDF-formulas* (1990, DOI 10.1007/BF01386395) gives general step-ratio bounds; only its abstract and bibliographic details could be inspected, so its complete contents remain a priority risk. Skeel and Jackson's 1983 Nordsieck stability paper (DOI 10.1137/0720056) studies a different step-size adaptation; its full text was also inaccessible. Söderlind, Fekete and Faragó (2018, DOI 10.1007/s10543-018-0716-y) treat smoothly deformed nonuniform meshes with ratios asymptotic to one, not this fixed high-contrast three-periodic family. No inspected result stated or implied the exact degree-seven threshold, although nonappearance in a search is not a proof of novelty.

## Limitations

The theorem treats homogeneous zero stability for *genuine variable-coefficient* BDF4 on strictly three-periodic grids and its singular \(R\to\infty\) limit. It makes no claims about arbitrary nonperiodic grids, Nordsieck fixed-coefficient implementations, A-stability, or convergence on nonzero ODEs. At the finite threshold the parasitic \(-1\) multiplier is neutral, not strictly damped. Inaccessible specialist literature leaves an originality risk; no independent mathematical review has been performed.

## References

1. R. D. Skeel, “Construction of Variable-Stepsize Multistep Formulas,” *Mathematics of Computation* 47 (1986), 503–510, DOI: https://doi.org/10.1090/S0025-5718-1986-0856699-X. Author-uploaded full-text copy: https://www.researchgate.net/publication/278992956_Construction_of_variable-stepsize_multistep_formulas.
2. M. Calvo, T. Grande, R. D. Grigorieff, “On the zero stability of the variable order variable stepsize BDF-formulas,” *Numerische Mathematik* 57 (1990), 39–50, https://doi.org/10.1007/BF01386395. Public author-upload metadata: https://www.researchgate.net/publication/226854075_On_the_zero_stability_of_the_variable_order_variable_stepsize_BDF-Formulas.
3. R. D. Skeel and L. W. Jackson, “The Stability of Variable-Stepsize Nordsieck Methods,” *SIAM Journal on Numerical Analysis* 20 (1983), 840–853, https://doi.org/10.1137/0720056.
4. G. Söderlind, I. Fekete and I. Faragó, “On the zero-stability of multistep methods on smooth nonuniform grids,” *BIT Numerical Mathematics* 58 (2018), 1125–1143, https://doi.org/10.1007/s10543-018-0716-y (open-access full text).
