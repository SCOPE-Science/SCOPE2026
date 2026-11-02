# Universal third- and fourth-cumulant geometry for skew tent trajectories

## Finding
For each fixed \(0<a<1\), consider the full-branch skew tent map
\[
T_a(x)=\begin{cases}x/a,&0\le x\le a,\\(1-x)/(1-a),&a<x\le1,\end{cases}
\]
and its stationary trajectory \(X_j=T_a^j(X_0)\), where \(X_0\) is Lebesgue-uniform on \([0,1]\). Set \(g(x)=x-1/2\), \(S_N=\sum_{j=0}^{N-1}g(X_j)\), and let \(\operatorname{cum}_r\) denote the ordinary order-\(r\) cumulant. For \(r=2,3,4\), the limits \(K_r(a)=\lim_{N\to\infty}\operatorname{cum}_r(S_N)/N\) exist and satisfy
\[
\boxed{K_2(a)=\frac{a}{12(1-a)},\qquad K_3(a)=-\frac{a}{24(1-a)^2},\qquad K_4(a)=\frac{a\,[19+6a(1-a)]}{720(1-a)^3}.}
\]
Writing the asymptotic standardized coefficients as \(G(a)=K_3(a)/K_2(a)^{3/2}\) and \(H(a)=K_4(a)/K_2(a)^2\), one obtains the **exact parameter-independent shape relation**
\[
\boxed{G(a)=-\sqrt{\frac3{a(1-a)}},\qquad H(a)=\frac65+\frac{19}{15}G(a)^2.}
\]
In particular \(G(a)\le-2\sqrt3\), \(H(a)\ge82/5\), with equality in either inequality precisely at \(a=1/2\). Thus the Birkhoff sums have a negative order-\(N^{-1/2}\) standardized skewness and a positive order-\(N^{-1}\) excess kurtosis for every fixed parameter, although the one-time uniform marginal has third cumulant zero and fourth cumulant \(-1/120\).

The stationary position covariance is \(\operatorname{Cov}(X_0,X_n)=(2a-1)^n/12\) for every integer \(n\ge0\). At \(a=1/2\) all positive-lag covariances vanish, but \(K_3(1/2)=-1/12\) and \(K_4(1/2)=41/360\). These symmetric-map coefficients were calculated in earlier work; the parameter-wide cumulant identities and their shape relation are the stated extension.

## Assumptions and scope
The parameter \(a\) is fixed with \(0<a<1\), independently of \(N\). Endpoints of the branch partition can be assigned either branch without affecting the invariant measure or stated results. Since each branch maps onto \([0,1]\) and inverse slopes have magnitudes \(a\) and \(b=1-a\), the invariant probability law is Lebesgue measure and the piecewise expanding map is exact and mixing. Cumulants are those of the stationary sum \(S_N\), not the cumulants of a single \(X_j\), and \(K_r\) denotes the growth coefficient, not the unnormalized limiting cumulant.

## Proof
Put \(b=1-a\) and \(P h(x)=a h(ax)+b h(1-bx)\), the Perron--Frobenius operator. It preserves Lebesgue integration: \(\int_0^1Ph=\int_0^1h\). Since \(P1=1\) and each branch is onto and expanding, the leading eigenvalue \(1\) is simple and isolated on bounded variation, with the remainder of the spectrum strictly inside the unit circle. For \(t\) near zero, the analytic twist \(P_t h=P(e^{tg}h)\) therefore has a simple analytic eigenvalue \(\rho(t)\) and eigenfunction \(h_t\), normalized by \(\int h_t=1\). The spectral decomposition and \(\int P_t^N1=\mathbb E[e^{tS_N}]\) show, locally uniformly in complex \(t\),
\[
\log\mathbb E[e^{tS_N}]=N\log\rho(t)+O_a(1),\qquad \operatorname{cum}_r(S_N)=N(\log\rho)^{(r)}(0)+O_a(1)
\]
for every fixed derivative order \(r\le4\). Uniform analyticity makes the derivative of the bounded remainder bounded; finite orbit checks alone are not used for this step.

Define \(h_j=\left.\frac{d^j}{dt^j}h_t\right|_{t=0}\) and \(q_j=\left.\frac{d^j}{dt^j}\rho(t)\right|_{t=0}\). As \(\int g=0\), \(q_1=0\); by normalization, \(\int h_j=0\) for every \(j\ge1\). Differentiating \(P(e^{tg}h_t)=\rho(t)h_t\) gives
\[
\begin{aligned}
(I-P)h_1&=Pg,\\
q_2&=\int_0^1(g^2+2gh_1),\\
(I-P)h_2&=P(g^2+2gh_1)-q_2,\\
q_3&=\int_0^1(g^3+3g^2h_1+3gh_2),\\
(I-P)h_3&=P(g^3+3g^2h_1+3gh_2)-3q_2h_1-q_3,\\
q_4&=\int_0^1(g^4+4g^3h_1+6g^2h_2+4gh_3).
\end{aligned}
\]
All displayed integrals lacking limits are over \([0,1]\). Crucially, \(P\) maps polynomials of degree at most \(j\) to polynomials of degree at most \(j\). On the mean-zero polynomial space of each degree, \(I-P\) is invertible: its triangular diagonal is \(1-[a^{j+1}+(-1)^jb^{j+1}]\), which is nonzero for \(j\ge1\) and \(0<a,b<1\). Hence these differential equations are solved exactly within degrees one, two and three; the solution is unique under zero-mean normalization.

