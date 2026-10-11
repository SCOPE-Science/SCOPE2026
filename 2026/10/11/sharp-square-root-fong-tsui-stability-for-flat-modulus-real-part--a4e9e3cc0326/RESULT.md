# Sharp square-root Fong–Tsui stability for flat-modulus real parts

## Finding
Let \(H\ne\{0\}\) be a complex Hilbert space and let \(T\in\mathcal B(H)\). Define its Cartesian parts and one-sided modulus-order defect by
\[
A=\operatorname{Re}T=\frac{T+T^*}{2},\qquad
B=\operatorname{Im}T=\frac{T-T^*}{2i},\qquad
d(T)=\bigl\|\bigl(|T|-|A|\bigr)_+\bigr\|.
\]
Suppose \(a=\|A\|\) and \(|A|=aP\) for an orthogonal projection \(P\). Then
\[
\boxed{\|\operatorname{Im}T\|^2\le 2a\,d(T)+d(T)^2.}
\]
For every **fixed** self-adjoint \(A\) with this property and every \(\varepsilon\ge0\), the sharp constrained profile is
\[
\boxed{\sup\left\{\|B\|:B=B^*,\ \bigl\|\bigl(|A+iB|-|A|\bigr)_+\bigr\|\le\varepsilon\right\}=\sqrt{2a\varepsilon+\varepsilon^2}.}
\]
Thus, even allowing completely noncommuting imaginary parts, the optimal small-defect exponent is \(1/2\) when \(a>0\).

## Assumptions and scope
All operators are bounded on an arbitrary nonzero complex Hilbert space, without restrictions on dimension, separability, compactness, or the commutator \([A,B]\). The symbol \(X_+\) is the positive part of a bounded self-adjoint operator \(X\), and \(d(T)\) is the smallest scalar \(\varepsilon\ge0\) for which \(|T|\le|A|+\varepsilon I\). The flat-modulus condition \(|A|=aP\) is equivalent to \(A^2=a^2P\), and to \(A/a\) being a self-adjoint partial isometry if \(a>0\). In the zero case \(A=0\), set \(a=0\), \(P=0\). The nonzero spectrum of \(A\) can contain either or both signs and can have infinite multiplicity.

## Proof
**Upper bound.** Write \(S=|T|\), \(\varepsilon=d(T)\), and \(N=\|T\|=\|S\|\). Functional calculus for the self-adjoint difference \(S-aP\) gives \(S-aP\le(S-aP)_+\le\varepsilon I\), whence
\[
0\le S\le aP+\varepsilon I,\qquad N\le a+\varepsilon.
\]
If \(a=0\), then \(T=iB\), \(|T|=|B|\), and \(\varepsilon=\|B\|\), proving equality in the claimed upper bound. Assume henceforth \(a>0\). Since \(\|\operatorname{Re}T\|\le\|T\|\), we also have \(a\le N\).

For \(B=0\), the assertion is immediate. Otherwise choose an endpoint \(\lambda\in\sigma(B)\) such that \(|\lambda|=\|B\|\), and choose unit approximate eigenvectors \(x_k\) with \(\|(B-\lambda I)x_k\|\to0\). Such vectors exist by the spectral theorem for bounded self-adjoint operators; no eigenvector is assumed. Put \(p_k=\langle Px_k,x_k\rangle\in[0,1]\). Because \(A=A^*\), the cross term in \(\|(A+i\lambda I)x_k\|^2\) vanishes, and \(A^2=a^2P\) yields
\[
\|Tx_k\|^2=\|Ax_k\|^2+\lambda^2+o(1)=a^2p_k+\|B\|^2+o(1).
\]
For every positive operator \(S\) with \(\|S\|=N\), functional calculus gives \(S^2\le NS\). Hence
\[
\|Tx_k\|^2=\langle S^2x_k,x_k\rangle
\le N\langle Sx_k,x_k\rangle
\le N(ap_k+\varepsilon).
\]
Combining these estimates and using \(a\le N\le a+\varepsilon\),
\[
\begin{aligned}
\|B\|^2
&\le a(N-a)p_k+N\varepsilon+o(1)\\
&\le a(N-a)+N\varepsilon+o(1)\\
&\le a\varepsilon+(a+\varepsilon)\varepsilon+o(1).
\end{aligned}
\]
Letting \(k\to\infty\) proves \(\|B\|^2\le2a\varepsilon+\varepsilon^2\).

