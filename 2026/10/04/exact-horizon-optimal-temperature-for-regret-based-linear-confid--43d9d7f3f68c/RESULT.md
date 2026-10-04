# Exact horizon-optimal temperature for regret-based linear confidence sequences

## Finding
Fix \(\delta\in(0,1)\) and let \(A=\log(1/\delta)>0\). In the Gaussian sequential linear-regression online-to-confidence conversion of Kirschner, Krause, Meziu, and Mutny, Lemma 14 gives, for every fixed \(\beta\in(0,1)\), an anytime-valid confidence sequence whose quadratic threshold can be written
\[
R_\beta(B)=\frac{A}{\beta(1-\beta)}+\frac{B}{1-\beta}=\frac{A+B\beta}{\beta(1-\beta)},\qquad B\ge0.
\]
Suppose before observing the data one has deterministic regret envelopes \(b_t\ge0\) for \(1\le t\le T\), and set \(\bar b_T=\max_{1\le t\le T} b_t\). Among all single constant temperatures \(\beta\in(0,1)\) chosen before the data and held fixed for the confidence sequence, the unique minimizer of the worst-horizon threshold \(\max_{t\le T}R_\beta(b_t)=R_\beta(\bar b_T)\) is
\[
\beta_T^*=\frac{\sqrt A}{\sqrt A+\sqrt{A+\bar b_T}}=\frac{1}{1+\sqrt{1+\bar b_T/A}}.
\]
The exact optimized threshold is
\[
R_T^*=\left(\sqrt A+\sqrt{A+\bar b_T}\right)^2.
\]
The paper's sparse-linear-regression specialization uses \(\beta=1/2\), whose corresponding threshold is \(4A+2\bar b_T\). The exact improvement is
\[
R_{1/2}(\bar b_T)-R_T^*=\left(\sqrt{A+\bar b_T}-\sqrt A\right)^2.
\]
It is strictly positive for \(\bar b_T>0\). Moreover,
\[
\frac{R_T^*}{R_{1/2}(\bar b_T)}\longrightarrow\frac12
\qquad\text{as}\qquad \frac{\bar b_T}{A}\longrightarrow\infty.
\]
Thus the default \(\beta=1/2\) is optimal only in the zero-regret limit; for large deterministic regret envelopes, optimizing the already-present temperature asymptotically halves the dominant threshold.

## Assumptions and scope
The result is purely a tuning theorem for the fixed-temperature family already supplied by the source online-to-confidence conversion. It assumes the Gaussian sequential linear-regression setting and hypotheses of the cited Lemma 14, including a regret upper bound usable in that conversion. The quantities \(b_t\) and the horizon \(T\) are fixed before the observations used by the confidence sequence. The selected \(\beta_T^*\) is consequently fixed before the data and is not changed after observing outcomes.

The result does not claim validity for choosing \(\beta\) post hoc from the same data, nor for an adaptive sequence of temperatures. It also does not improve the regret envelope itself. Its conclusion is an exact minimax statement over a single constant \(\beta\) for the supplied deterministic horizon envelope.

## Proof
For fixed \(A>0\) and \(B\ge0\), write
\[
R_\beta(B)=\frac{A+B\beta}{\beta(1-\beta)}.
\]
Differentiation gives
\[
\frac{d}{d\beta}R_\beta(B)=\frac{B\beta^2+2A\beta-A}{\beta^2(1-\beta)^2}.
\]
The numerator \(q(\beta)=B\beta^2+2A\beta-A\) is strictly increasing on \((0,1)\), satisfies \(q(0)=-A<0\), and satisfies \(q(1)=A+B>0\). Hence there is exactly one critical point in \((0,1)\). Because \(R_\beta(B)\to\infty\) at both endpoints, that point is the unique global minimizer.

