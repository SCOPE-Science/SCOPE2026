# Cyclic-subgroup commutativity of extraspecial exponent-\(p\) groups

## Finding

Let \(p\) be an odd prime, and let \(G\) be an extraspecial group of exponent \(p\) and order
\[
|G|=p^{2n+1},
\qquad n\ge1.
\]
Put
\[
N=\frac{p^{2n}-1}{p-1},
\qquad
R=\frac{p^{2n-1}-1}{p-1}.
\]

Then
\[
\boxed{|L_1(G)|=pN+2.}
\]

The noncentral cyclic subgroups split into fibers of size \(p\), indexed by the projective points of the symplectic space
\[
G/Z(G)\cong \mathbf F_p^{2n}.
\]
Two noncentral cyclic subgroups commute exactly when their indexing projective points are orthogonal for the commutator symplectic form. Hence
\[
\boxed{
\operatorname{csd}(G)
=
\frac{p^2NR+4pN+4}{(pN+2)^2}.
}
\]

For \(n=1\),
\[
\operatorname{csd}(G)
=
\frac{p^3+5p^2+4p+4}{(p^2+p+2)^2},
\]
the previously recorded value for the nonabelian group of order \(p^3\) and exponent \(p\). For fixed \(p\),
\[
\boxed{
\lim_{n\to\infty}\operatorname{csd}(G)=\frac1p.
}
\]

Thus every reciprocal of an odd prime occurs as an accumulation point of cyclic subgroup commutativity degrees along this extraspecial family.

## Assumptions and scope

For a finite group \(X\),
\[
\operatorname{csd}(X)
=
\frac{
|\{(H,K)\in L_1(X)^2:HK=KH\}|
}{
|L_1(X)|^2
}.
\]

An extraspecial \(p\)-group satisfies
\[
Z(G)=G'=\Phi(G)
\]
and this common subgroup has order \(p\). The exponent-\(p\) hypothesis implies that every nonidentity element has order \(p\). For odd \(p\), the quotient
\[
V=G/Z(G)
\]
has dimension \(2n\) over \(\mathbf F_p\), and after fixing a generator \(z\) of \(Z(G)\),
\[
[x,y]=z^{B(\overline x,\overline y)}
\]
defines a nondegenerate alternating bilinear form \(B\).

The theorem is restricted to the exponent-\(p\) extraspecial type. Extraspecial groups of exponent \(p^2\) have additional cyclic-subgroup orders.

## Proof

Write \(Z=Z(G)\). Because \(G\) has exponent \(p\), every nonidentity cyclic subgroup has order \(p\). Therefore
\[
|L_1(G)|
=
1+\frac{|G|-1}{p-1}
=
1+\frac{p^{2n+1}-1}{p-1}
=
pN+2.
\]

Exactly one nontrivial cyclic subgroup is central, namely \(Z\), so there are \(pN\) noncentral cyclic subgroups.

Let
\[
\pi:G\to V=G/Z.
\]
If \(H\le G\) is noncentral and cyclic, then \(H\cap Z=1\), so \(\pi(H)\) is a one-dimensional subspace of \(V\).

Fix a projective point \(L\le V\). Its full preimage \(\pi^{-1}(L)\) has order \(p^2\). The commutator form vanishes on \(L\), so this preimage is abelian; exponent \(p\) makes it isomorphic to \(C_p^2\). It has \(p+1\) subgroups of order \(p\), one of which is \(Z\). Thus exactly \(p\) noncentral cyclic subgroups map onto \(L\).

There are
\[
N=\frac{p^{2n}-1}{p-1}
\]
projective points, recovering the count \(pN\).

Now let \(H,K\) be noncentral cyclic subgroups. Since both have order \(p\),
\[
HK=KH
\]
is equivalent to \([H,K]=1\). Indeed, if \(H\ne K\) and they permute, then \(HK\) is a subgroup of order \(p^2\), hence abelian. If \(L=\pi(H)\) and \(M=\pi(K)\), then
\[
[H,K]=1
\]
is equivalent to
\[
B(L,M)=0.
\]

