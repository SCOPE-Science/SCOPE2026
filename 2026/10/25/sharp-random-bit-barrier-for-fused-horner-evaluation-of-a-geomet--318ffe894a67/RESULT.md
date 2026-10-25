# Sharp random-bit barrier for fused Horner evaluation of a geometric polynomial

## Finding
For integers \(q\ge2\), \(p\ge q+1\), and \(r\ge1\), let \(x=1-2^{-q}\), and evaluate the all-one degree-\(n\) polynomial \(P_n(x)=\sum_{j=0}^{n}x^j\) in precision \(p\) by *fused* stochastic-rounding Horner steps \(Y_0=1\) and \(Y_{n+1}=\operatorname{SR}_{p,r}(1+xY_n)\). Here \(\operatorname{SR}_{p,r}\) uses the binary *truncation* of the exact FMA result to precision \(p+r\) in its upward probability (defined below), with independent random choices. Put \(L=2^q\) and \(\Delta=2^{q-p}\). Then, almost surely, the iterates stop changing after finitely many steps, and the deterministic terminal value is
\[
Y_\infty=\begin{cases}
L-(2^{q-r}-1)\Delta,&1\le r<q,\\
L,&r\ge q.
\end{cases}
\]
Thus the finite-bit fused Horner computation has the correct infinite-geometric-series limit **if and only if** \(r\ge q\). If \(r<q\), its exact limiting relative deficit is \((2^{q-r}-1)2^{-p}\), although \(P_n(x)\to L\). By contrast, ideal stochastic rounding with the exact upward probability reaches \(L\) almost surely for every admissible \(p,q\).

The final predecessor \(Y_\infty-\Delta\) is visited almost surely. Conditional on first reaching it, its number of update attempts until the terminal upward jump is geometric, of exact mean \(2^r\) for \(r<q\) and \(2^q\) for \(r\ge q\). In particular, the boundary case \(r=q\) removes the asymptotic bias but has an exact \(2^q\)-step expected waiting period for its final floating-point increment.

For example, at \(p=8\), \(q=7\), and \(r=1\), the evaluation point is \(127/128\), the infinite sum is \(128\), yet every run ultimately absorbs at \(193/2=96.5\); the limiting relative deficit is \(63/256\).

## Assumptions and scope
The binary normalized floating-point set has exactly \(p\) significant bits, with an exponent range wide enough for all values encountered. No overflow, underflow, subnormal effects, or independent product-rounding step is allowed. All operations in the affine expression \(1+xY_n\) are exact until the *single* prescribed FMA rounding. The coefficients, \(x\), and starting value are representable at precision \(p\). An independent uniform random choice is made at each call. The corresponding exact Horner polynomial is of degree \(n\), while the limiting assertion takes \(n\to\infty\) with \(p,q,r\) fixed.

For any positive real \(z\), let \(\lfloor z\rfloor_t\) and \(\lceil z\rceil_t\) denote adjacent precision-\(t\) floating-point bounds. Let \(T_{p+r}(z)=\lfloor z\rfloor_{p+r}\), binary truncation downward. If \(z\) lies strictly between two precision-\(p\) floats \(a<b\), the limited-bit stochastic rule rounds to \(b\) with probability
\[
\theta_{p,r}(z)=\frac{T_{p+r}(z)-a}{b-a},
\]
and otherwise to \(a\). A precision-\(p\) input is fixed. Classical ideal stochastic rounding replaces \(T_{p+r}(z)\) by \(z\). This is specifically the truncation-based rounding model, not a bias-corrected or independently double-rounded alternative.

## Proof
**1. Monotone bounded chain.** Set \(L=2^q\) and \(F(y)=1+xy=y+(L-y)/L\). Since \(x=1-L^{-1}\) and \(Y_0=1\), every \(Y_n\) is a precision-\(p\) float in \([1,L]\). For each float \(y<L\), \(y<F(y)<L\); therefore both precision-\(p\) rounding candidates for \(F(y)\) lie in \([y,L]\). The path is nondecreasing. The finite precision grid in this compact interval has only finitely many states.

**2. Exact absorbing threshold.** The spacing of precision-\(p\) floats immediately below \(L\) is \(\Delta=2^{q-p}\); the spacing of precision-\(p+r\) floats in \([L/2,L)\) is \(\Delta/2^r\). For any precision-\(p\) state \(y<L\), the exact increment is \(d(y)=(L-y)/L\). Since the truncation grid below \(L\) has spacing at most \(\Delta/2^r\), a strict upward move has positive conditional probability whenever \(d(y)\ge\Delta/2^r\). If \(r\ge q\), then \(L-y\ge\Delta\), so \(d(y)\ge\Delta/L\ge\Delta/2^r\) for every state \(y<L\). Hence \(L\) is the only absorbing state.

If \(1\le r<q\), let \(k=2^{q-r}\) and \(B=L-(k-1)\Delta\). Because \(k\le L/2\) and \(p\ge q+1\), both \(B\) and its predecessor \(A=B-\Delta=L-k\Delta\) lie in \([L/2,L)\). For \(y=L-j\Delta\in[B,L)\), \(1\le j\le k-1\), we have \(d(y)=j\Delta/L<\Delta/2^r\). The next \(p+r\) truncation therefore equals \(y\), making every one of these \(p\)-grid states absorbing. At every state \(y\le A\), conversely, \(d(y)\ge k\Delta/L=\Delta/2^r\), so there is positive probability of increasing.

