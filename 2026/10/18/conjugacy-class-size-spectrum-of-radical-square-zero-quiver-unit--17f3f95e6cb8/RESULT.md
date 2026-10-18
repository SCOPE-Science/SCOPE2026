# Conjugacy-class size spectrum of radical-square-zero quiver unit groups

## Finding
Let \(Q\) be an arbitrary finite quiver, with loops and parallel arrows allowed, and let \(G=(\mathbb F_q Q/J^2)^\times\), where \(J\) is the arrow ideal and \(q\) is any prime power. The following formula determines **the number of conjugacy classes of every possible size**, not merely the total class number.

Write \(V\) for the \(n\)-vertex set; let \(h\) be the number of loops. Collapse each bundle of nonloop arrows between two vertices, irrespective of orientation, to one simple undirected edge \(e\) with multiplicity \(\mu_e\), the total number of arrows in the bundle. Write \(H=(V,E)\) for this simple graph. For a subset \(F\subseteq E\), let \(c(F)\) count the components of the spanning graph \((V,F)\), including isolated vertices, and put \(\beta(F)=|F|-n+c(F)\). Let \(\mu(D)=\sum_{e\in D}\mu_e\).

For a vertex assignment \(t:V\to\mathbb F_q^\times\), define the monochromatic edge set
\[
B(t)=\{\{u,v\}\in E:t_u=t_v\}.
\]
Then the class-size enumerator, in which the coefficient of \(Z^s\) is the number of conjugacy classes of size \(s\), is exactly
\[
\boxed{\mathcal C_Q(Z)=q^h\sum_{t\in(\mathbb F_q^\times)^V}\ \sum_{F\subseteq B(t)}
 (q-1)^{\beta(F)}\!\prod_{e\in F}\frac{q^{\mu_e}-1}{q-1}\;
 Z^{\,q^{\mu(E\setminus B(t))}(q-1)^{n-c(F)}}.}
\]
Each summand corresponds to a diagonal assignment \(t\) and the precise set \(F\) of monochromatic edge bundles with a nonzero radical block after conjugating away all nonmonochromatic coordinates. The summand's coefficient counts distinct conjugacy classes and the exponent gives the size of each one. Empty products equal one. The formula applies in characteristic two and includes loops, parallel arrows, and arrows in both directions.

For \(q>2\), the two smallest class-size coefficients detect structural invariants. If \(c(H)\) is the number of connected components of \(H\) and \(b_1(H)\) counts bridges of \(H\) whose arrow multiplicity is **exactly one**, then
\[
[Z^1]\mathcal C_Q(Z)=q^h(q-1)^{c(H)},\qquad
[Z^q]\mathcal C_Q(Z)=q^h(q-1)^{c(H)}(q-2)b_1(H).
\]
Thus, in the nontrivial diagonal-torus regime, the class-size spectrum recovers the number of multiplicity-one bridges when \(q\), \(h\), and \(c(H)\) are known.

**An exact separation example.** Over \(\mathbb F_3\), let \(H_A\) and \(H_B\) have the same labelled vertices \(\{0,1,2,3,4,5\}\), with edges written as two-digit strings:
\[
 E(H_A)=\{01,02,03,04,13,15,23,25\},\qquad
 E(H_B)=\{04,05,13,14,23,24,34,45\}.
\]
Orient the edges arbitrarily, once each, to obtain two quivers. Both unit groups have order \(2^6 3^8=419904\) and exactly \(2340\) conjugacy classes, but the groups attached to \(H_A\) and \(H_B\) have respectively \(2\) and \(0\) conjugacy classes of size \(3\). In particular, the groups are not isomorphic. This is information not present in the common class number and group order.

## Assumptions and scope
All quivers and graphs are finite. A loop means an arrow beginning and ending at one vertex; \(J^2=0\) in the quotient. The graph \(H\) ignores loops but retains each nonloop arrow bundle's multiplicity. The coefficient field may be any \(\mathbb F_q\) with \(q\ge2\). Conjugacy classes are ordinary conjugacy classes inside the full unit group, not in the additive algebra or the radical subgroup. The result counts actual classes of the labelled group, not graph-isomorphism types. The graph need not be connected.

## Proof
**1. Unit-group structure.** The algebra is \(D\oplus J\) with \(D\cong\mathbb F_q^n\) and \(J^2=0\). Its units have unique expressions \((t,x)\), where \(t\in(\mathbb F_q^\times)^n\) and \(x\in J\). In the arrow basis, multiplication is
\[
(t,x)(s,y)=(ts,ty+xs),\qquad (ty+xs)_{a:u\to v}=t_u y_a+x_a s_v.
\]
Its order is \((q-1)^n q^{h+\mu(E)}\). Every loop coordinate commutes with all units and can be chosen independently in \(q\) ways.

**2. Canonical form at fixed diagonal.** Conjugation by a radical unit \((1,y)\) translates the arrow coordinate at \(a:u\to v\) by \((t_u-t_v)y_a\), with sign depending on conjugation convention. If \(t_u\ne t_v\), there is one and only one \(y_a\) eliminating a prescribed \(x_a\). If \(t_u=t_v\), conjugation by any radical unit leaves \(x_a\) unchanged. Thus every unit is conjugate to one with vanishing nonmonochromatic arrow coordinates; in this canonical form the set \(F\subseteq B(t)\) of undirected bundles with nonzero vector of arrow coordinates is a class invariant. The diagonal part \(t\) is conjugacy-invariant because the diagonal quotient is abelian.

