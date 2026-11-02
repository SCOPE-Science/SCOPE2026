# Sharp equilibrium-center law for average-distance Schelling stars

## Finding

Consider the fully occupied swap Schelling game on the star \(K_{1,n-1}\), \(n\ge3\), with labeled agents whose real types \(t_1,\ldots,t_n\) lie in \([0,1]\). An agent pays the arithmetic mean of the absolute type differences from agents at neighboring vertices. A swap is permitted only when **both** involved agents strictly reduce their costs. Write
\[
D_i=\sum_{j=1}^{n}|t_i-t_j|,\qquad m=n-1.
\]
A placement with agent \(i\) at the hub is a swap equilibrium **if and only if** there is no agent \(j\ne i\) satisfying
\[
\boxed{D_j<m|t_j-t_i|<D_i.}\tag{1}
\]
The identity of the hub agent alone determines equilibrium status; leaf permutations do not. Thus, if \(K\) labeled agents satisfy (1)'s no-witness condition, exactly \(K(n-1)!\) of the \(n!\) labeled placements are equilibria.

For the equally spaced type profile \(t_j=(j-1)/(n-1)\), \(1\le j\le n\), there is also an exact finite arithmetic test. Index the types by \(0,\ldots,m\), and for a candidate hub index \(c\) put \(a=\min\{c,m-c\}\). If \(2a\ge n-2\), it is stable. Otherwise set
\[
L_{n,a}=m-\sqrt{m\left(\frac{n-2}{2}-a\right)},
\qquad
U_{n,a}=\frac n2+\frac{a^2}{m}.
\]
The index \(c\) is unstable **if and only if** the open interval \((L_{n,a},U_{n,a})\) contains an integer. In particular, if \(K_n\) is the number of stable hub indices on this grid, then
\[
\boxed{K_n=(2-\sqrt3)n+O(1).}\tag{2}
\]

More generally, let a sequence of type multisets, each contained in \([0,1]\), have empirical probability measures converging weakly to the uniform law on \([0,1]\). Then the fraction of labeled star placements that are swap equilibria converges to
\[
\boxed{2-\sqrt3\approx0.2679491924.}\tag{3}
\]
The empirical distribution of the types of *stable* hub agents converges to the uniform law on
\[
\left[\frac{\sqrt3-1}{2},\frac{3-\sqrt3}{2}\right].\tag{4}
\]
In particular, (3)--(4) hold almost surely for independent uniformly sampled types. When an equilibrium is chosen uniformly from its labeled placements, its average agent cost converges in distribution to \(F(U)\), where \(U\) is uniform on the interval (4) and
\[
F(u)=u^2-u+\frac12.
\]
Its limiting expected average cost is
\[
\boxed{\frac14+\frac{(2-\sqrt3)^2}{12},}\tag{5}
\]
while the minimum average cost tends to \(1/4\). Hence the limiting ratio of expected equilibrium cost to optimal cost is \(1+(2-\sqrt3)^2/3\). These are statements about the number and distribution of *equilibrium placements*, not about convergence probabilities of a specified adjustment process.

Finally, the set of stable hub types need not be an interval for a finite nonuniform profile: for types \((0,1,4,5,6)/6\), exactly the agents with types \(0,4/6,5/6,1\) can be hub agents in equilibrium; the agent with type \(1/6\) cannot.

## Assumptions and scope

There are no vacant vertices. Every private leaf is adjacent only to the hub, and each agent uses the unweighted average of the absolute type distances to her neighbors, without self-inclusion. All agents may swap, but a swap takes place only if both strictly improve. The exact test (1) allows tied types; the equally spaced finite formula uses distinct types; asymptotic empirical convergence permits ties and does not assume independence. The stochastic corollary assumes iid uniform real types, so types are almost surely distinct.

For the asymptotic welfare statement, the ratio is a ratio of expected cost under a uniformly selected equilibrium (conditional on a realized profile) to its minimum cost, not a worst-case price of anarchy. No jump games, non-star networks, or non-absolute type metrics are considered.

## Proof

**1. Exact hub certificate.** Let agent \(i\) occupy the hub and agent \(j\) a leaf. Before their swap, their respective costs are \(D_i/m\) and \(|t_i-t_j|\). After they swap, their respective costs are \(|t_i-t_j|\) and \(D_j/m\). Therefore both strictly improve precisely when \(D_j<m|t_j-t_i|<D_i\). Two leaves cannot profitably swap: every leaf sees only the unchanged hub type, so each leaf agent's cost is unchanged by a leaf--leaf exchange. This proves (1) and the exact labeled-placement count.

