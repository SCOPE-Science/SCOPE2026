# Review

## Correctness
PASS. The claim reduces observed relative utility to the sign of the treat-all net benefit under perfect constant-risk predictions. On the event where relative utility is defined, the treat-all branch gives zero relative utility exactly at counts \(S_n\ge\lceil nt\rceil\), while the treat-none branch gives zero exactly at counts \(S_n\le\lfloor nt\rfloor\). The denominator \(1-q^n-(1-q)^n\) is exactly the probability that the relative-utility denominator is nonzero. The logarithmic limit follows by matching Chernoff and one-lattice-mass Stirling bounds, and the critical/local limits follow from the binomial central limit theorem. The finalized exact checker reconstructs the net-benefit definition and returns `VERIFY_OK`.

Risk: the large-deviation statement is logarithmic only; no Bahadur prefactor is claimed. Conditioning on defined relative utility is essential to the stated clean rate.

## Originality
PASS. Hoessly's Appendix A.4 assumes \(t<q<1\) and uses only a law-of-large-numbers argument to conclude that the unconditioned probability of defined zero relative utility tends to one. The inspected source does not give the exact finite-\(n\) binomial formula, the symmetric \(q<t\) branch, a large-deviation rate, the \(q=t\) limit, or the root-\(n\) transition profile. Earlier Baker relative-utility papers define and motivate the normalization but do not provide this constant-risk phase diagram. Targeted indexed searches for the exact formulation and its aliases returned no covering statement; the closest mathematical records concerned unrelated Bernoulli-tail problems.

Risk: the reduction is elementary once the 2026 example is written in terms of \(S_n\), so an unindexed note or application could contain an equivalent calculation. The claim is therefore limited to the precise phase diagram proved here rather than a broad novelty assertion about relative utility.

## Value
PASS. The source paper identifies a potentially misleading interpretation of observed relative utility but gives only an off-threshold probability-one limit. The exact formula and its phase transition distinguish three practically different regimes: exponential collapse to zero away from the treatment threshold, a nondegenerate half-probability exactly at the threshold, and a universal Gaussian transition when the true risk lies within \(O(n^{-1/2})\) of the threshold. This quantifies how quickly the interpretation pathology appears and pinpoints when finite-sample threshold uncertainty prevents the law-of-large-numbers conclusion from being representative.

Risk: the result is specialized to the constant-risk example and should not be generalized to heterogeneous clinical risk without additional work.

## Closest literature and limitations
The closest source is Hoessly, arXiv:2609.29133v1, especially Appendix A.4. Baker et al. (2009) and Baker (2019) provide the foundational relative-utility framework. The finding is a sharp characterization of one model used in the 2026 paper, not a replacement for the broader decision-curve literature.

Same-model review: passed. Independent audit: not yet performed.
