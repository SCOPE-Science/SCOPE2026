# Sharp three-viewpoint diversity for stable extensions of bidirected paths

## Finding

For each integer \(n\ge 4\), let \(F_n\) be the abstract argumentation framework on \(V_n=\{1,\ldots,n\}\) having both attacks \((i,i+1)\) and \((i+1,i)\) for every \(1\le i<n\), and no other attacks. Let \(\mathcal S_n\) be its set of stable extensions. Define the **three-viewpoint maximin diversity**
\[
\delta_3(F_n)=\max_{E_A,E_B,E_C\in\mathcal S_n\ \mathrm{pairwise\ distinct}}\ \min\{|E_A\triangle E_B|,|E_A\triangle E_C|,|E_B\triangle E_C|\}.
\]
Then, exactly,
\[
\boxed{\delta_3(F_n)=\begin{cases}3,&n=6,\\\lfloor 2n/3\rfloor,&n\ge4,\ n\ne6.\end{cases}}
\]
For \(n=1,2,3\), there are fewer than three distinct stable extensions, so this three-extension maximum is not defined. In particular, the unrestricted three-binary-word upper bound is attained by stable extensions on every path order \(n\ge4\) except \(n=6\), where the loss is exactly one.

## Assumptions and scope

The framework is **bidirected**, not a one-way orientation; the endpoints are not adjacent. A stable extension is a conflict-free set attacking every outside vertex. On \(F_n\), these are exactly the maximal independent sets, equivalently the independent dominating sets, of the ordinary undirected path \(P_n\). The distance is the ordinary cardinality of symmetric difference. The optimum ranges over **three pairwise distinct** stable extensions, not over an arbitrary repeated triple. The theorem concerns this fixed graph family, with no claim about arbitrary argumentation frameworks or arbitrary numbers of viewpoints.

## Proof

**1. A universal upper bound.** Associate three chosen subsets \(E_A,E_B,E_C\subseteq V_n\) with the column \(S_i\subseteq\{A,B,C\}\) indicating which subsets contain vertex \(i\). Write \(d_{AB}=|E_A\triangle E_B|\), and likewise for the other pairs. At one vertex the sum of the three pairwise disagreement indicators is exactly \(2\) if \(|S_i|\in\{1,2\}\), and \(0\) if \(|S_i|\in\{0,3\}\). Hence
\[
d_{AB}+d_{AC}+d_{BC}\le 2n,
\qquad \min(d_{AB},d_{AC},d_{BC})\le\lfloor 2n/3\rfloor.
\]
This argument applies to any three binary subsets, and in particular to stable extensions.

**2. Column criterion.** A finite column word \(S_1,\ldots,S_n\) describes three stable extensions of \(F_n\) if and only if, for each label \(L\in\{A,B,C\}\), (i) no consecutive columns both contain \(L\), and (ii) each column not containing \(L\) has an immediately adjacent column containing \(L\). For endpoints there is only one neighbor. Condition (i) is independence and condition (ii) is domination. We abbreviate \(\{A,B\}\) by `AB`, and the empty set by `0`.

**3. Explicit bases.** The following column words each satisfy the criterion; the displayed distances are in the order \((d_{AB},d_{AC},d_{BC})\):

| \(n\) | Column word | Distance triple |
|---:|---|---|
| 4 | `BC,A,C,AB` | \((2,4,2)\) |
| 5 | `BC,A,C,B,AC` | \((4,3,3)\) |
| 6 | `C,AB,C,B,A,BC` | \((3,5,4)\) |
| 7 | `C,AB,0,BC,A,B,AC` | \((4,4,4)\) |
| 8 | `BC,A,C,B,A,C,B,AC` | \((6,5,5)\) |
| 9 | `C,AB,C,B,A,BC,A,B,AC` | \((6,6,6)\) |

The three membership sets are pairwise distinct in every displayed word because every displayed distance is positive. At \(n=4,5,7,8,9\), the smallest distance meets the universal bound.

**4. A three-vertex insertion.** Work at the gap immediately after the fifth column, where that column is `A`. Three local replacements preserve the criterion:

- when the sixth column is `B`, replace `A,B` by `A,B,C,A,B`;
- when the sixth column is `C`, replace `A,C` by `A,C,B,A,C`;
- when the sixth column is `BC` and the fourth column is `B`, replace `A,BC` by `A,C,B,A,BC`.

