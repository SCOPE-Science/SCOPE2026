# Sharp exploration threshold and critical relaxation in bipartite anti-coordination learning

## Finding

For every pair of integers \(a,b\ge1\), positive edge reward \(J\), and common positive exploration parameter \(T\), continuous-time two-action Q-learning in the edgewise anti-coordination game on the complete bipartite graph \(K_{a,b}\) has an exact exploration boundary
\[
T_c=\frac{J\sqrt{ab}}2.
\]
Every strictly interior trajectory converges to a quantal-response equilibrium (QRE). At and above \(T_c\) the uniform mixed profile is the sole QRE. Below \(T_c\) there are exactly three: the uniform profile, a saddle, and two attracting oppositely polarized profiles. (The uniform profile is a saddle only below the boundary.) In the high-exploration regime \(T>T_c\), all log-odds trajectories contract at the **sharp** worst-case rate \(T-T_c\). Exactly at \(T=T_c\), every trajectory not on the codimension-one stable manifold converges at the sharp critical rate \(t^{-1/2}\), with explicit part-dependent leading constants. The two polarized QRE branches emerge as \((T_c-T)^{1/2}\).

## Assumptions and scope

Each agent has two pure actions, labeled 0 and 1. For each incident edge, an agent receives \(J>0\) when the two endpoint actions disagree and zero otherwise. Expected edge rewards are summed, not degree-averaged. All agents have the same positive exploration coefficient \(T\) in the continuous-time Q-learning/entropy-regularized replicator equation; the theorem concerns this deterministic ODE, **not** a discrete-time Q-table stochastic approximation or an asynchronous Glauber/logit Markov chain. Initial mixed strategies satisfy \(0<p_i(0)<1\) for every vertex. The part sizes \(a,b\) are fixed finite positive integers. Put \(z_i=\log(p_i/(1-p_i))\), so \(p_i=(1+e^{-z_i})^{-1}\). The dynamical equation is
\[
\dot z_i=-Tz_i-J\sum_{j\sim i}\tanh(z_j/2).
\tag{1}
\]
At equilibrium all first-part logits agree, say \(u\), and all second-part logits agree, say \(v\). For \(T<T_c\), let \((x_*,y_*)\) be the **unique positive solution** of
\[
Tx_*=Jb\tanh(y_*/2),\qquad Ty_*=Ja\tanh(x_*/2).
\tag{2}
\]
Then the three equilibrium logit vectors are \(0\) and \((u,v)=(x_*,-y_*),(-x_*,y_*)\). Repetitions within each part are implicit.

## Proof

**1. Derivation, bounds and strict potential.** The reward difference between choosing 1 and choosing 0 at vertex \(i\) is \(J\sum_{j\sim i}(1-2p_j)\). The standard two-action continuous-time Q-learning equation therefore gives
\[
\dot p_i=p_i(1-p_i)\left[J\sum_{j\sim i}(1-2p_j)-T\log\frac{p_i}{1-p_i}\right],
\]
which is (1) after the log-odds change of variables. Since \(|\tanh|\le1\), variation of constants yields
\[
|z_i(t)|\le e^{-Tt}|z_i(0)|+\frac{J\deg(i)}T(1-e^{-Tt});
\]
all trajectories are forward complete and bounded in logit space, hence stay uniformly interior in mixed-strategy space. Define
\[
\mathcal P(p)=J\sum_{ij\in E}\big[p_i(1-p_j)+(1-p_i)p_j\big]
+T\sum_i H(p_i),\quad H(s)=-s\log s-(1-s)\log(1-s).
\]
Then \(\partial_i\mathcal P=\dot z_i\) and
\[
\frac{d\mathcal P}{dt}=\sum_i p_i(1-p_i)(\partial_i\mathcal P)^2\ge0,
\]
with equality exactly at rest points. Bounded trajectories have omega-limit sets contained in the equilibrium set by the strict Lyapunov principle. Once the latter is shown finite, connectedness of omega-limit sets implies convergence to one point.

**2. Exact equilibrium classification.** The stationary equation (1) has identical neighbor input at every vertex in a part, so its stationary logits must be constant on each part. It becomes
\[
Tu=-Jb\tanh(v/2),\qquad Tv=-Ja\tanh(u/2).
\]
Besides \(u=v=0\), every solution has opposite nonzero signs. For \(u>0,v<0\), the positive value \(x=u\) obeys \(x=F(x)\), where
\[
F(x)=\frac{Jb}{T}\tanh\!\left(\frac{Ja}{2T}\tanh(x/2)\right),\qquad F'(0)=\frac{J^2ab}{4T^2}=\left(\frac{T_c}{T}\right)^2.
\]
The function \(F\) is strictly increasing, strictly concave for \(x>0\), bounded, and satisfies \(F(0)=0\). It has precisely one positive fixed point if \(F'(0)>1\) and none if \(F'(0)\le1\). The negative counterpart is obtained by simultaneously reversing signs. This proves the counts and establishes the finite equilibrium set.

