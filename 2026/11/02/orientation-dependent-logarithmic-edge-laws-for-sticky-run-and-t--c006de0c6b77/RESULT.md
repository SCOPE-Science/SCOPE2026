# Orientation-dependent logarithmic edge laws for sticky run-and-tumble occupation under resetting

## Finding
For the nonabsorbing sticky-wall run-and-tumble particle described below, the fraction \(U_T\) of time adsorbed at the wall obeys a full speed-\(T\) large-deviation principle. Its exact rate function is determined by an explicit inverse transform; in particular, the two endpoints have unequal singularities, and the right endpoint has a subleading correction that distinguishes the initial propulsion orientation.

Put \(\tau=x_0/v\), let \(\sigma\in\{-,+\}\) denote the fixed bulk-reset orientation (negative means toward the wall), and define for \(z>0\)
\[
w(z)=\sqrt{z(z+2\alpha)},\quad h_-(z)=e^{-\tau w(z)},\quad h_+(z)=\frac{\alpha e^{-\tau w(z)}}{z+\alpha+w(z)}.\]
For \(s\geq0\), and by analytic continuation to the real domain specified below, the Laplace transform of an entire resetting bulk excursion from desorption until next adsorption is
\[
\Phi_\sigma(s)=\frac{(s+r)h_\sigma(s+r)}{s+r h_\sigma(s+r)}.
\]
There is a unique \(z_\sigma\in(0,r)\) satisfying \(z_\sigma=r[1-h_\sigma(z_\sigma)]\). Define
\[
q_\sigma=r-z_\sigma,\qquad R_\sigma=\frac{z_\sigma h_\sigma(z_\sigma)}{1+r h'_\sigma(z_\sigma)}>0.
\]
The transform \(\Phi_\sigma\) is finite and strictly decreasing on \((-q_\sigma,\infty)\) and diverges as \(R_\sigma/(s+q_\sigma)\) at its left boundary. For every \(k\in\mathbb R\), there is a unique \(\psi_\sigma(k)>-q_\sigma\) such that
\[
k=\psi_\sigma(k)+\gamma[1-\Phi_\sigma(\psi_\sigma(k))].\]
This is the exact scaled cumulant generating function for adsorption time. The good rate function is
\[
I_\sigma(u)=\sup_{k\in\mathbb R}\{ku-\psi_\sigma(k)\},\qquad 0\le u\le1,
\]
and \(I_\sigma(u)=+\infty\) outside \([0,1]\). For a practical interior parameterization, write
\[
u(\lambda)=\frac1{1-\gamma\Phi'_\sigma(\lambda)},\quad I_\sigma(u(\lambda))=u(\lambda)\{\lambda+\gamma[1-\Phi_\sigma(\lambda)]\}-\lambda,\quad \lambda>-q_\sigma.\]
It is strictly convex in the interior and attains its unique zero at
\[
u_\sigma^*=\frac1{1+\gamma(1-h_\sigma(r))/(r h_\sigma(r))}.\]
Its endpoint values and sharp interior-edge asymptotics are
\[
I_\sigma(0)=q_\sigma,\qquad I_\sigma(1)=\gamma,\qquad
I_\sigma(\delta)=q_\sigma-2\sqrt{\gamma R_\sigma\delta}+O(\delta),
\]
and, as \(\delta\downarrow0\),
\[
I_\sigma(1-\delta)=\gamma-\frac{\delta}{\tau}\log\frac1\delta
+\frac{m_\sigma\delta}{\tau}\log\log\frac1\delta+O(\delta),
\qquad m_-=0,\quad m_+=1.
\]
In particular, the logarithmic correction at almost-complete adsorption is common to both reset orientations, but the log-log coefficient is zero for propulsion toward the wall and strictly positive for propulsion away from it.

## Assumptions and scope
Fix \(v>0\), tumbling rate \(\alpha>0\), bulk-reset rate \(r>0\), desorption rate \(\gamma>0\), and reset position \(x_0>0\). During a bulk episode the particle moves on \((0,\infty)\) at velocity \(\pm v\); independent exponential(\(\alpha\)) tumbles reverse the velocity, and independent exponential(\(r\)) resetting events restore the *entire* bulk state to \((x_0,\sigma)\). The first crossing of zero is adsorption. The particle then stays fixed at the boundary for an independent exponential(\(\gamma\)) bound episode, with no absorption. Desorption restarts its position and velocity at \((x_0,\sigma)\). This is the desorption-induced resetting protocol, and resetting clocks are refreshed at every renewal. All cycles are independent and identically distributed. Let \(U_T=T^{-1}\int_0^T\mathbf1_{\{\text{adsorbed}\}}(t)\,dt\), starting in a new bulk episode or a new bound episode. The asymptotic rate is independent of this initial choice.

No diffusion is superimposed on the ballistic motion, and no reset is applied during adsorption. All asymptotic limits in this finding keep the five physical parameters fixed while \(T\to\infty\) or \(\delta\downarrow0\), as appropriate.

## Proof
**1. Unreset bulk hitting transform.** Denote by \(f_\pm(x;z)\) the Laplace transform of the time to first hit zero without resetting, from position \(x\) and velocity \(\pm v\). The backward equations are \(v f_+'+\alpha(f_--f_+)=z f_+\) and \(-v f_-'+\alpha(f_+-f_-)=z f_-\). Their unique bounded solution obeying \(f_-(0;z)=1\) decays as \(e^{-xw(z)/v}\), where \(w(z)=\sqrt{z(z+2\alpha)}\). Evaluating at \(x_0\) gives exactly \(h_\pm(z)\) above. As \(z\downarrow0\), \(1-h_\pm(z)\) has a positive leading term proportional to \(\sqrt z\), so the unreset half-line adsorption time has infinite mean for either initial orientation.

**2. Resetting excursion and its spectral edge.** For the complete bulk adsorption time \(H\), conditioning on the first resetting event gives \(\Phi_\sigma(s)=(s+r)h_\sigma(s+r)/(s+r h_\sigma(s+r))\). To locate its first real singularity, use \((1-h_\sigma(z))/z=\int_0^\infty e^{-zt}\Pr(H_0>t)\,dt\), where \(H_0\) is the unreset adsorption time. This expression is continuous and strictly decreasing from infinity at zero to \((1-h_\sigma(r))/r<1/r\) at \(z=r\). It therefore equals \(1/r\) at exactly one \(z_\sigma\in(0,r)\). The derivative of the crossing is strictly negative, so \(1+r h'_\sigma(z_\sigma)>0\). The denominator of \(\Phi_\sigma\) has a simple zero at \(s=-q_\sigma\) with positive residue \(R_\sigma\), exactly as stated. To verify that this pole genuinely controls the excursion tail, use the survival-renewal equation
\[
\Pr(H>t)=e^{-rt}\Pr(H_0>t)+r\int_0^t e^{-ra}\Pr(H_0>a)\Pr(H>t-a)\,da.
\]
Multiplication by \(e^{q_\sigma t}\) turns the convolution kernel into the nonlattice probability measure \(r e^{-z_\sigma a}\Pr(H_0>a)\,da\), with finite mean. Its forcing \(e^{-z_\sigma t}\Pr(H_0>t)\) is directly Riemann integrable. The key renewal theorem gives \(\Pr(H>t)\sim(R_\sigma/q_\sigma)e^{-q_\sigma t}\). In particular \(\Phi_\sigma(s)<\infty\) exactly for real \(s>-q_\sigma\), and \(\Phi'_\sigma(s)<0\), \(\Phi''_\sigma(s)>0\) on this domain.

**3. Bound-time cumulants and full large deviations.** Consecutive cycles have a bulk duration \(H\) and an independent boundary duration \(B\sim\mathrm{Exp}(\gamma)\). The reward in each cycle is \(B\). The tilted cycle kernel has transform
\[
\mathbb E[e^{kB-\lambda(H+B)}]
=\Phi_\sigma(\lambda)\frac\gamma{\gamma+\lambda-k}.
\]
It equals one precisely for \(k=\lambda+\gamma[1-\Phi_\sigma(\lambda)]\). The right side is strictly increasing in \(\lambda\), with limits negative infinity and positive infinity at the two ends of \((-q_\sigma,\infty)\); hence its inverse \(\psi_\sigma\) exists for every real \(k\). Exponentially tilting the alternating-renewal equation by the unique root gives a positive, nonlattice probability renewal kernel. The incomplete-cycle forcing is integrable because \(\lambda>-q_\sigma\) and \(\gamma+\lambda-k=\gamma\Phi_\sigma(\lambda)>0\). The renewal theorem gives \(\lim_{T\to\infty}T^{-1}\log\mathbb E[e^{kTU_T}]=\psi_\sigma(k)\). The same exponent results when the initial episode is bulk rather than bound.

Implicit differentiation shows
\[
\psi'_\sigma(k)=\frac1{1-\gamma\Phi'_\sigma(\psi_\sigma(k))},\qquad
\psi''_\sigma(k)=\frac{\gamma\Phi''_\sigma(\psi_\sigma(k))}{[1-\gamma\Phi'_\sigma(\psi_\sigma(k))]^3}>0.
\]
Thus the cumulant limit is everywhere finite and differentiable. Since \(0\le U_T\le1\) is exponentially tight, the Gärtner–Ellis theorem provides the full good LDP on \([0,1]\). All interior slopes are exposed; the neighborhood lower bounds at endpoints follow by approximating from interior fractions. The inverse parameterization and strict convexity follow from the derivatives. At \(k=0\), the solution is \(\lambda=0\), giving the stated law-of-large-numbers occupation fraction. Taking \(\lambda\downarrow-q_\sigma\) and \(\lambda\to\infty\) gives endpoint rates \(q_\sigma\) and \(\gamma\).

**4. Left edge.** With \(\epsilon=\lambda+q_\sigma\downarrow0\), \(\Phi_\sigma(\lambda)=R_\sigma/\epsilon+O(1)\) and \(\Phi'_\sigma(\lambda)=-R_\sigma/\epsilon^2+O(1)\). Hence \(u(\lambda)=\epsilon^2/(\gamma R_\sigma)[1+O(\epsilon)]\). Substitution into the rate parameterization gives \(I_\sigma(u)=q_\sigma-2\sqrt{\gamma R_\sigma u}+O(u)\).

**5. Right edge and directional log-log law.** The shortest possible return from position \(x_0\) takes time \(\tau=x_0/v\). For initial negative velocity, the ballistic no-event path has an atom at \(\tau\) of weight \(e^{-(r+\alpha)\tau}\). For initial positive velocity, an immediate tumble is necessary, and the first-return density instead approaches \((\alpha/2)e^{-(r+\alpha)\tau}\) as the return time decreases to \(\tau\). Equivalently, the exact formulas give the uniform large-positive-\(\lambda\) expansions
\[
\Phi_\sigma(\lambda)=C_\sigma\lambda^{-m_\sigma}e^{-\tau\lambda}[1+O(\lambda^{-1})],\quad
C_-=e^{-(r+\alpha)\tau},\quad C_+=(\alpha/2)e^{-(r+\alpha)\tau},
\]
with \(m_-=0\), \(m_+=1\), and \(-\Phi'_\sigma(\lambda)=\tau\Phi_\sigma(\lambda)[1+O(\lambda^{-1})]\). Put \(\delta=1-u(\lambda)\). Then \(\delta=\gamma\tau C_\sigma\lambda^{-m_\sigma}e^{-\tau\lambda}[1+o(1)]\), so
\[
\lambda=\tau^{-1}\Bigl[\log(1/\delta)-m_\sigma\log\log(1/\delta)+O(1)\Bigr].
\]
Finally the exact rate identity gives \(\gamma-I_\sigma(1-\delta)=\delta\lambda+O(\delta)\), which proves the displayed log and log-log coefficients. The leading endpoint cost \(\gamma\) is independent of orientation, while the logarithmic correction of its rare-event approach remembers whether a shortest return carries an atom or only a near-minimal density.

## Verification
The accompanying standalone `verify_sticky_occupation.py` requires Python 3 and no external libraries. Run `python3 verify_sticky_occupation.py`. For \(v=\alpha=r=\gamma=x_0=1\), it tests transform normalization, residue/root relationships, mean identity, both edge expansions, positivity, and event-driven direct trajectories with no time discretization. Its completed run passed 164 finite assertions using 120,000 sampled bulk episodes in total. The sampled mean bulk adsorption times were approximately 4.65547 (toward wall) and 20.02912 (away); exact analytic values are approximately 4.65223 and 20.09442. The checks are supplementary; the stated infinite-time and all-parameter conclusions follow from the proof above.

## Relationship to prior work
Bressloff and Linn, arXiv:2602.02446 (publicly submitted February 2, 2026), introduce this stochastic-resetting sticky-boundary RTP and both desorption protocols. Their nonabsorbing stationary-state calculation includes the *mean* bound time fraction and bulk hitting-renewal quantities; those foundational facts are prior work, not claimed as new. Bressloff, arXiv:2009.01968 (2020), develops occupation-time large deviations for a resetting RTP on the whole line, but its positive-halfline occupation observable is different from *time physically adsorbed at a wall*. Mukherjee, Le Doussal and Smith, arXiv:2405.07032 (2024), study RTP local time at a point and spatial finite-interval occupation; these are neither reset-assisted nor time physically immobilized at a sticky wall. Meylahn, Sabhapandit and Touchette, arXiv:1510.02431 (2015), give a general renewal approach to resetting large deviations; the use of renewal tilting and Gärtner–Ellis is standard groundwork. Monthus, arXiv:2009.12287 (2020), likewise treats general resetting large-deviation structures. The specific all-parameter sticky-wall bound-occupation rate and, especially, its orientation-dependent log-log edge coefficient are the assessed contributions; no blanket originality claim is made beyond the sources inspected.

## Limitations
This result treats only nonabsorbing walls and *desorption-induced resetting* to a positive interior position. It does not extend the same formulas to wall-origin desorption, nonexponential waiting, asymmetric velocity switching, permanent target absorption, spatial diffusion, or finite-time occupation densities. The large-deviation principle controls exponential rates as total observation time tends to infinity; it does not state prefactors for finite-time probabilities. The endpoint asymptotics concern the mathematical rate function as its argument approaches zero or one; exact zero/one events at a fixed observation horizon may depend on initialization. Broader existing Markov-renewal results might imply some general structural aspects, and no independent priority audit is asserted.

## References
- P. C. Bressloff and S. Linn, *Renewal theory for a run-and-tumble particle with stochastic resetting and a sticky boundary*, arXiv:2602.02446 (first public February 2, 2026), https://arxiv.org/abs/2602.02446.
- P. C. Bressloff, *Occupation time of a run-and-tumble particle with resetting*, arXiv:2009.01968 (2020), https://arxiv.org/abs/2009.01968.
- S. Mukherjee, P. Le Doussal and N. R. Smith, *Large deviations in statistics of the local time and occupation time for a run and tumble particle*, arXiv:2405.07032 (2024), https://arxiv.org/abs/2405.07032.
- J. M. Meylahn, S. Sabhapandit and H. Touchette, *Large deviations for Markov processes with resetting*, arXiv:1510.02431 (2015), https://arxiv.org/abs/1510.02431.
- C. Monthus, *Large deviations for Markov processes with stochastic resetting: analysis via the empirical density and flows or via excursions between resets*, arXiv:2009.12287 (2020), https://arxiv.org/abs/2009.12287.