**Sharpness for each fixed real part.** If \(a>0\), then \(P\ne0\). For prescribed \(\varepsilon\ge0\), put \(b=\sqrt{2a\varepsilon+\varepsilon^2}\) and \(B=bP\). Since \(A^2=a^2P\) and \(AP=PA=A\), these parts commute and
\[
(A+iB)^*(A+iB)=A^2+B^2=(a^2+b^2)P=(a+\varepsilon)^2P.
\]
Therefore \(|A+iB|=(a+\varepsilon)P\), \(d(A+iB)=\varepsilon\), and \(\|B\|=b\), giving equality. If \(a=0\), choose \(B=\varepsilon I\), so \(d(iB)=\varepsilon=\|B\|\). The upper bound and these witnesses yield the asserted exact supremum. Finally, at fixed \(a>0\), \(b\sim\sqrt{2a\varepsilon}\) as \(\varepsilon\downarrow0\), excluding every stronger uniform Hölder exponent.

## Verification
The infinite-dimensional bound uses the self-adjoint approximate point spectrum, the elementary operator inequality \(S^2\le\|S\|S\), and the flat-modulus identity \(A^2=a^2P\). No finite computation replaces these steps. The boundary cases \(a=0\), \(B=0\), and \(\varepsilon=0\) are included. Equality is verified by direct multiplication for any fixed eligible \(A\), including sign-changing and infinite-rank \(A\).

The standalone standard-library script `verify.py` checks an exact \(3\)-\(4\)-\(5\) equality witness and a grid of noncommuting \(2\times2\) examples by the closed formula for the positive square root of a positive \(2\times2\) matrix. These finite tests are supplementary, not a substitute for the proof.

## Relationship to prior work
The original Fong–Tsui condition asks whether \(|T|\le|\operatorname{Re}T|\) forces self-adjointness. Ma's September 9, 2026 manuscript (arXiv:2609.10797v1, Section 4, Theorem 4.1 and Corollary 4.2) establishes a general approximate stability bound with exponent \(1/8\), and its Proposition 5.1 observes that scalar examples rule out exponents above \(1/2\). Aouichaoui, Kittaneh, and Ma (arXiv:2609.16236v1) establish the unrestricted *zero-defect* conjecture, without a quantitative positive-defect classification. An earlier study of partial isometries by Mbekhta and Suciu (arXiv:1511.09055v1) also addresses zero-defect sufficient conditions on \(T\), rather than a flat-modulus assumption on \(\operatorname{Re}T\) with arbitrary perturbations.

The published sharp normal-operator comparison (published-finding corpus record dated October 4, 2026, identifier `SCOPE-sharp-normal-operator-stability-for-the-approximate-fong-tsui-in--969c2f6b34c4`) calculates a sharp \(1/2\)-exponent profile when \(T\) is normal; it explicitly does not cover nonnormal operators. The present theorem instead fixes the spectral geometry of \(\operatorname{Re}T\) and allows arbitrary, including noncommuting, \(\operatorname{Im}T\). For example, on \(\mathbb C^2\), take \(A=\operatorname{diag}(a,0)\) and \(B=\begin{pmatrix}0&t\\t&0\end{pmatrix}\) with \(a,t>0\): then \([A,B]\ne0\) and the theorem applies. Normal-case results, even with matching equality examples, do not imply this assertion.

## Limitations
The flat-modulus hypothesis on \(\operatorname{Re}T\) is essential to the proof; the theorem does not establish an optimal positive-defect exponent for arbitrary real parts. Sharpness is attained by normal examples but the upper estimate holds throughout the nonnormal subclass; equality classifications among nonnormal operators are not asserted. The possibility of an equivalent special-case bound in older unindexed literature is a residual bibliographic risk. Independent mathematical validation has not been performed.

## References
1. Y. Ma, *A General Proof of the Fong–Tsui Conjecture*, arXiv:2609.10797v1 (first public version September 9, 2026), especially Section 4 and Proposition 5.1. https://arxiv.org/html/2609.10797v1
2. M. A. Aouichaoui, F. Kittaneh, and Y. Ma, *A proof of the Fong–Tsui conjecture*, arXiv:2609.16236v1 (September 14, 2026), Sections 1–2. https://arxiv.org/html/2609.16236v1
3. M. Mbekhta and D. Suciu, *Partial isometries and the conjecture of C. K. Fong and S. K. Tsui*, arXiv:1511.09055v1 (2015). https://arxiv.org/html/1511.09055v1
4. *Sharp normal-operator stability for the approximate Fong–Tsui inequality*, published mathematical result (October 4, 2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-sharp-normal-operator-stability-for-the-approximate-fong-tsui-in--969c2f6b34c4
5. C. K. Fong and S. K. Tsui, *A note on positive operators*, Journal of Operator Theory 5 (1981), 73–76.
