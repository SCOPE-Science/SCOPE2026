# A sharp random-bit threshold for invariant bias in two-level quantized gradient descent

## Finding

Consider gradient descent for \(f_b(x)=\tfrac12(x-b)^2\) with \(0<b<1\), a fixed learning rate \(0<\eta<1\), and an iterate stored on the two-level grid \(\{0,1\}\). Compute the pre-rounded update \(y=(1-\eta)x+\eta b\) exactly. At every step use fresh independent randomness to round \(y\) to one with probability \(\lfloor Ky\rfloor/K\), and to zero otherwise, where \(K=2^r\) and \(r\) is a nonnegative integer. This is the floor-probability (StochasticA-style) finite-random-bit rule on one unit quantization cell.

Put \(v=K\eta\). The iteration has a unique invariant law \(\pi_{K,\eta,b}\) and converges to it from either grid point. Its mass at one is exactly
\[
\pi_{K,\eta,b}(\{1\})=
\frac{\lfloor vb\rfloor}{\lfloor vb\rfloor+\lceil v(1-b)\rceil}.
\]
The **sharp uniform stationary-law error** relative to ideal, probability-untruncated stochastic rounding is
\[
\boxed{\sup_{0<b<1}\|\pi_{K,\eta,b}-\operatorname{Bernoulli}(b)\|_{\mathrm{TV}}
=\min\{1,(K\eta)^{-1}\}.}
\]
In particular, whenever \(K\eta\le1\), the finite-bit chain is absorbed at zero for every \(0<b<1\); when \(K\eta>1\), the supremum is approached by \(b\uparrow(K\eta)^{-1}\). Thus, along any family of stepsizes \(\eta\downarrow0\) and bit counts \(r=r(\eta)\), its invariant laws approximate their ideal counterparts **uniformly in the target** if and only if \(2^{r(\eta)}\eta\to\infty\).

Equivalently, to achieve a prescribed worst-target stationary total-variation error of at most \(\varepsilon\in(0,1)\), the exact bit requirement is \(2^r\eta\ge\varepsilon^{-1}\), or \(r\ge\lceil\log_2(1/(\varepsilon\eta))\rceil\). These are sharp thresholds, not merely sufficient bounds.

## Assumptions and scope

All pre-rounding arithmetic is exact. Only the final conversion to the two-level unit grid is random. The random integer used at each step is independent and uniform on \(\{0,\ldots,K-1\}\). The upward probability \(\lfloor Ky\rfloor/K\) is implemented by accepting an upward step when \(\lfloor Ky\rfloor+R\ge K\). The target \(b\) ranges over the open interval \((0,1)\), the learning rate \(\eta\) over \((0,1)\), and \(K\) over positive powers of two, including \(K=1\). The supremum in the theorem is not necessarily attained by an interior target.

The ideal comparator uses independent probability-exact rounding with upward probability \(y\). Its transition probabilities are \(\eta b\) and \(\eta(1-b)\); it has unique invariant law \(\operatorname{Bernoulli}(b)\), independent of \(\eta\). This comparator does not concentrate at the unconstrained real minimizer \(b\); the theorem measures **additional distortion** caused by quantizing the random threshold, not the inherent error of storing an iterate on a binary grid.

## Proof

**Step 1: Exact two-state transition.** At \(x=0\), the pre-rounded update is \(y=\eta b\), so the jump probability to one is \(p=\lfloor vb\rfloor/K\). At \(x=1\), the pre-rounded update is \(y=1-\eta(1-b)\); the jump probability to zero is
\[
q=1-\frac{\lfloor K-v(1-b)\rfloor}{K}=
\frac{\lceil v(1-b)\rceil}{K}.
\]
Since \(0<v<K\), one has \(0\le p<1\), \(0<q\le1\), and \(0<p+q\le1\). The last inequality also follows because \(\lfloor vb\rfloor+\lceil v(1-b)\rceil\) is at most \(\lceil v\rceil\le K\). (Here \(v<K\) follows from \(\eta<1\).) The transition matrix, in state order \(0,1\), is
\[
P=\begin{pmatrix}1-p&p\\q&1-q\end{pmatrix}.
\]
Since \(q>0\), the unique stationary mass at one is \(\pi_1=p/(p+q)\). The other eigenvalue is \(\lambda=1-p-q\in[0,1)\); for any initial probability \(u_0\) of state one,
\[
\Pr\{X_n=1\}=\pi_1+(u_0-\pi_1)\lambda^n,
\]
which proves convergence even when state zero is absorbing.

**Step 2: The error is one-sided.** Write \(v=K\eta\), \(a=\lfloor vb\rfloor\), and \(c=\lceil v(1-b)\rceil\). Because \(a\le vb\) and \(c\ge v(1-b)\), direct cross multiplication yields \(a/(a+c)\le b\); equality is permitted at lattice-aligned parameters. Both laws are supported on two points, hence their total-variation distance is exactly \(b-a/(a+c)\).

**Step 3: Exact upper bound.** If \(v\le1\), then \(a=0\) for all \(0<b<1\), so \(\pi_1=0\) and the error is \(b<1\). Its supremum is one.

