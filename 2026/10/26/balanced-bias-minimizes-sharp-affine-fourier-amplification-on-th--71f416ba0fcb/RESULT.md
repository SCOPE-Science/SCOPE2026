# Balanced bias minimizes sharp affine Fourier amplification on the Bernoulli cube

## Finding
Let \(n\ge2\), \(0<p<1\), and let \(\mu_p\) be the Bernoulli product probability measure on \(\{0,1\}^n\) with independent coordinates satisfying \(\Pr(X_i=1)=p\). Denote by \(P_{n,p}\) the \(L^2(\mu_p)\)-orthogonal projection onto the \((n+1)\)-dimensional affine subspace spanned by the constant function and the coordinates. Set \(q=\min\{p,1-p\}\), and let \(J\sim\operatorname{Bin}(n,q)\). Then the sharp operator norms on both endpoint spaces are equal and are given by
\[
\boxed{\|P_{n,p}\|_{L^1\to L^1}=\|P_{n,p}\|_{L^\infty\to L^\infty}=\frac{1}{q}\,\mathbb E|J-(n-1)q|.}
\]
The norm is attained by a sign-valued input. A maximizing output row occurs at the all-ones vertex if \(p\le1/2\), and at the all-zeros vertex if \(p\ge1/2\).

For every fixed \(n\ge2\), the norm is **strictly increasing in the magnitude of the bias** \(|p-1/2|\). Its unique minimizer is \(p=1/2\), where for every integer \(m\ge1\),
\[
\boxed{\|P_{2m,1/2}\|=\|P_{2m+1,1/2}\|=(2m+1)4^{-m}\binom{2m}{m}.}
\]
At the opposite extreme, \(\lim_{p\downarrow0}\|P_{n,p}\|=2n-1\), without attainment for \(0<p<1\).

The sharp norm exhibits distinct dense and sparse limits. For any fixed \(p\in(0,1)\),
\[
\frac{\|P_{n,p}\|}{\sqrt n}\longrightarrow
\sqrt{\frac{2(1-q)}{\pi q}}.
\]
If instead \(q_n\sim\lambda/n\), \(\lambda>0\), then
\[
\boxed{\frac{\|P_{n,p_n}\|}{n}\longrightarrow
2e^{-\lambda}\frac{\lambda^{\lfloor\lambda\rfloor}}{\lfloor\lambda\rfloor!}.}
\]
The sparse limit is continuous and strictly decreasing in \(\lambda>0\), but has a derivative jump at each positive integer.

## Assumptions and scope
All spaces and operators are real (the same endpoint norm holds for complex inputs by the absolute-kernel bound). Both endpoint norms use the fixed strictly positive product measure \(\mu_p\); the projection is the orthogonal projector in its \(L^2\) geometry. The displayed norm symbol without a subscript refers to either of the equal endpoint norms, not to the Hilbert-space norm (which is one). For \(n=1\) the affine space is the entire function space and both norms equal one for all biases; strictness is asserted only for \(n\ge2\). The rare-limit statement is for sequences \(p_n\) with \(n\min(p_n,1-p_n)\to\lambda\in(0,\infty)\).

## Proof
**Orthogonal kernel and exact row norm.** The functions \(1\) and \(\varphi_i(x)=(x_i-p)/\sqrt{p(1-p)}\), \(1\le i\le n\), are orthonormal. Therefore
\[
(P_{n,p}f)(x)=\mathbb E_{\mu_p}[K_p(x,Y)f(Y)],\qquad
K_p(x,y)=1+\sum_{i=1}^n\frac{(x_i-p)(y_i-p)}{p(1-p)}.
\]
Since every atom has positive measure, \(\|P_{n,p}\|_{\infty\to\infty}=\max_x\mathbb E|K_p(x,Y)|\); for a maximizing row take \(f(y)=\operatorname{sgn}K_p(x,y)\), with either sign at zeros. Symmetry of \(K_p\) also gives the identical \(L^1\to L^1\) norm, by duality.

**Extremizing corner via convex order.** Assume \(p\le1/2\), the other case following by bit-complementation. In a row of the kernel, the contribution from an output coordinate equal to one has law \(U_p=(Y-p)/p\), whereas that from a coordinate equal to zero has law \(V_p=-(Y-p)/(1-p)\). Both have mean zero and minimum \(-1\); their respective maxima are \((1-p)/p\) and \(p/(1-p)\). For any two centered two-point laws with a common minimum \(-1\), increasing the positive endpoint increases the law in convex order: explicitly the smaller positive value is a conditional mean of a mixture of the larger positive endpoint and \(-1\). Replacing any independent \(V_p\) by \(U_p\) therefore cannot decrease the expectation of the convex function \(|1+\sum Z_i|\). Hence the all-ones row maximizes. At that row the kernel is \(1-n+J/p\) with \(J\sim\operatorname{Bin}(n,p)\), proving the exact formula.

