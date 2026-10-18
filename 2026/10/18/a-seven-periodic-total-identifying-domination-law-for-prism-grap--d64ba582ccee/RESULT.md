# A seven-periodic total-identifying domination law for prism graphs

## Finding
For every integer \(n\geq4\), let \(Y_n=C_n\square K_2\). Its minimum total dominating identifying-code size satisfies
\[
\gamma_t^{\mathrm{ID}}(Y_n)=6\left\lfloor\frac n7\right\rfloor+f(n\bmod7),
\qquad (f(0),\ldots,f(6))=(0,2,3,3,4,5,6).
\]
The exceptional triangular prism has \(\gamma_t^{\mathrm{ID}}(Y_3)=4\). The limiting ratio to the number of prism columns is \(6/7\), and to the number of vertices is \(3/7\).

## Assumptions and scope
Here \(n\geq3\) is an integer, all graphs are finite, undirected, and simple, and the vertices of \(Y_n\) are \((i,a)\) with \(i\in\mathbb Z/n\mathbb Z\) and \(a\in\{0,1\}\). The open neighborhood \(N(i,a)\) consists of \((i-1,a),(i+1,a),(i,1-a)\); the closed neighborhood is \(N[i,a]=N(i,a)\cup\{(i,a)\}\). A total dominating identifying code is a set \(C\) for which \(N(v)\cap C\ne\varnothing\) for every vertex \(v\), and \(N[u]\cap C\ne N[v]\cap C\) for every pair of distinct vertices \(u,v\). We minimize \(|C|\) over such sets. The two conditions must both hold; ordinary locating-total domination only compares vertices outside \(C\) and is not the same invariant.

## Proof
**Local equivalence.** Associate to each column \(i\) a symbol \(c_i\in\{0,1,2,3\}\) whose two binary digits say which of its two vertices are in \(C\). For a five-column word \(w=(c_0,c_1,c_2,c_3,c_4)\), let \(M(w)\) be its selected vertices within columns zero through four. Use the unwrapped neighborhoods \(\mathcal N(j,a)=\{(j-1,a),(j+1,a),(j,1-a)\}\), with \(\mathcal N[j,a]=\mathcal N(j,a)\cup\{(j,a)\}\). Call \(w\) admissible if both following requirements hold:

1. \(M(w)\cap\mathcal N(2,a)\ne\varnothing\) for each \(a\in\{0,1\}\).
2. For each \(a,b\in\{0,1\}\) and \(j\in\{1,2,3\}\), whenever \(j\ne1\) or \(b>a\), the intersection \(M(w)\cap(\mathcal N[1,a]\triangle\mathcal N[j,b])\) is nonempty.

For \(n\geq7\), a cyclic column word encodes a total dominating identifying code **if and only if** each cyclic window of five columns is admissible. The first requirement checks total domination at each column. In the second, every unordered distinct vertex pair whose column distance along the shorter circular arc is at most two is tested by a window whose second column is the first member's column (same-column pairs are tested once). Every remaining pair has cyclic column distance at least three. Its two closed neighborhoods are disjoint, so total domination guarantees that their (nonempty) intersections with \(C\) differ. This proves both implications, not merely necessity.

**Finite-state reduction.** Take the \(4^4=256\) four-symbol states. For every admissible five-symbol word \((a,b,c,d,e)\), introduce the transition \((a,b,c,d)\to(b,c,d,e)\) of weight equal to the number of set binary digits of \(e\). The preceding equivalence and cyclic consistency show that an admissible length-\(n\) cyclic word corresponds to a length-\(n\) closed walk, with the same total weight, whenever \(n\geq7\). The graph has exactly 661 directed transitions. Direct strongly connected component enumeration shows that all its directed cycles lie in a single strongly connected component containing exactly 147 states and 489 internal transitions; the remaining components are acyclic singletons. Consequently no minimum code is lost by restricting to this component.

