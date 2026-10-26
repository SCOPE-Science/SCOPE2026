# A fourth-cumulant sign law for telegraphic particles in moving harmonic traps

## Finding
For a stationary one-dimensional run-and-tumble particle subject to any deterministic **monotone** harmonic-trap translation of nonzero total displacement, the finite-time experimenter work has **strictly negative fourth cumulant**, even when the thermal diffusivity is nonzero. This sign law fails for general protocols: a two-jump cyclic reversal can have strictly **positive** fourth cumulant. For the previously identified mean-work-minimizing open-loop transport, the exact fourth cumulant is a scalar ordered integral given below, and its long-duration standardized excess kurtosis has a universal leading coefficient independent of harmonic stiffness and transported distance:

\[
\frac{\kappa_4(W_T)}{\operatorname{Var}(W_T)^2}
=-\frac{6\omega^4}{\gamma^3(D+\omega^2/\gamma)^2}\frac1T+O(T^{-2}).
\]

The result distinguishes telegraphic propulsion from covariance-matched Gaussian active Ornstein–Uhlenbeck propulsion: both have the same mean and variance of the work for every prescribed protocol, whereas the Gaussian model has identically zero fourth cumulant.

## Assumptions and scope
Fix \(k>0\) (trap stiffness), \(\omega>0\) (active propulsion speed), \(\gamma>0\) (telegraph decorrelation rate), \(D\ge0\) (thermal diffusivity), and \(T>0\). Let \(\sigma_t\in\{-1,+1\}\) be an equilibrium, symmetric continuous-time Markov chain that switches sign at rate \(\gamma/2\), and let \(B\) be an independent two-sided standard Brownian motion. Before the protocol begins, the particle is stationary in a trap centered at zero. During the protocol,
\[
 dX_t=-k(X_t-\lambda_t)\,dt+\omega\sigma_t\,dt+\sqrt{2D}\,dB_t.
\]
The potential is \(V(x,\lambda)=\frac{k}{2}(x-\lambda)^2\). A deterministic protocol \(\lambda:[0,T]\to\mathbb R\) has finite variation; finite jumps, including endpoint jumps, are allowed. Define experimenter work by the Stieltjes integral of the potential change at **fixed particle position**: along continuous pieces, \(dW_t=k(\lambda_t-X_t)\,d\lambda_t\), and at a jump \(\Delta\lambda\), use \(\Delta W=V(X,\lambda^+)-V(X,\lambda^-)\). This agrees with the same Stieltjes rule for the random portion of work. The coordinate is continuous at a trap jump. A protocol is monotone if its signed measure \(d\lambda\) has one sign.

For a real random variable with four finite moments, \(\kappa_4(W)=\mathbb E[(W-\mathbb EW)^4]-3\operatorname{Var}(W)^2\). A Gaussian variable has fourth cumulant zero. All cumulants in the result are unconditional over the stationary particle state, telegraph dynamics, and thermal Brownian noise.

## Proof
**1. Exact linear work filter.** Write \(Y_t=X_t-\mathbb E X_t\). The stationary solution of the centered equation is
\[
Y_t=\omega\int_{-\infty}^{t}e^{-k(t-s)}\sigma_s\,ds
+\sqrt{2D}\int_{-\infty}^{t}e^{-k(t-s)}\,dB_s.
\]
For any deterministic finite-variation protocol,
\[
W-\mathbb EW=-k\int_{[0,T]}Y_t\,d\lambda_t
=-\omega\int_{-\infty}^{T}g(s)\sigma_s\,ds
-\sqrt{2D}\int_{-\infty}^{T}g(s)\,dB_s,
\]
with the deterministic integrable weight
\[
g(s)=k\int_{[\max(s,0),T]}e^{-k(t-s)}\,d\lambda_t,\quad s\le T,
\]
where the endpoint convention includes any initial jump when \(s\le0\). The last integral is Gaussian and independent of the telegraph contribution, so it contributes no fourth cumulant. Nonconstant monotone \(\lambda\) makes \(g\) nonzero and one-signed on a set of positive Lebesgue measure.

