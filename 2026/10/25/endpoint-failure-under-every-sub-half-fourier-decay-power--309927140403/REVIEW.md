# Review

## Correctness

**PASS.** The uniform point-selection lemma follows from Hoeffding's inequality on an \(O(N^4)\)-point grid and a deterministic derivative bound. With bump radius \(r_N=\varepsilon N^{-1-b}\), the exact Fourier transform formula gives the bound \((1+|\xi|)^{-\alpha}\sqrt{\log(2+|\xi|)}\), where \(\alpha=1/[2(1+b)]\). Choosing \(b\) so that the target \(\rho<\alpha\) absorbs the logarithm and yields the claimed power decay. The atom argument remains valid for \(\theta L\le k\le bL\), and the mixture estimates show weak-\(L^1\) quasi-norms growing like \(q^{m+1}\) while the \(H^1\) norms remain at most one.

## Originality

**PASS.** The closest primary source is Zhou, arXiv:2610.21197v1, whose Theorem 1.1 establishes the same endpoint failure with Fourier decay exponent \(1/8\). Remark 1.2 states that this exponent is not claimed optimal. The new construction improves the uniform approximation threshold to \(C\sqrt{\log N/N}\), chooses bump radius \(\varepsilon N^{-1-b}\), and retains a positive proportion of \(\log N\) scales \(\theta L\le k\le bL\). The resulting exponent \(\alpha=1/[2(1+b)]\) can be made larger than any prescribed \(\rho<1/2\). Targeted database and primary-literature searches found no same-object statement of this sub-half family; this is not treated as proof of exhaustive novelty.

The earlier paper of Seeger and Wright, arXiv:1007.4731, gives endpoint boundedness under additional dimensional and smoothing hypotheses. Grafakos et al., arXiv:1701.06637v1, records the motivating decay-only endpoint questions. Neither source covers the sub-half decay refinement.

## Value

**PASS.** Fourier-decay exponent is the central quantitative parameter in the endpoint question. Extending the counterexample from exponent \(1/8\) to every exponent below \(1/2\) materially narrows the unknown range and approaches the natural Plancherel threshold without claiming the endpoint itself.

## Limitations and residual risks

The theorem is one-dimensional, and the measure depends on the target exponent through the parameters \(a,b,q\). It does not include \(\rho=1/2\) or establish optimality beyond the sub-half range. The centers are chosen existentially rather than by an explicit deterministic algorithm. No exhaustive historical-priority claim is made.

Self-review: passed. Independent audit: not yet performed.
