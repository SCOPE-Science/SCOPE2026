# Relative subgroup commutativity in irreducible elementary-abelian Frobenius groups

## Finding

Let \(p\) and \(q\) be distinct primes, let \(r\ge2\), let
\[
V\cong C_p^r,
\]
and let
\[
G=V\rtimes C_q,
\]
where the nontrivial action of \(C_q\) on \(V\) is irreducible over \(\mathbf F_p\).

For \(d\ge0\), write \(s_d(p)\) for the number of subspaces of \(\mathbf F_p^d\):
\[
s_d(p)
=
\sum_{i=0}^{d}
\prod_{j=0}^{i-1}
\frac{p^{d-j}-1}{p^{i-j}-1}.
\]
Put
\[
s=s_r(p),\qquad P=p^r,\qquad L=s+P+1.
\]

Then
\[
|L(G)|=L,
\]
and every subgroup of \(G\) is exactly one of the following: a subspace of \(V\), one of the \(P\) complements of order \(q\), or \(G\) itself.

The relative subgroup commutativity degree
\[
sd(H,G)
=
\frac{
|\{(H_1,G_1)\in L(H)\times L(G):H_1G_1=G_1H_1\}|
}{
|L(H)|\,|L(G)|
}
\]
is completely explicit:
\[
\boxed{sd(1,G)=1.}
\]
If
\[
0<\dim_{\mathbf F_p}H=d<r,
\]
then
\[
\boxed{
sd(H,G)
=
\frac{s_d(p)(s+1)+P}{s_d(p)L}.
}
\]
For the kernel,
\[
\boxed{
sd(V,G)
=
\frac{s(s+1)+2P}{sL}.
}
\]
For every complement \(C\cong C_q\),
\[
\boxed{
sd(C,G)
=
\frac{L+4}{2L}.
}
\]
Finally,
\[
\boxed{
sd(G)
=
\frac{s^2+2s+7P+1}{L^2}.
}
\]

Among nonzero proper subspaces the value depends only on dimension and is strictly decreasing with dimension, since
\[
sd(H,G)
=
\frac{s+1}{L}
+
\frac{P}{s_d(p)L}
\]
and \(s_d(p)\) strictly increases with \(d\).

## Assumptions and scope

The action is irreducible and nontrivial. Since the acting group has prime order \(q\), every nonidentity element of \(C_q\) generates the same group. A nonzero fixed vector for one such element would therefore give a nonzero invariant subspace; irreducibility would force the whole action to be trivial. Hence every nonidentity complement element fixes no nonzero vector, and \(G\) is a Frobenius group.

The result concerns the relative subgroup commutativity degree \(sd(H,G)\). The case \(H=G\) is the ordinary subgroup commutativity degree.

The rank condition \(r\ge2\) isolates the noncyclic-kernel case. Rank-one kernels are cyclic and belong to previously studied cyclic-by-cyclic semidirect-product families.

## Proof

Write
\[
G=V\rtimes\langle c\rangle,\qquad |c|=q.
\]

Let \(H\le G\) and suppose \(H\nleq V\). The projection \(G\to C_q\) maps \(H\) onto all of \(C_q\). The subgroup
\[
H\cap V
\]
is invariant under conjugation by \(H\). Choose \(vc^j\in H\) with \(j\ne0\). Since \(V\) is abelian, conjugation by \(vc^j\) on \(V\) equals conjugation by \(c^j\). As \(q\) is prime,
\[
\langle c^j\rangle=\langle c\rangle.
\]
Thus \(H\cap V\) is \(C_q\)-invariant, so irreducibility gives
\[
H\cap V=0\quad\text{or}\quad H\cap V=V.
\]
In the second case \(H=G\); in the first case \(H\cong C_q\) is a complement.

All complements are conjugate by \(V\). The normalizer in \(V\) of a fixed complement is the fixed-point space of its action, which is zero. Hence there are exactly
\[
|V|=P
\]
complements. Therefore
\[
|L(G)|=s+P+1=L.
\]

Now count permuting partners.

The trivial subgroup, \(V\), and \(G\) permute with every subgroup, so each has \(L\) partners.

Let \(0<U<V\). Since \(V\) is abelian, \(U\) permutes with every subspace of \(V\), and it permutes with \(G\). It permutes with no complement. Indeed, if a complement \(C\) satisfied \(UC=CU\), then \(UC\) would be a subgroup. Since \(V\trianglelefteq G\),
\[
(UC)\cap V=U
\]
would be normal in \(UC\); hence \(C\) would normalize \(U\), contradicting irreducibility. Thus \(U\) has exactly
\[
s+1
\]
partners.