**2. Four-time telegraph cumulant.** For ordered times \(s_1<s_2<s_3<s_4\), stationarity, the Markov property, and reflection symmetry give
\[
\mathbb E[\sigma_{s_1}\sigma_{s_2}\sigma_{s_3}\sigma_{s_4}]
=e^{-\gamma[(s_2-s_1)+(s_4-s_3)]},
\quad \mathbb E[\sigma_s\sigma_t]=e^{-\gamma|t-s|}.
\]
Subtracting the three pairwise products yields
\[
\operatorname{cum}(\sigma_{s_1},\sigma_{s_2},\sigma_{s_3},\sigma_{s_4})
=-2e^{-\gamma[(s_3-s_1)+(s_4-s_2)]}.
\]
Permutation symmetry and Tonelli's theorem (the integrand is absolutely integrable) now imply the **exact** formula
\[
\boxed{\kappa_4(W)=-48\omega^4\!\int_{s_1<s_2<s_3<s_4\le T}
\prod_{j=1}^{4}g(s_j)\,
 e^{-\gamma[(s_3-s_1)+(s_4-s_2)]}\,ds_1ds_2ds_3ds_4.}
\]
For a nonconstant monotone protocol the ordered integral is strictly positive, since the weight product is nonnegative and positive on a set of positive four-dimensional measure. This proves strict negativity for every \(T>0\), regardless of \(D\). More generally, the sign is not fixed for signed weights.

**3. Exact finite-duration optimum and cumulant recursion.** The previously known mean-work-minimizing open-loop displacement from \(0\) to \(\ell\ne0\) has
\[
c=\frac{\ell}{T+2/k},\qquad
\lambda(0^+)=\frac ck,\quad
\lambda(t)=c(t+1/k)\ (0<t<T),\quad
\lambda(T)=\ell,
\]
with a final jump of size \(c/k\). For this protocol \(g(s)=c w(s)\), where
\[
w(s)=\begin{cases}2e^{ks},&s<0,\\1,&0\le s\le T.\end{cases}
\]
Define
\[
J_{k,\gamma}(T)=\int_{s_1<s_2<s_3<s_4\le T}
\prod_{j=1}^4w(s_j)
 e^{-\gamma[(s_3-s_1)+(s_4-s_2)]}\,ds_1ds_2ds_3ds_4.
\]
Thus \(\kappa_4(W_T)=-48c^4\omega^4J_{k,\gamma}(T)\). The integral is exactly evaluable without simulation through four scalar ordinary differential equations. On \([0,T]\), solve
\[
A'=1-\gamma A,\qquad B'=A-2\gamma B,\qquad
C'=B-\gamma C,\qquad J'=C
\]
with initial values
\[
A(0)=\frac{2}{k+\gamma},\quad B(0)=\frac{2}{(k+\gamma)^2},\quad
C(0)=\frac{4}{(k+\gamma)^2(3k+\gamma)},\quad
J(0)=\frac{2}{k(k+\gamma)^2(3k+\gamma)}.
\]
These follow by successively integrating the ordered kernel on \(( -\infty,0)\). Then \(J(T)=J_{k,\gamma}(T)\). The system has a globally unique smooth solution and hence is a complete exact finite-time specification. All terms are positive for \(T>0\).

The variance is
\[
\operatorname{Var}(W_T)=c^2\left[2D\left(T+\frac2k\right)+\omega^2Q_{k,\gamma}(T)\right],
\]
where
\[
Q_{k,\gamma}(T)=\frac{2T}{\gamma}+
\frac{4}{k(k+\gamma)}+
\frac{2(\gamma-k)}{\gamma^2(k+\gamma)}(1-e^{-\gamma T}).
\]
The formula follows by integrating the Gaussian white-noise covariance and \(\mathbb E[\sigma_s\sigma_t]=e^{-\gamma|s-t|}\). It is consistent with the previously published optimal-protocol variance.

From the constant-coefficient cascade, \(C(t)\to1/(2\gamma^3)\) exponentially and hence \(J_{k,\gamma}(T)=T/(2\gamma^3)+O(1)\). Moreover \(Q_{k,\gamma}(T)=2T/\gamma+O(1)\). Substitution into the exact cumulant and variance formulas, with \(D+\omega^2/\gamma>0\), yields the stated \(T^{-1}\) excess-kurtosis law with an \(O(T^{-2})\) remainder. Notice that \(c\) cancels, so the leading coefficient depends on neither \(k\) nor \(\ell\).

