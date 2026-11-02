# Mathematical review

## Correctness

**PASS.** The theorem has fixed finite dimension, positive initial masses and fixed positive integer quotas. The Dirichlet–multinomial identity gives exact one- and two-colour low-count probabilities, with the two-colour exceptional case handled by impossibility of simultaneous deficiencies at large time. Finite unions and the strict positivity of every mass justify the leading tail constant; the last-draw identity produces the sharp colour-marked local mass and the conditional terminal-colour limit. The standard discrete tail-sum criterion proves the exact moment threshold. At unit initial masses, counting weak compositions gives the completion CDF, independent last-colour law and power-law tail; comparison of two quota patterns at each of the totals \(d+1\) and \(d+2\) proves the converse rigidity. The entire proof uses explicit finite algebra and fixed-parameter Gamma asymptotics, not an extrapolation from computational checks.

An independent rational-path recurrence and a Dirichlet–multinomial summation check produced 6,214 passing exact or numerical spot comparisons. The checker does not certify infinite asymptotics; those follow from the displayed analytic argument.

## Originality

**PASS, subject to historical-priority limitations.** Jacobs, *Urns & Tubes* (arXiv:2110.02155), defines the general multicolour negative Pólya mass function in Definition 4 and explicitly leaves statistical properties of general tubes open in Section 10. That formula is acknowledged, not repackaged as new. The claimed advance is the sharp multi-quota tail and moment constants, conditional last-colour bottleneck rule, and unusual exact quota-blindness with a **converse classification**. Henze and Holmes, *Curiosities regarding waiting times in Pólya’s urn model* (arXiv:1911.01052), establishes the one-target waiting-time moment threshold; it does not assert a theorem for simultaneous multiple quotas or the terminal-colour mark. Anceaume et al., *Optimization results for a generalized coupon collector problem* (arXiv:1504.03878), treats independently drawn fixed-probability coupons rather than reinforcement. No equivalent statement was found in the checked published results or other accessible earlier claims, but classical occupancy literature is extensive, so historical priority remains a live risk. A full specialist literature review was not undertaken.

## Value

**PASS.** In the multiple-quota model already proposed in the literature, even finiteness of the expected time is not evident from finite simulations: the theorem gives the precise smallest-mass threshold for all positive moments, its leading constants, and the last-bottleneck composition. The unit-mass exception is structural rather than merely a parameter substitution: it gives a closed CDF valid for every quota vector, independence of the stopping time from the identity of the last completed tube, and an if-and-only-if classification of initial masses that can yield complete quota blindness. This sharpens the literature's general pointwise summation without claiming that the summation itself is new.

## Limitations and closest literature

The analysis assumes finitely many colours, unit reinforcement, fixed quotas and strictly positive initial masses. It does not give rates uniform over growing dimension or quotas, or a similar rigidity law for other reinforcement rules. The closest paper already contains an exact pointwise completion-mass formula, so a historical result extracting the same asymptotic and rigidity statements would supersede this finding. Comparisons of published work and accessible mathematical records did not yield such a result, but search incompleteness and possible unpublished or specialist literature are residual originality risks. Independent mathematical assessment is outstanding.

Self-review: passed. Independent audit: not yet performed.
