# A sharp thermal ceiling and essential-contrast collapse for photon-added light detected by multiplexed clicks

## Finding
Consider balanced multiplexed click detection of photon-added thermal light. There is a sharp, detector-dependent upper thermal occupation above which adding *any finite number of photons* can never produce a negative sub-binomial second-order click witness. Below the ceiling an explicit finite order is sufficient, but the largest possible negative contrast over all addition orders vanishes with an essential singularity as the ceiling is approached.

For \(0<h<1/2\), set
\[
 A(h)=\log\frac{(1-h)^2}{1-2h},\qquad
 B(h,\beta)=\log\frac{(1+\beta h)^2}{1+2\beta h},\qquad
 \beta_*(h)=\frac1{1-2h}.
\]
The exact sign criterion is
\[
 Q_B(m,\beta,h)<0\quad\Longleftrightarrow\quad
 m\big[A(h)-B(h,\beta)\big]>B(h,\beta).
\]
The strict inequality is solvable in a finite integer \(m\ge1\) **if and only if** \(\beta<\beta_*\). In that range, the least successful order and the fixed-order cutoff are
\[
 m_{\min}=\left\lfloor\frac{B}{A-B}\right\rfloor+1,\qquad
 \beta_m(h)=\frac{\tau_m}{h(1-\tau_m)},\qquad
 \tau_m=\sqrt{1-e^{-mA/(m+1)}}.
\]
Thus \(Q_B<0\) at fixed \(m\) precisely for \(\beta<\beta_m\). For fixed \(0<h<1/2\), the thresholds \(\beta_m\) increase strictly with \(m\) and approach \(\beta_*\) from below; they also increase strictly with \(h\). Their small-\(h\) limit is \(\sqrt{m/(m+1)}\). At \(h\uparrow1/2\), \(\beta_m(h)\sim4^{1/(m+1)}(1-2h)^{-m/(m+1)}\).

The optimal measurable *population-level witness contrast*, maximized only over finite addition orders, is
\[
 \mathcal D_{N,h}(\beta)=\sup_{m\in\mathbb Z_{\ge1}}\max\{0,-Q_B(m,\beta,h)\}.
\]
For each \(\beta<\beta_*\), the supremum is positive and attained at a finite order; for \(\beta\ge\beta_*\), it is zero. Its sharp near-ceiling law is
\[
 \boxed{\lim_{\beta\uparrow\beta_*}
 (\beta_* -\beta)\log\mathcal D_{N,h}(\beta)
 =-\kappa(h)},\qquad
 \kappa(h)=\frac{(1-h)A(h)}{2h^2(1-2h)}
 \log\frac1{1-2h}>0.
\]
The statement is solely about the second-order witness \(Q_B\), not the nonclassicality of the underlying state or optimal discrimination by all possible statistical procedures.

## Assumptions and scope
Let \(m\in\mathbb Z_{\ge1}\), \(\beta\in[0,\infty)\), \(N\in\mathbb Z_{\ge2}\), and \(0<\eta\le1\). The normalized input is obtained by adding exactly \(m\) photons to a single-mode thermal state of seed mean \(\beta\):
\[
 \rho_{m,\beta}=\frac{(a^\dagger)^m\rho_{\mathrm{th},\beta}a^m}
 {\operatorname{Tr}[(a^\dagger)^m\rho_{\mathrm{th},\beta}a^m]},\qquad
 \Pr_{\rho_{m,\beta}}(n=m+k)
 ={m+k\choose m}\frac{\beta^k}{(1+\beta)^{m+k+1}},\quad k\ge0.
\]
The \(N\) on-off detectors are equally illuminated: each incoming photon independently selects precisely one bin with probability \(h=\eta/N\) per bin, or is lost with probability \(1-\eta\), with no dark counts. A bin registers at most one click. The total number of clicked bins is \(C\). The sub-binomial witness is
\[
 Q_B=\frac{N\operatorname{Var}(C)}{\mathbb E(C)[N-\mathbb E(C)]}-1.
\]
For finite \(m,\beta\) and \(\eta>0\), its denominator is strictly positive. For \(N\ge3\), all admissible efficiencies satisfy \(h<1/2\); for \(N=2\), \(h=1/2\) occurs only at ideal efficiency \(\eta=1\).

