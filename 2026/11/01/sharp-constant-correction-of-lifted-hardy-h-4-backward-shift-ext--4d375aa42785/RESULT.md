# Sharp constant correction of lifted Hardy \(H^4\) backward-shift extremizers

## Finding
Let \(Bf(z)=(f(z)-f(0))/z\) be the classical backward shift on the complex Hardy space \(H^4(\mathbb D)\). Put
\[
\varphi=\frac{1+\sqrt5}{2},\quad r=\sqrt{\frac{\varphi}{2}},\quad
 t=\frac1{\sqrt{2\varphi}},\quad q=t^2,\quad A=q(1-r^2),\quad
 D=\frac{1-r^4}{\varphi}.
\]
Let \(\delta>0\) be the unique positive solution of
\[
\delta^3+2q\delta=A,
\]
and set
\[
D_*=D+\delta^4+4q\delta^2-4A\delta.
\]
For the natural family of one-step lifts of *all* norm-attaining vectors for \(B\),
\[
\mathcal E=\{z(I(z)-t)+c:\ I\text{ is inner},\ I(0)=r,\ c\in\mathbb C\},
\]
the exact restricted second-iterate norm is
\[
\boxed{\ \sup_{F\in\mathcal E}\frac{\|B^2F\|_{H^4}}{\|F\|_{H^4}}
=\left(\frac{1-r^4}{D_*}\right)^{1/4}=1.143119317106\ldots\ .\ }
\]
Every maximizing \(I\) is a disk automorphism
\[
I(z)=\frac{r-\omega z}{1-r\omega z},\qquad |\omega|=1,
\]
and, for this parametrization, its unique minimizing constant is \(c=\delta\overline\omega\). Scalar multiplication of \(F\) does not affect the quotient.
In particular the *unrestricted* second backward-shift norm obeys the strict bound
\[
\boxed{\ \|B^2\|_{H^4\to H^4}\ge1.143119317106\ldots>
\|B\|_{H^4\to H^4}=\varphi^{1/4}=1.127838485561\ldots\ .\ }
\]
The exact unrestricted value of \(\|B^2\|\) is **not** asserted.

## Assumptions and scope
The Hardy norm is \(\|f\|_{H^4}^4=\int_{\mathbb T}|f|^4\,dm\), where \(dm=d\theta/(2\pi)\). An inner function is analytic on the disk and has unit-modulus radial boundary values almost everywhere. Such functions are in \(H^4\). All stated suprema range over complex scalars, not just real corrections. The source theorem of Bampouras and Llinares gives \(\|B\|^4=\varphi\) and says its nonzero extremizers are exactly scalar multiples of \(I-t\) with \(I(0)=r\). Thus \(\mathcal E\) is canonical: multiply any normalized first-step extremizer by \(z\), then add an arbitrary constant (which belongs to the kernel of \(B^2\)). This restriction is deliberate; additional linear corrections to the lift are not optimized here.

## Proof
**1. Fixed numerator and fixed initial denominator.** Fix inner \(I\) with \(I(0)=r\), and write \(f=I-t\), \(F_0=zf\). Since \(I\) is inner, multiplication by \(I\) is an isometry of \(H^2\); since \(I^k(0)=r^k\), elementary boundary integration yields
\[
\|f\|_{H^2}^2=1+t^2-2tr=q,
\qquad
\|f\|_{H^4}^4=D=\frac{1-r^4}{\varphi}.
\]
The last identity is also the extremizer identity in Bampouras--Llinares. On the unit circle, \(|zf|=|f|\), so \(\|F_0\|_{H^4}^4=D\). Moreover \(B(F_0+c)=f\) and \(B^2(F_0+c)=BI\), independently of \(c\). The elementary inner-function formula
\[
\|BI\|_{H^4}^4=1-|I(0)|^4=1-r^4
\]
therefore fixes the numerator for the entire family.