For fixed \(L\), the orthogonal space \(L^\perp\) has dimension \(2n-1\), so it contains exactly
\[
R=\frac{p^{2n-1}-1}{p-1}
\]
projective points. Each contributes \(p\) noncentral cyclic subgroups. Hence every noncentral cyclic subgroup commutes with exactly
\[
pR
\]
noncentral cyclic subgroups, including itself, and therefore with \(pR+2\) cyclic subgroups after adding \(1\) and \(Z\).

The two universal cyclic subgroups \(1\) and \(Z\) each have \(pN+2\) partners. Thus the ordered commuting-pair count is
\[
2(pN+2)+pN(pR+2)
=
p^2NR+4pN+4.
\]
Division by \((pN+2)^2\) proves the formula.

For \(n=1\), \(N=p+1\) and \(R=1\), giving the known order-\(p^3\) formula. Finally,
\[
\frac{R}{N}
=
\frac{p^{2n-1}-1}{p^{2n}-1}
\longrightarrow
\frac1p,
\]
and the lower-order terms vanish after division by \(p^2N^2\), proving the limit.

## Verification

The included replay uses the standard Heisenberg model
\[
H_n(p)=\mathbf F_p^n\times\mathbf F_p^n\times\mathbf F_p
\]
with multiplication
\[
(x,y,z)(x',y',z')
=
(x+x',y+y',z+z'+x\cdot y').
\]

For
\[
(p,n)=(3,1),(3,2),(5,1),(5,2),
\]
the replay enumerates every cyclic subgroup from the multiplication law, identifies the center, verifies the \(p\)-to-one projective fibers, tests every ordered pair of cyclic subgroups for permutability, and checks the closed formula and the known \(n=1\) specialization.

The replay returns `VERIFY_OK`.

Finite computation is not used to prove the universal theorem.

## Relationship to prior work

Lazorec's 2017 work on probabilistic aspects of ZM-groups treats cyclic subgroup commutativity degree as a central invariant, develops explicit formulas for a substantial solvable family, studies asymptotic behavior, and ends with open problems about the range and structural behavior of cyclic subgroup commutativity degrees.

The earlier foundational paper computes the rank-one extraspecial boundary case:
\[
\operatorname{csd}(E(p^3))
=
\frac{p^3+5p^2+4p+4}{(p^2+p+2)^2}.
\]
It does not state an arbitrary-rank extraspecial formula.

The theorem here extends that isolated order-\(p^3\) calculation to every extraspecial exponent-\(p\) group and identifies the geometric mechanism: cyclic-subgroup commutation is a \(p\)-fold lift of projective symplectic orthogonality. It also yields the positive accumulation value \(1/p\), contrasting with the vanishing families emphasized in the 2017 ZM-group study.

Targeted searches for extraspecial groups, cyclic subgroup commutativity, symplectic orthogonality, and the order-\(p^{2n+1}\) parameterization did not locate an equivalent general formula.

## Limitations

The theorem does not cover extraspecial groups of exponent \(p^2\), nor extraspecial \(2\)-groups.

It determines cyclic subgroup commutativity degree, not ordinary subgroup commutativity degree.

The rank-one case was already known. The originality claim concerns the arbitrary-rank formula, the symplectic-fiber description, and the fixed-\(p\) limit.

An equivalent statement could exist under the language of symplectic polar spaces or subgroup-permutability graphs.

## References

1. M.-S. Lazorec, “Probabilistic aspects of ZM-groups,” arXiv:1712.06692v1, first public version 18 December 2017; later published in *Communications in Algebra* 47 (2019), 541–552, DOI 10.1080/00927872.2018.1482310.
2. M. Tărnăuceanu and M.-S. Lazorec, “Cyclic subgroup commutativity degrees of finite groups,” arXiv:1609.00476v1, first public version 2 September 2016; later published in *Rendiconti del Seminario Matematico della Università di Padova* 139 (2018), 225–240, DOI 10.4171/RSMUP/139-9.
