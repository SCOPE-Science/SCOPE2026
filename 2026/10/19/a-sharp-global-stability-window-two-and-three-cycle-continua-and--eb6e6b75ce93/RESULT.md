# A sharp global stability window, two- and three-cycle continua, and five-step collapse at a degenerate border collision

## Finding
Consider the continuous homogeneous planar border-collision map
\[
F(x,y)=\begin{cases}
(-ax+y,0),&x\leq0,\\
(-bx+y,-dx),&x\geq0,
\end{cases}
\qquad a>0,\quad b\geq0,\quad d>0.
\]
The origin is **globally exponentially stable if and only if**
\[
\boxed{ab-1<d<ab+\frac1a.}
\]
At the admissible lower boundary \(d=ab-1>0\), there is a continuum of primitive two-cycles. At the upper boundary \(d=ab+1/a\), there is a continuum of primitive three-cycles. These are every nonzero periodic orbit at their respective boundary. At \(d=ab\) (necessarily \(b>0\)), the exact global finite-time identity is \(F^5\equiv0\), whereas \(F^4\not\equiv0\). Outside the closed stability window, every orbit that does not eventually reach the origin has unbounded norm.

In particular \((a,b,d)=(2,1,2)\) has \(F^5\equiv0\) even though the spectral radii of both branch matrices are greater than one (respectively \(2\) and \(\sqrt2\)).

## Assumptions and scope
The domain is all of \(\mathbb R^2\). The branch values at \(x=0\) agree, so either weak inequality defines the same map. The left determinant is zero; the switching offset is identically zero. The constants satisfy \(a>0\), \(b\ge0\), and \(d>0\), with no further restrictions. Global exponential stability means there are \(C>0\) and \(0<\rho<1\) for which \(\|F^n z\|\le C\rho^n\|z\|\) for all \(z\in\mathbb R^2\) and nonnegative integers \(n\). A primitive cycle has least positive period equal to its stated length.

Put \(q=ab\) and \(S=\{(r,0):r>0\}\). The exact radial return and its time are
\[
F^{\ell}(r,0)=(\kappa r,0),\qquad
(\ell,\kappa)=\begin{cases}
(2,q-d),&0<d<q,\\
(2,0),&d=q,\\
(3,a(d-q)),&d>q.
\end{cases}
\]
In the middle case the orbit reaches the origin in two more steps. In the outer cases \(\kappa>0\).

## Proof
**1. Universal entrance into a positive ray.** If \(x\le0\), then \(F(x,y)=(u,0)\), where \(u=-ax+y\). When \(u\ge0\) the image already lies in \(S\cup\{0\}\); when \(u<0\) the second image is \((-au,0)\in S\).

If \(x>0\), let \(s=y-bx\). Then \(F(x,y)=(s,-dx)\). For \(s\le0\),
\[
F^2(x,y)=(-as-dx,0),
\]
which lies in \(S\cup\{0\}\) or is sent there by one additional left step. For \(s>0\),
\[
F^2(x,y)=(-bs-dx,-ds),\qquad
F^3(x,y)=((ab-d)s+ad x,0).
\]
The first coordinate of \(F^2\) is strictly negative because \(d,x>0\). The displayed third iterate is in \(S\cup\{0\}\) or its next left iterate is in \(S\). Thus every orbit hits \(S\cup\{0\}\) within at most four steps. This argument also covers \(b=0\) and boundary equality cases.

**2. Exact returns.** For each \(r>0\),
\[
F(r,0)=(-br,-dr),\qquad F^2(r,0)=((ab-d)r,0).
\]
If \(d<ab\), the second point is in \(S\), with return time two and factor \(\kappa=ab-d\). If \(d=ab\), the second point is zero. If \(d>ab\), the second point lies strictly left and the third is \((a(d-ab)r,0)\in S\), with return time three and factor \(\kappa=a(d-ab)\). No positive-ray point is fixed, since its first image has second coordinate \(-dr<0\). Likewise, for \(d>ab\), the second image has negative first coordinate, so the resulting three-cycles are primitive.

**3. Stability and the entire periodic set.** The entrance argument gives a finite collection of affine branches for each of the first four iterates. Their operator norms are uniformly bounded over all initial points, by a constant depending only on \((a,b,d)\). Subsequently every orbit either has hit zero or makes consecutive ray returns of time \(\ell\in\{2,3\}\) and factor \(\kappa\). If \(0\le\kappa<1\), geometric contraction of these returns, together with the finitely many intermediate steps, yields \(\|F^n z\|\le C\rho^n\|z\|\) uniformly, including \(\kappa=0\) (when finite-time convergence holds). The inequalities \(\kappa<1\) amount exactly to \(d>ab-1\) on \(d<ab\), and \(d<ab+1/a\) on \(d>ab\). Since \(d>0\), these combine into the boxed open interval.

