# Mean-zero fourth-moment obstruction for the third symmetric Fourier cutoff

## Finding
Let \(\mathbb T=\{e^{i\theta}:\theta\in\mathbb R\}\) carry normalized Haar measure \(dm=d\theta/(2\pi)\), and let
\[
S_3 f(\zeta)=\sum_{n=-3}^{3}\widehat f(n)\zeta^n,
\qquad \widehat f(n)=\int_{\mathbb T}f(\zeta)\overline\zeta^{\,n}\,dm(\zeta).
\]
There exists a continuous, odd, unimodular, complex-valued function \(f\) of mean zero for which
\[
\boxed{\|S_3f\|_{L^4(\mathbb T)}>\|f\|_{L^\infty(\mathbb T)}=1.}
\]
Indeed an explicit one-parameter family \(f_t(e^{i\theta})=e^{i\theta}\exp(it\cos2\theta)\), \(t\in\mathbb R\), satisfies
\[
\|S_3 f_t\|_4^4
=1+\frac{5}{576}t^6-\frac{11}{2304}t^8+O(t^{10})
\qquad(t\to0).
\]
Thus every sufficiently small nonzero \(t\) witnesses failure, and the specific value \(t=1\) also gives a rigorously certified strict inequality. Consequently the operator norm \(\|S_3\|_{L^\infty_0(\mathbb T)\to L^4(\mathbb T)}\) is strictly greater than one. The same witness violates an asserted contraction into any \(L^p\) with \(p\ge4\).

## Assumptions and scope
The domain \(L^\infty_0(\mathbb T)\) consists of **complex-valued** essentially bounded functions with zeroth Fourier coefficient zero. No analyticity is required. Oddness means \(f(-\zeta)=-f(\zeta)\). The operator \(S_3\) is the **sharp symmetric Fourier partial sum**, not the Poisson convolution \(P_r\). The comparison uses probability-normalized \(L^p\) norms. The theorem concerns a finite Fourier-section contraction, not the unresolved Poisson Schwarz-contractivity conjecture.

## Proof
For each real \(t\), \(|f_t|\equiv1\). Since \(\cos(2(\theta+\pi))=\cos2\theta\), one has \(f_t(-\zeta)=-f_t(\zeta)\), whence \(\widehat f_t(0)=0\).

Let \(J_j\) denote the Bessel function of the first kind of integer order \(j\). The Jacobi–Anger identity
\[
\exp(it\cos 2\theta)=\sum_{j\in\mathbb Z}i^jJ_j(t)e^{2ij\theta}
\]
converges uniformly for fixed real \(t\). Hence, with real numbers \(A=J_0(t)\), \(B=J_1(t)\) and \(C=J_2(t)\), the four retained Fourier coefficients give
\[
S_3 f_t(\zeta)=-C\zeta^{-3}+iB\zeta^{-1}+A\zeta+iB\zeta^3.
\]
Write \(g=S_3f_t\). Its squared modulus is a trigonometric polynomial whose nonnegative-frequency Fourier coefficients are exactly
\[
\widehat{|g|^2}(0)=A^2+2B^2+C^2,\qquad
\widehat{|g|^2}(2)=-iBC,\qquad
\widehat{|g|^2}(4)=B^2-AC,\qquad
\widehat{|g|^2}(6)=-iBC.
\]
The corresponding negative coefficients are the conjugates, and all others vanish. Parseval's identity therefore yields the **exact** fourth-moment identity
\[
\boxed{\|S_3f_t\|_4^4=(A^2+2B^2+C^2)^2+4B^2C^2+2(B^2-AC)^2.}
\]
The Bessel power series
\[
J_j(t)=\sum_{k=0}^{\infty}
\frac{(-1)^k(t/2)^{2k+j}}{k!(k+j)!}\qquad(j=0,1,2)
\]
converges absolutely. Inserting it into the preceding exact polynomial and collecting powers gives
\[
\|S_3 f_t\|_4^4
=1+\frac5{576}t^6-\frac{11}{2304}t^8
+\frac{473}{460800}t^{10}+O(t^{12}).
\]
The positive first nonzero coefficient proves the asserted strict inequality for all sufficiently small \(t\ne0\). Since \(\|f_t\|_\infty=1\), this is a genuine norm violation.

