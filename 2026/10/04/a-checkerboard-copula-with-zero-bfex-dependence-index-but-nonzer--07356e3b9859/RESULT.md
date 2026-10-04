# A checkerboard copula with zero BFEx dependence index but nonzero Spearman dependence
## Finding
Pandey and Kundu propose a normalized dependence index \(D\) built from bivariate failure extropy (BFEx), with the independence benchmark
\[
J_0=\frac14\int_0^1\int_0^1 (uv)^2\,du\,dv=\frac1{36}.
\]
The condition \(D=0\) does **not** characterize independence, even among absolutely continuous distributions with positive checkerboard density and uniform margins.

Partition \([0,1]\) into three equal intervals and assign the nine cell probabilities
\[
P=\frac1{1089}
\begin{pmatrix}
265&49&49\\
13&49&301\\
85&265&13
\end{pmatrix}.
\]
Take the density to be constant on each cell. Every row and every column of \(P\) sums to \(1/3\), so both margins are uniform. The law is not independent because, for example, the first cell has probability \(265/1089\), whereas independence would give \(1/9=121/1089\).

For this law,
\[
\int_0^1\int_0^1 C(u,v)^2\,du\,dv=\frac19,
\]
so its BFEx is
\[
J=\frac14\int_0^1\int_0^1 C(u,v)^2\,du\,dv=\frac1{36}=J_0.
\]
Consequently the proposed normalized index is exactly \(D=0\), although the variables are dependent. Moreover,
\[
\rho_S=12\int_0^1\int_0^1 C(u,v)\,du\,dv-3=\frac{64}{363}\ne0,
\]
so a classical copula dependence coefficient independently detects the dependence.

## Assumptions and scope
The construction uses an absolutely continuous bivariate law supported on \([0,1]^2\), with uniform continuous margins. Boundary conventions for the nine cells are irrelevant because cell boundaries have Lebesgue measure zero. The BFEx normalization is exactly the finite-support definition used for the dependence index in Pandey and Kundu. For uniform margins the comparison values are
\[
J_{\max}=\frac1{24},\qquad J_0=\frac1{36},\qquad J_{\min}=\frac1{48},
\]
so both denominators in the piecewise definition of \(D\) are nonzero.

The claim is only that \(D=0\) need not imply independence. It does not assert that the index is useless for all alternatives, nor does it assess its empirical estimator or the paper's conditional failure-extropy results.

## Proof
Write
\[
Q=\begin{pmatrix}
-4&2&2\\
3&2&-5\\
1&-4&3
\end{pmatrix},
\qquad
P(t)=\frac19\mathbf 1_{3\times3}+tQ.
\]
Every row sum and every column sum of \(Q\) is zero, hence every admissible \(P(t)\) has uniform margins. At
\[
t=-\frac4{121},
\]
all nine entries are positive and \(P(t)\) is exactly the matrix displayed above.

On a checkerboard cell, use local coordinates \(x,y\in[0,1]\). The copula is bilinear there:
\[
C=A+Bx+Cy+Dxy,
\]
where \(A\) is the probability in the southwest completed cells, \(B\) and \(C\) are the completed strips in the current row and column, and \(D\) is the current cell probability. Integrating this polynomial cell by cell gives the exact identity
\[
\int_0^1\int_0^1 C_t(u,v)^2\,du\,dv
=\frac19+\frac4{81}t+\frac{121}{81}t^2.
\]
Substitution of \(t=-4/121\) cancels the linear and quadratic terms, so the integral equals \(1/9\), exactly the independence value. Multiplication by the BFEx factor \(1/4\) gives \(J=J_0=1/36\), and therefore \(D=0\).

The same cell integration gives
\[
\int_0^1\int_0^1 C(u,v)\,du\,dv=\frac{1153}{4356},
\]
whence
\[
\rho_S=12\frac{1153}{4356}-3=\frac{64}{363}.
\]
This is nonzero and therefore also certifies nonindependence. Independently, nonindependence already follows from the unequal cell probabilities.

## Verification
The accompanying `verify_checkerboard.py` uses exact rational arithmetic. It checks positivity and the row/column sums of \(P\), nonindependence of the cell table, the exact values
\[
\int C^2=\frac19,
\qquad
\int C=\frac{1153}{4356},
\qquad
\rho_S=\frac{64}{363},
\]
and the quadratic identity for \(\int C_t^2\) along the entire checkerboard direction.

The argument is finite symbolic integration of the exact piecewise-bilinear copula; no floating-point approximation, simulation, or incomplete enumeration is used as proof.

## Relationship to prior work
Pandey and Kundu introduce BFEx for bivariate distributions and, in their dependence-measure section, normalize it between the countermonotone, independent, and comonotone benchmarks. Their stated independence characterization treats equality of the scalar BFEx value with the independence benchmark as if it forced equality of the joint CDF with the product CDF. The checkerboard construction shows that this implication fails: signed deviations of \(C^2\) from \((uv)^2\) can cancel in the integral.

Kayal's earlier work introduced failure extropy and its bivariate extension, but it does not supply the later normalized dependence index or the independence characterization addressed here. Standard copula dependence measures based on a nonnegative distance such as an integral of \((C-uv)^2\) do not suffer this particular cancellation mechanism; the present finding concerns the signed difference of two squared-CDF integrals used in the BFEx index.

## Limitations
This counterexample concerns the zero set of the proposed BFEx dependence index. It does not classify all copulas with \(D=0\), optimize how far such copulas can be from independence, or analyze sampling variability of an estimator. The checkerboard density has jumps across cell boundaries, although the joint distribution is absolutely continuous and the density is positive almost everywhere. A smoother counterexample is plausible by perturbation but is not claimed here.

## References
1. A. Pandey and C. Kundu, *On the Study of Bivariate and Conditional Failure Extropy with Application*, author manuscript publicly uploaded 2025-09-14, DOI 10.13140/RG.2.2.22787.77600; journal version, *Journal of Statistical Computation and Simulation*, published online 2026-08-06, DOI 10.1080/00949655.2026.2713196.
2. S. Kayal, *Failure Extropy, Dynamic Failure Extropy and Their Weighted Versions*, arXiv:2104.13705, 2021; *Stochastics and Quality Control* 36 (2021), 59–71.
