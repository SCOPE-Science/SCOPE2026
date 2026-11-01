# Corner-deletion instability and dual extremizers for affine least squares on Boolean cubes

## Finding
For every integer \(d\ge2\), remove one vertex from the Boolean cube \(\{-1,1\}^d\), equip the remaining \(2^d-1\) points with uniform probability, and let \(P_d\) be the orthogonal \(L^2\) projector onto restrictions of real affine functions. Put
\[
M=2^d,\qquad C_d=\binom{d}{\lfloor d/2\rfloor},\qquad q_d=d-(-1)^d.
\]
The exact operator norm is
\[
\boxed{\|P_d\|_{\ell^\infty\to\ell^\infty}
=\frac{(d+1)C_d}{M}+
\frac{(d-1)\big(q_d C_d/M-1\big)}{M-d-1}.}
\]
For \(d\ge3\), the unique maximizing evaluation-point orbits are the vertices at Hamming distance \(1\) or \(d\) from the missing corner. Every corresponding kernel-row sign function attains the norm. At \(d=2\), the projector is the identity on the three remaining points.

The full-cube affine projection norm is \((d+1)C_d/M\). Thus deleting just one corner **strictly increases** the norm for every \(d\ge3\), but decreases it at \(d=2\). The increase satisfies
\[
\|P_d\|-\frac{(d+1)C_d}{M}
\sim \sqrt{\frac{2}{\pi}}\,\frac{d^{3/2}}{2^d}
\qquad(d\to\infty).
\]
For data constrained by \(0\le f\le1\), the exact greatest negative projected output magnitude equals \((\|P_d\|-1)/2\). All formulas are attained by explicit sign or indicator inputs.

## Assumptions and scope
One vertex may be removed arbitrarily: cube sign-flips carry it to \(e=(1,\ldots,1)\). Write \(X_d=\{-1,1\}^d\setminus\{e\}\). The projector is formed using uniform counting probability on \(X_d\); because the weights are equal, its matrix also equals the unnormalized least-squares hat matrix. Norms are the supremum norm on \(X_d\), not on the continuous cube or on a product probability law. The affine span has dimension \(d+1\), because \(2^d>d+1\) for \(d\ge2\).

## Proof
**1. Exact kernel under one missing design row.** Let \(\phi(x)=(1,x_1,\ldots,x_d)^{\mathsf T}\), \(m=d+1\), and \(M=2^d\). The full-cube Gram matrix is \(MI_m\). Removing \(e\) produces \(G=MI_m-\mathbf1\mathbf1^{\mathsf T}\), where \(\mathbf1\in\mathbb R^m\). Sherman--Morrison gives
\[
G^{-1}=\frac1M\left(I_m+\frac{\mathbf1\mathbf1^{\mathsf T}}{M-m}\right).
\]
The projection matrix \(K\) therefore has entries, for \(x,y\in X_d\),
\[
K(x,y)=\frac{1+x\cdot y}{M}
+\frac{(1+\sum_i x_i)(1+\sum_i y_i)}{M(M-m)}.
\]
It is symmetric, idempotent and satisfies \(\sum_{y\in X_d}K(x,y)=1\). Hence its \(\ell^\infty\)-norm is the maximum absolute row sum, with each row norm attained by \(f(y)=\operatorname{sgn}K(x,y)\) (arbitrary sign at a zero).

**2. The rank-one correction does not reverse a nonzero full-cube kernel sign.** Let \(p=1+x\cdot y\), \(t_x=1+\sum_i x_i\), and \(t_y=1+\sum_i y_i\). Since both vertices differ from \(e\), \(|t_x|,|t_y|\le d-1\). The numerator of \(K(x,y)\) has sign of \((M-m)p+t_xt_y\). For \(d\ge4\), \(M-m>(d-1)^2\). For \(d=3\), a nonzero \(p\) has magnitude at least \(2\), which again prevents reversal; for \(d=2\), equality may occur but no strict reversal does. A zero \(p\) can occur only for odd \(d\).

**3. Hamming-row formulas.** Suppose \(x\) has \(k\in\{1,\ldots,d\}\) negative coordinates, put \(t=m-2k\), and let \(C=C_d\). Under the substitution \(z_i=x_i y_i\), direct binomial counting, with \(\operatorname{sgn}(0)=0\), yields
\[
\sum_{z\in\{-1,1\}^d}\operatorname{sgn}(1+\sum_i z_i)
=\sum_z z_j\operatorname{sgn}(1+\sum_i z_i)=C
\quad(1\le j\le d),
\]
and
\[
\frac1M\sum_z|1+\sum_i z_i|=\frac{mC}{M}=:B_d.
\]
The correction summed over the nonzero full-cube rows is consequently \(Ct^2/[M(M-m)]\). The fictitious missing-column kernel is \(K(x,e)=t/(M-m)\), so it contributes \(|t|/(M-m)\), which must be subtracted.

If \(d\) is even, there are no full-kernel zeros and the exact row norm is
\[
F_d(k)=B_d+\frac{Ct^2/M-|t|}{M-m}.
\]
If \(d\) is odd, there are \(C\) full-kernel zeros. Define
\[
H_d(k)=\sum_{\substack{z\in\{-1,1\}^d\\\sum_i z_i=-1}}
\left|1+\sum_i x_i z_i\right|.
\]
The exact row norm is
\[
F_d(k)=B_d+\frac{Ct^2/M-|t|+|t|H_d(k)/M}{M-m}.
\]
These identities include the omitted-column correction and are valid for every allowed \(k\).

