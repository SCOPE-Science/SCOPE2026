# Scientific review of the genus-four branch-orbit census

## Correctness — PASS

For every odd prime power \(q\), the exact smooth domain is \(v(u^2-4v)(1+u+v)\ne0\). The displayed branch polynomial factors as \((x^2+1)P_{t_1}(x)P_{t_2}(x)\), where \(P_t(x)=t(x^2+1)^2-4x^2\) and \(t_1,t_2\) are distinct roots of \(t^2+ut+v\) not equal to \(0\) or \(1\). The four radical roots of each factor and the norm identities completely determine Frobenius cycles, without a geometric genericity assumption. The two quadratic-character counts prove the four exact frequency formulas, and the even-branch-subset computation gives rational Jacobian \(2\)-torsion orders. The standalone checker tested polynomial separability, genuine Frobenius root counts for extension degrees \(1,2,4\), and all parameters over eight prime fields; checks over two nonprime fields independently verified rational branch counts and the frequency formulas. The proof is universal; the finite checks are not used to infer infinite validity.

## Originality — PASS, with priority limitations

Bruin and Kulkarni's September 5, 2023 preprint, Section 7.1, Example 7.3, and its September 12, 2025 journal presentation give the two-parameter genus-four model and the Jacobian-square isogeny. These are explicitly attributed. The inspected Example and related classification tables concern geometric constructions and permutations of six genus-two branch points, not Frobenius on the ten genus-four branch points. Neither inspected version states the four-type census, exact parameter frequencies, or rational two-torsion orders. Searches targeting the exact polynomial, the cover \(2x/(x^2+1)\), and these arithmetic invariants found no identical result; a search failure does not prove priority. Overlap comparisons with accessible earlier findings found related genus-two Weierstrass studies and separate genus-four isogeny and Hasse-stratum results, but none imply this all-\(q\), all-parameter ten-point classification. An equivalent calculation in an unindexed general finite-field factorization source remains the main residual risk.

## Mathematical value — PASS

The source identifies an exceptional two-dimensional family whose genus-four Jacobians are isogenous to squares of genus-two Jacobians. Its ten geometric Weierstrass points naturally encode the full rational \(2\)-division branch data. The result gives **the complete Frobenius type distribution**, not a selected example, and proves a uniform degree-four splitting cutoff with an exact count \(3(q^2-1)/8\) of pairs requiring degree four. It yields exact rational Weierstrass and Jacobian \(2\)-torsion distributions across the entire coefficient surface, providing concrete arithmetic information not determined by the geometric isogeny statement alone. The counting is motivated by the unexpected large-dimensional family; no unproved downstream conjecture is invoked to justify value.

## Closest literature and limitations

The closest source is Bruin–Kulkarni, *On (2,2)-decomposable genus 4 Jacobians*, arXiv:2309.01959v1, Section 7.1, Example 7.3, and the 2025 Canadian Journal of Mathematics online version of the same paper. Prior mathematics includes finite-field quadratic character identities and the hyperelliptic even-subset model for Jacobian two-torsion. The accepted statement counts literal smooth coefficient pairs, not isomorphism classes, and determines branch-point arithmetic rather than full curve zeta functions. A prior equivalent enumeration may exist in unindexed literature. No independent external mathematical audit has been performed.

Self-review: passed. Independent audit: not yet performed.
