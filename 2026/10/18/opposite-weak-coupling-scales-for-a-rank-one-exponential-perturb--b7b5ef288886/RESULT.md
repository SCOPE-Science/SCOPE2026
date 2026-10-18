# Opposite weak-coupling scales for a rank-one exponential perturbation of the Carleman operator

## Finding

Let \(\mathcal H=L^2((0,\infty),dt)\), and define the positive Carleman operator
\[
(Cf)(t)=\int_0^\infty\frac{f(s)}{t+s}\,ds.
\]
Set \(g(t)=\sqrt2e^{-t}\), \(P_gf=\langle f,g\rangle g\), and \(A_\gamma=C+\gamma P_g\), for real \(\gamma\). Then \(\sigma_{\mathrm{ess}}(A_\gamma)=[0,\pi]\). For each \(\gamma>0\), there is exactly one eigenvalue \(\lambda_+(\gamma)>\pi\); for each \(\gamma<0\), there is exactly one eigenvalue \(\lambda_-(\gamma)<0\). Both are simple, and no other eigenvalues, including embedded or endpoint eigenvalues, occur.

The eigenvalues are determined by the *exact scalar secular equation*
\[
1=\gamma F(\lambda),\qquad
F(z)=\frac1\pi\int_{-\pi/2}^{\pi/2}\frac{d\theta}{z-\pi\cos\theta},\quad z\in\mathbb R\setminus[0,\pi].
\]
For \(z>\pi\), this becomes
\[
F(z)=\frac{4}{\pi\sqrt{z^2-\pi^2}}
\arctan\sqrt{\frac{z+\pi}{z-\pi}}.
\]
For \(z=-a<0\) with \(0<a<\pi\), it becomes
\[
-F(-a)=\frac{4}{\pi\sqrt{\pi^2-a^2}}
\operatorname{artanh}\sqrt{\frac{\pi-a}{\pi+a}}.
\]
For \(a=\pi\), the last positive quantity is \(2/\pi^2\); for \(a>\pi\) it equals
\[
\frac{4}{\pi\sqrt{a^2-\pi^2}}
\arctan\sqrt{\frac{a-\pi}{a+\pi}}.
\]

The two emerging eigenvalues have *inequivalent sharp weak-coupling scales*:
\[
\boxed{\lambda_+(\gamma)-\pi=\frac2\pi\gamma^2+O(\gamma^3)}\qquad(\gamma\downarrow0),
\]
\[
\boxed{\lambda_-(\gamma)=-2\pi\exp\!\left(-\frac{\pi^2}{2|\gamma|}\right)(1+o(1))}\qquad(\gamma\uparrow0).
\]
The exact coupling landmarks \(\lambda_+(3\pi\sqrt3/4)=2\pi\) and \(\lambda_-(-\pi^2/2)=-\pi\) follow from the same scalar formula. At strong coupling, \(\lambda_\pm(\gamma)=\gamma+2+O(|\gamma|^{-1})\), with the sign of \(\gamma\) selecting the branch.

## Assumptions and scope

The Hilbert space is complex, the integration variable is Lebesgue measure on the half-line, and the rank-one vector is exactly \(\sqrt2e^{-t}\), with \(\|g\|_2=1\). The coupling \(\gamma\) is an arbitrary real scalar. The operator \(C\) is initially defined on compactly supported smooth functions and extended by its bounded Mellin multiplier representation. All spectra refer to this bounded self-adjoint extension. The limiting formulas are for fixed normalized \(g\) with \(\gamma\) approaching zero through the indicated one-sided real ranges. Neither statement asserts an asymptotic for arbitrary perturbing vectors or arbitrary finite-rank Hankel perturbations.

## Proof

**1. Mellin normalization.** The unitary Mellin transform
\[
(\mathcal Mf)(\xi)=\frac1{\sqrt{2\pi}}
\int_0^\infty t^{-1/2-i\xi}f(t)\,dt
\]
converts \(C\) into multiplication by \(m(\xi)=\pi/\cosh(\pi\xi)\). It follows that \(C\) is positive, \(\|C\|=\pi\), and it has purely continuous spectrum \([0,\pi]\). For the chosen vector,
\[
(\mathcal Mg)(\xi)=\frac{\Gamma(1/2-i\xi)}{\sqrt\pi},
\qquad |(\mathcal Mg)(\xi)|^2=\frac1{\cosh(\pi\xi)}=:w(\xi).
\]
The latter identity is the Gamma reflection formula. Notice that \(\int_{\mathbb R}w(\xi)\,d\xi=1\), confirming the normalization.

**2. Exact rank-one reduction.** If \(z\notin[0,\pi]\), then the eigenvector equation reduces to
\[
f=\gamma\langle f,g\rangle(z-C)^{-1}g.
\]
Since \(\mathcal Mg\) never vanishes, a nonzero solution exists precisely when \(1=\gamma F(z)\), where
\[
F(z)=\langle g,(z-C)^{-1}g\rangle
=\int_{\mathbb R}\frac{w(\xi)}{z-\pi w(\xi)}\,d\xi.
\]
Make the substitution \(x=\sinh(\pi\xi)\), followed by \(x=\tan\theta\). Then \(w(\xi)\,d\xi=d\theta/\pi\) and \(w(\xi)=\cos\theta\) for \(-\pi/2<\theta<\pi/2\), proving the angular integral stated above. The half-angle substitution \(u=\tan(\theta/2)\) turns it into
\[
F(z)=\frac{2}{\pi}\int_{-1}^{1}
\frac{du}{(z-\pi)+(z+\pi)u^2}.
\]
Elementary integration gives the three displayed exterior formulas.

