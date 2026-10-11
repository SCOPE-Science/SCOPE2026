# Exact Steinberg Fourier endpoint norms over finite general linear groups

## Finding
Let \(q\ge2\) be any prime power, let \(n\ge1\), and let \(G=\operatorname{GL}_n(\mathbf F_q)\). In \(\ell^2(G)\) with counting or normalized counting measure, let \(P_{n,q}\) be the orthogonal Fourier projection onto the *full* isotypic subspace associated with the complex Steinberg representation \(\mathrm{St}_{n,q}\) of degree \(d_{n,q}=q^{n(n-1)/2}\). Its endpoint operator norms agree. Their common value, normalized by the representation degree, is
\[
A_{n,q}:=\frac{\|P_{n,q}\|_{\ell^1\to\ell^1}}{d_{n,q}}
=\frac{\|P_{n,q}\|_{\ell^\infty\to\ell^\infty}}{d_{n,q}}
=\sum_{j=0}^{\lfloor n/2\rfloor}a_j(q),
\quad a_0(q)=1,\quad
 a_j(q)=a_{j-1}(q)\frac{q^{2j-2}-q}{q^{2j}-1}\ (j\ge1).
\]
Equivalently, for every fixed prime power \(q\), the formal power series is
\[
\sum_{n\ge0} A_{n,q}u^n
=\frac1{1-u}\prod_{r=1}^{\infty}
\frac{1-u^2q^{-(2r-1)}}{1-u^2q^{-2r}},
\]
where \(A_{0,q}=1\) is an auxiliary generating-series convention, not an assertion about a nonzero-rank group. Consequently, for \(m\ge1\),
\[
A_{2m,q}=A_{2m+1,q},\qquad
A_{2m+2,q}<A_{2m,q}.
\]
These *degree-normalized* norms, not the unnormalized operator norms, have the exact parity plateaus. They tend to the strictly positive Euler-product constant
\[
\lim_{n\to\infty}A_{n,q}=C_q
=\prod_{r=1}^{\infty}\frac{1-q^{-(2r-1)}}{1-q^{-2r}},
\qquad
\|P_{n,q}\|_{\ell^1\to\ell^1}
\sim C_q\,q^{n(n-1)/2}.
\]
If \(m=\lfloor n/2\rfloor\), the explicit error satisfies
\[
0<A_{n,q}-C_q\le \frac{|a_{m+1}(q)|}{1-q^{-2}}.
\]
For example, \(A_{2,q}=A_{3,q}=q/(q+1)\), and \(A_{4,2}=A_{5,2}=28/45\).

## Assumptions and scope
The field has order \(q=p^f\) for some prime \(p\) and positive integer \(f\). The Steinberg representation is the canonical irreducible constituent of the finite general linear group arising from its building; its dimension is \(d_{n,q}\). The projection is onto the *whole regular-representation isotypic block*, of dimension \(d_{n,q}^2\), not a single copy of the representation and not the identity projection onto all class functions. The endpoint norms are the sharp induced operator norms on all complex-valued functions on \(G\). No assertion is made about intermediate \(\ell^p\)-operator norms or joint limits in which \(q\) varies with \(n\).

## Proof
**1. Projection kernel and norm.** For an irreducible complex character \(\chi\) of any finite group \(G\), with \(d=\chi(1)\), character orthogonality gives the central idempotent projection as convolution with \(d\overline{\chi}/|G|\). Each matrix row and column of this convolution has the same absolute sum. Therefore
\[
\|P_\chi\|_{\ell^1\to\ell^1}
=\|P_\chi\|_{\ell^\infty\to\ell^\infty}
=d\,\frac1{|G|}\sum_{g\in G}|\chi(g)|.
\]
For \(\chi=\mathrm{St}_{n,q}\), its degree is \(d_{n,q}=q^{n(n-1)/2}\). The standard Steinberg character-value theorem says that the character vanishes on nonsemisimple elements; for a semisimple element \(s\), its absolute value is the \(p\)-part of \(|C_G(s)|\). These are equalities, not character bounds.

