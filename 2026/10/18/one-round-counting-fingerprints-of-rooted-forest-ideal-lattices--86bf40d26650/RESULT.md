# One-round counting fingerprints of rooted-forest ideal lattices of width at most two

## Finding
Let \(P\) be a nonempty finite rooted forest, regarded as a poset by ancestry (roots minimal), whose width is at most two. Let \(J(P)\) be its lattice of order ideals with the directed cover relation \(I\to I\cup\{p\}\). For each ideal \(I\), let \(d_-(I)\) and \(d_+(I)\) count its lower and upper covers. Define
\[
F_P(x,y)=\sum_{I\in J(P)}x^{d_-(I)}y^{d_+(I)},\qquad B_P(y)=F_P(1,y).
\]

**Complete paired fingerprint:** For any two such forests \(P,Q\), equality \(F_P=F_Q\) holds if and only if \(P\cong Q\). Thus the multiset of one-round directed counting-refinement colours on the ideal lattice determines the underlying rooted forest. Within this family of ideal lattices, two-variable first-order logic with counting, \(C^2\), distinguishes nonisomorphic members with a sentence of quantifier rank at most two.

**Complete one-sided fibres:** For \(n=|P|\), every forest of width two has \(B_P(y)=1+ny+my^2\) for an integer \(m\). At fixed \(n\), the exact number of isomorphism classes with this polynomial equals
\[
M_n(m)=\#\{1\le a\le b:ab=m,\ a+b\le n-1\}
+\#\{1\le c\le d:cd=m,\ c+d=n\}.
\]
The first nonisomorphic one-sided collision occurs at \(n=5\), uniquely between two chains of lengths \(1,4\) and a tree with a single root and two length-two arms. The first collision between *connected* forests occurs at \(n=6\), between a fork with one-vertex stem and arms of lengths \(1,4\), and a fork with two-vertex stem and arms of lengths \(2,2\).

**A sharp arithmetic subfamily:** Among collisions of a two-chain forest with a connected fork having a one-vertex stem, the size \(n\) admits a collision exactly when the odd integer \(2n-1\) is composite. Such collision pairs correspond bijectively to unordered factorizations \(2n-1=(2k+1)(2r+1)\) with \(1\le k\le r\): the arm lengths are \(k(r+1),r(k+1)\), and the two separate chain lengths are \(kr,(k+1)(r+1)\).

## Assumptions and scope
All forests are finite and unordered; an isolated vertex is both a chain and a rooted tree. A rooted forest poset is a disjoint union of rooted trees with each ancestor below its descendants. The width is the largest antichain size, equivalently the total number of terminal vertices of these rooted components. The empty forest is excluded from the theorem, although its fingerprint would be \(1\). The formula for \(M_n(m)\) concerns width exactly two; the unique width-one chain on \(n\) vertices has \(B(y)=1+ny\).

Every width-two forest has exactly one of the following mutually exclusive shapes: (i) disjoint chains \(C_c\sqcup C_d\), with \(1\le c\le d\); or (ii) a connected fork \(Y_{s;a,b}\), with a stem of \(s\ge1\) vertices, terminating in a branching vertex followed by two chains of lengths \(1\le a\le b\). Its total size is \(n=s+a+b\). The fork with \(s=1\) has its root as branching vertex. Equality and isomorphism refer to the directed cover structures, so the root orientation is part of the objects.

## Proof
For any ideal \(I\), its lower covers arise by deleting one maximal member of \(I\), while its upper covers arise by inserting one minimal member of \(P\setminus I\). Both counts add under disjoint unions of forests. For a chain of \(t\ge1\) elements, the empty ideal has degree pair \((0,1)\), the whole chain has \((1,0)\), and the \(t-1\) other ideals have \((1,1)\); therefore
\[
F_{C_t}(x,y)=x+y+(t-1)xy.
\]
For a forest of two chains, multiplication gives
\[
F_{C_c\sqcup C_d}=x^2+2xy+y^2+(c+d-2)(x^2y+xy^2)+(c-1)(d-1)x^2y^2.
\]
For a fork with one-vertex stem, the empty ideal contributes \(y\). The nonempty ideals include the root and independent ideals of the two arm chains. In the product of the arm polynomials, the root-only ideal has to change its lower-cover count from zero to one; its upper-cover count is two. Thus
\[
F_{Y_{1;a,b}}=y+F_{C_a}F_{C_b}+(x-1)y^2.
\]
Adding each further vertex atop the old root as a new minimal root (extending the stem) changes the polynomial by \(xy\): the previous ideals are transported by adjoining that new root, except the empty ideal, and one obtains an additional singleton initial ideal. Iterating \(s-1\) times yields
\[
F_{Y_{s;a,b}}=x^2+y+(s+1)xy+(a+b-2)x^2y+(a+b-1)xy^2+(a-1)(b-1)x^2y^2.
\]
The three shape classes are separated by their monomials: a chain has highest \(x\)-degree one; a two-chain forest has a \(y^2\) term of coefficient one; and a connected fork has no \(y^2\) term but has an \(x^2\) term. For a two-chain forest, the \(x^2y\) coefficient determines \(c+d\), while the \(x^2y^2\) coefficient determines \((c-1)(d-1)\), hence determines \(cd\) and the unordered pair \(\{c,d\}\). For a fork, the \(xy\) coefficient determines \(s\); the \(x^2y\) coefficient determines \(a+b\); and the \(x^2y^2\) coefficient determines \((a-1)(b-1)\), hence \(ab\) and the unordered pair \(\{a,b\}\). This proves injectivity for all sizes.

