# Sharp adaptive-dispersal population ceiling for Beverton–Holt patch networks

## Finding

**Theorem (all-patch adaptive ceiling, attainability, and rigidity).** Fix an integer \(m\ge2\). For every patch \(i=1,\ldots,m\), let the Beverton–Holt reproduction function be
\[
f_i(z)=\frac{r_i z}{1+c_i z},\qquad r_i>1,\quad c_i>0,\quad z\ge0.
\]
Write
\[
A=\sum_{i=1}^m\frac{r_i+1}{c_i},\qquad
B=\sum_{i=1}^m\frac{\sqrt{r_i}}{c_i},\qquad
C=\sum_{i=1}^m\frac1{c_i},
\]
\[
h=\frac AB>2,\qquad q=\frac{h-\sqrt{h^2-4}}2\in(0,1),\qquad
K_*=\frac Bq-C,
\]
and define the optimal pre-reproduction allocation and its fractions by
\[
y_i^*=\frac{\sqrt{r_i}/q-1}{c_i}>0,\qquad p_i=\frac{y_i^*}{K_*}>0.
\]
Then \(\sum_i y_i^*=K_*\) and \(\sum_i p_i=1\). Every conservative (possibly time-varying, adaptive, history-dependent, or even nonanticipatively randomized) redistribution policy satisfies
\[
\limsup_{t\to\infty}\sum_i x_{i,t}\le K_*.
\]
The bound is sharp: the single, **time-independent rank-one stochastic matrix** \(D=p\mathbf1^{\mathsf T}\) achieves \(\sum_i x_{i,t}\to K_*\) from every nonzero nonnegative initial state. For isolated-patch carrying capacities \(K_i=(r_i-1)/c_i\),
\[
K_*\ge\sum_i K_i,\qquad
K_*=\sum_i K_i\ \Longleftrightarrow\ r_1=\cdots=r_m.
\]
The optimal pre-growth allocation is unique. In particular, any admissible policy with \(\sum_i x_{i,t}\to K_*\) necessarily has \(D_t x_t\to y^*\). All assertions are deterministic, pathwise, with no probabilistic assumptions on choices of matrices.

## Assumptions and scope

Populations are nonnegative real-valued (not integer-valued stochastic agent counts). A time step first redistributes and then reproduces:
\[
y_t=D_t x_t,\qquad x_{i,t+1}=f_i((y_t)_i),
\]
where every \(D_t\) has nonnegative entries and columns summing to one. Thus redistribution conserves total population; there are **no constraints** on migration network, movement costs, or matrix switching. A policy may use the full previous trajectory, and random policies are covered pathwise whenever the stochastic-matrix condition holds. Initially \(N_0=\sum_i x_{i,0}>0\). The claim concerns an asymptotic upper bound on total abundance and exact attainment under this unrestricted redistribution class. It does not claim the same bound is attainable under geographically constrained migration.

## Proof

**1. Scalar growth envelope.** For \(N\ge0\), define
\[
H(N)=\max_{z_i\ge0,\ \sum_i z_i=N}\sum_i f_i(z_i).
\]
The simplex is compact. Each \(f_i\) is strictly increasing and strictly concave, because
\[
f_i'(z)=\frac{r_i}{(1+c_i z)^2}>0,\qquad
f_i''(z)=-\frac{2r_i c_i}{(1+c_i z)^3}<0.
\]
Hence for every \(N>0\) the maximizing vector \(z(N)\) is unique. The envelope \(H\) is continuous and strictly increasing: scaling an optimizer to a larger total strictly raises every occupied patch's output. The ratio \(H(N)/N\) is strictly decreasing on \(N>0\): given \(N_1<N_2\), rescale an optimizer for \(N_2\) by \(N_1/N_2\) and use the strict concavity of the occupied components with \(f_i(0)=0\). Furthermore \(H(N)/N\to\max_i r_i>1\) as \(N\downarrow0\), while \(H(N)/N\to0\) as \(N\to\infty\), since \(H(N)\le\sum_i r_i/c_i\). Thus \(H\) has exactly one positive fixed point, and the scalar iteration \(v_{t+1}=H(v_t)\) converges monotonically to it for every \(v_0>0\).

