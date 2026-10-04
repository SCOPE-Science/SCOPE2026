# Total and paired domination in join graphs of elementary abelian groups

## Finding

Let \(p\) be a prime and \(d\ge2\), and let \(G\cong C_p^d\). In the join graph \(\Delta(G)\), whose vertices are the nontrivial proper subgroups and where \(H\) and \(K\) are adjacent exactly when \(\langle H,K\rangle=G\), one has \[\gamma_t(\Delta(G))=d.\] Moreover, the minimum total dominating sets are exactly the \(d\)-element sets of hyperplanes with trivial intersection. Hence their number is \[N_t(p,d)=\frac{|\operatorname{GL}(d,p)|}{(p-1)^d d!}=\frac{\prod_{i=0}^{d-1}(p^d-p^i)}{(p-1)^d d!}.\] The paired-domination number is \[\gamma_{\mathrm{pr}}(\Delta(G))=\begin{cases}d,&d\text{ even},\\ d+1,&d\text{ odd}.\end{cases}\]

Thus total domination recovers the vector-space rank from the join graph in this family, while the minimum total dominating sets are precisely projective dual bases. Paired domination adds only the unavoidable parity correction.

## Assumptions and scope

Let \(p\) be prime, let \(d\ge2\), and identify
\[
G=C_p^d
\]
with the additive group of the vector space \(V=\mathbb F_p^d\). Since \(G\) is elementary abelian, its Frattini subgroup is trivial. Therefore the join graph \(\Delta(G)\) has as vertices all nonzero proper subspaces of \(V\), and distinct vertices \(A,B\) are adjacent exactly when
\[
A+B=V.
\]

A total dominating set \(D\) is a set of vertices such that every vertex, including each member of \(D\), has a neighbor in \(D\). A paired dominating set is a dominating set whose induced subgraph has a perfect matching.

## Proof

Let \(L\) be any one-dimensional subspace. If a proper subspace \(W\) is adjacent to \(L\), then \(V=L+W\). The dimension formula gives \(\dim W=d-1\), and \(L\not\subseteq W\). Thus only hyperplanes can dominate one-dimensional vertices.

Let \(D\) be a total dominating set, and let \(H_1,\ldots,H_m\) be the hyperplanes that occur in \(D\). If
\[
\bigcap_{j=1}^m H_j\ne\{0\},
\]
choose a one-dimensional subspace \(L\) inside this intersection. Then \(L\) is adjacent to none of the selected hyperplanes. It is also adjacent to none of the selected vertices of dimension at most \(d-2\), because then \(\dim(L+W)\le d-1\). Hence \(L\) would not be dominated. Therefore every total dominating set contains hyperplanes satisfying
\[
\bigcap_{j=1}^m H_j=\{0\}.
\tag{1}
\]
For hyperplanes, codimension is subadditive under intersections, so the left side of (1) has codimension at most \(m\). Since it is zero, its codimension is \(d\), giving \(m\ge d\). Thus \(\gamma_t(\Delta(G))\ge d\).

Conversely, take the \(d\) coordinate hyperplanes \(H_i=\{(x_1,\ldots,x_d):x_i=0\}\). They have trivial intersection. Any two distinct hyperplanes sum to \(V\), so they form a clique. If \(0\ne X<V\), then \(X\) cannot be contained in every \(H_i\); for some \(i\), \(X\not\subseteq H_i\), and hence \(X+H_i=V\). Therefore they totally dominate the whole graph and
\[
\gamma_t(\Delta(G))=d.
\]

The lower-bound proof also classifies equality. A total dominating set of size \(d\) must consist entirely of \(d\) hyperplanes, and their intersection must be trivial. Conversely, every \(d\)-set of hyperplanes with trivial intersection is a clique and dominates every nonzero proper subspace.

