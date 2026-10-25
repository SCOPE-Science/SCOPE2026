# Sharp worst-case noise amplification for smooth Fourier-continuation blending

## Finding

Let \(d\ge2\), \(C\ge2\), and \(N\ge2d\) be integers. Consider the two-sided degree-\((d-1)\) equispaced Lagrange extrapolation and blending continuation defined in the next section. For each smooth, symmetric, strictly increasing transition \(\sigma\) with endpoint derivatives vanishing through order \(d\), denote the exact data-to-continuation operator by \(E_\sigma\). Define the positive-integer extrapolation Lebesgue function

\[
\Lambda_d(q)=\sum_{j=0}^{d-1}\binom{q+j-1}{j}\binom{q+d-1}{d-1-j},\qquad q\ge1.
\]

The exact worst-case \(\ell^\infty\) data-perturbation amplification and its sharp minimax value are

\[
\|E_\sigma\|_{\infty\to\infty}
=\max_{1\le q<C}\left[(1-\sigma(q/C))\Lambda_d(q)+\sigma(q/C)\Lambda_d(C-q)\right],
\]
\[
\boxed{\inf_{\sigma}\|E_\sigma\|_{\infty\to\infty}=\Lambda_d(\lfloor C/2\rfloor).}
\]

**Parity of attainment:** if \(C\) is even, the infimum is attained by a symmetric, strictly increasing polynomial transition with arbitrarily many vanishing endpoint derivatives. If \(C\) is odd, the infimum is not attained by any transition in the stated strict class, although it is approached by a sequence of admissible polynomial transitions. The same sharp norm applies to the full extension operator that retains all \(N\) original data samples.

For fixed \(d\) and \(C\to\infty\),

\[
\Lambda_d(\lfloor C/2\rfloor)=\frac{C^{d-1}}{(d-1)!}+O_d(C^{d-2}).
\]

In particular, at \(d=9\), \(C=64\), the unavoidable worst-case amplification is at least \(17{,}527{,}209{,}985\). This is a deterministic *input-perturbation* bound, not a forecast of actual error for smooth data or a bound on floating-point recurrence error.

## Assumptions and scope

By affine rescaling, take original equispaced data at \(0,\dots,N-1\). Let \(p_R\) be the degree-at-most-\((d-1)\) polynomial interpolating the rightmost \(d\) samples at \(N-d,\dots,N-1\); let \(p_L\) interpolate the leftmost \(d\) at \(0,\dots,d-1\). For each continuation index \(q=1,\dots,C-1\), define

\[
(E_\sigma f)_q=(1-\sigma(q/C))p_R(N-1+q)+\sigma(q/C)p_L(q-C).
\]

The admissible transitions are functions \(\sigma\in C^d([0,1])\) satisfying \(\sigma(0)=0\), \(\sigma(1)=1\), strict increase on \([0,1]\), reflection symmetry \(\sigma(t)+\sigma(1-t)=1\), and \(\sigma^{(j)}(0)=\sigma^{(j)}(1)=0\) for \(1\le j\le d\). The polynomial transitions constructed below are \(C^\infty\). We use the ordinary real vector \(\ell^\infty\) norms. Because \(N\ge2d\), the two boundary data stencils are disjoint; this hypothesis is essential to the stated exact row-norm formula.

## Proof

**1. An exact extrapolation coefficient identity.** At integer position \(-q\) outside nodes \(0,\dots,d-1\), the absolute value of the Lagrange coefficient at node \(j\) is

\[
|\ell_j(-q)|
=\prod_{\substack{0\le i<d\\i\ne j}}\frac{q+i}{|j-i|}
=\binom{q+j-1}{j}\binom{q+d-1}{d-1-j}.
\]

Reflection about the right endpoint gives the identical absolute row sum for right extrapolation at distance \(q\). Each product above is strictly increasing in \(q>0\) when \(d\ge2\); therefore \(\Lambda_d(q)\) is strictly increasing in positive integers \(q\). The operator norm of a real row acting on \(\ell^\infty\) is its absolute coefficient sum, attained by a sign-vector input. With disjoint left/right stencils and nonnegative blending weights, the continuation row has precisely the absolute sum in the first displayed formula under Finding. Taking the maximum over the finite set of rows establishes the exact operator norm. Each extrapolant reproduces constant data, but its worst-case sign-alternating perturbation can be much larger.

**2. A universal center-row lower bound.** Write \(k=\lfloor C/2\rfloor\). If \(C=2k\), the central row \(q=k\) has both extrapolation distances equal to \(k\), so its norm is exactly \(\Lambda_d(k)\), irrespective of the transition. If \(C=2k+1\), the row \(q=k\) has value

\[
\Lambda_d(k)+\sigma(k/C)[\Lambda_d(k+1)-\Lambda_d(k)].
\]

Because strict increase forces \(\sigma(k/C)>0\), this exceeds \(\Lambda_d(k)\) for every admissible transition. Thus the announced infimum is a lower bound and is unattainable for odd \(C\), provided the matching upper-bound sequence exists.

**3. Smooth realizing/approximating transitions.** For integer \(m\ge1\) define

\[
\sigma_m(t)=\frac{\int_0^t [s(1-s)]^{d+m}\,ds}{\int_0^1 [s(1-s)]^{d+m}\,ds}.
\]