**4. Exact localization of maximizing rows.** For even \(d\), set \(a=|m-2k|\), so \(1\le a\le d-1\). Subtracting the preceding row formula from its value at \(a=d-1\) yields
\[
F_{d,\max}-F_d(k)=
\frac{(d-1-a)\big(C(d-1+a)/M-1\big)}{M-m}.
\]
The central-binomial inequality \(Cd/M\ge1\) holds for every even \(d\ge2\), and it is strict for \(d\ge4\). Therefore the maximizing rows are precisely \(k=1,d\) for \(d\ge4\); at \(d=2\), both available rows have norm one.

For odd \(d\), put \(s=\min(k,m-k)\) and \(a=m-2s=|t|\). On the zero shell \(\sum_i z_i=-1\), if \(S\) is the set of the \(k\) negative coordinates of \(x\), then
\[
\left|1+\sum_i x_i z_i\right|
=2\left|\sum_{i\in S}z_i\right|
\le2\min(k,m-k)=2s.
\]
Consequently \(H_d(k)\le2Cs\). Substitution gives
\[
F_d(k)\le B_d+
\frac{a\big(mC/M-1\big)}{M-m}
\le B_d+\frac{(d-1)\big(mC/M-1\big)}{M-m}.
\]
Since \(mC/M>1\) for odd \(d\ge3\), the last bound is strict unless \(k=1\) or \(k=d\). For both endpoint values, the zero-shell bound is attained, and therefore both rows attain this common maximum. Combining the two parities gives the boxed formula, with \(q_d=d-1\) for even \(d\) and \(q_d=d+1\) for odd \(d\).

**5. Sign inputs, positivity defect, and dimension asymptotics.** For a maximizing row, taking its sign as input realizes \(\sum_y|K(x,y)|\). Because its coefficients sum to one, the total magnitude of negative coefficients is exactly \((\|P_d\|-1)/2\); selecting the indicator of those negative coefficients gives the lowest possible output from a \([0,1]\)-valued input. The exact full-cube norm is \(B_d=mC/M\). The odd formula has a positive defect since \(mC/M>1\). For even \(d\ge4\), the inequality \((d-1)\binom{d}{d/2}>2^d\) holds at \(d=4\) and persists under increasing \(d\) by two, because the ratio of its left-to-right sides at successive even dimensions is \((d+1)^2/((d+2)(d-1))>1\). Thus the even deletion defect is positive as well; \(d=2\) instead gives a negative defect of \(-1/2\). Finally, Stirling's formula \(C/M\sim\sqrt{2/(\pi d)}\) gives the stated exponentially small, sharp deletion defect.

## Verification
The included standalone \(\texttt{verify.py}\) uses exact integers and rational arithmetic. It independently constructs all projection rows from the Gram-inverse formula in dimensions \(2\) through \(10\), tests row-sum normalization and sign preservation, and compares with the binomial closed formula. It also evaluates every Hamming row via exact orbit counting in dimensions \(2\) through \(100\) and tests strict localization of maximizing rows. One reproducible command is \(\texttt{python3 verify.py}\). All reported tests passed. The proof, not finite tests, establishes the theorem for arbitrary dimension.

## Relationship to prior work
The full Boolean cube's affine Walsh projection is classical. Nayar's 2013 paper treats affine Fourier structure under product laws, while Defant--Galicer--Mansilla--Mastyło--Muro study projection constants for full-cube Fourier subspaces. Neither setup includes a deleted sampling vertex: conditioning uniform cube measure on the complement of a corner destroys the product law and the transitive cube group action. The 2010 work by Hangelbroek--Narcowich--Sun--Ward develops general \(L^\infty\) least-squares stability for kernel approximation, rather than this discrete exact constant. John's 1979 factorial missing-points article is highly relevant to rank loss and variance efficiency; its accessible abstract concerns parameter variances, not worst-case \(\ell^\infty\) hat-matrix row sums, but its complete text was unavailable. Earlier related exact constants for continuous cubical domains and biased product cubes do not imply the corner-deleted formula. Residual risk of an implicit exact formula in missing-run design literature remains.

## Limitations
This is the canonical orthogonal projection for uniform counting measure on precisely one-corner-deleted cubes; it is not the minimum norm among all possible affine projections. The result does not cover removal of several vertices, nonuniform surviving weights, higher polynomial degrees, or continuous measures on cubes. The novelty assessment is conditional on accessible primary texts and semantic database searches; unavailable historical articles could contain a mathematically equivalent formula.

## References
- T. Hangelbroek, F. J. Narcowich, X. Sun, J. D. Ward, *Kernel Approximation on Manifolds II: The \(L_\infty\)-norm of the \(L_2\)-projector*, arXiv:1005.2424v1 (first public preprint 2010-05-13).
- P. Nayar, *FKN Theorem on the biased cube*, arXiv:1311.3179v1 (2013-11-13).
- A. Defant, D. Galicer, M. Mansilla, M. Mastyło, S. Muro, *Asymptotic insights for projection, Gordon--Lewis and Sidon constants in Boolean cube function spaces*, arXiv:2302.00233v1 (2023-02-01).
- P. W. M. John, *Missing Points in \(2^n\) and \(2^{n-k}\) Factorial Designs*, Technometrics 21 (1979), 225--228, DOI:10.1080/00401706.1979.10489752 (only abstract/bibliographic material accessible).
