# Sharp quadratic onset of the tent-spline Gabor lower frame bound

## Finding
For every integer \(q\ge2\), define \(c_q=2+1/(2q)\), \(b_\delta=c_q+\delta\), and \(a_\delta=1/(qb_\delta)\). Let \(A_q(\delta)\) be the optimal lower Gabor frame bound for the second-order cardinal B-spline \(Q_2(t)=(1-|t|)_+\) on the rectangular lattice \(a_\delta\mathbb Z\times b_\delta\mathbb Z\). Then
\[
\boxed{\lim_{\delta\downarrow0}\frac{A_q(\delta)}{\delta^2}=\frac{2}{(2+1/(2q))^3}.}
\]
For all sufficiently small \(\delta>0\), the upper estimate \(0<A_q(\delta)\le 2\delta^2/b_\delta^3\) holds. This is a sharp asymptotic coefficient, not merely a positive upper or lower order estimate. For \(q=2\), the coefficient is \(128/729\). The frame threshold at \(\delta=0\) and non-frame behavior on the nearby negative side are already known; the new claim concerns the optimal bound's quantitative onset on the frame side.

## Assumptions and scope
The window is the unit-height tent \(Q_2(t)=\max\{1-|t|,0\}\). The Gabor atoms are \(e^{2\pi i m b t}Q_2(t-na)\), with \(m,n\in\mathbb Z\); there is no additional window normalization. The quantity \(A_q(\delta)\) is the largest real constant such that
\[
 A_q(\delta)\|f\|_2^2\le\sum_{m,n\in\mathbb Z}|\langle f,e^{2\pi i m b_\delta\cdot}Q_2(\cdot-na_\delta)\rangle|^2
\]
for every \(f\in L^2(\mathbb R)\). Throughout the proof \(q\) is fixed, \(\delta\downarrow0\) through positive real numbers, and \(\delta<\tfrac12-\tfrac1{2q}\) so that \(2<b_\delta<5/2\). This result asserts no estimate uniform in simultaneously unbounded \(q\) and varying \(\delta\).

Define the unitary Zak transform at scale \(1/b\) by
\[
 Z_b(x,\gamma)=b^{-1/2}\sum_{k\in\mathbb Z}Q_2((x-k)/b)e^{2\pi i k\gamma}.
\]
It satisfies \(|Z_b(x+1,\gamma)|=|Z_b(x,\gamma)|\). The integer-oversampling Zibulski--Zeevi representation, with numerator parameter \(p=1\), gives the exact optimal bound
\[
 A_q(\delta)=\min_{(x,\gamma)\in(\mathbb R/\mathbb Z)^2} M_{b_\delta}(x,\gamma),\quad
 M_b(x,\gamma)=\sum_{j=0}^{q-1}|Z_b(x+j/q,\gamma)|^2.
\]
The sign of the sample shift is immaterial because it permutes the cyclic grid. This identity fixes the normalization of the claimed coefficient.

## Proof
**Exact alternating identity.** Write \(b=2+\varepsilon\) with \(0<\varepsilon<1/2\). For \(0\le y<1\), direct evaluation of the finitely supported sum gives
\[
 b^{3/2}Z_b(y,1/2)=(\varepsilon-y)_+-(y-1+\varepsilon)_+.
 \tag{1}
\]
Indeed, the four contributions with indices \(k=-1,0,1,2\), at alternating phase, cancel identically. Only the extra \(k=-2\) contribution occurs for \(y<\varepsilon\), while the extra \(k=3\) contribution occurs for \(y>1-\varepsilon\), with signs \(+\) and \(-\), respectively. This also proves that the zeros at phase \(1/2\) are exactly the closed interval \([\varepsilon,1-\varepsilon]\).

**Critical simultaneous zeros.** Set \(\varepsilon_0=1/(2q)\), \(c=2+\varepsilon_0\), and \(b=c\). The exact Zak-zero classification for the tent spline (Stangl--Frederick, Theorem 2) states that, for \(b\in(2,5/2)\), the only nonisolated zero family is at phase \(\gamma=1/2\), on \([\varepsilon,1-\varepsilon]\); any other phase has at most one zero in \([0,1)\). Thus \(q\ge2\) distinct equally spaced samples can all vanish only at \(\gamma=1/2\). An interval of length \(1-1/q\) contains all \(q\) equally spaced circle samples precisely when its endpoints coincide with their two extremes. Therefore, modulo the grid's cyclic permutations, every zero of \(M_c\) is
\[
 (\gamma,y_j)=(1/2,\varepsilon_0+j/q),\qquad j=0,\ldots,q-1.
 \tag{2}
\]
The cited zero theorem supplies the global exclusion of additional phase roots; at phase \(1/2\), (1) directly supplies the exact real zero interval. The zero set of the continuous nonnegative function \(M_c\) on its compact torus is consequently a finite set of cyclic shifts of (2).

**Exact upper trial.** For \(b=c+\delta\) and \(0<\delta<\varepsilon_0\), take phase \(1/2\) and circle samples \(y_j=\varepsilon_0+j/q\). By (1), the first and last Zak values are \(\delta/b^{3/2}\) and \(-\delta/b^{3/2}\), respectively, and all others vanish. Hence
\[
 0<A_q(\delta)\le M_{c+\delta}(\varepsilon_0,1/2)=\frac{2\delta^2}{(c+\delta)^3}.
 \tag{3}
\]
Positivity for \(\delta>0\) follows from the published complete integer-oversampling frame-set theorem (Stangl--Frederick, Theorem 3).

