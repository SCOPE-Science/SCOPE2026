# Orbit-gcd torsion and degree-congruence centers of permutation Zhang twists

## Finding

Fix a finite nonempty set of \(n\) letters and a permutation \(\pi\). Denote its cycle lengths by \(\ell_1,\ldots,\ell_c\), with \(c\ge1\), and put \(g=\gcd(\ell_1,\ldots,\ell_c)\) and \(m=\operatorname{lcm}(\ell_1,\ldots,\ell_c)\). Let \(P\) be the permutation matrix of \(\pi\), acting on integer column vectors by \(Pe_i=e_{\pi(i)}\), and write \(|a|=\sum_i a_i\).

The permutation Zhang twist of the free commutative monoid is the monoid \(M_\pi=(\mathbb N^n,\star)\) with multiplication
\[a\star b=a+P^{|a|}b.\]
Here \(\mathbb N\) contains zero. If an absorbing zero is adjoined, all assertions concern its nonzero part; adding that zero does not change the center among nonzero elements.

**Theorem.** The monoid \(M_\pi\) is cancellative and Ore, and its universal group of fractions is \(G_\pi=(\mathbb Z^n,\star)\). There is a canonical presentation
\[G_\pi=\langle x_1,\ldots,x_n\mid x_i x_j=x_{\pi(j)}x_{\pi^{-1}(i)}\ \text{for all }i,j\rangle.\]
Consequently it is the structure group of the involutive permutation Yang--Baxter solution \(r(i,j)=(\pi(j),\pi^{-1}(i))\). Its full abelianization is
\[\boxed{G_\pi^{\mathrm{ab}}\cong\mathbb Z^c\oplus\mathbb Z/g\mathbb Z.}\]
The cyclic group of order one is understood to be trivial. Its center is
\[\boxed{Z(G_\pi)=\{v\in\mathbb Z^n:Pv=v,\ m\mid|v|\}.}\]
The center of \(M_\pi\) is the intersection of this set with \(\mathbb N^n\). The center has rank \(c\) and index \(m/g\) in the permutation-invariant integer lattice \(\operatorname{Fix}_{\mathbb Z}(P)\).

In particular, abelianization torsion is absent exactly when \(\gcd(\ell_1,\ldots,\ell_c)=1\). The exponent of that torsion is exactly \(g\). The center is characterized by a simultaneous orbit-constancy condition and a total-degree divisibility condition, rather than by orbit constancy alone.

## Assumptions and scope

The result holds for **every** finite nonempty permutation and for **all** cycle patterns, including fixed points and repeated lengths. All groups, lattices, and monoids are purely algebraic; there is no assumption of a field or a characteristic. The monoid multiplication is the Zhang twist by the degree-preserving permutation automorphism of the free commutative monoid. The correspondence with a Yang--Baxter solution concerns the indicated involutive permutation solution only; it is not a classification for arbitrary set-theoretic solutions.

## Proof

**(1) The twisted monoid and its fraction group.** A permutation preserves coordinate sum. Thus \(|a\star b|=|a|+|b|\), and
\[(a\star b)\star c=a+P^{|a|}b+P^{|a|+|b|}c=a\star(b\star c).\]
The zero vector is the identity. The same formula works for integral vectors, with inverse \(a^{-1}=-P^{-|a|}a\). The submonoid of nonnegative vectors is cancellative, since it is a submonoid of the group. Given nonnegative \(a,b\), choose a vector \(z\in\mathbb N^n\) coordinatewise above both. Then
\[a\star P^{-|a|}(z-a)=z=b\star P^{-|b|}(z-b),\]
so the monoid is right Ore. Every integral vector \(v\) can be expressed as a right fraction: choose \(b\in\mathbb N^n\) large enough that \(a=v+P^{|v|}b\) is nonnegative, giving \(v=a\star b^{-1}\). Hence this group is the full universal group of fractions.

**(2) The presentation.** The product of generators in a positive word of length \(k\) has integral coordinate vector
\[x_{i_1}\star\cdots\star x_{i_k}=\sum_{t=1}^{k}P^{t-1}e_{i_t}.\]
Two positive words are equal exactly when the corresponding multisets of the \(k\) transformed letters agree. Any two orderings of the same multiset are connected by adjacent swaps. Swapping transformed letters at consecutive positions corresponds exactly to
\[x_i x_j=x_{\pi(j)}x_{\pi^{-1}(i)}.\]
Therefore these are a complete monoid presentation; adjoining inverses yields the fraction-group presentation. The indicated map \(r\) is involutive (apply it twice). Both sides of the braid relation send \((i,j,k)\) to \((\pi^2(k),j,\pi^{-2}(i))\), so it is a Yang--Baxter solution. Its structure group, by definition, has precisely the displayed relations.

