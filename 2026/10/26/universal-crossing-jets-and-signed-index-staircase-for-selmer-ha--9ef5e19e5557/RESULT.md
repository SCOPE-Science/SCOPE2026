# Universal crossing jets and signed-index staircase for Selmer harmonic trinomials

## Finding
Fix integers \(n>k\ge1\), signs \(\varepsilon,\delta\in\{+1,-1\}\), and define the real-parameter harmonic trinomial
\[
H_s(z)=z^n+\varepsilon\overline z^{\,k}+\delta s,\qquad s>0.
\]
Write \(g=\gcd(n,k)\), \(L=(n-k)/g\), \(n_0=n/g\), and \(\chi=0\) when \(\varepsilon=1\) or \(\chi=\pi\) when \(\varepsilon=-1\). Define the finite list of real levels
\[
\sigma_q=-2\delta\cos\left(\frac{2\pi q+n_0\chi}{L}\right),\qquad q=0,\ldots,L-1.
\]
Unit-circle roots occur **exactly** at positive levels \(s=\sigma_q\). Every such root has positive Jacobian, and the unique real-analytic local zero branch \(z(s)\) satisfies, with \(\rho(s)=\log|z(s)|\),
\[
\boxed{\rho'(s_0)=\frac{s_0}{2(n+k)},\qquad
\rho''(s_0)=\frac{(n+k)^2-\tfrac12(n^2+nk+k^2)s_0^2}{(n+k)^3}.}
\]
In particular the roots always cross outward as \(s\) increases; their logarithmic radial acceleration changes sign exactly at
\[
s_*=\frac{\sqrt2(n+k)}{\sqrt{n^2+nk+k^2}},\qquad \sqrt2<s_*<\sqrt{8/3}.
\]
For \(s>0\) not equal to any positive level, the **signed**, not unsigned, disk-zero count is
\[
\boxed{\operatorname{wind}(H_s(e^{it}),0)=g\sum_{q=0}^{L-1}\mathbf 1_{\{\sigma_q>s\}}.}
\]
A wall in \((0,2)\) has \(2g\) distinct unit roots; a wall at \(2\), if present, has \(g\). The signed count drops by precisely these values at each wall.

## Assumptions and scope
All exponents are positive integers with \(n>k\), both signs are independent, and \(s\) ranges over the positive real line. A zero branch is defined only in a neighborhood of a specified unit root at a wall. The Jacobian is \(\lvert (H_s)_z\rvert^2-\lvert (H_s)_{\bar z}\rvert^2\). The winding number is the winding of the parameterized boundary image about zero; it agrees with the sum of orientation signs of interior zeros when zero is absent from the boundary, and is not generally the number of distinct interior roots.

## Proof
**(1) Boundary walls.** At a unit root set \(u=z^n\) and \(v=\varepsilon z^{-k}\). They are unit complex numbers with \(u+v=-\delta s\) real and nonzero. Necessarily \(v=\bar u\); hence \(uv=1\), i.e. \(z^{n-k}=\varepsilon\). Conversely, if \(z^{n-k}=\varepsilon\) and \(-2\delta\operatorname{Re}(z^n)=s>0\), then \(u+v=-\delta s\) and \(H_s(z)=0\). For \(z=\exp(i(\chi+2\pi j)/(n-k))\), the phases \(z^n\) run through the list \(\exp(i(2\pi q+n_0\chi)/L)\), each repeated exactly \(g\) times because \(\gcd(n_0,L)=1\). This proves the wall list. Conjugate phase pairing implies that every interior wall \(0<s<2\) has \(2g\) roots and the limiting wall \(s=2\) has \(g\); distinct levels could arise from one conjugate pair but not from two distinct cosine pairs.

**(2) Analytic zero branches and first derivative.** At \(|z|=1\), the harmonic Jacobian is \(J=n^2-k^2>0\), so the real implicit-function theorem yields a unique real-analytic branch \(z(s)\). Put \(N=n+k\), \(w=z'(s)/z(s)\). Differentiating \(H_s(z(s))=0\) yields \(nu w+kv\bar w=-\delta\). At the crossing, \(u=\bar v\) and \(|v|=1\), whence uniquely \(w=-\delta v/N\). Since \(2\operatorname{Re}v=-\delta s_0\), it follows that \(\rho'(s_0)=\operatorname{Re}w=s_0/(2N)>0\). Moreover \(\frac{d}{ds}\arg z(s)|_{s_0}=\delta\operatorname{Im}(u)/N\) and \(|w|=1/N\).

