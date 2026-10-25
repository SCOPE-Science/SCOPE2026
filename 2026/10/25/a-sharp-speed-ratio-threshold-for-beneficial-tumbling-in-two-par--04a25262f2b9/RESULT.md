# A sharp speed-ratio threshold for beneficial tumbling in two-particle ring encounters

## Finding

For two independent persistent walkers on a continuous ring, the sign of the response of the expected first collision time to weak direction-reversal noise changes at the exact velocity ratio \(v_2/v_1=1/\sqrt{5}\). Unlike the equal-speed problem, ballistic first encounters have finite mean for every strict speed mismatch. Let \(M(\alpha)\) denote the mean when both walkers reverse directions independently at rate \(\alpha\). The expansion is

\[
M(\alpha)=\frac{\ell v_1}{2(v_1^2-v_2^2)}+\frac{\ell^2(v_1^2-5v_2^2)}{6(v_1^2-v_2^2)^2}\alpha+\frac{2\ell^3v_1v_2^2}{3(v_1^2-v_2^2)^3}\alpha^2+O(\alpha^3).
\]

Therefore weak tumbling decreases the mean exactly if \(1/\sqrt{5}<v_2/v_1<1\), increases it if \(0<v_2/v_1<1/\sqrt{5}\), and has zero first derivative but a strictly positive second-order coefficient at the threshold:

\[
M(\alpha)-M(0)=\frac{25\ell^3}{96v_1^3}\alpha^2+O(\alpha^3),\qquad v_2/v_1=1/\sqrt{5}.
\]

At every strict speed mismatch, \(M(\alpha)\to\infty\) as \(\alpha\to\infty\). Hence when \(v_2/v_1>1/\sqrt{5}\), the encounter time has at least one global minimizer at a strictly positive finite rate. No uniqueness of that minimizer and no global ballistic-optimality claim for lower speed ratios is made.

## Assumptions and scope

Fix a ring of circumference \(\ell>0\), speeds \(v_1>v_2>0\), and rate \(\alpha\ge0\). Walker \(i\) has position \(X_i\in\mathbb R/\ell\mathbb Z\), and an independent sign \(\sigma_i\in\{-1,+1\}\). Between reversals, \(\dot X_i=v_i\sigma_i\); each sign reverses at the times of an independent rate-\(\alpha\) Poisson process. Initially positions are independent uniform and signs are independent uniform. The stopping time is \(T_\alpha=\inf\{t\ge0:X_1(t)=X_2(t)\}\), with immediate absorption at first contact. There is no hard-core interaction or scattering before contact.

For \(\alpha=0\), all four possible relative velocities are nonzero because \(v_1>v_2\), so contact occurs on the ring within \(\ell/(v_1-v_2)\). For each fixed \(\alpha>0\), the hitting time is finite in expectation: within a bounded interval and with a uniform positive probability, prescribed independent reversals produce relative velocity \(v_1+v_2\) for a long enough uninterrupted run to cover the entire circle. Applying this probability successively yields a geometric tail bound.

## Proof

Put \(y=(X_1-X_2)\bmod\ell\in(0,\ell)\), and order the sign pairs as \((+,+),(+,-),(-,+),(-,-)\). Their relative velocities are

\[
w=(v_1-v_2,\ v_1+v_2,\ -v_1-v_2,\ -v_1+v_2).
\]

Let \(f_s(y,\alpha)\) be the conditional mean first encounter time in sign state \(s\), and define \((Qh)_s=\sum_{t:\text{one sign flip from }s}(h_t-h_s)\). The backward equations are the coupled transport equations

\[
w_s\partial_y f_s+\alpha(Qf)_s=-1,
\]

with *incoming-to-absorption* conditions \(f_s(\ell,\alpha)=0\) when \(w_s>0\) and \(f_s(0,\alpha)=0\) when \(w_s<0\). There are two conditions at each endpoint. They apply to an open interval in relative position; imposing four simultaneous zero conditions at a single coincident position would be incorrect.

At \(\alpha=0\), the transport equations decouple. Their unique solutions are \(f_s(y,0)=(\ell-y)/w_s\) for \(w_s>0\), and \(f_s(y,0)=-y/w_s\) for \(w_s<0\). The boundary map for the inhomogeneous constant-coefficient system is invertible at \(\alpha=0\); therefore ordinary analytic dependence of linear ODE solutions and the inverse function theorem imply analyticity of each \(f_s(y,\alpha)\) near zero. Write \(f_s=\sum_{k\ge0}\alpha^k f_{k,s}\). Matching orders gives

\[
w_s f'_{0,s}=-1,\qquad w_s f'_{k,s}=-(Qf_{k-1})_s\quad(k\ge1),
\]

with the same homogeneous endpoint condition at each order \(k\ge1\). Thus every coefficient is obtained by explicit polynomial integration; for positive \(w_s\),

\[
f_{k,s}(y)=\int_y^\ell\frac{(Qf_{k-1})_s(z)}{w_s}\,dz,
\]

and for negative \(w_s\),

\[
f_{k,s}(y)=-\int_0^y\frac{(Qf_{k-1})_s(z)}{w_s}\,dz.
\]

Average these recursions over the four initial signs and over uniform \(y\). Rescale by setting \(r=v_2/v_1\in(0,1)\). Direct integration gives the first three coefficients in units of \(v_1\):

