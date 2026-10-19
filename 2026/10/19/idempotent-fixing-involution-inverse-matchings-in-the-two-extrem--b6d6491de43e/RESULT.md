# Idempotent-fixing involution inverse matchings in the two extremal ranks of chain endomorphism monoids

## Finding
For every integer \(n\ge3\), both the rank-two and the rank-\(n-1\) Green \(\mathcal D\)-classes of the order-preserving transformation monoid \(\mathcal O_n\) admit an explicit involution taking every transformation to a mutual inverse and fixing every idempotent. Consequently the only ranks not covered by such an explicit rank-wise involution are \(3\le r\le n-2\). The assertion is uniform in \(n\), not an enumeration bounded by chain size.

## Assumptions and scope
Let \([n]=\{1,\ldots,n\}\) with its usual order. An order-preserving transformation means a weakly increasing map \(f:[n]\to[n]\). Write composition in the ordinary functional sense. Its rank is the cardinality of its image. An involution inverse matching on a set of transformations is a bijection \(J\) satisfying \(J^2=\mathrm{id}\), \(fJ(f)f=f\) and \(J(f)fJ(f)=J(f)\). An idempotent is a map satisfying \(f^2=f\). The claim does not assert a single general closed-form matching for every intermediate-rank class.

## Proof
**Rank two.** Every rank-two map is uniquely specified by integers \(1\le c<n\), \(1\le a<b\le n\), and
\[
f_{c;a,b}(i)=\begin{cases}a&i\le c,\\ b&i>c.\end{cases}
\]
Such a map is idempotent exactly when \(a\le c<b\). A rank-two map \(f_{d;u,v}\) is a mutual inverse of \(f_{c;a,b}\) exactly when each image has one point on either side of the other map's kernel cut; explicitly,
\[
a\le d<b\quad\text{and}\quad u\le c<v.
\]
Indeed \(fgf=f\) holds precisely when the image of \(g\) is a transversal of the kernel blocks of \(f\), and the reverse equation yields the other transversal condition.

For \(a<b\le c\) set
\[
J(f_{c;a,b})=f_{a;b,c+1}.
\]
The output satisfies \(a<b<c+1\), hence is on the complementary nonidempotent side \(d<u<v\). Conversely, for \(c<a<b\) put
\[
J(f_{c;a,b})=f_{b-1;c,a}.
\]
These formulas are inverse to each other, and both satisfy the displayed transversal conditions. Set \(J(f)=f\) if \(a\le c<b\). This defines an involution inverse matching fixing every idempotent.

**Rank \(n-1\).** Each such map has one two-element kernel block \(\{c,c+1\}\), with \(1\le c<n\), and all other blocks singleton. Its image is \([n]\setminus\{z\}\) for a unique \(z\in[n]\). Denote the unique order-preserving map with this kernel and image by \(g_{c;z}\). It is idempotent exactly when \(z\in\{c,c+1\}\). By the same two-sided kernel-transversal criterion, \(g_{d;w}\) is a mutual inverse of \(g_{c;z}\) exactly when
\[
z\in\{d,d+1\},\qquad w\in\{c,c+1\}.
\]
For \(z<c\), define \(J(g_{c;z})=g_{z;c+1}\). The right side has missing image point strictly to the right of its doubled kernel block, and its inverse is \(g_{c;z}\). For \(z>c+1\), define \(J(g_{c;z})=g_{z-1;c}\); this is the inverse branch of the preceding rule. Fix \(g_{c;z}\) if \(z=c\) or \(c+1\). This is again an involution inverse matching, fixing every idempotent.

Rank one consists of constant idempotents. Rank \(n\) contains only the identity. Thus the four extreme rank values are covered; when some coincide, the rank-two and rank-\(n-1\) constructions both provide valid involution matchings.

## Verification
The standalone `check_extremal.py` enumerates all weakly increasing maps for each \(3\le n\le8\), reconstructs the two maps explicitly, and verifies rank preservation, involutivity, idempotent fixing, and both mutual-inverse equations on every element in the relevant classes. It is a finite consistency check, not a proof for unbounded \(n\).

## Relationship to prior work
Higgins (2026), Theorem B, obtains a **permutation** matching for all of \(\mathcal O_n\), without requiring that matching to be involutory or fix idempotents. Higgins (2024), Proposition 2.3, supplies an involution matching whenever the number of columns of the structure matrix is divisible by its number of rows. For rank two, this covers even \(n\), because the corresponding class counts are \(\binom n2\) and \(n-1\), with ratio \(n/2\); it does not cover odd \(n\) or the rank-\(n-1\) class for \(n>2\), whose ratio is \(n/(n-1)\). Earlier results on involution matchings for the larger orientation-preserving transformation monoid do not restrict automatically to \(\mathcal O_n\). The present result gives explicit formulas in precisely these uniform extremal families.

## Limitations
Nothing is asserted about general intermediate rank \(3\le r\le n-2\), where global involution matching remains more difficult. The idempotent-fixing property is special and need not extend to all ranks. The current literature comparison does not rule out equivalent unpublished constructions under different terminology; independent mathematical audit has not been performed.

## References
- P. M. Higgins, *Balanced weightings and permutation matchings applied to the monoid of order-preserving mappings*, arXiv:2610.01912v1 (October 1, 2026), Theorems A and B.
- P. M. Higgins, *Finite regular semigroups with permutations that map elements to inverses*, Semigroup Forum **109** (2024), 141–147, Proposition 2.3; DOI:10.1007/s00233-024-10430-0.
- P. M. Higgins, *Involution matchings, the semigroup of orientation-preserving and orientation-reversing mappings, and inverse covers of the full transformation semigroup*, Semigroup Forum **98** (2019), 669–689; DOI:10.1007/s00233-019-10018-z.
