# Weight enumerator of outer-independent Roman functions on complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph with \(r\ge2\) and \(N=\sum_i n_i\). If \(\mathcal O_G(z)=\sum_f z^{\omega(f)}\), summed over all outer-independent Roman dominating functions, then \[\mathcal O_G(z)=(z+z^2)^N+\sum_{i=1}^r\Big((1+z+z^2)^{n_i}-(z+z^2)^{n_i}\Big)\Big((z+z^2)^{N-n_i}-z^{N-n_i}\Big).\] Equivalently, either no vertex has label \(0\), or all zero labels lie in one unique part and at least one label \(2\) lies outside that part. Thus the total number of such functions is \[2^N+\sum_{i=1}^r(3^{n_i}-2^{n_i})(2^{N-n_i}-1).\] The known minimum formula \(\gamma_{oiR}(G)=N-\max_i n_i+1\) is recovered as the least exponent with nonzero coefficient.

## Assumptions and scope
All graphs are finite and simple. Let \(G=K_{n_1,\ldots,n_r}\) be connected with partite classes \(X_1,\ldots,X_r\), \(r\ge2\), and \(N=\sum_i n_i\). An outer-independent Roman dominating function is a map \(f:V(G)\to\{0,1,2\}\) whose zero set is independent and every zero-labeled vertex has a neighbor labeled \(2\).

## Proof
Because vertices in different parts are adjacent, an independent zero set is either empty or contained in exactly one part.

If the zero set is empty, every vertex independently receives label \(1\) or \(2\), giving \((z+z^2)^N\).

If the zero set is nonempty and contained in \(X_i\), then inside \(X_i\) every label in \(\{0,1,2\}\) is allowed except the all-positive case, giving
\[
(1+z+z^2)^{n_i}-(z+z^2)^{n_i}.
\]
Every zero vertex is adjacent to every vertex outside \(X_i\) and to no vertex inside \(X_i\). Hence the Roman condition is exactly that at least one outside vertex has label \(2\). Outside \(X_i\), labels are otherwise in \(\{1,2\}\), giving
\[
(z+z^2)^{N-n_i}-z^{N-n_i}.
\]
The nonempty-zero cases for different \(i\) are disjoint, so summing gives the polynomial.

At \(z=1\) this yields the stated total count. The least weight in the \(i\)-th nonempty-zero family is obtained by labeling all of \(X_i\) with \(0\), one outside vertex with \(2\), and all other outside vertices with \(1\), giving \(N-n_i+1\). Minimizing gives \(N-\max_i n_i+1\), the previously published minimum formula.

## Verification
The included checker enumerates every ternary labeling of every connected complete multipartite isomorphism type of orders \(2\) through \(9\). It tests independence of the zero set and the required adjacent label \(2\) directly, expands the claimed polynomial independently with integer arithmetic, and compares every coefficient, the total count, and the least nonzero exponent.

## Relationship to prior work
The 2017 paper introducing outer-independent Roman domination already gives complete bipartite and complete multipartite minimum values. Its Corollary 5 states \(\gamma_{oiR}(K_{n_1,\ldots,n_r})=N-\max_i n_i+1\), so that minimum is prior work and is not the originality claim.

The accepted-author full text studies minimum values, complexity, bounds, and extremal graphs. Targeted full-text searches found no weight polynomial, enumerator, or count of all feasible functions. Later same-parameter papers and surveys retrieved in targeted searches likewise focus on bounds, products, trees, or related variants. The new content is the exact classification of every feasible labeling and its full weight distribution.

## Limitations
The theorem concerns outer-independent Roman domination only, not total, double, signed, Italian, or rainbow variants. The minimum-value corollary is prior-covered. The finite computation through order \(9\) is corroborative only; the arbitrary-order theorem follows from the proof. Search coverage cannot exclude differently phrased or non-indexed enumerative work.

## References
1. H. Abdollahzadeh Ahangar, M. Chellali, V. Samodivkin, “Outer independent Roman dominating functions in graphs,” International Journal of Computer Mathematics 94(12) (2017), 2547–2557, DOI 10.1080/00207160.2017.1301437. Accepted author version posted online 13 March 2017.
2. A. Cabrera Martínez, S. Cabrera García, A. Carrión García, A. M. Grisales del Rio, “On the Outer-Independent Roman Domination in Graphs,” Symmetry 12 (2020), 1846, DOI 10.3390/sym12111846.
3. M. Chellali, N. Jafari Rad, S. M. Sheikholeslami, L. Volkmann, “Varieties of Roman domination II,” AKCE International Journal of Graphs and Combinatorics 17(3) (2020), 966–984, DOI 10.1016/j.akcej.2019.12.001.
