# Extremizer spectrum and index rigidity for sharp harmonic Hardy coefficients
## Finding
Fix \(1<p<\infty\), let \(q=p/(p-1)\), \(r=1/(p-1)\), and let \(n\ge1\). Write normalized arclength on the circle as \(d\sigma=dt/(2\pi)\), and set
\[
I_q=\int_{\mathbb T}|\cos t|^q\,d\sigma(t)
=\frac{{\Gamma((q+1)/2)}}{{\sqrt{{\pi}}\,\Gamma((q+2)/2)}},
\qquad C_p=2I_q^{{1/q}}.
\]
For a nonzero \(f=h+\overline g\in\mathbf h^p\), with
\[
h(z)=\sum_{{j\ge0}}a_jz^j,\qquad g(z)=\sum_{{j\ge1}}b_jz^j,
\]
equality in the sharp coefficient estimate
\[
|a_n|+|b_n|=C_p\|f\|_p
\]
holds if and only if its radial boundary trace is
\[
f^*(e^{{it}})=\alpha\,\Phi_r(nt+\theta)\quad\text{{a.e.}},
\qquad
\Phi_r(u)=\operatorname{{sgn}}(\cos u)|\cos u|^r,
\]
for some \(\alpha\in\mathbb C\setminus\{{0\}}\) and \(\theta\in\mathbb R\).

Moreover, for every positive odd integer \(m\), define
\[
c_m(r)=
\frac{{2^{{-r}}\Gamma(r+1)}}
{{\Gamma((r+m+2)/2)\Gamma((r-m+2)/2)}},
\]
where reciprocal Gamma is interpreted as zero at its poles. Then every extremizer satisfies
\[
a_{{mn}}=\alpha e^{{im\theta}}c_m(r),\qquad
\overline{{b_{{mn}}}}=\alpha e^{{-im\theta}}c_m(r),
\]
and all positive-index coefficients whose indices are not odd multiples of \(n\) vanish.

Consequently the extremizer has finite Fourier spectrum exactly when
\[
r=2s+1\quad\Longleftrightarrow\quad p=1+\frac1{{2s+1}},\qquad s=0,1,2,\ldots.
\]
In that case its highest positive frequency is \((2s+1)n\). For every other \(p\in(1,\infty)\), every positive odd multiple of \(n\) occurs with a nonzero analytic and coanalytic coefficient. Finally, for fixed \(p\), a nonzero function cannot attain the sharp coefficient constant at two distinct indices.

## Assumptions and scope
The harmonic Hardy norm is the radial \(L^p\) norm used in arXiv:2609.33159v1. The statement concerns \(1<p<\infty\) only. In this range the radial trace \(F=f^*\) lies in \(L^p(\mathbb T)\), \(\|F\|_p=\|f\|_p\), and
\[
a_n=\int_\mathbb T F(e^{{it}})e^{{-int}}\,d\sigma(t),\qquad
\overline{{b_n}}=\int_\mathbb T F(e^{{it}})e^{{int}}\,d\sigma(t).
\]
The sharp constant \(C_p\) is the constant established in Theorem 1.3 of arXiv:2609.33159v1. The result here classifies every equality case and derives its entire coefficient spectrum; it does not claim a new value of the sharp constant.

## Proof
Let \(F=f^*\). First, \(C_p>1\). Indeed, monotonicity of normalized \(L^s\) norms gives \(I_q^{{1/q}}\ge \int_\mathbb T|\cos t|\,d\sigma(t)=2/\pi\), hence \(C_p\ge4/\pi>1\). Therefore an extremizer cannot have \(a_n=0\) or \(b_n=0\), because a single Fourier coefficient functional has \(L^p\to\mathbb C\) norm one.

Choose unimodular \(\lambda,\mu\) so that \(\lambda a_n=|a_n|\) and \(\mu\overline{{b_n}}=|b_n|\). Then
\[
|a_n|+|b_n|
=\left|\int_\mathbb T F(e^{{it}})Q(t)\,d\sigma(t)\right|,
\qquad
Q(t)=\lambda e^{{-int}}+\mu e^{{int}}.
\]
There are a unimodular \(\eta\) and a real \(\theta\) with
\[
Q(t)=2\eta\cos(nt+\theta).
\]
Hölder's inequality gives
\[
|a_n|+|b_n|\le\|F\|_p\|Q\|_q
=2I_q^{{1/q}}\|F\|_p=C_p\|F\|_p.
\]
Because \(1<p,q<\infty\), equality in complex Hölder is rigid: equality holds exactly when, for some nonzero constant \(\kappa\),
\[
F=\kappa\,\overline Q|Q|^{{q-2}}\quad\text{{a.e.}}
\]
Absorbing constants and the unimodular factor into \(\alpha\) yields
\[
F(e^{{it}})=\alpha\,\operatorname{{sgn}}(\cos(nt+\theta))|\cos(nt+\theta)|^{{q-1}},
\]
and \(q-1=r\). Conversely, for this trace,
\[
\|F\|_p=|\alpha|I_q^{{1/p}},\qquad
|a_n|=|b_n|=|\alpha|I_q,
\]
so the ratio is \(2I_q^{{1-1/p}}=2I_q^{{1/q}}=C_p\). This proves the complete equality classification.

