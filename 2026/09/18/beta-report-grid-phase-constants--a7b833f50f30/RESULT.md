# Sharp grid-phase constants for two-site Beta report quantization

## Setting

Consider one simple hypothesis tested from two independent sites. Under the null,
\[
U_1,U_2\stackrel{\mathrm{iid}}\sim \operatorname{Unif}(0,1),
\]
and under the alternative,
\[
U_1,U_2\stackrel{\mathrm{iid}}\sim \operatorname{Beta}(1,\theta),
\qquad \theta>1,
\]
with density \(g_\theta(u)=\theta(1-u)^{\theta-1}\). Each site is allowed to report only one of \(m\) values, after which the center applies the most powerful randomized test measurable with respect to the two reports.

Dubey and Huo (2026) prove that, under their regularity conditions, the optimal loss over all \(m\)-cell componentwise reports is \(\Theta(m^{-2})\). Their numerical study for equal-width p-value cells also reports grid-alignment oscillations in \(m^2\) times the loss. The result below resolves those oscillations exactly for a natural likelihood-coordinate lattice and identifies the phase minimizing its leading constant.

Set
\[
E_s=-\log(1-U_s),\qquad s=1,2.
\]
Then under the null \(E_s\sim\operatorname{Exp}(1)\), under the alternative \(E_s\sim\operatorname{Exp}(\theta)\), and the joint likelihood ratio is
\[
\theta^2\exp\{-(\theta-1)(E_1+E_2)\}.
\]
For a fixed level \(\alpha\in(0,1)\), let \(a=a_\alpha>0\) be the unique solution of
\[
\alpha=1-e^{-a}(1+a),
\]
and write \(q=e^{-a}\). The oracle Neyman--Pearson test rejects when
\[
E_1+E_2<a,
\]
with power
\[
\pi^*_{\theta,\alpha}=1-e^{-\theta a}(1+\theta a).
\]

## A phased log-evidence report family

Fix \(\rho\in[0,1]\) and an integer \(L\ge2\), put
\[
h=\frac{a}{L-1+\rho},\qquad m=L+1,
\]
and let each site report the cell containing \(E\):
\[
I_j=[jh,(j+1)h),\quad j=0,\ldots,L-1,
\qquad I_L=[Lh,\infty).
\]
Equivalently, in the original p-value coordinate the finite thresholds are
\[
1-e^{-jh},\qquad j=0,\ldots,L.
\]
The report construction depends on \(\alpha\) but not on \(\theta\).

Let \(d_{\theta,L,\rho}\) denote oracle power minus the power of the most powerful level-\(\alpha\) test based on the two reports.

## Main theorem: an exact phase law

Define
\[
\Phi(\rho)=
\begin{cases}
\dfrac{1-3\rho^2}{6},&0\le \rho\le \tfrac12,\\[6pt]
\dfrac{1-3(1-\rho)^2}{6},&\tfrac12\le \rho\le1.
\end{cases}
\]
Equivalently,
\[
\Phi(\rho)=\frac{1-3\min\{\rho,1-\rho\}^2}{6}.
\]
Then, for every fixed \(\theta>1\), \(\alpha\in(0,1)\), and \(\rho\in[0,1]\),
\[
\boxed{
 d_{\theta,L,\rho}
 =
 \theta^2(\theta-1)e^{-\theta a}a\,\Phi(\rho)\,h^2
 +O(h^3).
}
\]
Hence
\[
\boxed{
 (L-1+\rho)^2d_{\theta,L,\rho}
 \longrightarrow
 \theta^2(\theta-1)e^{-\theta a}a^3\Phi(\rho),
}
\]
and, since \(m=L+1\), the same limit holds with \(m^2d_{\theta,L,\rho}\).

The phase function is uniquely minimized at
\[
\boxed{\rho=\tfrac12,\qquad \Phi(1/2)=\frac1{24}.}
\]
At either aligned endpoint, \(\Phi(0)=\Phi(1)=1/6\). Thus within this log-evidence lattice family, a half-cell shift divides the leading \(m^{-2}\) power-loss constant by exactly four:
\[
\boxed{
 d_{\theta,L,1/2}
 \sim
 \frac{\theta^2(\theta-1)e^{-\theta a}a^3}{24m^2}.
}
\]
The phase choice \(\rho=1/2\) is simultaneously optimal within this family for every \(\theta>1\), because \(\Phi\) is independent of \(\theta\).

This is a phase-optimality statement for the displayed lattice family, not a claim that these reports attain the globally best constant over all measurable \(m\)-cell reports.

## Exact finite-resolution formula

