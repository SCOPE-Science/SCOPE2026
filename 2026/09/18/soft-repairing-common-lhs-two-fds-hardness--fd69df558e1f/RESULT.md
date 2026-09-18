# Soft repairing is NP-hard for two common-left functional dependencies

## Result

Consider the fixed relation schema \(R(A,B,C)\) and the two functional dependencies
\[
\Delta=\{A\to B,\ A\to C\}.
\]
Under the standard soft-repair semantics of Carmeli, Grohe, Kimelfeld, Livshits and Tibi, soft repairing for this fixed FD set is NP-hard. More strongly, the associated threshold decision problem is NP-complete even under all of the following restrictions:

- both FD weights are exactly \(1\);
- all facts have the same \(A\)-value;
- all fact-deletion weights are the same positive integer.

This resolves one of the simplest complexity cases explicitly left open in the 2024 ACM Transactions on Database Systems paper *Database Repairing with Soft Functional Dependencies*.

The proof is a reduction from CLIQUE. Its main device is a cardinality-locking identity: the two common-left FDs turn a selected database subset into a quadratic objective on the degree sequence of a bipartite incidence graph, while one uniform tuple weight forces every optimum to select exactly the full incidence stars of a prescribed number of original vertices.

## Soft-repair cost

For a database \(D\), a subset \(E\subseteq D\), tuple weights \(w_f\), and FD weights \(w_\varphi\), the soft-repair cost is
\[
\operatorname{cost}(E\mid D)
 =\sum_{f\in D\setminus E}w_f
  +\sum_{\varphi\in\Delta}w_\varphi\,|\operatorname{vio}(E,\varphi)|,
\]
where a violation is an unordered pair of facts that agree on the left-hand side of an FD and disagree on its right-hand side.

We consider the decision version asking whether there exists \(E\subseteq D\) with cost at most a supplied threshold. Membership in NP is immediate.

## Reduction

Let \((H,r)\) be a CLIQUE instance, where \(H=(V,F)\) has \(n\) vertices and \(m\ge1\) edges and \(r\ge3\). CLIQUE remains NP-hard under these harmless restrictions. Put
\[
D_0=2m+1.
\]
Construct a bipartite graph \(J\) with left side \(V\) as follows.

For every edge \(e=uv\in F\), introduce one right vertex \(c_e\) adjacent to \(u\) and \(v\). Then, for every \(v\in V\), add \(D_0-d_H(v)\) private right leaves adjacent only to \(v\). Thus every left vertex of \(J\) has degree exactly \(D_0\), while every right vertex has degree at most two.

Fix one constant \(a\). For every edge \(vc\) of \(J\), create the fact
\[
R(a,v,c).
\]
Hence the database contains exactly \(nD_0\) facts. Give both FDs unit weight and give every fact the same integer deletion weight
\[
W=\frac{(4r-1)D_0-1}{2}.
\]
This is an integer because \(D_0\) and \(4r-1\) are both odd.

## The quadratic identity

Fix a selected subset \(E\) of facts. Regard it as an edge set of \(J\), and write
\[
s=|E|,
\]
\[
x_v=d_E(v)\quad(v\in V),
\qquad
y_c=d_E(c)\quad(c\text{ on the right side}).
\]
Because all facts have the same \(A\)-value, the number of violations of \(A\to B\) is
\[
\binom{s}{2}-\sum_{v\in V}\binom{x_v}{2},
\]
and the number of violations of \(A\to C\) is
\[
\binom{s}{2}-\sum_c\binom{y_c}{2}.
\]
Therefore the total number of violations is
\[
s^2-\frac12\sum_vx_v^2-\frac12\sum_cy_c^2.
\]
Consequently
\[
\operatorname{cost}(E\mid D)
 =WnD_0-U(E),
\]
where
\[
U(E)=Ws-s^2+\frac12\sum_vx_v^2+\frac12\sum_cy_c^2.
\]

Let \(z(E)\) be the number of shared right vertices \(c_e\) having selected degree two. Since every right degree is \(0,1\), or \(2\),
\[
\sum_c y_c^2=s+2z(E).
\]
Thus
\[
U(E)=\left(W+\frac12\right)s-s^2+\frac12\sum_vx_v^2+z(E).
\]
By the choice of \(W\),
\[
W+\frac12=\left(2r-\frac12\right)D_0.
\]
Also \(0\le z(E)\le m\).

## Cardinality-locking lemma

Define the base term
\[
B(E)=\left(2r-\frac12\right)D_0s-s^2+\frac12\sum_vx_v^2.
\]
We claim that an optimum of \(U\) must have \(s=rD_0\) and exactly \(r\) left degrees equal to \(D_0\), all remaining left degrees being zero.

