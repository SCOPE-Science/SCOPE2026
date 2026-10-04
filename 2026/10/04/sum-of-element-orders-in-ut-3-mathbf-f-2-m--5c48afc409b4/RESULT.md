# Sum of element orders in \(UT_3(\mathbf F_{2^m})\)

## Finding

Let
\[
q=2^m,
\qquad m\ge1,
\]
and let
\[
H(q)=UT_3(\mathbf F_q)
\]
be the group of upper unitriangular \(3\)-by-\(3\) matrices over \(\mathbf F_q\). Then
\[
|H(q)|=q^3,
\]
and the element-order distribution is
\[
n_2(H(q))=2q^2-q-1,
\qquad
n_4(H(q))=q(q-1)^2.
\]
Hence
\[
\boxed{
\psi(H(q))=4q^3-4q^2+2q-1.
}
\]

Moreover,
\[
H(q)'=Z(H(q))=\Phi(H(q))
\]
has order \(q\). Thus \(H(q)\) is a nonabelian special \(2\)-group, and for \(m\ge2\) it is not extraspecial, generalized extraspecial, or almost extraspecial in the sense used in the motivating literature, because those latter families have derived subgroup of order \(2\).

The normalized sum satisfies
\[
\boxed{
\frac{\psi(H(q))}{|H(q)|}
=
4-\frac4q+\frac2{q^2}-\frac1{q^3}
\longrightarrow 4.
}
\]

Thus the explicit-sum problem for nonabelian special \(2\)-groups admits a closed solution on the canonical infinite nonextraspecial family \(UT_3(\mathbf F_{2^m})\), \(m\ge2\).

## Assumptions and scope

For a finite group \(G\), define
\[
\psi(G)=\sum_{g\in G} o(g),
\]
where \(o(g)\) is the order of \(g\).

