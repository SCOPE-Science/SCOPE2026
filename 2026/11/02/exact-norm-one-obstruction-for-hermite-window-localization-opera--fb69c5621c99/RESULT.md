# Exact norm-one obstruction for Hermite-window localization operators

## Finding

The result is a sharp norm-approximation obstruction in Hermite-window time-frequency analysis. Under the order-\(k\) polyanalytic Bargmann transform, bounded-mask Hermite-window localization operators are unitarily equivalent (after the fixed phase-space coordinate rescaling) to bounded-symbol Toeplitz operators on the true order-\(k\) Fock level. In particular, the theorem below gives, for every non-Gaussian Hermite window, a time-frequency shift at exact operator-norm distance \(1\) from the complete bounded-mask localization-operator range.

Let \(k\ge 2\) be an integer, let \(\mathcal F_{(k)}^2\) be the true order-\(k\) polyanalytic Gaussian Fock Hilbert space over \(\mathbb C\), and let \(T_{f,(k)}\) be Toeplitz quantization of a bounded measurable symbol \(f\). Define the Weyl shifts by
\[
(W_\xi u)(w)=\exp(w\overline\xi-|\xi|^2/2)u(w-\xi).
\]
For every \(\xi\in\mathbb C\) at which the ordinary Laguerre polynomial satisfies \(L_{k-1}(|\xi|^2)=0\), the exact operator-norm distance is
\[
\boxed{\inf_{f\in L^\infty(\mathbb C)}\|W_\xi-T_{f,(k)}\|_{\mathrm{op}}=1.}
\]
The same distance holds to the operator-norm closure of this linear Toeplitz range. Nevertheless \(W_\xi\) belongs to the algebra \(\mathcal C_1\) of operators continuous in norm under Weyl conjugation. Thus, for every nonanalytic true polyanalytic level, the norm closure of Toeplitz operators with bounded uniformly continuous symbols is a proper subset of \(\mathcal C_1\). In particular, the first, linear-closure question in Fulsche--Hagger's 2024 Question 2 has a negative answer. No claim is made about the separate \(C^*\)-generation question.

## Assumptions and scope

The ambient measure is \(d\mu(w)=\pi^{-1}e^{-|w|^2}dA(w)\). Write \(\mathcal F_{(k)}^2\subset L^2(\mu)\) for the \(k\)-th irreducible Weyl-invariant Landau/Fock level and \(P_{(k)}\) for its orthogonal projection. For each essentially bounded complex-valued symbol \(f\), \(T_{f,(k)}=P_{(k)}M_f|_{\mathcal F_{(k)}^2}\), a bounded operator with \(\|T_{f,(k)}\|\le\|f\|_\infty\). The phase convention is \(\sigma(z,w)=2\operatorname{Im}(z\overline w)\), with \(W_zW_w=e^{-i\sigma(z,w)/2}W_{z+w}\). The true levels have irreducible Weyl action; no semiclassical or uniform-in-\(k\) limit is assumed. The normalized Hermite window of index \(k-1\) defines an isometric short-time Fourier transform; its anti-Wick time-frequency localization operator with bounded mask is unitarily conjugate to \(T_{f,(k)}\) for a corresponding bounded symbol (Abreu--Speckbacher, Section 6.3). Thus the norm-distance assertion has the stated Gabor localization interpretation, with the frequency parameter converted by that fixed coordinate rescaling. The ordinary Laguerre polynomial is \(L_n(x)=\sum_{j=0}^n(-1)^j\binom nj x^j/j!\). Each \(L_n\), for \(n\ge1\), has \(n\) distinct strictly positive roots.

## Proof

