# Exact Gaussian missingness modulus and a log-log adaptation window
## Finding
Let \(\phi\) and \(\Phi\) denote the standard normal density and distribution function, and write \(\bar\Phi=1-\Phi\). Fix \(b\in(0,1)\), put \(L=\log(1/b)\), and let \(a_n=(2n)^{-1}\). Consider
\[
M_{r,b}=bN(r,1)+(1-b)\delta_\star,
\]
which is the MCAR law with observation probability \(b\) and Gaussian location \(r\). Let
\[
\mathcal C_n=\mathcal M(N(0,1),0,1-a_n).
\]
By the density characterization of the realisable missingness model, a member of \(\mathcal C_n\) has an observed density \(m\) satisfying
\[
a_n\phi(x)\le m(x)\le\phi(x)\qquad\text{for all }x\in\mathbb R,
\]
with the remaining probability at \(\star\).

Define
\[
D_n(r;b)=\inf_{M\in\mathcal C_n}\operatorname{TV}(M,M_{r,b}).
\]
Then, for every \(r>0\),
\[
D_n(r;b)=\max\{A_b(r),B_{n,b}(r)\},
\]
where
\[
A_b(r)=b\,\bar\Phi\!\left(\frac{L}{r}-\frac r2\right)-\bar\Phi\!\left(\frac{L}{r}+\frac r2\right)
\]
and
\[
B_{n,b}(r)=a_n\Phi\!\left(\frac r2-\frac{\log(2nb)}r\right)-b\Phi\!\left(-\frac r2-\frac{\log(2nb)}r\right).
\]
The infimum is attained by clipping \(b\phi(x-r)\) to the interval \([a_n\phi(x),\phi(x)]\) pointwise.

For fixed \(x\in\mathbb R\), set
\[
C_b=\frac{\sqrt b\,L}{4\sqrt\pi},\qquad
S_n(x)=\log n-\frac32\log\log n+\log C_b+x,
\]
and, for all sufficiently large \(n\),
\[
r_n(x)=\frac{L}{\sqrt{2S_n(x)}}.
\]
Then
\[
nD_n(r_n(x);b)\longrightarrow e^{-x}.
\]
Consequently, the product-distance tensorization bound gives
\[
\limsup_{n\to\infty}\inf_{M\in\mathcal C_n}
\operatorname{TV}\!\left(M^{\otimes n},M_{r_n(x),b}^{\otimes n}\right)
\le 1-\exp(-e^{-x}).
\]

In the known-variance Gaussian adaptive-confidence setting of Ma, Verchand, Gao and Samworth, fix an MCAR fraction \(\epsilon\in(0,1)\), so \(b=1-\epsilon\), and a miscoverage level \(\alpha\in(0,1/9)\). Their adaptive class permits the null-side missingness level \(1-a_n\). Applying their testing reduction to the exact modulus above yields
\[
\liminf_{n\to\infty}
\frac{\sqrt{\log n}}{\sigma}
L_{n,\sigma,\epsilon,0}
\ge
\frac{\log(1/(1-\epsilon))}{\sqrt2}.
\]
For every fixed \(x> -\log\log 3\), the stronger finite-asymptotic statement
\[
L_{n,\sigma,\epsilon,0}\ge
\frac{\sigma\log(1/(1-\epsilon))}{\sqrt{2S_n(x)}}
\]
holds for all sufficiently large \(n\). This improves the explicit constants furnished by the two cases in Proposition 22 while remaining a lower-bound result; no matching sharp upper constant is asserted.

## Assumptions and scope
The finding concerns the one-dimensional Gaussian realisable-missingness model on \(\mathbb R_\star\), known scale \(\sigma\), and adaptation over the same broad contamination-parameter class used in Proposition 22 of arXiv:2609.28336v1. The exact modulus is stated after standardizing \(\sigma=1\); scaling restores \(\sigma\). The MCAR fraction \(\epsilon\) is fixed in the asymptotic confidence-interval consequence. The result does not cover unknown scale, non-Gaussian base distributions, or contamination fractions varying with \(n\).

## Proof
Let \(m_2(x)=b\phi(x-r)\). For any \(M\in\mathcal C_n\), let \(m\) be its observed density and define
\[
P=\int_{\mathbb R}(m_2-m)_+\,dx,\qquad
N=\int_{\mathbb R}(m-m_2)_+\,dx.
\]
The difference of the two atom masses at \(\star\) is \(N-P\). Hence
\[
\operatorname{TV}(M,M_{r,b})
=\frac12\{P+N+|P-N|\}
=\max\{P,N\}.
\]
The likelihood ratio \(m_2(x)/\phi(x)=b\exp(rx-r^2/2)\) is strictly increasing. It crosses the lower admissible ratio \(a_n\) at
\[
\gamma=\frac r2-\frac{\log(2nb)}r
\]
and the upper ratio \(1\) at
\[
\tau=\frac r2+\frac Lr.
\]
Every admissible \(m\) therefore has unavoidable negative discrepancy on \(( -\infty,\gamma)\) and unavoidable positive discrepancy on \((\tau,\infty)\). These masses are exactly \(B_{n,b}(r)\) and \(A_b(r)\), respectively. Thus \(P\ge A_b(r)\), \(N\ge B_{n,b}(r)\), and
\[
D_n(r;b)\ge\max\{A_b(r),B_{n,b}(r)\}.
\]
The clipped density
\[
m^*(x)=\min\{\phi(x),\max\{a_n\phi(x),m_2(x)\}\}
\]
is admissible and has no discrepancy outside those two unavoidable regions. It attains \(P=A_b(r)\) and \(N=B_{n,b}(r)\), proving the exact formula.

