# Exact arity boundary for the finite-model property of polyadic Kripke logic

## Finding

In classical set theory with choice, let \(\tau\) be any set-sized polyadic modal signature: a set of operator symbols \(O\), together with a set \(I_o\) of argument positions for each \(o\in O\). Use the Boolean connectives and well-founded modal formula trees, permitting a node \(\Delta_o\) to have one immediate subformula at each position of \(I_o\). Interpret these formulas on arbitrary nonempty Kripke frames with relations \(R_o\subseteq W\times W^{I_o}\) using the existential-tuple modality.

Then the unrestricted logic has the finite-model property **if and only if every argument-position set \(I_o\) is finite**. The signature may have infinitely many operators and nullary operators.

When any \(I_o\) is infinite, failure of the finite-model property is witnessed by a single satisfiable formula containing **no propositional atoms and using only that operator**. Its smallest possible model cardinality is \(\aleph_0\).

## Assumptions and scope

All sets and structures are ordinary sets in ZFC. A frame has a nonempty world set \(W\) and, for every \(o\in O\), a relation \(R_o\subseteq W\times W^{I_o}\). The semantic clause is

\[
w\models\Delta_o((\varphi_i)_{i\in I_o})\ \Longleftrightarrow\ \exists f:I_o\to W\;\bigl(R_o(w,f)\ \land\ \forall i\in I_o\ f(i)\models\varphi_i\bigr).
\]

Formula trees are *well-founded*, though the sets of immediate subformulas need not be finite and modal depth need not have a finite uniform bound. Boolean negation and binary disjunction remain finitary; \(\top\) abbreviates \(\neg\bot\). No restriction such as transitivity, seriality, or image-finiteness is imposed on the frames. The finite-model property here means that every satisfiable formula has some finite-world model (not necessarily a submodel of its given model).

## Proof

**All arities finite.** Fix a satisfiable formula \(\varphi\). Its parse tree is well-founded and finitely branching, hence finite (a finitely branching infinite tree would admit an infinite branch). Therefore the set \(S\) of subformulas is finite. Starting from a model \(M\) of \(\varphi\), put \(u\sim v\) when \(u\) and \(v\) agree on the truth of every element of \(S\). The quotient \(W/{\sim}\) has at most \(2^{|S|}\) elements. For each operator, define the quotient relation on tuple classes by the existence of a related tuple of representatives. Keep the induced atomic valuations, which are well-defined for atoms in \(S\); atoms outside \(S\) may be assigned arbitrarily.

Induct over \(S\) to prove the filtration truth lemma. For the modal step, an original witness yields a quotient witness. Conversely, a quotient witness for \(\Delta_o((\theta_i))\) comes from an original tuple at some \(u'\sim u\), with successor representatives in the required classes. By induction these successors satisfy the respective \(\theta_i\); thus \(u'\) satisfies the modal formula, and therefore \(u\) does too because the formula belongs to \(S\). For a nullary operator the same argument uses the unique empty tuple. The quotient is finite and still satisfies \(\varphi\).

**An infinite arity.** Fix \(o\in O\) with infinite \(I_o\). In ZFC choose an injection \(j:\mathbb N\hookrightarrow I_o\), and write \(a=j(0)\). Define a derived unary modal context \(E\theta:=\Delta_o((\eta_i)_{i\in I_o})\), with \(\eta_a=\theta\) and \(\eta_i=\top\) otherwise. For each \(n\in\mathbb N\), let

\[
\chi_n:=E^n\top\ \land\ \neg E^{n+1}\top.
\]

Here \(E^0\top=\top\) and \(E^{n+1}\top=E(E^n\top)\). A world satisfying \(E^{n+1}\top\) has an \(E\)-path of length \(n+1\), hence also an \(E\)-path of every shorter length. It follows that the truth sets of \(\chi_n\) and \(\chi_m\) are disjoint whenever \(n\ne m\), in **every** frame, including cyclic ones.

Form the single well-founded, infinitely branching formula

\[
\Phi:=\Delta_o((\rho_i)_{i\in I_o}),\qquad
\rho_{j(n)}=\chi_n\ (n\in\mathbb N),\quad
\rho_i=\top\ (i\notin j[\mathbb N]).
\]

