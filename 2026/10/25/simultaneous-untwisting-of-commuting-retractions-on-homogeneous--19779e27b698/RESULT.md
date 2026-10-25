# Simultaneous untwisting of commuting retractions on homogeneous finite group-sets

## Finding
Let \(W\) be any finite group, not necessarily abelian, and let \(\mathcal T_n\) denote the full transformation monoid on \([n]\), where \(n\geq1\). In the group-labelled transformation monoid \(W\wr\mathcal T_n\), **every finite pairwise commuting family of idempotents is simultaneously conjugate by a diagonal unit in \(W^n\) to a family with every group label equal to the identity**. The conjugating unit does not permute the \(n\) positions.

More exactly, for \(k\ge1\) and an ordered pairwise-commuting idempotent tuple \((f_1,\ldots,f_k)\) of \(\mathcal T_n\), set
\[
 c=\left|\bigcap_{j=1}^k\operatorname{im}(f_j)\right|.
\]
There are exactly
\[
\boxed{|W|^{n-c}}
\]
ordered pairwise-commuting idempotent tuples in \(W\wr\mathcal T_n\) projecting to that fixed tuple. They constitute one orbit under conjugation by diagonal units \(W^n\); the stabilizer is naturally the direct product of \(c\) copies of \(W\), one for each common-product fiber. In particular, if \(b_{n,k,c}\) counts ordered pairwise commuting \(k\)-tuples of idempotents of \(\mathcal T_n\) whose product has rank \(c\), then the corresponding number in the group-labelled monoid is
\[
\boxed{\sum_{c=1}^{n} b_{n,k,c}|W|^{n-c}.}
\]
The statement applies to every arity \(k\), including arbitrarily many compatible retractions, and to nonabelian \(W\).

The same simultaneous normalization applies to every finite commutative idempotent subsemigroup (semilattice subsemigroup). For a specified base subsemigroup \(B\subseteq\mathcal T_n\), its distinct group-labelled subsemigroup lifts projecting bijectively onto \(B\) number \(|W|^{n-c(B)}\), where \(c(B)\) is the rank of the product of all elements of \(B\). A commuting idempotent family cannot contain distinct members with the same base transformation; consequently maximal commuting-idempotent subsemigroups project bijectively to, and arise from, maximal commuting-idempotent subsemigroups of \(\mathcal T_n\).

For any finite group \(G\), subgroup \(H\le G\), and homogeneous \(G\)-set consisting of \(n\) copies of \(G/H\), the theorem applies to its equivariant endomorphism monoid with \(W=N_G(H)/H\).

## Assumptions and scope
All sets and groups are finite, with \(n\ge1\) and \(k\ge1\). A map in \(W\wr\mathcal T_n\) is encoded as \((f,a)\), with \(f:[n]\to[n]\) and \(a=(a_1,\ldots,a_n)\in W^n\), acting on the disjoint union of regular \(W\)-orbits by \((w,i)\mapsto(w a_i,f(i))\). Composition is read from right to left:
\[
 (f,a)\circ(h,b)=\left(f\circ h,\bigl(b_i a_{h(i)}\bigr)_{i=1}^n\right).
\]
An element \((f,a)\) is idempotent exactly when \(f^2=f\) and \(a_x=1_W\) for every \(x\in\operatorname{im}(f)\). A diagonal unit is \((\mathrm{id},s)\) with \(s\in W^n\). No commutativity assumption is imposed on \(W\). The word 'conjugation' refers only to conjugation inside this finite monoid by its diagonal unit subgroup.

## Proof
**1. The common retraction.** Let \(E_1,\ldots,E_k\) be commuting idempotents. Their product \(P=E_1\circ\cdots\circ E_k\) is idempotent, and for each \(j\), \(P\circ E_j=E_j\circ P=P\). Write \(P=(p,a)\). Since \(P^2=P\), the base \(p\) is idempotent and \(a_x=1_W\) at every \(x\in\operatorname{im}(p)\).