**Step 1: Exact vanishing of a character Toeplitz operator.** Put \(\chi_\xi(w)=e^{i\sigma(w,\xi)}\). Covariance gives
\[
W_zT_{\chi_\xi,(k)}W_z^*=e^{-i\sigma(z,\xi)}T_{\chi_\xi,(k)},\qquad
W_zW_\xi W_z^*=e^{-i\sigma(z,\xi)}W_\xi.
\]
Irreducibility therefore implies \(T_{\chi_\xi,(k)}=c_k(\xi)W_\xi\). To determine the scalar without presupposing a Fourier-symbol theorem, use the unit vector \(u_n(w)=L_n(|w|^2)\in\mathcal F_{(n+1)}^2\), whose norm is one by Laguerre orthogonality. Rotational covariance reduces to real \(\xi=a\ge0\). The inner product with \(W_a u_n\) gives
\[
c_{n+1}(a)=e^{-a^2/2}\,I_{n,n}(a),\quad
I_{n,m}(a)=\frac1\pi\int_{\mathbb C}e^{-|w|^2+aw}L_n(|w|^2)L_m(|w-a|^2)\,dA(w).
\]
The generating identity \(\sum_{n\ge0}s^nL_n(x)=(1-s)^{-1}\exp[-sx/(1-s)]\), followed by elementary complex Gaussian integration, yields for sufficiently small \(|s|,|t|\)
\[
\sum_{n,m\ge0}s^nt^m I_{n,m}(a)
=\frac1{1-st}\exp\!\left(-\frac{a^2st}{1-st}\right)
=\sum_{n\ge0}(st)^nL_n(a^2).
\]
Hence \(I_{n,m}(a)=\mathbf1_{\{n=m\}}L_n(a^2)\), so
\[
\boxed{T_{\chi_\xi,(k)}=e^{-|\xi|^2/2}L_{k-1}(|\xi|^2)W_\xi.}
\]
For the stated frequencies this Toeplitz operator is exactly zero. The identity is consistent with Fulsche--Hagger's kernel characterization, but the Gaussian computation above supplies an independent normalization check.

**Step 2: A contractive coefficient extractor.** Fix a unit vector \(u\in\mathcal F_{(k)}^2\), and put \(v=W_\xi u\). For \(R>0\) and an arbitrary bounded operator \(A\), set
\[
\Lambda_R(A)=\frac1{\pi R^2}\int_{|z|<R}
 e^{i\sigma(z,\xi)}\langle W_z A W_z^*u,v\rangle\,dA(z).
\]
The integral exists as an ordinary scalar integral, \(|\Lambda_R(A)|\le\|A\|\), and the Weyl commutation relation gives \(\Lambda_R(W_\xi)=1\) for every \(R>0\).

**Step 3: The extractor kills every bounded-symbol Toeplitz operator asymptotically.** Covariance implies \(W_zT_{f,(k)}W_z^*=T_{f(\cdot-z),(k)}\). Writing \(K(w)=u(w)\overline{v(w)}\), one obtains
\[
\Lambda_R(T_{f,(k)})=
\int_{\mathbb C}K(w)\left[\frac1{\pi R^2}
\int_{|z|<R}e^{i\sigma(z,\xi)}f(w-z)\,dA(z)\right]d\mu(w).
\]
Define the bounded scalar \(a_R=(\pi R^2)^{-1}\int_{|y|<R}e^{-i\sigma(y,\xi)}f(y)\,dA(y)\). Substitution \(y=w-z\) changes the inner bracket into
\[
e^{i\sigma(w,\xi)}[a_R+\varepsilon_R(w)],
\qquad
|\varepsilon_R(w)|\le
\|f\|_\infty\frac{|B_R(w)\mathbin\triangle B_R(0)|}{\pi R^2}.
\]
The symmetric-difference ratio tends to zero for every fixed \(w\), and is at most \(2\). Since \(K\in L^1(\mu)\) by Cauchy--Schwarz, dominated convergence yields
\[
\Lambda_R(T_{f,(k)})
=a_R\langle T_{\chi_\xi,(k)}u,v\rangle+o(1)=o(1).
\]
For a quantitative variant, the elementary disk-slicing estimate \(|B_R(w)\triangle B_R(0)|\le4R|w|\) gives
\[
|\Lambda_R(T_{f,(k)})|\le
\frac{4\|f\|_\infty}{\pi R}\int_{\mathbb C}|w|\,|K(w)|\,d\mu(w)
\]
whenever the displayed first moment is finite; this holds for the explicit normalized radial polynomial \(u=L_{k-1}(|\cdot|^2)\) and \(v=W_\xi u\).

**Step 4: Exact distance and properness.** For each fixed \(f\in L^\infty\), contractivity gives \(\|W_\xi-T_{f,(k)}\|\ge|\Lambda_R(W_\xi-T_{f,(k)})|\to1\). Taking \(f=0\) proves equality. The same equality holds for the norm closure of the linear range because distance to a set equals distance to its closure. Finally \(\|W_zW_\xi W_z^*-W_\xi\|=|e^{-i\sigma(z,\xi)}-1|\to0\) as \(z\to0\), hence \(W_\xi\in\mathcal C_1\). Since \(\mathrm{BUC}(\mathbb C)\subset L^\infty(\mathbb C)\), density fails even for the larger symbol class.