The tree of \(\Phi\) is well-founded: every immediate subtree has finite modal depth (although it may itself branch infinitely), and these depths are unbounded as \(n\) varies. If \(w\models\Phi\), a witness \(f:I_o\to W\) must assign each \(j(n)\) to a world satisfying \(\chi_n\). By disjointness, the worlds \(f(j(n))\) are pairwise different. Thus any model of \(\Phi\) has at least \(\aleph_0\) worlds.

To establish satisfiability with *exactly* \(\aleph_0\) worlds, take \(W=\mathbb N\cup\{r\}\), with \(r\notin\mathbb N\), and let all other modal relations be empty. For \(n\ge1\), make the only \(o\)-tuple at \(n\) the map \(g_n\) with \(g_n(a)=n-1\) and \(g_n(i)=0\) for \(i\ne a\); give \(0\) no \(o\)-tuple. At \(r\), use the unique \(o\)-tuple \(g_r\) satisfying \(g_r(j(n))=n\) for all \(n\), and \(g_r(i)=0\) for the remaining positions. On natural-number worlds, the derived modality \(E\) follows the decreasing successor path, so \(n\models\chi_n\) for every \(n\). Consequently \(r\models\Phi\). This attains the lower cardinal bound and completes both directions.

## Verification

The accompanying standalone `verify.py` checks, for each finite arity from \(1\) to \(9\), a finite approximation of the witness formula and the corresponding explicit chain model. It checks that the \(n\)-th height formula holds exactly at world \(n\), that the root satisfies the approximant, and that distinct height formulas have no common world in these examples. Running `python verify.py` reports `INFINITE_ARITY_FMP_VERIFY_OK`.

This is a finite *sanity test*, not a substitute for either the arbitrary-signature filtration proof or the infinite-arity cardinality argument.

## Relationship to prior work

Girlando and Montesi, *Library-Grade Modal Logic* (arXiv:2610.04511v1, publicly available 2026-10-03), Section 3, introduce polynomial-functor signatures whose modal operators can have arbitrary, including infinite, sets of argument positions and give the relational semantics used here. Their article addresses general modal infrastructure and correspondence principles rather than a finite-model-property characterization by arity.

Finite filtrations for ordinary propositional modal logic are classical; they supply the positive half here. Jaakkola's study of polyadic modal logic (arXiv:2210.01034) concentrates on finitary operator signatures and computational complexity. Sayed Ahmed's 2013 *Interpolation for infinitary modal logic using polyadic algebras* permits infinite-arity **atomic predicates** in quantified modal logic, a different source of infinitary syntax. Bellas Acosta and Venema's *Counting to Infinity* introduces an **infinity diamond**, an additional generalized unary operator that directly tests infinite successor sets; this differs from gaining infinite expressivity through the argument-position set of an ordinary existential-tuple diamond.

The contribution isolated here is the uniform **if-and-only-if arity criterion for arbitrary polyadic modal signatures**, with an atom-free countable witness in the failing case. Older treatments of infinitary modal trees could contain an equivalent or dominating general theorem; no definitive claim of historical uniqueness is made.

## Limitations

The result assumes ZFC (in particular a countably infinite subset of every infinite set), unrestricted existential-tuple frames, classical Boolean semantics, and well-founded infinitary branching syntax. It does **not** assert failure of finite models when infinitely many operators are present but each has finite arity. It does not apply automatically to a language that artificially forbids formulas with unboundedly many immediate subformulas, nor to special frame classes with extra restrictions. The construction does not characterize satisfiability complexity or model sizes of arbitrary infinite-arity formulas. No independent audit has been performed.

## References

1. M. Girlando and F. Montesi, *Library-Grade Modal Logic*, arXiv:2610.04511v1 (2026-10-03), https://arxiv.org/html/2610.04511v1 .
2. R. Jaakkola, *Complexity of Polyadic Boolean Modal Logics: Model Checking and Satisfiability*, arXiv:2210.01034 (2022), https://arxiv.org/abs/2210.01034 .
3. T. Sayed Ahmed, *Interpolation for infinitary modal logic using polyadic algebras*, arXiv:1304.0958v1 (2013), https://arxiv.org/html/1304.0958v1 .
4. I. Bellas Acosta and Y. Venema, *Counting to Infinity: Graded Modal Logic with an Infinity Diamond*, *Review of Symbolic Logic* 17 (2024), 1–35, doi:10.1017/S1755020322000247 .
5. P. Blackburn, M. de Rijke and Y. Venema, *Modal Logic*, Cambridge University Press (2001), standard filtration and polyadic modal syntax.
