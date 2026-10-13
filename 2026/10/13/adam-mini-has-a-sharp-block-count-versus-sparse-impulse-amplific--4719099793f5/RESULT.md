# Adam-mini has a sharp block-count versus sparse-impulse amplification frontier
## Finding

Adam-mini compresses Adam's coordinatewise second-moment state by assigning one scalar second moment and one adaptive learning rate to each parameter block. For every block to which the source's scalar mean-square rule is applied,
\[
v_b
\leftarrow
(1-\beta_2)\operatorname{mean}(g_b^2)+\beta_2v_b.
\]

That memory compression has an exact sparse-impulse robustness cost.

Consider \(N\) coordinates partitioned into \(B\) nonempty blocks. Let a block have size \(d\). Assume
\[
0\le \beta_1,\beta_2<1,
\qquad
\epsilon>0,
\]
zero weight decay, zero initial moments, and zero gradients in the block before time \(\tau\). At time \(\tau\), apply an arbitrary nonzero impulse
\[
g\in\mathbb R^d.
\]
Define
\[
c_1(\tau)
=
\frac{1-\beta_1}{1-\beta_1^\tau},
\qquad
c_2(\tau)
=
\sqrt{\frac{1-\beta_2}{1-\beta_2^\tau}}.
\]

The source update then gives the exact block step
\[
\boxed{
\Delta_{\rm mini}
=
-\eta_\tau
\frac{c_1(\tau)g}
{c_2(\tau)\lVert g\rVert_2/\sqrt d+\epsilon}.
}
\]

For coordinatewise Adam with the same \(\eta_\tau\), moments, bias corrections, and \(\epsilon\), the \(j\)-th active coordinate has
\[
\Delta_{{\rm Adam},j}
=
-\eta_\tau
\frac{c_1(\tau)g_j}
{c_2(\tau)|g_j|+\epsilon}.
\]

Hence
\[
\frac{|\Delta_{{\rm mini},j}|}
{|\Delta_{{\rm Adam},j}|}
=
\frac{c_2(\tau)|g_j|+\epsilon}
{c_2(\tau)\lVert g\rVert_2/\sqrt d+\epsilon}.
\]
For every active coordinate,
\[
\boxed{
\frac{|\Delta_{{\rm mini},j}|}
{|\Delta_{{\rm Adam},j}|}
\le \sqrt d,
}
\]
and the constant is sharp: a one-coordinate impulse of growing amplitude makes the ratio tend to
\[
\sqrt d.
\]

More generally, if exactly \(k\) coordinates in the block are active with the same magnitude \(G>0\), then every active coordinate has ratio
\[
\boxed{
R_{d,k}(G)
=
\frac{c_2(\tau)G+\epsilon}
{c_2(\tau)G\sqrt{k/d}+\epsilon},
}
\]
which is increasing in \(G\) when \(k<d\) and satisfies
\[
\boxed{
\sup_{G>0}R_{d,k}(G)
=
\sqrt{\frac{d}{k}}.
}
\]

Now let the \(B\) block sizes be
\[
d_1,\ldots,d_B,
\qquad
\sum_{b=1}^B d_b=N.
\]
The sharp worst one-coordinate impulse amplification for that partition is
\[
\boxed{
A(d_1,\ldots,d_B)
=
\sqrt{\max_b d_b}.
}
\]
Therefore
\[
\boxed{
\min_{\substack{d_b\in\mathbb N\\ \sum_b d_b=N}}
A(d_1,\ldots,d_B)
=
\sqrt{\left\lceil\frac{N}{B}\right\rceil}.
}
\]
Balanced block sizes attain the minimum.

At the first step,
\[
c_1(1)=c_2(1)=1,
\]
so the exact block-count frontier is independent of both moment parameters. With positive \(\epsilon\), the displayed constants are sharp suprema as the impulse amplitude grows; with a vanishing denominator floor they are attained by the corresponding sparse impulses.

This gives an exact memory-versus-impulse tradeoff for Adam-mini's defining block-mean compression: using only \(B\) scalar second-moment states for \(N\) coordinates necessarily permits a worst sparse-coordinate response larger than coordinatewise Adam by
\[
\sqrt{\left\lceil\frac{N}{B}\right\rceil}.
\]

## Assumptions and scope

The theorem concerns blocks to which Adam-mini applies the scalar mean-square second moment. The source treats some architecture-specific blocks specially; those coordinatewise exceptions are outside this theorem.

The moment states start at zero and the block receives zero gradients before the analyzed impulse. This isolates the optimizer's response to a newly appearing sparse direction.

The comparison with coordinatewise Adam uses the same first-moment recursion, bias correction, base learning rate, and denominator floor.

The result is a sharp update-amplification theorem. It does not claim that a large coordinate update necessarily increases the training loss, nor that balanced partitions are optimal for Hessian conditioning or final model quality.

## Proof

Because all earlier gradients are zero, the first-moment state at time \(\tau\) is
\[
m_\tau=(1-\beta_1)g.
\]
After bias correction,
\[
\widehat m_\tau
=
c_1(\tau)g.
\]

