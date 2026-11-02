# Sharp finite-amplitude lag–dissipation constant for binary reversible Markov networks

## Finding

For every irreducible two-state continuous-time Markov network with frozen transition rates \(a>0\) from state \(0\) to state \(1\) and \(b>0\) in the reverse direction, put \(s=a+b\) and \(q=a/s\). If \(x\in(0,1)\) denotes the instantaneous probability of state \(1\), let \(\varepsilon=x-q\) be the lag of its indicator output and let \(\sigma_s(x)\) denote the corresponding frozen-generator entropy-production rate, with natural logarithms. The **optimal global constant** in

\[
\varepsilon^2\le C(q,s)\,\sigma_s(x)\qquad\text{for every }x\in(0,1)
\]

is given as follows.

If \(q=1/2\), then \(C(q,s)=1/(4s)\); this constant is sharp as \(x\to q\). If \(0<q<1/2\), there is a **unique** \(x_q\in(1/2,1)\) satisfying

\[
\log\!\frac{x_q(1-q)}{q(1-x_q)}
=\frac{x_q-q}{x_q(1-x_q)},
\qquad C(q,s)=\frac{x_q(1-x_q)}s.
\]

For \(1/2<q<1\), use \(x_q=1-x_{1-q}\) and the same formula. If \(q\ne1/2\), the bound is attained at the non-equilibrium state \(x=x_q\), and

\[
C(q,s)>\tau_{\mathrm m}:=\frac{q(1-q)}s.
\]

In particular, the leading near-equilibrium memory coefficient is not a valid global coefficient at finite lag. As \(q\downarrow0\), with \(L=\log((1-q)/q)\), the optimizer and sharp constant have the explicit rare-output laws

\[
\frac1{1-x_q}=L+\log L+o(1),\qquad
\frac1{sC(q,s)}=L+\log L+1+o(1),
\qquad \frac{C(q,s)}{\tau_{\mathrm m}}\sim\frac1{q\log(1/q)}.
\]

The corresponding statements as \(q\uparrow1\) follow by interchanging the states.

## Assumptions and scope

The rates \(a,b\) are fixed positive real numbers during the instantaneous comparison. The network is reversible with frozen equilibrium probabilities \((1-q,q)\), and its output is the state-\(1\) indicator. The current probability vector \((1-x,x)\) is strictly positive; it need not solve any particular input protocol, although every interior vector can occur as an initial distribution. Define the probability log-odds function \(h(t)=\log(t/(1-t))\), for \(t\in(0,1)\). Frozen entropy production is

\[
\sigma_s(x)=[a(1-x)-bx]\log\!\frac{a(1-x)}{bx}
=s(x-q)[h(x)-h(q)]\ge0.
\]

At \(x=q\), both sides of the bound vanish. The theorem optimizes the inequality over every interior instantaneous distribution; no claim about a nonreversible many-state network, physical work protocol, or arbitrary observables is made. Boundary point masses are outside the finite-logarithm domain and may be treated only by limits.

## Proof

**1. Exact reduction.** For \(x\ne q\), direct cancellation gives

\[
\frac{(x-q)^2}{\sigma_s(x)}=\frac1s F_q(x),
\qquad F_q(x)=\frac{x-q}{h(x)-h(q)}>0.
\]

This quotient extends continuously at equilibrium with \(F_q(q)=q(1-q)\), and tends to zero at both endpoints \(x\downarrow0\) and \(x\uparrow1\). Consequently the largest value is attained in the interior or is the equilibrium limit. The stationary points away from equilibrium obey

\[
N_q(x):=h(x)-h(q)-(x-q)h'(x)=0,
\qquad h'(x)=\frac1{x(1-x)},\quad
h''(x)=\frac{2x-1}{x^2(1-x)^2}.
\]

