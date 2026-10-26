# Gaussian-order resolvent growth of a noncompact homogeneous Hankel quasinilpotent

## Finding
For each fixed real \(a\ne0\), define the bounded integral Hankel operator \(H_a\) on \(L^2(0,\infty)\) initially on compactly supported functions by
\[
(H_af)(x)=\int_0^\infty (x+y)^{-1+ia}f(y)\,dy.
\]
Put \(c=\pi|a|\) and \(C_a=(\pi\sinh c/|a|)^{1/2}\). For every integer \(n\ge1\), its **exact power norm** is
\[
\|H_a^n\|=\frac{C_a^n}{\displaystyle\cosh(cn/2)\prod_{j=1}^{n-1}\cosh\bigl(c(n-2j)/2\bigr)}.
\]
In particular,
\[
\log\|H_a^n\|=-\frac{\pi|a|}{4}n^2+n\log(2C_a)+O_a(1).
\]
The **sharp logarithmic resolvent-growth law** is
\[
\boxed{\lim_{\substack{\lambda\to0\\\lambda\ne0}}\frac{\log\|(\lambda I-H_a)^{-1}\|}{\bigl(\log(1/|\lambda|)\bigr)^2}=\frac{1}{\pi|a|}.}
\]
Every positive power is noncompact; its singular-modulus operator has spectrum \([0,\|H_a^n\|]\), with no eigenvalues. The norm and growth statements are uniform in the argument of the complex resolvent parameter.

## Assumptions and scope
The space is the complex Hilbert space \(L^2(0,\infty;dx)\); the kernel has coefficient exactly one, the integral uses Lebesgue measure, the complex power is \((x+y)^{-1+ia}=\exp((-1+ia)\log(x+y))\) with the real logarithm, and \(a\in\mathbb R\setminus\{0\}\) is fixed. No scaling of the operator is implicit. All norms are Hilbert-space operator norms. The resolvent assertion concerns all nonzero complex \(\lambda\) tending to zero, not only positive real \(\lambda\). The endpoint \(a=0\) is excluded: it is the Carleman operator, not quasinilpotent.

## Proof
**1. Unitary Mellin translation.** The unitary Mellin transform is
\[
(\mathcal Mf)(s)=(2\pi)^{-1/2}\int_0^\infty x^{-1/2-is}f(x)\,dx.
\]
Fubini for compactly supported smooth inputs is justified by the Carleman majorant \((x+y)^{-1}\) and \(\int_0^\infty x^{-1/2}(x+y)^{-1}\,dx=\pi y^{-1/2}\). Euler's beta integral therefore gives
\[
(\mathcal MH_a\mathcal M^{-1}g)(s)=\phi_a(s)g(s-a),\qquad
\phi_a(s)=\frac{\Gamma(1/2-is)\Gamma(1/2+i(s-a))}{\Gamma(1-ia)}.
\]
The reflection and recurrence identities for Gamma give
\[
|\phi_a(s)|=\frac{C_a}{\sqrt{\cosh(\pi s)\cosh(\pi(s-a))}},\qquad C_a=\frac{\pi}{|\Gamma(1-ia)|}=\sqrt{\frac{\pi\sinh(\pi|a|)}{|a|}}.
\]
In particular \(\phi_a\) is bounded, continuous, and vanishes at both infinities; the identity extends from the dense initial domain to a bounded operator.

**2. Exact power norm.** Iterating the weighted translation yields
\[
(\mathcal MH_a^n\mathcal M^{-1}g)(s)=\Phi_{a,n}(s)g(s-na),\quad
\Phi_{a,n}(s)=\prod_{k=0}^{n-1}\phi_a(s-ka).
\]
Since translation is unitary, \(\|H_a^n\|=\max_{s\in\mathbb R}|\Phi_{a,n}(s)|\). The exact modulus simplifies to
\[
|\Phi_{a,n}(s)|=\frac{C_a^n}{\sqrt{\cosh(\pi s)\cosh(\pi(s-na))}\,\prod_{j=1}^{n-1}\cosh(\pi(s-ja))}.
\]
The negative logarithm is strictly convex because \(d^2\log\cosh(\pi s)/ds^2=\pi^2\operatorname{sech}^2(\pi s)>0\). It is symmetric about \(s=na/2\), hence has its unique minimum there. Substitution proves the displayed finite-product norm formula for every \(n\ge1\), including \(n=1\).

**3. Quadratic log-power expansion.** For \(t\in\mathbb R\), \(\log\cosh t=|t|-\log2+\log(1+e^{-2|t|})\). The sum of absolute values in the denominator is \(cn^2/4\) if \(n\) is even and \(c(n^2+1)/4\) if \(n\) is odd. The remaining correction is uniformly bounded in \(n\), since it is bounded by \(\log2+2\sum_{j\ge0}\log(1+e^{-(2j+1)c})+2\sum_{j\ge1}\log(1+e^{-2jc})\), which is finite for \(c>0\). There are exactly \(n\) hyperbolic cosine factors. Consequently
\[
\log\|H_a^n\|=-cn^2/4+n\log(2C_a)+O_a(1).
\]
This implies the absolute convergence in operator norm of \(\sum_{n\ge0}\lambda^{-n-1}H_a^n\) for every \(\lambda\ne0\). Its sum is the resolvent, by multiplication with \(\lambda I-H_a\) and norm convergence.

