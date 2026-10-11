# Sharp fourth-moment norm of the four-term arithmetic progression
## Finding
For
\[
F(t)=a+b e^{2\pi i t}+c e^{4\pi i t}+d e^{6\pi i t},\qquad t\in\mathbb T,
\]
with normalized Haar measure on \(\mathbb T\), the sharp fourth-moment inequality is
\[
\|F\|_4\le K_4(\{0,1,2,3\})\bigl(|a|^2+|b|^2+|c|^2+|d|^2\bigr)^{1/2},
\]
where
\[
K_4(\{0,1,2,3\})^4=X_*,
\qquad
208X_*^3-1224X_*^2+2268X_*-1323=0,
\]
and \(X_*\) is the largest real root. Numerically,
\[
X_*=2.808840165474396887068345490608\ldots,
\qquad
K_4(\{0,1,2,3\})=1.2945885354364894097\ldots.
\]

Let \(\tau>0\) be the unique positive root of
\[
\tau^3+3\tau^2-3\tau-3=0,
\qquad
\tau=1.2618022452599717001\ldots.
\]
Every nonzero extremizer is exactly
\[
(a,b,c,d)=\lambda(1,\tau\eta,\tau\eta^2,\eta^3),
\qquad \lambda\ne0,\quad |\eta|=1,
\]
and every such coefficient vector attains equality.

## Assumptions and scope
The group is the continuous circle \(\mathbb T=\mathbb R/\mathbb Z\) with normalized Haar measure, and the spectrum is exactly the four consecutive characters \(\{0,1,2,3\}\). Translation of the spectrum does not change the ratio, and multiplying all frequencies by a nonzero integer gives the same circle distribution, so the same constant applies to any nondegenerate four-term arithmetic progression in \(\mathbb Z\).

The theorem concerns the unrestricted complex coefficient problem. It does not assert the corresponding value on a finite cyclic sampling grid, where aliasing can change fourth moments, and it does not address spectra that are not affine copies of a four-term arithmetic progression.

## Proof
Write \(x=|a|\), \(y=|b|\), \(z=|c|\), and \(w=|d|\). Parseval applied to \(F^2\) gives
\[
\|F\|_4^4
=|a^2|^2+|2ab|^2+|b^2+2ac|^2+|2ad+2bc|^2+|c^2+2bd|^2+|2cd|^2+|d^2|^2.
\]
For fixed magnitudes, the three phase-sensitive cross terms have positive coefficients and phases
\[
\arg(ac\overline{b}^2),\qquad
\arg(ad\overline{b}\overline{c}),\qquad
\arg(bd\overline{c}^2).
\]
The middle phase is the sum of the other two. Hence the maximum over phases is attained precisely, when all four magnitudes are positive, when the coefficient phases form an arithmetic progression. After removing a common phase and a character modulation, it is therefore enough to maximize over \(x,y,z,w\ge0\). Put
\[
S=x^2+y^2+z^2+w^2,
\]
\[
Q=(xy+yz+zw)^2+(xz+yw)^2+(xw)^2.
\]
Then
\[
\|F\|_4^4=S^2+2Q,
\]
so the problem is to maximize \(Q/S^2\).

On the boundary, if an outer variable vanishes, say \(w=0\), then with \(S=1\), \(r=y^2\), and \(x^2+z^2=1-r\),
\[
Q=y^2(x+z)^2+x^2z^2
\le 2r(1-r)+\frac{(1-r)^2}{4}
\le\frac47.
\]
If an inner variable vanishes, \(Q\) is the sum of the three pairwise products of three nonnegative squared magnitudes and is at most \(1/3\). Thus every boundary point satisfies
\[
\frac{\|F\|_4^4}{S^2}\le1+2\cdot\frac47=\frac{15}{7}.
\]

