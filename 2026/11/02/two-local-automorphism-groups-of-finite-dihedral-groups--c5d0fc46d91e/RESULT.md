# Two-local automorphism groups of finite dihedral groups

## Finding

A *two-local automorphism* of a group \(G\) is a map \(F:G\to G\) such that, for every ordered pair \((x,y)\), there is an automorphism \(\alpha_{x,y}\in\operatorname{Aut}(G)\) with \(F(x)=\alpha_{x,y}(x)\) and \(F(y)=\alpha_{x,y}(y)\). Such a map is automatically injective, and hence bijective when \(G\) is finite. Its collection is therefore a group under composition, denoted \(\operatorname{Loc}_2(G)\).

Let \(n\ge3\) and
\[
D_{2n}=\langle r,s\mid r^n=s^2=1,\ srs=r^{-1}\rangle
\]
be the dihedral group of order \(2n\). Write \(U_n=(\mathbb Z/n\mathbb Z)^\times\), and define
\[
\mathcal I_n=\{\pi\in\operatorname{Sym}(\mathbb Z/n\mathbb Z):
\gcd(\pi(i)-\pi(j),n)=\gcd(i-j,n)\text{ for all }i,j\}.
\]
Here a greatest common divisor of a residue and \(n\) is independent of the integer representative.

**Theorem.** Every two-local automorphism has the **unique** form
\[
F_{u,\pi}(r^i)=r^{ui},\qquad F_{u,\pi}(r^is)=r^{\pi(i)}s,
\quad u\in U_n,\ \pi\in\mathcal I_n,
\]
and every displayed map is two-local. As a group,
\[
\operatorname{Loc}_2(D_{2n})\cong U_n\times\mathcal I_n
\cong U_n\times\prod_{p^e\parallel n}W_{p,e},
\]
where \(W_{p,e}\) is the automorphism group of the rooted \(p\)-ary tree of depth \(e\), acting on its \(p^e\) leaves. Equivalently, \(W_{p,e}\) is the \(e\)-fold iterated imprimitive wreath product of \(S_p\). Consequently,
\[
\boxed{\bigl|\operatorname{Loc}_2(D_{2n})\bigr|=
\varphi(n)\prod_{p^e\parallel n}(p!)^{(p^e-1)/(p-1)}.}
\]
The automorphisms themselves are precisely the pairs with \(\pi(i)=ui+b\) for some \(b\in\mathbb Z/n\mathbb Z\), and number \(n\varphi(n)\). Thus the exact index is
\[
\boxed{[\operatorname{Loc}_2(D_{2n}):\operatorname{Aut}(D_{2n})]
=\frac1n\prod_{p^e\parallel n}(p!)^{(p^e-1)/(p-1)}.}
\]
It is strictly greater than one for all \(n\ge3\). In particular, for a prime \(p\ge3\), the index equals \((p-1)!\). The boundary groups have \(\operatorname{Loc}_2(D_2)=\operatorname{Aut}(D_2)\) of order one and \(\operatorname{Loc}_2(D_4)=\operatorname{Aut}(D_4)\) of order six, with the convention \(D_4\cong C_2\times C_2\).

## Assumptions and scope

All groups and sets are finite, the integer \(n\) is arbitrary with \(n\ge3\) unless an exception is explicitly stated, and maps are **not** initially assumed homomorphisms or bijections. Locality always means interpolation at *two arbitrary points by one global automorphism*. This should not be confused with the local-subgroup terminology of finite-group theory or with one-point orbit preservation. The full group \(D_{2n}\), not just its reflection conjugacy class, is the domain.

## Proof

**1. Automorphisms of a dihedral group.** For \(n\ge3\), the rotation subgroup \(\langle r\rangle\) is the unique cyclic subgroup of order \(n\): every element outside it has order two. It is therefore characteristic. Any automorphism sends \(r\) to \(r^a\) for a unique unit \(a\in U_n\); it sends \(s\) to some \(r^b s\), because the images must generate the whole dihedral group. Conversely each choice of \(a\in U_n\) and \(b\in\mathbb Z/n\mathbb Z\) respects the defining relations and is surjective, hence is an automorphism. Denote it by \(\alpha_{a,b}\). Its action is
\[
\alpha_{a,b}(r^i)=r^{ai},\qquad \alpha_{a,b}(r^is)=r^{ai+b}s.
\]
In particular, there are \(n\varphi(n)\) automorphisms.

