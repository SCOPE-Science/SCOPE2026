# Total and paired domination of proper power graphs of finite prime-power groups

## Finding

Let \(G\) be a finite \(p\)-group and let \(t_p(G)\) be the number of subgroups of \(G\) of order \(p\). For the proper power graph \(\mathcal P^*(G)\), if \(p\) is odd then \[\gamma_t(\mathcal P^*(G))=\gamma_{\mathrm{pr}}(\mathcal P^*(G))=2t_p(G).\] If \(p=2\), total and paired dominating sets exist if and only if every involution of \(G\) is a square (equivalently, every subgroup of order \(2\) lies in a cyclic subgroup of order \(4\)); when they exist, both parameters equal \(2t_2(G)\). Moreover every minimum total dominating set is automatically paired. In particular, for an abelian \(2\)-group \(G\cong C_{2^{a_1}}\times\cdots\times C_{2^{a_r}}\), the parameters exist exactly when every \(a_i\ge2\), and then both equal \(2(2^r-1)\).

This gives a complete existence-and-value classification for the two strengthened domination parameters on proper power graphs of finite prime-power groups.

## Assumptions and scope

Let \(G\) be a finite group of order a power of a prime \(p\). Its proper power graph \(\mathcal P^*(G)\) has vertex set \(G\setminus\{e\}\), and two distinct vertices are adjacent exactly when one is a power of the other.

For a nonidentity element \(x\), the cyclic \(p\)-group \(\langle x\rangle\) has a unique subgroup of order \(p\); denote it by \(H(x)\). Let \(t_p(G)\) be the number of subgroups of \(G\) of order \(p\).

A total dominating set is a vertex set \(D\) such that every vertex has a neighbor in \(D\). A paired dominating set is a dominating set whose induced subgraph has a perfect matching.

## Proof

If \(x\) and \(y\) are adjacent, then one of \(\langle x\rangle\) and \(\langle y\rangle\) is contained in the other. Hence
\[
H(x)=H(y).
\tag{1}
\]
Thus every connected component of \(\mathcal P^*(G)\) is contained in one fiber of the map \(x\mapsto H(x)\).

Conversely, suppose \(H(x)=H(y)=H\). Choose any nonidentity \(h\in H\). Since \(H\) is the unique subgroup of order \(p\) in each of the cyclic groups \(\langle x\rangle\) and \(\langle y\rangle\), the element \(h\) is a power of both \(x\) and \(y\). Hence \(x\) and \(y\) lie in the same component, with a path of length at most two through \(h\). Therefore the connected components are indexed exactly by the order-\(p\) subgroups of \(G\), so there are \(t_p(G)\) components.

Fix such a component corresponding to \(H\). Every nonidentity element \(h\in H\) is adjacent to every other vertex of that component, because \(H\subseteq\langle x\rangle\) for every vertex \(x\) in the component. Thus \(h\) is universal inside its component.

If \(p\) is odd, then \(H\setminus\{e\}\) has \(p-1\ge2\) vertices. Choose two distinct elements \(h_1,h_2\in H\setminus\{e\}\). They are adjacent and together totally dominate the entire component. Since a total dominating set must contain at least two vertices in every connected component, summing over the \(t_p(G)\) components gives
\[
\gamma_t(\mathcal P^*(G))=2t_p(G).
\]
The chosen two vertices in each component form an edge, so the union of these edges is a perfect matching on the selected vertices. Hence
\[
\gamma_{\mathrm{pr}}(\mathcal P^*(G))=2t_p(G).
\]

Now let \(p=2\). The unique nonidentity element \(h\) of an order-\(2\) subgroup \(H\) is universal in its component. This component has another vertex if and only if \(h\) is adjacent to some distinct \(x\). The alternative \(x\in\langle h\rangle\) is impossible, so necessarily \(h\in\langle x\rangle\). Since \(x\) has order a power of two greater than two, the cyclic group \(\langle x\rangle\) contains an element \(y\) of order four with
\[
y^2=h.
\]
Conversely, such a square root \(y\) is adjacent to \(h\). Therefore the component is nontrivial exactly when its involution is a square. Consequently \(\mathcal P^*(G)\) has no isolated vertices exactly when every involution of \(G\) is a square.

If some involution is not a square, it is an isolated vertex, so neither total nor paired domination exists. If every involution is a square, then in every component choose its involution \(h\) and an order-four element \(y\) with \(y^2=h\). This adjacent pair totally dominates the component. Again two vertices per component are necessary, and the selected pairs form a perfect matching. Thus
\[
\gamma_t(\mathcal P^*(G))
=
\gamma_{\mathrm{pr}}(\mathcal P^*(G))
=
2t_2(G).
\]

Finally, any minimum total dominating set has exactly two vertices in each component. Because each selected vertex must itself have a selected neighbor, those two vertices are adjacent. Hence the componentwise pairs form a perfect matching, proving that every minimum total dominating set is paired.

