# Review of Optimality certificates for three length-six limited-permutation covers

## Correctness
The claim is reduced to three finite set-cover instances defined directly by the channel. Each upper bound is witnessed by an explicit center list. Each lower bound is witnessed by a nonnegative rational weight function with ball weight at most \(1\) and total weight equal to the proposed cover size. The standard weighted-cover inequality therefore proves the matching lower bound. The bundled verifier reconstructs the universes and all legal channel balls from definitions rather than trusting a solver output.

## Originality
The closest source is arXiv:2607.19566v1, Section 5.1, Table 3. It gives the same three cover sizes as explicit replacement constructions, but the surrounding text explicitly says that no optimality of any replacement size is claimed. Searches for the channel name, the three multiset types, the exact sizes, set-cover language, and adjacent-swap aliases did not locate a published statement proving these three optima. The 2017 foundational paper treats the general limited-permutation channel rather than these concrete finite covering numbers.

Residual originality risk remains because finite covering results can be reported under permutation-cover or set-cover terminology rather than the multiset-type notation used here. The direct non-optimality statement in the closest same-parameter source substantially reduces that risk.

## Value
These are not arbitrary finite slices: they are three of the five concrete type replacements used in the recent length-six covering bound. Exact optimality shows that the savings contributed by these three rows cannot be increased without changing the local covering construction or using another type. The rational lower certificates are compact and reusable in later searches for sharper global covers.

## Limitations
The remaining two replacement rows, of types \((2,1,1,1,1)\) and all-distinct, are not settled. No global optimality statement for \(K_q(6;1)\) follows.

Same-model review: passed. Independent audit: not yet performed.
