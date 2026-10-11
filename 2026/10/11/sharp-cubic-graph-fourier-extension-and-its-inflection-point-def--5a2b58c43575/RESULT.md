# Sharp cubic-graph Fourier extension and its inflection-point deficit

## Finding

Let \(F\) be a finite field of order \(q\), of characteristic strictly greater than \(3\), and let \(\psi:F\to\mathbb C\) be a nontrivial additive character. For \(f:F\to\mathbb C\), define
\[
T f(u,v)=\sum_{t\in F}f(t)\,\psi(ut+vt^3),\qquad
\|Tf\|_4^4=\frac1{q^2}\sum_{u,v\in F}|Tf(u,v)|^4.
\]
The input norm is \(\|f\|_2^2=\sum_{t\in F}|f(t)|^2\). Then, for every \(q\) and every such \(\psi\),
\[
\boxed{\|T\|_{\ell^2(F)\to L^4(F^2)}^4=3-\frac6{2q+1}.}
\]
All nonzero extremizers, and no others, have the following form. Write \(A=\|f\|_2^2>0\). Then
\[
|f(0)|^2=\frac{3A}{2q+1},\qquad
|f(t)|^2=\frac{2A}{2q+1}\quad(t\ne0),
\]
and all the nonzero complex numbers \(f(t)f(-t)\), for \(t\ne0\), have the same argument as \(f(0)^2\). Equivalently, up to a nonzero complex scalar, choose independently one phase for each of the \((q-1)/2\) nonzero antipodal pairs; the opposite point has the reciprocal phase relative to the central phase. The projective extremizer locus is a real torus of dimension \((q-1)/2\).

In particular, the constant function is not extremal. Its fourth-power quotient equals \(3-3/q+1/q^2\), strictly less than the sharp value by
\[
\frac{q-1}{q^2(2q+1)}>0.
\]
The same norm, equality classification, and deficit decomposition apply to the graph of every polynomial \(P(t)=a t^3+b t^2+c t+d\) with \(a\ne0\); replace the distinguished parameter \(0\) by the flex parameter \(-b/(3a)\).

## Assumptions and scope

No primality assumption on \(q\) is needed: \(F\) can be a non-prime finite field. The restriction on characteristic guarantees that \(2\) and \(3\) are invertible and the cubic pair-sum identity identifies unordered pairs away from zero sum. All averages on \(F^2\) use uniform probability, all input sums use counting measure, and an extremizer means a nonzero complex-valued function attaining the displayed operator norm. The theorem does not address characteristic \(2\) or \(3\).

Choose one representative from each unordered antipodal pair \(\{t,-t\}\subset F^\times\), and call the representative set \(R\), so \(|R|=(q-1)/2\). Define
\[
\begin{aligned}
A&=\sum_{t\in F}|f(t)|^2,& z&=|f(0)|^2,\\
s_t&=|f(t)|^2+|f(-t)|^2,& r_t&=|f(t)f(-t)|,\\
\tau_t&=s_t-2r_t=(|f(t)|-|f(-t)|)^2,&
B&=z+2\sum_{t\in R}r_t,\\
Z&=f(0)^2+2\sum_{t\in R}f(t)f(-t),&
\delta(f)&=\left(3-\frac6{2q+1}\right)A^2-\|Tf\|_4^4.
\end{aligned}
\]
The central quantitative claim is the following **exact deficit identity**, valid without any nonvanishing hypotheses on \(f\):
\[
\boxed{\begin{aligned}
\delta(f)={}&2\left(z-\frac{3A}{2q+1}\right)^2
+\frac32\sum_{t\in R}\left(s_t-\frac{4A}{2q+1}\right)^2\\
&+(B^2-|Z|^2)
+\sum_{t\in R}\tau_t\left(A+B-\frac{s_t+2r_t}{2}\right).
\end{aligned}}
\]
Every summand is nonnegative. This single identity provides the norm and every equality case.

## Proof

