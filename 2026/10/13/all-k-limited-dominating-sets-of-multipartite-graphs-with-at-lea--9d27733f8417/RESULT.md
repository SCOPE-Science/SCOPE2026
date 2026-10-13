# All k-limited dominating sets of multipartite graphs with at least three parts

## Finding

Let
\[
G=K_{n_1,\ldots,n_r}
\]
be a connected complete multipartite graph with
\[
r\ge3,\qquad N=\sum_{i=1}^r n_i,
\]
and let
\[
1\le k<\Delta(G).
\]
For a vertex set \(D\subseteq V(G)\), write
\[
S=\{i:D\cap V_i\ne\varnothing\},\qquad
d_i=|D\cap V_i|,\qquad
y_i=n_i-d_i.
\]

Then \(D\) is a \(k\)-limited dominating set if and only if exactly one of the following alternatives holds.

If
\[
S=\{i\},
\]
then
\[
D=V_i
\]
and
\[
N-n_i\le k.
\]

If
\[
|S|\ge2,
\]
then, for every \(i\in S\),
\[
\sum_{j\notin S}n_j
+
\sum_{h\in S\setminus\{i\}}y_h
\le k.
\]

Thus, for support of size at least two, the entire condition is a family of linear inequalities on the numbers of omitted vertices.

Define the cardinality enumerator
\[
L_k(G;x)
=
\sum_{D\text{ \(k\)-limited dominating}}x^{|D|}.
\]
For
\[
B_S=\sum_{j\notin S}n_j,
\]
one has
\[
\boxed{
L_k(G;x)
=
\sum_{\substack{i\\N-n_i\le k}}x^{n_i}
+
\sum_{\substack{S\subseteq[r]\\|S|\ge2}}
\ \sum_{\substack{
0\le y_i\le n_i-1\ (i\in S)\\
B_S+\sum_{h\in S\setminus\{i\}}y_h\le k\ \forall i\in S
}}
\left(\prod_{i\in S}\binom{n_i}{y_i}\right)
x^{N-B_S-\sum_{i\in S}y_i}.
}
\]

The same inequalities give an exact support formula for the minimum. For a fixed support
\[
S\subseteq[r],\qquad |S|=s\ge2,
\]
assume
\[
B_S\le k
\]
and put
\[
K_S=k-B_S,
\]
\[
C_S=\sum_{i\in S}(n_i-1),
\qquad
c_S=\min_{i\in S}(n_i-1).
\]
Define
\[
Y_S
=
\min\left\{
C_S,\,
K_S+c_S,\,
\left\lfloor\frac{sK_S}{s-1}\right\rfloor
\right\}.
\]
Then the smallest \(k\)-limited dominating set with support exactly \(S\) has size
\[
N-B_S-Y_S.
\]
Consequently
\[
\boxed{
\gamma_k^{\mathrm L}(G)
=
\min\left(
\{n_i:N-n_i\le k\}
\cup
\{N-B_S-Y_S:|S|\ge2,\ B_S\le k\}
\right).
}
\]

## Assumptions and scope

All graphs are finite, simple, undirected, and connected. The graph has at least three nonempty partite classes. A set \(D\) is \(k\)-limited dominating when it is dominating and every vertex \(v\in D\) has at most \(k\) neighbors in
\[
V(G)\setminus D.
\]

The theorem is stated in the nontrivial range
\[
1\le k<\Delta(G),
\]
matching the range emphasized in the initiating paper. The same structural characterization remains valid for larger \(k\), where the parameter eventually reduces to ordinary domination.

The result deliberately excludes the complete-bipartite scalar minimum formula as a novelty claim: that case was already determined in the initiating paper.

## Proof

A set \(D\) dominates a complete multipartite graph exactly when either it meets at least two partite classes or it is one entire partite class.

Indeed, if \(D\) meets at least two parts, every vertex outside \(D\) is adjacent to every selected vertex lying outside its own part, so it is dominated. If \(D\) lies inside one part \(V_i\), an omitted vertex of \(V_i\) has no neighbor in \(D\); hence domination in this one-part case forces
\[
D=V_i.
\]

Suppose first that
\[
D=V_i.
\]
Every selected vertex is adjacent to all
\[
N-n_i
\]
vertices outside \(V_i\), all of which lie outside \(D\). Hence the \(k\)-limited condition is exactly
\[
N-n_i\le k.
\]

Now assume
\[
|S|\ge2.
\]
Fix a selected vertex \(v\in D\cap V_i\). Its neighbors outside \(D\) are precisely the omitted vertices lying outside \(V_i\). There are
\[
\sum_{j\notin S}n_j
+
\sum_{h\in S\setminus\{i\}}y_h
\]
such vertices. Therefore the defining condition
\[
|N(v)\setminus D|\le k
\]
is exactly the displayed inequality for \(i\). Vertices in the same part have identical neighborhoods, so one inequality per occupied part is sufficient. This proves the all-set characterization.

For the enumerator, fix a support \(S\) of size at least two and fixed omission counts
\[
0\le y_i\le n_i-1
\qquad(i\in S)
\]
satisfying the inequalities. Every part outside \(S\) is wholly omitted. Inside part \(V_i\), the omitted set can be chosen in
\[
\binom{n_i}{y_i}
\]
ways. The resulting dominating set has size
\[
N-B_S-\sum_{i\in S}y_i.
\]
Multiplying these independent choices and summing over all feasible supports and omission vectors gives the polynomial. The one-part feasible sets contribute the first sum.