## Proof
**1. Generating function and click covariance.** The photon-number probability-generating function, calculated directly from the negative-binomial normalization, is
\[
 G(z)=\sum_{n\ge0}\Pr(n)z^n=\frac{z^m}{[1+\beta(1-z)]^{m+1}}.
\]
Put \(u=G(1-h)\) and \(v=G(1-2h)\). Each detector remains silent with probability \(u\); a specified pair both remain silent with probability \(v\). Therefore
\[
 \mathbb E C=N(1-u),\quad
 \operatorname{Var}(C)=Nu(1-u)+N(N-1)(v-u^2),\quad
 Q_B=(N-1)\frac{v-u^2}{u(1-u)}.
\]
The denominator is positive since \(0<u<1\). For \(0<h<1/2\), substitution yields
\[
 \frac{v}{u^2}=\exp[-mA(h)+(m+1)B(h,\beta)]
 =\exp[B-m(A-B)].
\]
This is the exact sign criterion.

**2. Thermal ceiling and least addition order.** The function \(B(h,\beta)\) increases continuously and strictly with \(\beta>0\), starts from zero, and obeys \(B(h,\beta_*)=A(h)\) for \(\beta_*=1/(1-2h)\). Therefore \(A-B\le0\) when \(\beta\ge\beta_*\), precluding a strict negative witness at every finite \(m\). When \(\beta<\beta_*\), the strict inequality is equivalent to \(m>B/(A-B)\), yielding the stated least integer. The unique equation \(B=mA/(m+1)\) can be solved by putting \(t=\beta h/(1+\beta h)\), since
\[
 \frac{(1+\beta h)^2}{1+2\beta h}=\frac1{1-t^2};
\]
this gives the displayed \(\tau_m\) and \(\beta_m\), including the equality boundary. Since \(m/(m+1)\) grows strictly with \(m\), so does \(\beta_m\). To see monotonicity in \(h\), differentiate:
\[
 \frac{\partial_h B(h,\beta)}{A'(h)}
 =\beta^2\frac{(1-h)(1-2h)}{(1+\beta h)(1+2\beta h)},
\]
which strictly decreases with \(h\) when \(\beta>0\). Since \(A(0)=B(0,\beta)=0\), the monotone weighted-average rule implies that \(B/A\) decreases in \(h\). The equality-level cutoff therefore increases strictly with \(h\). Expansion at \(h\downarrow0\) yields \(A\sim h^2\), \(B\sim\beta^2h^2\). The expansion \(A=\log[(1-h)^2/(1-2h)]=-\log[4(1-2h)]+o(1)\) gives the stated \(h\uparrow1/2\) cutoff asymptotic. At \(h=1/2\), \(G(0)=0\) for every \(m\ge1\), hence \(v=0<u^2\), proving the separate ideal two-bin case.

**3. Optimal contrast near the ceiling.** Fix \(0<h<1/2\). For \(0\le\beta<\beta_*\), abbreviate \(\Delta=A-B>0\), \(t=B/\Delta\), \(\lambda=(1-h)/(1+\beta h)\), and \(w=1/(1+\beta h)\). Then \(0<\lambda<1\) and \(u=w\lambda^m\). The exact negative contrast for an integer \(m>t\) is
\[
 -Q_B(m,\beta)=(N-1)\frac{w\lambda^m
 [1-e^{-\Delta(m-t)}]}{1-w\lambda^m}.
\]
It is zero or negative when \(m\le t\) in the expression for \(-Q_B\). The displayed positive expression tends to zero as \(m\to\infty\); at least one admissible integer exists, so a finite optimizer exists. In particular,
\[
 0<\mathcal D_{N,h}(\beta)
 \le\frac{(N-1)w\lambda^t}{1-w\lambda^t}.
\]
For the integer \(m_0=\lfloor t\rfloor+2\), one has \(1<m_0-t\le2\). Substitution gives the lower bound
\[
 \mathcal D_{N,h}(\beta)
 \ge(N-1)w\lambda^{t+2}(1-e^{-\Delta}),
\]
using \(1-w\lambda^{m_0}<1\). Put \(\epsilon=\beta_* -\beta\). A one-sided Taylor expansion gives
\[
 \Delta=c_h\epsilon+O(\epsilon^2),\quad
 c_h=\partial_\beta B(h,\beta_*)
 =\frac{2h^2(1-2h)}{1-h}>0,
 \quad t=\frac{A}{c_h\epsilon}+O(1),
 \quad\lambda\longrightarrow1-2h.
\]
Taking logarithms of the two positive bounds and observing \(\log(1-e^{-\Delta})=\log\epsilon+O(1)\), one obtains
\[
 \log\mathcal D_{N,h}(\beta)
 =t\log\lambda+O(|\log\epsilon|).
\]
Multiplication by \(\epsilon\) produces the stated \(-\kappa(h)\). This is an infinite-order, exact two-sided asymptotic argument rather than inference from numerical extrapolation.

## Verification
The self-contained executable \(\texttt{artifacts/verify.py}\) uses Python's standard library. It constructs a physically independent distribution of occupied detector bins by sending photons through an occupancy Markov chain, then mixes it with the negative-binomial photon-number weights. It checks 240 direct click distributions against the analytic \(Q_B\), 120 fixed-order cutoff identities, monotonicity grids, and six numerically stable near-ceiling contrast values calculated in log-space. Run with \(\texttt{python3 artifacts/verify.py}\). The observed maximum absolute error in direct click-witness comparisons is below \(3\times10^{-12}\). The mathematical proof, not this finite test, establishes the all-parameter statements.

## Relationship to prior work
Sperling, Vogel and Agarwal, *Sub-binomial light* (arXiv:1205.4669), introduced the click witness and derived its general click-covariance form (Section II, Eqs. 4–8). Their Section V and Appendix B study the **single**-photon-added thermal state. In particular, detecting nonclassicality of super-Poisson single-photon-added thermal states with \(Q_B<0\) is their established result and is not claimed here.

Barnett, Ferenczi, Gilson and Speirits, *Statistics of photon-subtracted and photon-added states* (arXiv:1806.09475), give the general photon-added thermal counting law. Lee, Ferrari, Pernice and Rockstuhl, *Sub-Poisson-Binomial Light* (arXiv:1606.04826), examine an unbalanced witness and single-photon-added thermal examples. Sperling and collaborators' *Identification of nonclassical properties of light with multiplexing layouts* (arXiv:1701.07642) generalizes click moment tests. Gebhart and Bohmann, *Neural-network approach for identifying nonclassicality from click-counting data* (Phys. Rev. Research 2, 023150, 2020), includes several added-photon thermal states as inputs and tabulates their click distributions, focusing on learned and moment-based recognition.

The click-covariance identity and all-order photon-number law therefore **already exist** and jointly imply the starting expression for \(Q_B\) by substitution. The contribution assessed here is the optimized sharp *all-addition-order* detector thermal ceiling, equality/cutoff classification, and especially the proven essential-singularity exponent of the best negative contrast. These results should not be mistaken for the prior general moment formula or for known numerical examples.

## Limitations
The no-go is for negative values of the *second-order sub-binomial click witness* only. It does not imply that the photon-added state is classical, nor preclude a different higher-order witness, state reconstruction, or other detector model. Equal splitting, independent bin attempts, no dark counts, fixed efficiency, and exactly one thermal mode are essential assumptions. The near-ceiling limiting exponent concerns the population-level witness and does **not** establish experimental sample complexity or a detectable finite-statistics signal. Publication priority beyond the inspected sources is not independently certified.

## References
1. J. Sperling, W. Vogel and G. S. Agarwal, *Sub-binomial light*, arXiv:1205.4669v1 (21 May 2012), https://arxiv.org/pdf/1205.4669 .
2. S. M. Barnett, G. Ferenczi, C. R. Gilson and F. C. Speirits, *Statistics of photon-subtracted and photon-added states*, arXiv:1806.09475, https://arxiv.org/pdf/1806.09475 .
3. C. Lee, S. Ferrari, M. Pernice and C. Rockstuhl, *Sub-Poisson-Binomial Light*, arXiv:1606.04826, https://arxiv.org/pdf/1606.04826 .
4. J. Sperling and collaborators, *Identification of nonclassical properties of light with multiplexing layouts*, arXiv:1701.07642, https://arxiv.org/pdf/1701.07642 .
5. V. Gebhart and M. Bohmann, *Neural-network approach for identifying nonclassicality from click-counting data*, Phys. Rev. Research **2**, 023150 (2020), DOI:10.1103/PhysRevResearch.2.023150, https://doi.org/10.1103/PhysRevResearch.2.023150 .