It remains to compute the spectrum. Put
\[
c_m=\int_\mathbb T\Phi_r(u)e^{{-imu}}\,d\sigma(u).
\]
The function \(\Phi_r\) is even and satisfies \(\Phi_r(u+\pi)=-\Phi_r(u)\), so only odd Fourier modes can occur. Let \(G(u)=|\cos u|^{{r+1}}=\cos u\,\Phi_r(u)\). Since \(r>0\), \(G\) is absolutely continuous and
\[
G'(u)=-(r+1)\sin u\,\Phi_r(u)\quad\text{{a.e.}}
\]
Taking Fourier coefficients of these two identities gives
\[
\widehat G(m)=\frac{{c_{{m-1}}+c_{{m+1}}}}2,
\qquad
im\widehat G(m)=\frac{{i(r+1)}}2\bigl(c_{{m-1}}-c_{{m+1}}\bigr),
\]
and therefore
\[
(m+r+1)c_{{m+1}}=(r+1-m)c_{{m-1}}.
\]
For \(m=2k\),
\[
c_{{2k+1}}=\frac{{r+1-2k}}{{r+1+2k}}c_{{2k-1}},
\qquad
c_1=\int_\mathbb T|\cos u|^{{r+1}}\,d\sigma(u)
=\frac{{\Gamma((r+2)/2)}}{{\sqrt\pi\,\Gamma((r+3)/2)}}.
\]
Iteration and the Gamma duplication identity yield
\[
c_m(r)=
\frac{{2^{{-r}}\Gamma(r+1)}}
{{\Gamma((r+m+2)/2)\Gamma((r-m+2)/2)}}
\]
for positive odd \(m\). Shifting by \(\theta\), dilating the argument by \(n\), and multiplying by \(\alpha\) gives the asserted formulas for \(a_{{mn}}\) and \(\overline{{b_{{mn}}}}\).

The recurrence coefficient vanishes for the first time precisely when \(r=2s+1\) is a positive odd integer; then \(\Phi_r(u)=\cos^{{2s+1}}u\) and the Fourier series terminates at frequency \(2s+1\). If \(r\) is not a positive odd integer, no recurrence factor vanishes, so every positive odd Fourier mode is nonzero. Since \(r=1/(p-1)\), this is exactly the stated discrete family of \(p\)-values.

For index rigidity, suppose the same nonzero boundary trace is an extremizer at indices \(n\) and \(m\). The two classified representatives are continuous functions and agree almost everywhere, hence everywhere. The zero set of \(\Phi_r(nt+\theta)\) on one period has exactly \(2n\) points, while the zero set for index \(m\) has exactly \(2m\) points. Equality of the functions therefore forces \(n=m\).

## Verification
The proof is analytic. A standalone standard-library checker numerically integrates representative cosine-power Fourier coefficients, checks the exact Gamma formula and recurrence, and checks truncation for several odd integer values of \(r\). These finite computations are sanity checks only; they are not used to infer the infinite theorem.

## Relationship to prior work
Chen, Huang, Jin and Li, arXiv:2609.33159v1, determine the sharp constant for this harmonic Hardy coefficient inequality for \(1\le p<\infty\). Their proof derives the bound from the two boundary Fourier coefficients and Hölder's inequality and constructs an explicit cosine-power boundary function to prove sharpness. The source does not state the converse equality classification, the full coefficient spectrum of every extremizer, the finite-spectrum phase, or disjointness of extremizer families across coefficient indices.

Ahamed and Hossain, arXiv:2604.14217v1, quote the coefficient theorem of Shi, Li and Lian and use it in a Bohr-radius setting; the quoted theorem supplies coefficient bounds and examples but not the finite-\(p\) all-extremizer classification above. Chen, Ponnusamy and Wang (2012) give earlier coefficient estimates and classify extremals for their \(p=\infty\) result, not for the new finite-\(p\) sharp constant. The 2026 Shi-Li-Lian paper is highly relevant; its abstract and a precise quotation of its coefficient theorem were available, but complete primary text was not available through accessible open sources during this review. Thus an unobserved equivalent finite-\(p\) equality classification there remains a residual literature risk.

The Gamma-form Fourier coefficients of cosine powers are classical algebra and are not claimed independently as new. The contribution claimed here is the complete equality-case geometry for the newly sharp coefficient theorem and the structural consequences for the entire harmonic spectrum and coefficient-order rigidity.

## Limitations
The endpoint \(p=1\) is excluded because the strict Hölder equality argument used here degenerates there. No quantitative stability theorem for near-extremizers is claimed. The result does not improve the sharp constant itself. The inaccessible complete text of the Shi-Li-Lian paper leaves a specific, disclosed originality risk, although the accessible theorem statement quoted in later open literature does not imply the classification proved here.

## References
1. S. Chen, M. Huang, L. Jin, Q. Li, “Sharp constant problems for harmonic mappings,” arXiv:2609.33159v1, 2026.
2. M. Ahamed, R. Hossain, arXiv:2604.14217v1, 2026.
3. S. Chen, S. Ponnusamy, X. Wang, “Integral means and coefficient estimates on planar harmonic mappings,” Annales Fennici Mathematici 37 (2012), 69–79, doi:10.5186/aasfm.2012.3707.
4. Q. Shi, X. Li, X. Lian, “Estimates on the Schwarz Lemma and Landau Theorem for a Harmonic Mapping with a Given Boundary Function in Lebesgue Space,” Computational Methods and Function Theory (2026), doi:10.1007/s40315-025-00600-8.
