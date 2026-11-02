# Generic Grassmann distance degree of the ruling curve of a balanced rational normal scroll

## Finding
For every pair of integers \(n\geq 2\), \(d\geq 2\), let \(S(n,\ldots,n)\subset\mathbb P^{d(n+1)-1}_{\mathbb C}\) be the balanced rational normal scroll, with \(d\) summands of degree \(n\). Its ruling projective \((d-1)\)-planes give a smooth rational curve \(\mathcal R_{n,d}\) of rank-\(d\) orthogonal projectors, in the rational symmetric-projector model of the complex Grassmannian \(\operatorname{pGr}(d,d(n+1))\). For generic rank-\(d\) projector data \(Q\), the squared chordal (projection) distance function has exactly \(4n-2\) distinct complex critical points on \(\mathcal R_{n,d}\), all outside the algebraic cut locus of \(Q\). Consequently the Grassmann distance degree in the projection-distance sense is
\[
\operatorname{GDdeg}(\mathcal R_{n,d})=4n-2.
\]
This equals the Euclidean distance degree already computed in the motivating article, but the generic projector-data restriction and the cut-locus exclusion are new assertions.

## Assumptions and scope
All varieties and generic points are over \(\mathbb C\), and transpose denotes the standard complex bilinear form, not Hermitian conjugation. Write \(V_n=\mathbb C[t]_{\le n}\), and \(v(t)=(1,t,\ldots,t^n)^\top\). Set \(s(t)=v(t)^\top v(t)=\sum_{j=0}^{n}t^{2j}\). For \(s(t)\ne0\), the ruling projector is the block-diagonal matrix with \(d\) copies of \(v(t)v(t)^\top/s(t)\). Its image closure is the curve \(\mathcal R_{n,d}\). Its rational projective parameterization extends over \(t=\infty\); computations use the finite affine chart.

The squared projection distance is \(\frac12\operatorname{tr}((P-Q)^2)=d-\operatorname{tr}(PQ)\), since \(P\) and \(Q\) are rank-\(d\) symmetric idempotents. A critical point is excluded if \(s(t)=0\), where the projector parameterization is undefined, or if the two rank-\(d\) subspaces have singular overlap (the algebraic Grassmann cut locus, equivalently \(\operatorname{rank}(PQ)<d\)). Critical points are counted over \(\mathbb C\) for Zariski-general \(Q\).

## Proof
**1. Rational critical equation.** Write the diagonal \((n+1)\times(n+1)\) blocks of \(Q\) as \(Q_{ii}\), and set \(N_Q(t)=\sum_{i=1}^d v(t)^\top Q_{ii}v(t)\), a polynomial of degree at most \(2n\). Then
\[
\operatorname{tr}(P(t)Q)=\frac{N_Q(t)}{s(t)},\qquad W_Q(t)=N_Q'(t)s(t)-N_Q(t)s'(t).
\]
The derivative vanishes precisely at roots of \(W_Q\) away from zeros of \(s\). For arbitrary \(N\in V_{2n}\), its Wronskian \(W_N=N's-Ns'\) has degree at most \(4n-2\), because the degree-\(4n-1\) terms cancel. The coefficient of \(t^{4n-2}\) is \(-[t^{2n-1}]N\), since the next-to-leading coefficient of \(s\) vanishes. Thus a Zariski-general \(N\) has exact Wronskian degree \(4n-2\).

