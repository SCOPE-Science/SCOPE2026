# Exact identifying-code numbers for complementary prisms of cycles

## Finding
Let \(P_n\) be the complementary prism of the cycle \(C_n\): its vertices are \(v_i,\bar v_i\) for \(i\in\mathbb Z_n\), with the cycle edges \(v_iv_{i+1}\), the complementary-cycle edges \(\bar v_i\bar v_j\) whenever \(i\ne j\) and \(j\not\equiv i\pm1\pmod n\), and the matching edges \(v_i\bar v_i\). An identifying code is a set \(S\) such that \(N[u]\cap S\) is nonempty for each vertex \(u\) and these intersections are pairwise distinct. Write \(\gamma_{\rm ID}(P_n)\) for its minimum cardinality.

**Theorem.** For every integer \(n\ge9\), writing \(n=9k+r\), \(k\ge1\), \(0\le r<9\),
\[
\gamma_{\rm ID}(P_n)=7k+a_r,\qquad
(a_0,a_1,\ldots,a_8)=(0,1,1,3,3,4,5,6,6).
\]
In particular, the minimum is exactly \(7k\) at every multiple \(n=9k\). The residue-class offsets are exact, not merely asymptotic error terms.

## Assumptions and scope
All graphs are finite, simple, undirected; code neighborhoods are **closed**. Both the cycle and complementary-cycle layers are vertex-labeled by the same cyclic indices. The result is for every \(n\ge9\), without an assumption on parity or primality. Index arithmetic below is modulo \(n\). The value for smaller cycles is not asserted.

Let \(x_i={\bf1}_{v_i\in S}\), \(b_i={\bf1}_{\bar v_i\in S}\), and use a column letter \(c_i=x_i+2b_i\in\{0,1,2,3\}\). A *defect* is an index satisfying \(b_{i-1}+x_i+b_{i+1}=0\).

## Proof
**1. Necessary conditions.** Distinguishing the cycle vertices at distances one and two, distinguishing complementary-layer vertices at distance two, and dominating cycle vertices yields, for every \(i\), the following four local inequalities:
\[
\begin{aligned}
 x_{i-1}+x_i+b_i+x_{i+1}&\ge1,\\
 x_{i-1}+b_i+b_{i+1}+x_{i+2}&\ge1,\\
 x_{i-1}+x_i+b_i+x_{i+2}+b_{i+2}+x_{i+3}&\ge1,\\
 b_{i-1}+x_i+x_{i+2}+b_{i+3}&\ge1.
\end{aligned}
\]
Any two distinct defect positions \(i,j\) would yield two complementary-layer vertices with indistinguishable identifying traces when their cyclic distance is not two; when their distance is two, the fourth local inequality is violated. Thus every identifying code has at most one defect. These conditions also follow from the full-neighborhood characterization in Lemma 2 of Cappelle–Coelho–Coelho–Penso–Rautenbach (2015), including its global complementary-layer distinguishing inequalities.

Conversely, if these four local inequalities hold, there is at most one defect, and \(\sum_i b_i\ge4\), then \(S\) is identifying. Indeed, the first three inequalities ensure domination and separation among cycle-layer vertices. The fourth separates complementary-layer indices two apart. For any other pair of complementary-layer vertices, the symmetric difference of their closed neighborhoods meets \(S\) whenever the sum of their two quantities \(b_{i-1}+x_i+b_{i+1}\) is nonzero; at most one defect guarantees this. Finally, at least four selected complementary-layer vertices make each complementary-layer trace contain at least two complementary-layer symbols, while any cycle-layer trace has at most one, so cross-layer traces are distinct; complementary-layer traces are also nonempty.

