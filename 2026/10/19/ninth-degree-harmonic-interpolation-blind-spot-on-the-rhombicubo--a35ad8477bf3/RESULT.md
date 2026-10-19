# Ninth-degree harmonic interpolation blind spot on the rhombicuboctahedron

## Finding

Let \(X\subset S^2\) contain one point from each antipodal pair of the 24 vertices of the regular rhombicuboctahedron. Let \(\mathcal H_\ell\) be the complex homogeneous spherical-harmonic space of degree \(\ell\), of dimension \(2\ell+1\). Denote its point-evaluation map on \(X\) by \(E_\ell:\mathcal H_\ell\to\mathbb C^{12}\).

For every integer \(\ell\ge0\),
\[
\operatorname{rank}E_\ell=\begin{cases}10,&\ell=9,\\ \min(2\ell+1,12),&\ell\ne9.\end{cases}
\]
The complete initial rank sequence, for \(\ell=0,\ldots,12\), is
\[(1,3,5,7,9,11,12,12,12,10,12,12,12).\]
In particular, the degree-eight map is surjective but degree nine loses exactly two dimensions; every degree \(\ell\ge10\) is again surjective. At degree nine the attainable sample vectors are characterized by two explicit homogeneous linear constraints below.

## Assumptions and scope

Put \(t=1+\sqrt2\), \(d=t^2+2=5+2\sqrt2\). The 24 vertices are exactly all vectors obtained by independently assigning signs to the coordinates and permuting
\[(1,1,t)/\sqrt d.\]
The choice \(t=1+\sqrt2\) makes the edges of the signed-permutation orbit equal: edges within a fixed distinguished-coordinate layer have length \(2/\sqrt d\), and adjacent interlayer edges have length \(\sqrt2(t-1)/\sqrt d\). The twelve representative points may, for example, be chosen to have positive first coordinate. All ranks are over \(\mathbb C\), and the sphere carries normalized surface probability measure.

For each point \(x\in X\), let \(i(x)\in\{1,2,3\}\) be the unique index for which \(|x_{i(x)}|=t/\sqrt d\). Define three linear sample functionals
\[
S_i(y)=\sum_{\substack{x\in X\\i(x)=i}}\operatorname{sgn}(x_1x_2x_3)y(x),\quad i=1,2,3.
\]
Then at degree nine,
\[
E_9(\mathcal H_9)=\{y\in\mathbb C^{12}:S_1(y)=S_2(y)=S_3(y)\}.
\]
Each \(S_i\) is independent of the selection of antipodal representatives when applied to odd-degree compatible data (both the sign factor and the sample change sign on replacing \(x\) by \(-x\)).

## Proof

**1. Gram reduction.** The spherical-harmonic addition formula gives, up to the strictly positive scalar \(2\ell+1\), the data-side Gram matrix
\[G_\ell=(P_\ell(x\cdot y))_{x,y\in X},\]
where \(P_\ell\) denotes the Legendre polynomial with \(P_\ell(1)=1\). Thus \(\operatorname{rank}E_\ell=\operatorname{rank}G_\ell\). The diagonal of \(G_\ell\) equals one. Every off-diagonal dot product lies among the six signed values \(\pm a,\pm b,\pm c\), where
\[
a=\frac{7+4\sqrt2}{17},\quad b=\frac{-3+8\sqrt2}{17},\quad c=\frac{5-2\sqrt2}{17},\quad 0<c<b<a<\tfrac34.
\]

**2. Two exact missing-data functionals.** Work temporarily on all 24 signed vertices and group them into three layers according to their unique coordinate of absolute value \(t/\sqrt d\). Under the eight coordinate-sign changes, the sign character \(\sigma_1\sigma_2\sigma_3\) gives a three-dimensional invariant block of the full 24-point Gram. For odd \(\ell\), let \(A=P_\ell(a)\), \(B=P_\ell(b)\), and \(C=P_\ell(c)\). In the basis of the three layer-indicator functions multiplied by \(\sigma_1\sigma_2\sigma_3\), this block has diagonal entry \(-4A+2B+2\) and all off-diagonal entries \(2A-2B-4C\). Its two-dimensional sum-zero eigenspace has eigenvalue
\[2(1-3A+2B+2C).\]
The Legendre recurrence \((\ell+1)P_{\ell+1}(z)=(2\ell+1)zP_\ell(z)-\ell P_{\ell-1}(z)\), evaluated exactly in \(\mathbb Q(\sqrt2)\), gives
\[1-3P_9(a)+2P_9(b)+2P_9(c)=0.\]
Consequently the two vectors with coefficients \(\operatorname{sgn}(x_1x_2x_3)(\mathbf1_{i(x)=1}-\mathbf1_{i(x)=2})\) and \(\operatorname{sgn}(x_1x_2x_3)(\mathbf1_{i(x)=1}-\mathbf1_{i(x)=3})\) lie in the left nullspace of \(G_9\). They are independent because the three layers are nonempty. Hence \(\operatorname{rank}E_9\le10\), and every degree-nine sample satisfies \(S_1=S_2=S_3\).

