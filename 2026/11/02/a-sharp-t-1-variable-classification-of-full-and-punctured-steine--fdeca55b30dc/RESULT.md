# A sharp \((t+1)\)-variable classification of full and punctured Steiner systems

## Finding

Fix an integer \(t\ge 2\). A Steiner system \(S(t,t+1,v)\) is a finite set \(V\) of \(v\) points with a family of \((t+1)\)-element blocks, such that every \(t\)-element point set belongs to exactly one block. Regard it as a relational structure with equality and a single symmetric, irreflexive \((t+1)\)-ary block relation \(B\), where \(B(a_1,\ldots,a_{t+1})\) holds exactly for distinct elements forming a block. A *puncture* is the induced structure obtained by deleting any single point, with no marker naming the deleted point.

**Classification theorem.** Suppose each source system has \(v\ge 2t+2\) points and actually exists. Assign a phase to every full system or single-point puncture:

* \(F\): any full system;
* \(P_0\): a puncture of a system with \(v=2t+2\);
* \(P_+\): a puncture of a system with \(v\ge 2t+3\).

Two members of this union satisfy exactly the same **counting-free first-order sentences using at most \(t+1\) reusable variables, at unrestricted quantifier depth**, if and only if their phases agree. A phase whose source system does not exist for the fixed \(t\) is simply absent; the statement does **not** assert existence for every parameter. Moreover, every two members of the union agree in the fragment using at most \(t\) variables.

The boundary is genuine: Steiner quadruple systems \(S(3,4,8)\) and \(S(3,4,10)\) exist, so all three phases are realized at \(t=3\). In particular, any two punctures of orders at least ten are equivalent in unrestricted \(\mathrm{FO}^4\), regardless of the source quadruple systems, while a puncture of order eight is distinct from them and from every full system.

## Assumptions and scope

The signature contains **only** equality and \(B\). There are no named points, unary sorts, order, counting quantifiers, functional operations or predicates for covered tuples. The block relation is false on repetitions and invariant under coordinate permutations. A puncture has universe \(V\setminus\{p\}\) and exactly the source blocks that avoid \(p\). There are no requirements of resolvability, symmetry, Desarguesian origin, automorphism transitivity, or any other special structure. The same \(t\) and the same relation arity are fixed on both sides of every comparison. An unpunctured source has at least \(2t+2\) points by assumption; the puncture has at least \(2t+1\).

Define \(\mathsf{Cov}(a_1,\ldots,a_t)\) as the \((t+1)\)-variable formula \(\exists z\,B(a_1,\ldots,a_t,z)\). For distinct \(t\)-tuples, \(\mathsf{Cov}\) asserts that the tuple has a block completion *inside the structure*. In a puncture, define the missing \(t\)-set predicate semantically by \(M(A)\iff \neg\mathsf{Cov}(A)\), for \(|A|=t\). The predicate \(M\) is used in the proof as a convenient invariant, not added to the language. All formulas below expand it using \(\mathsf{Cov}\).

## Proof

**1. Derived uniqueness.** Let \(D=S-p\), with \(n=v-1\) surviving points. A distinct surviving \(t\)-set \(A\) is missing exactly if its unique source block was \(A\cup\{p\}\). Consequently, the missing \(t\)-sets form a Steiner system \(S(t-1,t,n)\): every surviving \((t-1)\)-set \(C\) belongs to precisely one missing \(t\)-set \(C\cup\{w\}\). To see this, complete the source \(t\)-set \(C\cup\{p\}\); its block has \(t\) surviving points and yields the required \(w\). Uniqueness follows from the source Steiner property. In particular, two distinct missing \(t\)-sets cannot share \(t-1\) points.

**2. Exact one-point extension patterns.** Hold \(t\) pairwise distinct surviving anchor points \(A\subset D\). For every outside point \(w\), examine both whether \(A\cup\{w\}\) is a surviving block and which of its \((t+1)\) distinct \(t\)-subsets are missing.

If \(M(A)\), no outside \(w\) completes \(A\) to a block, and none of the other \(t\) subsets of \(A\cup\{w\}\) can be missing: any such missing subset would share \(t-1\) elements with the missing \(A\). Thus all \(n-t=v-t-1\) outside points have exactly the same extension pattern (precisely one missing \(t\)-set, namely \(A\)).

