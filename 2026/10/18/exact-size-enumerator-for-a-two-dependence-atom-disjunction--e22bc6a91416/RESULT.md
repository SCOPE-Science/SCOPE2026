# Exact size enumerator for a two-dependence-atom disjunction

## Finding

For three finite nonempty sets \(X,Y,Z\) of cardinalities \(m,r,s\), respectively, consider all teams \(T\subseteq X\times Y\times Z\) under lax splitting-disjunction semantics. Let
\[
\Phi=\operatorname{dep}(x,y)\vee\operatorname{dep}(x,z),
\]
where \(\operatorname{dep}(x,y)\) means that any two assignments agreeing in \(x\) agree in \(y\). Define the size enumerator
\[
F_{m,r,s}(t)=\sum_{\substack{T\subseteq X\times Y\times Z\\T\models\Phi}}t^{|T|}.
\]
**Theorem.** For every \(m,r,s\ge1\),
\[
\boxed{F_{m,r,s}(t)=H_{r,s}(t)^m},
\]
where the following explicitly given polynomial counts admissible single-fiber subteams:
\[
\begin{aligned}
H_{r,s}(t)={}&rs(1+t)^{r+s-1}-(rs-1)-rs(r+s-2)t\\
&-r(s-1)\big((1+t)^s-1-st\big)\\
&-s(r-1)\big((1+t)^r-1-rt\big)\\
&-2\binom r2\binom s2t^2.
\end{aligned}
\]
In particular \([t^k]F_{m,r,s}(t)\) is the exact number of satisfying teams of size \(k\). For the ordinary unsorted domain of size \(q\), take \(m=r=s=q\): the numbers of satisfying teams are \(2\), \(225\), and \(5{,}639{,}752\) for \(q=1,2,3\), respectively. The one-fiber totals for \(q=1,2,3,4\) are \(2,15,178,1601\).

For independently present assignments, each included with probability \(p\in(0,1)\), the exact satisfaction probability is
\[
\Pr_p(T\models\Phi)=(1-p)^{mrs}H_{r,s}\!\left(\frac p{1-p}\right)^m.
\]
The endpoint probabilities at \(p=0\) and \(p=1\) follow directly from the finite polynomial.

## Assumptions and scope

A team is a **set** of assignments (not a multiset), with one element of each finite sort \(X,Y,Z\) per assignment. Splitting disjunction permits \(T=T_1\cup T_2\), with either or both subteams empty and with overlap allowed; downward closure makes overlap immaterial here. The formula \(\Phi\) is open, and satisfaction is evaluated on the whole team; no probabilistic independence is needed for the enumerator itself. All three cardinalities are positive integers, and polynomial coefficients are over the ordinary integers.

## Proof

**Step 1 (fiberwise characterization).** For each \(a\in X\), write \(S_a=\{(b,c):(a,b,c)\in T\}\subseteq Y\times Z\). A split witnessing \(\Phi\) restricts on each \(a\)-fiber to a set of assignments having one \(y\)-value and a complementary set having one \(z\)-value. Thus for some \(b_a\in Y\), \(c_a\in Z\),
\[
S_a\subseteq C_{b_a,c_a}:=(\{b_a\}\times Z)\cup(Y\times\{c_a\}).
\]
Conversely, if all fibers admit such a *cross*, collect into the first disjunct all assignments with \(y=b_a\); the remaining assignments have \(z=c_a\) and satisfy the second disjunct. This is a valid global split, so the cross condition is necessary and sufficient. Choices for distinct \(a\) are independent; if \(H_{r,s}\) counts each cross-coverable fiber by its number of cells, \(F_{m,r,s}=H_{r,s}^m\).

**Step 2 (multiplicity of cross coverings).** Each of the \(rs\) crosses \(C_{b,c}\) has exactly \(r+s-1\) cells. The sum of their subset-generating polynomials is \(rs(1+t)^{r+s-1}\). This counts a cross-coverable set \(U\) as many times as there are crosses containing it. If two distinct crosses have the same designated row, their intersection is that row; if they have the same designated column, their intersection is that column. If both row and column differ, the intersection consists of exactly the two diagonally opposite cells \((b,c')\) and \((b',c)\). Consequently the **only** repeatedly counted sets are: the empty set; singletons; subsets of size at least two lying in one row; subsets of size at least two lying in one column; and diagonal pairs (two points in different rows and columns).

