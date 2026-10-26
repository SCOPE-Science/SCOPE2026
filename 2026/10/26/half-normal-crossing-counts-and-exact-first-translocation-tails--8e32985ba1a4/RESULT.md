# Half-normal crossing counts and exact first-translocation tails at a Markov-gated Brownian interface

## Finding

For a particle repeatedly encountering a dynamic interface, the **number of true side changes** is not determined by its position at the final time: a particle can cross back and forth. In the positive-offset renewal model of [1], the exact time-Laplace probability-generating function of the count, its universal fluctuation law, and the full first-translocation tail are as follows.

Let \(N_t\) count actual changes of half-line by time \(t\). For \(z\in[0,1]\) and \(s>0\), the column vector of transforms conditional on initial gate states \(O,C\) is

\[
\mathcal G_x(z,s)=\int_0^\infty e^{-st}\begin{pmatrix}\mathbb E_{x,O}z^{N_t}\\\mathbb E_{x,C}z^{N_t}\end{pmatrix}dt
=S_x(s)\mathbf 1+K_x(s)M(z)[I-K_\epsilon(s)M(z)]^{-1}S_\epsilon(s)\mathbf 1.
\]

All matrices and functions are explicit below. For independent standard normal \(Z\), both initial gate states satisfy

\[
\frac{N_t}{\sqrt t}\ \Longrightarrow\ \frac{p\sqrt{2D}}{2\epsilon}|Z|,
\qquad p=\frac{\beta}{\alpha+\beta}.
\]

Moreover, the convergence holds for **every positive real moment**, and in particular

\[
\lim_{t\to\infty}\frac{\mathbb E N_t}{\sqrt t}=\frac{p\sqrt D}{\epsilon\sqrt\pi},\qquad
\lim_{t\to\infty}\frac{\operatorname{Var}N_t}{t}=\frac{p^2D}{\epsilon^2}\left(\frac12-\frac1\pi\right),\qquad
\lim_{t\to\infty}\frac{\operatorname{Var}N_t}{(\mathbb E N_t)^2}=\frac\pi2-1.
\]

The first actual translocation \(T=\inf\{t:N_t\ge 1\}\) is finite almost surely but has infinite mean. Put

\[
\lambda=\alpha+\beta,\quad k=e^{-\epsilon\sqrt{\lambda/D}},\quad a=e^{-x\sqrt{\lambda/D}},\quad p=\beta/\lambda.
\]

For both initial gate states,

\[
\Pr_{x,i}(T>t)\sim\frac{C_i(x)}{\sqrt{\pi t}},\qquad
C_O(x)=\frac{x}{\sqrt D}+\frac{\epsilon[2-p-k-(1-p)a]}{p(1-k)\sqrt D},\qquad
C_C(x)=\frac{x}{\sqrt D}+\frac{\epsilon[2-p-k+pa]}{p(1-k)\sqrt D}.
\]

In particular \(C_C(x)-C_O(x)=\epsilon a/[p(1-k)\sqrt D]>0\): the initially closed gate has a strictly heavier first-translocation tail.

## Assumptions and scope

The particle starts at \(x>0\) on the positive half-line, with gate initially \(O\) or \(C\). Independently of the particle's Brownian noise, its single gate evolves continuously in time via the transition rates \(O\to C\) at \(\alpha>0\) and \(C\to O\) at \(\beta>0\). Brownian motion on each half-line has generator \(D\,\partial_{xx}\), with \(D>0\). At each hit of the interface at zero, if the gate is closed the new excursion starts on the same side at distance \(\epsilon>0\); if open, the next side is chosen independently and uniformly between the two sides, again at distance \(\epsilon\). A translocation is scored only when the newly selected side differs from the preceding side. No independent bulk reset occurs. All parameters are fixed as \(t\to\infty\).

In gate order \((O,C)\), let \(\mathbf1=(1,1)^\top\), \(\pi=(p,1-p)\), \(\Pi=\mathbf1\pi\), \(I\) be the identity, and

\[
K_y(s)=e^{-y\sqrt{s/D}}\Pi+e^{-y\sqrt{(s+\lambda)/D}}(I-\Pi),\quad
S_y(s)=\frac{1-e^{-y\sqrt{s/D}}}{s},\quad M(z)=\operatorname{diag}\left(\frac{1+z}2,1\right).
\]

