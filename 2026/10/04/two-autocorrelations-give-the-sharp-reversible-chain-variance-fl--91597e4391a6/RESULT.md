# Two autocorrelations give the sharp reversible-chain variance floor

## Finding

Let \(P\) be a stationary reversible Markov kernel with invariant law \(\pi\), and let
\[
g\in L^2(\pi),
\qquad
\pi(g)=0,
\qquad
\gamma_0=\langle g,g\rangle_\pi>0.
\]
Write
\[
\gamma_k=\langle g,P^kg\rangle_\pi,
\qquad
\rho_k=\frac{\gamma_k}{\gamma_0},
\qquad
r=\rho_1,
\qquad
s=\rho_2.
\]
Let \(\nu\) be the probability spectral measure of \(g\), so
\[
\rho_k=\int_{[-1,1]}\lambda^k\,\nu(d\lambda).
\]
Define the spectral asymptotic-variance factor
\[
\tau_g
=
\int_{[-1,1]}
\frac{1+\lambda}{1-\lambda}\,
\nu(d\lambda),
\]
with value \(+\infty\) when the integral diverges.

If
\[
s<1,
\]
then
\[
\boxed{
\tau_g
\ge
\frac{(1+r)^2}{1-s}.
}
\tag{1}
\]
Consequently, whenever the usual reversible-chain asymptotic variance is represented by
\[
\sigma_{\mathrm{as}}^2=\gamma_0\tau_g,
\]
one has
\[
\boxed{
\sigma_{\mathrm{as}}^2
\ge
\frac{(\gamma_0+\gamma_1)^2}
{\gamma_0-\gamma_2}.
}
\tag{2}
\]

The bound is exact from the first two autocorrelations alone. Equality in (1) holds precisely when the normalized spectral measure is supported on
\[
\{-1,q\},
\]
where
\[
q=\frac{r+s}{1+r}
\]
and
\[
\nu(\{q\})
=
\frac{(1+r)^2}{1+2r+s}.
\tag{3}
\]
The remaining mass is at \(-1\). When
\[
s=r^2,
\]
that remaining mass is zero and the equality measure is the single atom \(\delta_r\).

Every feasible two-lag pair
\[
-1<r<1,
\qquad
r^2\le s<1
\]
has such an equality realization by an irreducible four-state reversible chain. If irreducibility and aperiodicity are both imposed, the same right side of (1) remains the exact infimum. It is attained when \(s=r^2\); for \(s>r^2\) it is strict for every finite irreducible aperiodic chain but is approached by an explicit family that preserves \(r\) and \(s\) exactly.

The two-lag bound strengthens the one-lag Jensen bound:
\[
\frac{(1+r)^2}{1-s}
\ge
\frac{1+r}{1-r},
\tag{4}
\]
with strict inequality exactly when
\[
s>r^2.
\]

## Assumptions and scope

The result concerns a centered square-integrable observable of a stationary reversible chain.

The quantity \(\tau_g\) is the standard reversible spectral asymptotic-variance functional. Formula (2) is asserted in settings where that spectral functional equals the asymptotic variance, including the usual finite-state irreducible aperiodic setting and the standard finite-integral reversible CLT setting.

The result uses only the normalized lag-one and lag-two autocorrelations. It does not claim that those two numbers identify the full spectral measure or the full autocorrelation sequence.

The periodic equality constructions are used to prove global sharpness. The aperiodic statement is separately handled by exact-moment lazy approximations.

## Proof

Normalize the spectral measure by \(\gamma_0\). Then
\[
r=\int\lambda\,\nu(d\lambda),
\qquad
s=\int\lambda^2\,\nu(d\lambda).
\]
Since \(\nu\) is a probability measure,
\[
r^2\le s.
\]

