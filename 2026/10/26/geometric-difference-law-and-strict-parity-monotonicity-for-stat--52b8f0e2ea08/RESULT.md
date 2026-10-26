# Geometric-difference law and strict parity monotonicity for stationary Mallows displacement

## Finding
Fix \(0<q<1\) and let \(\Sigma\) have the stationary, balanced two-sided Mallows distribution on bijections of \(\mathbb Z\) with parameter \(q\). For a fixed \(i\in\mathbb Z\), write \(D=\Sigma(i)-i\). Let \(G_k,G'_k\), for \(k\ge1\), be independent nonnegative geometric random variables with
\[
\Pr(G_k=j)=\Pr(G'_k=j)=(1-q^k)q^{kj},\qquad j=0,1,2,\ldots.
\]
Then both sums \(X=\sum_{k\ge1}G_k\) and \(X'=\sum_{k\ge1}G'_k\) are almost surely finite and
\[
\boxed{D\ \stackrel{\mathrm d}=\ X-X'.}
\]
In particular, the bilateral probability generating function is exactly
\[
\boxed{\mathbb E[z^D]=\prod_{k=1}^{\infty}\frac{(1-q^k)^2}{(1-q^k z)(1-q^k/z)},\qquad q<|z|<q^{-1}.}
\]
Here \(z\) can be complex, and the expression is absolutely convergent in the stated annulus.

For the notation of He--Müller--Verstraaten, set \(Q=q^{-1}>1\) and let \(c_o(Q)=\Pr(D\text{ is even})\), \(c_e(Q)=\Pr(D\text{ is odd})\). The exact parity gap is
\[
\boxed{c_o(Q)-c_e(Q)=\prod_{k=1}^{\infty}\left(\frac{1-Q^{-k}}{1+Q^{-k}}\right)^2>0.}
\]
Thus \(c_o(Q)>\tfrac12>c_e(Q)\) for **every** \(Q>1\), and \(c_o(Q)\) is strictly increasing while \(c_e(Q)\) is strictly decreasing in \(Q\). Both the strict inequalities and the strict monotonicities answer the two explicit questions in Section 10 of He--Müller--Verstraaten [2].

## Assumptions and scope
The probability space is the ergodic balanced two-sided Mallows measure of Gnedin and Olshanski [1], *not* the later non-ergodic Mallows product measure. The underlying permutation has infinitely many indices, but \(q\) is a fixed real number strictly between zero and one. The result concerns the **one-point displacement**; it asserts neither independence of displacements at distinct indices nor a description of their joint law. The variable \(Q=q^{-1}\) is the \(Q>1\) parameter used by [2] for its parity constants.

Write \((a;q)_r=\prod_{j=0}^{r-1}(1-aq^j)\), with \((a;q)_0=1\), and \((a;q)_\infty=\prod_{j=0}^\infty(1-aq^j)\), whenever the infinite product converges. The proof requires only the standard \(q\)-binomial theorem, applied inside its disk of absolute convergence.

## Proof
**Step 1: the established displacement law.** Gnedin--Olshanski [1, Theorem 5.1, equation (19)] give the following exactly normalized one-point marginal:
\[
\Pr(D=d)=(1-q)(q;q)_\infty
\sum_{\substack{r,s\ge0\\r-s=d}}
\frac{q^{rs+r+s}}{(q;q)_r(q;q)_s},\qquad d\in\mathbb Z.
\]
Since \((q;q)_r\ge(q;q)_\infty>0\), multiplying a summand by \(z^{r-s}\) yields a series absolutely dominated by convergent geometric series whenever \(q<|z|<q^{-1}\). Rearrangement and summation are therefore legitimate in this annulus.

**Step 2: two applications of the \(q\)-binomial identity.** The Euler special case and the general \(q\)-binomial identity are, respectively,
\[
\sum_{s\ge0}\frac{u^s}{(q;q)_s}=\frac1{(u;q)_\infty},\qquad
\sum_{r\ge0}\frac{(a;q)_r}{(q;q)_r}t^r=\frac{(at;q)_\infty}{(t;q)_\infty},
\]
for \(|u|<1\), \(|t|<1\). With \(u=q^{r+1}/z\), followed by \(a=q/z\) and \(t=qz\), one obtains
\[
\begin{aligned}
\mathbb E[z^D]
&=(1-q)(q;q)_\infty\sum_{r\ge0}
 \frac{(qz)^r}{(q;q)_r}\frac1{(q^{r+1}/z;q)_\infty}\\
&=\frac{(1-q)(q;q)_\infty}{(q/z;q)_\infty}
 \sum_{r\ge0}\frac{(q/z;q)_r}{(q;q)_r}(qz)^r\\
&=\frac{(1-q)(q;q)_\infty(q^2;q)_\infty}
 {(q/z;q)_\infty(qz;q)_\infty}\\
&=\frac{(q;q)_\infty^2}
 {(q/z;q)_\infty(qz;q)_\infty}.
\end{aligned}
\]
The last equality uses \((q;q)_\infty=(1-q)(q^2;q)_\infty\). Expanding the denominators gives the claimed product.

**Step 3: the independent-geometric representation.** For \(G_k\) as above,
\[
\mathbb E[z^{G_k}]=\frac{1-q^k}{1-q^kz}.
\]
The expectation of \(X=\sum_{k\ge1}G_k\) is \(\sum_{k\ge1}q^k/(1-q^k)<\infty\), so \(X\) and the independent copy \(X'\) are finite almost surely. Their bilateral generating function is the product in Step 2. Uniqueness of Laurent coefficients of an absolutely convergent bilateral generating function proves \(D\stackrel{\mathrm d}=X-X'\).

**Step 4: parity and monotonicity.** Evaluate at \(z=-1\), which lies in the annulus for every \(0<q<1\):
\[
B(q):=\mathbb E[(-1)^D]=\prod_{k\ge1}\left(\frac{1-q^k}{1+q^k}\right)^2.
\]
All factors are strictly positive and their logarithms are absolutely summable for fixed \(q<1\), so \(B(q)>0\). Since \(c_o+c_e=1\) and \(c_o-c_e=B(q)\), the strict parity inequalities follow. The uniformly convergent differentiated logarithmic series on compact subsets of \((0,1)\) gives
\[
\frac{d}{dq}\log B(q)=-4\sum_{k\ge1}\frac{kq^{k-1}}{1-q^{2k}}<0.
\]
It follows that \(B(1/Q)\), hence \(c_o(Q)=(1+B(1/Q))/2\), increases strictly in \(Q>1\), while \(c_e(Q)\) decreases strictly. Finally, \(B(q)\to1\) as \(q\downarrow0\), since \(\sum q^k\to0\); and \(B(q)\to0\) as \(q\uparrow1\), since \(0<B(q)\le[(1-q)/(1+q)]^2\). These give the endpoint limits.

## Verification
A separate standard-library program, `verify_product.py`, compares direct finite truncations of [1, equation (19)] with the truncated infinite product at five rational parameter values. Its checks include explicit geometric-tail error budgets, mass normalization, positivity, and ordered monotonicity samples. Running `python verify_product.py` produces 30 passing decimal assertions. The checker is **diagnostic only**: the proof of every infinitely quantified assertion is the argument above, including uniform convergence, summation identities, and strict derivative sign.

## Relationship to prior work
Gnedin and Olshanski [1] derived the full one-point displacement distribution as a two-index hypergeometric sum and as a basic hypergeometric function. Their theorem is an essential starting point and, in combination with classical \(q\)-binomial identities, *logically implies* the present formulas; the value of the present result is the new closed-form evaluation, independent-geometric law, and its exact global inequalities. He, Müller, and Verstraaten [2, Section 10] explicitly posed \(c_o>1/2>c_e\) and the strict monotonicity of both constants as open problems. Their Theorem 1.6 identifies the constants but does not resolve these questions. Bufetov and Chen [3] study a different, non-ergodic mixture called the Mallows product measure and obtain separate displacement formulas; their theorems are not a statement about the fixed ergodic law here. Definitive priority beyond the inspected sources requires further specialist review.

## Limitations
No claim is made about joint displacements at distinct sites, finite-permutation error bounds, parameter values \(q=0\) or \(q=1\), or analogous parity laws for other permutation models. The infinite-series identity is an exact consequence of an existing one-point distribution and classical summation identities, rather than a new construction of the Mallows measure. The present comparison cannot exclude an equivalent, previously unnoticed transform in other sources. Independent validation is outstanding.

## References
[1] A. Gnedin and G. Olshanski, *The two-sided infinite extension of the Mallows model for random permutations*, arXiv:1103.1498v1 (first posted 2011-03-08), Theorem 5.1, equation (19). https://arxiv.org/abs/1103.1498

[2] J. He, T. Müller, and T. W. Verstraaten, *Cycles in Mallows random permutations*, arXiv:2201.11610v1 (first posted 2022-01-27), Theorem 1.6 and Section 10; subsequently *Random Structures & Algorithms* (2023). https://arxiv.org/abs/2201.11610

[3] A. Bufetov and K. Chen, *Mallows Product Measure*, arXiv:2402.09892 (first posted 2024-02-15), Theorem 1.1 and introductory distinction between ergodic Mallows and their mixture. https://arxiv.org/abs/2402.09892

[4] G. Gasper and M. Rahman, *Basic Hypergeometric Series*, 2nd ed., Cambridge University Press (2004), the \(q\)-binomial theorem.