**2. Exact closed form of the fixed point.** Since \(r_i>1\), the arithmetic–geometric mean inequality implies \((r_i+1)/\sqrt{r_i}>2\), and therefore \(h>2\); the smaller root \(q\) of \(q+q^{-1}=h\) belongs to \((0,1)\). Every \(y_i^*\) is strictly positive and
\[
f_i'(y_i^*)=\frac{r_i}{(\sqrt{r_i}/q)^2}=q^2.
\]
Consequently the Lagrange/KKT supporting-hyperplane condition for the strictly concave objective holds at \(y^*\): this vector uniquely maximizes \(\sum_i f_i\) at its total \(K_*=\sum_i y_i^*=B/q-C\). Direct evaluation yields
\[
\sum_i f_i(y_i^*)=\sum_i\frac{r_i-q\sqrt{r_i}}{c_i}.
\]
Subtracting \(K_*\) gives
\[
\sum_i f_i(y_i^*)-K_*=A-B(q+q^{-1})=0.
\]
Hence \(H(K_*)=K_*\). By the uniqueness just established, this is the entire positive fixed-point formula.

**3. Dominating arbitrary adaptive migration.** Conservation gives \(\sum_i (D_tx_t)_i=N_t\), hence for each history
\[
N_{t+1}=\sum_i f_i((D_tx_t)_i)\le H(N_t).
\]
Because \(H\) is increasing, induction yields \(N_t\le H^{\circ t}(N_0)\), with the right side converging to \(K_*\). This proves the universal pathwise limsup ceiling for every sequence of stochastic matrices, without any regularity or convergence requirement on the policy.

