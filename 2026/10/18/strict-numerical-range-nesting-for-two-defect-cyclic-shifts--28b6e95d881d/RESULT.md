# Strict numerical-range nesting for two-defect cyclic shifts

## Finding
For every integer \(n\ge4\), positive real numbers \(a,b\), and \(1\le k\le\lfloor n/2\rfloor\), define \(S_{n,k}(a,b)\) on \(\mathbb C^n\) by
\[
(S_{n,k})_{j,j+1}=\begin{cases}a&j=0,\\b&j=k,\\1&\text{otherwise},\end{cases}\quad(0\le j<n),
\]
where column \(j+1\) is interpreted modulo \(n\); all other entries are zero. Let \(W(S)=\{\langle Sx,x\rangle:\|x\|_2=1\}\) denote the numerical range.

Set \(\Delta=(a^2-1)(b^2-1)\). For **every** \(1\le k<\lfloor n/2\rfloor\), the full numerical ranges obey the strict alternatives
\[
\begin{aligned}
\Delta>0 &: \quad W(S_{n,k+1})\subset\operatorname{int} W(S_{n,k}),\\
\Delta<0 &: \quad W(S_{n,k})\subset\operatorname{int} W(S_{n,k+1}),\\
\Delta=0 &: \quad W(S_{n,k+1})=W(S_{n,k}).
\end{aligned}
\]
In particular the numerical radii are strictly decreasing with defect separation if both exceptional weights are on the same side of \(1\), strictly increasing if they lie on opposite sides, and constant if either equals \(1\). These conclusions hold without a lower bound on \(a\) or \(b\) other than positivity. At \(n=4,5\) there is one comparison; for larger \(n\) they yield a complete ordered chain of all possible separations up to reflection.

## Assumptions and scope
The matrices are complex cyclic unilateral-direction shifts in finite dimension, with two real *positive* distinguished edge weights \(a,b\). The two exceptional edges are distinct: their indices are \(0\) and \(k\), with cyclic distance \(k\). Separation \(k\) and \(n-k\) give unitarily equivalent numerical ranges after reflection and transpose, so \(1\le k\le\lfloor n/2\rfloor\) enumerates the placements. Numerical-range inclusion is ordinary inclusion of compact convex subsets of \(\mathbb C\); \(\operatorname{int}\) means Euclidean interior. No assertion is made for matrices with more than two nonunit weights.

## Proof
For each real \(\theta\), let
\[
H_k(\theta)=e^{i\theta}S_{n,k}+e^{-i\theta}S_{n,k}^{*},\qquad
h_k(\theta)=\tfrac12\lambda_{\max}(H_k(\theta)).
\]
Then \(h_k(\theta)\) is the support function of \(W(S_{n,k})\) in the direction \(e^{-i\theta}\). Thus pointwise strict inequalities between the \(h_k\)'s imply the asserted strict inclusions, by compactness of the angular parameter circle.

Introduce the path polynomials \(q_{-1}(x)=0\), \(q_0(x)=1\), and \(q_j(x)=xq_{j-1}(x)-q_{j-2}(x)\) for \(j\ge1\). Thus \(q_j(x)=U_j(x/2)\), and \(q_j\) is the characteristic polynomial of the unweighted \(j\)-vertex path. For \(j\ge1\) its largest zero is \(2\cos(\pi/(j+1))\).

Write \(D_k(x,\theta)=\det(xI-H_k(\theta))\). Diagonal unitary conjugation removes all edge phases except a total cycle phase \(e^{in\theta}\). Expanding the determinant by disjoint adjacent transpositions (matchings) and the two oriented Hamiltonian cycles gives the exact identity
\[
\boxed{D_k(x,\theta)=q_n(x)-(a^2+b^2-1)q_{n-2}(x)
 +(a^2-1)(b^2-1)q_{k-2}(x)q_{n-k-2}(x)
 -2ab\cos(n\theta).} \tag{1}
\]
To justify the matching term explicitly: relative to all-unit edge weights, selecting edge \(0\) contributes \(-(a^2-1)q_{n-2}\); selecting edge \(k\) contributes \(-(b^2-1)q_{n-2}\); selecting both, which is possible only for nonadjacent edges, contributes \((a^2-1)(b^2-1)q_{k-2}q_{n-k-2}\). The convention \(q_{-1}=0\) correctly handles adjacent edges. The only phase-dependent determinant terms are the two oriented full cycles, with total contribution \(-2ab\cos(n\theta)\). The all-unit cycle matching contribution is \(q_n-q_{n-2}\).

For consecutive separations, the Chebyshev product identity
\[
q_{k-1}(x)q_{n-k-3}(x)-q_{k-2}(x)q_{n-k-2}(x)
=q_{n-2k-2}(x)
\]
(which follows inductively from the recurrence) therefore yields
\[
\boxed{D_{k+1}(x,\theta)-D_k(x,\theta)=
\Delta\,q_{m}(x),\qquad m=n-2k-2\ge0.} \tag{2}
\]
This difference is independent of \(\theta\).

