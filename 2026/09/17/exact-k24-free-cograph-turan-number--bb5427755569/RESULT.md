# Exact \(K_{2,4}\)-free Turán number for cographs

**Same-model review: passed. Cross-model review: not yet performed.**

## Statement

Let
\[
\operatorname{ex}_{\mathrm{cog}}(n,K_{2,4})
=\operatorname{ex}\!\left(n,\{K_{2,4},P_4\text{-ind}\}\right),
\]
the maximum number of edges in an \(n\)-vertex cograph containing no \(K_{2,4}\) as a (not necessarily induced) subgraph. Write
\[
n-1=4q+r,\qquad 0\le r\le 3.
\]

**Theorem.** For every \(n\ge 1\),
\[
\boxed{\operatorname{ex}_{\mathrm{cog}}(n,K_{2,4})
=(n-1)+6q+\binom r2.}
\]

The extremal graphs are classified up to isomorphism as follows.

- For \(1\le n\le 5\), the unique extremal graph is \(K_n\).
- For \(n=6\), there are exactly two extremal graphs:
  \[
  K_1\vee(K_4\cup K_1)
  \quad\text{and}\quad
  (K_2\cup K_1)\vee(K_2\cup K_1).
  \]
- For every \(n\ge 7\), the unique extremal graph is
  \[
  K_1\vee(qK_4\cup K_r),
  \]
  where \(K_0\) is omitted.

Here \(\vee\) denotes graph join and \(\cup\) denotes disjoint union.

## Proof

Define, for \(m\ge0\),
\[
\phi(m)=6\left\lfloor\frac m4\right\rfloor
+\binom{m\bmod4}{2}.
\]
Equivalently, \(\phi(m)\) is the largest number of edges in a disjoint union of cliques of order at most \(4\) on \(m\) vertices. Indeed, replacing two parts \(a\le b<4\) by \(a-1,b+1\) (when \(a>0\)) increases the sum of the binomial edge counts, so all but at most one nonempty part have order \(4\). Put
\[
f(n)=n-1+\phi(n-1).
\]

### 1. Construction

Let \(H=qK_4\cup K_r\), so \(|H|=n-1\), and let
\[
G=K_1\vee H.
\]
Write \(v\) for the vertex of the \(K_1\).

For a pair \(v,x\) with \(x\in H\), the common neighbors of \(v\) and \(x\) are exactly the neighbors of \(x\) in \(H\), of which there are at most \(3\). For a pair \(x,y\in H\), their common neighbors in \(G\) consist of \(v\) together with their common neighbors in \(H\). Two vertices of \(H\) have at most \(2\) common neighbors in \(H\): this is attained only when they lie in the same \(K_4\). Thus every pair of vertices of \(G\) has at most \(3\) common neighbors, so \(G\) is \(K_{2,4}\)-free.

Its edge count is
\[
e(G)=(n-1)+e(H)=n-1+\phi(n-1)=f(n).
\]

### 2. Connected cographs of order at least seven have a universal vertex

Let \(G\) be a connected \(K_{2,4}\)-free cograph on \(n\ge7\) vertices. A connected nontrivial cograph is a join of the children of the root of its reduced cotree. If one root factor is a singleton, its vertex is universal.

Suppose instead that \(G\) has no universal vertex. Then every root factor has at least two vertices. Let \(A\) be a smallest root factor and let \(B\) be the union of all the others. Because \(n\ge7\), we have \(|A|\ge2\) and \(|B|\ge4\). Every edge between \(A\) and \(B\) is present, so any two vertices of \(A\) together with any four vertices of \(B\) form a \(K_{2,4}\), a contradiction. Hence \(G\) has a universal vertex.

### 3. The universal-vertex case

Write \(G=K_1\vee H\), with universal vertex \(v\). Then \(G\) is \(K_{2,4}\)-free if and only if
\[
\Delta(H)\le3
\quad\text{and}\quad
H\text{ is }K_{2,3}\text{-free}.
\]
Indeed, \(v\) and \(x\in H\) have \(\deg_H(x)\) common neighbors, while two vertices \(x,y\in H\) have one common neighbor \(v\) in addition to their common neighbors in \(H\).

We claim that every connected component \(D\) of \(H\) has at most four vertices. If \(|D|\ge2\), then, since \(D\) is a connected cograph, it is a nontrivial join \(X\vee Y\). If one side is a singleton, that vertex has degree \(|D|-1\), so \(\Delta(H)\le3\) gives \(|D|\le4\). If both sides have at least two vertices and one side has at least three, the join contains a \(K_{2,3}\), impossible. Hence in the remaining case both sides have size at most two, again giving \(|D|\le4\).

