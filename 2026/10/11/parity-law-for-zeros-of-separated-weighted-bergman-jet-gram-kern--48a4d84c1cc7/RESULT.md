# Parity law for zeros of separated weighted Bergman jet Gram kernels

## Finding

Let \(\mathbb H=\{z\in\mathbb C:\operatorname{Im}z>0\}\). For every real \(\alpha>-1\), integers \(0\le p<q\) with \(d=q-p\ge2\), and coefficient \(c\in\mathbb C\setminus\{0\}\), consider the weighted Bergman space
\[
A^2_\alpha(\mathbb H)=\left\{f\text{ holomorphic on }\mathbb H:\int_{\mathbb H}|f(x+iy)|^2y^\alpha\,dx\,dy<\infty\right\}
\]
and its differential evaluation functional
\[
\Lambda_z f=\frac{f^{(p)}(z)}{p!}+c\frac{f^{(q)}(z)}{q!}.
\]
Let \(B_{\alpha;p,q,c}(z,w)\) be the Hermitian Gram kernel of the Riesz representatives of these functionals, holomorphic in \(z\) and antiholomorphic in \(w\). Define the scalar variable \(t=(z-\overline w)^{-1}\); as \((z,w)\) runs over \(\mathbb H^2\), \(t\) runs over the entire open lower half-plane \(\mathbb C_-\).

**Theorem.** The number \(N\) of distinct scalar values \(t\in\mathbb C_-\) at which the Gram kernel vanishes is
\[
\boxed{
N=\begin{cases}
 d,& d\text{ even},\\
 d+1,& d\text{ odd and }\operatorname{Im}c>0,\\
 d-1,& d\text{ odd and }\operatorname{Im}c\le0.
\end{cases}}
\]
Every such scalar zero is simple. In particular, **every separated two-jet kernel in this entire parameter range has off-diagonal zeros**, so none is zero-free on \(\mathbb H\times\mathbb H\). When \(d\) is odd and \(\operatorname{Im}c=0\), there are exactly two additional distinct real roots of the reduced zero polynomial, neither accessible from interior pairs. These counts are independent of the weight \(\alpha\), starting order \(p\), and modulus \(|c|\).

An explicit root formula is available. Put \(h=\alpha+2\), and let
\[
A=\frac{p!\,\Gamma(h+p+q)}{q!\,\Gamma(h+2p)},\qquad
B=\left(\frac{p!}{q!}\right)^2\frac{\Gamma(h+2q)}{\Gamma(h+2p)}.
\]
These real numbers satisfy \(B>A^2>0\). Define the reduced polynomial
\[
Q(t)=1+A\bigl((-1)^d c+\overline c\bigr)t^d+(-1)^d B|c|^2t^{2d}.
\]
The complete scalar zero set is the collection of \(d\)-th roots in \(\mathbb C_-\) of the two solutions of the quadratic equation obtained by setting \(u=t^d\). For even \(d\), these quadratic roots are
\[
u_\pm=\frac{-A\operatorname{Re}c\ \pm i\sqrt{B|c|^2-A^2(\operatorname{Re}c)^2}}{B|c|^2};
\]
for odd \(d\), they are
\[
u_\pm=\frac{-iA\operatorname{Im}c\ \pm\sqrt{B|c|^2-A^2(\operatorname{Im}c)^2}}{B|c|^2}.
\]
Both square-root radicands are strictly positive.

## Assumptions and scope

The weighted norm uses **unnormalized** Lebesgue area \(dx\,dy\), with the precise weight \((\operatorname{Im}z)^\alpha\). For \(\alpha>-1\), all local derivative evaluations are bounded on the weighted Bergman space. Our Gram-kernel convention is
\[
B_{\alpha;p,q,c}(z,w)=\bigl(\Lambda_z\overline{\Lambda_w}\bigr)K_\alpha(z,w),
\]
where the bar means conjugating coefficients and differentiating with respect to \(\overline w\). No assumption on the sign or argument of \(c\) is imposed. The separation restriction \(d\ge2\) excludes the adjacent-order case. A scalar zero means a zero of the kernel under the variable \(t=(z-\overline w)^{-1}\), **not** the count of zeros on an arbitrarily fixed \(w\)-slice.

## Proof

