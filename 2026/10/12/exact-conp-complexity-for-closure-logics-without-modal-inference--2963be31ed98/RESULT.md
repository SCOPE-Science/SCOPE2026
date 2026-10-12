# Exact coNP complexity for closure logics without modal inference rules
## Finding

Fix
\[
\Lambda\subseteq\{\mathsf M,\mathsf C,\mathsf N,\mathsf K\}
\]
in Nishimura's closure-semantics family \(L_\Lambda\). These are exactly the sixteen systems in that family with no modal inference rule \(\mathsf E\) or \(\mathsf G\).

Then
\[
\boxed{\operatorname{SAT}(L_\Lambda)\text{ is NP-complete}}
\]
and
\[
\boxed{\operatorname{VAL}(L_\Lambda)\text{ is coNP-complete}.}
\]

By the source's strong completeness theorem, validity may equivalently be replaced by theoremhood/provability.

The source proves a finite model property and primitive-recursive decidability for these systems and explicitly leaves computational complexity as a problem. The exact upper bound follows from a polynomial relevance argument for the source's one-point closure models. The main point is that the closure operator may itself be infinite when \(\mathsf C\) is present, but only a polynomial-size finite fragment can matter to evaluation of a fixed input formula.

## Assumptions and scope

The source defines, for
\[
\Lambda\subseteq\{\mathsf E,\mathsf G,\mathsf M,\mathsf C,\mathsf N,\mathsf K\},
\]
a Hilbert system \(L_\Lambda\) and a matching class of closure frames.

For the present theorem,
\[
\Lambda\subseteq\{\mathsf M,\mathsf C,\mathsf N,\mathsf K\}.
\]
Thus neither of the modal inference rules \(\mathsf E\) or \(\mathsf G\) is available.

For a finite generator \(\Gamma\), the closure \(cl_\Lambda(\Gamma)\) is obtained by iterating the rules corresponding to the selected axioms. The relevant operations are:

\[
\mathsf N:\quad \top\text{ is available},
\]

\[
\mathsf M:\quad
\psi\wedge\chi\in S\Longrightarrow \psi,\chi\in S,
\]

\[
\mathsf C:\quad
\psi,\chi\in S\Longrightarrow \psi\wedge\chi\in S,
\]

and

\[
\mathsf K:\quad
\psi,\ \psi\to\chi\in S\Longrightarrow \chi\in S.
\]

The source proves that, for these no-inference systems, failure of derivability has a countermodel on a singleton world whose closure generator is drawn from a finite fragment built from subformulas of the formula under consideration.

Complexity is measured with the formula given in an ordinary explicit syntax-tree or string representation. The set \(\Lambda\) is fixed, not part of the input.

## Proof

We prove hardness and membership separately.

### Lower bounds

Every system \(L_\Lambda\) extends classical propositional logic and leaves the semantics of modal-free formulas unchanged.

Therefore propositional SAT reduces identically to \(\operatorname{SAT}(L_\Lambda)\). Hence
\[
\operatorname{SAT}(L_\Lambda)
\]
is NP-hard.

Likewise propositional TAUT reduces identically to \(\operatorname{VAL}(L_\Lambda)\), so
\[
\operatorname{VAL}(L_\Lambda)
\]
is coNP-hard.

### Polynomial witnesses

Let \(\varphi\) be an input formula.

Nishimura's singleton construction for the no-inference systems shows that whenever \(\varphi\) is satisfiable there is a one-point closure model whose propositional valuation and closure generator are determined inside a finite fragment obtained from the subformulas relevant to \(\varphi\).

Let
\[
F(\varphi)
\]
denote such a finite fragment, enlarged if necessary by \(\top\), the immediate constituents of its conjunctions and implications, and the arguments of all boxed formulas occurring in the evaluation of \(\varphi\).

Because every member of \(F(\varphi)\) is assembled from a subformula of \(\varphi\) by only a bounded amount of syntactic bookkeeping from the source's construction, both its cardinality and its total written length are polynomial in
\[
|\varphi|.
\]

A nondeterministic certificate consists of:

1. truth values for the propositional atoms occurring in \(\varphi\); and
2. a subset
\[
G\subseteq F(\varphi)
\]
used as the generator of the singleton closure model.

The certificate therefore has polynomial size.

### Polynomial closure membership

A complication is that the full closure
\[
cl_\Lambda(G)
\]
need not be finite. In particular, if \(\mathsf C\in\Lambda\), repeated conjunction formation can generate arbitrarily nested conjunctions.

For verification of \(\varphi\), however, only membership questions for formulas in a fixed polynomial-size relevant set are needed.

Let
\[
R
\]
be the closure of \(F(\varphi)\) under taking syntactic subformulas, together with \(\top\). Then \(R\) has polynomial size.

We claim that for every
\[
\theta\in R,
\]
whether
\[
\theta\in cl_\Lambda(G)
\]
is determined by the following saturation restricted to \(R\):

- if \(\mathsf N\in\Lambda\), insert \(\top\);
- if \(\mathsf M\in\Lambda\) and \(\alpha\wedge\beta\in R\) is present, insert \(\alpha\) and \(\beta\);
- if \(\mathsf C\in\Lambda\), and \(\alpha,\beta\) are present with \(\alpha\wedge\beta\in R\), insert \(\alpha\wedge\beta\);
- if \(\mathsf K\in\Lambda\), and \(\alpha\) and \(\alpha\to\beta\) are present with \(\alpha\to\beta\in R\), insert \(\beta\).

The forward inclusion is immediate because every restricted step is a legitimate closure step.

For the converse, take a closure derivation of a target
\[
\theta\in R
\]
and remove inessential formulas from it.

