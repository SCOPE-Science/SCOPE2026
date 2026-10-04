# Weight enumerator of signed Roman dominating functions on complete multipartite graphs

## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph with \(r\ge2\), with nonempty parts \(V_1,\ldots,V_r\). For a labeling \(f:V(G)\to\{-1,1,2\}\), define within each part
\[
a_i=|\{v\in V_i:f(v)=-1\}|,\qquad b_i=|\{v\in V_i:f(v)=1\}|,\qquad c_i=|\{v\in V_i:f(v)=2\}|,
\]
so that \(a_i+b_i+c_i=n_i\). Put
\[
\sigma_i=-a_i+b_i+2c_i,\qquad W=\sum_{i=1}^r\sigma_i,\qquad C=\sum_{i=1}^r c_i,
\]
and let \(\mu_i\) be the minimum label occurring in \(V_i\): explicitly, \(\mu_i=-1\) when \(a_i>0\), \(\mu_i=1\) when \(a_i=0<b_i\), and \(\mu_i=2\) when \(a_i=b_i=0\).

Then \(f\) is a signed Roman dominating function if and only if both of the following hold for every part \(i\):
\[
W-\sigma_i+\mu_i\ge1,
\]
and
\[
a_i>0\quad\Longrightarrow\quad C-c_i\ge1.
\]

Therefore, if
\[
R_{sR}(G;x)=\sum_{f\text{ signed Roman}}x^{\omega(f)},
\]
where \(\omega(f)=\sum_{v\in V(G)}f(v)\), then the exact all-weight enumerator is
\[
R_{sR}(G;x)=\sum_{\substack{a_i,b_i,c_i\ge0\\a_i+b_i+c_i=n_i}}
\left(\prod_{i=1}^r\binom{n_i}{a_i,b_i,c_i}\right)
x^{\sum_i(-a_i+b_i+2c_i)}
\prod_{i=1}^r\mathbf 1[W-\sigma_i+\mu_i\ge1]
\prod_{i:a_i>0}\mathbf 1[C-c_i\ge1].
\]
The coefficient of \(x^w\) is thus exactly the number of signed Roman dominating functions of weight \(w\).

## Assumptions and scope
The graph is finite, simple, connected, and complete multipartite, with \(r\ge2\) and \(n_i\ge1\). The signed Roman definition used here is the standard one: every closed-neighborhood sum is at least \(1\), and every vertex labeled \(-1\) has a neighbor labeled \(2\). The result classifies every such function, not only minimum-weight functions.

The scalar signed Roman domination number for complete multipartite graphs has already been studied in the literature and is not claimed as new here. The contribution assessed here is the exact all-function profile criterion and the resulting full weight distribution.

## Proof
Fix a part \(V_i\) and a vertex \(v\in V_i\). In a complete multipartite graph,
\[
N[v]=\{v\}\cup\bigl(V(G)\setminus V_i\bigr).
\]
Hence
\[
\sum_{u\in N[v]}f(u)=W-\sigma_i+f(v).
\]
The smallest closed-neighborhood sum among vertices of \(V_i\) is therefore \(W-\sigma_i+\mu_i\). Thus the condition that every closed-neighborhood sum be at least \(1\) is equivalent, part by part, to
\[
W-\sigma_i+\mu_i\ge1.
\]

Now suppose \(a_i>0\), so some vertex of \(V_i\) has label \(-1\). Such a vertex is adjacent to every vertex outside \(V_i\) and to no other vertex of \(V_i\). It has a neighbor labeled \(2\) if and only if at least one label \(2\) occurs outside \(V_i\), which is exactly
\[
C-c_i\ge1.
\]
If \(a_i=0\), the signed Roman neighbor condition imposes nothing on part \(V_i\). This proves the stated if-and-only-if criterion.

For a fixed profile \((a_i,b_i,c_i)_{i=1}^r\), the number of labelings realizing it is
\[
\prod_{i=1}^r\binom{n_i}{a_i,b_i,c_i}.
\]
Every such labeling has weight \(\sum_i(-a_i+b_i+2c_i)\), and the two indicator products in the displayed enumerator are exactly the two necessary-and-sufficient conditions proved above. Summing over all part profiles proves the formula.

## Verification
The included verifier enumerates every nondecreasing complete-multipartite part profile of total order from \(2\) through \(9\). For every labeling by \(\{-1,1,2\}\), it evaluates the signed Roman definition directly from graph neighborhoods and independently evaluates the part-profile criterion. It also computes the weight distribution twice: once by brute-force labelings and once from the multinomial profile sum.

A replay of the packaged verifier returned:

`VERIFY_OK profiles=87 labelings=748341 valid_functions=489054 criterion_checks=748341 coefficient_checks=1215 max_order=9`

The finite census is a regression and boundary check; it is not used as a proof for arbitrary order.

## Relationship to prior work
Abdollahzadeh Ahangar, Henning, Löwenstein, Zhao, and Samodivkin introduced signed Roman domination and established general and bipartite bounds. Zhao and Miao later computed exact scalar signed Roman and signed total Roman domination numbers for complete bipartite graphs. Yin and Chen published a paper specifically on the signed Roman domination number of complete multipartite graphs. Those scalar results are treated as prior-covered.

The retained statement is different in logical strength and output: it characterizes every signed Roman dominating function on an arbitrary complete multipartite graph by its partwise label counts and gives every coefficient of the weight enumerator. Focused published-finding searches did not identify a matching all-function enumerator. The full text of the 2017 Yin--Chen paper was not obtained in this run, so an equivalent unpublished-in-index structural lemma inside that paper remains a residual originality risk; the scalar minimum itself is expressly excluded from the novelty claim.

## Limitations
The theorem is restricted to complete multipartite graphs. The finite verifier stops at order \(9\), while the proof is symbolic for arbitrary order. The exact-day public-date field uses the verified public bibliographic date \(2014\text{-}04\text{-}08\); the founding full text bears a \(2012\) copyright and DOI stem, so an earlier exact public day may exist but was not verified and has not been invented. The 2017 complete-multipartite scalar paper was confirmed bibliographically and through later literature, but its full text was not available for direct inspection in this run.

## References
1. H. Abdollahzadeh Ahangar, M. A. Henning, C. Löwenstein, Y. Zhao, V. Samodivkin, “Signed Roman domination in graphs,” Journal of Combinatorial Optimization 27 (2014), 241–255. DOI: 10.1007/s10878-012-9500-0.
2. Y. Zhao, L. Miao, “Signed Roman (Total) Domination Numbers of Complete Bipartite Graphs and Wheels,” Communications in Mathematical Research 33(4) (2017), 318–326. DOI: 10.13447/j.1674-5647.2017.04.04.
3. K. Yin, X.-G. Chen, “Signed Roman domination number of complete multipartite graphs,” Journal of Shantou University (Natural Science) 31(4) (2017), 25–34.
4. M. Duan, X. Hong, “The Signed Roman Domination Number of Two Classes Corona Graph,” Pure Mathematics 10(2) (2020), 91–95. DOI: 10.12677/PM.2020.102014. This later full text supplies an independently accessible bibliographic reference to the Yin--Chen complete-multipartite paper.
