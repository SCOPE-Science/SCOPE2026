# Zero forcing and minimum rank of local total graphs with zero deleted

## Finding

Let \(R\) be a finite commutative local ring that is not a field, with maximal ideal \(\mathfrak m\), \(q=|R/\mathfrak m|\), and \(s=|\mathfrak m|\). Let \(T_0(\Gamma(R))\) be the total graph of \(R\) with the zero vertex deleted. For real symmetric graph minimum rank, \[Z(T_0(\Gamma(R)))=M(T_0(\Gamma(R)))=\begin{cases}2,&s=2,\\q(s-1)-1,&s\ge3,\end{cases}\] and \[\operatorname{mr}(T_0(\Gamma(R)))=\begin{cases}1,&s=2,\\q,&s\ge3.\end{cases}\] The case \(s=2\) necessarily has \(q=2\). The number of minimum zero forcing sets is \((s-1)s^{q-1}\). For \(s\ge3\), these minimum sets are exactly the complements of transversals that choose one nonzero element from \(\mathfrak m\) and one element from each nonzero coset of \(\mathfrak m\); for \(s=2\), the unique nonzero element of \(\mathfrak m\) must instead be initially blue.

In particular, outside the two three-vertex boundary rings, the real symmetric minimum rank of \(T_0(\Gamma(R))\) is exactly the residue-field order \(q\). Together with the graph order \(qs-1\), this recovers both \(q\) and \(s\).

## Assumptions and scope

Let \(R\) be a finite commutative local ring with identity that is not a field. Its set of zero divisors is its maximal ideal \(\mathfrak m\). Put
\[
q=|R/\mathfrak m|,
\qquad
s=|\mathfrak m|.
\]
The graph \(T_0(\Gamma(R))\) has vertex set \(R\setminus\{0\}\), and two distinct vertices \(x,y\) are adjacent exactly when
\[
x+y\in\mathfrak m.
\]

The minimum-rank model is the standard real symmetric one: \(\mathcal S(G)\) is the set of real symmetric matrices whose off-diagonal nonzero pattern is exactly \(G\),
\[
\operatorname{mr}(G)=\min_{A\in\mathcal S(G)}\operatorname{rank}A,
\qquad
M(G)=|V(G)|-\operatorname{mr}(G).
\]
The standard zero forcing number \(Z(G)\) satisfies
\[
M(G)\le Z(G).
\]

## Proof

The total-graph structure theorem for rings whose zero divisors form an ideal gives a complete component description. The zero-divisor coset \(\mathfrak m\) induces \(K_s\). If \(2\in\mathfrak m\), every nonzero coset of \(\mathfrak m\) induces another \(K_s\), and there are no edges between distinct cosets. Thus
\[
T(\Gamma(R))\cong qK_s.
\]
Deleting the zero vertex gives
\[
T_0(\Gamma(R))
\cong
K_{s-1}\ \cup\ (q-1)K_s.
\tag{1}
\]

If \(2\notin\mathfrak m\), the zero-divisor coset still induces \(K_s\), while every pair of opposite nonzero cosets \(a+\mathfrak m\) and \(-a+\mathfrak m\) induces \(K_{s,s}\). Hence
\[
T_0(\Gamma(R))
\cong
K_{s-1}\ \cup\
\frac{q-1}{2}K_{s,s}.
\tag{2}
\]

Zero forcing is additive over connected components because a force can never cross components. For \(t\ge2\),
\[
Z(K_t)=t-1:
\]
if at least two vertices remain white, no blue vertex has a unique white neighbor, while one white vertex is immediately forced. For \(s\ge2\),
\[
Z(K_{s,s})=2s-2.
\]
Indeed, with three or more white vertices, either both parts contain at least two whites, or one part contains at least two and the other at most one; after any possible first force, at least two whites remain in one part and no further force is possible. Conversely, leaving exactly one white vertex in each part gives a forcing set. Finally,
\[
Z(K_1)=1.
\]

Assume \(s\ge3\). Applying these component formulas to either (1) or (2) gives
\[
Z(T_0(\Gamma(R)))
=
(s-2)+(q-1)(s-1)
=
q(s-1)-1.
\tag{3}
\]

For the minimum-rank side, construct a block diagonal real symmetric matrix following the same components. Use an all-ones matrix on every clique block. This has rank \(1\) and the correct off-diagonal pattern. On every \(K_{s,s}\) block use
\[
\begin{pmatrix}
0&J_s\\
J_s&0
\end{pmatrix},
\]
which has rank \(2\) and exactly the required pattern. Thus, in the characteristic-two case the witness rank is
\[
1+(q-1)=q,
\]
while in the odd-characteristic case it is
\[
1+2\frac{q-1}{2}=q.
\]
Since \(T_0(\Gamma(R))\) has \(qs-1\) vertices, this gives
\[
M(T_0(\Gamma(R)))
\ge
qs-1-q
=
q(s-1)-1.
\]
Together with (3) and \(M(G)\le Z(G)\), equality holds throughout:
\[
Z=M=q(s-1)-1,
\qquad
\operatorname{mr}=q.
\]

Now suppose \(s=2\). For a finite local nonfield ring this is the exceptional case
\[
R\cong\mathbb Z_4
\quad\text{or}\quad
R\cong\mathbb F_2[X]/(X^2),
\]
so \(q=2\). Deleting zero from the two copies of \(K_2\) gives
\[
T_0(\Gamma(R))\cong K_1\cup K_2.
\]
Therefore
\[
Z=1+1=2.
\]
A block matrix consisting of the zero \(1\times1\) block and an all-ones \(2\times2\) block has rank \(1\), so
\[
M\ge3-1=2.
\]
Again \(M\le Z\), hence
\[
Z=M=2,
\qquad
\operatorname{mr}=1.
\]

