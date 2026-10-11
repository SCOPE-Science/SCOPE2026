# Sharp Gabor frame bounds and quadratic collapse for the hat spline at half-density

## Finding
For \(g(t)=(1-|t|)_+\), \(3/2\le b\le 7/4\), and \(a=1/(2b)\), the exact optimal bounds of the associated Gabor system are
\[
A(b)=\frac{2(7/4-b)^2}{b^3},\qquad
B(b)=\frac{(3b-2)^2+(4b-4)^2}{b^3}.
\]
The optimal lower bound is zero at the endpoint \(b=7/4\), and positive elsewhere in the indicated interval. Consequently the sharp ratio on \(3/2\le b<7/4\) is
\[
\frac{B(b)}{A(b)}=\frac{(3b-2)^2+(4b-4)^2}{2(7/4-b)^2}
\sim\frac{313}{32}(7/4-b)^{-2}\quad\text{as }b\uparrow7/4.
\]
Both extrema occur at explicit Zak-transform fibers, specified below.

## Assumptions and scope
Take the real hat spline \(g(t)=\max\{1-|t|,0\}\). For real \(b\) in the closed interval \([3/2,7/4]\), put \(a=1/(2b)\) and define
\[
\mathcal G(g,a,b)=\{e^{2\pi imb t}g(t-na):m,n\in\mathbb Z\}\subset L^2(\mathbb R).
\]
The optimal bounds are the greatest possible lower and least possible upper constants in
\[
A\|f\|_2^2\le\sum_{m,n\in\mathbb Z}|\langle f,e^{2\pi imb(\cdot)}g(\cdot-na)\rangle|^2\le B\|f\|_2^2
\]
for every \(f\in L^2(\mathbb R)\). At the nonframe endpoint the optimal lower constant is understood as zero. The parameter \(b\) is modulation spacing, not the physical spline support width.

## Proof
**Step 1: exact fiberization and normalization.** Use the unitary Zak transform at \(\lambda=1/b\):
\[
Z_{1/b}g(x,\gamma)=\frac1{\sqrt b}\sum_{k\in\mathbb Z}g((x-k)/b)e^{2\pi ik\gamma}
=b^{-3/2}\sum_{k\in\mathbb Z}(b-|x-k|)_+e^{2\pi ik\gamma}.
\]
The Zibulski–Zeevi characterization for \(ab=1/2\) (one row and two columns, with the normalization above) identifies the **optimal**, rather than merely sufficient, bounds as the essential minimum and maximum over the unit torus of
\[
\mathcal H_b(x,\gamma)=|Z_{1/b}g(x,\gamma)|^2+|Z_{1/b}g(x+1/2,\gamma)|^2.
\]
Since \(g\) is continuous and compactly supported, the fiber is continuous and these are ordinary global extrema. Quasiperiodicity and swapping the two summands make \(\mathcal H_b\) half-periodic in \(x\), so it suffices to study \(0\le x\le1/2\).

**Step 2: short, exact Laurent polynomials.** Put \(z=e^{2\pi i\gamma}\), \(U=2-b\), and \(L=b-3/2\). Throughout the range, \(0\le L\le U\le1/2\). Define \(P=b^{3/2}Z_{1/b}g\). For \(0\le x\le1/2\), direct enumeration of nonzero integer translates gives
\[
\begin{aligned}
P_x(z)&=(b-1-x)z^{-1}+(b-x)+(b-1+x)z+(x-U)_+z^2,\\
P_{x+1/2}(z)&=(L-x)_+z^{-1}+(b-1/2-x)+(b-1/2+x)z+(x+L)z^2.
\end{aligned}
\]
Here \((t)_+=\max\{t,0\}\). These formulae remain valid at support endpoints, where a listed coefficient can be zero.

**Step 3: the exact lower envelope.** If \(x\ge U\), the four consecutive Laurent coefficients of \(P_x\), denoted \(\alpha,\beta,\chi,\delta\), satisfy \(\beta=\alpha+1\) and \(\chi=\delta+1\). Hence
\[
zP_x(z)=(1+z)(\alpha+z+\delta z^2),
\]
so \(P_x(-1)=0\). If \(x<U\), only three coefficients remain and their middle coefficient dominates the other two by the positive quantity \(U-x\). The reverse triangle inequality gives \(|P_x(z)|\ge U-x\), with equality at \(z=-1\). Thus, in every case,
\[
\min_{|z|=1}|P_x(z)|=|P_x(-1)|=(U-x)_+.
\]
Similarly, if \(x\le L\), the four coefficients of \(P_{x+1/2}\) satisfy the same relations and the polynomial vanishes at \(z=-1\). If \(x>L\), the coefficient at \(z\) exceeds the sum of the coefficients at \(1\) and \(z^2\) by \(x-L\). Hence
\[
\min_{|z|=1}|P_{x+1/2}(z)|=|P_{x+1/2}(-1)|=(x-L)_+.
\]
Crucially, **both minima occur at the same phase** \(z=-1\). Consequently
\[
\min_{\gamma}\mathcal H_b(x,\gamma)=b^{-3}\left((U-x)_+^2+(x-L)_+^2\right).
\]
Because \(L\le U\), this sum is minimized at \(x=(L+U)/2=1/4\), with minimum \((U-L)^2/2\). As \(U-L=7/2-2b\), this proves \(A(b)=2(7/4-b)^2/b^3\), attained at \((x,\gamma)=(1/4,1/2)\). At \(b=7/4\) both Laurent polynomials vanish at that fiber, so the optimal lower bound is exactly zero.

