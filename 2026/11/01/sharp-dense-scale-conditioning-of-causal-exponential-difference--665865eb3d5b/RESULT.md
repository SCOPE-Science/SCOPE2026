# Sharp dense-scale conditioning of causal exponential-difference dilates

## Finding

Fix a real scale ratio \(c>1\) and put \(L=\log c\). For \(a>0\), let
\[
h_a(t)=a^{-1}e^{-t/a}\mathbf 1_{(0,\infty)}(t),\qquad
\psi_c=h_c-h_1,\qquad
N_c^2=\|\psi_c\|_{L^2(0,\infty)}^2=\frac{(c-1)^2}{2c(c+1)}.
\]
For each integer \(j\in\mathbb Z\), define the unit-norm causal dilation
\[
\phi_{j,c}(t)=\frac{c^{-j/2}}{N_c}\psi_c(c^{-j}t),\qquad t>0.
\]
The family \((\phi_{j,c})_{j\in\mathbb Z}\) is a Riesz sequence in \(L^2(0,\infty)\) for every \(c>1\). Its exactly computable Gram entries are
\[
\langle\phi_{j,c},\phi_{j+k,c}\rangle
 =g_{|k|}(c),\qquad
 g_k(c)=\frac{2(c+1)^2c^{3k/2}}
 {(c+c^k)(1+c^k)(1+c^{k+1})},\quad k\ge0.
\]
Writing \(q=c^{-1/2}\), its sharp squared Riesz bounds \(A(c)\), \(B(c)\) are the minimum and maximum over \(\theta\in[-\pi,\pi]\) of the strictly positive continuous function
\[
\mathcal G_c(\theta)=
\frac{\pi(1+q^2-2q\cos\theta)}{L N_c^2}
\sum_{m\in\mathbb Z}
\operatorname{sech}\!\left(\frac{\pi(\theta+2\pi m)}{L}\right).
\]
The maximum occurs at \(\theta=0\). In particular,
\[
B(c)=\frac{2\pi(c+1)}{L(\sqrt c+1)^2}
\sum_{m\in\mathbb Z}\operatorname{sech}\!\left(\frac{2\pi^2m}{L}\right).
\]
The **sharp dense-scale laws** as \(c\downarrow1\), equivalently \(L\downarrow0\), are
\[
\boxed{A(c)\sim\frac{64\pi}{L^3}e^{-\pi^2/L},\qquad
B(c)\sim\frac{\pi}{L},\qquad
\frac{B(c)}{A(c)}\sim\frac{L^2}{64}e^{\pi^2/L}.}
\]
The same optimal infinite-family bounds apply to the one-sided sequence indexed by \(j\ge0\). The theorem concerns the Riesz stability of unshifted **scale-channel functions**; it does not assert a frame for all of \(L^2(0,\infty)\), nor identify the frequency-wise analysis bounds of a translated wavelet filter bank.

## Assumptions and scope

The time variable satisfies \(t>0\), each \(h_a\) vanishes for \(t\le0\), and all Hilbert-space norms and inner products use Lebesgue measure \(dt\). The ratio \(c\) is any fixed real number greater than one, not necessarily integral or dyadic. The definition of sharp Riesz bounds is that, for every finitely supported complex sequence \((u_j)\),
\[
A(c)\sum_j|u_j|^2\le\left\|\sum_j u_j\phi_{j,c}\right\|_2^2
\le B(c)\sum_j|u_j|^2,
\]
with neither constant improvable uniformly over finitely supported sequences. The limits stated above take \(L=\log c\) to zero through all positive real values; no relation between the number of chosen scales and \(c\) is assumed.

## Proof

**1. Exact Gram matrix.** Direct integration gives, for all \(a,b>0\),
\[
\langle h_a,h_b\rangle=\frac1{a+b}.
\]
For \(t>0\), four such terms give
\[
\langle \psi_c,h_{ct}-h_t\rangle
=\frac{1+c^{-1}}{1+t}-\frac1{c+t}-\frac1{1+ct}
=\frac{t(c-1)^2(c+1)}{c(c+t)(1+t)(1+ct)}.
\]
Setting \(t=1\) yields the claimed norm \(N_c^2\). The normalized dilation at scale \(t\) is \(\sqrt t\,(h_{ct}-h_t)/N_c\). Substituting \(t=c^k\), dividing by \(N_c^2\), and using unitary dilation invariance proves the formula for \(g_{|k|}(c)\). Every Gram coefficient is positive, and the explicit expression shows \(g_k(c)=O_c(c^{-3k/2})\) for \(k\to\infty\). Thus the Gram matrix defines a bounded Laurent-convolution operator on \(\ell^2(\mathbb Z)\), with continuous real symbol \(\mathcal G_c(\theta)=\sum_{k\in\mathbb Z}g_{|k|}(c)e^{ik\theta}\).