The linear Wronskian system is base-point-free: at a simple root of \(s\) its value is \(-Ns'\), and away from the roots of \(s\) its value is a nonzero linear first-jet functional in \(N\). Since \(s=(t^{2n+2}-1)/(t^2-1)\) has distinct roots in characteristic zero, generic Wronskians are squarefree and coprime to \(s\). Indeed, at any point where the first-jet functional vanishes, varying the second jet makes its root simple; nonconstant rational functions with prescribed jets yield a nonempty discriminant complement. The generic coefficient above prevents a zero at infinity. Therefore a general numerator produces precisely \(4n-2\) simple finite critical points away from poles.

**2. Generic projector data generate a generic numerator.** Restrict to block-diagonal projectors determined by nonisotropic coefficient vectors \(f,g\in V_n\): use the normalized rank-one projector of \(f\) in each of \(d-1\) blocks and that of \(g\) in the final block. With coefficient dot product \(\langle f,g\rangle=\sum_{j=0}^{n} f_jg_j\), we obtain
\[
N_{f,g}=\frac{(d-1)f(t)^2}{\langle f,f\rangle}+\frac{g(t)^2}{\langle g,g\rangle}.
\]
Consider the map \(\Phi:\mathbb P(V_n)\times\mathbb P(V_n)\dashrightarrow\mathbb P(V_{2n})\), sending \(([f],[g])\) to \([N_{f,g}]\). Choose \(f,g\) coprime with \(\langle f,f\rangle\langle g,g\rangle\langle f,g\rangle\ne0\), possible on a nonempty open set. The affine differential image is
\[
U=f\,f^\perp+g\,g^\perp\subset V_{2n},
\]
where perpendicularity is in coefficient space. Each summand has dimension \(n\). If \(fh=gk\) with \(h\perp f\), \(k\perp g\), coprimality gives \(h=\lambda g\), \(k=\lambda f\), and \(\langle f,g\rangle\ne0\) forces \(\lambda=0\). Hence \(\dim U=2n\).

Moreover \(N_{f,g}\notin U\). If \(N_{f,g}=fh+gk\) with \(h\perp f\), \(k\perp g\), again coprimality gives
\[
h=\frac{d-1}{\langle f,f\rangle}f+\lambda g,\qquad
k=\frac{1}{\langle g,g\rangle}g-\lambda f.
\]
The two perpendicularity equations become \((d-1)+\lambda\langle f,g\rangle=0\) and \(1-\lambda\langle f,g\rangle=0\), a contradiction because \(d\ne0\) in characteristic zero. Thus \(U+\mathbb C N_{f,g}=V_{2n}\); the differential of \(\Phi\) is surjective onto the \(2n\)-dimensional projective target. Therefore \(\Phi\) is dominant. Its image contains a dense open subset, so generic projector data have generic numerator in the sense of step 1.

**3. Algebraic cut-locus exclusion.** For the restricted block projectors, the overlap matrix between the ruling \(d\)-plane and the projector image is diagonal up to nonzero factors, with diagonal values \(f(t)\) repeated \(d-1\) times and \(g(t)\) once. Thus the cut condition is \(f(t)g(t)=0\). At any zero \(f(t_0)=0\) with \(s(t_0)\ne0\), the critical equation reduces to
\[
W_{N_{f,g}}(t_0)=\frac{1}{\langle g,g\rangle}(2g(t_0)g'(t_0)s(t_0)-g(t_0)^2s'(t_0)).
\]
The analogous formula holds at a zero of \(g\), with coefficient \(d-1\) and the function \(f\). The nonintersection \(\gcd(W_{N_{f,g}},f g)=1\), as well as nonisotropy, \(\gcd(f,g)=1\), and avoidance of zeros of \(s\), are nonempty Zariski-open requirements. Nonemptiness follows, for example, by fixing one polynomial to a nonzero constant: the other polynomial may have distinct generic zeros avoiding the finite zero set of the derivative of that constant's contribution, namely \(s'\), and then swapping the roles. The intersection of these two nonempty opens with the dominant-map genericity open is nonempty because the parameter space is irreducible. Thus the \(4n-2\) roots do not lie in the cut locus for some, hence general, rank-\(d\) projector data. Since the complex rank-\(d\) projector variety is irreducible, nonemptiness of these generic nonvanishing conditions on this subfamily proves the generic assertion on the full data space. This establishes the theorem.

## Verification
Run `python3 checks/verify.py` in a standard Python 3 environment. The program performs exact polynomial arithmetic over \(\mathbb F_{1000003}\) for \(2\le n\le7\) and \(d\in\{2,3,5\}\), independently builds the restricted projector numerator, checks Wronskian degree and squarefreeness, verifies absence of common roots with \(s f g\), and computes the rank of a Jacobian augmented by \(N\). Its result is `VERIFY_OK`. Finite-field calculations check examples only; the uniform characteristic-zero statement follows from the proof above.

## Relationship to prior work
Friedman–Hoşten–Rosana compute the Euclidean distance degree of scroll ruling curves in their Theorem 2.2 and discuss Grassmann distance degree for projector data in Section 4. Their general comparison result and expectations do not explicitly settle the Grassmann-distance degree of these balanced ruling curves or ensure cut-locus avoidance. For the present equal-degree family, their Euclidean-distance formula is already \(4n-2\); the new part is dominance of the restricted numerator map and proof that generic projector data retain all critical points off the cut locus. The earlier Grassmann-distance-complexity literature on the Riemannian intrinsic metric concerns a different enumerative invariant.

## Limitations
The assertion is for balanced scrolls with all summand degrees equal, characteristic zero, and the projection/chordal distance on rank-\(d\) projectors; it does not compute Grassmann distance degree of arbitrary unbalanced scrolls or the Riemannian geodesic-distance degree. The literature comparison cannot rule out an unlocated equivalent general theorem. No independent mathematical audit has been performed.

## References
1. Friedman, Hoşten, Rosana, *Euclidean Distance Optimization Within the Grassmannian*, arXiv:2610.02018, version first made public 2026-10-01, https://arxiv.org/abs/2610.02018. See Theorem 2.2 and Section 4.
2. Lerario and Rosana, *The Grassmann distance complexity*, arXiv:2411.16589, https://arxiv.org/abs/2411.16589 (background on a different, intrinsic metric).
