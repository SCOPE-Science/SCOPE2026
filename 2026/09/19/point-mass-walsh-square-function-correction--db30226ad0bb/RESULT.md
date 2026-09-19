# Exact point-mass Walsh square functions and a correction to higher-order exponent sharpness

## Result

Let \(\Omega_n=\{-1,1\}^n\) carry normalized counting measure and let
\[
(D_j f)(x)=\frac{f(x)-f(x^{(j)})}{2}.
\]
For a \(k\)-set \(J\subset[n]\), write \(D_J=\prod_{j\in J}D_j\), and define the distinct-index order-\(k\) square function
\[
S_{k,n}f(x)=\left(\sum_{\substack{J\subset[n]\\ |J|=k}}|D_Jf(x)|^2\right)^{1/2}.
\]
Let \(F_n=\mathbf 1_{\{(1,\ldots,1)\}}\).

For every \(1\le k\le n\), every \(0<p<\infty\), and every \(x\in\Omega_n\) with exactly \(r\) negative coordinates,
\[
S_{k,n}F_n(x)=
\begin{cases}
2^{-k}\binom{n-r}{k-r}^{1/2},&0\le r\le k,\\
0,&r>k.
\end{cases}
\]
Consequently,
\[
\boxed{
\frac{\|S_{k,n}F_n\|_p^p}{\|F_n\|_p^p}
=2^{-kp}\sum_{r=0}^k\binom nr\binom{n-r}{k-r}^{p/2}.
}
\]
In particular, for fixed \(k\) and fixed \(p\),
\[
\frac{\|S_{k,n}F_n\|_p}{\|F_n\|_p}
\sim
\begin{cases}
2^{-k}(k!)^{-1/p}n^{k/p},&0<p<2,\\
2^{-k/2}(k!)^{-1/2}n^{k/2},&p=2,\\
2^{-k}(k!)^{-1/2}n^{k/2},&p>2.
\end{cases}
\]
At \(p=2\) there is also the exact identity
\[
\frac{\|S_{k,n}F_n\|_2}{\|F_n\|_2}
=2^{-k/2}\binom nk^{1/2}.
\]
Thus the point mass has a genuine \(p=2\) layer transition: below \(2\) its \(L^p\) square-function mass is asymptotically carried by the Hamming sphere of radius \(k\), whereas above \(2\) it is carried by the original point.

There is a critical-window refinement. If \(p_n=2+\lambda/\log n\) with fixed \(\lambda\in\mathbb R\), then
\[
\boxed{
 n^{-k/2}\frac{\|S_{k,n}F_n\|_{p_n}}{\|F_n\|_{p_n}}
\longrightarrow
2^{-k}(k!)^{-1/2}\bigl(1+e^{-\lambda/2}\bigr)^{k/2}.
}
\]
This interpolates between the two one-sided fixed-\(p\) mechanisms on the natural \(1/\log n\) scale.

## Proof

The singleton has the product representation
\[
F_n(x)=\prod_{i=1}^n\frac{1+x_i}{2}.
\]
Since \(D_j((1+x_j)/2)=x_j/2\), the commuting derivatives give, exactly,
\[
D_JF_n(x)
=2^{-k}\left(\prod_{j\in J}x_j\right)
\prod_{i\notin J}\frac{1+x_i}{2}.
\]
Let \(N(x)=\{i:x_i=-1\}\) and \(|N(x)|=r\). The last product vanishes unless \(N(x)\subseteq J\). If \(r\le k\), exactly \(\binom{n-r}{k-r}\) sets \(J\) of size \(k\) contain \(N(x)\), and every surviving derivative has modulus \(2^{-k}\). This proves the pointwise formula. There are \(\binom nr\) points with \(r\) negative coordinates, while \(\|F_n\|_p^p=2^{-n}\), giving the displayed exact norm formula.

For fixed \(p\), the \(r\)-th summand has order
\[
n^{\,r+(k-r)p/2}.
\]
The exponent is strictly increasing in \(r\) when \(p<2\), strictly decreasing when \(p>2\), and independent of \(r\) when \(p=2\). This gives the two off-critical asymptotics. At \(p=2\),
\[
\sum_{r=0}^k\binom nr\binom{n-r}{k-r}
=\binom nk\sum_{r=0}^k\binom kr
=2^k\binom nk,
\]
which yields the exact \(L^2\) formula.