It remains to prove the closed support minimum. Fix
\[
S,\qquad |S|=s\ge2.
\]
Write
\[
Y=\sum_{i\in S}y_i.
\]
The support inequalities become
\[
B_S+Y-y_i\le k,
\]
or, after putting
\[
K_S=k-B_S,
\]
\[
Y-y_i\le K_S
\qquad(i\in S).
\]
Thus \(B_S\le k\) is necessary.

The upper bounds on \(Y\) are immediate. Since
\[
y_i\le n_i-1,
\]
one has
\[
Y\le C_S.
\]
Also
\[
y_i\ge Y-K_S,
\]
so using a part with the smallest capacity gives
\[
Y\le K_S+c_S.
\]
Finally, summing
\[
Y-y_i\le K_S
\]
over all \(i\in S\) yields
\[
(s-1)Y\le sK_S,
\]
hence
\[
Y\le
\left\lfloor\frac{sK_S}{s-1}\right\rfloor.
\]

Therefore
\[
Y\le Y_S.
\]

Conversely, take
\[
Y=Y_S
\]
and set
\[
\ell=\max\{0,Y-K_S\}.
\]
The bound
\[
Y\le K_S+c_S
\]
gives
\[
\ell\le c_S\le n_i-1
\]
for every \(i\in S\). If \(Y>K_S\), the bound
\[
(s-1)Y\le sK_S
\]
is equivalent to
\[
s\ell\le Y;
\]
if \(Y\le K_S\), this also holds because \(\ell=0\). Finally
\[
Y\le C_S
\]
ensures enough total upper capacity. Hence there exist integers
\[
y_i\in[\ell,n_i-1]
\]
summing to \(Y\). For every \(i\),
\[
Y-y_i\le Y-\ell\le K_S,
\]
so this omission vector is feasible. Thus \(Y_S\) is exactly the maximum number of omitted vertices inside the occupied parts.

The smallest set with support \(S\) therefore has
\[
N-B_S-Y_S
\]
vertices. Taking the minimum over feasible supports and the feasible one-part sets proves the formula for
\[
\gamma_k^{\mathrm L}(G).
\]

## Verification

The accompanying script `artifacts/verify.py` enumerates every nondecreasing complete-multipartite part profile of total order \(3\) through \(9\) having at least three parts. For each profile it checks every integer
\[
1\le k<\Delta(G)
\]
and every vertex subset.

The direct test constructs adjacency, checks domination, and verifies from neighborhoods that every selected vertex has at most \(k\) neighbors outside the set. Independently, it checks the support/omission characterization, computes the complete coefficient sequence from the displayed enumerator, and evaluates the support formula for the minimum.

Replay output:

`ALL CHECKS PASSED; profiles=67; parameter_cases=367; subset_checks=121480; orders=3..9`

The finite computation is corroborative only. The arbitrary-order theorem is proved analytically above.

## Relationship to prior work

Božović, Radić, Kovijanić-Vukićević, and Tepeh introduced \(k\)-limited domination in 2026. Their first public preprint appeared on June 21, 2026. The later open-access journal version lists Mathematics Subject Classification \(05C69\) first, followed by \(05C70\).

Their Proposition 1 determines the parameter for paths, stars, complete graphs, and complete bipartite graphs. In particular, for
\[
2\le m\le n
\]
it gives the exact scalar value of
\[
\gamma_k^{\mathrm L}(K_{m,n}).
\]
The searchable full text contains no complete-multipartite theorem. The result here starts at three partite classes and gives substantially more information: every feasible set, every cardinality coefficient, and an exact fixed-support optimization formula.

The same paper observes that \(k\)-limited domination is the
\[
(0,k)
\]
case of pitchfork domination, while existing pitchfork-domination work concentrates on positive lower load, especially the
\[
(1,2)
\]
case. Targeted searches under the pitchfork terminology did not locate a complete-multipartite
\[
(0,k)
\]
classification.

A recent follow-up studies complexity and Sierpiński graphs, not complete multipartite graphs. A nearby published-result database record treats \(k\)-limited packing of complete multipartite graphs, but limited packing constrains closed-neighborhood intersections of the packed set and is a different invariant from capacity-limited domination.

## Limitations

The theorem is restricted to complete multipartite graphs with at least three parts. Although the same support inequalities can be specialized to two parts, the scalar complete-bipartite minimum is prior work and is not claimed as new here.

The displayed minimum formula is exact but involves optimization over supports \(S\subseteq[r]\); no claim is made that the best support can always be chosen from a smaller predetermined family.

The originality assessment is literature-based. The equivalent
\[
(0,k)
\]
pitchfork terminology was searched explicitly, but older pitchfork papers often emphasize
\[
(1,2)
\]
variants, so poorly indexed equivalent work remains a residual risk.

## References

1. D. Božović, G. Radić, Ž. Kovijanić-Vukićević, and A. Tepeh, “On \(k\)-limited domination in graphs,” arXiv:2606.22422v1, first public June 21, 2026; Computational and Applied Mathematics 46 (2027), article 43, DOI 10.1007/s40314-026-03902-2.
2. M. A. Abdlhusein and M. N. Al-Harere, “Pitchfork Domination and It's Inverse for Corona and Join Operations in Graphs,” Proceedings of International Mathematical Sciences 1(2) (2019).
3. D. Božović, “On \(k\)-limited domination: complexity and Sierpiński graphs,” arXiv:2610.01584v1, October 1, 2026.
