# Exact uniform intersection numbers for coprime products and finite nilpotent groups

## Finding

For a nontrivial finite group \(X\), let \(m(X)\) be its number of maximal subgroups. Its **uniform intersection number** \(u(X)\) is the smallest positive integer \(k\) such that *every* family of \(k\) distinct maximal subgroups has intersection equal to the Frattini subgroup \(\Phi(X)\). Put \(\delta(X)=m(X)-u(X)\).

**Theorem (coprime-product law).** If \(G,H\) are nontrivial finite groups with \(\gcd(|G|,|H|)=1\), then
\[
u(G\times H)=m(G)+m(H)-\min\{\delta(G),\delta(H)\}
=u(G)+u(H)+\max\{\delta(G),\delta(H)\}.
\]
This applies to nonabelian as well as abelian groups.

**Theorem (nilpotent classification).** For a nontrivial finite \(p\)-group \(P\), put \(d=\dim_{\mathbb F_p}P/\Phi(P)\). Then
\[
m(P)=\frac{p^d-1}{p-1},\qquad
u(P)=1+\frac{p^{d-1}-1}{p-1},\qquad
\delta(P)=p^{d-1}-1.
\]
For an arbitrary nontrivial finite nilpotent group \(N=\prod_{i=1}^r P_i\), where the Sylow \(p_i\)-subgroup \(P_i\) requires \(d_i\ge1\) generators,
\[
\boxed{\quad
u(N)=1+\sum_{i=1}^r\frac{p_i^{d_i}-1}{p_i-1}
-\min_{1\le i\le r}p_i^{d_i-1}.
\quad}
\]
In particular, \(u(N)=m(N)\) whenever a Sylow subgroup has generator rank one.

**Sharp correction and unbounded gap.** Let \(A=C_2^2\) and \(B=C_3\). Then \((m(A),u(A))=(3,2)\), \((m(B),u(B))=(1,1)\), but \((m(A\times B),u(A\times B))=(4,4)\), contrary to the proposed product upper bound \(u(A\times B)\le u(A)+u(B)\) and to the coprime abelian additivity formula in the motivating literature. More generally, for \(d\ge2\),
\[
u(C_2^d\times C_3)-u(C_2^d)-u(C_3)=2^{d-1}-1,
\]
so the defect of the proposed inequality is unbounded.

## Assumptions and scope

All groups considered are nontrivial and finite. The coprime-product law assumes relatively prime **group orders**, not merely commuting factors. Empty families of maximal subgroups have intersection \(X\) by convention. Each nontrivial finite group has at least one maximal subgroup, and \(1\le u(X)\le m(X)\). The nilpotent formula includes nonabelian Sylow groups and cyclic Sylow factors; \(r\ge1\), all primes \(p_i\) are distinct, and \(d_i\ge1\). There is no assertion of the coprime-product identity for direct factors whose orders share a prime.

## Proof

**1. Largest deficient family.** Call a family \(\mathcal F\) of distinct maximal subgroups *deficient* if \(\bigcap\mathcal F\ne\Phi(X)\). Since adding maximal subgroups can only reduce the intersection and every maximal subgroup contains \(\Phi(X)\), nondeficiency is upward-closed. By the definition and minimality of \(u(X)\), every \(u(X)\)-element family is nondeficient and some \((u(X)-1)\)-element family is deficient. The last assertion also holds when \(u(X)=1\): the empty family is deficient because \(X\ne\Phi(X)\). Thus the maximum size of a deficient family is exactly \(u(X)-1\).

**2. Maximal-subgroup splitting for coprime orders.** Every subgroup \(K\le G\times H\) equals the product of its coordinate projections. Indeed, if \((g,h)\in K\), write \(a=|g|\), \(b=|h|\); the coprime-order hypothesis implies \(\gcd(a,b)=1\). The Chinese remainder theorem supplies powers of \((g,h)\) equal to \((g,1)\) and \((1,h)\). Applying this to each element yields \(K=\pi_G(K)\times\pi_H(K)\). The maximal subgroups of \(G\times H\) are therefore precisely
\[
\{M\times H:M\in\mathcal M(G)\}\ \cup\
\{G\times L:L\in\mathcal M(H)\};
\]
the two classes are disjoint. In particular, \(m(G\times H)=m(G)+m(H)\) and \(\Phi(G\times H)=\Phi(G)\times\Phi(H)\).

**3. Exact product threshold.** A selection containing \(a\) maximal subgroups of the first type and \(b\) of the second intersects in \((\bigcap_{j=1}^a M_j)\times(\bigcap_{j=1}^b L_j)\). This is deficient exactly when at least one coordinate selection is deficient. If the first coordinate is deficient, necessarily \(a\le u(G)-1\), while \(b\le m(H)\), and these bounds can be attained together. Swapping coordinates gives the other extreme. Hence the maximum size of a deficient product family is
\[
\max\{u(G)-1+m(H),\ m(G)+u(H)-1\}.
\]
Adding one proves \(u(G\times H)=\max\{u(G)+m(H),m(G)+u(H)\}\), equivalent to the two formulas in the first theorem.

