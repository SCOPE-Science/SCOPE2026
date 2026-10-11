# Scientific review

## Correctness — PASS
The normalized Fourier character basis and shell probability are fixed explicitly. The proof decomposes each coordinate's mean-zero space into a radial mode and \((q-2)\) transverse modes, derives their conditional Gram blocks from the hypergeometric covariance law, and computes the remaining rank-one block exactly. It therefore proves all eigenvalues, multiplicities, the unique kernel and exact condition number in all claimed ranges. The integer variable \(z=qk-(q-1)n\) gives three exact rational eigenvalue-difference identities, proving that tightness occurs if and only if \(z=1\). The standalone implementation computes actual Fourier matrices for 18 cases and exactly checks the arithmetic condition on a much larger finite grid. Neither finite check is substituted for the algebraic all-parameter proof.

## Originality — PASS
The closest inspected primary sources concern different operators: Diaconis–Griffiths develop multivariate Krawtchouk theory on multinomial compositions; Xu's explicit tight polynomial frames act on composition spaces; Bannai–Bannai–Bannai classify relative designs on binary shells. Their read theorems do not specify the spectrum of restriction of the complete unsymmetrized first Fourier band to a single \(q\)-ary shell, nor its arithmetic quotient-tightness classification. Published mathematical results found under Hamming-shell, Krawtchouk, and sampling aliases concern distinct Fourier supports or frame problems. Related Boolean first-band ball concentration, degree-two shell concentration, and positive-definite Turán-shell problems have different hypotheses and are not covering implications. An older association-scheme or Terwilliger-algebra statement could imply these elementary Gram formulas under different terminology, so this is not a certification of absolute priority.

## Value — PASS
The whole fixed-weight Hamming shell is a canonical symmetric sampling set. The result determines every singular value, the unavoidable sampling obstruction, sharp stable recovery on the quotient, and an infinite arithmetically characterized family with optimal condition number one. The nonbinary transverse sector changes the spectrum and its arithmetic resonances; this is not a parameter re-labeling of binary-shell results. It is a complete natural finite-harmonic classification, not an arbitrary small numerical case or a claim that the elementary covariance lemma alone is novel.

## Closest literature and limitations
The claim is limited to the first Fourier band, one full interior shell, and arbitrary integers \(q\ge3\). Higher bands, weighted shells, and partial samples remain unstudied. A latent general association-scheme spectral formula is the main priority risk. The numerical checker confirms finite instances only.

Same-model review: passed. Independent audit: not yet performed.