It remains to classify interior critical points. By homogeneity set \(x=1\). Let \(Q_x,Q_y,Q_z,Q_w\) denote the partial derivatives. The Lagrange equations are
\[
Q_y-yQ_x=Q_z-zQ_x=Q_w-wQ_x=0.
\]
Exact lexicographic elimination in \(w,z,y\) gives, apart from the boundary factor \(y\),
\[
(y^3-3y^2-3y+3)(y^3+3y^2-3y-3)
\]
\[
\cdot(y^4-2y^3+5y^2-4y-3)(y^4+2y^3+5y^2+4y-3)
\]
\[
\cdot(243y^8-558y^6+372y^4-62y^2+3)=0.
\]
The first cubic branch forces \(z=-y\) and \(w=-1\). The second forces \(z=y\), \(w=1\), and its unique positive root is \(y=\tau\). The first quartic branch forces \(3w=-(y^3+5y+3)\), while the second forces \(3z=-(y^3+2y)\); neither can lie in the positive orthant. For the octic branch, exact Sturm isolation gives four positive roots, and exact sign isolation of the back-substitution polynomials shows that at each root either \(z<0\) or \(w<0\). These computations are reproduced exactly by `artifacts/verify.py`.

Thus the only positive critical ray is \((1,\tau,\tau,1)\). At that point
\[
\frac{\|F\|_4^4}{S^2}
=
\frac{3\tau^4+4\tau^3+12\tau^2+3}{2(1+\tau^2)^2}.
\]
Eliminating \(\tau\) with \(\tau^3+3\tau^2-3\tau-3=0\) gives
\[
208X^3-1224X^2+2268X-1323=0.
\]
The attained value is the largest root \(X_*\), and \(X_*>2.8088>15/7\), so it strictly exceeds every boundary value. This proves global sharpness.

Finally, equality in the phase reduction requires the two second phase differences to vanish. Hence the phases are affine in the frequency index, giving exactly \(\lambda(1,\tau\eta,\tau\eta^2,\eta^3)\).

## Verification
Run `python3 artifacts/verify.py` with SymPy available. The script reconstructs the fourth-moment identity, recomputes the Gröbner elimination, verifies the exact back-substitution relations for all five interior branches, uses rational Sturm isolation to rule out every positive octic branch, checks the resultant polynomial for \(X_*\), and isolates the relevant roots with rational endpoints. Decimal values are reported only after the exact checks.

The exact algebraic certificate, not floating-point optimization, proves the global statement. The only analytic estimate outside the symbolic elimination is the displayed elementary boundary bound.

## Relationship to prior work
Schmidt's 2013 paper studies fourth norms of polynomials with unimodular coefficients and records the autocorrelation identity
\[
\|f\|_4^4=c_0^2+2\sum_{u\ge1}|c_u|^2.
\]
That work is asymptotic and keeps all coefficient magnitudes equal to one. It supplies a direct literature motivation for asking for exact finite-support fourth-moment geometry, but it does not determine the unrestricted four-coefficient \(L^4/L^2\) operator norm or its equality class.

A separate finite-cyclic four-point calculation with equal-magnitude coefficients determines a phase-only minimum and explicitly excludes unequal coefficient magnitudes from its scope. Its statement therefore does not imply the present unrestricted maximum problem. Michels' general \(\Lambda(p)\) framework defines the constants \(K_p(\Lambda)\) for character sets but addresses infinite-set and operator-ideal questions rather than this finite exact value.

## Limitations
No claim is made about finite cyclic grids, where wraparound relations can alter the moment identity, or about other four-point support geometries. The proof uses exact symbolic elimination for the interior critical-point classification; `artifacts/verify.py` is therefore part of the reproducibility package. A residual literature risk remains that an older small-degree trigonometric-polynomial calculation may encode the same constant under different terminology.

## References
1. K.-U. Schmidt, *On a problem due to Littlewood concerning polynomials with unimodular coefficients*, arXiv:1302.2766v1, first public 2013-02-12, primary MSC 42A05 and 11B83.
2. C. Michels, *Lambda(p)-sets and the limit order of operator ideals*, arXiv:math/9904176v1, first public 1999-04-30; the manuscript lists 43A40 and 43A46 among its primary classifications.
