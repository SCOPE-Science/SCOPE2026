# A sharp carrying-capacity switch for proportional-payoff evolutionary resource games

## Finding

The proportional-payoff subclass of a growing-population environmental-feedback game admits a complete, exact carrying-capacity phase transition. In particular, for an initially cooperative enough population, a single explicit critical carrying capacity separates eventual full preservation of a shared resource from eventual complete depletion, *even though defection is strictly dominant at every nonterminal time*.

**Theorem.** Let \(M=\begin{pmatrix}R&S\\T&P\end{pmatrix}\) satisfy \(T>R>P>S>0\), take \(\alpha_0,\alpha_1,\epsilon,\theta>0\), \(0<N_0<K\) and \(0<x_0,n_0<1\). The game and equations in the next section have a unique global solution. Define
\[
 b=P-S,\quad a=T-R,\quad d(x)=b+(a-b)x,\quad
 \Phi(x)=\frac{x^{P/b}d(x)^{1+R/a-P/b}}{(1-x)^{R/a}},\quad
 x_c=\frac1{1+\theta}.
\]
Then population increases to \(K\), while cooperator frequency decreases to the unique \(x_\infty\in(0,x_0)\) solving
\[
 K\Phi(x_\infty)=N_0\Phi(x_0).
\]
If \(x_0\le x_c\), the common resource tends to zero. If \(x_0>x_c\), let
\[
 \boxed{K_c=N_0\frac{\Phi(x_0)}{\Phi(x_c)}>N_0.}
\]
For \(N_0<K<K_c\), \(n(t)\to1\). For \(K=K_c\), the resource increases strictly and converges to some \(n_*\in(n_0,1)\). For \(K>K_c\), it increases strictly until the **unique** time \(N(t)=K_c\), decreases strictly afterward, and converges to zero. Hence the final resource level as a function of \(K\) jumps from \(1\) to \(0\), with a nontrivial interior value at its critical point. Both the capacity threshold and the location of the unique maximum are independent of \(n_0,\epsilon,\alpha_0,\alpha_1\). All these statements hold for every admissible initial point, not merely generic ones.

**Exact calibration.** For \(M=\begin{pmatrix}3&1\\4&2\end{pmatrix}\), \(U_0=M/2,U_1=M\), \(\epsilon=1/2,\theta=1,N_0=1,x_0=3/4,n_0=1/2\), the invariant and threshold simplify to
\[
 \frac{Nx^2}{(1-x)^3}=36,\qquad K_c=18.
\]
At the critical capacity define
\[
 J=\log 2+\frac12\log\frac{17}{20}-\arctan\frac29,\qquad L=e^J.
\]
The limiting common-resource value is exactly
\[
 \boxed{n_*=\frac{4L+1-\sqrt{8L+1}}{4L}=0.563817739263549\ldots.}
\]

## Assumptions and scope

The population state is \(N(t)\), the cooperator fraction is \(x(t)\), and normalized common-resource level is \(n(t)\). The environmentally modulated payoff matrix is
\[
 U(n,N)=\left(1-\frac NK\right)[(1-n)\alpha_0+n\alpha_1]M.
\]
Write \(g(n)=\alpha_0+(\alpha_1-\alpha_0)n\), \(f_C(x)=Rx+S(1-x)\), \(f_D(x)=Tx+P(1-x)\), \(d(x)=f_D(x)-f_C(x)=b+(a-b)x\), and \(W(x)=xf_C(x)+(1-x)f_D(x)\). The full equations are
\[
 \begin{aligned}
 \dot N&=N\left(1-\frac NK\right)g(n)W(x),\\
 \dot x&=-\left(1-\frac NK\right)g(n)x(1-x)d(x),\\
 \dot n&=\epsilon[(1+\theta)x-1]n(1-n).
 \end{aligned}
\]
Both endpoints of the environmental payoff interpolation are positive multiples of one fixed strict Prisoner's-dilemma matrix. Thus the *ranking* of strategic payoffs never changes, although their magnitudes can change with the common resource. We do not assume any linearization or timescale separation. The theorem concerns interior initial states and fixed finite \(K>N_0\).

