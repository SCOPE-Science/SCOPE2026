# Independent mathematical audit

## correctness

PASS

The theorem is correct for every N≥3 and 1≤k<N with the stated complex projector span. The Weyl character diagonalization gives R=# of nonzero ambiguities (Goldberger–Kang–Okoudjou Theorem 1). The overlap I∩(I+a) is exactly two possible intervals with lengths r=max(k−a,0), s=max(k+a−N,0). For a single interval, nonzero b geometric-series zeros count gcd(N,r+s)−1; for two nonempty intervals the numerator factorization is (1−z^k)(1+z^a), z=exp(2πib/N)≠1. The condition z^k=1 contributes gcd(N,k)−1, z^a=−1 contributes β_N(a), and the intersection contributes β_d(a), while b=0 is positive. Summing yields c_a as claimed. For k≤N/2 an empty overlap prevents full rank; for k>N/2 odd N requires all lengths in [2k−N,k] coprime to N, equivalent to [s,2s] avoiding smallest prime divisor p and hence s≤(p−1)/2. For even N the a=N/2, odd b two-arc coefficient vanishes. For N=2^q, grouping b by exact root order t=2^j gives Z_t(k)≥N/t for k≤N/2 and Z_t(k)=N/t except positive t|k excess for k>N/2; summing φ(t)=t/2 gives N²−R=qN/2+(2k−N)(2d−2−h)/2, and exactly odd k>N/2 minimize the deficiency. A separately written exact integer cyclotomic-residue checker (not the supplied code) directly counted all lags/order classes for every 3≤N≤45 and every k, agreeing with the per-lag rank count, odd thresholds, and 2-power formulas; the infinite claim follows from the derivation, not finite testing.

## originality

PASS

Qualified best-of-knowledge originality for the complete (N,k) quantitative rank profile and sharp power-of-two capacity. Goldberger–Kang–Okoudjou (2021/2022) establish the general rank/nonzero-ambiguity equivalence and support-one/two cases but no all-length interval-indicator census. Bendory–Eldar (2015) supply the sufficient overlap-coprimality criterion for successful long rectangular windows; those successful odd-dimensional cases are therefore not claimed as novel. The 2026 published prime-dimension positive-rational-window theorem already implies every odd-prime boxcar rank; a published two-hole theorem covers the k=N−2 special case. Neither mathematically determines all composite dimensions/lengths or the sharp 2^q capacity and optimizer classification. The claim derives these via two-arc overlap cancellations and order-specific exact zero counts. Search absence alone is not used as a novelty proof; unindexed exact rank tables and a possible implication in uninspected sources remain risks.

## value

PASS

A contiguous flat (“boxcar”) window is a canonical experimental probe in cyclic STFT/spectrogram measurements, and the complex dimension of its full rank-one measurement-operator span is a natural quantitative linear-tomography invariant. Prior general ambiguity criteria and rectangular-window recoverability conditions do not give the number of undetectable Hermitian observables at each deficient N,k. The family-wide exact gcd/2-torsion formula is reusable for composite dimensions, detects nonmonotonicity under increasing window length, and the sharp 2^q law N²−(N/2)log2 N with all odd upper-half maximizing k gives a nontrivial constrained-design obstruction. These specific unknown arithmetic ranks could reasonably be needed in structured measurement design even without a new reconstruction algorithm or a paper-sized downstream theorem. The standard endpoint k=1, all odd-prime ranks and k=N−2 have published antecedents, but the complete composite classification and quantitative 2-power optimum are independently motivated and not an arbitrary finite slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
