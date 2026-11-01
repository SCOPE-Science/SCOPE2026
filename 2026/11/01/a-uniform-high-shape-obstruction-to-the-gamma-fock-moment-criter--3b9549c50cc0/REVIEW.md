# Scientific review

## Correctness — PASS
The claim is precisely the impossibility of the Gamma-shape moment inequalities for every real \(\kappa\ge144\). The second moment bound forces \(0\le\mathbb E(X-\kappa)\le1\); the two families of rising-factorial moments sandwich the complete exponential moment generating function. For \(\lambda=3/(4\sqrt\kappa)\), a one-sided exponential interpolation bound and Cauchy–Schwarz conflict with the Gamma exponential lower bound. Both sides reduce to exact strict rational inequalities, independently checked with `verify_bounds.py`. All sums are justified by monotone convergence and finite upper exponential moments; no finite enumeration stands in for an infinite proof.

## Originality — PASS under checked evidence
The most relevant primary paper, Wikström (arXiv:2609.39622, first public version 2026-09-30), explicitly gives isolated nonexistence certificates, starting at shape \(50\), and says it has no proof of nonexistence for all shapes above a threshold. The present real half-line \(\kappa\ge144\) follows from a different global moment-generating-function contradiction and is not an implication of an isolated certificate. Its Theorem 1.2 states a sufficient criterion, not a necessity theorem. The relevant earlier Bergman moment work and weighted Fock upper-radius work do not assert the present uniform obstruction in the material checked. Indexed mathematical-record searches returned related Korenblum extremizer-rigidity and Gamma-function results, but no statement covering the moment infeasibility ray.

## Mathematical value — PASS
The natural parameter is the shape of a Gamma radial weight in the weighted Fock Korenblum question. The source identifies infeasibility for all large real shapes as unresolved even though individual large shapes admit certificates. A global analytic cutoff replaces infinitely many isolated feasibility tests, clarifies a genuine limitation of the moment-duality method, and needs no numerical linear programming. The threshold is intentionally not represented as sharp.

## Closest literature and limitations
- F. Wikström, *The sharp radius in Korenblum's maximum principle for the Fock space*, arXiv:2609.39622, Theorem 1.2, Corollary 1.4, Proposition 7.3, and Section 7.1 (relevant full text inspected).
- F. Wikström, *Moment duality and an improved lower bound for Korenblum's constant*, arXiv:2607.17748 (abstract inspected; distinct Bergman-domain setting).
- J. Wee and L. H. Khoi, *Korenblum constants for various weighted Fock spaces*, Complex Variables and Elliptic Equations 68 (2023), 1385–1406 (publisher abstract inspected).

The claim excludes the indicated moment measures only, not any other proof of Fock norm domination. The interval below shape \(144\) is not classified; no optimal transition is asserted. Historical priority and independent mathematical review remain outstanding.

Self-review: passed. Independent audit: not yet performed.
