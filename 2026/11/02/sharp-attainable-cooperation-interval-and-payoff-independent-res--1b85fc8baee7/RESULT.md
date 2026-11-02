# Sharp attainable cooperation interval and payoff-independent resource fates at carrying capacity

## Finding
Fix the rich-resource payoff matrix of the finite-capacity two-strategy eco-evolutionary game model. Across all positive depleted-resource payoff matrices, the possible terminal cooperator fractions form an **exact, sharp, open interval** determined solely by the initial numbers of cooperators and defectors. This gives a necessary-and-sufficient criterion for guaranteeing environmental recovery or exhaustion **independently of the game played in the depleted environment**.

Let \(C_0=N_0x_0\), \(D_0=N_0(1-x_0)\), \(a=C_0/K\), \(b=1-D_0/K\), and \(\rho=1/(1+\theta)\). Holding the positive rich-resource payoff matrix \(U_1\) fixed while varying any strictly positive depleted-resource payoff matrix \(U_0\), the full set of terminal cooperator fractions is
\[
\{x_\infty(U_0): U_0\in(0,\infty)^{2\times2}\}=(a,b).
\]
For any particular matrix, the environmental limit satisfies
\[
n_\infty=\begin{cases}1,&x_\infty>\rho,\\0,&x_\infty<\rho,\\\text{a number strictly between }0\text{ and }1,&x_\infty=\rho.\end{cases}
\]
Therefore \(\rho\le a\) guarantees complete recovery for **every** positive depleted-state payoff matrix; \(\rho\ge b\) guarantees complete exhaustion for **every** such matrix. If \(a<\rho<b\), the choice of positive depleted-state payoffs can instead produce **all three** environmental limit types with identical fixed initial data and rich-state payoffs. The weak inequalities at the universal-outcome boundaries are essential.

## Assumptions and scope
Take \(K>0\), \(\varepsilon>0\), \(\theta>0\), \(0<N_0<K\), and \(0<x_0,n_0<1\). Both \(2\times2\) payoff matrices have strictly positive entries. Write \(B(n)=(1-n)U_0+nU_1\), \(v=(x,1-x)^\mathsf T\), \(F_C=(B(n)v)_1\), \(F_D=(B(n)v)_2\), and \(\bar F=xF_C+(1-x)F_D\). The equations, directly in the normalization of the underlying finite-capacity model, are
\[
\dot N=N(1-N/K)\bar F,\quad
\dot x=x(1-x)(1-N/K)(F_C-F_D),\quad
\dot n=\varepsilon((1+\theta)x-1)n(1-n).
\]
The fixed matrix \(U_1\) may, in particular, be any strictly positive prisoner's-dilemma matrix. No smallness assumption on \(\varepsilon\) is used. The claim concerns this *deterministic* model, not stochastic fixation or models with adult turnover, negative payoffs, intrinsic resource renewal, or resource-dependent carrying capacity.

## Proof
**1. Positive strategy numbers and an exponential density deficit.** Set \(C=Nx\) and \(D=N(1-x)\). Direct differentiation gives the exact identities
\[
\dot C=C(1-N/K)F_C,\qquad \dot D=D(1-N/K)F_D.
\]
If \(m>0\) is the minimum of the eight payoff entries, then \(F_C,F_D,\bar F\ge m\) on the invariant domain. Because \(0<N_0<K\), one has \(N_0\le N(t)<K\), with \(N(t)\) increasing and
\[
0<K-N(t)\le(K-N_0)\exp(-mN_0t/K).
\]
Thus \(N\to K\), whereas \(C,D\) increase strictly and converge to positive limits \(C_\infty>C_0\), \(D_\infty>D_0\) whose sum is \(K\). Necessarily
\[
a=C_0/K<x_\infty=C_\infty/K<1-D_0/K=b.
\]
Moreover, after time \(t\) at most \(K-N(t)\) individuals can be added. With \(0\le C_\infty-C(t)\le K-N(t)\), the identity \(x(t)=C(t)/N(t)\) gives
\[
|x_\infty-x(t)|\le(K-N(t))/K.
\]
In particular \(\int_0^\infty|x(t)-x_\infty|\,dt<\infty\).