If \(\tau_g=+\infty\), (1) is immediate. Assume henceforth that \(\tau_g<\infty\). Write
\[
1+r
=
\int(1+\lambda)\,\nu(d\lambda).
\]
For \(\lambda\in[-1,1]\),
\[
1+\lambda
=
\sqrt{\frac{1+\lambda}{1-\lambda}}\,
\sqrt{1-\lambda^2},
\]
with both factors interpreted as zero at \(\lambda=-1\). Cauchy--Schwarz gives
\[
(1+r)^2
\le
\left(
\int\frac{1+\lambda}{1-\lambda}\,\nu(d\lambda)
\right)
\left(
\int(1-\lambda^2)\,\nu(d\lambda)
\right).
\]
The two factors are
\[
\tau_g
\qquad\text{and}\qquad
1-s,
\]
which proves (1).

For equality, Cauchy--Schwarz requires the two displayed square-root functions to be proportional \(\nu\)-almost surely. Away from \(-1\), their ratio is
\[
\frac1{1-\lambda}.
\]
Hence all spectral mass outside \(-1\) must sit at one point \(q\). Conversely, any measure supported on \(\{-1,q\}\) gives equality.

Solving the first two moment equations determines the equality measure uniquely. If
\[
\alpha=\nu(\{q\}),
\]
then
\[
r=-(1-\alpha)+\alpha q
\]
and
\[
s=(1-\alpha)+\alpha q^2.
\]
Solving gives
\[
q=\frac{r+s}{1+r},
\qquad
\alpha=\frac{(1+r)^2}{1+2r+s}.
\]
For every
\[
-1<r<1,
\qquad
r^2\le s<1,
\]
one has
\[
-1<q<1,
\qquad
0<\alpha\le1.
\]
Moreover,
\[
1-\alpha
=
\frac{s-r^2}{1+2r+s}.
\]
Thus the \(-1\) mass is positive exactly when \(s>r^2\).

To realize equality by a finite chain, put
\[
\theta=\frac{1+q}{2}
\]
and use the symmetric stochastic matrix
\[
P_q=
\begin{pmatrix}
0&0&\theta&1-\theta\\
0&0&1-\theta&\theta\\
\theta&1-\theta&0&0\\
1-\theta&\theta&0&0
\end{pmatrix}.
\tag{5}
\]
Its invariant law is uniform. The vectors
\[
u_-=(1,1,-1,-1)
\]
and
\[
u_q=(1,-1,1,-1)
\]
are orthonormal in \(L^2\) of the uniform law and satisfy
\[
P_qu_-=-u_-,
\qquad
P_qu_q=qu_q.
\]
Therefore
\[
g=\sqrt{1-\alpha}\,u_-+\sqrt{\alpha}\,u_q
\]
has variance one and spectral measure
\[
(1-\alpha)\delta_{-1}+\alpha\delta_q.
\]
The chain is irreducible and has period two, proving exact global sharpness.

Now impose aperiodicity. When \(s>r^2\), equality requires positive spectral mass at \(-1\). A finite irreducible aperiodic reversible chain has no eigenvalue \(-1\), so equality is impossible.

Nevertheless the bound is still the exact aperiodic infimum. For sufficiently small
\[
\eta>0,
\]
set
\[
r_0=\frac{r-\eta}{1-\eta},
\qquad
s_0=
\frac{s-2\eta r+\eta^2}{(1-\eta)^2}.
\tag{6}
\]
Then
\[
s_0-r_0^2
=
\frac{s-r^2}{(1-\eta)^2},
\]
and \((r_0,s_0)\) remains feasible for small \(\eta\). Build the periodic equality chain for \((r_0,s_0)\), and then lazify it:
\[
P_\eta
=
\eta I+(1-\eta)P_0.
\tag{7}
\]
The chain is now irreducible and aperiodic. Its eigenvalues on the two spectral components are transformed by
\[
\lambda\mapsto\eta+(1-\eta)\lambda.
\]
Equations (6) ensure that the resulting observable has exactly the target first and second autocorrelations \(r,s\). As
\[
\eta\downarrow0,
\]
its spectral asymptotic-variance factor converges to the equality value in (1). This proves the sharp aperiodic infimum.

