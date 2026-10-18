# Review of the Hamming geodesic rooted Horn-circuit spectrum

## Correctness — PASS

The claim is restricted to the shortest-path geodesic convexity operator on Hamming graphs. Its interval hull is a Cartesian rectangle; minimal rooted stems are characterized exactly by one private matching coordinate per premise row. Weighted inclusion-exclusion counts those stems without duplicate rows and gives the stated rank polynomial. The one-pass necessity argument follows from taking each minimal stem itself as input. A separate pair-interval rule system yields the stated polynomial-size chained basis. The written proof derives the exponential quadratic size bounds. An executable independent finite checker reports PASS for seven small (dimension, alphabet)-pairs and 984 test subsets, but is not evidence for an infinite theorem on its own.

## Originality — PASS, qualified

The binary specialization is **not novel**: its per-root rank counts coincide exactly with classical minimal-set-cover counts (Hearne–Wagner/Devitt–Jackson, the Royle set-cover article, and the MathWorld/A035348 table), except for the trivial one-set cover. The rectangular closure property is established in graph Cartesian-product convexity, and the generic prime-implicate/stem correspondence is established in Wild's survey. No equivalent all-nonbinary-\(q\) weighted-rooted-stem polynomial combined with the direct-vs-chained basis-size separation was identified in the inspected literature or searched mathematical-record index. Because weighted cover enumeration is elementary once the encoding is recognized, and some related originals were inaccessible, prior implicit coverage remains a material risk. This review does not certify publication priority.

## Mathematical value — PASS

The directness requirement has concrete mathematical cost in a natural infinite class of geodesic convexities: from at most cubicly many multi-pass rules to \(\exp(\Theta_q(d^2))\) indispensable one-pass unit rules, with every premise arity enumerated. The exact nonbinary spectrum and separation supply a reproducible size benchmark, not just a routine finite recomputation. General results and binary minimal-cover counts are explicitly excluded from the assessed novelty.

## Scope and limitations

The finding concerns equal-size alphabet Cartesian powers, one simultaneous pass, and unit conclusions; grouped or arbitrary chain-minimal bases are not classified. The formula and size-growth proof are mathematical; finite checker outcomes are corroboration. The greatest unresolved originality risk is a previously published weighted minimal-cover census or a general Horn/Cartesian-convexity result implying all nonbinary cases. No independent mathematical validation has occurred.

Self-review: passed. Independent audit: not yet performed.