For an Adam-mini block of size \(d\),
\[
v_\tau
=
(1-\beta_2)
\frac{\lVert g\rVert_2^2}{d}.
\]
The bias-corrected scalar second moment is therefore
\[
\widehat v_\tau
=
c_2(\tau)^2
\frac{\lVert g\rVert_2^2}{d}.
\]
Substitution into the source update proves
\[
\Delta_{\rm mini}
=
-\eta_\tau
\frac{c_1(\tau)g}
{c_2(\tau)\lVert g\rVert_2/\sqrt d+\epsilon}.
\]

Coordinatewise Adam instead has
\[
\widehat v_{\tau,j}
=
c_2(\tau)^2g_j^2,
\]
which gives the stated comparator.

For an active coordinate \(j\),
\[
|g_j|\le \lVert g\rVert_2.
\]
Thus
\[
c_2(\tau)|g_j|+\epsilon
\le
c_2(\tau)\lVert g\rVert_2+\epsilon
\le
\sqrt d
\left(
c_2(\tau)\lVert g\rVert_2/\sqrt d+\epsilon
\right),
\]
proving the \(\sqrt d\) upper bound. If \(g\) is one-sparse in coordinate \(j\), the ratio is
\[
\frac{c_2(\tau)G+\epsilon}
{c_2(\tau)G/\sqrt d+\epsilon}
\longrightarrow
\sqrt d
\]
as \(G\to\infty\), so the bound is sharp.

If \(k\) coordinates have equal magnitude \(G\), then
\[
\lVert g\rVert_2=G\sqrt k.
\]
Substitution gives \(R_{d,k}(G)\). Its derivative has the sign of
\[
1-\sqrt{k/d},
\]
so for \(k<d\) it increases strictly with \(G\), and its sharp supremum is \(\sqrt{d/k}\).

For a fixed partition, a one-coordinate impulse can be placed in any block. The preceding result shows that the worst sharp factor is therefore
\[
\sqrt{\max_b d_b}.
\]
Every partition of \(N\) coordinates into \(B\) nonempty blocks has
\[
\max_b d_b
\ge
\left\lceil\frac{N}{B}\right\rceil
\]
by the pigeonhole principle. A balanced partition has every block size at most
\[
\left\lceil\frac{N}{B}\right\rceil,
\]
so equality is attained.

## Verification

The accompanying `verify.py` reconstructs Adam-mini's scalar block second moment and coordinatewise Adam directly.

It checks the exact silent-history impulse formulas for several moment parameters and times, verifies the \(\sqrt{d/k}\) support law numerically at large amplitude, exhaustively checks the finite integer-partition minimax formula for small \(N\) and \(B\), and confirms that balanced partitions attain the lower bound.

The numerical calculations are transcription guards. The sharp constants and minimax frontier are proved analytically above.

## Relationship to prior work

The first public Adam-mini version already defines the block scalar second moment as the mean of the coordinatewise squared gradients. It also identifies an important sparse case: many embedding rows can be zero in a minibatch, so averaging over the whole embedding layer can absorb many zeros, produce highly biased learning rates, and cause training instability. The paper therefore excludes those blocks from the original averaging rule. Later revisions refine the architecture-specific partition and continue to report that overly coarse partitions can produce loss spikes.

Those observations motivate the present question, but they do not state the sharp coordinatewise amplification factor, its dependence on active support size, or the minimax lower bound imposed solely by compressing \(N\) coordinates into \(B\) block states.

Later work on spike-aware optimization documents the practical harm of gradient spikes and compares against memory-efficient methods including Adam-mini. A separate later blockwise optimizer augments Adam-mini's scalar block preconditioner with a rank-one anisotropic correction motivated by spiked curvature. These works motivate robustness and anisotropy, but the inspected public material does not provide the exact block-count versus sparse-impulse frontier above.

Focused published-record searches for Adam-mini sparse impulses, block-size amplification, blockwise scalar second moments, and memory-versus-robustness frontiers did not identify an implication-equivalent result.

## Limitations

The result is an impulse-response statement under a silent block history. Pre-existing second-moment mass can reduce the amplification.

The minimax partition is optimal only for this sparse-impulse criterion; Adam-mini's actual partition is chosen using Hessian structure, and a balanced partition can be inferior for the source's intended conditioning criterion.

The theorem compares raw adaptive updates, not objective values or training loss.

The later blockwise-rank-one paper was available through its abstract and publisher summary during the comparison; its complete publisher text was not used to assert whole-document noncoverage.

## References

1. Yushun Zhang, Congliang Chen, Ziniu Li, Tian Ding, Chenwei Wu, Diederik P. Kingma, Yinyu Ye, Zhi-Quan Luo, and Ruoyu Sun, “Adam-mini: Use Fewer Learning Rates To Gain More,” arXiv:2406.16793v1, first submitted 2024-06-24.
2. Yushun Zhang et al., “Adam-mini: Use Fewer Learning Rates To Gain More,” arXiv:2406.16793v7; ICLR 2025.
3. Tianjin Huang, Ziquan Zhu, Gaojie Jin, Lu Liu, Zhangyang Wang, and Shiwei Liu, “SPAM: Spike-Aware Adam with Momentum Reset for Stable LLM Training,” arXiv:2501.06842; ICLR 2025.
4. “BORA: Blockwise Orthogonal Rank-1 Adaptive Optimization,” ICASSP 2026, DOI `10.1109/ICASSP55912.2026.11464667`.