**1. Weighted Bergman normalization and mixed derivatives.** The reproducing kernel for the stated norm is
\[
K_\alpha(z,w)=\frac{2^\alpha(\alpha+1)}{\pi}\bigl[-i(z-\overline w)\bigr]^{-h},\qquad h=\alpha+2,
\]
with the principal holomorphic power on the right half-plane. It follows, for example, by the Fourier–Laplace representation with density \(t^{h-1}\):
\[
K_\alpha(z,w)=\frac{2^\alpha}{\pi\Gamma(\alpha+1)}
\int_0^\infty s^{\alpha+1}e^{is(z-\overline w)}\,ds.
\]
Indeed, if \(f(z)=\int_0^\infty e^{isz}g(s)\,ds\), Plancherel followed by the gamma integral yields the norm
\[
\|f\|_\alpha^2=\frac{\pi\Gamma(\alpha+1)}{2^\alpha}
\int_0^\infty |g(s)|^2s^{-\alpha-1}\,ds,
\]
which gives the displayed reproducing integral by Riesz duality. The integral and all its finite mixed derivatives converge absolutely for \(z,w\in\mathbb H\). Differentiating in \(z\) and \(\overline w\) gives, for all nonnegative integers \(r,s\),
\[
\frac{\partial_z^r\partial_{\overline w}^sK_\alpha(z,w)}{K_\alpha(z,w)}
=(-1)^r(h)_{r+s}t^{r+s},\qquad (h)_m=\frac{\Gamma(h+m)}{\Gamma(h)}.
\]
The signs follow from \(\partial_z(z-\overline w)=1\) and \(\partial_{\overline w}(z-\overline w)=-1\).

**2. The quadratic reduction.** Expand the Gram kernel into the four pairs of derivatives of orders \((p,p),(p,q),(q,p),(q,q)\). Divide by the nowhere-vanishing factor
\[
\frac{(-1)^p(h)_{2p}}{(p!)^2}\,t^{2p}K_\alpha(z,w).
\]
Since \(t\ne0\) for interior pairs, division is legitimate and leaves **exactly** \(Q(t)\) displayed above. The two reduced coefficients are precisely \(A\) and \(B\), with no extra normalization or omitted mixed term.

**3. A strict inequality for every weight and order.** Since \(q>p\), strict log-convexity of the gamma function on positive reals yields
\[
\frac{B}{A^2}=
\frac{\Gamma(h+2p)\Gamma(h+2q)}{\Gamma(h+p+q)^2}>1.
\]
This is the midpoint strict-convexity inequality, with \(h+2p>0\) and \(h+2q>0\). Thus \(B>A^2\), and all the radicands in the stated formulas are strictly positive for \(c\ne0\). Consequently the two roots \(u_\pm\) are distinct and nonzero; hence the \(2d\) complex roots of \(Q\), obtained by taking their \(d\)-th roots, are all distinct and simple.

**4. Count by parity and phase.** If \(d\) is even, the quadratic in \(u=t^d\) is
\[
1+2A(\operatorname{Re}c)u+B|c|^2u^2.
\]
Its discriminant is strictly negative by \(B>A^2\), so its roots are a nonreal conjugate pair. Every nonreal number has exactly \(d/2\) distinct \(d\)-th roots in \(\mathbb C_-\) for even \(d\); hence \(N=d\).

If \(d\) is odd, the quadratic is
\[
1-2iA(\operatorname{Im}c)u-B|c|^2u^2.
\]
Its two roots have equal imaginary part \(-A\operatorname{Im}c/(B|c|^2)\) and opposite real parts. For odd \(d\), a number strictly below the real axis has \((d+1)/2\) distinct \(d\)-th roots below the axis, and a number strictly above has \((d-1)/2\); this follows by counting the equally spaced root arguments \((\arg u+2\pi j)/d\), for \(0\le j<d\). If \(\operatorname{Im}c>0\), both quadratic roots are below the axis, giving \(N=d+1\). If \(\operatorname{Im}c<0\), both are above, giving \(N=d-1\). If \(\operatorname{Im}c=0\), the quadratic roots are two distinct nonzero real numbers of opposite signs. Each has one real \(d\)-th root and \((d-1)/2\) lower roots, giving \(N=d-1\) and precisely two extra real boundary roots of \(Q\).

