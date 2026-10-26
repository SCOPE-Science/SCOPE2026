# Exact finite-field variance of idempotents in random perfect evolution algebras

## Finding

Let \(q\) be a prime power, \(n\geq 2\), and let \(M\) be uniform in \(\operatorname{GL}_n(\mathbb F_q)\). Form the perfect evolution algebra with natural basis \(e_1,\ldots,e_n\) whose idempotent equation, in column coordinates, is
\[
 x=Mx^{[2]},\qquad x^{[2]}=(x_1^2,\ldots,x_n^2)^T.
\]
Let \(N=N(M)\) count **nonzero** idempotents over \(\mathbb F_q\). Then \(\mathbb E[N]=1\) and
\[
\boxed{\operatorname{Var}(N)=
\begin{cases}
 1,&\operatorname{char}(\mathbb F_q)=2,\\[3pt]
 1-\displaystyle\frac{(q-1)\big((2q-1)^n-2q^n+1\big)}{2(q^n-1)(q^n-q)},&\operatorname{char}(\mathbb F_q)\ne2.
\end{cases}}
\]
For every odd prime power \(q\) and \(n\ge2\), the variance is strictly smaller than \(1\). At fixed \(n\ge2\), the odd-characteristic variance defect is
\[
1-\operatorname{Var}(N)=(2^{n-1}-1)q^{1-n}+O_n(q^{-n})
\]
as \(q\) grows through odd prime powers. For \(n=2\), the exact odd-characteristic value simplifies to \((q^2+1)/(q(q+1))\); for example \(q=3\) gives \(5/6\). For \(n=1\), excluded from the main formula, \(N=1\) identically and its variance is \(0\).

## Assumptions and scope

The structure matrix is chosen *uniformly from the invertible matrices*, not from all matrices and not from isomorphism classes of algebras. A transpose convention for structure constants does not alter this uniform distribution. Each point of \(\mathbb F_q^n\) is counted once: no algebraic multiplicities or points over extension fields enter. The zero vector is always an idempotent but is excluded from \(N\). The formula covers all finite fields, including non-prime fields; no assumption of generic separability is needed.

## Proof

Put \(V=\mathbb F_q^n\), \(s(x)=x^{[2]}\), and \(Q=q^n\). For each nonzero \(x\), also \(s(x)\ne0\). The uniform invertible linear map sends a fixed nonzero vector uniformly to the \(Q-1\) nonzero vectors. Thus \(\Pr(Ms(x)=x)=1/(Q-1)\), and \(\mathbb E[N]=1\).

To count the second factorial moment, consider **ordered** pairs \((x,y)\) of distinct nonzero vectors that could both be idempotents. They cannot be collinear: if \(y=tx\) with \(t\in\mathbb F_q^\times\) and \(t\ne1\), then \(Ms(y)=t^2Ms(x)=t^2x\) cannot equal \(y=tx\). If \(x,y\) are independent but \(s(x),s(y)\) are dependent, invertibility of \(M\) likewise makes simultaneous idempotence impossible. If both pairs are independent, uniform transitivity of \(\operatorname{GL}_n(\mathbb F_q)\) on ordered independent pairs shows that the simultaneous probability is
\[
\frac1{(Q-1)(Q-q)}.
\]
Hence, writing \(B\) for the number of ordered independent pairs \((x,y)\) with dependent squares,
\[
\mathbb E[N(N-1)]=1-\frac{B}{(Q-1)(Q-q)}.
\]
As \(\mathbb E[N]=1\), the variance equals this factorial moment.

If \(q\) is even, Frobenius squaring is an automorphism of \(\mathbb F_q\); applying its inverse to a putative scalar relation between \(s(x),s(y)\) yields a scalar relation between \(x,y\). Thus \(B=0\).

Suppose \(q\) is odd. Fix \(x\ne0\) with exactly \(r\ge1\) nonzero coordinates. For \(s(y)=cs(x)\) with \(y\ne0\), the scalar \(c\in\mathbb F_q^\times\) must be a square, giving exactly \((q-1)/2\) possibilities. For each such \(c\), the \(r\) active coordinates of \(y\) have independent signs relative to a chosen square root of \(c\), and all inactive coordinates vanish. Exactly two of the \(2^r\) sign patterns make \(y\) a scalar multiple of \(x\). Therefore the number of *independent* \(y\) with dependent squares is \((q-1)(2^r-2)/2\).

There are \(\binom nr(q-1)^r\) choices of \(x\) with support of size \(r\). Summing and using the binomial theorem yields
\[
\begin{aligned}
B&=\frac{q-1}{2}\sum_{r=1}^n\binom nr(q-1)^r(2^r-2)\\
 &=\frac{q-1}{2}\big((2q-1)^n-2q^n+1\big).
\end{aligned}
\]
Substitution into the factorial-moment identity gives the displayed theorem. The sum has strictly positive contributions for \(r=2\), so \(B>0\) for odd \(q\), \(n\ge2\); independent vectors with disjoint singleton supports show \(B<(Q-1)(Q-q)\). The asymptotic formula follows by expanding the numerator and denominator for fixed \(n\).

## Verification

The accompanying standalone `verify.py` enumerates all invertible structure matrices and all vectors for ten small cases, checks the exact rational mean and variance, and prints each empirical distribution. It covers prime fields \(\mathbb F_2,\mathbb F_3,\mathbb F_5,\mathbb F_7\), the extension field \(\mathbb F_4\), dimensions \(n=1,2,3,4\), and the excluded \(n=1\) boundary. Its expected success marker is `VERIFY_OK`. Finite enumeration is corroboration only: the proof above establishes all quantifiers.

## Relationship to prior work

Kaygorodov, Martín González and Viruel (2026, Remark 23) prove the *mean* \(\mathbb E[N]=1\) for this uniform-invertible-matrix model and pose a random-permutation fixed-point prediction in their generic-Galois Conjecture 2. The formula here determines the exact **second** moment and shows a strictly negative finite-field correction in odd characteristic; it agrees with the proposed symmetric-group variance in the large-\(q\) limit, not a contradiction to that limit. The characteristic-two value is included for comparison, and is also a consequence of stronger characteristic-two distributional information.

Jain (2024) studies random systems drawn from polynomial spaces containing all functions and obtains binomial counts. That coefficient sampling regime is not the invertible-matrix-constrained, coordinatewise-square system studied here. The isomorphism-class counts of Wei and Zou (2023) concern the orbit space of perfect evolution structures, rather than the distribution of individual idempotents for a uniform structure matrix.

## Limitations

No full distribution of \(N\) is claimed in odd characteristic, nor any independence of idempotent events. Invertibility of \(M\) is essential to the pair-transitivity argument. This is an exact arithmetic finite-field moment result; it is not an independent verification of the characteristic-zero generic Galois-group conjecture. An equivalent variance identity embedded in unrelated finite-field fixed-point literature cannot be excluded solely by index searches.

## References

1. I. Kaygorodov, C. Martín González, A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248v1 (first posted 2026-10-15); Remark 23, Question 22 and Conjecture 2. https://arxiv.org/html/2610.22248v1
2. R. Jain, *The number of solutions of a random system of polynomials over a finite field*, arXiv:2409.06866v1 (2024); Theorems 1.4 and 1.5. https://arxiv.org/html/2409.06866v1
3. Y. Wei and Y. M. Zou, *Isomorphism Classes of Idempotent Evolution Algebras*, Linear Algebra and its Applications 675 (2023), 142–178; arXiv:2310.12368. https://arxiv.org/abs/2310.12368
