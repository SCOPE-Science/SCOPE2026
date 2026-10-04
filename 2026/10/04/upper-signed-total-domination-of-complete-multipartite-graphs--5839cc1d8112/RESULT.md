# Upper signed total domination of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph with \(r\ge2\), with parts \(V_1,\ldots,V_r\) of sizes \(n_1,\ldots,n_r\), and let \(N=\sum_i n_i\). A signed total dominating function is a map \(f:V(G)\to\{-1,1\}\) such that the sum on every open neighborhood is at least \(1\). It is minimal when no distinct signed total dominating function is coordinatewise at most \(f\).

For each part define
\[
\varepsilon_i=\begin{cases}1,&N-n_i\text{ is odd},\\2,&N-n_i\text{ is even}.\end{cases}
\]
For a signed total dominating function put \(W=f(V(G))\), \(\sigma_i=f(V_i)\), and
\[
Q(f)=\{i:W-\sigma_i=\varepsilon_i\}.
\]
Then \(f\) is minimal exactly when every part containing a \(+1\)-vertex has a different tight part in \(Q(f)\). Equivalently, either \(|Q(f)|\ge2\), or \(Q(f)=\{q\}\) and every vertex of \(V_q\) has value \(-1\).

Consequently,
\[
\Gamma_t^s(G)=\max_{1\le i<j\le r}
\min\{n_i+\varepsilon_i,\ n_j+\varepsilon_j,\ N-n_i-n_j+\varepsilon_i+\varepsilon_j\}.
\]

## Assumptions and scope
The graph is finite, simple, undirected, connected, and complete multipartite; equivalently \(r\ge2\) and every \(n_i\ge1\). The parameter \(\Gamma_t^s\) is the maximum weight of a minimal signed total dominating function, using open neighborhoods. This is distinct from the signed total domination number, which minimizes over all signed total dominating functions, and from upper signed domination, which uses closed neighborhoods.

## Proof
For a vertex of \(V_i\), its open-neighborhood sum is
\[
T_i=f(V(G)\setminus V_i)=W-\sigma_i.
\]
This sum has the parity of \(N-n_i\). Hence the condition \(T_i\ge1\) is equivalent to \(T_i\ge\varepsilon_i\).

Suppose a \(+1\)-vertex in \(V_j\) is changed to \(-1\). The value \(T_j\) is unchanged, while every \(T_i\) with \(i\ne j\) decreases by exactly \(2\). Therefore this single change destroys signed total domination exactly when some \(i\ne j\) is tight, meaning \(T_i=\varepsilon_i\). If no such tight part exists, parity gives \(T_i\ge\varepsilon_i+2\) for every \(i\ne j\), so the change preserves all inequalities. Since any coordinatewise smaller function is obtained by changing one or more \(+1\)-values to \(-1\), this proves the stated minimality criterion.

Now let \(f\) be minimal and suppose at least two parts \(V_i,V_j\) are tight. Then
\[
\sigma_i=W-\varepsilon_i,\qquad \sigma_j=W-\varepsilon_j.
\]
The bounds \(|\sigma_i|\le n_i\) and \(|\sigma_j|\le n_j\) give
\[
W\le n_i+\varepsilon_i,\qquad W\le n_j+\varepsilon_j.
\]
The sum on the remaining \(N-n_i-n_j\) vertices equals
\[
\varepsilon_i+\varepsilon_j-W,
\]
and cannot be smaller than \(-(N-n_i-n_j)\). Thus
\[
W\le N-n_i-n_j+\varepsilon_i+\varepsilon_j.
\]
So the weight of every minimal function with at least two tight parts is bounded by the displayed pairwise minimum. If there is a unique tight part \(V_q\), minimality forces every value on \(V_q\) to be \(-1\), and tightness gives \(W=\varepsilon_q-n_q\le1\). Every pairwise minimum is at least \(2\), so this case never determines the upper parameter.

