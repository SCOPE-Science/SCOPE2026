# A sharp finite-threshold first-passage uncertainty law for semi-Markov clocks

## Finding

**Theorem (finite-threshold semi-Markov first-passage uncertainty and exact optimality).** Under the finite-state, positive-holding-time assumptions below, there is an explicitly computable constant \(C\geq0\), depending on the embedded chain and the conditional holding-time first two moments but **not** on the chosen jump-flux weights, threshold, or initial configuration, such that every positive-drift additive jump flux obeys

\[
\operatorname{Var}(H_\alpha(k))\geq B\,\mathbb E H_\alpha(k)-C\qquad(k>0),
\]

where \(B\) is the stationary time-fraction-weighted mean of conditional holding-time variance divided by conditional mean. The optimal flux obtained by weighting each transition with its conditional **mean holding time** satisfies

\[
\left|\operatorname{Var}(H_\mu(k))-B\mathbb E H_\mu(k)\right|
\leq C+\frac{\mu_{\max}^2}{4},\qquad
\mathbb E H_\mu(k)=k+O(1).
\]

Consequently \(\liminf_{k\to\infty}\operatorname{Var}(H_\alpha(k))/\mathbb E H_\alpha(k)\geq B\) for every positive-drift flux, while the optimal flux (and its positive scalar multiples plus bounded state-boundary corrections) attains equality in the limit. Thus the stationary semi-Markov first-passage kinetic uncertainty conjecture of Macieszczak (2024), explicitly left open for first-passage times in the cited article, follows under the stated finite-state assumptions. The finite-threshold additive correction is a stronger non-asymptotic statement.

## Assumptions and scope

Let \(S\) be a nonempty finite state set, \(P=(P_{ij})\) an irreducible transition matrix on \(S\), and \(\pi\) its strictly positive stationary row distribution. The embedded chain \((J_n)_{n\geq0}\) has transition matrix \(P\) and starts from **any** fixed or random state. For each allowed directed edge \((i,j)\) with \(P_{ij}>0\), the positive holding time \(W_n\) conditional on \((J_{n-1},J_n)=(i,j)\) has a law depending only on this edge, with

\[
0<\mu_{ij}=\mathbb E[W_n\mid i,j]<\infty,\qquad
0\leq v_{ij}=\operatorname{Var}(W_n\mid i,j)<\infty.
\]

Conditionally on the complete embedded jump chain, all holding times are independent. The process is observed from a **renewal instant** (not a stationary random age). There is no aperiodicity, exponential-moment, or detailed-balance assumption.

Define stationary edge frequency \(q_{ij}=\pi_iP_{ij}\), stationary mean holding time per jump \(d=\sum_{ij}q_{ij}\mu_{ij}>0\), and

\[
B=\frac{\sum_{ij}q_{ij}v_{ij}}{d}
=\sum_{ij}p_{ij}\frac{v_{ij}}{\mu_{ij}},\qquad
p_{ij}=\frac{q_{ij}\mu_{ij}}{d}.
\]

The \(p_{ij}\) are nonnegative stationary **fractions of physical time**, summing to one. For each real-valued edge weighting \(\alpha=(\alpha_{ij})\) with positive stationary per-jump mean \(a=\sum_{ij}q_{ij}\alpha_{ij}>0\), define

\[
S_n^\alpha=\sum_{m=1}^n\alpha_{J_{m-1}J_m},\quad
N_\alpha(k)=\inf\{n\geq1:S_n^\alpha\geq k\},\quad
H_\alpha(k)=\sum_{m=1}^{N_\alpha(k)}W_m,\quad k>0.
\]

Negative individual edge weights are permitted as long as \(a>0\). The first crossing is observed at a jump epoch, so an overshoot can occur. Put \(\mu_{\max}=\max_{P_{ij}>0}\mu_{ij}\). Set \(g_{ij}=v_{ij}-B\mu_{ij}\), and let \(h:S\to\mathbb R\) solve the finite Poisson equation

\[
(I-P)h=\bar g,\qquad \bar g(i)=\sum_jP_{ij}g_{ij},\qquad
C=\max_i h(i)-\min_i h(i).
\]

A solution exists because \(\sum_i\pi_i\bar g(i)=0\); its oscillation \(C\) is independent of additive normalization and nonnegative.

## Proof

**1. Integrable stopping.** Given a finite edge weighting \(\alpha\) with stationary mean \(a>0\), let \(a_i=\sum_jP_{ij}\alpha_{ij}\). Irreducibility yields a bounded solution \(\psi\) of \((I-P)\psi=a_\bullet-a\mathbf1\). Therefore

