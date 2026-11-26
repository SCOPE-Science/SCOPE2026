# Sharp switching-rate resonance of positional non-Gaussianity in a two-stiffness harmonic trap

## Finding

Fix \(D>0\) and positive harmonic relaxation coefficients \(a,b>0\). A Brownian particle is confined by a trap whose stiffness switches at a common Poisson rate \(k>0\). Write \(M_j(k)=\mathbb E[X^j]\) for stationary positional moments, and define
\[
Q(k)=\frac{M_4(k)}{3M_2(k)^2}-1.
\]
This normalization is one third of conventional excess kurtosis. The exact forward formula is known: it follows from the stationary mixture in [3] and is equivalent to the normalized squared-position correlator explicitly given in [4, Eq. (5)]:
\[
Q(k)=\frac{(a-b)^2\,[4ab+3(a+b)k+2k^2]}{(a+b+2k)^2\,[4ab+(a+b)k]}.
\]
The rate classification concerns **unequal** stiffnesses. If \(a\ne b\), both \(M_2\) and \(M_4\) decrease strictly with \(k\), yet \(Q\) has a unique interior global maximum if and only if
\[
\boxed{\frac{\max(a,b)}{\min(a,b)}>3+2\sqrt2.}
\]
When the inequality holds, \(Q\) increases before the maximizing rate \(k_*>0\) and decreases after it. The rate is the unique positive root of
\[
4ab[(a+b)^2-8ab]-16ab(a+b)k_*-5(a+b)^2k_*^2-2(a+b)k_*^3=0.
\]
For unequal stiffnesses at or below the threshold, \(Q\) instead decreases strictly at every positive rate. Exactly at the contrast threshold its right derivative at \(k=0\) is zero for the continuous extension of the formula; there is no zero of the derivative at positive \(k\). If \(a=b\), the positional law is Gaussian with variance \(D/a\) for every rate, and \(M_2,M_4,Q\) are all constant, with \(Q=0\).

## Assumptions and scope

Let \(S_t\in\{1,2\}\) be an irreducible stationary continuous-time Markov chain with generator \(\left(\begin{smallmatrix}-k&k\\ k&-k\end{smallmatrix}\right)\). Let \(W_t\) be an independent two-sided standard Brownian motion. The scalar Itô equation is
\[
dX_t=-a_{S_t}X_t\,dt+\sqrt{2D}\,dW_t,\qquad a_1=a,\ a_2=b.
\]
All conclusions concern the unique stationary law and population moments. The harmonic potential is \(V_i(x)=a_i x^2/2\) in units of unit mobility. The chain does not reset position or directly impart impulses.

Two positions driven by the same noise and chain approach one another at a rate bounded by \(e^{-\min(a,b)t}\). A stationary solution is the convergent past integral
\[
X_t=\sqrt{2D}\int_{-\infty}^t \exp\!\left(-\int_s^t a_{S_u}\,du\right)\,dW_s.
\]
For this integral one can condition on the whole chain, making the integrand for each fixed \(t\) deterministic. The exponential bound makes the integral converge in mean square; conditional Gaussian variances are bounded by \(D/\min(a,b)\), so all stationary moments are finite. The solution uses only the past noise and chain at time \(t\) and satisfies the SDE by variation of constants. The chain's invariant marginal is unique, and coupling initial positions conditionally on the same chain state and using the same future chain and noise gives uniqueness of the joint stationary law by contraction.

## Proof

Set \(u_i=\mathbb E[X^2\mathbf1_{\{S=i\}}]\) and \(v_i=\mathbb E[X^4\mathbf1_{\{S=i\}}]\). Each stationary chain state has probability \(1/2\). Applying Itô's formula and the switching generator gives
\[
\begin{pmatrix}2a+k&-k\\-k&2b+k\end{pmatrix}\binom{u_1}{u_2}=\binom D D,
\qquad
\begin{pmatrix}4a+k&-k\\-k&4b+k\end{pmatrix}\binom{v_1}{v_2}=12D\binom{u_1}{u_2}.
\]
The determinants are \(4ab+2(a+b)k\) and \(16ab+4(a+b)k\), respectively. Inversion gives
\[
M_2(k)=\frac{D(a+b+2k)}{2ab+(a+b)k},\qquad
M_4(k)=\frac{6D^2[2a^2+2b^2+3(a+b)k+2k^2]}{[2ab+(a+b)k][4ab+(a+b)k]}.
\]
Substitution into \(M_4/(3M_2^2)-1\) recovers the forward formula. Every denominator is positive.

