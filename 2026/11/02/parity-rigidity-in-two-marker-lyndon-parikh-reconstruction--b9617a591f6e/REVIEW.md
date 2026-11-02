# Scientific review: parity rigidity in two-marker Lyndon–Parikh reconstruction

## Correctness — PASS

The observation is precisely defined, including the alphabet ordering and its two components. The unique three-gap parameterization of a word with two ones gives the ordinary \(01\) count \(2a+b\). The lexicographically minimal rotation is determined by the longer of the two *circular* zero gaps, giving the second statistic \(N+\max\{b,N-b\}\). These two independently reconstructed identities restrict every inverse fiber to at most two words; parity eliminates the second when \(N\) is odd. When \(N=2h\), the proof gives every doubleton explicitly and counts it exactly once by its smaller circular gap and left exterior run. The boundary \(N=0\) is covered. The self-contained verifier enumerated all 39,711 candidate words through \(N=60\), using literal rotations independently of the structural formula. Finite checks are corroborative, not a proof of all \(N\).

## Originality — PASS, with residual access risk

The natural closest source is Dick et al., LATA 2020, DOI `10.1007/978-3-030-40608-0_28`. Its introduction, definitions, propositions on Lyndon-based ambiguity reduction, and main Theorem 2 were examined in the accessible indexed HTML text, though mathematical images were not all available. That theorem characterizes certain original Parikh classes whose ambiguity is *not reduced* by the Lyndon transformation; the current claim instead completely classifies *every joint-observation fiber* in the fixed-two-marker layer and enumerates singleton/doubleton fibers. Neither implication direction from the published qualitative criterion alone yields the explicit joint-fiber census. The 2021 journal version (DOI `10.1016/j.tcs.2021.01.025`) is a material residual risk because the full text could not be obtained; its accessible abstract concerns the same method but does not state these counts. The 2022 toolkit (DOI `10.1007/978-3-031-07469-1_9`) concerns implementations of matrices and their variants. Publicly indexed related results on ordinary Parikh-matrix singleton counts and adjacent-pair reconstruction measure different observations and do not dominate this exact claim. No exact equivalent was found by checked aliases, but absence from search results is not a uniqueness certificate.

## Mathematical value — PASS

This solves a motivated reconstruction question arising directly from the published proposal to augment Parikh matrices with canonical conjugate information. It gives an explicit all-length ambiguity partition, a strong parity threshold (full injectivity at odd zero-count), and an exact zero-error message capacity for a natural sparse two-marker input family. Even zero-count inputs retain only one- or two-source ambiguity; the uniquely recoverable fraction tends to one-half along even zero counts while it is identically one at every odd zero count. The result is more than a small finite table or a restatement of ordinary Parikh-matrix equivalence.

## Scientific limitations

The proof does not address arbitrary marker weights, alphabet extensions, noisy decoding or full class distributions for arbitrary words. Full-text access to the longer 2021 journal article and equation images embedded in the indexed conference article was incomplete. A differently formulated prior result could therefore remain unidentified; independent specialist validation has not occurred.

Self-review: passed. Independent audit: not yet performed.
