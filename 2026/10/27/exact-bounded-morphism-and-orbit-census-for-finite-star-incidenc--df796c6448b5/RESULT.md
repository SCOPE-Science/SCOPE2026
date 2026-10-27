# Exact bounded-morphism and orbit census for finite star-incidence frames
## Finding
For integers \(r,s\ge2\), let \(S_r\) denote the finite reflexive Kripke frame with worlds \(c,v_1,\ldots,v_r,e_1,\ldots,e_r\), with exactly the nonreflexive accessibility pairs \(c<e_i\) and \(v_i<e_i\), for \(1\le i\le r\). It is the incidence order of the star graph with \(r\) edges. A bounded morphism is a function preserving accessibility and satisfying the usual back condition. It is called *onto* when globally surjective on worlds.

Every onto bounded morphism \(S_r\to S_s\) is uniquely described by a word of length \(r\) over \(2s\) tagged symbols: for each \(i\), choose \(j_i\in\{1,\ldots,s\}\) and a tag \(\epsilon_i\in\{L,E\}\); require that each target index \(j\) occurs with tag \(L\) at least once. The function corresponding to the word is
\[
f(c)=c',\qquad f(e_i)=e'_{j_i},\qquad f(v_i)=\begin{cases}v'_{j_i}&\epsilon_i=L,\\ e'_{j_i}&\epsilon_i=E.\end{cases}
\]
Consequently the number of onto bounded morphisms of these fixed, indexed frames is
\[
N(r,s)=\sum_{k=0}^{s}(-1)^k\binom{s}{k}(2s-k)^r.
\]
In particular, an onto bounded morphism exists if and only if \(r\ge s\).

Up to independent automorphisms of source and target, the maps are classified by unordered multisets of exactly \(s\) pairs \((\ell,m)\) of integers with \(\ell\ge1\), \(m\ge0\), whose coordinate sums total \(r\). If \(O(r,s)\) is the number of such map-orbits, then for \(r,s\ge2\),
\[
O(r,s)=[u^s z^r]\prod_{n\ge1}(1-u z^n)^{-n}.
\]
The product is interpreted formally; its coefficients outside the specified \(r,s\ge2\) domain are not asserted to count morphisms of exceptional one-arm frames. For example, \(N(4,2)=110\) and \(O(4,2)=6\), while \(N(3,2)=18\) and \(O(3,2)=2\).

## Assumptions and scope
A reflexive Kripke frame is a pair \((W,R)\) with \(R\) reflexive; the frames here are finite partial orders, so \(R\) is also transitive and antisymmetric. A bounded morphism \(f:(W,R)\to(W',R')\) obeys *forth*, \(xRy\implies f(x)R'f(y)\), and *back*, \(f(x)R'y'\implies(\exists y\in W)\,xRy\text{ and }f(y)=y'\). Global surjectivity is an additional hypothesis. The source and target worlds are indexed as displayed; the literal count is not divided by automorphisms. All parameters are integers \(r,s\ge2\), including \(r<s\), when the count is zero. Automorphism orbits are for the action \(\operatorname{Aut}(S_r)\times\operatorname{Aut}(S_s)\) by pre- and post-composition.

## Proof
Write the source star's minima as the center \(c\) and leaves \(v_i\), and its maxima as the edge-worlds \(e_i\). For a maximal source world \(e_i\), back says every target successor of \(f(e_i)\) is already the image of \(e_i\), hence \(f(e_i)\) must be maximal in the target and therefore equal some \(e'_{j_i}\).

A source leaf \(v_i\) has only two successors, itself and \(e_i\). If it mapped to the target center \(c'\), back would demand preimages for all \(s\) target maxima, as well as \(c'\). This is impossible with only two successors when \(s\ge2\). Therefore \(f(v_i)\) is either a target leaf or target maximum. Since \(v_i<e_i\) and the only strict upper world of target leaf \(v'_j\) is \(e'_j\), its image must be either \(v'_{j_i}\) or \(e'_{j_i}\). (If both source worlds collapse to a maximal target, back is automatic at the leaf.)

