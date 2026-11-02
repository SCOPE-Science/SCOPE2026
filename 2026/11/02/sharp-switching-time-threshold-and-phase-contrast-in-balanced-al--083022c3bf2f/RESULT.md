# Sharp switching-time threshold and phase contrast in balanced alternating-star SIS networks

## Finding
For each integer \(m\geq1\), take a hub and two disjoint sets of \(m\) leaves. In each half-period of length \(T>0\), the hub contacts exactly one leaf set; the sets alternate. Define
\[
 f(r)=\operatorname{arcosh}\!\left(\frac{1+\cosh r}{2}\right),\qquad \kappa=\beta\sqrt{m},\qquad q=\frac{\delta}{\kappa}.
\]
The exact disease-free Floquet multiplier is
\[
 \mathscr M=\exp\left(2[f(\kappa T)-\delta T]\right).
\]
The **global threshold classification** is as follows. If \(\delta\ge\kappa\), all initial states converge to the disease-free state. If \(\delta\le\kappa/\sqrt2\), every nonzero initial state converges in phase to a unique strictly positive \(2T\)-periodic endemic orbit. For \(\kappa/\sqrt2<\delta<\kappa\), there exists one and only one \(T_*>0\) such that
\[
 f(\kappa T_*)=\delta T_*.
\]
All states converge to the disease-free state for \(0<T\le T_*\); all nonzero states converge in phase to the unique positive orbit for \(T>T_*\). Equality at the threshold is extinct, not endemic.

The critical time obeys the sharp endpoint laws, where the parameter \(q\) varies within \((1/\sqrt2,1)\):
\[
 \kappa T_*\sim\sqrt{48\sqrt2\,(q-1/\sqrt2)}\quad(q\downarrow1/\sqrt2),\qquad
 T_*\sim\frac{\log2}{\kappa-\delta}\quad(q\uparrow1).
\]
Finally, on the unique endemic periodic orbit, let \(a\) be the common prevalence on leaves that are about to become active and \(b\) the common prevalence on leaves that are about to become inactive, both measured at a switching instant. Then
\[
 \frac ba=e^{\delta T}.
\]
This exact nonlinear phase-contrast identity is independent of infection rate and leaf-set size.

## Assumptions and scope
The model contains \(2m+1\) labeled vertices \(\{0,1,\ldots,2m\}\); vertex zero is the hub, \(L=\{1,\ldots,m\}\), \(R=\{m+1,\ldots,2m\}\). Put \(A_0\) for the adjacency matrix with edges \(0\leftrightarrow j\) for \(j\in L\), and \(A_1\) for the analogous edges with \(j\in R\). Switch deterministically with \(A(t)=A_0\) for \(2kT\le t<(2k+1)T\) and \(A(t)=A_1\) for \((2k+1)T\le t<(2k+2)T\), for every integer \(k\ge0\). On the infection cube \([0,1]^{2m+1}\), the system is
\[
 \dot x_i(t)=-\delta x_i(t)+\beta(1-x_i(t))\sum_{j=0}^{2m}A_{ij}(t)x_j(t),\qquad\beta,\delta,T>0.
\]
Solutions are continuous at switching instants. A positive periodic orbit means all its infection coordinates stay strictly positive for every real time and repeat after \(2T\). Global phase convergence means \(x(t)-x_*(t)\to0\), not merely convergence of the orbit as an unphased set. Zero is the sole disease-free solution. The time-averaged adjacency matrix has largest eigenvalue \(\sqrt{m/2}\); each single-phase star has largest eigenvalue \(\sqrt m\).