**(3) Abelianization.** In the free abelian group on images \(X_i\) of the generators, each quadratic relation becomes
\[X_i+X_j=X_{\pi(j)}+X_{\pi^{-1}(i)}.\]
Put \(d_i=X_i-X_{\pi^{-1}(i)}\). The relations say that \(d_i=X_{\pi(j)}-X_j\); equivalently, every \(d_i\) equals every \(d_{\pi(j)}\). Since \(\pi\) is onto, all \(d_i\) have the same image \(t\). In a cycle of length \(\ell\), successive images are \(X_{\pi^h(i)}=X_i+h t\), and closing the cycle forces \(\ell t=0\). Choosing one image \(u_j\) for each of the \(c\) cycles gives a presentation with generators \(u_1,\ldots,u_c,t\) and *only* the relations \(\ell_jt=0\). (Conversely, assigning every image its displayed expression satisfies all original quadratic relations, so no further relations are introduced.) Bezout's identity reduces these relations to \(g t=0\), proving \(G_\pi^{\mathrm{ab}}\cong\mathbb Z^c\oplus\mathbb Z/g\mathbb Z\).

**(4) The center.** Since the vectors \(e_i\) generate \(G_\pi\), a vector \(v\in\mathbb Z^n\) is central exactly when \(v\star e_i=e_i\star v\) for every \(i\). Expanding gives
\[(I-P)v=(I-P^{|v|})e_i\qquad(1\le i\le n).\]
Summing over all \(i\) makes the right-hand side zero, because every power of \(P\) preserves \(\sum_i e_i\). Thus \(n(I-P)v=0\), and integral torsion-freeness implies \(Pv=v\). The displayed equations then require \(P^{|v|}e_i=e_i\) for all \(i\), or equivalently \(m\mid |v|\). These two conditions suffice: for any \(w\), \(v\star w=v+w=w+Pv=w\star v\). The monoid center is the group center intersected with the submonoid, since commuting with all positive generators is equivalent to commuting with their inverses.

Finally \(\operatorname{Fix}_{\mathbb Z}(P)\cong\mathbb Z^c\): an invariant vector is constant on each cycle, say with values \(t_j\). Its coordinate sum is \(\sum_j\ell_jt_j\), whose possible values form exactly \(g\mathbb Z\). The degree constraint is membership in \(m\mathbb Z\). Since \(g\mid m\), the index of \(m\mathbb Z\) in \(g\mathbb Z\) is \(m/g\), and the lattice index follows.

## Verification

The companion `verify.py` uses independent Smith normal forms of the integer relation matrices to confirm the predicted free rank and elementary torsion for every permutation in degrees one through six (\(873\) permutations). For all permutations in degrees one through four it also checks every vector with coordinates in \(\{-1,0,1\}\), comparing direct twisted multiplication against the proposed centrality criterion. Running `python verify.py` with the dependency specified in `requirements.txt` prints `VERIFY_OK 873`. These finite computations are regression tests, not an exhaustive proof for arbitrary degrees. All general conclusions above follow from the algebraic argument.

## Relationship to prior work

Hazrat, Mesyan and Steinberg (2026), Example 2.7 and Remark 2.6, construct the same permutation Zhang twists of free commutative semigroups, illustrating noncommutativity for the two-letter transposition. Their work develops the general twisting theory but does not give the present full abelianization, centrality criterion, or lattice index for arbitrary finite permutations.

Lebed and Vendramin (2018/2019), Proposition 6.3, establish the **rank** of the abelianization of a general Yang--Baxter structure group; the text immediately afterward asks for a description of its **torsion**. Their Examples 6.4 and 6.5 calculate the two-letter transposition and the two-letter transposition plus fixed point. These are previously known instances of the formula (respectively \(\mathbb Z\oplus\mathbb Z/2\mathbb Z\) and \(\mathbb Z^2\)). The contribution here is the all-cycle gcd torsion rule together with the precise center and central-lattice index, not the rank result or those examples.

Cedó, Jespers and Okniński (2020) identify cyclic permutation solutions in a classification of primitive solutions; their main results do not compute the abelianization torsion or centers of all finite-permutation structure groups.

## Limitations

The result is confined to twists of free commutative monoids by finite permutations and to their associated involutive permutation Yang--Baxter solutions. It does not solve the general torsion question for arbitrary nondegenerate set-theoretic solutions, and it does not classify all isomorphism types of these groups beyond the stated invariants. An equivalent formulation could exist in older literature on monoids of I-type or Bieberbach structure groups; this possibility remains a bibliographic risk despite the primary-source comparisons and searches. No independent audit has been performed.

## References

1. R. Hazrat, Z. Mesyan, B. Steinberg, *Zhang twists for semigroups and groupoids, with applications to Steinberg algebras*, arXiv:2610.21005v1 (first posted 2026-10-14), especially Remark 2.6 and Example 2.7. https://arxiv.org/html/2610.21005v1
2. V. Lebed, L. Vendramin, *On structure groups of set-theoretic solutions to the Yang--Baxter equation*, arXiv:1707.00633v2 (2018), especially Proposition 6.3 and Examples 6.4--6.5; published in *Proceedings of the Edinburgh Mathematical Society* 62 (2019), 683--717. https://arxiv.org/pdf/1707.00633
3. F. Cedó, E. Jespers, J. Okniński, *Primitive set-theoretic solutions of the Yang--Baxter equation*, arXiv:2003.01983v1 (2020). https://arxiv.org/pdf/2003.01983
