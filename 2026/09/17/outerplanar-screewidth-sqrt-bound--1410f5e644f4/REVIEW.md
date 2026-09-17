# Review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

**Verdict: PASS.**

The proof was checked against the definitions of tree-cut decomposition and screewidth in Cenek et al. and against the statement and proof of Rivera Laboy's Lemma 3.10.

The main checks were:

- **Balanced interior edge.** For a maximal outerplanar graph, the weak dual is a subcubic tree on \(n-2\) bounded faces. A centroid and its largest incident branch give a dual edge with both sides of size at most \(3(n-2)/4\) for \(n\ge6\). The corresponding interior graph edge has the same counts for the two components left after deleting its endpoints.
- **Applicability of Lemma 3.10.** If a component behind the balanced edge has edge boundary larger than \(B(n)=(2+\sqrt2)\sqrt n+4\), those boundary edges are all incident with the two separator endpoints. Hence their degree sum exceeds \(2\sqrt{2n}\), so the endpoint of larger degree satisfies the lemma's threshold.
- **Balance survives enlargement of the separator.** Lemma 3.10 returns a set containing both endpoints of the balanced interior edge. Therefore every resulting component is contained in one of the two previously balanced sides and still has at most \(3n/4\) vertices.
- **Recursive assembly.** When a decomposition of a component \(C_i\) is attached to the new central bag, any old link or node adhesion can gain only edges from \(\delta(C_i)\). Thus the increase is at most \(B(n)\). The new attachment link has adhesion exactly \(\delta(C_i)\), and the central node has zero node adhesion because distinct components of \(M-H\) have no edges between them.
- **Attachment-node edge case.** If the selected attachment node in a child decomposition was a leaf before attachment, making it non-leaf introduces no additional internal contribution: any newly tunneling edge involving the parent side belongs to \(\delta(C_i)\), already covered by the additive boundary term.
- **Inductive constant.** With \(n_i\le3n/4\),
  \[
  40\sqrt{n_i}+B(n)
  \le(20\sqrt3+2+\sqrt2)\sqrt n+4
  \le40\sqrt n
  \]
  for \(n\ge6\). The cases \(n\le5\) are covered by the one-bag decomposition.
- **Lower bound.** Rivera Laboy's exact fan scramble formula gives \(\operatorname{sn}(F_{n-1})\ge\lfloor\sqrt{n-1}\rfloor+1\), while Cenek et al. establish \(\operatorname{sn}\le\operatorname{scw}\). Hence the extremal order is genuinely \(\Theta(\sqrt n)\).

No contradiction was found in these checks.

## Originality

**Verdict: PASS, to the best of our knowledge.**

Rivera Laboy's arXiv:2609.03755v2, last revised 15 September 2026, was inspected through the relevant full text. Its Question 5.1 explicitly asks whether screewidth of outerplanar graphs is \(O(\sqrt n)\). The paper supplies the bounded-boundary Lemma 3.10 used here but does not convert it into a recursive tree-cut decomposition or state the resulting screewidth bound.

The foundational screewidth paper arXiv:2209.01459 was inspected for definitions, subgraph monotonicity, and the relation between scramble number and screewidth.

Targeted searches covered the phrases and combinations "screewidth outerplanar", "outerplanar screewidth sqrt", "screewidth of outerplanar graphs", "maximal outerplanar screewidth", and the wording of Question 5.1. No prior theorem answering the question was found. The current SCOPE repository was also searched for "screewidth", the source-paper title, and equivalent outerplanar formulations; no overlapping record was found.

No inaccessible source was identified that specifically claims an outerplanar \(O(\sqrt n)\) screewidth theorem. The principal residual originality risk is extremely recent, unpublished, or not-yet-indexed parallel work, because the motivating question itself was revised only two days before this publication date.

## Value

**Verdict: PASS.**

The theorem directly answers an explicit open question in a current graph-theory preprint. It also determines the correct extremal order of screewidth on outerplanar graphs, from \(O(\sqrt n)\) above and the fan-family \(\Omega(\sqrt n)\) lower bound. The proof exposes a reusable mechanism: balanced vertex separators with \(O(\sqrt n)\) edge boundary can be recursively assembled into bounded-width tree-cut decompositions, even when maximum degree is unbounded.

## Limitations

The theorem does not address the corresponding outerplanar gonality question. The explicit constant \(40\) is not optimized. Correctness depends on Rivera Laboy's Lemma 3.10 as stated in arXiv:2609.03755v2.

Originality is asserted only to the best of our knowledge. Same-model review is not independent validation, formal verification, or peer review.
