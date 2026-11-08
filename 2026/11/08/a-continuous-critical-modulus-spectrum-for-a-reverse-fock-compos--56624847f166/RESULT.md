# A continuous critical modulus spectrum for a reverse Fock composition product

## Finding

Let \(\mathcal F^2\) be the standard one-variable Gaussian Fock Hilbert space with reproducing kernels \(K_w(z)=e^{z\overline w}\). Fix real parameters \(c>1\) and \(0<\tau<1\), and set
\[
a=(c^2+\tau)^{-1/2},\qquad t=\tau a^2=\frac{\tau}{c^2+\tau},\qquad \lambda=\frac{t}{1-t}.
\]
Define \(Af(z)=f(az)\), and let \(B\) denote the maximal weighted composition operator \(Bf(z)=e^{\tau z^2/2}f(cz)\). Then \(A\) is compact and \(B\) is densely defined, closed and unbounded. Nevertheless, the **reverse natural product** \(T=B^*A\) is an everywhere-defined bounded operator. Let \(\mathcal B:L^2(\mathbb R,dx)\to\mathcal F^2\) be the unitary Segal--Bargmann transform described below and let \((Rf)(z)=f(iz)\). Then
\[
\boxed{\quad T^*T=(1-t)^{-1/2}\,R\mathcal B\,M_{\exp(-\lambda x^2)}\,\mathcal B^*R^*.\quad}
\]
In particular,
\[
\sigma(T^*T)=\sigma_{\mathrm{ess}}(T^*T)=[0,(1-t)^{-1/2}],\qquad
\|T\|=\|T\|_{\mathrm{ess}}=(1-t)^{-1/4}.
\]
The spectrum is purely absolutely continuous and has no eigenvalues. Thus the critical noncompact product has a full interval of continuous singular spectrum, in contrast with discrete singular-value sequences for compact Gaussian kernels.

## Assumptions and scope

The inner product on \(\mathcal F^2\) is linear in its first entry, and
\[
\langle f,h\rangle_{\mathcal F^2}=\frac1\pi\int_{\mathbb C}f(z)\overline{h(z)}e^{-|z|^2}\,dA(z).
\]
The maximal domain of \(B\) consists exactly of the \(f\in\mathcal F^2\) for which \(e^{\tau z^2/2}f(cz)\in\mathcal F^2\). In particular every polynomial belongs to this domain, because \(0<\tau<1\). Its adjoint is taken as an unbounded Hilbert-space adjoint. The critical identity \(a^2(c^2+\tau)=1\) is imposed throughout the theorem. The essential norm is the distance to compact operators; essential spectrum is in the Fredholm/Calkin sense.

Use the normalized Segal--Bargmann transform
\[
(\mathcal B h)(z)=\pi^{-1/4}\int_{\mathbb R}
 e^{-x^2/2+\sqrt2xz-z^2/2}\,h(x)\,dx.
\]
It maps \(L^2(\mathbb R,dx)\) unitarily onto \(\mathcal F^2\); \(R\) is a unitary quarter-turn. The multiplier \(M_{\exp(-\lambda x^2)}\) is the usual bounded self-adjoint multiplication operator on \(L^2(\mathbb R)\).

## Proof

**1. The factors and the natural domain.** Since \(A(z^n/\sqrt{n!})=a^n z^n/\sqrt{n!}\) and \(0<a<1\), \(A\) is compact. A maximal weighted composition operator is closed: if \(f_j\to f\) and \(Bf_j\to g\) in the Fock norm, convergence of point evaluations gives \(g(z)=e^{\tau z^2/2}f(cz)\) for every \(z\). Every polynomial lies in \(D(B)\) because the integrand defining its norm is bounded by a polynomial times \(e^{-(1-\tau)(\operatorname{Re}z)^2-(1+\tau)(\operatorname{Im}z)^2}\). For the monomial \(e_n(z)=z^n/\sqrt{n!}\), the angular average of \(\exp(\tau\operatorname{Re}(z^2))\) is at least one (Jensen), whence \(\|Be_n\|\ge c^n\); thus \(B\) is unbounded. The composition \(B^*A\) is closed because \(B^*\) is closed and \(A\) is bounded.

By evaluating the adjoint against kernels,
\[
B^*K_w=e^{\tau\overline w^{\,2}/2}K_{cw},\qquad
AK_w=K_{aw},\qquad
TK_w=e^{t\overline w^{\,2}/2}K_{ca w}.
\]
Each \(K_w\) therefore belongs to \(D(T)\); the algebraic span \(E\) of all such kernels is dense in \(\mathcal F^2\).

