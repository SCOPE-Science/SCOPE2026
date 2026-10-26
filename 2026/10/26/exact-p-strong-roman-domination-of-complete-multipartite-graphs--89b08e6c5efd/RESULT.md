# Exact \(p\)-strong Roman domination of complete multipartite graphs: a two-defender residue correction

## Finding
Let \(G=K_{a_1,\ldots,a_r}\) be a complete multipartite graph with \(r\ge3\) nonempty parts, \(N=\sum_{i=1}^r a_i\), \(m=\min_i a_i\), and let \(p\) be an integer satisfying \(3\le p\le N-m-1\). Define for every pair of distinct parts
\[
X_{ij}=N-a_i-1,\qquad Y_{ij}=N-a_j-1,\qquad
\varepsilon_{ij}=\begin{cases}
1,&X_{ij}\equiv Y_{ij}\equiv1\pmod p,\\
0,&\text{otherwise}.
\end{cases}
\]
Then the \(p\)-strong Roman domination number is
\[
\boxed{\displaystyle
\gamma^p_{\mathrm{StR}}(G)=
\min\left\{
 m+\left\lceil\frac{N-m}{p}\right\rceil,
 \min_{1\le i<j\le r}\left(2+\left\lceil\frac{X_{ij}}p\right\rceil+
 \left\lceil\frac{Y_{ij}}p\right\rceil-\varepsilon_{ij}\right)
\right\}.}
\]
In particular, the invariant can be calculated from the part sizes in \(O(r^2)\) arithmetic operations. Each term is attained by an explicit labeling. The one-unit correction is genuine: for \(G=K_{5,5,5}\) and \(p=4\), the result is \(7\), whereas the best one-defender labeling and every uncorrected two-defender labeling have weight \(8\).

For balanced tripartite graphs, whenever \(3\le p\le2s-1\),
\[
\gamma^p_{\mathrm{StR}}(K_{s,s,s})=\min\left\{
 s+\left\lceil\frac{2s}{p}\right\rceil,
 2+2\left\lceil\frac{2s-1}{p}\right\rceil-
 \mathbf1_{\,2s-1\equiv1\ (\mathrm{mod}\ p)}\right\}.
\]
For every fixed \(p\ge3\), this equals \(4s/p+O(1)\) as \(s\to\infty\). Thus the improvement over the standard one-defender construction grows linearly with \(s\).

## Assumptions and scope
A \(p\)-strong Roman dominating function on a finite simple graph of maximum degree \(\Delta\) is a map
\[
f:V(G)\longrightarrow \{0,1,\ldots,1+\lceil\Delta/p\rceil\}
\]
such that every zero-labeled vertex has a neighbor \(u\) satisfying
\[
f(u)\ge1+\left\lceil\frac{|N(u)\cap B_0|}{p}\right\rceil,
\qquad B_0=\{v\in V(G):f(v)=0\}.
\]
The weight is \(\sum_{v\in V(G)}f(v)\), and \(\gamma^p_{\mathrm{StR}}(G)\) is its minimum over feasible functions. We use exactly the defender-capacity convention of Valenzuela-Tripodoro and coauthors. The stipulated range \(3\le p\le\Delta-1\), with \(\Delta=N-m\), isolates the nontrivial generalized case. The argument works for \(p=2\) as well, but that specialization is not presented as new.

## Proof
Write the partite sets as \(A_i\), with \(|A_i|=a_i\). For any feasible function write \(z_i=|B_0\cap A_i|\) and \(Z=\sum_i z_i\). A positive vertex in \(A_i\) has exactly \(Z-z_i\) zero-labeled neighbors. An *effective defender* is a positive vertex \(u\in A_i\) with \(Z-z_i>0\) and
\[
f(u)\ge1+\left\lceil\frac{Z-z_i}{p}\right\rceil.
\]
Every zero has an effective defender in a different part.

**Reduction to at most two effective defenders.** If there is just one effective-defender part, it must be zero-free. One effective defender there covers every zero. If there are at least two distinct effective-defender parts \(A_i,A_j\), choose one effective defender in each. Every zero lies outside at least one of these two parts, so those two vertices alone cover every zero. All other positive vertices can be downgraded to label \(1\), without changing the zero set or invalidating coverage. This transformation does not increase weight. Hence some optimum uses a single defender in a zero-free part or at most two defenders in distinct parts.

**One-defender case.** Suppose the effective defender lies in \(A_i\) and \(z_i=0\). All \(a_i\) vertices of this part must be positive. Replace any positive vertex outside \(A_i\) by a zero, increasing the chosen defender's label if necessary. Each replacement saves at least one unit and increases the required defender excess by at most one unit, so never increases total weight. At the end the chosen vertex has label \(1+\lceil(N-a_i)/p\rceil\), the other \(a_i-1\) vertices of its part have label \(1\), and all remaining vertices have label \(0\). Thus its minimum weight is
\[
a_i+\left\lceil\frac{N-a_i}{p}\right\rceil.
\]
This expression is nondecreasing in \(a_i\) for integral \(p\ge2\), since raising \(a_i\) by one changes the expression by zero or one. The best value is therefore \(m+\lceil(N-m)/p\rceil\), attained by a smallest part.

