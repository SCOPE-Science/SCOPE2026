# Seven rank-two first-order theories of finite dicyclic groups

## Finding

Let \(\operatorname{Dic}_n=\langle a,b\mid a^{2n}=1,\ b^2=a^n,\ bab^{-1}=a^{-1}\rangle\) for every integer \(n\ge2\), a group of order \(4n\). Use first-order logic with equality, a named identity \(e\), and a **ternary relation** \(M(u,v,w)\) interpreted as \(uv=w\), rather than multiplication as a function symbol. Write \(G\equiv_2H\) when the groups satisfy the same sentences of quantifier rank at most two.

**Theorem.** The family has precisely seven rank-two equivalence classes. Three are the singleton widths \(n=2\), \(n=3\), and \(n=4\). For \(n,m\ge5\),
\[
 \operatorname{Dic}_n\equiv_2\operatorname{Dic}_m
 \quad\Longleftrightarrow\quad
 (3\mid n\iff3\mid m)\ \land\ (4\mid n\iff4\mid m).
\]
No group from one of the first three classes is equivalent to any other class. The least parameter representatives of all seven classes are \(2,3,4,5,6,8,12\); therefore every group in this family has a rank-two equivalent representative of order at most \(48\), and \(48\) is the sharp maximum among minimal representative orders.

## Assumptions and scope

The dicyclic group is presented above, with the given identity interpreted as a constant and multiplication as a *relational* ternary predicate. Only \(n\ge2\) is considered, excluding the degenerate cyclic case \(n=1\). The quantifier rank is the maximal nesting depth; a conjunction of two existential subformulas inside one outer existential has rank two. No claim is made in the functional group language, where nested terms have different expressive power.

## Proof

**1. Rank-two atomic diagrams.** For any group \(G\) with identity \(e\), every atomic equality and multiplication statement involving only \(e,x,y\) is determined by the following eight truth values:
\[
 x=e,\quad y=e,\quad x=y,\quad x^2=e,\quad y^2=e,\quad xy=e,\quad x^2=y,\quad y^2=x.
\]
Indeed, multiplication by \(e\) is an identity, \(xy=x\) forces \(y=e\), \(xy=y\) forces \(x=e\), and \(xy=e\) is equivalent to \(yx=e\). The only remaining nontrivial products are the squares. Conversely all eight tests are atomic. For a fixed first-round pick \(x\), denote by \(S_G(x)\) the set of eight-bit diagrams realized by varying the second-round pick \(y\). The standard two-round game criterion says that \(G\equiv_2H\) exactly when the collections \(\{S_G(x):x\in G\}\) and \(\{S_H(x):x\in H\}\) agree. This is a set of sets, not a count of witnesses, because each side has only one further move.

**2. Dicyclic square roots and the involution.** Let \(z=a^n\). The elements are the rotations \(a^j\) and the nonrotation elements \(a^jb\) for \(j\) modulo \(2n\). Their squares are
\[
 (a^j)^2=a^{2j},\qquad(a^jb)^2=z.
\]
There is exactly one involution \(z\); it is central. No nonrotation element can be a square. A rotation is a square precisely when its exponent is even, except that \(z\) is also a square of every nonrotation element. Each nonrotation element has order four and is not itself a square.

**3. Complete first-pick categories.** Divide possible first picks \(x\) into the following seven categories, where *rooted* means that some \(y\) satisfies \(y^2=x\): identity; involution; order three; unrooted order four; rooted order four; unrooted order other than \(1,2,3,4\); and rooted order other than \(1,2,3,4\). For \(n\ge3\) the extension spectrum \(S_G(x)\) depends only on this category, not on \(n\) or the chosen element. To verify this statement directly, the possible special second picks are \(y=e\), \(y=z\), \(y=x\), \(y=x^{-1}\), \(y=x^2\), and \(y^2=x\); the first four can coincide in the obvious small-order cases. Their equalities and associated eight atomic tests depend exactly on the category. For an element of order three, \(x^{-1}=x^2\) is itself a root; the additional, different root \(zx^{-1}\) always exists. For \(x=e\), the root \(z\) always exists. For \(x=z\), each nonrotation gives a root. For a rooted element of order four or higher, all roots not among those named are a single additional atomic diagram. Thus no extra category emerges from root multiplicities.

There is also always a *generic* second pick, for which \(y\notin\{e,z,x,x^{-1},x^2\}\) and \(y^2\ne x\): if \(x\) is a rotation other than \(z\), choose \(y=b\); if \(x\) is a nonrotation, choose \(y=a\); and if \(x=z\), choose \(y=a\), which works for \(n\ge3\) because \(a^2\ne z\). For \(x=e\), choose \(y=a\) as well. These witnesses, together with the special possibilities, exhaust all eight-bit diagrams: by the atomic reduction in step 1, any remaining \(y\) has exactly the generic diagram. The only exception at \(n=2\) is that \(S_G(z)\) has no such generic witness; the theorem treats that group separately.