For the critical window \(p_n=2+\lambda/\log n\), fixed \(k,r\) give
\[
\binom nr\binom{n-r}{k-r}^{p_n/2}
=\frac{n^k}{r!(k-r)!}\,e^{\lambda(k-r)/2}(1+o(1)).
\]
Summing over \(r\) yields
\[
\sum_{r=0}^k\binom nr\binom{n-r}{k-r}^{p_n/2}
=\frac{n^k}{k!}(1+e^{\lambda/2})^k(1+o(1)).
\]
Taking the \(p_n\)-th root and using
\[
\frac1{p_n}=\frac12-\frac{\lambda}{4\log n}+o((\log n)^{-1})
\]
gives the stated limit.

## Correction to the sharpness argument in arXiv:2609.09040

Jiao--Luo--Zanin--Zhou, *Sharp Fractional Riesz Estimates on the Hypercube* (arXiv:2609.09040v1), prove a higher-order endpoint estimate and state that the power \(k/p\) is optimal even when only pairwise-distinct indices are retained. Their Section 6.3 uses Lemma 6.3 for the same singleton \(F_n\). With the derivative normalization used in that paper, Lemma 6.3 as stated is false: at the point whose negative coordinates are exactly \(J\), their displayed computation gives \((-2)^k\), whereas the exact value is
\[
(D_JF_n)(x_J)=(-1)^k2^{-k}.
\]
For example, already at \(k=1,n=2,p=3/2\), the claimed lower bound exceeds the exact norm.

The exponent-optimality conclusion nevertheless remains valid. From the exact formula, just the Hamming layer \(r=k\) gives
\[
\frac{\|S_{k,n}F_n\|_p}{\|F_n\|_p}
\ge 2^{-k}\binom nk^{1/p}.
\]
For \(n\ge2k\),
\[
\binom nk\ge \frac{n^k}{2^k k!},
\]
so
\[
\frac{\|S_{k,n}F_n\|_p}{\|F_n\|_p}
\ge
2^{-k-k/p}(k!)^{-1/p}n^{k/p}.
\]
Combining this corrected estimate with the source paper's bound \(\|\Delta^\gamma\|_{L^p\to L^p}\le 3n^\gamma\) proves that any uniform inequality of the form
\[
\|S_{k,n}f\|_p\le C\|\Delta^\beta f\|_p
\]
requires \(\beta\ge k/p\) for \(1<p<2\). Thus the normalization slip invalidates the numerical lower bound in Lemma 6.3 but does not invalidate the stated exponent sharpness.

## Context and limitations

The source paper establishes the dimension-free endpoint estimate and its higher-order analogue; those upper-bound arguments are not challenged here. This record concerns only the distinct-index singleton calculation used for exponent optimality, repairs that step, and gives the exact finite-\(n\) profile and its \(p=2\) crossover.

No claim is made that the singleton extremizes the full higher-order fractional Riesz operator norm, or that the source paper's open dependence on \(p-1\) is resolved. The exact singleton identity is elementary once the correct product formula for \(D_JF_n\) is written down. Originality is therefore asserted only to the best of our knowledge for the combination of the correction, the exact \(L^p\) profile, and the critical-window asymptotic.

## Verification

`artifacts/verify_spike_formula.py` independently enumerates small cubes, computes the iterated discrete derivatives from their defining finite differences, and checks the exact closed formula. It also checks an explicit counterexample to the numerical bound stated in Lemma 6.3 of arXiv:2609.09040v1. The script was executed successfully with Python 3.

## References

1. Y. Jiao, S. Luo, D. Zanin, D. Zhou, *Sharp Fractional Riesz Estimates on the Hypercube*, arXiv:2609.09040v1 (2026), especially Theorem 1.3 and Section 6.3.
2. Z. Xu, H. Zhang, *The Endpoint Fractional Riesz Estimate on the Hamming Cube*, arXiv:2609.03993v1 (2026). This independent endpoint paper addresses the first-order endpoint estimate and does not supply the exact higher-order singleton profile above.
3. L. Efraim, F. Lust-Piquard, *Poincare type inequalities on the discrete cube and in the CAR algebra*, Probab. Theory Related Fields 141 (2008), 569--602.
