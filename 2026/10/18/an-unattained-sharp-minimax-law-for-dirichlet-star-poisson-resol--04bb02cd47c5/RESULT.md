# An unattained sharp minimax law for Dirichlet-star Poisson resolvents

## Finding
Fix an integer \(k\ge3\) and a total length \(L>0\). Among all compact metric stars with \(k\) strictly positive arm lengths summing to \(L\), with a Dirichlet condition at each leaf and a Kirchhoff condition at the center, the sharp \(L^\infty\)-Poisson-resolvent norms fill exactly the open interval
\[
\boxed{\left(\frac{L^2}{8(k-1)^2},\frac{L^2}{8}\right).}
\]
Neither endpoint is attained by a nondegenerate star. The lower endpoint is approached by shrinking one arm to length zero while equalizing the remaining \(k-1\) arms. The upper endpoint is approached by shrinking \(k-1\) arms while the remaining length approaches \(L\). This is an extremal statement about worst-case pointwise response, not about the integral of the torsion function.

For comparison, all-equal arms have norm \(L^2/(2k^2)\). The ratio of this symmetric norm to the sharp infimum is \(4(k-1)^2/k^2\), which tends to \(4\) as \(k\to\infty\). Thus symmetric allocation is not asymptotically minimax for this endpoint invariant.