**2. Mellin diagonalization.** The map \(Uf(x)=e^{x/2}f(e^x)\) is unitary from \(L^2((0,\infty),dt)\) onto \(L^2(\mathbb R,dx)\), and sends \(\phi_{j,c}\) to a translation by \(jL\) of \(H_c=U\phi_{0,c}\). Using the Fourier convention \(\widehat H_c(\xi)=\int_{\mathbb R}e^{-i\xi x}H_c(x)\,dx\), the Gamma integral gives
\[
\widehat H_c(\xi)
=\frac{\Gamma(\tfrac12-i\xi)}{N_c}
 \bigl(c^{-1/2-i\xi}-1\bigr).
\]
By the classical identity \(|\Gamma(\tfrac12+i\xi)|^2=\pi/\cosh(\pi\xi)\),
\[
|\widehat H_c(\xi)|^2
=\frac{\pi}{N_c^2\cosh(\pi\xi)}
\bigl(1+q^2-2q\cos(L\xi)\bigr).
\]
Plancherel and partition into frequency cells of width \(2\pi/L\) show that the Gram symbol equals the alias sum
\[
\mathcal G_c(\theta)=\frac1L\sum_{m\in\mathbb Z}
\left|\widehat H_c\!\left(\frac{\theta+2\pi m}{L}\right)\right|^2,
\]
which gives the claimed hyperbolic-secant representation. Since \(0<q<1\), the first factor is at least \((1-q)^2>0\). The periodized \(\operatorname{sech}\) sum is everywhere positive and continuous, with uniform exponential convergence. Consequently \(0<A(c)\le B(c)<\infty\), establishing the Riesz-sequence assertion.

For finitely supported \((u_j)\), Fourier-series Parseval gives
\[
\left\|\sum_j u_j\phi_{j,c}\right\|_2^2
=\frac1{2\pi}\int_{-\pi}^{\pi}
\mathcal G_c(\theta)\left|\sum_j u_je^{ij\theta}\right|^2d\theta.
\]
Normalized Dirichlet-polynomial/Fejér packets concentrate at any prescribed \(\theta\); hence the essential minimum and maximum of the continuous symbol are precisely the best possible Riesz constants, for both the two-sided and one-sided index sets. Because \(g_k(c)>0\), the cosine-series representation gives \(\mathcal G_c(\theta)\le\mathcal G_c(0)\). Simplifying \((1-q)^2/N_c^2=2(c+1)/(\sqrt c+1)^2\) yields the formula for \(B(c)\).

**3. Dense-scale upper bound.** Put
\[
D_L(\theta)=1+e^{-L}-2e^{-L/2}\cos\theta,
\qquad
P_L(\theta)=\sum_{m\in\mathbb Z}
\operatorname{sech}\!\left(\frac{\pi(\theta+2\pi m)}L\right).
\]
Then \(\mathcal G_c=\pi D_LP_L/(LN_c^2)\). At \(\theta=0\),
\[
P_L(0)=1+O(e^{-2\pi^2/L}),\quad
\frac{D_L(0)}{N_c^2}=
\frac{2(c+1)}{(\sqrt c+1)^2}=1+O(L^2).
\]
The exact maximum identity from Step 2 therefore yields \(B(c)\sim\pi/L\).

**4. Sharp lower-bound asymptotic.** At the antipodal frequency \(\theta=\pi\), the nearest terms of the periodization are those indexed by \(m=0,-1\), and
\[
P_L(\pi)=4e^{-\pi^2/L}(1+o(1)),\qquad
\frac{D_L(\pi)}{N_c^2}=\frac{2(c+1)}{(\sqrt c-1)^2}
\sim\frac{16}{L^2}.
\]
It follows that \(\mathcal G_c(\pi)\sim64\pi L^{-3}e^{-\pi^2/L}\). To show that this is the asymptotic global minimum, use evenness and periodicity to restrict \(\theta\) to \([0,\pi]\) and set \(u=\pi-\theta\). Split into two ranges.