**2. Semisimple classes.** Write \(\mathcal I_q\) for all monic irreducible polynomials over \(\mathbf F_q\) with nonzero constant coefficient; let \(d_f\) be the degree of \(f\). A semisimple conjugacy class in \(\operatorname{GL}_n(\mathbf F_q)\) is uniquely specified by finitely supported multiplicities \(m_f\ge0\) satisfying \(\sum_f d_fm_f=n\). Its centralizer is
\[
C_G(s)\cong\prod_{f\in\mathcal I_q}\operatorname{GL}_{m_f}(\mathbf F_{q^{d_f}}).
\]
Since
\[
|\operatorname{GL}_m(\mathbf F_Q)|=Q^{m(m-1)/2}\prod_{i=1}^m(Q^i-1)
\]
for every prime power \(Q\), the class contribution to the mean absolute Steinberg character is
\[
\frac{|\mathrm{St}(s)|}{|C_G(s)|}
=\prod_{f\in\mathcal I_q}\frac1{\prod_{i=1}^{m_f}(q^{d_fi}-1)}.
\]
Here an empty product is \(1\). Summing over semisimple types, rather than over group elements, is exact because each conjugacy class has size \(|G|/|C_G(s)|\). Thus the normalized endpoint norm is the coefficient of \(u^n\) in
\[
Z_q(u)=\prod_{f\in\mathcal I_q}
\left(\sum_{m\ge0}\frac{u^{m d_f}}{\prod_{i=1}^m(q^{d_fi}-1)}\right).
\]

**3. Euler-product reduction.** For every real \(Q>1\), the elementary generating identity
\[
\sum_{m\ge0}\frac{t^m}{\prod_{i=1}^m(Q^i-1)}
=\prod_{r\ge1}(1+tQ^{-r})
\]
follows by expanding the product and summing all increasing \(m\)-tuples of indices: the coefficient is \(Q^{-m(m+1)/2}/\prod_{i=1}^m(1-Q^{-i})\). Applying this with \(Q=q^{d_f}\), then using the unique factorization of monic polynomials with nonzero constant term, gives
\[
Z_q(u)=\prod_{r\ge1}\prod_{f\in\mathcal I_q}
(1+(u q^{-r})^{d_f}),
\qquad
\prod_{f\in\mathcal I_q}(1-t^{d_f})^{-1}=\frac{1-t}{1-qt}.
\]
The identity \(1+x=(1-x^2)/(1-x)\) and the second displayed Euler product turn the inner product into
\[
\prod_{f\in\mathcal I_q}(1+v^{d_f})
=\frac{(1-v)(1-qv^2)}{(1-qv)(1-v^2)}.
\]
Taking \(v=uq^{-r}\) and telescoping the factors linear in \(u\) yields
\[
Z_q(u)=\frac1{1-u}
\prod_{r\ge1}\frac{1-u^2 q^{-(2r-1)}}{1-u^2q^{-2r}}.
\]
All these identities hold as formal power series in \(u\): each fixed coefficient also follows by truncation of the finitely many relevant polynomial degrees, and the infinite products over \(r\) converge coefficientwise because \(q^{-r}\) is summable.

**4. Coefficients, plateaus and limit.** The elementary \(q\)-binomial identity, with base \(t=q^{-2}\), is
\[
\frac{(ax;t)_\infty}{(x;t)_\infty}
=\sum_{j\ge0}\frac{(a;t)_j}{(t;t)_j}x^j,
\qquad
(a;t)_j=\prod_{i=0}^{j-1}(1-at^i).
\]
Use \(a=q\) and \(x=u^2/q^2\). The coefficient \(a_j(q)\) has consecutive ratio
\[
\frac{a_j(q)}{a_{j-1}(q)}
=\frac{q^{2j-2}-q}{q^{2j}-1}.
\]
Because multiplication by \((1-u)^{-1}\) takes even-power coefficients into cumulative sums, \(A_{n,q}=\sum_{j\le\lfloor n/2\rfloor}a_j(q)\). The initial coefficient \(a_1(q)=-1/(q+1)\), and every later ratio lies strictly between \(0\) and \(q^{-2}\). Hence \(a_j(q)<0\) for all \(j\ge1\), giving exact two-rank plateaus, strict drops at each subsequent even rank, and the quoted geometric tail estimate. Evaluating the absolutely convergent \(q\)-binomial series at \(u=1\) gives the positive Euler product \(C_q\), completing the proof.