A conjunction created by \(\mathsf C\) outside \(R\) cannot be an essential bridge back into \(R\) through \(\mathsf M\): decomposing that conjunction merely recovers conjuncts that were already present before the conjunction was formed. Thus a create-then-decompose detour outside \(R\) may be deleted.

The only other way a formula can influence a later formula is through \(\mathsf K\). But \(\mathsf M\) and \(\mathsf C\) create no implications. Hence every implication used in a \(\mathsf K\)-step traces back to the original finite generator or its relevant source fragment. If its consequent is needed in the evaluation of \(\varphi\), that implication, its antecedent, and its consequent all belong to \(R\) by construction.

After deleting the irrelevant conjunction detours, every essential step lies in \(R\). This proves the relevance claim.

A naive implementation repeatedly scans all conjunction and implication nodes in \(R\). Each formula of \(R\) is inserted at most once, so even this implementation runs in polynomial time, for example in
\[
O(|R|^2)
\]
set-membership operations after indexing the formulas.

Thus every closure-membership query needed to interpret a box in the singleton model is polynomial-time decidable.

### NP membership

Given the guessed valuation and generator \(G\), first compute the restricted saturation above. Then evaluate \(\varphi\) bottom-up in the singleton closure model.

This verification is polynomial in
\[
|\varphi|.
\]

The source's singleton completeness construction guarantees that if \(\varphi\) is satisfiable, a certificate of this form exists. Conversely, every accepted certificate explicitly describes a legitimate closure model satisfying \(\varphi\).

Therefore
\[
\operatorname{SAT}(L_\Lambda)\in\mathrm{NP}.
\]

Together with propositional NP-hardness,
\[
\operatorname{SAT}(L_\Lambda)
\]
is NP-complete.

### coNP completeness of validity

A formula \(\varphi\) is invalid exactly when
\[
\neg\varphi
\]
is satisfiable.

Hence invalidity is in NP, so validity is in coNP. The propositional lower bound gives coNP-hardness. Therefore
\[
\operatorname{VAL}(L_\Lambda)
\]
is coNP-complete.

Finally, the source's strong completeness theorem identifies semantic validity with derivability in \(L_\Lambda\), so theoremhood is coNP-complete as well.

## Verification

The proof uses the following source statements directly.

Definition 3.7 gives the closure operations corresponding to \(\mathsf M,\mathsf C,\mathsf N,\mathsf K\).

Definition 3.8 begins the canonical construction for the systems without modal inference rules. The countermodel used there has one world and a finite generator drawn from the source's finite syntactic fragment.

Lemma 3.10 supplies the truth lemma for this canonical model.

Theorem 3.12 proves strong completeness.

Theorem 3.13 proves the finite model property.

Corollary 3.14 proves primitive-recursive decidability by enumerating finitely many one-point candidates and computing the needed closure memberships in a finite relevant fragment.

The source's prospects section explicitly lists computational complexity of validity and satisfiability as a remaining problem.

The only new technical ingredient needed for the exact bound is the polynomial relevance lemma above. It avoids the false claim that the unrestricted \(\mathsf C\)-closure is finite.

## Relationship to prior work

There is substantial complexity literature for **congruential** non-normal modal logics, but it does not subsume the present theorem.

Dalmonte and Mazzullo study the classical non-normal modal cube built over the minimal logic \(E\). Their systems include the rule of replacement of equivalents. They report coNP-completeness for several members of that congruential cube and the familiar PSPACE jump when the agglomeration axiom \(\mathsf C\) is combined with the standard congruential setting.

Nishimura's no-inference systems considered here are different: they omit both modal inference mechanisms \(\mathsf E\) and \(\mathsf G\). In particular, \(L_{\{\mathsf C\}}\) and its no-inference extensions are covered by the coNP theorem above despite containing \(\mathsf C\). Thus the result identifies the absence of modal inference, rather than the bare presence of the \(\mathsf C\) axiom, as the decisive reason the closure-model decision problem remains at propositional complexity in this family.

Pascucci and Sedlár provide semantics for non-congruential modal logics. Their accessible abstract and bibliographic record do not state an exact decision-complexity classification of the present sixteen closure systems. The full text was not available through the noninteractive lawful-access routes used for this comparison, so this remains a residual literature risk rather than evidence of coverage.

Targeted searches under the terms non-congruential, no-inference, least modal logic, closure semantics, and the exact NP/coNP formulations did not locate a prior statement equivalent to the theorem above.

## Limitations

The theorem applies only when
\[
\Lambda\subseteq\{\mathsf M,\mathsf C,\mathsf N,\mathsf K\}.
\]
No complexity classification is claimed here for systems containing the modal inference rules \(\mathsf E\) or \(\mathsf G\).

The proof shows polynomial verification for closure-membership questions relevant to a fixed input formula. It does not claim that the unrestricted closure \(cl_\Lambda(G)\) is finite or that every arbitrary closure-membership problem has the same complexity under unrelated encodings.

The result sharpens the decision bound for the source's new semantics but does not replace the different complexity classifications known for congruential non-normal modal logics.

## References

[1] Yuki Nishimura, “Closure Semantics for Weak Modal Logics: Completeness and Representations,” arXiv:2610.01433v1, first posted 1 October 2026.

[2] Tiziano Dalmonte and Andrea Mazzullo, “CoNP Complexity for Combinations of Non-normal Modal Logics,” *Automated Reasoning with Analytic Tableaux and Related Methods (TABLEAUX 2023)*, Lecture Notes in Computer Science 14278, 2023, DOI 10.1007/978-3-031-43513-3_17.

[3] Matteo Pascucci and Igor Sedlár, “Hyperintensional models for non-congruential modal logics,” *Logic Journal of the IGPL* 33(5), 2025, DOI 10.1093/jigpal/jzad018.
