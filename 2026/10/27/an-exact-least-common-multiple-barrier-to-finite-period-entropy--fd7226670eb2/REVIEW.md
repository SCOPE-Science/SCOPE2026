# Independent mathematical audit

## correctness

PASS

The constraints are local on windows of length m+2. Assign any initial m symbols and any golden-mean output; the recurrence determines x in both directions, giving exactly kappa^m lifts. More directly, a length-L word for L≥m is determined by its initial m symbols and a golden-mean word of length L-m, and all such choices extend by padding the output with zeros. Fibonacci growth gives log(phi). In the state graph (m-block, previous output), each advance rotates the coordinates and increments the coordinate scheduled in its time residue class mod m if the output is one. For any sufficiently large prescribed path length, choose the requisite residue increments with isolated ones in disjoint padded windows, after accounting for the final required output. This permits either previous-output symbol and works also at m=1, where alternating positions give spacing. Hence the presentation is primitive. For n dividing m every ambient n-periodic point has zero output. Otherwise the singleton-one input has forbidden residue -1 when kappa≥3; for kappa=2 demanding output ones at positions 0 and 1 prescribes two nonloop parity edges, consistent even if they coincide. At least one point is therefore excluded. Divisibility gives the least lag; inversion between fixed-point and primitive-orbit counts and the formal log and exponential give the two finite-cutoff equivalent descriptions. An independent bounded enumeration checked 108 period and residue-sum cases and strong connectivity plus a loop in all 18 presentations for kappa=2,3,4 and m=1,...,6; frozen CHECK.py and VERIFICATION.md were inspected, not run. No uniform-memory or all-family minimal delay is implied.

## originality

PASS

The modular difference code and general periodic-lift algorithms are already covered, and a distinct later indexed theorem explicitly covers the cycle-sum period calculation. Credit is limited to the joint mixing golden-mean construction of a fixed entropy gap with the sharp finite observation equivalence in this lag family. The sources compared do not establish that joint statement.

## value

PASS

These explicit mixing SFTs can agree with full-shift periodic data to any prescribed finite order at a fixed positive entropy gap. The sharp LCM cost answers how large the delay must be within the same simple family rather than replacing the problem by arbitrary graph size. The result is a meaningful nonidentifiability example with a stated cost, not a claim about all SFTs at fixed memory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