**3. Diagonal orbit count.** Conjugation by \(s\in(\mathbb F_q^\times)^n\) scales every coordinate for \(a:u\to v\) by \(s_u/s_v\). A nonzero bundle at \(e=\{u,v\}\) is fixed precisely when \(s_u=s_v\), even if some arrows in the bundle have opposite orientations. Hence the stabilizer of any canonical radical vector with support \(F\) has order \((q-1)^{c(F)}\); each diagonal orbit has size \((q-1)^{n-c(F)}\). For given \(F\) there are \(\prod_{e\in F}(q^{\mu_e}-1)\) allowed nonzero vectors. Therefore the number of diagonal orbits at that support is
\[
\frac{\prod_{e\in F}(q^{\mu_e}-1)}{(q-1)^{n-c(F)}}
=(q-1)^{\beta(F)}\prod_{e\in F}\frac{q^{\mu_e}-1}{q-1}.
\]
All these are integers: the first factor has nonnegative exponent \(\beta(F)\), the cycle rank, and each fraction is an integer.

**4. Full class sizes and centralizers.** At a canonical pair \((t,x)\), the equation \((s,y)(t,x)=(t,x)(s,y)\) becomes the independent family
\[
 (t_u-t_v)y_a=(s_u-s_v)x_a
\]
for every arrow \(a:u\to v\). If the edge is nonmonochromatic, \(y_a\) is uniquely determined for each \(s\). If it is monochromatic, every \(y_a\) is free, whereas a nonzero bundle forces \(s_u=s_v\). Loop coordinates are free. Therefore
\[
 |C_G(t,x)|=q^{h+\mu(B(t))}(q-1)^{c(F)},\qquad
 |(t,x)^G|=q^{\mu(E\setminus B(t))}(q-1)^{n-c(F)}.
\]
Multiplying the number of diagonal orbits by \(q^h\) central loop choices and summing over \(t\) and \(F\) proves the class-size formula. No assumption on the characteristic was used.

**5. Bridge coefficients.** For \(q>2\), the factors \(q\) and \(q-1\) are coprime and \(q-1>1\). The class size is \(1\) exactly when \(F=\varnothing\) and every edge is monochromatic, so the diagonal values are constant on each component of \(H\): this gives \(q^h(q-1)^{c(H)}\) singleton classes. Class size \(q\) requires \(F=\varnothing\) and exactly one nonmonochromatic arrow (counted with multiplicity). The unique nonmonochromatic undirected edge must have multiplicity one, and it must be a bridge, since every other edge joins equal labels. Conversely, after deleting such a bridge, assign unequal nonzero labels to its two sides and constant labels on every remaining connected component. There are \((q-1)^{c(H)}(q-2)\) such assignments per multiplicity-one bridge. Multiplying by \(q^h\) proves both identities.

## Verification
The accompanying standalone `checker.py` has two logically separate modes. It constructs every unit for eleven small finite examples, multiplies units directly in the quotient algebra, computes all centralizers by exhaustive comparison, and divides the number of elements in each size stratum by the corresponding class size. It independently compares this distribution with the graph formula. It also checks two six-vertex graph instances using the graph formula and the bridge coefficient, confirms their common class number \(2340\), and confirms the total class mass \(419904\) independently in each case. The eleven examples include \(q=2,3,4,5\), opposite and parallel arrows, loops, cycles and disconnected graphs. Run using `python3 checker.py`. Successful output ends with `ALL_QUOTIENT_UNIT_CLASS_TESTS_PASSED 11`. This finite check is not a proof for arbitrary quivers; the group-theoretic argument above supplies the uniform proof.

## Relationship to prior work
André and Dias, *Smooth representations of unit groups of split basic algebras over non-Archimedean local fields* (2019, arXiv:1910.14639), establish the structural diagonal-by-radical framework and study induced representations over local fields. The present work uses the split-basic perspective, but addresses exact conjugacy sizes over finite fields, a different invariant and base-field setting. Rossmann, *Enumerating conjugacy classes of graphical groups over finite fields* (2021, arXiv:2107.05564), gives class-size polynomials for a distinct family of graphical groups defined through central commutators; their groups are class-two nilpotent, whereas the groups here have an abelian normal radical subgroup and a multiplicative diagonal quotient. Neither result is asserted to cover the present family.

The total number of unit-group conjugacy classes for these quiver algebras has previously been obtained by an evaluation of a graph partition polynomial, and special conjugacy classes from torsion diagonal units have also been counted. **Neither of these established statements is claimed as new.** The new subject here is the full size-by-size enumeration together with its structural bridge-detection consequence; a class-number identity alone does not imply this refinement, as the two explicit graphs demonstrate.

## Limitations
No classification up to isomorphism of quivers or unit groups is claimed. The result counts class sizes, not character degrees or conjugacy-class power maps. For \(q=2\), the diagonal torus is trivial and the entire group is abelian, so the bridge coefficient formula is explicitly restricted to \(q>2\). This is a mathematical proof with bounded finite computational tests, not an independently certified result. An equivalent theorem in older or differently indexed semidirect-product group literature may exist; the source comparisons performed cannot prove historical priority.

## References
1. C. A. M. André and J. Dias, *Smooth representations of unit groups of split basic algebras over non-Archimedean local fields* (2019), https://arxiv.org/abs/1910.14639 (first public version 2019-10-31).
2. T. Rossmann, *Enumerating conjugacy classes of graphical groups over finite fields* (2021), https://arxiv.org/abs/2107.05564 (first public version 2021-07-12).
