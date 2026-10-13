# Dihedral–dicyclic pseudo-algebra collisions obey a parity law

## Finding

For \(n\ge2\), let
\[
\operatorname{Dic}_n
=
\langle a,x\mid a^{2n}=1,\ x^2=a^n,\ x^{-1}ax=a^{-1}\rangle
\]
be the dicyclic group of order \(4n\), and let
\[
D_{4n}
=
\langle a,s\mid a^{2n}=s^2=1,\ sas=a^{-1}\rangle
\]
be the dihedral group of order \(4n\).

For a finite group \(G\), write
\[
\operatorname{cod}(\chi)=\frac{|G:\ker\chi|}{\chi(1)}
\]
and let \(m_G(d)\) be the number of irreducible characters of codegree \(d\).

For every divisor \(d>2\) of \(2n\), both groups have exactly
\[
\boxed{\frac{\varphi(d)}2}
\]
nonlinear irreducible characters of codegree \(d\).

The complete pseudo-algebras are
\[
\boxed{
C(D_{4n})
=
\{(1,1),(2,3)\}
\cup
\left\{
\left(d,\frac{\varphi(d)}2\right):d\mid2n,\ d>2
\right\}.
}
\]
For the dicyclic group,
\[
\boxed{
C(\operatorname{Dic}_n)
=
\begin{cases}
\{(1,1),(2,3)\}\cup
\left\{\left(d,\frac{\varphi(d)}2\right):d\mid2n,\ d>2\right\},&2\mid n,\\[6pt]
\{(1,1),(2,1),(4,2)\}\cup
\left\{\left(d,\frac{\varphi(d)}2\right):d\mid2n,\ d>2\right\},&2\nmid n.
\end{cases}
}
\]

Therefore
\[
\boxed{
C(\operatorname{Dic}_n)=C(D_{4n})
\iff
2\mid n.
}
\]

For every even \(n\), the two groups are nonisomorphic despite having the same order and the same pseudo-algebra. Indeed, \(\operatorname{Dic}_n\) has a unique involution \(a^n\), whereas \(D_{4n}\) has the central involution \(a^n\) together with all \(2n\) reflections.

Thus the group pseudo-algebra is completely blind to the split-versus-dicyclic distinction precisely in the even-parameter half of this canonical metacyclic pair.

## Assumptions and scope

The notation \(D_{4n}\) means the dihedral group of order \(4n\), so its rotation subgroup has order \(2n\).

The group pseudo-algebra is the codegree-multiplicity set
\[
C(G)=\{(d,m_G(d)):d\in\operatorname{cod}(G)\}.
\]

The result is for the ordinary dicyclic and dihedral families. It does not assert an analogous formula for arbitrary generalized dicyclic groups over noncyclic abelian kernels.

The parameter range starts at \(n=2\), where \(\operatorname{Dic}_2\cong Q_8\) and the first collision is
\[
C(Q_8)=C(D_8)=\{(1,1),(2,3),(4,1)\}.
\]

## Proof

Fix a primitive \(2n\)-th root of unity \(\zeta\).

Both groups have \(n-1\) irreducible characters of degree \(2\), indexed by
\[
k=1,2,\ldots,n-1.
\]
For the dihedral group one may take
\[
\rho_k(a)=
\begin{pmatrix}
\zeta^k&0\\
0&\zeta^{-k}
\end{pmatrix},
\qquad
\rho_k(s)=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
\]
For the dicyclic group one may use the same matrix for \(a\) and
\[
\rho_k(x)=
\begin{pmatrix}
0&(-1)^k\\
1&0
\end{pmatrix}.
\]
Then
\[
\rho_k(x)^2=(-1)^kI=\rho_k(a)^n
\]
and
\[
\rho_k(x)^{-1}\rho_k(a)\rho_k(x)=\rho_k(a)^{-1},
\]
so these are representations of \(\operatorname{Dic}_n\).

In either group, no element outside \(\langle a\rangle\) lies in the kernel of \(\rho_k\): the representing matrix is off-diagonal. On the rotation subgroup,
\[
\rho_k(a^j)=I
\iff
2n\mid kj.
\]
Therefore
\[
|\ker\rho_k|=\gcd(2n,k)
\]
and
\[
\operatorname{cod}(\rho_k)
=
\frac{4n}{2\gcd(2n,k)}
=
\frac{2n}{\gcd(2n,k)}.
\]

For a divisor \(d>2\) of \(2n\), the residue classes modulo \(2n\) of exact additive order \(d\) number \(\varphi(d)\). They occur in inverse pairs
\[
\{k,2n-k\},
\]
and each pair contains exactly one representative with
\[
1\le k\le n-1.
\]
Hence exactly
\[
\frac{\varphi(d)}2
\]
of the degree-two irreducibles have codegree \(d\). This proves that the nonlinear parts of the two pseudo-algebras coincide.

