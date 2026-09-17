# Near-maximum connected mutual visibility and Nordhaus--Gaddum equality

## Definitions

For a finite simple graph \(G\), a set \(S\subseteq V(G)\) is a connected mutual-visibility set if \(G[S]\) is connected and, for every two distinct \(u,v\in S\), there is a \(u,v\)-geodesic whose internal vertices avoid \(S\). Write \(\mu_c(G)\) for the maximum size of such a set.

For disconnected graphs we use the natural extension of the same definition. Every connected mutual-visibility set lies in one connected component, so for a disjoint union \(G=G_1\cup\cdots\cup G_t\),
\[
\mu_c(G)=\max_i \mu_c(G_i).
\]

## Near-maximum characterization

**Theorem 1.** Let \(G\) be a noncomplete graph of order \(n\ge 3\). Then
\[
\boxed{\mu_c(G)=n-1}
\]
if and only if there is a vertex \(x\in V(G)\) such that

1. \(G-x\) is connected; and
2. every vertex \(y\in N_{\overline G}(x)\) has degree \(1\) in \(\overline G\).

Equivalently, every nonneighbor \(y\) of \(x\) in \(G\) is adjacent in \(G\) to every vertex of \(V(G)\setminus\{x,y\}\).

### Proof

Suppose first that \(\mu_c(G)=n-1\), and let
\[
S=V(G)\setminus\{x\}
\]
be a connected mutual-visibility set. Then \(G-x=G[S]\) is connected.

Let \(y\in N_{\overline G}(x)\), so \(xy\notin E(G)\). We claim that \(y\) is adjacent in \(G\) to every vertex of \(S\setminus\{y\}\). If not, choose \(z\in S\setminus\{y\}\) with \(yz\notin E(G)\). Since \(y,z\in S\) are nonadjacent, an \(S\)-avoiding \(y,z\)-geodesic must have all internal vertices in
\[
V(G)\setminus S=\{x\}.
\]
Thus the geodesic would have to be \(y-x-z\), which is impossible because \(xy\notin E(G)\). Hence \(y\) is adjacent to every vertex of \(S\setminus\{y\}\), so its only neighbor in \(\overline G\) is \(x\). Therefore
\[
d_{\overline G}(y)=1.
\]

Conversely, suppose that a vertex \(x\) satisfies the two stated conditions, and put
\[
S=V(G)\setminus\{x\}.
\]
By assumption, \(G[S]\) is connected. Let \(u,v\in S\) be distinct. If \(uv\in E(G)\), then the edge \(uv\) itself witnesses visibility. If \(uv\notin E(G)\), neither \(u\) nor \(v\) can lie in \(N_{\overline G}(x)\): indeed, a vertex in \(N_{\overline G}(x)\) has no neighbor in \(\overline G\) other than \(x\), whereas \(uv\) would be another complement edge. Hence
\[
xu,xv\in E(G).
\]
Since \(u\) and \(v\) are nonadjacent, \(u-x-v\) is a geodesic of length \(2\), and its only internal vertex lies outside \(S\). Thus \(S\) is a connected mutual-visibility set, so
\[
\mu_c(G)\ge n-1.
\]
Because \(G\) is not complete, \(\mu_c(G)\le n-1\), proving equality. \(\square\)

## Complement decomposition

The criterion has a useful equivalent form. For a witnessing vertex \(x\), let
\[
r=d_{\overline G}(x).
\]
All vertices of \(N_{\overline G}(x)\) are leaves of \(\overline G\), so the connected component of \(\overline G\) containing \(x\) is a star \(K_{1,r}\), with \(x\) as its center. Therefore
\[
\boxed{\overline G=K_{1,r}\cup Q}
\tag{1}
\]
for some graph \(Q\) on \(n-r-1\) vertices. If \(r\ge1\), then \(G-x\) is automatically connected because every leaf of this complement star is universal in \(G-x\). If \(r=0\), condition 1 of Theorem 1 is exactly that
\[
\overline Q=G-x
\]
is connected.

A direct consequence is the following.

**Corollary 2.** If \(G\) and \(\overline G\) are both connected and \(n\ge3\), then
\[
\mu_c(G)\le n-2
\qquad\text{and}\qquad
\mu_c(\overline G)\le n-2.
\]

**Proof.** If \(\mu_c(G)=n-1\), then (1) gives a star component of \(\overline G\). Since \(\overline G\) is connected, that star must contain every vertex, so
\[
\overline G\cong K_{1,n-1}.
\]
But then
\[
G\cong K_{n-1}\cup K_1,
\]
contrary to the connectedness of \(G\). The complementary statement follows symmetrically. \(\square\)

## Equality cases in the Nordhaus--Gaddum bounds

Tonny and Shikhi proved that, for every graph \(G\) of order \(n\ge4\),
\[
\mu_c(G)+\mu_c(\overline G)\le 2n-3
\tag{2}
\]
and
\[
\mu_c(G)\mu_c(\overline G)\le (n-1)(n-2),
\tag{3}
\]
and showed that both bounds are sharp. Their proof does not classify all equality cases.

For \(n\ge5\), the equality graphs admit a complete classification.

**Theorem 3.** Let \(G\) be a graph of order \(n\ge5\). The following are equivalent:

