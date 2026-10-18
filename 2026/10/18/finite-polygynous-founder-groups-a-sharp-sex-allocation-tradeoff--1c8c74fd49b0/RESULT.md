# Finite polygynous founder groups: a sharp sex-allocation tradeoff and logarithmic male reserves

## Finding
For every integer group size \(n\ge3\) and male mating capacity \(h\ge2\), suppose the sexes of the \(n\) founders are independently assigned, with female probability \(p\). One male can fertilize at most \(h\) females, each female requires one available mating, and other constraints are absent. If \(F\sim\operatorname{Bin}(n,p)\), let \(B=\min\{F,h(n-F)\}\) be the number of reproductive females and \(R_{n,h}(p)=\mathbb E B\).

**Theorem (one-generation output versus feasibility).** The polynomial \(R_{n,h}\) is strictly concave on \((0,1)\) and has a unique maximizer \(p_{n,h}\in(1/2,1)\). In contrast, the probability of at least one mating,
\[
S_n(p)=1-p^n-(1-p)^n,
\]
has its unique maximizer at \(p=1/2\). Thus for every \(n\ge3,h\ge2\), the output-maximizing stochastic sex allocation strictly reduces the probability that at least one pair can reproduce. The boundaries are sharp: for \(h=1\), or for \(n=2\), the two criteria share the optimum \(1/2\).

For fixed \(h\) and increasing \(n\), put \(p_0=h/(h+1)\). Then
\[
p_{n,h}\longrightarrow p_0,\qquad
R_{n,h}(p_{n,h})-R_{n,h}(1/2)
=\frac{h-1}{2(h+1)}n+o(n).
\]
When \(n\) is a multiple of \(h+1\), set \(q=hn/(h+1)\). The optimum is uniquely specified by the exact binomial quantile equation
\[
\Pr\{\operatorname{Bin}(n-1,p_{n,h})\le q-1\}=\frac{h}{h+1}.
\]
For fixed \(h\ge2\), along these multiples,
\[
\sqrt n\,(p_0-p_{n,h})\longrightarrow
\frac{\sqrt h}{h+1}\Phi^{-1}\!\left(\frac{h}{h+1}\right)>0,
\]
where \(\Phi\) is the standard normal distribution function. The finite optimum is therefore shifted toward males by a quantitatively determined square-root correction relative to the capacity-balanced deterministic ratio.

Finally, if one male can service every other founder (\(h\ge n-1\)), the finite optimum and its yield have the closed forms
\[
p_{n,h}=n^{-1/(n-1)},\qquad
R_{n,h}(p_{n,h})=(n-1)n^{-1/(n-1)}.
\]
Along \(n\to\infty\) with \(h\ge n-1\), the expected number of **male** founders at this optimum is \(\log n+o(1)\), while the probability of no mating is \(n^{-1}+o(n^{-1})\). The optimal reserve is logarithmic rather than a fixed number of males.

## Assumptions and scope
The claim concerns a single mating episode in a finite founding group with independently assigned sex. The controllable parameter \(p\in[0,1]\) is the *female* assignment probability and \(h\in\{1,2,\ldots\}\) is an integer capacity. Every individual has unit potential reproductive contribution, male capacities are additive and fungible, and group members can encounter each other; no female mates more than once. No spatial, density, pedigree, age, energetic, game-theoretic, evolutionary-stability, or multigeneration dynamics are assumed. The feasibility objective \(S_n\) means the group has at least one member of each sex, not its probability of indefinite persistence.

Define \(g_{n,h}(k)=\min\{k,h(n-k)\}\), for integer \(0\le k\le n\). For any \(0\le p\le1\),
\[
R_{n,h}(p)=\sum_{k=0}^n{n\choose k}p^k(1-p)^{n-k}g_{n,h}(k).
\]
The conventions are \(R_{1,h}=0\) and \(S_1=0\) when only one founder exists. The strict-concavity assertion holds for \(n\ge2\), all \(h\ge1\).

## Proof
**1. Strict concavity and the unique output optimum.** Write \(g=g_{n,h}\), \(\Delta g(k)=g(k+1)-g(k)\), and \(\Delta^2g(k)=g(k+2)-2g(k+1)+g(k)\). The function on the real interval \([0,n]\) given by the minimum of the affine functions \(x\) and \(h(n-x)\) is concave, so \(\Delta^2g(k)\le0\) for every \(0\le k\le n-2\). Its first discrete slopes start positive and end negative, hence at least one second difference is strictly negative whenever \(n\ge2\) and \(h\ge1\). Twice differentiating the Bernstein polynomial gives
\[
R_{n,h}''(p)=n(n-1)\sum_{k=0}^{n-2}{n-2\choose k}p^k(1-p)^{n-2-k}\Delta^2g(k)<0
\]
for every \(0<p<1\), since every binomial weight is strictly positive there. The endpoint slopes are \(R'(0)=n[g(1)-g(0)]>0\) and \(R'(1)=n[g(n)-g(n-1)]<0\). Thus there is exactly one interior maximizer.

