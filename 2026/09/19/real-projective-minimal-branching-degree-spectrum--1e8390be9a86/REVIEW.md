# Review

## Correctness

**PASS.** The argument uses four explicit results of Faraco--Rungi. Their
Theorem A gives at least one branched real projective realization for every
representation, so the nonnegative integer minimum \(d(\rho)\) exists.
Corollary 4.6 forces the total branching degree of every realization to have
parity \(w_2(\rho)\). Their bubbling construction applies to a possibly
branched structure, increases total degree by exactly two, and Proposition
4.11 preserves holonomy. Starting from a minimal realization therefore
produces every larger degree of the same parity, while minimality and the
parity obstruction exclude every other degree. This proves
\(\mathcal D(\rho)=d(\rho)+2\mathbb Z_{\ge0}\).

For topology, Proposition 2.13 states that the holonomy image of each fixed
signature stratum is open. There are finitely many signatures of each fixed
total degree, so the exact-degree locus \(\mathcal R_m\) is open; finite unions
then give openness of \(\mathcal U_m=\{d\le m\}\), which is exactly upper
semicontinuity in the stated convention.

The dense local-constancy argument does not require a Baire assumption. In
any nonempty open set \(O\), the integer set \(d(O)\) has a minimum \(m\).
Intersecting \(O\) with the open sublevel \(\mathcal U_m\) produces a nonempty
open set on which \(d\equiv m\). Thus the locally constant locus is open
dense. If \(d(\rho)=r\) is not locally constant, openness of
\(\mathcal U_r\) forces arbitrarily nearby values below \(r\), placing
\(\rho\) on \(\partial\mathcal U_{r-1}\); the converse boundary implication is
immediate. Hence the jump locus is exactly the stated union of boundaries and,
as the complement of an open dense set, is closed nowhere dense.

Finally, the compact-family statement is a direct finite-subcover argument
using one fixed-signature holonomy neighborhood around each representation.
No compactness or continuity claim stronger than this is used.

## Originality

**PASS, to the best of our knowledge.** Faraco--Rungi's current
arXiv:2609.18436 version was checked at Problem 1.4, Proposition 2.13,
Corollary 4.6, and the bubbling subsection. The paper formulates minimal
branching degree as an open problem for non-Hitchin representations and gives
the ingredients above, but no upper-semicontinuity statement, degree-spectrum
theorem, generic local-constancy theorem, jump-locus description, or compact
finite-signature-bank result was located. Full-text searches for
“semicont”, “locally constant”, “degree spectrum”, and “compact family” found
no matching formulation.

The closest prior analogue located is Le Fils (Journal of Topology 16
(2023)), who computes minimal branching degree for complex projective
\(\mathrm{PSL}(2,\mathbb C)\) holonomy and proves degree-raising surgeries.
That article contains no matching “upper semicontinuous” or “locally
constant” formulation. This precedent is explicitly acknowledged because the
notion of minimal branching degree itself is not new.

The current SCOPE repository contains no record matching real-projective
minimal branching degree, the Faraco--Rungi preprint, or this holonomy-degree
filtration. The principal residual originality risk is that the motivating
preprint is extremely recent and the present theorem is a structural
consequence of several of its results; a later revision, forthcoming sequel,
or unindexed parallel note could make the same observation. No specifically
identified inaccessible paper provides concrete evidence of prior coverage.

## Value

**PASS.** Faraco--Rungi ask for the minimum branching degree of a non-Hitchin
representation, while prescribed-signature realization remains finer and
largely open. The present result isolates what can already be said globally
without computing that minimum: once \(d(\rho)\) is known, the entire
total-degree realization problem is solved, because the spectrum is exactly
one parity ray.

The deformation-theoretic consequence is also useful. Minimal branching
degree is an integer-valued upper-semicontinuous complexity, and such
complexity is locally constant on an open dense subset here; every failure of
local constancy lies on a closed nowhere-dense jump set. Thus the unknown
invariant has a stable generic regime rather than arbitrary variation.
The compact finite-signature-bank statement gives a practical uniformity
principle for compact representation families that is stronger than merely
bounding the degree.

## Limitations

The result does not compute \(d(\rho)\) for non-Hitchin representations and
does not solve the prescribed-signature realization problem. It gives no
effective degree bounds, neighborhood radii, or description of the jump
locus. The spectrum theorem concerns total branching degree only. The main
input is a very recent preprint, so later revisions or unindexed parallel
observations remain a real originality risk.

**Same-model review: passed. Independent audit: not yet performed.**
