# Scientific review: diagonal cubic incidence classification

## Correctness — PASS
The classified domain consists of all smooth diagonal cubic threefolds over \(\mathbf F_7\), modulo projective linear equivalence over that field. Nonzero derivatives establish smoothness; Hessian-factor preservation forces every projective equivalence to be monomial; nonzero cube cosets and five-variable multisets give precisely seven coefficient classes. A complete enumeration of the \(140050\) echelon-represented lines in \(\mathbf P^4(\mathbf F_7)\) supplies every point-degree multiplicity. A second local-polar algorithm computes the multiplicity directly at each rational point and agrees point-for-point. The included Python program was executed from its final scientific file path and all assertions passed. The exhaustive finite computations are proofs of finite cases; there is no extrapolation to other fields.

## Originality — PASS, with bibliographic qualification
The closest source, de Frutos Fernández–Garai–Isham–Murayama–Smith, arXiv:2111.10976, Section 3, provides random distributions for \(\mathbf F_7\)-rational lines on cubic threefolds, not the complete seven-class incidence classification. Debarre–Laface–Roulleau give the general Galkin–Shinder counting identity and Fermat zeta-function calculations, but total line counts cannot determine the numbers of rational lines through individual rational points. Roulleau's geometric study of the complex Fermat Fano surface addresses a different field-dependent question. Targeted searches for diagonal twists, rational line counts, and incidence profiles found no equivalent or stronger explicit incidence classification. An unindexed incidence treatment or a refined calculation from classical Jacobi sums remains possible; novelty is not an independent certification.

## Value — PASS
Rational lines on smooth cubic threefolds over \(\mathbf F_7\) are an established open-field problem. A complete point-on-line profile for every member of its natural diagonal subfamily provides more geometric information than the number of lines: three forms have all rational points covered, whereas four have respectively \(189,135,135,162\) uncovered points. The two projectively inequivalent classes with \(27\) lines have different coverage profiles. This is a natural and fully reproducible finite geometric classification, rather than an arbitrary coefficient slice.

## Scope and risks
The general smooth-cubic problem at \(q=7\) remains unsolved by these calculations. The literature comparison includes full-text inspection of the closest finite-field cubic references, but no exhaustive bibliography can be guaranteed. The Fermat total-line count follows from existing zeta-function work; the claimed addition is the seven-class **local rational incidence spectrum**. No claim of third-party or independent audit is made.

Self-review: passed. Independent audit: not yet performed.
