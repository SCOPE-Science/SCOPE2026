# A unique cross-community mixing maximizer for within-group voter discord

## Finding

In a symmetric two-community voter model with opposing stubborn sources, **within-community stationary discord has exactly one strict global maximum as cross-community copying increases**, even though the difference between mean opinions decreases strictly throughout. The maximizing per-neighbor copying rate has the sharp scaling \(b_m^*\sim\sqrt{az/(2m)}\), and the optimal discord converges to the sharp, unattained finite-population ceiling \(z/(a+2z)\).

More precisely, with the notation below, for every integer \(m\ge2\) and \(a,z>0\), the distinct-member, within-community disagreement probability is
\[
W_m(b)=\frac{2mbz(mb+z)}{(2mb+z)(amb+az+mb^2+2mbz+z^2)}.
\]
For \(h=a/z\), let \(r=b/z\). There is exactly one positive root \(r_{m,h}\) of
\[
F_{m,h}(r)=(h+1)+2m(h+1)r+m(hm-1)r^2-4m^2r^3-2m^3r^4.
\]
The unique global maximizing rate is \(b_m^*=z r_{m,h}\), and \(W_m\) is strictly increasing before this rate and strictly decreasing after it. For fixed \(a,z>0\),
\[
\lim_{m\to\infty}\sqrt{m}\,b_m^*=\sqrt{az/2},\qquad
\lim_{m\to\infty}\max_{b\ge0}W_m(b)=\frac{z}{a+2z}.
\]
Every finite population and every finite rate obey \(W_m(b)<z/(a+2z)\); thus this is the sharp uniform ceiling across all population sizes and rates.

## Assumptions and scope

There are two disjoint sets \(A,B\), each containing exactly \(m\ge2\) mutable, binary-state individuals. In continuous time, independently for each ordered pair of **distinct** people in the same community, the target copies the source at rate \(a>0\). Independently for each ordered cross-community pair, copying occurs at rate \(b\ge0\). Each person in \(A\) additionally resets to opinion \(0\) at rate \(z>0\), and each in \(B\) resets to opinion \(1\) at the same rate. All rates are per directed edge or individual, not row-normalized probabilities. Events that do not change a state are permitted and have no effect on the generator.

For \(b>0\), the finite-state chain is irreducible: external resets can create the uniform opposing configuration, and repeated cross-community copies and resets reach all assignments. At \(b=0\) there is a unique absorbing state with all \(A\) individuals at \(0\) and all \(B\) individuals at \(1\), which also uniquely determines the stationary distribution. Consequently the stationary disagreement probabilities below are well-defined for all \(b\ge0\).

Let \(x\) be the stationary probability that an individual in \(A\) holds opinion \(1\). By complement-swap symmetry, a member of \(B\) holds opinion \(1\) with probability \(1-x\). Let \(W_m(b)\) be the stationary probability that two *distinct* people in the same community disagree, and \(E_m(b)\) the probability of disagreement between people belonging to opposite communities. The average opinion difference between communities is \(1-2x\).

## Proof

**First moments.** Within-community copying cancels in the evolution of community means by symmetry. Cross-community copying and the stubborn sources give
\[
\dot x=mb(1-2x)-zx,
\]
whence \(x=mb/(z+2mb)\) and the mean opinion gap is
\[
1-2x=\frac{z}{z+2mb}.
\]
This gap is strictly decreasing in \(b\ge0\).

**Pair equations.** For two distinct same-community agents, copying their counterpart destroys discord at rate \(2aW\); copying anybody else in their community cancels by exchangeability. Opposite-community copies contribute \(2mb(E-W)\); source resets contribute \(2z(x-W)\). Thus stationarity gives
\[
(a+mb+z)W=mbE+zx.
\]
For a cross-community pair, copying anyone in the same group cancels; copying across the communities contributes \(2(m-1)bW-2mbE\); the two opposing source resets contribute \(2z(1-x-E)\). Thus
\[
(mb+z)E=(m-1)bW+z(1-x).
\]
The equations have a strictly positive determinant because \(z>0\). Their solution is
\[
W=\frac{2mbz(mb+z)}{(2mb+z)H},\quad
E=\frac{z\{amb+az+(2m^2-m)b^2+2mbz+z^2\}}{(2mb+z)H},
\]
where \(H=amb+az+mb^2+2mbz+z^2\).

**One and only one maximum.** Put \(h=a/z>0\) and \(r=b/z\). Then
\[
W_m(zr)=\frac{2mr(mr+1)}{(2mr+1)(hmr+h+mr^2+2mr+1)}.
\]
A direct differentiation yields
\[
\frac{d}{dr}W_m(zr)=\frac{2mF_{m,h}(r)}{(2mr+1)^2(hmr+h+mr^2+2mr+1)^2}.
\]
The coefficients of \(F_{m,h}\), read in increasing powers of \(r\), have signs \(+,+,\pm,-,-\), with a possible zero coefficient in the middle. Thus their *descending* sequence has exactly one sign change. By Descartes' rule of signs, \(F_{m,h}\) has at most one positive root, counted with multiplicity. Since \(F_{m,h}(0)=h+1>0\) and the leading term is negative, it has exactly one positive root and that root is simple. Hence \(W\) increases strictly before it and decreases strictly afterward. Also \(W_m(0)=0\) and \(W_m(b)\to0\) as \(b\to\infty\), proving the global claim.

