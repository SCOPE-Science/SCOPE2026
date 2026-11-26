# Independent mathematical audit

## correctness

PASS

Each nonempty subset of [1,N] defines exactly one admissible sequence in increasing order. Each nonempty contiguous block is represented by a positive prefix difference, and all such differences are between 1 and N(N+1)/2. In the supplied code, nonzero mask stamps are unique within each N and their array is reset between domains, so they mark exactly one occurrence of each distinct sum per candidate. The maximizer counter is reset on improvement and incremented on ties. Independently implemented NumPy enumeration instead uses packed bit flags for the positive differences of prefixes at all original boundaries, dropping zero differences from empty blocks; repeated boundaries cannot add a new positive difference. It exhausted all 33,554,406 nonempty masks across N=1 through 24. Through 23 the maximum equals the full-sequence count; at 24 it found maximum 188, full-sequence count 186, and exactly one winner with mask 16776191, which is the full mask with bit 10 removed. This verifies minimality, the exact maximum and the claimed uniqueness without any inference about N>24.

## originality

PASS

The benchmark sequence's values and the general extremal question are prior. The least N where the benchmark fails, the exact maximum there, and the unique optimizer are not covered by the strongest inspected material.

## value

PASS

The full initial interval is the canonical benchmark for an established extremal problem. Its sharp first failure, after 23 domains of exact optimality, is a natural finite boundary independent of the size of the gain. The unique maximizing deletion shows precisely what changes at that boundary and gives an exact reference point for future structural or computational analyses.

The dated certificate retains the supplied scientific assessment, sources and limitations.