The integrand is a symmetric polynomial, strictly positive for \(0<s<1\). Consequently \(\sigma_m\) is a polynomial, strictly increasing, symmetric about \((1/2,1/2)\), and flat through order \(d\) at both endpoints. By concentration of symmetric beta integrals around \(1/2\), \(\sigma_m(t)\to0\) at each fixed \(t<1/2\), \(\sigma_m(t)\to1\) at each fixed \(t>1/2\), and \(\sigma_m(1/2)=1/2\). For example, viewing its derivative as the density of a symmetric beta distribution, its variance is \(1/[4(2d+2m+3)]\), so Chebyshev's inequality proves the asserted convergence.

Since the set of continuation indices is finite, as \(m\to\infty\) every noncentral row approaches \(\Lambda_d(\min\{q,C-q\})\); the even central row is fixed at \(\Lambda_d(C/2)\). If \(C=2k\), strict monotonicity leaves a positive gap between the central row and the limiting norms of all other rows. Therefore **some finite \(m\)** makes every row at most \(\Lambda_d(k)\), achieving the infimum. If \(C=2k+1\), all rows converge to norms at most \(\Lambda_d(k)\), with the two central rows approaching this value. Hence the infimum is approached but, by step 2, never attained.

**4. Growth and extension to the full data vector.** For fixed \(d\), each binomial-product summand has leading coefficient \(1/[j!(d-1-j)!]\) times \(q^{d-1}\), so

\[
\Lambda_d(q)=\frac{2^{d-1}}{(d-1)!}q^{d-1}+O_d(q^{d-2}).
\]

With \(q=\lfloor C/2\rfloor\), this yields the stated asymptotic. The full data-plus-continuation operator contains an identity block, so its norm is \(\max\{1,\|E_\sigma\|_{\infty\to\infty}\}\). Since \(\Lambda_d(1)=2^d-1\ge3\), this equals the continuation norm for all admissible choices. All claims follow.

## Verification

The included standard-library script `VERIFY_EB.py` forms exact rational Lagrange interpolation weights, checks all continuation rows against the binomial expression, and constructs sign-vector norm witnesses. It passes 1,482 finite exact-rational row/coefficient and boundary tests, as well as exact beta-polynomial attaining and nonattaining examples for both parities. It verifies \(\Lambda_3(3)=31\), \(\Lambda_3(4)=49\), and \(\Lambda_9(32)=17{,}527{,}209{,}985\). The infinite minimax and asymptotic assertions are established by the proof, not by finite testing.

Run with `python3 VERIFY_EB.py` from a directory containing the included script; no third-party Python packages are required.

## Relationship to prior work

Méndez-Cruz and Amlani (2026, arXiv:2610.19797, sections 4–6, especially equations (8), (13)–(14), Algorithm 1 and Remark 2) define the extrapolation-and-blending operator and study numerical FFT differentiation and smoothness. They do not state or imply a sharp \(\ell^\infty\) operator-norm minimax characterization or the even/odd attainment distinction. The present finding analyzes that same discrete operator; it does **not** claim invention of the algorithm or of Lagrange interpolation.

Albin and Pathmanathan (2014, DOI 10.1137/130932533, sections 2–4) previously considered blending polynomial extrapolants with smooth approximate step functions and explicitly discussed extrapolation magnitudes. Their bounds concern the extension and spectral approximation of smooth functions and the chosen approximate window, not the stated sharp minimax over all strictly increasing flat-ended symmetric transitions. De Camargo and Mascarenhas (2014, arXiv:1409.2808) show that extrapolation can produce large Lebesgue constants for **different**, extended Floater–Hormann interpolants; this supports the conditioning motivation without containing the present blend-specific equality and parity classification. Nainwal and Anand (2026, arXiv:2605.04765) analyze FC-Gram variants and their numerical bounds, a different continuation operator.

## Limitations

The result optimizes only the worst-case \(\ell^\infty\) sensitivity to arbitrary data perturbations. It does not optimize Fourier spectral accuracy, derivatives of the transition, window bandwidth, rounded recurrence implementation, or error for smooth structured data. The near-step polynomial family may create large derivatives or Fourier-resolution costs, so minimax data stability need not be best practical differentiation accuracy. The disjoint-stencil assumption \(N\ge2d\) excludes the single-overlap case allowed by the motivating algorithm. Strict monotonicity is essential to odd-\(C\) nonattainment; enlarging the admissible class to permit flat interior intervals changes attainment. No claim is made about more general Gram-based continuation or nonlinear discretizations.

## References

1. I. Méndez-Cruz and F. Amlani, *Smooth periodic extensions by extrapolation and blending for FFT-based differentiation*, arXiv:2610.19797, first posted 2026-10-14. https://arxiv.org/abs/2610.19797
2. N. Albin and S. Pathmanathan, *Discrete Periodic Extension Using an Approximate Step Function*, SIAM Journal on Scientific Computing 36 (2014), A668–A692, DOI 10.1137/130932533. https://www.math.k-state.edu/~albin/pubs/albin_pathmanathan_2014_dpe.pdf
3. A. P. de Camargo and W. F. Mascarenhas, *The stability of extended Floater-Hormann interpolants*, arXiv:1409.2808, 2014. https://arxiv.org/abs/1409.2808
4. P. Nainwal and A. Anand, *Computational and Analytical Study of Variations and Generalizations of the FC-Gram Approximation Algorithm*, arXiv:2605.04765, 2026. https://arxiv.org/abs/2605.04765