## Proof
**Linear monodromy.** The infection cube is positively invariant: at coordinate zero the derivative is nonnegative, and at coordinate one it is \(-\delta<0\). Linearizing at the origin gives the period propagator
\[
 M=e^{-2\delta T}e^{\beta T A_1}e^{\beta T A_0}.
\]
On the orthonormal coordinates \((\text{hub},|L|^{-1/2}\mathbf1_L,|R|^{-1/2}\mathbf1_R)\), \(A_0\) and \(A_1\) have only the couplings \(\sqrt m\) between the hub and the corresponding group. Let \(P\) interchange the leaf-group coordinates. With \(r=\kappa T\), set \(E_0=e^{\beta T A_0}\). Since \(e^{\beta T A_1}=PE_0P\), the unrecovered propagator is \((PE_0)^2\). Direct determinant expansion yields
\[
 \det(zI-PE_0)=(z+1)\{z^2-(1+\cosh r)z+1\}.
\]
Its positive Perron eigenvalue is \(e^{f(r)}\), since \(2\cosh f(r)=1+\cosh r\). All within-leaf-group contrast modes have linear period multiplier \(e^{-2\delta T}\). The Perron eigenvalue of the full nonnegative primitive matrix is therefore \(\mathscr M=e^{2[f(r)-\delta T]}\). Notice that \(M^2\) has strictly positive entries: every vertex can transmit to every other vertex during two periods.

**One and only one positive transition.** Differentiating the defining hyperbolic identity gives
\[
 f'(r)=\sqrt{\frac{\cosh r+1}{\cosh r+3}},\qquad f''(r)>0\ (r>0),\qquad
 \lim_{r\downarrow0}\frac{f(r)}r=\frac1{\sqrt2},\quad\lim_{r\to\infty}\frac{f(r)}r=1.
\]
Consequently \(r\mapsto f(r)/r\) increases strictly and continuously between those limits, giving the complete threshold trichotomy. Expansions \(f(r)=r/\sqrt2+r^3/(48\sqrt2)+O(r^5)\) near zero and \(f(r)=r-\log2+O(e^{-r})\) at infinity give the stated sharp \(T_*\) endpoint laws.

**Nonlinear global dichotomy.** Let \(F\) be the time-\(2T\) map. Its flow is order preserving by the cooperative comparison principle. Moreover \(F([0,1]^n)\subset[0,1]^n\), and \(F(\mathbf1)\le\mathbf1\). For every strictly positive \(z\) and \(0<a<1\),
\[
 F(az)\gg aF(z).
\]
Indeed for either active star the vector field satisfies \(g(az)-ag(z)=\beta a(1-a)\operatorname{diag}(z)A_jz\), strictly positive at its hub and active leaves; positivity propagates to all vertices during the two successive active phases. Also \(F^2(z)\gg0\) for any \(z\ge0\) with \(z\ne0\), by connectivity across successive star activations. (Here \(\gg\) denotes componentwise strict inequality.)

If \(\mathscr M>1\), let \(p\gg0\) be the Perron vector of \(M=DF(0)\). For sufficiently small \(\epsilon>0\), \(F(\epsilon p)\gg\epsilon p\). Monotone iteration from \(\epsilon p\) increases to a positive fixed point \(u\), while iteration from \(\mathbf1\) decreases to a fixed point. Strict sublinearity, together with a minimal-ratio comparison between any two positive fixed points, proves their equality and uniqueness. Each nonzero initial point enters the strictly positive cone after two periods; comparison with a small multiple of \(u\) and with \(\mathbf1\) yields convergence to \(u\). Flow continuity within each half-period promotes period-sample convergence to phase convergence to the endemic orbit.

If \(\mathscr M\le1\), nonlinear inhibition gives \(F(z)\le Mz\), with strict inequality in at least one coordinate for all \(z\gg0\). A hypothetical positive fixed point \(u\) would contradict \(w^T F(u)<w^T M u=\mathscr M w^T u\le w^T u\), where \(w\gg0\) is a left Perron vector. No nonzero boundary fixed point exists because \(F^2(z)\gg0\) for \(z\ge0\), \(z\ne0\). Thus the decreasing orbit \(F^k(\mathbf1)\) tends to zero, and order comparison forces every trajectory to zero, including at criticality.

