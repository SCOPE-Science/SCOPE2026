# Rank-rounded optimization and sharp efficiency boundaries in continuous-type Schelling bicliques

## Finding

**Theorem (complete-bipartite average-distance swap games).** Let \(a,b\geq1\), \(n=a+b\), and let \(n\) individually labeled agents have arbitrary real types \(t_i\in[0,1]\). Each vertex of the complete bipartite graph \(K_{a,b}\) is occupied. An agent pays the mean absolute type difference to all neighbors. A location swap is permitted only if *both* swapping agents strictly reduce their own costs.

For an assignment, write \(A\) and \(B\) for the agents in the two vertex classes, and define
\[
 W(A,B)=\frac{1}{a}\sum_{\{i,j\}\subseteq A}|t_i-t_j|+\frac{1}{b}\sum_{\{i,j\}\subseteq B}|t_i-t_j|.
\]
Then for every swap of \(x\in A\) with \(y\in B\),
\[
W(A',B')-W(A,B)=\bigl(c_x(A,B)-c_x(A',B')\bigr)+\bigl(c_y(A,B)-c_y(A',B')\bigr).
\]
Consequently every strictly mutually beneficial swap increases \(W\), so **every improvement sequence terminates** even when \(a\ne b\). A maximizing assignment is a swap equilibrium.

Two optimal assignment rules, requiring \(O(n\log n)\) comparisons for sorting and only \(O(n)\) additional operations, are explicit. Sort the types as \(t_{(1)}\leq\cdots\leq t_{(n)}\). For a sequence of prefix counts \(j_k\), place the agent of rank \(k\) in \(A\) precisely when \(j_k-j_{k-1}=1\).

* **Potential-maximizing equilibrium:** use \(j_0=0\) and
\[
 j_k=\left\lfloor\frac{ak}{n}+\frac12\right\rfloor,\qquad 1\leq k\leq n.
\]
* **Globally minimum social cost:** use \(j_0=0\), \(L_k=\max\{0,k-b\}\), \(U_k=\min\{a,k\}\), and
\[
 j_k=\min\!\left\{U_k,\max\!\left\{L_k,\left\lfloor\frac{a-b+2k}{4}+\frac12\right\rfloor\right\}\right\},\qquad1\leq k\leq n.
\]

These are **different objective functions when \(a\ne b\)**: the socially optimal allocation need not be an equilibrium. On \(K_{2,5}\) with types \((0,0,0,0,\tfrac14,\tfrac34,1)\), the minimum sum of all agents' costs is proportional to \(15\), whereas the minimum among swap equilibria is proportional to \(17\). Thus the instance has an exact price of stability \(17/15>1\). The type values are rescaled from \((0,0,0,0,1,3,4)\), which preserves all equilibrium and welfare ratios.

For the star \(K_{1,n-1}\) with \(n\geq2\), a median-type agent at the center is an equilibrium and a social optimum; hence its price of stability is \(1\). For every nonconstant type profile the price of anarchy is at most \(n-1\), and this bound is achieved by one type-\(0\) agent and \(n-1\) type-\(1\) agents, with the unique type-\(0\) agent at the center. (When all costs vanish, the conventional welfare ratio is \(1\).)

## Assumptions and scope

Types are fixed, agents are distinguishable even if types coincide, all vertices are occupied, edges are unweighted, and \(a,b\) are positive. The cost of an agent in \(A\) is \(c_i=\frac1b\sum_{j\in B}|t_i-t_j|\), and in \(B\) is \(c_j=\frac1a\sum_{i\in A}|t_i-t_j|\). Within-class swaps leave both agents' neighborhood type-multisets unchanged and cannot be strictly mutually improving. No claims are made about jump moves, general bipartite graphs, maximum-distance costs, heterogeneous edge weights, arbitrary nonlinear types, or unilateral incentives. An improvement sequence may be exponentially long; only finite termination and an explicitly computed equilibrium are asserted.

Social cost is \(C(A,B)=\sum_i c_i=(\frac1a+\frac1b)\sum_{i\in A,j\in B}|t_i-t_j|\). The comparison-based complexity includes sorting; it is linear after the sorted types are supplied.

## Proof