**Step 1: resolve the pair-sum fibers.** Character orthogonality gives the exact identity
\[
\|Tf\|_4^4=
\sum_{(s,c)\in F^2}
\left|\sum_{\substack{x+y=s\\x^3+y^3=c}}f(x)f(y)\right|^2.
\]
If \(s\ne0\), the identity \(x^3+y^3=s^3-3sxy\) determines the product \(xy=(s^3-c)/(3s)\). Consequently a nonempty fiber with nonzero sum consists either of a single diagonal ordered pair or of precisely the two orderings of one distinct unordered pair. If \(s=0\), every pair has the form \((t,-t)\), and all such ordered pairs have cubic sum zero. Thus the only exceptional fiber is at \((s,c)=(0,0)\), and its contribution is \(|Z|^2\).

**Step 2: write the exact fourth moment.** Put \(w_t=|f(t)|^2\). Every nonzero-sum unordered pair of distinct points contributes \(4w_xw_y\), every nonzero diagonal \((t,t)\) contributes \(w_t^2\), and the exceptional fiber contributes \(|Z|^2\). Expanding \(A^2\) and separating opposite pairs yields
\[
\begin{aligned}
\|Tf\|_4^4
&=|Z|^2+\sum_{t\ne0}w_t^2
  +4\!\sum_{\substack{\{x,y\}\subset F,\ x\ne y\\x+y\ne0}}w_xw_y\\
&=2A^2-2z^2-\sum_{t\in R}s_t^2-2\sum_{t\in R}r_t^2+|Z|^2.
\end{aligned}
\]
Here the unordered-pair sum counts each two-element subset once. Every equality is exact for arbitrary complex \(f\).

**Step 3: split the deficit into nonnegative obstructions.** The triangle inequality gives \(|Z|\le B\), and \(0\le\tau_t\), with
\[
A=z+\sum_{t\in R}s_t,\qquad B=A-\sum_{t\in R}\tau_t.
\]
Since \(2r_t=s_t-\tau_t\), the previous fourth-moment formula becomes
\[
\|Tf\|_4^4=2A^2-2z^2-\frac32\sum s_t^2
 +\sum s_t\tau_t-\frac12\sum\tau_t^2+|Z|^2.
\]
Subtract this from \(3A^2-2z^2-\frac32\sum s_t^2\), and use \(A^2-B^2=(A-B)(A+B)\). It follows exactly that
\[
\left(3A^2-2z^2-\frac32\sum s_t^2\right)-\|Tf\|_4^4
=(B^2-|Z|^2)+\sum_{t\in R}\tau_t\left(A+B-\frac{s_t+2r_t}{2}\right).
\]
Each coefficient in the last sum is nonnegative: \(A\ge s_t\) and \(B\ge2r_t\) imply
\[
A+B-\frac{s_t+2r_t}{2}\ge\frac{s_t}{2}+r_t\ge0.
\]
The inequality is strict whenever \(\tau_t>0\), since then \(s_t>0\).

**Step 4: optimize the total mass allocation.** Under \(z+\sum_{R}s_t=A\), the quadratic form \(2z^2+\frac32\sum_R s_t^2\) has unique minimizer
\[
z_*=\frac{3A}{2q+1},\qquad s_*=\frac{4A}{2q+1}\quad\text{for every }t\in R.
\]
Indeed \(4z_*=3s_*\), and completing squares gives the exact identity
\[
2z^2+\frac32\sum_R s_t^2-\frac{6A^2}{2q+1}
=2(z-z_*)^2+\frac32\sum_R(s_t-s_*)^2.
\]
Combining Steps 3 and 4 proves the boxed nonnegative deficit identity and the universal sharp upper bound.

**Step 5: classify equality.** If \(A>0\) and the deficit is zero, the positive square terms force \(z=z_*>0\) and \(s_t=s_*>0\) for all pairs. The last nonnegative sum forces each \(\tau_t=0\), hence equal magnitudes within every antipodal pair. Therefore \(|f(0)|^2=3A/(2q+1)\), and each \(|f(\pm t)|^2=s_*/2=2A/(2q+1)\). Finally \(B^2=|Z|^2\) forces equality in the triangle inequality; since all summands are nonzero, \(f(0)^2\) and every \(f(t)f(-t)\) share one argument. Conversely, these conditions force every deficit term to vanish. They are realizable, for instance by \(f(0)=\sqrt3\), \(f(t)=\sqrt2\) for \(t\ne0\), up to rescaling, completing the sharp-norm and classification proof.

