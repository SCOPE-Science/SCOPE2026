# Lower central series and a prime-power-cycle criterion for permutation-twist groups

## Finding
For every finite permutation \(\pi\) on \(n\ge1\) letters, the group completion of its free-commutative-monoid Zhang twist has an exact lower central series. Its residual nilpotence is controlled by a simple arithmetic condition: **each nontrivial permutation cycle must have prime-power length**. The statement concerns residual nilpotence (trivial intersection of lower-central terms), not ordinary nilpotence (eventual triviality of a term). Indeed, every nonidentity permutation gives a nonnilpotent group.

Write \(P(e_i)=e_{\pi(i)}\), \(|a|=\sum_i a_i\), \(A=I-P\), and \(K=\ker(|\cdot|:\mathbb Z^n\to\mathbb Z)\). On \(\mathbb Z^n\), define \(a\star b=a+P^{|a|}b\). Then for every \(r\ge2\),
\[
\gamma_r(G_\pi)=A^{r-1}K.
\]
Consequently, \(G_\pi\) is residually nilpotent exactly when every cycle length is one or a prime power. For example, a six-cycle fails the criterion, whereas a permutation with disjoint cycles of lengths two, three, and one satisfies it, even though both permutations have order six.

## Assumptions and scope
All lattices are over the integers, with no finiteness restriction on group elements beyond \(n<\infty\). A prime power means \(p^s\) with \(p\) prime and \(s\ge1\); the length-one cycles are harmless. The lower central series uses \(\gamma_1(G)=G\) and \(\gamma_{r+1}(G)=[G,\gamma_r(G)]\). The identity of \(G_\pi\) is the zero vector; group elements of degree zero form the usual additive lattice \(K\). The original monoid is \(M_\pi=(\mathbb N^n,\star)\).

## Proof
**1. The group and its commutators.** The degree map is additive for \(\star\), because \(P\) preserves coordinate sums. Thus associativity follows from \(P^{|a\star b|}=P^{|a|+|b|}\), and the inverse is \(a^{-1}=-P^{-|a|}a\). The nonnegative cone is a cancellative submonoid. Any integral vector \(a\) is a right fraction: choose \(b\in\mathbb N^n\) sufficiently large that \(a\star b\in\mathbb N^n\). Thus its universal group of fractions is \(G_\pi\).

For \(a,b\in\mathbb Z^n\), put \(s=|a|\) and \(t=|b|\). Since \(a\star b\) and \(b\star a\) have the same degree, their quotient in \(G_\pi\) is the additive vector
\[
(a\star b)\star(b\star a)^{-1}=(I-P^t)a-(I-P^s)b.
\]
For every integer \(j\), \(I-P^j\) is divisible by \(I-P\) in the Laurent polynomial ring \(\mathbb Z[P,P^{-1}]\). The preimage in the displayed formula has degree \(ts-st=0\). It follows that \(G_\pi'\subseteq AK\). Conversely, for standard vectors \(e_i,e_j\), the quotient of \(e_i\star e_j\) and \(e_j\star e_i\) is precisely \(A(e_i-e_j)\). These vectors generate \(AK\), so \(G_\pi'=AK\).

For \(u\in K\), conjugation by any \(a\in G_\pi\) acts as \(P^{|a|}u\); in particular a degree-one element induces \(P\). Therefore \([G_\pi,A^jK]=A^{j+1}K\) for every \(j\ge1\), establishing the exact lower central series by induction.

**2. A cyclotomic lattice obstruction.** For each permutation cycle of length \(\ell\), the coordinate-sum-zero lattice is the root lattice of that cycle. Let \(L=\operatorname{im}(I-P)\), the direct sum of these root lattices. On \(L\), the operator \(A\) is injective over \(\mathbb Q\); its eigenvalues are \(1-\zeta\) for all nontrivial roots of unity \(\zeta\) of orders dividing the cycle lengths.