**4. Which categories exist.** Identity, the unique involution, and unrooted order-four elements occur for every \(n\ge2\). Order-three elements occur precisely when \(3\mid n\). Rooted order-four elements occur precisely when the cyclic rotation subgroup has an element of order eight, equivalently \(4\mid n\). An unrooted element of order other than \(1,2,3,4\) occurs for every \(n\ge3\): the generator \(a\) has order \(2n\ge6\) and is not a square. A rooted element of this last order category occurs precisely when \(n\ge5\): for \(n\ge5\), \(a^2\) has order \(n\ge5\) and root \(a\); for \(n=2,3,4\), any square in the rotation subgroup has order dividing \(n\), and nonrotation squares are just \(z\). These existence statements and step 3 prove the equivalence in the theorem for all \(n,m\ge5\).

**5. Sharp separation.** The following three rank-two sentences distinguish all seven cases. Write \(M(u,v,w)\) for multiplication. First,
\[
 \Phi_3:=\exists x\exists y\,[x\ne e\land M(x,x,y)\land M(x,y,e)],
\]
which holds precisely when an element of order three exists. Second,
\[
 \Phi_8:=\exists x\,[\,(\exists y\ M(y,y,x))\land
 (\exists z\ [M(x,x,z)\land z\ne e\land M(z,z,e)])\,],
\]
which holds precisely when some order-four element has a square root. Third, define
\[
 \begin{aligned}
 \Phi_{\mathrm{gen}}:=\exists x\,[&x\ne e\land\neg M(x,x,e)\land
 (\exists y\,M(y,y,x))\\
 &\land\neg\exists y\,[M(x,x,y)\land M(x,y,e)]\\
 &\land\neg\exists y\,[M(x,x,y)\land y\ne e\land M(y,y,e)]\,].
 \end{aligned}
\]
This says that a square-rooted element exists whose order is none of \(1,2,3,4\). The triples of truth values \((\Phi_3,\Phi_8,\Phi_{\mathrm{gen}})\) are \((0,0,0)\) at \(n=2\), \((1,0,0)\) at \(n=3\), \((0,1,0)\) at \(n=4\), and \((\mathbf{1}_{3\mid n},\mathbf{1}_{4\mid n},1)\) for \(n\ge5\). These are exactly seven different triples, so all seven predicted classes are distinct. The representative bound follows, with the last class first appearing at \(n=12\). This completes the proof.

## Verification

Two independent finite checks accompany this proof. The direct checker constructs each \(\operatorname{Dic}_n\), evaluates all atomic equalities and all \(27\) multiplication atoms on \((e,x,y)\), and forms exact two-round extension profiles for \(2\le n\le56\). The second checker independently uses the reduced eight-predicate basis, includes *every* first-round choice, and checks the proposed seven-class classification through \(n=100\). Both checks complete with PASS. Neither finite check is used in place of the infinite proof in steps 1–5.

Reproduce using `python3 verify_dic_rank2_direct.py` and `python3 verify_dic_rank2_basis.py` (Python standard library only). Their exact recorded outputs are supplied alongside the programs.

## Relationship to prior work

Gomaa's 2007 thesis (chapter 3, especially §§3.1–3.3 and 3.8) uses precisely the identity-and-ternary-product language, studies cyclic-group quantifier depth, and proves a transfer theorem for **split dihedral groups** and their cyclic rotation groups (Lemma 3.10). The non-split dicyclic construction is not treated there. Morozov and Nies study the first-order theories of broad classes of finitely generated groups rather than the seven fixed-rank types here. Daugulis gives a full classification of generating-pair presentations and Cayley-graph presentation equivalence for dicyclic groups, not first-order quantifier-rank equivalence. The statements do not imply this exact classification through any identified rank-preserving reduction.

The distinction is structural: these groups have a unique involution and all nonrotations have order four, unlike split dihedral groups, whose nonrotations have order two. Nevertheless the family retains a precise periodic logical signature in \(3\)- and \(4\)-divisibility.

## Limitations

This is a relative classification of the family \(\operatorname{Dic}_n\) in the relational signature only. It does not classify arbitrary nonabelian groups, higher quantifier ranks, or the language with multiplication as a function. Historical priority beyond the inspected sources is not independently certified, and no independent mathematical audit is claimed.

## References

1. Walid Gomaa, *Model Theory and Complexity Theory*, PhD dissertation, University of Maryland, 2007; chapter 3, pp. 45–91, especially Lemma 3.10, pp. 87–88. https://api.drum.lib.umd.edu/server/api/core/bitstreams/5a564fe0-5c19-4da2-8ce0-2cc76964e427/content
2. A. Morozov and A. Nies, *Finitely Generated Groups and First-Order Logic*, J. London Math. Soc. 71 (2005), 545–562, DOI 10.1112/S0024610704006106. https://doi.org/10.1112/S0024610704006106
3. P. Daugulis, *Classifying presentations of finite groups—the case of dicyclic groups*, arXiv:1903.06639 (2019), §§2.3 and 3. https://arxiv.org/html/1903.06639v1