**2. Equal-grid certificate.** Distances may be multiplied by \(m\) without changing profitability. Work with types \(0,1,\ldots,m\), and reflect the grid if necessary so that the candidate hub has type index \(a\le m/2\). Its total distance is
\[
S_a=\sum_{j=0}^{m}|a-j|=a^2-ma+\frac{n m}{2}.
\]
For any \(x<a\), the convex sequence \(S_x\) satisfies \(S_x\ge S_a\); hence no such \(x\) can be a profitable partner. For \(x>a\), substituting the quadratic formula for \(S_x\) into (1) gives
\[
 x< a+\frac{S_a}{m}=\frac n2+\frac{a^2}{m}=U_{n,a}
\]
and
\[
S_x<m(x-a)
\quad\Longleftrightarrow\quad
(x-m)^2<m\left(\frac{n-2}{2}-a\right).
\]
If the right-hand side is nonpositive, no swap is possible. Otherwise, since \(x\le m\), this last inequality is exactly \(x>L_{n,a}\). Its lower endpoint is strictly larger than \(a\), so the two displayed strict inequalities are equivalent to an integer \(x\in(L_{n,a},U_{n,a})\). This proves the finite arithmetic test, including equality and endpoint conventions.

**3. Continuum threshold.** Let
\[
F(s)=\int_0^1|s-u|\,du=s^2-s+\frac12,
\qquad s_* =\frac{\sqrt3-1}{2}.
\]
For a prospective hub type \(s\le1/2\), a continuum analogue of (1) is a type \(y\in[0,1]\) with
\[
F(y)<y-s<F(s).
\tag{6}
\]
It suffices to consider \(y>s\): if \(y<s\), then \(F(y)\ge F(s)\), making strict improvement impossible. If \(F(y)<F(s)\), then \(s<y<1-s\). On this interval,
\[
F(y)-(y-s)=(1-y)^2+s-\frac12
\ge s^2+s-\frac12.
\]
For \(s\ge s_*\) the last quantity is nonnegative, so (6) has no solution. For \(s<s_*\), put \(y_0=s+F(s)=s^2+1/2\). The inequality \(s^2+s<1/2\) implies \(s<y_0<1-s\), hence \(F(y_0)<F(s)=y_0-s\). Decreasing \(y_0\) by a sufficiently small positive amount makes both inequalities in (6) strict. Reflection about \(1/2\) gives the full stable continuum interval \([s_*,1-s_*]\), of length \(1-2s_*=2-\sqrt3\).

**4. Transfer from uniform empirical distributions.** For a multiset of \(n\) types define
\[
H_n(y)=\frac1{n-1}\sum_{j=1}^{n}|y-t_j|.
\]
Weak convergence of the empirical measures to the uniform distribution on the compact interval implies \(\sup_{y\in[0,1]}|H_n(y)-F(y)|\to0\). One way to prove this is pointwise weak convergence of the bounded continuous distance functions, combined with the equi-Lipschitz property of \(H_n\) and a finite net in \([0,1]\). Uniform empirical convergence also implies that every fixed nonempty open subinterval eventually contains at least one type.

The two strict inequalities in (6) hold with a positive margin for each \(s\) outside the closed stable continuum interval. For centers in any compact subset of \([0,s_*)\cup(1-s_*,1]\), continuity, a finite subcover, uniform convergence of \(H_n\), and the eventual availability of a type near a continuum witness show that all sufficiently large profiles have a profitable partner. Conversely, on any compact subset of \((s_*,1-s_*)\), the continuous function
\[
R(s,y)=\max\{F(y)-|y-s|,\ |y-s|-F(s)\}
\]
is strictly positive uniformly over all \(y\in[0,1]\). Indeed, any simultaneous weak inequalities \(F(y)\le|y-s|\le F(s)\) would first require \(F(y)\le F(s)\), hence (after reflection if necessary) \(s\le y\le1-s\); but then \(F(y)-(y-s)\ge s^2+s-1/2>0\), a contradiction. Compactness supplies a strictly positive common margin. Uniform convergence then excludes profitable partners. The empirical mass of the omitted small neighborhoods of the two boundary points tends to their lengths. Letting these neighborhoods shrink proves the stable-center fraction (3) and the conditional stable-center type law (4). The iid case follows from the almost-sure empirical-distribution law of large numbers.

