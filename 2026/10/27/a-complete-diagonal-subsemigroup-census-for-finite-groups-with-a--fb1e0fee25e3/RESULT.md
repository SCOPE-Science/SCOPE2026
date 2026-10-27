# A complete diagonal-subsemigroup census for finite groups with a fresh identity

## Finding

Let \(G\) be any finite group with identity \(e\), and let \(S=G\sqcup\{\ast\}\) be the monoid obtained by adjoining a **new** global identity \(\ast\), distinct from \(e\). A diagonal subsemigroup is a relation \(\rho\subseteq S\times S\) that contains every \((s,s)\) and is closed under coordinatewise multiplication.

Every diagonal subsemigroup has a **unique** form
\[
\rho(N,A,B)=\{(g,h)\in G\times G:gh^{-1}\in N\}
\cup\{(\ast,\ast)\}
\cup(\{\ast\}\times A)\cup(B\times\{\ast\}),
\]
where \(N\trianglelefteq G\), and each of \(A,B\) is **independently** either the empty set or a subgroup of \(N\). Conversely, every such triple gives a diagonal subsemigroup. Inclusion is precisely coordinatewise inclusion of \(N,A,B\) (with \(\varnothing\) below every subgroup).

Write \(s(N)=|\{H:H\leq N\}|\), and \(k(G)=|\{N:N\trianglelefteq G\}|\). Then the complete numbers of diagonal subsemigroups, symmetric diagonal subsemigroups, and congruences are, respectively,
\[
D(S)=\sum_{N\trianglelefteq G}(s(N)+1)^2,\qquad
T(S)=\sum_{N\trianglelefteq G}(s(N)+1),\qquad
C(S)=2k(G).
\]
A triple gives a symmetric relation precisely when either \(A=B=\varnothing\), or \(A=B\) is a subgroup; it gives a congruence precisely when either \(A=B=\varnothing\), or \(A=B=N\).

Consequently the diagonal-subsemigroup coefficient is
\[
\chi(S)=\frac{2k(G)}{\sum_{N\trianglelefteq G}(s(N)+1)^2}.
\]
It equals \(1/2\) when \(G\) is trivial and is strictly less than \(1/2\) for every nontrivial finite group. In particular, for any prime \(p\) and integer \(r\geq0\),
\[
\chi\bigl((C_{p^r})^\sharp\bigr)=
\frac{2(r+1)}{\sum_{j=0}^{r}(j+2)^2}
\sim\frac{6}{r^2}\quad(r\longrightarrow\infty),
\]
where the superscript \(\sharp\) means that a fresh identity is adjoined even though the group already has one. Thus among finite Clifford semigroups with the **same two-element idempotent semilattice**, the coefficient has infimum zero. This is one integrated classification and its enumerative consequences.

## Assumptions and scope

The group \(G\) is arbitrary but finite, including the one-element group; it need not be abelian. The new element \(\ast\) satisfies \(\ast x=x\ast=x\) for every \(x\in S\). Products of two old group elements are taken in \(G\); in particular, \(e\neq\ast\). The set \(\varnothing\) in the parameters is a formal allowed choice, not a subgroup. Congruences are equivalence relations compatible with the semigroup multiplication. The coefficient \(\chi(S)=C(S)/D(S)\) counts **labeled relations**, not relations modulo automorphisms.

## Proof

**1. Restriction to the group block.** Let \(\rho\) be a diagonal subsemigroup. The intersection \(K=\rho\cap(G\times G)\) is a subsemigroup of the finite group \(G\times G\) containing its full diagonal. Every nonempty subsemigroup of a finite group is a subgroup: for each member, a positive power equals the identity and the preceding power is its inverse. Therefore \(K\) is a subgroup containing the diagonal. Define \(N=\{g\in G:(g,e)\in K\}\). It is a normal subgroup, because conjugating \((g,e)\) by \((h,h)\) leaves the second coordinate \(e\) and produces \((hgh^{-1},e)\). Moreover \((g,h)\in K\) if and only if \((gh^{-1},e)\in K\), by multiplying by \((h^{-1},h^{-1})\); hence \(K=\{(g,h):gh^{-1}\in N\}\). This determines \(N\) uniquely.

**2. Both cross-sections.** Put \(A=\{a\in G:(\ast,a)\in\rho\}\) and \(B=\{b\in G:(b,\ast)\in\rho\}\). Each is closed under multiplication because \(\rho\) is; when nonempty it is a subgroup of the finite group \(G\) by the same positive-power argument. For \(a\in A\), multiply \((\ast,a)\) with the diagonal pair \((e,e)\). The product \((e,a)\) belongs to \(K\), so \(a^{-1}\in N\), hence \(a\in N\). Similarly \(B\subseteq N\). The remaining block contains \((\ast,\ast)\) and has no other elements. Thus the asserted triple is forced and unique.