**Step 6: arbitrary cubic graphs.** In characteristic exceeding three, translating \(t=u-b/(3a)\) removes the quadratic term from \(P(t)\), yielding \(P(t)=a u^3+\alpha u+\beta\) for suitable \(\alpha,\beta\in F\). An invertible affine change of the two output coordinates maps the graph of \(P\) to that of \(u^3\). Such transformations only permute Fourier sampling frequencies and apply unit-modulus factors, so the normalized fourth moment is unchanged after the corresponding bijective reparameterization of the input. Its distinguished parameter is \(t=-b/(3a)\), giving the stated generality.

## Verification

The attached `artifacts/verify.py` uses only the Python 3 standard library. Reproduce by running `python artifacts/verify.py` from the extracted package. It exhaustively checks every ordered pair-sum fiber for four prime fields and one quadratic extension field, compares a direct exact Gaussian-integer convolution to the closed fourth-moment formula in forty test cases, checks the sharp deficit decomposition, and compares twenty numerical character sums to exact convolution predictions. Its execution reports:

`VERIFY_OK finite_fields=5 quadratic_extension=F25 exact_integer_convolution_cases=40 direct_fourier_cases=20 deficit_checks=PASS`

The finite calculations corroborate the algebraic proof; they do not prove the theorem for all finite fields. They also do not provide a complete extremizer enumeration over continuous complex coefficients.

## Relationship to prior work

The character-orthogonality reduction is standard in finite-field Fourier restriction, as in Mockenhaupt–Tao [1]. Iosevich–Koh [2] study extensions of nondegenerate quadratic surfaces. Koh–Shen [3] establish sharp *ranges of extension exponents* for planar algebraic curves, including broad classes of polynomial graphs; their theorem does not specify the exact finite-field constant, equality set, or an exact deficit for the cubic graph. González-Riquelme–Oliveira e Silva [4] analyze sharp finite-field extension inequalities for parabolas, paraboloids, hyperbolic paraboloids and cones, not the cubic graph in the plane. Thus the present theorem targets a more specific exact-constant and equality-case question not resolved by those statements.

The mechanism differs from the quadratic planar parabola: the odd cubic has a uniquely large pair-sum fiber at zero, forcing the optimal input modulus to be higher at the flex parameter. Results for monomial moment curves at other extension exponents or for quartic graph constant-input additive energy do not imply this exact weighted \(\ell^2\to L^4\) result. The literature comparison is substantive but not exhaustive; an equivalent older additive-energy or algebraic-curve formulation remains possible.

## Limitations

This is a same-model mathematical review, not an independent audit or a certified claim of bibliographic priority. The norm, exact deficit and equality cases are proved only for characteristic greater than three. The coefficient of any derived global stability distance to the extremizer set is not asserted optimal; no such global distance inequality is claimed. Test cases are finite and cannot substitute for the all-field proof. The literature inspection compared specified principal theorems and relevant proof material, not every historical article in finite harmonic analysis.

## References

[1] G. Mockenhaupt and T. Tao, *Restriction and Kakeya phenomena for finite fields*, arXiv:math/0204234, initially public 18 April 2002.

[2] A. Iosevich and D. Koh, *Extension theorems for the Fourier transform associated with non-degenerate quadratic surfaces in vector spaces over finite fields*, arXiv:0804.4505, initially public 28 April 2008.

[3] D. Koh and C.-Y. Shen, *Sharp extension theorems and Falconer distance problems for algebraic curves in two dimensional vector spaces over finite fields*, arXiv:1003.4240, initially public March 2010.

[4] C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647, initially public 26 May 2024.