**4. Resolvent upper bound.** Write \(r=|\lambda|\) and \(L=\log(1/r)\). The Neumann series and Step 3 give, for \(r<1\),
\[
\|(\lambda I-H_a)^{-1}\|\le r^{-1}\sum_{n\ge0}\exp\bigl(n(L+\log(2C_a))-cn^2/4+O_a(1)\bigr).
\]
Completing the square and summing a translated Gaussian lattice yields
\[
\log\|(\lambda I-H_a)^{-1}\|\le L^2/c+O_a(L+1).
\]
The estimate is independent of \(\arg\lambda\).

**5. Matching resolvent lower bound.** Fix \(0<\delta<|a|/2\) and an integer \(n\ge1\). Let \(J_n=(na/2-\delta,na/2+\delta)\), \(I_n=J_n-na\), and \(g_n=|I_n|^{-1/2}\mathbf 1_{I_n}\in L^2(\mathbb R)\). The functions \((\mathcal MH_a^k\mathcal M^{-1})g_n\), \(k\ge0\), have mutually disjoint supports \(I_n+ka\), since the support intervals have length less than \(|a|\). The Neumann-series terms on this input are therefore orthogonal for every complex \(\lambda\). Moreover,
\[
\left|\frac{d}{ds}\log|\phi_a(s)|\right|=\frac\pi2|\tanh(\pi s)+\tanh(\pi(s-a))|\le\pi.
\]
By Step 2, \(|\Phi_{a,n}(s)|\ge e^{-\pi n\delta}\|H_a^n\|\) for every \(s\in J_n\). Thus orthogonality gives
\[
\|(\lambda I-H_a)^{-1}\|\ge r^{-n-1}e^{-\pi n\delta}\|H_a^n\|.
\]
Choose \(n\) to be an integer nearest to \(2L/c\) as \(L\to\infty\). Then Step 3 yields
\[
\log\|(\lambda I-H_a)^{-1}\|\ge L^2/c-O_a(L+1).
\]
Combining upper and lower bounds proves the claimed limit with the exact coefficient \(1/c\). No cancellation assumption on the complex phase of \(\lambda\) was used.

**6. Singular modulus and noncompact powers.** In the Mellin representation, \((H_a^n)^*H_a^n\) is unitarily equivalent to multiplication by a translate of \(|\Phi_{a,n}|^2\). Strict convexity in Step 2 shows that \(|\Phi_{a,n}|\) is strictly increasing then strictly decreasing, has one maximum, and tends to zero at both infinities. Its essential range is therefore \([0,\|H_a^n\|]\), and no level set has positive Lebesgue measure. Hence \(|H_a^n|\) has that full spectrum and no point spectrum. Each nonzero multiplication operator on the nonatomic \(L^2(\mathbb R)\) is noncompact, so every \(H_a^n\) is noncompact.

## Verification
The standalone file `verify_power_resolvent.py` evaluates the gamma-modulus identity numerically, compares the closed product with direct weighted-translation maximization for multiple positive and negative parameters and powers, checks the bounded log-power remainder, and verifies numerical convergence toward the logarithmic resolvent coefficient through the saddle-point estimates. Its output is finite numerical corroboration, not a proof of the infinite-dimensional conclusions. The analytic proof above establishes every quantified statement without relying on finite sampling.

## Relationship to prior work
Sang's 2026 work introduces exactly the noncompact quasinilpotent kernel \((x+y)^{-1+ia}\), identifies its Mellin weighted-translation symbol, and gives a general supremum formula for norms of powers of weighted translations. Those facts, the quasinilpotence conclusion, and the Gamma formulas are prior work. The present contribution is the precise all-power optimization and, principally, the matching upper and lower estimates for the resolvent leading to the sharp logarithmic-square growth coefficient. Ignatev's 2026 theorem treats local resolvent-growth exponents of strictly decreasing **unilateral backward** weighted shifts; its general saddle-point lemma is related to the upper-bound strategy but does not cover this two-sided Mellin translation or provide the stated Hankel coefficient. Pushnitski–Sobolev's 2025 band-spectral theory treats **self-adjoint dilation-periodic** Hankel operators and does not determine the non-self-adjoint quasinilpotent resolvent law proved here. Prior coverage risks remain for unindexed pseudospectral or bilateral-shift literature.

## Limitations
The result is for the homogeneous Hankel kernel with unit coefficient and fixed \(a\ne0\). It does not give an exact finite-\(\lambda\) resolvent norm, an optimal second-order term in its logarithm, or the power-set invariant for individual vectors. The asymptotic is nonuniform as \(a\to0\); the Carleman endpoint has different spectral behavior. A search cannot certify publication priority, and independent mathematical validation has not been performed.

## References
1. Y. Sang, *Examples of Noncompact Quasinilpotent Hankel Operators*, arXiv:2609.25184v1 (first public 2026-09-21), especially Proposition 2.1, Theorems 2.2 and 2.4 and equations (2.3)–(2.4). https://arxiv.org/html/2609.25184
2. E. Ignatev, *The power set of a quasinilpotent backward weighted shift*, arXiv:2607.16743v1 (first public 2026-07-18), Section 3, Lemma 1 and equation (11). https://arxiv.org/html/2607.16743v1
3. A. Pushnitski and A. Sobolev, *Hankel operators with band spectra and elliptic functions*, Duke Math. J. 174 (2025), 685–746; arXiv:2307.09242 (first public 2023-07-18). https://arxiv.org/abs/2307.09242
