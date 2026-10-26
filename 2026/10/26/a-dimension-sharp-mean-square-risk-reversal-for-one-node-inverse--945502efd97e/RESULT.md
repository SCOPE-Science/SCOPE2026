# A dimension-sharp mean-square risk reversal for one-node inverse spectral quadrature

## Finding

For every integer \(n\ge2\), every unit vector \(u\in\mathbb R^n\), and every \(0<\eta<1\), let
\[
 A_\eta=I-(1-\eta)uu^{\mathsf T},\qquad
 T_\eta=\frac1n\operatorname{tr}(A_\eta^{-1})=1+\frac{1-\eta}{n\eta}.
\]
Draw a single real uniformly random unit vector \(v\). Consider the one-node Gaussian/Lanczos quadrature estimate and a degree-one spectral-endpoint interpolatory estimate of the same normalized inverse trace:
\[
 G_\eta=\frac1{v^{\mathsf T}A_\eta v},\qquad
 I_\eta=1+\frac{1-v^{\mathsf T}A_\eta v}{\eta}.
\]
Both use the same one matrix-vector product with \(A_\eta\); \(I_\eta\) additionally uses the exact spectral endpoints \(\eta,1\). Define \(R_G=\mathbb E(G_\eta-T_\eta)^2\) and \(R_I=\mathbb E(I_\eta-T_\eta)^2\). The full strict risk ordering is:

* \(n=2\): \(R_G>R_I\) at every \(0<\eta<1\).
* \(n=3\): there is exactly one \(\eta_c\in(0,1)\), numerically \(\eta_c=0.0503804097941478994\ldots\). One has \(R_G>R_I\) for \(0<\eta<\eta_c\), equality at \(\eta_c\), and \(R_G<R_I\) for \(\eta_c<\eta<1\).
* Every \(n\ge4\): \(R_G<R_I\) at every \(0<\eta<1\).

In every dimension the ill-conditioning limit is sharp:
\[
 \lim_{\eta\downarrow0}\frac{R_G}{R_I}=\frac{n+2}{2(n-1)}.
\]
Thus the biased one-node Gaussian estimate uniformly wins in mean-square risk from dimension four onward, even against an unbiased interpolant that is exact at both eigenvalues. This is a statement about a one-probe finite-budget risk, **not** superiority for arbitrary spectra or computational tasks.

## Assumptions and scope

All random vectors are uniform on the **real** unit sphere, not complex Haar, Gaussian without normalization, or Rademacher. The matrix is real symmetric positive definite with precisely two eigenvalues, the smaller one of multiplicity one. The baseline \(I_\eta\) uses *known* spectral endpoints, not an approximation to them. Risk is squared error of one normalized-trace estimator, with no averaging across probes. No computation or regularity assumptions beyond \(n\ge2\) and \(0<\eta<1\) are made. The orientation of \(u\) is arbitrary by rotation invariance.

## Proof

Put \(\delta=1-\eta\), \(W=(u^{\mathsf T}v)^2\), and \(\mu=1/n\). Real spherical invariance gives \(W\sim\mathrm{Beta}(1/2,(n-1)/2)\), with moments
\[
 m_j=\mathbb E[W^j]=\frac{(1/2)_j}{(n/2)_j},\quad m_1=\mu,\quad
 m_2=\frac3{n(n+2)},\quad
 \operatorname{Var}(W)=\frac{2(n-1)}{n^2(n+2)}.
\]
Since \(v^{\mathsf T}A_\eta v=1-\delta W\), one-node Lanczos gives \(G_\eta=(1-\delta W)^{-1}\). The line through \((\eta,\eta^{-1})\) and \((1,1)\) is \(p(x)=1+(1-x)/\eta\), giving \(I_\eta=1+(\delta/\eta)W\). Consequently \(\mathbb E I_\eta=T_\eta\) and
\[
 R_I=\frac{\delta^2}{\eta^2}\frac{2(n-1)}{n^2(n+2)}.
\]

For \(|\delta|<1\), both geometric series converge absolutely and uniformly on \(0\le W\le1\). Therefore
\[
 G_\eta-T_\eta=\sum_{k\ge1}\delta^k(W^k-\mu),\quad
 I_\eta-T_\eta=\sum_{k\ge1}\delta^k(W-\mu).
\]
Subtracting squared expectations yields the convergent series \(R_G-R_I=\sum_{j\ge3}d_j\delta^j\), where \(d_2=0\) and, for every integer \(j\ge2\),
\[
 d_j=(j-1)(m_j-m_2+2\mu^2)-2\mu\sum_{k=1}^{j-1}m_k,
\]
\[
 d_{j+1}-d_j=
 m_j\left(\frac{n-2}{n}-\frac{j(n-1)}{2j+n}\right)
 +\frac{4-n}{n^2(n+2)}.
\]
The bracket is strictly negative for all \(n\ge2,j\ge2\): after multiplication by the positive denominator its numerator is \(n(n-2)-j(n^2-3n+4)\), which is at most \(-[(n-2)^2+4]\) for \(j\ge2\). Thus when \(n\ge4\), every increment is negative; from \(d_2=0\), all \(d_j<0\) for \(j\ge3\). This proves \(R_G<R_I\) throughout the entire claimed parameter range, without asymptotic or sampling arguments.