These formulas are for \(y>0\), \(s>0\). The resolvent inverse exists because each excursion has strictly subunit probability of completion before exponential killing \(s\). The gate is sampled at the **arrival** time at the interface, after the Brownian excursion, and does not reset with the particle.

## Proof

**1. Excursion renewal and exact counting transform.** Let \(H_y\) be the first hitting time of zero by Brownian motion started at distance \(y\). Its Laplace transform is \(\mathbb E e^{-sH_y}=e^{-y\sqrt{s/D}}\). The gate transition semigroup is \(e^{Qt}=\Pi+e^{-\lambda t}(I-\Pi)\), where \(Q\) is its two-state generator. Independence implies the matrix of joint first-hit discounted gate transitions is precisely \(K_y(s)=\mathbb E[e^{-sH_y}e^{QH_y}]\). The contribution before first interface contact has transform \(S_y(s)\mathbf1\). Each completed contact contributes \(M(z)\), encoding one Bernoulli side change if the gate is open and zero otherwise; subsequent excursions start at distance \(\epsilon\). Summing the matrix geometric series proves the displayed \(\mathcal G_x(z,s)\). At \(z=1\), since \(K_y(s)\mathbf1=e^{-y\sqrt{s/D}}\mathbf1\), the transform equals \(\mathbf1/s\), as required by normalization. At \(z=0\), it is the Laplace transform of \(\Pr(T>t)\).

**2. The unmarked renewal clock is exactly tractable.** Let \(H_t^*\) be the number of interface contacts by \(t\), regardless of crossing. The first excursion is from \(x\) and later excursions from \(\epsilon\). Brownian hitting times of successive excursions are independent and have the positive \(1/2\)-stable convolution property, so their first \(n\) durations sum in law to the Brownian first-hit time from \(x+(n-1)\epsilon\). Hence for every integer \(n\ge1\),

\[
\Pr(H_t^*\ge n)=\operatorname{erfc}\left(\frac{x+(n-1)\epsilon}{2\sqrt{Dt}}\right).
\]

Set \(n=\lfloor u\sqrt t\rfloor+1\) to get \(H_t^*/\sqrt t\Rightarrow(\sqrt{2D}/\epsilon)|Z|\). The exact complementary-error-function bound decays faster than any power for \(n/\sqrt t\to\infty\), so the normalized clock is uniformly integrable to **every positive power**.

**3. Marked gate contacts.** At successive interface hits the gate states form a homogeneous irreducible Markov chain with transition matrix \(K_\epsilon(0)=kI+(1-k)\Pi\). Because \(0<k<1\), its unique stationary distribution is \(\pi=(p,1-p)\). At an open contact, the independent side-choice coin records a genuine translocation with probability \(1/2\). The finite-state Markov-chain ergodic theorem with independent marks gives

\[
\frac{\text{number of translocations among the first }n\text{ contacts}}{n}\longrightarrow p/2 \quad\text{almost surely}.
\]

The total contacts \(H_t^*\to\infty\) almost surely, and the random-index version of this pathwise limit implies \(N_t/H_t^*\to p/2\) almost surely. By Slutsky's theorem, the limiting count law follows. Since \(0\le N_t\le H_t^*\), the uniform moment bounds from Step 2 imply convergence of every positive count moment, proving the stated mean, variance and asymptotic squared coefficient of variation.

**4. First-switch tail.** Define \(R=M(0)=\operatorname{diag}(1/2,1)\) and \(b=(1/2,0)^\top=\mathbf1-R\mathbf1\). Let \(\phi_y(s)\) be the two-vector of Laplace transforms of \(T\) with initial distance \(y\). First-step conditioning yields

\[
\phi_x(s)=K_x(s)[b+R\phi_\epsilon(s)],\qquad
\phi_\epsilon(s)=[I-K_\epsilon(s)R]^{-1}K_\epsilon(s)b.
\]

At \(s=0\), the probability of eventual crossing is one: the embedded chain visits open infinitely often and infinitely many independent open-side coins succeed. Expand the Brownian factor as \(e^{-y\sqrt{s/D}}=1-y\sqrt{s/D}+O(s)\), while the gate-relaxation factor is analytic at zero. Writing \(\phi_\epsilon(s)=\mathbf1-\sqrt s\,g+O(s)\) and \(K_y^0=k_y I+(1-k_y)\Pi\), with \(k_y=e^{-y\sqrt{\lambda/D}}\), gives

