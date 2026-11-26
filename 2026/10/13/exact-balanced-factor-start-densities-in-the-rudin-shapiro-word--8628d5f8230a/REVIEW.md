# Independent mathematical audit

## correctness

PASS

The coding satisfies a(2i)=a(i), a(2i+1)=(-1)^i a(i) with a(0)=1, so it represents overlapping 11 parity. In a positive scale-m block every nonempty prefix is positive; the A and B upper bounds 2H-1 and H, respectively, propagate under the two-step substitution with block-entry heights (0,H,2H,3H) and (0,H,2H,H). At height 2H the only hits are in the second and fourth subblocks, including the second subblock's right endpoint, giving T_(m+1)=(Q+T_m) union (3Q+T_m). A full window has signed mass S_X-P_X(j)+P_Y(j); complement and the two prefix-difference cases give the six stated admissible bigrams, while BA and DC give no hits. Primitivity gives limiting frequencies; the four internal-image pairs have frequency 1/8 and the boundary-pair equations force the other four to have the same frequency. Thus there are six contributing pairs each with 2^(k-1) offsets per 4^k positions, giving 3/(8*2^k). This covers j=0, the block endpoints, and k=1. An independently written digit-parity/prefix-sum check matched every predicted start for 0 <= i < 262144 and 1 <= k <= 8 (counts 49152, 24576, 12288, 6144, 3072, 1536, 768, 384); replay with python3 /workspace/branches/ce62b1a5-10db-471b-99bc-453ad619124f/independent_check.py. This is bounded corroboration, not the proof or a formal certificate.

## originality

PASS

The best-supported distinct finding is the joint all-scale occurrence-density formula and explicit start-location classification. The closest inspected results concern global cumulative sums, existence of more constrained factors, or distinct factor classes. None was shown to give this formula or classification; this is not a priority guarantee.

## value

PASS

For a canonical automatic word, the probability that a uniformly sampled start has zero discrepancy over a complete substitution scale is not given by Abelian complexity or the range of discrepancies. The theorem supplies that probability (including its exact inverse-square-root coefficient) and a finite digit rule locating every qualifying start. This resolves a natural occurrence question at all complete scales without extrapolation from a prefix.

The dated certificate retains the supplied scientific assessment, sources and limitations.