There is also an explicit certificate at \(t=1\), not reliant on floating-point approximations. For \(j=0,1,2\) define
\[
L_j=\sum_{k=0}^{9}\frac{(-1)^k}{2^{2k+j}k!(k+j)!},\qquad
U_j=\sum_{k=0}^{10}\frac{(-1)^k}{2^{2k+j}k!(k+j)!}.
\]
Alternating-series remainder bounds give \(0<L_j<J_j(1)<U_j\). Direct rational arithmetic establishes \(L_1^2>U_0U_2\) and
\[
(L_0^2+2L_1^2+L_2^2)^2
+4L_1^2L_2^2+2(L_1^2-U_0U_2)^2>1.
\]
By the exact fourth-moment identity this lower bound proves \(\|S_3f_1\|_4^4>1\) rigorously. The rational operations are reproduced by the included checker.

Finally normalized Haar measure is a probability measure, so \(\|S_3f_1\|_p\ge\|S_3f_1\|_4>1\) for every \(p\ge4\).

## Verification
Run `python3 verify_bessel.py` from the package directory. The checker uses only Python standard-library exact rational arithmetic. It computes alternating rational enclosures of \(J_0(1)\), \(J_1(1)\), and \(J_2(1)\), verifies the positive lower margin, and independently checks the exact Taylor coefficients through order ten. It terminates with `VERIFY_OK`. For orientation only, the fourth moment at \(t=1\) is approximately \(1.00481446547905\); the strict inequality rests on the rational certificate, not these digits.

## Relationship to prior work
Kovalev [1], Theorem 1.3 and Proposition 4.1, proves that the same symmetric sections \(S_N\) map \(L^\infty(\mathbb T)\) contractively to \(L^3(\mathbb T)\) for every integer \(N\ge0\), and obtains the complex Poisson \(L^\infty_0\)-to-\(L^3\) bound by taking a positive Abel mean of these sections. Remark 4.3 exhibits failure for exponents above three by testing \(S_1\) on functions with **nonzero** mean. The present result isolates a different obstruction: even restricting to odd, unimodular **zero-mean** input does not make the higher section \(S_3\) contractive into the conjectural exponent four. Thus the Abel-section proof route cannot simply be upgraded by replacing three by four; this does **not** refute Kovalev's Poisson \(L^\infty_0\)-to-\(L^4\) conjecture.

Marzo and Seip [2] prove sharp \(L^\infty\)-to-\(L^4\) contraction for the **one-sided Riesz projection**, a different multiplier. Kovalev and Yang [3] address sharp harmonic first-coefficient and first-order limiting bounds, not the displayed third symmetric Fourier-section obstruction. The published result [4] verifies that a canonical odd unimodular family does *not* violate the Poisson endpoint inequality; it concerns a Poisson multiplier rather than \(S_3\), and neither asserts nor implies the present noncontractivity. No claim of exhaustive priority is made.

## Limitations
This is a counterexample to contraction of \(S_3\), not a determination of the exact norm of \(S_3\), not a sharp minimum frequency cutoff for arbitrary inputs, and not a counterexample to any positive Poisson-semigroup inequality. The sixth-order asymptotic is local in \(t\); the separate exact-rational argument certifies \(t=1\). The literature comparison cannot rule out an unindexed equivalent Fourier-section example.

## References
[1] Leonid V. Kovalev, *Schwarz-contractivity of the Poisson operator*, arXiv:2609.28938v1 (first publicly posted 2026-09-24), Sections 4–5, especially Proposition 4.1, Remark 4.3, and Conjecture 5.1. https://arxiv.org/abs/2609.28938

[2] Jordi Marzo and Kristian Seip, *\(L^\infty\) to \(L^p\) constants for Riesz projections*, arXiv:1005.1842v1 (2010), Theorem 1. https://arxiv.org/abs/1005.1842

[3] Leonid V. Kovalev and X. Yang, *Near-isometric duality of Hardy norms with applications to harmonic mappings*, arXiv:2001.09465 (2020). https://arxiv.org/abs/2001.09465

[4] *Exact endpoint deficit for the canonical complex Poisson obstruction family*, publicly available mathematical finding (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-endpoint-deficit-for-the-canonical-complex-poisson-obstruc--87cdbe275635
