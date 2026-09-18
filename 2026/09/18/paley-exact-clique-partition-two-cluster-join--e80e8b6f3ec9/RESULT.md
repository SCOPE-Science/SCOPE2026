# Exact clique partition at two clusters via a Paley pairing

## Statement

For a finite simple graph \(G\), let \(cc(G)\) be the minimum number of cliques whose edge sets cover \(E(G)\), and let \(cp(G)\) be the minimum number of cliques whose edge sets partition \(E(G)\).

For positive integers \(h,k\), write
\[
G_{h,k}=(hK_k)\vee(hK_k),
\]
where \(\vee\) denotes graph join. Thus the two sides are each the disjoint union of \(h\) copies of \(K_k\), and all edges between the two sides are present.

**Theorem.** Let \(q\ge 5\) be a prime power with \(q\equiv1\pmod4\). Then
\[
\boxed{cc(G_{2,q})=4,\qquad cp(G_{2,q})=q^2+3q.}
\]
Consequently
\[
cp(G_{2,q})-cc(G_{2,q})=q^2+3q-4.
\]

The clique-partition value attains the standard cut lower bound. This supplies an exact infinite family in the two-cluster regime \(h=2\), whereas the directly motivating exact result determines \(G_{h,k}\) for even \(k\) under \(h\ge k-1\).

There is also an arithmetic obstruction on the complementary odd congruence class.

**Proposition.** If \(k\ge3\) is odd and \(k\equiv3\pmod4\), then
\[
cp(G_{2,k})\ge k^2+3k+1.
\]
In particular, the same cut lower bound cannot be attained in this congruence class.

## Proof of the theorem

Write the four \(q\)-cliques as
\[
A=A_0\mathbin{\dot\cup}A_1,\qquad B=B_0\mathbin{\dot\cup}B_1,
\]
with every \(A_i\) complete to every \(B_j\).

### Clique covering number

The four sets \(A_i\cup B_j\) are cliques and cover every edge, so \(cc(G_{2,q})\le4\). Conversely, choose one vertex from each \(A_i\) and each \(B_j\). These four chosen vertices induce \(K_{2,2}\). Any clique of \(G_{2,q}\) contains at most one chosen \(A\)-vertex and at most one chosen \(B\)-vertex, and hence covers at most one of the four edges of this \(K_{2,2}\). Thus \(cc(G_{2,q})\ge4\), proving \(cc(G_{2,q})=4\).

### Cut lower bound for the partition number

Across the cut \(A\mid B\) there are
\[
s=4q^2
\]
edges, while each side contains
\[
a=b=2\binom q2=q(q-1)
\]
internal edges. The Erdős--Faudree--Ordman cut inequality, in the form used in the recent work on \(G_{h,k}\), gives
\[
cp(G)\ge s-a-b-\min\{a,b\}.
\]
Therefore
\[
cp(G_{2,q})\ge4q^2-3q(q-1)=q^2+3q.
\]
It remains to construct a partition of this size.

### A finite-field pairing

Identify every cluster with the finite field \(\mathbb F_q\), and let \(\chi\) be its quadratic character. Since \(q\equiv1\pmod4\), we have \(\chi(-1)=1\). Split the edges of \(K_q\) into
\[
E_+=\{\{x,y\}:\chi(y-x)=1\},\qquad
E_-=\{\{x,y\}:\chi(y-x)=-1\}.
\]
This is well-defined on unordered pairs because \(-1\) is a square, and each class has \(q(q-1)/4\) edges.

We need two nonsquares \(r_+,r_-\in\mathbb F_q^\times\) such that
\[
\chi(1-r_+)=1,\qquad \chi(1-r_-)=-1.
\]
They always exist. Indeed, if
\[
N_{ab}=|\{r\ne0,1:\chi(r)=a,\ \chi(1-r)=b\}|\qquad(a,b\in\{\pm1\}),
\]
then symmetry under \(r\mapsto1-r\), together with the quadratic Jacobi sum
\[
\sum_{r\in\mathbb F_q}\chi(r)\chi(1-r)=-1,
\]
gives
\[
N_{-+}=N_{--}=\frac{q-1}{4}.
\]
Thus both choices exist. Since \(\pm1\) are squares, neither \(r_+\) nor \(r_-\) equals \(\pm1\).

For a nonsquare \(r\), define on unordered pairs
\[
T_r(\{x,y\})=\{x+ry,\ rx+y\}.
\]
The matrix
\[
\begin{pmatrix}1&r\\ r&1\end{pmatrix}
\]
has determinant \(1-r^2\ne0\), so \(T_r\) is a bijection on the edges of \(K_q\). Moreover,
\[
(rx+y)-(x+ry)=(1-r)(y-x),
\]
and hence
\[
T_r(E_\varepsilon)=E_{\varepsilon\chi(1-r)}.
\]

There is one more property that makes the construction a clique partition rather than merely a pairing of internal edges. Fix an \(A\)-vertex \(a\) and a \(B\)-vertex \(b\), and consider input edges in one class \(E_\varepsilon\) containing \(a\). Write such an edge as \(\{a,a+d\}\). If \(b\) is an endpoint of its image under \(T_r\), then
\[
d=b-(1+r)a\quad\text{or}\quad d=r^{-1}(b-(1+r)a).
\]
The two candidate differences differ by the nonsquare factor \(r\), so they have opposite quadratic characters. Hence at most one belongs to \(E_\varepsilon\). Therefore the \(K_4\)'s produced from distinct input edges in a fixed cell \(A_i\cup B_j\) never repeat an \(A_iB_j\) crossing edge.

