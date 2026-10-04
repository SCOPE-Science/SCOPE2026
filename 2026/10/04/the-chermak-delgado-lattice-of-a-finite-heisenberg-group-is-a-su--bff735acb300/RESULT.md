# The Chermak–Delgado lattice of a finite Heisenberg group is a subspace lattice

## Finding

Let \(q=p^f\) be a prime power and \(n\ge1\). Write the finite Heisenberg group as
\[
H_n(q)=\mathbf F_q^n\times\mathbf F_q^n\times\mathbf F_q
\]
with multiplication
\[
(x,y,z)(x',y',z')
=
(x+x',\,y+y',\,z+z'+x\cdot y').
\]
Its center is
\[
Z=\{(0,0,z):z\in\mathbf F_q\},
\]
and
\[
V=H_n(q)/Z\cong\mathbf F_q^{2n}.
\]
Equip \(V\) with the nondegenerate alternating form
\[
B((x,y),(x',y'))=x\cdot y'-x'\cdot y.
\]

Then the centralizer lattice and Chermak–Delgado lattice coincide:
\[
\boxed{
\mathcal{CD}(H_n(q))
=
\mathcal C(H_n(q))
=
\{\pi^{-1}(W):W\le_{\mathbf F_q}V\}.
}
\]
Consequently both are canonically isomorphic to the full subspace lattice
\[
L_{2n}(q),
\]
and the centralizer involution corresponds exactly to symplectic orthogonal complementation
\[
W\longmapsto W^\perp.
\]
In particular,
\[
|\mathcal{CD}(H_n(q))|
=
\sum_{d=0}^{2n}{2n\brack d}_q.
\]

The maximal Chermak–Delgado measure is
\[
\boxed{m^*(H_n(q))=q^{2n+2}.}
\]
More precisely, let \(K\) be any subgroup containing \(Z\), put
\[
U=K/Z,
\]
let
\[
s=\dim_{\mathbf F_p}U,
\]
and let
\[
d=\dim_{\mathbf F_q}\langle U\rangle_{\mathbf F_q}.
\]
Then
\[
\boxed{
m(K)=q^{2n+2}p^{\,s-fd}.
}
\]
Hence \(K\) has maximal measure if and only if \(U\) is already an \(\mathbf F_q\)-linear subspace.

There is a sharp monotonicity distinction. The Chermak–Delgado measure is constant, hence increasing, on the centralizer lattice for every \(q\). On the entire subgroup lattice it is increasing if and only if
\[
\boxed{q=p}
\]
is prime.

For \(n=1\), the subspace lattice \(L_2(q)\) is the previously known quasi-antichain of width \(q+1\). For \(n\ge2\), the result gives a higher-rank lattice with all intermediate subspace dimensions present.

## Assumptions and scope

For a finite group \(G\) and subgroup \(K\le G\), the Chermak–Delgado measure is
\[
m_G(K)=|K|\,|C_G(K)|.
\]
The Chermak–Delgado lattice consists of the subgroups attaining the maximum value of this measure. The centralizer lattice is the set of all subgroups of the form \(C_G(X)\), ordered by inclusion.

The notation \(H_n(q)\) here means the \(2n+1\)-dimensional Heisenberg group over the finite field \(\mathbf F_q\). This is not the same family as the three-dimensional Heisenberg group over the ring \(\mathbb Z/p^a\mathbb Z\).

## Proof

The commutator is
\[
[(x,y,z),(x',y',z')]
=
(0,0,B((x,y),(x',y'))).
\]
Thus \(Z\) is the displayed center and centralization modulo \(Z\) is exactly symplectic orthogonality.

First suppose \(K\ge Z\). Then \(U=K/Z\) is an additive subgroup of \(V\), hence an \(\mathbf F_p\)-subspace. Put
\[
S=\langle U\rangle_{\mathbf F_q},
\qquad
d=\dim_{\mathbf F_q}S,
\qquad
s=\dim_{\mathbf F_p}U.
\]
Because \(B\) is \(\mathbf F_q\)-bilinear,
\[
C_{H_n(q)}(K)/Z
=
U^\perp
=
S^\perp.
\]
Nondegeneracy gives
\[
\dim_{\mathbf F_q}S^\perp=2n-d.
\]
Therefore
\[
|K|=q\,p^s
\]
and
\[
|C_{H_n(q)}(K)|=q^{2n-d+1}.
\]
Multiplication yields
\[
m(K)
=
q^{2n-d+2}p^s
=
q^{2n+2}p^{s-fd}.
\]
Since \(U\subseteq S\),
\[
s\le fd,
\]
with equality exactly when \(U=S\), equivalently when \(U\) is \(\mathbf F_q\)-linear. Thus every subgroup containing \(Z\) has measure at most \(q^{2n+2}\), with equality exactly for the inverse images of \(\mathbf F_q\)-subspaces.

Now let \(K\) be arbitrary. Since \(Z\) is central,
\[
C(KZ)=C(K)
\]
and
\[
|KZ|=\frac{|K||Z|}{|K\cap Z|}.
\]
Hence
\[
m(K)
=
\frac{|K\cap Z|}{|Z|}\,m(KZ)
\le q^{2n+2},
\]
with equality only if \(Z\le K\) and \(K/Z\) is \(\mathbf F_q\)-linear. This proves the Chermak–Delgado description and the maximal measure.

For the centralizer lattice, every centralizer is the inverse image of an \(\mathbf F_q\)-subspace: if \(X\subseteq H_n(q)\) and \(S\) is the \(\mathbf F_q\)-span of its image in \(V\), then
\[
C(X)=\pi^{-1}(S^\perp).
\]
Conversely, if \(W\le_{\mathbf F_q}V\), nondegeneracy gives
\[
(W^\perp)^\perp=W,
\]
so
\[
\pi^{-1}(W)
=
C\!\left(\pi^{-1}(W^\perp)\right).
\]
Thus the centralizer lattice is exactly the same collection.

Every centralizer therefore has measure \(q^{2n+2}\), so the measure is constant on the centralizer lattice.

Finally consider monotonicity on all subgroups. If \(f=1\), every additive subgroup of \(V\) is an \(\mathbf F_q=\mathbf F_p\)-subspace, so every subgroup containing \(Z\) has maximal measure. The general monotonicity criterion of Cocke and McCulloch then gives that \(m\) is increasing on the entire subgroup lattice.

If \(f>1\), take a nonzero \(v\in V\) and
\[
U=\mathbf F_pv.
\]
Then \(U\) has \(\mathbf F_p\)-dimension \(1\) but \(\mathbf F_q\)-span of dimension \(1\). For \(K=\pi^{-1}(U)\),
\[
Z<K
\]
while
\[
m(Z)=q^{2n+2}
>
q^{2n+2}p^{1-f}
=
m(K).
\]
Thus monotonicity fails. This proves the if-and-only-if statement.

## Verification

The included replay independently checks the finite-field linear algebra behind the proof.

It exhaustively enumerates all additive subspaces in the cases
\[
(n,q)=(2,2),\quad (2,3),\quad (1,4).
\]
For each additive subspace \(U\), it constructs its \(\mathbf F_q\)-span, computes its symplectic annihilator directly, and verifies
\[
|U^\perp|=q^{2n-d}.
\]
It then checks the exact measure formula
\[
m(\pi^{-1}(U))
=
q^{2n+2}p^{s-fd}
\]
and verifies that maximal measure occurs exactly for \(\mathbf F_q\)-linear subspaces.

For \((n,q)=(1,4)\), the replay explicitly detects non-\(\mathbf F_4\)-linear additive lines and verifies the strict drop from \(m(Z)\), while for the prime-field cases every additive subspace is field-linear.

The replay returns `VERIFY_OK`.

Finite enumeration is not used to prove the theorem.

## Relationship to prior work

Cocke and McCulloch give necessary and sufficient criteria for the Chermak–Delgado measure to be increasing on the subgroup lattice or on the centralizer lattice. Their Proposition 10 recalls the general characterization of finite \(p\)-groups whose entire interval above the center equals the centralizer lattice, and their Theorem B characterizes monotonicity on centralizers by
\[
\mathcal C(G)=\mathcal{CD}(G).
\]
They also discuss the three-dimensional unitriangular group over \(GF(p^a)\): its centralizer and Chermak–Delgado lattices form a quasi-antichain of width \(p^a+1\). That is exactly the \(n=1\) boundary of the present statement.

The present result identifies the complete higher-rank structure. For \(H_n(q)\), every centralizer is the inverse image of an \(\mathbf F_q\)-subspace of the \(2n\)-dimensional symplectic quotient, and every such inverse image has maximal Chermak–Delgado measure. Thus the quasi-antichain at \(n=1\) expands to the full subspace lattice \(L_{2n}(q)\).

Allen, La Luz, Majewicz, and Zyman study the Chermak–Delgado measure of the different family of Heisenberg groups over \(\mathbb Z/p^a\mathbb Z\). Their public 2024 preprint computes the maximal measure for that ring-based three-dimensional family; it does not state the finite-field higher-rank subspace-lattice theorem above.

Targeted searches for “Heisenberg group”, “Chermak–Delgado lattice”, “finite field”, “centralizer lattice”, and “subspace lattice” did not locate an equivalent published statement. A current faculty research page does list “the Chermak–Delgado lattice of finite Heisenberg groups” as an active project, so possible unpublished or not-yet-indexed overlap remains a specific bibliographic risk.

## Limitations

The theorem is for the standard Heisenberg group over a finite field. It does not describe Heisenberg groups over nonfields such as \(\mathbb Z/p^a\mathbb Z\), where submodules need not be vector spaces and the centralizer geometry is different.

The result identifies the lattice and its measure but does not classify automorphisms of the Chermak–Delgado lattice beyond the evident finite-geometry interpretation.

The \(n=1\) quasi-antichain case is prior work and is included as a boundary of the uniform theorem, not claimed as new.

A faculty research page indicates ongoing work specifically on Chermak–Delgado lattices of finite Heisenberg groups. No public theorem matching the higher-rank finite-field statement was located; this remains the main residual originality risk.

## References

1. W. Cocke and R. McCulloch, “The Chermak–Delgado measure as a map on posets,” *Archiv der Mathematik* 123 (2024), 241–251, first published 22 August 2024, DOI 10.1007/s00013-024-02015-8. MSC 20D30, 20E15.
2. D. Allen, J. J. La Luz, S. Majewicz, and M. Zyman, “Pseudocentralizers and the Chermak Delgado Measure of the Mod \(p^n\) Heisenberg Group,” arXiv:2405.07080v1, first public 11 May 2024.
3. L. An, “Groups whose Chermak–Delgado lattice is a quasi-antichain,” *Journal of Group Theory* 22 (2019), 529–544.