\[
[I-K_\epsilon^0R]g=(\epsilon/\sqrt D)\mathbf1,\qquad
\phi_x(s)=\mathbf1-\sqrt s\left[(x/\sqrt D)\mathbf1+K_x^0Rg\right]+O(s).
\]

The determinant \(\det(I-K_\epsilon^0R)=p(1-k)/2>0\); solving the two-by-two system and simplifying gives exactly the two constants \(C_O(x)\) and \(C_C(x)\) above. Finally, for the nonincreasing survival function,

\[
\int_0^\infty e^{-st}\Pr(T>t)dt=\frac{1-\mathbb E e^{-sT}}{s}\sim C_i(x)s^{-1/2}.
\]

Karamata's monotone Tauberian theorem implies \(\Pr(T>t)\sim C_i(x)/(\sqrt{\pi t})\), which in turn implies \(\mathbb ET=\infty\).

## Verification

The standalone Python file `VERIFY.py` recomputes the two-state symbolic determinant, the closed tail constants and their positive difference; it also checks time-Laplace normalization at \(z=1\), the exact link of \(z=0\) to the first-translocation transform, and multiple high-precision small-\(s\) asymptotics for distinct gate rates, starting distances and diffusivities. It uses SymPy and mpmath and prints its total passing check count; execute with `python VERIFY.py`. These finite checks corroborate the calculations; the long-time law and tail are established analytically above.

## Relationship to prior work

Bressloff [1] constructs the **underlying finite-offset stochastically gated interface renewal model** and solves the unmarked position/gate propagator, including a separate bulk-reset extension. Its position probabilities can distinguish the parity of the side-switch count but do not specify the full count law. Kay and Giuggioli [2] determine crossing-count distributions for **constant-permeability** snapping-out Brownian motion by a local-time-subordinated Poisson process; the present temporally switching gate, finite-offset Brownian excursion dynamics and Markov-correlated opening marks are not described by that independent Poisson crossing clock. Bressloff [3] and Scher et al. [4] treat the **first absorption at gated targets**, whose process terminates at success, rather than repeated translocations through a continuing gated interface. Grebenkov [5] analyzes boundary-local-time encounters for confined targets, not the gate-correlated count and finite-offset first-side-switch tail. The stable half-normal renewal-count limit itself is classical; the claim is its parameter-calibrated combination with the exact finite-parameter Markov-gated transform and two distinct first-translocation tail constants, not a new general renewal theorem.

## Limitations

The interface has a single exogenous two-state Markov gate; particle motion is unbiased and independent of gate transitions. Each hit resets the particle a fixed **positive** distance \(\epsilon\). Actual translocation counts need not remain finite in a zero-offset limit, and the paper makes no interchange of \(\epsilon\to0\) and \(t\to\infty\). No multi-particle, non-Markovian, spatially dependent, finite-interval or bulk-reset extension is proved. An exact finite-time count density is given through a Laplace generating transform rather than inverted to elementary physical-time functions. Independent priority examination against all possible general Markov-additive and boundary-local-time counting results has not been performed.

## References

[1] P. C. Bressloff, *Renewal theory for Brownian motion across a stochastically gated interface*, arXiv:2601.13414v1 (first posted 2026-01-19), https://arxiv.org/abs/2601.13414 .

[2] T. Kay and L. Giuggioli, *Local Time Statistics and Permeable Barrier Crossing: from Poisson to Birth-Death Diffusion Equations*, arXiv:2406.07142, https://arxiv.org/abs/2406.07142 ; *Physical Review Research* 7, 013097 (2025).

[3] P. C. Bressloff, *Renewal theory for Brownian motion with stochastically gated targets*, arXiv:2601.01588v1, https://arxiv.org/abs/2601.01588 .

[4] Y. Scher, A. Kumar, M. S. Santhanam and S. Reuveni, *Continuous Gated First-Passage Processes*, arXiv:2211.09164, https://arxiv.org/abs/2211.09164 .

[5] D. S. Grebenkov, *Statistics of diffusive encounters with a small target: Three complementary approaches*, arXiv:2205.06566, https://arxiv.org/abs/2205.06566 .
