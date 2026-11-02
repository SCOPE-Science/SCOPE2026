# Self-review

## Correctness — PASS
The central rational lemma has two independent rational identities: deck symmetry under \(w\mapsto r/w\), and unit-circle Schwarz reflection \(h(w)h^*(1/w)=1\). Their combination yields \(h(w)=h(r^2w)\) for \(0<r<1\); Laurent uniqueness forces constancy. Quotient reduction gives polynomial phase rigidity. Laurent support \([-n,n]\) of an ellipse-parametrized degree-\(n\) polynomial gives trigonometric intensity degree at most \(2n\), so any \(4n+1\) distinct samples suffice by a polynomial root bound. A reciprocal linear pair disproves circle rigidity. The checker verifies representative symbolic and numerical consequences but is not used as an infinite proof.

## Originality — PASS, provisional
The closest inspected source is Chalendar–Partington (2024), which treats two intersecting lines and two circles, not a single noncircular ellipse; Perez (2020) has a corresponding earlier two-set result. Orevkov–Pakovich (2023) is the strongest nearby source: its Cartwright discussion and rational-lemniscate theorem could conceivably yield this assertion as a corollary, but the inspected source does not formulate an ellipse exception or the universal \(4n+1\)-sample polynomial statement. Searches for ellipse phase retrieval, rational lemniscates on ellipses, and exact finite interpolation did not identify a directly dominating result. The historical-priority risk is explicit; the absence of a search result is not treated as a proof of novelty.

## Mathematical value — PASS
The theorem gives a full geometric dichotomy in a standard inverse problem: a single generic ellipse is universally phaselessly determining for the entire polynomial class, while the most symmetric limiting case (a circle) is not. It also supplies a uniform, location-independent finite measurement scheme for *all* degrees, with no generic-coefficient assumption. This addresses a concrete gap between known two-curve uniqueness and classical circle ambiguities; the sample count is not claimed optimal or stable under noise.

## Residual limitations
The proof is restricted to rational functions and complex polynomials, not all local holomorphic functions. No independent review was undertaken and no worldwide priority certification is asserted.

Self-review: passed. Independent audit: not yet performed.
