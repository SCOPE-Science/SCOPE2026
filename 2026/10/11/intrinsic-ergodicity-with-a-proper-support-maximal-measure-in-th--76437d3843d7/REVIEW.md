# Review

## Correctness
PASS. The source's explicit lift bound gives a uniform estimate in terms of the terminal zero-run length. Under any ergodic measure with positive marker frequency that terminal run is sublinear by the ergodic theorem, so conditional entropy over the factor is at most \(\alpha\log\lambda\) beyond the factor entropy. Since \(h(\mathsf X(S))=\log\eta\) and \(\log\eta+\alpha\log\lambda<\log\lambda\), marker-positive invariant measures cannot be maximal. Ergodic decomposition extends the conclusion to arbitrary maximal measures. The source's all-zero fiber identity makes the marker-free subsystem exactly \(Y\), and variable specification gives \(Y\) a unique fully supported maximal measure. Thus the maximal-measure sets of \(X\) and \(Y\) coincide and are singletons.

## Originality
PASS with a stated bibliographic risk. The motivating paper proves the construction, the fiber estimates, and \(h(Y)=h(X)\), but it does not state maximal-measure localization or intrinsic ergodicity of the ambient one-sided-balanced example. General synchronized-shift theory controls fully supported maximal measures and therefore does not imply this improper-support uniqueness statement. Targeted searches for marker-supported entropy loss, one-sided balance plus intrinsic ergodicity, and proper full-entropy support found no implication-equivalent theorem. A thesis cited by the source as an antecedent of Theorem 3.7 was not directly inspectable in the bounded search, so an equivalent observation there remains a residual risk.

## Value
PASS. The result separates three properties that the paper's bi-balanced theory links together: intrinsic ergodicity, entropy minimality, and full support of the maximal measure. The fresh one-sided-balanced counterexamples retain uniqueness of the maximal measure while losing both entropy minimality and full support, and the proof identifies the exact mechanism: positive marker frequency carries a strict entropy penalty. This is a structural classification of the paper's full counterexample family for every prescribed positive entropy, not a numerical slice or a restatement of the equal-entropy subsystem.

## Closest literature and limitations
The closest source is Hong--Kim, arXiv:2609.33476v1, especially Theorem 3.7 and its preimage estimates. Thomsen's synchronized-system theory concerns fully supported maximal measures and does not settle the present improper-support uniqueness. The result is limited to the source's marker-coded construction and does not claim a general theorem for all one-sided balanced shifts.

Same-model review: passed. Independent audit: not yet performed.