## Verification
Run the self-contained Python 3 program `python3 verify.py` from the directory containing this document. It uses only the Python standard library. It compares the closed recurrence against the separate rational-canonical-class generating function for \(q\in\{2,3,4,5\}\) and \(0\le n\le8\) (**36 exact coefficient comparisons**). It also enumerates *every* invertible matrix in \(\operatorname{GL}_2(\mathbf F_2)\), \(\operatorname{GL}_2(\mathbf F_3)\), \(\operatorname{GL}_3(\mathbf F_2)\), and \(\operatorname{GL}_3(\mathbf F_3)\), recovering Steinberg traces from fixed flags rather than from the character-value theorem. Their group sizes are respectively \(6,48,168,11232\); their exact mean absolute traces agree with the formula: \(2/3,3/4,2/3,3/4\). The finite tests support, but do not replace, the symbolic all-rank proof.

## Relationship to prior work
Scarabotti and Tolli [1] develop the finite homogeneous-space harmonic-analysis and isotypic projector framework (their original first public version has primary MSC 43A95). Srinivasan [2] states the standard Steinberg character-value rule, while Fulman [3] gives rational-canonical cycle-index machinery and semisimple **probabilities**. Their statements provide crucial ingredients, but the absolute Steinberg mean includes the nonconstant centralizer \(p\)-part weight, which is absent in the ordinary semisimple probability. Møller [4] studies signed equivariant Euler characteristics of the same type of subspace poset and separately counts semisimple conjugacy classes; taking an absolute value inside the group average does not follow from the signed average. Fulman–Guralnick [5] enumerate **regular** semisimple classes; the present sum includes all semisimple classes with nonuniform weights. The exact endpoint norm, its even/odd normalized plateaus, and its Euler limit are not stated in the inspected relevant portions of these works.

## Limitations
The result concerns only the specific Steinberg isotypic Fourier projector and the endpoint spaces \(\ell^1\) and \(\ell^\infty\). No bound beyond the explicit geometric-tail estimate is claimed for varying \(q\) or other representations. Literature searches cannot rule out an equivalent identity in an older source expressed in terms of weighted semisimple classes, building Euler characteristics, or \(q\)-series rather than projection norms.

## References
[1] F. Scarabotti and F. Tolli, *Harmonic analysis on a finite homogeneous space*, arXiv:math/0701533v1 (first posted 2007-01-19), https://arxiv.org/abs/math/0701533.

[2] B. Srinivasan, *On the Steinberg Character of a Finite Simple Group of Lie Type*, J. Austral. Math. Soc. 12 (1971), 1–14, https://doi.org/10.1017/S1446788700008247.

[3] J. Fulman, *Finite Affine Groups: Cycle Indices, Hall-Littlewood Polynomials, and Probabilistic Algorithms*, arXiv:math/0009182 (first posted 2000-09-19; inspected v2), https://arxiv.org/abs/math/0009182.

[4] J. M. Møller, *Equivariant Euler characteristics of subspace posets*, arXiv:1701.03411 (first posted 2017-01-12; inspected v2), https://arxiv.org/abs/1701.03411.

[5] J. Fulman and R. Guralnick, *The number of regular semisimple conjugacy classes in the finite classical groups*, arXiv:1209.3345, https://arxiv.org/abs/1209.3345.