**3. Finite, exact lower-rank certificates.** For each \(0\le\ell\le119\), the standalone checker evaluates \(G_\ell\) by the three-term Legendre recurrence over the prime fields of sizes \(1000000007\) and \(1000000009\), with fixed square roots of \(2\) respectively \(59713600\) and \(291087696\). Both are genuine roots modulo their respective primes. All denominators (including \(17\) and the recurrence indices \(1,\ldots,120\)) are invertible. A nonzero minor after either specialization is a nonzero minor of the characteristic-zero matrix in \(\mathbb Q(\sqrt2)\); these are lower-bound rank certificates, not probabilistic guesses. Every one of the 120 checked degrees in both fields has rank \(\min(2\ell+1,12)\) except degree nine with rank ten. For \(\ell\le5\), the universal dimension bound \(2\ell+1\) supplies matching upper bounds; for degree nine the exact two-dimensional annihilator supplies the matching upper bound; for all other degrees from six to 119 the verified rank twelve is maximal. The checker separately verifies the annihilator identity and both functionals using exact rational arithmetic in \(\mathbb Q(\sqrt2)\).

**4. Infinite tail without extrapolation.** The classical Bernstein inequality, in the form [DLMF 18.14.7] specialized to \(\lambda=\tfrac12\), states that for \(\ell\ge1\), \(-1<u<1\),
\[
|P_\ell(u)|<\sqrt{\frac{2}{\pi(\ell+\tfrac12)\sqrt{1-u^2}}}.
\]
Since all off-diagonal Gram arguments satisfy \(|u|\le a<3/4\), their squared complementary sine is greater than \(7/16\). For every \(\ell\ge120\), the sum of the absolute values of the eleven off-diagonal entries in any Gram row is strictly smaller than
\[
11\sqrt{\frac{8}{\pi(120+\tfrac12)\sqrt7}}<1.
\]
Thus the Hermitian Gram is strictly diagonally dominant with diagonal one, hence positive definite, for every \(\ell\ge120\). This finishes the all-degree rank classification. At \(\ell=9\), the exact dimension ten and the two independent relations show that they describe the entire image.

## Verification

The standalone standard-library checker `checker.py` is part of this package. Run `python3 checker.py`. It verifies the exact \(\mathbb Q(\sqrt2)\) Legendre cancellation at degree nine, checks both pointwise annihilators directly in that field, constructs all twelve representative nodes, and performs exact modular Gaussian elimination for all 120 degrees in two independent prime fields. The expected rank lists are asserted explicitly. The analytic step in the previous section proves all degrees beyond those checked; finite computation is not offered as an infinite proof.

## Relationship to prior work

The spherical-code and design framework of Delsarte, Goethals and Seidel and the 24-point polyhedral-orbit study of Hardin and Sloane motivate exact harmonic tests on symmetric point sets. Hardin and Sloane's accessible full text treats spherical design strength and an improved snub cube; the present rhombicuboctahedral sample set and its exact-degree ninth-order rank obstruction are different. Design strength, cumulative polynomial interpolation and exact-degree image rank are different questions. The Legendre inequality used in the infinite tail is the classical, already known bound recorded by NIST, not a new claim. No priority claim beyond comparisons with the inspected literature is made.

## Limitations

The theorem concerns this fixed 24-vertex Archimedean orbit (twelve antipodal sample lines), with equal unweighted point evaluations; it does not classify deformation parameters, perturbation stability, sampling condition numbers, or other Archimedean solids. The literature comparison includes one broad foundational paper whose complete text was not accessible, and unindexed harmonic-branching tables could contain equivalent calculations. Independent publication priority and independent validation are not established.

## References

- R. H. Hardin and N. J. A. Sloane, *McLaren's Improved Snub Cube and Other New Spherical Designs in Three Dimensions*, arXiv:math/0207211, public preprint dated 2002-07-23; full text at https://arxiv.org/html/math/0207211v1.
- P. Delsarte, J. M. Goethals and J. J. Seidel, *Spherical Codes and Designs*, Geometriae Dedicata **6** (1977), 363–388, DOI 10.1007/BF03187604. The accessible record did not provide the complete text.
- NIST Digital Library of Mathematical Functions, §18.14, formula 18.14.7, https://dlmf.nist.gov/18.14.E7.
