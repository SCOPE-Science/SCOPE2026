# Scientific review

## Correctness — PASS
The object and width-one normalization are fixed explicitly. Disk erosion commutes with finite intersection, and the farthest disk-center sector gives an exact radial equation and area integral. The convex Cheeger identity \(|K_{-t}|=\pi t^2\) gives a unique positive root. Uniform Taylor expansion of the radial integral has coefficients \(-a-5/288\) and \(7a/216-b-107/69120\), requiring the stated rational values of \(a,b\). At the disk limit, the implicit-function derivative is \(-1\), so the even analytic expansion and controlled \(O(n^{-6})\) error are justified. The executable checker confirms the exact coefficient identities and finite-\(n\) numerical cases, but the analytic argument—not the finite tests—proves the theorem.

## Originality — PASS, with explicit risk
Compared by mathematical implication to the accessible primary texts: Falco–Myroshnychenko classifies regular Reuleaux polygons as area minimizers under symmetry, without computing the Cheeger convergence coefficients. Henrot–Lucardesi and Bogosel prove broader Cheeger/inner-erosion facts and allow implicit evaluation, but their inspected materials do not state the two sharp Cheeger expansion coefficients or the normalized limit. Pan–Yao–Zhang proves the finite-complexity Cheeger minimizer classification, so that classification is *prior work*; only its quantitative sharp-rate corollary is considered here. Its complete text could not be inspected, so pre-existing coefficients there remain a concrete residual priority risk, not a verified absence. Published-search results did not identify the exact expansion, but search failure is not a priority certificate.

## Value — PASS
Pan–Yao–Zhang's finite-complexity minimization makes the sequence \(h_n\) a sharp extremal geometric invariant, not an arbitrary sample of shapes. The theorem quantifies how the sharp extremal Cheeger value approaches the disk at the exact quadratic order and specifies the next nonzero correction. The area-normalized ratio distinguishes this Cheeger deficit from the area deficit of the same canonical shapes. This supplies a reproducible benchmark for quantitative constant-width shape optimization, beyond numerical tabulation or rephrasing the existing minimizer theorem.

## Scope and sources
The claim concerns only width-one *regular* Reuleaux polygons with odd side count and a large-\(n\) expansion. Original published Cheeger characterization and its geometric erosion are used as inputs. The most relevant incomplete comparison is the 2026 paper on minimizing Cheeger constants of Reuleaux polygons, for which only an abstract and bibliographic material were accessible. There is no independent audit.

Self-review: passed. Independent audit: not yet performed.
