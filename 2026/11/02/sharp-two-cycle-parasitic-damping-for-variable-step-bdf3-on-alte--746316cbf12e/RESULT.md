# Sharp two-cycle parasitic damping for variable-step BDF3 on alternating grids

## Finding
For every real ratio \(r>0\), apply the ordinary interpolation-based variable-step third-order backward differentiation formula (BDF3) on the homogeneous differential equation \(y'(t)=0\), with step lengths alternating indefinitely between \(h>0\) and \(rh\). Let \(d_n=y_n-y_{n-1}\). The transfer of \((d_n,d_{n-1})^\mathsf T\) over any complete pair of consecutive steps has both eigenvalues \(z\) satisfying
\[
|z|<\frac15.
\]
This is **sharp as a uniform bound on two-step spectral radii**: the supremum over all \(r>0\) is exactly \(1/5\), approached as \(r\to0^+\) or \(r\to\infty\), but never attained at a positive finite ratio. In particular, for each fixed positive \(r\), all parasitic increments decay geometrically and every numerical solution converges to a finite constant, even when one adjacent-step ratio exceeds the usual general-mesh sufficient BDF3 restriction on infinitely many steps. The multiplier spectra are invariant under swapping \(r\) and \(1/r\).

## Assumptions and scope
The real or complex scalar sequence \((y_n)_{n\ge0}\) starts from arbitrary finite values \(y_0,y_1,y_2\). At each \(n\ge3\), its next value is determined by the standard BDF3 equation \((\Pi_{n,3}y)'(t_n)=0\), where \(\Pi_{n,3}y\) is the degree-at-most-three Lagrange interpolant through the four data \((t_{n-j},y_{n-j})\), \(j=0,1,2,3\). Each mesh width \(h_n=t_n-t_{n-1}>0\) alternates between \(h\) and \(rh\); the starting phase is arbitrary. No time-dependent right-hand side or nonzero eigenvalue stability region is considered.

The conclusion controls the **spectral radius of the two-step parasitic map**, not its operator norm in a common norm, and does not assert a stability constant uniform in the varying ratio \(r\). The exact zero-stability claim is for every *fixed* ratio, as the number of alternations grows.

## Proof
For three successive positive widths \((a,b,c)=(h_n,h_{n-1},h_{n-2})\), differentiate the cubic interpolant at its newest node. After eliminating the constant solution mode, the homogeneous BDF3 equation has the two-difference recurrence
\[
\begin{pmatrix}d_n\\d_{n-1}\end{pmatrix}
=T(a,b,c)\begin{pmatrix}d_{n-1}\\d_{n-2}\end{pmatrix},
\qquad T(a,b,c)=\begin{pmatrix}U(a,b,c)&V(a,b,c)\\1&0\end{pmatrix}.
\]
The entries follow uniquely by differentiating the Lagrange basis at the four nodes \(0,-a,-a-b,-a-b-c\). Because multiplication of all widths by a common positive scalar leaves the homogeneous equation unchanged, take \(h=1\).

For the two alternating width triples \((r,1,r)\) and \((1,r,1)\), direct simplification yields
\[
T_A=\begin{pmatrix}
\dfrac{r^2(4r+3)}{5r^2+5r+1}&-\dfrac{r(r+1)}{5r^2+5r+1}\\
1&0
\end{pmatrix},\qquad
T_B=\begin{pmatrix}
\dfrac{3r+4}{r(r^2+5r+5)}&-\dfrac{r+1}{r^2+5r+5}\\
1&0
\end{pmatrix}.
\]
Write \(M=T_BT_A\) and \(P=(r^2+5r+5)(5r^2+5r+1)\). Elementary matrix multiplication gives the trace and determinant
\[
t(r)=\operatorname{tr}M=\frac{-r^4+r^3+5r^2+r-1}{P},\qquad
q(r)=\det M=\frac{r(r+1)^2}{P}.
\]
Thus the nonconstant two-step multipliers are the two roots of \(z^2-t(r)z+q(r)=0\). Reversing the starting parity produces \(T_AT_B\); these matrices have the same characteristic polynomial. Substitution also gives \(t(1/r)=t(r)\) and \(q(1/r)=q(r)\).

For a real monic quadratic \(w^2-aw+b\), both roots lie strictly in the unit disk if and only if \(1-b>0\), \(1-a+b>0\), and \(1+a+b>0\). Apply this elementary second-order Schur criterion to \(w=5z\). Its three expressions factor exactly as
\[
1-25q(r)=\frac{5r^4+5r^3+r^2+5r+5}{P}>0,
\]
\[
1-5t(r)+25q(r)=\frac{2(5r^4+25r^3+38r^2+25r+5)}{P}>0,
\]
\[
1+5t(r)+25q(r)=\frac{6r(10r^2+21r+10)}{P}>0.
\]
All numerators and \(P\) are strictly positive for \(r>0\). Therefore both characteristic roots satisfy \(|5z|<1\), proving the strict damping bound for every positive finite ratio.

For each fixed \(r\), powers of \(M\) decay geometrically (including repeated-root cases, since its spectral radius is strictly below \(1/5\)); the interposed one-step transfer is a fixed finite matrix. Hence \(\sum_{n\ge3}|d_n|<\infty\) and \(y_n=y_2+\sum_{j=3}^{n}d_j\) converges to a finite constant. Finally,
\[
\lim_{r\to\infty}t(r)=-\frac15,\qquad
\lim_{r\to\infty}q(r)=0.
\]
The two characteristic roots consequently approach \(-1/5\) and \(0\), establishing sharpness. The reciprocal symmetry yields the same limits as \(r\to0^+\).

## Verification
Run `python verify.py` with Python 3 and SymPy as specified in `requirements.txt`. The standalone verifier derives both alternating transfer matrices independently by differentiating a four-node interpolation polynomial and by substituting the published BDF3 difference coefficients; it simplifies the trace, determinant, three factorizations, reciprocal symmetry and limiting expressions. It also checks seven representative positive rational ratios by characteristic roots. Successful output begins with `VERIFY_OK`. The finite rational samples do not replace the all-ratio proof: universal positivity follows from the explicit polynomial identities above.

## Relationship to prior work
Li and Liao (2022), equations (1.1)–(1.5), provide the variable-step BDF3 coefficients; their Theorem 3.1 proves stability under a uniform bound of approximately \(2.553\) on adjacent ratios, and their tests observe stability beyond the sufficient restriction. That result does not imply the present all-positive-ratio alternating-grid statement, because for every sufficiently extreme fixed alternating ratio infinitely many adjacent ratios violate that hypothesis. Söderlind, Fekete and Faragó (2018), Theorem 5.1, give zero-stability on smoothly deformed grids whose local ratios tend to one; the fixed unequal alternating mesh does not satisfy that asymptotic smoothness condition. Earlier general BDF3 matrix-product and Nordsieck analyses established step-ratio restrictions, but their full texts were not all accessible for exhaustive priority exclusion; see `REVIEW.md` for qualification.

## Limitations
The \(1/5\) factor is per *two* steps and concerns eigenvalues, not a common norm-wise contraction bound. The one-step transfers can be large for extreme ratios, so there is no claim of a ratio-independent transient-amplification bound. A periodically alternating mesh is much more structured than an arbitrary grid; the theorem does not remove mesh restrictions for general variable-step BDF3, nor establish absolute stability for nonzero test-equation parameters or nonlinear differential equations. Independent priority verification remains outstanding.

## References
1. Z. Li and H.-l. Liao, *Stability of variable-step BDF2 and BDF3 methods*, arXiv:2201.00527v1, first posted 2022-01-03; SIAM J. Numer. Anal. 60 (2022), 2253–2272. https://arxiv.org/html/2201.00527v1 ; https://doi.org/10.1137/21M1462398 .
2. G. Söderlind, I. Fekete and I. Faragó, *On the zero-stability of multistep methods on smooth nonuniform grids*, BIT Numer. Math. 58 (2018), 1125–1143. https://doi.org/10.1007/s10543-018-0716-y .
3. N. Guglielmi and M. Zennaro, *On the zero-stability of variable stepsize multistep methods: the spectral radius approach*, Numer. Math. 88 (2001), 445–458. https://doi.org/10.1007/s211-001-8010-0 .
4. R. D. Skeel and L. W. Jackson, *The stability of variable-stepsize Nordsieck methods*, SIAM J. Numer. Anal. 20 (1983), 840–853. https://doi.org/10.1137/0720056 .
