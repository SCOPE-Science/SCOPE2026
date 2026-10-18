# Scientific review

## Correctness — PASS

The claim has three linked identities: an explicit nine-template word union gives the exact labelled zero-deletion count; the same endpoint-colouring equivalence yields the pointwise minimal-deletion formula; and averaging three diagonal left-colour choices plus a balanced directed three-cycle proves the worst-case sharpness. Every quantifier and boundary is covered for all integers \(n\ge0\). The finite intersection table is completely specified by 511 masks and reproduced by `verify.py`; it is an exhaustive algebraic calculation rather than an extrapolation. Genuine lax-split semantics and deletion searches were separately compared on all colourings through four columns, and a fifth-column census was checked. Risk: the general proof has no independent mathematical audit, and the executable examples do not by themselves prove the all-size claim.

## Originality — PASS, with limitations

The primary 2025 disjunction paper studies model-checking complexity, coherence, and a graph condition for the *different* two-atom formula \(\operatorname{dep}(x,y)\vee\operatorname{dep}(y,x)\); its treatment of \(\operatorname{dep}(x,z)\vee\operatorname{dep}(y,z)\) does not give this two-row exact counting formula or a deletion-distance extremal theorem. The 2026 approximate-dependence paper motivates deletion but does not report these fixed-support enumerative identities. A prior all-support three-colour robustness/pseudoforest criterion yields the yes/no existence boundary, not an exact probability or repair guarantee. Searches of published mathematical research records and targeted public literature found no statement implying both quantitative formulas. Risk: a general combinatorial covering-language theorem or an unindexed article could subsume them; failed discovery is not a uniqueness proof.

## Value — PASS

The zero-error probability drops asymptotically like \(3(7/9)^n\), while adversarial data still need only \(\lfloor n/3\rfloor\) tuple removals out of \(2n\). Their contrast is a concrete error-correction phenomenon for an integrity constraint whose general decision complexity is known to be nontrivial. The exact all-\(n\) census is a natural invariant for the smallest complete support family exhibiting a genuine three-colour obstruction; the sharp deletion bound is constructive and works on every labelled instance. The result is not merely a reformulation of a pseudoforest existence classification, though its fixed-support scope limits generality.

## Closest literature and limits

Fröhlich–Kolaitis–Meier, *Disjunctions of Two Dependence Atoms* (2025 preprint, CSL 2026): original semantics, decision/coherence classification, and graph-theoretic analysis. Fröhlich–Häggblom–Hirvonen–Hirvonen, *Approximate Functional Dependencies—Implication Problem Revisited* (2026): approximation motivation and complexity. Related published records on forced three-colouring of bipartite graphs concern a distinct colouring predicate and do not provide the present row/column endpoint-cover disjunction. Relevant earlier finite claims in the same subject were compared for implication. A more general named colouring or covering theorem could remain undiscovered. The proof has not been independently audited.

Self-review: passed. Independent audit: not yet performed.
