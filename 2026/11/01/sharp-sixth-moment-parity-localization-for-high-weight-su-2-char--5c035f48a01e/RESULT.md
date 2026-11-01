# Sharp sixth-moment parity localization for high-weight \(SU(2)\) character packets

## Finding
Let \(S\subset\mathbb Z_{\ge0}\) be a nonempty finite set with \(\min S=0\), and let \(e\) and \(o\) be its numbers of even and odd offsets. For each integer \(m\ge\max S\), use the ordinary, unnormalized irreducible trace characters \(\chi_j\) of \(SU(2)\), orthonormal for probability Haar measure, and put
\[
K_m^{(6)}(S)=\max_{\sum_{s\in S}|c_s|^2=1}
\int_{SU(2)}\left|\sum_{s\in S}c_s\chi_{m+s}(g)\right|^6\,dg.
\]
With \(A(c)=\sum_{s\text{ even}}c_s\), \(B(c)=\sum_{s\text{ odd}}c_s\), uniformly on the unit coefficient sphere,
\[
\int_{SU(2)}\left|\sum_{s\in S}c_s\chi_{m+s}\right|^6dg
=\frac{m^3}{4}\bigl(|A(c)+B(c)|^6+|A(c)-B(c)|^6\bigr)+O_S((m+1)^2).
\]
Consequently \(K_m^{(6)}(S)=m^3 C_6(e,o)+O_S((m+1)^2)\), where the exact sharp coefficient \(C_6(e,o)\) depends only on the parity counts, not on within-parity offset spacings.

Set \(a=\max(e,o)\) and \(b=\min(e,o)\). If \(b=0\), or more generally \(a\ge5b\), then
\[
C_6(e,o)=\frac{a^3}{2}.
\]
When \(0<b\le a<5b\), put \(r=a/b\), and let \(p_*\in(0,1)\) be the **unique** root of
\[
(5r-1)(1-p)^2+10r(r-1)p(1-p)+r^2(r-5)p^2=0.
\]
Then, writing \(q_*=a p_*+b(1-p_*)\),
\[
C_6(e,o)=\frac12\bigl(q_*^3+12ab\,q_*p_*(1-p_*)\bigr).
\]
The maximizing coefficient profiles for this limiting functional are completely classified: if \(a\ge5b\), all coefficients of the minority parity vanish and the \(a\) majority-parity coefficients are identical with modulus \(a^{-1/2}\). If \(0<b\le a<5b\), the majority coefficients are identical with modulus \(\sqrt{p_*/a}\), the minority coefficients are identical with modulus \(\sqrt{(1-p_*)/b}\), and their two common phases agree or differ by \(\pi\), up to a global phase. Every sequence of finite-\(m\) optimizers approaches the indicated compact set of limiting profiles in coefficient Euclidean distance as \(m\to\infty\).

The **sharp sixth-moment parity transition is \(5:1\)**: a minority of size \(b>0\) improves the leading constant exactly when \(a<5b\). In particular, \((e,o)=(4,1)\) mixes strictly, whereas \((5,1)\) and all more unbalanced pairs use only the majority class at leading order.

## Assumptions and scope
All \(L^p\) integrals are with respect to probability Haar measure on the classical compact Lie group \(SU(2)\). The character \(\chi_j\) is the ordinary trace of the \((j+1)\)-dimensional irreducible representation, not the dimension-normalized character. Thus \(\|\chi_j\|_2=1\). The support \(S\), including its diameter, is fixed while \(m\to\infty\); no uniformity is claimed for growing supports. Coefficients are arbitrary complex numbers, normalized by \(\sum|c_s|^2=1\). The result concerns central Fourier synthesis and not full matrix-coefficient spaces. A zero parity count is permitted.

