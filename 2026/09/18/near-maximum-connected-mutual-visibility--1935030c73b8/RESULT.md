# Near-maximum connected mutual visibility and sharp co-connected Nordhaus--Gaddum bounds

## Result

Let \(G\) be a finite connected non-complete simple graph of order \(n\ge 3\), and let
\(\mu_c(G)\) denote its connected mutual-visibility number.

### Theorem 1 (the \(n-1\) level)

The following are equivalent.

1. \(\mu_c(G)=n-1\).
2. There is a vertex \(x\in V(G)\) such that \(G-x\) is connected and every vertex
   non-adjacent to \(x\) is universal in \(G-x\).
3. There is a vertex \(x\in V(G)\) such that \(G-x\) is connected and the component
   of \(x\) in \(\overline G\) is a star centered at \(x\) (with \(K_1\) allowed as
   the degenerate star).

Equivalently, the connected mutual-visibility sets of cardinality \(n-1\) are
exactly the sets \(V(G)\setminus\{x\}\) whose omitted vertex satisfies conditions
2 and 3.

### Corollary 2 (co-connected Nordhaus--Gaddum bounds)

If \(n\ge 4\) and both \(G\) and \(\overline G\) are connected, then
\[
\boxed{\mu_c(G)+\mu_c(\overline G)\le 2n-4}
\]
and
\[
\boxed{\mu_c(G)\mu_c(\overline G)\le (n-2)^2}.
\]
Both bounds are sharp for every \(n\ge4\).

These improve, under the natural co-connected hypothesis, the general bounds
\(2n-3\) and \((n-1)(n-2)\) proved by Tonny K B and Shikhi M.

## Proof of Theorem 1

Assume first that \(\mu_c(G)=n-1\). Let
\[
S=V(G)\setminus\{x\}
\]
be a connected mutual-visibility set of cardinality \(n-1\). By definition,
\(G[S]=G-x\) is connected.

Take two non-adjacent vertices \(u,v\in S\). Since \(S\) contains every vertex
except \(x\), an \(S\)-avoiding geodesic from \(u\) to \(v\) can have no internal
vertex other than \(x\). Because \(u\) and \(v\) are non-adjacent, that geodesic
must therefore be
\[
u-x-v.
\]
Hence
\[
uv\notin E(G),\quad u,v\ne x
\quad\Longrightarrow\quad
ux,vx\in E(G). \tag{1}
\]

Now let \(z\ne x\) be non-adjacent to \(x\). If \(z\) failed to be universal in
\(G-x\), there would be \(y\notin\{x,z\}\) with \(zy\notin E(G)\). Applying (1)
to \(z,y\) would imply \(zx\in E(G)\), a contradiction. Thus every non-neighbour
of \(x\) is universal in \(G-x\), proving condition 2.

Conversely, suppose condition 2 holds, and put \(S=V(G)\setminus\{x\}\).
The graph \(G[S]\) is connected. If \(u,v\in S\) are non-adjacent, neither can be
a non-neighbour of \(x\), because every such vertex is universal in \(G-x\).
Therefore both \(u\) and \(v\) are adjacent to \(x\), and
\[
u-x-v
\]
is a geodesic of length two whose internal vertex lies outside \(S\). Adjacent
pairs are automatically visible. Hence \(S\) is a connected mutual-visibility
set, so \(\mu_c(G)\ge n-1\). Since \(G\) is non-complete, the known extremal
characterization \(\mu_c(G)=n\iff G=K_n\) gives \(\mu_c(G)=n-1\).

It remains to identify the complement formulation. A vertex \(z\ne x\) is a
non-neighbour of \(x\) in \(G\) exactly when \(xz\in E(\overline G)\). Condition
2 says that every such \(z\) has no neighbour in \(\overline G-x\). Thus every
neighbour of \(x\) in \(\overline G\) has degree one inside the component
containing \(x\), and there are no edges from these neighbours farther into that
component. Consequently the component of \(x\) in \(\overline G\) is precisely
a star centered at \(x\). The converse is the same argument reversed. This proves
the equivalence of conditions 2 and 3.

