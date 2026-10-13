# Sharp human-prevalence control interval under a persistent Mpox rodent reservoir
## Finding
For the eight-compartment human–rodent Mpox system of Arhinful, Anafo and Ampofi, a persistently infected rodent reservoir imposes an **exact, strictly positive lower bound** on the human endemic infectious fraction even if the human-to-human transmission rate is reduced to zero. More strongly, as that rate varies, the complete interval of attainable endemic human prevalence and its inverse control law are explicit.

Write the human states as \(S_h,E_h,I_h,Q_h,R_h\), the rodent states as \(S_r,E_r,I_r\), and the respective total populations as \(N_h\) and \(N_r\). Introduce positive combinations
\[
A=\delta+\gamma+\mu_h,\quad
B=\mu_h+d_h+\phi,\quad
C=\mu_h+d_h+\tau+\psi,
\]
\[
p=\frac{\delta}{AB},\qquad
q=\frac{\gamma}{AC},\qquad
r=\frac{\phi p+\psi q}{\mu_h},\qquad
k=\frac1A+p+q+r.
\]
The source's rodent reproduction quantity is
\[
\mathcal R_r=\frac{\beta_3\nu}{(\mu_r+\nu)(\mu_r+d_r)}.
\]
Suppose \(\mathcal R_r>1\), \(\beta_1>0\), and all demographic and progression/removal parameters are strictly positive. The unique rodent-endemic equilibrium has infection force
\[
\ell_r=\frac{\beta_3\nu-(\mu_r+\nu)(\mu_r+d_r)}{\mu_r+d_r+\nu}>0,
\]
and it supplies the strictly positive external human infection force
\[
z=\beta_1\frac{I_r^*}{N_r^*}
=\frac{\beta_1\ell_r}{\beta_3}>0.
\]

Hold all parameters except the nonnegative human-to-human contact rate \(\beta_2\) fixed. For each \(\beta_2\ge0\), the system has a **unique** equilibrium with infected rodents. Its human infectious fraction
\[
J(\beta_2)=\frac{I_h^*}{N_h^*}
\]
is strictly increasing and continuous, and maps \([0,\infty)\) bijectively onto
\[
\boxed{\left[\frac{p z}{1+kz},\,\frac pk\right)}.
\]
For a target prevalence \(J\) in this interval, the exact human-to-human contact rate required to realize it at equilibrium is
\[
\boxed{\beta_2=\frac{1}{p-kJ}-\frac zJ.}
\]
In particular, for every strictly positive \(\beta_2\),
\[
\frac{p z}{1+kz}<\frac{I_h^*}{N_h^*}<\frac pk.
\]
The lower endpoint is attained at \(\beta_2=0\) and is therefore a **sharp, non-eradicable zoonotic prevalence floor** when human-to-human transmission alone is controlled. The upper endpoint is approached as \(\beta_2\to\infty\) but is not attained at any finite rate. These equilibrium fractions are independent of the constant human and rodent recruitment rates \(\Lambda_h,\Lambda_r\).

For completeness, the number of distinct nonnegative equilibria for strictly positive \(\beta_1,\beta_2,\beta_3\) is
\[
1+\mathbf 1_{\{\mathcal R_h>1\}}+\mathbf 1_{\{\mathcal R_r>1\}},\qquad
\mathcal R_h=\beta_2p.
\]
They are the always-present disease-free equilibrium; a human-only endemic equilibrium when \(\mathcal R_h>1\); and the unique coexistence equilibrium when \(\mathcal R_r>1\). There is no rodent-only infected equilibrium when \(\beta_1>0\). This last equilibrium taxonomy is a companion classification, not a claim that such qualitative taxonomy was unknown in other Mpox models.

## Assumptions and scope
Use precisely the source's standard-incidence human–rodent system:
\[
\begin{aligned}
\dot S_h&=\Lambda_h+\tau Q_h-(\beta_1 I_r/N_r+\beta_2 I_h/N_h)S_h-\mu_hS_h,\\
\dot E_h&=(\beta_1 I_r/N_r+\beta_2 I_h/N_h)S_h-AE_h,\\
\dot I_h&=\delta E_h-BI_h,\\
\dot Q_h&=\gamma E_h-CQ_h,\\
\dot R_h&=\phi I_h+\psi Q_h-\mu_hR_h,\\
\dot S_r&=\Lambda_r-(\mu_r+\beta_3 I_r/N_r)S_r,\\
\dot E_r&=\beta_3 I_rS_r/N_r-(\mu_r+\nu)E_r,\\
\dot I_r&=\nu E_r-(\mu_r+d_r)I_r.
\end{aligned}
\]
Both recruitment rates and all mortality, transfer, and cross-species rates are positive. The contact rate \(\beta_2\) is allowed to equal zero solely to include the sharp control endpoint; for strictly positive \(\beta_2\), the lower-bound inequality is strict. Only equilibria in the nonnegative state space with positive total host populations are counted. Because recruitment is positive, every such equilibrium has positive susceptible populations and no denominator vanishes.

