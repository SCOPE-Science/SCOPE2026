## Correctness

PASS. The derivative recurrence is obtained by differentiating the defining polynomial recurrence. The characteristic polynomial at \(z=1\) has a double root at \(1\) and all other roots strictly inside the unit disk; the coefficient proof for this root-location statement is included in RESULT.md. The finite-difference operator has leading action \(a\binom{2k}{2}\sigma^2 n^{2k-2}\), giving the coefficient recursively. Polynomial functional calculus then yields the Jordan-block norm asymptotic. The variance bound and its equality case follow from \((1-Y)(Y+m-1)\ge0\).

## Originality

PASS, with residual literature risk disclosed. The closest primary source proves scalar boundedness/rapid growth for the same recurrence but does not state the fixed-order derivative asymptotic or the Jordan-block coefficient and assumes diagonalizability in its matrix application. General Faber-polynomial norm results concern boundary supremum norms, not this derivative law. A related deltoid preprint and a momentum/Lanczos preprint were identified but their full texts were not inspected; the claim is not presented as an exhaustive census of all literature.

## Value

PASS. The result gives an exact sensitivity invariant for a natural family of accelerated eigenvalue polynomials on defective/non-normal boundary models, and identifies the unique variance-maximizing recurrence law that minimizes leading Jordan-block amplification at fixed order. It is a precise robustness diagnostic, not a claim that the defective iteration converges.

Closest literature: arXiv:2510.24608; arXiv:2509.22588. Limitations: fixed recurrence order, derivative order, and Jordan size only.

Self-review: passed. Independent audit: not yet performed.