**3. Selection and finite absorption.** The map \(F\) is increasing, and \(F(A)=A+\Delta/2^r<B\). Therefore any path starting below \(B\) cannot jump over \(B\): for \(y\le A\), \(F(y)\le F(A)<B\), and the upper precision-\(p\) rounding candidate is at most \(B\). Every state below \(B\) has a positive upward transition probability. A nondecreasing finite-state chain cannot remain forever at such a state; its holding time there is geometric with finite mean. After finitely many upward jumps it reaches \(B\) almost surely, and remains there. When \(r\ge q\) the same argument reaches \(L\). This also gives finite expected total absorption time in every case.

**4. Inevitable final predecessor and holding law.** The terminal target is \(B\) for \(r<q\), or \(L\) for \(r\ge q\); denote it by \(Z\), and let \(A_*=Z-\Delta\). When \(r<q\), the exact increment from \(A_*\) is \(k\Delta/L=\Delta/2^r\), an exactly representable \(p+r\) increment, so the upward probability is exactly \(2^{-r}\). When \(r\ge q\), it is \(\Delta/L\), also exactly representable at precision \(p+r\), and the upward probability is exactly \(L^{-1}=2^{-q}\). The next lower float \(A_*-\Delta\) obeys \(F(A_*-\Delta)<A_*\): this is equivalent to \((k+1)/L<1\) for \(r<q\), or \(2/L<1\) for \(r\ge q\), both true for \(q\ge2\). By monotonicity of \(F\), no state below \(A_*\) can round past \(A_*\). Consequently the path visits \(A_*\) with probability one before absorption at \(Z\), and the final residence time has the stated geometric law. The exact relative deficit follows by dividing \(L-B=(2^{q-r}-1)\Delta\) by \(L\).

**5. Ideal rounding.** Replacing truncation by the exact argument yields a strictly positive probability of an upward move at every precision-\(p\) state below \(L\). Finite-state monotone absorption therefore takes place at \(L\) almost surely.

## Verification
The standalone script `verify_fma_horner.py` uses Python exact rational arithmetic. It enumerates every reachable state and nonzero-probability transition for all \(224\) triples with \(4\le p\le10\), \(2\le q<p\), and \(1\le r\le q+2\). For each triple it confirms monotonicity, the unique reachable absorbing state, the predicted terminal value, visitation of the final predecessor, and its exact geometric jump probability. The largest enumerated state graph contains \(2382\) reachable floats. An additional seeded trajectory for \((p,q,r)=(8,7,1)\) reaches \(193/2\) after \(245\) calls. Invoke with `python verify_fma_horner.py` using Python 3; no nonstandard dependencies are required. The analytic argument, not finite enumeration, establishes the theorem for all stated integers.

## Relationship to prior work
El Arar, Fasi, Filip, and Mikaitis (2026), arXiv:2603.24161, Definition 2, introduce the specific truncation-based \(\operatorname{SR}_{p,r}\) model and analyze finite-degree Horner error with separately rounded multiplication and addition. Their Remark 3 explicitly excludes FMA Horner; their Section 5.1 investigates finite-degree stagnation numerically. Those finite-horizon bounds and experiments neither imply the deterministic absorbing-state law here nor contradict it. El Arar et al. (2024/2025), arXiv:2408.03069, establish the general rounding bias model and analyze recursive summation and dot products, but not the fused affine recurrence. Fitzgibbon and Felix (2025), arXiv:2504.20634, analyze biases of alternative few-random-bit rounding implementations, not the present Horner absorbing states. The 2026 limited-precision SR survey, arXiv:2603.06060, gives context but no matching exact FMA geometric-series cutoff. None of these observations constitutes a claim of exhaustive historical priority.

## Limitations
This is a sharp result for the *truncation-based* limited-bit rule and the exact one-parameter geometric-polynomial family \(x=1-2^{-q}\) with all coefficients equal to one. It does not assert the same cutoff for round-to-nearest higher-precision intermediates, bias-corrected rounding, two-rounding Horner, arbitrary polynomials, or actual finite-exponent hardware. The result is an infinite-degree limit: it does not give uniform finite-degree accuracy bounds or guarantee practical benefit from using arbitrarily many FMA calls. Historical priority has not been independently established.

## References
1. E.-M. El Arar, M. Fasi, S.-I. Filip, and M. Mikaitis, *Probabilistic Error Analysis of Limited-Precision Stochastic Rounding: Horner's Algorithm and Pairwise Summation*, arXiv:2603.24161 (first posted 2026-03-25), https://arxiv.org/abs/2603.24161.
2. E.-M. El Arar, M. Fasi, S.-I. Filip, and M. Mikaitis, *Probabilistic Error Analysis of Limited-Precision Stochastic Rounding*, arXiv:2408.03069 (first posted 2024-08-06), https://arxiv.org/abs/2408.03069.
3. A. Fitzgibbon and S. Felix, *On Stochastic Rounding with Few Random Bits*, arXiv:2504.20634 (first posted 2025-04-29), https://arxiv.org/abs/2504.20634.
4. E.-M. El Arar et al., *Limited-Precision Stochastic Rounding*, arXiv:2603.06060 (2026), https://arxiv.org/abs/2603.06060.
