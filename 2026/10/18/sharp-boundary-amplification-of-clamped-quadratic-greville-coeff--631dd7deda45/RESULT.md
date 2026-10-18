# Sharp boundary amplification of clamped quadratic Greville coefficient recovery

## Finding
For each integer \(n\ge2\), take the open (clamped) uniform knot vector
\[
(0,0,0,1,2,\ldots,n-1,n,n,n)
\]
on \([0,n]\). Let \(N_j\), \(0\le j\le n+1\), be the normalized quadratic B-splines, and \(\xi_i=(t_{i+1}+t_{i+2})/2\) their Greville sites, with knot-vector indices beginning at zero. Let \(A_n=(N_j(\xi_i))_{0\le i,j\le n+1}\). The coefficient-recovery map takes sampled data \(y\) to spline coefficients \(c=A_n^{-1}y\). Set \(q=3-2\sqrt2\).

The exact sharp sup-norm amplification for every \(n\ge2\) is
\[
\boxed{K_n=\|A_n^{-1}\|_{\ell^\infty\to\ell^\infty}
=2+(\sqrt2-1)\frac{1+q^{n-1}}{1-q^n}.}
\]
The only maximizing coefficient positions are \(j=1\) and \(j=n\); the endpoint coefficients \(j=0,n+1\) have row norm one. Alternating bounded sample data \(y_j=(-1)^j\) attain \(K_n\). Consequently \(K_2=5/2\), \(K_n\) decreases strictly in \(n\), and
\[
\boxed{\sup_{n\ge2}K_n=\frac52,\qquad
\lim_{n\to\infty}K_n=1+\sqrt2,}
\]
with exact positive finite-length correction
\[
\boxed{K_n-(1+\sqrt2)
=(\sqrt2-1)(1+q)\frac{q^{n-1}}{1-q^n}.}
\]
For comparison, the pure-cardinal degree-two Greville Toeplitz matrix \(T_m\) of order \(m\ge2\), with diagonal \(3/4\) and adjacent entries \(1/8\), has \(\|T_m^{-1}\|_\infty<2\) at every finite order and approaches \(2\) as \(m\to\infty\). Thus clamped endpoint repetitions produce a persistent exact boundary coefficient-sensitivity excess of \(\sqrt2-1\) in the large-system limit.

## Assumptions and scope
All knots and Greville sites are as defined above, with unit spacing (arbitrary positive uniform spacing is equivalent by rescaling). Norms act on real or complex data vectors in the ordinary maximum-entry norm. The claim concerns recovery of spline *coefficients* from Greville samples, not the uniform norm of the reconstructed spline as a function. The B-spline basis is normalized to form a partition of unity. There is no assumption on the smoothness of the sampled data.

## Proof
Cox–de Boor recursion at the Greville sites gives the following complete nonzero-entry stencil, with \(0\le i,j\le n+1\): the rows \(i=0\) and \(i=n+1\) are the corresponding identity rows; row \(i=1\) has \((A_{1,0},A_{1,1},A_{1,2})=(1/4,5/8,1/8)\); row \(i=n\) has \((A_{n,n-1},A_{n,n},A_{n,n+1})=(1/8,5/8,1/4)\); and every row \(2\le i\le n-1\) has entries \(1/8,3/4,1/8\) in columns \(i-1,i,i+1\). These prescriptions also cover \(n=2\), when the interior range is empty.

Let \(D=\operatorname{diag}((-1)^j)\) and \(M=DA_nD\). Every off-diagonal entry of \(M\) is nonpositive, each diagonal is positive, and each row is strictly diagonally dominant. Hence \(M\) is a nonsingular \(M\)-matrix with entrywise nonnegative inverse. Since \(A_n^{-1}=DM^{-1}D\), its absolute row sums are exactly the entries of \(z=M^{-1}\boldsymbol1\). This also proves attainability by data \(D\boldsymbol1\).

