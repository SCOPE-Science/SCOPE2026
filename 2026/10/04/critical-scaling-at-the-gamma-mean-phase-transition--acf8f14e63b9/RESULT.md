# Critical scaling at the Gamma mean phase transition
## Finding
Let \(h_\kappa(\alpha)=\Pr\{X_{\alpha,1}\le \kappa\alpha\}\) for \(X_{\alpha,1}\sim\operatorname{Gamma}(\alpha,1)\), and for \(\kappa>1\) let \(m(\kappa)=\min_{\alpha>0}h_\kappa(\alpha)\). For every choice \(\alpha_\kappa\) of a minimizing shape, as \(\delta=\kappa-1\downarrow0\), \[\alpha_\kappa=\frac{1}{3\delta}+\frac{7}{45}+O(\sqrt{\delta}),\] and \[m(1+\delta)=\frac12+\frac{2}{\sqrt{6\pi}}\sqrt{\delta}-\frac{71\sqrt3}{270\sqrt{2\pi}}\delta^{3/2}+O(\delta^2).\] Thus the minimizing Gamma shape diverges on the exact \(1/[3(\kappa-1)]\) scale and the minimum rises above \(1/2\) with an explicit square-root critical law.

The scale parameter is immaterial: if \(X_{{\alpha,\beta}}\sim\operatorname{{Gamma}}(\alpha,\beta)\), then \(X_{{\alpha,\beta}}/\beta\sim\operatorname{{Gamma}}(\alpha,1)\), so the same statement describes the minimum of \(\Pr\{{X_{{\alpha,\beta}}\le\kappa\,\mathbb E X_{{\alpha,\beta}}\}}\) over positive \(\alpha,\beta\).

## Assumptions and scope
The parameter approaches the phase boundary from above: \(\kappa=1+\delta\) with \(\delta>0\) and \(\delta\downarrow0\). The result concerns every global minimizer of the one-dimensional shape problem. It does not assert that the minimizer is unique for each fixed nonasymptotic \(\kappa>1\).

For fixed \(\kappa>1\), the cited Gamma-extreme-value paper proves that \(h_\kappa(\alpha)\to1\) at both ends \(\alpha\downarrow0\) and \(\alpha\to\infty\), and hence that a global minimum exists and exceeds \(1/2\).

## Proof
Put \(\varepsilon=\sqrt{\delta}\), write a candidate shape as \(\alpha=r/\varepsilon^2\), and standardize \(Y_\alpha=(X_{{\alpha,1}}-\alpha)/\sqrt\alpha\). The moving upper endpoint becomes
\[
z=\frac{(1+\delta)\alpha-\alpha}{\sqrt\alpha}=\varepsilon\sqrt r.
\]

The uniform transition expansion of the normalized incomplete Gamma function, equivalently the standard Edgeworth expansion for \(Y_\alpha\), gives for bounded real \(z\), uniformly together with one derivative in \(z\),
\[
\Pr\{{Y_\alpha\le z\}}=\Phi(z)+\phi(z)\left[
\frac{1-z^2}{3\sqrt\alpha}
-\frac{z(2z^4-11z^2+3)}{36\alpha}
-\frac{10z^8-145z^6+399z^4-69z^2-3}{1620\alpha^{{3/2}}}
\right]+O(\alpha^{{-2}}).
\]
The remainder form is supplied by the standard uniform incomplete-Gamma transition expansion; the displayed coefficients can also be reconstructed directly by Stirling expansion of the standardized density. In particular, with \(\phi(0)=1/\sqrt{{2\pi}}\), substitution of \(z=\varepsilon\sqrt r\) and \(\alpha=r/\varepsilon^2\) yields, uniformly for \(r\) in compact subsets of \((0,\infty)\),
\[
h_{{1+\delta}}(r/\delta)
=\frac12+\phi(0)\varepsilon A(r)+\phi(0)\varepsilon^3 B(r)+O(\varepsilon^4),
\]
where
\[
A(r)=\sqrt r+\frac{1}{3\sqrt r},
\qquad
B(r)=-\frac{r^{{3/2}}}{6}-\frac{\sqrt r}{2}-\frac{1}{12\sqrt r}+\frac{1}{540r^{{3/2}}}.
\]

