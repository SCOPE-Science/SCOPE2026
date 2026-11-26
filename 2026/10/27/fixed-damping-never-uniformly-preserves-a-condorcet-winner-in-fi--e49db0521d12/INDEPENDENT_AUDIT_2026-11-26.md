# Independent mathematical audit

## correctness

PASS

The two-ballot gadget reverses every runner comparison except its designated one. Placing A at opposite ends doubles the runner margins while tying every A comparison, before the final ballot gives A four one-vote victories. Each runner column has at least one loss of order k; the A-entry and the bounded BallotRank self-loop vanish in the limit. A's column is exactly e_A. With t=(1-d)/5 the runner equations eliminate to (4-3d^3-d^4)b=t(4+6d+5d^2+d^3); factoring (1-d) yields the stated positive limiting B-A gap for every fixed 0<d<1. Resolvent continuity implies strict reversal at finite k for each d. For fixed k each runner has positive one-step transition to the absorbing A, proving the reversed high-damping limit and noncommutativity. The separately stated 601-voter fraction was reproduced exactly by reconstructing the ballots and using rational determinants in independent_checks.py (python /workspace/independent_checks.py).

## originality

PASS

The primary BallotRank work uses precisely the same weighting and raises fixed-damping extremal examples, but the inspected comparison does not supply the five-alternative family, all-d quantifier, limiting gap, or reversed limits. The nearby convergence-voting results use a different normalization. No distinct covering indexed record was identified in the bounded searches.

## value

PASS

This supplies a small-alternative finite obstruction for every fixed positive subunit damping and resolves the specific extremal direction raised in the BallotRank paper. The one-vote victories and noncommuting limits explain why moving damping close to one is not a profile-uniform remedy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