It remains to compare the linear characters.

For \(D_{4n}\), the abelianization is always
\[
D_{4n}^{\mathrm{ab}}\cong C_2\times C_2,
\]
so there are three nonprincipal linear characters, each of codegree \(2\).

For \(\operatorname{Dic}_n\), abelianization imposes
\[
a=a^{-1},
\qquad
x^2=a^n.
\]
Thus \(a^2=1\). If \(n\) is even, then \(a^n=1\) and
\[
\operatorname{Dic}_n^{\mathrm{ab}}\cong C_2\times C_2.
\]
Again the three nonprincipal linear characters all have codegree \(2\).

If \(n\) is odd, then \(a^n=a\) and \(x^2=a\), so
\[
\operatorname{Dic}_n^{\mathrm{ab}}\cong C_4.
\]
Its four linear characters have codegrees
\[
1,
\quad
2,
\quad
4,
\quad
4.
\]
Because \(4\nmid2n\) when \(n\) is odd, the codegree \(4\) does not merge with a nonlinear contribution.

This gives the two displayed formulas and proves the parity criterion.

Finally, the two groups are nonisomorphic. Every element outside \(\langle a\rangle\) in \(\operatorname{Dic}_n\) squares to \(a^n\), so it has order \(4\); hence \(a^n\) is the unique involution. In \(D_{4n}\), all \(2n\) reflections are involutions in addition to \(a^n\).

## Verification

The included checker evaluates the nonlinear kernel formula directly for every
\[
2\le n\le80.
\]
For each \(k\in\{1,\ldots,n-1\}\), it computes
\[
\frac{2n}{\gcd(2n,k)}
\]
and compares the resulting multiplicity table with
\[
\frac{\varphi(d)}2
\]
for every divisor \(d>2\) of \(2n\).

It then appends the correct linear-character contribution for both groups and verifies
\[
C(\operatorname{Dic}_n)=C(D_{4n})
\]
exactly for even \(n\), and inequality exactly for odd \(n\).

The checker also verifies the degree-squared identity
\[
4\cdot1^2+(n-1)\cdot2^2=4n
\]
and the involution counts
\[
1
\quad\text{for }\operatorname{Dic}_n,
\qquad
2n+1
\quad\text{for }D_{4n}.
\]

The checker returns `VERIFY_OK`.

Finite arithmetic checks are not used to prove the infinite family.

## Relationship to prior work

Lewis and Yan study the group pseudo-algebra, construct different-order collisions, and prove rigidity results for several classes of finite \(p\)-groups. Their full searchable preprint contains no occurrence of “dicyclic” or “dihedral”.

Moretó introduced the group pseudo-algebra and asked what structural information it determines. His full searchable article likewise contains no dicyclic or dihedral treatment.

The ordinary character table of dicyclic groups is classical. A public full-text source by Ćaćić, Marcolli, and Teh displays the four linear characters and the \(n-1\) degree-two characters for both parity cases. That table supplies standard character-theoretic background, but it does not compute codegree multiplicities or compare dicyclic and dihedral pseudo-algebras.

The result here identifies the exact pseudo-algebras of both same-order families and isolates the parity condition under which the invariant loses the split-versus-dicyclic distinction.

Targeted searches using dicyclic, dihedral, pseudo-algebra, character-codegree, and exact-multiplicity formulations did not locate this parity classification.

## Limitations

The irreducible-character parametrizations are standard. The new content is the codegree-multiplicity formula and the exact collision criterion.

The result compares the ordinary cyclic-kernel dicyclic and dihedral groups; generalized dicyclic groups over arbitrary abelian kernels are not treated.

The existence of an equivalent calculation in older codegree literature under different terminology remains a bibliographic risk.

Failed searches do not prove novelty.

## References

1. M. L. Lewis and Q. Yan, “On the group pseudo-algebra of finite groups,” arXiv:2402.12648v1, first public version 20 February 2024; *Comptes Rendus. Mathématique* 362 (2024), 1661–1665, DOI 10.5802/crmath.671. MSC 2020: 20C15, 20D15.
2. A. Moretó, “Multiplicities of character codegrees of finite groups,” *Bulletin of the London Mathematical Society* 55 (2023), 234–241, first published online 8 September 2022, DOI 10.1112/blms.12724.
3. B. Ćaćić, M. Marcolli, and K. Teh, “Coupling of gravity to matter, spectral action and cosmic topology,” *Journal of Noncommutative Geometry* 8 (2014), 473–504, DOI 10.4171/JNCG/162; Section 2.4 records the dicyclic character table.