## Verification

The standalone \(check.py\) uses only Python standard-library exact rational arithmetic to check \(256\) finite instances of the Gaussian Laguerre identity \(I_{n,m}(a)=\mathbf1_{\{n=m\}}L_n(a^2)\) for \(0\le n,m<8\) and four rational displacements. It separately confirms the explicit first-level root \(L_1(1)=0\). Those checks do not establish the all-order identity or the infinite-dimensional norm assertion; these are proved by the generating function, Weyl covariance, disk averaging and dominated convergence above. One concrete forbidden Weyl shift is \(W_1\) on the order-two true polyanalytic Fock level, at exact distance \(1\) from every bounded-symbol Toeplitz operator.

## Relationship to prior work

Abreu and Speckbacher, *Donoho--Logan Large Sieve Principles for Modulation and Polyanalytic Fock Spaces* (arXiv:1808.02258, first released 2018-08-07, Sections 2, 4 and 6.3) develop Hermite-window STFT localization and its unitary true-polyanalytic Fock representation, but do not establish operator-norm nonapproximability of a Weyl shift by bounded-mask localization operators.

Fulsche and Hagger, *Quantum Harmonic Analysis for Polyanalytic Fock Spaces* (first arXiv version 2023-08-22, Theorem 3.4 and Corollary 3.10), characterize Laguerre-zero symbols and show that the forbidden Weyl shifts have no exact bounded Toeplitz representation. Their Section 5, Question 2, explicitly asks whether bounded-uniformly-continuous-symbol Toeplitz operators are norm dense in \(\mathcal C_1\) on higher true levels. The finding proves a stronger negative conclusion for the linear range: a sharp operator-norm gap of one, including arbitrary bounded symbols.

Fulsche's earlier analytic \(p\)-Fock correspondence theorem (arXiv:1911.12668) proves a positive norm-density result for the analytic level; the present obstruction needs a nontrivial Laguerre zero and thus does not apply there. Keller and Luef (arXiv:1905.07741, Section 6) provide semiclassical and multi-level Weyl/Toeplitz expansions, not a fixed-level norm approximation at a Laguerre-zero shift. McNulty's work on translation-invariant operators on true polyanalytic \(p\)-Fock spaces addresses a different commutation class and does not state this sharp Toeplitz-range distance.

## Limitations

This is a linear-range and linear norm-closure theorem for Hermite-window time-frequency localization (and its unitarily equivalent true-Fock Toeplitz representation); it does not resolve whether the \(C^*\)-algebra generated by higher-level Toeplitz operators equals \(\mathcal C_1\). It concerns bounded measurable symbols on the standard one-complex-dimensional Gaussian true polyanalytic levels and special Weyl frequencies at Laguerre roots. No analogous assertion is made at other frequencies, for full reducible polyanalytic spaces, or for non-Gaussian weights. Historical priority beyond the inspected sources has not been independently certified.

## References

1. L. D. Abreu and M. Speckbacher, *Donoho--Logan large sieve principles for modulation and polyanalytic Fock spaces*, arXiv:1808.02258 (first submitted 2018-08-07), especially Section 6.3. https://arxiv.org/abs/1808.02258
2. R. Fulsche and R. Hagger, *Quantum Harmonic Analysis for Polyanalytic Fock Spaces*, arXiv:2308.11292 (first submitted 2023-08-22), especially Sections 3 and 5; *Journal of Fourier Analysis and Applications* 30 (2024), article 63. https://arxiv.org/abs/2308.11292
3. R. Fulsche, *Correspondence theory on \(p\)-Fock spaces with applications to Toeplitz algebras*, arXiv:1911.12668 (2019); *Journal of Functional Analysis* 279 (2020), 108661. https://arxiv.org/abs/1911.12668
4. J. Keller and F. Luef, *Polyanalytic Toeplitz operators: isomorphisms, symbolic calculus and approximation of Weyl operators*, arXiv:1905.07741 (2019); *Journal of Fourier Analysis and Applications* 27 (2021), article 47. https://arxiv.org/abs/1905.07741
5. H. McNulty, *Translation Invariant Operators on True Polyanalytic \(p\)-Fock Spaces*, *Integral Equations and Operator Theory* 98 (2026), article 49. https://doi.org/10.1007/s00020-026-02863-9
