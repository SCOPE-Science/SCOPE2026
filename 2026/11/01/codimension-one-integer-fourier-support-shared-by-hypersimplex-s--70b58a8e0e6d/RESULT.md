# Codimension-one integer Fourier support shared by hypersimplex slices

## Finding

Fix integers \(n\ge 5\) and \(2\le s\le n-2\). The (nontrivial) hypersimplex is
\[
\Delta(s,n)=\{x\in[0,1]^n:\sum_{j=1}^n x_j=s\}.
\]
On the hyperplane use normalized section measure \(d\mu=d\mathcal H^{n-1}/\sqrt n\), where \(\mathcal H^{n-1}\) is Euclidean hypersurface measure. For the unique integer-frequency representative \(k=(k_1,\ldots,k_{n-1},0)\), define
\[
C_{s,n}(k)=\int_{\Delta(s,n)}e^{-2\pi i\sum_{j=1}^n k_jx_j}\,d\mu(x).
\]

**Theorem (sharp leading Fourier support and collision coefficient).** If the \(n\) entries of \(k\) are pairwise distinct, then \(C_{s,n}(k)=0\). If exactly one equality \(k_a=k_b=r\) occurs among its entries, then
\[
\boxed{C_{s,n}(k)=(-1)^{s-1}\binom{n-2}{s-1}
\prod_{j\notin\{a,b\}}\frac{1}{2\pi i(k_j-r)}\ne0.}
\]
For positive integers \(N\), count the nonzero coefficients among \(|k_j|\le N\) for \(1\le j<n\):
\[
S_{s,n}(N)=\#\{(k_1,\ldots,k_{n-1})\in[-N,N]^{n-1}\cap\mathbb Z^{n-1}:C_{s,n}(k_1,\ldots,k_{n-1},0)\ne0\}.
\]
Then, uniformly over all interior hypersimplex levels \(2\le s\le n-2\),
\[
\boxed{S_{s,n}(N)=\binom n2(2N)^{n-2}+O_n(N^{n-3})\quad(N\to\infty).}
\]
In particular the nonzero integer Fourier modes have leading codimension one, with **the same sharp leading constant for every interior slice**. For any two such levels \(s,t\), at every frequency having exactly one equality, the coefficients obey the exact universal ratio
\[
\frac{C_{s,n}(k)}{C_{t,n}(k)}=(-1)^{s-t}\frac{\binom{n-2}{s-1}}{\binom{n-2}{t-1}}.
\]
No complete classification of higher-multiplicity collision frequencies is claimed.

## Assumptions and scope

Here \(n\) and \(s\) are integers in the indicated ranges. The coordinates \(k_j\) are integers, not real frequencies. The Fourier exponent uses \(2\pi\) and the minus sign above. Because \(\sum_jx_j=s\) is integral, adding any common integer to all \(k_j\) leaves the Fourier coefficient unchanged; choosing \(k_n=0\) gives an unambiguous representative. The measure \(d\mathcal H^{n-1}/\sqrt n\) is precisely \(dx_1\cdots dx_{n-1}\) after setting \(x_n=s-\sum_{j<n}x_j\). No limit in \(n\) is asserted: the remainder estimate is for fixed \(n\) as \(N\to\infty\).

## Proof

**1. A sliced-cube Laplace transform.** For every real \(u\), define \(F(u)\) by the same normalized Fourier integral on \(\{x\in[0,1]^n:\sum_jx_j=u\}\), and let \(F(u)=0\) outside \([0,n]\). Slicing Fubini's theorem gives, when \(\operatorname{Re}z>0\),
\[
\int_0^\infty F(u)e^{-zu}\,du
=\prod_{j=1}^n\frac{1-e^{-(z+2\pi i k_j)}}{z+2\pi i k_j}
=(1-e^{-z})^n R(z),\qquad R(z)=\prod_{j=1}^n(z+2\pi i k_j)^{-1}.
\]
Let \(h\) be the inverse Laplace transform of \(R\): it is the convolution of \(n\) functions \(u\mapsto\mathbf1_{u\ge0}e^{-2\pi i k_ju}\), hence continuous with \(h(0)=0\) for \(n\ge2\). By inversion of \((1-e^{-z})^n\), at each positive integer \(s<n\),
\[
F(s)=\sum_{j=0}^{s-1}(-1)^j\binom nj h(s-j).\tag{1}
\]

