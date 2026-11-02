# Exact consensus and polarization laws for biased random-majority on bicliques

## Finding

Consider synchronous binary majority dynamics on the complete bipartite social network \(K_{a,b}\), with \(a,b\ge1\). On a strict neighbor majority a vertex deterministically adopts that opinion. On an exact neighbor tie, vertices on side \(U\) independently adopt blue with probability \(p_U\in(0,1)\), while those on side \(V\) do so with probability \(p_V\in(0,1)\). Ties at different vertices and rounds use independent coins. Initial opinions are fixed, and the two sides initially contain \(i\) and \(j\) blue vertices.

For positive integer \(m\), define the binomial strict-majority and tie probabilities
\[
 A_m(p)=\sum_{h>m/2}\binom{m}{h}p^h(1-p)^{m-h},\qquad
 B_m(p)=\mathbf1_{2\mid m}\binom{m}{m/2}p^{m/2}(1-p)^{m/2}.
\]
Put \(A=A_a(p_U)\), \(B=B_a(p_U)\), \(C=A_b(p_V)\), \(D=B_b(p_V)\), and \(\rho=BD\). Define
\[
 u_*=\frac{C+DA}{1-BD},\qquad v_*=\frac{A+BC}{1-BD},
\]
and initial-side parameters
\[
 u=\begin{cases}0&2i<a,\\1&2i>a,\\u_*&2i=a,\end{cases}\qquad
 v=\begin{cases}0&2j<b,\\1&2j>b,\\v_*&2j=b.\end{cases}
\]
These quantities are well-defined because \(0\le B,D\le\frac12\).

**Theorem.** The only recurrent classes are blue consensus, white consensus, and the deterministic period-two class that alternates fully-blue \(U\) and fully-white \(V\). From every initial coloring, the process almost surely reaches their union. Its respective probabilities of entering the three classes are exactly
\[
 \boxed{uv,\qquad(1-u)(1-v),\qquad u(1-v)+(1-u)v.}
\]
In particular, the probabilities depend on the initial blue counts only through whether each side has a strict white majority, a tie, or a strict blue majority. If \(T\) is the first time at which the coloring belongs to one of these closed classes, then for every integer \(k\ge0\),
\[
 \Pr(T>2k+2)\le\left(\mathbf1_{2i=a}+\mathbf1_{2j=b}\right)\rho^k,
 \qquad \boxed{\mathbb E T\le\frac{22}{3}.}
\]
Thus the expected time to a closed class is bounded independently of both community sizes and both tie biases, even when the biases approach \(0\) or \(1\).

**Bias phase diagram.** If \(a,b\) are even, both sides initially have equal numbers of blue and white vertices, and \(p_U,p_V\) are fixed strictly away from \(1/2\), then as both side sizes tend to infinity: if both probabilities exceed \(1/2\), blue consensus occurs with probability tending to one; if both are below \(1/2\), white consensus occurs with probability tending to one; and if they lie on opposite sides of \(1/2\), the opposing-community two-cycle occurs with probability tending to one. More precisely, let \(N=a+b\to\infty\), with even \(a,b\), \(a/N\to r\in(0,1)\), and \(p_U=1/2+\lambda_U/\sqrt N\), \(p_V=1/2+\lambda_V/\sqrt N\) for fixed real \(\lambda_U,\lambda_V\). In this critical window,
\[
 u\longrightarrow\Phi\!\left(2\lambda_V\sqrt{1-r}\right),\qquad
 v\longrightarrow\Phi\!\left(2\lambda_U\sqrt r\right),
\]
where \(\Phi\) is the standard normal distribution function. Substitution in the three exact probabilities gives their limiting transition profiles.

For instance, on \(K_{4,4}\), take \(p_U=3/4\), \(p_V=1/4\), and \(i=j=2\). Blue consensus and white consensus each occur with probability \(16281/96100\); the alternating two-cycle occurs with probability \(31769/48050\).

## Assumptions and scope

