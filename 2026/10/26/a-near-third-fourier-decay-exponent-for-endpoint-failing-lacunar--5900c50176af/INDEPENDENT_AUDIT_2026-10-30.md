# Independent mathematical audit

## correctness

PASS

Read complete 9831-byte RESULT.md blob 90cc766ed1b4813dae4ec5163fef5b2b897621cb and reconstructed each proof component rather than relying on an absent verifier. The one-per-cell random x_j selection has expectation equal to uniform[1,2] Fourier integral; Hoeffding for real/imaginary parts, O(N⁴) mesh, 7π derivative bound and t=5sqrt(log N/N) give uniform empirical error. N^{-3/2}-radius density bumps have mass 1/N each, total mass one, at most two overlaps, ||K_N||∞=O(N^{1/2}), and sinc factor. Across frequency intervals |ξ|≤N^{3/2}, N^{3/2}..N³, and ≥N³ the worst noise exponent is N^{(3β−1)/2}sqrt(log N), uniformly controlled for β<1/3. For dyadic N=2^L a normalized cancellative atom and widely separated left-neighbor spikes yield disjoint positive output sets E_k with |E_k|≥c for ~L scales k∈[L/4,3L/8]; N^{-3/2} spike radii scale to o(N^{-1}). Superlacunary N_m=2^{q^{2m}} and positive mixture weights (q−1)q^{-m} preserve uniform Fourier decay; low-index density terms are O(N_m^{-1/4+1/(2q²)}), high-index mass errors are O(q^{-m}) in L1. After exceptional sets, the target contributions ≥cq^{1-m} on ≥c q^{2m} disjoint measure, giving weak quasi-norm ≥cq^{m+1}→∞ with uniformly normed atoms. Independent rational exponent checks corroborate 4 strict β choices; these numeric/symbolic checks are not infinite proof. Endpoint 1/3 and smooth density are excluded.

## originality

PASS

Qualified PASS for the specified ABSOLUTELY CONTINUOUS one-dimensional measure: Zhou (Oct 15, 2026) already proves the same endpoint failure for an absolutely continuous measure but with Fourier exponent 1/8, and his complete source makes explicit the N^{-1/4} sampling error and bump radius N^{-2}. Here a sharpened Hoeffding O(sqrt(log N/N)) bound and radius N^{-3/2} give all β<1/3, a strict new quantitative regime. Cen–Hong–Wu (Oct 16) independently proves stronger β<1/2 but its full primary theorem explicitly constructs a SINGULAR Lebesgue-null measure, so it does not directly entail an absolutely continuous counterexample. This distinction is essential; possible unsurveyed smoothing/mixture arguments extracting an absolutely continuous example from their theorem remain residual priority risk.

## value

PASS

Improving the Fourier decay of an absolutely continuous one-dimensional counterexample from a fixed 1/8 exponent to every β<1/3 is a substantial quantitative strengthening of a newly resolved endpoint problem, with a single fixed measure and explicit Hardy-atom failure. The result identifies a strong decay regime compatible with endpoint breakdown, rather than a trivial change of constants. It does not claim optimal exponent 1/3.

The dated certificate retains the supplied scientific assessment, sources and limitations.
