# A logarithmically shifted stochastic fixation threshold in a nonlinear mixed-order public-goods game

## Finding

A fixed pair/triple nonlinear public-goods payoff admits **three asymptotically different fixation regimes and a nontrivial logarithmically shifted crossover**, even though its deterministic flow has the same qualitative pair of positive equilibria in all three regimes. This is a statement about the *explicit expected-payoff Fermi birth–death closure* defined below, not the original finite-hypergraph process.

Fix the fraction of three-player interactions \(\theta=2/5\), the pairwise discount parameter \(\delta_2=1/2\), and the three-player synergy parameter \(\delta_3=3/2\). With cost normalized to one, the mixed payoff difference is
\[
F_r(x)=r\left(\frac{13}{30}-\frac{x}{60}+\frac{x^2}{30}\right)-1.
\]
For every \(30/13<r<160/69\), it has exactly two simple interior zeros \(0<a<b<1\), with \(a+b=1/2\) and \(F_r(x)=A(x-a)(x-b)\), where \(A=r/30\). The lower equilibrium \(a\) is attracting and the upper equilibrium \(b\) repelling for the deterministic equation \(\dot x=x(1-x)F_r(x)\); the full-cooperation state \(x=1\) is also attracting.

For the discrete absorbing birth–death model in the next section, let \(h_N\) be the probability of eventual full-cooperator fixation when the initial number of cooperators is \(\lfloor Na\rfloor\), for all sufficiently large \(N\) so this is an interior state. Fix arbitrary \(w>0\), and write
\[
f_0=Aab>0,\qquad d=A(b-a)>0,\qquad
D=\int_0^bF_r(x)\,dx=\frac{A b^2(3a-b)}6,
\qquad C=\frac{1}{2\sinh(wf_0/2)}\sqrt{\frac{wd}{2\pi}}>0.
\]
As \(N\to\infty\), for every fixed \(r\) in the stated open interval,
\[
\begin{array}{ll}
 h_N\sim C N^{-1/2}e^{NwD},&30/13<r<1920/829,\\[2pt]
 h_N\sim C N^{-1/2},&r=1920/829,\\[2pt]
 1-h_N\sim C^{-1}N^{1/2}e^{-NwD},&1920/829<r<160/69.
\end{array}
\]
In particular, equal potential heights at the critical parameter do **not** yield a fifty–fifty fixation probability: full-cooperator fixation tends to zero there, at the precise square-root rate.

