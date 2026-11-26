# Ordering the stationary energy-covariance and fourth-cumulant thresholds of a telegraph-driven oscillator

## Finding

Let \(\sigma(t)\in\{-1,1\}\) be a two-sided, stationary, symmetric continuous-time Markov chain with flip rate \(u/2\), where \(u>0\). Consider the stationary solution of
\[
\dot X=V,\qquad \dot V=-V-kX+\sigma,\qquad k>0.
\]
Write \(K_X=\mathbb E[X^4]-3\mathbb E[X^2]^2\), \(K_V=\mathbb E[V^4]-3\mathbb E[V^2]^2\), and \(C_{XV}=\operatorname{Cov}(X^2,V^2)\). The one-dimensional excess fourth cumulants have these expressions because the stationary position and velocity are mean zero.

For each \(u>0\), the covariance \(C_{XV}\) changes sign from negative to positive at its unique zero
\[
\begin{aligned}
B(u)&=26u^2+68u+51,\\
C(u)&=3u^4+24u^3+72u^2+69u+18,\\
k_c(u)&=\frac{B(u)+\sqrt{B(u)^2+36C(u)}}{18}.
\end{aligned}
\]
It satisfies \(k_c(u)>6\), is strictly increasing in \(u\), and
\[
k_c(u)=6+\frac{159}{19}u+O(u^2)\quad(u\downarrow0),
\qquad k_c(u)\sim3u^2\quad(u\to\infty).
\]

The velocity cumulant \(K_V\) changes sign from negative to positive at its unique zero \(k_v(u)\). The position cumulant \(K_X\) is strictly negative for all \(k>0\) when \(0<u\le4/3\); for \(u>4/3\) it changes sign from negative to positive at its unique zero \(k_x(u)\). The strict comparison of these thresholds is
\[
0<k_v(u)<k_c(u)\quad(u>0),\qquad
k_c(u)<k_x(u)\quad(u>4/3).
\]
Thus the velocity fourth cumulant changes sign first, the potential–kinetic covariance second, and the position fourth cumulant last if it has a positive zero. These are stationary sign crossings, not dynamical or thermodynamic phase transitions.

## Assumptions and scope

The sign chain is autonomous: its flip intensity does not depend on \(X\) or \(V\). This does not require \(\sigma(0)\) to be independent of the stationary oscillator state. Indeed the oscillator is driven by the past of the same chain. With
\[
A=\begin{pmatrix}0&1\\-k&-1\end{pmatrix},\qquad e_2=\begin{pmatrix}0\\1\end{pmatrix},
\]
the stationary solution is \((X(t),V(t))^{\mathsf T}=\int_{-\infty}^t e^{A(t-s)}e_2\,\sigma(s)\,ds\). The matrix \(A\) is Hurwitz for \(k>0\), so the convolution is bounded and all polynomial moments are finite. Uniqueness in the stationary joint law follows by writing the linear solution from time \(-T\): the homogeneous term tends to zero in probability by exponential stability and tightness of the stationary state at \(-T\). The conclusions concern this law, not the finite-time trajectory of an independently initialized oscillator.

For the physical model \(m\ddot x+\gamma\dot x+\mu x=a_0\sigma\), take positive \(m,\gamma,\mu,\tau_a\) and \(a_0\ne0\), with flip rate \(1/\tau_a\). The normalization is
\[
s=\frac{\gamma t}{m},\quad X=\frac{\gamma^2x}{a_0m},\quad V=\frac{\gamma v}{a_0},\quad k=\frac{m\mu}{\gamma^2},\quad u=\frac{2m}{\gamma\tau_a}.
\]
Potential and kinetic energies are positive multiples of \(X^2\) and \(V^2\), so their covariance has the sign of \(C_{XV}\). The entire overdamped regime \(0<k\le1/4\) has strictly negative energy covariance; positive energy covariance requires \(k>6\). The force amplitude does not influence the thresholds.

## Proof

Let \(M_{ij}^{(s)}=\mathbb E[X^iV^j\sigma^s]\) for integers \(i,j\ge0\) and \(s\in\{0,1\}\), with negative-index moments set to zero. Stationarity applied to the polynomial generator gives
\[
0=iM_{i-1,j+1}^{(s)}-jM_{ij}^{(s)}-kjM_{i+1,j-1}^{(s)}+jM_{i,j-1}^{(1-s)}-suM_{ij}^{(s)}.
\]
The convolution law is invariant under simultaneous sign reversal of \(X,V,\sigma\), which eliminates the complementary parity. Starting with \(M_{00}^{(0)}=1\), \(M_{00}^{(1)}=0\), the equations give
\[
\mathbb E[X^2]=\frac{u+1}{k(k+u+u^2)},\quad
\mathbb E[V^2]=\frac{u}{k+u+u^2},\quad \mathbb E[XV]=0.
\]
Define the strictly positive common denominator
\[
H=(4k+3)(k+u+u^2)^2(9k+3u+u^2)(k+2+3u+u^2).
\]
Eliminating sign-weighted moments through degree three and ordinary moments through degree four gives
\[
C_{XV}=-\frac{2uP_c(k,u)}{H},\qquad
K_X=-\frac{6P_x(k,u)}{kH},\qquad
K_V=-\frac{6uP_v(k,u)}{H},
\]
where
\[
\begin{aligned}
P_c={}&-9k^2+(26u^2+68u+51)k+3u^4+24u^3+72u^2+69u+18,\\
P_x={}&(12-9u)k^2+(33+119u+112u^2+26u^3)k\\
&+18+69u+102u^2+72u^3+24u^4+3u^5,\\
P_v={}&-9k^3+(-18+16u+26u^2)k^2\\
&+(6u+10u^2+4u^3+3u^4)k+6u^2+9u^3+3u^4.
\end{aligned}
\]