**5. Exhaustion and realizability.** The map \(z,w\mapsto t=(z-\overline w)^{-1}\) has range precisely \(\mathbb C_-\). For any \(t\in\mathbb C_-\), write \(t^{-1}=a+ib\) with \(b>0\), and choose \(z=a/2+ib/2\), \(w=-a/2+ib/2\). Then \(z,w\in\mathbb H\) and \(t=(z-\overline w)^{-1}\). Because the prefactor removed in Step 2 never vanishes, the counted roots are all and only the attainable kernel-zero scalar values. The smallest allowed separation is \(d=2\), and the table gives \(N\ge2\) in every case, proving nonvanishing fails throughout the stated class.

## Verification

The standalone companion `check_twojet.py` executes \(560\) numerical root-count tests across four weights, four starting orders, seven gaps and five complex coefficients, including the real-coefficient boundary cases. It also compares the Fourier–Laplace integral of the mixed-derivative Gram kernel with the claimed closed expression at four independent high-precision sample configurations. The observed maximum relative discrepancy in these four comparisons is below \(10^{-25}\). Execute `python -m pip install -r requirements.txt`, followed by `python check_twojet.py`. The dependency is pinned to the version used for the checks. These finite checks test normalization and signs; the infinite-parameter assertion is established in the proof, not inferred from tests.

## Relationship to prior work

Gehlawat, Jain and Sarkar [1] introduced the canonical Hermitian Gram kernel for differential-sequence evaluations. Their Theorem 4.1, particularly formula (4.6), gives a general series expression on the **unweighted** upper half-plane; their Proposition 4.5 and Theorem 4.11 analyze single-supported sequences and a factorially supported infinite sequence. Those results are compatible with the present construction but do not state or imply by an explicit zero-location theorem the uniform parity-and-phase count for every pair of nonadjacent derivative orders. The existing general series formula supplies an ingredient, not the strict gamma comparison and exhaustive angular counting needed here.

Bao, Guan and Sun [2] study Bergman extremal kernels associated with differential functionals and higher-order conditions; their theorems concern extremal properties, regularity and plurisubharmonicity rather than the present off-diagonal count. Deng, Huang and Qian [3] and Bonyo [4] provide weighted half-plane Bergman-kernel representations and normalizations; they do not establish this two-jet zero geometry. Thus the present statement combines a natural two-term differential-functional model with a **complete count** across all separated orders and all power weights, rather than merely reproducing a known kernel formula.

## Limitations

The theorem concerns scalar zeros in \(\mathbb C_-\), not the number of zeros of \(z\mapsto B_{\alpha;p,q,c}(z,w)\) for a fixed point \(w\); a fixed slice need not reach every scalar zero. It does not cover the adjacent case \(q-p=1\), a vanishing coefficient \(c=0\), weights outside \(\alpha>-1\), more than two derivative orders, or other domains. The real boundary roots in the odd-gap real-coefficient case are **not** kernel zeros at interior pairs. This proof is self-contained once the standard weighted half-plane Bergman representation and strict gamma log-convexity are known. As with any literature search, a previously unindexed equivalent theorem may exist.

## References

1. S. Gehlawat, A. Jain and A. D. Sarkar, *A Canonical Positive Definite Kernel Associated with the \(\xi\)-Bergman Kernel*, arXiv:2608.13193v1 (first available 2026-08-13), especially Theorem 4.1, formula (4.6), Proposition 4.5 and Theorem 4.11. https://arxiv.org/abs/2608.13193
2. S. Bao, Q. Guan and X. Sun, *On the \(p\)-Bergman Kernel with Respect to a Functional \(\xi\)*, arXiv:2510.13144 (first available 2025-10-15), especially Sections 1, 2 and 5. https://arxiv.org/abs/2510.13144
3. G.-T. Deng, Y. Huang and T. Qian, *Reproducing Kernels of Some Weighted Bergman Spaces*, arXiv:2009.02989 (2020), especially the weighted upper-half-plane formula in Section 1. https://arxiv.org/abs/2009.02989
4. J. O. Bonyo, *Reproducing Kernels for Hardy and Bergman Spaces of the Upper Half Plane*, Communications in Advanced Mathematical Sciences 3 (2020), 13–23, especially Section 2.1. DOI: 10.33434/cams.631112.
