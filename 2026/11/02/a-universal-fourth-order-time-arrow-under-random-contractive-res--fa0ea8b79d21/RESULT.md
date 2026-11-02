# A universal fourth-order time arrow under random contractive resetting

## Finding
For a stationary one-dimensional Brownian particle, suppose independent Poisson events of rate \(r>0\) multiply the current position by an independent random \(Q\) with \(|Q|\le c<1\), allowing either sign. Between events the particle diffuses with variance rate \(2D\), where \(D>0\). Let \(m_j=\mathbb E[Q^j]\), \(\lambda_j=r(1-m_j)\), and \(M_2=2D/\lambda_2\). The chronological fourth-moment difference is
\[
\Delta(t)=\mathbb E[X_0X_t^3]-\mathbb E[X_0^3X_t]
=\frac{6DM_2\,\mathbb E[(1-Q)^3(1+Q)]}{1-m_4}\,H(t), \qquad t\ge0,
\]
where
\[
H(t)=\begin{cases}
\dfrac{e^{-\lambda_1t}-e^{-\lambda_3t}}{\lambda_3-\lambda_1},&\lambda_1\ne\lambda_3,\\[3pt]
t e^{-\lambda_1t},&\lambda_1=\lambda_3.
\end{cases}
\]
In particular, \(\Delta(t)>0\) for every \(t>0\), for **every** admissible distribution of signed contraction factors. There is exactly one positive-lag maximum, at
\[
t_* =\begin{cases}
\dfrac{\log(\lambda_3/\lambda_1)}{\lambda_3-\lambda_1},&\lambda_1\ne\lambda_3,\\[3pt]
\lambda_1^{-1},&\lambda_1=\lambda_3.
\end{cases}
\]
The chronological difference is unchanged if the observed signal is augmented by any independent, centered, stationary time-reversible process with finite fourth moments.

## Assumptions and scope
Let \(B\) be standard Brownian motion, \(N\) an independent homogeneous Poisson process of rate \(r>0\), and \((Q_k)\) independent identically distributed multipliers, independent of both, supported in \([-c,c]\) for some \(0\le c<1\). The process evolves by \(dX_t=\sqrt{2D}\,dB_t\) away from the Poisson times and obeys \(X_{T_k}=Q_kX_{T_k-}\) at each event. All expectations use its unique stationary law. An additional observation process \(V\) is independent of \(X\), centered, stationary, time reversible, and has finite fourth moments. No assumptions of Gaussianity, whiteness, or independence over time are imposed on \(V\).

## Proof
The Poisson-sampled dynamics are random contractive affine recurrences with Gaussian innovations; uniform strict contraction gives a unique stationary solution with moments through order four (indeed, all finite integer moments). Symmetry of innovations gives \(\mathbb E X=\mathbb E X^3=0\). Its polynomial generator is
\[
Lf(x)=Df''(x)+r\left(\mathbb E f(Qx)-f(x)\right).
\]
In particular, \(Lx=-\lambda_1x\), \(Lx^2=2D-\lambda_2x^2\), \(Lx^3=6Dx-\lambda_3x^3\), and \(Lx^4=12Dx^2-\lambda_4x^4\). Stationarity consequently yields \(M_2=\mathbb E X^2=2D/\lambda_2\) and \(M_4=\mathbb E X^4=12DM_2/\lambda_4\).

The Markov semigroup gives \(\mathbb E[X_t\mid X_0=x]=e^{-\lambda_1t}x\) and, by variation of constants,
\[
\mathbb E[X_t^3\mid X_0=x]
=e^{-\lambda_3t}x^3+6Dx\,H(t).
\]
Taking stationary products with \(X_0\) and \(X_0^3\) therefore yields
\[
\Delta(t)=6DM_2H(t)+M_4(e^{-\lambda_3t}-e^{-\lambda_1t})
=(6DM_2-M_4(\lambda_3-\lambda_1))H(t).
\]
Since \(\lambda_3-\lambda_1=r(m_1-m_3)\), substituting \(M_4\) gives
\[
6DM_2-M_4(\lambda_3-\lambda_1)
=\frac{6DM_2}{1-m_4}\bigl[1-m_4-2m_1+2m_3\bigr]
=\frac{6DM_2}{1-m_4}\,\mathbb E[(1-Q)^3(1+Q)].
\]
This amplitude is strictly positive because \(-1<Q<1\) almost surely. Furthermore,
\[
H(t)=\int_0^t e^{-\lambda_1 s-\lambda_3(t-s)}\,ds>0
\]
for every \(t>0\). Both rates are positive. The derivative of the explicit difference of exponentials changes sign exactly once; solving its zero gives the displayed \(t_*\). If the rates coincide, \(H(t)=t e^{-\lambda_1t}\) has its unique maximum at \(1/\lambda_1\). Since reversibility would require equality of the two chronological fourth moments, their strict difference proves that \(X\) is not reversible.

For \(Z_t=X_t+V_t\), expand \(\mathbb E[Z_0Z_t^3-Z_0^3Z_t]\). Terms involving one centered independent factor vanish; those with exactly two factors from each process cancel because \(\mathbb E X_0^2=\mathbb E X_t^2\), \(\mathbb E V_0^2=\mathbb E V_t^2\), and two-point covariances are symmetric under swapping the times. The all-\(V\) term vanishes by reversibility. Hence \(\Delta_Z(t)=\Delta_X(t)\).

## Verification
The standalone file `verify_time_arrow.py` independently implements the polynomial generator as a finite matrix and evaluates its matrix exponential rather than the displayed chronological formula. It compares stationary mixed moments from that semigroup against the closed form over 500 seeded four-point reset laws and 20 deterministic reset tests, including reflection and the degenerate case \(\lambda_1=\lambda_3\). All 520 tests passed with the specified tolerances. The verification also compares values on both sides of the derived unique peak. The generator calculation and positivity factorization above are the proof; finite checks are corroboration only.

## Relationship to prior work
Biroli, Feld, Hartmann, Majumdar, and Schehr (arXiv:2406.08387, first posted 12 June 2024) establish the stationary one-time density and target-search properties of deterministic signed rescaling. The present claim instead concerns the ordered fourth moments at two stationary times and extends the reset multiplier to an arbitrary compactly supported signed law. Related polynomial-moment descriptions determine relaxation rates but do not by themselves state the universal positive chronological factorization or the unique optimal lag. Time-irreversibility diagnostics in nonequilibrium processes are established context, not a claim of inventing fourth-order diagnostics.

## Limitations
All statements require uniform strict contractivity, Poissonian event times, independent Brownian forcing, and stationarity. There is no assertion for arbitrary heavy-tailed multipliers, renewal event times, or observation noise correlated with the particle. The signature does not quantify entropy production or finite-sample detection power. Its algebra can be approached from existing polynomial-generator methods, so publication priority over all equivalent general theorems is not established.

## References
1. M. Biroli, Y. Feld, A. K. Hartmann, S. N. Majumdar, G. Schehr, *Resetting by rescaling: exact results for a diffusing particle in one-dimension*, arXiv:2406.08387v1 (12 June 2024), https://arxiv.org/abs/2406.08387.
2. I. M. Sokolov, *Linear Response and Fluctuation-Dissipation Relations for Brownian Motion under Resetting*, Physical Review Letters **130**, 067101 (2023), DOI:10.1103/PhysRevLett.130.067101 (related background, different protocol).