There is an additional *finite-size crossover*, not visible in the fixed-parameter limit. Put \(r_c=1920/829\) and \(C_c=C\rvert_{r=r_c}\). For any sequence \(r_N\to r_c\) within the open parameter interval such that
\[
NwD(r_N)-\tfrac12\log N\longrightarrow z\in\mathbb R,
\]
the fixation probabilities, initialized at \(\lfloor Na(r_N)\rfloor\), satisfy
\[
 h_N\longrightarrow\frac{C_c e^z}{1+C_c e^z}.
\]
Since \(D'(r_c)=829/5120\), the nontrivial transition is displaced to leading order by
\[
 r_N=r_c+\frac{2560}{829w}\frac{\log N}{N}+O(N^{-1}).
\]
The three fixed-parameter regimes and the crossover are components of one fixation-selection classification for this canonical model.

## Assumptions and scope

The state of the finite model is an integer \(i\in\{0,1,\ldots,N\}\), with \(N\ge2\). States \(0\) and \(N\) are absorbing. For \(1\le i\le N-1\), put \(g_i=i(N-i)/(N(N-1))\) and
\[
 T_i^+=\frac{g_i}{1+e^{-wF_r(i/N)}},\qquad
 T_i^-=\frac{g_i}{1+e^{wF_r(i/N)}}.
\]
In one discrete update, move from \(i\) to \(i+1\) with probability \(T_i^+\), to \(i-1\) with probability \(T_i^-\), and otherwise hold. These are genuine transition probabilities because \(T_i^++T_i^-=g_i\le1\). The chain is eventually absorbed almost surely, and every interior state communicates with both absorbing endpoints.

This stochastic model evaluates the *infinite-well-mixed-population expected payoff difference* at \(i/N\) and inserts it into the standard Fermi pairwise-comparison kernel. It is an explicitly defined, model-level mean-field-payoff closure. The original microscopic hypergraph process uses accumulated individual payoffs and its own partner-selection rule; no identity of its finite-state law with this closure is asserted. At fixed \(w\), the drift in the closure is proportional to \(x(1-x)\tanh(wF_r(x)/2)\), which has the same equilibria and local stability signs as the cited replicator model, but not generally the identical velocity. The theorem assumes fixed positive \(w\) unless a varying \(r_N\) is expressly stated; simultaneous weak-selection or population-dependent \(w\) limits are outside its scope.

## Proof

**1. Payoff factorization and deterministic branches.** The motivating mixed-order formulas give
\[
F_r(x)=\frac35\left[\frac r2(1-x/2)-1\right]
+\frac25\left[\frac r3(1+x/2)^2-1\right].
\]
Collecting coefficients yields the quadratic stated above. Completing its square gives roots
\[
 a=\frac14-\sqrt{\frac{30}{r}-\frac{207}{16}},\qquad
 b=\frac14+\sqrt{\frac{30}{r}-\frac{207}{16}}.
\]
The inequalities \(0<a<b<1\) hold precisely for \(30/13<r<160/69\). The signs of the upward-opening quadratic are positive on \([0,a)\) and \((b,1]\) and negative on \((a,b)\), proving the stated attracting/repelling classification. Integrating its factorization to \(b\) gives \(D=A b^2(3a-b)/6\). Since \(a+b=1/2\), the sign changes when \(a=1/8\), \(b=3/8\), equivalently \(r=r_c=1920/829\). Implicit differentiation or differentiation of the displayed roots gives \(D'(r_c)=829/5120\).

**2. Exact finite-population fixation formula.** The Fermi ratio cancels the encounter factor:
\[
 \frac{T_i^-}{T_i^+}=e^{-wF_r(i/N)}.
\]
Writing \(S_N(k)=\sum_{j=1}^{k}F_r(j/N)\), with \(S_N(0)=0\), the second-order harmonic equation for fixation, together with the endpoint values \(h(0)=0\), \(h(N)=1\), gives exactly
\[
 h_N=\frac{\sum_{k=0}^{\lfloor Na\rfloor-1}e^{-wS_N(k)}}
 {\sum_{k=0}^{N-1}e^{-wS_N(k)}}.
\]
For reproducibility, because the payoff is quadratic, every discrete potential sum is given without numerical integration by
\[
 S_N(k)=A\left[
 \frac{k(k+1)(2k+1)}{6N^2}
 -\frac{(a+b)k(k+1)}{2N}+abk
 \right].
\]
The same exact formula holds when \(r\) varies with \(N\).

**3. Boundary and interior asymptotics.** Define \(H(x)=\int_0^xF_r(y)\,dy\). Uniform Euler–Maclaurin for this polynomial yields
\[
 S_N(k)=NH(k/N)+\frac{F_r(k/N)-f_0}{2}+O(N^{-1})
\]
uniformly for \(0\le k<N\). The function \(H\) has \(H(0)=0\), a strict local maximum at \(a\), and a strict local minimum at \(b\), with \(H(b)=D\) and \(H''(b)=d>0\). Its only possible global minima on \([0,1]\) are therefore \(0\) and \(b\); \(H(1)>H(b)\).

The numerator receives only the boundary contribution near \(k=0\): for fixed \(k\), \(S_N(k)\to kf_0\). Because \(H\) is positive on \((0,a]\), standard geometric domination on a small initial subinterval and an exponential bound outside it show
\[
 \sum_{k=0}^{\lfloor Na\rfloor-1}e^{-wS_N(k)}
 \longrightarrow B:=\frac{1}{1-e^{-wf_0}}.
\]
The same boundary limit holds uniformly for \(r_N\to r_c\) inside a compact neighborhood of \(r_c\).

A lattice Laplace expansion at the nondegenerate interior minimum \(b\), using \(F_r(b)=0\), yields the competing contribution
\[
 L_N=e^{-NwD+wf_0/2}\sqrt{\frac{2\pi N}{wd}}\,(1+o(1)).
\]
It holds uniformly in a sufficiently small compact neighborhood of \(r_c\), including the logarithmically moving sequences considered above. Away from fixed small neighborhoods of \(0\) and \(b\), the potential is separated from their competing minimum, and the remainder is negligible relative to the larger contribution. Thus the whole denominator equals \(B+L_N+o(B+L_N)\), while its tail starting at \(\lfloor Na\rfloor\) equals \(L_N(1+o(1))\) whenever that tail is needed. These assertions also apply for each fixed \(r\) elsewhere in the stated interval, by choosing parameter-dependent separated neighborhoods.

**4. Three regimes and crossover.** Since
\[
 \frac{B}{e^{wf_0/2}\sqrt{2\pi/(wd)}}=
 \frac1{2\sinh(wf_0/2)}\sqrt{\frac{wd}{2\pi}}=C,
\]
we have \(L_N/B=C^{-1}\sqrt N e^{-NwD}(1+o(1))\). If \(D<0\) the interior contribution dominates; if \(D=0\) it still dominates by a square-root factor; if \(D>0\) it is exponentially suppressed. Taking ratios, and using the tail representation for \(1-h_N\), proves all three equivalents. For \(r_N\to r_c\) with \(NwD(r_N)-(\log N)/2\to z\), the ratio \(L_N/B\to C_c^{-1}e^{-z}\), hence the claimed logistic crossover. Taylor expansion at \(r_c\), where \(D'(r_c)=829/5120\), proves the logarithmic displacement.

## Verification

The self-contained Python program `verify.py` uses exact rational arithmetic to check all three factorization examples and both signs of the potential, and independent log-domain finite sums to check fixation asymptotics without numerical underflow. It also checks the shifted crossover against the nontrivial limiting probability. Run `python verify.py` with Python 3 and its standard library. The exact lattice-potential identity allows independent reproduction of the finite probabilities; numerical tests support but do not replace the unrestricted Euler–Maclaurin and Laplace proof.

The rational examples are \((r,a,b)=(125/54,1/10,2/5)\), \((1920/829,1/8,3/8)\), and \((1500/647,1/5,3/10)\). Their respective potential gaps are \(-1/4860\), \(0\), and \(9/25880\).

## Relationship to prior work

Llabrés, Sadekar, Malizia and Battiston derive the nonlinear pair/triple payoff difference, two interior equilibrium branches and deterministic coexistence–cooperation bistability. Their finite-hypergraph experiments monitor quasistationary and absorbing branches but do not state the present exact finite-payoff Fermi closure's large-\(N\) fixation trichotomy or logarithmic crossover.

Traulsen, Nowak and Pacheco give the general exact ratio-of-products fixation formula for Fermi pairwise comparison; that identity is used openly as the starting point here, not claimed as new. Assaf and Mobilia derive WKB large-deviation and prefactor methods for classical pairwise \(2\times2\) games, whose payoff difference has at most one internal zero. Gokhale and Traulsen compare invasion success and stability conditions for multiplayer games, including risk-dominance criteria, but do not give the specific two-interior-well boundary-versus-saddle sharp asymptotics or this model's shifted crossover. Zhu and collaborators study a different stochastic nonlinearity mechanism and corresponding deterministic bistability; their finite-system results do not establish the present sharp fixation classification. These established general methods delimit the novelty: the contribution is the full quantitative classification and finite-size crossover of this particular motivated mixed-order closure, not the invention of birth–death fixation theory or Laplace's method.

## Limitations

The result concerns a well-mixed expected-payoff Fermi chain with two absorbing states and no mutation. It does not compute absorption times, finite-hypergraph fixation probabilities, or the quasistationary distribution of the source's spatially structured microscopic update. The parameters \(\theta,\delta_2,\delta_3\) are fixed; the benefit parameter ranges over an open interval excluding merging and boundary-root degeneracies. The selection strength \(w\) is fixed and positive. Every asymptotic equivalent is a limit, not an assertion of accuracy at a prescribed small \(N\). The model-specific asymptotics employ established birth–death and lattice Laplace tools, and overlap with a broader unpublished or unindexed theorem remains possible. No independent verification has been performed.

## References

1. J. Llabrés, O. Sadekar, F. Malizia, and F. Battiston, *Emergence of cooperation in nonlinear higher-order public goods games*, arXiv:2604.07228 (first version 8 April 2026), https://arxiv.org/html/2604.07228v2; especially equations (14)–(19) and Appendix B.
2. A. Traulsen, M. A. Nowak, and J. M. Pacheco, *Stochastic dynamics of invasion and fixation*, Physical Review E **74**, 011909 (2006), https://pmc.ncbi.nlm.nih.gov/articles/PMC2904085/; especially equation (5).
3. M. Assaf and M. Mobilia, *Large fluctuations and fixation in evolutionary games*, Journal of Statistical Mechanics P09009 (2010), arXiv:1007.0327, https://arxiv.org/html/1007.0327v3.
4. C. S. Gokhale and A. Traulsen, *Evolutionary games in the multiverse*, Proceedings of the National Academy of Sciences **107**, 5500–5504 (2010), https://pmc.ncbi.nlm.nih.gov/articles/PMC2851774/.
5. W. Zhu et al., *Evolutionary dynamics in stochastic nonlinear public goods games*, Communications Physics **7**, 377 (2024), https://www.nature.com/articles/s42005-024-01865-6.
