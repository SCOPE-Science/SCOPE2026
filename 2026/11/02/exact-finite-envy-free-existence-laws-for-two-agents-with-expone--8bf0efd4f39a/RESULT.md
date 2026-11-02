# Exact finite envy-free existence laws for two agents with exponential chore costs

## Finding

Consider two agents allocating \(m\) indivisible chores, each agent's cost for each chore being an independent rate-one exponential random variable, with additive bundle costs. For \(m\in\{1,2,3,4\}\), the exact probability that **some complete allocation is envy-free** is respectively

\[
\Pr(\mathrm{EF\ exists})=0,\quad \frac12,\quad \frac34,\quad \frac{29}{32}.
\]

For four chores, each agent's normalized cost vector belongs almost surely to exactly one of **12 comparison chambers**: four singleton-dominance chambers, each with probability \(1/8\), and eight nondominant chambers, each with probability \(1/16\). The event of nonexistence is precisely that both agents occupy the same chamber. Consequently the exact failure probability is \(3/32\). The same existence probabilities also hold if the positive costs are interpreted as goods valuations, because the two-agent subset inequalities interchange under complementing the allocation.

## Assumptions and scope

There are exactly two labeled agents and \(m\in\{1,2,3,4\}\) labeled indivisible chores. The \(2m\) costs \(C_{ij}\) are mutually independent with \(C_{ij}\sim\operatorname{Exp}(1)\). Each agent has additive cost \(c_i(S)=\sum_{j\in S}C_{ij}\). An allocation assigns all chores, with one bundle \(S\) to agent 1 and its complement \(S^c\) to agent 2. It is envy-free when \(c_1(S)\le c_1(S^c)\) and \(c_2(S^c)\le c_2(S)\). Empty bundles are allowed but never envy-free for positive costs if the other bundle contains all chores. All subset-half ties have probability zero, so strict inequalities suffice almost surely.

Let \(X_j=C_{1j}/\sum_k C_{1k}\) and \(Y_j=C_{2j}/\sum_k C_{2k}\). Each vector is independent and uniform on the simplex \(\{x_j>0:\sum_jx_j=1\}\): the change of variables from exponential coordinates to total and proportions has joint density proportional to \(e^{-t}t^{m-1}\), which factorizes, leaving constant density in the proportions. The claim is exactly about this exponential/Dirichlet model, not arbitrary cost distributions.

## Proof

**1. Comparison-chamber reduction.** For a normalized cost vector \(x\) and subset \(S\), put \(h_S(x)=2\sum_{j\in S}x_j-1\). Almost surely \(h_S(x)\ne0\) simultaneously for all proper subsets \(S\). Allocating \(S\) to agent 1 is envy-free precisely when \(h_S(X)<0<h_S(Y)\). Since \(h_{S^c}=-h_S\), an envy-free allocation exists if and only if the two agents' full sign vectors \((\operatorname{sgn}h_S)\) differ. If they differ on one subset in the reverse direction, its complement gives the required orientation. Thus, for the distinct feasible sign chambers with probabilities \(p_H\), independence gives

\[
\Pr(\mathrm{EF\ does\ not\ exist})=\sum_H p_H^2.
\]

For \(m=1\), every cost is positive and no envy-free allocation is possible. For \(m=2\), the sign comparison is just which of two coordinates is larger. Each of two chambers has probability \(1/2\), yielding success \(1/2\).

**2. Three chores.** Every singleton may have normalized cost above \(1/2\), but at most one can. For a uniform three-coordinate simplex point, \(\Pr(X_1>1/2)=(1/2)^2=1/4\) (the indicated corner is a \(1/2\)-scaled simplex). The three dominant-singleton events each have probability \(1/4\), and their complement, in which none dominates, has probability \(1/4\). All subset signs are determined by these singleton signs and their complements. Therefore there are four chambers of mass \(1/4\), yielding \(1-4(1/4)^2=3/4\).

**3. Four chores: tetrahedral sign geometry.** For \(x_1+x_2+x_3+x_4=1\), define the three representative pair contrasts

\[
u=x_1+x_2-x_3-x_4,\qquad
v=x_1+x_3-x_2-x_4,\qquad
w=x_1+x_4-x_2-x_3.
\]

The inverse map is

\[
4(x_1,x_2,x_3,x_4)=
(1+u+v+w,\,1+u-v-w,\,1-u+v-w,\,1-u-v+w).
\]

The uniform simplex maps by a constant-Jacobian affine transformation onto the tetrahedron \(T\subset\mathbb R^3\) with vertices

\[
(1,1,1),\ (1,-1,-1),\ (-1,1,-1),\ (-1,-1,1).
\]

