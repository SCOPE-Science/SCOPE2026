# Infinite separation rank of exponential-type Fock kernels

## Finding
Let \(V:\mathbb C^2\to\mathbb C\) be entire, not identically zero, and suppose that for some \(C,a>0\),
\[
|V(z,w)|\le C e^{a(|z|+|w|)}\qquad(z,w\in\mathbb C).
\]
Then the kernel \(K(z,w)=e^{zw}V(z,w)\) has **infinite algebraic separation rank**. Equivalently, for every integer \(m\ge1\) there are \(w_1,\ldots,w_m\in\mathbb C\) such that the entire functions \(K(\cdot,w_j)\), \(1\le j\le m\), are linearly independent. No finite expression \(K(z,w)=\sum_{j=1}^r A_j(z)B_j(w)\) is possible, even with arbitrary functions \(A_j,B_j\).

Consequently, let \(\mathcal F^2(\mathbb C)\) be the standard Bargmann--Fock Hilbert space with Gaussian weight \(\pi^{-1}e^{-|z|^2}\), and let \(P=T_{\varphi_1}\cdots T_{\varphi_N}\) be a finite product with \(N\ge1\),
\[
\varphi_j=f_j+\overline{g_j},\qquad
|f_j(z)|+|g_j(z)|\le C_j e^{a_j|z|},\qquad\varphi_j\not\equiv0.
\]
The functions \(f_j,g_j\) are entire and \(C_j,a_j>0\). On the common invariant dense space containing every coherent state \(k_w(z)=e^{zw}\), the range of \(P\) already has infinite algebraic dimension. In fact for every \(m\) one can choose \(m\) coherent states with linearly independent images. This does not require the factors or their product to extend boundedly to the whole Hilbert space.

## Assumptions and scope
The variable \(w\) in \(k_w(z)=e^{zw}\) is an **independent complex parameter** (it indexes the usual reproducing kernel at \(\overline w\)). Joint exponential type means one uniform exponent \(a\) in both variables; separate exponential type with a constant depending arbitrarily on the other variable is not claimed. All kernel-rank assertions are algebraic, not statements about singular values, closed ranges, or Schatten classes. The operator consequence concerns one complex dimension and the common invariant domain \(\mathcal H(\mathbb C)\) defined and justified in Liu--Qin--Huang [1].

## Proof
**1. Fourier--Borel transform of a one-variable exponential-type entire function.** Let \(u\) be entire with \(|u(w)|\le C_u e^{a|w|}\). Cauchy's estimate on the circle of radius \(n/a\) gives, for \(n\ge1\),
\[
|u^{(n)}(0)|\le C_u n!e^n(a/n)^n\le C_u(ea)^n.
\]
The \(n=0\) bound also holds. Fix \(R>ea\). Its Laurent series
\[
\mathcal B u(\zeta)=\sum_{n=0}^\infty
\frac{u^{(n)}(0)}{\zeta^{n+1}}
\]
therefore converges absolutely and locally uniformly when \(|\zeta|>R\), and is \(O(1/\zeta)\) at infinity. The transform is injective: a zero Laurent series has all derivatives zero. Crucially,
\[
\mathcal B(e^{\lambda w}u(w))(\zeta)
=\mathcal B u(\zeta-\lambda)
\]
for sufficiently large \(|\zeta|\). This follows by Leibniz's rule and the convergent expansion \((\zeta-\lambda)^{-k-1}=\sum_{h\ge0}\binom{k+h}{k}\lambda^h\zeta^{-k-h-1}\). No distributional boundary-value theorem is used.

**2. Separation lemma.** Fix finitely many nonzero entire functions \(u_j\) satisfying \(|u_j(w)|\le C_j e^{a|w|}\) with the **same** \(a\), and choose complex numbers \(\lambda_j\) satisfying \(|\lambda_i-\lambda_j|>4R\) for \(i\ne j\), where \(R>ea\). Then the functions \(e^{\lambda_jw}u_j(w)\) are linearly independent.

Indeed, if \(\sum_j c_j e^{\lambda_jw}u_j(w)=0\), applying the transform gives
\[
\sum_j c_j\mathcal Bu_j(\zeta-\lambda_j)=0
\]
first near infinity. Every summand is holomorphic outside its closed radius-\(R\) disk centered at \(\lambda_j\). The complement \(\Omega\) of their union is connected, so the identity theorem extends this relation throughout \(\Omega\). Fix an index \(i\) with \(c_i\ne0\). On the disk \(|\zeta-\lambda_i|<2R\), all functions \(\mathcal Bu_j(\zeta-\lambda_j)\) with \(j\ne i\) are holomorphic because the centers are more than \(4R\) apart. Thus the relation defines a holomorphic continuation of \(\mathcal Bu_i(\zeta-\lambda_i)\) across its disk of radius \(R\); the definition agrees on the overlapping annulus \(R<|\zeta-\lambda_i|<2R\). The continued transform is entire and vanishes at infinity, hence is zero by Liouville's theorem. Injectivity forces \(u_i=0\), a contradiction.