**First transverse derivative.** For each \(y\in[\varepsilon_0,1-\varepsilon_0]\), only \(k=-1,0,1,2\) can contribute nonzero terms at \(b=c\). Differentiating the *finite* Zak sum yields
\[
 \partial_\gamma Z_c(y,1/2)=\frac{2\pi i}{c^{3/2}}\sum_{k=-1}^{2}k(-1)^k(c-|y-k|)
 =\frac{4\pi i\varepsilon_0}{c^{3/2}}.
 \tag{4}
\]
The derivative is purely imaginary, is independent of \(y\) over the full critical zero interval, and is nonzero for every fixed \(q\ge2\). The Zak sum has uniformly bounded second phase derivative near this compact configuration; its coefficients depend continuously and piecewise affinely on \((b,y)\).

**Localization and sharp lower bound.** For every \(\delta>0\), compactness yields a minimizing torus point \((x_\delta,\gamma_\delta)\). By (3), \(M_{c+\delta}(x_\delta,\gamma_\delta)=O(\delta^2)\). Uniform convergence \(M_{c+\delta}\to M_c\) and the critical zero classification imply that, after passing to a subsequence and cyclically reindexing the samples, the minimizer approaches (2). Thus its sample positions can be written
\[
 y_j=\varepsilon_0+j/q+h_\delta,\qquad \gamma_\delta=1/2+\tau_\delta,
\]
where \(h_\delta,\tau_\delta\to0\); all represented \(y_j\) lie in \((0,1)\) for sufficiently small \(\delta\).

At phase \(1/2\) the Zak sum is real. For nearby parameters its imaginary part, by the nonzero derivative (4) and uniform Taylor estimates, obeys a fixed lower bound proportional to \(|\tau_\delta|\) in the sample neighborhood. Since each squared modulus is at most \(O(\delta^2)\), it follows that \(\tau_\delta=O(\delta)\). Its real part differs from its value at phase \(1/2\) by \(O(\tau_\delta^2)=O(\delta^2)\). Applying (1) to the first and last samples now gives
\[
 (\delta-h_\delta)_+=O(\delta),\qquad(\delta+h_\delta)_+=O(\delta),
\]
which together force \(h_\delta=O(\delta)\).

With \(h,\tau=O(\delta)\), the exact alternating identity (1), the uniform derivative (4), and bounded second phase derivatives give, uniformly in each sample index,
\[
 Z_{c+\delta}(y_j,1/2+\tau)=c^{-3/2}\big[
 \mathbf1_{j=0}(\delta-h)_+-\mathbf1_{j=q-1}(\delta+h)_+
 +4\pi i\varepsilon_0\tau\big]+o(\delta).
\]
The real and imaginary leading terms have no mixed quadratic cross term. Squaring and summing yields
\[
 M_{c+\delta}=c^{-3}\left[(\delta-h)_+^2+(\delta+h)_+^2+
 \frac{4\pi^2}{q}\tau^2\right]+o(\delta^2).
 \tag{5}
\]
For all real \(h\), \((\delta-h)_+^2+(\delta+h)_+^2\ge2\delta^2\), with equality at \(h=0\). Equation (5) therefore yields \(\liminf_{\delta\downarrow0}A_q(\delta)/\delta^2\ge2/c^3\), along *every* minimizing subsequence. The exact upper trial (3) gives the matching limsup and proves the theorem.

## Verification
The standalone program `verify_zak_endpoint.py` reproduces the alternating identity with rational arithmetic, the real derivative identity on critical grids, the exact two-edge trial energy, and supplementary local complex-Zak mesh comparisons. It passes 2,622 rational identities and 1,740 supplementary numerical checks. The local mesh is not used to infer global minimality: compactness, the Zak-zero theorem, uniform phase derivatives, and the hinge inequality furnish the infinite proof. The finite calculation is supplementary evidence and can be rerun with `python3 verify_zak_endpoint.py`.

## Relationship to prior work
Stangl and Frederick, arXiv:2609.00481v1 (public August 31, 2026), establish the zero-set classification and the qualitative frame/non-frame dichotomy for integer oversampling; their subsequent version supplies the explicit normalization in Theorem 4. Lemvig and Nielsen established the original non-frame obstruction at the threshold. Neither the qualitative classification nor the obstruction theorem supplies the present optimal *frame-bound asymptotic coefficient*, which depends on the transverse phase derivative and a two-sided hinge minimization. A September 2026 paper by Hasannasab and Lemvig (arXiv:2609.13116) also concerns hat-spline Zak zeros and integer-oversampling frame properties; its abstract does not specify the present quantitative asymptotic, but its full text could not be inspected and is an explicit novelty risk.

## Limitations
The limit is pointwise for each fixed integer \(q\ge2\), not uniform in \(q\). The exact optimal bound for a fixed positive \(\delta\) is not determined. No assertion is made for rational lattice products other than \(1/q\), or near different half-integer/integer boundaries. Published frame-membership theorems and the non-frame behavior are not new results. The fully inaccessible later same-object paper leaves a genuine residual literature-overlap risk; independent scientific review has not been performed.

## References
1. A. Stangl and C. Frederick, *The frameset of the second-order B-spline along \(ab=1/q\)*, arXiv:2609.00481v1, submitted August 31, 2026; relevant full-text comparison uses v2 of September 2, 2026, https://arxiv.org/html/2609.00481v2 .
2. J. Lemvig and K. H. Nielsen, *Counterexamples to the B-spline conjecture for Gabor frames*, Journal of Fourier Analysis and Applications 22 (2016), 1440–1451.
3. M. Hasannasab and J. Lemvig, *The zero set of the Zak transform of B-splines with applications to Gabor frames*, arXiv:2609.13116 (September 11, 2026), https://arxiv.org/abs/2609.13116 .
4. M. Zibulski and Y. Y. Zeevi, *Analysis of multiwindow Gabor-type schemes by frame methods*, Applied and Computational Harmonic Analysis 4 (1997), 188–221.
