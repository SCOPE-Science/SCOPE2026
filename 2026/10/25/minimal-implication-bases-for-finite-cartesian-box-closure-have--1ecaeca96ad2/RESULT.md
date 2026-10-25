# Minimal implication bases for finite Cartesian box closure have sharp logarithmic parallel depth

## Finding

**Theorem.** Fix an integer \(d\ge1\), integers \(q_1,\ldots,q_d\ge2\), and the finite grid \(X=\prod_{i=1}^d\{0,\ldots,q_i-1\}\) of size \(N=\prod_i q_i\). Let \(c(S)\) be the smallest axis-parallel integer box containing \(S\subseteq X\), with \(c(\varnothing)=\varnothing\). Put \([u,v]=\{z\in X:\min(u_i,v_i)\le z_i\le\max(u_i,v_i)\text{ for all }i\}\).

The complete set of Duquenne–Guigues pseudo-intents of \(c\) is
\[
\mathcal P=\bigl\{\{u,v\}:u\ne v,\ [u,v]\ne\{u,v\}\bigr\}.
\]
Consequently, the canonical Duquenne–Guigues basis is exactly
\[
\mathcal B=\bigl\{\{u,v\}\longrightarrow [u,v]\setminus\{u,v\}:\{u,v\}\in\mathcal P\bigr\},
\]
and, allowing multiple conclusion points per implication, its number of rules is **globally minimum** among *all* sound complete finite implicational bases:
\[
\boxed{\ |\mathcal B|=\binom N2-\sum_{i=1}^d(q_i-1)\prod_{j\ne i}q_j.\ }
\]

For simultaneous rounds of forward chaining by this basis, with all premises tested against the preceding round, the exact maximum number of nontrivial rounds over all initial sets \(S\subseteq X\) is
\[
\boxed{\quad R(q_1,\ldots,q_d)=
\begin{cases}
0,&d=1,\ q_1=2,\\
1,&d=1,\ q_1\ge3,\\
\lceil\log_2 d\rceil,&d\ge2.
\end{cases}\quad }
\]
Thus a globally cardinality-minimal implication basis need not be one-round direct; its sharp worst-case parallel depth is logarithmic in the number of factors and independent of their lengths.

## Assumptions and scope

All chains are finite and nontrivial. The incidence context providing the closure has **objects** all nonempty Cartesian integer boxes \(B\subseteq X\), **attributes** the points \(x\in X\), and incidence \(B I x\) precisely when \(x\in B\). Attribute closure is \(c(S)=S''\), the intersection of all boxes containing \(S\). Empty-set closure is empty because at least two singleton boxes have empty intersection.

A sound implication \(A\to C\) has \(C\subseteq c(A)\); a complete basis generates precisely \(c\) by iterated forward chaining. A rule with several conclusions counts as **one** implication. Two distinct elements \(u,v\in X\) form a closed pair exactly when they differ in one coordinate by one step. The formula does not claim minimality of the **total number of conclusion literals**, nor an optimal parallel depth among every possible cardinality-minimal basis. The depth assertion concerns the displayed canonical basis with its full-box conclusions.

For \(S\ne\varnothing\), write \(\ell_i(S)=\min\{s_i:s\in S\}\), \(h_i(S)=\max\{s_i:s\in S\}\). Then \(c(S)=\prod_i[\ell_i(S),h_i(S)]\cap X\). This is an integer box, not the Euclidean convex hull.

## Proof

**1. Pair-generated closure.** For any \(S\subseteq X\), repeatedly filling the boxes \([u,v]\) for all pairs currently present yields \(c(S)\). Indeed the process never leaves \(c(S)\). If its terminal set \(T\) is nonempty and closed under all pair boxes, then for every \(u,v\in T\) it contains their coordinatewise meet and join. Finiteness yields \(\ell(S)=\bigwedge_{s\in S}s\in T\) and \(h(S)=\bigvee_{s\in S}s\in T\); because \([\ell(S),h(S)]\subseteq T\), necessarily \(T=c(S)\). The empty case is immediate.

**2. Exact pseudo-intents.** We use the recursive definition: a nonclosed set \(P\) is a pseudo-intent if every pseudo-intent \(Q\subsetneq P\) has \(c(Q)\subseteq P\). The empty set and every singleton are closed. Hence each nonclosed pair is a pseudo-intent. Suppose a pseudo-intent \(P\) has at least three elements. Every distinct pair \(\{u,v\}\subseteq P\) is either closed (so \([u,v]=\{u,v\}\subseteq P\)) or is a smaller pseudo-intent (so \([u,v]\subseteq P\) by definition). Thus \(P\) is pair-box closed, whence \(P=c(P)\) by step 1, contradiction. Therefore the pseudo-intents are precisely the nonclosed pairs, and the displayed implications are exactly the canonical basis.

**3. Global minimum number of rules.** Let \(\mathcal D\) be *any* sound complete basis. For each nonclosed pair \(Q=\{u,v\}\), its closure contains points outside \(Q\). Both \(\varnothing\) and all singletons are closed, so no sound implication with a premise properly contained in \(Q\) can add a point outside \(Q\) when forward chaining starts at \(Q\). The first addition must therefore be licensed by some nontrivial rule whose premise is exactly \(Q\). Distinct pairs require distinct premise sets and hence distinct rules. So \(|\mathcal D|\ge|\mathcal P|\); equality is attained by \(\mathcal B\). An unordered pair is closed exactly if it is an edge of the Cartesian product of paths on the chains, whose number of edges is \(\sum_i(q_i-1)\prod_{j\ne i}q_j\). Subtracting from \(\binom N2\) gives the formula.

