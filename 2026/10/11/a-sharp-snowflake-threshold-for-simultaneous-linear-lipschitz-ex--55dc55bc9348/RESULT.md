# A sharp snowflake threshold for simultaneous linear Lipschitz extensions from regular polygons

## Finding

Take an integer \(n\ge3\). Let \(A_n\) be the vertices of a regular unit-circumradius \(n\)-gon, and adjoin its center, giving \(X_n=A_n\cup\{0\}\). For \(0<\alpha\le1\), equip the set with the snowflake metric \(d_\alpha(x,y)=|x-y|^\alpha\). Let \(\Lambda_n(\alpha)\) be the infimum of the Lipschitz-seminorm operator norms of **real-linear, simultaneous extension operators** from all real Lipschitz functions on \(A_n\) to real Lipschitz functions on \(X_n\). Then

\[\boxed{\Lambda_n(\alpha)=\max\left\{1,F_n(\alpha)\right\},\qquad F_n(\alpha)=\frac1n\sum_{j=1}^{n-1}\left(2\sin\frac{\pi j}{n}\right)^\alpha.}\]

The infimum is attained by the explicit extension that preserves vertex values and assigns their arithmetic mean to the center. There is exactly one exponent \(\alpha_n\in(0,1)\) such that \(F_n(\alpha_n)=1\). Accordingly,

\[\Lambda_n(\alpha)=1\quad\Longleftrightarrow\quad 0<\alpha\le\alpha_n.\]

The threshold has an exact large-polygon scale:

\[\boxed{\lim_{n\to\infty}\sqrt n\,\alpha_n=\frac{2\sqrt6}{\pi}.}\]

For the original, unsnowflaked Euclidean chord metric,

\[\Lambda_n(1)=\frac2n\cot\left(\frac\pi{2n}\right)>1,\qquad\lim_{n\to\infty}\Lambda_n(1)=\frac4\pi.\]

The first two nontrivial thresholds are

\[\alpha_3=\frac{2\log(3/2)}{\log3},\qquad\alpha_4=\frac{2\log(\sqrt5-1)}{\log2}.\]

## Assumptions and scope

All functions and operators are real-valued and real-linear. We use the Lipschitz seminorm

\[\|f\|_{\mathrm{Lip}(Y)}=\max_{x\ne y\in Y}\frac{|f(x)-f(y)|}{d_\alpha(x,y)}.\]

The operator norm is the best number \(L\) such that \(\|Ef\|_{\mathrm{Lip}(X_n)}\le L\|f\|_{\mathrm{Lip}(A_n)}\) for every \(f:A_n\to\mathbb R\). A finite-norm extension necessarily preserves constant functions because the seminorm of an extended constant must vanish; the center value must therefore equal the given constant. This rules out non-constant-preserving linear maps and makes the seminorm operator norm unambiguous. The extension need not be positive or preserve any other structure. The snowflake power is restricted to \(0<\alpha\le1\), where \(d_\alpha\) is a metric. The center-to-vertex distance is exactly \(1\).

## Proof

**Step 1: one-center extension norm.** Every real-linear extension from functions on \(A_n\) to the extra point is described by a linear center functional

\[(Ef)(0)=\sum_{j=0}^{n-1}w_jf(v_j),\quad \sum_{j=0}^{n-1}w_j=1,\]

where \(v_j=\exp(2\pi i j/n)\). The sum condition follows from preservation of constants. Each cyclic rotation of the polygon induces isometries of both Lipschitz seminormed function spaces. Conjugating an extension by such a rotation preserves its operator norm. Averaging the conjugate extensions cannot increase that norm and produces a rotation-invariant center functional. Cyclic transitivity then forces \(w_j=1/n\) for all \(j\). Thus no linear extension can have smaller norm than the uniform-mean extension, regardless of whether its original weights were signed.

For this mean extension, the original vertex pairs require norm at least \(1\). For any vertex \(v_i\), a function with Lipschitz seminorm at most one satisfies

\[\left|f(v_i)-\frac1n\sum_j f(v_j)\right|\le\frac1n\sum_jd_\alpha(v_i,v_j)=F_n(\alpha).\]

The center-to-vertex distance is \(1\), and the right side is independent of the vertex. This estimate is sharp: for a fixed \(i\), take \(f(v_j)=d_\alpha(v_i,v_j)\); the triangle inequality makes this function one-Lipschitz, and the center-to-vertex inequality at \(v_i\) becomes an equality. Together with the untouched vertex pairs, this proves the exact formula.

More generally, this argument works without any Euclidean assumption for every finite metric space whose vertex set has a transitive isometry group fixing one new point at a common distance \(r>0\): the optimal center value is the uniform average, and the optimal norm is the maximum of \(1\) and the mean vertex-to-vertex distance divided by \(r\). For the regular snowflaked polygon, the chord lengths are \(2\sin(\pi j/n)\), yielding the stated sum.

**Step 2: unique contractivity threshold.** Extend \(F_n\) continuously to the auxiliary value \(\alpha=0\), so \(F_n(0)=(n-1)/n<1\). The classical product of chord lengths gives