**3. Converse closure.** Fix arbitrary \(N\trianglelefteq G\) and \(A,B\) each empty or a subgroup of \(N\). Pairs in the \(G\times G\) block have equal images in \(G/N\). Multiplying one such pair by a cross-block pair results in a \(G\times G\) pair with equal images in \(G/N\), because the old-group entry in every cross pair lies in \(N\). Multiplying two cross pairs of the same orientation stays in that orientation and uses closure of \(A\) or \(B\). Multiplying opposite cross orientations yields a pair in \(N\times N\), contained in the group block. The pair \((\ast,\ast)\) is the identity of \(S\times S\). Therefore \(\rho(N,A,B)\) is closed and contains the diagonal. The unique recovery of the three blocks also proves the asserted coordinatewise inclusion criterion.

**4. Symmetry, transitivity, counts.** Inversion of a relation swaps \(A,B\), while the group block is symmetric because \(N\) is normal. Thus symmetry holds precisely for \(A=B\). If these sections are both empty, \(\ast\) is a singleton equivalence class and the group block is a congruence. If they are a nonempty subgroup \(H\le N\), then \((\ast,e)\) and \((e,n)\) lie in the relation for every \(n\in N\); transitivity requires \((\ast,n)\), forcing \(H=N\). Conversely \(H=N\) makes \(\ast\) part of the \(N\)-coset class and all other classes the remaining \(N\)-cosets, producing a congruence. For each \(N\), the two independently chosen cross sections have \(s(N)+1\) possibilities apiece; exactly \(s(N)+1\) paired choices are symmetric, and exactly two choices are congruences. Summation gives \(D,T,C\) and the coefficient.

**5. The fixed-idempotent-semilattice phenomenon.** If \(G\) is trivial, its only normal subgroup has one subgroup, so \(D=4\), \(C=2\). For nontrivial \(G\), every \(N\) has \(s(N)\ge1\), while \(s(G)\ge2\). Hence \(D>4k(G)\), implying \(\chi(S)<1/2\). When \(G=C_{p^r}\), normal subgroups are \(C_{p^j}\) for \(0\le j\le r\), with \(s(C_{p^j})=j+1\); the displayed formula follows. Since the denominator is \(r^3/3+O(r^2)\), the quotient is asymptotic to \(6/r^2\). In every \(S\), the idempotents are exactly \(e\) and \(\ast\), satisfying \(e\ast=\ast e=e\), so their semilattice is always the same two-element chain.

## Verification

The standalone standard-library script `verify.py` reconstructs the product table of \(G\sqcup\{\ast\}\), independently enumerates **every reflexive binary relation** on the underlying set for cyclic groups of orders one through four and the Klein four-group, and tests coordinatewise closure, symmetry, and transitivity by direct multiplication. It then computes predicted counts from independently enumerated subgroup and normal-subgroup sets and checks all normal-form relations. It also checks every predicted normal form for the nonabelian symmetric group on three symbols. Observed \((D,T,C)\) triples are \((4,2,2)\), \((13,5,4)\), \((13,5,4)\), \((29,9,6)\), \((67,17,10)\), and \((62,12,6)\) in that order. The script prints `VERIFY_OK` on success. The infinite-family claims depend on the proof, not on finite checks.

## Relationship to prior work

Barber and Ruškuc introduced the finite DSC coefficient and, in their 2026 paper on Rees matrix semigroups, gave the bound \(0<\chi(S)\le\chi(E(S))\) for finite Clifford semigroups. In Section 4 they explicitly use a finite group with an adjoined new identity to show that their constructed family of diagonal subsemigroups is incomplete. Their formula is a lower bound for the number of such relations, not an enumeration of this specific family. The present theorem classifies **all** cross-block relations in their example by two independent subgroup parameters, and supplies exact symmetric and congruence counts and a fixed-semilattice vanishing sequence.

Their earlier paper establishes that a finite semigroup has no noncongruence diagonal subsemigroups exactly when it is a group, and recalls the normal-subgroup description in finite groups. That result gives no number for the adjoined-identity case. Later work on left groups addresses direct-product left-group semigroups, not this non-product two-level Clifford family. No absolute historical-priority claim is made.

## Limitations

The result concerns exactly a finite group with one **fresh** identity adjoined, not an arbitrary strong semilattice of groups or an arbitrary finite Clifford semigroup. A finite-only step uses that subsemigroups of finite groups are groups, so the proof does not extend without modification to infinite groups. The coefficient counts actual relations; it is not an isomorphism-class count. Older or unindexed semigroup literature might contain an equivalent specialized enumeration, despite targeted searches. No external independent mathematical audit has been performed.

## References

1. C. Barber and N. Ruškuc, *Comparing numbers of diagonal subsemigroups and congruences for semigroups*, arXiv:2602.17286, first version 2026-02-19; especially Section 4 (Clifford semigroups and the fresh-identity example). https://arxiv.org/abs/2602.17286
2. C. Barber and N. Ruškuc, *Semigroup congruences and subsemigroups of the direct square*, Bulletin of the Australian Mathematical Society 113 (2026), 123–134; first arXiv version 2025-04-03, arXiv:2504.02428. https://arxiv.org/abs/2504.02428
3. *On Group-like Properties of Left Groups*, Mathematics 13 (2025), 3109; Section 5 discusses diagonal subsemigroups for left groups. https://www.mdpi.com/2227-7390/13/19/3109
