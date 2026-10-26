# Exact inverse-power amplification and norming modes of harmonic Bergman monomial Toeplitz operators

## Finding
Let \(L_h^2(\mathbb D,dA)\) be the complex harmonic Bergman Hilbert space on the unit disk, with normalized area \(dA=\pi^{-1}\,dx\,dy\), and let \(P_h\) be the orthogonal projection onto this space. For each integer \(m\ge1\), put \(T_m=P_hM_{z^m}|_{L_h^2}\). Then \(T_m\) is a boundedly invertible contraction, its spectrum equals the unit circle, and for **every** integer \(N\ge1\),
\[
\boxed{\|T_m^{-N}\|^2=\bigl(m\lfloor N/2\rfloor+1\bigr)\bigl(m\lceil N/2\rceil+1\bigr).}
\]
Moreover its entire norm-attaining subspace is the span of the normalized harmonic monomials of Fourier indices \(m\lfloor N/2\rfloor\) and \(m\lceil N/2\rceil\). Hence that subspace has dimension one if \(N\) is even and dimension two if \(N\) is odd. In contrast \(\|T_m^N\|=1\). In particular
\[
\lim_{N\to\infty}\frac{\|T_m^{-N}\|}{N}=\frac m2,
\quad \sigma(T_m)=\mathbb T,\quad \sup_N\|T_m^{-N}\|=\infty.
\]
This provides an exact finite-horizon amplification law, not merely the spectrum or the order of power growth.

## Assumptions and scope
The underlying functions are complex-valued harmonic functions, with their inherited \(L^2(\mathbb D,dA)\) norm. No weighting beyond normalized planar area is imposed; \(m,N\) are arbitrary **positive integers**. For \(k\in\mathbb Z\), write
\[
e_k(z)=\begin{cases}
\sqrt{k+1}\,z^k,&k\ge0,\\
\sqrt{1-k}\,\overline z^{-k},&k<0.
\end{cases}
\]
This is a complete orthonormal basis. The norm-attaining subspace means the collection of all vectors \(f\) for which \(\|T_m^{-N}f\|=\|T_m^{-N}\|\|f\|\), together with zero. There are no claims about Toeplitz symbols other than the specified monomials, nor about weighted harmonic Bergman spaces.

## Proof
**1. Projection and weighted-shift coefficients.** Angular orthogonality and the exact moment identity
\[
\int_{\mathbb D}|z|^{2q}dA=\frac1{q+1}\qquad(q\in\mathbb N_0)
\]
show \(T_me_k=w_ke_{k+m}\), where all coefficients are positive and
\[
w_k^2=\begin{cases}
\dfrac{k+1}{k+m+1},&k\ge0,\\[3pt]
\dfrac{j-m+1}{j+1},&k=-j,\ j\ge m,\\[3pt]
\dfrac{(j+1)(m-j+1)}{(m+1)^2},&k=-j,\ 1\le j\le m.
\end{cases}
\]
The two displayed cases for \(j=m\) agree. To verify the crossing case, multiply the input basis vector \(\sqrt{j+1}\,\overline z^j\) by \(z^m\), project onto the only harmonic basis vector with its Fourier frequency, \(\sqrt{m-j+1}\,z^{m-j}\), and use \(\int |z|^{2m}dA=1/(m+1)\). The same moment calculation gives the other two cases.

Each \(w_k\) lies in \((0,1]\), and \(w_k\to1\) as \(k\to\pm\infty\). Since \(m\) is fixed, \(\inf_{k\in\mathbb Z}w_k>0\). Thus \(T_m\) is invertible. Its forward powers are shifts with coefficient products bounded by one, which converge to one as the starting index tends to positive infinity: \(\|T_m^N\|=1\) for all \(N\ge1\).

**2. Paths staying entirely on one side of the origin.** As the forward shift sends \(e_k\) to \(e_{k+Nm}\), its \(N\)-fold coefficient product for \(k\ge0\) is
\[
\prod_{i=0}^{N-1}w_{k+im}^2=\frac{k+1}{k+Nm+1}.
\]
For \(k\le-Nm\), write \(k=-j\) with \(j\ge Nm\); then the squared coefficient product is \((j-Nm+1)/(j+1)\). The largest reciprocal squared coefficient among these paths is \(Nm+1\), attained at \(k=0\) and \(k=-Nm\). Both are cases of the claimed maximum, corresponding to \(t=0\) and \(t=N\) in Step 4.

**3. Paths crossing the analytic/antianalytic junction.** Every remaining starting index has a unique representation
\[
k=-am-j,\quad 0\le a\le N-1,\quad1\le j\le m,\quad b=N-1-a,
\]
and its terminal index is \(bm+(m-j)\ge0\). (At \(j=m\) the crossing lands at zero.) Telescoping the negative segment, the single crossing step and the positive segment gives the **exact** coefficient product
\[
\prod_{i=0}^{N-1}w_{k+im}=
\frac{(j+1)(m-j+1)}{(m+1)\sqrt{(am+j+1)(bm+m-j+1)}}.
\]
Consequently the reciprocal squared product is
\[
F_{a,b}(j)=
\frac{(m+1)^2(am+j+1)(bm+m-j+1)}{(j+1)^2(m-j+1)^2}.
\]
Treat \(j\) temporarily as a real variable in \([0,m]\). A direct second differentiation yields
\[
\frac{d^2}{dj^2}\log F_{a,b}(j)=
\frac2{(j+1)^2}-\frac1{(am+j+1)^2}
+\frac2{(m-j+1)^2}-\frac1{(bm+m-j+1)^2}
\ge\frac1{(j+1)^2}+\frac1{(m-j+1)^2}>0.
\]
Thus \(\log F_{a,b}\) is **strictly convex** on the entire closed interval; its maximum occurs at an endpoint, and every interior \(j\) gives a strictly smaller value than the greater endpoint. The endpoints simplify to
\[
F_{a,b}(0)=(am+1)((b+1)m+1),\quad
F_{a,b}(m)=((a+1)m+1)(bm+1).
\]
Although \(j=0\) is an auxiliary endpoint rather than a crossing index, its value corresponds exactly to the actual path starting at \(-am\); the \(j=m\) endpoint is an actual path. Therefore the optimization introduces no fictitious norming vector.

