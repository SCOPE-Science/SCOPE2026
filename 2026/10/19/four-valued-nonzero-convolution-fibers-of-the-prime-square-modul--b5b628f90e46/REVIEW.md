# Scientific review

## Correctness

**PASS.** The proof enumerates all \(p^4\) targets by the exact matching-valuation condition, derives the unit-unit fibers from a quadratic discriminant modulo \(p^2\), and derives the valuation-one spikes from an equation in \(\mathbb F_p\). These are exhaustive for every odd prime \(p\ge5\), not an extrapolation from enumeration. The special zero fiber and the normalization of the fourth Fourier moment were checked separately. `verify.py` independently enumerates all representations for five primes.

## Originality

**PASS, best knowledge.** Full-text comparisons establish that Hickman--Wright's ring restriction estimates and Humphries' modular-inverse equidistribution do not assert the four-level prime-square convolution fiber classification. Ricotta--Royer (Proposition 5.4) study the relevant collision equations to obtain bounds; Bower--Evans--Luo--Miller count coordinate sums, not the vector Minkowski square. The closest indexed finite-field hyperbola results give sharp norms in actual fields rather than singular prime-square rings. The new full target-by-target multiplicity spectrum is not implied by any located statement. Residual risk: an equivalent exact Kloosterman fourth moment or full fiber table may be implicit in specialized earlier literature.

## Mathematical value

**PASS.** The object is the standard prime-square modular hyperbola and its natural two-fold convolution, not an arbitrary numerical slice. Resolving its entire nonzero fiber spectrum shows distinct generic and singular \(p\)-adic regimes, including the \(2p\) spike confined to valuation-one targets. The resulting exact averaged Kloosterman fourth moment has constant-input amplification tending to \(6\), contrasting with the field-level \(3\)-scale. This is a reusable quantitative invariant in finite-ring Fourier restriction, even though the unrestricted norm is open here.

## Literature and limitations

The nearest primary material is Hickman--Wright (2018), Humphries (2020), Ricotta--Royer (2018), and Bower--Evans--Luo--Miller (2012), along with separately indexed finite-field hyperbola findings. The ring exponent is restricted to two, and the fourth moment has constant input; no sharp unrestricted operator norm is claimed. Searches cannot exclude unindexed equivalent results.

Self-review: passed. Independent audit: not yet performed.