If \(s=r^2\), the spectral equality measure is \(\delta_r\). It is attained by the two-state symmetric chain
\[
\begin{pmatrix}
(1+r)/2&(1-r)/2\\
(1-r)/2&(1+r)/2
\end{pmatrix}
\]
with observable \((1,-1)\); because \(-1<r<1\), this chain is irreducible and aperiodic.

Finally, since
\[
s\ge r^2,
\]
\[
\frac{(1+r)^2}{1-s}
\ge
\frac{(1+r)^2}{1-r^2}
=
\frac{1+r}{1-r},
\]
which proves (4).

## Verification

The accompanying checker uses exact rational arithmetic.

It verifies the Cauchy--Schwarz inequality after clearing denominators for thousands of finitely supported rational spectral measures. It then generates rational equality measures on \(\{-1,q\}\), reconstructs \(r,s,q,\alpha\), checks the exact bound, and verifies the eigenvectors of the four-state transition matrix.

It also performs the recalibration (6) before lazification, checks that the lazy chain preserves the target \(r,s\) exactly, and confirms that its spectral asymptotic-variance factor lies strictly above the bound when \(s>r^2\).

These finite computations are supplementary. The universal result is proved analytically above.

## Relationship to prior work

Geyer's 1992 article is a classical MCMC source emphasizing asymptotic variance, Monte Carlo error, reversible-chain central limit theory, and variance estimation.

Häggström and Rosenthal give a detailed spectral treatment of asymptotic variance for reversible Markov-chain central limit theorems. Their notation includes the autocovariances
\[
\gamma_k=\langle h,P^kh\rangle
\]
and the spectral expression
\[
\int_{-1}^1\frac{1+\lambda}{1-\lambda}\,E_h(d\lambda).
\]
Their results compare several standard definitions of asymptotic variance and state conditions under which they agree. They do not state the sharp lower envelope determined solely by \(\gamma_0,\gamma_1,\gamma_2\).

Longla likewise develops limit theorems through reversible spectral measures and relates asymptotically linear partial-sum variance to integrability of the spectral kernel.

Berg and Song represent reversible autocovariance sequences as moment sequences on \([-1,1]\) and study shape-constrained estimation, including Geyer's paired sequence. Their framework makes the two-lag problem a truncated spectral-moment question, but the inspected statements do not give inequality (1), its equality fiber, or the exact finite-state realizability result.

Targeted searches for the raw-autocovariance formula, two-lag integrated-autocorrelation lower bounds, effective-sample-size bounds from \(\rho_1,\rho_2\), and equivalent spectral-moment formulations did not locate this exact statement.

## Limitations

The bound uses reversibility. For nonreversible chains the scalar spectral-measure representation on \([-1,1]\) is unavailable in this form.

Two lags cannot identify the asymptotic variance; the theorem gives only its exact lower envelope.

When \(s>r^2\), exact equality uses a period-two spectral component. In the finite irreducible aperiodic class the bound is an unattained infimum, although it is approached while preserving the two specified autocorrelations exactly.

The originality search was targeted. Classical truncated-moment or variational literature may contain an equivalent Cauchy--Schwarz envelope under different notation.

## References

1. C. J. Geyer, “Practical Markov Chain Monte Carlo,” *Statistical Science* 7 (1992), 473–483, DOI 10.1214/ss/1177011137.
2. O. Häggström and J. S. Rosenthal, “On Variance Conditions for Markov Chain CLTs,” *Electronic Communications in Probability* 12 (2007), 454–464, DOI 10.1214/ECP.v12-1336.
3. M. Longla, “Remarks on limit theorems for reversible Markov processes,” arXiv:1310.8239, first submitted 2013-10-30.
4. S. Berg and H. Song, “Efficient shape-constrained inference for the autocovariance sequence from a reversible Markov chain,” arXiv:2207.12705, 2022.