First fix \(s\), and write
\[
s=qD_0+t,\qquad 0\le t<D_0.
\]
Because \(0\le x_v\le D_0\) and \(\sum_vx_v=s\), convexity of \(x^2\) gives
\[
\sum_vx_v^2\le qD_0^2+t^2.
\]
Let \(j=q-r\). Substituting the right-hand side into \(B\) gives the exact gap
\[
\begin{aligned}
r^2D_0^2-B(E)
&\ge D_0^2j^2+D_0t\left(2j+\frac12\right)+\frac{t^2}{2}.
\end{aligned}
\]
If \(s\ne rD_0\), the right-hand side is at least
\[
\frac{D_0+1}{2}=m+1.
\]
For \(j\ge0\) this is immediate; for \(j\le-1\), the expression decreases with \(t\in\{0,\ldots,D_0-1\}\), and its smallest possible value occurs at \(j=-1,t=D_0-1\), where it equals \((D_0+1)/2\).

Now suppose \(s=rD_0\). The maximum possible value of \(\sum_vx_v^2\) is \(rD_0^2\), attained exactly when \(r\) coordinates are \(D_0\) and all others are zero. For any other integer degree vector with the same sum, the square-sum drops by at least
\[
D_0^2-\bigl((D_0-1)^2+1\bigr)=2(D_0-1),
\]
so the base term drops by at least \(D_0-1=2m\).

Since \(z(E)\le m\), neither a non-target cardinality nor a non-saturated degree vector at the target cardinality can compensate for these losses. On the other hand, selecting all \(D_0\) incident facts of any \(r\) left vertices gives base value exactly \(r^2D_0^2\). Hence every global maximizer of \(U\) is precisely the union of the full incidence stars of some \(r\)-element set \(K\subseteq V\).

## Recovering CLIQUE

For such a star union, a shared right vertex \(c_e\) has selected degree two exactly when both endpoints of \(e\) lie in \(K\). Therefore
\[
z(E)=|F[K]|,
\]
and hence
\[
U(E)=r^2D_0^2+|F[K]|.
\]
It follows that
\[
\max_E U(E)
 =r^2D_0^2+
   \max_{\substack{K\subseteq V\\|K|=r}}|F[K]|.
\]
Thus \(H\) has an \(r\)-clique if and only if
\[
\min_E\operatorname{cost}(E\mid D)
\le
WnD_0-r^2D_0^2-\binom r2.
\]
The construction has \(nD_0=O(nm)\) facts and all weights have polynomial bit length, so it is a polynomial-time many-one reduction. The threshold decision problem is therefore NP-complete, and soft repairing for the fixed FD set \(\{A\to B,A\to C\}\) is NP-hard.

## Relation to prior work

Carmeli, Grohe, Kimelfeld, Livshits and Tibi prove polynomial-time algorithms for several soft-FD families, but explicitly list \(\{A\to B,A\to C\}\) as one of the simplest unresolved cases. The point is that although this pair is logically equivalent to the single hard FD \(A\to BC\), the two soft penalties are not equivalent to one soft penalty.

There is also a close optimization connection to degree-sequence problems. Meunier and Onn (2026) discuss the NP-hard fixed-cardinality problem of maximizing a sum of squared degrees even on bipartite graphs. The reduction above does not assume a fixed cardinality: the uniform tuple weight is calibrated so that the common-left soft-FD objective itself locks the optimum onto exactly \(rD_0\) selected incidence edges. Hence that fixed-cardinality hardness result does not by itself imply the theorem here, though the convex degree-concentration mechanism is closely related.

## Reproducibility

`artifacts/check_small_instances.py` constructs the reduction and exhaustively checks two three-vertex examples. It verifies the closed-form optimum and that every maximizing subset is a union of full left stars; `artifacts/verification.txt` records the resulting values. This finite check is only a sanity test; the theorem is established by the general proof above.

## Limitations

- The theorem settles the exact optimization complexity of this FD set, not its best approximation ratio. The later 2-approximation for functional-dependency soft repairs obtained by Guo, Chen, Yang and Miao (2026) still applies.
- The reduction uses a common tuple weight that depends on the CLIQUE instance. It does not prove hardness when tuple weights are fixed to one.
- The result concerns tuple-deletion soft repairs under the pairwise-violation semantics above; it does not automatically transfer to update repairs or other soft-constraint semantics.
- Originality is asserted only to the best of our knowledge. Searches of the exact FD set, synonymous common-left formulations, soft-repair hardness, and literature citing the 2024 paper found no prior resolution. A later or poorly indexed result could still exist.

## References

1. N. Carmeli, M. Grohe, B. Kimelfeld, E. Livshits, and M. Tibi, “Database Repairing with Soft Functional Dependencies,” *ACM Transactions on Database Systems* 49(2), Article 8, 2024. https://doi.org/10.1145/3651156
2. N. Carmeli, M. Grohe, B. Kimelfeld, E. Livshits, and M. Tibi, “Database Repairing with Soft Functional Dependencies,” ICDT 2021 / arXiv:2009.13821. https://arxiv.org/abs/2009.13821
3. Z. Guo, P. Chen, J. Yang, and D. Miao, “Approximating Optimal Soft Repairs for Denial Constraints,” *IEEE Transactions on Knowledge and Data Engineering* 38(8), 4883–4896, 2026. https://doi.org/10.1109/TKDE.2026.3689023
4. F. Meunier and S. Onn, “Quadratic Degree Sequence Optimization and the Critical Roots of a Graph,” arXiv:2608.05827, 2026. https://arxiv.org/abs/2608.05827
