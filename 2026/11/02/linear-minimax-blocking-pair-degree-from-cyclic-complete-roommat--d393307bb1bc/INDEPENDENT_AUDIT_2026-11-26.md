# Independent mathematical audit

## correctness

PASS

For a core pair {a,b} and a third core agent u, exactly one arc from an endpoint to the other contains u, so exactly one endpoint prefers u to its partner. In the odd core, an unmatched u therefore has r+s-1=2k-r incident blockers with r pairs and s unmatched core agents, at least k. In even order an unmatched dummy adds one blocker to this count; if the dummy is matched to z, z instead wants every other core agent and has r+s=2k-r blockers among the remaining 2k agents. These cases cover all partial matchings and include the two-agent boundary. In the proposed matchings core pair offsets are k and k+1, so the matched core endpoints have at most k preferred alternatives. The residual core agent has exactly k blockers, whether unmatched or dummy-paired; a paired dummy cannot block with another core endpoint. The universal upper bound n-1 proves the claimed worst-case rate, not a universal sharp constant. For the threshold and census, I inspected the packaged code without executing it and ran a separate exact enumeration (checks/roommates_small.py, Python 3 with NumPy), generating matchings as disjoint subsets of edges and computing mutual preference by masks. Orders 1–4 had 1, 2, 18, 2634 strict symmetric profiles and none with optimum at least two. At n=5 the exact counts by optimum 0, 1, 2 were 9859346, 5331976, 7752, with 7272 of the last count complete-list. The five-agent cyclic instance already proves attainment. The census is not needed for the all-order construction.

## originality

PASS

The objective and a cyclic lower-bound idea are prior. The distinct content supported by the comparisons is the explicit all-order complete-list family attaining floor((n-1)/2) against arbitrary partial matchings, its unrestricted linear worst-case consequence, and the exact five-agent onset. This is not a priority guarantee.

## value

PASS

The circular-core argument closes the asymptotic order for concentrated blocking incentives under unrestricted matching, where allowing unmatched agents changes the lower-bound question. The exact value of the witness and the first five-agent obstruction distinguish a structural parity effect from a merely numerical rate or a lower bound forced by requiring cardinality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
