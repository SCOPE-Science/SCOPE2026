# Sharp binary–ternary phase diagram for bilinear Fourier fourth moments

## Finding

Let \(n\ge3\) be an integer and let \(A=(a_{ij})\) be a \(3\times n\) matrix with all entries of modulus one. On the product torus with normalized Haar probability measure define
\[
P_A(z,w)=\sum_{i=1}^{3}\sum_{j=1}^{n}a_{ij}z_iw_j,
\qquad
\mathcal M_4(A)=\int_{\mathbb T^{n+3}}|P_A(z,w)|^4\,dm(z,w).
\]
For \(q=2,3\), let \(\mathcal U_q\) denote the \(q\)-th roots of unity, and write \(\mathcal M_{4,q}(n)\) for the minimum with all \(a_{ij}\in\mathcal U_q\). Then the exact sharp values are
\[
\boxed{\begin{aligned}
\min_{|a_{ij}|=1}\mathcal M_4(A)&=18n^2-15n,\\
\mathcal M_{4,2}(n)&=18n^2-15n+4r(4-r),\qquad r\equiv n\pmod4,\ 0\le r<4,\\
\mathcal M_{4,3}(n)&=18n^2-15n+12\mathbf1_{3\nmid n}.
\end{aligned}}
\]
The binary–ternary winner is exactly periodic in \(n\bmod12\): binary wins strictly for residues \(4,8\); ternary wins strictly for residues \(2,3,6,9,10\); both tie for residues \(0,1,5,7,11\).

All minimizers admit a finite combinatorial characterization. Multiply each column by the inverse of its first entry. For binary phases, let \(c_{uv}\) count columns of normalized type \((1,u,v)\), with \(u,v\in\{1,-1\}\), and write \(n=4t+r\), \(0\le r<4\). Equality holds precisely when all four counts belong to \(\{t,t+1\}\). Consequently, the number of *labelled, first-row-normalized* binary optimizers is exactly
\[
N_2(n)=\binom4r\frac{n!}{(t+1)!^r\,t!^{4-r}}.
\]
For ternary phases, write \(\omega=e^{2\pi i/3}\) and record each normalized column as \((1,\omega^u,\omega^v)\), \(u,v\in\mathbb Z_3\). Equality holds precisely when **each** of the three multisets of residues \(u\), \(v\), and \(u-v\) has multiplicities differing by at most one. In particular, if \(n=3t\), all equality configurations have the exact joint type-count matrix
\[
(c_{uv})_{u,v\in\mathbb Z_3}=
\begin{pmatrix}a&b&c\\b&c&a\\c&a&b\end{pmatrix},
\qquad a,b,c\in\mathbb Z_{\ge0},\qquad a+b+c=t,
\]
so the number of labelled, first-row-normalized ternary optimizers in this case is
\[
N_3(3t)=(3t)!\sum_{a+b+c=t}\frac1{(a!)^3(b!)^3(c!)^3}.
\]
These are counts of normalized coefficient arrays, **not** equivalence classes under further row, permutation, or modulation symmetries.

## Assumptions and scope

The \(n+3\) torus coordinates \(z_1,z_2,z_3,w_1,\ldots,w_n\) are independent. This is the **bilinear Segre frequency support** \(\{e_i+f_j\}\) in a free character group; it is not the two-variable rectangular exponent grid \(\{z^iw^j\}\). Every coefficient has modulus one. The minimum with unrestricted phases, with real signs, and with cube-root phases is computed separately. No assertion is made for \(n<3\), for other alphabets, for arbitrary nonuniform magnitudes, or for finite torus grids with possible frequency aliasing.

## Proof

Put
\[
S(A)=\sum_{1\le i<k\le3}
\left|\sum_{j=1}^{n}a_{ij}\overline{a_{kj}}\right|^2.
\]
Fourier-character orthogonality converts the fourth moment into the squared coefficient energy of \(P_A^2\). There are \(3n\) diagonal monomial pairs, \(3\binom n2+3n\) unordered pairs sharing exactly one endpoint, and \(3\binom n2\) four-edge rectangles. Each rectangle has two distinct products contributing to the same convolution coefficient. Counting their cross terms yields
\[
\mathcal M_4(A)=18n^2-3n
+8\sum_{i<k}\sum_{j<\ell}
\operatorname{Re}(a_{ij}a_{k\ell}\overline{a_{i\ell}a_{kj}}).
\]
Expansion of \(S(A)\) gives
\[
S(A)=3n+2\sum_{i<k}\sum_{j<\ell}
\operatorname{Re}(a_{ij}a_{k\ell}\overline{a_{i\ell}a_{kj}}),
\]
which proves the exact master identity
\[
\boxed{\mathcal M_4(A)=18n^2-15n+4S(A).}\tag{1}
\]
Since \(S(A)\ge0\), the unrestricted lower bound follows. Take the first three rows of the \(n\times n\) discrete Fourier matrix: \(a_{ij}=e^{2\pi i(i-1)(j-1)/n}\). For \(n\ge3\), distinct rows are orthogonal and \(S(A)=0\), so the bound is sharp.

The summand \(S(A)\) is invariant under multiplying any column by a scalar of modulus one. For the binary problem normalize each column to \((1,u,v)\in\{1\}\times\{\pm1\}^2\). Let \(c_0,c_1,c_2,c_3\) be the four type counts, summing to \(n\). The three inter-row correlations are exactly the three nontrivial Walsh transforms of the vector \((c_0,c_1,c_2,c_3)\). Orthogonality of the \(4\times4\) Walsh matrix gives
\[
n^2+S(A)=4\sum_{h=0}^3c_h^2.
\]
For fixed nonnegative integer sum \(\sum c_h=n\), the square sum is minimal if and only if the counts differ by at most one: transferring a unit from a count exceeding another by at least two strictly decreases that sum. With \(n=4t+r\), there are \(r\) counts equal to \(t+1\), the others \(t\), giving \(S_{2,\min}=r(4-r)\). Every such count vector is realized by arranging its four column types, and multinomial counting yields the stated exact \(N_2(n)\).