**2. One diagonal conjugation kills all labels.** Put \(D=(\mathrm{id},a)\). Its inverse is \((\mathrm{id},(a_i^{-1})_i)\), and the composition rule gives
\[
 D\circ P\circ D^{-1}=(p,\mathbf1).
\]
Indeed, the label at \(i\) of the conjugate is \(a_i^{-1}a_i a_{p(i)}=1_W\). Write \(E'_j=D\circ E_j\circ D^{-1}=(f_j,b^{(j)})\). Then \((p,\mathbf1)\circ E'_j=(p,\mathbf1)\). Comparing the \(i\)-th labels gives \(b_i^{(j)}=1_W\) for all \(i\) and \(j\). Thus every \(E'_j=(f_j,\mathbf1)\). This argument uses neither the number of maps nor commutativity of \(W\).

**3. Orbit and fiber count.** Fix a base tuple \((f_1,\ldots,f_k)\), and write \(p=f_1\circ\cdots\circ f_k\). Every group-labelled commuting lift is in the \(W^n\)-orbit of its unlabeled lift by step 2. A diagonal unit \((\mathrm{id},s)\) fixes the unlabeled product \((p,\mathbf1)\) exactly when \(s_i=s_{p(i)}\) for every \(i\). This says that \(s\) is constant on each of the \(c=|\operatorname{im}(p)|\) fibers of \(p\). Such a unit fixes each unlabeled \((f_j,\mathbf1)\) as well: the relation \(p\circ f_j=p\) implies \(p(f_j(i))=p(i)\), hence \(s_{f_j(i)}=s_i\). So the exact stabilizer is \(W^c\), of order \(|W|^c\), and the orbit contains \(|W|^{n-c}\) elements. For commuting idempotents, \(\operatorname{im}(p)=\bigcap_j\operatorname{im}(f_j)\): the product image lies in every constituent image, and it fixes the intersection pointwise. The formula follows.

**4. Semilattices and maximality.** For a finite commutative idempotent subsemigroup \(B'\), take the product of all its members and apply step 2 to the entire set. After conjugation, every element has trivial group labels. Thus the base projection is injective on \(B'\) and identifies \(B'\) with its image \(B\), a subsemigroup of commuting idempotents in \(\mathcal T_n\). Step 3 counts its lifts. If \(B\) is not maximal, first untwist and add an unlabeled idempotent commuting with \(B\), together with any missing products; conversely a purported extension of a lift of maximal \(B\) untwists to a larger base commuting family, which is impossible. Therefore maximality corresponds.

**5. Homogeneous equivariant version.** Every equivariant self-map of \(G/H\) is determined by the image of the coset \(H\), which must be an \(H\)-fixed coset; the resulting permutation group of equivariant automorphisms is \(N_G(H)/H\). Choosing orbit identifications in a disjoint union of \(n\) copies yields precisely the above group-labelled transformation monoid. Hence all preceding conclusions transfer.

## Verification
The standalone Python program `verify_gacts_multi.py` directly enumerates the idempotent group-labelled transformations, composes maps using each group's multiplication law, and checks all ordered pairwise-commuting tuples in small cases. The independently enumerated base-map profile is weighted by \(|W|^{n-c}\) and compared **for every product-rank cell**, not just in total. It tests cyclic groups and two nonisomorphic groups of order four, as well as the nonabelian group \(S_3\). The largest verified higher-arity instances are \(35,641\) commuting ordered quadruples for \(n=3\), \(|W|=6\), and \(286,673\) commuting ordered triples for \(n=4\), \(|W|=4\). Every one of the \(8,137\) commuting ordered triples for \(n=3\), \(W=S_3\), is also directly conjugated to its unlabeled counterpart by the product-label gauge. The program outputs `VERIFY_OK simultaneous higher-arity group-labelled idempotents`. Finite computations corroborate but do not replace the proof for arbitrary finite groups and tuple sizes.

## Relationship to prior work
The standard wreath-product model, its individual idempotence criterion, and exact **single-idempotent** counts are established in A. D. H. Al-Aadhami's thesis, Section 4.3.1. The general equivariant endomorphism and automorphism framework is developed by Castillo-Ramirez and Ruiz-Medina. Work by Dandan, Dolinka, and Gould on the free idempotent generated semigroup uses the same wreath-product setting and biordered idempotents. Earlier rank-profile enumeration of **pairs** of commuting idempotents of ordinary transformation monoids is distinct prior coverage; this note does not claim a new pair count. The present theorem concerns simultaneous diagonal conjugacy for *arbitrary-size commuting families*, the exact lift torsor for every base family, semilattice extensions, and maximality, including for nonabelian groups. These stronger statements do not follow merely from the standard single-idempotent enumeration or from knowing two-map counts.

## Limitations
This result does not classify the base semilattice subsemigroups of \(\mathcal T_n\), and it does not provide a closed form for \(b_{n,k,c}\) at arbitrary \(k\); it provides an exact universal lifting formula in terms of those intrinsic base counts. It does not extend unmodified to a monoid label alphabet with noninvertible elements, nor to nonhomogeneous unions of inequivalent orbit types. The literature comparison covered directly relevant primary sources and an accessible thesis section, but did not exhaust every historical treatment of wreath-product conjugacy or group-valued cocycles. Independent validation has not been performed.

## References
1. A. D. H. Al-Aadhami, *Combinatorial Questions for \(S\wr_n\mathcal T_n\) for a Semigroup*, University of York thesis (2017; first verified open repository deposit 2018-02-26), Chapter 4, Section 4.3.1. https://etheses.whiterose.ac.uk/id/eprint/19494/
2. A. Castillo-Ramirez and R. H. Ruiz-Medina, *The relative rank of the endomorphism monoid of a finite \(G\)-set*, arXiv:2203.12158v1 (posted 2022-03-23). https://arxiv.org/abs/2203.12158
3. Y. Dandan, I. Dolinka, and V. Gould, *Free idempotent generated semigroups and endomorphism monoids of free \(G\)-acts*, arXiv:1402.4042 (first posted 2014-02-17). https://arxiv.org/abs/1402.4042
4. R. F. Petersen, *Transformation Semigroups Over Groups*, North Carolina State University thesis (2008); repository abstract consulted as historical conjugacy background, not assessed as full-text evidence. https://repository.lib.ncsu.edu/items/befddea1-461e-4252-81a1-84b642df8546