1. \(\mu_c(G)+\mu_c(\overline G)=2n-3\);
2. \(\mu_c(G)\mu_c(\overline G)=(n-1)(n-2)\);
3. up to replacing \(G\) by its complement,
   \[
   \boxed{G\cong K_{2,n-2}}
   \qquad\text{or}\qquad
   \boxed{G\cong K_2\vee\overline K_{n-2}}.
   \]

Equivalently, the four labeled isomorphism families are
\[
K_{2,n-2},\quad
K_2\vee\overline K_{n-2},\quad
K_2\cup K_{n-2},\quad
2K_1\cup K_{n-2}.
\]

In every equality case,
\[
\{\mu_c(G),\mu_c(\overline G)\}=\{n-1,n-2\}.
\]

### Proof

For \(n\ge5\), if \(G\) is complete or edgeless then
\[
\{\mu_c(G),\mu_c(\overline G)\}=\{n,1\},
\]
which gives neither equality in (2) nor in (3). In all other cases, the bounds of Tonny and Shikhi imply that at least one of the two parameters is at most \(n-2\), while both are at most \(n-1\). Hence equality in either (2) or (3) forces
\[
\{\mu_c(G),\mu_c(\overline G)\}=\{n-1,n-2\},
\tag{4}
\]
and (4) conversely yields equality in both bounds.

Assume without loss of generality that
\[
\mu_c(G)=n-1,\qquad \mu_c(\overline G)=n-2.
\]
By Theorem 1, for some vertex \(x\),
\[
\overline G=K_{1,r}\cup Q,
\tag{5}
\]
where the star is centered at \(x\), and
\[
|V(Q)|=n-r-1.
\]
The connected mutual-visibility number of a nontrivial star is \(2\), while \(\mu_c(K_1)=1\). Since \(n\ge5\), we have \(n-2\ge3\). Therefore (5) and the disjoint-union rule give
\[
\mu_c(Q)=n-2.
\]
In particular,
\[
|V(Q)|\ge n-2,
\]
so \(r\le1\).

### Case 1: \(r=1\)

Then \(|V(Q)|=n-2\) and
\[
\mu_c(Q)=|V(Q)|.
\]
The only graph whose entire vertex set is a connected mutual-visibility set is a complete graph: if two vertices were nonadjacent, every geodesic between them would have an internal vertex belonging to the full vertex set. Hence
\[
Q\cong K_{n-2}.
\]
Thus
\[
\overline G\cong K_2\cup K_{n-2},
\]
and therefore
\[
G\cong K_{2,n-2}.
\]

### Case 2: \(r=0\)

Now
\[
\overline G=K_1\cup Q,
\qquad |V(Q)|=n-1,
\qquad \mu_c(Q)=n-2=|V(Q)|-1.
\]
Since \(r=0\), Theorem 1 also gives that
\[
G-x=\overline Q
\]
is connected.

Apply Theorem 1 to the noncomplete graph \(Q\). There is a vertex \(y\in V(Q)\) such that every neighbor of \(y\) in \(\overline Q\) is a leaf of \(\overline Q\). But \(\overline Q\) is connected. Hence the star component centered at \(y\) must be all of \(\overline Q\), and therefore
\[
\overline Q\cong K_{1,n-2}.
\]
Consequently
\[
Q\cong K_{n-2}\cup K_1,
\]
so
\[
\overline G\cong K_{n-2}\cup 2K_1
\]
and
\[
G\cong K_2\vee\overline K_{n-2}.
\]

This proves necessity. Conversely, for \(K_{2,n-2}\), Theorem 1 gives \(\mu_c=n-1\), while its complement \(K_2\cup K_{n-2}\) has connected mutual-visibility number \(n-2\). Similarly, \(K_2\vee\overline K_{n-2}\) has \(\mu_c=n-1\), while its complement \(2K_1\cup K_{n-2}\) has \(\mu_c=n-2\). Hence both families, and their complements, attain equality in (2) and (3). \(\square\)

## Context and comparison with prior work

Tonny K B and Shikhi M introduced connected mutual visibility in *Connected Mutual-Visibility in Graphs*, arXiv:2609.18877v1 (16 September 2026). Their Proposition 2 characterizes the maximum value \(\mu_c(G)=n\), their Theorem 3 characterizes the minimum value \(2\) for connected graphs, and their Theorem 7 proves the Nordhaus--Gaddum inequalities (2)--(3) and supplies a sharpness example. The paper does not state a characterization of the second-largest value \(n-1\), nor does it classify all equality cases in the Nordhaus--Gaddum bounds.

Theorem 1 fills the first gap with a local complement criterion. Theorem 3 then turns that criterion into an exact equality classification for both Nordhaus--Gaddum inequalities when \(n\ge5\).

Searches for the exact phrase “connected mutual-visibility”, the second-largest value \(n-1\), Nordhaus--Gaddum equality cases, complete-bipartite/complement formulations, and synonymous “connected mutual visibility” wording located the introducing preprint but no prior theorem implying the results above. Since the parameter was introduced only in September 2026, very recent or not-yet-indexed parallel work remains a residual originality risk.

## Limitations

The equality classification in Theorem 3 is stated for \(n\ge5\). The order-\(4\) boundary has additional equality cases caused by the small numerical coincidences in the Nordhaus--Gaddum bounds and is not classified here.

The originality claim is to the best of our knowledge. No independent validation is asserted.

## Reference

1. Tonny K B, Shikhi M, *Connected Mutual-Visibility in Graphs*, arXiv:2609.18877v1 (2026). https://arxiv.org/abs/2609.18877