**2. Complete environmental classification.** The resource log-odds \(\ell(t)=\log(n(t)/(1-n(t)))\) obeys
\[
\dot\ell=\varepsilon(1+\theta)(x(t)-\rho),\qquad \rho=(1+\theta)^{-1}.
\]
If \(x_\infty\ne\rho\), the integral on the right diverges with the sign of \(x_\infty-\rho\), forcing the resource to \(1\) or \(0\). If \(x_\infty=\rho\), the integrability established in Step 1 makes \(\ell(t)\) converge to a finite real number, so \(n_\infty\) is strictly interior. This proves convergence of all three state variables.

**3. Sharp attainability without fixing \(U_1\).** First let both environmental matrices have the same two constant rows, \(U_0=U_1=\begin{pmatrix}c&c\\d&d\end{pmatrix}\), with \(c,d>0\). Introduce \(s(t)=\int_0^t(1-N(u)/K)\,du\). Then \(C=C_0e^{cs}\), \(D=D_0e^{ds}\). For any desired \(z\in(a,b)\), choose \(c=\log(Kz/C_0)>0\) and \(d=\log(K(1-z)/D_0)>0\). At the limiting effective time \(s_\infty=1\), \(C_0e^c+D_0e^d=K\), yielding \(x_\infty=z\). The interval's endpoints cannot be attained because both strategy numbers grow strictly.

**4. The same attainability with an arbitrary preassigned positive \(U_1\).** This strengthening is not obtained by altering the rich-state game. For each \(q>0\) and scale \(L>0\), take
\[
U_0(L,q)=L\begin{pmatrix}q&q\\1&1\end{pmatrix}.
\]
Put \(\tau=Lt\). For every finite interval of \(\tau\), as \(L\to\infty\) the state \(n(\tau/L)\) converges uniformly to \(n_0\), and the \(U_1/L\) contribution to the count equations disappears. Continuous dependence on the ODE therefore gives the frozen-resource limiting count system
\[
\frac{dC}{d\tau}=(1-n_0)(1-N/K)qC,\qquad
\frac{dD}{d\tau}=(1-n_0)(1-N/K)D.
\]
Let \(s_q>0\) be the unique solution of \(C_0e^{qs_q}+D_0e^{s_q}=K\). Its terminal cooperator fraction is \(\Psi(q)=C_0e^{qs_q}/K\). The function \(\Psi\) is continuous, with \(\Psi(q)\to a\) as \(q\downarrow0\) and \(\Psi(q)\to b\) as \(q\to\infty\). For fixed \(q\), convergence on compact fast-time intervals together with the tail bound \(|x_\infty-x(t)|\le(K-N(t))/K\) shows
\[
\lim_{L\to\infty}x_\infty(U_0(L,q))=\Psi(q).
\]
Indeed, first run the frozen count system long enough that its remaining distance from capacity is arbitrarily small; for sufficiently large \(L\), the actual count system is arbitrarily close at that finite fast time, and the remaining total capacity bounds any further change in its terminal frequency. For fixed finite \(L\), \(q\mapsto x_\infty(U_0(L,q))\) is continuous on every compact subinterval of \((0,\infty)\): finite-time ODE dependence is continuous, and the exponential capacity-deficit estimate is uniform there. Given \(z\in(a,b)\), choose \(q_-\) and \(q_+\) with \(\Psi(q_-)<z<\Psi(q_+)\). For sufficiently large common \(L\), the actual terminal fractions retain these strict inequalities; the intermediate-value theorem provides a positive \(q\) for which \(x_\infty=z\). This proves the claimed exact attainable interval with \(U_1\) *fixed*.