**Exact min-plus certificate.** Let \(T\) be the \(147\times147\) weighted adjacency matrix of the cyclic component over the min-plus semiring. Write \(D_k=T^{\otimes k}\); a nonexistent path has entry \(+\infty\). Then for every \(n\geq7\),
\[\gamma_t^{\mathrm{ID}}(Y_n)=\min_i(D_n)_{ii}.\]
The standalone program `verify.py`, consisting only of enumerations and integer arithmetic, reconstructs the admissible transitions and computes the finite matrices. It checks the *entrywise* identity
\[ D_{16}=D_9+6\mathbf1, \]
for all 21,609 entries, which are finite, and independently computes
\[(\min_i(D_k)_{ii})_{k=7}^{13}=(6,8,9,9,10,11,12).\]
The matrix identity is an exact finite computation, **not** an extrapolation from finitely many code minima. For every \(k\geq9\), min-plus matrix associativity gives
\[ D_{k+7}=D_{16}\otimes D_{k-9}=(D_9+6\mathbf1)\otimes D_{k-9}=D_k+6\mathbf1.\]
Thus the minimum closed-walk weight increases by six whenever the length increases by seven, for all lengths at least nine. Direct matrix calculations give the same increment from seven to fourteen and eight to fifteen. The seven initial values above therefore prove the displayed formula for every \(n\geq7\).

**Short cyclic orders.** When \(3\leq n\leq6\), the five-column local correspondence is not used. Instead, a separate direct exhaustive enumerator tests every vertex subset against all nonempty open-neighborhood constraints and all pairwise closed-neighborhood symmetric-difference constraints. It obtains respective minimum sizes \(4,4,5,6\), with 9, 30, 32, and 110 minimum codes. These values prove the exceptional case and complete the formula for orders four through six.

## Verification
Run `python3 verify.py` using the Python standard library. It reconstructs all 256 states and 661 transitions; finds the unique cyclic 147-state component; calculates and compares the full ninth and sixteenth min-plus powers; checks traces through length 23; exhaustively tests all subsets for orders three through eight; and, for orders seven and eight, checks the equivalence of the cyclic local rule to the direct global definition on **all** 16,384 and 65,536 possible column words. It also reconstructs optimal cyclic witnesses in several residue classes and independently tests them against the graph definition. The unmodified run terminates with `VERIFY_OK`. The complete output is supplied as `verification_output.txt`.

Example optimal cyclic words (digits indicate binary selections of the two levels) are `0230031` for seven columns, `30130031` for eight, and `0320130031` for ten. Their weights are respectively six, eight, and nine. The proof of the infinite assertion is the min-plus identity and its induction, not the finite sample tests.

## Relationship to prior work
Foucaud and Lehtilä (first submitted June 19, 2022) define total dominating identifying codes, prove general bounds and extremal results, and provide a recent motivating framework, but their inspected paper gives no exact seven-periodic prism law [1]. Omamalin, Canoy, and Rara give a necessary-and-sufficient Cartesian-product description of differentiating total dominating sets (the same invariant), plus a general upper bound; their Theorem 3.1 and Corollary 3.2 do not evaluate the prism optimum [2]. Raza, Iqbal, Khan, and Botmart study the weaker **locating-total** domination number of the prism and a distinct five-column construction [3]. Their exhibited size \(4n/5\) for every positive multiple of five shows that at orders divisible by 35, the separation between this weaker invariant and the present exact total-identifying invariant is at least \(2n/35\). These are different optimization requirements, not conflicting numerical formulas.

## Limitations
The claim concerns the exact minimum size, **not** a classification or full enumerator of every minimum code at general order. Its infinite proof relies on a finite exact min-plus identity whose reproducible verifier is supplied, rather than a shorter hand-derived packing inequality. The finite subset checks alone would not establish the infinite formula. Unindexed historical results under the alternative name *differentiating-total domination*, or another language, remain a residual originality risk. No independent audit of this result is claimed.

## References
[1] F. Foucaud and T. Lehtilä, *Bounds and extremal graphs for total dominating identifying codes*, arXiv:2206.09481 (first posted 2022-06-19), Electronic Journal of Combinatorics 30(3), P3.15 (2023). https://arxiv.org/abs/2206.09481 ; https://doi.org/10.37236/11342.

[2] B. N. Omamalin, S. R. Canoy Jr., and H. M. Rara, *Differentiating total domination in graphs: revisited*, International Journal of Mathematical Analysis 8 (2014), 2789–2798, https://doi.org/10.12988/ijma.2014.410307.

[3] H. Raza, N. Iqbal, H. Khan, and T. Botmart, *Computing locating-total domination number in some rotationally symmetric graphs*, Science Progress (2021), first online 2021-11-17, https://doi.org/10.1177/00368504211053417.