It remains to attain every pairwise bound. Fix distinct \(i,j\), let \(M=N-n_i-n_j\), and set
\[
B=\min\{n_i+\varepsilon_i,\ n_j+\varepsilon_j,\ M+\varepsilon_i+\varepsilon_j\}.
\]
The three quantities in this minimum all have the parity of \(N\), so \(B\) has that parity. Choose values on \(V_i\) and \(V_j\) with sums \(B-\varepsilon_i\) and \(B-\varepsilon_j\), respectively; the defining bounds for \(B\) make these sums attainable. The remaining vertices must have total sum \(\varepsilon_i+\varepsilon_j-B\). Equivalently, they must contain
\[
K=\frac{M+\varepsilon_i+\varepsilon_j-B}2
\]
positive vertices. One has \(K\le\lceil M/2\rceil\). Indeed, if \(M\) is even then each of \(n_i+\varepsilon_i\) and \(n_j+\varepsilon_j\) is at least \(\varepsilon_i+\varepsilon_j\); if \(M\) is odd each is at least \(\varepsilon_i+\varepsilon_j-1\). Therefore the positive vertices can be distributed among the remaining parts with at most \(\lceil n_h/2\rceil\) positives in each \(V_h\). Such a choice gives \(\sigma_h\le0\) when \(n_h\) is even and \(\sigma_h\le1\) when \(n_h\) is odd. Because \(B\ge2\) for even \(N\) and \(B\ge3\) for odd \(N\), these inequalities imply \(\sigma_h\le B-\varepsilon_h\), hence \(T_h\ge\varepsilon_h\). The parts \(i\) and \(j\) are tight, so the constructed function is minimal and has weight \(B\). Maximizing over pairs proves the formula.

## Verification
The standalone verifier `verify.py` constructs every nondecreasing complete-multipartite part profile through order \(10\), enumerates every \((-1, 1)\)-labeling, checks the open-neighborhood inequalities directly, and compares literal one-coordinate minimality with the tight-part criterion. Through order \(7\) it also checks minimality against every coordinatewise smaller labeling, independently validating the one-coordinate reduction. It then compares the maximum minimal weight with the formula for every profile and confirms that every pairwise bottleneck value is attained. A replay of the packaged verifier returned:

`VERIFY_OK profiles=128 labelings=64916 minimal_functions=6921 full_lower_checks=511 formula_checks=128 pair_targets=1026 max_order=10`

The finite computation is a regression check, not the proof of the infinite statement.

## Relationship to prior work
Henning introduced the upper signed total domination number as the maximum weight of a minimal signed total dominating function and established general bounds. Liang later determined the minimum signed total domination number for complete multipartite graphs under MSC 05C69. Those results concern, respectively, general upper bounds and the opposite extremum on the same graph class. The result here supplies an exact arbitrary-part-size upper formula together with a complete minimality criterion for the multipartite class. Shan and Cheng subsequently sharpened general upper bounds for the upper signed total domination number; their accessible abstract does not state an exact complete-multipartite evaluation.

A related exact result for upper signed domination of complete multipartite graphs uses closed neighborhoods and therefore does not imply the present open-neighborhood formula.

## Limitations
The theorem is confined to complete multipartite graphs. The literature comparison used full accessible text for Liang's complete-multipartite minimum-parameter paper and bibliographic abstracts for the two papers on the upper signed total parameter; the latter full texts were not available through the accessible open sources. Thus the main residual originality risk is an older exact complete-multipartite specialization hidden in inaccessible literature or indexed under alternate terminology. No claim is made about graphs outside the stated class.

## References
1. M. A. Henning, “Signed total domination in graphs,” *Discrete Mathematics* 278 (2004), 109–125. DOI: 10.1016/j.disc.2003.06.002.
2. H. Liang, “Signed and Minus Domination in Complete Multipartite Graphs,” arXiv:1205.0343v1 (2012), MSC 05C69.
3. E. Shan and E. T. C. Cheng, “Upper bounds on the upper signed total domination number of graphs,” *Discrete Applied Mathematics* 157 (2009), 1098–1103. DOI: 10.1016/j.dam.2008.04.005.