**5. Sharp resource-fate trichotomy.** Every attainable terminal fraction lies strictly between \(a\) and \(b\), and every number in this interval is attained with the same \(U_1\). Combine this with Step 2. If \(\rho\le a\), all solutions recover. If \(\rho\ge b\), all exhaust. If \(a<\rho<b\), choose attainable terminal fractions below, equal to, and above \(\rho\) to produce exhaustion, an interior limiting resource, and recovery respectively. None of the three cases can be enlarged without losing the asserted universal property.

## Verification
A self-contained Python checker (`verify.py`) verifies symbolically the two count identities for general symbolic payoff matrices, checks exact algebraic constant-row examples on both sides of the resource threshold, and verifies an exact nonstationary example with terminal cooperator fraction at the threshold. It also integrates two examples with *the same fixed rich-state prisoner's-dilemma matrix* and opposite depleted-state selection, demonstrating different resource outcomes. The proof above covers all parameters; these finite checks are not used as a substitute for its limit and reachability arguments. Run `python verify.py` with Python, NumPy, SciPy and SymPy.

## Relationship to prior work
The originating finite-capacity model and its three evolution equations appear in Bairagya et al., arXiv:2109.14971v1, Section II (equations (5), (8)–(10) in the preprint's PDF), and its resource-bistability regimes are investigated numerically in Sections III–IV. Those analyses identify the influence of initial conditions and carrying capacity but do not give an all-payoff sharp attainable interval with an independently fixed rich-resource game or the exact universal initial-density criteria proved here. Weitz et al. (2016) study feedback games in which population density is not an independent logistic growth variable, so their oscillatory limit sets cannot imply this density-deficit reachability theorem. Argasinski and Broom (2017) analyze more general evolutionary stability and turnover with birth and death; this is related conceptually but does not impose the two nondecreasing population counts required for the sharp interval construction. Bairagya et al. (2022) study a self-renewing resource with death/harvesting feedback and a different population model; it does not contain this fixed-capacity, no-turnover family as an exact stated special case.

## Limitations
The all-payoff attainable set presumes \(U_0\) can vary over **every strictly positive** matrix; fixing its social-dilemma class or bounding its entries can shrink the attainable interval. The rich-state matrix is fixed but must have strictly positive entries. This continuous deterministic model has no turnover after capacity is reached; allowing death, mutation, additional resource renewal, a changing carrying capacity, or negative fitness can invalidate the monotone-count argument. The environmental outcome criterion describes infinite-time limits and does not estimate finite-horizon recovery times. Positive initial cooperator and defector populations and a strictly interior initial environmental state are required. Bibliographic equivalence with an unindexed specialization of a general positive-growth theorem cannot be ruled out by database searches alone.

## References
1. J. D. Bairagya, S. S. Mondal, D. Chowdhury, S. Chakraborty, *Game-environment feedback dynamics in growing population: Effect of finite carrying capacity*, arXiv:2109.14971v1 (first public 2021-09-30), Physical Review E 104, 044407 (2021). https://arxiv.org/abs/2109.14971
2. J. S. Weitz, C. Eksin, K. Paarporn, S. P. Brown, W. C. Ratcliff, *An oscillating tragedy of the commons in replicator dynamics with game-environment feedback*, PNAS 113, E7518–E7525 (2016). https://pmc.ncbi.nlm.nih.gov/articles/PMC5127343/
3. K. Argasinski, M. Broom, *Evolutionary stability under limited population growth: Eco-evolutionary feedbacks and replicator dynamics*, Ecological Complexity (2017). https://www.staff.city.ac.uk/mark.broom/AB17ECOCOM.pdf
4. J. D. Bairagya, S. S. Mondal, D. Chowdhury, S. Chakraborty, *Eco-evolutionary games for harvesting self-renewing common resource: Effect of growing harvester population*, arXiv:2205.04877 (2022). https://arxiv.org/abs/2205.04877