For the asymptotic, put
\[
z=\frac Lr-\frac r2.
\]
At the upper crossing, \(\phi(z+r)=b\phi(z)\). The Mills expansion
\[
\bar\Phi(t)=\phi(t)\{t^{-1}-t^{-3}+O(t^{-5})\}
\]
gives, whenever \(r\to0\) and \(L^2/(2r^2)\asymp\log n\),
\[
A_b(r)
\sim b\phi(z)\frac{r}{z^2}
\sim
\frac{\sqrt b}{\sqrt{2\pi}L^2}
 r^3\exp\!\left(-\frac{L^2}{2r^2}\right).
\]
Writing \(S=L^2/(2r^2)\) converts this to
\[
A_b(r)\sim C_bS^{-3/2}e^{-S},
\qquad
C_b=\frac{\sqrt b\,L}{4\sqrt\pi}.
\]
At \(r=r_n(x)\), the definition of \(S_n(x)\) yields
\[
nA_b(r_n(x))\to e^{-x}.
\]
Meanwhile \(\gamma\) is of order \(- (\log n)^{3/2}\), so a Gaussian tail bound gives \(nB_{n,b}(r_n(x))\to0\). Hence \(nD_n(r_n(x);b)\to e^{-x}\).

Choose the one-sample optimizer \(M_n^*\). Standard product tensorization gives
\[
\operatorname{TV}\!\left((M_n^*)^{\otimes n},M_{r_n(x),b}^{\otimes n}\right)
\le 1-\{1-D_n(r_n(x);b)\}^n,
\]
which proves the displayed product bound.

Finally, Proposition 22 of arXiv:2609.28336v1 reduces a too-short adaptive interval to a test between a law in \(\mathcal M(N(0,\sigma^2),0,1-1/(2n))\) and the target law in \(\mathcal M(N(\sigma r,\sigma^2),\epsilon,0)\), with a required sum of testing errors at most \(1/3\). For fixed \(x> -\log\log3\),
\[
1-\exp(-e^{-x})<\frac23,
\]
so the exact-modulus pair has, for all sufficiently large \(n\), product total variation below \(2/3\). Le Cam's inequality therefore forces the sum of testing errors above \(1/3\), contradicting the reduction whenever the adaptive length is below \(\sigma r_n(x)\). This proves the second-order lower bound. The leading constant follows because \(S_n(x)/\log n\to1\).

## Verification
The proof uses only the exact density-band characterization of the realisable missingness model, elementary total-variation algebra, Gaussian likelihood-ratio crossings, the standard Mills expansion, and product total-variation tensorization. The accompanying verifier evaluates the exact formula and the critical-window normalization numerically for several fixed \(b\) and increasing \(n\); those computations illustrate but do not replace the analytic proof.

## Relationship to prior work
Ma, Verchand, Gao and Samworth establish the adaptive minimax rate and, in Proposition 22, construct two Gaussian missing-data laws whose product distributions are close. Their high-missingness case uses the same pointwise clipping geometry but bounds its tail discrepancy coarsely and selects \(r=L/(2\sqrt{\log n})\); their lower-missingness case uses a wider lower clip and a Kullback--Leibler bound with \(r\) carrying an explicit factor \(1/4\). They do not state the exact infimum over the density band, the \(-\tfrac32\log\log n\) critical correction, or the resulting \(1/\sqrt2\) leading lower-bound coefficient for fixed MCAR missingness.

Luo and Gao study adaptive robust confidence intervals under Huber contamination. Their Gaussian lower bound also exploits tail truncation and obtains the \(1/\sqrt{\log n}\) order, but the admissible contamination class is different and the inspected theorem gives order-level separation rather than the exact realisable-missingness modulus above. Ma et al. introduce the underlying realisable missingness model and prove estimation rates, but the inspected material does not state this adaptive-confidence modulus.

## Limitations
The exact formula is for the one-step total-variation projection onto the specific null-side density band \([\phi/(2n),\phi]\). The product-distance statement is an upper bound from tensorization, not an exact product total variation. The confidence-interval consequence is therefore a lower-bound refinement only. It does not establish that \(\log(1/(1-\epsilon))/\sqrt2\) is the exact asymptotic minimax constant, and it does not address varying \(\epsilon\), unknown \(\sigma\), or non-Gaussian base laws. A residual literature risk remains that a general sharp robust-testing theorem could imply the same clipping asymptotic without using the missing-data terminology.

## References
1. T. Ma, K. A. Verchand, C. Gao and R. J. Samworth, *Adaptive confidence intervals with missing data*, arXiv:2609.28336v1, first public 2026-09-23. Relevant items: model equations (2)--(3), Lemma 8, and Proposition 22.
2. Y. Luo and C. Gao, *Adaptive Robust Confidence Intervals*, arXiv:2410.22647. Relevant items: Gaussian location model and the lower-bound construction in Section 4.3.
3. T. Ma, K. A. Verchand, T. B. Berrett, T. Wang and R. J. Samworth, *Estimation beyond Missing (Completely) at Random*, arXiv:2410.10704. Relevant item: the realisable contamination framework and Gaussian mean estimation results.