The first and last equations give \(z_0=z_{n+1}=1\). Multiplying the other equations by eight yields
\[
5z_1-z_2=10,\qquad
-z_{i-1}+6z_i-z_{i+1}=8\quad(2\le i\le n-1),\qquad
5z_n-z_{n-1}=10.
\]
The characteristic equation of the homogeneous interior recurrence has roots \(3\pm2\sqrt2\), which are \(q\) and \(q^{-1}\). Direct substitution and reflection symmetry give the unique solution
\[
z_j=2+(\sqrt2-1)\frac{q^{j-1}+q^{n-j}}{1-q^n},\quad 1\le j\le n.
\]
To check the boundary equation explicitly, write \(z_j=2+C(q^{j-1}+q^{n-j})\). Then \(5z_1-z_2=8+C((5-q)+(5q-1)q^{n-2})\); since \(q^2-6q+1=0\), the parenthesis equals \((1-q)(1-q^n)/q\). Thus \(C=2q/((1-q)(1-q^n))=(\sqrt2-1)/(1-q^n)\), including \(n=2\). The right boundary follows by symmetry.

The sequence \(j\mapsto q^{j-1}+q^{n-j}\) is strictly convex and symmetric about \((n+1)/2\), so its only maxima among \(1\le j\le n\) are at \(1,n\) (both entries for \(n=2\)). Their row sums exceed the endpoint value one. The displayed formula for \(K_n\) follows. Because both \(q^{n-1}\) and \(q^n\) decrease strictly with \(n\), the ratio \((1+q^{n-1})/(1-q^n)\) decreases strictly. Elementary rearrangement gives the exact correction and the sharp uniform bound at \(n=2\).

Finally \(T_m\) is symmetric strictly diagonally dominant. Its checkerboard sign conjugate \(S_m\) has row sums at least \(1/2\), with strict excess at its boundary rows. Since \(S_m^{-1}\) is entrywise positive, the maximum principle gives \(S_m^{-1}\boldsymbol1<2\boldsymbol1\), so \(\|T_m^{-1}\|_\infty<2\). The central rows tend to two by the explicit infinite-line inverse kernel \(\sqrt2(-q)^{|i-j|}\), whose absolute row sum is \(\sqrt2(1+q)/(1-q)=2\). The boundary excess is therefore \((1+\sqrt2)-2=\sqrt2-1\).

## Verification
The standalone standard-library script `verify.py` constructs the clamped quadratic B-spline collocation matrix directly by recursive basis evaluation at rational Greville sites. It inverts independent tridiagonal systems in exact rational arithmetic and checks every inverse entry's checkerboard sign, all row norms, and both sharp maximizing positions for each \(2\le n\le40\). Ninety-digit decimal arithmetic checks the radical closed forms and finite-length corrections; the cardinal Toeplitz strict bound is also checked on finite test orders. The script gives 53,171 assertions. These finite checks are diagnostics and not the proof of universal claims.

## Relationship to prior work
Novaković, Singer and Singer (arXiv:1004.4014, §§1–3) analyze the *cardinal simple-knot Toeplitz* Greville matrices and their spectral condition numbers. The matrix here instead has *repeated endpoint knots*, non-Toeplitz boundary rows, and concerns the sharp induced maximum-entry norm of coefficient recovery. Classical spline interpolation theory supplies the B-spline recurrence, invertibility and boundedness background, while the full finite-length formula and sharp boundary localization are the comparison being assessed. The closest broader work by Marsden on quadratic interpolation at knot averages is relevant but its full text was not accessible in this examination; equivalence is a residual priority risk.

## Limitations
No statement is made about nonuniform meshes, higher spline degree, interpolation-function Lebesgue constants, operator norms on \(L^p\), or optimal knot placement. This is an elementary exact family whose significance is a natural, persistent boundary stability penalty for clamped quadratic coefficient recovery. Earlier equivalent formulas in the full quadratic-spline interpolation literature cannot be ruled out absolutely without additional bibliographic review.

## References
- V. Novaković, S. Singer, S. Singer, *Estimates for the Spectral Condition Number of Cardinal B-Spline Collocation Matrices (Long version)*, arXiv:1004.4014, first posted 2010-04-22. Sections 1–3 and Toeplitz matrix (7).
- M. J. Marsden, *Linear and quadratic spline interpolation at knot averages*, Journal of Approximation Theory 38 (1983), 201–208, DOI:10.1016/0021-9045(83)90128-4. Abstract available; full text not inspected.
- C. de Boor, *On bounding spline interpolation*, Journal of Approximation Theory 14 (1975), 191–203, DOI:10.1016/0021-9045(75)90055-6. Abstract and later contextual discussion only.
