# Quadratic adjacent-swap detours among \(132\)-avoiding permutations

## Finding
For each integer \(n\ge 2\), let \(G_n\) be the induced subgraph of the adjacent-transposition permutohedron on the permutations of \([n]\) that avoid the classical pattern \(132\). The graph \(G_n\) is connected and has exactly
\[
|V(G_n)|=\frac{1}{n+1}\binom{2n}{n},\qquad |E(G_n)|=\binom{2n-2}{n-2}.
\]
If \(e_n=(1,2,\ldots,n)\) and \(r_n=(n,1,2,\ldots,n-1)\), then their **exact graph distance** is
\[
d_{G_n}(e_n,r_n)=(n-1)^2.
\]
Their distance in the unrestricted permutohedron is \(n-1\). Hence the intrinsic-to-ambient distance ratio for this explicit pair is \(n-1\) and is unbounded. The theorem does **not** assert that \((n-1)^2\) is the diameter of \(G_n\).

## Assumptions and scope
A permutation \(p=(p_1,\ldots,p_n)\) avoids \(132\) when no indices \(i<j<k\) satisfy \(p_i<p_k<p_j\). A legal move exchanges the entries at two consecutive positions only when both permutations avoid \(132\). Graph distance counts such moves, and each unordered adjacent pair of distinct permutations constitutes one graph edge. This result concerns all integers \(n\ge2\), with fixed distinct labels \(1,\ldots,n\), and uses ordinary, not consecutive, pattern avoidance.

## Proof
**Local swap criterion.** Let \(p\) avoid \(132\), and consider consecutive entries \(x=p_i\) and \(y=p_{i+1}\). If \(x<y\), swapping them preserves avoidance exactly when no entry before position \(i\) is smaller than \(x\). If \(x>y\), swapping them preserves avoidance exactly when no entry after position \(i+1\) lies strictly between \(y\) and \(x\). Indeed, a newly created forbidden triple must contain both exchanged entries, since all other pairwise relative orders are unchanged. In the first case its form is \((z,y,x)\) with \(z<x<y\) to the left; in the second it is \((y,x,z)\) with \(y<z<x\) to the right. This proves both necessity and sufficiency.

**Connectedness.** In any word other than \((n,n-1,\ldots,1)\), take the leftmost adjacent ascent \(x<y\). Everything preceding \(x\) is in decreasing order, so \(x\) is the minimum of its prefix. The local criterion permits that ascent-to-descent swap. It increases inversion number by exactly one. After exactly \(\binom n2-\operatorname{inv}(p)\) such steps the reverse permutation is reached, proving every vertex lies in its component.

**Lower bound on the specified distance.** Consider any legal path from \(e_n\) to \(r_n\). For every \(b<n\), the symbol \(n\) must at least once cross \(b\) from right to left, using a legal ascending pair \((b,n)\). At that instant the local criterion requires every smaller symbol \(a<b\) to appear after \(b\). But \(a\) precedes \(b\) in both the initial and final words. Therefore the pair of symbols \((a,b)\) must have exchanged relative order at least twice during the path. This holds for all \(\binom{n-1}{2}\) pairs among the first \(n-1\) symbols. Separately, \(n\) must cross each of those \(n-1\) symbols at least once. As one adjacent swap changes the relative order of exactly one pair of symbols, the path has length at least
\[
2\binom{n-1}{2}+(n-1)=(n-1)^2.
\]

**Attaining path.** Start from \(e_n\), repeatedly swap the first adjacent ascent, and arrive at the reverse word \((n,n-1,\ldots,1)\) in precisely \(\binom n2\) legal swaps. Keep the first \(n\) fixed and sort its descending suffix by the following procedure: move the largest remaining suffix entry rightward across every smaller remaining entry, then repeat on the shorter descending initial segment. Each swap is a descent-to-ascent swap \((x,y)\mapsto(y,x)\), and all entries to its right are either smaller than \(y\) in the as-yet-unsorted decreasing segment or larger than \(x\) in the already sorted final segment. The local criterion makes every swap legal. Exactly \(\binom{n-1}{2}\) swaps sort the suffix. The resulting word is \(r_n\). This path has length \(\binom n2+\binom{n-1}{2}=(n-1)^2\), matching the lower bound.