**Strict bias law.** If \(0<a<b\le1/2\), then \(U_a\) dominates \(U_b\) in convex order by the same two-point coupling, because its positive endpoint \(1/a-1\) is larger. Consequently the all-ones norm at bias \(a\) is at least that at \(b\). This comparison is strict whenever \((n-1)b\) is not an integer: hold \(n-1\) of the \(U_b\) variables fixed and condition on exactly \(j=\lfloor(n-1)b\rfloor\) successes. The residual constant \(c=2-n+j/b\) satisfies \(c-1<0<c+(1-b)/b\); splitting the positive atom of the final \(U_b\) into \(-1\) and the strictly larger positive atom of \(U_a\) makes Jensen's inequality strict for the absolute value. Other replacements only increase the expectation. If \((n-1)b\) is an integer, insert an intermediate nonexceptional bias between \(a\) and \(b\) and use continuity. Complementation proves strict monotonicity in \(|p-1/2|\), and hence uniqueness of the balanced minimizer.

**Finite closed form and parity pair.** Write \(k=\lfloor(n-1)q\rfloor\), \(B_s\sim\operatorname{Bin}(s,q)\). From \(\mathbb E(J-(n-1)q)=q\), splitting at \(k\) and using the binomial identity \(\mathbb E[(J-nq)\mathbf1_{J\le k}]=-nq(1-q)\Pr(B_{n-1}=k)\) gives
\[
\|P_{n,p}\|=1+2n(1-q)\Pr(B_{n-1}=k)-2\Pr(B_n\le k).
\]
At \(q=1/2\), the representation \(1-n+2J=1+S_n\) for a symmetric \(n\)-step random walk yields \(\mathbb E|1+S_{2m}|=\mathbb E|S_{2m}|+\Pr(S_{2m}=0)\) and \(\mathbb E|1+S_{2m+1}|=\mathbb E|S_{2m+1}|\). Elementary binomial identities give the displayed equal value for both adjacent dimensions. For fixed \(n\), the formula for \(q<1/(n-1)\) reduces to \(1+2(n-1)(1-q)^n\), proving the limiting upper envelope \(2n-1\), strict at every positive bias.

**Dense/sparse limits.** For fixed \(q\in(0,1/2]\), the centered binomial central limit theorem gives \((J-nq)/\sqrt{nq(1-q)}\Rightarrow N(0,1)\). Uniform integrability follows from the bounded second moments; shifting the center from \(nq\) to \((n-1)q\) does not affect the leading absolute first moment. This proves the Gaussian formula. If \(q_n\sim\lambda/n\), binomial-to-Poisson convergence and uniform integrability (bounded means, with controlled second moments) give \(\|P_{n,p_n}\|/n\to\lambda^{-1}\mathbb E|Z-\lambda|\) for \(Z\sim\operatorname{Poisson}(\lambda)\). The elementary identity \(\mathbb E|Z-\lambda|=2\lambda\Pr(Z=\lfloor\lambda\rfloor)\) gives the stated expression. On each \((k,k+1)\) its derivative is strictly negative; values match at integers because successive Poisson masses are equal when their index equals the mean. At every positive integer the left derivative is strictly negative and the right derivative vanishes, proving the asserted corners.

## Verification
The accompanying standalone script `check_projection.py` computes the kernel by exact rational arithmetic and independently evaluates every output row for \(2\le n\le7\), at seven rational biases. It confirms sharp corner attainment, the closed binomial expression, the binomial-tail identity, strict monotonicity on a rational grid, and fair-bias parity pairing; 1,866 assertions pass. The proof above, not these finite tests, establishes statements for all dimensions, all biases and the asymptotic limits.

## Relationship to prior work
The biased tensor Fourier basis and low-degree concentration framework are standard, including Nayar's FKN theorem on the biased cube and the treatment in O'Donnell's *Analysis of Boolean Functions*, Section 8.4. Those works supply the harmonic setting but their inspected sections do not state the present sharp \(L^1/L^\infty\) projector norm, its global bias minimization or the combined Gaussian/Poisson phase law. Related homogeneous-degree-two Walsh and Hamming projection norm results concern a different spectral subspace or a different underlying probability measure; neither formula algebraically implies this degree-zero-plus-one, biased-product statement.

## Limitations
The theorem treats common-coordinate bias only, not heterogeneous Bernoulli parameters, higher Fourier degrees or general correlated measures. It is a theorem about endpoint operator norms and does not establish a new FKN approximation bound. A thorough historical priority investigation remains necessary; the elementary kernel may have appeared previously in different approximation-theoretic terminology. The claimed originality is provisional pending independent bibliographic review.

## References
- P. Nayar, *FKN Theorem on the biased cube*, arXiv:1311.3179v1, first posted 2013-11-13, especially pp. 1–3 and the later proofs. https://arxiv.org/abs/1311.3179
- R. O'Donnell, *Analysis of Boolean Functions*, Cambridge University Press (2014), Section 8.4, “\(p\)-biased analysis”; accessible revised electronic version arXiv:2105.10386. https://arxiv.org/abs/2105.10386
