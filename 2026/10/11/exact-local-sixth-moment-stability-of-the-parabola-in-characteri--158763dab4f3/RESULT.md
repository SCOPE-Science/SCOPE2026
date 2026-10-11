# Exact local sixth-moment stability of the parabola in characteristic three

## Finding

Let \(q=3^n\), where \(n\ge 1\), and let \(\psi:\mathbb F_q\to\mathbb C\) be any nontrivial additive character. Define
\[
\mathcal E_q f(X,Y)=\frac1q\sum_{t\in\mathbb F_q}f(t)\psi(Xt+Yt^2),\qquad
\mathcal J_q(f)=\frac{\sum_{X,Y\in\mathbb F_q}|\mathcal E_qf(X,Y)|^6}{\left(q^{-1}\sum_t|f(t)|^2\right)^3},\quad f\ne0.
\]
Then \(\mathcal J_q(\mathbf1)=1+q^{-1}-q^{-2}\). For any mean-zero \(h=u+iv\), with \(u,v:\mathbb F_q\to\mathbb R\), and real \(\varepsilon\to0\),
\[
\mathcal J_q(\mathbf1+\varepsilon h)=1+q^{-1}-q^{-2}
-\varepsilon^2\left(\frac{3(q^2-2q+4)}{q^3}\sum_tu(t)^2
+\frac{3(q-2)}{q^2}\sum_tv(t)^2\right)+O_h(\varepsilon^3).
\]
The real half-Hessian of this local deficit has the following complete spectrum:
\[
\begin{array}{c|c|c}
\text{eigenvalue}&\text{multiplicity}&\text{eigenspace}\\\hline
0&2&\text{complex constants}\\
3(q^2-2q+4)/q^3&q-1&\text{real mean-zero functions}\\
3(q-2)/q^2&q-1&\text{purely imaginary mean-zero functions}.
\end{array}
\]
Thus nonzero constants are strict local maximizers modulo complex scaling. The sharp transverse quadratic coefficient, with respect to the unnormalized squared \(\ell^2\)-distance to complex constants, is \(3(q-2)/q^2\), attained infinitesimally precisely in imaginary mean-zero directions.

## Assumptions and scope

All sums over unspecified variables range over \(\mathbb F_q\), and the norm on coefficient functions is \(\|h\|_2^2=\sum_t|h(t)|^2\). The complex scalar action \(f\mapsto\lambda f\), \(\lambda\in\mathbb C^\times\), leaves \(\mathcal J_q\) invariant. A mean-zero direction satisfies \(\sum_t h(t)=0\); complex constants are the two real scalar tangent directions.

For a function \(f\) with \(\sum_t|f(t)|^2=q\), write \(d(f)^2=\sum_t|f(t)-q^{-1}\sum_sf(s)|^2\). The coefficient is sharp in the invariant sense
\[
\lim_{\delta\downarrow0}\ \inf_{\substack{\sum_t|f(t)|^2=q\\0<d(f)<\delta}}\frac{\mathcal J_q(\mathbf1)-\mathcal J_q(f)}{d(f)^2}=\frac{3(q-2)}{q^2}.
\]
The infimum is local, not over all nonconstant inputs without the small-distance constraint.

## Proof

**1. Exact sixth moment and triple fibers.** For \((s,w)\in\mathbb F_q^2\), set
\[
T_f(s,w)=\sum_{\substack{a+b+c=s\\a^2+b^2+c^2=w}}f(a)f(b)f(c),\qquad M(f)=\sum_{s,w}|T_f(s,w)|^2,\qquad S(f)=\sum_t|f(t)|^2.
\]
Additive character orthogonality, with precisely the normalization in the finding, gives \(\sum_{X,Y}|\mathcal E_qf(X,Y)|^6=q^{-4}M(f)\), and therefore \(\mathcal J_q(f)=M(f)/(qS(f)^3)\). Let \(r=T_{\mathbf1}\). Put \(v=a+b\), \(u=a-b\) and \(c=s-v\). Since the characteristic is three, the two fiber equations reduce to
\[
w=s^2+sv-u^2.
\]
For \(s\ne0\), each \(u\) determines a unique \(v\), hence \(r(s,w)=q\). For \(s=0\), the equation reads \(w=-u^2\), and \(v\) is free: \(r(0,0)=q\), \(r(0,w)=2q\) for nonzero negative squares, and zero otherwise. Exactly \((q-1)/2\) field elements are nonzero negative squares. Thus
\[
M(\mathbf1)=\sum_{s,w}r(s,w)^2=q^4+q^3-q^2,\qquad \mathcal J_q(\mathbf1)=1+q^{-1}-q^{-2}.
\]

