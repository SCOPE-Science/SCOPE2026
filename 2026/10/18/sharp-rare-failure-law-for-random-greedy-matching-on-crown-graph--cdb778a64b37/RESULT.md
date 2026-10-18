# Sharp rare-failure law for random greedy matching on crown graphs

## Finding

For each integer \(n\ge2\), let \(G_n\) be the crown graph with left vertices \(u_1,\dots,u_n\), right vertices \(v_1,\dots,v_n\), and edge \(u_i v_j\) exactly when \(i\ne j\). Inspect its edges in a uniformly random order, selecting an edge if and only if both endpoints are still unmatched. Let \(q_n\) be the probability that the resulting maximal matching is not perfect.

**Theorem.** The resulting matching always has either \(n\) or \(n-1\) edges. Its failure probability is determined exactly by the triangular rational recurrence
\[
\begin{aligned}
f_{1,0}&=0,\qquad f_{1,1}=1,\\
f_{r,c}&=\frac{c(c-1)f_{r-1,c-2}+2c(r-c)f_{r-1,c-1}+(r-c)^2f_{r-1,c}}{r^2-c},
\quad 2\le r,\quad 0\le c\le r,\\
q_n&=f_{n,n}.
\end{aligned}
\]
Only terms with positive multipliers are included, so no out-of-range state is needed. All values are exact rational numbers, computable using \(O(n^2)\) arithmetic operations and \(O(n)\) memory if evaluated layer by layer.

Writing \(H_j=\sum_{i=1}^{j}1/i\), the following explicit bound holds for every \(n\ge2\):
\[
0\le \frac{2}{n+1}-q_n\le
\frac{4e^{\pi^2/3}\bigl(H_{n+1}-H_2\bigr)}{n(n-1)}.
\]
Consequently,
\[
\boxed{q_n=\frac{2}{n}+O\!\left(\frac{\log n}{n^2}\right),\qquad
\lim_{n\to\infty}nq_n=2.}
\]
For example, \(q_2=0\), \(q_3=1/3\), \(q_4=q_5=4/21\), and \(q_6=172/1029\).

## Assumptions and scope

All graphs are finite, simple, and labeled as above. The random experiment samples one uniformly random permutation of the \(n(n-1)\) edges, then uses irrevocable first-available-edge greedy selection. Equivalently, at each stage it chooses uniformly among the currently available edges. This is **not** the algorithm that first samples an unmatched vertex and then a neighbor, nor any independently sampled edge-weight optimization rule. The probabilities concern the greedy output itself, not the existence or number of perfect matchings.

## Proof

**1. State reduction.** After \(n-r\) edges have been accepted, the unmatched left and right label sets each have size \(r\). Write \(c\) for the number of labels present on both sides; exactly these \(c\) diagonal pairs remain forbidden. Thus there are \(r^2-c\) available edges. For \(r\ge2\) this is positive, hence termination is possible only with zero unmatched vertices (perfect matching) or one unmatched vertex on each side whose labels agree (matching of size \(n-1\)).

Choosing an available edge from among these \(r^2-c\) possibilities removes two shared labels in \(c(c-1)\) choices, one shared label in \(2c(r-c)\) choices, and no shared label in \((r-c)^2\) choices. The new state is respectively \((r-1,c-2)\), \((r-1,c-1)\), or \((r-1,c)\). The uniform original edge order induces a uniform next available edge after every accepted edge because rejected edges cannot become feasible later. This proves the recurrence and both terminal values.

**2. A nearly harmonic potential.** Let \(C_r\) be the random number of shared labels when \(r\) vertices remain on each side, and set \(V_r(c)=2c/[r(r+1)]\). The transition counts give
\[
\mathbb E[C_{r-1}\mid C_r=c]=c-\frac{2c(r-1)}{r^2-c}.
\]
Elementary cancellation then yields the exact drift identity
\[
\mathbb E[V_{r-1}(C_{r-1})\mid C_r=c]-V_r(c)
=-\frac{4c(c-1)}{r(r-1)(r+1)(r^2-c)}.
\]
Since \(C_n=n\) and \(V_1(C_1)=C_1\) is precisely the failure indicator,
\[
\frac{2}{n+1}-q_n
=\sum_{r=2}^n\mathbb E\!\left[
\frac{4C_r(C_r-1)}{r(r-1)(r+1)(r^2-C_r)}
\right]\ge0.
\]
This exact expression also shows where the leading approximation loses mass: stages with at least two surviving forbidden pairs.

