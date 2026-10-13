# Reversible modulation resolves the stationary-interarrival order for MMPPs
## Finding
Consider a finite-state irreducible Markov-modulated Poisson process (MMPP). Let \(Q\) be the generator of the modulating chain, let \(\pi\) be its stationary distribution, and let
\[
D=\operatorname{diag}(\lambda_1,\ldots,\lambda_m)
\]
contain the state-dependent event rates. Put
\[
C=Q-D,
\qquad
\lambda_*=\pi D\mathbf 1>0,
\qquad
\alpha_i=\frac{\pi_i\lambda_i}{\lambda_*}.
\]
Assume the modulating chain is reversible:
\[
\pi_iq_{ij}=\pi_jq_{ji}.
\]

Let \(T^\pi\) be the first interarrival time under the time-stationary initialization and \(T^\alpha\) the first interarrival time under the event-stationary initialization. Then
\[
T^\pi\ge_{\mathrm{st}}T^\alpha.
\tag{1}
\]
Equivalently,
\[
\pi e^{Ct}\mathbf 1
\ge
\alpha e^{Ct}\mathbf 1
\qquad(t\ge0).
\]

The inequality is strict for every \(t>0\) unless
\[
\lambda_1=\cdots=\lambda_m.
\]
When all event rates are equal, the two interarrival laws coincide and are exponential.

There is also an explicit structural description. If
\[
A=-C=-Q+D,
\]
then there are rates \(r_j>0\) and weights \(w_j\ge0\), with
\[
\sum_jw_j=1,
\]
such that
\[
\Pr(T^\pi>t)
=
\sum_jw_je^{-r_jt}.
\tag{2}
\]
Thus the time-stationary interarrival law is a finite hyperexponential mixture. Its hazard is nonincreasing, and is strictly decreasing unless all \(\lambda_i\) are equal.

Every finite irreducible birth-death MMPP satisfies the reversibility hypothesis, so (1) holds for arbitrary state-dependent event rates in that entire class.

## Assumptions and scope
The modulating state space is finite, \(Q\) is irreducible, and the average event rate
\[
\lambda_*=\sum_i\pi_i\lambda_i
\]
is positive. Individual \(\lambda_i\) may be zero.

Reversibility is with respect to the stationary distribution \(\pi\). No assumption that \(Q\) or \(C\) is symmetric in the ordinary Euclidean inner product is made.

The result compares only the time-stationary and event-stationary first interarrival distributions. It does not assert that successive interarrival times are independent.

## Proof
Use the weighted inner product
\[
\langle f,g\rangle_\pi
=
\sum_i\pi_i f_i g_i.
\]
Reversibility of \(Q\) is exactly self-adjointness of \(Q\) in this inner product. Since \(D\) is diagonal, it is also self-adjoint, and therefore
\[
A=-Q+D
\]
is self-adjoint.

For every nonzero vector \(f\),
\[
\langle f,Af\rangle_\pi
=
\frac12
\sum_{i,j}\pi_iq_{ij}(f_i-f_j)^2
+
\sum_i\pi_i\lambda_i f_i^2.
\tag{3}
\]
Both terms are nonnegative. If their sum were zero, irreducibility would force \(f\) to be constant, while the second term and \(\lambda_*>0\) would then force that constant to be zero. Hence \(A\) is positive definite in \(L^2(\pi)\).

Choose an orthonormal eigenbasis
\[
A\phi_j=r_j\phi_j,
\qquad r_j>0,
\]
and expand
\[
\mathbf 1=\sum_j a_j\phi_j.
\]
Set
\[
w_j=a_j^2.
\]
Then
\[
w_j\ge0,
\qquad
\sum_jw_j
=
\langle\mathbf 1,\mathbf 1\rangle_\pi
=
1.
\]
The time-stationary survival function is
\[
S_\pi(t)
=
\pi e^{Ct}\mathbf 1
=
\langle\mathbf 1,e^{-At}\mathbf 1\rangle_\pi
=
\sum_jw_je^{-r_jt},
\]
which proves (2).