Therefore
\[
e(H)\le\phi(n-1).
\]
Equality forces every component of \(H\) to be complete and the component orders to be \(4,\ldots,4,r\): for a component of order \(d\le4\), equality in \(e(D)\le\binom d2\) forces \(D=K_d\), and the convex packing argument defining \(\phi\) makes the maximizing multiset of component sizes unique. Consequently,
\[
e(G)\le f(n),
\]
with equality, in the universal-vertex case, exactly for
\[
G\cong K_1\vee(qK_4\cup K_r).
\]

Together with Step 2, this proves the bound and uniqueness for connected graphs when \(n\ge7\).

### 4. The orders \(n\le6\)

For \(n\le5\), the forbidden graph \(K_{2,4}\) has too many vertices to occur, so \(K_n\) is the unique extremal graph. Its edge count agrees with \(f(n)\).

Now let \(n=6\). In the universal-vertex case, Step 3 gives at most
\[
f(6)=5+\phi(5)=11
\]
edges, with equality only for \(K_1\vee(K_4\cup K_1)\).

Consider a connected cograph \(G\) on six vertices with no universal vertex. At the root join of its reduced cotree every factor has size at least two. Three or more factors would give a two-vertex factor joined to at least four vertices, producing \(K_{2,4}\); a \(2+4\) split does the same. Thus the only possible root split of an extremal candidate is \(3+3\), say
\[
G=A\vee B,\qquad |A|=|B|=3.
\]
If \(A\) has at least two edges, then some pair of vertices of \(A\) has a common neighbor inside \(A\); together with all three vertices of \(B\), that pair has four common neighbors in \(G\), producing \(K_{2,4}\). Hence \(e(A)\le1\), and similarly \(e(B)\le1\). Therefore
\[
e(G)\le 9+1+1=11.
\]
Equality forces \(A\cong B\cong K_2\cup K_1\). The graph
\[
(K_2\cup K_1)\vee(K_2\cup K_1)
\]
is \(K_{2,4}\)-free: a pair within one side has exactly the three vertices of the other side as common neighbors, and a cross-side pair has at most two common neighbors. This gives exactly the second extremal isomorphism type.

### 5. Disconnected graphs cannot be extremal

The function \(\phi\) is superadditive: combining optimal clique packings on \(x\) and \(y\) vertices gives an admissible clique packing on \(x+y\) vertices, so
\[
\phi(x+y)\ge\phi(x)+\phi(y).
\]
Thus for all \(a,b\ge1\),
\[
\begin{aligned}
f(a+b)-f(a)-f(b)
&=1+\phi(a+b-1)-\phi(a-1)-\phi(b-1)\\
&\ge1.
\end{aligned}
\]
Hence \(f\) is strictly superadditive. Applying the already established connected bound to each component shows that every disconnected \(K_{2,4}\)-free cograph on \(n\) vertices has strictly fewer than \(f(n)\) edges.

This completes the proof of the formula and the extremal classification. \(\square\)

## Relation to prior work

Zimmermann studies the same extremal function for general \(K_{s,t}\) on cographs. His Pumping Theorem proves eventual periodic linearity and gives the asymptotic coefficient
\[
s-1+\frac{t-1}{2}.
\]
For \((s,t)=(2,4)\), this coefficient is \(5/2\), consistent with the formula above. His all-order structural theorem for \(K_{2,t}\) is stated only for \(t\in\{2,3\}\); the paper explicitly notes that larger \(t\) can have small extremal examples without a complete vertex. The associated repository also contains dynamic-programming data for small instances, including a stored \(K_{2,4}\) data file. Those computations can establish individual finite values, but they are not a closed all-\(n\) formula or an all-\(n\) extremal classification.

The theorem here resolves the next case \(t=4\) with an elementary structural argument. Its leading term is \(5n/2\), while the exact periodic correction and the exceptional second extremal graph at \(n=6\) are determined explicitly.

## Limitations and scope

- The host class is cographs, equivalently induced-\(P_4\)-free graphs.
- \(K_{2,4}\) is forbidden as an ordinary subgraph, not as an induced subgraph.
- The result does not address unrestricted Zarankiewicz numbers.
- Originality is asserted only to the best of our knowledge within the documented search. Precomputed finite data in the closest prior source reduce the novelty of the individual small-\(n\) values; the claimed contribution is the closed formula, proof for every \(n\), and extremal classification.

## References

1. Jakob Paul Zimmermann, *Bipartite Turán problem on cographs*, arXiv:2601.07406v2 (2026), especially Theorems 1 and 3 and the accompanying discussion of larger \(t\). https://arxiv.org/abs/2601.07406v2
2. D. G. Corneil, H. Lerchs, and L. Stewart Burlingham, *Complement reducible graphs*, Discrete Applied Mathematics **3** (1981), 163–174. DOI: 10.1016/0166-218X(81)90013-5.