The empty set occurs \(rs\) times and contributes an excess \(rs-1\). Each of the \(rs\) singleton sets occurs \(r+s-1\) times, giving excess \(rs(r+s-2)t\). For a fixed row, any subset of size at least two is covered by exactly \(s\) crosses; there are \(r\) rows, giving excess
\[
r(s-1)\big((1+t)^s-1-st\big).
\]
Analogously the column excess is \(s(r-1)((1+t)^r-1-rt)\). Every diagonal pair is covered by exactly two crosses, and their number is \(2\binom r2\binom s2\), yielding the final excess term. The five cases are disjoint and exhaustive among sets with multiplicity greater than one. Subtracting exactly these excess weights proves the formula for \(H_{r,s}\).

**Step 3 (size and probability).** The coefficient definition proves the exact cardinality distribution. Under independent Bernoulli inclusion, each team of size \(k\) has probability \(p^k(1-p)^{mrs-k}\). Summing over satisfying teams gives \((1-p)^{mrs}F_{m,r,s}(p/(1-p))\), as claimed.

## Verification

The standalone `verify.py` independently enumerates all subsets of each rectangular \(r\times s\) fiber for \(1\le r,s\le4\), computes the admissibility criterion directly from cross masks, and checks each coefficient of the closed polynomial. It also enumerates all \(256\) teams on a two-element unsorted domain with three variables, testing the defining lax-split semantics by examining all splits rather than using the cross characterization. Both checks agree with the proof, including the total \(225\) satisfying binary teams. Run with `python3 verify.py`; expected final line: `DEPENDENCE_RECTANGULAR_SIZE_ENUMERATOR_OK`. Finite checks are corroboration; the preceding proof applies to all cardinalities.

## Relationship to prior work

Fröhlich, Kolaitis, and Meier establish in *Disjunctions of Two Dependence Atoms* that \(\operatorname{dep}(x,y)\vee\operatorname{dep}(x,z)\) has coherence level four and belongs to the first-order-definable model-checking class (Theorem 22 and the main trichotomy). The present exact size-by-size enumeration, rectangular-domain formula, and Bernoulli satisfaction law concern counting *all* satisfying teams, not deciding one supplied team or bounding minimal counterexamples. Their proof includes a local splitting characterization; it does not state the above weighted enumerator. Earlier work on enumeration *algorithms* for satisfying teams likewise addresses a different quantitative question. The underlying graph-theoretic notion is a bipartite edge set contained in the edges incident to one vertex on each side. No novelty is claimed for elementary counting principles, union-of-crosses descriptions, or dependence-logic syntax.

## Limitations

This is a theorem about a specific quantifier-free disjunction and finite Cartesian-product teams. It does not classify arbitrary disjunctions or give an efficient formula for structurally constrained input teams. The count treats teams as labeled sets of tuples and does not quotient by value permutations. Historical priority of the resulting polynomial outside the dependence-logic vocabulary remains a possible risk; the proof supplies the formula independently. All polynomial and probability identities are mathematical conclusions, not claims of external formal or independent verification.

## References

1. N. Fröhlich, P. G. Kolaitis, A. Meier, *Disjunctions of Two Dependence Atoms*, arXiv:2508.16146v1 (22 August 2025), https://arxiv.org/abs/2508.16146 ; published in *CSL 2026*, https://doi.org/10.4230/LIPIcs.CSL.2026.10. Relevant material: team-semantics definitions, Theorem 22, Theorem 26 and their proofs.
2. A. Meier, C. Reinbold, *Enumeration Complexity of Poor Man's Propositional Dependence Logic*, arXiv:1704.03292 (2017), https://arxiv.org/abs/1704.03292. Related algorithmic-enumeration setting; not used as an exact counting formula.
