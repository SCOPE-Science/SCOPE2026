# Poisson and Gumbel laws for one-flip instability in Gaussian binary MIMO

## Result

Consider the rectangular Gaussian binary MIMO model
\[
y=\sqrt{\rho_N/N}\,H x^\star+w,
\qquad x^\star\in\{\pm1\}^N,
\]
where \(H\in\mathbb R^{m_N\times N}\) has i.i.d. \(N(0,1)\) entries, \(w\sim N(0,I_{m_N})\) is independent, and
\[
0<a\le \alpha_N:=m_N/N\le b<\infty.
\]
Let
\[
f(x)=\|y-\sqrt{\rho_N/N}\,Hx\|_2^2
\]
and let \(K_N\) be the number of Hamming-distance-one neighbors of \(x^\star\) having strictly smaller objective value than \(x^\star\).

Set
\[
b_N=2\log N-\log\log N,
\qquad \tau_N=\alpha_N\rho_N.
\]
If
\[
\tau_N=b_N+c_N,\qquad c_N\to c\in\mathbb R,
\]
then
\[
\boxed{K_N\ \Rightarrow\ \operatorname{Poisson}(\lambda_c)},
\qquad
\boxed{\lambda_c=\frac{e^{-c/2}}{2\sqrt\pi}}.
\]
Consequently,
\[
\boxed{
\Pr\{x^\star\text{ is a strict one-bit local minimum}\}
\longrightarrow
\exp\!\left(-\frac{e^{-c/2}}{2\sqrt\pi}\right).
}
\]
The limit is uniform over deterministic transmitted words \(x^\star\), by column-sign symmetry.

For the square model \(m_N=N\), this resolves the full \(O(1)\) critical window for the one-bit obstruction underlying the converse in Papailiopoulos (2026). That paper proves that a one-bit neighbor beats the truth with probability tending to one when
\(\rho_N\le 2\log N-\log\log N-s_N\), \(s_N\to\infty\), and explicitly notes that its theorem does not determine the complete lower-order transition window. Its introduction also gives the heuristic \(NQ(\sqrt\rho)\asymp1\). The statement above identifies the limiting law inside that window.

## Gumbel local-stability threshold

For each realization, define the one-flip local-stability threshold
\[
\rho_{\mathrm{loc},N}
=
\inf\{\rho>0: x^\star\text{ has no improving Hamming-one neighbor at SNR }\rho\}.
\]
Each individual one-bit gap changes sign at most once as \(\rho\) increases, so this threshold is well defined almost surely. The Poisson law gives
\[
\boxed{
\frac{\alpha_N\rho_{\mathrm{loc},N}-b_N+\log(4\pi)}{2}
\ \Rightarrow\ G,
}
\]
where \(G\) is standard Gumbel:
\[
\Pr\{G\le x\}=e^{-e^{-x}}.
\]
Thus the random SNR at which the planted word becomes one-flip stable has an explicit second-order centering, scale, and limiting distribution.

## Decision-theoretic consequence

Put a uniform prior on \(x^\star\in\{\pm1\}^N\). With Gaussian noise, maximum likelihood is MAP. Whenever a one-bit neighbor has lower objective value, the transmitted word is not a MAP minimizer. Column-sign symmetry makes this event have the same probability for every transmitted word. Hence, at \(\alpha_N\rho_N=b_N+c+o(1)\), every detector \(\widehat x\) obeys
\[
\boxed{
\liminf_{N\to\infty}\ \sup_{x^\star}
\Pr\{\widehat x\ne x^\star\}
\ge
1-\exp\!\left(-\frac{e^{-c/2}}{2\sqrt\pi}\right).
}
\]
This is only a lower bound on the full ML block-error probability: competitors at Hamming distance two or larger may create additional errors.

## Proof

By multiplying column \(i\) of \(H\) by \(x_i^\star\), it suffices to take \(x^\star=\mathbf1\). Write \(h_i\) for column \(i\), and \(s_N=\sqrt{\rho_N/N}\). Flipping bit \(i\) changes the residual from \(w\) to \(w+2s_Nh_i\), so
\[
f(\mathbf1^{(i)})-f(\mathbf1)
=4\left(\frac{\rho_N}{N}\|h_i\|_2^2
+\sqrt{\frac{\rho_N}{N}}\,h_i^Tw\right).
\]
Thus neighbor \(i\) improves exactly when
\[
h_i^Tw<-s_N\|h_i\|_2^2. \tag{1}
\]

Condition on \(w\). The columns \(h_i\) are independent, so the \(N\) events in (1) are conditionally i.i.d. Let their common conditional probability be \(p_N(w)\). Put \(r=\|w\|_2\), rotate so that \(w/r\) is the first coordinate direction, and let \(g=h_i^Tw/r\sim N(0,1)\). Then
\[
p_N(w)=\Pr\left\{g<-\frac{s_N\|h_i\|_2^2}{r}\ \middle|\ w\right\}. \tag{2}
\]

