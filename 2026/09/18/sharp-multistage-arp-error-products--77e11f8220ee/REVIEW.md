# Review

## Correctness

**PASS.** In ambient dimension \(d+1\), the final projection DPP is exactly a distribution over one omitted index. For \(K=I-zz^T\), principal minors give omission probability \(z_j^2\), and conditioning renormalizes those weights over unselected indices. The oblique error for omission \(j\) is exactly \(1/z_j^2\).

The explicit two-stage family therefore yields the closed mean
\[
\frac{(k+1)(p+1)}{1+kp\varepsilon^2},
\]
which approaches the source upper factor. In the arbitrary-stage construction, zero-padding preserves every previous basis block. The new conditional stage has one old omitted candidate plus \(k_r\) new candidates, and its conditional mean is exactly \((k_r+1)/D_j\). Taking \(\varepsilon_r\to0\) multiplies the preceding expectation by \(k_r+1\), proving full product sharpness by induction.

The orthogonal-CSS transfer was checked separately rather than inferred from oblique equality. For
\[
A_\delta=\operatorname{diag}(1,\ldots,1,\delta)[V,z]^T,
\]
a Gram-determinant height identity gives the exact ratio
\[
[z_j^2+\delta^2(1-z_j^2)]^{-1},
\]
which tends to the oblique ratio. This validates sharpness for the actual orthogonal projection objective. One-shot ARP on the same final subspace tends to \(d+1\), establishing the stated separation.

Adversarial checks included normalization of every conditional law, preservation of nested orthonormal blocks, the distinction between oblique and orthogonal objectives, and the order of the \(\varepsilon\) and \(\delta\) limits. The standalone artifact checks representative cases numerically; the theorem itself is analytic.

## Originality

**PASS, to the best of our knowledge.** The primary source arXiv:2609.20556 was inspected at its conditional-DPP construction, Theorems 3.1–3.3, appendix proof, and experiment discussion. It proves that a single conditional-stage factor \(p+1\) can be attained for a prescribed initial set, then proves the unconditional two-stage factor \((k+1)(p+1)\) and the general product upper bound. It does not establish unconditional multi-stage sharpness. The paper explicitly notes that experiments show MSARP comparable to one-shot ARP.

Searches combining conditional or projection DPPs, multistage or incremental column subset selection, volume sampling, adaptive randomized pivoting, and sharp or worst-case product bounds did not reveal the present result. Cortinovis–Kressner treats one-shot ARP; Epperly connects one-shot ARP with volume sampling; classical volume-sampling literature treats the one-shot \(k+1\) phenomenon. Deshpande et al.'s adaptive sampling is a different residual-resampling mechanism.

No specific inaccessible paper was identified as likely to contain the same construction. The main residual risk is simultaneous or not-yet-indexed follow-up to the very recent Grigori–Xue preprint. The originality claim is restricted to the full product sharpness, orthogonal-CSS transfer, rare-event explanation, and staged-versus-one-shot separation stated in RESULT.md.

## Value

**PASS.** The source product can be exponentially larger than the one-shot factor, especially for singleton stages, yet the reported experiments are benign. Whether the product is proof slack or a genuine worst-case cost is therefore a meaningful algorithmic question. The result resolves that distinction: the product is genuinely sharp, even for the actual CSS projection error, but sharpness is carried by vanishing-probability catastrophic omissions. The singleton construction gives an exponential worst-case separation from one-shot ARP on the same final matrix and subspace.

## Limitations

The result is worst-case and asymptotic in the construction parameters. It does not predict average behavior on natural matrix ensembles, optimize stage partitions for a given matrix, or provide a high-probability bound. The variance-divergence statement is explicit for the oblique surrogate; orthogonal-CSS sharpness concerns the mean after an additional small-singular-value limit. Repeated leading singular values are allowed. Very recent simultaneous work remains possible.

**Same-model review: passed. Independent audit: not yet performed.**