For ternary phases similarly gauge-normalize all columns to \((1,\omega^u,\omega^v)\). The three pair correlations, up to conjugation, are
\[
\sum_j\omega^{u_j},\qquad \sum_j\omega^{v_j},\qquad \sum_j\omega^{u_j-v_j}.
\]
If a residue distribution has counts \(d_0,d_1,d_2\), its squared root sum is
\[
\left|d_0+d_1\omega+d_2\omega^2\right|^2
=d_0^2+d_1^2+d_2^2-d_0d_1-d_0d_2-d_1d_2
=\frac12\sum_{0\le h<k\le2}(d_h-d_k)^2.
\]
This is minimized, for an integer total \(n\), precisely when its three counts differ by at most one. The minimum is zero when \(3\mid n\) and one otherwise. Therefore \(S(A)\ge3\mathbf1_{3\nmid n}\). Equality is simultaneously attainable: arrange the normalized columns cyclically as \((1,\omega^j,\omega^{2j})\), with \(0\le j<n\). Every difference projection then cycles through all three residues, so each contributes the individual minimum. This proves the ternary formula and the complete balancing criterion.

When \(n=3t\), each of the three residue projections must be uniform. Writing the nine unknown joint counts as a \(3\times3\) array, the three families of row, column, and diagonal-slope-one sum equations all equal \(t\). To solve these equations, write the first two rows as \((a,b,c)\) and \((d,e,f)\). The diagonal and column sums give \(d=e+b-c\) and \(f=e+a-c\); because each row totals \(t=a+b+c\), the second-row sum forces \(3e=3c\), hence \(e=c\), \(d=b\), and \(f=a\). The column sums then force the third row to be \((c,a,b)\). Thus the full nonnegative solution is exactly the cyclic array displayed in the theorem, with \(a,b,c\ge0\) and \(a+b+c=t\). A fixed such array has \((3t)!/(a!^3b!^3c!^3)\) labelled column orderings, proving the ternary count formula.

Finally, comparing the two nonnegative defects \(r(4-r)\) and \(3\mathbf1_{3\nmid n}\) across the twelve residue classes proves the sharp winner table; no additional optimizer can occur because every inequality used has its equality condition accounted for.

## Verification

A standalone Python 3 standard-library checker, `checks/check_segre.py`, evaluates the master identity through a separate exact additive-frequency convolution for representative arrays. It completely enumerates all normalized binary arrays for widths \(3\le n\le7\) and all normalized ternary arrays for \(3\le n\le5\), and verifies the claimed optima and binary optimizer counts. It checks explicit achieving constructions for every width \(3\le n\le120\). It passed 273 assertions. Exhaustive checks at finite widths are supplementary: the proof for arbitrary \(n\) is the Walsh-orthogonality and Eisenstein-root-count argument above.

For orientation, at width \(n=3\) the ternary/binary optima are \(117\) and \(129\); at width \(n=4\) the binary/ternary optima are \(228\) and \(240\). At width \(n=5\) the two alphabets tie at \(387\), while at width \(n=6\) the ternary/binary optima are \(558\) and \(574\).

## Relationship to prior work

Balister–Bollobás–Morris–Sahasrabudhe–Tiba (2019 preprint; 2020 publication) establish uniform-amplitude flatness for univariate binary Littlewood polynomials; they do not state this exact bilinear-Segre fourth-moment minimization. Katz (2012) studies asymptotic fourth norms for multivariable **rectangular exponent-array** character polynomials, a different additive-frequency geometry. Raposo and Serrano-Rodríguez (2023) study coefficient inequalities for bilinear forms under supremum/sequence-space norms, not the exact \(L^4\) torus moment of the Segre character support. Existing complex Hadamard and frame-potential theory motivates the orthogonal-row lower bound; the binary/ternary integer defects, complete equality constraints, and periodic strict reversals are the specific conclusions here. A known stronger quantized-frame theorem could imply parts of these conclusions, so novelty is provisional pending broader bibliographic review.

## Limitations

The sharp formulas and equality classifications concern exactly three independent row characters, an arbitrary finite number of independent column characters, and the binary or ternary phase alphabets. The ternary **count** formula is asserted only for widths divisible by three; for other widths equality is characterized by three balancing conditions but no closed optimizer-count formula is claimed. These finite-dimensional exact facts do not establish asymptotic flatness in \(L^\infty\), robustness under measurement noise, or extensions to other frequency geometries.

## References

- P. Balister, B. Bollobás, R. Morris, J. Sahasrabudhe, M. Tiba, *Flat Littlewood Polynomials Exist*, arXiv:1907.09464v1 (first public 2019-07-22); *Annals of Mathematics* 192 (2020), 977–1004.
- D. J. Katz, *Asymptotic L4 Norm of Polynomials Derived from Characters*, arXiv:1205.1069v2 (2012).
- A. Raposo Jr. and D. M. Serrano-Rodríguez, *Coefficients of Multilinear Forms on Sequence Spaces*, *Bulletin of the Brazilian Mathematical Society* 54, article 43 (2023), doi:10.1007/s00574-023-00359-3.
- M. Fickus, J. Jasper, D. G. Mixon, J. D. Peterson, *Hadamard Equiangular Tight Frames*, *Applied and Computational Harmonic Analysis* 50 (2021), 281–302, doi:10.1016/j.acha.2019.08.003. (Context for flat-frame constructions; not used to derive the sharp phase-defect formulas.)