**2. Its location and opposing feasibility objective.** At \(p=1/2\), direct differentiation and pairing each term \(k\) with \(n-k\) yields
\[
R_{n,h}'(1/2)=2^{1-n}\sum_{0\le k<n/2}{n\choose k}(n-2k)\,[g(n-k)-g(k)].
\]
For every \(k<n/2\), \(g(k)=k\), whereas \(g(n-k)=\min\{n-k,hk\}\ge k\). If \(n\ge3\) and \(h\ge2\), the summand for \(k=1\) is strictly positive because both \(n-1>1\) and \(h>1\). Thus \(R'(1/2)>0\) and the strict-concavity maximizer satisfies \(p_{n,h}>1/2\). If \(h=1\), then \(g(k)=g(n-k)\), and if \(n=2\), \(g(1)=1\) for every capacity: in either case the maximizer is \(1/2\). The feasibility function is \(S_n(p)=\Pr(1\le F\le n-1)=1-p^n-(1-p)^n\). Its derivative is \(n[(1-p)^{n-1}-p^{n-1}]\), giving the unique maximizer \(1/2\) for \(n\ge2\). This proves the sharp conflict, including the strict loss of feasibility at the output optimum.

**3. The fixed-capacity limit.** For fixed \(h\), the normalized function \(\bar g(x)=\min\{x,h(1-x)\}\) is Lipschitz with constant at most \(h\). Since \(\mathbb E(F/n)=p\) and \(\operatorname{Var}(F/n)=p(1-p)/n\), uniformly in \(p\in[0,1]\),
\[
\left|\frac{R_{n,h}(p)}n-\bar g(p)\right|
\le h\,\mathbb E|F/n-p|\le\frac{h}{2\sqrt n}.
\]
The unique maximum of \(\bar g\) is at \(p_0=h/(h+1)\), with height \(h/(h+1)\); at \(p=1/2\), its value is \(1/2\). Uniform convergence and uniqueness force \(p_{n,h}\to p_0\), and the displayed asymptotic gain follows.

**4. Exact quantile and second-order displacement.** Suppose \(n=(h+1)t\), so \(q=ht\) is the integer junction of the two branches of \(g\). The discrete slopes obey \(\Delta g(k)=1\) for \(0\le k\le q-1\) and \(\Delta g(k)=-h\) for \(q\le k\le n-1\). The first Bernstein derivative is therefore
\[
\frac1nR_{n,h}'(p)=(h+1)\Pr\{\operatorname{Bin}(n-1,p)\le q-1\}-h.
\]
The probability is strictly decreasing from one to zero in \(p\in(0,1)\), giving the unique quantile equation. Let \(Z\sim\operatorname{Bin}(n-1,p_{n,h})\). We already proved \(p_{n,h}\to p_0\in(0,1)\). Standard binomial central-limit convergence for these varying parameters, together with the continuity and strict monotonicity of \(\Phi\), implies
\[
\frac{q-1-(n-1)p_{n,h}}{\sqrt{(n-1)p_{n,h}(1-p_{n,h})}}
\longrightarrow \Phi^{-1}(p_0).
\]
Since \(q=np_0\), the numerator is \(n(p_0-p_{n,h})-(1-p_{n,h})\). Dividing by \(\sqrt n\) and rearranging establishes
\[
\sqrt n(p_0-p_{n,h})\to\sqrt{p_0(1-p_0)}\Phi^{-1}(p_0)
=\frac{\sqrt h}{h+1}\Phi^{-1}\!\left(\frac h{h+1}\right).
\]
The normal quantile is strictly positive for \(h\ge2\).

**5. Saturated male capacity.** If \(h\ge n-1\), then \(g(k)=k\) for each \(k<n\), while \(g(n)=0\). Thus
\[
R_{n,h}(p)=\mathbb EF-n\Pr(F=n)=np-np^n,
\]
whose interior derivative vanishes only at \(p=n^{-1/(n-1)}\). Substitution yields the stated yield. The identity \(p=\exp[-\log n/(n-1)]\) gives \(n(1-p)=\log n+O((\log n)^2/n)\). Furthermore, the no-mating probability is \(p^n+(1-p)^n=n^{-n/(n-1)}+(1-n^{-1/(n-1)})^n=n^{-1}+o(n^{-1})\), establishing the asymptotics.

## Verification
A standalone Python standard-library checker (`verify_polygynous_founders.py`) reconstructs the exact Bernstein coefficients, computes endpoint/center derivatives, checks binomial-quantile identities and saturated-capacity formulas, and compares the CLT and logarithmic-reserve predictions with finite examples. It passes 600 exact-arithmetic discrete-concavity and sex-ratio cases, plus additional exact identities and numerical illustrations. Finite checks do not establish the assertions for all \(n,h\); Steps 1–5 above provide the universal proofs.

For the smallest strict case \(n=3,h=2\), the optimal female probability is \(1/\sqrt3\), expected reproductive females equal \(2/\sqrt3\) (versus \(9/8\) at \(p=1/2\)), and the probability of at least one mating is \(\sqrt3-1\) (versus \(3/4\) at \(p=1/2\)).

## Relationship to prior work
Bessa-Gomes, Legendre, and Clobert (2004) already write down **the identical binomial expectation of the minimum mating function** as their per-capita birth rate (their Eq. 9) and examine sex-ratio effects on extinction risk. Neither that expectation nor the qualitative sex-ratio dependence is claimed as new. Their figures and text do not give the unique finite optimum for every group size, its exact binomial-quantile equation, square-root asymptotic correction, or logarithmic optimal male reserve when mating capacity grows with group size. Tongen, Zubillaga, and Rabinovich (2016) provide an age-structured harem-population matrix model, including sex-ratio and harem-size effects; their growth-rate and stage-structure analysis is not a finite independent-sex founder-group allocation theorem. Lindström (1998) studies sex-sensitive harvest management and deterministic adult sex-ratio choices, providing context for female-biased mating systems but not the displayed random finite-group dual objective or binomial quantile. Engen, Lande, and Sæther (2003) and Sæther and coauthors (2004) analyze demographic sex-ratio fluctuations, extinction, and mating systems; these general phenomena are not claimed as new. Leach and coauthors (2020) explicitly model binomial stochastic sex assignment and group-formation effects; their accessible model fixes the sex-assignment parameter at \(1/2\) in the stochastic experiments and does not state the analytic maximizer, quantile, or logarithmic reserve result. The mating-capacity minimum function itself is pre-existing, including Bessa-Gomes, Legendre, and Clobert (2004, 2010): originality claimed here is restricted to the sharp optimization classification and the two asymptotic laws under the explicit model.

## Limitations
Only one mating episode is modeled; \(S_n\) is a feasibility probability, not the probability of long-term population survival. The model ignores differential survival, mate-search friction, reproductive variance beyond sex assignment, density feedback, interactions between groups, and fitness evolution. The quantile formula and square-root correction are stated for integer capacities and sizes divisible by \(h+1\); the leading fixed-capacity limit holds for arbitrary group sizes. The logarithmic reserve holds for a capacity growing at least as fast as group size, not for fixed capacity. The 2004 article already contains the same binomial expected-mating expression and sex-ratio graphs; a relevant 2010 mating-function paper could not be inspected in full; an overlooked equivalent optimization statement is a residual literature risk. Neither finite checks nor unsuccessful searches establish novelty.

## References
1. C. Bessa-Gomes, S. Legendre, and J. Clobert (2004), “Allee effects, mating systems and the extinction risk in populations with two sexes,” *Ecology Letters* 7(9), 802–812. DOI: 10.1111/j.1461-0248.2004.00632.x. Public date: 2004-07-28.
2. A. Tongen, M. Zubillaga, and J. E. Rabinovich (2016), “A two-sex matrix population model to represent harem structure,” *Mathematical Biosciences and Engineering* 13(5), 1077–1092. DOI: 10.3934/mbe.2016031. Public date: 2016-07-01.
3. J. Lindström (1998), “Harvesting and sex differences in demography,” *Wildlife Biology*. DOI: 10.2981/wlb.1998.024.
4. S. Engen, R. Lande, and B.-E. Sæther (2003), “Demographic stochasticity and Allee effects in populations with two sexes,” *Ecology* 84(9), 2378–2386. DOI: 10.1890/02-0123.
5. B.-E. Sæther et al. (2004), “Time to extinction in relation to mating system and type of density regulation in populations with two sexes,” *Journal of Animal Ecology* (online full text examined).
6. A. Bessa-Gomes, S. Legendre, and J. Clobert (2010), “Discrete two-sex models of population dynamics: on modelling the mating function,” *Acta Oecologica*. DOI: 10.1016/j.actao.2010.02.010 (full text not inspected).
7. T. Leach et al. (2020), “Stochasticity in social structure and mating system drive extinction risk,” *Ecosphere*. DOI: 10.1002/ecs2.3038.
