# The exact universal third-moment majorant gap on finite cyclic groups

## Finding
For an integer \(N\ge5\), let \(\zeta_N=\exp(2\pi i/N)\), and define the normalized signed-majorant difference
\[
\Delta_N=\frac1N\sum_{j=0}^{N-1}\Bigl(
|1+\zeta_N^j-\zeta_N^{3j}|^3-
|1+\zeta_N^j+\zeta_N^{3j}|^3\Bigr).
\]
Then the **exact sharp universal margin** is
\[
\boxed{\inf_{N\ge5}\Delta_N=1-\frac2{\sqrt5}=0.105572809000084\ldots.}
\]
Equality holds if and only if \(N=10\). Consequently, every finite cyclic character of order at least five produces a third-moment Hardy–Littlewood majorant reversal with the best possible *order-independent* positive gap. The finite-cyclic reversal and a weaker uniform margin were known; the exact optimal margin and uniqueness are the present finding.

## Assumptions and scope
The sums use uniform probability measure over all \(N\)-th roots of unity and the fixed polynomial pair \(1+z\pm z^3\). Equivalently, \(N\) is the order of a character of a finite abelian group, and the ambient-group mean reduces to the displayed cyclic mean. No claims are made for other three-term supports, other exponents, or all characters simultaneously. In particular, this is a difference of **cubed norms**, not a difference of the norms themselves.

## Proof
**Exact tenth-order evaluation.** For \(t_j=2\pi j/10\), put
\[
X_\pm(j)=|1+e^{it_j}\pm e^{3it_j}|^2
=3+2\cos t_j\pm2(\cos2t_j+\cos3t_j).
\]
Write \(h_j=X_-(j)^{3/2}-X_+(j)^{3/2}\). By reflection \(h_{10-j}=h_j\), and direct exact trigonometric evaluation gives
\[
\begin{array}{c|cccccc}
j&0&1&2&3&4&5\\\hline
h_j&-26&0&11+3\sqrt5&0&7-5\sqrt5&0
\end{array}.
\]
For example, at \(j=2\) the two squared moduli are \((7+3\sqrt5)/2\) and \((3-\sqrt5)/2\). Their \(3/2\)-powers are \(9+4\sqrt5\) and \(\sqrt5-2\). At \(j=4\) they are \((7-3\sqrt5)/2\) and \((3+\sqrt5)/2\), whose \(3/2\)-powers are \(9-4\sqrt5\) and \(2+\sqrt5\). Thus
\[
\Delta_{10}=\frac{-26+2(11+3\sqrt5+7-5\sqrt5)}{10}
=1-\frac2{\sqrt5}<\frac{107}{1000}.
\]

**A cubic-order aliasing estimate.** Define \(q_\pm(t)=1+e^{it}\pm e^{3it}\), \(H_\pm(t)=|q_\pm(t)|^3\), and \(D(t)=H_-(t)-H_+(t)\). Let \(I=(2\pi)^{-1}\int_0^{2\pi}D(t)\,dt\). For the real function \(F(w)=|w|^3\) on \(\mathbb R^2\), the first two derivatives have norms at most \(3|w|^2\) and \(6|w|\), respectively, and its weak third derivative has norm at most \(12\). The third-derivative bound follows by differentiating the Hessian \(3|w|\mathrm{Id}+3ww^{\mathsf T}/|w|\) away from zero; the Hessian is globally Lipschitz, so the a.e. estimate extends in the weak sense. Since
\[
|q_\pm|\le3,\quad |q_\pm'|\le4,\quad
|q_\pm''|\le10,\quad |q_\pm^{(3)}|\le28,
\]
the third-order chain rule shows
\[
\|H_\pm^{(3)}\|_\infty\le
12\cdot4^3+3\cdot(6\cdot3)\cdot10\cdot4+(3\cdot3^2)\cdot28
=3684.
\]
Thus \(D\in W^{3,\infty}(\mathbb T)\) and \(\|D^{(3)}\|_\infty\le7368\). Three integrations by parts give
\[
|\widehat D(k)|\le\frac{7368}{|k|^3}\qquad(k\ne0).
\]
The absolutely convergent Fourier series permits averaging over roots of unity, yielding \(\Delta_N-I=\sum_{m\ne0}\widehat D(mN)\). Using \(2\zeta(3)<5/2\),
\[
\boxed{|\Delta_N-I|<\frac{18420}{N^3}.}
\tag{1}
\]
Here \(\zeta(3)\) is the Riemann zeta value, not a root of unity.