\[
D_m=\alpha_{J_{m-1}J_m}-a+\psi(J_m)-\psi(J_{m-1})
\]

are bounded martingale differences for the embedded-chain filtration. The identity \(S_n^\alpha=an+\sum_{m\leq n}D_m+\psi(J_0)-\psi(J_n)\), followed by Azuma's inequality, shows for all sufficiently large \(n\) (depending on \(k\) and \(\alpha\)) that \(\mathbb P(N_\alpha(k)>n)\leq\mathbb P(S_n^\alpha<k)\leq e^{-c_\alpha n}\). Hence \(N_\alpha(k)\) has moments of every order. Since the edge means and variances are bounded, \(H_\alpha(k)\) has a finite second moment. The above also proves almost-sure crossing, even with some negative edge weights.

**2. Conditional variance decomposition.** Write \(N=N_\alpha(k)\), and condition on the full embedded chain. The stopping index \(N\) then is fixed, and independent edge-conditioned holding times give

\[
M=\mathbb E[H_\alpha(k)\mid J_0,J_1,\ldots]=\sum_{m=1}^N\mu_{J_{m-1}J_m},\qquad
V=\operatorname{Var}(H_\alpha(k)\mid J_0,J_1,\ldots)=\sum_{m=1}^Nv_{J_{m-1}J_m}.
\]

Therefore \(\operatorname{Var}(H_\alpha(k))=\mathbb EV+\operatorname{Var}(M)\) and \(\mathbb EH_\alpha(k)=\mathbb EM\).

**3. Exact stopping identity.** Define \(g_{ij}=v_{ij}-B\mu_{ij}\). From the Poisson equation, the increments

\[
Z_m=g_{J_{m-1}J_m}+h(J_m)-h(J_{m-1})
\]

have conditional mean zero and bounded size. Since \(\mathbb EN<\infty\), optional stopping (or dominated summation of bounded increments) gives

\[
\mathbb E\sum_{m=1}^Ng_{J_{m-1}J_m}
=\mathbb E[h(J_0)-h(J_N)].
\]

Substitution into the conditional-variance formula yields the **exact finite-threshold identity**

\[
\boxed{\operatorname{Var}(H_\alpha(k))-B\mathbb EH_\alpha(k)
=\operatorname{Var}(M)+\mathbb E[h(J_0)-h(J_N)].}
\]

The first term on the right is nonnegative, while the second is bounded below by \(-C\) for every initial state. This proves \(\operatorname{Var}(H_\alpha(k))\geq B\mathbb EH_\alpha(k)-C\).

**4. Large-threshold lower bound.** Let \(\alpha_{\max}=\max_{P_{ij}>0}\alpha_{ij}>0\) and \(\mu_{\min}=\min_{P_{ij}>0}\mu_{ij}>0\). At the crossing, \(k\leq S_N^\alpha\leq\alpha_{\max}N\), so

\[
\mathbb EH_\alpha(k)=\mathbb EM\geq\mu_{\min}\mathbb EN
\geq \frac{\mu_{\min}}{\alpha_{\max}}k\longrightarrow\infty.
\]

Dividing the finite-level bound by the mean establishes \(\liminf\operatorname{Var}H_\alpha/\mathbb EH_\alpha\geq B\).

**5. Optimality.** For \(\alpha_{ij}=\mu_{ij}\), the stopped sum of edge means is the marked current itself. The first-crossing overshoot \(U=S_N^\mu-k\) lies in \([0,\mu_{\max})\), because the preceding cumulative sum was below \(k\) and the final mark is at most \(\mu_{\max}\). Thus \(M=k+U\), \(\mathbb EH_\mu(k)=k+\mathbb EU\), and by the elementary variance-range bound \(0\leq\operatorname{Var}(M)\leq\mu_{\max}^2/4\). The exact stopping identity now proves

\[
\left|\operatorname{Var}H_\mu(k)-B\mathbb EH_\mu(k)\right|
\leq C+\mu_{\max}^2/4,
\qquad \lim_{k\to\infty}\frac{\operatorname{Var}H_\mu(k)}{\mathbb EH_\mu(k)}=B.
\]

More generally, any \(\alpha_{ij}=c\mu_{ij}+b_i-b_j\) with \(c>0\) and bounded state potential \(b\) has positive mean \(a=cd\). The telescoping identity \(S_N^\alpha=cM+b_{J_0}-b_{J_N}\), together with \(0\leq S_N^\alpha-k<\alpha_{\max}\), bounds \(M-k/c\) in a fixed interval independent of \(k\). Hence \(\operatorname{Var}M=O(1)\), and equality in the asymptotic uncertainty lower bound follows for every such gauge-optimal weighting.

