# Independent mathematical audit

## correctness

PASS

For a disliked sincere winner b and liked new winner a, a successful report must include a and exclude b. If P is the opponent score, the two strict victories imply u_s<P_b-P_a<u_t. For m=1 no liked/disliked pair exists; for m=2 a sincere singleton already supplies the maximal weight; for m=3 the only candidate interval (3/2,3) contains no multiple of 3/2. Independently for m=4, scale weights to 2,3,6. The strict gap forces a size-three report (there is no integer strictly between 2 and 3), consisting of all names except b. Thus P_b>P_a and P_a>P_c for both other names c. If only one positive opponent ballot contains b, that ballot cannot contain a (or the gap is nonpositive) or any other name (that name would receive at least P_b); as a singleton its weight 2 is too small. If two positive ballots contain b, exactly one must contain a (P_a>0 and P_b>P_a). The other has weight 3 since its weight equals the gap, and hence includes another name c; P_a>P_c>=3 forces the a-containing ballot to have weight 6, but it then also supports a third name that ties or exceeds P_a. These contradictions cover at most two opponents. A separate exact unordered-opponent replay (reproductions/frozen_checks.py, argument 5) tested 256, 4096 and 34816 tuples with zero events; quotienting by opponent permutations is exhaustive. The four-voter witness yields (14/3,10/3,0,0) and (14/3,6,4,4), with different strict winners. Joint minimality is under the coordinatewise order (or minimizing candidates first), not a universal four-voter lower bound independent of m: with five candidates, opponents {A,B},{B,C}, truth {A} and deviation {A,D,E} give strict B then A with three voters. The original's explicitly scoped claims hold. The supplied checker uses int.bit_count(), so its documented Python 3.8 minimum should be read as Python 3.10 for replay; this does not affect the exact verdict.

## originality

PASS

The rule and its dual formulation are prior. The supported distinct claim is the strict-winner obstruction for all electorates with at most three candidates and the exact first electorate size conditional on four candidates. The inspected same-rule primary passages prove FVR optimality and scoring-rule uniqueness, not this incentive classification. Nearby exact catalog thresholds use different voting or allocation maps; the known size-approval weight class in the inspected abstract has opposite monotonicity. This is a bounded priority assessment.

## value

PASS

For a rule motivated by a representation guarantee, the first strict incentive failure at the smallest feasible candidate count is meaningful independently of tie policy. The all-electorate small-candidate obstruction comes from a score lattice, and the sharp four-candidate distinction additionally depends on compulsory padding. This is more than a computed example; it identifies a discrete boundary without claiming ordinary strategyproofness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