Fix \(\theta\) and set \(\lambda_k=\lambda_{\max}(H_k(\theta))\). Restrict \(H_k(\theta)\) to the consecutive vertices \(k+1,k+2,\ldots,n-1,0\). This principal submatrix is a unit-weight path on \(n-k\) vertices, up to diagonal-unitary conjugation. The variational principle gives
\[
\lambda_k\ge 2\cos\frac\pi{n-k+1}.
\]
For \(m\ge1\), the largest zero of \(q_m\) is \(2\cos\!\left(\pi/(m+1)\right)\), strictly smaller than that path eigenvalue, since \(n-k+1>m+1=n-2k-1\). When \(m=0\), \(q_m=1\). Consequently
\[
q_m(x)>0\quad\text{for every }x\ge\lambda_k. \tag{3}
\]

If \(\Delta>0\), equations (2)–(3) and \(D_k(x,\theta)\ge0\) for \(x\ge\lambda_k\) imply \(D_{k+1}(x,\theta)>0\) on that entire half-line. Since \(D_{k+1}(\cdot,\theta)\) is a monic polynomial with only real roots, its largest root is strictly below \(\lambda_k\). If \(\Delta<0\), equation (2) at \(x=\lambda_k\) gives \(D_{k+1}(\lambda_k,\theta)<0\), whereas \(D_{k+1}(x,\theta)\to+\infty\) as \(x\to\infty\). Hence its largest root is strictly above \(\lambda_k\). If \(\Delta=0\), equation (2) gives identical characteristic polynomials and support functions.

The strict inequality holds at every angle \(\theta\). The support functions are continuous on the compact unit circle, so their strict difference has a positive minimum. The support-function characterization of planar compact convex bodies now implies the stated inclusions in the **interiors**, not merely non-strict nesting. Finally, for nonnegative cyclic weights, \(w(S_{n,k})=\frac12\lambda_{\max}(H_k(0))\): the triangle inequality bounds the modulus of the quadratic form by its value on absolute coordinates, and a nonnegative Perron vector realizes equality. This gives the numerical-radius corollaries.

## Verification
The accompanying `verify.py` (Python 3 with SymPy and NumPy) checks exact zero-flux characteristic-polynomial identities for \(4\le n\le10\), the Chebyshev difference identities, and exact flux-dependent identities at nontrivial symbolic phases for \(4\le n\le8\). It also tests the strict direction of all support-function inequalities for several mixed/same-sign weights, \(4\le n\le12\), and 49 sampled angles. The analytic proof above establishes the universal quantifiers; the finite checks are independent arithmetic corroboration, not an exhaustive proof.

## Relationship to prior work
Chang and Wang (2012) characterized **global numerical-radius maximizers** among weight permutations for general cyclic weighted shifts. This does not order every intermediate separation nor yield strict inclusion of the entire numerical ranges. Chien, Kirkland, Li and Nakazato (2023) studied **numerical-range inclusion** under permutations, proved their general maximizing-pattern conjecture through six dimensions (with further computational evidence), and supplied support-function/characteristic-polynomial tools. Their paper does not state the uniform two-defect nesting chain for all dimensions or its mixed-sign reversal. The determinantal approach to weighted shifts in Chien, Nakazato, Undrakh and Vandanjav (first online 2015) is a historical impetus, but its full text could not be inspected and its possible implications remain a bibliographic risk. The exact factorized difference (2), positivity beyond an induced path's spectral edge, and consequent strict support-function ordering are the material additions here.

## Limitations
This is a mathematical derivation with exact symbolic and finite numerical corroboration, not independent peer review. It does not prove a global permutation-ordering theorem for arbitrary multisets of more than two nonunit weights, nor a quantitative explicit lower bound on the Hausdorff support gap. Older or unavailable literature may contain an equivalent two-defect theorem or a directly applicable stronger spectral-rearrangement result. The inaccessible 2012 publisher PDF and 2015 original are specifically noted in the research comparison.

## References
1. C.-T. Chang and K.-Z. Wang, “Maximizing numerical radii of weighted shifts under weight permutations,” *Journal of Mathematical Analysis and Applications* 394 (2012), 592–602, doi:10.1016/j.jmaa.2012.04.039.
2. M.-T. Chien, H. Nakazato, B. Undrakh and A. Vandanjav, “Determinantal polynomials of a weighted shift operator,” *Linear and Multilinear Algebra* 64 (2016), 2–13; first published online 2015-01-21, doi:10.1080/03081087.2014.1003528.
3. M.-T. Chien, S. Kirkland, C.-K. Li and H. Nakazato, “Numerical ranges of cyclic shift matrices,” arXiv:2304.06050, version 2 (2023); especially Sections 1–2, 4, and 7.