**3. Uniqueness and full point spectrum.** On either complementary component of \([0,\pi]\),
\[
F'(z)=-\int_{\mathbb R}\frac{w(\xi)}{(z-m(\xi))^2}\,d\xi<0.
\]
For \(z\in(\pi,\infty)\), \(F\) decreases continuously from \(+\infty\) to zero; for \(z\in(-\infty,0)\), it decreases from zero to \(-\infty\). Thus there is one and only one exterior solution, on the side prescribed by the sign of \(\gamma\), and its eigenspace is one-dimensional. In the Mellin representation, an interior eigenfunction with eigenvalue \(\lambda\in(0,\pi)\) would have to be proportional to \((m(\xi)-\lambda)^{-1}(\mathcal Mg)(\xi)\). This is not square-integrable near either of the two simple zeros of \(m-\lambda\). At \(\lambda=\pi\) the denominator has a double zero at \(\xi=0\), and at \(\lambda=0\) the inverse quotient has squared modulus \(1/(\pi^2w(\xi))\), whose integral diverges. A vanishing proportionality coefficient forces a zero function. Therefore there are no embedded or edge eigenvalues. Compactness of \(P_g\) preserves the essential spectrum; the entire spectrum is \([0,\pi]\) together with the stated single exterior eigenvalue when \(\gamma\ne0\).

**4. Different edge singularities.** Write \(z=\pi+\delta\), \(\delta>0\). Expansion of the closed form gives
\[
F(\pi+\delta)=\sqrt{\frac2\pi}\,\delta^{-1/2}
-\frac2{\pi^2}+O(\sqrt\delta).
\]
Inverting \(1=\gamma F(\pi+\delta)\) proves \(\delta=(2/\pi)\gamma^2+O(\gamma^3)\). On the other side, with \(a=-z\downarrow0\),
\[
-F(-a)=\frac2{\pi^2}\log\frac{2\pi}{a}
+O\!\left(a^2\log\frac1a\right).
\]
Inversion of \(1=|\gamma|[-F(-a)]\) yields \(a=2\pi\exp[-\pi^2/(2|\gamma|)](1+o(1))\). The error term is small even after exponentiation because \(a\) is exponentially small.

**5. Landmarks and strong coupling.** At \(z=2\pi\), the exterior formula gives \(F(2\pi)=4/(3\pi\sqrt3)\); at \(z=-\pi\) it gives \(F(-\pi)=-2/\pi^2\), proving the two exact landmarks. Finally, the expansion of the rank-one Stieltjes transform is \(F(z)=z^{-1}+2z^{-2}+O(|z|^{-3})\): the first moment is \(\langle g,Cg\rangle=\pi\int_{\mathbb R}w(\xi)^2\,d\xi=2\). The exterior solution tends to the respective infinity as \(|\gamma|\to\infty\), so substitution in the secular equation gives \(\lambda_\pm(\gamma)=\gamma+2+O(|\gamma|^{-1})\).

## Verification

The standalone script `check_carleman.py` compares the exterior closed forms against independently integrated angular resolvents, verifies two exact spectral landmarks, checks monotonicity, and exercises both weak-coupling limits and the strong-coupling moment. These checks corroborate numerical constants and algebra but do not replace the Mellin-transform and rank-one arguments establishing the operator-theoretic statements. Run it with `python3 check_carleman.py` using the Python standard library. The report of an actual execution appears in `VERIFICATION.md`.

## Relationship to prior work

Yafaev's 2012 work derives the Mellin dispersion relation and Carleman resolvent, and studies perturbations above \(\pi\) in broad generality. In particular, existence of an exterior positive-coupling eigenvalue is not new here. Yafaev's 2013 paper proves that the number of negative eigenvalues of a finite-rank Hankel perturbation is unchanged by addition of the Carleman operator; the negative-coupling eigenvalue count is therefore also known. The contribution isolated here is the *closed scalar law for the canonical normalized exponential perturbation, exact coupling landmarks, and explicit nonmatching quadratic versus exponentially small edge emergence with prefactors*. Neither inspected primary treatment states those two sharp edge laws for this rank-one kernel. The absence of a matching item in searchable records is not by itself evidence of novelty.

## Limitations

The result is restricted to the fixed exponential rank-one direction and real coupling. It does not give a scattering matrix, an embedded-resonance expansion, or weak-coupling laws for more general Hankel kernels. The literature comparison identifies no equivalent quantitative result in the inspected sources, but a differently formulated historical treatment may exist. The accompanying computational checks are finite consistency tests, not independent verification of originality or of the analytical proof.

## References

1. D. R. Yafaev, *Spectral and scattering theory for perturbations of the Carleman operator*, arXiv:1210.5709 (first public version 2012-10-21), especially Sections 1–3 and 6. https://arxiv.org/abs/1210.5709
2. D. R. Yafaev, *On finite rank Hankel operators*, arXiv:1304.2677 (first public version 2013-04-09), Theorem 1.3 and Sections 1.2 and 3.4. https://arxiv.org/abs/1304.2677
