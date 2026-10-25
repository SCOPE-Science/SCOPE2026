# Maximal subgroups of finite multipermutation monoids via Boolean row semilattices

## Finding

Let \(X\) be any nonempty finite set, let \(\mathcal B_X\) be the monoid of all binary relations on \(X\), and let \(\mathcal M_X\subseteq\mathcal B_X\) consist of relations in which every element of \(X\) occurs both as a source and as a target. Multiplication is ordinary relational composition, equivalently Boolean matrix multiplication. For any idempotent \(e\in\mathcal M_X\), define its Boolean row semilattice
\[
\mathcal L(e)=\{Ue:U\subseteq X\},\qquad
Ue=\{y\in X:\exists x\in U,\ (x,y)\in e\}.
\]
Then the maximal subgroup with identity \(e\) is canonically isomorphic to the automorphism group of the finite join-semilattice \((\mathcal L(e),\cup)\):
\[
H_e(\mathcal M_X)=H_e(\mathcal B_X)
\cong \operatorname{Aut}_{\vee}(\mathcal L(e)).
\]
In particular, for the reflexive order relation \(e_P\) of any finite poset \(P\),
\[
H_{e_P}(\mathcal M_P)\cong\operatorname{Aut}(P).
\]
Consequently **every finite group occurs, up to isomorphism, as a maximal subgroup of a finite multipermutation monoid**. More quantitatively, if a nontrivial finite group \(G\) has a generating set of \(d\) nonidentity elements, such a subgroup occurs already in \(\mathcal M_X\) with
\[
|X|=|G|\left(1+2d+\frac{d(d+1)}2\right).
\]
The trivial group occurs for \(|X|=1\). One may choose \(d\le\lfloor\log_2|G|\rfloor\).

## Assumptions and scope

All sets, groups and posets are finite. The term *maximal subgroup* has its semigroup-theoretic meaning: the group \(H_e(S)\) consisting of the units of the local monoid \(eSe\) at an idempotent \(e\in S\). This is not the notion of a maximal proper subgroup inside an ambient group. A Boolean relation is represented by a matrix indexed by \(X\); a *multipermutation* is one with no zero row or column. The join-semilattice automorphisms preserve unions and are bijective; preservation of the unique empty element follows automatically.

The first equality above is an equality of actual subsets of \(\mathcal B_X\), not just abstract group isomorphism. The construction does not assert a minimal carrier size and does not classify the idempotents themselves.

## Proof

**Step 1: Transfer of maximal subgroups.** Fix an idempotent \(e\in\mathcal M_X\). An element \(g\in H_e(\mathcal B_X)\) has a two-sided inverse \(h\in e\mathcal B_Xe\) such that
\[
gh=hg=e,\qquad eg=ge=g,\qquad eh=he=h.
\]
If \(g\) had an empty row, then \(gh=e\) would have an empty row, a contradiction. If \(g\) had an empty column, then \(hg=e\) would have an empty column. Hence \(g\in\mathcal M_X\). The same argument puts \(h\) in \(\mathcal M_X\). Therefore every group unit at \(e\) in \(\mathcal B_X\) is already a group unit in \(\mathcal M_X\), proving \(H_e(\mathcal B_X)=H_e(\mathcal M_X)\).

**Step 2: Identify the group with row-semilattice automorphisms.** For a relation \(r\), write \(Ur\) for the relational image of \(U\subseteq X\). The idempotence of \(e\) implies that \(\mathcal L(e)\) is precisely the family of subsets fixed by right multiplication by \(e\): if \(U\in\mathcal L(e)\), then \(Ue=U\), and conversely every fixed subset equals \(Ue\). The family contains \(\varnothing\) and is closed under unions.

Every \(g\in H_e(\mathcal B_X)\) gives a map
\[
F_g:\mathcal L(e)\longrightarrow\mathcal L(e),\qquad F_g(U)=Ug.
\]
It preserves unions and has inverse \(F_h\), where \(h\) is the inverse of \(g\). The right action satisfies \(F_{gh}=F_h\circ F_g\), so the assignment is an anti-homomorphism; the assignment \(g\mapsto F_{g^{-1}}\) is therefore a group homomorphism. It is injective: if \(e_x=\{x\}e\) denotes the row of \(e\) indexed by \(x\), then the row of \(g\) indexed by \(x\) is \(e_xg=F_g(e_x)\), since \(eg=g\).

Conversely let \(F\in\operatorname{Aut}_{\vee}(\mathcal L(e))\). Define relations \(g,h\) by specifying their rows:
\[
\{x\}g=F(e_x),\qquad \{x\}h=F^{-1}(e_x)\quad(x\in X).
\]
Every member \(U\) of \(\mathcal L(e)\) is the union of the rows \(e_x\) over \(x\in U\), since \(Ue=U\). Consequently \(Ug=F(U)\) and \(Uh=F^{-1}(U)\). Using \(e^2=e\) and the fact that \(F\) preserves unions yields \(eg=ge=g\) and \(eh=he=h\). On the row \(x\), the product \(gh\) has image \(F(e_x)h=F^{-1}(F(e_x))=e_x\); likewise \(hg=e\). Thus \(g\) is a unit at \(e\) implementing \(F\). Taking inversion in the action converts this bijective anti-homomorphism into the asserted canonical group isomorphism.

