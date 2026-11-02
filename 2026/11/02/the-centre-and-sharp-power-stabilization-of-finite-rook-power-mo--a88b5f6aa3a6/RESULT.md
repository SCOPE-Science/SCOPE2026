# The centre and sharp power stabilization of finite rook power monoids

## Finding
For every integer \(n\ge1\), let \(\mathcal I_n\) be the symmetric inverse monoid of all partial bijections of an \(n\)-point set, including the empty partial map. Let \(\mathcal P^*(\mathcal I_n)\) be the monoid of **nonempty** subsets of \(\mathcal I_n\) under setwise composition. This is the ordinary (unreduced) power monoid; it does not contain the empty subset as an element.

Write \(e_D\) for the partial identity on \(D\subseteq[n]\), and, for \(0\le r\le n\), put
\[
E_r=\{e_D:D\subseteq[n],\ |D|=r\},\qquad
A_R=\bigcup_{r\in R}E_r\quad(\varnothing\ne R\subseteq\{0,\ldots,n\}).
\]
The complete centre is
\[
\boxed{Z(\mathcal P^*(\mathcal I_n))
       =\{A_R:\varnothing\ne R\subseteq\{0,\ldots,n\}\}.}
\]
Consequently its cardinality is \(2^{n+1}-1\). Its multiplication, written on nonempty rank sets, is the closed formula
\[
\boxed{R\star T=\bigcup_{r\in R,\ s\in T}
\{u\in\mathbb Z:\max(0,r+s-n)\le u\le\min(r,s)\}.}
\]
Exactly \(2n+1\) central elements are idempotent. More precisely, their rank sets are \(\{n\}\), \(\{0,\ldots,k\}\), and \(\{0,\ldots,k,n\}\) for \(0\le k<n\).

For **every** central element \(A\), one has \(A^n=A^{n+1}\), and this exponent is sharp across the family: for \(n\ge2\), \(E_{n-1}^{\,n-1}\ne E_{n-1}^{\,n}\). In particular the entire central monoid is aperiodic (all its subgroups are trivial), although for \(n\ge2\) it is not a band.

## Assumptions and scope
Multiplication of partial maps uses ordinary composition; reversing the composition convention does not change the statements. The notation \(A^m\) means an \(m\)-fold product in the power monoid, **not** a pointwise power of individual maps. A central element commutes with every nonempty subset, equivalently with every singleton. The finite base set has size \(n\ge1\); no infinite-set analogue is asserted. Rank refers to the cardinality of the domain of a partial bijection, while the elements of \(E_r\) are partial identities, not the full rank-\(r\) layer of \(\mathcal I_n\).

## Proof
**1. Central subsets contain only partial identities.** Fix a central nonempty subset \(A\subseteq\mathcal I_n\). For a point \(i\in[n]\), let \(e_i=e_{\{i\}}\). Since \(A\{e_i\}=\{e_i\}A\), no map in \(A\) can move a point. Indeed, if \(a\in A\) has \(a(i)=j\ne i\), then \(a\circ e_i\), a map with the arrow \(i\mapsto j\), belongs to \(A\{e_i\}\). But every map in \(\{e_i\}A\) has its image contained in \(\{i\}\), a contradiction. Thus every map in \(A\) is a partial identity.

Now let \(g\) be any full permutation. Centrality implies \(gA=Ag\), hence \(gAg^{-1}=A\). Under conjugation by full permutations, partial identities form exactly the \(n+1\) orbits \(E_0,\ldots,E_n\), distinguished by the size of their domains. So \(A=A_R\) for a unique nonempty rank set \(R\).

**2. Every union of rank layers is central.** Fix a partial bijection \(f:D\to J\) of rank \(d\). The products \(E_r\{f\}\) and \(\{f\}E_r\) each consist precisely of the restrictions \(f|_U\) for which \(U\subseteq D\) has cardinality \(u\) satisfying
\[
\max(0,r+d-n)\le u\le\min(r,d).
\]
For one multiplication order, choose the domain of a rank-\(r\) partial identity to have prescribed intersection \(U\) with \(D\); for the other order, prescribe the image intersection \(f(U)\) with \(J\). In either case the remaining \(r-u\) points can be chosen outside the corresponding \(d\)-element set exactly when \(0\le r-u\le n-d\). Thus \(E_r\{f\}=\{f\}E_r\). Setwise multiplication distributes over unions, so every \(A_R\) commutes with every singleton and hence every nonempty subset. This proves the centre classification and cardinality.

**3. Multiplication on the rank sets.** Partial identities satisfy \(e_D\circ e_F=e_{D\cap F}\). As \(D,F\) independently range over subsets of sizes \(r,s\), the possible cardinalities of their intersection are exactly all integers from \(\max(0,r+s-n)\) through \(\min(r,s)\), inclusive. Each possible intersection \(U\) can occur, and permutations make every partial identity of that rank occur. Therefore \(E_rE_s\) is the union of precisely those layers, and the displayed rank-set multiplication follows.

**4. All central idempotents.** Since each \(r\) belongs to the interval for \(r\star r\), we have \(A_R\subseteq A_R^2\). If an idempotent rank set \(R\) contains an integer \(r\) with \(1\le r<n\), then the product \(E_rE_r\) contains \(E_{r-1}\). Repeating forces every smaller nonnegative rank into \(R\). The rank \(n\) is the identity layer and does not create smaller ranks when multiplied by any rank. Hence every nonempty idempotent rank set is exactly one of \(\{n\}\), \(\{0,\ldots,k\}\), or \(\{0,\ldots,k,n\}\) with \(k<n\). Conversely these sets are closed under all intersection ranks, so their elements square to themselves. The alternatives are distinct, totaling \(1+2n\).