**4. Discrete balancing and all equality cases.** Combining Steps 2 and 3, the squared norm of \(T_m^{-N}\) is exactly
\[
\max_{0\le t\le N}\{(mt+1)(m(N-t)+1)\}.
\]
The expression equals \((1+mN/2)^2-m^2(t-N/2)^2\); hence its maximizing integers are precisely \(t=\lfloor N/2\rfloor\) and \(t=\lceil N/2\rceil\). The strict convexity from Step 3 excludes every crossing residue \(1\le j<m\) from equality, and the one-sided formulas from Step 2 are strict away from their boundary indices. Hence the only maximizing **forward starting indices** are \(k=-m\lfloor N/2\rfloor\) and \(k=-m\lceil N/2\rceil\). For the inverse operator, however, the **input** is the terminal index of the corresponding forward path: \(T_m^{-N}e_{k+Nm}\) is a scalar multiple of \(e_k\). Thus the inverse-power **norming basis vectors** are precisely \(e_{m\lfloor N/2\rfloor}\) and \(e_{m\lceil N/2\rceil}\). Since the images of distinct basis vectors under the inverse power are orthogonal, **all** norming vectors are exactly their linear combinations. This proves the formula and the complete equality classification for all \(m,N\).

**5. Spectral and growth consequences.** Let \(U_me_k=e_{k+m}\) denote the unitary bilateral shift of step \(m\). Since \(w_k\to1\) in both tails, \(T_m-U_m\) is compact. The essential spectrum of \(U_m\), a direct sum of \(m\) bilateral unit shifts, is \(\mathbb T\); compact invariance yields \(\mathbb T\subset\sigma(T_m)\). On the other hand \(\|T_m^N\|=1\) and the proved \(\|T_m^{-N}\|=O(N)\), so the spectral-radius formula gives \(r(T_m)=r(T_m^{-1})=1\), confining \(\sigma(T_m)\) to \(\mathbb T\). It follows that \(\sigma(T_m)=\mathbb T\). Taking the large-\(N\) limit of the exact formula proves the stated slope \(m/2\).

## Verification
The standalone Python program `VERIFY.py` independently constructs each squared shift coefficient using exact disk-moment rational arithmetic, multiplies the coefficients along Fourier-index paths, and enumerates the maximizing forward starting indices and the corresponding inverse-domain norming indices. It verifies the claimed formula and exact equality set for all \(1\le m\le20\) and \(1\le N\le13\), checking every starting index in a finite interval covering all paths that can cross zero and enough exterior paths to test telescoping. It also checks algebraic endpoint and strict-convexity inequalities with exact rational arithmetic on a finite parameter grid. The universal statement does **not** follow from this finite experiment: it is established by the general analytic argument in Steps 1–5.

## Relationship to prior work
Huang, Wang and Zhao [1] treat spectral structure of analytic-polynomial Toeplitz operators on the harmonic Bergman space, including essential spectral curves and possible isolated eigenvalues. In their setting \(z^m\) is a natural canonical symbol. The spectrum \(\mathbb T\) here is consistent with their results and is **not** asserted to be a new spectral determination. The issue addressed here is instead the exact operator norm of **every inverse power and its complete norming modes**, information not implied by spectral localization or Weyl's theorem.

Louhichi and Zakariasy [2] develop quasihomogeneous harmonic-Bergman Toeplitz coefficient formulas in their study of products and commutants. In particular, the underlying Fourier-basis projection mechanism is established background, not claimed as new. The contribution lies in the all-horizon sharp extremal product and the discrete balanced-index equality classification. Wang and Zhao [3] establish polynomial-symbol Weyl theorems; their accessible abstract treats spectral topology rather than quantitative inverse powers. Existing norm results for other weighted shifts concern different objects and do not by themselves evaluate these operators.

## Limitations
Only unweighted harmonic Bergman space and analytic monomials are considered. The result gives norms of powers, not an explicit full resolvent norm, pseudospectra, or analogous formulas for arbitrary polynomials or radial weights. A related formula might occur in unindexed weighted-bilateral-shift or older Toeplitz literature; the 2021 article [3] was not available in full text during this comparison. The inverse-power law is proved here as a mathematical identity; no independent publication-priority determination or independent external scientific audit is claimed.

## References
[1] M. Huang, J. Wang, X. Zhao, *The spectral structure of Toeplitz operators with polynomial symbols on the harmonic Bergman space*, arXiv:2610.09638v1, first public 2026-10-07, https://arxiv.org/abs/2610.09638.

[2] I. Louhichi, L. Zakariasy, *Quasihomogeneous Toeplitz operators on the harmonic Bergman space*, arXiv:1107.3951, https://arxiv.org/abs/1107.3951; published in Archiv der Mathematik 98 (2012), 49–60.

[3] C. Wang, X. Zhao, *Weyl's theorem for Toeplitz operators with polynomial symbols on the harmonic Bergman space*, J. Math. Anal. Appl. 495 (2021), 124770, https://doi.org/10.1016/j.jmaa.2020.124770.