The asymptotic result follows from a closed finite-\(L\) expression. Write
\[
r=e^{-h}.
\]
For a rate \(\lambda>0\), define the probability of the lower triangle of a cell by
\[
A^{<}_{\lambda}(\tau,h)
=1-e^{-\lambda\tau h}(1+\lambda\tau h),
\qquad 0\le\tau\le1,
\]
and the probability below a line crossing both upper edges by
\[
A^{>}_{\lambda}(\tau,h)
=1-2e^{-\lambda h}
+e^{-\lambda\tau h}\{1-\lambda h(2-\tau)\},
\qquad 1\le\tau\le2.
\]
Because
\[
\frac{a}{h}=L-1+\rho,
\]
all report squares with index sum at most \(L-3\) lie wholly inside the oracle region. Only the two adjacent diagonals
\[
A:\ i+j=L-2,
\qquad
B:\ i+j=L-1
\]
intersect the oracle boundary.

Their total oracle boundary masses under the null and alternative are
\[
N_0=(L-1)r^{L-2}A^{>}_{1}(1+\rho,h)
+Lr^{L-1}A^{<}_{1}(\rho,h),
\]
\[
N_1=(L-1)r^{\theta(L-2)}A^{>}_{\theta}(1+\rho,h)
+Lr^{\theta(L-1)}A^{<}_{\theta}(\rho,h).
\]
The full masses of diagonal \(A\) are
\[
F_{0A}=(L-1)r^{L-2}(1-r)^2,
\qquad
F_{1A}=(L-1)r^{\theta(L-2)}(1-r^\theta)^2,
\]
and those of diagonal \(B\) are
\[
F_{0B}=Lr^{L-1}(1-r)^2,
\qquad
F_{1B}=Lr^{\theta(L-1)}(1-r^\theta)^2.
\]
For all sufficiently large \(L\), the exact report-space Neyman--Pearson deficit is therefore
\[
\boxed{
 d_{\theta,L,\rho}
 =N_1-\frac{N_0}{F_{0A}}F_{1A},
 \qquad 0\le\rho<\frac12,
}
\]
where the report test randomizes on diagonal \(A\), while
\[
\boxed{
 d_{\theta,L,\rho}
 =N_1-F_{1A}
 -\frac{N_0-F_{0A}}{F_{0B}}F_{1B},
 \qquad \frac12\le\rho\le1,
}
\]
where it rejects diagonal \(A\) and randomizes on \(B\). At \(\rho=1/2\), the randomization probability on \(B\) is \(O(h)\), so the two asymptotic branches join continuously.

These formulas also give an exact finite-resolution evaluator without numerical integration.

## Proof

For a regular report bin \(I_j\), the null and alternative probabilities are
\[
P_0(I_j)=r^j(1-r),
\qquad
P_1(I_j)=r^{\theta j}(1-r^\theta).
\]
Thus its report likelihood ratio is
\[
\ell_j
=r^{(\theta-1)j}\frac{1-r^\theta}{1-r},
\]
which strictly decreases with \(j\). The joint report likelihood ratio on a regular square therefore depends only on \(i+j\) and strictly decreases from diagonal to diagonal. Cells involving the tail \(I_L\) have still smaller likelihood ratio than the two diagonals intersecting the oracle boundary. Consequently the report-space Neyman--Pearson test fills the diagonals in increasing order of \(i+j\), with randomization only at the last accepted likelihood-ratio level.

The geometry above shows that the entire difference between oracle and report power is concentrated on diagonals \(A\) and \(B\). Integrating the exponential densities over the two partial-square shapes gives \(N_0,N_1\), while integrating over full squares gives \(F_{0A},F_{1A},F_{0B},F_{1B}\). This proves the exact formulas.

For the asymptotics, the elementary Taylor expansions are
\[
A^{<}_{\lambda}(\rho,h)
=\frac{\lambda^2\rho^2}{2}h^2
-\frac{\lambda^3\rho^3}{3}h^3
+O(h^4),
\]
\[
A^{>}_{\lambda}(1+\rho,h)
=\lambda^2\left(\frac12+\rho-\frac{\rho^2}{2}\right)h^2
+\lambda^3\left(\frac{\rho^3}{3}-\rho-\frac13\right)h^3
+O(h^4).
\]
Using \(L=a/h+1-\rho\) in the exact formulas gives
\[
\frac{N_0}{F_{0A}}=\frac12+\rho+O(h).
\]
Thus \(N_0<F_{0A}\) eventually when \(\rho<1/2\); when \(\rho>1/2\),
\[
\frac{N_0-F_{0A}}{F_{0B}}=\rho-\frac12+O(h).
\]
Substitution into the exact deficit formulas and cancellation of the order-\(h\) terms yields
\[
 d_{\theta,L,\rho}
 =a\theta^2(\theta-1)e^{-\theta a}
 \left(\frac16-\frac{\rho^2}{2}\right)h^2+O(h^3)
\]
for \(\rho<1/2\), and
\[
 d_{\theta,L,\rho}
 =a\theta^2(\theta-1)e^{-\theta a}
 \left(-\frac13+\rho-\frac{\rho^2}{2}\right)h^2+O(h^3)
\]
for \(\rho>1/2\). These are exactly the two branches of \(\Phi\). Direct expansion at \(\rho=1/2\) gives the common coefficient \(1/24\), completing the proof.