**(3) Second derivative.** Because \(u'=nu w\) and \(v'=kv\bar w\), a second differentiation gives
\[
nu w'+kv\overline{w'}=-n^2u w^2-k^2v\bar w^2.
\]
Here \(w'=\frac d{ds}(z'/z)\). At the crossing use \(uv=1\), \(w=-\delta v/N\), \(\bar w=-\delta u/N\). The right side becomes \(-(n^2v+k^2u)/N^2\). Solving this invertible real-linear equation and its conjugate yields the exact complex identity
\[
w'(s_0)=\frac{nk-(n^2+nk+k^2)v^2}{N^3}.
\]
Taking real parts and using \(\operatorname{Re}(v^2)=s_0^2/2-1\) proves the two-jet formula. The numerator vanishes at the displayed \(s_*\); since \(0<k<n\), the strict threshold bounds follow from \(1<(n+k)^2/(n^2+nk+k^2)<4/3\).

**(4) The global signed index.** The boundary image cannot hit zero except at the finitely many levels above. For \(s>2\), \(\lvert z^n+\varepsilon\bar z^k\rvert\le2<s\) on the circle, so its winding number is zero. On increasing \(s\) through a single level, every associated root is simple, has positive Jacobian, and crosses transversely outward by step (2). The winding number therefore decreases by the exact number of crossing roots. Downward induction from \(s>2\) yields the indicator sum for every non-wall \(s>0\). This also proves that no unseen changes of index occur.

**(5) A single family exhibits both curvature signs.** For \(n=9\), \(k=1\), \(\varepsilon=1\), \(\delta=-1\), the only positive walls are \(\sqrt2\) with two roots and \(2\) with one. The signed index on successive positive parameter intervals is \(3,1,0\). The corresponding second derivatives of log radius are \(9/1000>0\) at \(\sqrt2\) and \(-41/500<0\) at \(2\). Thus the sign transition is realized, not merely formal.

## Verification
The proof consists of exact algebra, elementary root-of-unity counting, and an orientation-preserving transverse-crossing argument. The expressions can be checked by substituting \(u=\bar v\), \(uv=1\), and \(\operatorname{Re}v=-\delta s_0/2\) in the twice-differentiated harmonic equation. Direct substitution in the example gives \(9/1000\) and \(-41/500\). A standalone computational diagnostic verifies phase multiplicities, displayed rational values and representative winding changes; it is supplementary and not used as an exhaustive proof for infinite \(n,k\).

## Relationship to prior work
Barrera, Barrera and Navarrete (2026) classify unit-circle roots of the fixed-coefficient family with \(s=1\) and provide the natural motivating question. Barrera, Campa and Navarrete (2026) study general harmonic-trinomial parameter spaces and reproduce stronger general Bohl root-count formulas; the signed-index staircase alone is not claimed to supersede that count theory. Brilleslyper and collaborators (2020) vary the **anti-analytic** coefficient, unlike the constant coefficient varied here. The asserted contribution is the uniform exact radial two-jet at all positive unit-circle crossings and its acceleration threshold, integrated with the signed-boundary-index changes.

## Limitations
No claim is made about total unsigned interior zero counts, root branches away from the local wall neighborhoods, non-real coefficient paths, general harmonic polynomials, or global analytic continuation. The two-jet concerns \(\log|z(s)|\), not Euclidean radial second acceleration. The threshold is a continuous parameter threshold; the discrete set of walls for fixed exponents need not hit it. Related earlier root-count and parameter-space results could imply portions of the indexing statement; a historical unindexed formula for the local two-jet cannot be ruled out. The result has undergone only self-review, not independent validation.

## References
1. G. Barrera, W. Barrera and J. P. Navarrete, *Unimodular Zeros of Selmer's Harmonic Trinomials*, arXiv:2610.22132v1 (first posted 2026-10-15), https://arxiv.org/html/2610.22132v1.
2. W. Barrera, L. Campa and J. P. Navarrete, *On the Parameter Spaces of Harmonic Trinomial Equations*, arXiv:2602.11296v1 (first posted 2026-02-11), https://arxiv.org/html/2602.11296v1.
3. M. Brilleslyper, J. Brooks, M. Dorff, R. Howell and L. Schaubroeck, *Zeros of a one-parameter family of harmonic trinomials*, Proc. Amer. Math. Soc. Ser. B 7 (2020), 82–90, https://doi.org/10.1090/bproc/51.