## Proof
**1. Exact single-character sixth moment.** Weyl integration for a central function gives
\[
\int_{SU(2)}F(g)dg=\frac2\pi\int_0^\pi F(\theta)\sin^2\theta\,d\theta,
\qquad \chi_j(\theta)=\frac{\sin((j+1)\theta)}{\sin\theta}.
\]
By the Clebsch–Gordan identity \(\chi_j\chi_k=\sum_{\ell=0}^{\min(j,k)}\chi_{j+k-2\ell}\), the coefficient of \(\chi_{m+2u}\) in \(\chi_m^3\) is \(m-u+1\) when \(0\le u\le m\), and \(m+2u+1\) when \(-\lfloor m/2\rfloor\le u<0\); all others vanish. Character orthogonality and sums of consecutive squares give
\[
\int\chi_m^6\,dg=\sum_{u=0}^m(m-u+1)^2+\sum_{u=-\lfloor m/2\rfloor}^{-1}(m+2u+1)^2
=\frac{(m+1)(m^2+2m+2)}2
=\frac{m^3}{2}+O((m+1)^2).
\]
This exact identity also fixes the normalization of the endpoint contributions.

**2. Uniform two-endpoint reduction.** For \(0\le\theta\le\pi/2\) and any fixed \(s\ge0\),
\[
|\chi_{m+s}(\theta)-\chi_m(\theta)|
\le\frac{s\theta}{\sin\theta}\le\frac\pi2s.
\]
Since \(\sum_{s\in S}|c_s|\le\sqrt{|S|}\), on this half-interval the character sum differs from \((A+B)\chi_m\) by a uniformly bounded quantity depending only on \(S\). Under reflection \(\theta\mapsto\pi-\theta\), the identity \(\chi_{m+s}(\pi-\theta)=(-1)^{m+s}\chi_{m+s}(\theta)\) shows that the other half differs, up to a unimodular sign, from \((A-B)\chi_m\) by the same bounded amount.

The elementary bound \(|\chi_m(\theta)|\le\min(m+1,1/\sin\theta)\), together with the Weyl weight \(\sin^2\theta\), yields \(\int_0^{\pi/2}|\chi_m|^5\sin^2\theta d\theta=O((m+1)^2)\); every lower absolute moment on that half-interval has the same upper bound. Expanding the sixth powers using \(\big||z+w|^6-|z|^6\big|\le6|w|(|z|+|w|)^5\) therefore gives an error \(O_S((m+1)^2)\), uniformly over coefficient vectors. The exact single-character sixth moment has equal contributions on both half-intervals, so step 1 gives
\[
\|\textstyle\sum c_s\chi_{m+s}\|_6^6
=\frac{(m+1)(m^2+2m+2)}4\bigl(|A+B|^6+|A-B|^6\bigr)+O_S((m+1)^2).
\]
Replacing the prefactor by \(m^3/4\) proves the claimed uniform expansion.

**3. Exact optimization of the leading functional.** Write \(X=|A|^2\), \(Y=|B|^2\). The algebraic identity
\[
\frac{|A+B|^6+|A-B|^6}{4}
=\frac12\bigl((X+Y)^3+12(X+Y)(\operatorname{Re}(A\overline B))^2\bigr)
\]
shows that when both parity classes are nonzero, relative phases must agree or differ by \(\pi\). Cauchy–Schwarz shows that the class sums have \(X\le e\sum_{s\text{ even}}|c_s|^2\) and \(Y\le o\sum_{s\text{ odd}}|c_s|^2\), with equality precisely when coefficients are identical within each nonempty class. Since the displayed functional increases strictly with nonnegative \(X\) and \(Y\), every maximizer saturates these inequalities in each active class.

