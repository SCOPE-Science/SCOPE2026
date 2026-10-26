# Fourth-cumulant neutrality conceals a sixth-cumulant sign reversal in intermittent active motion

## Finding

A three-velocity stop-and-go particle can be tuned to have zero **long-time fourth-cumulant growth**, but this does not remove its higher non-Gaussian signatures. On the unique tuning surface, the sixth displacement cumulant has a strictly negative long-time growth rate, while the eighth has a strictly positive growth rate. Above an explicit reorientation-rate threshold, the sixth cumulant instead starts positive at short times and therefore must change sign at least once at a finite observation time.

Precisely, for positive active-to-rest rate \(a\), rest-to-active rate \(b\), propulsion speed \(v\), nonnegative direction-flip rate \(h\), and independent translational Brownian diffusivity \(D\geq0\), the unique fourth-cumulant-neutral rate is
\[
 b=b_*(a,h)=\frac{\sqrt{5a^2+8ah}-a}{2}.
\]
Let \(L=2a+b+2h\). On this surface,
\[
\lim_{T\to\infty}\frac{\kappa_4(X_T)}T=0,\qquad
\lim_{T\to\infty}\frac{\kappa_6(X_T)}T=-\frac{720v^6}{bL^4}<0,\qquad
\lim_{T\to\infty}\frac{\kappa_8(X_T)}T=\frac{40320v^8}{b^2L^5}>0.
\]
If additionally
\[
 \frac ha>\eta_0:=\frac{29\sqrt{105}-167}{1024}=0.127110910364\ldots,
\]
then \(\kappa_6(X_T)>0\) for all sufficiently small \(T>0\), whereas \(\kappa_6(X_T)<0\) for all sufficiently large \(T\). Consequently, continuity forces at least one strictly positive time \(T_*\) satisfying \(\kappa_6(X_{T_*})=0\). The theorem does not assert uniqueness of that zero.

## Assumptions and scope

The particle moves on the real line. Let \(J_t\) be the time-homogeneous continuous-time Markov chain with states \(+, -, 0\). In state \(+\) or \(-\), the particle has deterministic velocity \(+v\) or \(-v\). Each moving state enters immobile state \(0\) at rate \(a>0\). Direct sign reversals \(+\leftrightarrow-\) occur independently at rate \(h\geq0\) in each direction. From state \(0\), departures occur at total rate \(b>0\), choosing \(+\) or \(-\) with equal probability. This chain is irreducible even at \(h=0\). It is initialized in its unique stationary distribution,
\[
 \Pr(J_0=+)=\Pr(J_0=-)=\frac{b}{2(a+b)},\qquad
 \Pr(J_0=0)=\frac{a}{a+b}.
\]
With an independent standard Brownian motion \(W\), define for every \(T\geq0\)
\[
 X_T=v\int_0^T\bigl(\mathbf1_{J_t=+}-\mathbf1_{J_t=-}\bigr)\,dt+\sqrt{2D}\,W_T.
\]
Cumulants \(\kappa_j\) are the coefficients defined by the logarithm of the moment-generating function: \(\log\mathbb E[e^{qX_T}]=\sum_{j\geq1}\kappa_j(X_T)q^j/j!\) near \(q=0\). All parameters are fixed as \(T\to\infty\). The rates \(a,b\) have inverse-time units, while \(v\) has length/time units.

## Proof

**1. Tilted spectral polynomial.** Order states as \(+, -, 0\). The forward generator and its displacement tilt are
\[
 Q=\begin{pmatrix}-a-h&h&b/2\\h&-a-h&b/2\\a&a&-b\end{pmatrix},\qquad
 K(q)=Q+vq\,\operatorname{diag}(1,-1,0).
\]
Writing \(c=a+2h\), the characteristic equation for an eigenvalue \(\lambda\) of \(K(q)\) is exactly
\[
 \lambda(\lambda+a+b)(\lambda+c)-(\lambda+b)v^2q^2=0. \tag{1}
\]
The chain is finite and irreducible, so at \(q=0\) its zero eigenvalue is simple, while its other eigenvalues have strictly negative real parts. Analytic perturbation of a simple eigenvalue and the finite-state Feynman–Kac formula imply, locally uniformly for \(q\) near zero,
\[
 \log\mathbb E[e^{qX_T}]=T\bigl(Dq^2+\lambda(q)\bigr)+O(1)
\]
with analytic remainder and its derivatives bounded as \(T\to\infty\); \(\lambda(0)=0\) is the branch of (1) continuous at zero. The Gaussian term contributes to the second cumulant only. Thus every fixed even cumulant growth coefficient is the corresponding derivative of \(\lambda(q)\), except the second, whose growth coefficient also includes \(2D\).

**2. Unique fourth-neutral surface.** Set \(s=v^2q^2\). By substituting \(\lambda=A s+B s^2+O(s^3)\) into (1) and matching successive powers,
\[
 A=\frac b{c(a+b)},\qquad
 B=\frac{b\,[ac-b(a+b)]}{c^3(a+b)^3}.
\]
Therefore \(\lim_{T\to\infty}\kappa_4(X_T)/T=24v^4B\). Vanishing is equivalent to \(b^2+ab-ac=0\). Since its left side is strictly increasing in \(b>0\), the unique positive solution is precisely \(b_*(a,h)\) above. In general, the long-time fourth-cumulant sign changes from positive to negative as \(b\) passes this value; that fourth-order antecedent is not the novelty claim here.

