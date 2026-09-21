# Four-step Sparre-Andersen persistence detects a pure fourth-order interaction

## Result

Let `A_1,...,A_4` be iid copies of any non-atomic positive random variable `A` supported in an interval `[a,b]` with

\[
0<a\le b<2a.
\]

Let `epsilon_1,...,epsilon_4` be fair Rademacher signs, independent of the amplitudes, and suppose the signs are **3-wise independent**. Put

\[
X_i=\epsilon_i A_i,\qquad S_k=\sum_{i=1}^kX_i,
\]

and define the only potentially nonzero higher-order sign interaction

\[
\theta=\mathbb E[\epsilon_1\epsilon_2\epsilon_3\epsilon_4]\in[-1,1].
\]

Then 3-wise independence already forces the complete sign law to be

\[
\boxed{
\Pr(\epsilon=e)=2^{-4}\left(1+\theta\prod_{i=1}^4e_i\right),
\qquad e\in\{-1,+1\}^4.
}
\]

Consequently `(X_1,...,X_4)` is exchangeable, each `X_i` has the same continuous distribution symmetric about zero, and **every proper subset of the four increments is iid**. Nevertheless its four-step strong persistence probability is

\[
\boxed{
\Pr(S_1>0,S_2>0,S_3>0,S_4>0)=\frac{35-5\theta}{128}.
}
\]

Thus the classical iid Sparre-Andersen value `35/128` is shifted linearly by a fourth-order interaction that is completely invisible to every one-, two-, and three-dimensional marginal.

The endpoints are explicit. Conditioning the signs on positive parity, `prod_i epsilon_i=+1`, gives `theta=+1` and

\[
\Pr(S_1>0,\ldots,S_4>0)=\frac{15}{64}.
\]

Conditioning on negative parity gives `theta=-1` and

\[
\Pr(S_1>0,\ldots,S_4>0)=\frac{5}{16}.
\]

These two exchangeable continuous laws have **identical every-proper-subset distributions** yet their persistence probabilities differ by `5/64`. Their equal mixture has fully independent signs, hence iid increments, and gives

\[
\frac12\left(\frac{15}{64}+\frac{5}{16}\right)
=\frac{35}{128}
=\frac1{4^4}{8\choose4},
\]

exactly the classical four-step Sparre-Andersen probability.

## Proof

### The sign law has only one remaining Fourier coefficient

Any probability mass function on `{-1,+1}^4` has the Walsh-Fourier expansion

\[
\Pr(\epsilon=e)
=2^{-4}\sum_{J\subseteq[4]}
\mathbb E\!\left[\prod_{j\in J}\epsilon_j\right]
\prod_{j\in J}e_j.
\]

Fairness and 3-wise independence make every nonempty coefficient with `|J|<=3` equal to zero. The only remaining coefficient is

\[
\theta=\mathbb E[\epsilon_1\epsilon_2\epsilon_3\epsilon_4],
\]

which proves the displayed sign law. Nonnegativity is equivalent to `|theta|<=1`. In particular, all proper sign marginals are iid Rademacher, while the complete law is automatically exchangeable. Independent iid amplitudes transfer these facts to the increments.

It is useful to write this law as the mixture

\[
P_\theta=\frac{1+\theta}{2}P_+ + \frac{1-\theta}{2}P_-,
\]

where `P_+` and `P_-` are the uniform sign laws conditional on product `+1` and `-1`, respectively.

### Positive-parity persistence

Because `b<2a`, any partial sum containing two positive amplitudes and one negative amplitude is strictly positive:

\[
A_i+A_j-A_k\ge2a-b>0,
\]

whereas one positive minus two negative amplitudes is strictly negative. Under `P_+`, persistence forces the first sign to be `+`; the four relevant even-parity patterns each have probability `1/8` under the full parity-conditioned law:

- `++++`: persistence occurs surely.
- `+--+`: the third partial sum is strictly negative, so it fails.
- `++--`: the first three partial sums are positive, and the final condition is `A_1+A_2>A_3+A_4`. The two sides are iid and non-atomic, so this has probability `1/2`.
- `+-+-`: write `D_1=A_1-A_2` and `D_2=A_3-A_4`. Persistence is equivalent to `D_1>0` and `D_1+D_2>0`. The variables `D_1,D_2` are iid, continuous and symmetric. The quadrant `D_1>0,D_2>0` contributes `1/4`. In the quadrant `D_1>0>D_2`, the positive variables `D_1` and `-D_2`, conditional on their signs, are iid and non-atomic, so `D_1>-D_2` has conditional probability `1/2`; this contributes `1/8`. Hence the conditional persistence probability for this sign pattern is `3/8`.

Therefore

\[
P_+(S_1>0,\ldots,S_4>0)
=\frac18\left(1+0+\frac12+\frac38\right)
=\frac{15}{64}.
\]

### Negative-parity persistence

Under `P_-`, the four odd-parity sign patterns beginning with `+` are `+++-`, `++-+`, `+-++`, and `+---`. The first two survive surely by `b<2a`; `+-++` survives exactly when `A_1>A_2`, with probability `1/2`; and `+---` has a strictly negative third partial sum. Hence

