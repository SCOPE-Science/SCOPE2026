# Exact finite-block codebooks for a proper-colouring noise channel

## Finding

Let \(q\ge2\), let the input and noise alphabets be \(\mathbb Z_q\), and let the noise block of length \(n\) range over all words \(z\in\mathbb Z_q^n\) satisfying \(z_i\ne z_{i+1}\) for \(1\le i<n\). The channel output is \(Y=X+Z\pmod q\), with the noise word unknown and chosen adversarially from this set. Let \(M_q(n)\) be the maximum size of a zero-error codebook. For every integer \(n\ge1\),

\[
M_q(n)=\begin{cases}
2^{n-1},&q=2,\\
1,&q\ge3.
\end{cases}
\]

When \(q=2\), every maximum codebook contains exactly one word from each bitwise-complement pair \(\{x,\bar x\}\). There are exactly \(2^{2^{n-1}}\) such maximum codebooks. When \(q\ge3\), the maximum codebooks are precisely the singleton subsets, of which there are \(q^n\).

## Assumptions and scope

- The alphabet is the additive group \(\mathbb Z_q\), where \(q\ge2\) is an integer. All additions and subtractions in the channel are modulo \(q\).
- The allowed length-\(n\) noise words are exactly \(N_q(n)=\{z\in\mathbb Z_q^n:z_i\ne z_{i+1}\text{ for }1\le i<n\}\). No probability distribution is assigned to these words.
- The initial noise symbol is unknown; every word in \(N_q(n)\) is possible. A codebook \(C\subseteq\mathbb Z_q^n\) is zero-error when the output sets \(\mathcal Y(x)=\{x+z:z\in N_q(n)\}\) are pairwise disjoint for distinct \(x\in C\).
- The result concerns finite-block worst-case zero-error coding for this specific finite-state noise constraint. It does not assert a formula for stochastic channel capacity.

## Proof

First suppose \(q=2\). The condition \(z_i\ne z_{i+1}\) forces the noise word to alternate, so \(N_2(n)=\{a,\bar a\}\), where \(a=(0,1,0,1,\ldots)\) truncated to length \(n\), and \(\bar a=a+\mathbf 1\) is its bitwise complement. For every input word \(x\),

\[
\mathcal Y(x)=\{x+a,\ x+\bar a\}=\{x+a,\ \overline{x+a}\}.
\]

Thus the two possible outputs of \(x\) form one complement pair. If two distinct words \(x,x'\) share an output, then for some \(z,z'\in N_2(n)\), \(x+z=x'+z'\), hence \(x-x'=z'-z\in\{0,\mathbf 1\}\). Since \(x\ne x'\), this forces \(x'=\bar x\). Conversely, complementary inputs have identical output sets. Therefore a binary zero-error codebook contains at most one member of each complement pair. The \(2^n\) binary words partition into \(2^{n-1}\) such pairs, and choosing one word from each pair gives a zero-error codebook of that size. Hence \(M_2(n)=2^{n-1}\), and every maximum codebook must choose exactly one member of every pair. Each pair contributes two independent choices, so the number of maximum codebooks is \(2^{2^{n-1}}\).

Now suppose \(q\ge3\). Fix any target difference word \(d\in\mathbb Z_q^n\). Choose \(z'_1\in\mathbb Z_q\) arbitrarily and set \(z_1=d_1+z'_1\). Given \(z'_i\), choose \(z'_{i+1}\) outside

\[
\{z'_i,\ z'_i+d_i-d_{i+1}\}.
\]

At most two symbols are excluded, so such a choice exists because \(q\ge3\). Set \(z_{i+1}=d_{i+1}+z'_{i+1}\). The first exclusion guarantees \(z'_i\ne z'_{i+1}\); the second guarantees \(z_i\ne z_{i+1}\). Thus both \(z,z'\) belong to \(N_q(n)\), and by construction \(z-z'=d\). Every difference of two input words is therefore the difference of two admissible noise words. For any distinct inputs \(x,x'\), apply this construction to \(d=x'-x\); then \(x+z=x'+z'\), so the two inputs are confusable. No zero-error codebook can contain two distinct words, giving \(M_q(n)=1\). Every singleton is optimal, and there are \(q^n\) singleton codebooks.

## Verification

The all-length claims follow from the proof above and do not depend on finite enumeration. The included dependency-free script `verify.py` checks the binary complement-pair classification for \(1\le n\le5\) and checks difference coverage for \(q\in\{3,4,5\}\) and \(1\le n\le4\). Those bounded checks are sanity checks only; they are not used as proof of the universal statements.

## Relationship to prior work

Saberi, Farokhi, and Nair give a general coupled-graph criterion for when a finite-state additive-noise channel has zero zero-error capacity, and show that its zero-error feedback capacity is either zero or the input-alphabet logarithm minus the noise shift's topological entropy [1]. Their Example 1 treats binary-valued noise with no consecutive \(1\)'s, which is a different constraint from allowing all \(q\) noise symbols while forbidding adjacent equal symbols. Their general criterion implies the singleton-codebook branch once the difference-coverage argument above is established, but it does not state the exact finite-block binary optimum, classify every maximum binary codebook, or count those codebooks. The later paper [2] develops related finite-state capacity and run-length-limited examples but likewise does not give this finite-block extremizer census. The contribution here is the exact finite-block codebook classification, not a new general capacity theorem.

## Limitations

The noise is treated adversarially through its allowed finite words; no stochastic law, expected error, or probabilistic capacity is claimed. The general zero-capacity criterion for finite-state channels is prior work, and the searches described in the review are not a proof of global novelty. Independent audit and independent validation have not been performed.

## References

1. A. Saberi, F. Farokhi, and G. N. Nair, “An Explicit Formula for the Zero-Error Feedback Capacity of a Class of Finite-State Additive Noise Channels,” arXiv:2006.00892v1, first posted 2020-05-29. https://arxiv.org/abs/2006.00892
2. A. Saberi, F. Farokhi, and G. N. Nair, “Zero-Error Feedback Capacity for Bounded Stabilization and Finite-State Additive Noise Channels,” arXiv:2108.03874v1, first posted 2021-08-09. https://arxiv.org/abs/2108.03874