If \(\neg M(A)\), then the following \(t+1\) *distinct* outside points are forced. There is one point \(b\) completing \(A\) to a surviving block. For each \(a\in A\), derived uniqueness yields a point \(c_a\notin A\) such that \((A\setminus\{a\})\cup\{c_a\}\) is missing. These \(t\) points \(c_a\) are pairwise different, since otherwise two missing \(t\)-sets would share \(t-1\) points. None equals \(b\), since that would put the same \(t\)-set simultaneously in a source block containing \(p\) and in the surviving block \(A\cup\{b\}\). No \(c_a\) makes a surviving block of \(A\), and each produces *exactly one* missing \(t\)-subset, the subset replacing \(a\); any second would violate derived uniqueness. The point \(b\) produces a surviving block and no missing \(t\)-subset. Every other outside point produces neither a surviving block nor a missing \(t\)-subset. The number of these *free* outside points is exactly

\[
(n-t)-(t+1)=v-2t-2.
\]

This number is zero at \(v=2t+2\) and positive at every \(v\ge 2t+3\). These are **all** extension types; no assumption about the source design beyond the Steiner axiom was used.

If there are fewer than \(t\) distinct retained anchors, one may freely choose a new point or duplicate a retained one according to the desired equality pattern. For exactly \(t-1\) distinct retained anchors, derived uniqueness likewise gives one missing completion and at least one nonmissing completion (the counts are \(1\) and \(v-t-1\)); all other relation instances still have too few distinct arguments to satisfy \(B\). This handles repeated pebbles as well as injective assignments.

**3. Permanent pebble strategies.** In a game with \(t+1\) pebbles, maintain equality and, for all currently selected distinct \(t\)-subsets, the truth of \(M\), together with the source-language atomic block relation on \((t+1)\)-tuples. On moving a pebble, at most \(t\) points remain fixed. With exactly \(t\) distinct anchors, step 2 enumerates every possible atomic and missing-tuple extension pattern. Its support depends only on whether the anchors form a missing set, and on whether \(v-2t-2\) is zero or positive. Corresponding punctures of the same phase therefore allow the responder to select an exactly matching new point at every move. The cases with fewer distinct anchors follow from the final paragraph of step 2. This is a permanent, back-and-forth invariant: there is **no bound on the number of rounds**. It proves unrestricted \(\mathrm{FO}^{t+1}\) equivalence inside either punctured phase.

For full systems, there is no missing \(t\)-set. Given \(t\) distinct anchors, precisely one outside point completes them to a block, and at least one other outside point does not, since \(v\ge 2t+2\). With fewer distinct anchors, any requested equality pattern can be matched. Thus an analogous permanent \((t+1)\)-pebble strategy proves that all full systems are equivalent to one another.

**4. Separating the phases with \(t+1\) variables.** Full and punctured structures differ on the sentence

\[
\exists x_1\cdots\exists x_t\left(\bigwedge_{i<j}x_i\ne x_j\ \land\ \neg\mathsf{Cov}(x_1,\ldots,x_t)\right).
\]

It is false in every full system, and true in every puncture because a block through the removed point produces a missing \(t\)-set.

To separate the two punctured phases, consider \(t\) distinct anchors \(x_1,\ldots,x_t\) with \(\mathsf{Cov}(x_1,\ldots,x_t)\), and ask for a further distinct point \(y\) such that \(B(x_1,\ldots,x_t,y)\) is false but every \(t\)-tuple obtained by replacing one anchor with \(y\) remains covered. Written schematically, the sentence is

\[
\begin{split}
\exists x_1\cdots\exists x_t\exists y\bigg[&\operatorname{Distinct}(x_1,\ldots,x_t,y)
\land \mathsf{Cov}(x_1,\ldots,x_t)\\
&\land\neg B(x_1,\ldots,x_t,y)
\land\bigwedge_{i=1}^{t}\mathsf{Cov}(x_1,\ldots,x_{i-1},y,x_{i+1},\ldots,x_t)\bigg].
\end{split}
\]

This is a genuine \((t+1)\)-variable sentence, not a \((t+2)\)-variable sentence: when expanding the first \(\mathsf{Cov}\), reuse the temporarily bound variable symbol \(y\) as its completion witness; when expanding the replacement tuple indexed by \(i\), reuse the temporarily absent symbol \(x_i\) as its witness. These rebindings occur only within their respective subformulas. Step 2 proves that this sentence has a witness exactly when \(v-2t-2>0\). Nonmissing anchors always exist: otherwise every \((t-1)\)-set would have multiple missing completions, contradicting the derived Steiner property. Hence \(P_0\) and \(P_+\) are distinct whenever both exist.

**5. Why \(t\) variables are insufficient.** Every block-relation atom with at most \(t\) available variable symbols necessarily repeats at least one argument, so it is false. The restricted syntax reduces to pure equality. All structures under consideration have at least \(t+1\) points, and consequently satisfy exactly the same \(\mathrm{FO}^t\) sentences. This establishes the claimed sharp variable-width boundary.

## Verification