**3. The first two nonvanishing higher growth coefficients.** On the neutral surface, \(ac=b(a+b)\), hence \(c(a+b)=bL\), where \(L=a+b+c\). Equation (1) becomes
\[
 \lambda^3+L\lambda^2+bL\lambda-(\lambda+b)s=0. \tag{2}
\]
Substitute \(\lambda(s)=s/L+C_2s^2+C_3s^3+C_4s^4+O(s^5)\) into (2). Comparing coefficients of \(s^2,s^3,s^4\) gives successively
\[
 C_2=0,\qquad C_3=-\frac1{bL^4},\qquad C_4=\frac1{b^2L^5}.
\]
Multiplying by \(6!v^6\) and \(8!v^8\) establishes the stated strict negative sixth and strict positive eighth rates. Since \(v,b,L>0\), no further exceptional parameters exist on the surface. Moreover,
\[
 \lim_{T\to\infty}\frac{\kappa_2(X_T)}T=2D+\frac{2v^2}L>0.
\]
On the neutral surface, \(\kappa_4(X_T)=O(1)\), so standardized excess kurtosis decays at least as \(O(T^{-2})\), while the standardized sixth cumulant has an explicitly negative leading term of order \(T^{-2}\). Neither assertion says that finite-time fourth cumulants vanish.

**4. The short-time sixth cumulant.** The stationary instantaneous velocity has distribution \(+v\) and \(-v\), each with probability \(p/2\), and \(0\) with probability \(1-p\), where \(p=b/(a+b)\). Because the velocity is bounded and the chain has almost surely no jump at \(t=0\), its integrated velocity divided by \(T\) converges in every fixed moment to the instantaneous velocity. The independent Brownian term has zero cumulants of orders at least three. Consequently,
\[
 \lim_{T\downarrow0}\frac{\kappa_6(X_T)}{T^6}
 =v^6p(1-15p+30p^2). \tag{3}
\]
The larger root of the quadratic is \(p_+=(15+\sqrt{105})/60\). Along \(b=b_*(a,h)\), \(p\) increases strictly with \(h/a\), starting at \((3-\sqrt5)/2\) when \(h=0\). Solving \(p=p_+\) yields exactly \(h/a=\eta_0\). For \(h/a>\eta_0\), the right side of (3) is positive. The strictly negative sixth growth coefficient proved in step 3 makes the cumulant negative for sufficiently large time. Finite-time moment continuity (from matrix exponentials) and the intermediate value theorem give a positive zero, completing the proof.

## Verification

A standalone Python checker `checker.py` independently constructs the tilted three-state generator, verifies its characteristic polynomial and low-order series coefficient identities with exact symbolic algebra, and checks the critical-series coefficients through eighth displacement order. It also computes moments up to order eight by an **independent finite-time block-matrix differential system**, then compares cumulant growth with the analytic limits for four parameter sets, including nonzero independent Brownian diffusion. The checker passed 33 explicit symbolic/numerical assertions. For the illustrative parameters \(a=b=v=1\), \(h=1/2\), and \(D=0.2\), it locates a sixth-cumulant zero numerically near \(T=0.898364443\); this numerical root is illustration only. The assertion count and computations do not replace the analytic argument for all parameters.

## Relationship to prior work

Peruani and Chaudhuri introduced and analyzed related active stop-and-go processes and their velocity-correlation and diffusion properties (arXiv:2306.05647, first public 9 June 2023). Datta, Beta and Großmann studied intermittent self-propulsion with waiting-time-dependent transport characteristics (arXiv:2406.15277). Santra, Olsen and Gupta studied a directly relevant three-phase forward/backward/passive process and gave a general characteristic-function framework together with **explicit fourth-order** and lower position fluctuations, including an asymptotic kurtosis formula (arXiv:2408.16643, especially Section 4.2 and equation (54)). Their fourth-order calculation subsumes the fourth-cumulant-neutral tuning; it is used here as an acknowledged antecedent. The claim assessed here concerns the paired **sixth and eighth** rates on that tuning surface and the **sharp sufficient threshold for an unavoidable finite-time sixth-cumulant sign reversal**. The prior characteristic-function framework could be used to calculate these quantities, and independent priority scrutiny remains appropriate.

## Limitations

The theorem assumes exponential moving/resting times, fair independent direction on each departure, stationary initialization of the internal velocity chain, and a fixed nonzero propulsion speed. It does not establish uniqueness of the finite-time sixth-cumulant zero, nor characterize non-exponential waiting times or asymmetric directions. The spectral perturbation establishes long-time growth, not strict finite-time signs for the eighth cumulant. The fourth-neutral tuning and the general stochastic propagator are prior-work antecedents, not new contributions. Self-review does not constitute independent scholarly priority review.

## References

1. F. Peruani and D. Chaudhuri, *Active stop and go motion: a strategy to improve spatial exploration and survival*, arXiv:2306.05647, first posted 9 June 2023, https://arxiv.org/abs/2306.05647.
2. A. Datta, C. Beta and R. Großmann, *The random walk of intermittently self-propelled particles*, arXiv:2406.15277, first posted 21 June 2024, https://arxiv.org/abs/2406.15277.
3. I. Santra, K. S. Olsen and D. Gupta, *Dynamics of switching processes: general results and applications to intermittent active motion*, arXiv:2408.16643, first posted 29 August 2024; see the fourth-cumulant calculation in Section 4.2 and equation (54), https://arxiv.org/abs/2408.16643.
