# Cyclic-subgroup graphs of prime-kernel Frobenius groups with even cyclic complement

## Finding

Let \(r\) be an odd prime, let \(m\ge4\) be even with
\[
m\mid r-1,
\]
and let
\[
G=C_r\rtimes C_m
\]
be the faithful semidirect product. Write
\[
m=\prod_{i=1}^{k}p_i^{a_i},
\qquad
\tau(m)=\prod_{i=1}^{k}(a_i+1),
\]
and put
\[
e(m)=
\tau(m)\sum_{i=1}^{k}\frac{a_i}{a_i+1}.
\]
Thus \(e(m)\) is the number of edges in the cyclic-subgroup graph of \(C_m\).

Then the cyclic-subgroup graph of \(G\) is the one-point union, at the trivial subgroup, of \(r\) copies of the cyclic-subgroup graph of \(C_m\), together with one additional leaf corresponding to the normal subgroup \(C_r\).

In particular,
\[
\boxed{
|C(G)|=2+r(\tau(m)-1)
}
\]
and
\[
\boxed{
|E(C(G)^*)|=1+r\,e(m).
}
\]

For the cyclic group of the same order,
\[
|E(C_{rm})^*|
=
\tau(m)+2e(m).
\]
Hence
\[
\boxed{
|E(C(G)^*)|-|E(C_{rm})^*|
=
(r-2)e(m)-(\tau(m)-1)>0.
}
\]

Therefore the conjectured cyclic-group lower bound for the number of edges in the cyclic-subgroup graph holds strictly for every faithful Frobenius group with prime kernel and even cyclic complement of order at least \(4\).

## Assumptions and scope

The cyclic-subgroup graph \(C(X)^*\) of a finite group \(X\) has the cyclic subgroups of \(X\) as vertices. Two distinct cyclic subgroups are adjacent when one is maximal as a cyclic subgroup inside the other, equivalently when they form a cover relation in the inclusion poset of cyclic subgroups.

The action in
\[
G=C_r\rtimes C_m
\]
is faithful. Since
\[
m\mid r-1,
\]
such an action is obtained by embedding \(C_m\) into
\[
\operatorname{Aut}(C_r)\cong C_{r-1}.
\]
Every nonidentity element of the complement therefore acts fixed-point freely on the nonidentity elements of the kernel, so \(G\) is a Frobenius group.

The restriction that \(m\) is even places the theorem in the even-order range not covered by the odd-order case of the published edge-minimality theorem. The condition \(m\ge4\) excludes the generalized-dihedral boundary \(m=2\), whose cyclic-subgroup graph is already a standard special family.

## Proof

Choose a presentation
\[
G=
\langle x,y:
x^r=y^m=1,\;
yxy^{-1}=x^u
\rangle,
\]
where the residue class of \(u\) modulo \(r\) has multiplicative order \(m\).

For
\[
t\in\mathbf F_r,
\]
let
\[
H_t=\langle y\rangle^{x^t}.
\]
These are \(r\) conjugate complements, each isomorphic to \(C_m\).

We first show that every element outside
\[
R=\langle x\rangle
\]
belongs to a unique \(H_t\). Write an element of \(G\) as \(x^a y^b\). If
\[
b\not\equiv0\pmod m,
\]
then
\[
u^b\not\equiv1\pmod r
\]
because \(u\) has order \(m\). Conjugating \(y^b\) by \(x^t\) gives an element whose \(C_r\)-coordinate is
\[
(1-u^b)t.
\]
Since \(1-u^b\) is invertible modulo \(r\), there is a unique \(t\) producing any prescribed \(C_r\)-coordinate \(a\). Thus every element outside \(R\) belongs to exactly one conjugate complement \(H_t\).

It follows that distinct complements intersect trivially:
\[
H_s\cap H_t=1
\qquad
(s\ne t).
\]
It also follows that every nontrivial cyclic subgroup other than \(R\) lies in exactly one \(H_t\): take any nonidentity generator outside \(R\), and use uniqueness of its complement.

There is no cyclic subgroup properly containing \(R\). Indeed every element outside \(R\) lies in some \(H_t\), hence has order dividing \(m\), while
\[
\gcd(r,m)=1.
\]
Thus \(R\) is adjacent only to the trivial subgroup and is a leaf.

Inside each \(H_t\), the cover relations among cyclic subgroups are exactly those of
\[
C_m.
\]
Between two different complements there are no additional nontrivial inclusion relations because their intersection is trivial. Therefore the whole cyclic-subgroup graph is obtained by identifying the trivial vertices of \(r\) disjoint copies of
\[
C(C_m)^*
\]
and then adjoining the leaf \(R\).

