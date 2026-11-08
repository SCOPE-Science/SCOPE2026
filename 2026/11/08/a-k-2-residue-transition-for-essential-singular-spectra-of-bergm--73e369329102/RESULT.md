# A \(k^2\)-residue transition for essential singular spectra of Bergman slant commutators

## Finding

Fix an integer \(k\ge 2\), a real Bergman parameter \(\alpha>-1\), and two **distinct** nonnegative integers \(a,b\). On the standard weighted Bergman Hilbert space \(A^2_\alpha(\mathbb D)\), define the monomial-decimation operator \(W_k\) by \(W_kz^{kn}=z^n\) and \(W_kz^j=0\) when \(k\nmid j\). Put \(B_a=W_k M_{z^a}\), \(B_b=W_k M_{z^b}\), and \(C=[B_a,B_b]=B_aB_b-B_bB_a\). These are bounded operators.

Let \(S e_n=e_{n+1}\) denote the unilateral shift of the normalized monomial basis, \(\pi\) the quotient map to the Calkin algebra, and \(u=\pi(S)\). Write \(L=k^{2\alpha+2}\). Then the **exact Calkin Gram operator** has the following arithmetic dichotomy:

\[
\pi(CC^*)=\begin{cases}
2L\,1,&a\not\equiv b\pmod{k^2},\\
L(2\,1-u^d-u^{-d}),&a\equiv b\pmod{k^2},\quad d=(k-1)(a-b)/k^2\ne0.
\end{cases}
\]

In particular, with \(\sigma_{\mathrm{ess}}\) denoting Fredholm essential spectrum,

\[
\sigma_{\mathrm{ess}}(CC^*)=\begin{cases}
\{2k^{2\alpha+2}\},&k^2\nmid(a-b),\\
[0,4k^{2\alpha+2}],&k^2\mid(a-b),
\end{cases}
\quad
\|C\|_{\mathrm{ess}}=\begin{cases}
\sqrt2\,k^{\alpha+1},&k^2\nmid(a-b),\\
2k^{\alpha+1},&k^2\mid(a-b).
\end{cases}
\]

Thus the image of \(C\) in the Calkin algebra is **right-invertible precisely when** \(k^2\nmid(a-b)\): in the first case its Gram element is a positive scalar unit, whereas in the second case zero lies in its Gram essential spectrum. For the ordinary (unweighted) Bergman space \(\alpha=0\), the *ordinary* operator norm equals the essential norm in both cases, and that norm is **not attained** by any nonzero vector.

## Assumptions and scope

The weighted area probability measure is \((\alpha+1)(1-|z|^2)^\alpha\,dA(z)\), where \(dA\) is normalized planar area measure. The orthonormal monomials are \(e_n=z^n/\gamma_n\), with

\[
\gamma_n^2=\frac{\Gamma(\alpha+2)\Gamma(n+1)}{\Gamma(n+\alpha+2)}.
\]

The operator \(W_k\) is specifically **unnormalized monomial decimation** (not the alternative orthonormal-basis decimator). It is bounded because \(\gamma_n/\gamma_{kn}\to k^{(\alpha+1)/2}\) as \(n\to\infty\). Symbols here are exactly the analytic monomials \(z^a,z^b\), with \(a,b\in\mathbb N_0\) distinct. There is no assertion for general polyanalytic or harmonic symbols. The Calkin quotient is \(\mathcal B(A^2_\alpha)/\mathcal K(A^2_\alpha)\). The shift \(S\) acts on the normalized monomial basis; it is not generally multiplication by \(z\).

## Proof

**1. Exact two-step monomial maps.** For nonnegative integers \(n,m\), multiplication by \(z^a\) followed by monomial decimation gives

\[
B_a e_n=\begin{cases}\dfrac{\gamma_m}{\gamma_n}e_m,&n+a=km,\\0,&k\nmid(n+a).\end{cases}
\]