Write an element of \(H(q)\) as
\[
g(a,b,c)=
\begin{pmatrix}
1&a&c\\
0&1&b\\
0&0&1
\end{pmatrix},
\qquad a,b,c\in\mathbf F_q.
\]
The group law is
\[
g(a,b,c)g(a',b',c')
=
g(a+a',b+b',c+c'+ab').
\]

The characteristic is \(2\). The statement covers all \(m\ge1\), but the genuinely new special-group range relative to the cited extraspecial calculations is \(m\ge2\). The case \(q=2\) is the dihedral group of order \(8\), so it is an extraspecial boundary check rather than part of the originality claim.

## Proof

The inverse calculation is immediate from the multiplication law, and a direct commutator calculation gives
\[
[g(a,b,c),g(a',b',c')]
=
g(0,0,ab'+a'b).
\]
Therefore every commutator lies in
\[
Z_0=\{g(0,0,c):c\in\mathbf F_q\}.
\]
Conversely, for every \(t\in\mathbf F_q\),
\[
[g(t,0,0),g(0,1,0)]=g(0,0,t),
\]
so
\[
H(q)'=Z_0.
\]

An element \(g(a,b,c)\) commutes with both \(g(1,0,0)\) and \(g(0,1,0)\) only when \(b=0\) and \(a=0\), respectively. Hence
\[
Z(H(q))=Z_0=H(q)'.
\]

Because \(H(q)\) is a finite \(2\)-group,
\[
\Phi(H(q))=H(q)^2H(q)'.
\]
In characteristic \(2\),
\[
g(a,b,c)^2=g(0,0,ab).
\]
Thus every square lies in \(Z_0\), while every element \(g(0,0,t)\) occurs as a square by taking \(a=t\) and \(b=1\). Therefore
\[
H(q)^2=Z_0,
\]
and consequently
\[
\Phi(H(q))=H(q)'=Z(H(q))=Z_0\cong C_2^m.
\]
This proves that \(H(q)\) is special.

The same square formula determines all element orders. The identity is \(g(0,0,0)\). A nonidentity element has order \(2\) precisely when
\[
ab=0.
\]
There are \(2q-1\) pairs \((a,b)\) with \(ab=0\): \(q\) with \(a=0\), \(q\) with \(b=0\), and the pair \((0,0)\) has been counted twice. For each such pair there are \(q\) choices of \(c\). Hence the number of elements whose square is the identity is
\[
q(2q-1).
\]
Removing the identity yields
\[
n_2(H(q))=q(2q-1)-1=2q^2-q-1.
\]

All remaining elements have square a nonidentity central involution, and therefore have order \(4\). Their number is
\[
\begin{aligned}
n_4(H(q))
&=q^3-1-n_2(H(q))\\
&=q^3-q(2q-1)\\
&=q(q-1)^2.
\end{aligned}
\]
It follows that
\[
\begin{aligned}
\psi(H(q))
&=1+2n_2(H(q))+4n_4(H(q))\\
&=1+2(2q^2-q-1)+4q(q-1)^2\\
&=4q^3-4q^2+2q-1.
\end{aligned}
\]
Dividing by \(q^3\) proves the normalized formula and limit.

For \(m\ge2\),
\[
|H(q)'|=q>2,
\]
so these groups lie outside the extraspecial, generalized extraspecial, and almost extraspecial \(2\)-group families treated in the cited 2024 paper, all of which impose derived subgroup of order \(2\).

## Verification

The included replay implements \(\mathbf F_{2^m}\) directly for
\[
m=1,2,3,4,
\]
so
\[
q=2,4,8,16.
\]
For every triple \((a,b,c)\), it constructs the group law and square, determines the element order without using the closed formula, and checks the resulting counts against
\[
n_2=2q^2-q-1,
\qquad
n_4=q(q-1)^2,
\qquad
\psi=4q^3-4q^2+2q-1.
\]
It also verifies directly that the central-coordinate subgroup is obtained both from commutators and from squares.

The replay produces the exact rows
\[
(q,n_2,n_4,\psi)
=(2,5,2,19),
(4,27,36,199),
(8,119,392,1807),
(16,495,3600,15391)
\]
and returns `VERIFY_OK`.

Finite enumeration is not used as the proof of the universal formula.

## Relationship to prior work

The 2024 paper *Element orders in extraspecial groups* defines special, extraspecial, almost extraspecial, and generalized extraspecial \(p\)-groups, and explicitly states that obtaining a formula for \(\psi(G)\) for a nonabelian special \(2\)-group remains open. It then solves the problem for the narrower extraspecial and generalized/almost extraspecial families. Its primary classification formulas for \(2\)-groups all stay in the regime where the derived subgroup has order \(2\).

The family \(H(q)=UT_3(\mathbf F_q)\) with \(q=2^m\) is special, but when \(m\ge2\) its derived subgroup has order \(q>2\). It is therefore outside those solved families. The calculation above supplies a closed sum-of-element-orders formula on a standard infinite family that crosses precisely that boundary.

Targeted searches using the unitriangular, finite-Heisenberg, special-\(2\)-group, element-order-distribution, and sum-of-element-orders formulations did not locate this arbitrary-\(m\) formula. Searches also found work on finite Heisenberg Lie-algebra commutativity and general unitriangular-group properties, but those address different invariants and do not imply the stated \(\psi\)-formula.

## Limitations

The result concerns the class-three matrix size \(UT_3\) over fields of characteristic \(2\). It does not give a formula for arbitrary special \(2\)-groups, nor for higher unitriangular groups.

The proof exploits the particularly simple square identity
\[
g(a,b,c)^2=g(0,0,ab).
\]
For larger unitriangular groups, higher nilpotency class introduces additional order strata.

The novelty claim is restricted to the nonextraspecial range \(m\ge2\). The boundary case \(q=2\) is already contained in known extraspecial calculations.

An equivalent element-order distribution could exist in older unitriangular-group literature under notation not captured by the searches; this remains the principal bibliographic risk.

## References

1. M.-S. Lazorec, “Element orders in extraspecial groups,” arXiv:2405.04141v1, first public version 7 May 2024.
2. M.-S. Lazorec, “Subgroups with a small sum of element orders,” arXiv:2404.05010v1, first public version 7 April 2024.