**2. Distinct poles.** If all \(k_j\) differ, the partial fractions of \(R\) have only simple poles. Write \(R(z)=\sum_j a_j(z+2\pi i k_j)^{-1}\). As \(R(z)=O(z^{-n})\) and \(n\ge2\), comparison of the \(z^{-1}\) coefficient shows \(\sum_j a_j=0\). Therefore \(h(m)=\sum_j a_je^{-2\pi i k_jm}=0\) for every positive integer \(m\). Equation (1) gives \(F(s)=0\).

**3. One double pole.** Suppose exactly two entries equal \(r\). Partial fractions have one term of order two,
\[
R(z)=\frac{A}{(z+2\pi i r)^2}+\sum_{v\in\operatorname{distinct}(k)}\frac{b_v}{z+2\pi i v},\qquad
A=\prod_{j\notin\{a,b\}}[2\pi i(k_j-r)]^{-1}.
\]
As before, the \(z^{-1}\) coefficient forces \(\sum_v b_v=0\). Laplace inversion now gives \(h(m)=Am\) for every positive integer \(m\). The finite binomial identity
\[
\sum_{j=0}^{s-1}(-1)^j\binom nj(s-j)=(-1)^{s-1}\binom{n-2}{s-1}
\]
follows by using the standard partial alternating binomial sums separately on \(s\sum(-1)^j\binom nj\) and \(\sum j(-1)^j\binom nj\). Substituting in (1) proves the stated coefficient. No factor vanishes, so it is nonzero.

**4. Sharp count.** Let \(H_{ab}\) be the integer-frequency hyperplane \(k_a=k_b\) in the \(n-1\) free coordinates \(k_n=0\). There are \(\binom n2\) distinct hyperplanes. Each contains exactly \((2N+1)^{n-2}\) grid points in the frequency box. Any intersection of two distinct such hyperplanes contains at most \((2N+1)^{n-3}\) points, because their defining equations are independent (including when an index is \(n\)). Thus the union has size \(\binom n2(2N+1)^{n-2}+O_n(N^{n-3})\). Frequencies outside the union vanish by Step 2; frequencies on exactly one hyperplane are nonzero by Step 3. Only intersections, numbering \(O_n(N^{n-3})\), remain undecided, and therefore the claimed count follows. Dividing the Step 3 formula for levels \(s,t\) proves the ratio identity.

## Verification

The accompanying `check_hypersimplex.py` verifies 552 exact binomial and collision-count identities, compares seven low-dimensional coefficients with alternate direct numerical integration (one coordinate integrated analytically), and tests four coefficients for the first nontrivial dimensions \(n=5\), \(s=2,3\) using deterministic Sobol cubature. It passed 552 exact checks and 11 integral checks. Run with Python 3, SciPy and NumPy using `python check_hypersimplex.py`. The proof above, not the finite checks, establishes all quantified claims.

## Relationship to prior work

Xu (2008) develops multivariate splines, exponential truncated powers, and cube-slicing volumes. Li (2011) studies the hypersimplex and its integral-slab realization and Ehrhart invariants. Diaz, Le and Robins (2016) give general Fourier transforms of polytopes via Stokes chains, including nongeneric frequency behavior. These works supply a natural framework and broad methods; the assertion here is a particular arithmetic distinction between no collisions and exactly one collision, its explicit nonvanishing coefficient, and a uniform sharp support-count law across all interior levels. The general formulas alone do not state those counts and require specialization and confluent-pole analysis to obtain them. The previously accessible simplexes and the four-dimensional ambient octahedron are deliberately outside the novel \(n\ge5\) range. A hidden equivalent formula in earlier spline or Fourier-polytope literature remains a genuine originality risk.

## Limitations

The support asymptotic does not determine exact support for modes with two or more coordinate equalities. The implied constant depends on \(n\); no joint \(n,N\) limit is established. The Fourier normalization is part of the theorem and cannot be changed without adjusting coefficients. General explicit polytope-Fourier machinery may subsume the statement after nontrivial specialization, so independent literature review remains important. Numerical tests are finite corroboration, not a substitute for the infinite proof.

## References

1. Zhiqiang Xu, *Multivariate Splines and Polytopes*, first public arXiv version 2008-06-06, arXiv:0806.1127. https://arxiv.org/abs/0806.1127
2. Nan Li, *Ehrhart h-star vectors of hypersimplices*, first public arXiv version 2011-04-28, arXiv:1104.5292. https://arxiv.org/abs/1104.5292
3. Ricardo Diaz, Quang-Nhat Le, and Sinai Robins, *Fourier transforms of polytopes, solid angle sums, and discrete volume*, first public arXiv version 2016-02-27, arXiv:1602.08593. https://arxiv.org/abs/1602.08593