**1. Exact pair-swap identity.** For \(x\in A\) and \(y\in B\), put \(S_A(z)=\sum_{i\in A\setminus\{x\}}|t_z-t_i|\) and \(S_B(z)=\sum_{j\in B\setminus\{y\}}|t_z-t_j|\). The change in \(W\) is
\[
\Delta W=\frac{S_A(y)-S_A(x)}a+\frac{S_B(x)-S_B(y)}b.
\]
The costs before and after the swap, with \(d=|t_x-t_y|\), are
\[
 c_x^{\rm old}=\frac{S_B(x)+d}b,\quad c_x^{\rm new}=\frac{S_A(x)+d}a,\qquad
 c_y^{\rm old}=\frac{S_A(y)+d}a,\quad c_y^{\rm new}=\frac{S_B(y)+d}b.
\]
Adding their reductions cancels the \(d\)-terms and yields exactly \(\Delta W\). There are at most \(\binom na\) agent-identity assignments to the two parts. Every beneficial swap strictly raises \(W\), so no improving assignment repeats and any sequence contains at most \(\binom na-1\) steps. This argument uses only symmetric dissimilarities for this first part, though the sorted construction uses real absolute differences.

**2. Gap decomposition and maximum \(W\).** Define nonnegative successive gaps \(g_k=t_{(k+1)}-t_{(k)}\) for \(1\leq k<n\). Let \(j_k\) be the number of the first \(k\) ranked agents assigned to \(A\). For each gap, the number of within-\(A\) pairs straddling it is \(j_k(a-j_k)\), and within-\(B\) pairs is \((k-j_k)(b-k+j_k)\). Hence
\[
 W=\sum_{k=1}^{n-1}g_k\left[\frac{j_k(a-j_k)}a+\frac{(k-j_k)(b-k+j_k)}b\right]
  =\sum_{k=1}^{n-1}g_k\left[k-\frac{j_k^2}a-\frac{(k-j_k)^2}b\right].
\]
For each \(k\), the bracket is a strictly concave quadratic in \(j_k\), maximized over integers at the integer nearest \(ak/n\) (either nearest integer is allowed in a tie). With the specified half-up rounding, the sequence starts at \(0\), ends at \(a\), and increments by exactly \(0\) or \(1\), since \(ak/n\) increases by at most \(1\) when \(k\) increases by \(1\). The independently optimal prefix counts are therefore jointly realizable by the rank construction. Since all \(g_k\geq0\), this assignment globally maximizes \(W\); the gain identity makes it a swap equilibrium.

**3. Gap decomposition and global minimum social cost.** Let \(T=\sum_{i<j}|t_i-t_j|\), independent of placement, and \(H=\sum_{\{i,j\}\subseteq A}|t_i-t_j|+\sum_{\{i,j\}\subseteq B}|t_i-t_j|\). The cross-class pair sum is \(T-H\). Therefore minimizing \(C\) is equivalent to maximizing \(H\). Gap counting gives
\[
H=\sum_{k=1}^{n-1}g_k\left[j_k(a-j_k)+(k-j_k)(b-k+j_k)\right]
 =\sum_{k=1}^{n-1}g_k\left[-2j_k^2+(a-b+2k)j_k+bk-k^2\right].
\]
At prefix \(k\), the feasible integer interval is \([L_k,U_k]\), and the vertex of this concave quadratic is \((a-b+2k)/4\). Its maximizing integer is the displayed nearest-integer-and-clamp rule. As \(k\) increases by \(1\), its un-clamped rounded value increases by \(0\) or \(1\), while both bounds \(L_k,U_k\) are nondecreasing and each increases by at most \(1\). Clamping preserves these properties. The resulting prefix-count path begins at \(0\), ends at \(a\), and has increments in \(\{0,1\}\). Every individual gap is therefore optimized simultaneously, giving a globally minimum social cost. Sorting and scanning take the claimed time. Ties in types make some gaps zero but do not affect the proof.

**4. Exact strict-efficiency separation.** Rescale the seven types to the integer list \((0,0,0,0,1,3,4)\) while comparing ratios. Assigning two agents to \(A\) gives seven possible unordered type-pair classes. For \(A\) of types \((0,0),(0,1),(0,3),(0,4),(1,3),(1,4),(3,4)\), the cross-class pair sums are respectively \(16,15,17,20,20,23,33\). Of these, the swap equilibria are exactly the three classes \((0,3),(0,4),(1,4)\). For each non-equilibrium class one can explicitly improve both agents by exchanging types respectively \((0,3),(1,3),(3,0),(3,0)\); all resulting individual cost reductions are strictly positive (see standalone exact verifier). Thus the minimum cross-class sum overall is \(15\), whereas the minimum across equilibria is \(17\). Since \(C=\frac7{10}\) times that sum, the cost ratio is \(17/15\). Multiplying types by \(1/4\) ensures the stated \([0,1]\) domain without changing the ratio, profitable swaps, or equilibrium classifications.