**5. A sharp stabilization identity.** The \(m\)-fold product \(E_k^m\) consists of partial identities supported on intersections of \(m\) subsets of size \(k\) in an \(n\)-element universe. Equivalently their complements, each of cardinality \(n-k\), have a union of any cardinality between \(n-k\) and \(\min(n,m(n-k))\). Indeed, a union of this cardinality can be obtained by distributing the points among the \(m\) sets, and padding each to size \(n-k\) within the chosen union. Consequently
\[
E_k^m=\bigcup_{u=\max(0,n-m(n-k))}^{k} E_u.
\]
Take a nonidentity rank-set element \(A_R\ne E_n\), and let \(k=\max(R\setminus\{n\})<n\). Its \(m\)-fold product contains \(E_k^m\), and all products containing at least one rank below \(n\) have rank at most \(k\). The rank-\(n\) layer occurs if and only if it was present initially. Since \(n-m(n-k)\le0\) for \(m\ge n\), we obtain
\[
A_R^m=\bigcup_{u=0}^{k}E_u
\quad\text{possibly together with }E_n,
\qquad(m\ge n),
\]
with \(E_n\) included precisely when \(n\in R\). Thus \(A_R^n=A_R^{n+1}\) for all central elements (also trivially for \(A_R=E_n\)). Taking \(R=\{n-1\}\), for \(n\ge2\), gives \(E_{n-1}^{n-1}=\bigcup_{u=1}^{n-1}E_u\) but \(E_{n-1}^{n}=\bigcup_{u=0}^{n-1}E_u\), proving sharpness.

An element of a subgroup of a semigroup satisfying \(x^n=x^{n+1}\) must be that subgroup's identity, by cancellation within the subgroup. Hence the centre is aperiodic. For \(n\ge2\), \(E_{n-1}^2\ne E_{n-1}\), so the centre is not a band.

## Verification
The standalone `verify.py` enumerates all partial bijections for \(n=1,2,3\) and computes their full multiplication tables directly. For \(n=1,2\), it searches **every nonempty subset** of the base monoid for centrality, giving exactly \(3\) and \(7\) central subsets. For \(n=3\), whose full power monoid is too large for subset enumeration, it independently checks that all \(15\) predicted central subsets commute with every singleton. For all three values it compares every pairwise central product against the intersection-rank formula, checks the count of central idempotents and stabilization, and detects the sharpness witness for \(n\ge2\). A separate rank-index computation checks the formulas for every nonempty rank set for \(1\le n\le9\). Execution with standard Python 3 returned `VERIFY_OK`. The finite checks support, but do not replace, the proof for all \(n\).

## Relationship to prior work
Liu and Tringali, *Kobayashi's problem for power semigroups of inverse semigroups*, arXiv:2610.29525v1 (first posted 2026-10-21), establish that inverse semigroups can be reconstructed from their power semigroups and study localizers and preservation of singletons. Their results do not state the centre, its intersection-rank multiplication, idempotent census, or stabilization index for symmetric inverse monoids. Their earlier *Power Semigroups and Two Rigidity Theorems for Groups*, arXiv:2606.01917v1, concerns global isomorphisms and unit groups, not this centre. Tringali's *Power monoids and their arithmetic: a survey*, arXiv:2602.15754v3, discusses isomorphism problems and factorization/arithmetic rather than this classification.

The present result is a theorem about a **submonoid** of the power monoid; it neither solves nor restates a power-semigroup isomorphism problem. Classical results on centralizers **inside** \(\mathcal I_n\) involve individual partial maps and do not directly determine central **subsets of** \(\mathcal I_n\) under setwise multiplication. These are implication comparisons, not claims of absolute historical priority.

## Limitations
The result is for the full nonempty power monoid of a finite symmetric inverse monoid, including the empty partial map as a base element. It is not an assertion about arbitrary inverse semigroups, the monoid of nonempty **idempotent-containing** subsets, or an infinite symmetric inverse monoid. Literature searches cannot exclude a previously unindexed formulation of the same centre theorem, possibly under the terms *rook monoid*, *semigroup of complexes*, or *setwise centralizer*; no absolute novelty is asserted. No external independent proof audit has been performed.

## References
1. S. Liu and S. Tringali, *Kobayashi's problem for power semigroups of inverse semigroups*, arXiv:2610.29525v1 (2026-10-21), https://arxiv.org/html/2610.29525v1.
2. S. Liu and S. Tringali, *Power Semigroups and Two Rigidity Theorems for Groups*, arXiv:2606.01917v1 (2026-06-01), https://arxiv.org/html/2606.01917v1.
3. S. Tringali, *Power monoids and their arithmetic: a survey*, arXiv:2602.15754v3 (2026-05-15 revision; first preprint 2026-02-17), https://arxiv.org/html/2602.15754v3.
4. J. Konieczny, *The structure of centralizers in the finite symmetric inverse semigroup*, Communications in Algebra **48** (2020), 5181–5194, https://doi.org/10.1080/00927872.2020.1782926 (abstract examined; individual-map centralizers).