A complement \(C\) permutes with \(1\), \(V\), itself, and \(G\). It has no nonzero proper kernel-subspace partner by the preceding argument. Two distinct complements cannot permute: if \(C\ne D\) and \(CD=DC\), then \(CD\) would be a subgroup of order \(q^2\), impossible because
\[
q^2\nmid |G|=p^rq.
\]
Thus each complement has exactly four partners.

For a nonzero proper \(d\)-dimensional subspace \(H\), the subgroup lattice \(L(H)\) has \(s_d(p)\) elements. Its trivial subgroup has \(L\) partners and each of its other \(s_d(p)-1\) subgroups has \(s+1\) partners. Hence
\[
L+\bigl(s_d(p)-1\bigr)(s+1)
=
s_d(p)(s+1)+P,
\]
giving the stated \(sd(H,G)\).

For \(H=V\), the trivial subgroup and \(V\) each have \(L\) partners, while the other \(s-2\) subspaces each have \(s+1\), so the numerator is
\[
2L+(s-2)(s+1)=s(s+1)+2P.
\]

For a complement \(C\), \(L(C)\) has two elements whose partner counts are \(L\) and \(4\), giving
\[
sd(C,G)=\frac{L+4}{2L}.
\]

Finally, summing partner counts over all of \(L(G)\) gives
\[
3L+(s-2)(s+1)+4P
=
s^2+2s+7P+1,
\]
and division by \(L^2\) proves the global formula.

## Verification

The included replay constructs irreducible fixed-point-free actions for
\[
(p,r,q)=(2,2,3),\quad(2,3,7),\quad(5,2,3).
\]
For each case it enumerates all subspaces of \(V\), constructs the \(p^r\) complements, builds the claimed complete subgroup list, tests every subgroup pair directly by comparing \(HK\) with \(KH\), and computes \(sd(H,G)\) for every subgroup from the definition.

The direct computations agree with every closed formula. In particular,
\[
sd(C_2^2\rtimes C_3)=\frac{16}{25},
\]
\[
sd(C_2^3\rtimes C_7)=\frac{69}{125},
\]
and
\[
sd(C_5^2\rtimes C_3)=\frac{64}{289}.
\]

The replay returns `VERIFY_OK`.

Finite enumeration is not used as the proof of the universal statement.

## Relationship to prior work

The 2018 paper *Finite groups with two relative subgroup commutativity degrees* develops the function
\[
H\longmapsto sd(H,G)
\]
and studies groups for which this function takes very few values. Its explicit semidirect-product calculations use cyclic normal kernels, including groups of the form
\[
C_p\rtimes C_{q^n}.
\]
Those formulas do not cover a noncyclic elementary abelian kernel.

Related work on probabilistic aspects of ZM-groups likewise concerns groups whose Sylow subgroups are cyclic, excluding
\[
V\cong C_p^r
\]
for \(r\ge2\).

The theorem here instead uses the full subspace lattice of \(V\) and irreducibility of the complement action. It determines the entire relative function, not only \(sd(G)\): proper subspaces are controlled by dimension, the kernel has a separate value, and all complements have one common value.

Targeted searches using relative subgroup commutativity, Frobenius-group, elementary-abelian-kernel, affine-semidirct-product, and subgroup-permutability formulations found no equivalent formula for this family.

## Limitations

The theorem requires irreducibility. If the complement stabilizes a proper nonzero subspace, that subspace can permute with complements and the formulas change.

The complement is required to have prime order. Composite complements introduce intermediate projected subgroups.

The kernel is elementary abelian. Non-elementary abelian Frobenius kernels have different invariant-subgroup lattices.

An equivalent calculation could exist under different affine-Frobenius or subgroup-permutability terminology.

## References

1. M. Lazorec and M. Tărnăuceanu, “Finite groups with two relative subgroup commutativity degrees,” arXiv:1801.09133v1, first public version 27 January 2018; *Publicationes Mathematicae Debrecen* 94 (2019), 157–169, DOI 10.5486/PMD.2019.8290.
2. M.-S. Lazorec and M. Tărnăuceanu, “Probabilistic aspects of ZM-groups,” arXiv:1712.06692; later published in *Communications in Algebra* 47 (2019), 1973–1985.