**2. An exact finite-state lower-bound certificate valid for all lengths.** Take states to be four consecutive columns \(q=(c_0,c_1,c_2,c_3)\in\{0,1,2,3\}^4\), encoded by \(q=64c_0+16c_1+4c_2+c_3\). There is a directed transition \(q\to q'=(c_1,c_2,c_3,c_4)\) for each appended symbol \(c_4\) if the above four inequalities hold at the middle column \(c_1\) of the five-column window. Assign the transition weight \(w=(c_4\bmod2)+\lfloor c_4/2\rfloor\) and defect indicator \(d={\bf1}_{b_0+x_1+b_2=0}\). This graph has exactly 256 possible states and 857 allowed transitions (counting labeled append operations). A cyclic length-\(n\) column sequence is exactly a closed walk of length \(n\); its total weight equals \(|S|\), and its total defect indicator equals the number of defects.

Expand each state by a defect counter \(e\in\{0,1\}\), forbidding transitions that would increase it beyond one, and a residue \(r\in\mathbb Z_9\) incremented at each transition. This yields 4608 states and 14706 allowed transitions. Give every transition the **integer reduced cost** \(9w-7\). An identifying code gives a path from some \((q,0,0)\) to \((q,e,n\bmod9)\) for \(e\in\{0,1\}\), of reduced cost \(9|S|-7n\).

The complete integer shortest-path certificate in `finite_lower.cpp` uses a potential \(h\) satisfying \(h(v)\le h(u)+9w(u,v)-7\) on all 14706 edges, which proves the absence of a negative reduced-cost cycle. All reweighted arcs are nonnegative, so exhaustive Dijkstra searches from all 256 starting four-column states return the exact unrestricted-length lower costs, by residue,
\[
(\delta_0,\ldots,\delta_8)=(0,2,-5,6,-1,1,3,5,-2).
\]
The program constructs the entire graph, computes and checks the potential inequality on **every arc**, runs the shortest-path searches, and asserts all nine integers; there is no fixed-length enumeration masquerading as a theorem. Consequently
\[
9|S|-7n\ge\delta_r=9a_r-7r,
\]
so \(|S|\ge7k+a_r\) for every length \(n=9k+r\). Negative values of \(\delta_r\) are legitimate; the potential method handles them without assuming nonnegative original reduced costs.

**3. Explicit constructions for every length.** The following table specifies the selected vertices in both layers as two binary column words of equal length \(9+r\). A `1` in the first word selects the corresponding cycle vertex, and a `1` in the second selects the complementary-layer vertex. These are independently checked by complete closed-neighborhood comparisons in `upper_and_direct.cpp`.

| \(r\) | Cycle-layer bits | Complement-layer bits | Weight |
|---:|---|---|---:|
| 0 | `000010101` | `011010001` | 7 |
| 1 | `0001010101` | `1101000001` | 8 |
| 2 | `00001010101` | `01101000001` | 8 |
| 3 | `101000010101` | `001011010001` | 10 |
| 4 | `0100001010101` | `0101101000001` | 10 |
| 5 | `10100001010101` | `00101101000001` | 11 |
| 6 | `010101000010101` | `010001011010001` | 12 |
| 7 | `0100101000010101` | `0100101011010001` | 13 |
| 8 | `01010100001010101` | `01000101101000001` | 13 |

Each word pair describes a closed walk through state 19 of the transition graph; the length-nine word pair \(W\) has **zero defects** and weight seven, and each length-\(9+r\) pair \(W_r\) has at most one defect and weight \(7+a_r\). To construct a code at \(n=9k+r\), concatenate \(k-1\) copies of \(W\) followed by \(W_r\) columnwise. Concatenation of these closed state-19 walks preserves all local inequalities and the at-most-one-defect property. At least four complementary-layer vertices are selected (each copy of \(W\) adds four), so the converse in step 1 applies. The resulting code has weight \(7(k-1)+(7+a_r)=7k+a_r\), matching step 2.

## Verification
Compile `finite_lower.cpp` and `upper_and_direct.cpp` separately with a C++17 compiler, for example `g++ -std=c++17 -O3`. Execute both without input. The first checks 4608 reduced-cost states, all 14706 transition inequalities after potential computation, all relevant shortest paths and the exact nine-entry certificate. The second verifies each base word, all concatenated lengths from nine through 89, and independently enumerates all vertex subsets for lengths nine and ten, obtaining minimum sizes seven and eight, respectively. The source files are the complete computations; output records are included for repeatability. Neither a numerical cutoff nor a search timeout is used in the proof of the infinite-family lower bound.

## Relationship to prior work
Cappelle, Coelho, Coelho, Penso and Rautenbach proved the leading asymptotic coefficient \(7/9\), gave an explicit upper construction of size \(n-2\lfloor n/9\rfloor\), and obtained a lower bound \(7n/9-12\), but their work did not give the exact nine-residue formula. We retain their identifying-code conventions and elementary local necessary-and-sufficient conditions. The contribution here is the exact periodic constant term for all \(n\ge9\), established by finite-state reduced-cost bounds and matching period-nine constructions. Locating-domination in complementary prisms is a different invariant: it requires distinct traces only for vertices outside the chosen set and does not itself provide the exact identifying-code numbers.

## Limitations
The claim concerns only minimum **cardinality** of identifying codes in the cycle complementary prism and only \(n\ge9\). It does not enumerate all minima, assert uniqueness, or extend to other graph families. The finite-state shortest-path certificate is a reproducible computer-assisted finite verification of a nontrivial lemma; an independent external audit of the program and originality has not been performed. As always, unindexed equivalent literature could affect publication priority.

## References
1. M. R. Cappelle, E. M. M. Coelho, H. Coelho, L. D. Penso and D. Rautenbach, *Identifying Codes in the Complementary Prism of Cycles*, arXiv:1507.05083, first posted 2015-07-17; journal version in *Electronic Notes in Theoretical Computer Science* 346 (2019), DOI:10.1016/j.entcs.2019.08.022.
2. *Locating-Domination in Complementary Prisms*, *Journal of Combinatorial Mathematics and Combinatorial Computing* 72 (2010), 163–171 (related but distinct invariant).