## Proof

**1. Positivity, convergence, and the invariant.** All factors are smooth on the closed biological box \([0,K]\times[0,1]\times[0,1]\); its faces are invariant, so an interior trajectory exists globally and remains interior at all finite times. Because all entries of \(M\) are strictly positive, \(W(x)\ge m>0\) on \([0,1]\). Also \(g(n)\ge g_->0\) and \(d(x)>0\) on \([0,1]\). Thus \(N(t)\) increases to \(K\). More precisely, for \(u(t)=1-N(t)/K\),
\[
 \dot u=-\frac{N}{K}\,g(n)W(x)u\le -\frac{N_0}{K}g_-m\,u,
\]
so \(u(t)\to0\) exponentially. Meanwhile \(x(t)\) decreases strictly and has a limit.

For \(0<x<1\), divide the first equation by the second to obtain
\[
 \frac{d\log N}{dx}=-\frac{W(x)}{x(1-x)d(x)}.
\]
The key *exact* partial fraction identity, valid for all \(T>R>P>S>0\), is
\[
 \frac{W(x)}{x(1-x)d(x)}
 =\frac{P/b}{x}+\frac{R/a}{1-x}
 +\left(1+\frac Ra-\frac Pb\right)\frac{a-b}{d(x)}.
\]
It integrates to \(d\log\Phi(x)/dx=W(x)/[x(1-x)d(x)]\). Hence
\[
 \log N+\log\Phi(x)=\log N_0+\log\Phi(x_0).
\]
The derivative of \(\Phi\) is everywhere strictly positive. At the endpoints, \(\Phi(0+)=0\) and \(\Phi(1-)=\infty\). Therefore the invariant uniquely selects \(x_\infty\in(0,x_0)\), and its smooth inverse yields \(x(t)-x_\infty=O(K-N(t))\), so \(x(t)\to x_\infty\) exponentially.

**2. The three resource phases and turning level.** Put \(x_c=(1+\theta)^{-1}\). The resource log-odds \(H(t)=\log[n(t)/(1-n(t))]\) satisfies
\[
 \dot H=\epsilon(1+\theta)[x(t)-x_c].
\]
If \(x_\infty>x_c\), then \(H(t)\to+\infty\), giving \(n\to1\). If \(x_\infty<x_c\), then \(H(t)\to-\infty\), giving \(n\to0\). If \(x_\infty=x_c\), the exponentially decaying difference \(x(t)-x_c>0\) has finite positive integral, so \(H(t)\) reaches a finite value larger than \(H(0)\). Consequently \(n(t)\to n_*\in(n_0,1)\). Strict monotonicity of \(\Phi\) and the invariant translate these alternatives into the three ranges of \(K\) separated by \(K_c\). If \(x_0\le x_c\), we have \(x(t)<x_c\) for every positive time, hence \(n\to0\). If \(x_0>x_c\) and \(K>K_c\), strict decrease of \(x(t)\) produces one crossing of \(x_c\); the invariant shows that \(N\) is exactly \(K_c\) at that crossing. The resource derivative changes from positive to negative precisely once. This proves every global statement.