**2. Exact positive Gram kernel.** Set \(\rho=ca\); by the critical identity \(\rho^2=1-t\). The preceding formula and \(\langle K_u,K_v\rangle=e^{v\overline u}\) give, for all \(z,w\in\mathbb C\),
\[
\langle TK_w,TK_z\rangle
=\exp\!\left((1-t)z\overline w+\frac t2(z^2+\overline w^{\,2})\right).\tag{1}
\]
On the other hand, a one-dimensional Gaussian integral evaluates the kernel of the Bargmann conjugate of a Gaussian multiplier:
\[
\langle \mathcal B M_{\exp(-\lambda x^2)}\mathcal B^*K_w,K_z\rangle
=(1+\lambda)^{-1/2}
\exp\!\left(\frac{z\overline w}{1+\lambda}
-\frac{\lambda(z^2+\overline w^{\,2})}{2(1+\lambda)}\right).\tag{2}
\]
Indeed insert the integral kernel of \(\mathcal B\) and complete the square in \(x\); the scalar integral is \(\int_{\mathbb R}e^{-(1+\lambda)x^2+\sqrt2x(z+\overline w)}dx\). Conjugating (2) by \(R\) changes the signs of the two square terms but leaves \(z\overline w\) invariant. Since \((1+\lambda)^{-1}=1-t\), multiplying by \((1-t)^{-1/2}\) yields exactly (1). Thus if
\[
P=(1-t)^{-1/2}R\mathcal B M_{\exp(-\lambda x^2)}\mathcal B^*R^*,
\]
then \(P\ge0\), \(P\) is bounded, and \(\|Th\|^2=\langle Ph,h\rangle\) for every \(h\in E\). In particular \(\|Th\|\le\sqrt{\|P\|}\,\|h\|\) on the dense space \(E\). The restriction \(T|_E\) has a bounded extension to all \(\mathcal F^2\); since the original natural product \(T=B^*A\) is closed and contains the restriction, its domain contains the closure of the graph of \(T|_E\), which projects onto all \(\mathcal F^2\). Hence the natural product itself is bounded everywhere. Polarization of the Gram identities gives \(T^*T=P\).

**3. Spectrum and essential norm.** For \(\lambda>0\), multiplication by \(e^{-\lambda x^2}\) on \(L^2(\mathbb R,dx)\) has spectrum and Fredholm essential spectrum equal to its essential range \([0,1]\). Every level set has Lebesgue measure zero, so there are no eigenvalues. The change of variables from \(x\) to \(e^{-\lambda x^2}\) gives a spectral measure equivalent to Lebesgue measure on the interior of \([0,1]\), establishing purely absolutely continuous spectrum. Scaling by \((1-t)^{-1/2}\) proves the asserted spectrum of \(P=T^*T\). A nonzero multiplication operator on a nonatomic \(L^2\) space is noncompact here; furthermore its Calkin norm is its usual norm, so \(\|P\|_{\mathrm{ess}}=(1-t)^{-1/2}\). The \(C^*\)-identity in the Calkin algebra gives \(\|T\|_{\mathrm{ess}}^2=\|T^*T\|_{\mathrm{ess}}\), proving the remaining norm formulas.

As a rational-parameter illustration, take \(c=2\), \(\tau=1/2\), \(a=\sqrt2/3\). Then \(t=1/9\) and the exact positive spectral interval is \([0,\sqrt{9/8}]\).

## Verification

The accompanying `CHECK.py` is a self-contained standard-library program verifying, at 732 exact rational coefficient comparisons, the equality of the two-variable power series in (1) and (2) after the quarter-turn and scaling. It expands physicists' Hermite polynomials, evaluates Gaussian moments exactly, and compares the resulting coefficients with the Fock-space Gram kernel. The test uses six rational values of \(t\) and degrees through ten in each variable. Run `python CHECK.py` in the extracted directory. It verifies the critical algebra at finite orders; it does not certify the unbounded-domain argument or the infinite-dimensional spectral theorem. Those depend on the proof above.

## Relationship to prior work

Sang and Zhao [1] study a five-parameter Gaussian integral kernel, of which the present kernel is a special case. Their Theorems 1.1–1.2 already characterize boundedness and compactness in full generality, and their Section 5 studies Schatten classes and Hilbert–Schmidt norms. The bounded/noncompact threshold is therefore **not** claimed as a new classification. The result here is the exact positive spectral model, purely continuous essential spectrum, and sharp norm and essential norm at that threshold.

Tian [2] studies natural products of Fock-space weighted composition operators. Section 4 treats the forward product when one factor is unbounded; the introduction explicitly leaves its reverse counterpart for further study. The present result resolves the critical spectral structure of a quadratic-exponential, reverse-order subfamily, not the general open problem.

Dong and Zhu [3] analyze a canonical two-parameter Gaussian family having paired quadratic terms and find all singular values in its compact region; its bounded boundary consists of unitary operators, unlike the nonunitary continuous-modulus model above. Hai [4] gives adjoint formulas for narrower exponential-affine weighted compositions but does not establish the quadratic-weight spectral identity here. The unitary Bargmann transform and the Gaussian moment calculation are classical tools, not new assertions.

## Limitations

The theorem is for one complex variable with real \(c>1\), \(0<\tau<1\) and exactly the critical relation \(a^2(c^2+\tau)=1\). No general result for complex affine symbols, all quadratic weights, or nonlinear maps is claimed. Classical Gaussian operator theory could provide a more abstract route to the same multiplication model, and older oscillator-semigroup treatments are a residual priority risk; no claim of independence or external audit is made. The theorem gives the spectrum of the modulus and not the full complex spectrum of the nonnormal product \(T\).

## References

[1] Y. Sang and L. Zhao, *Gaussian Integral Operator between Fock Spaces* (first public October 20, 2026), arXiv:2610.28279, https://arxiv.org/abs/2610.28279.

[2] X. Tian, *Weighted composition operators on the Fock space* (first public October 21, 2026), arXiv:2610.29786, https://arxiv.org/abs/2610.29786.

[3] X. Dong and K. Zhu, *Canonical integral operators on the Fock space II* (2025), arXiv:2509.16672, https://arxiv.org/abs/2509.16672.

[4] P. V. Hai, *Unbounded Weighted Composition Operators on Fock space* (2018 first public), arXiv:1804.00414, https://arxiv.org/abs/1804.00414.

[5] V. Bargmann, *On a Hilbert space of analytic functions and an associated integral transform, Part I*, Comm. Pure Appl. Math. 14 (1961), 187–214.
