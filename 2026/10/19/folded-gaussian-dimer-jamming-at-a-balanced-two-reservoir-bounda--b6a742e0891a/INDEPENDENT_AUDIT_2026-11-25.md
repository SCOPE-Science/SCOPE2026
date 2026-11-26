# Independent mathematical audit

## correctness

PASS

This is a pass for the repaired claim, not for the frozen formula interpreted literally. The frozen disjoint-union symbol deletes all A–B edges, contradicts its prose and rate AB/N, and for α>1/4 would leave at least 4m_N−N unmatched vertices deterministically, disproving the stated scaling under that reading. The complete corrected RESULT.md in /workspace/repairs/5/ replaces the disjoint union by the complete bipartite graph and preserves the adjacency actually used by the proof and verifier. It explicitly states the rescaled time, makes the stopping/localization argument precise, and describes the finite verifier as labeled-subset recursion rather than full permutation enumeration. On the corrected graph, exponential memorylessness gives the four rates, parity and maximality give U=|D_jam|, and A–B matching plus clique pairing gives a perfect matching. I substituted each jump into both scaled generator ratios and checked the deficits with AB≤L²/4 and C≤L, including C=0. The D² compensator bound uses the actual cross-to-clique count (at most C₀); stopping bounds imbalance exits by O(N^(−1/3)). The 2C/L estimate controls both the ratio exit and the tail integral of c, and the NC/L² supermartingale with its integrating factor gives C at L≈N^(2/3) of order O_P(N^(1/3)). The cutoff time bound follows from summing 9N/L² over remaining levels; a failed cutoff has vanishing probability. Hence later D changes are o_P(√N). The squared integrating factor is tight, and the tail of the unweighted bracket has expectation ≤E C_T/N, which vanishes in the successive limits. With the stated localization, the jumps vanish uniformly and the martingale CLT yields the claimed normal for D and folded normal for U. Evaluating the positive fluid bracket gives the displayed variance; E D_jam²≤C₀ gives uniform integrability for the mean. Independent bounded calculation agrees with the recorded three nontrivial exact probabilities and variance values.

## originality

PASS

For the corrected graph, the credited result is the terminal centered √N fluctuation with the explicit variance and uniform-integrability conclusion under balanced, macroscopic reservoirs and a macroscopic clique. The greedy algorithm and density-dependent finite-time framework are known. The strongest earlier indexed split-graph result has the same scale for fluctuations but about positive density in a different graph. The closest folded-normal analogue concerns a rare independent third part and is later. No checked prior passage covers the corrected finding.

## value

PASS

On the corrected dense graph, a perfect matching is immediate while irreversible uniform greedy matching leaves a diverging terminal defect despite its limiting fraction being zero. The explicit folded-normal law and mean identify the finite-size amount of jamming and its dependence on composition; a fixed-time or density approximation cannot supply that information. The terminal cutoff matters mathematically because the observable lives at absorption rather than at a fixed fluid time.

The dated certificate retains the supplied scientific assessment, sources and limitations.
