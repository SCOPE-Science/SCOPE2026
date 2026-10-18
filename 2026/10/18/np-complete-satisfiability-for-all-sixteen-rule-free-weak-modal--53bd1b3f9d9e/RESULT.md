# NP-complete satisfiability for all sixteen rule-free weak modal closure logics

## Finding

Let \(\Lambda\) be **any** subset of \(\{\mathsf M,\mathsf C,\mathsf N,\mathsf K\}\), with no modal replacement-of-equivalents rule and no generalization/necessitation rule. For the weak modal logic \(L_\Lambda\) of Nishimura's closure semantics, satisfiability of an arbitrary finite formula is **NP-complete** and validity is **coNP-complete**, under polynomial-time many-one reductions. The choice of \(\Lambda\) may itself be supplied as a four-bit input without changing the complexity bounds. This includes the case where conjunction-aggregation \(\mathsf C\), distribution \(\mathsf K\), and all other listed axioms are present together.

More precisely, given a formula of length \(n\), a satisfying model, if one exists, admits a certificate consisting of at most \(n\) propositional truth bits and at most \(n\) membership bits for the modal bodies occurring in the formula. All modal membership checks can be performed by a polynomial-time saturation on at most \(n+1\) syntactic subformulas. Thus exponentially many candidate witnesses may exist, but **each is checkable in polynomial time**.

## Assumptions and scope

The language is classical propositional modal logic with a single unary modal connective \(\Box\); negation, implication, and the usual Boolean constants/connectives are permitted. **Syntax matters**: conjunction is the fixed syntactic connective (or its fixed, uniquely parsed Boolean abbreviation), and formulas are not replaced by classically equivalent alternatives inside \(\Box\). Brackets/associativity of nested conjunctions are retained. The input formula is given as an ordinary finite syntax tree; equality of formulas means literal syntactic equality after consistently expanding the chosen Boolean abbreviations.

A closure model assigns each world \(w\) a set \(H_w\) of modal formulas and interprets \(w\models\Box\alpha\) precisely when \(\alpha\in H_w\). The allowed conditions, when selected in \(\Lambda\), are: \(\mathsf N\), membership of \(\top\); \(\mathsf M\), removal of conjuncts from a member \(\alpha\wedge\beta\); \(\mathsf C\), insertion of \(\alpha\wedge\beta\) from two members; and \(\mathsf K\), insertion of \(\beta\) when \(\alpha\) and \(\alpha\to\beta\) are members. Arbitrary modal nesting within \(\alpha,\beta\) is allowed. There is **no rule** of replacement of equivalents or generalization. This is exactly the rule-free sixteen-system subfamily of the 2026 closure semantics, not the congruential non-normal modal cube.

For a set \(G\) of formulas write \(\operatorname{Cl}_\Lambda(G)\) for its least set closed under these selected rules. Given any finite **subformula-closed** set \(S\) containing \(G\cup\{\top\}\), let \(Q\) be the least subset of \(S\) containing \(G\) and saturated by every selected rule **only when its conclusion belongs to \(S\)**. Then the finite-support lemma is

\[
\boxed{\operatorname{Cl}_\Lambda(G)\cap S=Q.}
\]

If \(\top\) is not selected by \(\mathsf N\), adjoining it to \(S\) does not assert that it is a member of \(Q\).

## Proof

**Finite-support lemma.** Because every rule used to construct \(Q\) is a legitimate unrestricted rule, \(Q\subseteq\operatorname{Cl}_\Lambda(G)\). Write \(\widehat Q\) for the set of **all finite binary conjunction trees whose leaves lie in \(Q\)**, including one-leaf trees (that is, \(Q\subseteq\widehat Q\)). This is a possibly infinite set when \(\mathsf C\) is enabled; it is useful as a proof device even otherwise.

First establish \(\widehat Q\cap S=Q\). If a conjunction tree \(t\) of leaves in \(Q\) is itself in \(S\), either \(t\in Q\) already, or it is a newly built term \(u\wedge v\). Subformula-closure gives \(u,v\in S\). Inductively, \(u,v\in Q\). The finite saturation adds \(u\wedge v\), so \(t\in Q\). When \(\mathsf C\) is absent, take \(\widehat Q=Q\) and the equality is immediate.

Now verify that \(\widehat Q\) is closed under all selected rules. The \(\mathsf C\)-condition holds by construction when enabled. The \(\mathsf N\)-condition holds because finite saturation includes \(\top\). For \(\mathsf M\), if \(u\wedge v\in\widehat Q\) arose by constructing a conjunction tree, its two children are also in \(\widehat Q\); if it was a leaf in \(Q\), finite saturation had already inserted its two conjuncts in \(Q\subseteq\widehat Q\) because \(S\) is subformula-closed. For \(\mathsf K\), suppose \(u\to v\in\widehat Q\) and \(u\in\widehat Q\). A newly formed conjunction has a conjunction head, not an implication head, so \(u\to v\in Q\). Consequently \(u\in S\), as a subformula of \(u\to v\in S\); the established intersection equality yields \(u\in Q\). Finite saturation then inserts \(v\in Q\), since \(v\) is also a subformula of the implication. This checks all possibilities. Thus \(\operatorname{Cl}_\Lambda(G)\subseteq\widehat Q\) by leastness, and intersecting with \(S\) completes the lemma. The proof uses literal term structure; identifying classically equivalent conjunctions would invalidate this argument.

**NP membership.** Given input \(\varphi\), let \(S=\operatorname{Sub}(\varphi)\cup\{\top\}\). Guess a truth value for each propositional variable occurring in \(\varphi\), and a truth value for every distinct modal occurrence \(\Box\alpha\) (duplicates must agree). Let \(G\) consist precisely of bodies \(\alpha\) of those occurrences guessed true. Thus \(G\subseteq S\). Saturate \(G\) within \(S\) using the finite rules; accept only if every guessed true body belongs to the resulting \(Q\) and every guessed false body is absent. Then evaluate \(\varphi\) propositionally using the guessed bits for modal occurrences and accept if it evaluates true.

