# Minimal domination spectra of cycle powers and parity-rigid maxima

## Finding

For integers \(r\ge1\) and \(n\ge2r+1\), let \(C_n^r\) have vertex set \(\mathbb Z/n\mathbb Z\), with distinct vertices joined when their cyclic distance is at most \(r\). A set \(S\) is *inclusion-minimal dominating* if its closed neighborhoods cover every vertex but removing any member destroys domination. Let \(M_{n,r}(z)=\sum_{S}z^{|S|}\), summing over all such sets.

Order the \(k\ge1\) selected vertices clockwise, and write \(g_1,\ldots,g_k\) for their positive successive clockwise gaps, with \(\sum_i g_i=n\) and cyclic indices. Then \(S\) is inclusion-minimal dominating if and only if
\[
1\le g_i\le2r+1\quad\text{and}\quad g_i+g_{i+1}\ge2r+2\qquad\text{for every }i.
\]
This includes \(k=1\), using \(g_1=n\).

In particular, for every integer \(k\ge1\),
\[
[z^k]M_{n,r}(z)=\frac nk\left|\left\{(g_1,\ldots,g_k)\in\{1,\ldots,2r+1\}^k:\ \sum_i g_i=n,\ \ g_i+g_{i+1}\ge2r+2\ \forall i\right\}\right|.
\]
Define the \((2r+1)\)-square matrix \(B_r(u)\) indexed by \(1\le a,b\le2r+1\) by
\[
(B_r(u))_{a,b}=u^b\,\mathbf1_{\{a+b\ge2r+2\}}.
\]
Then the complete cardinality-refined minimal-domination enumerator satisfies
\[
M_{n,r}(z)=[u^n]\left[-u\frac{\partial}{\partial u}\log\det(I-zB_r(u))\right]\qquad(n\ge2r+1).
\]
The generating function in brackets is rational in \(u,z\), since its logarithmic derivative is a rational function. For the square-of-a-cycle case \(r=2\), its determinant is
\[
\begin{aligned}
Q_2(u,z)={}&1-z(u^3+u^4+u^5)-z^2(2u^6+u^7)\\
&+z^3(2u^9+2u^{10})+z^4u^{12}-z^5u^{15}.
\end{aligned}
\]
Every nonzero coefficient occurs at every integer degree in the *gap-free* range
\[
\left\lceil\frac{n}{2r+1}\right\rceil\le k\le\left\lfloor\frac{n}{r+1}\right\rfloor.
\]
Thus the lower and upper domination numbers are respectively the endpoints of this interval.

If \(n=k(r+1)\) with \(k\ge2\), the number of maximum-cardinality inclusion-minimal dominating sets depends only on the parity of \(k\):
\[
[z^k]M_{k(r+1),r}(z)=
\begin{cases}
r+1,&k\text{ odd},\\
(r+1)(2r+1),&k\text{ even}.
\end{cases}
\]
For example, \(C_{12}^2\) has exactly fifteen maximum-cardinality inclusion-minimal dominating sets, whereas \(C_9^2\) has exactly three.

## Assumptions and scope

Graphs are finite, simple and undirected. The power parameter \(r\) is a positive integer, and \(n\ge2r+1\); in particular \(C_{2r+1}^r\) is complete. A dominating set is always nonempty here. *Inclusion-minimal* is not synonymous with *minimum cardinality*. No assertion is made about powers of paths or nonuniform circulants.

## Proof

**1. Dominating sets and gaps.** Lift the selected positions periodically to the ordered integers. Between consecutive selected positions at distance \(g\), each unselected position is covered by one of the endpoints' closed \(r\)-neighborhoods exactly when \(g\le2r+1\). Other selected positions lie beyond those endpoints and cannot close an uncovered interval between them. Thus \(S\) dominates exactly when every gap is at most \(2r+1\).

**2. Private closed-neighborhood witnesses.** A dominating set is inclusion-minimal exactly when each chosen vertex \(v\) has a witness in its closed neighborhood not belonging to the closed neighborhood of any other chosen vertex. Translate the chosen vertex to integer position zero, and let the nearest predecessor and successor be at \(-a\) and \(b\), where \(a,b\le2r+1\). A witness position \(t\in[-r,r]\) must satisfy \(t>r-a\) (outside the predecessor's radius) and \(t<b-r\) (outside the successor's radius). More distant periodic chosen vertices cannot reach a point that the nearest predecessor and successor fail to reach. The witness interval therefore is
\[
[-r,r]\cap[r-a+1,b-r-1]\cap\mathbb Z.
\]
Given \(a,b\le2r+1\), it is nonempty exactly when \(a+b\ge2r+2\). Applying this at each chosen vertex proves the claimed necessary-and-sufficient cyclic gap characterization, including the one- and two-selected-vertex cases via the periodic lift.