For \(n=2\), elementary beta integration gives
\[
 R_G=\frac{(1+\eta)(1-\sqrt\eta)^2}{4\eta^2},\quad
 R_I=\frac{(1-\eta)^2}{8\eta^2},\quad
 \frac{R_G}{R_I}=\frac{2(1+\eta)}{(1+\sqrt\eta)^2}>1,
\]
since the positive difference of the numerator and denominator on the right is \((1-\sqrt\eta)^2\).

For \(n=3\), one has \(m_j=(2j+1)^{-1}\) and
\[
 d_{j+1}-d_j=\frac1{45}-\frac{4j-3}{3(2j+1)(2j+3)}.
\]
The subtracted term is equal for \(j=2,3\), then strictly decreases for every integer \(j\ge3\) (cross-multiplication reduces this to \(j>2\)). Hence these increments are first negative, then positive, with exactly one switch, because they tend to \(1/45\). As \(d_3=-8/315<0\), while \(d_j\to+\infty\), the sequence of coefficients \(d_j\) has exactly one sign switch from negative to positive. If \(J\) is its last nonpositive index, the function \(\delta^{-J}\sum_{j\ge3}d_j\delta^j\) is strictly increasing for \(0<\delta<1\): terms of nonpositive coefficients and nonpositive exponent decrease in magnitude with \(\delta\), while positive-coefficient terms have positive exponent and increase. Thus \(R_G-R_I\) can cross zero at most once on \((0,1)\). It is negative near \(\delta=0\).

To see the opposite sign near \(\delta=1\), note that \(0\le\eta G_\eta\le1\) and \(\eta G_\eta\to0\) almost surely as \(\eta\downarrow0\), because \(W<1\) almost surely. Bounded convergence gives \(\eta^2R_G\to1/n^2\). Meanwhile \(\eta^2R_I\to2(n-1)/[n^2(n+2)]\). For \(n=3\), the former exceeds the latter, proving existence and uniqueness of the crossing. This also proves the stated ratio for every dimension.

For numerical identification of the unique \(n=3\) crossing, set
\[
 L(\eta)=\frac{\operatorname{artanh}\sqrt{1-\eta}}{\sqrt{1-\eta}},\quad
 B(\eta)=\frac{1+2\eta}{3\eta}.
\]
The exact defining equation is
\[
 \frac1{2\eta}+\frac{L(\eta)}2-2B(\eta)L(\eta)+B(\eta)^2
 =\frac{4(1-\eta)^2}{45\eta^2}.
\]
This follows by integrating \((1-\delta z^2)^{-1}\) and its square over \(0<z<1\), because \(W\stackrel{d}{=}Z^2\) for uniform \(Z\in(0,1)\). Uniqueness is already established independently of numerical root finding.

## Verification

The accompanying standalone `verify.py` checks the beta-moment recurrence and coefficient-increment identity using exact rational arithmetic; coefficient signs across finite parameter grids; thousands of exact rational one-matvec identities for the estimators; and numerical consistency of the unique \(n=3\) crossing. It executed successfully with 18,835 deterministic assertions. These finite tests supplement, rather than replace, the infinite-dimensional-parameter sign proof above.

## Relationship to prior work

Chen, Trogdon and Ubaru (arXiv:2204.01941, first public April 5, 2022), Sections 1–3, define stochastic spectral measures, one-point Gaussian/Lanczos quadrature, degree-limited polynomial quadrature, and general high-probability spectral approximation bounds. Their sections on numerical comparisons concern empirical KPM/SLQ differences, not the precise one-probe inverse-trace risk comparison proved here. Ubaru, Chen and Saad (2017) introduce SLQ for matrix-function traces and establish general approximation bounds, including inverse traces; those general bounds likewise do not state the dimension-sharp risk ordering for the pair of estimators above. The ordinary beta moment formula, Gauss quadrature definition, and pointwise interpolation identity are background; the new assessment concerns their complete non-asymptotic risk comparison and the unique exceptional-dimensional crossing.

## Limitations

The two eigenvalues and their multiplicities are specified mathematically; thus the normalized trace could be calculated analytically if this complete model information were known to an implementer. The endpoint interpolant assumes \(\eta\) is available, whereas the Gaussian estimator does not. The theorem is a controlled matrix-free risk benchmark isolating the difference between nonlinear one-node Gaussian evaluation and a degree-one endpoint polynomial, not a claim of practical supremacy for trace estimation when spectral information is unknown. It says nothing about multiple independent probes, non-real sampling, other matrix spectra, other matrix functions, or computational work required to obtain endpoints. Publication-priority searches cannot prove absolute uniqueness, and the result has no independent external scientific audit.

## References

1. T. Chen, T. Trogdon, S. Ubaru, *Randomized matrix-free quadrature: unified and uniform bounds for stochastic Lanczos quadrature and the kernel polynomial method*, arXiv:2204.01941 (first submitted 2022-04-05), https://arxiv.org/abs/2204.01941.
2. S. Ubaru, J. Chen, Y. Saad, *Fast Estimation of tr(f(A)) via Stochastic Lanczos Quadrature*, SIAM J. Matrix Anal. Appl. 38 (2017), 1075–1099, https://doi.org/10.1137/16M1104974.
3. G. H. Golub, G. Meurant, *Matrices, Moments and Quadrature with Applications*, Princeton University Press (2009), background on Gaussian quadrature.
