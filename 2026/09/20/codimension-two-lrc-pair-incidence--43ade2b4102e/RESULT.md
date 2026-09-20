# Exact codimension-two LRC distance criteria from pair-incidence covers

## Statement

For an all-symbol linear locally recoverable code (LRC), write
\[
k_1=\left\lceil\frac{k}{r}\right\rceil,\qquad
k_2=k_1r-k,
\]
\[
n_1=\left\lceil\frac{n}{r+1}\right\rceil,\qquad
n_2=n_1(r+1)-n,
\]
and
\[
d^*=n-k-\left\lceil\frac{k}{r}\right\rceil+2.
\]
Assume throughout this result that
\[
n_1-k_1=2,
\]
and put \(q=n_2-k_2\).

Define \(\mu_q(N)\) to be the minimum number of edges in a loopless multigraph on \(N\) vertices such that every pair of distinct vertices is incident with at least \(q\) edges in total, where an edge joining the two chosen vertices is counted once.

The following values are exact for \(N\ge 3\):
\[
\mu_1(N)=\left\lfloor\frac N2\right\rfloor,
\qquad
\mu_2(N)=\left\lceil\frac{2N}{3}\right\rceil,
\qquad
\mu_4(N)=\left\lceil\frac{6N}{5}\right\rceil.
\]
More generally, if \(q=2h+1\ge3\) is odd and \(N\ge h+2\) (equivalently \(q\le2N-3\)), then
\[
\boxed{\mu_q(N)=\left\lceil\frac{(h+1)N}{2}\right\rceil
      =\left\lceil\frac{(q+1)N}{4}\right\rceil.}
\]

Consequently, when \(n_1-k_1=2\), the largest minimum distance satisfies
\[
D(n,k,r)=d^* \quad\Longleftrightarrow\quad n_2\ge \mu_{n_2-k_2}(n_1)
\]
for the solved values above. In particular, for odd \(q=n_2-k_2\ge3\) with \(q\le2n_1-3\),
\[
\boxed{
D(n,k,r)=
\begin{cases}
d^*,& n_2\ge \left\lceil\dfrac{(q+1)n_1}{4}\right\rceil,\\[5pt]
d^*-1,& n_2< \left\lceil\dfrac{(q+1)n_1}{4}\right\rceil.
\end{cases}}
\]
For \(q=2\) and \(q=4\), replace the threshold respectively by \(\lceil2n_1/3\rceil\) and \(\lceil6n_1/5\rceil\); for \(q=1\), the threshold is \(\lfloor n_1/2\rfloor\).

A simple infinite consequence is that for every integer \(N\ge5\),
\[
\boxed{D(N^2+N-1,\,N(N-2),\,N+1)=2N+3.}
\]
For this family, \((n_1,k_1,n_2,k_2)=(N,N-2,N+1,N-2)\), so \(q=3\), and the sharp threshold is \(n_2\ge n_1\).

## Proof

Khabbazian and Médard proved that \(D(n,k,r)=d^*\) if and only if there is a loopless multigraph \(G\) with \(n_1\) vertices and \(n_2\) edges such that every \(k_1\)-vertex subgraph has at most \(k_2\) edges. Here \(k_1=n_1-2\). Thus, for every pair \(u,v\), the induced graph on the other \(n_1-2\) vertices must contain at most \(k_2\) edges.

If \(G\) has \(M=n_2\) edges, let
\[
c_G(u,v)=d(u)+d(v)-m(u,v),
\]
where \(m(u,v)\) is the multiplicity of the edge \(uv\). This is exactly the number of edges incident with at least one of \(u,v\). Therefore
\[
|E(G[V\setminus\{u,v\}])|=M-c_G(u,v).
\]
The LRC condition is consequently equivalent to
\[
c_G(u,v)\ge M-k_2=n_2-k_2=q
\]
for every distinct \(u,v\). Hence an admissible graph of size \(n_2\) exists exactly when \(n_2\ge\mu_q(n_1)\): once a graph with \(\mu_q(n_1)\) edges is available, arbitrary additional edges cannot decrease any \(c_G(u,v)\).

### Odd \(q\ge3\)

Write \(q=2h+1\), and let \(G\) be any loopless multigraph on \(N\) vertices satisfying \(c_G(u,v)\ge q\) for every pair. Choose a vertex \(u\) of minimum degree \(a\). If \(a\ge h+1\), the handshake lemma gives
\[
2|E(G)|\ge(h+1)N.
\]
If \(a\le h\), then for every \(v\ne u\),
\[
d(v)\ge q-a+m(u,v).
\]
Summing over \(v\ne u\), using \(\sum_{v\ne u}m(u,v)=a\), and then adding \(d(u)=a\), gives
\[
2|E(G)|\ge 2a+(N-1)(2h+1-a).
\]
For \(N\ge3\), the right side is minimized over \(0\le a\le h\) at \(a=h\), where it equals
\[
(h+1)N+h-1\ge(h+1)N.
\]
Thus every such multigraph has at least \(\lceil(h+1)N/2\rceil\) edges.