## Assumptions and scope
Each arm \(i\) is an interval \([0,\ell_i]\) oriented from the common center to a Dirichlet leaf, with \(\ell_i>0\) and \(\sum_{i=1}^k\ell_i=L\). The generator is the positive Kirchhoff–Dirichlet Laplacian \(A=-\Delta\), acting as \(-u_i''\) with continuous common value \(u_i(0)\), terminal conditions \(u_i(\ell_i)=0\), and \(\sum_i u_i'(0)=0\). On continuous or bounded measurable real or complex forcing, its zero-energy Green inverse \(G=A^{-1}\) is positive and bounded from \(L^\infty\) to continuous functions. Norms and lengths use the unweighted arclength measure and edgewise second derivative without a factor of \(1/2\).

A length sequence is allowed to degenerate only when discussing limits; all actual stars in the theorem have strictly positive arm lengths. The two-arm case is simply a Dirichlet interval and has constant norm \(L^2/8\), explaining the restriction \(k\ge3\).

## Proof
**Step 1: exact torsion and resolvent norm.** Let \(v=G\mathbf1\), where \(\mathbf1\) is constant forcing. Uniqueness of the mixed Poisson boundary-value problem and the edge equation give
\[
v_i(x)=C+B_i x-\frac{x^2}{2},\qquad
C=\frac{L}{2\sum_{j=1}^k\ell_j^{-1}},\qquad
B_i=\frac{\ell_i}{2}-\frac{C}{\ell_i}.
\]
Indeed, every terminal condition is satisfied and the Kirchhoff flux identity is \(\sum_i B_i=L/2-C\sum_i\ell_i^{-1}=0\). Since \(C>0\) and \(B_i<\ell_i/2\), every positive stationary coordinate \(x=B_i\) lies inside its arm. Consequently,
\[
M(\boldsymbol\ell):=\max_{i,x}v_i(x)
=C+\frac12\max_{1\le i\le k}(B_i)_+^2.
\]
The maximum principle implies that \(G\) is positivity-preserving. Therefore \(\lvert Gf\rvert\le G\lvert f\rvert\le G\mathbf1=v\) for \(\|f\|_\infty\le1\), and equality is achieved by \(f=\mathbf1\). Hence \(M(\boldsymbol\ell)=\|G\|_{L^\infty\to L^\infty}\).

**Step 2: a length identity.** Solving the positive quadratic root \(0=C+B_i\ell_i-\ell_i^2/2\) yields
\[
\ell_i=B_i+\sqrt{B_i^2+2C},\qquad
L=\sum_{i=1}^k\sqrt{B_i^2+2C},
\qquad \sum_i B_i=0.
\]
Set \(t=\max\{0,B_1,\ldots,B_k\}\). Then \(2M=2C+t^2\) and each \(B_i\le t\).

**Step 3: strict universal lower bound.** For fixed \(C>0\) and \(t>0\), the vectors \((B_1,\ldots,B_k)\) satisfying \(\sum_i B_i=0\) and \(B_i\le t\) form a simplex. Since \(b\mapsto\sqrt{b^2+2C}\) is convex, the sum of those functions is at most its value at a simplex vertex, where \(k-1\) coordinates are \(t\) and one coordinate is \(-(k-1)t\). Therefore
\[
L\le(k-1)\sqrt{t^2+2C}+\sqrt{(k-1)^2t^2+2C}
<2(k-1)\sqrt{t^2+2C}=2(k-1)\sqrt{2M}.
\]
The second inequality is strict because \(k-1>1\) and \(C>0\). If \(t=0\), the flux sum forces every \(B_i=0\), and \(L=k\sqrt{2C}<2(k-1)\sqrt{2M}\) again. Rearrangement proves
\[
M>\frac{L^2}{8(k-1)^2}.
\]

**Step 4: strict universal upper bound.** If \(t>0\), take \(i\) with \(B_i=t\). Using the Euclidean triangle inequality on the \(k-1\) vectors \((B_j,\sqrt{2C})\) for \(j\ne i\) gives
\[
\begin{aligned}
L&=\sqrt{t^2+2C}+\sum_{j\ne i}\sqrt{B_j^2+2C}\\
&\ge\sqrt{t^2+2C}+\sqrt{t^2+2C(k-1)^2}
>2\sqrt{t^2+2C}=2\sqrt{2M}.
\end{aligned}
\]
The equality \(\sum_{j\ne i}B_j=-t\) was used, and the second inequality is strict for \(k\ge3\). If \(t=0\), then \(L=k\sqrt{2C}>2\sqrt{2M}\). Hence \(M<L^2/8\).

**Step 5: sharpness and complete range.** For the lower boundary set \(\ell_1=\varepsilon\) and \(\ell_2=\cdots=\ell_k=(L-\varepsilon)/(k-1)\). As \(\varepsilon\downarrow0\), the formula in Step 1 gives \(C\to0\) and the largest positive slope tends to \(L/(2(k-1))\). Thus \(M\to L^2/[8(k-1)^2]\). For the upper boundary set \(\ell_1=L-(k-1)\varepsilon\) and the other \(k-1\) arms equal to \(\varepsilon\). Here \(C\to0\), the largest positive slope tends to \(L/2\), and \(M\to L^2/8\). The open positive-length simplex is connected and the explicit formula in Step 1 is continuous on it. Its image is therefore an interval. The strict bounds and the two limiting families prove that its image is precisely the open interval claimed.

## Verification
The standalone `check_star.py` independently reconstructs the Kirchhoff Poisson problem by dense linear finite-element assembly and a separately sampled shooting solution. With a fixed random seed it checks 1,000 random metric stars across four arm counts; 32 finite-element solutions; and 24 sharp-boundary degenerations, as well as the equal-arm identities. The checks passed in the development environment. The analytic proof above covers every real positive length vector and is not inferred from finite experiments. The code uses Python 3 and NumPy and may be run with `python check_star.py`.

## Relationship to prior work
Frank–Kovařík (2011) study heat semigroups on metric trees and their geometry-dependent kernel bounds, but their main theorems address infinite symmetric trees and do not imply a compact Dirichlet-star endpoint resolvent allocation. Colladay–Kaganovskiy–McDonald (2016) study torsional rigidity and heat content of isospectral quantum graphs, not this fixed-length sharp \(L^\infty\)-norm range. Mugnolo–Plümer (2021 preprint) provide the general edgewise quadratic torsion description, arbitrary-length stower torsional-*integral* formula and an equilateral star; these classical torsion ingredients are not claimed as new. The result here is instead the sharp two-ended **pointwise** allocation range and nonattainment, derived by convex slope geometry. The known integral extremal inequalities do not give this lower endpoint or characterize the norm image.

## Limitations
The theorem is for unweighted second derivatives, Kirchhoff matching and all Dirichlet leaves on a star with at least three positive edges. It does not characterize all sequences approaching either boundary, establish uniqueness of optimal *degenerate* allocations, or optimize the integral torsional rigidity or other \(L^p\) norms. The extrema are not attained in the positive-length class; the limiting statements must not be misread as constructions of admissible zero-length edges. Searches cannot establish definitive historical priority; an earlier equivalent formula under maximum torsion, Brownian exit-time, or Green potential terminology remains possible. No independent mathematical review has been performed.

## References
- R. L. Frank and H. Kovařík, *Heat kernels of metric trees and applications*, arXiv:1108.6145, first public version 2011-08-31.
- D. Colladay, L. Kaganovskiy and P. McDonald, *Torsional Rigidity, Isospectrality and Quantum Graphs*, arXiv:1607.05752, first public version 2016-07-19.
- D. Mugnolo and M. Plümer, *On torsional rigidity and ground-state energy of compact quantum graphs*, arXiv:2112.00782 (2021 preprint), especially Example 2.4, Example 3.10 and Section 4.