**Sharp large-population scale.** For fixed \(h>0\) and any fixed \(c>0\),
\[
\frac{F_{m,h}(c/\sqrt m)}m\longrightarrow hc^2-2c^4.
\]
The limiting expression is positive for \(0<c<\sqrt{h/2}\) and negative for \(c>\sqrt{h/2}\). The uniqueness of each positive root traps \(\sqrt m\,r_{m,h}\) between any two such bracketing constants; therefore \(\sqrt m\,r_{m,h}\to\sqrt{h/2}\). Multiplying by \(z\) proves \(\sqrt m\,b_m^*\to\sqrt{az/2}\). Substituting \(r=c/\sqrt m\) into the expression for \(W\) yields \(W_m(zc/\sqrt m)\to1/(h+2)\) for every fixed \(c>0\), including at the optimizing sequence, because \(\sqrt m\,r_{m,h}\) converges to a positive constant.

**Strict finite ceiling and its sharpness.** The explicit positive identity
\[
\frac1{h+2}-W_m(zr)=
\frac{hmr+h+2m^2r^3+mr^2+1}
{(h+2)(2mr+1)(hmr+h+mr^2+2mr+1)}>0
\]
holds for every \(m\ge2\), \(h>0\), and \(r\ge0\). The just-proved maximum limit shows the constant \(1/(h+2)=z/(a+2z)\) cannot be lowered uniformly in \(m\). This completes all assertions.

## Verification

The standalone `verify.py` independently solves the full \((m+1)^2\)-state, two-community count-chain stationary master equations using exact rational Gaussian elimination. It compares its within-community discord, cross-community discord, and mean probabilities with the three closed formulas for 12 parameter choices with \(m\in\{2,3,4\}\). It also checks the stated derivative signs and maximizing root numerically for multiple population sizes and rate ratios, and samples the large-population asymptotics. Execute with `python3 verify.py` using the Python standard library only. The program's finite checks corroborate but do not prove the quantified all-size statements; those follow from the preceding analytic proof.

For example, \(m=2\) and \(a=b=z=1\) give \(W=6/25\), \(E=7/25\), \(x=2/5\). If instead \(m=2\) and \(a=z=1\) with variable \(b\), the unique optimal \(b\) is approximately \(0.677224299\).

## Relationship to prior work

Vendeville, Zhou, and Guedj (arXiv:2203.02002) derive general exact pairwise voter-discord master equations for weighted networks with zealots and numerically study within- and between-community discord. The pair equations here are a symmetry reduction of that established general framework, not claimed as a new method. The additional result is a *complete global optimizer classification*, its unique algebraic root, sharp large-community location, and strict optimal-discord envelope for this natural two-clique family.

Gastner and Ishida (arXiv:1908.00849) study two-clique voter consensus times without opposing source resets, and obtain an \(N^{3/2}\) optimal interclique-edge scaling for a different, transient consensus-time objective. The present result concerns a unique stationary law, and its scaling is for the sum of cross-community copying intensities \(m^2b_m^*\), not the number of random links in that paper. Zimmaro, Contucci, and Kertész (arXiv:2303.09587) examine voter-like conflicting preferences on modular networks through approximations and simulation, not this exact stationary discord maximizer. Vendeville and collaborators (arXiv:2006.07265) study stubborn-agent voter opinion distributions with a distinct emphasis. These comparisons do not exclude an unindexed or differently formulated earlier derivation.

## Limitations

The uniqueness and asymptotics require equal-size complete communities, homogeneous pair-copying rates, identical-strength opposing external sources, and binary opinions. The theorem does not assert nonmonotonicity of every possible aggregate discord measure; it concerns a pair of distinct members *within* one community. No stochastic large-network limit beyond the stated probabilities is claimed. The equal-size, rate-homogeneous setting is essential to the two-variable closure. Mathematical originality relative to all possible earlier work is not independently certified.

## References

- A. Vendeville, S. Zhou, B. Guedj, *Discord in the voter model for complex networks*, arXiv:2203.02002v1 (2022-03-03); updated 2024, Phys. Rev. E 109, 024312. https://arxiv.org/abs/2203.02002
- M. T. Gastner, K. Ishida, *Voter model on networks partitioned into two cliques of arbitrary sizes*, arXiv:1908.00849v1 (2019-08-02). https://arxiv.org/abs/1908.00849
- F. Zimmaro, P. Contucci, J. Kertész, *Voter-like dynamics with conflicting preferences on modular networks*, arXiv:2303.09587v1 (2023-03-16). https://arxiv.org/abs/2303.09587
- A. Vendeville et al., *Voter Model with Stubborn Agents on Strongly Connected Social Networks*, arXiv:2006.07265. https://arxiv.org/abs/2006.07265
