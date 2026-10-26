# Review: Petersen incidence-poset rowmotion

## Correctness — PASS
The ideal parametrization \((U,F)\), with \(F\subseteq E(U)\), is exhaustive. Rowmotion is derived directly from the minimal outside elements. A separate edge-first/vertex-second toggle computation agrees on all \(133958\) ideals, and two different Petersen graph models independently give the same \(39\) length multiplicities, \(6207\) disjoint cycles, and the exact least common multiple. The embedded standard-library verifier completed with `VERIFY_OK`.

## Originality — PASS, with residual risks
The most relevant full text, Grinberg–Roby (2014/2016), derives period information for *skeletal* posets; the present incidence poset is a connected non-skeletal cyclic example. Elizalde–Plante–Roby–Sagan (2021) derives fence orbit structures, whereas the Petersen incidence poset is not a fence. Searches under graph-incidence rowmotion, antichain toggles, and exact numerical parameters did not locate this census. A previously unindexed enumeration and uninspected incidental examples remain possible; the absence of a hit is not treated as a proof of priority.

## Value — PASS
The Petersen graph supplies a distinguished symmetric test object with a standard incidence poset. The exact orbit census (39 distinct lengths and an order with 11 distinct prime factors) exhibits dynamics far richer than a small-period guess based on the two ranks would suggest. It is a motivated complete finite invariant, not an arbitrary slice and not an asserted general theorem.

## Boundaries
The finding concerns only classical rowmotion on the specified labelled 25-element poset. Independent verification by a separate reviewer has not occurred.

Self-review: passed. Independent audit: not yet performed.