For any hub type \(s\), the total social cost equals \(D_s+D_s/m\). Thus its average per-agent cost is exactly \(H_n(s)\). A uniform draw from equilibrium placements makes its hub uniform among stable labeled agents, proving convergence in distribution to \(F(U)\). Since all costs are bounded, expectations converge as well. As \(U-1/2\) is uniform on a centered interval of half-width \((2-\sqrt3)/2\), its squared mean is \((2-\sqrt3)^2/12\), proving (5). Absolute-deviation sums attain their minimum at a median; empirical uniform convergence gives the limiting minimum \(F(1/2)=1/4\).

**5. Sharper equal-grid error.** In the finite test, write \(m=n-1\), \(s=a/m\), and \(U_{n,a}-L_{n,a}=m g_m(s)\), where
\[
g_m(s)=s^2-\frac12+\frac1{2m}+\sqrt{\frac12-\frac1{2m}-s}.
\]
On every closed subinterval of \([0,1/2)\), \(g_m\) differs uniformly by \(O(1/m)\) from
\[
g(s)=s^2-\frac12+\sqrt{\frac12-s}.
\]
The latter vanishes exactly at \(s_*\); indeed \(s_*^2+s_*=1/2\), and direct differentiation shows \(g'(s)\le-1/2\) throughout \([0,1/2)\). Thus for some absolute constant \(C\), sufficiently large grids have \(U-L>1\) whenever \(s<s_*-C/m\), and \(U-L<0\) whenever \(s>s_*+C/m\) within, say, \([0,9/20]\). On \([9/20,1/2]\), the finite interval is empty for sufficiently large grids by its explicit endpoint formulas. An open real interval of length greater than one always contains an integer; an interval of nonpositive length never does. Only \(O(1)\) indices on either side are undecided, giving (2).

**6. Finite noninterval example.** For unscaled types \((0,1,4,5,6)\), the total-distance vector is \((16,13,10,11,14)\). At hub type \(1\), swapping with type \(4\) gives \(10<4\cdot3<13\), so it is unstable. Applying (1) to each of the other four types shows no profitable hub--leaf swap. Multiplying all types by \(1/6\) preserves these strict comparisons.

## Verification

The standalone file `verify.py` independently evaluates before- and after-swap costs using exact rational arithmetic, compares them with certificate (1) on all sorted multisets of up to eight values chosen from six integer type levels, and checks the exact equal-grid radical interval formula for every hub on grid sizes \(3\) through \(400\). It also checks the five-agent disconnected example and numerical consistency of (2) for grids of sizes \(100,200,400,800,1600\). Run `python3 verify.py` with Python 3 and no additional packages. Finite tests corroborate, but do not prove, the infinite or asymptotic statements.

## Relationship to prior work

Bilò, Bilò, Döring, Lenzner, Molitor and Schmidt (2023) introduced the average type-distance swap Schelling game with real types. They establish existence and potential arguments for several network classes, especially regular graphs, and analyze welfare for paths and other settings. Their model, definitions and contribution are assumed here. The star-specific exact equilibrium-center census and the uniform-population \(2-\sqrt3\) law are the new assertions assessed here. General existence or potential statements, a median-hub equilibrium, and worst-equilibrium welfare bounds do not determine the fraction or distribution of equilibrium placements. Discrete-type Schelling stability and network-creation games use different payoffs or permissible changes and do not directly provide this census. The proof uses elementary absolute-deviation geometry, not a claim of a new general potential theorem.

## Limitations

The sharp fraction relies on asymptotically uniform types: a different limiting type distribution can produce a different set of stable hub types, and finite stable sets can be noninterval. The analysis does not determine which equilibrium arises from a prescribed stochastic adjustment rule, nor does it apply unchanged to arbitrary graph topologies or to jump games. The priority comparison is based on inspected accessible published literature and searchable records; unindexed equivalent results cannot be excluded. Independent external proof review has not been performed.

## References

1. Davide Bilò, Vittorio Bilò, Michelle Döring, Pascal Lenzner, Louise Molitor and Jonas Schmidt, *Schelling Games with Continuous Types* (2023), arXiv:2305.06819v1, first publicly posted May 11, 2023, https://arxiv.org/abs/2305.06819 ; IJCAI 2023, DOI:10.24963/ijcai.2023/280.
2. Aishwarya Agarwal, Edith Elkind, Jiarui Gan and Alexandros A. Voudouris, *Swap Stability in Schelling Games on Graphs* (2019/2020), arXiv:1909.02421, https://arxiv.org/abs/1909.02421.
3. Luca Kreisel, Niclas Boehmer, Vincent Froese and Rolf Niedermeier, *Equilibria in Schelling Games: Computational Hardness and Robustness* (2021 preprint; 2024 journal), arXiv:2105.06561, https://arxiv.org/abs/2105.06561.
