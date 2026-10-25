# A one-parameter counterexample to reversible two-lag variance bounds

## Finding

For every \(\alpha\in(0,1)\), consider the three-state Markov chain on \(\{0,1,2\}\) with transition kernel \(P_\alpha=(1-\alpha)I+\alpha S\), where \(S\) moves each state one step clockwise modulo three. Its stationary distribution is uniform. For the centered observable \(f(i)=\cos(2\pi i/3)\), the normalized lag correlations and normalized long-run variance are

\[
\rho_1=1-\frac{3\alpha}{2},\qquad
\rho_2=1-3\alpha+\frac{3\alpha^2}{2},\qquad
\tau=1+2\sum_{k\ge1}\rho_k=\frac{1-\alpha}{\alpha}.
\]

Consequently,

\[
\frac{(1+\rho_1)^2}{1-\rho_2}-\tau
=\frac{4-6\alpha+3\alpha^2}{6\alpha(2-\alpha)}>0
\quad(0<\alpha<1).
\]

Thus the lower bound \(\tau\ge(1+\rho_1)^2/(1-\rho_2)\), obtained from the reversible spectral moment representation, fails for every member of this irreducible, aperiodic, nonreversible family.

## Assumptions and scope

Time is discrete and the chain is started in stationarity. The parameter satisfies \(0<\alpha<1\). The transition matrix is

\[
P_\alpha=\begin{pmatrix}
1-\alpha&\alpha&0\\
0&1-\alpha&\alpha\\
\alpha&0&1-\alpha
\end{pmatrix}.
\]

Every clockwise edge has positive probability and every state has a positive self-loop, so the chain is irreducible and aperiodic. It is not reversible: for example, \(P_\alpha(0,1)=\alpha>0\) but \(P_\alpha(1,0)=0\). The observable \(f(i)=\cos(2\pi i/3)\) has stationary mean zero and variance \(1/2\). Here \(\rho_k=\operatorname{Cov}(f(X_0),f(X_k))/\operatorname{Var}_\pi(f)\) and \(\tau\) is the asymptotic variance divided by \(\operatorname{Var}_\pi(f)\). The result concerns this family and this observable; it does not classify all nonreversible chains.

## Proof

Let \(\omega=e^{2\pi i/3}\). The nonconstant Fourier mode \(i\mapsto\omega^i\) is an eigenfunction of \(P_\alpha\) with eigenvalue

\[
\lambda=1-\alpha+\alpha\omega
=1-\frac{3\alpha}{2}+i\frac{\sqrt3\alpha}{2}.
\]

Taking real parts and normalizing by \(\operatorname{Var}_\pi(f)=1/2\) gives \(\rho_k=\operatorname{Re}(\lambda^k)\). Hence the displayed formulas for \(\rho_1\) and \(\rho_2\) follow by expanding \(\lambda\) and \(\lambda^2\).

For \(0<\alpha<1\),

\[
|\lambda|^2=1-3\alpha+3\alpha^2<1,\qquad
|1-\lambda|^2=3\alpha^2.
\]

The correlation series therefore converges absolutely, and

\[
\begin{aligned}
\tau
&=1+2\operatorname{Re}\frac{\lambda}{1-\lambda}
=\frac{1-|\lambda|^2}{|1-\lambda|^2}\\
&=\frac{3\alpha(1-\alpha)}{3\alpha^2}
=\frac{1-\alpha}{\alpha}.
\end{aligned}
\]

The proposed reversible lower-bound expression simplifies to

\[
\frac{(1+\rho_1)^2}{1-\rho_2}
=\frac{(4-3\alpha)^2}{6\alpha(2-\alpha)}.
\]

Subtracting \(\tau\) gives

\[
\frac{(4-3\alpha)^2-6(2-\alpha)(1-\alpha)}{6\alpha(2-\alpha)}
=\frac{4-6\alpha+3\alpha^2}{6\alpha(2-\alpha)}.
\]

The denominator is positive on \((0,1)\). The numerator is positive for every real \(\alpha\), since its discriminant is \((-6)^2-4\cdot3\cdot4=-12<0\) and its leading coefficient is positive. This proves the strict gap throughout the full parameter interval.

For comparison, if a reversible stationary chain has normalized spectral measure \(F\) on \([-1,1]\), then \(\rho_k=\int x^kF(dx)\) and, when the long-run variance is finite, \(\tau=\int (1+x)/(1-x)\,F(dx)\). Cauchy–Schwarz yields

\[
\tau=\int\frac{(1+x)^2}{1-x^2}\,F(dx)
\ge\frac{(1+\rho_1)^2}{1-\rho_2}.
\]

That argument relies on the reversible moment representation; the complex eigenvalue above is why it does not apply to \(P_\alpha\).

## Verification

The accompanying standard-library checker evaluates the transition matrix and the first two autocorrelations using exact rational arithmetic at \(\alpha\in\{1/4,1/2,3/4,9/10\}\), and verifies the algebraic gap identity at those points. At \(\alpha=1/2\), it obtains \(\rho_1=1/4\), \(\rho_2=-1/8\), \(\tau=1\), and \((1+\rho_1)^2/(1-\rho_2)=25/18\), giving gap \(7/18\). These finite checks are consistency checks only; the proof of the universal claim is the analytic calculation above.

Reproduction: run `python3 verify.py` with Python 3. No third-party package is required.

## Relationship to prior work

Berg and Song (2022) use the reversible-chain spectral moment representation of the autocovariance sequence to motivate shape constraints for estimating asymptotic variance. Choi (2017) studies spectral and variance bounds for nonreversible Markov chains, including asymmetric cycle walks. The present calculation gives an explicit lazy one-way three-cycle family and the exact strict gap from the reversible two-lag expression; the inspected sources do not state this parameter-uniform comparison. The related general spectral methods make this a deliberately narrow boundary result rather than a broad theory of nonreversible variance estimation.

## Limitations

The claim is restricted to one three-state family and one Fourier observable. It does not characterize the feasible set of autocorrelation pairs for general nonreversible chains, give an optimal bound for that class, or prove a statement about the finite-sample performance of any estimator. The exact computation is elementary once the complex eigenvalue is identified; the mathematical content is the uniform strict comparison over the full parameter interval.

## References

1. M. C. H. Choi, “Metropolis–Hastings reversiblizations of non-reversible Markov chains,” arXiv:1706.00068, version 1 posted 2017-05-31; see the discussion of asymmetric cycle walks and variance bounds.
2. S. Berg and H. Song, “Efficient shape-constrained inference for the autocovariance sequence from a reversible Markov chain,” arXiv:2207.12705, version 1 posted 2022-07-26; see the reversible spectral moment representation in equation (7).