The derivative \(F_q'(x)\) has the sign of \(N_q(x)\), because its denominator is the square of \(h(x)-h(q)\).

**2. Unique global maximum.** Assume \(0<q<1/2\). On \((0,q)\), the derivative \(h'\) decreases along the interval from \(x\) to \(q\); its secant mean is therefore strictly greater than \(h'(q)\), so \(F_q(x)<q(1-q)\). On \((q,1/2]\), the secant mean of the decreasing function \(h'\) strictly decreases as its right endpoint increases; hence \(F_q\) strictly increases there and \(N_q(1/2)>0\). On \((1/2,1)\),

\[
N_q'(x)=-(x-q)h''(x)<0,
\qquad \lim_{x\uparrow1}N_q(x)=-\infty.
\]

Thus precisely one root \(x_q\in(1/2,1)\) exists; \(F_q\) rises before that root and falls after it. Its value at the root is \(F_q(x_q)=1/h'(x_q)=x_q(1-x_q)\), which exceeds \(F_q(q)\). This establishes global optimality, uniqueness of the nontrivial equality state, and strict improvement over the local constant. Reflection \((q,x)\mapsto(1-q,1-x)\) proves the \(q>1/2\) case. When \(q=1/2\), the pointwise inequality \(h'(x)\ge4\), strict away from \(1/2\), makes every nontrivial secant mean greater than \(4\); hence \(\sup F_{1/2}=1/4\), approached only in the equilibrium limit.

**3. Rare-output asymptotics.** For \(q\downarrow0\), write \(L=\log((1-q)/q)\) and \(y=(1-x_q)^{-1}>2\). The root equation is exactly

\[
y-\frac{q y^2}{y-1}-L-\log(y-1)=0.
\]

Its left side has positive derivative for \(y>2\): explicitly,

\[
\frac{y-2}{y-1}\left(1-\frac{qy}{y-1}\right)>0.
\]

For each fixed \(\delta>0\), evaluating this expression at \(y=L+\log L-\delta\) and at \(y=L+\log L+\delta\) gives, as \(L\to\infty\), respectively \(-\delta+o(1)\) and \(+\delta+o(1)\). (Here \(q=(1+e^L)^{-1}\), so the term containing \(q\) is negligible.) The unique root is therefore \(y=L+\log L+o(1)\). At that root,

\[
\frac1{sC(q,s)}=\frac1{x_q(1-x_q)}=\frac{y^2}{y-1}=y+1+\frac1{y-1},
\]

which proves the stated second expansion. Because \(\tau_{\mathrm m}=q(1-q)/s\) and \(L\sim\log(1/q)\), the amplification ratio follows.

**4. Memory normalization.** At equilibrium, the indicator covariance at lag \(t\ge0\) equals \(q(1-q)e^{-st}\). Its time integral is exactly \(\tau_{\mathrm m}=q(1-q)/s\), verifying the normalization used above. All inequalities are in natural-logarithm entropy units.

## Verification

The accompanying dependency-free \(\texttt{verify.py}\) evaluates the nonlinear root by bisection, checks flux and entropy-production normalizations, exercises the sharp inequality on a grid of \(999\) interior states for each tested rate/equilibrium pair, tests the optimizer equality, checks state-exchange symmetry, and inspects the rare-output expansion. The saved script reports \(96{,}157\) deterministic assertions, with \(x_{0.1}=0.729394843024\), \(sC(0.1,s)=0.197378005994\), and \(s\tau_{\mathrm m}=0.09\). These finite computations are reproducibility tests, **not** substitutes for the preceding proof for all real parameters.

## Relationship to prior work

Chen and Limmer (2026) derive the frozen reversible-network entropy-production identity, a general nonsharp arbitrary-amplitude bound via a modified log-Sobolev inequality, and the integrated-autocorrelation coefficient for a **small-lag** quadratic bound. Their principal quadratic result is explicitly restricted to leading order near equilibrium. The theorem here supplies an optimal finite-amplitude constant, a unique non-equilibrium equality state when the frozen equilibrium is asymmetric, and a rare-state expansion. It neither disputes their small-lag statement nor claims their basic thermodynamic identities.

Classical binary-chain log-Sobolev calculations, including the explicit two-state example in Aldous and Fill, optimize a different entropy-to-Dirichlet functional, not the observable squared-lag to entropy-production quotient optimized here. General Markov-chain entropy-dissipation theorems may imply related bounds; no broad noncoverage conclusion follows merely from search results.

## Limitations

This is a binary-state, reversible, single-indicator theorem at a frozen input. It does not establish an optimal constant for arbitrary finite networks, nor analyze a time-varying input trajectory. For unbiased equilibrium the bound is sharp only as an equilibrium limit; for biased equilibrium it has a nontrivial exact equality state. A broader functional-inequality result could implicitly contain this binary extremal computation; independent publication-priority and proof audits have not been performed.

## References

1. Songela W. Chen and David T. Limmer, *Entropy Production Bounds the Accuracy of Computation in Markov Networks*, arXiv:2608.23764v1, first publicly submitted 2026-08-24. Main text, thermodynamic bounds; Supporting Material, Sections I–II. https://arxiv.org/html/2608.23764v1
2. David Aldous and James Fill, *Reversible Markov Chains and Random Walks on Graphs*, Chapter 8, Section 8.4.3, Example 8.28 (explicit two-state logarithmic Sobolev time). https://www.stat.berkeley.edu/~aldous/RWG/Book_Ralph/Ch8.S4.html
3. Persi Diaconis and Laurent Saloff-Coste, *Logarithmic Sobolev inequalities for finite Markov chains*, Annals of Applied Probability 6 (1996), 695–750. https://doi.org/10.1214/aoap/1034968224
4. Ioannis Karatzas, Jan Maas and Walter Schachermayer, *Trajectorial dissipation and gradient flow for relative entropy in Markov chains*, arXiv:2005.14177. https://arxiv.org/abs/2005.14177