\[
\frac{\ell}{2v_1(1-r^2)},\quad
\frac{\ell^2(1-5r^2)}{6v_1^2(1-r^2)^2},\quad
\frac{2\ell^3r^2}{3v_1^3(1-r^2)^3}.
\]

The standalone verification program independently reconstructs all four polynomial functions at each order, substitutes them into every backward equation and endpoint condition, and integrates them symbolically. The first-order coefficient changes sign exactly at \(r=1/\sqrt{5}\). At equality, substitution into the second-order coefficient gives \(25\ell^3/(96v_1^3)>0\).

To establish the strong-reversal limit, for each velocity sign process define the compensated-jump martingale \(N_i(t)=\sigma_i(t)-\sigma_i(0)+2\alpha\int_0^t\sigma_i(s)\,ds\). Its predictable quadratic variation is \(4\alpha t\). Doob's inequality then gives, for every fixed \(t>0\), a bound of order \(t/\alpha+\alpha^{-2}\) on \(\mathbb E\sup_{0\le s\le t}|\int_0^s\sigma_i(u)\,du|^2\). For any \(\delta\in(0,\ell/2)\), initial separations outside \((\delta,\ell-\delta)\) have probability \(2\delta/\ell\); for separations inside that interval, collision by fixed time requires the magnitude of unwrapped relative displacement to reach at least \(\delta\). Markov's inequality yields

\[
\limsup_{\alpha\to\infty}\Pr(T_\alpha\le t)\le2\delta/\ell.
\]

Sending \(\delta\downarrow0\) proves \(\Pr(T_\alpha\le t)\to0\) for every fixed finite \(t\). Hence \(M(\alpha)\to\infty\). Together with continuity of the finite mean and the strictly negative derivative above threshold, this proves existence of a finite positive global minimizer there.

## Verification

The standalone `verify.py` evaluates the polynomial coefficient recursion with exact symbolic algebra, checks four transport equations and the mixed absorbing boundary conditions at orders zero, one and two, and reproduces all three averaged coefficients. It then solves the independent four-state matrix-exponential boundary-value problem for six distinct velocity ratios and compares with the second-order expansion; three independent seeded event-driven Monte Carlo tests compare empirical means against the numerical boundary-value solution. All tests passed when executed against the included source file. These finite and symbolic checks support but do not replace the analytical argument for the strong-reversal limit and optimum existence.

## Relationship to prior work

Pogorui (2012) studied meeting times of equal-speed telegraph particles on the infinite line and stated primary MSC 82C70. Soto and Golestanian (first public 2013-06-03, arXiv:1306.0481) investigated persistent excluded-volume walkers and motivate the physical interaction model. Cheliotis, Kontoyiannis, Loulakis and Toumpis (arXiv:1808.03830, particularly Lemma 4.5 and its generator potential in Section 4.2) obtained the exact conditional first-meeting mean for **two equal-speed** telegraph walkers on a ring, in studying message transmission. That result **already covers** the equal-speed conditional and uniformly averaged mean and any elementary optimizer of the latter; these are not claimed here. The new assertion instead concerns a *strictly unequal-speed* family, its ballistic endpoint derivative, the exact threshold \(1/\sqrt{5}\), and the quadratic threshold boundary. Its four nonzero transport velocities make the mixed boundary problem different from the equal-speed model's zero-velocity states. Le Doussal, Majumdar and Schehr (arXiv:1902.06176) treat noncrossing equal-speed walkers on an unbounded line. Slowman, Evans and Blythe (arXiv:1705.04812) treat a hard-core lattice-ring stationary law, not this initial-encounter question.

## Limitations

The rates are equal across particles; speeds are strictly positive and unequal; orientation and position laws are uniform and independent. The result is a **local weak-reversal threshold**, not a classification of all global minimizers. It does not prove ballistic global optimality below threshold or uniqueness of the positive minimizer above it. The equal-speed limit is singular and must not be obtained by substituting \(v_2=v_1\) in the expansion. Alternative collision reactions, correlated reversals, nonlinear drifts, and non-circular geometries are outside the theorem.

## References

1. A. A. Pogorui, *System of interacting particles with Markovian switching*, Theory of Stochastic Processes 18 (34), no. 2 (2012), 83–95. https://tsp.imath.kiev.ua/files/1820/art1820_09.pdf (Section 2, infinite-line first-collision law).
2. R. Soto and R. Golestanian, *Run-and-tumble in a crowded environment: persistent exclusion process for swimmers*, arXiv:1306.0481, first posted 2013-06-03; Physical Review E 89, 012706 (2014). https://arxiv.org/abs/1306.0481.
3. D. Cheliotis, I. Kontoyiannis, M. Loulakis, S. Toumpis, *A Simple Network of Nodes Moving on the Circle*, arXiv:1808.03830, Random Structures & Algorithms 57 (2020), 317–338. https://arxiv.org/pdf/1808.03830 (Section 4.2, Lemma 4.5 and Eq. (8)).
4. P. Le Doussal, S. N. Majumdar, G. Schehr, *Noncrossing run-and-tumble particles on a line*, Physical Review E 100 (2019), 012113. https://arxiv.org/pdf/1902.06176.
5. A. B. Slowman, M. R. Evans, R. A. Blythe, *Exact Solution of Two Interacting Run-and-Tumble Random Walkers with Finite Tumble Duration*, Journal of Physics A 50 (2017). https://arxiv.org/pdf/1705.04812.