**3. Exact stability and convergence.** Linearization at the zero vector has eigenvalues \(-T+T_c\), \(-T-T_c\), and \(-T\) repeated \(a+b-2\) times. At a polarized equilibrium the two exceptional eigenvalues are
\[
-T\pm T_c\operatorname{sech}(x_*/2)\operatorname{sech}(y_*/2),
\]
with the remaining eigenvalues equal to \(-T\). Strict concavity of \(F\) at its positive fixed point gives \(F'(x_*)<1\), equivalently \(T_c\operatorname{sech}(x_*/2)\operatorname{sech}(y_*/2)<T\); thus both polarized equilibria are linearly attracting. Below \(T_c\), zero is a hyperbolic saddle with a codimension-one stable manifold. Combined with Step 1, all trajectories converge to one of the listed QRE, and below threshold only points in that saddle's stable manifold converge to zero.

For any pair of solutions let \(d\) be their logit difference and weight part-A coordinates by \(\sqrt b\) and part-B coordinates by \(\sqrt a\). The inequality \(|\tanh(r/2)-\tanh(s/2)|\le|r-s|/2\), applied to the upper Dini derivative of the weighted maximum, gives
\[
\|d(t)\|_{w,\infty}\le e^{-(T-T_c)t}\|d(0)\|_{w,\infty},\qquad
\|d\|_{w,\infty}=\max\left\{\max_{i\in A}\frac{|d_i|}{\sqrt b},\max_{j\in B}\frac{|d_j|}{\sqrt a}\right\}.
\tag{3}
\]
This is a genuine contraction when \(T>T_c\), sharp because the linearization at zero has eigenvalue \(-(T-T_c)\) in the weighted anti-alignment direction. At equality \(T=T_c\), uniqueness of the equilibrium and the strict potential still prove global convergence to zero.

**4. Critical center direction and precise rate.** At \(T=T_c\), let
\[
q=(\sqrt b\,\mathbf1_A,-\sqrt a\,\mathbf1_B),\qquad q\cdot q=2ab,
\]
and normalize the critical center amplitude by \(s=(q\cdot z)/(2ab)\). The linearized field has one zero eigenvalue along \(q\) and all remaining eigenvalues equal to \(-T_c\) or \(-2T_c\). The odd vector field and the smooth equivariant one-dimensional center-manifold theorem provide a local graph \(z=sq+h(s)\), with \(h(s)\perp q\), \(h(s)=O(s^3)\). Using \(\tanh(w/2)=w/2-w^3/24+O(w^5)\), the projection of the cubic term yields
\[
\dot s=-\kappa s^3+O(s^5),\qquad
\kappa=\frac{J\sqrt{ab}(a+b)}{48}=\frac{T_c(a+b)}{24}>0.
\tag{4}
\]
The coefficient follows by computing \(J(q_A\sum_B q_B^3+q_B\sum_A q_A^3)/(24q\cdot q)\), where the two summands include all vertices in their respective parts; the result is \(-\kappa\). Exponential tracking of the center manifold implies that every trajectory outside the full stable manifold of zero has a nonzero eventually signed center coordinate obeying \(s(t)\sim\sigma(2\kappa t)^{-1/2}\), with \(\sigma\in\{-1,1\}\). Therefore, for every first-part vertex and second-part vertex respectively,
\[
\begin{aligned}
z_i(t)&=\sigma\sqrt b\sqrt{\frac{12}{T_c(a+b)t}}+o(t^{-1/2}), &&i\in A,\\
z_j(t)&=-\sigma\sqrt a\sqrt{\frac{12}{T_c(a+b)t}}+o(t^{-1/2}), &&j\in B.
\end{aligned}
\tag{5}
\]
The stable-manifold exceptional trajectories decay exponentially, so no universal two-sided \(t^{-1/2}\) estimate is asserted for them. Finally, with \(\mu=T_c-T>0\), the parameter-dependent center equation has \(\dot s=\mu s-\kappa s^3+O(\mu s^3+s^5)\). The polarized equilibrium logits consequently satisfy
\[
x_*=\sqrt b\sqrt{\frac{24(T_c-T)}{T_c(a+b)}}+O((T_c-T)^{3/2}),\qquad
y_*=\sqrt a\sqrt{\frac{24(T_c-T)}{T_c(a+b)}}+O((T_c-T)^{3/2}).
\tag{6}
\]
The errors hold as \(T\uparrow T_c\) for fixed \(a,b,J\). This completes the integrated phase-portrait theorem.

## Verification

The included `verify.py` uses only the Python standard library. Run `python3 verify.py` to check random full-network reward-gradient identities and the entropy potential, the high-temperature contraction inequality on several irregular and regular part sizes, numerical positive-branch equations and the square-root onset, the critical asymptotic coefficients, and 100 independent numerical cubic-projection identities. Its finite checks are supplementary evidence; existence, uniqueness, global convergence, sharpness and the infinite families are established by the proof above.

## Relationship to prior work

The exact Q-learning ODE and broad network-learning motivation are from Hussain and Belardinelli [1]. That work studies a random-payoff ensemble and derives a stability boundary under regularity and large-action assumptions; it does not provide the present deterministic, finite, possibly irregular complete-bipartite phase portrait or time-resolved critical coefficient. Hussain, Leonte, Belardinelli and Piliouras [2] give a general **sufficient** high-exploration criterion involving the maximum graph degree; that theorem does not imply sharp necessity, a three-QRE region, or the critical \(t^{-1/2}\) law. Bipartite Curie–Weiss equilibrium/statistical-mechanics results [3,4] already describe related static symmetry breaking and quartic critical fluctuations; static magnetization statements are **not claimed new** here and do not by themselves yield deterministic Q-learning basins or the time-asymptotic coefficient. Auletta et al. [5] analyze a **discrete-time stochastic all-logit Markov chain**, not equation (1). Existing QRE uniqueness work [6] also establishes broad static sufficient conditions. Ansah [7] analyzes a bipartite mean-field **Glauber spin-flip** dynamics in 2026 and gives a one-to-three stationary-state transition with local stability; that covers a related static phase-portrait component but its macroscopic vector field is \(\dot m_i=2\sinh(A_i)-2m_i\cosh(A_i)\), not the continuous-time Q-learning logit dynamics (1), and it does not give (3) or the logit-based critical coefficient in (5). The specific claim here is the unified sharp finite-network deterministic learning theorem, notably its critical time law and rate sharpness; specialist-priority uncertainty remains.

## Limitations

This theorem assumes identical positive temperatures, symmetric two-action mismatch payoffs, complete bipartite interactions, deterministic continuous-time QLD, and strictly interior initial profiles. It does not cover arbitrary payoff matrices, asynchronous random updates, discrete-time Q-table learning, degree-normalized payoff conventions, boundary initial conditions, heterogeneous exploration, or finite-population stationary noise. The critical-center analysis uses standard smooth center-manifold and tracking results and establishes leading orders, not an explicit globally uniform error term. No independent external audit or publication-priority certification has been performed.

## References

1. A. Hussain and F. Belardinelli, *Stability of Multi-Agent Learning in Competitive Networks: Delaying the Onset of Chaos*, arXiv:2312.11943 (first public version, 2023-12-19). https://arxiv.org/abs/2312.11943
2. A. Hussain, D. Leonte, F. Belardinelli and G. Piliouras, *Stability of Multi-Agent Learning: Convergence in Network Games with Many Players*, arXiv:2307.13922 (2023-07-26). https://arxiv.org/abs/2307.13922
3. M. Fedele and F. Unguendoli, *Rigorous Results on the Bipartite Mean-Field Model*, arXiv:1204.4420 (2012). https://arxiv.org/html/1204.4420v2
4. M. Fedele, *Rescaled Magnetization for Critical Bipartite Mean-Fields Models*, arXiv:1310.7615 (2013). https://arxiv.org/abs/1310.7615
5. V. Auletta, D. Ferraioli, F. Pasquale, P. Penna and G. Persiano, *Logit Dynamics with Concurrent Updates for Local Interaction Games*, arXiv:1207.2908 (2012; revision 2013). https://arxiv.org/html/1207.2908v4
6. E. Melo, *On the Uniqueness of Quantal Response Equilibria and Its Application to Network Games*, Economic Theory 74 (2022), 681–725, DOI:10.1007/s00199-021-01385-2. https://doi.org/10.1007/s00199-021-01385-2
7. R. K. Ansah, *Macroscopic dynamics and phase transitions in a bipartite mean-field model with averaged coupling*, AIP Advances 16, 055006 (2026-05-07), DOI:10.1063/5.0331428. https://doi.org/10.1063/5.0331428
