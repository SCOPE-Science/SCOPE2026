# Sharp reentrant zero-free phase for first jets of fractional binomial kernels

## Finding
For each real \(0<\beta\le1\), let \(\mathcal H_\beta\) be the analytic reproducing-kernel Hilbert space on \(\mathbb D=\{z\in\mathbb C:|z|<1\}\) with kernel
\[
K_\beta(z,w)=(1-z\overline w)^{-\beta}.
\]
For a constant coefficient pair \((c,d)\in\mathbb C^2\setminus\{(0,0)\}\), let \(B_{\beta;c,d}\) be the Hermitian Gram kernel of the functionals \(f\mapsto c f(z)+d f'(z)\). Then the exact zero-free classification on \(\mathbb D\times\mathbb D\) is:

* For \(0<\beta<1\), the kernel is zero-free if and only if \(c=0\), or \(d=0\), or \(cd\ne0\) and \(|d/c|\ge 2/\sqrt{1-\beta}\).
* For \(\beta=1\), the kernel is zero-free if and only if \(c=0\) or \(d=0\).

Thus, for every \(0<\beta<1\), both pure value evaluation and pure first-derivative evaluation have zero-free Gram kernels; their mixtures have zeros below a **sharp finite threshold**, but become zero-free again above that threshold. The borderline value belongs to the zero-free regime. For the Hardy endpoint \(\beta=1\), the finite upper threshold escapes to infinity and every nontrivial finite mixture has zeros.

For the normalized positive real ratio \(c=1,d=t>0\), the two boundary-variable zeros at the sharp threshold \(t=2/\sqrt{1-\beta}\) have \(z=\overline w=-\sqrt{1-\beta}\pm i\sqrt\beta\) and occur **only on the excluded unit circles**, not in the open bidisk.

## Assumptions and scope
The binomial series \(K_\beta(z,w)=\sum_{n\ge0}(\beta)_n(z\overline w)^n/n!\) has strictly positive coefficients. Hence it defines an analytic Hilbert space with norm \(\|\sum a_nz^n\|^2=\sum_{n\ge0}|a_n|^2 n!/(\beta)_n\). Every point evaluation and first derivative evaluation is continuous by local uniform convergence of the kernel and its derivatives. The Gram definition, with inner product linear in the first variable, is
\[
B_{\beta;c,d}(z,w)=|c|^2K_\beta+d\overline c\,\partial_z K_\beta+c\overline d\,\partial_{\overline w}K_\beta+|d|^2\partial_z\partial_{\overline w}K_\beta.
\]
The kernel is holomorphic in \(z\), antiholomorphic in \(w\), and strictly positive on its diagonal. The result is about its off-diagonal zeros; the parameter pair is constant in the evaluation point. The result covers \(0<\beta\le1\), not the ordinary Bergman value \(\beta=2\).

## Proof
**Reduction to a polynomial.** Direct differentiation yields, with \(u=z\overline w\),
\[
\partial_zK_\beta=\frac{\beta\overline w}{(1-u)^{\beta+1}},\quad
\partial_{\overline w}K_\beta=\frac{\beta z}{(1-u)^{\beta+1}},\quad
\partial_z\partial_{\overline w}K_\beta=\frac{\beta(1+\beta u)}{(1-u)^{\beta+2}}.
\]
When \(cd\ne0\), multiplying the entire Gram kernel by \(|c|^{-2}\) permits \(c=1\). A simultaneous rotation of its two evaluation points replaces the complex coefficient \(d/c\) by its absolute value \(t=|d/c|\). Set \(a=z\) and \(b=\overline w\). The numerator of the normalized Gram kernel is the polynomial
\[
P_{\beta,t}(a,b)=(1-ab)^2+\beta t(a+b)(1-ab)+\beta t^2(1+\beta ab),
\]
so that \(B_{\beta;1,t}(z,w)=P_{\beta,t}(z,\overline w)/(1-z\overline w)^{\beta+2}\). The denominator is nowhere zero in the bidisk.

**Exact boundary-zero threshold.** On the distinguished boundary \(|a|=|b|=1\), write \(a=e^{i(\psi+\delta)}\) and \(b=e^{i(\psi-\delta)}\), with real \(\psi,\delta\). Multiplying by the nonzero phase \(e^{-2i\psi}\) gives
\[
\begin{aligned}
\operatorname{Re}(e^{-2i\psi}P_{\beta,t})
  &=\beta(\beta+1)t^2-(4+2\beta t^2)\sin^2\psi,\\
\operatorname{Im}(e^{-2i\psi}P_{\beta,t})
  &=-2\beta t\sin\psi\,(2\cos\delta+t\cos\psi).
\end{aligned}
\]
The real equation forces
\[
\sin^2\psi=\frac{\beta(\beta+1)t^2}{4+2\beta t^2}\in(0,1),
\]
so \(\sin\psi\ne0\), and the imaginary equation then forces \(\cos\delta=-t\cos\psi/2\). These conditions are solvable on the torus precisely when \(t^2\cos^2\psi\le4\). On eliminating \(\psi\), this is equivalent to
\[
Q_\beta(t^2):=\beta(1-\beta)t^4+4(1-2\beta)t^2-16\le0.
\]
For \(0<\beta<1\), the exact factorization
\[
Q_\beta(X)=\beta(1-\beta)\left(X-\frac4{1-\beta}\right)\left(X+\frac4\beta\right)
\]
shows that torus zeros occur exactly for \(0<t\le T_\beta:=2/\sqrt{1-\beta}\). For \(\beta=1\), the quantity \(Q_1(t^2)=-4t^2-16\) is negative for all finite \(t>0\), so there are torus zeros for every finite mixture.

**The zero side is genuinely interior.** Suppose \(0<\beta<1\) and \(0<t<T_\beta\), or \(\beta=1\) and \(t>0\). Choose \(\psi\in(0,\pi/2)\) with the displayed sine, and \(\delta\in(0,\pi)\) with the displayed cosine. At this torus zero, the Jacobian of the two real equations with respect to \((\psi,\delta)\) is nonzero: its diagonal entries, after arranging the real and imaginary components, are
\[
-2(4+2\beta t^2)\sin\psi\cos\psi\ne0,
\qquad 4\beta t\sin\psi\sin\delta\ne0,
\]
while the real component has zero \(\delta\)-derivative. Replace \((a,b)\) by \((r e^{i(\psi+\delta)},r e^{i(\psi-\delta)})\). The real implicit function theorem preserves the common zero with continuously adjusted angles for all \(r<1\) sufficiently close to \(1\). These are actual bidisk zeros.

**The zero-free side.** Fix \(0<\beta<1\). For \(t>T_\beta\) there are no zeros on the distinguished boundary. Moreover, as \(t\to\infty\), the polynomial \(t^{-2}P_{\beta,t}(a,b)\) converges uniformly on the closed bidisk to \(\beta(1+\beta ab)\), whose modulus is at least \(\beta(1-\beta)>0\). Thus, at all sufficiently large \(t\), there are no zeros even on the closed bidisk.

For each \(t>T_\beta\) and \(|a|=1\), the argument principle counts zeros of the polynomial in \(b\) inside \(\mathbb D\). Because the boundary has no zeros, this integer is locally constant in the connected parameter space \((T_\beta,\infty)\times\partial\mathbb D\). It is zero at sufficiently large \(t\), so it is zero for every such \(t\) and every \(|a|=1\). Fixing any such \(t\), the argument principle in the other variable now shows that the number of zeros in \(a\in\mathbb D\) is constant as \(b\) varies in the connected disk. At \(b=0\) we have
\[
P_{\beta,t}(a,0)=1+\beta t a+\beta t^2,
\]
whose unique root satisfies \(|a|=(1+\beta t^2)/(\beta t)>1\); indeed \(1+\beta t^2-\beta t>0\) for \(0<\beta\le1\). Therefore there are no bidisk zeros for any \(t>T_\beta\).

At \(t=T_\beta\), an interior zero would persist, with \(b\) fixed, for slightly larger \(t\) by Rouché's theorem applied to a small circle around that zero as a root in \(a\). This contradicts the just-proved zero-free property. Hence the threshold is inclusive.

**Pure jets.** If \(d=0\), the Gram kernel is \(|c|^2(1-u)^{-\beta}\), hence zero-free. If \(c=0\), the kernel is \(|d|^2\beta(1+\beta u)/(1-u)^{\beta+2}\), zero-free because \(|\beta u|<1\). This completes all cases.

## Verification
The standalone standard-library file `check_fractional_jet.py` verifies the threshold factorization exactly over rational parameter grids, checks the transformed boundary equations and nondegenerate Jacobian factors for representative interior-zero regimes, verifies the boundary contact configurations at the critical ratio, and compares the polynomial numerator to independently differentiated kernel formulas. It was executed successfully and returned `CHECK_OK`. The universal classification is proved analytically above: no finite grid, sampling, or symbolic spot check substitutes for the torus, argument-principle, and implicit-function arguments.

## Relationship to prior work
Gehlawat, Jain, and Sarkar introduced the canonical positive-definite Gram construction for differential evaluation sequences and investigated its zero sets, principally for **ordinary Bergman spaces**, in arXiv:2608.13193v1. The present analytic Hilbert spaces have fractional binomial kernels and possess a distinct sharp regime \(0<\beta\le1\). The classical disk Bergman jet theorem, *First-order Bergman jet kernels on the disk have a sharp zero-free dichotomy*, concerns the \(\beta=2\) kernel and shows that every nonzero derivative perturbation creates zeros, including the pure derivative. It neither implies nor contains the opposite reentrant phenomenon for \(\beta<1\). The upper-half-plane classical Bergman theorem, *Exact two-jet Lu Qi-Keng phase for the canonical \(\xi\)-Bergman Gram kernel*, classifies a different projective complex-coefficient phase on another space and domain. The all-orders pure-jet Bergman disk theorem concerns the same classical \(\beta=2\) kernel and single derivative orders; it also does not imply this fractional-space classification. The complete Pick nature of \(K_\beta\) for \(0<\beta\le1\) is standard, not claimed as new.

The new invariant is the exact threshold \(2/\sqrt{1-\beta}\) governing an otherwise unexpected return to zero-freeness as the derivative coefficient grows. Related results should be compared by both kernel exponent and the meaning of the jet ratio; conformal transport or a bare parameter renaming does not identify the classical \(\beta=2\) kernel with \(0<\beta\le1\).

## Limitations
The theorem assumes a fixed first-order **constant-coefficient** differential functional and the exact binomial kernel. It does not address arbitrary complete Pick kernels, higher mixed jet orders, other domains, or exponents \(\beta>1\). The boundary-root locations are not interior zeros. Earlier unindexed observations of equivalent fractional-jet classifications cannot be ruled out; independent priority validation has not been performed.

## References
1. S. Gehlawat, A. Jain, and A. D. Sarkar, *A Canonical Positive Definite Kernel Associated with the \(\xi\)-Bergman Kernel*, arXiv:2608.13193v1, first publicly posted August 13, 2026. https://arxiv.org/abs/2608.13193
2. *First-order Bergman jet kernels on the disk have a sharp zero-free dichotomy*, published mathematical record, October 11, 2026. https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-first-order-bergman-jet-kernels-on-the-disk-have-a-sharp-zero-fr--6c2c52725478
3. *Exact two-jet Lu Qi-Keng phase for the canonical \(\xi\)-Bergman Gram kernel*, published mathematical record, October 11, 2026. https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-two-jet-lu-qi-keng-phase-for-the-canonical-bergman-gram-ke--364c00673845
4. *Exact zero fibres of pure-jet Bergman Gram kernels on the disk*, published mathematical record, October 11, 2026. https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-zero-fibres-of-pure-jet-bergman-gram-kernels-on-the-disk--98259fe7e47b