**Finite exact-arithmetic certificate.** The accompanying self-contained Python checker implements a uniformly bounded rational-Taylor enclosure, with integer-only computations. For every integer \(5\le N\le129\), \(N\ne10\), it proves \(\Delta_N>107/1000\). It also proves \(\Delta_{1000}>11554/100000\). These are finite rational inequalities, proved by the full stated finite loops and explicit analytic truncation-error bounds; they are not claims about arbitrary larger \(N\).

Specifically, the checker represents \(\pi\) using thirty terms of Machin's arctangent identity, with absolute error below \(700\cdot10^{-30}\). A degree-forty-four cosine Taylor polynomial, evaluated with integer truncation, has error below \(800\cdot10^{-30}\) for every necessary phase. The resulting exact squared-modulus enclosure has error below \(4800\cdot10^{-30}\). Since \(x\mapsto x^{3/2}\) is \(5\)-Lipschitz on the needed range, integer square roots give a gap-summand error below \(50000\cdot10^{-30}\). The checker tests the resulting strict lower bounds using only integer comparisons; it does not assume floating-point agreement or extrapolate from enumerated orders.

**The infinite tail.** By (1) at \(N=1000\),
\[
I>\frac{11554}{100000}-\frac{18420}{1000^3}.
\]
By (1) again, for every \(N\ge130\),
\[
\Delta_N>
\frac{11554}{100000}-\frac{18420}{1000^3}-\frac{18420}{130^3}
>\frac{107}{1000}>
1-\frac2{\sqrt5}.
\]
This is an exact rational inequality, separately verified in the checker. Together with the finite certificate and tenth-order evaluation, it proves the global sharp margin and uniqueness.

## Verification
Run `python3 artifacts/verify_majorant_gap.py` with a standard Python 3 interpreter. The checker establishes 124 finite-order strict inequalities (all \(5\le N\le129\) except ten), one high-order integral proxy at \(N=1000\), and the rational bridge. Its expected final line is `VERIFY_OK exact-integer trigonometric enclosure, all finite orders and continuous bridge`. The universal tail is proved analytically above, not by enumeration. The tenth-order algebraic identity is reproduced symbolically in the proof rather than inferred from a decimal approximation.

## Relationship to prior work
Pan–You–Wang–Zhou–Chen (first posted 2026-09-09) prove the continuous-circle three-term Hardy–Littlewood majorant conjecture for all frequency gaps; this does not compare the relevant complete finite root-of-unity grids or provide the sharp uniform grid margin. Krenedits studied the classical continuous majorant pair and quotes Mockenhaupt's earlier work on a discrete-uniform version. The closest posted finite-cyclic theorem already proves \(\Delta_N>0\) for all \(N\ge5\) and \(\Delta_N>0.0237\) uniformly, also noting a numerical finite-grid minimum at order ten. That theorem does **not** establish the global exact infimum, the unique minimizer over all orders, or the required stronger tail estimate. The present claim is exactly the sharp margin and uniqueness, not rediscovery of the positive sign or of the observed small-order candidate.

## Limitations
No theorem is asserted for arbitrary Fourier coefficients, other supports, or exponents other than three. Proof of the strict inequalities at the finitely many low orders depends on executing and inspecting the included exact-arithmetic checker with its stated error bounds; those finite verifications are not replaced by a closed-form case analysis. The full text of Mockenhaupt's 1996 habilitation thesis and of Krenedits' 2010 study was not available for statement-by-statement comparison. The full 23-page September 2026 revision of the continuous-conjecture preprint was inspected; its first version's omitted sections may merit separate priority review. Consequently, an independent literature-priority audit remains necessary. The proof and checker establish mathematical validity only within the precise stated assumptions.

## References
G. Pan, C. You, H. Wang, J. Zhou, Y. Chen, *Mockenhaupt's Three-Term Hardy-Littlewood Majorant Conjecture*, arXiv:2609.09740v1, first submitted 2026-09-09; primary MSC 42A05. https://arxiv.org/abs/2609.09740

S. Krenedits, *Three-term idempotent counterexamples in the Hardy–Littlewood majorant problem*, arXiv:1006.0409v1, first submitted 2010-06-02. https://arxiv.org/abs/1006.0409

*A finite-cyclic three-term majorant reversal exactly from order five onward*, published research record, 2026-10-04. https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-a-finite-cyclic-three-term-majorant-reversal-exactly-from-order--60a27acbb9f3/RESULT.md