The theorem is about the algebraic **equilibria** and attainable endemic prevalence, not their dynamical stability, transient behavior, finite-time eradication, epidemiological inference, or empirical calibration. The upper bound is a mathematical high-contact limit; it is not a biologically calibrated prediction at arbitrarily large contact rates.

## Proof
**Step 1: the rodent force.** Put
\[
a_r=\mu_r+\nu,\qquad b_r=\mu_r+d_r,\qquad
\ell_r=\beta_3 I_r/N_r.
\]
At any rodent equilibrium, the last two rodent equations yield
\[
E_r=\frac{\ell_r S_r}{a_r},\qquad
I_r=\frac{\nu\ell_r S_r}{a_rb_r},\qquad
N_r=S_r\!\left(1+\ell_r\frac{b_r+\nu}{a_rb_r}\right).
\]
If \(\ell_r=0\), the unique rodent-free equilibrium is
\[
(S_r,E_r,I_r)=(\Lambda_r/\mu_r,0,0).
\]
For \(\ell_r>0\), cancellation in \(\ell_r=\beta_3 I_r/N_r\) gives
\[
a_rb_r+\ell_r(b_r+\nu)=\beta_3\nu.
\]
Thus exactly one rodent-endemic equilibrium exists if and only if
\[
\mathcal R_r=\frac{\beta_3\nu}{a_rb_r}>1,
\]
with \(\ell_r\) as in the Finding and
\[
S_r^*=\frac{\Lambda_r}{\mu_r+\ell_r},\qquad
E_r^*=\frac{\ell_r S_r^*}{a_r},\qquad
I_r^*=\frac{\nu E_r^*}{b_r}.
\]
It furnishes \(z=\beta_1\ell_r/\beta_3>0\), which does not depend on \(\Lambda_r\).