Write each hyperplane as the kernel of a nonzero functional in \(V^*\). A \(d\)-set of hyperplanes has trivial intersection exactly when the corresponding one-dimensional subspaces of \(V^*\) form a projective basis. Ordered vector bases of \(V^*\) number \(|\operatorname{GL}(d,p)|\). Passing from vectors to one-dimensional subspaces divides by \((p-1)^d\), and forgetting the order divides by \(d!\). Hence
\[
N_t(p,d)=\frac{|\operatorname{GL}(d,p)|}{(p-1)^d d!}
=\frac{\prod_{i=0}^{d-1}(p^d-p^i)}{(p-1)^d d!}.
\]

Every paired dominating set is total dominating, so it has cardinality at least \(d\), and it must have even cardinality. If \(d\) is even, any minimum total dominating set induces \(K_d\), which has a perfect matching. If \(d\) is odd, the lower bound is \(d+1\); adding any extra hyperplane to a minimum total dominating set gives \(d+1\) hyperplanes inducing \(K_{d+1}\). Thus
\[
\gamma_{\mathrm{pr}}(\Delta(G))=
\begin{cases}
d,&d\text{ even},\\
d+1,&d\text{ odd}.
\end{cases}
\]

## Verification

The standalone checker enumerates all subspaces over small finite fields by canonical row-reduced bases, builds adjacency from \(A+B=V\), and exhaustively verifies minimum total dominating sets for
\[
(p,d)\in\{(2,2),(3,2),(5,2),(2,3),(3,3),(2,4)\}.
\]
It exhaustively checks the paired minimum through rank \(3\) and constructs a minimum paired set in rank \(4\). The exact minimum-total-set counts include \(28\) for \((2,3)\), \(234\) for \((3,3)\), and \(840\) for \((2,4)\).

Exact replay output:

```text
p=2 d=2 vertices=3 hyperplanes=3 gamma_t=2 min_total_count=3 gamma_pr=2
p=3 d=2 vertices=4 hyperplanes=4 gamma_t=2 min_total_count=6 gamma_pr=2
p=5 d=2 vertices=6 hyperplanes=6 gamma_t=2 min_total_count=15 gamma_pr=2
p=2 d=3 vertices=14 hyperplanes=7 gamma_t=3 min_total_count=28 gamma_pr=4
p=3 d=3 vertices=26 hyperplanes=13 gamma_t=3 min_total_count=234 gamma_pr=4
p=2 d=4 vertices=65 hyperplanes=15 gamma_t=4 min_total_count=840 gamma_pr=4
VERIFY_OK
```

The finite tests are corroborative only. The arbitrary-\(p\), arbitrary-\(d\) result is proved by the dimension and hyperplane arguments above.

## Relationship to prior work

Ahmadi and Taeri introduced the join graph of a finite group, proved connectivity and several clique, chromatic, diameter, girth, independence, and regularity results, and classified the groups whose join graph has ordinary domination number \(1\). Their paper discusses elementary abelian groups but does not formulate total or paired domination.

Bahrami and Taeri later classified finite groups whose join graphs have ordinary domination number at most \(2\), together with small-independence cases. The accessible publisher abstract states ordinary domination and independence results; it does not state total domination, paired domination, the hyperplane-intersection characterization, or the projective-basis enumerator.

Targeted searches under “join graph”, “elementary abelian”, “hyperplane”, “total domination”, “paired domination”, “trivial intersection”, and “projective basis” did not locate the theorem above.

## Limitations

The theorem is restricted to elementary abelian groups. For a general finite group, subgroup generation is not linear span, and minimum total dominating sets need not be controlled by hyperplane intersections.

The enumeration formula classifies minimum total dominating sets only. No enumeration of all minimum paired dominating sets is claimed in odd rank.

The 2019 follow-up paper was compared through its publisher abstract because its direct publisher PDF endpoint rejected automated retrieval. This access limitation remains a residual originality risk.

## References

1. H. Ahmadi and B. Taeri, “A graph related to the join of subgroups of a finite group,” *Rendiconti del Seminario Matematico della Università di Padova* 131 (2014), 281–292. DOI: 10.4171/RSMUP/131-17.
2. Z. Bahrami and B. Taeri, “Further results on the join graph of a finite group,” *Turkish Journal of Mathematics* 43 (2019), 2097–2113. DOI: 10.3906/mat-1902-61.
