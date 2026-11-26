# Independent mathematical audit

## correctness

PASS

The overlap graph has one edge per linearly allowed n-word. Appending 11 and then the destination state gives strong connectivity. Edge-label sequences of closed walks, with periodic reading, are exactly the legal covering cycles when the walks cover all mandatory edges. For length L=n-1 states the divergence is [starts 10]-[ends 01]; added flow must connect each negative state to a positive one, giving a lower bound by the sum of nearest-positive distances. The exceptional state 0^{L-1}1 needs L shifts: before L-1 there is a leading zero, and at L-1 a leading 10 would require the first appended bit to complete 010. Appending 10^{L-1} attains L legally, including L=2. Otherwise the initial position j of the first 10 is necessary, and writing the state 0^a1^b t with a+b=j, b≥1, gives a legal extension 1^b0^a, attaining j. Each ordinary target is decoded at its last 01; the exceptional target has no 01. Hence the targets are distinct and exhaust the positives, so the shortest paths give an optimal Eulerian augmentation simultaneously. Suffix states empty, 0, 01 give the E_n series. The suffix t consists of an initial and final 1 around positive zero-runs separated by one-runs of length at least two; its series is z^3(1-z)/((1-z)^2-z^3). There are j choices of a,b at cost j, yielding the claimed C_n series with exceptional term sum_{n≥3}(n-1)z^n. Independently solved the unit-cost flow on the allowed graph using residual shortest augmenting paths and checked a nonnegative reduced-cost potential at termination; n=3–12 gave the ten stated minima and excess costs 2,3,5,10,20,38,70,127,228,406. The all-n result follows from the proof, not the finite check.

## originality

PASS

The supported distinct contribution is the all-order legal-host augmentation optimum and its explicit shortest-path bijection, not the routine finite-word avoidance count or the directed-postman framework. The strongest same-pattern match is the November 2 catalogue record: it even has the same ordinary paths and the same finite-word count, but uses one forbidden transition at the exceptional state to lower the optimum by one. Its stated theorem is for unrestricted hosts and its catalogue date is later. No compared earlier result entails the legal-host optimum.

## value

PASS

A legal host is the natural model when the printed forbidden pattern must never occur, not just when only legal windows are required. Balancing a non-Eulerian restricted graph by simultaneously nearest positive states gives a reusable constructive mechanism and an exact rational excess series for an infinite family. The single forced extra transition relative to an unrestricted host identifies exactly where cyclic legality imposes a cost.

The dated certificate retains the supplied scientific assessment, sources and limitations.