The quadratic \(P_c\) has a negative leading coefficient and positive constant term, so has one positive and one negative root. Its positive root is \(k_c\). Since \(P_c(6,u)=3u(u^3+8u^2+76u+159)>0\), this root exceeds six. Since \(B'(u),C'(u)>0\), the positive root increases strictly in \(u\). At \(u=0\) the positive root extends analytically with value \(6\) and derivative \(477/57=159/19\), by implicit differentiation of \(P_c\). At large \(u\), the leading coefficients of \(B(u)\) and \(C(u)\) are \(26\) and \(3\); the leading coefficient of \(k_c(u)\) is \((26+\sqrt{26^2+108})/18=3\).

The coefficient signs of \(P_v\) in descending powers of \(k\), omitting any zero, have exactly one sign change, so Descartes' rule and the opposite signs at zero and large \(k\) give one positive zero. The polynomial \(P_x\) is strictly positive for \(u\le4/3\); for \(u>4/3\) it likewise has one positive zero, being positive below it and negative above it.

To compare the zeros, divide \(P_v\) and \(P_x\) by \(P_c\) in \(k\). The remainders \(R_v\), \(R_x\) satisfy
\[
\begin{aligned}
-9R_v={}&k(1532u^3+5888u^2+7911u+3681)\\
&+156u^5+1428u^4+5319u^3+8502u^2+5697u+1242,\\
3R_x={}&k(236u^2+476u+303)+12u^4+96u^3+387u^2+429u+126.
\end{aligned}
\]
Both right-hand sides are strictly positive for \(k,u>0\). Therefore \(P_v(k_c,u)<0\) and \(P_x(k_c,u)>0\). By the single crossings, \(k_v<k_c\) always and \(k_c<k_x\) whenever \(k_x\) exists.

## Verification

The accompanying `verify.py` gives a reproducible symbolic reconstruction of the invariant-moment generator equations through degree four, both remainder identities, and the exact threshold limits. Its additional 168 rational diagnostic substitutions and seven representative threshold-order tests are not substitutes for the exact positivity and sign arguments above.

## Relationship to prior work

Dutta, Kundu, Sabhapandit and Basu give this inertial run-and-tumble model, its stationary second moments and a recurrence for arbitrary stationary moments. The stationary moment method is not new. The individual covariance threshold is also available in a published Resultary record [2] with parameters \(g=1/\sqrt{k}\), \(u_{\rm old}=gu/2\); its sign polynomial becomes \(g^4P_c(k,u)\). The individual marginal sign frontiers, including the \(4/3\) boundary, appear with the same \(P_v,P_x\) in a separate record [3]. These individual frontiers are not claimed as distinct contributions here. The comparison proved above is the strict all-parameter interlacing using opposite-sign remainders on the mixed covariance zero curve, rather than three separate root counts.

Méndez, Campos and Horsthemke study harmonic oscillator energies for Gaussian colored driving; in the stationary jointly Gaussian case, zero position–velocity covariance gives independence and zero squared-energy covariance. The force law here is non-Gaussian. Masoliver and Porrà study the oscillator with dichotomous noise, including second-order correlations and spectra. The present ordering is about stationary fourth-order observables.

## Limitations

The result assumes symmetric Poisson sign reversals, linear damping and a harmonic trap. It does not include thermal Gaussian noise, nonlinear potentials, biased switching or multidimensional propulsion. The comparison is of exact stationary sign thresholds, not of time-dependent transitions. Statement-level comparison does not certify historical priority against inaccessible or uninspected texts.

## References

1. D. Dutta, A. Kundu, S. Sabhapandit and U. Basu, *Harmonically trapped inertial run-and-tumble particle in one dimension*, [arXiv:2406.06120v2](https://arxiv.org/html/2406.06120v2), Secs. III and IV.1; *Physical Review E* **110**, 044107 (2024), DOI 10.1103/PhysRevE.110.044107.
2. *Sharp potential–kinetic energy covariance boundary for an inertial telegraph oscillator*, [Resultary 66ee9dbaa5a1](https://github.com/Resultary/2026/tree/main/2026/10/26/SCOPE-sharp-potential-kinetic-energy-covariance-boundary-for-an-inerti--66ee9dbaa5a1).
3. *Exact fourth-cumulant sign frontiers for an inertial run-and-tumble particle*, [Resultary 8126e2ff3632](https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-exact-fourth-cumulant-sign-frontiers-for-an-inertial-run-and-tum--8126e2ff3632).
4. V. Méndez, D. Campos and W. Horsthemke, *Stationary energy probability density of oscillators driven by a random external force*, *Physical Review E* **87**, 062132 (2013), DOI 10.1103/PhysRevE.87.062132.
5. J. Masoliver and J. M. Porrà, *Harmonic oscillators driven by colored noise: Crossovers, resonances, and spectra*, *Physical Review E* **48**, 4309 (1993), DOI 10.1103/PhysRevE.48.4309.