For the stated abelian corollary, write
\[
G\cong C_{2^{a_1}}\times\cdots\times C_{2^{a_r}},
\qquad a_i\ge1.
\]
An involution is divisible by two exactly when its coordinates in every direct \(C_2\)-factor are zero. Thus every involution is a square if and only if no \(C_2\)-factor occurs, equivalently every \(a_i\ge2\). In that case the order-two subgroups are the nonzero elements of the \(r\)-dimensional vector space \(G[2]\), so
\[
t_2(G)=2^r-1.
\]

## Verification

The standalone `verify.py` constructs proper power graphs directly from multiplication tables. It checks the component-to-order-\(p\)-subgroup correspondence, the universal prime-order vertices, the involution-square criterion, and—on graphs with at most fifteen vertices—exhaustively computes the total and paired domination minima.

The examples include cyclic groups, elementary and mixed abelian \(p\)-groups, the dihedral group of order eight, and the quaternion group of order eight. The last two distinguish the two possible \(2\)-group behaviors: reflections in the dihedral group yield isolated involutions, whereas the unique involution in the quaternion group is a square.

Exact output:

```text
VERIFY_OK
group=C3 vertices=2 order_p_subgroups=1 exists=True predicted=2 gamma_t=2 gamma_pr=2
group=C9 vertices=8 order_p_subgroups=1 exists=True predicted=2 gamma_t=2 gamma_pr=2
group=C3xC3 vertices=8 order_p_subgroups=4 exists=True predicted=8 gamma_t=8 gamma_pr=8
group=C4 vertices=3 order_p_subgroups=1 exists=True predicted=2 gamma_t=2 gamma_pr=2
group=C8 vertices=7 order_p_subgroups=1 exists=True predicted=2 gamma_t=2 gamma_pr=2
group=C4xC4 vertices=15 order_p_subgroups=3 exists=True predicted=6 gamma_t=6 gamma_pr=6
group=C2xC4 vertices=7 order_p_subgroups=3 exists=False predicted=None gamma_t=None gamma_pr=None
group=C2xC2 vertices=3 order_p_subgroups=3 exists=False predicted=None gamma_t=None gamma_pr=None
group=D8 vertices=7 order_p_subgroups=5 exists=False predicted=None gamma_t=None gamma_pr=None
group=Q8 vertices=7 order_p_subgroups=1 exists=True predicted=2 gamma_t=2 gamma_pr=2
group=C9xC3 vertices=26 order_p_subgroups=4 exists=True predicted=8 gamma_t=not_exhaustive gamma_pr=not_exhaustive
```

The finite calculations are corroborative only. The arbitrary finite \(p\)-group theorem is proved by the component argument above.

## Relationship to prior work

Curtin and Pourgholi study power graphs of finite groups from a group-theoretic direction and provide an archive-era source with primary algebra classification. Their paper concerns edge counts and extremality rather than domination.

Bera, Dey, Patra, and Sahoo determine the ordinary domination number of the proper power graph of a finite \(p\)-group: it is the number \(t_p(G)\) of order-\(p\) subgroups. Their paper also records that the number of connected components is \(t_p(G)\). The present result strengthens this picture for total and paired domination. The strengthened parameters double the ordinary value whenever they exist, but for \(2\)-groups existence itself detects whether every involution extends to a cyclic subgroup of order four.

A separate paper on domination parameters of undirected power graphs of cyclic groups treats the full power graph, where the identity is retained. That setting has a universal identity vertex and does not imply the proper-graph componentwise formula or the involution obstruction.

Targeted searches for the exact phrases “total domination” and “paired domination” together with “proper power graph” did not locate a theorem covering the classification above.

## Limitations

The theorem is restricted to finite groups of prime-power order. For groups with at least two prime divisors, a connected component of the proper power graph can interact with several prime-order subgroups, so the component argument used here no longer yields the same formula.

For \(2\)-groups the theorem deliberately leaves the involution-square condition in intrinsic group-theoretic form; it does not classify all finite nonabelian \(2\)-groups satisfying that condition.

The ordinary domination result in the closest 2025 paper is used only for literature comparison, not as a proof premise: the component decomposition and the strengthened domination bounds are reconstructed directly here.

## References

1. B. Curtin and G. R. Pourgholi, “A group sum inequality and its application to power graphs,” *Bulletin of the Australian Mathematical Society* 90 (2014), 418–426. DOI: 10.1017/S0004972714000434.
2. S. Bera, H. K. Dey, K. L. Patra, and B. K. Sahoo, “On the domination number of proper power graphs of finite groups,” *Discrete Mathematics* 348 (2025), 114557. DOI: 10.1016/j.disc.2025.114557.
3. A. Khan and S. A. Kauser, “A study of some domination parameters of undirected power graphs of cyclic groups,” *International Journal of Future Generation Communication and Networking* 13 (2020), 2674–2677.