Assume the majority class has \(a\) offsets and let \(p\) be its coefficient energy, leaving \(1-p\) for the minority of size \(b\). The reduced objective is
\[
\Phi_{a,b}(p)=\tfrac12\bigl(q(p)^3+12ab\,q(p)p(1-p)\bigr),\qquad q(p)=ap+b(1-p).
\]
For \(b=0\), it is maximized uniquely by \(p=1\). If \(b>0\), write \(r=a/b\ge1\). Direct differentiation gives the Bernstein-form identity
\[
\Phi_{a,b}'(p)=\frac{3b^3}{2}
\left[(5r-1)(1-p)^2+10r(r-1)p(1-p)+r^2(r-5)p^2\right].
\]
If \(r\ge5\), every term is nonnegative and the derivative is strictly positive on \([0,1)\), so the unique maximizer is \(p=1\). If \(1\le r<5\), substitute \(t=p/(1-p)\): after division by \((1-p)^2\), the derivative's sign is that of
\[
(5r-1)+10r(r-1)t-r^2(5-r)t^2.
\]
Its constant is positive and its quadratic coefficient negative, so it has exactly one positive zero; the derivative changes from positive to negative there. This is the unique global maximizer, and it is interior. Equality in the prior phase and Cauchy–Schwarz inequalities proves the complete classification, including the threshold case \(r=5\).

**4. Uniformity and optimizer convergence.** The uniform \(O_S(m^2)\) bound on the unit coefficient sphere passes to its supremum, giving the sharp asymptotic of \(K_m^{(6)}(S)\). This sphere is compact, so finite-\(m\) maximizers exist. Uniform convergence of the normalized moment functionals to the continuous limiting functional implies that any sequence of maximizers has distance tending to zero from its full equality set: otherwise a compact convergent subsequence would limit to a nonmaximizer while retaining the optimal value. This concludes the proof for every fixed finite support.

## Verification
The accompanying standalone `verify.py` independently computes Haar sixth moments from triple Clebsch–Gordan products, checks the exact single-character polynomial for 29 weights, tests seven complex coefficient families against the predicted two-endpoint asymptotics, and compares the algebraic maximizing profile with 101 rational grid points for each of 144 positive parity-count pairs. The deterministic checker passes 14,766 assertions. The infinite-weight theorem is proved analytically above; finite tests are not used to establish convergence for arbitrary offsets.

## Relationship to prior work
The classical Clebsch–Gordan rule, Weyl integration and Schur orthogonality are inputs, not discoveries. Youn (2024) analyzes Khintchine inequalities for central Fourier series on non-Kac compact quantum groups, and discusses the contrasting failures of dimension-independent bounds for connected semisimple classical groups; it does not calculate a sharp fixed-packet classical sixth-moment constant. Dooley and Gupta (1996) analyze the fourth norm of noncentral matrix-coefficient polynomials, not sharp sixth powers of high-weight central packets. An earlier published parity-localization result on \(SU(2)\) determines **fourth** moments and a different \(3:1\) threshold, whereas here the sixth moment has a genuinely different \(5:1\) boundary and a new cubic maximization. Known sixth-moment calculations for individual or two adjacent characters cover strict special cases but do not imply the arbitrary finite-support threshold or classification. The exact two-adjacent-character sixth norm is expressly not claimed as new.

## Limitations
The theorem determines the leading sixth-power sharp constant, with a uniform fixed-support quadratic-order remainder, but not the exact maximizing coefficients at every finite weight or a sharp second-order coefficient for arbitrary support. Offsets cannot grow with \(m\) under the stated error bound. No claim is made for noncentral Peter–Weyl matrix coefficients, other compact groups, or moments other than six. Mathematical priority remains best-knowledge pending independent literature review, particularly for older representation-theoretic estimates.

## References
- S.-G. Youn, *A Khintchine inequality for central Fourier series on non-Kac compact quantum groups*, arXiv:2408.13519, first public version 2024-08-24, https://arxiv.org/abs/2408.13519.
- A. H. Dooley and S. K. Gupta, *On norms of trigonometric polynomials on \(SU(2)\)*, Pacific Journal of Mathematics 175 (1996), 491–509, https://msp.org/pjm/1996/175-2/pjm-v175-n2-p09-p.pdf.
- *High-weight parity localization of central fourth moments on \(SU(2)\)*, published mathematical research note, 2026-10-11, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-high-weight-parity-localization-of-central-fourth-moments-on-su--00a2a7bedf04.
