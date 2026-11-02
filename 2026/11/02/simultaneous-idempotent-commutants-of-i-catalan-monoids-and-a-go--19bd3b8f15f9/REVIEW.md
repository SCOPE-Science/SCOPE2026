# Review of the simultaneous-idempotent-commutant theorem

## Correctness

**PASS.** Every idempotent is a partial identity by injectivity. The strict-arrow directed graph is a forest of paths, so membership subsets constant on its components give the exact count \(2^{n-r(f)}\). A fixed point separates the ordered partial map into independent strict maps on the gaps; shifting images by one identifies strict maps with smaller \(i\)-Catalan maps. Reflection counting and Lagrange inversion derive the Narayana polynomial. The geometric sequence of gap choices gives \(F=S/(1-zS)\). The positive pole and square-root singularities are explicitly located, and their leading coefficients are obtained by differentiation and local expansion; the critical case has inverse-square-root order. Independent direct-composition enumeration agrees for all stated finite test cases. The proof, not the tests, establishes the result for arbitrary \(n\) and fixed \(k\).

## Originality

**PASS relative to inspected sources and searches, with residual risk.** Sapir and Volkov (arXiv:2211.12952, 2022) define the \(i\)-Catalan family and prove a finite-basis theorem; their cardinality bijection and identity-theoretic analysis do not give centralizing-idempotent moments. The \(k=1\) numerical sequence and asymptotic are **already known** from OEIS A225887 and are excluded from the independent novelty claim. Oste and Van der Jeugt (2015) establish general weighted Motzkin/Schröder path machinery, and their combinatorial path formalism is not claimed as new. Al-Kharousi, Umar, and Zubairu (arXiv:2501.00285v1, 2024) study the **same** injective partial Catalan monoid under order-reversal and its Green, rank, and maximal-subsemigroup structure, but the inspected entire HTML paper does not establish the centralizer-moment theorem. Stein (2018) studies representation theory of a different, noninjective partial Catalan monoid. Searches for exact \(i\)-Catalan idempotent-relative centralizers and simultaneous moments did not return a published equivalent. The claimed new content is the complete \(i\)-Catalan idempotent-centralizer spectrum, counts with \(k\ge2\) simultaneous commuting idempotents, and the associated dominant-singularity transition. A prior specialized colored-path formula or monoid centralizer theorem not identified by these searches remains a meaningful risk.

## Mathematical value

**PASS.** Because idempotents of this monoid form a natural Boolean semilattice and \(IC_4\) is a prominent finite-basis example, common centralizers of collections of idempotents are intrinsic structural invariants. The theorem determines their distribution for *every* size and every fixed number of independent commuting idempotents. The switch between the \(n^{-3/2}\) branch mechanism for one idempotent and a simple pole with an \(n^{3/2}\) probability prefactor for two or more is a mathematically motivated large-size phenomenon, with sharp golden-ratio threshold and exact constants; it is not a claim that Narayana numbers or the old one-idempotent sequence themselves are new.

## Limitations

The theorem does not count all elements of each full centralizer, and the asymptotic analysis fixes \(k\). The known numerical one-idempotent specialization is explicitly separated from the claim's new contribution. Publication-priority certification and independent mathematical validation are outside the supplied verification.

Self-review: passed. Independent audit: not yet performed.