For \(a\ne b\), direct differentiation gives
\[
\frac{dM_2}{dk}=-\frac{D(a-b)^2}{[2ab+(a+b)k]^2}<0,
\]
\[
\frac{dM_4}{dk}=-\frac{6D^2(a-b)^2\{12ab(a+b)+4(a^2+4ab+b^2)k+3(a+b)k^2\}}{[2ab+(a+b)k]^2[4ab+(a+b)k]^2}<0.
\]
Write \(s=a+b\) and \(p=ab\). The derivative of \(Q\) has the factorization
\[
\frac{dQ}{dk}=\frac{2(a-b)^2P(k)}{(s+2k)^3(4p+sk)^2},\qquad P(k)=4p(s^2-8p)-16psk-5s^2k^2-2sk^3.
\]
For unequal stiffnesses the derivative has the sign of \(P(k)\). Also,
\[
P'(k)=-16ps-10s^2k-6sk^2<0\qquad(k\ge0).
\]
We have \(P(0)=4p(s^2-8p)\) and \(P(k)\to-\infty\). If \(s^2\le8p\), then \(P(k)<0\) throughout \(k>0\). Otherwise \(P\) has exactly one positive root, where \(Q\) changes from strictly increasing to strictly decreasing. As \(s^2>8p\) is equivalent to \(a/b+b/a>6\), the threshold for the larger-to-smaller ratio is \(3+2\sqrt2\).

The rational expression also gives
\[
\lim_{k\downarrow0}Q(k)=\frac{(a-b)^2}{(a+b)^2},\qquad
Q(k)=\frac{(a-b)^2}{2(a+b)k}+O(k^{-2})\quad(k\to\infty).
\]
At \(a=b\) the SDE reduces to an ordinary stationary Ornstein–Uhlenbeck process, giving the constant branch directly.

## Verification

The frozen source package's `check.py` reconstructs the stationary moment systems and checks the rational expressions and their derivative factorizations. With \(a=1,b=9,D=1\), the polynomial is \(1008-1440k-500k^2-20k^3\), with its unique positive root approximately \(0.580341977711327\). The slow-rate limit is \(16/25\), strictly less than \(Q(1/4)=22336/33957\). The symbolic and finite checks corroborate but do not replace the analytic sign argument.

## Relationship to prior work

Kwon, Noh, and Park [1] study work fluctuations under time-dependent harmonic confinement; Alston, Cocconi, and Bertrand [2, §4] analyze stationary second moments and entropy production with two-state switching. The full stationary joint Gaussian mixture of Biroli, Kulkarni, Majumdar, and Schehr [3, Eqs. (10)–(14)] contains this model. With common random conditional variance \(V\), one coordinate has \(M_2=\mathbb E V\) and \(M_4=3\mathbb E V^2\), while two conditionally independent coordinates have \(\mathbb E[X_i^2X_j^2]=\mathbb E V^2\). Thus the normalized mixed fourth moment minus one is exactly \(Q\).

Biroli et al. [4, Eqs. (4)–(5)] explicitly give that normalized correlator, \(C_2\), for the symmetric-rate theory. Identifying their \((k_1,k_2,r)\) with \((a,b,k)\), one has \(R_1+R_2=k(a+b)/(2ab)\) and \(4R_1R_2=k^2/(ab)\); direct substitution into Eq. (5) yields the forward formula above. Their Fig. 2 compares variance and normalized correlations while varying the weaker stiffness at two fixed rates. It is related experimental work, not a test of optimizing the switching rate at fixed stiffnesses. The distinct contribution here is the complete switching-rate derivative classification, including the sharp contrast threshold, unique optimum, and the contrast with monotonicity of the raw moments. Neither the stationary law, its forward moments, nor the forward formula for \(Q\) is claimed new. An equivalent earlier rate classification remains a priority risk.

## Limitations

The theorem requires two strictly positive stiffnesses, symmetric switching rates, and common positive additive Brownian noise in the stated scalar system. Off or inverted states, asymmetry, non-Markov environments, and finite-time estimates are outside its scope. Conventional excess kurtosis is \(3Q\), so it has the same rate monotonicity and maximizer, with a different numerical normalization. At exactly zero switching there are multiple choices of stationary chain law; the stated slow-switching limit is one-sided. Empirical resolution of the rate optimum is not claimed.

## References

[1] C. Kwon, J. D. Noh, H. Park, *Work fluctuations in a time-dependent harmonic potential: rigorous results and beyond the overdamped limit*, arXiv:1303.6742v1. https://arxiv.org/abs/1303.6742

[2] H. Alston, L. Cocconi, T. Bertrand, *Non-equilibrium thermodynamics of diffusion in fluctuating potentials*, arXiv:2202.02630v1. https://arxiv.org/abs/2202.02630

[3] M. Biroli, M. Kulkarni, S. N. Majumdar, G. Schehr, *Dynamically emergent correlations between particles in a switching harmonic trap*, arXiv:2312.02570v1; Phys. Rev. E 109, L032106 (2024). https://arxiv.org/abs/2312.02570

[4] M. Biroli, S. Ciliberto, M. Kulkarni, S. N. Majumdar, A. Petrosyan, G. Schehr, *Experimental Evidence for Strong Emergent Correlations between Particles in a Switching Trap*, arXiv:2508.07199v2; Phys. Rev. Lett. 137, 037102 (2026), DOI:10.1103/jkn8-h939. https://arxiv.org/abs/2508.07199