**4. Cyclic-reversal sign change.** Take a protocol that jumps from \(0\) to \(a\ne0\) at \(t=0\), holds that center until \(t=\delta>0\), then jumps back to \(0\). Its random work is \(-ka(Y_0-Y_\delta)\). For the propulsion component, \(k\int_{-\infty}^t e^{-k(t-s)}\sigma_sds\to\sigma_t\) in \(L^4\) as \(k\to\infty\), since the telegraph process is almost surely continuous at any fixed deterministic time. Independent thermal Gaussian contributions have no fourth cumulant. The limits are therefore
\[
\lim_{k\to\infty}\frac{\kappa_4(W)}{a^4\omega^4}
=\kappa_4(\sigma_0-\sigma_\delta)
=4(1-e^{-\gamma\delta})(3e^{-\gamma\delta}-1).
\]
Indeed \(\sigma_0-\sigma_\delta\) equals \(0\) unless an odd number of flips occurs, in which case it equals \(\pm2\) symmetrically; the odd-flip probability is \((1-e^{-\gamma\delta})/2\). This proves that for every fixed \(0<\delta<(\log3)/\gamma\), **all sufficiently large but finite** \(k\) give \(\kappa_4(W)>0\). For fixed \(\delta>(\log3)/\gamma\), the same large-\(k\) limit is strictly negative. At equality the limiting cumulant is zero; its sign at finite \(k\) is not asserted.

**5. Gaussian active comparator.** Replace the propulsion \(\omega\sigma_t\) by a centered stationary Gaussian Ornstein–Uhlenbeck propulsion with covariance \(\omega^2 e^{-\gamma|t-s|}\). Linear filtering preserves Gaussianity. Its mean work and variance equal those of the telegraph model for every prescribed protocol, but its fourth work cumulant is exactly zero. This conclusion is not a statement about other nonlinear observables or feedback protocols.

## Verification
A standalone Python checker `checker.py` reproduces the finite-duration cumulant via two independent methods: (i) the ordered four-time cumulant cascade and (ii) a separate two-state Markov moment hierarchy through fourth order. It also checks the exact variance, large-duration standardized coefficient, and the cyclic-reversal sign and limiting formula. Run `python checker.py` with Python 3, NumPy, and SciPy. The executable completed **171 deterministic checks**, including the finite-stiffness cyclic example \(k=20\), \(\gamma=1\), \(\delta=0.5\), whose normalized fourth cumulant is approximately \(1.027222619811016>0\). All continuum-wide conclusions follow analytically above; finite checks are corroboration, not proofs of infinite parameter ranges.

## Relationship to prior work
Garcia-Millan, Schüttler, Cates, and Loos (arXiv:2407.18542, first submitted 2024-07-26) introduced the active harmonic-trap displacement/control setting and discussed optimal open-loop control and increased work variance. Their subsequent expanded treatment (arXiv:2501.18613, Sec. III, especially Eqs. 29–36) supplies the optimal displacement protocol and exact variance for the run-and-tumble and Gaussian active models, and notes that higher moments distinguish them. Those **first- and second-order statements and the protocol itself are prior results**. The present finding is the strict fourth-cumulant sign theorem for all monotone protocols, its exact optimal-protocol formula and asymptotic coefficient, and the opposite sign possible in cyclic reversal. General fourth-order telegraph correlators are also established tools; the novelty claim is the physically specified work-functional consequences and the sign boundary between protocol classes, not the Markov correlation identity alone. Baldovin and Manacorda (arXiv:2602.04560) consider control of trapping stiffness and tumbling rate, rather than translated-trap work fourth cumulants. Related general theories of Markov-additive functionals could contain implicit equivalents; exhaustive publication priority is not claimed.

## Limitations
The theory assumes stationary symmetric two-state propulsion, fixed \(k\), fixed \(\gamma\), a harmonic trap, independent Gaussian thermal noise, and prescribed (open-loop) protocols of bounded variation. The universal negative sign applies only to nonconstant monotone protocols. The cyclic statement proves existence of positive signs for sufficiently large finite stiffness for short fixed inter-jump delays, **not** a complete finite-stiffness sign phase diagram. The optimal-transport asymptotic keeps \(k,D,\omega,\gamma\) fixed as \(T\to\infty\); the underlying work variance decays during slow transport, and its normalized excess kurtosis is an asymptotic diagnostic. No finite-sample inference guarantee or independent scholarly validation is asserted.

## References
1. R. Garcia-Millan, J. Schüttler, M. E. Cates, and S. A. M. Loos, *Optimal closed-loop control of active particles and a minimal information engine*, arXiv:2407.18542 (first public version 2024-07-26), https://arxiv.org/abs/2407.18542 .
2. J. Schüttler, R. Garcia-Millan, M. E. Cates, and S. A. M. Loos, *Active particles in moving traps: minimum work protocols and information efficiency of work extraction*, arXiv:2501.18613, especially Sec. III, https://arxiv.org/html/2501.18613 .
3. M. Baldovin and A. Manacorda, *Control protocols for harmonically confined run-and-tumble particles*, arXiv:2602.04560, https://arxiv.org/abs/2602.04560 .
