# Even-column rectangular tensor-norm saturation has an exponential row threshold

## Finding

Fix an even integer \(n=2k\ge2\) and an integer \(m\ge1\). For every real matrix \(A=(a_{ij})\in\mathbb R^{m\times n}\), put
\[
P(A)=\sum_{i=1}^m\sum_{j=1}^n|a_{ij}|,\qquad
C(A)=\max_{\varepsilon\in\{-1,1\}^n}\sum_{i=1}^m\left|\sum_{j=1}^n a_{ij}\varepsilon_j\right|.
\]
The denominator equals the induced operator norm \(\|A\|_{\infty\to1}\). Define \(R_{m,n}=\max_{A\ne0}P(A)/C(A)\); compactness of the normalized finite-dimensional unit sphere guarantees that this maximum exists. Then
\[
\boxed{R_{m,n}\le\frac{2^n}{\binom n{n/2}},\qquad
R_{m,n}=\frac{2^n}{\binom n{n/2}}\ \Longleftrightarrow\ m\ge2^{n-1}.}
\]
The minimum number of rows required to attain the known universal Rademacher upper bound is thus exactly \(2^{n-1}\).

There is a complete equality classification. A nonzero real matrix \(A\) satisfies \(P(A)/C(A)=2^n/\binom n{n/2}\) if and only if: (i) every nonzero row is \(c_i s_i\), with \(c_i>0\) and \(s_i\in\{-1,1\}^n\); and (ii) writing \([s]=\{s,-s\}\) for an antipodal sign class, the total row magnitude
\[
w_{[s]}=\sum_{i:[s_i]=[s]}c_i
\]
is one common strictly positive value for all \(2^{n-1}\) sign classes. Zero rows and repeated sign classes are permitted. Taking one representative from each class with unit magnitude gives the minimal-row extremizer; rows may be split within classes or zero-padded thereafter.

For example, the first even-column universal ratios are \(2\) at \(n=2\), \(8/3\) at \(n=4\), and \(16/5\) at \(n=6\), requiring respectively \(2,8,32\) rows. As \(n\to\infty\) through even integers, the bound is asymptotic to \(\sqrt{\pi n/2}\).

## Assumptions and scope

Matrices are finite, real and not identically zero; the column dimension is a positive even integer, the row dimension is any positive integer, and zero rows are allowed. The assertion concerns the rectangular tensor ratio \(\rho(\ell_1^m(\mathbb R),\ell_1^n(\mathbb R))\), which the standard finite-dimensional tensor identification equates with \(R_{m,n}\). No claim is made about odd column dimensions or complex matrices.

As a direct use of the previously proved endpoint-column compression identity of Santos and Serrano-Rodríguez, for every integer \(r\ge n\), the same result also says
\[
\Gamma_\infty^{\mathbb R}(r;m,n)=\frac{2^n}{\binom n{n/2}}
\quad\Longleftrightarrow\quad m\ge2^{n-1},
\]
while the left-hand side is strictly smaller when \(m<2^{n-1}\). The identity relating \(\Gamma_\infty\) to \(R_{m,n}\) is not asserted to be new.

## Proof

**1. The sharp Rademacher bound and rowwise equality.** For \(a\in\mathbb R^n\) define
\[
F(a)=2^{-n}\sum_{\varepsilon\in\{-1,1\}^n}\left|\sum_{j=1}^n\varepsilon_j a_j\right|,
\quad \mu_n=F(1,\ldots,1).
\]
Sign invariance allows replacement of \(a_j\) by \(|a_j|\). Since \(F\) is convex and invariant under permutations, averaging the \(n!\) permutations of \((|a_1|,\ldots,|a_n|)\) gives
\[
F(a)\ge F\left(\frac{\|a\|_1}{n}(1,\ldots,1)\right)
=\frac{\mu_n}{n}\|a\|_1.
\tag{1}
\]
For even \(n\), equality in (1), for a nonzero row, is possible only when all \(|a_j|\) are equal. To see strictness when these magnitudes are unequal, choose a balanced sign vector with exactly \(n/2\) plus signs. The signed sum of the averaged constant vector is zero. If two original magnitudes differ, choose a permutation positioning them on opposite signs; swapping their positions changes the signed sum by twice their difference, so the signed sums of all permutations cannot all vanish. Their permutation average is zero, hence their average absolute value is strictly positive. Jensen's inequality is therefore strict for this balanced sign vector, while it is non-strict for all others. Conversely, constant magnitudes give equality by sign invariance. This proves both (1) and its exact equality condition.

For even \(n=2k\), a direct binomial summation gives
\[
\mu_n=\frac{n}{2^n}\binom n{n/2};
\tag{2}
\]
for example, this follows by pairing sign sums of opposite sign and telescoping the resulting binomial differences. Therefore
\[
C(A)\ge 2^{-n}\sum_{\varepsilon}\sum_i|a_i\cdot\varepsilon|
=\sum_iF(a_i)\ge\frac{\mu_n}{n}P(A),
\]
proving the universal bound. Equality requires every nonzero row to have the form \(c_i s_i\) as stated, and requires the function \(\varepsilon\mapsto\sum_i c_i|s_i\cdot\varepsilon|\) to be constant over all sign vectors. These two conditions together are also sufficient.

