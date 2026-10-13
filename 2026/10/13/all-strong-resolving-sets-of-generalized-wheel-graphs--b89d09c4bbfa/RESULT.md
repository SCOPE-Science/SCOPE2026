# All strong resolving sets of generalized wheel graphs
## Finding
For integers \(m\ge1\) and \(n\ge3\), let
\[
W_{m,n}=C_n\vee\overline{K_m},
\]
where the \(m\) center vertices are pairwise nonadjacent and each is adjacent to every vertex of the rim cycle \(C_n\). A set \(S\subseteq V(W_{m,n})\) is strong resolving when every distinct pair of vertices is strongly resolved by some vertex of \(S\).

For \(n\ge4\), \(S\) is strong resolving if and only if its complement contains at most one center and the omitted rim vertices are either empty, a singleton, or an adjacent pair. Consequently
\[
\mathcal R_{m,n}(x)=\sum_{S\text{ strong resolving}}x^{|S|}
=(x^m+m x^{m-1})(x^n+n x^{n-1}+n x^{n-2}).
\]
In particular,
\[
\operatorname{sdim}(W_{m,n})=m+n-3,
\qquad
\#\{\text{strong metric bases}\}=mn,
\]
and the total number of strong resolving sets is \((m+1)(2n+1)\).

For \(n=3\) and \(m\ge2\), \(S\) is strong resolving if and only if its complement contains at most one center and at most one rim vertex. Hence
\[
\mathcal R_{m,3}(x)=(x^m+m x^{m-1})(x^3+3x^2),
\]
so \(\operatorname{sdim}(W_{m,3})=m+1\), with exactly \(3m\) bases and \(4(m+1)\) strong resolving sets. Finally, \(W_{1,3}\cong K_4\), so
\[
\mathcal R_{1,3}(x)=x^4+4x^3,
\]
with strong metric dimension \(3\) and four bases.

The scalar values of the strong metric dimension are prior results; the new claim is the complete all-set classification and its enumerative consequences.

## Assumptions and scope
Graphs are finite, simple, connected, and undirected. The cycle vertices are indexed cyclically as \(v_0,\ldots,v_{n-1}\), and the centers are \(u_1,\ldots,u_m\). A vertex \(w\) strongly resolves \(a,b\) when either \(a\) lies on a shortest \(b\)-to-\(w\) path or \(b\) lies on a shortest \(a\)-to-\(w\) path. Endpoints count as lying on their shortest paths.

The result covers every \(m\ge1\) and \(n\ge3\). The special case \(n=3,m=1\) is separated because the graph is complete.

## Proof
First suppose \(n\ge4\). Any two distinct centers are at distance two and are mutually maximally distant: moving from either center to any neighbor cannot increase its distance from the other center. Thus no third vertex strongly resolves a pair of omitted centers, so a strong resolving set can omit at most one center.

Two nonadjacent rim vertices are also at distance two and mutually maximally distant. Therefore two omitted rim vertices, when both occur, must be adjacent. Three omitted rim vertices necessarily contain a nonadjacent pair, so at most two rim vertices may be omitted. This proves the necessity of the stated omission pattern.

For sufficiency, let \(T=V(W_{m,n})\setminus S\) satisfy the omission rule. Any pair with an endpoint in \(S\) is strongly resolved by that endpoint, so only pairs inside \(T\) require attention. If \(T\) contains two rim vertices, they are adjacent, say \(v_i,v_{i+1}\); a selected neighbor on the other side of one endpoint, such as \(v_{i-1}\) or \(v_{i+2}\), lies on a shortest path through that endpoint and strongly resolves the pair. If \(T\) contains a center \(u\) and a rim vertex \(v_i\), then because \(n\ge4\) there is a selected rim vertex \(v_j\) nonadjacent to \(v_i\). The path \(v_j-u-v_i\) has length two and is shortest, so \(v_j\) strongly resolves \(u,v_i\). These observations also handle the case in which \(T\) consists of one center together with two adjacent rim vertices. Hence every allowed omission pattern is strong resolving.

