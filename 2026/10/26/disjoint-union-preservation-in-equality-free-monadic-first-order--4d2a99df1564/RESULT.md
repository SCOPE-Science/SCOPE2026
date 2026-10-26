# Disjoint-union preservation in equality-free monadic first-order logic: a canonical rank-two normal form

## Finding

Fix a finite signature of \(k\geq0\) unary predicates and no equality, constants, functions, nullary predicates, or relations of higher arity. All structures have **nonempty** domains, finite or infinite. There are \(c=2^k\) possible unary colours. Write \(C\) for their finite set, and \(S(M)\subseteq C\) for the nonempty set of colours realised by a structure \(M\). For any first-order sentence \(\varphi\), define its support family
\[
 F_\varphi=\{S\subseteq C:S\ne\varnothing,\ M_S\models\varphi\},
\]
where \(M_S\) is the finite model with one element of each colour in \(S\).

**Theorem (complete monadic disjoint-union normal form).** The following are equivalent, with identical answers for all structures and for finite structures:

1. \(\varphi\) is preserved under nonempty disjoint unions of models.
2. \(F_\varphi\) is closed under binary set union.
3. \(\varphi\) is equivalent to a formula of the form \(\forall x\,\alpha(x)\), in which \(\alpha\) is built solely from unary atoms and their negations using \(\wedge,\vee\), and existential quantifiers. No further universal or equality quantifiers occur.

There is an **effective canonical construction** of the formula in item 3 from the unique minimal nonempty-union generator basis of \(F_\varphi\). In particular, the constructed formula uses only two variables and has quantifier rank at most \(2\). This rank bound is optimal *within the target syntactic shape*: formulas \(\forall x\,\alpha(x)\) with quantifier-free \(\alpha\) cannot express the union-preserved property \(\exists y\,P(y)\) when \(k\ge1\).

Every violation of disjoint-union preservation has two finite witness models, each containing at most \(c\) elements. The number of inequivalent union-preserved sentences for \(k=0,1,2\) is respectively \(2,7,2480\), the respective counts of union-closed families of nonempty colour supports. The counts themselves are standard finite-family enumerations, not asserted as new numerical discoveries.

## Assumptions and scope

The vocabulary is purely unary and equality-free, and domains are nonempty. Disjoint union means the disjoint tagged union of domains with the unary predicates interpreted componentwise. A nonempty indexed family of models is required so that the union has nonempty domain. Both arbitrary and finite structures are covered, but neither equality nor binary predicates are allowed. The number \(k\) of predicate symbols is fixed, although the construction applies separately to every finite \(k\).

For every unary colour \(t\in C\), let \(\tau_t(z)\) be the conjunction that, for each unary predicate, asserts its positive or negated occurrence according to \(t\); for \(k=0\), this is \(\top\). For nonempty \(J\subseteq C\), put
\[
 B_J(x)=\bigvee_{t\in J}\tau_t(x),\qquad
 E_J=\bigwedge_{t\in J}\exists y\,\tau_t(y).
\]
Each existential occurrence binds its own variable and witnesses the presence of its colour somewhere in the structure.

A member \(J\) of a binary-union-closed family \(F\) is called *join-irreducible in \(F\)* when there are no proper members \(A,B\in F\) with \(A,B\subsetneq J\) and \(A\cup B=J\). Let \(\mathcal J(F)\) be their collection. The canonical sentence is
\[
 \boxed{\Theta_F=\forall x\,\bigvee_{J\in\mathcal J(F)}\bigl(B_J(x)\wedge E_J\bigr).}
\]
For empty \(F\), the disjunction is false and \(\Theta_F=\forall x\,\bot\), false because domains are nonempty. The normal form is evaluated by ordinary first-order semantics, not team semantics.

## Proof

**1. Unary support invariance (known normal-form principle).** For an assignment of any finite tuple of variables, the truth of an equality-free monadic formula depends only on their assigned colours and on the global set of colours realised. This follows by induction on formulas: unary atomic formulas depend only on the current variable's colour, Boolean connectives preserve the statement, and \(\exists z\) corresponds to choosing any realised colour for \(z\), independently of the other variables because no equality constraint exists. The universal case is dual. For sentences, all variable assignments disappear; therefore \(M\models\varphi\) depends only on \(S(M)\), for arbitrary finite or infinite \(M\). The structural observation is classical, and is not itself claimed new.

**2. Union closure and finite counterexamples.** For every nonempty family of structures \((M_i)_{i\in I}\),
\[
 S\bigl(\biguplus_{i\in I}M_i\bigr)=\bigcup_{i\in I}S(M_i).
\]
If \(\varphi\) is disjoint-union-preserved, test it on canonical finite models \(M_A,M_B\) to obtain \(A,B\in F_\varphi\Rightarrow A\cup B\in F_\varphi\). Conversely, binary union closure implies closure under unions of arbitrary nonempty families because every resulting union is a subset of the finite set \(C\), and is attained by some finite subfamily: select one input family index for each realised colour. Thus the union support lies in \(F_\varphi\) and the union model satisfies \(\varphi\). If closure fails, a pair \(A,B\in F_\varphi\) with \(A\cup B\notin F_\varphi\) supplies the claimed two countermodels of sizes at most \(c\).

**3. Canonical generators.** Every member of a finite nonempty union-closed family \(F\) is a union of members of \(\mathcal J(F)\) contained in it. Prove this by induction on the cardinality of \(S\in F\): a join-irreducible is already a generator; otherwise \(S=A\cup B\) for two proper members of \(F\), and recursively decompose each. For minimality, any family \(G\subseteq F\) generating \(F\) under nonempty unions must contain every join-irreducible \(J\in F\). Otherwise a finite union expression for \(J\) from members of \(G\) would express it as a union of two proper members of \(F\), contrary to irreducibility (discard redundant terms and group the rest). Consequently \(\mathcal J(F)\) is the unique inclusion-minimal generator family of \(F\). The empty family has the empty basis.