## Proof of Corollary 2

Suppose \(G\) and \(\overline G\) are both connected.

If \(\mu_c(G)=n-1\), Theorem 1 says that \(\overline G\) has a star component
containing a witness \(x\). Since \(\overline G\) is connected, this component
would be all of \(\overline G\), so \(\overline G\) itself would be a star.
For \(n\ge3\), the complement of a star has an isolated vertex, contradicting
the connectedness of \(G\). Hence
\[
\mu_c(G)\le n-2.
\]
Applying the same argument with \(G\) and \(\overline G\) interchanged yields
\[
\mu_c(\overline G)\le n-2.
\]
The two displayed Nordhaus--Gaddum bounds follow immediately.

## Sharpness for every order

For \(n=4\), take \(G=P_4\). Its complement is again \(P_4\), and the block
formula for connected mutual visibility gives
\[
\mu_c(G)=\mu_c(\overline G)=2=n-2.
\]

For \(n\ge5\), let \(G_n\) be obtained from \(K_{2,n-3}\), with the part of size
two written \(\{u,v\}\), by adjoining a new leaf \(w\) adjacent to \(u\).
The graph \(G_n\) is connected. Its blocks are \(K_{2,n-3}\) and the bridge
\(uw\). The known complete-bipartite formula gives
\[
\mu_c(K_{2,n-3})=n-2,
\]
while \(\mu_c(K_2)=2\). By block locality,
\[
\mu_c(G_n)=n-2.
\]

The complement has a particularly simple form:
\[
\overline{G_n}
\]
is a clique \(K_{n-2}\) with a path of length two attached to one clique vertex.
Indeed, if \(A\) is the \((n-3)\)-vertex part of the original complete bipartite
graph, then \(A\cup\{w\}\) induces \(K_{n-2}\), and the remaining vertices form
the continuation \(w-v-u\). Hence the blocks of \(\overline{G_n}\) are
\(K_{n-2}\) and two copies of \(K_2\), so again by block locality,
\[
\mu_c(\overline{G_n})=n-2.
\]
Thus \(G_n\) and its complement are both connected and attain simultaneously
\[
\mu_c(G_n)+\mu_c(\overline{G_n})=2n-4,
\qquad
\mu_c(G_n)\mu_c(\overline{G_n})=(n-2)^2.
\]

## Context and originality

Tonny K B and Shikhi M introduced connected mutual visibility in
arXiv:2609.18877 (submitted 16 September 2026). Their Theorem 7 proves, for
graphs of order \(n\ge4\),
\[
\mu_c(G)+\mu_c(\overline G)\le2n-3,\qquad
\mu_c(G)\mu_c(\overline G)\le(n-1)(n-2),
\]
and shows that the pair \((n-1,n-1)\) cannot occur. Their paper also proves the
block-local formula for \(\mu_c\) and the complete multipartite formulas used in
the sharpness construction above.

The source paper's full available text was inspected, including its
Nordhaus--Gaddum proof and conclusion. It does not state a characterization of
the \(n-1\) level by complement components, nor the co-connected bounds above.
Searches for connected mutual visibility together with \(n-1\), co-connected
graphs, connected complements, star components, and the bound \(2n-4\) found no
prior statement of these results. Since the parameter was introduced only very
recently, originality is necessarily asserted only to the best of our knowledge;
very recent or unindexed parallel work is the main residual risk.

## Limitations

The result treats the near-maximum level \(n-1\) and the co-connected
Nordhaus--Gaddum regime. It does not characterize graphs with
\(\mu_c(G)=n-2\), and it does not classify all equality cases in the sharpened
co-connected bounds. No claim is made about other mutual-visibility variants.

## References

1. Tonny K B and Shikhi M, *Connected Mutual-Visibility in Graphs*,
   arXiv:2609.18877, 2026. https://arxiv.org/abs/2609.18877
2. G. Di Stefano, *Mutual visibility in graphs*, Applied Mathematics and
   Computation 419 (2022), 126850.