The network is a finite simple complete bipartite graph \(K_{a,b}\), where both parts are nonempty. Updates are simultaneous. Vertices inspect only *neighbors*, not their own current opinions. Both tie probabilities are constant over time and identical within a side; no assumption equates the two sides' biases. All tie coins are mutually independent. Initial configurations are deterministic. The period-two class is the pair of configurations with all \(U\) blue and all \(V\) white, and vice versa, not a stationary single configuration. The result is about hitting a *closed periodic class*, not necessarily consensus.

## Proof

Write \(X_t\) for the number of blue opinions in \(U\) and \(Y_t\) for the number in \(V\). All vertices on one side have the same opposing neighborhood. Conditioned on \((X_t,Y_t)\), the next \(U\)-count is \(0\), \(a\), or a \(\mathrm{Bin}(a,p_U)\) variable according as \(2Y_t\) is less than, greater than, or equal to \(b\); independently the next \(V\)-count is \(0\), \(b\), or \(\mathrm{Bin}(b,p_V)\), according as \(2X_t\) is less than, greater than, or equal to \(a\). This is an exact reduction from the labeled-coloring process to two counts.

At even times the \(U\)-process depends only on the original \(U\)-opinions and the tie coins on \(V\) at odd rounds and \(U\) at even rounds. The even-time \(V\)-process depends only on the original \(V\)-opinions and the complementary sets of coins. Hence the two even-time processes, and their eventual absorbing colors, are independent. This statement holds for arbitrarily correlated *fixed* initial labeling only because the initial data here are not random.

For a side initially having a strict majority of a color, the two-round update makes that whole side the same color at the next even round, and it remains so at every subsequent even round. For a tied \(U\)-side, examine the first odd \(V\)-round. Its blue count is \(\mathrm{Bin}(b,p_V)\). With probability \(C\), the \(U\)-side becomes fully blue two rounds later; with probability \(1-C-D\), it becomes fully white; with probability \(D\), its blue count is freshly \(\mathrm{Bin}(a,p_U)\). In the last case, with probabilities \(A\), \(1-A-B\), and \(B\), it is blue-majority, white-majority, or tied. Upon a strict majority the subsequent even-time configuration becomes fully that color in two further rounds; a tie restarts the same distributional problem. Therefore, if \(u_*\) denotes the final even-time blue probability from an initial tied \(U\)-side, then
\[
 u_*=C+D\bigl(A+B u_*\bigr),\qquad
 u_*=\frac{C+DA}{1-DB}.
\]
Interchanging the sides gives \(v_*=A+B(C+Dv_*)\) and the displayed formula for \(v_*\). The central binomial mass satisfies \(B_m(p)\le1/2\): it is zero for odd \(m\), and for even \(m\ge2\) its maximum occurs at \(p=1/2\) and equals \(\binom m{m/2}2^{-m}\le1/2\). Thus \(\rho\le1/4<1\). The sidewise tie-restart probabilities vanish geometrically, so each even-time process eventually reaches and retains a monochromatic side with probability one.

At sufficiently late even times both sides are monochromatic. If their colors match, the whole graph is in the corresponding fixed consensus. Otherwise the sides swap their two colors at every round, forming the claimed closed period-two class. Their independent eventual blue indicators have Bernoulli success parameters \(u\) and \(v\), which yields the three product formulas. No other recurrent class is possible because a finite-state Markov chain whose trajectories almost surely enter those three closed classes has no further closed communicating classes.

For the tail bound, if an initially tied side remains non-monochromatic at round \(2k+2\), its own count must have been exactly tied at round \(2k\); otherwise it would become monochromatic after two rounds. For its count to be tied at round \(2k\) after an initial tie, it must have passed through \(k\) successive two-round tie restarts, each with probability \(DB=\rho\). A union bound over the (at most two) initially tied sides gives \(\Pr(T>2k+2)\le(\mathbf1_{2i=a}+\mathbf1_{2j=b})\rho^k\). Summing the tail of this nonnegative integer-valued hitting time gives
\[
 \mathbb ET=\sum_{t\ge0}\Pr(T>t)
 \le2+2\sum_{k\ge0}\left(\mathbf1_{2i=a}+\mathbf1_{2j=b}\right)\rho^k
 \le2+\frac4{1-1/4}=\frac{22}{3}.
\]