Its hazard is
\[
h_\pi(t)
=
-\frac{S_\pi'(t)}{S_\pi(t)}
=
\frac{\sum_jw_jr_je^{-r_jt}}
{\sum_jw_je^{-r_jt}}.
\]
Differentiating gives
\[
h_\pi'(t)
=
-
\operatorname{Var}_t(r)
\le0,
\tag{4}
\]
where the variance is taken under the tilted weights proportional to
\[
w_je^{-r_jt}.
\]

At time zero,
\[
h_\pi(0)
=
\langle\mathbf 1,A\mathbf 1\rangle_\pi.
\]
Since
\[
Q\mathbf 1=0,
\]
one has
\[
A\mathbf 1=D\mathbf 1,
\]
and therefore
\[
h_\pi(0)
=
\pi D\mathbf 1
=
\lambda_*.
\tag{5}
\]

For the event-stationary initialization,
\[
S_\alpha(t)
=
\alpha e^{Ct}\mathbf 1
=
\frac1{\lambda_*}
\langle D\mathbf 1,e^{-At}\mathbf 1\rangle_\pi.
\]
Using
\[
D\mathbf 1=A\mathbf 1
\]
and self-adjointness of \(A\),
\[
S_\alpha(t)
=
\frac1{\lambda_*}
\langle\mathbf 1,Ae^{-At}\mathbf 1\rangle_\pi
=
-\frac{S_\pi'(t)}{\lambda_*}.
\]
Hence
\[
S_\alpha(t)
=
\frac{h_\pi(t)}{\lambda_*}S_\pi(t).
\tag{6}
\]
Equations (4) and (5) imply
\[
h_\pi(t)\le\lambda_*,
\]
and (6) gives
\[
S_\alpha(t)\le S_\pi(t),
\]
which is exactly (1).

It remains to identify equality. Equality of the hazards for a positive interval would force the spectral variance in (4) to vanish. Because every tilted weight with \(w_j>0\) remains positive at finite \(t\), this happens exactly when all spectral mass of \(\mathbf 1\) is concentrated at one eigenvalue. Equivalently,
\[
A\mathbf 1=r\mathbf 1.
\]
But
\[
A\mathbf 1=D\mathbf 1,
\]
so this occurs exactly when all \(\lambda_i\) are equal. Otherwise
\[
h_\pi'(t)<0
\qquad(t\ge0),
\]
and (6) is strict for every \(t>0\).

## Verification
The standalone script `verify.py` checks a reversible three-state example whose generator is not symmetric in the ordinary Euclidean inner product:
\[
Q=
\begin{pmatrix}
-1&1&0\\
2&-5&3\\
0&4&-4
\end{pmatrix},
\qquad
\pi=
\left(\frac8{15},\frac4{15},\frac3{15}\right),
\qquad
D=\operatorname{diag}(1,4,2).
\]
It verifies detailed balance, the average rate
\[
\lambda_*=2,
\]
the event-stationary distribution
\[
\alpha=
\left(\frac4{15},\frac8{15},\frac3{15}\right),
\]
symmetry of the weighted transform of \(A\), positivity of its eigenvalues and spectral weights, and the identities
\[
S_\alpha(t)=-S_\pi'(t)/\lambda_*
\]
and
\[
S_\pi(t)>S_\alpha(t)
\]
at deterministic positive times.

The script also verifies that the computed hyperexponential hazard decreases and that equal event rates collapse the two initializations to the same exponential law.

A successful run ends with a line beginning
`VERIFY_OK lambda_star=2.000000000000`.

The numerical checks replay finite-dimensional linear algebra only. The order for all finite reversible MMPPs is proved analytically above.

## Relationship to prior work
Asanjarani and Nazarathy formulate the stationary MMPP comparison
\[
\pi e^{Ct}\mathbf 1
\ge
\alpha e^{Ct}\mathbf 1
\]
as Property IV and conjecture it for irreducible MMPPs. They prove the two-state case. Their conclusion also notes that analogous arguments yield the desired properties when \(C\) is symmetric, while the general higher-order MMPP problem remains open.

The present result covers a strictly broader structural class. Reversibility only requires self-adjointness in the weighted space \(L^2(\pi)\), or equivalently diagonal symmetrizability. When \(\pi\) is nonuniform, a reversible generator \(Q\) and the corresponding \(C=Q-D\) need not be symmetric as ordinary matrices. In particular, arbitrary finite birth-death modulators can be nonsymmetric while remaining reversible.

The diagonal symmetrization is not merely a restatement of the symmetric-\(C\) MMPP case: the similarity transform that makes a reversible generator symmetric generally does not preserve the all-ones vector and therefore does not itself produce a new Markov generator representation with the same stationary-arrival formulas. The proof instead works directly in the weighted Hilbert space and exploits the spectral measure of \(\mathbf 1\).

He later proved a squared-coefficient-of-variation lower bound for event-stationary MMPP inter-event times in full generality. That scalar moment result is consistent with the stochastic-order consequence here but is weaker than the survival-function inequality and does not provide the reversible spectral representation.

## Limitations
The theorem does not resolve the conjecture for nonreversible modulators. The key step is self-adjointness of the killed generator \(A=-Q+D\); without reversibility its spectral expansion need not have nonnegative mixture weights.

The hyperexponential representation is for the time-stationary first interarrival law, not a claim that the entire MMPP is equivalent to a renewal process.

A residual bibliographic risk is that the weighted self-adjoint argument may appear implicitly in older reversible killed-chain or phase-type literature without being stated as the stationary MMPP comparison.

## References
1. A. Asanjarani and Y. Nazarathy, “Stationary Markovian Arrival Processes, Results and Open Problems,” arXiv:1905.01736v1, 5 May 2019; *The ANZIAM Journal* 64 (2022), 54–68. DOI: 10.1017/S1446181122000013.
2. Q.-M. He, “Bounds on the mean and squared coefficient of variation of phase-type distributions,” *Journal of Applied Probability* 59 (2022), 601–620. DOI: 10.1017/jpr.2021.18.
