# Three sharp dissent-decay regimes at a coincident social-contagion threshold

## Finding

Consider the normalized three-state, interaction-driven social-contagion equations of Crokidakis and Sigaud. On the **coincident critical surface** \(\beta=\eta=\mu=m>0\), with spontaneous resistance-on-contact \(\alpha=a>0\) and infected-to-denier conversion \(\delta=k>0\), every initially infected orbit tends to the all-susceptible state. Its infected and denier fractions have the following **three distinct sharp long-time regimes**, for every admissible initial population with \(i(0)>0\):

\[
\begin{array}{c|c|c}
\text{parameter regime}&\lim_{t\to\infty}t\,d(t)&\text{sharp infected limit}\\ \hline
0<k<m&2/(m+k)&\displaystyle\lim_{t\to\infty}t^2i(t)=\frac{2(m-k)}{a(m+k)^2}\\[4pt]
k=m&1/m&\displaystyle\lim_{t\to\infty}t^2\log(t)\,i(t)=\frac{1}{2am}\\[4pt]
k>m&1/m&\displaystyle\lim_{t\to\infty}t^{1+k/m}i(t)=C(i(0),d(0);a,m,k)\in(0,\infty)
\end{array}
\]

The logarithm applies at sufficiently large \(t>1\). The constant in the third regime depends on the initial condition and is not claimed universal. In particular, \(k=m\) is a genuinely marginal line: the usual inverse-square infected scaling acquires a logarithmic divisor. The theorem quantifies critical slowing at the intersection of the source's two transition curves; it makes no claim about stochastic network critical exponents.

## Assumptions and scope

The normalized population fractions \((s,i,d)\) solve the autonomous mean-field system

\[
\begin{aligned}
\dot s&=m-(m+a)si-msd-ms,\\
\dot i&=msi-kid-mi,\\
\dot d&=kid+msd+asi-md,
\end{aligned}\qquad s+i+d=1.
\]

Here \(a,m,k\) are arbitrary positive **continuous-time kinetic coefficients**; a parameter region interpreting them as microscopic probabilities is an admissible subdomain. Initial data satisfy \(s(0),d(0)\ge0\), \(i(0)>0\), and \(s(0)+i(0)+d(0)=1\). Time is the physical time of the differential equations, with no hidden rescaling. All limits concern \(t\to+\infty\), and the estimates hold for every such initial condition. In the original model \(a=\alpha\), \(m=\beta=\eta=\mu\), and \(k=\delta\). The source's thresholds \(\beta_c^{(1)}=\mu\) and \(\beta_c^{(2)}=(\delta+\mu)\eta/\mu-\delta\) coincide when \(\eta=\mu\) and \(\beta=\mu\).

## Proof

**1. Positivity and extinction.** The vector field points into the nonnegative unit simplex at its boundary, which is therefore invariant and compact. Since the susceptible birth term is positive, \(s(t)>0\) for each \(t>0\). Since \(i(0)>0\), \(i(t)>0\) for every finite time, and since \(\dot d\vert_{d=0}=asi\), \(d(t)>0\) for all \(t>0\). Eliminating \(s=1-i-d\) gives the *exact* planar equations

\[
\dot i=-mi^2-(m+k)id,\qquad
\dot d=ai-md^2-(a+m-k)id-ai^2.
\tag{1}
\]

The first implies \(\dot i\le-mi^2\) and hence \(i(t)\to0\). The second implies \(\dot d\le (a+\max\{k-m,0\})i-md^2\). For every \(\varepsilon>0\), eventually \(i(t)\le\varepsilon\); comparison with the Riccati equation \(y\prime=(a+\max\{k-m,0\})\varepsilon-my^2\) bounds \(\limsup_{t\to\infty}d(t)\) by \(\sqrt{(a+\max\{k-m,0\})\varepsilon/m}\). Sending \(\varepsilon\to0\) gives \(d(t)\to0\). In particular, \(s(t)\to1\), proving global attraction without relying on a linearization at the nonhyperbolic equilibrium.

**2. A divergent nonlinear clock.** Fix any \(t_0>0\) and define

\[
\tau(t)=\int_{t_0}^t d(u)\,du.
\]

We show \(\tau(t)\to\infty\). Otherwise \(\int_0^\infty d(u)\,du<\infty\). By the first equation in (1), putting \(F(t)=\exp(-(m+k)\int_0^t d(u)\,du)\), one has the exact identity

\[
i(t)=\frac{F(t)}{i(0)^{-1}+m\int_0^tF(u)\,du}.
\]

An integrable \(d\) would make \(F(t)\) converge to a positive value, giving \(i(t)\sim1/(mt)\) and thus \(\int_0^\infty i(u)\,du=\infty\). Yet the original denier equation gives \(\dot d+md=kid+msd+asi\ge asi\); because \(s(t)\to1\), integrating this inequality would force \(d(t)+m\int_0^td(u)\,du\to\infty\), a contradiction. Hence the new clock is unbounded.

**3. Exact scalar reduction.** Set \(r=i/d^2>0\). Because \(d\tau/dt=d>0\), direct differentiation of (1) gives the identities

\[
\frac{dr}{d\tau}=r\big[(m-k)-2ar+(2a+m-2k)rd+2ar i\big],
\tag{2}
\]
\[
\frac{d\log d}{d\tau}=-m+ar-(a+m-k)rd-ar i,
\tag{3}
\]