The number of cyclic subgroups of \(C_m\) is
\[
\tau(m).
\]
After identifying the \(r\) trivial vertices, the \(r\) copies contribute
\[
1+r(\tau(m)-1)
\]
vertices, and \(R\) contributes one more. Hence
\[
|C(G)|=2+r(\tau(m)-1).
\]

The cyclic group
\[
C_m
\]
has
\[
e(m)=
\tau(m)\sum_{i=1}^{k}\frac{a_i}{a_i+1}
\]
edges in its cyclic-subgroup graph. The \(r\) copies therefore contribute \(r e(m)\) edges, and the leaf \(R\) contributes one:
\[
|E(C(G)^*)|=1+r e(m).
\]

Since
\[
\gcd(r,m)=1,
\]
the cyclic group of order \(rm\) has prime-exponent vector obtained from that of \(m\) by adding one exponent equal to \(1\). Therefore
\[
|E(C_{rm})^*|
=
2\tau(m)
\left(
\frac12+
\sum_{i=1}^{k}\frac{a_i}{a_i+1}
\right)
=
\tau(m)+2e(m).
\]
Subtracting gives
\[
|E(C(G)^*)|-|E(C_{rm})^*|
=
(r-2)e(m)-(\tau(m)-1).
\]

The graph
\[
C(C_m)^*
\]
is connected and has \(\tau(m)\) vertices, so
\[
e(m)\ge\tau(m)-1.
\]
Because \(m\ge4\) is even and divides \(r-1\), one has \(r\ge5\). Consequently
\[
(r-2)e(m)-(\tau(m)-1)
\ge
(r-3)(\tau(m)-1)>0.
\]
This proves the strict inequality.

## Verification

The included replay constructs the semidirect products directly from the multiplication law
\[
(a,b)(c,d)
=
(a+u^b c,\;b+d),
\]
with the first coordinate modulo \(r\) and the second modulo \(m\), where \(u\) has multiplicative order \(m\) modulo \(r\).

For
\[
(r,m)=(5,4),(7,6),(13,4),(13,6),(17,8),(31,10),
\]
the replay independently:

- enumerates every element;
- enumerates every cyclic subgroup from the multiplication law;
- constructs every cover relation in the cyclic-subgroup poset;
- verifies
  \[
  |C(G)|=2+r(\tau(m)-1);
  \]
- verifies
  \[
  |E(C(G)^*)|=1+r e(m);
  \]
- verifies that the \(r\) complement copies meet only in the trivial subgroup;
- verifies that the normal subgroup of order \(r\) is a leaf;
- checks the strict comparison with the cyclic group of order \(rm\).

The edge counts obtained are
\[
11,29,27,53,52,125,
\]
whereas the corresponding cyclic groups have
\[
7,12,7,12,10,12
\]
edges.

The replay returns `VERIFY_OK`.

Finite enumeration is not used to prove the universal theorem.

## Relationship to prior work

Tărnăuceanu introduced the edge-count formula for cyclic-subgroup graphs and proved that, among finite nilpotent groups of a fixed order and among finite groups of a fixed odd order, the cyclic group minimizes the number of edges. The same paper explicitly conjectures the inequality for arbitrary even-order groups.

The later structural study of cyclic-subgroup graphs analyzes cyclic, dihedral, dicyclic, generalized quaternion, nilpotent, and minimal non-cyclic families. Its tabulated edge formulas include the dihedral boundary corresponding to a complement of order \(2\), but not the faithful prime-kernel Frobenius groups with composite even cyclic complement treated here.

The present theorem supplies an exact graph decomposition for that family, not only an inequality. The decomposition shows why the edge count scales by the number \(r\) of Frobenius complements and yields the conjectured lower bound strictly.

Targeted searches using cyclic-subgroup graph, Frobenius group, prime kernel, cyclic complement, semidirect product, and edge-count terminology did not locate this decomposition or the displayed formula.

## Limitations

The kernel is assumed to have prime order. For a noncyclic elementary-abelian or larger cyclic Frobenius kernel, cyclic subgroups outside the kernel need not organize into the same simple one-point-union pattern.

The complement is assumed cyclic and acts faithfully.

The theorem addresses the even-complement range
\[
m\ge4.
\]
The case
\[
m=2
\]
is the familiar dihedral boundary and is not part of the originality claim.

The theorem proves the published edge-minimality conjecture only for this Frobenius family, not for all finite groups of even order.

A semidirect-product treatment using equivalent Frobenius-complement terminology may exist outside the search vocabulary used here.

## References

1. M. Tărnăuceanu, “On the number of edges of cyclic subgroup graphs of finite groups,” arXiv:2302.05784v1, first public version 11 February 2023; *Archiv der Mathematik* 120 (2023), 349–353, DOI 10.1007/s00013-023-01846-1.
2. K. Sharma and A. Satyanarayana Reddy, “Cyclic Subgroup Graph of a Group,” arXiv:2409.13796v1, first public version 20 September 2024.