**3. Uniform control of the loss.** Directly from the same transition counts, for every valid state,
\[
\mathbb E[C_{r-1}(C_{r-1}-1)\mid C_r=c]
=c(c-1)\left(1-\frac{4r-6}{r^2-c}\right)
\le c(c-1)\frac{(r-2)^2+2}{r^2}.
\]
Put \(F_r=\mathbb E[C_r(C_r-1)]\), so \(F_n=n(n-1)\). Iterating this inequality for \(2\le r\le n\) gives
\[
\begin{aligned}
F_r&\le n(n-1)\prod_{j=r+1}^n\frac{(j-2)^2+2}{j^2}\\
&=\frac{r^2(r-1)^2}{n(n-1)}
\prod_{t=r-1}^{n-2}\left(1+\frac{2}{t^2}\right)
\le\frac{e^{\pi^2/3}r^2(r-1)^2}{n(n-1)}.
\end{aligned}
\]
We used \(1+x\le e^x\) and \(\sum_{t\ge1}2/t^2=\pi^2/3\). As \(0\le C_r\le r\), we have \(r^2-C_r\ge r(r-1)\). Substitute the displayed bound for \(F_r\) in the exact loss identity:
\[
0\le \frac{2}{n+1}-q_n
\le \sum_{r=2}^n\frac{4e^{\pi^2/3}}{n(n-1)(r+1)}
=\frac{4e^{\pi^2/3}(H_{n+1}-H_2)}{n(n-1)}.
\]
This proves the explicit inequality and the asserted asymptotics without numerical extrapolation. \(\square\)

## Verification

The accompanying standalone `verify.py` uses exact rational arithmetic in two different implementations: a two-parameter recurrence and a direct recursion over labeled sets of remaining vertices. They agree for all starting crown graphs with \(2\le n\le7\). The code separately exhausts all \(2!\) and \(6!\) initial edge orders for \(n=2,3\), and checks both algebraic conditional identities for every state with \(2\le r\le30\). The finite computations support the proof but do not replace the all-orders drift and moment argument. Run `python3 verify.py`; compare its stdout with `verification_output.txt`.

## Relationship to prior work

The randomized edge-greedy matching process was studied in a general graph setting by Dyer and Frieze (1991); their published abstract emphasizes global performance examples and sparse graph classes, not an exact crown-graph failure law. The open-access full-text 2024 work of Krivelevich and collaborators identifies greedy matching with greedy independent sets on line graphs and analyzes chiefly locally convergent and locally tree-like graph sequences. The present dense crown-graph sequence instead has growing degree and the result concerns a rare, exact one-pair defect rather than a limiting matching density. McGregor's 2026 manuscript studies a different matching approximation procedure built from random greedy independent sets. No cited general result directly implies the exact two-parameter law or the sharp coefficient two.

## Limitations

The theorem is specific to uniform random **available-edge** selection on \(K_{n,n}\) with exactly one perfect matching deleted. It is not a theorem about arbitrary dense bipartite graphs, vertex-first greedy algorithms, the time at which a random edge-addition graph acquires a perfect matching, or higher-order expansion constants. The explicit error bound is not claimed to be optimal. Search-based originality assessments cannot exclude all unindexed literature, and the full texts of some older and recent relevant articles were not available for comparison; these remain bibliographic risks.

## References

1. A. McGregor, *Matchings via Random Greedy Independent Set: A Simpler Algorithm and Analysis*, arXiv:2608.11163, first public August 11, 2026. https://arxiv.org/abs/2608.11163
2. M. Dyer and A. Frieze, *Randomized greedy matching*, Random Structures & Algorithms 2 (1991), 29–45, doi:10.1002/rsa.3240020104. https://doi.org/10.1002/rsa.3240020104
3. M. Krivelevich, T. Mészáros, P. Michaeli, and C. Shikhelman, *Greedy maximal independent sets via local limits*, Random Structures & Algorithms 64 (2024), 986–1015, doi:10.1002/rsa.21200. https://doi.org/10.1002/rsa.21200
4. R. Glebov, Z. Luria, and M. Simkin, *Perfect Matchings in Random Subgraphs of Regular Bipartite Graphs*, first posted May 17, 2018, arXiv:1805.06944 (a different edge-addition model). https://arxiv.org/abs/1805.06944
