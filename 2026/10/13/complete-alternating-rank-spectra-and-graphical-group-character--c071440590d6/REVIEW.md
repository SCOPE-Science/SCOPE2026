# Scientific review: complete tripartite graphical-group character-degree spectra

## Correctness — PASS

The claim is the exact alternating-rank count \(N_q(a,b,c;t)\) for every prime power \(q\) and all \(a,b,c\ge2\), together with its graphical-group character-degree interpretation for odd \(q\). Lemma 1 in RESULT.md reconstructs the pullback-form distribution by partitioning each linear map according to image dimension and radical dimension; the isotropic-plane and nondegenerate symplectic-complement counts follow from standard flag counting and the orders of finite symplectic groups. Lemma 2 establishes, by explicit congruence elimination, that a fixed first cross-block of rank \(r\) contributes a hyperbolic space of dimension \(2r\), then a second hyperbolic space of dimension \(2s\), and leaves the form induced on \(\ker U\), of dimension \(c-s\). The free part of the map on the complement of this kernel accounts for exactly \(q^{2rs}\), not a heuristic independence assumption. Combining both lemmas counts every choice of the \(ab+ac+bc\) edge variables once. The central-character argument yields the group-character multiplicities.

As independent finite evidence, the stdlib verifier in `artifacts/verify.py` enumerates all matrices in twelve small cases over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\), and checks eight directly enumerated pullback histograms plus 125 pullback count normalizations. The last line is `EXHAUSTIVE_CASES 12 DIRECT_PULLBACK_CASES 8 PULLBACK_CHECKS 125 VERIFY_OK`. The finite checks corroborate but do not establish the universal proof. Both the matrix and group formulas are explicitly restricted to their stated domains.

## Originality — PASS, with residual risks

Rossmann's *Enumerating conjugacy classes of graphical groups over finite fields* (2022), §1.6, asks for degree-by-degree character enumeration and identifies its alternating-rank interpretation; it does not give the complete \(K_{a,b,c}\) distribution. Rossmann and Voll's *Ask zeta functions of joins of graphs* (arXiv:2505.10263, 2025), inspected at Theorem A and its proof in §11, gives formulas for average kernel-size generating functions under graph joins. Its demonstrated output is one average per finite quotient level, not the entire fixed-field rank histogram with separate counts at every rank. This is substantial closely related work, not automatically a complete rank-spectrum theorem.

The separate *Coning recurrence for character degrees of graphical groups* note, inspected in full, supplies a complete distribution transformation for a universal-vertex extension and handles \(K_{1,a,b}\) and its iterated cones. The new domain deliberately has \(a,b,c\ge2\), so no vertex is universal and those results do not already cover it. Other nearby explicit rank-spectrum notes address trees and cycles, not general tripartite graphs. No equivalently strong all-parameter statement or numerical table was found by searches for tripartite alternating ranks, graphical-group character degrees, symplectic pullback distributions, and complete multipartite forms.

**Residual risk:** a reformulation through earlier finite symplectic-form enumeration or through deeper consequences of ask-zeta machinery might exist, and finite search does not establish absolute priority. The result does not claim the character-rank conversion or rectangular rank count as new.

## Value — PASS

Rossmann's explicitly posed degree-multiplicity problem motivates the full rank-by-rank invariant. This theorem computes it for an infinite, genuinely non-cone graph family in every field size, including a nontrivial symplectic residual arising from a positive-rank first cross-block. It gives exact character-degree multiplicities, not only the group order, total character number, or an average kernel size. The smallest symmetric member \(K_{2,2,2}\) already has four nontrivial strata with concrete reproducible counts. The method exposes a reusable structural lemma for arbitrary symplectic pullback rank distributions. The significance does not depend on unproved downstream applications or the number of finite examples.

## Limitations and literature

The displayed sum need not be computationally optimal, and the theorem does not cover arbitrary joins. The group consequence is asserted for odd characteristic. Literature comparisons are to exact statements and their known implications; inaccessible or unidentified equivalent historical work remains a residual risk. No external independent mathematical review has been performed.

References: Rossmann (2022), DOI 10.1112/blms.12665; Rossmann–Voll (2025), arXiv:2505.10263; *Coning recurrence for character degrees of graphical groups* (2026), publicly accessible at https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-coning-recurrence-for-character-degrees-of-graphical-groups--732adc755a75; Rossmann's small-graph ask-zeta tables at https://torossmann.github.io/cico/.

Self-review: passed. Independent audit: not yet performed.