**3. Infinite rank.** Because \(V\not\equiv0\), some coefficient function \(v_k(z)=\partial_w^kV(z,0)\) is not identically zero. It has discrete zeros in \(\mathbb C\), so one can select arbitrarily many real numbers \(z_1,\ldots,z_m\) with pairwise distances greater than \(4R\), avoiding its zeros. Put \(u_i(w)=V(z_i,w)\). Each \(u_i\ne0\) and satisfies \(|u_i(w)|\le C e^{a|z_i|}e^{a|w|}\). The separation lemma applied with \(\lambda_i=z_i\) proves that the functions \(w\mapsto K(z_i,w)=e^{z_iw}u_i(w)\) are linearly independent. Elementary linear algebra for independent functions yields evaluation points \(w_1,\ldots,w_m\) such that the matrix \([K(z_i,w_j)]_{i,j=1}^m\) is invertible. Therefore the column functions \(z\mapsto K(z,w_j)\) are independent, for arbitrary \(m\), as asserted.

**4. Toeplitz-product consequence.** Liu--Qin--Huang [1, Section 4, equations (4.2)--(4.3)] construct, for the stated harmonic symbols, a jointly exponential-type entire function \(V\) satisfying
\[
(Pk_w)(z)=e^{zw}V(z,w).
\]
Their Theorem 1.2 proves that \(V\equiv0\) for such a product only when a factor symbol vanishes. The hypotheses above match theirs exactly: nonzero harmonic symbols with both entire parts of exponential type, and the common invariant domain containing all coherent states. Hence \(V\not\equiv0\). Apply Step 3. The coherent-state images of \(P\) span an infinite-dimensional subspace of the range, proving the operator consequence.

## Verification
The proof is independent of numerical experiments and finite enumeration. Its critical steps are the uniform Cauchy derivative bound, an absolutely convergent Laurent/Borel translation identity, gluing of analytic continuations across **disjoint** singularity disks, and the passage from independent rows to an invertible finite evaluation matrix. The kernel representation and nonvanishing premise in Step 4 are taken from [1], whose hypotheses and formulas were checked against the statement above. In particular the conclusion does **not** incorrectly infer infinite rank merely from nonvanishing of an operator.

As a boundary check, if \(V(z,w)=e^{-zw}\) then \(K(z,w)=1\) has rank one, but \(V\) is **not** jointly of exponential type: along \(z=t\), \(w=-t\) its modulus grows as \(e^{t^2}\). This exhibits why the joint growth hypothesis is essential. Another boundary check is that \(V\equiv0\) gives the zero kernel and is explicitly excluded.

## Relationship to prior work
Liu, Qin and Huang [1] establish the nonzero-product theorem and the joint-exponential-type kernel formula, but do not assert that the resulting kernel or operator has infinite algebraic rank. The present separated-Borel-transform lemma supplies that additional conclusion for **every nonzero** joint exponential-type factor, not just for the Toeplitz examples. Bauer and Le [2] analyze single-symbol finite rank and general zero products, but do not give this all-length harmonic finite-product rank theorem. Borichev and Rozenblum [3] prove a finite-rank theorem for a **single Toeplitz symbol** under integrability/growth conditions, not for an arbitrary finite product. Published finite-frequency Fock operator-algebra findings [4] exclude zero products in a more restrictive exponential-polynomial class but do not establish the general kernel separation-rank conclusion. These distinctions are statements of implication and hypothesis, not title comparisons.

## Limitations
The Fock part relies on the published-in-preprint nonvanishing theorem of [1]; this note proves the new separation-rank lemma directly rather than reconstructing [1]'s long cancellation argument. No result is asserted for general bounded nonharmonic Toeplitz symbols, several-variable Fock products, or joint kernels outside the stated exponential-type class. The conclusion has no quantitative lower singular-value bounds, and unbounded Toeplitz factors may have no bounded Hilbert-space extension. Standard Fourier--Borel transform theory could encode the abstract separation principle implicitly in older sources; the historical-priority assessment is therefore provisional pending independent review.

## References
[1] Y. Liu, J. Qin and S. Huang, *Finite zero products of Toeplitz operators with harmonic symbols*, arXiv:2610.30209v1, first posted 2026-10-21, Sections 1--4. https://arxiv.org/html/2610.30209v1

[2] W. Bauer and T. Le, *Algebraic properties and the finite rank problem for Toeplitz operators on the Segal--Bargmann space*, J. Funct. Anal. 261 (2011), 2617--2640, Section 5. https://doi.org/10.1016/j.jfa.2011.07.006

[3] A. Borichev and G. Rozenblum, *The finite rank theorem for Toeplitz operators on the Fock space*, arXiv:1303.2996v1 (2013), Theorem 3.1. https://arxiv.org/html/1303.2996v1

[4] *Finite-frequency pluriharmonic Fock Toeplitz operators form a zero-divisor-free algebra*, public mathematical record (2026), https://github.com/Resultary/2026/tree/main/2026/9/19/SCOPE-zero-divisor-free-fock-toeplitz-exponential-polynomials--ea7c12552247