Its ordinary Euclidean volume is \(\operatorname{Vol}(T)=8/3\). Its intersection with the positive octant \(\{u,v,w>0\}\) is the union (up to their common base) of the tetrahedra with apexes \((0,0,0)\) and \((1,1,1)\), respectively, and common base \((1,0,0),(0,1,0),(0,0,1)\). Their volumes are \(1/6\) and \(1/3\). Therefore that octant has probability \((1/2)/(8/3)=3/16\). Permutations of the four chores interchange the four octants containing tetrahedron vertices, so each of these four *even-sign* octants has probability \(3/16\). The remaining four octants are also permuted transitively, so each has probability \((1-4\cdot3/16)/4=1/16\).

On the other hand, \(\Pr(X_j>1/2)=(1/2)^3=1/8\) for every \(j\). These four disjoint events are contained one apiece in the four even-sign pair-contrast octants: if \(x_j>1/2\), every pair containing \(j\) weighs more than half, and the resulting triple of pair signs specifies the associated even-sign octant. Each even-sign octant consequently has nondominant mass \(3/16-1/8=1/16\); an odd-sign octant cannot contain a dominant singleton and therefore has nondominant mass \(1/16\). When no singleton dominates, the singleton signs are all negative and the three pair signs distinguish its eight chambers. When a singleton dominates, all pair signs are determined by that singleton. Thus there are exactly four chambers of mass \(1/8\) and eight of mass \(1/16\). Substitution into the chamber-collision formula gives

\[
\Pr(\mathrm{EF\ fails})=4\left(\frac18\right)^2+8\left(\frac1{16}\right)^2
=\frac3{32},\qquad
\Pr(\mathrm{EF\ exists})=\frac{29}{32}.
\]

**4. Goods–chores equivalence for two agents.** With the same positive numbers treated instead as goods valuations, the fairness inequalities for a subset \(S\) assigned to the first agent are \(h_S(X)>0>h_S(Y)\), the complement of the chore inequalities. As \(S\) ranges over all subsets, the existence events coincide pointwise (outside ties). This does not assert an equivalent probability for a fixed allocation or for more than two agents.

## Verification

The standalone standard-library program `verify.py` reproduces the tetrahedron determinant calculation and all exact chamber probabilities using rational arithmetic. It additionally compares direct exhaustive subset checks of the envy-free event with the sign-chamber criterion on \(30{,}000\), \(40{,}000\), and \(60{,}000\) seeded exponential samples for respectively two, three, and four chores. These samples are sanity checks, not substitutes for the general finite-dimensional measure proof above. Run `python3 verify.py` in the directory containing this file and `verify.py`.

## Relationship to prior work

Manurangsi and Suksompong, *Asymptotic Fair Division: Chores Are Easier Than Goods*, first made public on April 29, 2025, prove high-probability existence results for random chore costs, especially at or beyond the scale \(m\ge2n\). Their main upper/existence theorem assumes a distribution on \([0,1]\) with a density bounded above and below by positive constants. The unbounded exponential model here is **not** covered by that assumption; more importantly, a high-probability asymptotic theorem does not determine the exact two-agent, four-chore probability. Their paper's existence and nonexistence arguments, including the full formal preliminaries, were compared with this chamber-collision statement. Manurangsi and Suksompong, *When Do Envy-Free Allocations Exist?* (2018 preprint; 2020 journal publication), analyze corresponding asymptotic phenomena for goods, not this finite exact exponential probability. The goods formulation above is checked as an alias for the same two-agent existence event, not claimed as a separate discovery.

## Limitations

The sharp probabilities require independent identically distributed exponential costs, exactly two agents, and at most four items. The proof does not establish exact laws for five or more chores, other cost distributions, correlated costs, constrained/balanced allocations, or optimal expected social cost. Although all allocations are considered, an imposed requirement that the two bundles have equal cardinality may change the success event. The result is a mathematically exact but narrow finite benchmark and is not independently validated; an unindexed equivalent prior calculation may exist.

## References

- P. Manurangsi and W. Suksompong, *Asymptotic Fair Division: Chores Are Easier Than Goods*, arXiv:2504.20704v1, posted 2025-04-29, https://arxiv.org/html/2504.20704v1 .
- P. Manurangsi and W. Suksompong, *When Do Envy-Free Allocations Exist?*, arXiv:1811.01630v1, posted 2018-11-05; SIAM Journal on Discrete Mathematics 34(3) (2020), 1505–1521, https://arxiv.org/html/1811.01630v1 .
- J. Dickerson et al., *The Computational Rise and Fall of Fairness*, AAAI (2014); https://ojs.aaai.org/index.php/AAAI/article/view/8884 .