If \(B>0\), solving \(q(\beta)=0\) gives
\[
\beta^*=\frac{-A+\sqrt{A(A+B)}}{B}=\frac{\sqrt A}{\sqrt A+\sqrt{A+B}}.
\]
For \(B=0\), the same expression gives \(\beta^*=1/2\) by direct substitution. Substituting the optimizer into \(R_\beta(B)\) yields
\[
\min_{0<\beta<1}R_\beta(B)=\left(\sqrt A+\sqrt{A+B}\right)^2.
\]
Since \(R_\beta(B)\) is increasing in \(B\) for each fixed \(\beta\), the worst threshold over \(t\le T\) is attained at \(B=\bar b_T\). This proves the optimizer and the worst-horizon value.

At \(\beta=1/2\),
\[
R_{1/2}(B)=4A+2B.
\]
Subtracting the optimum gives
\[
4A+2B-\left(\sqrt A+\sqrt{A+B}\right)^2
=\left(\sqrt{A+B}-\sqrt A\right)^2.
\]
Finally, divide numerator and denominator by \(B\) to obtain the asymptotic ratio \(1/2\) as \(B/A\to\infty\).

Each fixed \(\beta\in(0,1)\) in the source lemma has the same anytime coverage statement. Selecting \(\beta_T^*\) from the pre-data deterministic pair \((A,\bar b_T)\) therefore amounts only to choosing one member of that valid family before observing the data; no post-selection argument is needed.

## Verification
A standalone script checks the derivative root, the exact minimum, the exact gap identity, dense-grid minimality over a broad range of \((A,B)\), and the limiting ratio. It prints `VERIFY_OK` when all checks pass.

The proof itself is symbolic and does not depend on finite numerical enumeration. The numerical checks are regression tests for the algebra, not substitutes for the derivative argument.

## Relationship to prior work
Kirschner, Krause, Meziu, and Mutny introduce tempered likelihood-ratio confidence sets and state the Gaussian online-to-confidence conversion for every fixed \(\beta\in(0,1)\). Their sparse-linear-regression application specializes the free parameter to \(\beta=1/2\). The calculation above retains that same valid family and solves the exact finite-horizon constant-temperature tuning problem induced by a deterministic regret envelope.

Clerico, Flynn, Kotłowski, and Neu independently develop a closely related regret-based framework for generalized-linear-model confidence sequences and explicitly note substantial overlap with the sequential-likelihood-mixing work. Their displayed deterministic-forecaster linear-Gaussian width has the same \(2B+4\log(1/\delta)\) coefficient pattern as the \(\beta=1/2\) specialization, but the inspected paper does not formulate or solve the temperature minimization above.

Abbasi-Yadkori, Pál, and Szepesvári introduced an earlier online-to-confidence-set conversion for linear prediction with martingale noise. Its theorem has a different regret-dependent boundary and does not provide the tempered fixed-\(\beta\) family optimized here.

## Limitations
The result optimizes only one constant temperature against a deterministic pre-data horizon envelope. It does not establish that a data-dependent, time-varying, mixture-over-temperatures, or otherwise adaptive procedure cannot improve further. It also does not claim that the displayed optimization is historically absent under every equivalent notation; the literature comparison covered the primary source, a close contemporaneous framework, the classical online-to-confidence precursor, and targeted database searches.

The improvement concerns the threshold delivered by this particular conversion. It does not imply an information-theoretic lower bound for all confidence sequences in sequential linear regression.

## References
1. J. Kirschner, A. Krause, M. Meziu, and M. Mutny, *Confidence Estimation via Sequential Likelihood Mixing*, arXiv:2502.14689, first public version 2025-02-20.
2. E. Clerico, H. Flynn, W. Kotłowski, and G. Neu, *Confidence Sequences for Generalized Linear Models via Regret Analysis*, arXiv:2504.16555, first public version 2025-04-23.
3. Y. Abbasi-Yadkori, D. Pál, and C. Szepesvári, *Online-to-Confidence-Set Conversions and Application to Sparse Stochastic Bandits*, Proceedings of Machine Learning Research 22:1--9, 2012.