**4. Finite \(p\)-groups.** By the standard Frattini property, every maximal subgroup of a finite \(p\)-group \(P\) contains \(\Phi(P)\), and maximal subgroups correspond bijectively to hyperplanes of \(V=P/\Phi(P)\cong\mathbb F_p^d\). There are \((p^d-1)/(p-1)\) hyperplanes. A collection of hyperplanes intersects nontrivially if and only if its intersection contains a one-dimensional subspace \(L\). The number of hyperplanes containing any fixed line is exactly the number of hyperplanes of \(V/L\), namely \((p^{d-1}-1)/(p-1)\). Every deficient family is contained in one of these line pencils, and each pencil is itself deficient, so this number is the largest possible deficient-family size. Part 1 gives the asserted \(u(P)\) and \(\delta(P)\), including the \(d=1\) case.

**5. Finite nilpotent groups.** A finite nilpotent group is the direct product of its nontrivial Sylow subgroups, which have pairwise coprime orders. Repeated application of part 3 shows that its total number of maximal subgroups is \(\sum_i m(P_i)\) and its total defect \(m(N)-u(N)\) is \(\min_i\delta(P_i)\); the latter follows inductively from \(\delta(G\times H)=\min\{\delta(G),\delta(H)\}\). Substitution of part 4 gives the boxed expression.

**6. Explicit contradiction.** In \(C_2^2\), the three maximal subgroups are the three order-two lines; any two meet in the identity. In \(C_3\), the sole maximal subgroup is the identity. In their coprime product, the three subgroups \(L\times C_3\), taken over all three lines \(L\le C_2^2\), intersect in \(\{1\}\times C_3\), strictly above \(\Phi(C_2^2\times C_3)=\{1\}\). Thus a deficient three-element family exists among the four maximal subgroups, proving \(u(C_2^2\times C_3)=4\) directly. The general unbounded gap follows from part 4 with \(p=2\) and rank \(d\).

## Verification

The accompanying self-contained `verify_uniform_intersection.py` enumerates actual hyperplanes, complete families of maximal subgroups, their intersections, and the maximum deficient-family size for sixteen elementary-abelian Sylow profiles, including mixed-prime products. It directly checks the four-maximal-subgroup counterexample. Independently, for \(S_3\), \(C_5\), and \(S_3\times C_5\) it generates full subgroup lattices from multiplication, enumerates all maximal-subgroup families, and verifies \((m,u)=(4,2),(1,1),(5,5)\), respectively. It ends in `VERIFY_OK`. These finite checks are not a proof of the general theorems; the unrestricted proof is above.

## Relationship to prior work

Choudhury and Khanra, *Uniform Intersection Numbers and Subgroup-Based Generating Graphs of Groups* (arXiv:2610.22268v1, first public October 15, 2026), Definition 1.1, introduce the same universal-choice invariant. Their Proposition 2.1 states the unrestricted upper bound \(u(G\times H)\le u(G)+u(H)\); Corollary 2.2 asserts additivity for finite abelian groups of coprime orders. The explicit four-maximal-subgroup example refutes both statements. The proof there constructs one successful family, which controls a minimum/existence-based intersection number but not the universal-choice invariant. Its Corollary 2.8 already gives the uniform number of finite cyclic groups; that special case is not claimed new here.

Archer and collaborators, *On the Intersection Numbers of Finite Groups* (arXiv:1907.02898), treat the minimum number of maximal subgroups **for which there exists** a Frattini intersection, a different invariant. Lucchini, *Maximal Intersections in Finite Groups* (DOI:10.1007/s00009-021-01961-9), studies parameters of chains and minimal/maximal intersections, not the universal maximum deficient-family size. The current result derives the exact universal-choice law and classification rather than restating these existence-based results.

## Limitations

The corrected product formula assumes coprime group orders; it does not classify products sharing common prime factors or arbitrary nonnilpotent groups. The examples and script do not establish literature-wide uniqueness. Independent verification of the general result has not been performed. Standard facts used without separate new proof are the elementary subgroup structure of finite \(p\)-groups, the Frattini quotient, and the decomposition of finite nilpotent groups into Sylow factors.

## References

1. P. N. Choudhury and B. Khanra, *Uniform Intersection Numbers and Subgroup-Based Generating Graphs of Groups*, arXiv:2610.22268v1 (October 15, 2026), https://arxiv.org/html/2610.22268v1, especially Definition 1.1, Proposition 2.1, and Corollary 2.2.
2. R. Archer et al., *On the Intersection Numbers of Finite Groups*, arXiv:1907.02898 (2019), https://arxiv.org/abs/1907.02898.
3. A. Lucchini, *Maximal Intersections in Finite Groups*, Mediterranean Journal of Mathematics 19 (2022), https://doi.org/10.1007/s00009-021-01961-9.