Substituting \(x=1\) gives \(B_{Y_{s;a,b}}(y)=1+(s+a+b)y+ab y^2\) and \(B_{C_c\sqcup C_d}(y)=1+(c+d)y+cd y^2\). The canonical shape decomposition is unique, so counting solutions of these Diophantine constraints gives exactly \(M_n(m)\). Exhausting the elementary positive parameter possibilities for \(n\le4\) gives no collision; at \(n=5\) the two displayed structures both have \(m=4\) and give the only collision; among connected forks the first coincidence is the two displayed \(n=6\) types, both with \(m=4\).

For the stem-one/fork versus two-chain subfamily, equality becomes \(a+b+1=c+d\) and \(ab=cd\). Order each pair increasingly; necessarily \(c<a\le b<d\). Write \(k=a-c\ge1\). The sum equation gives \(d-b=k+1\), and equality of products yields \((k+1)a-kb=k(k+1)\). Coprimality of \(k,k+1\) implies \(a=k(r+1)\), \(b=r(k+1)\), \(c=kr\), \(d=(k+1)(r+1)\) for an integer \(r\ge k\). Conversely all such parameters work. Their shared size satisfies \(2n-1=(2k+1)(2r+1)\), proving the stated bijection and odd-compositeness criterion.

To obtain the finite-model-theoretic statement, define \(\theta_{i,j}(v)\) using exactly two variables and counting quantifiers to assert that a vertex has exactly \(i\) incoming and \(j\) outgoing cover-neighbours. Each \(\theta_{i,j}\) has quantifier rank one, and a sentence asserting that exactly \(m\) vertices satisfy \(\theta_{i,j}\) has rank two. Distinct fingerprints differ in such a coefficient, so one rank-two \(C^2\) sentence separates each pair of nonisomorphic members of this family. This is relative identification, not a statement about all finite directed graphs or all distributive lattices.

## Verification
Run `python3 verify_width2.py`. It independently enumerates ideals by bitmasks of explicitly built parent arrays, computes both cover degrees from the definition, compares their histograms with the closed formulas for every canonical width-at-most-two forest on \(1\le n\le15\), and checks polynomial injectivity and exact univariate fibre multiplicities. It also checks 120 odd-factor collision instances. The recorded execution ends in `VERIFY_OK`, with 323 canonical types checked. The all-size results follow from the algebraic derivations above, not the finite run.

## Relationship to prior work
Finite-distributive-lattice representation as an order-ideal lattice is classical; Siggers (arXiv:1412.0011) discusses related representations. Chaudhary and Gordon (1991) developed complete, substantially richer tree polynomials from greedoid ranks. Burghart (arXiv:2302.08394; Electronic Journal of Combinatorics 31(4), 2024, #P4.37) defines a bivariate rooted-subtree size/boundary polynomial \(S_T(z,y)\), proves it is complete for rooted forests, and gives \(S_T(z,y)=y+z\prod_iS_{T_i}(z,y)\) for a rooted tree. The one-sided polynomial here is exactly the specialization \(S_P(1,y)\) (with product across components); its general recurrence is therefore established background, NOT a new contribution. The contribution claimed here is the explicit complete fibre classification at width two, the paired-cover-degree reconstruction by a weaker and different invariant (without ideal sizes), the first sharp collisions, and the arithmetic collision spectrum. Burghart's stronger size/boundary invariant distinguishes every rooted forest, but its theorem does not state or imply that the *paired cover-degree histogram* is injective on width two, nor supply the stated fibres of its one-variable specialization. No claim of a new general subtree-polynomial recurrence is made.

## Limitations
The paired-histogram reconstruction has been proved only for rooted-forest posets of width at most two. No conclusion is claimed for width three, general rooted forests, or arbitrary finite posets; the computer check does not establish results beyond its enumerated range. The one-sided fibre classification is specific to the same two-leaf family; outside this family different phenomena can occur. Two-variable counting identification is only relative to the specified ideal lattices, not an absolute defining sentence against all structures. The novelty comparison is based on inspected primary literature and research-index searches; earlier specialized results may exist. Independent external review has not occurred.

## References
1. M. Siggers, *On the representation of finite distributive lattices*, arXiv:1412.0011 (first arXiv submission 2014-11-28).
2. S. Chaudhary and G. Gordon, *Tutte polynomials for trees*, Journal of Graph Theory 15 (1991), 317–331, DOI:10.1002/jgt.3190150308.
3. F. Burghart, *Polynomial invariants for rooted trees related to their random destruction*, Electronic Journal of Combinatorics 31(4) (2024), #P4.37, DOI:10.37236/11975, arXiv:2302.08394.