Now use \(r_+\) on row \(A_0\) and \(r_-\) on row \(A_1\). In cells \(A_i\cup B_0\), pair every edge of \(E_+\) in \(A_i\) with its image under \(T_{r_i}\) in \(B_0\). In cells \(A_i\cup B_1\), do the same with \(E_-\). For each paired pair of internal edges, take the induced \(K_4\) on their four endpoints.

Every internal edge of each \(A_i\) is used exactly once. On \(B_0\), row \(A_0\) maps \(E_+\) to \(E_+\), while row \(A_1\) maps \(E_+\) to \(E_-\); thus every internal edge of \(B_0\) is used exactly once. Similarly, on \(B_1\), the two rows map \(E_-\) respectively to \(E_-\) and \(E_+\), so every internal edge of \(B_1\) is used exactly once. The preceding uniqueness argument shows that no crossing edge occurs in two of these \(K_4\)'s.

There are
\[
4\cdot\frac{q(q-1)}4=q(q-1)
\]
such \(K_4\)'s. They use \(4q(q-1)\) of the \(4q^2\) crossing edges. Put each of the remaining \(4q\) crossing edges into its own \(K_2\). This yields a clique partition with
\[
q(q-1)+4q=q^2+3q
\]
members. Together with the cut lower bound, this proves
\[
cp(G_{2,q})=q^2+3q.
\]

## Proof of the congruence obstruction

For a clique in a partition, let \(x\) and \(y\) be its numbers of vertices on the two sides of the cut. The elementary inequalities underlying the cut bound are
\[
xy-1\le 2\binom x2+\binom y2,
\qquad
xy-1\le \binom x2+2\binom y2.
\]
Their slacks are respectively
\[
\binom{y-x}{2}+\binom{x-1}{2},
\qquad
\binom{x-y}{2}+\binom{y-1}{2},
\]
where \(\binom t2=t(t-1)/2\) for integer \(t\). If \(cp(G_{2,k})=k^2+3k\), equality must hold after summing both inequalities, so every partition clique must have equality in both. The only nontrivial possibilities are
\[
(x,y)=(1,1)\quad\text{or}\quad(2,2).
\]
Thus every partition clique is either a crossing \(K_2\) or a \(K_4\) containing one internal edge from each side.

Fix a cluster \(A_i\) and a vertex \(v\in A_i\). Its \(k-1\) incident internal edges must lie in \(k-1\) such \(K_4\)'s. For a fixed \(B_j\), each \(K_4\) containing \(v\) uses two distinct crossing edges from \(v\) to \(B_j\), so at most \(\lfloor k/2\rfloor=(k-1)/2\) of these \(K_4\)'s can use \(B_j\). Since there are two \(B\)-clusters and altogether \(k-1\) incident internal edges, exactly \((k-1)/2\) must be assigned to each \(B_j\). Hence, for each fixed cell \(A_i\cup B_j\), the internal edges of \(A_i\) assigned to that cell form a \((k-1)/2\)-regular graph on \(k\) vertices.

If \(k\equiv3\pmod4\), then both \(k\) and \((k-1)/2\) are odd, contradicting the handshake lemma. Therefore equality in the cut bound is impossible, and integrality gives
\[
cp(G_{2,k})\ge k^2+3k+1.
\]

## Context and significance

Bo Ning's 2026 preprint studies the same graphs \(G_{h,k}\). Its Proposition 3.1 determines both clique parameters exactly when \(k\) is even and \(h\ge k-1\), using a one-factorization of \(K_k\). The theorem above instead treats an infinite odd-order family at \(h=2\), which is outside that hypothesis for every \(q\ge5\), and uses quadratic-character classes and a finite-field edge bijection. The congruence obstruction shows that saturation of the cut bound at \(h=2\) is not a parity-insensitive phenomenon.

## Limitations

The result does not determine \(cp(G_{2,k})\) for odd \(k\equiv3\pmod4\); it only proves that the cut lower bound misses by at least one. It also does not cover arbitrary composite \(k\equiv1\pmod4\) that are not prime powers, nor determine the full range of \((h,k)\) for which the cut lower bound is attained.

Originality is asserted only to the best of our knowledge. The most direct recent source was inspected in full. Exact and synonymous searches did not locate this two-cluster Paley formula or its congruence obstruction. Older clique-partition and combinatorial-design literature creates residual risk that an equivalent block-packing construction exists under different terminology.

## References

1. B. Ning, *On the difference between clique partition and clique covering numbers of graphs*, arXiv:2608.11536 (2026).
2. P. Erdős, R. Faudree, and E. T. Ordman, *Clique partitions and clique coverings*, Discrete Mathematics 72 (1988), 93--101, DOI: 10.1016/0012-365X(88)90197-5.
3. L. Caccetta, P. Erdős, E. T. Ordman, and N. J. Pullman, *The difference between the clique numbers of a graph*, Ars Combinatoria 19A (1985), 97--106.
