# Trivalent rooted stars already violate Cesàro normaloidity

## Finding
Let \(\mathcal T_m\) be the rooted tree consisting of one common root and \(m\) disjoint infinite rays, for each integer \(m\ge 3\). On counting-measure \(\ell^2(\mathcal T_m)\), define the ancestor-mean (Cesàro) operator by
\[
 (H_m f)(v)=\frac{1}{1+\operatorname{depth}(v)}\sum_{u\preceq v}f(u).
\]
Then
\[
 \|H_m\|>2=r(H_m)\qquad (m\ge3).
\]
In particular, the rooted three-ray (trivalent) star and every star with at least three rays are **not normaloid**. This strengthens the previously published elementary root-vector obstruction, which established this conclusion only for five or more rays. The proof gives a single finite-support witness valid for every \(m\ge3\), rather than an extrapolation from finite tree truncations. No assertion is made for the two-ray star.

## Assumptions and scope
All Hilbert spaces are complex, with ordinary counting measure on the vertices. The root has depth zero and each ray has one vertex at every strictly positive integer depth. The symbol \(u\preceq v\) means that \(u\) lies on the unique path from the root to \(v\). The integer \(m\) is at least three. The boundedness and spectral identity \(\sigma(H_m)=\{z:|z-1|\le1\}\) are previously published results for leafless narrow rooted trees; hence \(r(H_m)=2\). The new assertion is the strict operator-norm inequality, uniformly over all such integer branch counts.

## Proof
Let \(C\) denote the classical Cesàro operator on \(\ell^2(\mathbb N_0)\), so \((Cw)_n=(\sum_{j=0}^{n}w_j)/(n+1)\). Restrict \(H_m\) to the reducing symmetric subspace of inputs that have the same value on all rays at a given depth. In normalized coordinates, a vector with root coordinate \(a\) and symmetric depth coordinates \(y_j\), \(j\ge1\), has images
\[
 a,\qquad \frac{\sqrt m\,a+\sum_{s=1}^{j}y_s}{j+1},\quad j\ge1.
\]
Set \(w_0=\sqrt m\,a\) and \(w_j=y_j\), \(j\ge1\). Writing \(T=\sum_{j\ge1}|w_j|^2\), direct subtraction gives the exact identity
\[
 \|H_m(a,y)\|_2^2-4\|(a,y)\|_2^2
 =\|Cw\|_2^2-4\|w\|_2^2+3\left(1-\frac1m\right)|w_0|^2.
\tag{1}
\]
Choose the fixed finite vector
\[
 w_0=1,\qquad w_j=\frac{1}{2(j+1)}\ (1\le j\le19),\qquad w_j=0\ (j\ge20).
\]
Define the rational quantities
\[
 S=\sum_{j=0}^{19}w_j,\quad T=\sum_{j=1}^{19}w_j^2,\quad
 h_\ell=\sum_{s=1}^{\ell}\frac1{s^2}\ (h_0=0),\quad
 Z=\sum_{i,j=0}^{19}w_iw_j h_{\max(i,j)}.
\]
The exact Cesàro Gram entries are \(\langle Ce_i,Ce_j\rangle=\sum_{n\ge\max(i,j)}(n+1)^{-2}=\zeta(2)-h_{\max(i,j)}\); therefore
\[
 \|Cw\|_2^2=\zeta(2)S^2-Z.
\]
The following entirely rational checks are reproducible by `check.py`:
\[
 \sum_{s=1}^{203}s^{-2}>\frac{41}{25},\qquad
 \frac{41}{25}S^2-Z-2-4T>\frac1{400}>0.
\tag{2}
\]
Indeed, \(S=71354639/31039008\); the exact rational numerator of the latter gap is positive (the checker retains the complete fraction). By (1), for \(m=3\), the excess over four times the squared input norm equals \(\zeta(2)S^2-Z-2-4T>1/400\). For every integer \(m>3\) the last term in (1) increases, so the excess remains strictly positive. More explicitly, with \(a=1/\sqrt m\), the ratio yields
\[
 \|H_m\|^2>4+\frac{1}{400(1/3+T)}\quad (m\ge3).
\]
This establishes \(\|H_m\|>2\). The published spectral identity quoted above yields \(r(H_m)=2\), completing the nonnormaloid conclusion.

## Verification
Execute `python3 check.py` using the embedded standalone script. It checks the exact finite rational sums and strict signs in (2), including an exact value for the smaller rational gap. The infinite-output norm identity uses the convergent series \(\sum_{n\ge0}(n+1)^{-2}=\zeta(2)\); it is proved by summing the exact Gram entries, not by truncating outputs. Thus the finite certificate is an exact witness for the infinite operator, not an empirical approximation. The symmetric-subspace argument works for every \(m\ge3\). The spectral radius is imported from the published theorem and is not independently reproved here.

## Relationship to prior work
Vasil'eva (2013) developed bounds for weighted summation (Hardy-type) operators on rooted combinatorial trees, including the ancestor-summation framework; that paper supplies the archived problem setting but does not state this trivalent nonnormaloidity witness. Abhinand, Chavan, Dharan and Prasad (2025, arXiv:2504.00807), Theorem 1.6, established the disk spectrum for leafless narrow rooted trees. Their Example 3.1 treats exactly these \(m\)-ray stars and proves \(\|H_m\|>2\) for \(m\ge5\) by testing the root basis vector. Here an explicit mixed-depth witness establishes strictness already at \(m=3\), and monotonicity propagates to all larger branch counts. The claim is not a new spectral-radius theorem or a general exact norm formula.

## Limitations
The operator norm is not determined exactly. The nonnormaloidity question for the two-ray star is not resolved. The finite rational witness is not asserted to optimize the operator norm. The mathematical and bibliographic analysis has not received independent verification; equivalently formulated earlier inequalities might exist outside the inspected sources.

## References
1. A. A. Vasil'eva, *Estimates for norms of two-weighted summation operators on a tree under some conditions on weights*, arXiv:1311.0375 (first public version 2013-11-02), https://arxiv.org/abs/1311.0375.
2. M. Abhinand, S. Chavan, S. S. Dharan and T. Prasad, *Cesàro Operators on Rooted Directed Trees*, arXiv:2504.00807 (first public version 2025-04-01), https://arxiv.org/abs/2504.00807, Theorem 1.6 and Example 3.1.
3. A. Brown, P. R. Halmos and A. L. Shields, *Cesàro operators*, Acta Sci. Math. (Szeged) 26 (1965), 125–137, for the classical Cesàro setting as cited in Reference 2.