For the phase diagram, if \(p\) is fixed above (respectively below) \(1/2\), the binomial strict-majority probability tends to one (respectively zero), and its tie mass tends to zero. Thus \(u_*\) tends to the limiting majority sign of the *opposite* side's tie coins, and similarly for \(v_*\). For the critical window, the binomial central limit theorem shows \(A_a(p_U)\to\Phi(2\lambda_U\sqrt r)\) and \(A_b(p_V)\to\Phi(2\lambda_V\sqrt{1-r})\); both central tie masses are \(O(N^{-1/2})\). Substitute into the exact formulas for \(u_*\) and \(v_*\). No finite enumeration is used to prove these universal statements.

## Verification

The included self-contained `biclique_biased_verifier.py` uses exact rational arithmetic and an independent absorbing-chain matrix solution on all reduced count states; it does not rely on the closed-form proof to generate the transition matrix. Execution under Python 3 with SymPy gave `PASS: 80 exact absorbing chains, 980 state/parameter comparisons; 500 tie-mass checks`, including all initial counts for \(1\le a,b\le4\) across five rational bias pairs. The verifier also reproduces the rational \(K_{4,4}\) example. These are finite cross-checks, not evidence of infinite-size proof by enumeration; infinite statements are justified algebraically above.

## Relationship to prior work

Zehmakan (2023, arXiv:2302.06760; journal version 2024) introduces the simultaneous random-majority model, proves that general graphs may have exponential stabilization time, and characterizes behavior on cycle graphs. In particular, the journal's Corollary 4.3 already obtains probabilities \(p^2\), \((1-p)^2\), and \(2p(1-p)\) for the eventual classes of an even cycle under unbiased tie choices and random initial coloring; the argument identifies even-time bipartition independence. That principle, its terminology, the existence of a blinking class, and the uniform-tie model are prior art, not claimed as novel here. The new result gives a complete deterministic-initial-state *biclique* classification with side-specific, unequal random tie probabilities, an exact binomial-hitting law, a graph-size-independent hitting-time bound and an explicit Gaussian critical bias window.

Lesfari, Giroire and Pérennes (2022) study an *asynchronous* majority model with a globally favored opinion chosen with additional probability at each selected update. This distinct update rule does not imply the synchronous tie-only formulas above. Available related work on majority coloring and parity automata addresses static or different deterministic dynamics, not these random absorption probabilities. Although no equivalent earlier biclique theorem was located in the searched sources, priority remains subject to specialist literature review.

## Limitations

The theorem does not extend automatically to incomplete bipartite networks, asynchronous dynamics, self-loops, independent per-node biases within a side, or non-tie biased updates. The critical-window conclusion needs both side sizes even and both initial sides exactly tied. The bound \(22/3\) is a uniform upper bound, not asserted to be the best possible. The literature assessment is a search-supported originality judgment, not an independent certification or a proof of priority.

## References

- A. N. Zehmakan, *Random Majority Opinion Diffusion: Stabilization Time, Absorbing States, and Influential Nodes*, arXiv:2302.06760, first public 14 February 2023. https://arxiv.org/abs/2302.06760
- A. N. Zehmakan, *Majority opinion diffusion: when tie-breaking rule matters*, Autonomous Agents and Multi-Agent Systems 38, article 21 (20 May 2024). https://doi.org/10.1007/s10458-024-09651-y
- H. Lesfari, F. Giroire and S. Pérennes, *Biased Majority Opinion Dynamics: Exploiting Graph k-domination*, Proceedings IJCAI 2022, pp. 377–383. https://doi.org/10.24963/ijcai.2022/54