**4. Small-support lemma for coordinate boxes.** Suppose \(d\ge2\), \(S\subseteq X\), and \(z\in c(S)\). We claim some \(T\subseteq S\) with \(|T|\le d\) satisfies \(z\in c(T)\). Choose inclusion-minimal \(T\). If \(|T|\le2\), the claim holds. Otherwise, for each \(t\in T\), removal of \(t\) must make \(z\notin c(T\setminus\{t\})\). Thus for some coordinate \(i\), either every other member has coordinate strictly greater than \(z_i\) or every other member has coordinate strictly less than \(z_i\). Each such coordinate can certify at most one essential member of a set of at least three: two distinct candidates with the same strict direction contradict one another, and opposite strict directions are incompatible in the presence of a third member. Hence \(|T|\le d\).

**5. Balanced merging lemma.** If \(T\subseteq X\) has \(k\ge1\) elements, then every point in \(c(T)\) can be derived from \(T\) in at most \(\lceil\log_2 k\rceil\) parallel rounds of \(\mathcal B\). Induct on \(k\). Partition \(T=T_1\sqcup T_2\) with each block of size at most \(\lceil k/2\rceil\). By induction, after \(r=\lceil\log_2\lceil k/2\rceil\rceil\) rounds, every point of \(c(T_1)\cup c(T_2)\) has appeared. For any \(z\in c(T)\), in each coordinate choose \(u_i\) and \(v_i\) by clamping \(z_i\) to the two intervals \([\ell_i(T_1),h_i(T_1)]\) and \([\ell_i(T_2),h_i(T_2)]\), respectively. Then \(u\in c(T_1)\), \(v\in c(T_2)\), and \(z\in[u,v]\). (If the two interval projections lie on one side of \(z_i\), that side would also contain both original intervals, contradicting \(z_i\in[\ell_i(T),h_i(T)]\).) The rule for \(\{u,v\}\), or the fact \(z=u=v\), supplies \(z\) at the next round. Since \(1+\lceil\log_2\lceil k/2\rceil\rceil=\lceil\log_2 k\rceil\) for \(k\ge2\), the assertion follows. When \(\{u,v\}\) is an adjacent closed pair, its box is just the pair and the point was already present.

By steps 4 and 5, \(R\le\lceil\log_2 d\rceil\) when \(d\ge2\). For \(d=1\), the extrema of every nonempty \(S\) are an original pair, giving \(R\le1\); and if \(q_1=2\), all sets are closed.

**6. Sharpness.** For \(d\ge2\), choose the binary subgrid \(\{0,1\}^d\subseteq X\) and take \(S=\{e_1,\ldots,e_d\}\), the \(d\) unit vectors. The all-ones word \(\mathbf1\) belongs to \(c(S)\). Every point produced by round \(r\) is contained in \(c(T)\) for some \(T\subseteq S\) with \(|T|\le2^r\): true at round zero, and a newly inferred box point has a support equal to the union of two previous supports. But \(\mathbf1\in c(T)\) requires every \(e_i\in T\), since no other seed has a one in coordinate \(i\). Therefore \(2^r\ge d\), giving \(r\ge\lceil\log_2 d\rceil\). For \(d=1\), \(q_1\ge3\), the two extreme values produce an interior point after exactly one round. All bounds are attained.

## Verification

The standalone standard-library program `verify.py` reconstructs the grid and every pair box independently, enumerates the canonical rules, compares their iterated closure against direct min–max box closure, and for small grids recursively computes pseudo-intents from their definition. Exhaustive initial-subset runs cover seven grids up to the binary four-cube (65,536 initial sets); deterministic samples cover larger grids. It also checks the sharpness witness up to six coordinates. Reproduce with `python verify.py`.

Representative exhaustive counts: for \((q_1,q_2,q_3)=(2,2,2)\), there are 16 rules and the depth histogram is \((28,212,16)\) at rounds 0, 1, 2; for \((2,2,2,2)\), there are 88 rules and the histogram is \((82,61838,3616)\). These finite tests do not constitute a proof for all grids; steps 1–6 do.

## Relationship to prior work

Baixeries and Napoli (2024) compare minimal and direct implication bases, including the Duquenne–Guigues basis, in general closure computation. Buzmakov and coauthors (2022) experimentally investigate concise presentations of concepts and implications. Bichoupan (2022) establishes complexity barriers for optimizing implication bases of convex geometries. These results motivate the minimum-cardinality versus execution-depth question; no inspected theorem provides this grid-specific exhaustive pseudo-intent classification, exact formula, and sharp parallel-round bound together. The closure here is a coordinatewise box closure, not Euclidean convexity or the different rule closing pairs of words differing in exactly two coordinates.

## Limitations

The theorem treats finite products of nontrivial chains and multi-conclusion Horn rules. The round count concerns synchronous forward chaining for the specified full-box canonical basis, not arbitrary rule-firing schedules, literal-minimal presentations, or every minimum-cardinality basis. The originality comparison is best-knowledge rather than a proof of global publication priority; equivalent results under other terminology, especially discrete box convexity, remain possible. Independent validation has not been performed.

## References

1. J. Baixeries and A. Napoli, *A minimal base or a direct base? That is the question!*, arXiv:2404.12229, version 1 publicly posted 18 April 2024, https://arxiv.org/abs/2404.12229.
2. A. Buzmakov et al., *Experimental Study of Concise Representations of Concepts and Dependencies*, arXiv:2205.02464, https://arxiv.org/abs/2205.02464.
3. T. Bichoupan, *Complexity Results for Implication Bases of Convex Geometries*, arXiv:2211.08524, publicly posted 15 November 2022, https://arxiv.org/abs/2211.08524.
