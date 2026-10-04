# All 2-rainbow dominating functions of complete multipartite graphs

## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a complete multipartite graph with \(r\ge2\). A 2-rainbow dominating function is a map
\[
f:V(G)\longrightarrow\{\varnothing,\{1\},\{2\},\{1,2\}\}
\]
such that every vertex labelled \(\varnothing\) sees both colors in its open neighborhood. For each part \(V_i\), write \(e_i,a_i,b_i,d_i\) for the numbers of vertices carrying \(\varnothing,\{1\},\{2\},\{1,2\}\), respectively, and define
\[
I_1=\{i:a_i+d_i>0\},\qquad I_2=\{i:b_i+d_i>0\},\qquad E=\{i:e_i>0\}.
\]
Then \(f\) is 2-rainbow dominating if and only if, for every \(i\in E\),
\[
I_1\setminus\{i\}\ne\varnothing
\qquad\text{and}\qquad
I_2\setminus\{i\}\ne\varnothing.
\]
Thus all feasible functions are determined exactly by their four-label profiles in the parts. With the weight of \(f\) defined by \(w(f)=\sum_{v\in V(G)}|f(v)|\), the complete weight enumerator is
\[
R_G(x)=\sum_{\substack{e_i+a_i+b_i+d_i=n_i\\ e_i>0\Rightarrow\sum_{j\ne i}(a_j+d_j)>0\\ e_i>0\Rightarrow\sum_{j\ne i}(b_j+d_j)>0}}
\left(\prod_{i=1}^r\binom{n_i}{e_i,a_i,b_i,d_i}\right)x^{\sum_i(a_i+b_i+2d_i)}.
\]
In particular, if \(m=\min_i n_i\), then
\[
\gamma_{r2}(G)=\min\{4,\max\{2,m\}\}.
\]

## Assumptions and scope
Graphs are finite, simple, and undirected. Every part is nonempty and \(r\ge2\), so the graph is connected. The statement concerns ordinary 2-rainbow domination, not proper, maximal, independent, or total variants. The polynomial counts every labelled 2-rainbow dominating function by total color weight; it does not quotient by permutations of vertices, parts, or colors.

## Proof
A vertex \(v\in V_i\) has neighborhood \(V(G)\setminus V_i\). Hence, when \(f(v)=\varnothing\), color \(1\) is present in \(N(v)\) exactly when some part other than \(V_i\) belongs to \(I_1\), and color \(2\) is present exactly when some part other than \(V_i\) belongs to \(I_2\). Therefore every empty-labelled vertex is valid exactly when \(I_1\setminus\{i\}\) and \(I_2\setminus\{i\}\) are both nonempty. This proves the characterization, including both directions and all boundary cases.

For fixed nonnegative integers \((e_i,a_i,b_i,d_i)\) summing to \(n_i\), the number of assignments inside \(V_i\) is the multinomial coefficient \(\binom{n_i}{e_i,a_i,b_i,d_i}\). The part choices are independent once the profile satisfies the displayed feasibility conditions. Multiplying these counts and summing over all feasible profiles yields the stated polynomial, while the exponent is exactly \(\sum_i(a_i+b_i+2d_i)\).

For the minimum weight, weight \(1\) is impossible because an empty vertex in a different part cannot see both colors. If \(m=1\), assigning \(\{1,2\}\) to the unique vertex of a smallest part and \(\varnothing\) elsewhere has weight \(2\). If \(m=2\), assigning \(\{1\}\) and \(\{2\}\) to the two vertices of a smallest part has weight \(2\). If \(m=3\), assigning nonempty singleton-color labels to all three vertices of a smallest part, using both colors, has weight \(3\); weight \(2\) is impossible because every occupied part still contains an empty vertex or some other part is empty, forcing both colors to have support outside each relevant empty part. If \(m\ge4\), giving label \(\{1,2\}\) to one vertex in each of two distinct parts has weight \(4\). Weight \(3\) is impossible because every part contains an empty vertex, so the characterization forces each of the two colors to occur in at least two distinct parts, requiring at least four part-color incidences and therefore total weight at least \(4\). These cases give \(\gamma_{r2}(G)=\min\{4,\max\{2,m\}\}\).

## Verification
A standalone verifier exhaustively enumerates every integer part-size profile with at least two parts and total order at most \(8\). For each profile it checks every one of the \(4^N\) vertex labelings twice: once from the literal open-neighborhood definition and once from the structural criterion above. It then independently computes the multinomial profile sum and compares every coefficient with the brute-force weight distribution, and checks the minimum-weight formula. Exact replay reports:

`VERIFY_OK profiles=58 assignments=1653904 coefficient_checks=818 max_order=8`

The finite census is a stress test and reproducibility check; the infinite statement follows from the proof.

## Relationship to prior work
Wu and Jafari Rad define 2-rainbow domination in the form used here and develop general bounds and extremal results. Their inspected full text does not give an all-function complete-multipartite classification or weight enumerator. Jose and Sangeetha later study proper 2-rainbow domination and their abstract explicitly mentions complete multipartite graphs among classes for which scalar bounds are considered. The accessible record does not state the all-function ordinary enumerator above; the publisher full text was not accessible during the comparison. The scalar formula is included as a consequence of the classification, not as the sole originality claim.

## Limitations
The result is specific to complete multipartite graphs and to two colors. It does not assert an analogous product or profile formula for general \(k\)-rainbow domination. A residual literature risk remains because the full text of the directly relevant 2018 proper-variant paper could not be inspected end to end, and older results may be indexed under alternate rainbow-domination terminology.

## References
1. Y. Wu and N. Jafari Rad, *Bounds on the 2-rainbow domination number of graphs*, arXiv:1005.0988v1, first public posting 2010-05-06.
2. J. Jose and V. Sangeetha, *On Proper 2-rainbow Domination in Graphs*, International Journal of Mathematical Analysis and Applications 6(1-C) (2018), 429--434.
3. B. Brešar, M. A. Henning, and D. F. Rall, *Rainbow domination in graphs*, Taiwanese Journal of Mathematics 12 (2008), 213--225.