Two self-contained Python programs, requiring only the standard library, accompany this result. Run `python local_extension_checker.py` and `python pebble_fixedpoint_checker.py` in the same directory.

The first constructs the Steiner triple systems of orders seven and nine, and Steiner quadruple systems of orders eight, ten and sixteen. Order ten is represented by the 12 affine-line blocks (each augmented by infinity) and the 18 norm circles over \(\mathbb F_3^2\). Orders eight and sixteen are represented by distinct binary vectors \(a,b,c,a+b+c\) (four-element zero-sum blocks). It checks all source \(t\)-subsets for unique completion, all possible single-point deletions, and all extension-pattern counts for distinct \(t\)-anchors. The result covers 50 deletions and 8,757 distinct anchor cases; all exact patterns match the proof.

The second independently computes stable, counting-free, fixed-variable logical types by refining the complete assignment space under one-variable substitutions. It processes 73,683 four-variable assignments across full and punctured quadruple systems and 1,071 three-variable assignments across triple systems. The four-variable refinement stabilizes after five refinement steps and matches the predicted equivalences between full systems of orders eight and ten and between punctures of orders ten and sixteen; it distinguishes the puncture of order eight and the full-versus-punctured cases. The triple-system refinement stabilizes after three refinement steps and matches the predicted punctured equivalence and full-versus-punctured distinction. The recorded outputs `local_extension_output.json` and `pebble_fixedpoint_output.json` are reproducible.

These tests involve **specific finite designs only**. They are corroboration, not a proof of the universal theorem; its arbitrary-parameter and unrestricted-depth content is proved in steps 1–5.

## Relationship to prior work

Grohe and Otto, *Pebble Games and Linear Equations* (arXiv:1204.1990, originally posted 2012-04-09), provide general background on finite-variable pebble equivalence and its counting-free variants. This work does not state the parameter-independent phase classification above.

Baartmans, Blake and Tonchev, *On the extendability of Steiner \(t\)-designs* (1993, DOI 10.1002/jcd.3180010305), study when residual designs extend and report uniqueness of the one-point extension. Recovering a full design up to isomorphism is a different issue from distinguishing two residual designs using a fixed number of logical variables. Only the abstract/catalog material of this particular paper was accessible; no claim about the content of its unavailable full text is made.

Dukes, Feng and Ling, *A finite embedding theorem for partial Steiner 3-designs* (2015, DOI 10.1016/j.ffa.2014.09.011), prove embedding results for partial Steiner designs; their inspected introduction, construction, and main theorem concern embeddings rather than fixed-variable elementary theories. Keevash, *The existence of designs* (arXiv:1401.3665, originally posted 2014-01-15), establishes broad existence results; this explains why the large-order phases are mathematically relevant but does not imply their logical equivalence.

Previously recorded special cases comprise unrestricted three-variable equivalence of full and punctured Steiner **triple** systems, and a bounded-*quantifier-rank* comparison of full Steiner **quadruple** systems. Neither implies a uniform theorem for all \(t\), unrestricted quantifier depth, and the sharp punctured boundary \(v=2t+2\). Conversely, this result incorporates those logically weaker special-case phenomena without presenting them as new standalone discoveries.

## Limitations

This theorem does not decide which admissible \(v\) support designs of a given strength; all existence assertions are conditional except the explicitly constructed orders. It does not characterize variable widths above \(t+1\), counting logic, multiple-point deletions, added names or incidence sorts, or arbitrary Steiner systems with block size larger than \(t+1\). The logical equivalences are established by the mathematical proof, not by finite logical refinement alone. A full historical-priority review of every potentially stronger general theorem, particularly the unavailable 1993 residual-design paper, remains outstanding. No independent mathematical audit is claimed.

## References

1. M. Grohe and M. Otto, *Pebble Games and Linear Equations*, arXiv:1204.1990, original arXiv posting 2012-04-09. https://arxiv.org/abs/1204.1990
2. P. Keevash, *The existence of designs*, arXiv:1401.3665, original arXiv posting 2014-01-15. https://arxiv.org/abs/1401.3665
3. A. H. Baartmans, I. F. Blake and V. D. Tonchev, *On the extendability of Steiner \(t\)-designs*, Journal of Combinatorial Designs 1 (1993), 239–247, DOI 10.1002/jcd.3180010305. https://doi.org/10.1002/jcd.3180010305
4. P. J. Dukes, T. Feng and A. C. H. Ling, *A finite embedding theorem for partial Steiner 3-designs*, Finite Fields and Their Applications 33 (2015), 29–36, DOI 10.1016/j.ffa.2014.09.011. https://doi.org/10.1016/j.ffa.2014.09.011
