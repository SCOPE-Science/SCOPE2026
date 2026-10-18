# Exact diagonal-relation census and random-digraph law for flat semilattices

## Finding

Let \(F_n=\{0,a_1,\ldots,a_n\}\), with \(n\ge1\), be the finite flat meet-semilattice whose distinct nonzero atoms meet at zero. A *diagonal subsemigroup* is a reflexive binary relation \(R\subseteq F_n\times F_n\) closed under coordinatewise meet. Its off-diagonal-pair enumerator is

\[
\boxed{\sum_{R}z^{|R|-(n+1)}=\sum_{L,U\subseteq[n]}z^{|L|+|U|}(1+z)^{|L||U|-|L\cap U|}.}
\]

In particular the exact number of diagonal subsemigroups is

\[
\boxed{D_n=\sum_{L,U\subseteq[n]}2^{|L||U|-|L\cap U|}
=\sum_{a=0}^n\binom na(1+2^{a-1})^a(1+2^a)^{n-a}.}
\]

The factor with exponent \(a=0\) is understood as one. Exactly \(2^n\) of these relations are congruences, and exactly \(\sum_{k=0}^n\binom nk2^{\binom k2}\) are symmetric. Therefore

\[
\boxed{\chi(F_n)=\frac{2^n}{D_n}\sim2^{-n(n-2)}\qquad(n\to\infty).}
\]

Moreover, if a diagonal subsemigroup is chosen uniformly, then with probability tending to one it contains every ordered pair with exactly one zero coordinate. Conditional on that event, the remaining off-diagonal atom-to-atom pairs form an independent uniformly sampled directed graph without loops. The unconditional number of such pairs consequently converges in total variation to the family of binomial laws \(\operatorname{Bin}(n(n-1),1/2)\) in the sense that the total-variation distance tends to zero.

## Assumptions and scope

The ground object is the finite commutative idempotent semigroup \(F_n\) with operation \(x\wedge y\): \(0\wedge x=0\), \(a_i\wedge a_i=a_i\), and \(a_i\wedge a_j=0\) for \(i\ne j\). No group, field, or choice of characteristic is involved. A relation is compatible when \((x,y),(x',y')\in R\) implies \((x\wedge x',y\wedge y')\in R\). Diagonal means \((x,x)\in R\) for every \(x\). A congruence is also symmetric and transitive. The coefficient \(\chi(F_n)\) is the number of congruences divided by the number of diagonal subsemigroups.

## Proof

**Normal form.** Given a diagonal relation \(R\), define

\[
L=\{i:(a_i,0)\in R\},\quad U=\{j:(0,a_j)\in R\},\quad
D=\{(i,j):i\ne j,(a_i,a_j)\in R\}.
\]

Compatibility with the diagonal element \((a_i,a_i)\) gives \((a_i,a_j)\wedge(a_i,a_i)=(a_i,0)\) whenever \(i\ne j\), so every \((i,j)\in D\) requires \(i\in L\). Meeting instead with \((a_j,a_j)\) gives \((0,a_j)\), forcing \(j\in U\). Thus \(D\subseteq(L\times U)\setminus\{(i,i):i\in L\cap U\}\).

Conversely take arbitrary \(L,U\subseteq[n]\) and any such \(D\), and include the entire diagonal, all \((a_i,0)\) for \(i\in L\), all \((0,a_j)\) for \(j\in U\), and the pairs \((a_i,a_j)\) for \((i,j)\in D\). This relation is meet-closed: a meet of two atom-to-atom off-diagonal pairs is the same pair, a permitted atom-to-zero pair, a permitted zero-to-atom pair, or \((0,0)\). Meeting a non-diagonal pair with a diagonal pair has exactly those possibilities. Meetings involving an atom-zero pair cannot create new nonzero atom-atom pairs. All required resulting arms are present by the definition of admissible \(D\). Hence the correspondence \(R\longleftrightarrow(L,U,D)\) is bijective.

**Exact counts and size polynomial.** For fixed \(L,U\), there are \(|L||U|-|L\cap U|\) independently optional directed atom-atom pairs. Each chosen atom-zero or zero-atom arm contributes one off-diagonal pair. Thus the contribution is \(z^{|L|+|U|}(1+z)^{|L||U|-|L\cap U|}\), proving the enumerator. At \(z=1\) this gives the first formula for \(D_n\). To obtain the single sum, first choose \(L\) of size \(a\); for a coordinate \(j\in L\), including \(j\) in \(U\) permits \(a-1\) atom-atom pairs, whereas a coordinate \(j\notin L\) permits \(a\). Summing inclusion/exclusion of each \(j\) independently gives \((1+2^{a-1})^a(1+2^a)^{n-a}\), and then sum over \(\binom na\) choices of \(L\).

**Congruences and symmetry.** In a compatible equivalence relation, distinct equivalent atoms \(a_i,a_j\) imply \(a_i\sim0\) by meeting with \(a_i\); hence only a chosen subset of atoms can merge with the zero class and every other atom is a singleton class. Every such subset gives a congruence, so there are \(2^n\). For symmetry, the arms must satisfy \(L=U=T\); each unordered pair of distinct elements of \(T\) may independently be present in both orientations or absent. Therefore the number of symmetric compatible relations is \(\sum_{k=0}^n\binom nk2^{\binom k2}\).

