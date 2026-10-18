# Scientific review

## Correctness — PASS

The first-round winner is approval-maximal for both methods. With second-candidate support \(s\) and \(u\) supporters outside the first winner, the actual PAV marginal is \((s+u)/2\) and the actual Phragmén load is \(1/d+(d-u)/(ds)\). The two strict inequalities they induce support a complete three-case integer proof of the electorate lower bound, uniqueness of the nine-voter orbit, and a constructive arbitrary-size extension. A separate exact-arithmetic implementation exhaustively checks all 11,439 anonymous profiles of size at most nine, finding exactly the stated six discrepancies, and directly checks the extension on 100 distinct sizes. Neither the proof nor verification assumes generic tie-breaking.

## Originality — PASS with residual priority uncertainty

Janson, *Phragmén's and Thiele's election methods*, arXiv:1611.08826, Sections 3, 4.2, 13.5–13.8, gives the two standard algorithms and large separating examples, including a two-seat counterexample in Example 13.6. This proves that rule separation is old; the new claim is the **sharp minimum** and **complete labeled classification** for the smallest nontrivial candidate/seat domain under strict comparisons. Lackner and Skowron's Chapter 2 defines and exemplifies both rules without the sharp boundary. General representation results for Phragmén's methods do not imply this exact electorate threshold. Overlap searches checked both exact and equivalent formulations. Undiscovered prior enumerations and a possible stronger comparison theorem remain priority risks.

## Value — PASS

The smallest domain in which the two historically central sequential proportional approval methods can disagree is three candidates and two seats. The theorem shows precisely when their genuinely different treatment of already represented supporters first affects a strict election, and shows the only minimal mechanism up to symmetry. This is a motivated natural boundary and complete minimal classification, not a numerically arbitrary sample; it is useful as a small benchmark for algorithms, explanations of the rules, and testing implementations.

## Limits

All results require exactly three candidates, two seats, nonempty approval ballots, and no tie at either step for either method. Publication priority has not been independently established. The computer checks are finite and do not substitute for the supplied integer proof of the all-size extension.

Self-review: passed. Independent audit: not yet performed.