**3. Exact enumeration and rationality.** Fix a positive integer \(k\). Each labeled set with \(k\) selected vertices has exactly \(k\) choices of distinguished first selected vertex. Conversely, each admissible rooted cyclic gap word and one of the \(n\) vertex positions specifies a selected set. Consequently the coefficient is \(n/k\) times the number of admissible length-\(k\) cyclic words with total gap \(n\). The transfer matrix \(B_r(u)\) records a transition from gap \(a\) to gap \(b\), with weight \(u^b\), if and only if their sum is at least \(2r+2\). Hence \(\operatorname{tr}(B_r(u)^k)\) enumerates the rooted cyclic words. The formal identity
\[
-\log\det(I-zB_r(u))=\sum_{k\ge1}\frac{z^k}{k}\operatorname{tr}(B_r(u)^k)
\]
and differentiation by \(u\) prove the coefficient formula. Formal power series are well-defined because every matrix entry has positive \(u\)-degree. Terms with \(n<2r+1\) are discarded because that range does not represent the specified cycle powers. Direct expansion of the \(5\)-square determinant supplies \(Q_2\) above.

**4. Sharp support.** Every allowed gap is at most \(2r+1\), so \(n\le k(2r+1)\). Summing all \(k\) consecutive-pair inequalities yields \(2n\ge2k(r+1)\). Thus \(\lceil n/(2r+1)\rceil\le k\le\lfloor n/(r+1)\rfloor\). Conversely, for every integer \(k\) in this interval, take \(k\) integers between \(r+1\) and \(2r+1\) whose sum is \(n\); this is possible by distributing \(n-k(r+1)\) increments, at most \(r\) per gap. Every such cyclic word satisfies both inequalities and produces a valid set, proving positivity at every intermediate cardinality.

**5. Parity rigidity at the upper endpoint.** Suppose \(n=k(r+1)\). The sum of all consecutive-pair gaps equals \(2n=2k(r+1)\), while each pair is at least \(2r+2\). Equality of sums forces every pair to have sum exactly \(2r+2\). Hence \(g_{i+2}=g_i\). For odd \(k\), all gaps must equal \(r+1\), leaving one admissible rooted word. For even \(k\), the first gap can be any of the \(2r+1\) integers from one to \(2r+1\), and all remaining gaps are determined by alternation. Multiplying the respective rooted-word counts by \(n/k=r+1\) gives the two formulas.

## Verification

The accompanying standalone Python program constructs graph adjacency directly and independently enumerates all nonempty vertex subsets, checking domination and inclusion-minimality without calling the gap classification. It compares complete coefficient distributions to a separate dynamic-programming implementation of cyclic gap-word counts. It also checks the cardinality support and parity-rigidity claims. A successful run prints `VERIFY_OK`. The computed tests corroborate the finite instances but are not the proof of the all-order theorem.

## Relationship to prior work

Galvin and Zhang, *The domination polynomial of powers of paths and cycles*, arXiv:2408.12731v1 (publicly posted 2024-08-22), prove recurrences and unimodality for the polynomial of **all** dominating sets. Their Theorems 1.4–1.5 and cycle recurrence do not classify **inclusion-minimal** sets or count them by size; the present private-witness condition and parity-rigid maximum multiplicity are different assertions. For \(r=1\), the univariate count of inclusion-minimal dominating sets of cycles is already recorded in OEIS A253413 and is not claimed new. General algorithmic work on minimal dominating set enumeration (Kanté and collaborators, 2014) does not give this uniform graph-family enumerator. A previous result for **connected** dominating sets of cycle powers has a distinct gap condition and neither implies nor is implied by this inclusion-minimal-domination formula.

## Limitations

The claim applies only to the cycle powers with \(n\ge2r+1\), not arbitrary circulants or path powers. The univariate \(r=1\) sequence is prior art. The finite checker does not establish infinite correctness; the combinatorial argument does. Search of indexed literature and closely related full texts cannot exclude an unindexed equivalent result, and independent mathematical validation remains unperformed.

## References

1. D. Galvin and Y. Zhang, *The domination polynomial of powers of paths and cycles*, arXiv:2408.12731v1, 2024-08-22, https://arxiv.org/html/2408.12731v1 .
2. OEIS A253413, *Number of minimal dominating sets in the cycle graph*, https://oeis.org/A253413 .
3. M. M. Kanté, V. Limouzy, A. Mary and L. Nourine, *On the Enumeration of Minimal Dominating Sets and Related Notions*, SIAM Journal on Discrete Mathematics 28 (2014), DOI:10.1137/120862612.
