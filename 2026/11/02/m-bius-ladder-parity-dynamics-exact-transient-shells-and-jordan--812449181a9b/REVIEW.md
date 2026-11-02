# Scientific review: Möbius-ladder parity dynamics

## Correctness — PASS

The update matrix is exactly multiplication by \(z+z^{-1}+z^n\) in the binary cyclic ring of length \(2n\). The factor \(h=z^2+z+1\) is the unique possible zero-eigenvalue factor because every root of the ring modulus obeys \(z^n=1\). Its multiplicity is \(2e\), while the update numerator has \(h\)-valuation at least two when \(n\) is odd and exactly one when \(n\) is even. This independently determines the entire zero-primary Jordan structure and all transient shells. The fixed-state formula follows by gcd kernel dimension; a separate \(z+1\)-valuation proof establishes the sharp parity trichotomy. The untwisted comparison is derived explicitly from a two-by-two local matrix and its Smith invariants, rather than assuming an earlier result.

Independent finite computations used a direct graph-update matrix and functional-graph enumeration, cross-checking the exact formulas for 1,115 matrix cases, 429 comparison cases and 87,360 binary states. No computational sample is used as an infinite proof.

## Originality — PASS, qualified

The strongest close predecessor is the known complete analysis of synchronous neighbor-XOR on the untwisted prism \(C_n\square K_2\), including its three-divisibility criterion and shells. For divisible half-circumference the prism has nilpotent partition \(2+2\) in the odd case and \(e+e+e+e\) in the even case, whereas the twisted Möbius ladder has \(1+1+1+1\) or \(2e+2e\). Those statements do not imply each other by graph isomorphism or the known prism recurrence. The primary texts by Martin–Odlyzko–Wolfram, Nordahl, Tadaki and Zaidenberg establish general polynomial/cellular-automaton methods, periodic sets and relaxation phenomena but do not present the exact Möbius-ladder chain-fusion theorem in the material examined. The residual risk is a differently titled earlier solution for twisted periodic boundary conditions or a specialized adjacency-matrix paper not retrieved.

## Mathematical value — PASS

This is a natural comparison of two three-regular periodic ladder families with the same vertex counts. The exact equality of periodic population despite a complete change of nilpotent Jordan partition is a nontrivial structural boundary: in the even case two longer chains replace four shorter ones, doubling the maximal transient while preserving the recurrent density. The all-length shell counts and fixed-state trichotomy are useful sharp quantitative invariants, not an arbitrary finite calculation.

## Limits

The result is restricted to characteristic two and synchronous neighbor sums. The finite tests cannot exclude unseen proofs elsewhere. The gcd primitive-cycle formula is exact but does not supply a simplified global-order formula at arbitrary non-dyadic sizes. Independent expert review has not been performed.

Self-review: passed. Independent audit: not yet performed.