When \(\kappa=1\), the ray return is the identity, so every \(r>0\) yields a distinct primitive cycle of period two or three, according to its branch. These nonzero periodic rays rule out asymptotic stability of zero. Any other periodic point must be on one of these cycles, because an arbitrary periodic orbit reaches \(S\cup\{0\}\) after finitely many steps and therefore already includes a point of that set. If \(\kappa>1\), ray points arbitrarily near zero grow without bound, ruling out Lyapunov stability; by entrance and the return formula every orbit not eventually zero diverges in norm along successive returns (and hence is unbounded). This proves necessity, sufficiency, and the full periodic-orbit classification.

**4. Uniform sharp deadbeat time.** At \(d=ab\), every positive-ray point goes to zero in precisely two steps. The entrance argument gives a sharper bound in this case: for \(x>0\) and \(s>0\), the third iterate above becomes \((ad x,0)\in S\), rather than possibly entering the negative ray. All other cases reach \(S\cup\{0\}\) by the third step or sooner. Hence \(F^5\equiv0\). Taking \(z=(1,b/2)\) with \(b>0\), direct evaluation gives
\[
F^4 z=(-a^2b^2/2,-a^3b/2)\ne(0,0),
\]
so the uniform exponent five is best possible. At \((a,b,d)=(2,1,2)\), the two Jacobian matrices have spectra \(\{-2,0\}\) and \(\{(-1+i\sqrt7)/2,(-1-i\sqrt7)/2\}\), confirming their respective spectral radii \(2\) and \(\sqrt2\). This concludes the proof.

## Verification
A standalone Python standard-library script `verify.py` uses exact rational arithmetic to exercise the branch map and its return formulas, including both neutral continua and deadbeat parameter cases. Executing `python verify.py` checks 229 parameter triples against 361 rational initial states each, with no floating-point tolerances. These computations are sanity checks: the arbitrary-real-state and infinite-parameter statements are established by the preceding explicit case analysis, not by the finite test grid.

## Relationship to prior work
The setting is the zero-left-determinant two-dimensional border-collision normal form of Simpson, *The two-dimensional border-collision normal form with a zero determinant* (arXiv:2408.04790, first posted 2024-08-08). Its §4.1 explicitly leaves the switching value \(\mu=0\) outside its analysis of asymptotic stability; subsequent sections address \(\mu<0\) and \(\mu>0\). Its existing linear combinations of traces and determinants overlap with the elementary two-step factor used here, but the sharp global stability window, the two distinct neutral periodic-ray boundaries, and the exact global five-step collapse are not supplied by its stated off-border bifurcation results. Simpson's earlier work on switching-manifold stability (arXiv:1612.02932) provides broader theory for homogeneous maps but does not itself give these parameter identities; its two-dimensional illustrative analysis treats a different determinant regime. Simpson's 2026 first-return study (arXiv:2606.08901) studies a nonzero switching offset and repelling-focus return geometry, and does not cover this homogeneous negative-trace cone.

## Limitations
These conclusions require \(a>0\), \(b\ge0\), \(d>0\), the zero-offset homogeneous normal form, and zero left determinant. They are not asserted for the remaining trace/determinant sign combinations, other nonzero offsets, or nonlinear perturbations. The full phase portrait here includes unbounded orbits; no chaos claim is made. Literature comparisons cannot exclude an earlier equivalent classification stated in a different coordinate system. No independent mathematical audit has been performed.

## References
1. D. J. W. Simpson, *The two-dimensional border-collision normal form with a zero determinant*, arXiv:2408.04790 (first posted 2024-08-08), https://arxiv.org/abs/2408.04790; subsequent article, *SIAM Journal on Applied Dynamical Systems* 24 (2025), 2205–2245, doi:10.1137/24M1683548.
2. D. J. W. Simpson, *The stability of fixed points on switching manifolds of piecewise-smooth continuous maps*, arXiv:1612.02932 (first posted 2016-12-09), https://arxiv.org/abs/1612.02932.
3. D. J. W. Simpson, *One-dimensional first return maps for the two-dimensional border-collision normal form with a zero determinant*, arXiv:2606.08901 (2026), https://arxiv.org/abs/2606.08901.
