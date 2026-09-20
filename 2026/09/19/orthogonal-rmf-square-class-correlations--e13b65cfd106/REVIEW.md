# Review: universal square-class correlations in orthogonal compact-group random multiplicative functions

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The argument reduces to standard compact-group character theory plus an elementary arithmetic summation.

The local identity
\[
\mathbb E[h_k\overline{h_l}]
=\dim\operatorname{Hom}_G(\operatorname{Sym}^lV,\operatorname{Sym}^kV)
\]
is immediate from Haar character orthogonality. For orthogonal Frobenius--Schur type, a nonzero invariant quadratic tensor \(Q\in(\operatorname{Sym}^2V)^G\) exists. Multiplication by \(Q\) is injective in the symmetric algebra, and compactness gives a \(G\)-stable complement. Iteration therefore places a common direct-summand ladder in symmetric powers of the same parity. For \(\dim V\ge2\), the dimension difference between consecutive terms in the ladder is positive, so none of the complementary summands used in the lower bound vanishes. The one-dimensional case is separated because this dimension argument degenerates there; a nontrivial one-dimensional orthogonal representation is quadratic and gives the exact parity kernel stated in the result.

The passage from local to global covariance uses only independence at distinct primes. For a common square class \(m=ru^2,n=rv^2\), the local bound multiplies to \(\tau(\gcd(u,v))\). Character inner products are nonnegative integers, so omitting all other pairs from the second-moment double sum is legitimate. The divisor identity
\[
\sum_{u,v\le N}\tau(\gcd(u,v))=\sum_{a\le N}\lfloor N/a\rfloor^2
\]
and the unique decomposition \(t=ra^2\) with \(r\) squarefree reduce the lower bound exactly to
\[
\sum_{t\le x}\lfloor\sqrt{x/t}\rfloor^2=x\log x+O(x).
\]
The mean bound follows because powers of the invariant quadratic tensor give a nonzero invariant in every even symmetric power, while all trivial-representation multiplicities are nonnegative. Jensen's inequality is used only when \(2q\ge1\), explaining the stated restriction \(q\ge1/2\).

No step requires a probabilistic independence assertion beyond the primewise independence built into the compact-group model. The theorem is not extended to the trivial representation, and no claim is made for \(q<1/2\).

## Originality

**PASS, to the best of our knowledge.** The primary recent source, Leung's arXiv:2609.20460v1, was inspected through its definition, compact-group examples, and Section 7. It proves the centered low-moment theorem for unitary and symplectic type, identifies \(\mathbb E h_2=1\) in orthogonal type, and gives an exact symmetric-square Sato--Tate computation in Proposition 7.1. That proposition produces the same \(x\log x\) phenomenon for one specific three-dimensional model, but the paper does not formulate a general orthogonal-type covariance theorem or derive an all-orthogonal lower bound.

Searches for equivalent formulations involving orthogonal compact-group random multiplicative functions, Frobenius--Schur indicators, square-class or squarefree-kernel correlations, symmetric-power character covariance, and even symmetric-power Sato--Tate random multiplicative functions did not locate a prior result implying the theorem. Harper's 2020 theorem covers classical Steinhaus and Rademacher models rather than this universal automorphic compact-group statement. The invariant-quadratic-tensor and semisimplicity ingredients are classical and are not presented as new; the claimed contribution is their use to force the explicit local correlation ladder and the global number-theoretic moment obstruction.

No inaccessible paper was identified whose title or available metadata specifically suggests the same universal square-class correlation result. The main residual risk is contemporaneous or not-yet-indexed work because the motivating preprint was submitted on 17 September 2026.

## Value

**PASS.** The result turns a single exact orthogonal example into a structural theorem for the entire orthogonal Frobenius--Schur class. It shows that prime-square centering is not merely a technical hypothesis needed by the existing proof: a quadratic invariant creates repeated same-parity constituents in every symmetric power, producing square-class correlations strong enough to force at least \(x\log x\) second-moment growth in every dimension at least two. It also applies at once to all even symmetric-power Sato--Tate models, not only the symmetric-square case.

The low-moment consequence is useful even without a matching upper bound: for every fixed \(q\in[1/2,1)\), the nonzero square mean alone forces \(x^q\) scale, separating orthogonal models from the centered scale by a divergent \((\log\log x)^{q/2}\) factor. The result also identifies a reusable representation-theoretic mechanism for analyzing other compact-group Euler-product models.

## Limitations

The general result is one-sided. It does not determine exact constants or upper bounds for \(d\ge2\), does not address \(q<1/2\), and does not classify additional correlations that may make a particular orthogonal model larger than the universal floor. Originality remains to the best of our knowledge, with elevated residual uncertainty from the recency of the motivating preprint. No independent validation or formal proof-assistant verification has been performed.