For the matching construction, set
\[
M=\left\lceil\frac{(h+1)N}{2}\right\rceil.
\]
Because \(N\ge h+2\), we have \(h+1\le N-1\). There exists a simple \(N\)-vertex graph with \(M\) edges whose degrees differ by at most one: among all simple graphs with \(M\) edges, choose one minimizing the sum of squared degrees; an edge transfer from a vertex whose degree exceeds another by at least two strictly lowers that sum, a contradiction. Its minimum degree is therefore at least \(h+1\). For adjacent vertices,
\[
c_G(u,v)=d(u)+d(v)-1\ge2(h+1)-1=2h+1,
\]
and for nonadjacent vertices the bound is larger. Hence the lower bound is attained.

### The cases \(q=1,2,4\)

For \(q=1\), fewer than \(\lfloor N/2\rfloor\) edges leave at least two vertices isolated, while a matching of size \(\lfloor N/2\rfloor\) leaves at most one isolated vertex. Hence \(\mu_1(N)=\lfloor N/2\rfloor\).

For \(q=2\), an isolated vertex forces every other vertex to have degree at least two, already giving at least \(N-1\) edges. Otherwise let \(A\) be the number of degree-one vertices. No two degree-one vertices can be adjacent, so all their incident edges run to vertices of degree at least two. Thus
\[
|E(G)|\ge A,
\qquad
2|E(G)|\ge A+2(N-A)=2N-A.
\]
Therefore \(|E(G)|\ge\lceil2N/3\rceil\). Equality is attained by disjoint unions of paths \(P_3\), with one \(P_4\) or \(P_5\) used to handle the two nonzero residues modulo three.

For \(q=4\), if the minimum degree is at most one, the same pair-sum inequality used above already yields at least \(\lceil6N/5\rceil\) edges. Otherwise let \(A\) be the number of degree-two vertices. Two degree-two vertices cannot be adjacent, so their \(2A\) edge incidences all go to vertices of degree at least three. Hence
\[
|E(G)|\ge2A,
\qquad
2|E(G)|\ge2A+3(N-A)=3N-A.
\]
Taking the larger of these two bounds gives \(|E(G)|\ge\lceil6N/5\rceil\).

The bound is attained for all \(N\ge3\). Use disjoint copies of \(K_{2,3}\) for blocks of five vertices. Residues are handled by the following sharp blocks: on three vertices, a triangle with one doubled edge (four edges); on four vertices, \(K_4\) minus one edge (five edges); on six vertices, \(K_{2,4}\) (eight edges); and on seven vertices, take a path \(x_0x_1x_2x_3\) together with three degree-two vertices \(a,b,c\) and cross edges
\[
a x_0,a x_3,b x_0,b x_1,c x_2,c x_3.
\]
The seven-vertex block has nine edges. Each listed block has minimum pair-incidence at least four, and disjoint unions preserve this because every vertex in these blocks has degree at least two.

Finally, the general LRC lower alternative is \(d^*-1\), so failure of the graph criterion gives the displayed exact piecewise value of \(D(n,k,r)\).

## Context and significance

Khabbazian and Médard reduce the LMD problem to an exact extremal multigraph condition. Their paper gives a complete formula when \(n_1-k_1=1\), and explicitly remarks that similar tools may extend to \(n_1-k_1\le3\), but it does not state an exact formula for the codimension-two case. The result above supplies such a formula for every feasible odd incidence gap and for the first two positive even gaps.

The infinite family
\[
[n,k,r]=[N^2+N-1,\,N(N-2),\,N+1],\qquad N\ge5,
\]
lies outside the exact parameter cases enumerated in the same paper: it has \(n_2=n_1+1\), \(k_2=k_1\), and \(n_1-k_1=2\). Thus it is not covered by the cases \(n_2\le n_1\), \(k_2<k_1-1\), \(k_2=k_1-1\), or \(n_1-k_1=1\); nor does it satisfy the earlier divisibility/residue sufficient conditions summarized there.

## Limitations

The closed form for arbitrary odd \(q\ge3\) assumes \(q\le2N-3\), exactly the range in which the matching construction can be simple with minimum degree \((q+1)/2\). Larger odd gaps and general even gaps beyond \(q=4\) are not settled here. The LRC conclusion concerns the unrestricted-field linear LMD problem used in the cited work; it does not impose a fixed alphabet size. Originality is to the best of our knowledge. The pair-incidence extremal lemma is elementary and could exist under another graph-invariant terminology; the main originality claim is the exact codimension-two LRC criterion and its resulting parameter families.

## Reproducibility

`artifacts/verify.py` constructs the sharp graphs for the solved cases over a finite test range, checks their pair-incidence constraints and edge counts, and verifies the displayed infinite-family parameter identities over sample values.

## References

1. M. Khabbazian and M. Médard, *On finding the largest minimum distance of locally recoverable codes: A graph theory approach*, Discrete Mathematics 348 (2025), 114298. DOI: 10.1016/j.disc.2024.114298. The paper is the journal development of the 2018 preprint arXiv:1809.09227.
2. A. Wang and Z. Zhang, *An Integer Programming-Based Bound for Locally Repairable Codes*, IEEE Transactions on Information Theory 61 (2015), 5280-5294. DOI: 10.1109/TIT.2015.2472515.