**5. Star extremal law.** For a center agent \(x\), define \(S(x)=\sum_{i\ne x}|t_x-t_i|\). The total social cost equals \(\frac n{n-1}S(x)\). Choosing a median \(m\) minimizes \(S\) over the agent types, so it minimizes social cost; as it maximizes the within-leaf sum \(W\), it is also an equilibrium. By the triangle inequality, for any possible center \(x\),
\[
 S(x)\leq S(m)+(n-2)|t_x-t_m|\leq(n-1)S(m).
\]
The second inequality follows because \(|t_x-t_m|\) is one term of \(S(m)\). The factor \(n-1\) is sharp: one \(0\) and \(n-1\) ones yield \(S(0)=n-1\), \(S(1)=1\). The center \(0\) cannot participate in a mutually improving swap because its cost after moving to a leaf equals its former cost, so the profile is an equilibrium.

## Verification

Execute `python check_biclique.py` with Python 3 (standard library only). The code exhaustively checks all nondecreasing length-\(2\)-through-\(8\) type lists from \(\{0,1,2,3\}\), every nontrivial part size, every class allocation, and every possible cross-class swap. It separately checks the two rounded constructions against exhaustive global optima and checks the seven-agent efficiency witness. The executed suite checked \(2674\) type/part-size families, \(64548\) partitions, \(803860\) pair swaps, \(2674\) equilibrium constructions, \(2674\) social-optimum constructions, and \(48\) sharp star examples. These finite checks are evidence of implementation consistency, not proofs for all type values or sizes; the algebra and gap arguments above supply the general proof.

## Relationship to prior work

Bilò, Bilò, Döring, Lenzner, Molitor and Schmidt (2023), *Schelling Games with Continuous Types*, introduces the exact continuous-type S-ADG swap model analyzed here. Its Proposition 3 (including the appendix proof) establishes finite improvement on regular graphs by an edge-distance potential, and Theorem 17 establishes price of stability \(1\) for regular graphs. These do not imply finite improvement on irregular \(K_{a,b}\), two explicit prefix-rounded optimal allocation schemes, or the strict price-of-stability gap on \(K_{2,5}\). The present claims are limited to complete bipartite graphs, not arbitrary irregular networks. Earlier two-type Schelling games and the 2024 paper on hardness and robustness use binary same-type-fraction preferences, so their stability or efficiency results do not directly imply this continuous distance theorem. Related finite-dimensional partition optimization methods might yield an equivalent characterization under different language; publication priority remains subject to independent checking.

## Limitations

The potential is an **exact identity for the sum of the two swapping agents' cost reductions**, and therefore an ordinal potential for mutually improving swaps. It is not claimed to be an exact potential for arbitrary unilateral deviations. The globally optimal social-cost construction need not itself be stable; the \(K_{2,5}\) witness proves that an optimal equilibrium may not exist. The star price-of-anarchy ratio is defined for positive optimal costs, with all-zero instances treated separately. No claim is made about minimal worst-case witness size or about convergence in polynomially many beneficial swaps. The originality comparison is a bounded literature check, not a certificate of global priority. There has been no independent mathematical audit.

## References

1. Davide Bilò, Vittorio Bilò, Michelle Döring, Pascal Lenzner, Louise Molitor, and Jonas Schmidt. *Schelling Games with Continuous Types*. IJCAI 2023, pp. 2520–2527, DOI: https://doi.org/10.24963/ijcai.2023/280. First publicly posted 2023-05-11: https://arxiv.org/abs/2305.06819 ; complete preprint: https://arxiv.org/pdf/2305.06819.
2. Luca Kreisel, Niclas Boehmer, Vincent Froese, and Rolf Niedermeier. *Equilibria in Schelling Games: Computational Hardness and Robustness*. Autonomous Agents and Multi-Agent Systems 38, 9 (2024). https://doi.org/10.1007/s10458-023-09632-7.
3. *Schelling games on graphs*. Artificial Intelligence 301 (2021), article 103576. https://doi.org/10.1016/j.artint.2021.103576.
