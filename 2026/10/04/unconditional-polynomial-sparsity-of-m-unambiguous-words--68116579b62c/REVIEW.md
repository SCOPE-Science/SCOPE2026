# Independent mathematical audit

## correctness

PASS

For every consecutive alphabet block of length \(\ell\), the corresponding Parikh-matrix entry is a scattered-subword count between zero and \(\binom n\ell\), and there are exactly \(s-\ell+1\) such nonconstant entries. Treating them independently therefore bounds the total matrix image by the displayed product. Two distinct \(M\)-unambiguous words cannot share a matrix, so singleton fibers inject into that image. The exponent is \(\sum_{\ell=1}^s\ell(s-\ell+1)=\binom{s+2}{3}\), while the total word count is geometric. Fresh independent arithmetic verified the exponent identity for \(2\le s<20\); no finite experiment is used to prove the all-\(n\) bound.

## originality

PASS

Teh's 2020 primary paper was materially inspected in full: Theorem 3.1 proves density zero only under Şerbănuţă's conjecture, and the paragraph immediately afterward explicitly leaves the unconditional conclusion open. Later Hahn–Cheon–Han work solves the structural \(M\)-unambiguity problem for the ternary alphabet, while its current abstract says the problem had remained open for larger alphabets; it does not imply an arbitrary-fixed-alphabet density theorem. Fresh Resultary searches returned no covering result.

## value

PASS

The theorem directly resolves an explicit published open density question without the conjectural hypothesis used in the source and strengthens the answer to polynomial sparsity for every fixed alphabet. It remains useful independently of the much harder word-by-word structural classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