Since the map is globally surjective, some source world maps to \(c'\). Maximal source worlds map to maximal target worlds; source leaves cannot map to \(c'\); hence necessarily \(f(c)=c'\). Surjectivity also demands that for every target leaf \(v'_j\) some source leaf maps there, which is exactly the assertion that index \(j\) occurs with tag \(L\). Conversely any tagged word having all \(s\) such occurrences defines a surjective order-preserving map. Back at each maximal source world is automatic. At a leaf mapping to \(v'_j\), the two target successors \(v'_j,e'_j\) are respectively attained by that leaf and its edge-world; at a leaf mapping to a maximum, back is automatic. At the center, its successors are itself and all source edge-worlds, and every target maximum is attained because some tagged \(L\) word uses each index. Thus back holds everywhere. This proves the bijection.

For each target index, there are two possible tags \(L,E\). To enforce at least one \(L\) occurrence in each of \(s\) indices, inclusion–exclusion on missing target-leaf symbols gives \(N(r,s)\). A tagged word with all target-leaf tags exists exactly when \(r\ge s\), proving the sharp existence criterion without depending on numerical cancellation.

The center is the unique minimal world having \(r\ge2\) incomparable strict successors; each other minimum has just one, and each maximum is uniquely paired with its degree-one lower leaf. Hence \(\operatorname{Aut}(S_r)\cong\mathfrak S_r\), acting by simultaneous permutation of source leaf-edge arms; similarly \(\operatorname{Aut}(S_s)\cong\mathfrak S_s\). The source action rearranges tagged letters, and the target action relabels their target indices. Exactly the multiplicity pairs \((\ell_j,m_j)\), with \(\ell_j\ge1\), classify the joint orbits, up to permutation of indices \(j\). For a pair of total size \(n\ge1\), there are exactly \(n\) options for \(\ell\in\{1,\ldots,n\}\), with \(m=n-\ell\). A multiset of these types therefore has bivariate ordinary generating function \(\prod_{n\ge1}(1-u z^n)^{-n}\). Extracting degree \(u^s z^r\) proves the orbit formula.

## Verification
The standalone standard-library program `artifacts/verify_star.py` independently constructs both reflexive accessibility matrices, enumerates *all* globally surjective functions for the three parameter pairs \((r,s)=(2,2),(3,2),(3,3)\), and tests the forth and back clauses directly. It additionally enumerates all tagged words and orbit vectors for the twelve parameter pairs with \(2\le r\le6\) and \(2\le s\le\min(4,r)\), comparing them with independent inclusion–exclusion and generating-function coefficient calculations. A further fourteen source-size boundary sweeps verify positivity against the existence criterion. The saved execution output ends with `VERIFY_OK`. Finite tests are corroborating checks only; the universal assertions follow from the preceding proof.

## Relationship to prior work
Barmak and Minian study finite posets and their incidence/Hasse models in *Minimal Finite Models* (2006). Their work supplies context for star-incidence posets but concerns homotopy rather than modal bounded morphisms. Hodkinson and Hussain's *The Modal Logic of Affine Planes Is Not Finitely Axiomatisable* (2008), especially Definition 2.4 and Remark 2.5, discusses bounded morphic images of incidence-based two-sorted frames. Their setting imposes sort preservation and additional modal relations, and their results concern axiomatisability, not enumeration of single-sorted reflexive star frames. Bozzelli et al.'s *Refinement Modal Logic* (2012) studies simulations, refinements, and modal semantics but not these exact finite quotient counts. Existing finite complete-height-two mapping-space classifications use complete bipartite comparability and ordinary order maps rather than the sparse star incidence relation with the modal back clause. Those statements do not imply either enumerator here without a new frame-specific argument.

## Limitations
The theorem concerns *unvalued*, one-relation, reflexive finite Kripke frames with \(r,s\ge2\), globally onto bounded morphisms, and no root-point preservation requirement. It does not count all monotone maps, non-surjective bounded morphisms, homomorphisms in a two-sorted incidence language, morphisms preserving valuations, or maps between arbitrary trees. The orbit product counts maps modulo both frame automorphism groups, not maps up to modal equivalence. The originality comparison involved targeted source and statement searches and accessible primary literature; an unlocated specialized earlier formula remains possible. No independent validation or publication-priority certification is claimed.

## References
1. J. A. Barmak and E. G. Minian, *Minimal Finite Models*, arXiv:math/0611156v1, first public 2006-11-06, especially Section 2 (finite orders) and Section 4 (graph models).
2. I. Hodkinson and A. Hussain, *The Modal Logic of Affine Planes Is Not Finitely Axiomatisable*, *Journal of Symbolic Logic* 73(3) (2008), especially Section 2.2, https://www.doc.ic.ac.uk/~imh/papers/affine.pdf.
3. L. Bozzelli, H. van Ditmarsch, T. French, J. Hales and S. Pinchinat, *Refinement Modal Logic*, arXiv:1202.3538v1, first public 2012-02-16, especially Sections 2–3.