**4. A single constant policy attains the ceiling.** The rank-one matrix \(D=p\mathbf1^{\mathsf T}\) is nonnegative and column stochastic; for every state its image is \(pN_t\). The total obeys the strictly increasing scalar recursion
\[
N_{t+1}=G(N_t),\qquad G(N)=\sum_i f_i(p_iN).
\]
Now \(G(K_*)=\sum_i f_i(y_i^*)=K_*\). Strict concavity and \(G(0)=0\) imply \(G(N)/N\) strictly decreases, and \(G'(0)=\sum_i p_i r_i>1\). Thus its unique positive fixed point is \(K_*\), and all \(N_0>0\) converge monotonically to it. This also proves attainability from an arbitrary, not necessarily well-mixed initial population.

**5. Exact strict-gain criterion.** At the isolated capacities \(K_i=(r_i-1)/c_i>0\), each \(f_i(K_i)=K_i\), so \(H(K_{\mathrm{iso}})\ge K_{\mathrm{iso}}\) with \(K_{\mathrm{iso}}=\sum_iK_i\). The gradient at this allocation is \(f_i'(K_i)=1/r_i\). If all \(r_i\) coincide, this common derivative and strict concavity make \((K_i)_i\) the unique optimizer, so \(H(K_{\mathrm{iso}})=K_{\mathrm{iso}}\) and \(K_*=K_{\mathrm{iso}}\). Conversely, if any two \(r_i\) differ, a sufficiently small redistribution from the component with smaller derivative to that with larger derivative strictly increases reproduction, as all \(K_i>0\). Thus \(H(K_{\mathrm{iso}})>K_{\mathrm{iso}}\), and strict decrease of \(H(N)/N\) forces \(K_*>K_{\mathrm{iso}}\).

**6. Quantitative allocation rigidity.** For any finite \(R>0\), let
\[
\mu_R=\min_i\frac{2r_i c_i}{(1+c_iR)^3}>0.
\]
On any simplex of total \(0<N\le R\), strong concavity and the first-order optimality inequality at \(z(N)\) imply
\[
H(N)-\sum_i f_i(y_i)\ge\frac{\mu_R}{2}\sum_i(y_i-z_i(N))^2
\quad (y_i\ge0,\ \sum_i y_i=N).
\]
If \(N_t\to K_*\), then \(H(N_t)-N_{t+1}\to0\), and a fixed \(R\) bounds all sufficiently late \(N_t\). The displayed estimate implies \(D_tx_t-z(N_t)\to0\). Continuity of the unique concave optimizer on these compact simplexes gives \(z(N_t)\to z(K_*)=y^*\), proving the asserted necessity. Notice that no assertion is made about convergence of the matrices \(D_t\) themselves.

## Verification

The standalone, standard-library-only `VERIFY.py` tests the exact two-patch algebra over \(\mathbb Q(\sqrt5)\) and 245 other two-to-eight-patch cases at 65-digit precision; each case compares the closed-form equilibrium, its Lagrange multiplier, the isolated-patch carrying capacities, growth-envelope values at five relative scales, and convergence under the optimal rank-one policy. Running `python3 VERIFY.py` reports 2701 passed independent comparisons. These are finite consistency checks, **not** substitutes for the quantified analytic argument above.

For an exactly checkable example choose \((r_1,r_2)=(4,9)\) and \((c_1,c_2)=(1,1)\). Then
\[
q=\frac{3-\sqrt5}{2},\qquad
(y_1^*,y_2^*)=\left(2+\sqrt5,\frac{7+3\sqrt5}{2}\right),
\]
\[
K_*=\frac{11+5\sqrt5}{2}>11=K_{\mathrm{iso}},\qquad
(p_1,p_2)=\left(\frac{3-\sqrt5}{2},\frac{\sqrt5-1}{2}\right).
\]
Both equal marginal derivatives and the exact reproduction balance are checked by the bundled program. No general conclusion is inferred solely from this example.

## Relationship to prior work

Grumbach, Reurik, Segura, Franco and Hilker (2023) study how **constant symmetric** dispersal affects the asymptotic population of **two** source patches, including the Beverton–Holt map; the present result changes the quantifier to **every** switching/adaptive stochastic redistribution over **arbitrary finitely many** patches, gives a closed-form sharp global ceiling and an attaining stationary rank-one policy. Earlier two-patch results about benefits of mixing do not imply that even an adaptive controller cannot do better.

Bravo de la Parra (2026) establishes a broad framework for **constant asymmetric** migration, proves stability of fixed dispersal equilibria, and obtains a two-patch explicit criterion for equilibrium gains; that work includes rank-one/perfect mixing as a special case. These facts are credited here, and the present claim is **not** that such matrices or qualitative heterogeneity benefits were previously unknown. The statement evaluated as distinct is the exact unrestricted all-patch optimum, its pathwise robustness against arbitrary temporal adaptation, the sharp equal-versus-unequal intrinsic-factor criterion, and quantitative rigidity at the envelope. Its full source text was not reliably accessible for a complete line-by-line comparison, so possible hidden specialization of its general results remains a priority risk.

Arditi, Lobry and Sari (2018) treat **continuous-time** asymmetric logistic dispersal, a related but different time evolution. No claim is made about priority for elementary concavity, KKT conditions or monotone one-dimensional dynamics.

## Limitations

The outcome depends on unrestricted complete redistribution before every reproductive stage. For locally constrained migration networks, patch-specific mortality during transfer, state-dependent local growth factors, finite-population demographic noise, or migration-cost objectives, the displayed ceiling may cease to be attainable; the bound itself remains valid only while conservation and the specified local maps hold. The theorem controls the long-run *total*, not each patch population or the stationary migration matrix. A published equivalent all-policy optimization may exist; the primary 2026 general-patch source was only partially accessible through indexed sections, making specialist priority review especially appropriate. No independent external scientific audit has been performed.

## References

1. C. Grumbach, F. N. Reurik, J. Segura, D. Franco, F. M. Hilker, "The effect of dispersal on asymptotic total population size in discrete- and continuous-time two-patch models," *Journal of Mathematical Biology* **87**, 60 (2023), first public date 2023-09-21. https://doi.org/10.1007/s00285-023-01984-8 ; full text https://pmc.ncbi.nlm.nih.gov/articles/PMC10514157/.
2. R. Bravo de la Parra, "Dispersal and Total Population Size in Discrete-Time Metapopulation Models," *Mathematics* **14**(19), 3624 (2026), first published 2026-10-07. https://doi.org/10.3390/math14193624.
3. R. Arditi, C. Lobry, T. Sari, "Asymmetric dispersal in the multi-patch logistic equation," (2018). https://folia.unifr.ch/unifr/documents/306813.