For \(s\ge3\), every minimum zero forcing set omits exactly one vertex from each coset component: one vertex of \(\mathfrak m\setminus\{0\}\), and one from each nonzero coset. In an odd-characteristic \(K_{s,s}\) component, the two omitted vertices must lie in opposite parts, which is exactly one omission from each of the paired residue cosets. Therefore the number of minimum sets is
\[
(s-1)s^{q-1}.
\]
When \(s=2\), the isolated nonzero zero divisor must be blue, and one of the two vertices in the regular \(K_2\) is omitted, giving \(2=(s-1)s^{q-1}\) minimum sets as well.

## Verification

The accompanying `verify.py` constructs \(T_0(\Gamma(\mathbb Z/(p^k)))\) directly from addition for several prime-power rings, computes connected components, exhaustively determines the zero forcing number and all minimum zero forcing sets whenever the graph has at most \(15\) vertices, and checks the rank of the explicit block witness over exact rational arithmetic.

It also independently constructs the noncyclic local ring
\[
\mathbb F_2[x,y]/(x,y)^2,
\]
whose maximal ideal has four elements, and verifies the same conclusions directly.

Exact replay output:

```text
Z/4: |V|=3 components=[1, 2] exhaustive Z=2 min_sets=2 witness_rank=1
Z/8: |V|=7 components=[3, 4] exhaustive Z=5 min_sets=12 witness_rank=2
Z/16: |V|=15 components=[7, 8] exhaustive Z=13 min_sets=56 witness_rank=2
Z/9: |V|=8 components=[2, 6] exhaustive Z=5 min_sets=18 witness_rank=3
Z/27: |V|=26 components=[8, 18] structural Z=23 predicted_min_sets=648 witness_rank=3
Z/25: |V|=24 components=[4, 10, 10] structural Z=19 predicted_min_sets=2500 witness_rank=5
F2[x,y]/(x,y)^2: |V|=7 components=[3, 4] exhaustive Z=5 min_sets=12 witness_rank=2
VERIFY_OK
```

The finite checks are corroborative only. The all-ring proof is the component decomposition, the elementary zero-forcing lemmas for cliques and balanced complete bipartite graphs, and the explicit low-rank block matrices.

## Relationship to prior work

Anderson and Badawi introduced \(T_0(\Gamma(R))\), the total graph with zero deleted, and studied connectivity, diameter, girth, zero-divisor paths, and regular paths. Their paper lists primary Mathematics Subject Classification \(13A15\). Full-text searches of that paper found no occurrence of “zero forcing,” “minimum rank,” or “nullity.”

Their earlier total-graph paper gives the component decomposition used here when \(Z(R)\) is an ideal: the regular part is a union of \(K_s\) components when \(2\in Z(R)\), and a union of \(K_{s,s}\) components when \(2\notin Z(R)\). The present result applies that structure after deleting zero and then determines zero forcing, maximum nullity, real minimum rank, and every minimum forcing set.

A 2016 survey of total graphs summarizes the literature on \(T_0(\Gamma(R))\) through that period and contains no occurrence of “zero forcing” or “minimum rank.”

Mishra and Patra later study zero forcing for a total graph of \(\mathbb Z_n\) defined with respect to the nil ideal and build a graph whose vertices are minimum zero forcing sets. Their paper includes the zero vertex in the underlying graph and does not study \(T_0(\Gamma(R))\) or real minimum rank. For prime-power \(\mathbb Z_n\), their underlying ideal agrees with the zero-divisor ideal, so their full-graph calculation is genuine nearby coverage and is not claimed here.

## Limitations

The theorem is restricted to finite commutative local nonfields. For a nonlocal finite ring, \(Z(R)\) is not an ideal and the component decomposition used in the proof fails.

The minimum rank is over real symmetric matrices. Different coefficient fields can change minimum rank.

The general zero-forcing inequality is used as a theorem from the graph minimum-rank literature; the ring-specific work is the exact matching upper and lower construction.

The strengthened parameters are elementary once the component theorem is available. The mathematical value is the exact equality \(Z=M\), the residue-field recovery by minimum rank, the deletion-of-zero boundary at \(s=2\), and the complete transversal classification of all minimum forcing sets.

## References

1. D. F. Anderson and A. Badawi, “On the total graph of a commutative ring without the zero element,” *Journal of Algebra and Its Applications* 11 (2012), 1250074. DOI: 10.1142/S0219498812500740.
2. D. F. Anderson and A. Badawi, “The total graph of a commutative ring,” *Journal of Algebra* 320 (2008), 2706–2719. DOI: 10.1016/j.jalgebra.2008.06.028.
3. K. Nazzal, “Total Graphs Associated to a Commutative Ring,” *Palestine Journal of Mathematics* 5 (Special Issue 1) (2016), 108–126.
4. A. Mishra and K. Patra, “Zero forcing graph associated to the total graph of \(\mathbb Z_n\) with respect to nil ideal,” *Advances in Mathematics: Scientific Journal* 9 (2020), 9443–9453. DOI: 10.37418/amsj.9.11.48.
5. AIM Minimum Rank — Special Graphs Work Group, “Zero forcing sets and the minimum rank of graphs,” *Linear Algebra and its Applications* 428 (2008), 1628–1648. DOI: 10.1016/j.laa.2007.10.009.