**6. Sharpness cannot be improved universally.** A single-state renewal process with identical positive holding mean \(\mu\) and variance \(v\), equipped with marked weight \(\alpha=\mu\), has deterministic crossing index \(\lceil k/\mu\rceil\) and exactly \(\operatorname{Var}H/\mathbb EH=v/\mu=B\) at every \(k>0\). Therefore a strictly greater universal asymptotic coefficient is impossible.

## Verification

The exact rational checker `checker.py` solves a three-state example with independent Gamma holding times of shape two and edge-dependent scale, obtains

\[
\pi=(4,3,4)/11,\qquad d=27/22,\qquad B=79/108,
\]

and computes \(h=(109/1188,-4/33,-1/1188)\), \(C=23/108\). For eight threshold values and each of three edge-weight families (mean-dwell weights, a gauge perturbation, and unit counts), it recursively enumerates all stopped jump paths and verifies the exact identity, finite-level lower bound, martingale-corrector expectation, and relevant overshoot bounds using rational arithmetic: **24 checks passed**. Run `python checker.py` with Python 3 and SymPy. These finite checks are independent algebraic illustrations; the infinite and arbitrary-weight claims rest on the preceding proof.

## Relationship to prior work

K. Macieszczak (2024), Eq. (9), proves the sharp **fixed-observation-time** semi-Markov flux uncertainty lower bound, Eq. (10) identifies the mean-holding-time-weighted optimal flux, and the paragraph following Eq. (11) expressly leaves its first-passage analogue as a hypothesis. The present result establishes that exact first-passage lower-bound coefficient and saturation from a finite-level identity, including an additive constant uniform over all flux weights and thresholds.

F. Liu, S. Xia and S. Su (2024) develop first-passage large-deviation transforms for open-quantum semi-Markov models and discuss general difficulties with current-like counting variables. Their transform and examples do not state the above finite-threshold all-flux inequality. K. Prech and collaborators (2024) study optimal clock precision primarily for Markov processes. Earlier Markov first-passage uncertainty relations (Garrahan 2017; Gingrich and Horowitz 2017; Hiura and Sasa 2021) concern narrower dynamics or different coefficients. These comparisons do not constitute an independent or exhaustive priority certification.

## Limitations

The theorem assumes finite irreducible embedded dynamics and edge-conditioned independent positive holding times with finite first two moments. It begins at a renewal epoch; an arbitrary stationary-age initialization is not included in the stated finite-threshold bound. The result concerns physical elapsed time at the **first jump-epoch crossing** of a positive-drift additive edge flux, and allows signed individual marks. It makes no claims about zero/negative-drift currents, nonergodic chains, interacting waiting times, heavy-tailed infinite-variance laws, or universal finite-threshold bounds without an additive correction. No universal optimality uniqueness is asserted. Identification of a related general Markov-additive theorem in uncatalogued literature could affect publication priority.

## References

1. K. Macieszczak, *Ultimate Kinetic Uncertainty Relation and Optimal Performance of Stochastic Clocks*, arXiv:2407.09839v1 (13 July 2024), https://arxiv.org/html/2407.09839v1 .
2. F. Liu, S. Xia and S. Su, *Semi-Markov Processes in Open Quantum Systems. III. Large Deviations of First Passage Time Statistics*, arXiv:2407.01940v1 (2 July 2024), https://arxiv.org/html/2407.01940v1 .
3. K. Prech et al., *Optimal Time Estimation and the Clock Uncertainty Relation for Stochastic Processes*, arXiv:2406.19450v1 (2024), https://arxiv.org/html/2406.19450v1 .
4. J. P. Garrahan, *Simple bounds on fluctuations and uncertainty relations for first-passage times of counting observables*, Phys. Rev. E 95, 032134 (2017), https://doi.org/10.1103/PhysRevE.95.032134 .
5. T. R. Gingrich and J. M. Horowitz, *Fundamental bounds on first passage time fluctuations for currents*, Phys. Rev. Lett. 119, 170601 (2017), https://doi.org/10.1103/PhysRevLett.119.170601 .
6. K. Hiura and S.-i. Sasa, *Kinetic uncertainty relation on first-passage time for accumulated current*, Phys. Rev. E 103, L050103 (2021), https://doi.org/10.1103/PhysRevE.103.L050103 .