**Phase contrast.** The transformation \((t,x)\mapsto(t+T,Px)\), with \(P\) now interchanging the actual two groups, preserves the switched system. Uniqueness of the endemic periodic orbit therefore forces \(x_*(t+T)=Px_*(t)\). Leaf permutations inside each group similarly force common within-group prevalences. If the inactive group has prevalence \(b\) at the beginning of a half-period, its members have no infected neighbors and decay exactly to \(e^{-\delta T}b\) at its end. By the half-period exchange symmetry this endpoint prevalence equals the then-inactive group's initial prevalence \(a\). Hence \(a=e^{-\delta T}b\), proving the ratio.

## Verification
A standalone numerical checker `verify.py` performs 72 full-matrix Floquet comparisons for six network sizes, three infection rates, and four residence times; finds the critical switching time for a three-vertex example; and integrates the nonlinear period map for three group sizes. The asserted phase relation holds to numerical solver precision. It requires Python, NumPy, and SciPy. The exact proofs above, not the finite computations, establish every universal and asymptotic statement. With \(m=1\), \(\beta=1\), and \(\delta=0.8\), the unique transition is \(T_*\approx3.03490842766049\), while the static average network is disease-free stable for every \(T\). At \(T=4\), the endemic switching ratio is \(e^{3.2}\approx24.53253\).

## Relationship to prior work
Persoons, Sensi, Prasse and Van Mieghem (2023/2024) develop time-varying NIMFA and analyze static-versus-dynamic timescale accuracy and convergence. Speidel, Klemm, Eguíluz and Masuda (2016) derive the general periodic temporal-network **linear** threshold in terms of a product of matrix exponentials and analyze random star-snapshot models. Those general Floquet principles underlie the linear starting point here; the matrix-product criterion itself, the qualitative advantage of slow switching, and general SIS persistence theory are not claimed as original. The contribution is the specific closed-form sharp threshold, its two endpoint laws, the global all-initial-state threshold classification at equality, and the exact finite-amplitude nonlinear switch-phase ratio for this balanced, noncommuting deterministic family. Ait Rami and coauthors (2014) study existence of periodic orbits under switching policies with different assumptions; Sanatkar and coauthors (2015) study a discrete-time probabilistic switching model. Neither inspected source supplies the same explicit combined statements for this family.

## Limitations
Only identical infection and recovery rates, two equal-size leaf sets, a common hub, exact half-period alternation, and deterministic NIMFA dynamics are treated. The epidemic threshold of a finite stochastic SIS process is not addressed; finite stochastic infection eventually goes extinct. Nonlinear periodic solutions are proved to exist and attract, but no closed form for their absolute prevalence is asserted. A broad general temporal SIS spectral formula predates this result; it implies the implicit eigenvalue computation, so any claim of independent novelty must rest on the explicit sharp classification and phase/amplitude laws rather than general Floquet methodology. Equivalent explicit treatments in unindexed literature cannot be excluded; independent audit is outstanding.

## References
1. R. Persoons, M. Sensi, B. Prasse, P. Van Mieghem, *Transition from time-variant to static networks: timescale separation in NIMFA SIS epidemics*, arXiv:2305.12446 (v1 public 21 May 2023); *Physical Review E* 109, 034308 (2024), https://arxiv.org/abs/2305.12446.
2. L. Speidel, K. Klemm, V. M. Eguíluz, N. Masuda, *Temporal interactions facilitate endemicity in the susceptible-infected-susceptible epidemic model*, arXiv:1602.00859 (2016), https://arxiv.org/pdf/1602.00859.
3. M. Ait Rami, V. S. Bokharaie, O. Mason, F. R. Wirth, *Stability criteria for SIS epidemiological models under switching policies*, *Discrete and Continuous Dynamical Systems B* 19 (2014), 2865–2887, https://doi.org/10.3934/dcdsb.2014.19.2865.
4. M. R. Sanatkar and coauthors, *Epidemic Threshold of an SIS Model in Dynamic Switching Networks*, arXiv:1501.02472 (2015), https://arxiv.org/abs/1501.02472.
