# Low-transmission covariance law for non-Markovian branching outbreaks

## Finding
Consider a continuous-time age-dependent branching process with one initial individual. Individuals live for independent copies of a positive random lifetime \(Q\) with \(\mathbb E[Q]=1\) and \(Q\le B\) almost surely, and produce children during their lives at independent Poisson rate \(\lambda\). If \(T_\lambda\) is the time of final extinction and \(S_\lambda\) is the sum of all individual lifetimes, then with \(v=\operatorname{Var}(Q)\),
\[
\boxed{\operatorname{Cov}(T_\lambda,S_\lambda)=v+\lambda(\tfrac12+2v)+O_B(\lambda^2)}\qquad(\lambda\downarrow0).
\]
The linear sensitivity is therefore \(\tfrac12+2v\ge\tfrac12\), with equality exactly for deterministic lifetimes. In contrast with the known insensitivity of the two separate means, this joint moment detects individual-life variance even to first order in transmission rate.

## Assumptions and scope
The lifetime law is arbitrary on \((0,B]\) for finite \(B\), with mean one; atoms, including a deterministic duration, are allowed. At each individual's birth, its lifetime and its independent rate-\(\lambda\) Poisson birth process are sampled, independently of every other individual. The initial ancestor is born at time zero. The population count \(Z_\lambda(t)\) is the number of people alive at time \(t\); thus \(S_\lambda=\int_0^\infty Z_\lambda(t)\,dt\). For \(0\le\lambda<1\), the offspring mean is \(\lambda\), so extinction is almost sure. The bound in the displayed expansion is uniform over lifetime distributions bounded by the same \(B\), for sufficiently small \(\lambda\) depending on \(B\).

## Proof
**1. A controlled one-birth expansion.** Let \(N\) be the total number of people ever born. Since each individual's own-life births are stochastically dominated by a Poisson number of mean \(\theta=\lambda B\), \(N\) is dominated by the total progeny \(N^*\) of a Galton–Watson process with Poisson-\(\theta\) offspring. For sufficiently small \(\theta\), its Borel total-progeny formula is
\[\Pr(N^*=n)=e^{-n\theta}\frac{(n\theta)^{n-1}}{n!},\quad n\ge1.\]
The inequality \(n^{n-1}/n!\le e^n\) bounds \(\mathbb E[(N^*)^2\mathbf1_{\{N^*\ge3\}}]\) by a convergent geometric series of order \(O(\theta^2)\) when \(e\theta<1\). Pathwise \(0\le T_\lambda\le S_\lambda\le BN\); hence the contribution of histories with at least three individuals to each of \(\mathbb E[T_\lambda]\), \(\mathbb E[S_\lambda]\), and \(\mathbb E[T_\lambda S_\lambda]\) is \(O_B(\lambda^2)\).

Write \(q\) for the founder lifetime and \(z\) for an independent child lifetime. A history with no birth has probability \(e^{-\lambda q}\) conditional on \(q\), with \(T=S=q\). Histories with exactly one birth, occurring at age \(u\in[0,q]\), have joint conditional density \(\lambda e^{-\lambda(q+z)}\,du\) and statistics
\[T=q+(u+z-q)_+,\qquad S=q+z.\]
Thus for any \(F\) among \(T\), \(S\), and \(TS\), Taylor expansion of the exponential factors (uniform since \(q,z\le B\)) gives the exact first-order identity
\[
\mathbb E[F_\lambda]=\mathbb E[F_0]+\lambda\,\mathbb E\!\left[\int_0^{Q_0}\bigl(F_1(Q_0,Q_1,u)-F_0(Q_0)\bigr)\,du\right]+O_B(\lambda^2),
\]
where \(Q_0,Q_1\) are independent copies of \(Q\).

**2. The geometry of overlapping lifetimes.** Define
\[
J(q,z)=\int_0^q(u+z-q)_+\,du=
\begin{cases}z^2/2,&z\le q,\\qz-q^2/2,&z>q.\end{cases}
\]
For all positive \(q,z\), \(J(q,z)+J(z,q)=qz\). Exchangeability and \(\mathbb E Q=1\) therefore give
\[\mathbb E J(Q_0,Q_1)=\tfrac12,\qquad
\mathbb E[(Q_0+Q_1)J(Q_0,Q_1)]=\mathbb E[Q^2].\]
Write \(m_2=\mathbb E[Q^2]\). Applying Step 1 separately to \(T,S,TS\),
\[
\mathbb E[T_\lambda]=1+\tfrac12\lambda+O_B(\lambda^2),\qquad
\mathbb E[S_\lambda]=1+\lambda+O_B(\lambda^2),
\]
\[
\mathbb E[T_\lambda S_\lambda]=m_2+\lambda\left(\mathbb E[Q_0^2Q_1]+\mathbb E[(Q_0+Q_1)J(Q_0,Q_1)]\right)+O_B(\lambda^2)
=m_2+2m_2\lambda+O_B(\lambda^2).
\]
Subtracting the product of means gives
\[
\operatorname{Cov}(T_\lambda,S_\lambda)=(m_2-1)+\lambda(2m_2-3/2)+O_B(\lambda^2)
=v+\lambda(1/2+2v)+O_B(\lambda^2),
\]
as asserted. The sign and variance-only characterization follow from \(v\ge0\).

## Verification
An accompanying standalone Python script, `verify_light_birth_covariance.py`, uses only the standard library and exact rational arithmetic. It directly enumerates the ordered parent–child lifetime combinations for four finite-support laws, checks the pairwise identity for \(J\), reconstructs the individual first-order derivatives of each moment, and verifies the claimed covariance coefficient. The resulting variance/coefficient pairs are \((0,1/2)\), \((1/4,1)\), \((9/32,17/16)\), and \((8/25,57/50)\). These finite checks are illustrative; the proof is the uniform Galton–Watson domination and the exchangeability identity above.

## Relationship to prior work
Britton and Neal (2013) proved exact first moments of occupation times in the same lifetime-general branching model. Ball, Britton and Neal (2014, Section 3.1; originally published on 4 August 2014) proved that \(\mathbb E[T_\lambda]=-\log(1-\lambda)/\lambda\) and \(\mathbb E[S_\lambda]=1/(1-\lambda)\) for \(0<\lambda<1\), independently of the lifetime distribution. Both are compatible with, but do not determine, the covariance established here. Garcia-Millan and collaborators (2018) study continuous-time **memoryless** branching with Poisson event clocks and universal critical scaling of population correlations and avalanche observables; this is a different lifetime assumption and parameter limit. The present result isolates non-Markovian lifetime dependence of a joint outbreak statistic in the sparse-birth limit.

## Limitations
The theorem gives a small-\(\lambda\) expansion, not exact covariance at arbitrary birth rates or a monotonicity theorem across the entire subcritical regime. Uniform quadratic control is established for bounded positive lifetimes; extension to unbounded distributions requires a separate tail argument. The originality comparison is literature-based and cannot exclude an equivalent older formulation in unindexed sources. No independent mathematical audit has been performed.

## References
1. T. Britton and P. Neal, *On the expected time a branching process has K individuals alive*, arXiv:1304.8014v1 (30 April 2013).
2. F. Ball, T. Britton and P. Neal, *On expected durations of birth-death processes, with applications to branching processes and SIS epidemics*, arXiv:1408.0641v1 (4 August 2014), especially Sections 2 and 3.1.
3. R. Garcia-Millan, J. Pausch, B. Walter and G. Pruessner, *Field-theoretic approach to the universality of branching processes*, arXiv:1808.08418v2 (2018), Sections I–III.
