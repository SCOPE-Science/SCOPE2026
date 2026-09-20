# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The exact capacity follows from independent direct transmission plus
two-hop block-Markov forwarding and from the two matching cutset inequalities
\(D+C_1\) and \(D+C_2\). The proposed decode-forward term is at most \(C_1\).
For both compress-forward terms, Shiu's relaxation and cancellation reduce the
compression constraint to
\[
I(\hat Y_r;Y_r\mid B,X_r)\le I(X_r;B,Z).
\]
Applying the input-free post-processing contraction coefficient conditionally
on \((B,X_r)\), then using
\(I(X_r;Z\mid B)\le C_2\), yields the stated
\(D+\eta C_2\) upper bound. The BSC specialization uses the standard
\(\eta=(1-2p)^2\), and the inequality is strict throughout
\(0<p\le q<1/2\).

Adversarial checks included the endpoint cases: at \(p=0\), \(p=1/2\), or
\(q=1/2\), the strict-gap argument can vanish, so these endpoints are excluded
from the BSC counterexample region. The theorem does not identify the exact
value of the proposed compress-forward optimization; it only needs a valid
upper bound.

## Originality

**PASS, to the best of our knowledge, with material priority risk.** The
closest source inspected in full is Shiu, arXiv:2609.18727, which gives the
single choice \(p=q=1/4\) and uses the BSC post-processing SDPI in its proof.
Ponniah, arXiv:2609.15709, supplies the characterization being refuted.
Targeted searches covered the motivating arXiv identifier and title, arbitrary
BSC crossover probabilities, relay counterexamples combined with contraction
coefficients/SDPI, and equivalent product/orthogonal relay formulations. No
source located stated the arbitrary-\(W_1,W_2\) contraction-coefficient
template or the full \(0<p\le q<1/2\) BSC region.

The exact capacity of the split channel, the cutset bound, block-Markov
relaying, and strong data-processing inequalities are established background
and are not claimed as new. The novelty claim is only the general counterexample
template and its quantitative consequences for the proposed 2026 formula.

No specific inaccessible paper was identified as especially likely to contain
the same theorem. The main residual uncertainty is folklore or a
near-simultaneous extension/revision, because the motivating counterexample is
very recent and the abstraction is concise.

## Value

**PASS.** The result changes the interpretation of the motivating example from
an isolated binary witness to a robust mechanism: whenever the first relay hop
has strict post-processing contraction and is no weaker than the second hop,
a sufficiently large noiseless direct component forces a gap. The BSC
corollary supplies an open two-parameter family and a simple \(p=q=1/8\)
instance with a certified gap about \(0.19969\) bits/use, larger than the
published \(p=q=1/4\) witness under the same bound.

## Limitations

The theorem is restricted to a split product relay architecture and to the
specific proposed DF/C-CF/U-CF characterization. The contraction bound may be
non-tight, so this is a sufficient counterexample criterion rather than a full
classification of failure. It does not challenge standard partial
decode-forward achievability or established relay-channel capacity results.
