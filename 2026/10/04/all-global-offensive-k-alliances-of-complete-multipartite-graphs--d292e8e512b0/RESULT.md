# All global offensive \(k\)-alliances of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph with parts \(V_1,\ldots,V_r\), where \(r\ge2\), \(n_i=|V_i|\), and \(N=\sum_i n_i\). Let \(\Delta=N-\min_i n_i\), and fix an integer \(k\) with \(1\le k\le\Delta\). For \(S\subseteq V(G)\), write \(s=|S|\) and \(s_i=|S\cap V_i|\), and define
\[
h_i(k)=\left\lceil\frac{N-n_i+k}{2}\right\rceil.
\]
Then
\[
S\text{ is a global offensive }k\text{-alliance}
\quad\Longleftrightarrow\quad
s_i<n_i\Longrightarrow s-s_i\ge h_i(k)\quad\text{for every }i.
\]
In particular, membership depends only on the part-intersection profile \((s_1,\ldots,s_r)\).

For \(1\le s\le N\), put
\[
u_i(s,k)=\min\{n_i-1,\,s-h_i(k)\}.
\]
If a sum whose upper limit is negative is interpreted as empty, then the exact cardinality enumerator of all global offensive \(k\)-alliances is
\[
A_{G,k}(x)=
\sum_{s=1}^N
\left(
[y^s]\prod_{i=1}^r
\left(
y^{n_i}+\sum_{j=0}^{u_i(s,k)}\binom{n_i}{j}y^j
\right)
\right)x^s.
\]
Hence \(\gamma_k^o(G)\) is the least \(s\) for which the displayed coefficient is nonzero.

## Assumptions and scope
The graph is finite, simple, and connected; equivalently for this family, \(r\ge2\) and every \(n_i\ge1\). The parameter range \(1\le k\le\Delta\) is the standard positive range for global offensive \(k\)-alliances. A global offensive \(k\)-alliance is a dominating set \(S\) such that every \(v\notin S\) satisfies
\[
\delta_S(v)\ge\delta_{V(G)\setminus S}(v)+k.
\]
Because \(k\ge1\), the displayed inequality itself forces every omitted vertex to have a neighbor in \(S\), so domination need not be checked separately after the inequalities are established.

## Proof
Fix a part \(V_i\) and an omitted vertex \(v\in V_i\setminus S\). In a complete multipartite graph, \(v\) is adjacent to every vertex outside \(V_i\) and to no vertex of \(V_i\). Therefore
\[
\delta_S(v)=s-s_i
\]
and
\[
\delta_{V(G)\setminus S}(v)=N-n_i-(s-s_i).
\]
The global offensive \(k\)-alliance inequality at \(v\) is therefore equivalent to
\[
s-s_i\ge N-n_i-(s-s_i)+k,
\]
which is equivalent to
\[
2(s-s_i)\ge N-n_i+k,
\]
and hence to
\[
s-s_i\ge\left\lceil\frac{N-n_i+k}{2}\right\rceil=h_i(k).
\]
All omitted vertices in the same part have the same two neighbor counts, so one inequality per incomplete part is both necessary and sufficient. If \(V_i\subseteq S\), that part contributes no omitted vertex and imposes no condition. This proves the profile characterization.

Now fix a cardinality \(s\). For part \(V_i\), an intersection size \(j<n_i\) is allowed exactly when \(j\le s-h_i(k)\); the full choice \(j=n_i\) is always allowed because then there is no omitted vertex in that part. Thus the partwise contribution to the profile-counting generating function is
\[
y^{n_i}+\sum_{j=0}^{u_i(s,k)}\binom{n_i}{j}y^j.
\]
Multiplying these factors chooses the intersection size independently in every part and weights a profile by the number \(\prod_i\binom{n_i}{s_i}\) of vertex sets having that profile. Extracting \([y^s]\) imposes total cardinality \(s\), proving the enumerator.

## Verification
A standalone verifier reconstructs every nondecreasing complete-multipartite part profile of total order from \(2\) through \(9\). For every admissible \(k\) and every vertex subset, it checks the literal neighborhood inequality against the profile criterion, then compares every coefficient of the displayed enumerator with exhaustive counting. It also checks the complete-bipartite minimum against the published piecewise formula and the \(k=1\) all-set condition against the published complete-bipartite characterization. Replay output is recorded in `VERIFICATION.md`.

The computation is a finite stress test only. The theorem for arbitrary part sizes follows from the symbolic neighbor-count identity above.

## Relationship to prior work
Bermudo, Rodríguez-Velázquez, Sigarreta, and Yero define global offensive \(k\)-alliances and give exact minimum formulas for complete bipartite graphs in Remark 2.1 of arXiv:0812.1528. Cabahug and Isla later give a necessary-and-sufficient classification of all ordinary global offensive alliances for \(K_{m,n}\), the \(k=1\) two-part case. Chellali and Volkmann study global offensive \(k\)-alliances on bipartite graphs and give general bounds and extremal-tree results.

The present result does not claim novelty for either the complete-bipartite minimum or the \(k=1\) complete-bipartite set characterization. Its originality-bearing content is the arbitrary complete-multipartite profile theorem for every positive \(k\) in the standard range, together with the exact all-cardinality enumerator. The inspected primary sources do not state that multipartite extension or its counting formula.

## Limitations
The result is specific to complete multipartite graphs and to positive \(k\). It does not address negative \(k\), where domination is no longer forced by the alliance inequality and an additional case analysis is required. Search and source inspection cannot exclude every obscure or poorly indexed earlier family-specific formula; this remains a bibliographic risk. The exhaustive computation through order \(9\) is not an infinite proof.

## References
1. S. Bermudo, J. A. Rodríguez-Velázquez, J. M. Sigarreta, and I. G. Yero, “On global offensive \(k\)-alliances in graphs,” arXiv:0812.1528, first posted 2008-12-08. The record gives AMS subject classification 05C69 and Remark 2.1 gives the exact complete-bipartite minimum.
2. I. S. Cabahug Jr. and R. T. Isla, “Global offensive alliances in some special classes of graphs,” *The Mindanawan Journal of Mathematics* 2(1), 43–48, published 2011-10-01. Theorem 3.8 classifies the complete-bipartite \(k=1\) case.
3. M. Chellali and L. Volkmann, “Global offensive \(k\)-alliance in bipartite graphs,” *Opuscula Mathematica* 32(1), 83–89, 2012, doi:10.7494/OpMath.2012.32.1.83. The article is classified under 05C69.