**Exact edge enumeration.** Let \(C_m\) denote the number of \(132\)-avoiders of length \(m\), including \(C_0=1\), and let \(E_m=|E(G_m)|\), with \(E_0=E_1=0\). Decompose each avoider uniquely around its maximum as \(L\,n\,R\), where every entry of \(L\) is larger than every entry of \(R\). Writing \(|L|=a\) and \(|R|=b\), we have \(a+b=n-1\), and the standardized left and right words are independent avoiders. The legal ascending swaps internal to either block give
\[
2\sum_{a+b=n-1}E_aC_b
\]
when summed over all block sizes. The only further possible ascending swap occurs immediately before \(n\). It is legal precisely if the last entry of \(L\) is its minimum. For each \(a\ge1\), there are exactly \(C_{a-1}\) such left blocks (delete the final minimum); summing over \(a+b=n-1\) contributes \(C_{n-1}\) by the Catalan convolution. Thus, for \(n\ge2\),
\[
E_n=2\sum_{a+b=n-1}E_aC_b+C_{n-1}.
\]
The maximum-element decomposition also gives \(C(z)=1+zC(z)^2\), hence \(C(z)=(1-\sqrt{1-4z})/(2z)\). The edge generating function \(E(z)=\sum_{n\ge0}E_nz^n\) satisfies
\[
E(z)=2zC(z)E(z)+z(C(z)-1)
=\frac{1-2z}{2\sqrt{1-4z}}-\frac12.
\]
Coefficient extraction for \(n\ge2\) gives
\[
E_n=\frac12\binom{2n}{n}-\binom{2n-2}{n-1}
=\binom{2n-2}{n-2}.
\]
The Catalan formula for \(C_n\) follows from the same generating function. All arguments are finite or algebraic identities valid for every indicated integer.

## Verification
The accompanying `verify.py` recursively generates all \(132\)-avoiders by the maximum-element decomposition, independently compares them to a three-index brute-force pattern predicate for \(2\le n\le7\), reconstructs all legal adjacent swaps, independently checks the local move criterion for \(2\le n\le7\), and breadth-first-searches from \(e_n\) for every \(2\le n\le10\). It checks the Catalan vertex count, the edge formula, connectedness, and the canonical distance on the resulting full graphs. The largest checked instance has \(16{,}796\) vertices, \(43{,}758\) edges, and canonical distance \(81\). Run `python3 verify.py` with a standard Python 3 interpreter. These finite checks support but do not replace the all-parameter proof above.

## Relationship to prior work
Reifegerste's 2002 paper characterizes \(132\)-avoiding permutation diagrams and relates them to Dyck paths; its Catalan count is standard. Aisbett's 2015 paper studies pattern popularity under a different operation, relocating an entry over a possibly nonempty block, rather than this graph's single adjacent-position exchange. Linusson, Potka, and Sulzgruber study the monotone reduced-word paths from identity to the reverse permutation that remain \(132\)-avoiding; such paths are used in the upper-bound construction but do not give the lower bound for the different endpoint \(r_n\). The graph of overlapping \(312\)-avoiding permutations studied by Ehrenborg, Kitaev, and Steingrímsson uses standardized prefix/suffix shifts and not adjacent transpositions. None of those inspected statements supplies the claimed exact restricted distance. The local geometry is not determined by Catalan equinumerosity with the class avoiding \(321\): pattern avoidance is not preserved by a generic vertex bijection with respect to adjacent-swap edges.

## Limitations
No formula for arbitrary-pair distances or for the full diameter of \(G_n\) is proved. Computational checking stops at \(n=10\). Literature checks can miss unpublished or unindexed equivalent results, and no independent mathematical audit has been performed. The size and the connectedness conclusions are parts of the same all-parameter theorem, not evidence for any unproved diameter assertion.

## References
1. Astrid Reifegerste, *On the diagram of 132-avoiding permutations*, arXiv:math/0208006 (first version posted 2002-08-01), especially Sections 1–3, https://arxiv.org/html/math/0208006v3 .
2. Natalie Aisbett, *A relation on 132-avoiding permutation patterns*, Discrete Mathematics and Theoretical Computer Science (2015), Sections 3–4, https://dmtcs.episciences.org/2141/pdf .
3. Svante Linusson, Samu Potka, Robin Sulzgruber, *On random shifted standard Young tableaux and 132-avoiding sorting networks*, arXiv:1804.01795 (2018), especially Section 1, https://arxiv.org/pdf/1804.01795 .
4. Richard Ehrenborg, Sergey Kitaev, Einar Steingrímsson, *Number of cycles in the graph of 312-avoiding permutations*, Journal of Combinatorial Theory Series A 129 (2015), 1–18, https://strathprints.strath.ac.uk/53181/ .
