# Three affine components in a nilpotent Leibniz endomorphism variety

## Finding

Fix an arbitrary field \(K\), with no restriction on its characteristic, and the three-dimensional left Leibniz algebra \(L\) with basis \(e_1,e_2,z\) and the only nonzero basis brackets
\[
[e_1,e_1]=[e_1,e_2]=z.
\]

Every Leibniz endomorphism has matrix
\[
T=\begin{pmatrix}a&b&0\\c&d&0\\u&v&t\end{pmatrix}
\]
relative to this basis. The reduced endomorphism variety is exactly the union of three geometrically irreducible components, each isomorphic to affine four-space:
\[
\begin{aligned}
C_0&:\ b=0,\quad d=a+c,\quad t=a(a+c),\\
C_1&:\ a=b=t=0,\\
C_2&:\ a+c=b+d=t=0.
\end{aligned}
\]
In all three components \(u,v\) are free. Their pairwise intersections have dimensions \(3,3,2\), with common triple intersection of dimension \(2\). Crucially,
\[
\overline{\operatorname{Aut}(L)}=C_0\ne\operatorname{End}(L)_{\mathrm{red}}.
\]
Thus the noninvertible endomorphisms contain two entire components that cannot be obtained as limits of automorphisms.

For every finite field \(\mathbf F_q\), including characteristic \(2\),
\[
\boxed{\#\operatorname{End}(L)=3q^4-2q^3,}
\qquad
\boxed{\#\{T:T^2=T\}=2q^2+2,}
\]
and
\[
\boxed{\#\{T:T\text{ is nilpotent}\}=q^2(2q-1).}
\]
The respective counts by matrix rank \(0,1,2,3\) are
\[
\boxed{1,\quad (q^2-1)(2q+1),\quad 2(q^2-1)(q^2-q),\quad q^2(q-1)^2.}
\]
The geometrically reduced endomorphism variety has Grothendieck class
\[
3\mathbb L^4-2\mathbb L^3
\]
and point-counting zeta function
\[
\boxed{Z(T)=\frac{(1-q^3T)^2}{(1-q^4T)^3}.}
\]

Every nonzero proper retract (the image of an idempotent Leibniz endomorphism other than the identity) is one-dimensional. The complete set of these retract subalgebras is
\[
K(e_2+s z),\qquad K(e_1-e_2+s z),\qquad s\in K.
\]
For finite \(K=\mathbf F_q\), there are exactly \(2q\) such retract lines, and each is the image of exactly \(q\) idempotent endomorphisms.

## Assumptions and scope

The bracket is the *left* Leibniz bracket. It satisfies the left Leibniz identity because the derived line \(Kz\) is central. The displayed endomorphism equations describe maps preserving this bracket; they do **not** refer to arbitrary linear maps or derivations.

The result is valid over every field, regardless of characteristic, and the geometric component statement concerns the **reduced** algebraic variety associated with the bracket-preservation equations. No claim is made here that its unreduced representing scheme has no additional infinitesimal structure.

The algebra occurs in the arbitrary-field structural classification of Kurdachenko–Pypka–Subbotin, publicly available 2 November 2022 (there labeled \(Lei_4(3,F)\)). The later Kurdachenko–Pypka–Semko automorphism paper, publicly available 30 April 2023, labels it \(Lei_3(3,F)\), gives the identical multiplication table, and classifies its automorphism group.

## Proof

For vectors written as \(x=(x_1,x_2,x_3)\), the bracket is
\[
[x,y]=x_1(y_1+y_2)z.
\]
Because \(z=[e_1,e_1]\), every bracket-preserving linear map sends \(z\) into the derived line \(Kz\). Consequently its matrix has the asserted block form. Put
\[
A=\begin{pmatrix}a&b\\c&d\end{pmatrix},\qquad
\ell=(1,0),\qquad m=(1,1).
\]
The homomorphism condition is exactly the rank-one tensor equation
\[
(A^\mathsf{T}\ell^\mathsf{T})(mA)=t\ell^\mathsf{T}m,
\]
or, componentwise,
\[
a(a+c)=t,\qquad a(b+d)=t,\qquad b(a+c)=0,\qquad b(b+d)=0.
\]
The central row \((u,v)\) is unrestricted.

If \(t\ne0\), equality of nonzero decomposable tensors forces \(\ell A=\alpha\ell\) and \(mA=\beta m\), with \(\alpha\beta=t\). In coordinates this gives
\[
b=0,\qquad d=a+c,\qquad t=a(a+c),
\]
with \(a\ne0\) and \(a+c\ne0\). Such \(T\) is invertible. This is the dense open automorphism group in \(C_0\).

If \(t=0\), then the outer product vanishes. Over a field one of its factors must be zero: either \(\ell A=0\), which is \(C_1\), or \(mA=0\), which is \(C_2\). Hence every endomorphism belongs to \(C_0\cup C_1\cup C_2\), and all matrices in those sets preserve the bracket. Each displayed component is parametrized polynomially and bijectively by four free coordinates, with a polynomial inverse. Hence each is an affine four-space, geometrically irreducible. They are distinct, so these are exactly the irreducible components. The nonzero-\(t\) automorphisms are Zariski dense in \(C_0\), while neither \(C_1\) nor \(C_2\) lies in \(C_0\), proving the closure assertion.

The intersection \(C_0\cap C_1\) is given by \(a=b=t=0\), \(d=c\), with free \(c,u,v\). The intersection \(C_0\cap C_2\) has \(b=d=t=0\), \(c=-a\), with free \(a,u,v\). Both are affine three-spaces. The intersection \(C_1\cap C_2\) and the triple intersection have \(a=b=c=d=t=0\), with free \(u,v\), and are affine two-spaces. Inclusion–exclusion gives the Grothendieck class and
\[
3q^4-2q^3
\]
points over every \(\mathbf F_q\).

The units are precisely those in \(C_0\) with \(a\ne0\) and \(a+c\ne0\), so there are \(q^2(q-1)^2\) rank-three endomorphisms. For \(t=0\), the \(2\times2\) block \(A\) has rank at most one. There are exactly \(2(q^2-1)\) nonzero such blocks: \(q^2-1\) in each of the two rank-one row-kernel planes. For every nonzero \(A\), the central row \((u,v)\) belongs to its one-dimensional row space for exactly \(q\) choices, yielding rank one; the other \(q^2-q\) choices yield rank two. If \(A=0\), there is one rank-zero map and \(q^2-1\) rank-one maps. This establishes the rank distribution.

For idempotents \(T^2=T\), the invertible case gives only the identity. In the noninvertible case \(t=0\), the conditions are
\[
A^2=A,\qquad (u,v)A=(u,v).
\]
A nonzero idempotent \(A\) in \(C_1\cup C_2\) is a rank-one projection whose image is one of the two fixed lines
\[
U=Ke_2,\qquad V=K(e_1-e_2)
\]
in the quotient \(L/Kz\). Each fixed line admits exactly \(q\) complementary kernel lines, hence exactly \(q\) projections \(A\). For each such projection, the central row lies in the one-dimensional row space of \(A\), giving exactly \(q\) choices. Including zero and identity yields \(2q^2+2\) idempotents. Their rank-one images are precisely the two asserted families of central lifts, each with \(q\) possible central shifts and \(q\) corresponding projections.

An endomorphism is nilpotent exactly when \(t=0\) and \(A\) is nilpotent. In \(C_1\), such \(A\) satisfy \(d=0\) and have \(q\) choices. In \(C_2\), such \(A\) satisfy \(a=b\) and have \(q\) choices. The two sets intersect only at \(A=0\), giving \(2q-1\) possible blocks, with \(q^2\) central rows each. Hence the nilpotent count is \(q^2(2q-1)\).

Over every extension \(\mathbf F_{q^m}\), the point count is \(3q^{4m}-2q^{3m}\). Substituting into the exponential definition of the zeta function gives the stated rational expression.

## Verification

The standalone Python checker `artifacts/verify.py` uses the original bracket table, not the asserted classification, to inspect **all** \(3\times3\) matrices over \(\mathbf F_2\) and \(\mathbf F_3\). For every matrix it independently verifies equivalence between the original nine bracket-preservation conditions and membership in the union of the three proposed components.

It independently computes ranks, squares, cubes, idempotents and nilpotents. For \(\mathbf F_5\), it forms the entire disjoint set-theoretic union from the three parametrizations and checks the same statistics. It returns `VERIFY_OK`. The reproducible output is embedded as `artifacts/verify_output.txt`.

The resulting totals for \(q=2,3,5\) are respectively
\[
\#\operatorname{End}=32,189,1625;
\]
for idempotents,
\[
10,20,52;
\]
and for nilpotents,
\[
12,45,225.
\]

Finite checks are evidence of consistency, not a proof for all fields. The case-independent proof is given above.

## Relationship to prior work

The 2022 full-text paper of Kurdachenko–Pypka–Subbotin includes this multiplication table within its structural classification of three-dimensional Leibniz algebras over arbitrary fields. It does not state a classification of the endomorphism variety or point counts.

The 2023 full-text automorphism paper of Kurdachenko–Pypka–Semko proves that the group of units consists precisely of matrices in \(C_0\) with nonzero parameters \(a\) and \(a+c\). This recovers exactly the unit stratum here. Its theorem does not cover the two additional irreducible components of noninvertible endomorphisms, nor the idempotent, nilpotent, and rank enumerations.

The 2021 work of Kurdachenko–Subbotin–Yashchuk studies the endomorphism monoid of **infinite-dimensional cyclic** Leibniz algebras. Its hypotheses do not apply to this finite-dimensional, noncyclic algebra.

Searches for the exact structure constants, alternate indexing labels, monoid/semigroup terminology, retracts, all-field classifications, and the count fingerprints did not find covering results.

## Limitations

The irreducible-component theorem is a theorem about the **reduced** endomorphism variety. No assertion about reducedness, smoothness, or embedded infinitesimal structure of the original scheme of homomorphism equations is made.

The counting formulas enumerate individual matrices preserving the **fixed bracket**, not endomorphism conjugacy classes or isomorphism classes of Leibniz algebras.

The search cannot exclude an uncatalogued equivalent semigroup computation under a different algebra label. A failed search is not an absolute novelty proof.

## References

1. L. A. Kurdachenko, O. O. Pypka, I. Ya. Subbotin, “On the inner structure of 3-dimensional Leibniz algebras,” arXiv:2211.01074v1, posted 2 November 2022, Section 2, especially the class labeled `Lei4(3,F)`.
2. L. A. Kurdachenko, O. O. Pypka, M. M. Semko, “Automorphism groups of some 3-dimensional Leibniz algebras,” arXiv:2305.00592v1, posted 30 April 2023, Theorem 3.1, especially `Lei3(3,F)`.
3. L. A. Kurdachenko, I. Ya. Subbotin, V. S. Yashchuk, “On the endomorphisms and derivations of some Leibniz algebras,” arXiv:2104.05922v1, posted 13 April 2021, Theorem A (infinite-dimensional cyclic case).
