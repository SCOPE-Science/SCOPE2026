# Three boundary-layer regimes for heteroscedastic Gaussian martingale transport

## Finding

The minimal nontrivial one-step martingale selection problem (two initial atoms and three terminal atoms) has an exact heteroscedastic Gaussian optimization law. Its optimizer undergoes a **three-way change of boundary-layer scale** when terminal endpoint mass crosses \(p=3/4\): an exponentially small conditional mass, a critical \(\sqrt{\log R}/R\) mass, and a regular \(1/R\) displacement. The transition occurs even though every finite \(R>0\) has a unique strictly positive martingale coupling.

For \(p\in(1/2,1)\), let
\[
\mu=\tfrac12\delta_{-1/2}+\tfrac12\delta_{1/2},\qquad
\nu_p=\tfrac p2\delta_{-1}+(1-p)\delta_0+\tfrac p2\delta_1.
\]
The state-dependent Gaussian references have distributions \(q_{-1/2}=N(-1/2,R^2)\) and \(q_{1/2}=N(1/2,1)\), with \(R>0\). A martingale coupling \(\pi\) is chosen by minimizing
\[
\mathcal I_R(\pi)=\tfrac12W_2^2(\pi_{-1/2},q_{-1/2})+\tfrac12W_2^2(\pi_{1/2},q_{1/2}).
\]
Write \(H=p-1/2\), and let \(\varphi\) and \(\Phi\) denote the standard normal density and distribution function. Set
\[
 g(t)=\varphi(\Phi^{-1}(t))+\varphi(\Phi^{-1}(t+1/2)),\quad 0<t\le1/4,
 \qquad c=\frac2{\varphi(\Phi^{-1}(3/4))}.
\]