If a cycle length \(\ell\) has a divisor \(d>1\) with at least two distinct prime factors, let \(W_d\) be the integral kernel of \(\Phi_d(P)\) on the corresponding cycle. It is nonzero since \(\Phi_d(t)\) divides \(t^\ell-1\), and it is contained in \(K\) because \(\Phi_d(1)\ne0\). The elementary cyclotomic identity \(\Phi_d(1)=1\) gives an integral polynomial \(H\) with \(\Phi_d(t)=1+(t-1)H(t)\). Thus \(A H(P)=I\) on \(W_d\), and \(A\) acts bijectively on \(W_d\). Hence \(W_d=A^jW_d\subseteq A^jK=\gamma_{j+1}(G_\pi)\) for every \(j\ge1\). Residual nilpotence fails.

**3. No further obstructions.** Conversely, suppose every nontrivial cycle length is a prime power. A nontrivial root of unity \(\zeta\) occurring on \(L\) then has prime-power order \(p^h\). Its conjugate product \(\Phi_{p^h}(1)=p\) shows that \(1-\zeta\) is not an algebraic unit. Set \(J=\bigcap_{j\ge0}A^jL\). Because \(A\) is injective on \(L\), the inclusion \(J\subseteq AL\) implies \(A^{-1}J=J\): indeed, if \(v\in J\) and \(v=Aw\), then \(v\in A^{j+1}L\) for each \(j\), hence by injectivity \(w\in A^jL\). If \(J\ne0\), the restriction of \(A\) to the nonzero finitely generated free abelian group \(J\) is an automorphism. Its determinant is a unit, so all eigenvalues are algebraic units. But its eigenvalues belong to those of \(A\) on \(L\), none of which are units. Contradiction. Thus \(J=0\). Since \(A^jK\subseteq A^{j-1}L\) for \(j\ge1\), the lower central intersection is zero.

The used cyclotomic evaluation follows from \(\prod_{d\mid m,d>1}\Phi_d(1)=m\) for \(m>1\): induction over positive integers gives \(\Phi_m(1)=p\) when \(m=p^s\), and \(1\) otherwise.

Finally, if \(P\ne I\), then \(L\ne0\), and \(A^jL\ne0\) for all \(j\) by injectivity; likewise \(A^jK\ne0\). Therefore \(G_\pi\) is not nilpotent. If \(P=I\), it is just the additive free abelian group.

## Verification
The accompanying `verify.py` uses exact integer Smith normal forms and the concrete twisted group law. It tests all \(66\) integer partitions (cycle types) with total size at most eight, including every pair of basis generators, their inverses, commutator vectors, and the first commutator-lattice invariant factors. It also checks the simplest non-prime-power cyclotomic-unit calculation for \(\Phi_6\). The script outputs `VERIFY_OK`. These bounded computations corroborate, but do not replace, the unrestricted lattice argument.

## Relationship to prior work
Hazrat, Mesyan, and Steinberg introduced this permutation-twist family for free commutative semigroups in their Example 2.7, which establishes noncommutativity in a two-generator example. General group-extension properties of Zhang twists appear later in their article. Pre-existing calculations of this family's group completion, abelianization, and center are treated as known and are not claimed here. The new target is the **entire lower central series and the precise residual-nilpotence criterion**.

Noferini and Williams develop substantially more general Smith-normal-form methods for cyclotomic products, including powers of finite-order matrices; these results are close in the requisite integer linear algebra. Their Theorem 4.22 addresses eventual Smith-form periodicity, not a necessary-and-sufficient group-theoretic residual-nilpotence statement for permutation twists. The present result translates cyclotomic-unit arithmetic into the exact infinite-depth lower-central intersection of this group family. Equivalent formulations in other sources may exist.

## Limitations
This is a theorem for a specific family of permutation Zhang twists, not arbitrary graded semigroups, arbitrary Yang–Baxter structure groups, or general virtually abelian groups. The lower-central intersection can contain more structure than the explicitly exhibited obstruction lattice; no complete decomposition of that intersection is asserted. Novelty is assessed from inspected and searched available sources and is not an independent priority determination.

## References
1. R. Hazrat, Z. Mesyan, B. Steinberg, *Zhang twists for semigroups and groupoids, with applications to Steinberg algebras*, arXiv:2610.21005v1 (first posted October 14, 2026), Example 2.7 and Section 2.9.
2. V. Noferini, G. Williams, *Invariant factors from products of cyclotomic polynomials, with applications*, arXiv:2610.19205v1 (first posted October 13, 2026), especially Section 4.3, Theorem 4.22.