The center and rim choices are independent. On the center side one may omit zero or one vertex, giving \(x^m+m x^{m-1}\). On an \(n\)-cycle with \(n\ge4\), one may omit zero vertices, one of \(n\) single vertices, or one of \(n\) cycle edges, giving \(x^n+n x^{n-1}+n x^{n-2}\). Multiplication gives the stated enumerator. Its least-degree term has degree \(m+n-3\) and coefficient \(mn\).

Now let \(n=3\) and \(m\ge2\). Every pair of centers is again mutually maximally distant, and every pair of rim vertices is mutually maximally distant because the rim is a triangle whose vertices have identical closed neighborhoods. Thus at most one center and at most one rim vertex may be omitted. Conversely, if one center \(u\) and one rim vertex \(v\) are omitted, another center \(u'\in S\) exists and the length-two path \(u'-v-u\) is shortest, so \(u'\) strongly resolves the omitted pair. This gives the triangular-rim factorization. When \(m=1\), the graph is \(K_4\), and a strong resolving set in a complete graph can omit at most one vertex.

## Verification
A standalone exact checker enumerates every subset of \(V(W_{m,n})\) for \(1\le m\le4\) and \(3\le n\le7\). It computes all-pairs graph distances, tests the definition of strong resolution directly, compares every subset with the structural criterion above, compares every coefficient with the closed polynomial, and checks the minimum degree and number of bases. The replay result is:

`VERIFY_OK pairs=20 subset_checks=7440 classification_checks=7440 coefficient_checks=170 minimum_checks=20 max_order=11`

This finite replay is a boundary and formula check; the all-orders conclusion comes from the proof above.

## Relationship to prior work
Oellermann and Peters-Fransen introduced the standard strong-dimension framework and reduced the minimum problem to a vertex-cover problem. Kusmayadi, Kuntari, Rahmadi, and Lathifah study exactly the same multiple-hub wheel family under the name \(t\)-fold wheel and prove the scalar values \(t+1\) for a triangular rim with \(t\ge2\), \(3\) for the ordinary triangular wheel, and \(t+n-3\) for rim order at least four. Their relevant section supplies lower bounds and one minimum construction; it does not state the complete family of strong resolving sets, a cardinality enumerator, or the number of all minimum bases. The later generalized-wheel treatment of dominant strong metric dimension again records the scalar strong metric dimension for \(C_n\vee\overline{K_m}\), not the all-set profile proved here.

Thus the scalar strong metric dimensions are not claimed as new. The contribution is the exact omission criterion for every strong resolving set, the factorized enumerators, and the resulting exact counts of all bases and all strong resolving sets.

## Limitations
No claim is made about directed strong metric dimension, fractional strong metric dimension, dominant strong metric dimension, or graph families other than \(C_n\vee\overline{K_m}\). The literature comparison found no equivalent all-set enumeration, but poorly indexed or differently named work remains a residual risk. The computational replay checks orders through eleven vertices only and is not used as an infinite proof.

## References
1. O. R. Oellermann and J. Peters-Fransen, “The strong metric dimension of graphs and digraphs,” *Discrete Applied Mathematics* 155 (2007), 356–364. DOI: 10.1016/j.dam.2006.06.009.
2. T. A. Kusmayadi, S. Kuntari, D. Rahmadi, and F. A. Lathifah, “On the strong metric dimension of some related wheel graph,” *Far East Journal of Mathematical Sciences* 99 (2016), 1325–1334. DOI: 10.17654/MS099091325.
3. D. Kuziak, I. G. Yero, and J. A. Rodríguez-Velázquez, “Strong metric dimension of rooted product graphs,” *International Journal of Computer Mathematics* 93 (2016), 1265–1280. DOI: 10.1080/00207160.2015.1061656.
4. “The dominant strong metric dimension of graphs,” 2025. DOI: 10.1080/09728600.2025.2574313.
