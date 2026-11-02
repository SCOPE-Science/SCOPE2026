# Scientific review — Eight three-round theories of Cartesian products of finite cycles

## Correctness — PASS

The stated language, graph domain and three-round Ehrenfeucht–Fraïssé semantics are precise. The proof first establishes an exact two-point-extension criterion for vertex-transitive graphs, including repeated selections. It then proves that for every product with at least two cycle factors the third-vertex patterns \(00,01,10\) always occur, and identifies exactly when \(11\) occurs from triangular edges or pairs at distance two. The exceptional product \(C_3\square C_3\) is checked explicitly. The one-factor table treats each small cycle separately and proves the uniform tail from length seven. All eight spectra are pairwise distinct, giving both directions of the full classification and the sharp maximum smallest representative size \(27\). Two standalone, exact finite checkers produce corroborating output. Their finite coverage is not substituted for the infinite argument.

## Originality — PASS, qualified

Brown and Hoshino's *The Ehrenfeucht–Fraïssé Game for Paths and Cycles* (2007), Theorem 4.9, gives the single-cycle three-round threshold, not multi-factor equivalence. Verbitsky's arXiv:math/0401361v1 develops general graph-definability bounds, not these sharp eight classes. Earlier Hamming-graph and two-factor torus classifications at rank four and a general three-round pair-spectrum method were compared by **statement and implication**; none of those claims contains the all-dimension, cross-dimensional eight-class theorem. The result should therefore be attributed as a new application/classification, not a new game-theoretic invariant. Accessible literature and research-database searches did not locate direct stronger coverage. This is a best-knowledge assessment, not a claim of exhaustive historical priority: the older Brown–Woodrow technical report and the wider product-logic literature have not been comprehensively checked.

## Mathematical value — PASS

The problem asks for a complete logical classification of a standard graph-product family under unbounded dimension and unbounded factor lengths. The exact eight-class answer is a natural full classification rather than an arbitrary parameter slice. Its cross-dimensional collapse is substantial: a degree-two seven-cycle and products of arbitrarily high degree are indistinguishable through three rounds, while pure triangular and mixed triangular factors create genuinely different classes. The sharp family representative bound \(27\), explicit spectra, and bounded-depth nondefinability consequences make this exact fact reusable in logic of graph products. The proof uses a short general extension lemma; the value lies in its complete nontrivial parameter consequences, not in claiming a wholly new EF technique.

## Closest literature and limitations

Jason Brown and Richard Hoshino, Ars Combinatoria 83 (2007), pages 193–212, https://combinatorialpress.com/article/ars/Volume%20083/volume-83-paper-13.pdf, covers single cycles; Theorem 4.9 and the concluding limitations were materially examined. Oleg Verbitsky, arXiv:math/0401361v1, https://arxiv.org/pdf/math/0401361, covers graph-definability estimates and broad EF methods; its introduction and related-work discussion were materially examined. Finite verification examines 76 pair spectra and 21 independently evaluated complete three-round logical types; it cannot establish the infinite theorem. The classification is not claimed for richer signatures, counting quantifiers, or higher ranks. Full historical-priority verification and third-party validation remain outstanding.

Self-review: passed. Independent audit: not yet performed.