**Step 2: the exact human-force parametrization.** Let
\[
L=\beta_1 I_r/N_r+\beta_2 I_h/N_h
\]
be the **per-susceptible** human infection force (so the total incidence in the source's notation is \(LS_h\)). At a human equilibrium the exposed, infected, quarantined, and recovered equations give
\[
E_h=\frac{LS_h}{A},\quad I_h=pLS_h,\quad
Q_h=qLS_h,\quad R_h=rLS_h.
\]
Substituting the quarantine return term into the susceptible equation yields
\[
S_h=\frac{\Lambda_h}{\mu_h+D L},\qquad D=1-\tau q>0.
\]
The strict inequality follows because \(A>\gamma\) and \(C>\tau\). Consequently
\[
N_h=S_h(1+kL),\qquad
J=\frac{I_h}{N_h}=\frac{pL}{1+kL}.
\]
The human recruitment factor cancels from \(J\). Conversely, every \(L\ge0\) satisfying the force consistency equation reconstructs precisely one nonnegative human equilibrium via these formulas.

**Step 3: sharp prevalence control at the rodent-endemic equilibrium.** For the rodent-endemic branch, the consistency equation is
\[
L=z+\beta_2\frac{pL}{1+kL}.
\]
Since \(z>0\), any solution has \(L\ge z\). Rearranging gives
\[
\beta_2=\frac{(L-z)(1+kL)}{pL}
=\frac1p\left(1-kz+kL-\frac zL\right).
\]
On \([z,\infty)\), this is continuous, starts at zero, tends to infinity, and has strictly positive derivative
\[
\frac{d\beta_2}{dL}=\frac1p\left(k+\frac z{L^2}\right)>0.
\]
Hence a unique finite \(L\) exists for every \(\beta_2\ge0\), and it increases strictly with the contact rate. Because
\[
\frac{dJ}{dL}=\frac{p}{(1+kL)^2}>0,
\]
\(J\) increases continuously from \(p z/(1+kz)\) to the unattained asymptote \(p/k\). Solving \(J=pL/(1+kL)\) gives
\[
L=\frac{J}{p-kJ},
\]
and substitution into \(\beta_2=(L-z)/J\) yields
\[
\beta_2=\frac{1}{p-kJ}-\frac zJ.
\]
This proves the exact range, its sharpness, the inverse control law, and recruitment independence.

Equivalently, elimination of the denominator yields the quadratic
\[
kL^2+(1-kz-\mathcal R_h)L-z=0,
\qquad \mathcal R_h=\beta_2p.
\]
For \(z>0\), its two roots have opposite signs, so the positive solution is unique even when \(\mathcal R_h\le1\).

**Step 4: exhaustive equilibrium branches.** On the rodent-free branch, \(z=0\), and the consistency equation becomes
\[
L\,[1+kL-\mathcal R_h]=0.
\]
Thus the disease-free equilibrium always exists, and an additional human-only endemic equilibrium with
\[
L=\frac{\mathcal R_h-1}{k}>0
\]
exists exactly when \(\mathcal R_h>1\). For \(z>0\), Step 3 gives exactly one positive human equilibrium, and no human-free state is possible because \(L\ge z>0\). Combining with Step 1 gives the stated count of distinct equilibria, including equality thresholds where branches coalesce.

## Verification
The included `verification/verify.py` reconstructs the full eight-equation right-hand side over exact rational numbers and evaluates an explicit coexistence witness. With
\[
\begin{gathered}
\Lambda_h=12,\quad \mu_h=d_h=\tau=\gamma=\phi=\psi=1,\quad \delta=2,\\
\beta_1=2,\quad\beta_2=49/16,\quad
\Lambda_r=12,\quad\mu_r=d_r=1,\quad\nu=2,\quad\beta_3=6,
\end{gathered}
\]
the two branch thresholds satisfy
\[
\mathcal R_h=\frac{49}{96}<1,\qquad \mathcal R_r=2>1.
\]
The exact unique coexistence equilibrium is
\[
(S_h,E_h,I_h,Q_h,R_h;S_r,E_r,I_r)
=\left(\frac{768}{109},\frac{144}{109},\frac{96}{109},
\frac{36}{109},\frac{132}{109};\frac{24}{5},\frac{12}{5},\frac{12}{5}\right).
\]
The checker verifies that every one of the eight differential-equation right-hand sides vanishes **exactly** at this state and that
\[
L=\frac34,\quad z=\frac12,\quad
J=\frac4{49}>\frac4{65}=\frac{pz}{1+kz}.
\]
It also checks the exact zero-human-contact endpoint. These finite checks support reproducibility; the exhaustive positive-parameter proof above does not depend on them.

## Relationship to prior work
The motivating paper provides a disease-free equilibrium, an implicitly parametrized endemic equilibrium, and separate human and rodent reproduction numbers. It does **not** state the precise attainable interval for \(I_h^*/N_h^*\), a sharp non-eradicable zoonotic floor, or an exact inverse map between \(\beta_2\) and endemic infectious prevalence.

The three qualitative equilibrium types are not new as a general phenomenon. Janan, Fatmawati and Hasan (2026) explicitly classify disease-free, human-endemic, and coexistence equilibria for a **different** seven-compartment human–rodent Mpox model that includes vaccination and asymptomatic infection, and they derive a different source-specific quadratic. That established comparison is acknowledged rather than treated as novel here. Their equations and results do not imply the exact prevalence range or inverse contact law for the quarantine-return eight-compartment system analyzed here.

Omede and coauthors (2026) treat a larger system with environmental infection and additional compartments, including nonlinear mechanisms permitting backward bifurcation. Alharbi and coauthors (2026) model a distinct mass-action human–rodent system with isolated infectious humans. Neither of these distinct systems supplies the present normalized-incidence prevalence-calibration formula. Broad Mpox modeling work already emphasizes reservoir control; the contribution here is the **sharp quantitative mathematical limitation on human-contact-only control in this particular system**, including its attainable full range.

## Limitations
The theorem only describes steady states. No local/global stability of the coexistence equilibrium is asserted, and coexistence may be dynamically inaccessible for some initial conditions.

The sharp floor is conditional on \(\mathcal R_r>1\) and \(\beta_1>0\) with the rodent parameters fixed. Lowering rodent transmission below the reservoir threshold, changing the cross-species transmission rate, or changing progression/removal rates changes the bound. In particular, the theorem does **not** claim that Mpox is universally non-eradicable.

The exact inverse contact rate is a structural model identity, not an epidemiological estimate. Large-contact asymptotics should not be extrapolated outside biologically credible parameter ranges. Recruitment independence concerns equilibrium **fractions**, not infected counts, and assumes standard incidence exactly as in the published equations.

## References
1. D. A. Arhinful, A. Y. Anafo, I. Ampofi, “Stability and sensitivity analysis of transmission dynamics of Mpox virus,” *International Journal of Advances in Applied Mathematics and Mechanics* **14**(1) (2026), 108–121. DOI: 10.26541/ijaamm.2026.140110.
2. T. Janan, Fatmawati, A. Hasan, “Dynamical Analysis of Mpox Transmission Model Incorporating Asymptomatic Individuals,” *Communication in Biomathematical Sciences* **9**(1) (2026), 48–67. DOI: 10.5614/cbms.2026.9.1.4.
3. B. I. Omede, S. A. Jose, A. Jirawattanapanit, O. Boubaker, “Stability and Bifurcation Analysis of Mpox Transmission Model,” *Chaos Theory and Applications* **8**(1) (2026), 36–55. DOI: 10.51537/chaos.1740622.
4. T. D. Alharbi, M. R. Hasan, J. G. AL-Juaid, M. T. Alharthi, “Modeling Zoonotic and Human Transmission of Mpox: Stability, Bifurcation, and Control Insights,” *Mathematics* **14**(8) (2026), 1291. DOI: 10.3390/math14081291.