**4. Equivalence of the canonical sentence.** Suppose \(S=S(M)\in F\). By step 3, \(S\) is the union of members \(J\in\mathcal J(F)\), all contained in \(S\). For every element \(a\in M\) of colour \(t\in S\), some such \(J\) contains \(t\); then \(B_J(a)\) and all witnesses in \(E_J\) hold, so \(M\models\Theta_F\). Conversely, suppose \(M\models\Theta_F\). Every realised colour \(t\in S(M)\) is contained in some \(J_t\in\mathcal J(F)\) with \(E_{J_t}\) true. Thus \(J_t\subseteq S(M)\); since \(t\in J_t\), the union of these finitely many \(J_t\)'s equals \(S(M)\). Each \(J_t\in F\), so union closure gives \(S(M)\in F\). This also handles \(F=\varnothing\), because \(M\) is nonempty and \(\forall x\bot\) is false.

**5. Converse syntax and sharpness.** Every sentence \(\forall x\alpha(x)\) of the stated target grammar is preserved under disjoint unions: for any element \(a\) of one component, each inner existential statement over that component remains true when additional disjoint components are added. Because the remaining connectives are \(\wedge\) and \(\vee\), truth of \(\alpha(a)\) is monotone under such extensions, and hence holds in the total union. (The construction in step 4 suffices for the main equivalence even without using this converse.) The exact quantifier-rank upper bound is \(2\). If \(\alpha\) is quantifier-free, \(\forall x\alpha(x)\) holds precisely when every realised colour belongs to one fixed permitted set of colours; hence its support family is downward-closed under nonempty subsets. For \(k\ge1\), \(\exists y\,P_1(y)\) is preserved under unions but its support family is not downward-closed: removing the only colour satisfying \(P_1\) changes the truth value. Rank \(1\) is therefore insufficient *for the displayed restricted universal-outer grammar*, although unrestricted first-order syntax can express this example at rank \(1\).

**6. Decidability and small signatures.** Compute \(F_\varphi\) by evaluating \(\varphi\) on each of the \(2^c-1\) canonical models \(M_S\), then test binary union closure and compute \(\mathcal J(F_\varphi)\). There are finitely many possible support families, and the union-preserved ones are precisely the union-closed subfamilies of the \(2^c-1\) nonempty colour supports. Exhaustive enumeration gives \(2\), \(7\), and \(2480\) such families when \(c=1,2,4\), respectively. This is an effective construction with no complexity-optimality assertion.

## Verification

Run `python3 monadic_union_check.py`. The standalone file enumerates all \(2^{2^c-1}\) families of nonempty supports when \(c=1,2,3,4\), selects precisely those closed under union, reconstructs their join-irreducible bases, and checks the semantics of \(\Theta_F\) on every support. For \(c\le2\) it additionally checks arbitrary positive colour multiplicities on labelled domains through size four. The expected markers are `UNION_CLOSED_PROFILE_OK 1 2`, `UNION_CLOSED_PROFILE_OK 2 7`, `UNION_CLOSED_PROFILE_OK 3 61`, `UNION_CLOSED_PROFILE_OK 4 2480`, and `RANK_TWO_SHARPNESS_EXAMPLE_OK`. These finite computations validate combinatorial examples, not the all-domain proof, which is supplied above.

## Relationship to prior work

Van Benthem, ten Cate, and Yang (2026), Section 3.4, examine first-order disjoint-union preservation and the conjectured \(\forall x\alpha\) normal form, produce a counterexample *with equality*, and leave the equality-free case open. The theorem above resolves **only the purely unary fragment**, not the unrestricted equality-free problem. The older Carreiro--Facchini--Venema--Zanasi (2021/2022) full paper, Section 3.1, already proves an effective complete realised-type normal form for equality-free monadic first-order logic. The support-invariance lemma and ordinary type tests are therefore **prior mathematics**. The separate result here is the union-preservation characterisation, explicit unique irreducible basis for the restricted \(\forall x\alpha(x)\) construction, and its exact finite obstruction/rank consequences. Union-closed family enumeration and elementary finite join-semilattice theory likewise precede this work. The claim is a self-contained conjunction of these consequences motivated by the 2026 preservation question, not a claim that either component technique was invented here.

## Limitations

The nonempty-domain assumption matters for the false formula \(\forall x\bot\) and for nonempty unions. The result fails to account for equality, constants, nullary predicates, binary relations, counting, or additional generalized quantifiers. The stated rank-two optimality is **only** within the outer-universal restricted grammar; unrestricted equality-free monadic first-order logic has other rank-one formulas. The known 2021 normal form makes the reduction to finite supports direct, so historical novelty may be limited to the precise preservation formulation and canonical construction; an older specialized preservation normal form might already imply the statement. Published-priority claims are therefore qualified. No independent mathematical audit has been performed.

## References

1. J. van Benthem, B. ten Cate, and X. Yang, *When do modal definability and preservation theorems transfer to the finite?* arXiv:2603.12171v1, first publicly submitted March 12, 2026; Section 3.4. https://arxiv.org/abs/2603.12171.
2. F. Carreiro, A. Facchini, Y. Venema, and F. Zanasi, *Model theory of monadic predicate logic with the infinity quantifier*, Archive for Mathematical Logic 61 (2022), 465–502; online October 27, 2021, DOI:10.1007/s00153-021-00797-0, especially Section 3.1.
3. G. Brinkmann and R. Deklerck, *Generation of Union Closed Sets and Moore Families*, arXiv:1709.07052 (2017). Included only as background for finite union-closed family enumeration, not for logical preservation.
