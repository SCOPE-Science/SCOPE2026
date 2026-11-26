# Independent mathematical audit

## correctness

PASS

Summing the three-mer counts by prefix and suffix separately recovers all two-mer counts except the final or initial occurrence, so the two endpoints are determined by the observations; with the shorter counts recovered conversely, this gives precisely indistinguishable-edge Euler trails with fixed endpoints. Every actual trail determines the last-exit tree, and the flow equations ensure that ordered outgoing lists with that tree exhaust all edges before stopping at the root. If two outgoing types are repeated, any valid tree has a local factor at least three. In the resulting functional heavy graph, the predecessor cut for a noncycle heavy edge has only that heavy exit, no heavy entrances, at most two entering unit edge types (by the four-vertex graph), and endpoint imbalance at most one, so its count is at most three. Across a consecutive segment of a heavy cycle of length c the difference in its boundary weights is bounded by 3(4−c)+3. Uniform reduction to cycle minimum two preserves support and trees. Every local factor affected by pumping is either constant or strictly increasing at the first step; if the reduced class is a singleton, its unique tree has all local factors one and no affected heavy type can share a nontrivial ordering with another type. Thus only canonical doubletons with individually permitted independent pumps are counted. The independently reproduced table gives all stated coefficients; for n>=14 its paired loop pumps give 6(n−10)+4(n−11) and single loop pumps give 90, yielding the stated periodic corrections and linear term. The repair clarifies earlier coverage without altering this proof or coefficient law.

## originality

PASS

The supported distinct part is the explicit doubleton coefficient law and generating function, not its rationality, the existence of an automaton, the individual class-size formula, or the total/singleton counts. The corrected literature section credits fixed-cardinality regularity and rationality explicitly. None of the strongest inspected sources supplies the bounded coefficient census, the binary size-two automaton with evaluated coefficients, or an equivalent exact coefficient formula.

## value

PASS

Size two is the first failure of unique reconstruction, a natural refinement of the known singleton and total counts. The formula determines how often that minimal ambiguity occurs, including its precise onset, linear rate and residue corrections. The finite census is useful here because the reduction proves it exhausts all lengths; it is not merely an implementation of prior rationality or a fixed-length table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