**Two-defender case.** Choose effective defenders \(u\in A_i\), \(v\in A_j\) with \(i\ne j\), and retain only them as vertices of label at least two. Every other positive vertex of \(A_i\) may be changed to zero: this costs one less unit but can increase the defender requirement at \(v\) by at most one; the defender requirement at \(u\) is unaffected. The same holds with \(i,j\) interchanged. Repeating leaves exactly \(u\) and \(v\) positive in their respective parts. Any remaining positive vertices, all outside \(A_i\cup A_j\), may be assigned label \(1\). Denote their number by \(t\), so
\[
0\le t\le N-a_i-a_j.
\]
There are \(N-2-t\) zeros. The zero neighbors of \(u\) number \(X_{ij}-t\), and those of \(v\) number \(Y_{ij}-t\). The minimum weight for that configuration is exactly
\[
F_{ij}(t)=2+t+\left\lceil\frac{X_{ij}-t}{p}\right\rceil+
\left\lceil\frac{Y_{ij}-t}{p}\right\rceil.
\]
Conversely, the function just described with each defender assigned the displayed threshold is feasible: every zero lies outside at least one defender's part. Thus minimizing \(F_{ij}\) gives the true two-defender optimum for that pair.

Write \(t=qp+s\), with \(0\le s<p\). The ceiling identity gives
\[
F_{ij}(t)=F_{ij}(s)+q(p-2).
\]
Since \(p\ge3\), discarding full groups of \(p\) unit-labeled vertices never worsens the weight. For \(0\le s<p\), each ceiling can fall by at most one relative to its value at \(s=0\). Therefore \(F_{ij}(s)\ge F_{ij}(0)\) for \(s\ge2\). At \(s=1\), a decrease by one occurs exactly when both \(X_{ij}\) and \(Y_{ij}\) are congruent to \(1\) modulo \(p\); otherwise the value is not smaller than at zero. Because \(r\ge3\), the complement of \(A_i\cup A_j\) contains a vertex, and \(t=1\) is always admissible. Consequently
\[
\min_{0\le t\le N-a_i-a_j}F_{ij}(t)
=2+\left\lceil\frac{X_{ij}}p\right\rceil+
\left\lceil\frac{Y_{ij}}p\right\rceil-\varepsilon_{ij}.
\]

Taking the minimum over all pairs and the one-defender term proves the theorem. Its constructions show equality throughout. For \(K_{5,5,5}\), \(p=4\), choose one vertex in each of two parts and label both by \(3\), choose one vertex in the third part and label it \(1\), and label the remaining twelve vertices \(0\). Each defended zero has a suitable neighbor, and the weight is \(7\). The formula proves that no smaller weight is feasible.

## Verification
Run `python3 verify.py` using the accompanying standalone, standard-library-only program. The verifier compares the formula with (i) an exact zero-profile search considering **all subsets of possible defender parts**, rather than assuming two suffice, and (ii) direct enumeration of every named labeling on small instances. It tested 844 zero-profile instances, 90 independently enumerated labeled instances, and four separately selected congruence examples. Its recorded output is in `verify_output.txt`. Both algorithms compute feasibility directly from the defined neighbor-zero threshold; they do not use the algebraic proof or the stated two-defender reduction as an oracle.

## Relationship to prior work
Valenzuela-Tripodoro et al. introduced \(p\)-strong Roman domination and determined exact values for complete bipartite graphs (Proposition 15), as well as general graph bounds. Their explicit future directions include other graph families. Those bipartite cases do not cover the present \(r\ge3\) problem, where a third part creates a genuine one-unit congruence improvement. Their general one-defender bound is attained by one term of the new formula but can be strictly larger than the new optimum, as for \(K_{5,5,5}\) at \(p=4\).

The published result *Strong Roman domination of complete multipartite graphs with at least three parts* gives the ordinary strong Roman parameter, equivalent to \(p=2\), with value \(\lceil(N+m)/2\rceil\). That result does not determine the \(p\ge3\) values or the residue-sensitive transition. The published note *Exact total strong Roman domination of complete multipartite graphs* imposes the different condition that the positive-label support have no isolated vertex, and treats the ordinary strong Roman capacity \(p=2\). Its binary parity correction is a useful analogue but neither its hypothesis nor its formula implies the present general \(p\)-strong result. Nikolić et al.'s \(k\)-strong Roman domination is a different simultaneous-attack model, not the neighbor-zero ceiling-capacity model used here.

## Limitations
This theorem applies to complete multipartite graphs with at least three nonempty parts and \(3\le p\le\Delta-1\). It does not determine the complete set or count of all minimum labelings: it establishes that an optimum has one of the canonical displayed forms. The case of two parts was studied in the original \(p\)-strong Roman paper. The computational experiments are finite checks; the unrestricted theorem is supplied by the preceding proof. No assertion of uniqueness in all unindexed literature is made.

## References
1. J. C. Valenzuela-Tripodoro, M. A. Mateos-Camacho, M. Cera, R. M. Casablanca, and M. P. Álvarez-Ruiz, *p-Strong Roman Domination in Graphs*, WSEAS Transactions on Mathematics 23 (2024), 1005–1017, DOI:10.37394/23206.2024.23.104; arXiv:2501.10140 (public preprint 2025-01-17). The university repository records the paper date as 2024-12-17.
2. *Strong Roman domination of complete multipartite graphs with at least three parts*, published published-finding corpus record `2026/10/4/SCOPE-strong-roman-domination-of-complete-multipartite-graphs-with-at--28025f4386ef`, `RESULT.md`.
3. *Exact total strong Roman domination of complete multipartite graphs*, published published-finding corpus record `2026/9/30/SCOPE-exact-total-strong-roman-domination-of-complete-multipartite-gra--f1a2cc307443`, `RESULT.md`.
4. B. Nikolić, M. Djukanović, M. Grbić, and D. Matić, *Theoretical studies of the k-strong Roman domination problem*, Kuwait Journal of Science 51 (2024), 100283, DOI:10.1016/j.kjs.2024.100283.
