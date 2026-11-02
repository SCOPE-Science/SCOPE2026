# Unrestricted two-periodic zero stability of variable-coefficient BDF4, with a BDF5 obstruction

## Finding

The variable-coefficient four-step backward differentiation formula (BDF4) is zero-stable on **every fixed positive two-periodic mesh** with consecutive step lengths \(rh,h,rh,h,\ldots\), for any \(h>0\) and \(r>0\), when applied to \(y'=0\). If \(T(r)\) is the two-step propagation matrix for differences, its three nontrivial multipliers satisfy

\[
\rho(T(r))<1\quad(r>0),\qquad \sup_{r>0}\rho(T(r))=1.
\]

The supremum is approached only by increasingly extreme step alternation, not attained at a finite positive ratio. Indeed,

\[
\rho(T(r))=1-\frac{16}{3r}+O(r^{-2})\quad(r\to\infty),
\]

with the reciprocal formula \(\rho(T(r))=1-\frac{16r}{3}+O(r^2)\) as \(r\to0^+\).

This robustness has an order boundary: the corresponding variable-coefficient **BDF5** is unstable on the alternating mesh of ratio \(r=10\). Its four-dimensional difference monodromy has a real eigenvalue strictly below \(-1\).

## Assumptions and scope

For an integer order \(k\ge2\), take strictly increasing mesh nodes \(t_n\). At the new node \(t_n\), interpolate the preceding \(k+1\) values \(y_n,\ldots,y_{n-k}\) by the unique polynomial of degree at most \(k\), and impose that its derivative at \(t_n\) is zero. This defines the **variable-coefficient** BDF recurrence on the homogeneous scalar equation \(y'=0\). The interpolation coefficients are recomputed from the actual last \(k\) steps and are not the fixed-coefficient Nordsieck stepsize-change technique.

For BDF4, set \(t_n-t_{n-1}\) to alternate between \(rh\) and \(h\) indefinitely. Choose any four initial values. Zero stability here means that for each *fixed* \(r>0\) the homogeneous solution remains uniformly bounded in the number of steps, and in fact converges to a constant. The stability constants are not asserted uniform as \(r\to0\) or \(r\to\infty\). No stability or convergence claim is made for arbitrary nonperiodic grids, nonzero right-hand sides, or nonlinear ODEs.

## Proof

Put \(d_n=y_n-y_{n-1}\) and \(D_n=(d_n,d_{n-1},d_{n-2})^\mathsf T\). For a BDF step of length \(s_0\) preceded by \(s_1,s_2,s_3\), set \(\tau_0=0\), \(\tau_j=-\sum_{\ell=0}^{j-1}s_\ell\), and let \(\omega_j\) denote the derivative at zero of the Lagrange cardinal polynomial for \(\tau_j\). Then \(\sum_{j=0}^4\omega_j y_{n-j}=0\); the coefficients of \(d_{n-1},d_{n-2},d_{n-3}\) are \(-\sum_{j=i+1}^4 c_j\), where \(c_j=-\omega_j/\omega_0\) and \(i=1,2,3\). The standalone checker reconstructs every coefficient from these cardinal polynomials.

After scaling \(h=1\), a current long step and a current short step have companion matrices

\[
F_r=\begin{pmatrix}
\frac{r^2(16r^2+36r+17)}{(r+2)(3r+2)(4r+1)}&
-\frac{r(12r^2+19r+8)}{(r+2)(3r+2)(4r+1)}&
\frac{r^2(2r+1)^2}{(r+2)(3r+2)(4r+1)}\\
1&0&0\\0&1&0
\end{pmatrix},
\]

\[
F_1=\begin{pmatrix}
\frac{17r^2+36r+16}{r(r+4)(2r+1)(2r+3)}&
-\frac{8r^2+19r+12}{(r+4)(2r+1)(2r+3)}&
\frac{(r+2)^2}{r(r+4)(2r+1)(2r+3)}\\
1&0&0\\0&1&0
\end{pmatrix}.
\]

Their two-step product is \(T(r)=F_1F_r\). Direct determinant expansion, verified by rational symbolic identities, gives \(\det(zI-T(r))=P_r(z)/A\), with

\[
\begin{aligned}
A&=24r^4+154r^3+269r^2+154r+24,\\
B&=24r^4+34r^3+5r^2+34r+24,\\
C&=6r^3+19r^2+6r,\\
H&=2r^3+5r^2+2r,\\
P_r(z)&=Az^3+Bz^2+Cz-H.
\end{aligned}
\]

In particular \(A=(r+4)(2r+3)(3r+2)(4r+1)>0\). For the monic real cubic \(z^3+az^2+bz+c\), the strict Schur conditions can be written \(|c|<1\), \(1+a+b+c>0\), \(1-a+b-c>0\), and \(1-b+ac-c^2>0\). They follow by reducing the cubic to its Schur quadratic, and applying the quadratic Jury test.

Here \(a=B/A\), \(b=C/A\), \(c=-H/A\). All requisite quantities have the following **strictly positive polynomial certificates** for every \(r>0\):

\[
\begin{aligned}
A-H&=8(3r^4+19r^3+33r^2+19r+3),\\
A+H&=2(12r^4+78r^3+137r^2+78r+12),\\
P_r(1)&=48(r+1)^4,\\
-P_r(-1)&=32r(4r^2+9r+4),\\
A^2-AC-BH-H^2&=16(36r^8+450r^7+2191r^6+5332r^5\\
&\quad+7112r^4+5332r^3+2191r^2+450r+36).
\end{aligned}
\]

The first two show \(|c|<1\); the next two yield the signs of the characteristic polynomial at \(\pm1\); the last gives \(1-b+ac-c^2>0\). Thus every root lies strictly inside the unit disk. Hence \(D_n\to0\) exponentially per two steps for fixed \(r\), and \(\sum_n|d_n|<\infty\), so \(y_n\) converges.

The polynomial satisfies \(P_r(z)=r^4P_{1/r}(z)\). As \(r\to\infty\), its normalized coefficient vector converges to that of \(z^2(z+1)\); therefore the spectral radius approaches one, proving sharpness. Expanding the simple root at \(-1\) under the substitution \(z=-1+u/r\) gives \(-24u+128=0\), so \(u=16/3\); the other two roots tend to zero. Reciprocity supplies the small-\(r\) asymptotic.

For order five, define the analogous four-dimensional difference companion matrices \(G_{10}\) (step length ten following \(1,10,1,10\)) and \(G_1\) (step length one following \(10,1,10,1\)). Exact-rational interpolation gives

\[
\det(I_4+G_1G_{10})=-\frac{8874496}{44681585}<0.
\]

The monic quartic characteristic polynomial is negative at \(z=-1\) but positive for sufficiently large negative \(z\), hence has a real root \(z<-1\). This proves BDF5 instability on the stated mesh.

## Verification

Run `python verify_bdf4.py` using Python 3, SymPy, and NumPy. The code independently reconstructs the interpolation weights, both companion matrices, the exact characteristic polynomial, five positive Schur certificates, reciprocal symmetry, both boundary limits, and the order-five rational witness. It additionally evaluates 301 sample ratios over five orders of magnitude in either direction. The finite sample is a numerical diagnostic, **not** a proof of the universal stability result; that result uses the displayed identities and the cubic Schur test.

## Relationship to prior work

Variable-coefficient BDF construction follows the classical distinction explained by Skeel (1986). Calvo–Grande–Grigorieff (1990) give zero-stability step-ratio bounds for variable-order BDF on general nonequidistant grids. Guglielmi–Zennaro (2001) analyze the variable-step BDF3 case by spectral radii. Kulikov (2012) studies adaptive variable-stepsize Nordsieck schemes and their error-control behavior; this is the dated archival methodological focal source, not the present BDF4 theorem. Söderlind–Fekete–Faragó (2018) treat smoothly varying grids where consecutive ratios approach unity, unlike an arbitrarily extreme fixed alternation.

The present claim is confined to the **specific two-periodic, variable-coefficient BDF4 family**, with its exact global Schur certificate, sharp nonuniform damping boundary, and explicit order-five obstruction. It does not assert novelty of multistep interpolation or the general spectral-radius method.

## Limitations

Zero stability for each fixed ratio is not uniform zero stability over all ratios. It does not imply A-stability or arbitrary nonperiodic-grid zero stability, nor does the BDF5 witness classify every unstable ratio. Priority comparison is limited because full text of several earlier variable-step BDF stability articles, and supplements to Skeel's 1986 construction paper, could not be completely inspected. Independent mathematical audit remains unperformed.

## References

- R. D. Skeel, “Construction of Variable-Stepsize Multistep Formulas,” *Mathematics of Computation* 47 (1986), 503–510. DOI: 10.1090/S0025-5718-1986-0856699-X.
- M. Calvo, T. Grande, R. D. Grigorieff, “On the Zero Stability of the Variable Order Variable Stepsize BDF-Formulas,” *Numerische Mathematik* 57 (1990), 39–50. DOI: 10.1007/BF01386395.
- N. Guglielmi, M. Zennaro, “On the Zero-Stability of Variable Stepsize Multistep Methods: The Spectral Radius Approach,” *Numerische Mathematik* 88 (2001), 445–458. DOI: 10.1007/s211-001-8010-0.
- G. Yu. Kulikov, “Global Error Control in Adaptive Nordsieck Methods,” *SIAM Journal on Scientific Computing* 34 (2012), A839–A860, published online 27 March 2012. DOI: 10.1137/100791932.
- G. Söderlind, I. Fekete, I. Faragó, “On the Zero-Stability of Multistep Methods on Smooth Nonuniform Grids,” *BIT Numerical Mathematics* 58 (2018), 1199–1221. DOI: 10.1007/s10543-018-0716-y.
- Z. Li, H.-L. Liao, “Stability of Variable-Step BDF2 and BDF3 Methods,” arXiv:2201.00527 (2022).