## Numerical specialization: the Beta(1,2) benchmark

At \(\alpha=0.05\),
\[
a=0.355361510698662\ldots,
\qquad
\pi^*_{2,0.05}=0.159540842753525\ldots.
\]
For the half-cell phase \(\rho=1/2\), the asymptotic constant is
\[
\frac{e^{-2a}a^3}{6}
=0.003674487934318\ldots.
\]
Exact finite-resolution evaluation gives

| \(m\) | power deficit | relative deficit | \(m^2\) deficit |
|---:|---:|---:|---:|
| 8 | \(1.0867749303\times10^{-4}\) | \(0.06812\%\) | 0.00695536 |
| 16 | \(1.9468517943\times10^{-5}\) | \(0.01220\%\) | 0.00498394 |
| 64 | \(9.6583044827\times10^{-7}\) | \(0.000605\%\) | 0.00395604 |
| 256 | \(5.7104688425\times10^{-8}\) | \(0.0000358\%\) | 0.00374241 |
| 512 | \(1.4145701711\times10^{-8}\) | \(0.00000887\%\) | 0.00370821 |

For comparison, Dubey and Huo report a \(0.72\%\) relative deficit at \(m=8\) for equal-width p-value cells in the same \(K=1,S=2,\operatorname{Beta}(1,2),\alpha=0.05\) benchmark. The half-phased log-evidence lattice therefore has about 10.6 times smaller deficit at that resolution. This finite-\(m\) comparison is between two explicit report families and does not assert global optimality of the log-evidence design.

## Relation to prior work

Dubey and Huo, *Report resolution in federated multiple testing under family-wise error control* (2026), prove the class-optimal \(m^{-2}\) exponent for a single hypothesis under their smoothness assumptions, including arbitrary measurable report cells in the lower bound. They explicitly observe grid-alignment oscillations for equal-width reports but do not give the phase-dependent leading constant derived here.

The \(m^{-2}\) phenomenon itself is not new to quantization theory. Poor (1988) develops general second-order fine-quantization formulas for detection and estimation, including uniform and companded quantizers. Gupta and Hero (2003) and later high-rate decentralized-detection work study asymptotically optimal quantization for detection criteria such as error exponents. Those results are treated as prior art for the general high-rate mechanism. The claim here is narrower: the exact finite boundary formulas and the explicit phase curve \(\Phi(\rho)\) for this two-site fixed-level Beta testing problem, together with its factor-four half-cell improvement and the \(\theta\)-independence of the phase-optimal grid.

To the best of our knowledge, these exact statements were not located in the inspected sources or targeted searches for shifted/offset high-rate Neyman--Pearson quantizers and p-value quantization.

## Limitations

The result treats one hypothesis, two independent sites, and a common \(\operatorname{Beta}(1,\theta)\) alternative. It does not give the globally optimal asymptotic constant over arbitrary measurable \(m\)-cell reports. It permits the standard Neyman--Pearson randomization required when a report likelihood-ratio atom straddles the target size. The phase law has not been extended here to multiplicity \(K\ge2\), heterogeneous site alternatives, or general decreasing p-value densities.

## References

1. Prasanjit Dubey and Xiaoming Huo, *Report resolution in federated multiple testing under family-wise error control*, arXiv:2609.19708 (2026). https://arxiv.org/abs/2609.19708
2. H. Vincent Poor, *Fine Quantization in Signal Detection and Estimation*, IEEE Transactions on Information Theory 34(5), 960--972 (1988). https://doi.org/10.1109/18.21219
3. Vivek K. Goyal and Alfred O. Hero III, *High-rate vector quantization for detection*, IEEE Transactions on Information Theory 49(8), 1951--1969 (2003). https://doi.org/10.1109/TIT.2003.814482
4. Joffrey Villard and Pascal Bianchi, *High-Rate Vector Quantization for the Neyman-Pearson Detection of Correlated Processes*, arXiv:1004.5529 (2010). https://arxiv.org/abs/1004.5529