Take \(\varepsilon_N=N^{-1/4}\). Standard chi-square concentration gives
\[
\Pr\left\{\left|\frac{\|w\|_2^2}{m_N}-1\right|>\varepsilon_N\right\}
=e^{-\Omega(\sqrt N)}
\]
and, for an independent Gaussian column,
\[
\Pr\left\{\left|\frac{\|h_i\|_2^2}{m_N}-1\right|>\varepsilon_N\right\}
=e^{-\Omega(\sqrt N)}.
\]
On the typical noise event, sandwiching (2) by the typical column-norm event yields
\[
Q\!\left((1+O(\varepsilon_N))\sqrt{\tau_N}\right)-e^{-\Omega(\sqrt N)}
\le p_N(w)\le
Q\!\left((1-O(\varepsilon_N))\sqrt{\tau_N}\right)+e^{-\Omega(\sqrt N)}, \tag{3}
\]
uniformly over such \(w\). Since \(\tau_N=2\log N+O(\log\log N)\), we have \(\tau_N\varepsilon_N\to0\); Mills' ratio therefore implies
\[
p_N(w)=(1+o(1))Q(\sqrt{\tau_N}) \tag{4}
\]
uniformly on the typical noise event. The exponentially small errors in (3) are negligible on the \(1/N\) scale.

Again by Mills' ratio,
\[
\begin{aligned}
NQ(\sqrt{\tau_N})
&=(1+o(1))\frac{N e^{-\tau_N/2}}{\sqrt{2\pi\tau_N}}\\
&\longrightarrow \frac{e^{-c/2}}{2\sqrt\pi}=\lambda_c.
\end{aligned}
\]
Conditional on \(w\),
\[
K_N\mid w\sim\operatorname{Binomial}(N,p_N(w)).
\]
On the typical noise event, \(Np_N(w)\to\lambda_c\) uniformly and \(p_N(w)\to0\), so the conditional binomial law converges uniformly to \(\operatorname{Poisson}(\lambda_c)\). The atypical noise event has probability \(o(1)\), proving the unconditional Poisson limit.

The local-minimum probability is the zero-count probability. For the Gumbel statement, evaluate it at
\[
\alpha_N\rho=b_N-\log(4\pi)+2x.
\]
Then \(\lambda=e^{-x}\), hence
\[
\Pr\{\alpha_N\rho_{\mathrm{loc},N}\le b_N-\log(4\pi)+2x\}
\to e^{-e^{-x}}.
\]
The minimax bound follows from the uniform-prior MAP argument described above.

## Relation to prior work

Papailiopoulos, *Polynomial-Time MIMO Detection at the Maximum-Likelihood Threshold*, arXiv:2609.19405 (2026), proves polynomial-time exact recovery for the square model at every \(\rho\ge2\log N\), and a one-bit-neighbor ML converse below \(2\log N-\log\log N-s_N\) for diverging \(s_N\). The paper predicts the one-bit transition from \(NQ(\sqrt\rho)\), but does not state a Poisson law, a Gumbel one-flip stability threshold, or the rectangular effective-SNR form above.

Hu and Lu, *The Limiting Poisson Law of Massive MIMO Detection with Box Relaxation*, arXiv:2006.08416 / IEEE JSAIT 1(3), 2020, prove a Poisson/Gumbel transition for the errors of the box-relaxation decoder. That is a different statistic and has square-model refined threshold \(4\log N-2\log\log N+O(1)\), rather than the one-bit ML obstruction treated here.

Targeted searches for one-bit/Hamming-one MIMO Poisson laws, local-minimum Gumbel laws, and the exact \(2\log N-\log\log N+O(1)\) one-bit window did not locate an equivalent theorem. Because the proof is short once conditional independence is exposed, an unstated folklore version remains a material originality risk.

## Limitations

The theorem concerns only Hamming-distance-one competitors. It does **not** determine the full lower-order threshold for maximum-likelihood recovery, because multi-bit competitors may matter in the same window. It assumes i.i.d. real Gaussian channels and Gaussian noise, with aspect ratio bounded away from zero and infinity. No claim is made for correlated channels, non-Gaussian ensembles, coded transmission, finite-precision algorithms, or the global landscape away from the planted word.

## References

1. D. Papailiopoulos, *Polynomial-Time MIMO Detection at the Maximum-Likelihood Threshold*, arXiv:2609.19405, 2026. https://arxiv.org/abs/2609.19405
2. H. Hu and Y. M. Lu, *The Limiting Poisson Law of Massive MIMO Detection with Box Relaxation*, arXiv:2006.08416, 2020; IEEE Journal on Selected Areas in Information Theory 1(3):695-704. https://arxiv.org/abs/2006.08416