Suppose \(v>1\), and decompose \(v=n+\theta\) with \(n=\lfloor v\rfloor\ge1\) and \(0\le\theta<1\). Write \(vb=k+u\) with \(k=\lfloor vb\rfloor\) and \(0\le u<1\). Then
\[
a+c=k+\lceil n+\theta-k-u\rceil
=\begin{cases}n+1,&u<\theta,\\ n,&u\ge\theta.\end{cases}
\]
For \(u<\theta\), necessarily \(\theta>0\) and \(k\le n\). The error equals
\[
\frac{k+u}{v}-\frac{k}{n+1}
=\frac{k(1-\theta)+(n+1)u}{v(n+1)}
<\frac{n+\theta}{v(n+1)}=\frac1{n+1}<\frac1v.
\]
For \(u\ge\theta\), \(k\le n-1\) unless \(b=1\) (excluded), and
\[
\frac{k+u}{v}-\frac{k}{n}
=\frac{nu-k\theta}{nv}<\frac1v,
\]
since \(u<1\) and \(k\theta\ge0\). This proves \(\sup_b\|\pi-\operatorname{Bernoulli}(b)\|_{\mathrm{TV}}\le1/v\).

**Step 4: Sharpness and bit budget.** Whenever \(v>1\), choose \(0<b<1/v\) and let \(b\uparrow1/v\). Then \(a=\lfloor vb\rfloor=0\), so \(\pi_1=0\) and the error equals \(b\uparrow1/v\). For \(v\le1\), take \(b\uparrow1\). Combining the lower and upper bounds gives the stated minimax identity. Applied to a sequence of positive stepsizes and integer bit counts, the identity proves uniform convergence if and only if \(K\eta\to\infty\); the exact prescribed-tolerance condition and its logarithmic restatement follow immediately. \(\square\)

## Verification

A standalone, dependency-free exact-rational test is included as `verify.py`. Invoke `python3 verify.py` from the extracted package directory. It separately computes the transition entries, stationary mass, finite-time spectral identity, and the claimed minimax upper bound over a grid of rational parameters. It checks the sharpness approach to the worst-case boundary and prints the number of successful cases. The program is finite corroboration, not a proof of the universal supremum; the universal proof is the case split above.

## Relationship to prior work

The first public release of El Arar, Fasi, Filip and Mikaitis's 2026 survey describes ideal rounding and the floor-probability StochasticA scheme, but does not give the stationary-law minimax distortion or the exact random-bit-versus-stepsize criterion for this two-level gradient-descent model. Fitzgibbon and Felix (2025) derive finite-random-bit rounding biases and remedies; their averaged single-rounding bias calculations do not imply the invariant law or its worst-target sharp constant. El Arar et al. (2024/2025) give finite-precision rounding error models and bounds for numerical algorithms, including finite-horizon gradient descent experiments, not the exact stationary-law transition. Li et al. (2017) investigate invariant laws of ideally stochastically rounded quantized training and prove stepsize-insensitive stationary limits under nondegenerate gradient-noise conditions; the present deterministic-gradient, biased probability-truncation model is not covered by that theorem. Xia et al. (2023) analyze stochastic fixed-point rounding and gradient descent under different rounding hypotheses rather than quantized random-threshold bits. The classical two-state Markov stationary balance identity is used, not asserted to be new.

The result is deliberately a natural minimal-cell classification; it does not establish global behavior on grids with three or more levels or universality across alternative stochastic rounding variants.

## Limitations

The claim assumes a noiseless quadratic and exact computation of the pre-rounding update; it excludes rounding in gradient evaluation, correlated random bits, data-dependent stepsizes, different rounding probability corrections, and higher-dimensional or nonuniform grids. The binary-grid ideal comparator has nonzero discretization error, distinct from the additional finite-randomness effect quantified here. Results for the output of an arbitrary deep learning implementation are not implied. The originality comparison does not prove global priority: specialized older finite-state quantization papers outside the inspected sources might contain an equivalent bound.

## References

1. El-Mehdi El Arar, Massimiliano Fasi, Silviu-Ioan Filip, Mantas Mikaitis. *What is New in Stochastic Rounding: a Survey on Theory, Hardware, and Applications*. arXiv:2603.06060 (first publicly posted 2026-03-06), §§2–4. https://arxiv.org/abs/2603.06060
2. Andrew Fitzgibbon, Stephen Felix. *On Stochastic Rounding with Few Random Bits*. arXiv:2504.20634 (2025), §§II–IV and Appendix A. https://arxiv.org/abs/2504.20634
3. El-Mehdi El Arar, Massimiliano Fasi, Silviu-Ioan Filip, Mantas Mikaitis. *Probabilistic error analysis of limited-precision stochastic rounding*. arXiv:2408.03069 (first posted 2024), Definition 4, Lemma 5, §§4–6. https://arxiv.org/abs/2408.03069
4. Hao Li, Soham De, Zheng Xu, Christoph Studer, Hanan Samet, Tom Goldstein. *Training Quantized Nets: A Deeper Understanding*. arXiv:1706.02379 (2017), Theorem 5 and Appendix F. https://arxiv.org/abs/1706.02379
5. Lu Xia, Michiel E. Hochstenbach, Stefano Massei. *On the Convergence of the Gradient Descent Method with Stochastic Fixed-point Rounding Errors under the Polyak–Łojasiewicz Inequality*. arXiv:2301.09511 (2023), §§1 and 4. https://arxiv.org/abs/2301.09511