\[
P_-(S_1>0,\ldots,S_4>0)
=\frac18\left(1+1+\frac12+0\right)
=\frac5{16}.
\]

Mixing the two parity laws now gives

\[
\frac{1+\theta}{2}\frac{15}{64}
+\frac{1-\theta}{2}\frac5{16}
=\frac{35-5\theta}{128}.
\]

For `theta=0`, the 16 sign vectors are uniformly distributed, so all four increments are iid; the formula reduces to the Sparre-Andersen value `35/128`.

## Interpretation

At horizon four, fair 3-wise independent signs have exactly one degree of dependence left: the fourth-order Walsh coefficient `theta`. The persistence event has a nonzero projection onto that coefficient, of size `-5/128`. Hence complete knowledge of every proper-subset distribution cannot recover the path probability. In this family, the Sparre-Andersen value is recovered exactly when `theta=0`, which is also exactly when the four signs are fully independent.

This gives a sharp finite-horizon boundary for a modern form of Sparre-Andersen universality. Berger and Béthencourt show that exchangeability together with **global sign-invariance** suffices for the standard persistence conclusion. The construction here is exchangeable and has iid continuous symmetric marginals; more strongly, every proper subset is iid. What fails is precisely the global sign-invariance encoded in the surviving fourth-order interaction. Thus global sign-invariance cannot be replaced by any condition determined only from proper-subset laws at this horizon.

## Relation to prior work

Sparre Andersen's classical fluctuation theorem gives the universal persistence law for iid continuous symmetric increments. His 1953 work also developed fluctuation identities for symmetrically dependent variables. Berger and Béthencourt later gave a short modern treatment showing that the persistence conclusion extends to vectors that are exchangeable and sign-invariant. A 2026 refinement by Iľkovič and Yan studies sharp strong/weak persistence bounds within that same exchangeable, sign-invariant class.

Limited-independence random walks are established territory. Benjamini, Kozma and Romik constructed `k`-wise independent walks with behavior radically different from fully independent walks; their proof explicitly uses parity/product conditioning in blocks. Narayanan later showed that 3-wise independent walks can have anomalous maximal displacement. Thus neither the parity-conditioning gadget nor the general fact that limited independence can alter path behavior is new.

The contribution here is narrower: **to the best of our knowledge, the exact four-step persistence formula `(35-5 theta)/128` for the sole surviving fourth-order interaction, and the resulting pair of exchangeable continuous models that agree on every proper-subset law but have persistence `15/64` versus `5/16`, have not been stated in the checked literature.** The result isolates the missing information in Sparre-Andersen universality rather than supplying only an arbitrary dependent counterexample.

## Scientific limitations

- This is a finite-horizon four-step theorem, not an asymptotic persistence-rate result.
- The amplitude assumption `A in [a,b]` with `b<2a` is sufficient for the clean distribution-free constants; broader amplitude laws can produce different fourth-order sensitivities.
- The theorem characterizes the complete sign law under fair 3-wise independence, but it does not characterize all possible 3-wise independent real-valued increment laws without the independent sign-amplitude representation.
- The parity-conditioning mechanism and Walsh-Fourier description of limited independence are classical; novelty is claimed only for the persistence response and proper-marginal indistinguishability conclusion.
- Literature search cannot exclude an older equivalent observation under different terminology. In particular, older dependent fluctuation theory is broad; the checked sources did not reveal this exact limited-independence boundary.

## Reproducibility

`artifacts/verify_exact.py` exhaustively checks that both parity classes have exactly uniform one-, two-, and three-sign marginals and verifies the rational arithmetic for the two endpoint persistence values, their separation, the iid midpoint, and the affine `theta` formula. `artifacts/VERIFICATION.txt` records its output.

## References

1. E. Sparre Andersen, *On the fluctuations of sums of random variables*, Mathematica Scandinavica 1 (1953), 263-285. https://doi.org/10.7146/math.scand.a-10385
2. E. Sparre Andersen, *On sums of symmetrically dependent random variables*, Scandinavian Actuarial Journal 1953(sup1), 123-138. https://doi.org/10.1080/03461238.1953.10419466
3. I. Benjamini, G. Kozma, D. Romik, *Random walks with k-wise independent increments*, Electronic Communications in Probability 11 (2006), 100-107. https://doi.org/10.1214/ECP.v11-1201
4. S. Narayanan, *Three-wise independent random walks can be slightly unbounded*, Random Structures & Algorithms 61 (2022), 573-598. https://doi.org/10.1002/rsa.21075
5. Q. Berger, L. Béthencourt, *An application of Sparre Andersen's fluctuation theorem for exchangeable and sign-invariant random variables*, arXiv:2304.09031 (2023). https://arxiv.org/abs/2304.09031
6. D. Iľkovič, J. Yan, *Extremal persistence probabilities of exchangeable sign-invariant random variables*, arXiv:2609.05586 (2026). https://arxiv.org/abs/2609.05586

**Same-model review: passed. Independent audit: not yet performed.**