**3. Critical exact value in the calibration.** With the stated numerical coefficients, \(f_C(x)=1+2x\), \(f_D(x)=2+2x\), \(d(x)=1\), \(W(x)=2+x\), and \(\Phi(x)=x^2/(1-x)^3\). Thus \(\Phi(3/4)=36\), \(\Phi(1/2)=2\), and \(K_c=18\). At criticality, \(N(x)=36(1-x)^3/x^2\). Take the strictly increasing resource coordinate
\[
 F(n)=\frac12\log n-\log(1-n),\qquad F'(n)=\frac{1/2+n/2}{n(1-n)}.
\]
Eliminating time between the resource and cooperator equations gives
\[
 F(n_*)-F(1/2)
 =\frac12\int_{1/2}^{3/4}
 \frac{2x-1}{x(1-x)[1-N(x)/18]}\,dx
 =\frac12\int_{1/2}^{3/4}
 \frac{x\,dx}{(1-x)(x^2-2x+2)}=\frac J2.
\]
The apparently singular integrand has a removable endpoint cancellation at \(x=1/2\). Integrating gives the stated \(J\). Exponentiating the equation for \(F\), one obtains \(\sqrt{n_*}/(1-n_*)=\sqrt2 e^{J/2}\), or \(n_*/(1-n_*)^2=2L\). Its unique solution in \((0,1)\) is the stated square-root expression. This proves the calibration exactly.

## Verification

The included standalone `verify.py` reconstructs the partial fraction identity symbolically for arbitrary \(R,S,T,P\), checks the critical rational capacity and the critical integral with symbolic integration, and integrates the original three-dimensional ODE at \(K=12\), \(K=18\), and \(K=30\). Each numerical test verifies the invariant and the appropriate terminal resource regime. Running `python verify.py` in an environment with SymPy and SciPy prints `VERIFICATION_OK`. These finite numerical checks supplement, but do not substitute for, the general analytic proof.

## Relationship to prior work

Bairagya, Mondal, Chowdhury, and Chakraborty (2021) introduced the growing-population game–resource model and numerically demonstrated a finite-capacity rescue of the commons in strict Prisoner's-dilemma regimes. Their analysis includes qualitative bistability, numerical basin plots, and nonisolated resource equilibria. The theorem here does **not** present qualitative finite-capacity rescue as a new phenomenon. Its distinct contribution is the **explicit sharp capacity formula for a natural positive proportional-payoff subclass**, its independence from feedback speed and resource initialization, a unique population-size turning law, and the exact intermediate resource at the critical boundary. In contrast, Wienand, Frey, and Mobilia (2018) study stochastic environments with randomly switching carrying capacities, not this deterministic three-variable game–resource system. Betz, Fu, and Masuda (2024) study an edge-dependent environment on two communities rather than a fixed carrying capacity in this model.

## Limitations

The invariant and its stated capacity-independence require that both environmental endpoint payoff matrices be proportional to the same fixed positive strict Prisoner's-dilemma matrix. The theorem does not claim the same threshold for nonproportional payoff matrices, state-dependent carrying capacities, negative payoffs, stochastic population sizes, or boundary initial conditions. The universal limiting-value claim applies for finite carrying capacities greater than the initial population; an infinite-capacity system is only a separate limiting regime. No stochastic robustness, finite-size demographic effects, or experimental measurement is established. Other mathematically equivalent derivations may exist outside the inspected literature.

## References

1. J. D. Bairagya, S. S. Mondal, D. Chowdhury and S. Chakraborty, *Game-environment feedback dynamics in growing population: Effect of finite carrying capacity*, Phys. Rev. E **104**, 044407 (2021), DOI 10.1103/PhysRevE.104.044407; arXiv:2109.14971v1 (first public September 30, 2021). https://arxiv.org/html/2109.14971v1
2. K. Wienand, E. Frey and M. Mobilia, *Eco-Evolutionary Dynamics of a Population with Randomly Switching Carrying Capacity*, J. R. Soc. Interface **15**, 20180343 (2018), arXiv:1712.07939. https://arxiv.org/abs/1712.07939
3. K. Betz, F. Fu and N. Masuda, *Evolutionary Game Dynamics with Environmental Feedback in a Network with Two Communities*, Bull. Math. Biol. **86**, 84 (2024), DOI 10.1007/s11538-024-01310-3. https://link.springer.com/article/10.1007/s11538-024-01310-3
