# The sharp slab Santaló advantage has exact exponential base two


## Finding
Let \(M_n\) be the sharp one-dimensional profile constant in the slab Santaló theorem of Artstein-Avidan, and write
\[
B_n=\Sigma_n(0)=\frac{\kappa_{{n+1}}}{\kappa_n}.
\]
For every integer \(n\ge 1\),
\[
\frac{{2^{{n/2+1}}}}{{n+1}}\le M_n\le 2^{{n/2+1}}.
\]
Hence, for
\[
R_n=\left(\frac{{M_n}}{{B_n}}\right)^2,
\]
which is simultaneously the ratio of the sharp slab volume-product constant to the Euclidean-ball volume product and the ratio of the sharp functional constant to the self-dual quadratic benchmark,
\[
\frac{{2^{{n+2}}}}{{(n+1)^2B_n^2}}\le R_n\le\frac{{2^{{n+2}}}}{{B_n^2}}.
\]
Moreover,
\[
B_n=\sqrt{{\pi}}\,\frac{{\Gamma(n/2+1)}}{{\Gamma((n+3)/2)}},
\qquad B_n^2\sim\frac{{2\pi}}n,
\]
so
\[
\lim_{{n\to\infty}}M_n^{{1/n}}=\sqrt2,
\qquad
\lim_{{n\to\infty}}R_n^{{1/n}}=2,
\]
and equivalently \(\log R_n=n\log2+O(\log n)\). Thus the sharp improvement over the Euclidean-ball or self-dual quadratic benchmark is not merely strict: it is exponentially large, with exact exponential base two per horizontal dimension.

## Assumptions and scope
The dimension parameter \(n\) is a positive integer. The constants \(M_n\), \(\Sigma_n(0)\), and \(\kappa_n\) have the normalization used in arXiv:2609.38041v1. The geometric comparison concerns the source's slab class with centrally symmetric horizontal sections, and the functional comparison concerns the source's corresponding sharp functional Santaló inequality. No assertion is made for unrestricted convex bodies or for a different functional normalization.

## Proof
The source proves that \(M_n\) is the maximum of the action
\[
I_n(T)=\int_{{-1}}^1(1-tT(t))^{{n/2}}\sqrt{{T'(t)}}\,dt
\]
over the admissible increasing absolutely continuous transports \(T:[-1,1]\to[-1,1]\) with \(T(-1)=-1\) and \(T(1)=1\). Its cone-profile calculation gives
\[
M_n\ge \frac{{2^{{(n+2)/2}}}}{{n+1}}=\frac{{2^{{n/2+1}}}}{{n+1}}.
\]

For the reverse bound, \(t,T(t)\in[-1,1]\) implies \(1-tT(t)\le2\). Therefore
\[
I_n(T)\le 2^{{n/2}}\int_{{-1}}^1\sqrt{{T'(t)}}\,dt.
\]
Cauchy--Schwarz and absolute continuity give
\[
\int_{{-1}}^1\sqrt{{T'(t)}}\,dt
\le\sqrt{{2\int_{{-1}}^1T'(t)\,dt}}
=\sqrt{{2(T(1)-T(-1))}}=2.
\]
Thus \(I_n(T)\le2^{{n/2+1}}\) for every admissible transport, and maximizing yields the asserted upper bound for \(M_n\).

The source identifies the Euclidean-ball profile value as
\[
B_n=\Sigma_n(0)=\int_{{-1}}^1(1-t^2)^{{n/2}}\,dt
=\sqrt{{\pi}}\,\frac{{\Gamma(n/2+1)}}{{\Gamma((n+3)/2)}}.
\]
The standard gamma-ratio asymptotic gives \(B_n^2\sim2\pi/n\). Taking \(n\)-th roots in the two-sided estimate for \(M_n\) gives \(M_n^{{1/n}}\to\sqrt2\). Squaring after division by \(B_n\), whose \(n\)-th root tends to one, gives \(R_n^{{1/n}}\to2\). The logarithmic form follows immediately.

Finally, the source's sharp geometric constant is \(\kappa_n^2M_n^2\), whereas the Euclidean ball has volume product \(\kappa_{{n+1}}^2=\kappa_n^2B_n^2\). The same paper writes its sharp functional constant as \((M_n/B_n)^2\) times the self-dual quadratic value. Hence the identical ratio \(R_n\) governs both comparisons.

## Verification
The argument uses only the source's exact variational representation, its explicit cone-profile lower bound, endpoint normalization of the admissible transport, Cauchy--Schwarz, and the standard gamma-ratio asymptotic. The upper bound is uniform over the full admissible transport class and does not rely on a finite search or numerical optimization. The conclusion determines the exponential rate only; it does not determine the optimal polynomial prefactor multiplying \(2^n\).

## Relationship to prior work
Artstein-Avidan proves the sharp slab and functional Santaló inequalities, identifies \(M_n\) as the corresponding optimal profile constant, gives the cone-profile lower bound used here, and proves that \(M_n>\Sigma_n(0)\) in the nontrivial dimensions. The same paper compares its sharp functional constant with Bobkov's earlier general convex-measure inequality and notes that the self-dual quadratic is no longer extremal. The present finding adds a dimension-asymptotic statement not supplied by those comparisons: the sharp-to-ball and sharp-to-quadratic ratio has exact exponential base two.

## Limitations
The bounds leave a polynomial-width gap and therefore do not determine a full asymptotic equivalent for \(M_n\) or \(R_n\), nor the asymptotics of the maximizing profile parameter. The result is tied to the sharp constants and normalization of the cited slab problem; it does not claim that the cone profile is asymptotically optimal up to a constant factor.

## References
1. S. Artstein-Avidan, *A sharp Santaló inequality in a slab with centrally symmetric sections*, arXiv:2609.38041v1, 2026.
2. S. G. Bobkov, *Convex bodies and norms associated to convex measures*, Probability Theory and Related Fields 147 (2010), 303--332.