\[\prod_{j=1}^{n-1}2\sin\left(\frac{\pi j}{n}\right)=n,\qquad F_n'(0)=\frac{\log n}{n}>0.\]

Also

\[F_n''(\alpha)=\frac1n\sum_{j=1}^{n-1}\left(2\sin\frac{\pi j}{n}\right)^\alpha\left(\log\left(2\sin\frac{\pi j}{n}\right)\right)^2>0\]

for all \(\alpha\ge0\). Hence \(F_n\) is strictly increasing on \([0,1]\). Summing the first powers of the chords gives

\[F_n(1)=\frac2n\cot\left(\frac\pi{2n}\right)>1.\]

Indeed this last expression increases with \(n\ge3\): writing \(t=\pi/(2n)\), it is \(4t\cot(t)/\pi\), and \(t\cot t\) decreases on \((0,\pi/2)\). At \(n=3\) its value is \(2\sqrt3/3>1\). The intermediate-value theorem and strict increase give one and only one root \(\alpha_n\in(0,1)\). The displayed values for \(n=3,4\) follow by solving a single exponential equation or a quadratic equation, respectively.

**Step 3: exact threshold asymptotics.** Let \(g(t)=\log(2\sin\pi t)\) for \(0<t<1\), which has integrable logarithmic endpoint singularities. The chord product identity yields the exact small-linear-term coefficient \(F_n'(0)=\log n/n\). Riemann sums, justified at the endpoints by logarithmic integrability, give

\[F_n''(0)=\frac1n\sum_{j=1}^{n-1}g(j/n)^2\longrightarrow\int_0^1g(t)^2\,dt=\frac{\pi^2}{12}.\]

The integral is the Parseval identity for the standard Fourier series

\[g(t)=-\sum_{k=1}^{\infty}\frac{\cos(2\pi kt)}{k},\qquad\int_0^1g(t)^2\,dt=\frac12\sum_{k=1}^{\infty}\frac1{k^2}=\frac{\pi^2}{12}.\]

Uniformly for \(0\le\alpha\le1\), the third derivative \(F_n^{(3)}(\alpha)\) has uniformly bounded absolute value because \((2\sin\pi t)^\alpha\le2\) and the discrete averages of \(|g(j/n)|^3\) are bounded independently of \(n\). One can see the latter from \(2\sin(\pi j/n)\ge4\min(j,n-j)/n\) and the integrability of the third power of the logarithm near zero. Consequently, uniformly as \(\alpha\to0\),

\[F_n(\alpha)=1-\frac1n+\frac{\log n}{n}\alpha+\frac12F_n''(0)\alpha^2+O(\alpha^3),\]

with an absolute remainder constant. For every fixed \(c>0\), substitute \(\alpha=c/\sqrt n\), multiply by \(n\), and take the limit:

\[\lim_{n\to\infty}n\left(F_n(c/\sqrt n)-1\right)=-1+\frac{\pi^2c^2}{24}.\]

The last limit is strictly negative when \(0<c<2\sqrt6/\pi\) and strictly positive when \(c>2\sqrt6/\pi\). Since \(F_n\) is strictly increasing, the unique root lies between the corresponding scaled test exponents for all sufficiently large \(n\). Squeezing \(c\) proves \(\sqrt n\,\alpha_n\to2\sqrt6/\pi\). Finally, the formula for \(F_n(1)\) converges to \(4/\pi\) by the small-angle limit.

## Verification

The standalone Python 3 script `verify.py` uses only the standard library. It numerically checks the full metric Lipschitz quotients against the predicted optimal constant for many polygon sizes and snowflake powers; constructs a sharp distance-function witness; compares the chord-product and unsnowflaked cotangent identities; verifies the closed thresholds for triangles and squares; and tests the predicted large-polygon scaling. The script reports `POLYGON_LINEAR_EXTENSION_VERIFY_OK` after 751 checks. The finite checks corroborate the formulas; the arguments above, not the script, prove the universal claims.

## Relationship to prior work

Brudnyi and Brudnyi developed general simultaneous linear Lipschitz extension constructions and estimates for homogeneous-type metric subspaces. Ambrosio and Puglisi identified the relationship between linear extension operators and random projections onto Lipschitz-free spaces. These frameworks motivate the present optimization, but their inspected statements supply neither the exact norm for this regular-polygon snowflake family nor the sharp contractivity threshold and its asymptotic. The proof here computes the optimum with a cyclic averaging argument and then resolves the analytic sine-power crossing problem.

One must distinguish the present simultaneous linear operator from the classical McShane extension of each individual real Lipschitz function, which always preserves its Lipschitz constant but depends nonlinearly on the input function. Work on Lipschitz extensions whose *ranges* are regular polygons concerns a different assignment from the regular-polygon *domains* considered here.

## Limitations

The result is for finite regular-polygon vertex sets plus one center point, real-valued functions, real-linear simultaneous operators, and power snowflake metrics with \(0<\alpha\le1\). It is not a theorem for arbitrary planar samples or for extensions to a full disk. The threshold is implicit for general \(n\), with closed forms only for the small cases stated; the asymptotic gives the first-order scale, not a uniform finite-\(n\) error bound. Finite numerical testing cannot establish an infinite family of inequalities. No independent mathematical audit has been performed, and possible historical coverage in alternative extension-operator formulations is a bibliographic risk.

## References

1. A. Brudnyi and Yu. Brudnyi, *Extension of Lipschitz functions defined on metric subspaces of homogeneous type*, arXiv:math/0609535v1 (2006), https://arxiv.org/abs/math/0609535.
2. L. Ambrosio and D. Puglisi, *Linear extension operators between spaces of Lipschitz maps and optimal transport*, preprint, https://cvgmt.sns.it/media/doc/paper/3155/weak@Lee-Naor.pdf.
3. M. Azizi and A. Rejali, *Urysohn and Tietze extensions of Lipschitz functions*, arXiv:2112.10265v1, https://arxiv.org/abs/2112.10265.
4. E. J. McShane, *Extension of range of functions*, Bull. Amer. Math. Soc. **40** (1934), 837–842. The reference is classical context for nonlinear individual-function extension; its full text was not used for any new assertion.
