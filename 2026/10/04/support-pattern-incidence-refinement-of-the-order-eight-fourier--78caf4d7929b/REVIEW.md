# Review

## Correctness
PASS. For each ordered support-set pair, realizability is equivalent to a three-part rank condition: a nonzero kernel, no time-coordinate functional identically zero on that kernel, and no desired Fourier-coordinate functional identically zero on that kernel. Over the infinite field \(\mathbb C\), finitely many proper hyperplanes cannot cover the kernel. The verifier computes all needed ranks exactly in \(\mathbb Q(\zeta_8)\), checks all \(65{,}025\) nonempty pairs, and recomputes the two finite orbit partitions. Packaged replay returns `VERIFY_OK`.

## Originality
PASS. Delvaux--Van Barel characterize rank deficiency and Hamming-weight uncertainty for prime-power Fourier matrices, and Bonami--Ghobber treat exact-support equality cases for other listed families. The closest source is Yang et al. (2023): their order-eight uncertainty diagram determines only whether a support-cardinality pair occurs, not how many actual support-set pairs realize it. Their size-level diagram is therefore the zero-versus-positive shadow of the claimed incidence matrix. Targeted published-finding corpus and web searches using support-pattern, incidence, orbit, uncertainty-diagram, and order-eight aliases did not locate the matrix, the total \(20{,}929\), or the orbit totals \(205\) and \(108\). Residual risk remains for an unindexed computational table.

## Value
PASS. Counting actual support-set pairs is a natural refinement of an uncertainty diagram: it distinguishes cardinality points that look identical at the size level but have very different geometric multiplicities. For example, \(I_8(2,4)=8\) whereas \(I_8(4,5)=2176\). The symmetry reduction to \(205\) affine classes and \(108\) Fourier-extended classes supplies a compact structural benchmark for future exact-support classifications at higher prime powers.

Same-model review: passed. Independent audit: not yet performed.