A trial at \(r=1/3\) gives \(m(1+\delta)=1/2+O(\sqrt\delta)\). Any minimizing shape must therefore tend to infinity: otherwise a bounded subsequence would converge to the strictly larger mean-tail probability \(h_1(\alpha)>1/2\), while shapes tending to zero have probability tending to one. Let \(r_\delta=\delta\alpha_{{1+\delta}}\). If \(r_\delta\to0\), the same transition expansion gives after division by \(\sqrt\delta\) a dominant term \(\phi(0)/(3\sqrt{{r_\delta}})\), contradicting the trial upper bound. If \(r_\delta\to\infty\), then either \(z=\sqrt{{\delta r_\delta}}\) stays away from zero, giving a fixed positive excess over \(1/2\), or \(z\to0\), in which case the dominant normalized excess is \(\phi(0)\sqrt{{r_\delta}}\); both again contradict the trial bound. Thus all minimizers localize in one fixed compact interval of \((0,\infty)\).

On that compact interval, \(A\) has the unique minimum
\[
r_0=\frac13,
\qquad
A(r_0)=\frac{2}{\sqrt3},
\qquad
A''(r_0)=\frac{3\sqrt3}{2}.
\]
Hence \(r_\delta\to1/3\). Since the localized minimizer is interior, the just-noted analytic remainder control permits differentiation of the uniform expansion, giving
\[
0=A'(r_\delta)+\delta B'(r_\delta)+O(\delta^{{3/2}}).
\]
At \(r_0=1/3\),
\[
B'(r_0)=-\frac{7\sqrt3}{30},
\qquad
B(r_0)=-\frac{71\sqrt3}{270}.
\]
Taylor expansion around \(r_0\) therefore yields
\[
r_\delta=\frac13+\frac{7}{45}\delta+O(\delta^{{3/2}}),
\]
which is the stated expansion of \(\alpha_\kappa=r_\delta/\delta\). Substituting the minimizer into the probability expansion gives
\[
m(1+\delta)=\frac12+\frac{2}{\sqrt{{6\pi}}}\sqrt\delta
-\frac{71\sqrt3}{270\sqrt{{2\pi}}}\delta^{{3/2}}+O(\delta^2).
\]

## Verification
The algebraic constants were independently replayed by `verify.py` using only the Python standard library. It checks
\[
-\frac{B'(1/3)}{A''(1/3)}=\frac{7}{45}
\]
and evaluates the two-term formulas at \(\delta=0.01\). The resulting shape prediction \(33.488888\ldots\) and minimum prediction \(0.545884182\ldots\) agree closely with the published numerical values \(33.4871\) and \(0.545885\). This numerical comparison is a stress test only; the infinite asymptotic claim is proved by the localization and uniform expansion above.

## Relationship to prior work
Sun, Hu, and Sun introduced exactly the function \(h_\kappa\), proved the qualitative trichotomy around \(\kappa=1\), and for \(\kappa>1\) established existence of a minimum greater than \(1/2\). Their full text gives numerical minimizers, including \(\alpha=33.4871\) at \(\kappa=1.01\), and explicitly calls \(\kappa=1\) a phase transition. It does not state a critical scaling law for the minimizing shape or for the minimum value.

Temme's uniform asymptotic expansion and the NIST DLMF treatment of the incomplete Gamma transition provide the analytic expansion used here. Those sources concern the incomplete Gamma function itself; the new step is the global localization and variational balance that selects \(r=\delta\alpha\to1/3\), followed by the next-order optimization producing \(7/45\) and the cubic correction to the minimum.

## Limitations
The result is asymptotic as \(\kappa\downarrow1\) from above. It does not give a nonasymptotic error constant, a uniqueness theorem for the minimizer at every fixed \(\kappa>1\), or a closed form for the minimum away from the critical regime. Search and source inspection found no statement equivalent to these critical constants, but unindexed or differently phrased prior work remains a residual originality risk.

## References
1. P. Sun, Z.-C. Hu, W. Sun, *The extreme values of two probability functions for the Gamma distribution*, arXiv:2303.17487v1, 30 March 2023.
2. P. Sun, Z.-C. Hu, W. Sun, *The infimum values of two probability functions for the Gamma distribution*, Journal of Inequalities and Applications 2024, Article 5, DOI 10.1186/s13660-024-03081-w.
3. N. M. Temme, *The Asymptotic Expansion of the Incomplete Gamma Functions*, SIAM Journal on Mathematical Analysis 10 (1979), 757–766, DOI 10.1137/0510071.
4. NIST Digital Library of Mathematical Functions, §8.12, *Uniform Asymptotic Expansions for Large Parameter*.
