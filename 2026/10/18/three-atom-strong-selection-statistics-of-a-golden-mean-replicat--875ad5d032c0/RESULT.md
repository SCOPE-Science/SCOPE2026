# Three-atom strong-selection statistics of a golden-mean replicator horseshoe

## Finding

For a two-strategy replicator map in the strongly selected, asymmetric regime, a chaotic invariant set can have infinitely many invariant laws with identical stationary mean yet a complete, nontrivial limiting variance spectrum. The full physical one-point marginal collapses uniformly to three atoms. The same symbolic frequency simultaneously determines an explicit two-term Lyapunov expansion and the sharp conditional entropy envelope.

For fixed \(b\in(0,1)\setminus\{1/2\}\), put \(\beta=\min(b,1-b)\). For sufficiently large \(a>0\), consider
\[
f_{a,b}(x)=\frac{x}{x+(1-x)e^{a(x-b)}},\qquad 0<x<1.
\]
There exists a compact uniformly expanding invariant set \(Q_{a,b}\subset(0,1)\), conjugate to the one-sided golden-mean shift \(\Sigma=\{s\in\{0,1\}^{\mathbb N_0}:s_js_{j+1}=0\}\). Its coding is specified constructively below. Every invariant probability \(\mu\) on \(Q_{a,b}\) has a unique symbolic pullback \(\nu\); write \(q=\nu\{s_0=1\}\in[0,1/2]\), and let \(\rho_{a,\mu}\) denote the distribution of the physical coordinate \(x\) under \(\mu\). Define
\[
\rho_q=(1-2q)\delta_b+q\delta_{b-\beta}+q\delta_{b+\beta}.
\]
Uniformly over **all** such invariant probabilities,
\[
W_1(\rho_{a,\mu},\rho_q)=O_b\!\left(\frac{\log a}{a}\right),\qquad
\int x\,d\mu=b,\qquad
\operatorname{Var}_\mu(x)=2\beta^2q+O_b\!\left(\frac{\log a}{a}\right).
\]
Here \(W_1\) is the \(1\)-Wasserstein distance on \([0,1]\), and the constants do not depend on the invariant law. The integrated Lyapunov exponent \(\Lambda_a(\mu)=\int\log|f'_{a,b}(x)|\,d\mu(x)\) satisfies, again uniformly,
\[
\boxed{\ \Lambda_a(\mu)=(1-q)\log a+(1-2q)\log[b(1-b)]
+q\log[2\beta(1-2\beta)]+O_b\!\left(\frac{\log a}{a}\right).\ }
\]
Consequently every limit pair of physical variance and normalized Lyapunov exponent lies on the **entire** line segment
\[
\boxed{\ (V,\ell)=(2\beta^2q,1-q),\quad 0\le q\le1/2.\ }
\]
Every point of this segment is attained as a limit by invariant **ergodic** measures, and the periodic-orbit values are dense along it.

The sharp maximal Kolmogorov–Sinai entropy among invariant measures of fixed symbolic frequency \(q\) is, for every sufficiently large \(a\),
\[
\boxed{\ H(q)=(1-q)\log(1-q)-q\log q-(1-2q)\log(1-2q),\ }
\]
where \(0\log0=0\). The maximum is attained by a stationary one-step Markov measure with transitions \(0\to1\) of probability \(q/(1-q)\) and \(1\to0\) of probability \(1\). Thus \(H(V/(2\beta^2))\) is the sharp limiting entropy envelope at physical variance \(V\in[0,\beta^2]\). The maximum across all variances is \(\log((1+\sqrt5)/2)\).

## Assumptions and scope

The result concerns the specific smooth interval map above, fixed \(b\ne1/2\), and the **particular compact hyperbolic subsystem** constructed from two monotone branches for sufficiently large \(a\). The invariant-law conclusions do not assert that every invariant law on the whole interval is supported there. All asymptotic bounds hold with \(b\) fixed; no uniformity is claimed as \(b\to0\) or \(b\to1/2\). The symbolic frequency \(q\) is associated with the canonical branch labels, not a newly introduced physical parameter.

For \(b>1/2\), the reflection \(x\mapsto1-x\) conjugates this family to the case \(\beta=1-b<1/2\), so it suffices to give the construction for \(0<b<1/2\). Natural logarithms are used throughout.

## Proof

**1. Direct construction of the two branches.** Define the decreasing log-odds homeomorphism \(h(x)=\log((1-x)/x)\), its inverse \(X(y)=(1+e^y)^{-1}\), and
\[
g_{a,b}(y)=h\circ f_{a,b}\circ h^{-1}(y)=y+aX(y)-ab,\qquad g'_{a,b}(y)=1-aX(y)(1-X(y)).
\]
For \(a>4\), the two turning points are \(\pm c_a\), where \(c_a=\operatorname{arcosh}(a/2-1)=\log a+O(1/a)\). The map decreases on \([-c_a,c_a]\) and increases on \([c_a,\infty)\). For large \(a\), define the unique \(L_a,R_a>c_a\) through \(g(L_a)=-c_a\), \(g(R_a)=c_a\), and the unique \(l_a,r_a\in(-c_a,c_a)\) through \(g(l_a)=R_a\), \(g(r_a)=-c_a\). These roots exist since \(g(c_a)=-ab+O(\log a)\), \(g(-c_a)=a(1-b)+O(\log a)\), and \(b<1/2\). Set \(J_0=[l_a,r_a]\), \(J_1=[L_a,R_a]\). Then
\[
g(J_0)=[-c_a,R_a]\supset J_0\cup J_1,\qquad
 g(J_1)=[-c_a,c_a]\supset J_0,\qquad g(J_1)\cap J_1=\varnothing.
\]
A direct inversion of these equations gives
\[
L_a=ab-c_a+o(1),\quad R_a=ab+c_a+o(1),\quad
l_a=h(2b)+O_b(\log a/a),\quad r_a=h(b)+O_b(\log a/a).
\]
In particular \(J_0\) remains in a fixed compact interval, while every point of \(J_1\) equals \(ab+O_b(\log a)\). On \(J_0\), \(|g'|\ge C_ba\) for some \(C_b>0\); on \(J_1\), \(g'=1+O_b(a^2e^{-ab})\). Because every admissible two-letter word contains a \(0\), inverse branches contract uniformly over two steps for large \(a\). Nested branch cylinders therefore have single-point intersections. The compact invariant set \(K_a=\bigcap_{j\ge0}g^{-j}(J_0\cup J_1)\) is conjugate to \(\Sigma\), and \(Q_{a,b}=h^{-1}(K_a)\) inherits the conjugacy and uniform expansion. This also independently verifies the critical covering and expansion conditions used in the original horseshoe construction.

**2. Uniform three-symbol physical-coordinate approximation.** If a coded point has symbols \(00\), then its current and next log-odds lie in \(J_0\), so the exact identity \(g(y)-y=a(X(y)-b)\) gives \(X(y)=b+O_b(1/a)\). For \(01\), the next log-odds is \(ab+O_b(\log a)\), hence \(X(y)=2b+O_b(\log a/a)\). For \(10\), its current log-odds belongs to \(J_1\), so \(X(y)=O_b(ae^{-ab})\). The symbol pair \(11\) is forbidden. Thus the physical coordinate is within \(O_b(\log a/a)\) of the corresponding point in \(\{b,2b,0\}\), uniformly over \(K_a\) and every itinerary. Reflection yields the unordered alphabet \(\{b-\beta,b,b+\beta\}\) for either asymmetry sign.

**3. Entire stationary marginal and variance spectrum.** Invariance of any symbolic probability makes the two mixed transition frequencies equal: \(\nu[01]=\nu[10]=q\). Since \(\nu[11]=0\), also \(\nu[00]=1-2q\). The approximation in Step 2 couples the physical marginal to \(\rho_q\) with error at most \(C_b\log(a)/a\) in \(W_1\). The mean equals \(b\) **exactly**, not merely asymptotically: telescoping \(h(f(x))-h(x)=a(x-b)\) and using boundedness of \(h\) on the compact invariant set gives \(\int x\,d\mu=b\). Integrating the Lipschitz function \((x-b)^2\) gives the variance formula.

**4. Two-term Lyapunov expansion.** On \(00\), \(\log|g'(y)|=\log a+\log[b(1-b)]+O_b(1/a)\). On \(01\), \(\log|g'(y)|=\log a+\log[2b(1-2b)]+O_b(\log a/a)\). On \(10\), \(\log|g'(y)|=O_b(a^2e^{-ab})\). Averaging with the exact transition frequencies proves the announced expansion for \(g\). The derivative conjugacy yields
\[
\log|f'(x)|=\log|g'(h(x))|+\log|h'(x)|-\log|h'(f(x))|,
\]
so the last two terms integrate to zero under every invariant probability on \(Q_{a,b}\). Reflection leaves the multiplier unchanged and replaces \(b\) in the second constant by \(\beta\), as asserted.

**5. Sharp entropy envelope and attainment.** For \(\nu[1]=q\), the one-step conditional entropy bound gives
\[
h_\nu(\sigma)\le H_\nu(s_1\mid s_0)
=(1-q)\,h_2\!\left(\frac q{1-q}\right)=H(q),
\]
where \(h_2(p)=-p\log p-(1-p)\log(1-p)\). Equality is achieved by the stated stationary Markov chain. Every \(q\in(0,1/2)\) gives an ergodic Markov chain; endpoint frequencies are realized by fixed or alternating periodic words. Rational frequencies of cyclic golden-mean words are dense in \([0,1/2]\), establishing the full limiting periodic-orbit segment. Elementary maximization of \(H(q)\) gives its maximal value \(\log((1+\sqrt5)/2)\). Topological conjugacy transports the entropy exactly to \(Q_{a,b}\).

## Verification

The self-contained script `verify.py` reconstructs both monotone branches using bracketed roots, builds representative coded periodic trajectories by inverse iteration, checks their mean, variance and Lyapunov values, and exhaustively checks admissible cyclic binary words through length twelve. It completed 899 finite symbolic/numerical diagnostics. The largest observed absolute errors against the asymptotic formulas were approximately \(3.74\times10^{-3}\) for variance and \(8.14\times10^{-2}\) for the two-term Lyapunov approximation. The exact mean error was below \(10^{-12}\). These are finite diagnostic checks, not a substitute for the uniform analytic arguments of the proof.

Reproduce with `python verify.py`, using Python 3 and SciPy. The derivation itself needs no numerical certificate.

## Relationship to prior work

Kryzhevich and Zhang (2026, arXiv:2603.20685v1), Sections 4–6 and Appendix A, establish the fixed stationary mean and an asymmetric large-parameter golden-mean horseshoe. The present result uses that mathematical setting but independently analyzes its **uniform physical marginal collapse**, **all-invariant-measure variance spectrum**, **two-term Lyapunov law**, and **fixed-frequency entropy envelope**. The source does not state these combined formulas. Its Appendix provides a different purpose for the same branch construction: existence of a hyperbolic chaotic subsystem. The distinction is substantive: a common first moment does not specify higher moments or dynamical expansion rates.

A published public-research record titled *Singular symmetry-breaking threshold for the period-two orbit of a replicator map* concerns a stability transition of one two-cycle near symmetric parameters. Such a local bifurcation statement does not imply the uniform large-parameter statistical spectrum for all invariant measures. Standard golden-mean symbolic-dynamics theory supplies the conditional entropy inequality, but not the map-specific three-atom and Lyapunov identifications. An earlier, possibly equivalent singular-selection analysis of this exact map remains a bibliographic risk; absence of an indexed match does not establish absolute novelty.

## Limitations

The theorem concerns one explicitly constructed uniformly expanding invariant subsystem, not the global attractor or the set of all invariant probabilities of \([0,1]\). It excludes \(b=1/2\) and does not quantify how rapidly the parameter lower bound diverges near the symmetric limit. At finite \(a\), the physical variance is close to, rather than exactly, \(2\beta^2q\); the entropy formula is exact conditional on symbolic frequency, not necessarily on the observed finite-parameter variance. The asymptotic Lyapunov formula concerns invariant-law averages, and does not assert uniform orbitwise Birkhoff convergence for arbitrary nonergodic points.

## References

1. Sergey Kryzhevich and Yiwei Zhang, *Shift maps and statistical invariants for some dynamical systems*, arXiv:2603.20685v1 (publicly submitted 2026-03-21), Sections 4–6 and Appendix A. https://arxiv.org/html/2603.20685
2. Douglas Lind and Brian Marcus, *An Introduction to Symbolic Dynamics and Coding*, Cambridge University Press. Standard background for shifts of finite type, entropy and Markov measures.
3. *Singular symmetry-breaking threshold for the period-two orbit of a replicator map*, public mathematical research record, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-singular-symmetry-breaking-threshold-for-the-period-two-orbit-of--fdee730ba349 (comparison to its published summary only).