If \(0\le u\le L\log(1/L)\), the two nearest translated hyperbolic secants dominate uniformly, giving
\[
P_L(\pi-u)=4e^{-\pi^2/L}\cosh(\pi u/L)(1+o(1))
\ge P_L(\pi)(1-o(1)).
\]
Also \(D_L(\pi-u)/D_L(\pi)=1-O(u^2)=1-o(1)\), uniformly on this range. Hence \(\mathcal G_c(\pi-u)\ge (1-o(1))\mathcal G_c(\pi)\).

If \(u\ge L\log(1/L)\), then \(P_L(\pi-u)\ge\operatorname{sech}(\pi(\pi-u)/L)\ge e^{-\pi(\pi-u)/L}\), while \(D_L(\pi-u)\ge(1-e^{-L/2})^2\). Dividing by the estimates at \(\pi\) yields a uniform bound of the form
\[
\frac{\mathcal G_c(\pi-u)}{\mathcal G_c(\pi)}
\ge C L^2e^{\pi u/L}
\ge C L^{2-\pi}\longrightarrow\infty
\]
for some absolute constant \(C>0\) and sufficiently small \(L\). Together the two ranges prove \(A(c)\sim\mathcal G_c(\pi)\), without assuming that \(\pi\) is the exact minimizer for every fixed \(c\). Taking the ratio of the two proven asymptotics gives the claimed sharp condition-number law.

## Verification

The accompanying `CHECK.py` independently evaluates \(84\) exact rational overlap identities, checks \(21\) finite spectral comparisons and sampled extrema, and checks \(8\) dense-scale asymptotic approximations for \(L\in\{0.30,0.20,0.15,0.10\}\). It uses only the Python standard library. Run `python CHECK.py` in the directory containing this document. The checker does not establish positivity on the continuum, a global minimum, or any infinite limiting claim; these follow from Steps 2–4. The exact rational tests target the nontrivial factorization in Step 1. The spectral comparisons target normalization and the \(1/L\) aliasing factor in Step 2. The asymptotic approximations target the constants \(64\pi\), \(\pi\), and \(1/64\).

## Relationship to prior work

Pedersen, Lindeberg and Gerstoft introduce the difference-of-truncated-exponentials channel and compute frequency-wise energy-capture frame bounds for a multiscale filtering bank. Their Section 5.1 introduces a channel Gram matrix and discusses interchannel overlap, but does not determine its exact infinite-scale Riesz spectrum or dense-spacing singular asymptotic. The present claim concerns normalized **time-domain scale functions**, whose Gram symbol is a Mellin alias sum. It does not restate or contradict the source's Fourier-domain capture bounds.

Lindeberg's preceding work develops the causal smoothing kernels, time-recursive wavelets, and normalization across scales. Classical Mellin transform and shift-invariant Riesz theory supply the general diagonalization method, but the explicit Gamma/hyperbolic-secant symbol and the essential-singularity conditioning coefficient for this concrete causal family require the specialized computations above.

## Limitations

The Riesz sequence is not a basis for all of \(L^2(0,\infty)\). The quantitative estimates concern only simultaneous variations of coefficients among unshifted dilated channels, not arbitrary time-translated wavelet coefficients or discrete implementations. The global minimizing frequency at a fixed \(c\) is defined by a one-dimensional periodic minimum; the result does not assert that it always equals \(\pi\), only the proved asymptotic equivalence as \(c\downarrow1\). An unlocated historical identity for Mellin periodizations could overlap implicitly with the explicit symbol, although no inspected source states the full sharp conditioning law.

## References

1. J. E. Pedersen, T. Lindeberg and P. Gerstoft, *Frame bounds and bandwidth tiling for time-causal bandpass wavelets*, arXiv:2609.17201, first public September 15, 2026, Sections 2, 4.3, 5.1. https://arxiv.org/html/2609.17201
2. T. Lindeberg, *Time-causal and time-recursive wavelets*, arXiv:2510.05834, first public October 7, 2025, Sections 2.8 and 3.2. https://arxiv.org/html/2510.05834
3. Classical Fourier--Mellin identities and the Gamma reflection identity are applied explicitly in the proof; no unprovided research theorem is required.
