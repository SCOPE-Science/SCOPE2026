# Paired mixed commutator spectra and sharp weak-Schatten law on weighted harmonic Bergman spaces

## Finding

For real \(\alpha>-1\) and **distinct** positive integers \(m,n\), let \(A_j=Q_\alpha M_{z^j}|_{h^2_\alpha}\) be the Toeplitz operator on the complex weighted harmonic Bergman space of the disk. The mixed commutator
\[
C_{m,n}=A_m A_n^*-A_n^* A_m
\]
is compact and has three quantitative properties:

1. Every positive singular value has even multiplicity, so \(s_{2j-1}(C_{m,n})=s_{2j}(C_{m,n})\) for all \(j\ge1\).
2. There is an explicit block of \(|m-n|+1\) orthogonal basis vectors in its kernel. The complete singular multiset consists of an explicitly computable finite central block together with **two copies of every** \(b_r\), \(r=0,1,\ldots\), where
\[
h_r=\frac{\Gamma(r+1)\Gamma(\alpha+2)}{\Gamma(r+\alpha+2)},\qquad
b_r=\frac{h_rh_{r+m+n}-h_{r+m}h_{r+n}}{h_r\sqrt{h_{r+m}h_{r+n}}}>0.
\]
3. The sharp singular-value law is
\[
\lim_{j\to\infty}j^2s_j(C_{m,n})=4(\alpha+1)mn.
\]
In particular, for every \(0<p<\infty\),
\[
C_{m,n}\in\mathcal S_p\quad\Longleftrightarrow\quad p>\tfrac12,
\]
and the precise critical logarithmic trace is
\[
\lim_{N\to\infty}\frac1{\log N}\sum_{j=1}^N s_j\bigl(|C_{m,n}|^{1/2}\bigr)=2\sqrt{(\alpha+1)mn}.
\]
The case \(m=n\) is excluded from the new assertion because its self-commutator spectral law has previously been established. No claim is made that the displayed guaranteed nullity is the only possible nullity.

## Assumptions and scope

Write \(d\mu_\alpha(z)=(\alpha+1)(1-|z|^2)^\alpha\,dA(z)/\pi\), where \(dA\) here denotes ordinary planar Lebesgue area. Let \(h^2_\alpha\) be the complex Hilbert space of \(L^2(\mu_\alpha)\) harmonic functions. The projection \(Q_\alpha\) is orthogonal. The symbols \(z^m\) and \(\overline z^{\,n}\) are bounded, so all Toeplitz operators and commutators are bounded everywhere on \(h^2_\alpha\). Singular values count multiplicity and are arranged in nonincreasing order. The asymptotic concerns a fixed \(\alpha,m,n\), not a joint uniform limit.

An orthonormal basis is \(e_k(z)=z^k/\sqrt{h_k}\) for \(k\ge0\), and \(e_k(z)=\overline z^{\,-k}/\sqrt{h_{-k}}\) for \(k<0\), indexed by \(k\in\mathbb Z\); \(h_0=1\). For a positive integer \(j\), write \(A_je_k=w_j(k)e_{k+j}\). Direct angular orthogonality gives
\[
w_j(k)=\begin{cases}
\sqrt{h_{k+j}/h_k},&k\ge0,\\
\sqrt{h_{-k}/h_{-k-j}},&k\le-j,\\
h_j/\sqrt{h_{-k}h_{k+j}},&-j<k<0.
\end{cases}
\]
These numbers are real and positive, and satisfy the reflection identity \(w_j(k)=w_j(-j-k)\).

## Proof

**1. Single-shift reduction.** Because \(A_n^*e_k=w_n(k-n)e_{k-n}\),
\[
C_{m,n}e_k=d_k e_{k+m-n},\quad
d_k=w_n(k-n)w_m(k-n)-w_m(k)w_n(k+m-n).
\]
The translation \(e_k\mapsto e_{k+m-n}\) is unitary. Thus the nonzero singular-value multiset is exactly the multiset of the nonzero \(|d_k|\), and \(|C_{m,n}|\) is diagonal in the indicated basis. No normality assumption is needed.

**2. Exact tails.** For \(k=n+r\), \(r\ge0\), substitute the positive/middle weights into the preceding identity. This gives
\[
d_{n+r}=\frac{\sqrt{h_{r+n}h_{r+m}}}{h_r}-\frac{h_{r+m+n}}{\sqrt{h_{r+m}h_{r+n}}}=-b_r.
\]
For \(k=-m-r\), the same formulas give \(d_{-m-r}=+b_r\). Therefore, apart from the finite central indices \(-m+1\le k\le n-1\), the full spectrum consists of two copies of each exact \(b_r\). The expressions for all central coefficients are completely determined by the displayed three-case \(w_j\) formula and the formula for \(d_k\); there are no unknown or omitted matrix entries.

**3. Positivity, reflection, and forced zero block.** The smooth interpolation
\[
\log h_t=\log\Gamma(t+1)+\log\Gamma(\alpha+2)-\log\Gamma(t+\alpha+2)
\]
has strictly positive second derivative for \(t\ge0\): it equals \(\psi_1(t+1)-\psi_1(t+\alpha+2)>0\), since the trigamma function decreases on positive arguments. Hence \(h_rh_{r+m+n}>h_{r+m}h_{r+n}\), and every \(b_r\) is strictly positive.

Using \(w_j(k)=w_j(-j-k)\) twice in the expression for \(d_k\) gives the exact antisymmetry
\[
d_{n-m-k}=-d_k,\qquad k\in\mathbb Z.
\]
Consequently all nonzero \(|d_k|\) occur in distinct reflected pairs; a fixed point of the reflection necessarily has \(d_k=0\). This proves even multiplicity of every nonzero singular value.

