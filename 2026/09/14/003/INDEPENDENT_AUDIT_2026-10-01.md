# Independent mathematical audit — 2026-10-01

## Final claim

For the Wagner graph \(M_8\), the edge ideal has Waldschmidt constant \(8/5\), the stated first five symbolic initial degrees, and \(I^{(4)}\subset I^3\); the record claims only a lower bound \(\rho(I)\ge 5/4\) for resurgence.

## Correctness — PASS

Independent enumeration finds exactly eight maximal independent sets, hence eight minimal vertex covers, all of size 5, with every vertex in five covers. Summing the cover inequalities gives \(5\deg(a)\ge 8m\), while diagonal exponent vectors attain ratio \(8/5\). Fresh composition search gives symbolic initial degrees \(2,4,5,7,8\) for \(m=1,\ldots,5\). For \(m=4\), exhaustive enumeration of the box \(\{0,\ldots,4\}^8\) gives 358134 symbolic candidates; there are 316 distinct three-edge load vectors, and every candidate dominates at least one load vector. Thus \(I^{(4)}\subset I^3\). The lower-bound sequence for resurgence follows by degree from the diagonal monomials.

## Originality — PASS

Bocci et al. give the general linear-program description of Waldschmidt constants for squarefree monomial ideals, so the \(8/5\) value alone is a routine specialization of known machinery. However, the final claim also contains the exact first-five initial-degree data and the exhaustive containment \(I^{(4)}\subset I^3\). Nguyen–Pham–Vu compute regularities for all cubic circulant edge ideals, not these containment data, and Gu–Hà–O'Rourke–Skelton's explicit symbolic-power formulas are for unicyclic graphs, whereas the Wagner graph is not unicyclic. No exact prior containment/table row was located.

### Equivalent formulations

The cover-inequality formulation and monomial-load formulation are equivalent to the symbolic and ordinary membership statements, respectively; the exhaustive comparison is graph-specific.

### Broader coverage

Neither broader result implies the audited containment for the non-unicyclic Wagner graph.

### Exact database or table

The exact object is indexed in the current published corpus only through the record being audited, so novelty remains best-knowledge.

### Claim versus prior implication

The LP framework mechanically explains how to obtain the Waldschmidt value after solving the graph-specific LP, but does not imply the fourth-symbolic containment or exact initial-degree table; those surviving parts keep the bundled final claim original.

## Scientific value — PASS

The Wagner graph is a canonical 8-vertex cubic circulant/Möbius ladder, and symbolic-versus-ordinary containment is a standard invariant question for edge ideals. The exact containment at a small nontrivial symbolic level, together with sharp initial-degree data, is a motivated benchmark rather than an arbitrary graph computation.

## Sources inspected

- **Cristiano Bocci et al., The Waldschmidt constant for squarefree monomial ideals** — https://arxiv.org/abs/1508.00477. GENERAL_FRAMEWORK_PARTIAL_COVERAGE: It covers the general method for the Waldschmidt constant but not the Wagner-specific symbolic containment or initial-degree table.
- **Nguyen Thu Hang, My Hanh Pham, Thanh Vu, Regularity of powers and symbolic powers of edge ideals of cubic circulant graphs** — https://arxiv.org/abs/2409.20161. SAME_GRAPH_CLASS_DIFFERENT_INVARIANT: The paper computes regularity, not the audited containment \(I^{(4)}\subset I^3\).
- **Yan Gu, Huy Tài Hà, Jonathan L. O'Rourke, Joseph W. Skelton, Symbolic powers of edge ideals of graphs** — https://doi.org/10.1080/00927872.2020.1745221. INAPPLICABLE_GRAPH_CLASS: The Wagner graph is cubic with multiple cycles and is not unicyclic.

## Checked evidence

- Assigned RESULT.md and all four Python artifacts from the exact Git tree.
- Fresh independent cover enumeration, first-five symbolic initial-degree search, and full 358134-by-316 containment check.
- Resultary published-record search and primary literature on squarefree Waldschmidt constants, cubic circulants, and graph symbolic powers.

## Residual risks

- The archived scripts use historical output/artifacts paths and one script expects a generated NumPy file not committed in the assigned tree; the audit therefore did not rely on that saved workflow.
- No claim is made that the conjectured equality for resurgence is proved.

## Disposition

**passed**