**Theorem.** The unique optimum has conditional probability vectors, in terminal order \((-1,0,1)\),
\[
\pi_{-1/2}=(1/2+r_R,\;1/2-2r_R,\;r_R),\qquad
\pi_{1/2}=(s_R,\;1/2-2s_R,\;1/2+s_R).
\]
Here \(r_R+s_R=H\), both variables lie strictly between \(0\) and \(1/4\), and the unique value of \(r_R\) solves
\[
 Rg'(r_R)=g'(s_R),\qquad
 g'(t)=-\Phi^{-1}(t)-\Phi^{-1}(t+1/2).
\]
The function \(R\mapsto r_R\) is strictly increasing and \(r_1=s_1=H/2\). The exact large-\(R\) transition is
\[
\begin{array}{ll}
\displaystyle\lim_{R\to\infty}\frac{\log(1/s_R)}{R^2}=\frac{g'(H)^2}{2},
&1/2<p<3/4,\\[1ex]
\displaystyle\lim_{R\to\infty}\frac{R s_R}{\sqrt{2\log R}}=\frac1c,
&p=3/4,\\[1ex]
\displaystyle\lim_{R\to\infty}R(1/4-r_R)=\frac{g'(H-1/4)}c,
&3/4<p<1.
\end{array}
\]
The first regime is logarithmically exact: it asserts a sharp Gaussian exponential decay rate, not a multiplicative asymptotic for \(s_R\).

## Assumptions and scope

All probability measures are on the real line. The parameter \(p\) is strictly between \(1/2\) and \(1\); \(R\) is finite and strictly positive. The Wasserstein distances are ordinary quadratic Wasserstein distances. The martingale constraint means \(\mathbb E[M_1\mid M_0]=M_0\), with first marginal \(\mu\) and terminal marginal \(\nu_p\). Both reference Gaussians are centered at their corresponding initial states. No limiting claims are made at \(p=1/2\), \(p=1\), or at \(R=0\), where coupling faces or reference regularity change.

## Proof

**1. Exact coupling polytope.** A conditional law on \((-1,0,1)\) with mean \(-1/2\) is necessarily \((1/2+r,1/2-2r,r)\), with \(0\le r\le1/4\). At initial state \(+1/2\), its analogue is \((s,1/2-2s,1/2+s)\), with \(0\le s\le1/4\). The terminal marginal constraint is exactly \(r+s=H\), where \(H=p-1/2\). Thus every feasible martingale coupling is described by
\[
 r\in[\max(0,H-1/4),\min(H,1/4)],\quad s=H-r.
\]
This interval has positive length for every stipulated \(p\).

**2. Exact Gaussian objective.** Let \(Z\sim N(0,1)\). One-dimensional quadratic optimal transport is the common-quantile coupling. For a row with masses \((\ell,m,h)\) on \((-1,0,1)\), its maximal covariance with \(Z\) is
\[
\int_0^1Q_{(\ell,m,h)}(u)\Phi^{-1}(u)\,du
=\varphi(\Phi^{-1}(\ell))+\varphi(\Phi^{-1}(h)).
\]
This follows by integrating \(z\varphi(z)\) over the lower and upper normal tails. For the first and second rows it equals \(g(r)\) and \(g(s)\), respectively. On expanding squared costs, all terms other than the Gaussian covariance are independent of the feasible coupling because both its terminal marginal and conditional means are fixed. Therefore
\[
\mathcal I_R(\pi)=C_{p,R}-R g(r)-g(s)
\]
for a constant \(C_{p,R}\) independent of \(r\). The optimization reduces exactly to maximizing \(F_R(r)=Rg(r)+g(H-r)\) over the displayed interval.

**3. Strict concavity and the unique optimizer.** With \(z_t=\Phi^{-1}(t)\), differentiation gives
\[
 g'(t)=-z_t-z_{t+1/2},\qquad
 g''(t)=-\frac1{\varphi(z_t)}-\frac1{\varphi(z_{t+1/2})}<0.
\]
For \(0<t<1/4\), \(g'(t)>0\), and \(g'(1/4)=0\), while \(g'(t)\to\infty\) as \(t\downarrow0\). At the left feasible endpoint the one-sided derivative \(F_R'\) is positive; at the right endpoint it is negative. Strict concavity therefore yields a unique interior maximizer and the claimed first-order equation. Differentiating that equation implicitly gives
\[
 \frac{dr_R}{dR}=\frac{-g'(r_R)}{R g''(r_R)+g''(s_R)}>0.
\]
At \(R=1\) symmetry forces \(r_1=s_1=H/2\).

**4. End-point asymptotics.** Standard Gaussian tail estimates (equivalently the Mills-ratio bound) give
\[
 g'(t)=\sqrt{2\log(1/t)}\,(1+o(1))\quad(t\downarrow0).
\]
At the other endpoint \(g'(1/4-t)=ct+O(t^2)\), with \(c=-g''(1/4)=2/\varphi(\Phi^{-1}(3/4))\). These are the only nonuniform estimates needed.

For \(H<1/4\), the first-order equation and strict monotonicity force \(r_R\uparrow H\), hence \(s_R\downarrow0\); otherwise the left side would diverge and the right side would remain bounded. Now \(g'(r_R)\to g'(H)>0\), so \(g'(s_R)/R\to g'(H)\). Squaring the normal-quantile asymptotic proves the first limit.

For \(H=1/4\), the same equation forces \(s_R\downarrow0\), while \(r_R=1/4-s_R\). Hence
\[
 Rc s_R(1+o(1))=\sqrt{2\log(1/s_R)}(1+o(1)).
\]
Taking logarithms first shows \(\log(1/s_R)/\log R\to1\); substitution gives the second limit.

For \(H>1/4\), the quantity \(s_R\ge H-1/4>0\) stays away from zero. The first-order equation forces \(r_R\uparrow1/4\), with \(s_R\to H-1/4\). Setting \(t_R=1/4-r_R\), the two endpoint expansions give \(Rc t_R\to g'(H-1/4)\), which is the third limit.

These alternatives cover every \(p\in(1/2,1)\). No appeal to finite-sample verification is used to infer an infinite asymptotic.

## Verification

Run `python verify.py` with Python 3 and SciPy. The program checks 255 exact rational parameter-row cases, 93 numerical objective comparisons against a direct Gaussian integration of the Wasserstein cost, the first-order equation, strict concavity, swap symmetry, and the critical-scale trend. The critical predicted constant is approximately \(0.158888286342\). These checks are reproducibility aids; the proof of all quantifiers and limits is analytical.

## Relationship to prior work

Marini (arXiv:2610.20920v1, sections 1–3 and 5) introduces the state-dependent \(q_x\)-Bass weak martingale transport objective, establishes a general duality/existence framework and a fixed-point algorithm, and proves uniqueness under its hypotheses. The present theorem keeps that objective but explicitly resolves a canonical finite-support family and its three distinct large-heteroscedasticity scales. General uniqueness alone does not specify which martingale atoms vanish, or the exponential/critical/algebraic boundary laws.

Acciaio and Marini (arXiv:2607.15872v1 and arXiv:2609.07351v1) study semidiscrete and general one-dimensional **state-independent** \(q\)-Bass problems, respectively; their reported existence, stability and fixed-point results are relevant antecedents but do not, at the level of their accessible abstracts, specify this state-dependent Gaussian-variance phase diagram. Their full texts could not be inspected here; overlap with an implicit example must be checked before external priority claims. The quantified asymptotic trichotomy, not general Bass optimality or Gaussian-quantile coupling, is the mathematical claim.

## Limitations

The result is a solvable two-initial/three-terminal-state calibration family, not a general universality theorem for arbitrary atomic marginals. The exponentially small regime supplies a log-equivalent sharp rate, not an exact pre-exponential constant. The reference Gaussians have a particular state-dependent variance ratio; non-Gaussian references can give other boundary layers. Literature coverage is qualified because the full texts of the two most relevant predecessor preprints were inaccessible; no claim of independent audit or publication priority is made.

## References

1. Antonio Marini, *\(q_x\)-Bass Martingales: Optimality, Existence and Convergence*, arXiv:2610.20920v1 (first publicly submitted 2026-10-14), https://arxiv.org/abs/2610.20920.
2. Beatrice Acciaio and Antonio Marini, *Existence of \(q\)-Bass martingales in the semidiscrete setting*, arXiv:2607.15872v1 (2026), https://arxiv.org/abs/2607.15872.
3. Beatrice Acciaio and Antonio Marini, *Fixed Points for the \(q\)-Bass Martingale: Existence, Stability, and Convergence*, arXiv:2609.07351 (2026), https://arxiv.org/abs/2609.07351.
4. Bertram Tschiderer, *\(q\)-Bass martingales*, arXiv:2402.05669 (2024), https://arxiv.org/abs/2402.05669.