**2. Exact fourth-power correction polynomial.** For a boundary function \(F_0\) analytic with \(F_0(0)=0\), expanding \(|F_0+c|^4\) and integrating shows
\[
\|F_0+c\|_{H^4}^4
=\|F_0\|_{H^4}^4+4\|F_0\|_{H^2}^2|c|^2+|c|^4
+4\operatorname{Re}\big(\overline c\,M\big),
\]
where \(M=\int_{\mathbb T}|F_0|^2F_0\,dm\). The terms involving \(\int F_0\,dm\) and \(\int F_0^2\,dm\) vanish because their constant Fourier coefficients are zero. In the present case \(M=\int z(I-t)|I-t|^2\,dm\). The boundary identity \(I\overline I=1\) gives
\[
(I-t)|I-t|^2=(1+2t^2)I-t I^2+t^2\overline I-t(2+t^2).
\]
Only the \(t^2\overline I\) term contributes a Fourier coefficient at frequency \(-1\); hence
\[
M=q\overline{I'(0)},
\quad
\boxed{\ \|F_0+c\|_{H^4}^4
=D+4q|c|^2+|c|^4+4q\operatorname{Re}(\overline c\,\overline{I'(0)})\ .\ }
\]
This identity holds for arbitrary (including singular) inner functions; all integrals are absolutely convergent because the functions are bounded.

**3. Optimization, with all equality cases.** Fix \(\rho=|I'(0)|\). For each \(x=|c|\), the final term is at least \(-4q\rho x\), with equality for \(c=-x\overline{I'(0)}/\rho\) when \(\rho>0\). The resulting denominator is
\[
Q_\rho(x)=D+x^4+4qx^2-4q\rho x,\qquad x\ge0.
\]
Its derivative is \(4(x^3+2qx-q\rho)\) and its second derivative is \(12x^2+8q>0\). Therefore there is a unique global minimizer, the positive solution of \(x^3+2qx=q\rho\), or \(x=0\) if \(\rho=0\). Furthermore \(\min_x Q_\rho(x)\) is strictly decreasing in \(\rho>0\). By Schwarz--Pick,
\[
|I'(0)|\le1-|I(0)|^2=1-r^2,
\]
with equality, because \(r\in(0,1)\), if and only if \(I(z)=(r-\omega z)/(1-r\omega z)\) for \(|\omega|=1\). Thus \(q\rho\le A\); the full constrained infimum equals \(D_*\), reached precisely by the stated disk automorphisms with \(I'(0)=-(1-r^2)\omega\) and \(c=\delta\overline\omega\). Since their denominator is positive (it is an actual norm of a nonzero analytic function), the quotient optimization is legitimate.

**4. Strict comparison with the first iterate.** The strictly convex function \(Q_{1-r^2}\) has \(Q_{1-r^2}'(0)=-4A<0\); hence \(D_*<D\). Consequently
\[
\frac{1-r^4}{D_*}>
\frac{1-r^4}{D}=\varphi=\|B\|^4.
\]
The decimal values displayed in the finding are numerical evaluations of these explicit algebraic formulas; they are not used in the proof.

## Verification
Run `python verify.py` with Python 3. It checks the defining cubic, rationally bracketed numerical values, the exact fourth-power formulas for four rotations of the extremizing Blaschke automorphism via circular quadrature, and the correction formula for a degree-two inner function. All checks passed. Independently of numerics, the proof requires only the cited first-iterate extremizer theorem, Fourier orthogonality, Schwarz--Pick and one-variable strict convexity. No enumeration or floating-point step is used to establish any infinite-dimensional conclusion.

## Relationship to prior work
Bampouras and Llinares (arXiv:2605.10469v1, May 11, 2026), Theorem 1.1 and Corollary 3.2, establish the exact first-iterate norm and characterize all its extremizers. Their Corollary 4.2 only states \(\varphi^{1/4}\le\|B^n\|\le\sqrt2\) for \(n\ge2\), with no strict first-step inequality or optimized lift constant. Ferguson (arXiv:1702.03313) treats norms of the first backward shift and related operators, not this restricted \(B^2\) optimization. The argument here takes the first-iterate extremal family as input, then uses an exact fourth-moment identity and Schwarz--Pick to optimize the entire lifted family. A fully global evaluation of \(\|B^2\|\), or an estimate for every iterate, does not follow.

## Limitations
The sharp number is the norm quotient supremum over \(\mathcal E\), not a claimed sharp global \(\|B^2\|\). The calculation does not determine whether some functions outside the family give larger quotients. The result relies on the published characterization of \(B\)-extremizers; the algebraic optimization is independent of the proof of that source theorem. The review of novelty cannot rule out equivalent arguments in unindexed, older, or inaccessible work, notably a separate norm-estimates manuscript announced but not available for content inspection. Independent mathematical audit is not claimed.

## References
1. K. Bampouras and A. Llinares, *The norm of the backward shift on \(H^4\) is \(\sqrt[4]{\varphi}\)*, arXiv:2605.10469v1, first submitted May 11, 2026. https://arxiv.org/pdf/2605.10469 . Relevant results: Theorem 1.1, Lemma 3.1, Corollaries 3.2 and 4.2.
2. T. Ferguson, *Bounds on the Norm of the Backward Shift and Related Operators in Hardy and Bergman Spaces*, arXiv:1702.03313v1 (2017), https://arxiv.org/pdf/1702.03313 .
3. Classical Schwarz--Pick equality theorem for analytic self-maps of the disk, used in the standard form \(|I'(0)|\le1-|I(0)|^2\), with equality only for automorphisms.