**2. First and second variations.** For \(f=\mathbf1+\varepsilon h\), expand
\[
T_f=r+\varepsilon A_h+\varepsilon^2B_h+O_h(\varepsilon^3),
\quad A_h(s,w)=3\sum_t h(t)r_2(s-t,w-t^2),
\]
where \(r_2(s,w)=\#\{(a,b):a+b=s,\ a^2+b^2=w\}\) and \(B_h(s,w)\) is the sum over triples in the fiber of the three pair-products \(h(a)h(b)+h(a)h(c)+h(b)h(c)\). The identity \(2ab=(a+b)^2-(a^2+b^2)\) shows that an unordered pair is uniquely determined by its sum and sum of squares; hence \(\sum_{s,w}r_2(s,w)^2=2q^2-q\).

The quantity \(\sum_{s,w}r(s,w)r_2(s-t,w-t^2)\) does not depend on \(t\): subtracting \(t\) from all three inputs is an invertible transformation of triple fibers in characteristic three. Summing this quantity over \(t\) gives \(M(\mathbf1)\), so the quantity is \(M(\mathbf1)/q\). Consequently \(\sum_{s,w}r(s,w)A_h(s,w)=3M(\mathbf1)\sum_t h(t)/q=0\) when \(h\) has mean zero.

**3. Pair correlation.** Define
\[
K(t,u)=\sum_{s,w}r_2(s-t,w-t^2)r_2(s-u,w-u^2).
\]
On the diagonal, \(K(t,t)=2q^2-q\). For \(t\ne u\), an invertible affine change of all pair and anchored triple coordinates reduces the count to \(K(0,1)\). This counts \((a,b,c,d)\) satisfying \(a+b=c+d+1\), \(a^2+b^2=c^2+d^2+1\). Put \(R=a-b\), \(U=c-d\), \(W=c+d\). The second equation becomes \(2W=1-R^2+U^2\), and each \((R,U)\) gives precisely one quadruple because two is invertible. Thus \(K(t,u)=q^2\) off the diagonal. It follows that
\[
\sum_{s,w}|A_h(s,w)|^2=9\left((q^2-q)\sum_t|h(t)|^2+q^2\left|\sum_th(t)\right|^2\right)
=9(q^2-q)\sum_t|h(t)|^2.
\]

**4. Weighted quadratic term.** Put
\[
L(t,u)=\sum_v r(t+u+v,t^2+u^2+v^2).
\]
For all but the unique value \(v=-t-u\), the triple-sum first coordinate is nonzero and \(r=q\). At that exceptional value the second coordinate is \(-(t-u)^2\), so the exceptional multiplicity equals \(q\) when \(t=u\) and \(2q\) otherwise. Therefore \(L(t,t)=q^2\), \(L(t,u)=q^2+q\) for \(t\ne u\). By permutation symmetry among the three variables,
\[
\sum_{s,w}r(s,w)B_h(s,w)=3\sum_{t,u}L(t,u)h(t)h(u)=-3q\sum_th(t)^2,
\]
where the last equality again uses \(\sum_t h(t)=0\).

**5. Normalization and optimality.** Combining the preceding terms yields
\[
M(\mathbf1+\varepsilon h)=M(\mathbf1)+\varepsilon^2\left(9(q^2-q)\sum_t|h(t)|^2-6q\operatorname{Re}\sum_t h(t)^2\right)+O_h(\varepsilon^3).
\]
Also \(S(\mathbf1+\varepsilon h)=q+\varepsilon^2\sum_t|h(t)|^2\). Expanding \(M/(qS^3)\) proves the displayed two-coefficient formula by setting \(h=u+iv\). Both coefficients are strictly positive for every \(q\ge3\); their difference is \(12/q^3\). Scalar invariance supplies the two zero modes. Positivity in all complementary directions and finite-dimensional smoothness prove strict local maximality modulo scaling. Uniform Taylor expansion on the compact unit sphere of mean-zero directions, together with imaginary mean-zero test directions, proves the sharp distance-to-scalars limit.

## Verification

The accompanying standalone file `verify.py` uses only the Python standard library. Run `python verify.py`. It constructs \(\mathbb F_3\), \(\mathbb F_9\), \(\mathbb F_{27}\), and \(\mathbb F_{81}\) by explicit irreducible polynomial quotients; exhaustively enumerates all ordered pairs and triples; checks every occupied triple-fiber multiplicity, both critical pair correlations, the weighted-pair identities, the exact constant moment, and the two independent real/imaginary Taylor coefficients. Its observed output ends with `All exact checks passed. Finite tests are not the unrestricted proof.` The unrestricted assertion follows from the preceding counting argument rather than extrapolation from these four fields.

## Relationship to prior work

González-Riquelme and Oliveira e Silva, *Sharp extension inequalities on finite fields*, Theorem 1.3, establish the global sharp parabola \(L^2\)-to-\(L^6\) inequality under the explicit hypothesis that the characteristic is strictly greater than three. The present result instead treats characteristic three and determines only the exact **local second variation**; it neither follows by specializing that theorem nor extends its global inequality without further argument. Finite-field moment-curve endpoint studies concern \(L^{2d}\) for the degree-\(d\) curve; the degree-two case is an \(L^4\) problem, not this \(L^6\) parabola problem. Existing quadratic-surface \(L^4\) Hessian calculations likewise have different convolution fibers and Fourier exponents. The new arithmetic input is the characteristic-three degeneracy of the three-point parabola convolution.

## Limitations

The coefficient and spectrum give a local, quadratic stability theorem at nonzero constant functions and their scalar multiples. They do not establish the unrestricted global extension norm or classify global maximizers when the characteristic is three. The cubic Taylor remainder is for each fixed finite field; no field-uniform stability neighborhood is asserted. Indexed-source searches cannot rule out an equivalent unindexed result, and independent review remains outstanding.

## References

1. C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647, first publicly submitted 26 May 2024, Theorem 1.3 and Section 6, https://arxiv.org/pdf/2405.16647.
2. *Sharp endpoint extension inequalities for the moment curve on finite fields*, arXiv:2508.08377, https://arxiv.org/pdf/2508.08377 (comparison of exponent and ambient curve).
3. *Sharp endpoint extension inequalities for the moment curve on finite fields II: an extremal property of the uniform distribution*, arXiv:2609.29882, https://arxiv.org/pdf/2609.29882 (comparison of endpoint formulation).