Put \(A=B_aB_b\), \(D=B_bB_a\), \(h=b+ka\), and \(h'=a+kb\). A second application of this formula yields

\[
A e_n=\frac{\gamma_m}{\gamma_n}e_m\quad\text{if }n+h=k^2m,
\qquad
D e_n=\frac{\gamma_m}{\gamma_n}e_m\quad\text{if }n+h'=k^2m,
\]

with zero otherwise. The intermediate normalization cancels exactly. Hence, for each \(m\ge0\),

\[
A^*e_m=\begin{cases}\dfrac{\gamma_m}{\gamma_{k^2m-h}}e_{k^2m-h},&k^2m\ge h,\\0,&k^2m<h,\end{cases}
\quad
D^*e_m=\begin{cases}\dfrac{\gamma_m}{\gamma_{k^2m-h'}}e_{k^2m-h'},&k^2m\ge h',\\0,&k^2m<h'.\end{cases}
\]

**2. All compact errors identified.** The gamma-ratio asymptotic, a direct consequence of \(\Gamma(t+\alpha+2)/\Gamma(t+1)\sim t^{\alpha+1}\), is

\[
\frac{\gamma_m}{\gamma_{k^2m-h}}\longrightarrow k^{\alpha+1},\qquad
\frac{\gamma_m}{\gamma_{k^2m-h'}}\longrightarrow k^{\alpha+1}.
\]

Therefore \(AA^*-L I\) and \(DD^*-L I\) are compact diagonal operators: their diagonal coefficients tend to zero. The two input supports occupy the residue classes \(-h\) and \(-h'\) modulo \(k^2\). Since

\[
h-h'=(k-1)(a-b),\qquad \gcd(k-1,k^2)=1,
\]

these residue classes are distinct exactly when \(k^2\nmid(a-b)\). In that case \(AD^*=DA^*=0\) **exactly**, and \(\pi(CC^*)=2L1\).

If \(k^2\mid(a-b)\), put \(d=(h-h')/k^2=(k-1)(a-b)/k^2\), a nonzero integer. Directly from the displayed adjoint formulas, \(AD^*e_m\) is a scalar multiple of \(e_{m+d}\) whenever the indices are nonnegative, and that scalar tends to \(L\). Thus \(AD^*-LS^d\) is compact for \(d>0\); when \(d<0\), interpret \(S^d\) as \((S^*)^{-d}\). This is the elementary fact that a fixed-step weighted shift whose weights tend to zero is compact, by finite-rank truncation. Taking adjoints gives \(\pi(DA^*)=Lu^{-d}\). Substituting in \(CC^*=AA^*+DD^*-AD^*-DA^*\) proves the two Calkin Gram identities.

**3. Spectra, norms, and right invertibility.** The Calkin class \(u=\pi(S)\) is unitary with spectrum the unit circle: \(S^*S=I\), \(SS^*=I-\langle\cdot,e_0\rangle e_0\), and normalized long blocks give approximate essential eigenvectors at every unimodular scalar. For every nonzero integer \(d\), the continuous functional calculus therefore gives

\[
\sigma(2-u^d-u^{-d})=\{2-2\cos(d\theta):0\le\theta\le2\pi\}=[0,4].
\]

The displayed essential-spectrum formulas follow. In any \(C^*\)-algebra \(\|x\|^2=\|xx^*\|\), so the essential-norm formulas follow by taking square roots. A Calkin element \(c\) is right-invertible exactly when \(cc^*\) is invertible: if \(cc^*\) is invertible, \(c^*(cc^*)^{-1}\) is a right inverse; conversely a right inverse makes \(cc^*\) bounded below. The scalar versus interval cases therefore yield the claimed right-invertibility dichotomy.

**4. Sharp ordinary norms at \(\alpha=0\).** Here \(\gamma_n=(n+1)^{-1/2}\). Every nonzero coefficient of either two-step map has square

\[
\left(\frac{\gamma_m}{\gamma_{k^2m-h}}\right)^2
=\frac{k^2m-h+1}{m+1}<k^2
\]

(and similarly with \(h'\)). Thus \(\|A\|=\|D\|=k\), with neither norm attained. If the residue classes are distinct, \(CC^*\) is diagonal and every diagonal entry is strictly less than \(2k^2\); its diagonal entries tend to \(2k^2\), so \(\|C\|=\sqrt2 k\). Neither \(C^*\) nor \(C\) attains the norm: if a unit vector \(x\) attained \(\|C\|\), then \(Cx/\|C\|\) would attain \(\|C^*\|\), contradicting strict diagonal inequalities. If they coincide, \(\|C\|\le\|A\|+\|D\|=2k\), while the essential norm proved above is \(2k\). Thus \(\|C\|=2k\). Strict norm inequality for both \(A\) and \(D\) on every nonzero input makes equality unattainable for \(C\) as well. This finishes the proof.

## Verification

The included `CHECKER.py` uses only the Python standard library. Execute `python CHECKER.py` to recompute direct two-stage decimation and the independently derived Gram-row formulas for multiple \(k,a,b,\alpha\), and to test the two possible limiting Gram patterns. A successful finite replay reports `SLANT_COMMUTATOR_ESSENTIAL_FINITE_OK 588`. These 588 finite assertions are **consistency tests**, not a substitute for the compactness and Calkin-spectrum proof above. No infinite-dimensional identity is inferred solely from numerical sampling.

## Relationship to prior work

Cui, Li and Lu (2026) prove qualitative commutativity, finite-rank commutator rigidity, and infinite-rank statements for slant Toeplitz operators with polyanalytic and harmonic symbols. Their framework motivates asking for a *quantitative essential* invariant. Their results do not supply the explicit Calkin Gram identities, exact essential norms, or the congruence-class transition above. Liu and Lu (2013) treat products and commutativity of higher-order slant Toeplitz operators; their Bergman-space section does not state this essential spectral classification. Lu, Liu and Yang (2010) establish equivalence of commutativity and essential commutativity in related classes, which yields a qualitative noncompactness conclusion but does not determine two different positive essential norms or the full Gram essential spectrum. Singh, Singh and Singh (2025) discuss weighted Bergman slant operators and their single-operator spectral properties; the normalization of decimation operators must be distinguished from the explicitly defined monomial decimation here, and their paper does not give the stated commutator result.

## Limitations

The theorem does not classify commutators of arbitrary analytic, polyanalytic, or harmonic symbols, and does not claim the exact ordinary norm for all \(\alpha>-1\). The exact spectrum of \(CC^*\), as opposed to its essential spectrum, may contain additional isolated spectral values. The full text of the 2010 predecessor was inaccessible at review time; an earlier equivalent quantitative formulation cannot be ruled out. No independent mathematical or publication-priority audit has been performed.

## References

1. P. Cui, R. Li and Y. Lu, *Commuting slant Toeplitz operators for polyanalytic and harmonic symbols*, arXiv:2610.09728 (first posted 7 October 2026), https://arxiv.org/abs/2610.09728.
2. C. Liu and Y. Lu, *Product and Commutativity of kth-Order Slant Toeplitz Operators*, Abstract and Applied Analysis 2013, article 473916, https://doi.org/10.1155/2013/473916.
3. Y. Lu, C. Liu and J. Yang, *Commutativity of kth-Order Slant Toeplitz Operators*, Mathematische Nachrichten 283 (2010), 1304–1313, https://doi.org/10.1002/mana.200710100.
4. O. N. Singh, M. P. Singh and T. S. Singh, *Algebraic and Spectral properties of slant Toeplitz and slant little Hankel Operators on weighted Bergman Space*, arXiv:2507.06546 (2025), https://arxiv.org/abs/2507.06546.
5. H. Y. Zhang, *Commuting Slant Toeplitz Operators on the Bergman Space*, arXiv:2504.01042 (2025), https://arxiv.org/abs/2504.01042.