where \(i=r d^2\). These are **identities**, not center-manifold approximations. The vanishing of \(i,d\) implies that the coefficient of \(r\) inside the brackets in (2) tends to \(-2a\). In particular, standard scalar logistic comparison bounds \(r\) from above for all sufficiently large \(\tau\) and supplies the trichotomy below.

**4. Lower-conversion regime \(0<k<m\).** Writing \(\lambda=m-k>0\), for every sufficiently small \(\varepsilon>0\), (2) traps \(r\) between logistic equations with coefficients \(\lambda\) and \(2a\pm\varepsilon\). As \(\tau\to\infty\), it follows that

\[
r\to\frac{m-k}{2a}.
\]

Equation (1) now gives \(\dot d/d^2=-m+ar+O(rd)\to-(m+k)/2\). Since \(d\to0\), integration of \((1/d)'=-\dot d/d^2\) yields \(t d(t)\to2/(m+k)\). Finally \(i=r d^2\) yields the first infected coefficient.

**5. Marginal regime \(k=m\).** Equation (2) reduces to \(dr/d\tau=-r^2[2a-(2a-m)d-2ad^2r]\), so \(r\to0\) and

\[
\frac{d}{d\tau}\left(\frac1r\right)=2a-(2a-m)d-2ai\longrightarrow2a.
\]

Thus \(\tau r\to1/(2a)\). Equation (1) implies \(t d(t)\to1/m\), hence \(\tau(t)/\log t\to1/m\). Since \(i=r d^2\), these limits give \(t^2\log t\,i(t)\to1/(2am)\).

**6. Higher-conversion regime \(k>m\).** Set \(\lambda=k-m>0\). By (2), \(d\log r/d\tau=-\lambda-2ar+o(1)r\); hence eventually \(r\le C e^{-\lambda\tau/2}\), so \(r\) is integrable in \(\tau\). From (3), \(d\log d/d\tau=-m+O(r)\) with an integrable remainder, whence \(d(\tau)e^{m\tau}\to D_\infty\in(0,\infty)\). Integrating the logarithmic form of (2) similarly gives \(r(\tau)e^{\lambda\tau}\to R_\infty\in(0,\infty)\). Since \(dt/d\tau=1/d\), one has \(t e^{-m\tau}\to1/(mD_\infty)\). Substitution into \(i=r d^2\) proves the final regime with the explicit positive representation

\[
C=\frac{R_\infty D_\infty^2}{(mD_\infty)^{1+k/m}}.
\]

The auxiliary clock may start at any fixed positive physical time, consistently modifying \(R_\infty\) and \(D_\infty\) so that the displayed physical-time constant remains unchanged. This completes the proof.

## Verification

The accompanying standalone `verify.py` derives equations (1)–(3) exactly using symbolic differentiation from the full three-compartment system. It also integrates the exact ratio and logarithmic equations in the nonlinear clock for six strictly positive sets of parameters and initial fractions, including all three regimes. For two parameter families it checks the universal denier coefficients, the low-conversion infected coefficient, the marginal logarithmic coefficient, and stabilization of the high-conversion initial-data-dependent amplitude. The numerical tests passed on the supplied program; their role is corroboration, not proof of any asymptotic limit. Execute from the extracted file directory with `python -m pip install -r requirements.txt` followed by `python verify.py`.

## Relationship to prior work

Crokidakis and Sigaud, *Nonequilibrium phase transitions in a racism-spreading model with interaction-driven dynamics* (arXiv:2601.19806v1, posted January 27, 2026; subsequent open-access journal article March 11, 2026), define equations (5)–(7) and identify the coincident phase-transition thresholds in equations (8)–(9) and Appendix A. In their Section 3.1 they explicitly state that critical exponents were not calculated. The contribution here is the **global sharp relaxation trichotomy** at the coincident threshold, including the parameter-driven continuous infected exponent and its marginal logarithmic correction; neither the model equations nor the equilibrium threshold itself is claimed as new.

Mamo, *Modeling the transmission dynamics of racism propagation with community resilience* (2021), develops the five-variable SERDC model with exposed and resilience compartments. Its reproduction-number criterion concerns a different differential system and does not imply (1)–(3) or the sharp time-domain coefficients. Critical relaxation exponents in other epidemic and opinion equations are related mathematical phenomena but do not determine the coupling-dependent regimes of this specific contact-conversion system. The same explicit asymptotic claim was not found in targeted published-record and mathematical-record searches; that negative search is **not** a proof of historical novelty.

## Limitations

This is a theorem about a deterministic, homogeneous-mixing, normalized compartmental ODE at an exactly coincident threshold. It assumes \(a,m,k>0\) and an initially positive infected fraction. The initial condition \(i(0)=0\) belongs to a different invariant face and is deliberately excluded from the infected-asymptotic statements. The result does not assert finite-agent extinction-time distributions, fluctuations, a critical exponent on heterogeneous social networks, or realism of the simplified state-transition assumptions. Historical priority has not been independently verified, and related general asymptotic ODE theorems could provide abstract tools from which portions are recoverable.

## References

1. N. Crokidakis and L. Sigaud, *Nonequilibrium phase transitions in a racism-spreading model with interaction-driven dynamics*, arXiv:2601.19806v1, January 27, 2026, https://arxiv.org/html/2601.19806v1. Journal version: *European Physical Journal B* **99** (2026), article 34, https://doi.org/10.1140/epjb/s10051-026-01127-0.
2. D. K. Mamo, *Modeling the transmission dynamics of racism propagation with community resilience*, *Computational Social Networks* **8** (2021), article 22, https://doi.org/10.1186/s40649-021-00102-2.
