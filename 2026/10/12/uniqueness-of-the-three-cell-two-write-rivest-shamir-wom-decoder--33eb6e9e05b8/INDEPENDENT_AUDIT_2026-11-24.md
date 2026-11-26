# Independent mathematical audit

## correctness

PASS

Passes the replacement files in repairs/5, not the frozen model/count combination. In the original model the same update is iterated without a generation input. The first state must have at least four states in its up-cone and hence weight at most one. All four low-weight states must carry distinct labels. The top vertex shares each unit-vector cone and cannot carry any unit-vector label; each weight-two vertex then must carry the label of its complementary unit vector. Conversely, a complementary-pair labeling has one representative of each label in every unit-vector cone. The initial update from zero is forced to return the low state for the requested message. The second-write inputs with state zero are identical to the initial inputs, because zero is itself a possible first state, and hence the second row at zero is already fixed. Thus one reachable common update table per decoder, not 16. If the second-write rule is allowed to be independent, four binary choices at zero give 16; this is separately identified as a different model. A new exhaustive check, now in repairs/5/verify.py, ran through 65536 functions and obtained 24 decoders, one shared table each, 16 separate second tables each, and the same decoder digest as originally reported. Two cells are impossible because four distinct first representatives would have to include the top state. Off-domain update values are not counted.

## originality

PASS

Pass the necessity/classification of all admissible decoders at the canonical minimum parameter, and its reachable-table rigidity under the correct model; do not count the original decoding formula, the known optimum, or the stated historical definition as new. No inspected result establishes the necessity direction; the independent-count distinction is a consequence of the classification, not an additional priority claim.

## value

PASS

The benchmark is the motivating minimum-size case of the original WOM problem. The full rigidity result answers whether the commonly reused terminal-pair coloring is a design choice and distinguishes the reachable rule in the original model from an update that knows the write number. This is an extremizer classification, not a count of repeated entries of a known table or a recomputation of the known minimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