**2. Pairwise interpolation fixes one global rotation multiplier.** Let \(F\) be two-local. A pair with distinct points cannot have equal images, since no automorphism maps distinct points to the same element. Hence \(F\) is injective and, since the group is finite, bijective. Any automorphism fixes the identity, so \(F(1)=1\). Interpolation at \((r,r^i)\) shows that a *single* unit \(u\), determined by \(F(r)=r^u\), satisfies \(F(r^i)=r^{ui}\) for every \(i\). Interpolation at \((r^is,r^js)\) implies \(F\) maps reflections to reflections, and injectivity gives a permutation \(\pi\) of their \(n\) indices such that \(F(r^is)=r^{\pi(i)}s\).

**3. Exact criterion for two reflections.** For residues \(d,d'\) modulo \(n\), there exists a unit \(a\in U_n\) with \(ad=d'\) if and only if \(\gcd(d,n)=\gcd(d',n)\). The forward implication is immediate. For the reverse, write \(n=\prod p^e\). The gcd condition gives the same \(p\)-adic order \(t\), capped at \(e\), for \(d\) and \(d'\). If \(t<e\), the congruence \(ad\equiv d'\pmod {p^e}\) is equivalent after division by \(p^t\) to a congruence that fixes a unit \(a\pmod {p^{e-t}}\); this unit can be lifted to a unit modulo \(p^e\). If \(t=e\), the congruence is automatic. The Chinese remainder theorem combines the choices across primes.

To interpolate at two reflections with indices \(i,j\), an automorphism \(\alpha_{a,b}\) must satisfy \(ai+b=\pi(i)\) and \(aj+b=\pi(j)\). By the preceding lemma this is possible exactly when
\[
\gcd(\pi(i)-\pi(j),n)=\gcd(i-j,n).
\]
Thus the reflection permutation must belong to \(\mathcal I_n\). Conversely, if it does, the lemma supplies an \(a\in U_n\), and then \(b=\pi(i)-ai\) supplies the required automorphism. For a mixed pair \((r^i,r^js)\), use \(\alpha_{u,\pi(j)-uj}\); for two rotations, use \(\alpha_{u,0}\). These cases prove both necessity and sufficiency of the displayed normal form. Composition is coordinatewise, giving the first direct product.

**4. Arithmetic decomposition and order.** Under the Chinese remainder identification
\[
\mathbb Z/n\mathbb Z\cong\prod_{p^e\parallel n}\mathbb Z/p^e\mathbb Z,
\]
a gcd-preserving permutation must preserve, for each prime \(p\mid n\) and every \(1\le k\le e\), the equivalence relation \(i\equiv j\pmod {p^k}\). In particular, its \(p\)-coordinate depends only on the input \(p\)-coordinate: equality modulo \(p^e\) forces equality of output \(p\)-coordinates, regardless of other prime coordinates. The inverse permutation has the same congruence-preservation property, so each induced coordinate map is a bijection. Conversely, independent permutations of the prime-power coordinates preserving all the associated congruence relations preserve the gcd of every difference.

Residues modulo \(p^e\) are the leaves of a rooted tree: the vertices at level \(k\) are residue classes modulo \(p^k\), and each vertex has \(p\) children. Permutations preserving all congruence partitions are precisely automorphisms of this rooted tree. There are \(1+p+\cdots+p^{e-1}=(p^e-1)/(p-1)\) internal nodes and an independent choice of a permutation of \(p\) children at each node. The tree-automorphism order is therefore \((p!)^{(p^e-1)/(p-1)}\). Multiplication over the primes proves both the group structure and exact order formula.

**5. Automorphism subgroup, strictness and small cases.** Comparison with the formula in step 1 shows that a two-local map is a homomorphism exactly when its reflection permutation is \(i\mapsto ui+b\); hence ordinary automorphisms form a subgroup of order \(n\varphi(n)\) with the stated index. For any \(n\ge3\) there is a unit \(v\ne1\). The map with rotation multiplier \(u=1\) and reflection permutation \(\pi(i)=vi\) is two-local, but is not a homomorphism. Thus the index exceeds one. For a prime \(p\ge3\), the gcd condition on distinct residues is automatic and \(\mathcal I_p=S_p\), giving the factor \((p-1)!\).

When \(n=1\), the group is \(C_2\), whose automorphism group is trivial. When \(n=2\), the group is the Klein four-group; its automorphisms are all six permutations of the three nonidentity elements. A two-local map fixes the identity and is injective, hence is one of those six automorphisms. This completes the boundary cases. \(\square\)

## Verification

A dependency-free exact-arithmetic checker, `check.py`, constructs the automorphisms \(\alpha_{a,b}\), independently tests the interpolation condition against the *actual image sets of all ordered pairs*, enumerates all gcd-preserving reflection permutations, and compares the count with the prime-power product. Full finite cases \(3\le n\le8\) pass. It separately brute-forces all permutations of the underlying sets for \(n=1,2,3\), testing the group-operation preservation and two-locality directly. Run `python check.py` in the directory containing this document and the checker; its final line is `VERIFY_OK`. The checker is finite corroboration; the proof above establishes the theorem for every permitted \(n\).

## Relationship to prior work

Molnár and Šemrl (2026) define two-point local automorphisms of groups and study real and complex classical matrix groups. Their motivating examples and classification do not address the natural action of the automorphism group of a finite dihedral group. The present calculation is a complete finite-family case of that question.

The two-local automorphism group is precisely the *2-closure* of \(\operatorname{Aut}(D_{2n})\) in its natural, generally intransitive, action on the elements of \(D_{2n}\). Wielandt's 2-closure formalism is classical. Yu and Pan (2019) treat primitive permutation groups of holomorph-simple and holomorph-compound types, not this intransitive action. Grech and Kisielewicz (2022) develop graphical representation and 2-closure criteria for **abelian permutation groups**, but do not calculate the present group. Klin and Kovács (2010), especially their Theorem 1.1 and Section 6, already explain automorphism groups preserving cyclic congruence block structures through generalized wreath products. In particular, the gcd-distance reflection-permutation factor is a standard block-structure phenomenon, not asserted to be independently new here. Known affine automorphisms of cyclic groups account for the \(U_n\) factor. The theorem's specific contribution is their exact *uncoupling* in the two-point interpolation problem for the full dihedral group (including its rotations), with the all-\(n\) order and strict non-globality conclusions. This is not a classification of all generalized wreath products.

## Limitations

This result makes no claim about two-local **endomorphisms**, generalized dihedral groups with noncyclic kernels, or arbitrary finite groups. Earlier results on the 2-closure of affine permutation groups, or on cyclotomic schemes over cyclic groups, might yield a different route to some ingredients; the present source comparison does not certify historical priority against every such specialization. The full arithmetic formula is not implied merely by a general definition of 2-closure.

## References

- L. Molnár and P. Šemrl, *Local automorphisms of some classical groups*, arXiv:2604.24299, first submitted 2026-04-27, https://arxiv.org/abs/2604.24299 .
- X. Yu and J. Pan, *2-closures of primitive permutation groups of holomorph type*, *Open Mathematics* **17** (2019), 795–801, https://doi.org/10.1515/math-2019-0063 .
- M. Grech and A. Kisielewicz, *Abelian permutation groups with graphical representations*, *Journal of Algebraic Combinatorics* **55** (2022), 513–531, https://doi.org/10.1007/s10801-021-01060-8 .
- M. Klin and I. Kovács, *Automorphism groups of rational circulant graphs through the use of Schur rings*, arXiv:1008.0751 (2010), https://arxiv.org/abs/1008.0751 .
- H. Wielandt, *Permutation Groups Through Invariant Relations and Invariant Functions*, Ohio State University, 1969, as cited by Yu and Pan (2019).