**Step 3: Poset idempotents.** For a poset \((P,\le)\), take \((p,q)\in e_P\) exactly when \(p\le q\). Reflexivity makes every row and column nonempty, and reflexivity plus transitivity gives \(e_P^2=e_P\). Its row semilattice is the lattice \(\operatorname{Up}(P)\) of upper sets, with union as join. The nonempty join-irreducibles of this lattice are exactly the principal upper sets \(\uparrow p\). Moreover, \(\uparrow p\subseteq\uparrow q\) exactly when \(q\le p\). Every join-automorphism therefore permutes principal upper sets by an order automorphism of \(P\), and conversely every order automorphism of \(P\) acts on upper sets. Hence \(\operatorname{Aut}_{\vee}(\operatorname{Up}(P))\cong\operatorname{Aut}(P)\).

**Step 4: Explicit finite-group realization.** For a nontrivial finite group \(G\), fix nonidentity generators \(s_1,\ldots,s_d\). Form a poset from the transitive closure of the following *cover relations*, for every \(g\in G\) and every index \(i\in\{1,\ldots,d\}\):
\[
v_g<a_{g,i}<b_{g,i}<c_{g,i,1}<\cdots<c_{g,i,i},
\qquad v_{gs_i}<b_{g,i}.
\]
All symbols denote distinct elements; there are no other covers. The arrows always ascend through the displayed levels, so they define a finite poset. There are \(|G|\) vertices \(v_g\), two auxiliary elements per pair \((g,i)\), and \(i\) chain markers per pair, giving the asserted size.

The heights above minimal elements distinguish the \(v\)-vertices (height zero), the \(a\)-vertices (height one), the \(b\)-vertices (height two), and the chain markers (height at least three). For each \(b_{g,i}\), the unique chain above it has length \(i\); hence an automorphism must preserve the index \(i\). Each \(b_{g,i}\) has one immediate predecessor of height one, namely \(a_{g,i}\), and one *other* minimal predecessor besides \(v_g\), namely \(v_{gs_i}\). Therefore any poset automorphism induces a permutation \(\pi\) of \(G\) obeying
\[
\pi(gs_i)=\pi(g)s_i\qquad(g\in G,\ 1\le i\le d).
\]
Because the \(s_i\) generate \(G\), it follows that \(\pi(g)=tg\) for the single element \(t=\pi(1_G)\). Conversely, each left translation \(g\mapsto tg\) extends to a poset automorphism by carrying every auxiliary symbol indexed by \(g\) to the correspondingly indexed symbol for \(tg\). There is no remaining freedom: the incident \(a\)- and \(b\)-vertices and their linear marker chains are uniquely determined by the \(v\)-vertices. Thus \(\operatorname{Aut}(P)\cong G\).

Finally, one can choose the generating list greedily, adjoining a generator only when it enlarges the subgroup already generated. Each enlargement multiplies subgroup order by at least two, so \(d\le\lfloor\log_2|G|\rfloor\). Combining this poset with Step 3 supplies the asserted maximal subgroup of \(\mathcal M_X\).

## Verification

A standalone standard-library Python program `verify.py` exhaustively checks the theorem's two group orders for every idempotent in \(\mathcal M_n\) for \(n=1,2,3\). It finds respectively \(1,7,265\) multipermutations and \(1,4,35\) idempotents; for all these idempotents it confirms \(|H_e|=|\operatorname{Aut}_{\vee}(\mathcal L(e))|\). The program also constructs the eight-element poset for \(G=C_2\), verifies that it has exactly two order automorphisms, and checks that the associated Boolean relation is a full-support idempotent. These finite checks are reproducibility tests, not proofs for all finite sets and groups: Steps 1–4 above provide the proofs.

## Relationship to prior work

Carvalho and Martin's 2021 work on multipermutations establishes Green relations and regularity tests and explicitly poses the determination of maximal subgroups as a question. The row-semilattice description for the larger monoid of *all* binary relations belongs to classical work of Zaretskii and is also reflected in Preston's 1973 and Brandon–Hardy–Markowsky's 1972 treatments. The contribution here is the exact, all-idempotent transfer from the full relation monoid to the *full-support* relation monoid, including an explicit realization of every finite group inside the latter with a finite carrier bound. The classical full-relation results are acknowledged rather than repackaged as new. The full text of Preston's 1973 paper was not accessible for direct inspection; a possible earlier equivalent support-preserving construction remains a literature risk.

## Limitations

The theorem classifies the abstract maximal subgroup at each given idempotent, not the idempotents or their multiplicities, and does not give a minimum carrier size for a specified finite group. Its construction is finite and is not asserted to generalize to arbitrary infinite sets. The literature search cannot guarantee priority, especially because the closest classical paper on maximal subgroups of all binary relations was available only through its abstract and bibliographic record. No independent audit or independent validation has been performed.

## References

1. Catarina Carvalho and Barnaby Martin, *The lattice and semigroup structure of multipermutations*, arXiv:2103.06012v1, posted 10 March 2021; *International Journal of Algebra and Computation* 32 (2022), 211–235. https://arxiv.org/abs/2103.06012
2. G. B. Preston, *Any group is a maximal subgroup of the semigroup of binary relations on some set*, *Glasgow Mathematical Journal* 14 (1973), 21–24. https://doi.org/10.1017/S0017089500001683
3. R. L. Brandon, D. W. Hardy, and G. Markowsky, *The Schützenberger group of an \(\mathcal H\)-class in the semigroup of binary relations*, *Semigroup Forum* 5 (1972), 45–53. https://doi.org/10.1007/BF02572873
4. K. A. Zaretskii, *The semigroup of binary relations*, *Matematicheskii Sbornik* 61 (1963), 291–305.