Each inserted triple consists of the three singleton columns `A`, `B`, `C`, in some order. Its contribution to each pairwise disagreement is therefore exactly \(2\). Every new singleton has the other two labels supplied by its neighbors. The two old boundary columns remain independent and dominated: in the first case, the old `A` has `BC` immediately to its left, and the old `B` retains an immediately preceding `A`; in the second case, the old `A` has `B` to its left and the old `C` still has preceding `A`; in the third case, the old `A` has left neighbor `B` and new right neighbor `C`, while the old `BC` retains preceding `A`. No remaining adjacency or domination requirement changes.

In the \(n=7\) base, the fifth/sixth columns are `A,B` and the fourth is `BC`; use the first replacement. In the \(n=8\) base they are `A,C` with fourth `B`; use the second. In the \(n=9\) base they are `A,BC` with fourth `B`; use the third. The fifth and sixth columns remain of the same form after each insertion, so the same replacement can be repeated indefinitely. Every step increases \(n\) by \(3\) and all three distances by \(2\). The three base families cover all \(n\ge7\). Consequently, they meet \(\lfloor2n/3\rfloor\) for every such \(n\).

**5. The six-vertex exception.** The complete list of maximal independent sets of \(P_6\) is
\[
\begin{aligned}
U_1&=\{2,5\},&U_2&=\{1,3,5\},&U_3&=\{1,3,6\},\\
U_4&=\{1,4,6\},&U_5&=\{2,4,6\}.&&
\end{aligned}
\]
Their symmetric-difference distance matrix (in that order) is
\[
\begin{pmatrix}
0&3&5&5&3\\3&0&2&4&6\\5&2&0&2&4\\5&4&2&0&2\\3&6&4&2&0
\end{pmatrix}.
\]
The graph joining pairs at distance at least \(4\) has precisely the edges \(13,14,24,25,35\), forming a five-cycle with no triangle. Hence no three stable extensions have all three distances at least \(4\). But \(U_1,U_2,U_4\) have distances \(3,5,4\), establishing \(\delta_3(F_6)=3\). The words at \(n=4,5\) complete the remaining cases.

## Verification

The standalone `checker.py` independently enumerates all independent dominating subsets of \(P_n\) and all triples for \(4\le n\le20\), checking the exact optimum including the unique \(n=6\) exception. It also checks the explicit column words and repeatable insertion witnesses for every \(4\le n\le600\) other than \(n=6\). Execute with `python checker.py`; the observed result is `ALL_CHECKS_OK`. The unrestricted theorem for every \(n\) is established by the combinatorial bound, finite six-set analysis and repeatable insertion argument, not by extrapolating this finite computation.

## Relationship to prior work

Fichte, Hecher, Mahmood and Wang (arXiv:2605.13332v1, May 13, 2026) introduce and study symmetric-difference diversity **between two** abstract-argumentation extensions and give complexity results for those tasks. The present objective instead selects **three simultaneously** and maximizes the **least of their three pairwise distances**, a packing-type invariant that is not determined by the maximum distance of one pair.

Classical independent domination identifies stable extensions of a bidirected path with maximal independent sets. The earlier work *Independent Domination in Directed Graphs* (arXiv:1909.05121v1) treats existence, uniqueness and the idomatic number of **disjoint** families, not the optimum minimum Hamming distance of three potentially overlapping sets. Related cyclic pair-distance enumerations concern a different graph family and only two simultaneously chosen extensions. The three-word bound is the elementary binary-coordinate bound; the substantive additional part is its nearly universal realization under path independence **and** domination, together with the exact six-world obstruction.

## Limitations

The result does not classify the number of optimal triples, does not cover more than three simultaneous extensions, and does not yield a general algorithmic complexity classification on arbitrary argumentation frameworks. Searches under maximin Hamming packing, independent dominating sets and diverse stable extensions found no exact prior formula for this path parameter, but absence from these searches is not a proof of priority. A differently named coding-theoretic treatment of independent dominating sets remains a possible source of equivalent prior results.

## References

1. Johannes K. Fichte, Markus Hecher, Yasir Mahmood, Zhengjun Wang, *Diversity of Extensions in Abstract Argumentation*, arXiv:2605.13332v1 (2026-05-13), https://arxiv.org/abs/2605.13332.
2. *Independent Domination in Directed Graphs*, arXiv:1909.05121v1 (2019), https://arxiv.org/abs/1909.05121.