An explicit zero-mean solution, whose substitution gives a finite algebraic proof, is
\[
\begin{aligned}
h_1&=\frac{2a-1}{2b}(x-\tfrac12),\\
h_2&=\frac{3a^2-3a+1}{3b^2}(x^2-\tfrac13)+\frac{-6a^2+5a-2}{6b^2}(x-\tfrac12),\\
h_3&=u(x^3-\tfrac14)+v(x^2-\tfrac13)+w(x-\tfrac12),\\
u&=\frac{4a^3-6a^2+4a-1}{4b^3},\\
v&=\frac{-18a^3+21a^2-15a+4}{12b^3},\\
w&=\frac{24a^3-12a^2+18a-5}{48b^3}.
\end{aligned}
\]
Termwise polynomial integration yields
\[
q_2=\frac{a}{12b},\qquad q_3=-\frac{a}{24b^2},\qquad q_4-3q_2^2=\frac{a(19+6ab)}{720b^3}.
\]
Because \(q_1=0\), the second and third derivatives of \(\log\rho\) equal \(q_2,q_3\), while its fourth derivative equals \(q_4-3q_2^2\). This proves the three cumulant-rate formulas.

The standardized identities follow by division, using \(ab\le1/4\), with equality only at \(a=1/2\). The finite-\(N\) standardized skewness and excess kurtosis consequently satisfy
\[
\operatorname{skew}(S_N)=\frac{G(a)}{\sqrt N}+O_a(N^{-3/2}),\qquad
\operatorname{excess}(S_N)=\frac{H(a)}{N}+O_a(N^{-2}).
\]
Finally \(Pg=(2a-1)g\), so stationarity gives \(\operatorname{Cov}(X_0,X_n)=\int gP^ng=(2a-1)^n/12\). The case \(a=1/2\) displays zero pair correlations despite nonzero higher cumulant rates, completing the proof.

## Verification
The standalone `verification.py` uses two independent forms of evidence. Its first block carries out exact rational finite-\(N\) twisted-transfer recursions for \(a=1/4,1/2,3/4\), including all derivatives through order four and \(N\le64\); it checks the one-step uniform cumulants and numerically displays convergence to the stated rates. Its second block uses symbolic polynomials to verify identically in \(a\) the three eigenfunction recursions, zero-mean normalizations, integral identities, and the standardized shape law. These checks were executed from the embedded file. The spectral-gap argument, rather than finite computations, establishes the infinite-time limits.

## Relationship to prior work
Smith [1] computed the scaled cumulant generating function for the **symmetric** tent map \(a=1/2\), including the coefficient \(-1/72\) of the cubic term and \(41/8640\) of the quartic term in the centered generating function (equivalently \(K_3=-1/12\), \(K_4=41/360\)); Smith's Appendix E develops the polynomial-twisted-operator method. These contributions are not new here. The present formulas treat every skew parameter \(0<a<1\), establish strict sign behavior and the exact standardized skewness--kurtosis line, and link the symmetric-map vanishing pair correlations to nonzero higher temporal cumulants. Lindström and Thunberg [2] provide general skew-tent dynamics and bifurcation context, but their retrieved abstract concerns attractors and bifurcations, not the stated cumulant law. General cumulant methods and expanding-map spectral perturbation are standard and not claimed as inventions.

## Limitations
The result is for one fixed full-height two-branch skew tent map with the affine coordinate observable and Lebesgue initial law; it does not give higher-order cumulants, an all-parameter large-deviation rate function, or parameter-uniform error estimates near \(a=0\) or \(a=1\). The formulas are intrinsic to the chosen coordinate observable, not topological-conjugacy invariants. Prior-work checks do not establish comprehensive publication priority; the exact parameterized formulas might be recoverable from a different general perturbative treatment not located in the inspected sources. No independent mathematical audit has been performed.

## References
[1] Naftali R. Smith, *Large deviations in chaotic systems: exact results and dynamical phase transition*, arXiv:2204.04652v1 (first posted 2022-04-10); *Physical Review E* **106**, L042202 (2022), doi:10.1103/PhysRevE.106.L042202. Main tent-map section and Appendix E, especially the cubic and quartic cumulant generating terms.

[2] Torsten Lindström and Hans Thunberg, *An elementary approach to dynamics and bifurcations of skew tent maps*, *Journal of Difference Equations and Applications* **14** (2008), 819--833, doi:10.1080/10236190801927462. Only the accessible abstract was inspected for this comparison.