**Sharp asymptotic.** The single term \(L=U=[n]\) in the first sum equals \(2^{n(n-1)}\). Put \(r=n-|L|\), \(s=n-|U|\), and \(k=r+s\). Since \(|L\cap U|\ge n-r-s\), the loss \(\Delta\) in the exponent relative to \(n(n-1)\) satisfies

\[
\Delta=n(n-1)-(|L||U|-|L\cap U|)\ge(n-1)(r+s)-rs\ge(n-1)k-k^2/4.
\]

For \(1\le k\le n\), \(\Delta\ge k(3n/4-1)\). The sum of all relative contributions of such pairs \((L,U)\), compared with \(2^{n(n-1)}\), is at most

\[
\sum_{k=1}^n\binom{2n}{k}2^{-k(3n/4-1)}
\le(1+2^{1-3n/4})^{2n}-1=o(1).
\]

For \(n<k\le2n\), the same bound yields \(\Delta\ge k(n/2-1)>n(n/2-1)\); the total relative contribution is at most \(4^n2^{-n(n/2-1)}=o(1)\). The inequalities are used for all sufficiently large \(n\), which is all that asymptotics require. This proves \(D_n/2^{n(n-1)}\to1\), and dividing the exact congruence count by this gives the stated equivalent for \(\chi(F_n)\).

**Typical random relation.** The number of relations with \(L=U=[n]\) is exactly \(2^{n(n-1)}\), so a uniform relation has this event with probability \(2^{n(n-1)}/D_n\to1\). On this event, its optional directed atom-atom pairs are mutually independent fair binary choices. If \(X_n\) is their number, the total variation distance from \(\operatorname{Bin}(n(n-1),1/2)\) is at most \(1-2^{n(n-1)}/D_n\to0\). In particular, its normal approximation follows from the ordinary binomial central limit theorem. This is a dimension-varying total-variation comparison, not convergence to a fixed binomial variable.

## Verification

The standalone `star_semilattice_checker.py` uses only the Python standard library. It independently enumerates every reflexive relation on \(F_n\) for \(n=1,2,3\), checks meet closure directly, symmetry, and transitivity, and obtains respectively the exact triples (diagonal relations, symmetric relations, congruences) \((4,2,2)\), \((25,5,4)\), and \((322,18,8)\). It independently evaluates the subset-sum and single-sum formulas for \(1\le n\le11\); for \(n=4\) the exact diagonal count is \(12643\). For \(n=20\), the ratio \(D_n/2^{n(n-1)}\) is approximately \(1.00007629817\), and for \(n=40\) it is approximately \(1.00000000015\). All checks completed with `VERIFY_OK`. Exhaustive checks for small \(n\) do not prove the arbitrary-\(n\) statements; those follow from the arguments above.

## Relationship to prior work

Barber and Ruškuc introduced the diagonal-subsemigroup comparison framework and proved that a finite semigroup has every compatible reflexive relation a congruence precisely when it is a group. Their 2026 follow-up `arXiv:2602.17286` gives complete value-realization results using Rees matrix semigroups and an upper bound for Clifford semigroups using their semilattice of idempotents; its concluding discussion explicitly raises the absence of formulas for \(\chi(Y)\) as \(Y\) ranges over finite semilattices. The present result evaluates the complementary natural *flat* family, proves a sharp superexponential coefficient law, and describes the typical compatible relation as an unconstrained random directed graph after saturation of the zero-coordinate arms. In particular, their general upper bound implies that every finite Clifford semigroup whose idempotent semilattice is \(F_n\) has DSC coefficient at most \(2^n/D_n\); no classification of all Clifford diagonal relations is claimed here. Results for linearly ordered semilattices count a different family and do not imply these flat-semigroup formulas.

## Limitations

The theorem applies only to the specified height-two flat semilattices, not to arbitrary height-two semilattices with several nonzero levels, arbitrary finite semilattices, or every Clifford semigroup. The total-variation statement concerns the number of optional atom-atom directed edges of a random relation; it does not assert that all compatibility events are independent unconditionally. Unindexed equivalent prior enumerations under another name remain possible. Independent mathematical validation is not supplied.

## References

- C. Barber and N. Ruškuc, *Comparing Numbers of Diagonal Subsemigroups and Congruences for Semigroups*, arXiv:2602.17286, first posted 2026-02-19, especially Sections 1, 3, and 4. https://arxiv.org/abs/2602.17286
- C. Barber and N. Ruškuc, *Semigroup Congruences and Subsemigroups of the Direct Square*, published online 2025-07-07, Bulletin of the Australian Mathematical Society, https://www.cambridge.org/core/journals/bulletin-of-the-australian-mathematical-society/article/semigroup-congruences-and-subsemigroups-of-the-direct-square/908B89A485FCB609DF3254EF1E40A537