**2. No Fourier zeros for the even sign-sum kernel.** Let \(G=\{-1,1\}^n/\{\pm(1,\ldots,1)\}\), a group with \(2^{n-1}\) elements, and let \(f([s])=|s_1+\cdots+s_n|\). Its characters correspond precisely to subsets \(S\subset\{1,\ldots,n\}\) of even cardinality, via \(\chi_S([s])=\prod_{j\in S}s_j\). For any nonempty such subset of size \(|S|=2j\), define the normalized Fourier coefficient
\[
\widehat f(S)=2^{-n}\sum_{s\in\{-1,1\}^n}\left|\sum_{h=1}^ns_h\right|\prod_{j\in S}s_j.
\]
Use the absolutely convergent integral identity, for each real \(x\),
\[
|x|=\frac2\pi\int_0^\infty\frac{1-\cos(tx)}{t^2}\,dt.
\]
The nontrivial character has mean zero, and independence of signs gives
\[
\mathbb E_s\left[\cos\left(t\sum_hs_h\right)\prod_{j\in S}s_j\right]
=(-1)^j(\sin t)^{2j}(\cos t)^{n-2j}.
\]
Thus
\[
\boxed{\widehat f(S)=\frac{2(-1)^{j+1}}\pi\int_0^\infty
\frac{(\sin t)^{2j}(\cos t)^{n-2j}}{t^2}\,dt\ne0.}
\tag{3}
\]
Indeed, both exponents are even, the integrand is nonnegative and positive on an interval, and it is integrable: near zero it is \(O(t^{2j-2})\), while at infinity it is \(O(t^{-2})\). The parity of \(n\) is crucial here.

**3. Exact classification by convolution.** For flat nonzero rows, aggregate weights \(w([s])=\sum_{i:[s_i]=[s]}c_i\ge0\). With coordinatewise group multiplication, the expression that must be constant is precisely the convolution \((w*f)([\varepsilon])\) on \(G\). Under normalized Fourier transform, \(\widehat{w*f}(S)=|G|\widehat w(S)\widehat f(S)\); the harmless factor \(|G|\) depends on the convolution convention. A function is constant exactly when all its nontrivial Fourier coefficients vanish. By (3), this forces \(\widehat w(S)=0\) for every nontrivial character. Fourier inversion on the finite abelian group then implies that \(w\) is constant on \(G\). Since \(A\ne0\), its common value is positive. Conversely, a constant weight function makes \(w*f\) constant, completing the equality classification.

Every class must consequently contribute at least one nonzero row, so \(m\ge|G|=2^{n-1}\) is necessary. Conversely, choose one representative from each class, assign every row magnitude \(1\), and insert any additional zero rows. The resulting matrix attains the bound and proves sufficiency. If \(m<2^{n-1}\), no matrix can attain the universal bound. Because \(P(A)=1\) defines a compact set and \(C(A)>0\) there, the ratio attains its supremum, which is therefore strictly smaller. Finally, the stated asymptotic follows from Stirling's formula applied to the central binomial coefficient.

## Verification

The finite checks in the accompanying `verify_rectangular_endpoint.py` recompute the sharp ratios for the explicit extremizing matrices at \(n=2,4,6,8\), enumerate every nontrivial even Fourier coefficient and confirm that none vanishes, and check strict loss after deleting a sign class. Those exhaustive *finite examples* are diagnostics, not proof of the result for arbitrarily large \(n\). The complete theorem follows from the analytic inequalities, integral formula and finite-group Fourier inversion just proved.

## Relationship to prior work

Santos and Serrano-Rodríguez (arXiv:2610.04398v1, Sections 4 and 8, and Proposition 1.2) identify the relevant projective/injective tensor ratio, prove endpoint column compression, and quote the classical universal \(1\)-summing norm \(n/\mu_n\) as an upper bound. They do not determine the minimum *number of rows* at which that bound becomes attained, nor characterize all equality matrices for even column dimension. Their open square-endpoint problem remains untouched: our equality requires exponentially more rows than columns for even \(n\ge4\).

Aubrun, Lami, Palazuelos, Szarek and Winter (2020, Proposition 12 and Appendix C) establish tensor-ratio/summing-operator links and the unrestricted \(1\)-summing identity norm. These facts explain the known universal bound but do not themselves imply the stated rigidity without the nonvanishing-Fourier argument. Friedland, Lim and Zhang (arXiv:1711.04427v2, Sections 4–5) develop the matrix-multiplication formulation of Grothendieck–Hölder inequalities; the exponential saturation threshold is not among the theorems in those sections.

## Limitations

This is a real-scalar, even-column result; the Fourier integrand need not retain the same sign for odd column dimension. It does not compute the exact smaller constants \(R_{m,n}\) for \(m<2^{n-1}\). It also does not resolve the square-dimensional endpoint constants studied in the motivating article, nor establish a result for complex scalars. An older or unindexed equivalent equality classification remains a possible originality risk.

## References

1. J. Santos and D. Serrano-Rodríguez, *Effective Dimensions in Grothendieck–Hölder Inequalities*, arXiv:2610.04398v1 (first posted 3 October 2026), particularly Section 4, Proposition 1.2, and Section 8.
2. G. Aubrun, L. Lami, C. Palazuelos, S. J. Szarek and A. Winter, *Universal gaps for XOR games from estimates on tensor norm ratios*, Communications in Mathematical Physics 375 (2020), 679–724, Proposition 12 and Appendix C; open-access article DOI:10.1007/s00220-020-03688-2.
3. S. Friedland, L.-H. Lim and J. Zhang, *Grothendieck constant is norm of Strassen matrix multiplication tensor*, Numerische Mathematik 143 (2019), 905–922; arXiv:1711.04427v2.