**Step 4: the exact upper envelope.** Every Laurent coefficient above is nonnegative. The ordinary triangle inequality therefore gives \(|P_x(z)|\le P_x(1)\) and \(|P_{x+1/2}(z)|\le P_{x+1/2}(1)\) simultaneously, with equality at \(z=1\). Direct summation yields the piecewise affine functions
\[
P_x(1)=\begin{cases}3b-2-x,&x\le U,\\4b-4,&x\ge U,\end{cases}
\qquad
P_{x+1/2}(1)=\begin{cases}4b-4,&x\le L,\\3b-5/2+x,&x\ge L.\end{cases}
\]
On \([0,L]\), the first function decreases and the second is constant; hence the squared sum is maximized at \(x=0\). On \([U,1/2]\), the second increases and the first is constant; hence the maximum is at \(x=1/2\). On \([L,U]\), the squared sum is a convex quadratic in \(x\), so its maximum is at an endpoint, never exceeding the values at \(0\) or \(1/2\) already found. Both outer endpoints give
\[
\max_{x,\gamma}\mathcal H_b(x,\gamma)=b^{-3}((3b-2)^2+(4b-4)^2)=B(b).
\]

**Step 5: frame criterion and conditioning.** The Zak characterization shows positivity of the exact lower bound is equivalent to the frame property. Dividing the proven expressions gives the exact condition-number formula. At \(b=7/4\), its numerator before division by two tends to \((13/4)^2+3^2=313/16\), giving the coefficient \(313/32\) in the stated quadratic divergence. No extrapolation from finite computations is used.

## Verification
The self-contained `verify.py` checks all piecewise Fourier coefficients against direct lattice sums at rational parameters, verifies the exact \(\gamma=0\) and \(\gamma=1/2\) envelopes, and compares sampled phase fibers with the analytic bounds. Run with `python3 verify.py`. These finite tests are supplementary; Steps 1–5 above prove the assertions for all real parameters in the specified interval.

## Relationship to prior work
Hasannasab and Lemvig (arXiv:2609.13116v1, September 2026) characterize Zak zeros and identify integer-oversampled hat-spline frame sets. Stangl and Frederick (arXiv:2609.00481v2, September 2026), Theorems 3 and 4 and Section 3, give an exact frame/nonframe criterion along \(ab=1/q\) via the same fiberization. Neither inspected assertion provides the **optimal lower and upper bound functions** or their sharp quadratic conditioning asymptotic on the continuous \(q=2\) subinterval. The earlier criterion does already imply that these parameters are frames in the interior and fail at the obstruction; the contribution here is the quantitative sharp spectrum and extremal fibers, not a rediscovery of that membership result. Christensen–Kim–Kim (2016) also give qualitative frame-set regions and examples.

## Limitations
The result concerns the specific nonnegative hat window, exact half-density lattice, and \(3/2\le b\le7/4\), not other orders of splines or other rational oversampling curves. It does not claim the prior qualitative frame criterion as novel. A contemporaneous Zak-zero manuscript was only partly available in accessible text; its uninspected portions and older Gram-matrix estimates remain possible sources of an equivalent pre-existing bound. The proof and finite checks constitute no independent audit.

## References
1. M. Hasannasab and J. Lemvig, *The zero set of the Zak transform of B-splines with applications to Gabor frames*, arXiv:2609.13116v1 (first submitted September 11, 2026). https://arxiv.org/abs/2609.13116
2. A. Stangl and C. Frederick, *The frameset of the second-order B-spline along \(ab=1/q\)*, arXiv:2609.00481v2 (September 2026), Theorems 3–4 and Sections 2–3. https://arxiv.org/html/2609.00481v2
3. O. Christensen, H. O. Kim and R. Y. Kim, *On the Gabor frame set for compactly supported continuous functions*, J. Inequal. Appl. (2016), article 94. https://doi.org/10.1186/s13660-016-1021-4
4. M. Zibulski and Y. Y. Zeevi, *Analysis of multiwindow Gabor-type schemes by frame methods*, Appl. Comput. Harmon. Anal. 4 (1997), 188–221.