If \(n>m\) and \(0\le k\le n-m\), the three-case formulas yield in both products
\[
w_n(k-n)w_m(k-n)=w_m(k)w_n(k+m-n)
=\frac{h_n}{\sqrt{h_kh_{n-m-k}}}.
\]
Thus \(d_k=0\) throughout this interval of \(n-m+1\) basis indices. For \(m>n\), the conclusion follows by interchanging \(m,n\) and taking adjoints, using \(C_{m,n}^*=C_{n,m}\); the zero block is \(m-n\) translated basis indices plus one, namely \(n-m\le k\le0\). This establishes the asserted nullity lower bound without presuming there are no further zeros.

**4. Sharp spectral asymptotics.** Put \(L(t)=\log h_t\). For fixed positive integers \(m,n\),
\[
L''(t)=\psi_1(t+1)-\psi_1(t+\alpha+2)
=\frac{\alpha+1}{t^2}+O(t^{-3})\quad(t\to\infty).
\]
Thus the double finite difference satisfies
\[
L(r)+L(r+m+n)-L(r+m)-L(r+n)
=\int_0^m\!\int_0^n L''(r+u+v)\,dv\,du
=\frac{(\alpha+1)mn}{r^2}+O(r^{-3}).
\]
Moreover \(h_{r+m+n}/\sqrt{h_{r+m}h_{r+n}}=1+O(r^{-1})\). Factoring \(b_r\) via these expressions gives
\[
b_r=\frac{(\alpha+1)mn}{r^2}+O(r^{-3})\qquad(r\to\infty).
\]
Writing \(\beta=(\alpha+1)mn>0\), the positive-tail counting function is \(\#\{r:b_r>t\}\sim\sqrt{\beta/t}\) as \(t\downarrow0\). Double multiplicity and the finite central set therefore yield
\[
\#\{j:s_j(C_{m,n})>t\}\sim2\sqrt{\beta/t},
\]
which is equivalent to \(j^2s_j(C_{m,n})\to4\beta\). Summation of the resulting \(s_j(|C_{m,n}|^{1/2})\sim2\sqrt\beta/j\) proves the logarithmic coefficient. Comparison with \(\sum j^{-2p}\) proves the Schatten phase transition, including failure at the endpoint \(p=1/2\).

## Verification

The self-contained supplementary Python file `check_harmonic_mixed.py` computes the basis weights from gamma moments, builds the commutator coefficients using two independent products, checks reflected equality and the exact tail formula, checks the forced zero block, and compares several large-index tails with their analytical leading coefficient. The checker reports 16,278 finite assertions passed. Those finite tests do not prove the universal spectral result; the proof is given above. The asymptotic equality and strict log-convexity depend on the explicit gamma-moment formula and positive-argument trigamma properties.

## Relationship to prior work

Tian–Wang–Zhao (2026), arXiv:2609.14635, proves a qualitative commuting rigidity result for analytic/coanalytic Toeplitz operators on the unweighted harmonic Bergman space, with an extension to standard weights indicated in their discussion. The present assertion instead concerns quantitative nonzero mixed commutators and their complete singular-value tails. Dong–Zhou (2013) proves a symmetry number governing vanishing coefficients of quasihomogeneous commutators; a vanishing-pattern reflection does not itself give equality of singular-value magnitudes or the weak-Schatten constant. Dong–Zhou (2014), arXiv:1411.0213, treats finite-rank commutators, not the precise infinite tail spectral asymptotics here. Iqtaish–Louhichi–Yousef (2025) addresses commuting classification. Chbichib–Ghiloufi (2026), arXiv:2605.24698, treats \([M_u,Q_\alpha]\) on the ambient \(L^2\) space with order \(1/j\), a different commutator from the Toeplitz–Toeplitz commutator treated here. Prior work on the weighted *self*-commutator \(m=n\) includes the law with coefficient \(4(\alpha+1)m^2\), and is expressly not claimed anew. The new claim is the mixed case \(m\ne n\), its paired spectrum and exact cross-index spectral coefficient.

## Limitations

The statement does not cover arbitrary analytic symbols, general quasihomogeneous symbols, domains other than the disk, or the uniform simultaneous limit of \(m,n,\alpha\). The given zero block is a lower bound, not an assertion of the exact kernel. Full publication priority against all older operator-theoretic equivalent formulations cannot be certified by literature searches; only a best-knowledge originality assessment is possible. Independent audit has not been performed. The result concerns compact bounded Toeplitz commutators; it does not say that the factors commute or that the commutator has finite rank.

## References

- X. Tian, J. Wang, X. Zhao, *Commuting analytic and co-analytic Toeplitz operators on the harmonic Bergman space*, arXiv:2609.14635 (first submitted 2026-09-13), https://arxiv.org/abs/2609.14635.
- X.-T. Dong, Z.-H. Zhou, *Commuting Quasihomogeneous Toeplitz Operators on the Harmonic Bergman Space*, Complex Analysis and Operator Theory 7 (2013), 1267–1285, DOI:10.1007/s11785-012-0223-0.
- X.-T. Dong, Z.-H. Zhou, *Ranks of Commutators and Generalized Semicommutators of Quasihomogeneous Toeplitz Operators*, arXiv:1411.0213 (2014), https://arxiv.org/abs/1411.0213.
- H. Iqtaish, I. Louhichi, A. Yousef, *On the commuting problem of Toeplitz operators on the harmonic Bergman space*, AIMS Mathematics 10 (2025), 17232–17247, DOI:10.3934/math.2025770.
- K. Chbichib, N. Ghiloufi, *Spectral properties of commutators on harmonic Bergman spaces of the unit disk*, arXiv:2605.24698 (2026), https://arxiv.org/abs/2605.24698.