For **soundness**, use one world with the guessed propositional valuation and \(H=\operatorname{Cl}_\Lambda(G)\). It satisfies all selected closure conditions, and the lemma says that every relevant box has exactly the guessed truth value. Propositional evaluation then gives \(\varphi\). For **completeness**, take any model satisfying \(\varphi\) at any world. Guess the propositional values and exact box values seen there. Every body guessed true belongs to the world's closed set \(H_w\). Hence \(G\subseteq H_w\), and the least-closure property gives \(\operatorname{Cl}_\Lambda(G)\subseteq H_w\). So no guessed-false body can appear in that least closure. Every guessed-true body was seeded, and all checks succeed.

There are at most \(n+1\) distinct elements of \(S\). Each saturation round adds an element or terminates, so at most \(n+1\) proper rounds occur. Every rule can be tested over the at most quadratic collection of premise pairs, with syntactic equality/lookups available in polynomial time (e.g. by interning syntax-tree nodes). This gives a deterministic polynomial-time certificate verifier, including \(\mathsf C\) and \(\mathsf K\) together.

**Lower bounds.** Boolean SAT reduces identically to satisfiability of modal-free formulas, since their truth is ordinary propositional truth in all sixteen systems. Thus satisfiability is NP-hard. A formula is invalid exactly when its negation is satisfiable. Complementing establishes coNP membership for validity, and classical tautology validity on modal-free formulas gives coNP-hardness. This proves both completeness statements for every fixed \(\Lambda\) and for the four-bit-uniform problem.

## Verification

The accompanying self-contained \`verify.py\` performs two logically distinct finite checks for all sixteen subsets of the four axioms. It compares subformula saturation to a separately implemented, term-size-bounded unrestricted closure on randomly generated formula sets, and compares saturation to exhaustive Boolean enumeration of finite Horn-closed subsets of the support. The seeded check produced

\`WEAK_MODAL_VERIFY_OK direct_bounded_closure=394 independent_horn_enumerations=391\`.

The comparison to bounded unrestricted closure is **not** an exhaustive infinite-closure computation, and neither set of finite checks proves the theorem for arbitrary formulas. The unrestricted claim follows from the proof above. Reproduce with \`python3 verify.py\` using only the standard Python library.

## Relationship to prior work

Nishimura, *Closure Semantics for Weak Modal Logics: Completeness and Representations* (arXiv:2610.01433, first released 2026-10-01), establishes strong completeness and one-point finite-model constructions for exactly this family in Theorem 3.12 and Corollaries 3.13–3.14. It explicitly shows primitive-recursive decidability. Its proof of Corollary 3.14 mentions restricting closure computation to a finite subformula set; this is related to the finite-support lemma and **must not be treated as a newly discovered device in isolation**. The contribution here is the sharp, uniform NP/coNP completeness classification and explicit polynomial certificate, not one-point-model existence or primitive-recursive decidability.

Dalmonte and Mazzullo, *CoNP Complexity for Combinations of Non-normal Modal Logics* (2023, DOI 10.1007/978-3-031-43513-3_17), proves complexity bounds for non-normal modal systems **containing replacement of equivalents**. It notes that its class with conjunction agglomeration behaves differently from the coNP cases. Its hypotheses do not cover any of the present explicitly noncongruential systems, including the \(\mathsf C\)-cases. Kogure and Kurahashi, *Modal logics of conjunctively closed provability predicates* (arXiv:2607.08730, 2026), study systems based on the **necessitation** logic (there labelled \(\mathsf N\)); those are outside this rule-free family and do not supply its sixteen uniform decision bounds. Standard NP modal satisfiability results in stronger normal systems likewise do not supply the proposed bound.

## Limitations

The result is strictly confined to absence of the modal inference rules RE and Gen. It makes **no** complexity assertion for systems containing either rule, or for alternative syntactic presentations which quotient the bodies of modal formulas by classical equivalence. Formula length assumes the usual explicit syntax-tree/string encoding rather than a circuit or succinct-DAG encoding. Only worst-case decision complexity is classified; the proof does not give a deterministic polynomial-time algorithm for SAT. Exhaustive finite experiments do not establish an infinite theorem. Older work on noncongruential/syntactic logics might contain an equivalent complexity classification; novelty is assessed from the specified inspections and searches rather than asserted as a universal bibliographic certainty.

## References

1. Yuki Nishimura, *Closure Semantics for Weak Modal Logics: Completeness and Representations*, arXiv:2610.01433, submitted 2026-10-01, https://arxiv.org/abs/2610.01433. Full HTML consulted, especially Definitions 2.1–2.5 and 3.7, Theorem 3.12, and Corollaries 3.13–3.14.
2. Tiziano Dalmonte and Andrea Mazzullo, *CoNP Complexity for Combinations of Non-normal Modal Logics*, in *Logics in Artificial Intelligence* (2023), DOI 10.1007/978-3-031-43513-3_17, https://link.springer.com/chapter/10.1007/978-3-031-43513-3_17. Full open-access HTML consulted, especially Sections 1–2 and main complexity results.
3. Haruka Kogure and Taishi Kurahashi, *Modal logics of conjunctively closed provability predicates*, arXiv:2607.08730, submitted 2026-07-09, https://arxiv.org/abs/2607.08730. Introduction and syntactic semantics context consulted.
4. S. A. Cook, *The Complexity of Theorem-Proving Procedures*, 1971; L. A. Levin, *Universal Search Problems*, 1973 (classical SAT NP-completeness background).
