# Spectral-hyperplane rigidity and the parity criterion for finite Turán boxes

## Finding
Let \(d\ge1\), let \(n_j\ge3\) be integers, let
\[
G=\prod_{j=1}^d\mathbb Z/n_j\mathbb Z,
\qquad
\Omega=\prod_{j=1}^d\{0,-1,1\},
\]
and let \(f:G\to\mathbb C\) be positive definite, normalized by \(f(0)=1\), with \(f(x)=0\) for \(x\notin\Omega\). Write \(M(f)=\sum_{x\in G}f(x)\), which is real and nonnegative by positive definiteness. Define
\[
C(n)=\begin{cases}
1+\sec(\pi/n),&n\text{ odd},\\
2,&n\text{ even}.
\end{cases}
\]
Then \(\max_f M(f)=\prod_{j=1}^d C(n_j)\). The scalar product formula follows from previously known Turán tensorization and the elementary one-dimensional bound; it is included to normalize the equality question.

**Equality classification:** the normalized maximizer is **unique if and only if every \(n_j\) is odd**. When all \(n_j\) are odd, it is necessarily the tensor product
\[
f_*(x)=\prod_{j=1}^d h_{n_j}(x_j),\qquad
h_n(0)=1,\quad h_n(\pm1)=\frac{1}{2\cos(\pi/n)},\quad
h_n(t)=0\text{ otherwise}.
\]
Its Fourier transform vanishes at precisely those frequency tuples \(k\) for which at least one coordinate is \(k_j=(n_j-1)/2\) or \(k_j=(n_j+1)/2\) modulo \(n_j\). Thus the exact number of nonzero Fourier coefficients of the unique maximizer is \(\prod_j(n_j-2)\).

If at least one \(n_j\) is even, there are uncountably many different normalized maximizers; in particular the equality face is not a singleton. This includes arbitrarily high-dimensional boxes with mixed odd and even side lengths.

## Assumptions and scope
The group is finite, the Fourier transform is **unnormalized**, and its sign convention is
\[
\widehat f(k)=\sum_{x\in G}f(x)
\exp\left(-2\pi i\sum_j k_jx_j/n_j\right).
\]
Positive definiteness means that every matrix \((f(x_r-x_s))_{r,s}\) is Hermitian positive semidefinite. Equivalently, \(\widehat f(k)\ge0\) for all \(k\). There are no positivity or reality requirements on spatial coefficients beyond positive definiteness. The three residues \(0,1,-1\) are distinct because \(n_j\ge3\). The objective uses counting measure; normalized Haar measure divides all masses by \(|G|\).

## Proof
**Step 1: one-dimensional inequality and equality contacts.** Let \(q\) be positive definite on \(\mathbb Z/n\mathbb Z\), supported on \(\{0,\pm1\}\), with \(q(0)=t\ge0\), \(q(1)=u\), and \(q(-1)=\overline u\). If \(n=2m+1\) is odd, put \(c=\cos(\pi/n)\) and \(\theta=2\pi m/n=\pi-\pi/n\). The two Fourier inequalities at \(k=m\) and \(k=-m\) give
\[
0\le\widehat q(m)+\widehat q(-m)
=2t-4c\operatorname{Re}u.
\]
Hence \(\sum_xq(x)=t+2\operatorname{Re}u\le(1+c^{-1})t\). Equality requires both nonnegative Fourier coefficients at \(\pm m\) to vanish. Subtracting their equations gives \(\operatorname{Im}u=0\), because \(\sin\theta\ne0\). Therefore \(u=t/(2c)\) is the only equality case. It is feasible because \(1+c^{-1}\cos(2\pi k/n)\ge0\) for every integer \(k\), with equality exactly at \(k=\pm m\). This includes \(n=3\).

For even \(n=2m\ge4\), the Fourier inequality at \(k=m\) gives \(2\operatorname{Re}u\le t\), hence \(\sum_x q(x)\le2t\). Equality holds for the entire family
\[
q(1)=\frac t2+i s,\qquad q(-1)=\frac t2-i s,
\qquad |s|\le\frac t2\tan(\pi/n).
\]
Indeed, Fourier positivity becomes \(t(1+\cos\phi)+2s\sin\phi\ge0\) for the grid angles \(\phi=2\pi k/n\). The two samples closest to \(\pi\) give the stated restriction and every other grid sample is weaker. For \(t>0\), this interval contains nonzero values of \(s\).

**Step 2: tensor upper bound, including all coordinate orders.** If \(g\) is positive definite on \(H\times K\), then \(x\mapsto\sum_{y\in K}g(x,y)\) is positive definite: its Fourier transform at a character of \(H\) equals \(\widehat g\) at that character paired with the trivial character of \(K\), and is nonnegative. The restriction \(y\mapsto g(0,y)\) is also positive definite. Summing one coordinate at a time and applying Step 1 therefore yields
\[
\sum_{x\in G} f(x)\le\prod_{j=1}^d C(n_j)f(0).
\]
All coordinate summation orders are allowed, and the product of one-dimensional optimizers attains equality. If global equality holds, choose an order leaving coordinate \(j\) to the end. Equality of the chained nonnegative inequalities forces the axis restriction \(u_j(t)=f(t e_j)\) to attain the one-dimensional bound for that \(j\).

**Step 3: Fourier hyperplanes annihilate every spatial slice.** Suppose \(n_j\) is odd and global equality holds. Step 1 says \(\widehat u_j(\pm m_j)=0\), where \(m_j=(n_j-1)/2\). Fourier inversion and nonnegativity give
\[
0=\widehat u_j(\pm m_j)
=\frac{1}{\prod_{i\ne j}n_i}
\sum_{k_i,\,i\ne j}\widehat f(k_1,\ldots,\pm m_j,\ldots,k_d).
\]
Every summand is nonnegative, so the full Fourier transform vanishes on both coordinate hyperplanes \(k_j=\pm m_j\). Inverting in all frequencies except coordinate \(j\), for every \(y\in\prod_{i\ne j}\mathbb Z/n_i\mathbb Z\) we obtain
\[
f(0,y)+e^{\mp i\theta_j}f(1,y)
+e^{\pm i\theta_j}f(-1,y)=0,
\qquad \theta_j=\pi-\pi/n_j.
\]
Subtracting the two equations forces \(f(1,y)=f(-1,y)\); substitution then yields
\[
f(1,y)=f(-1,y)=\frac{f(0,y)}{2\cos(\pi/n_j)}.
\]
There is no division by zero since \(n_j\ge3\) is odd. The displayed identities hold also for \(y\) outside the other coordinate support because both sides then vanish.

**Step 4: uniqueness and parity converse.** If all side lengths are odd, apply Step 3 independently in every coordinate. Repeated factorization determines every value of \(f\) as \(f(0)\prod_jh_{n_j}(x_j)\), hence yields exactly \(f_*\). Since \(\widehat{h_n}(k)=1+\cos(2\pi k/n)/\cos(\pi/n)\), its only zeros are the two stated odd-cycle contact frequencies, and Fourier multiplication gives the announced support mask and cardinality. If some side length is even, Step 1 gives a nontrivial continuum of complex one-dimensional maximizing factors on that coordinate. Tensor them with fixed maximizing factors on all other coordinates to obtain a continuum of distinct normalized global maximizers. This proves the if-and-only-if assertion.

## Verification
The standalone script `checker.py` evaluates the unnormalized complex discrete Fourier transforms directly, checks sharp masses and positivity for all cyclic lengths from 3 to 23, checks exact odd-cycle Fourier zero masks, verifies allowable and forbidden even-cycle imaginary phases, and tests product configurations including three dimensions. At the time of preparation it returned `PASS 81 Fourier-positivity, sharp-mass, odd-grid-zero-mask, and even-phase checks`. These finite calculations corroborate rather than replace Steps 1–4, which prove the theorem for all finite side lengths and dimensions.

## Relationship to prior work
Gorbachev–Manoshina (2002) reduce the periodic small-support Turán problem to finite-dimensional linear programs, including the three-point discrete case. Kolountzakis–Révész (2003 preprint; 2006 journal version), Corollary 2, establish multiplicativity of Turán constants on Cartesian products. Accordingly, the scalar constant in this finding is **not** claimed as new. The statement isolated here is the complete complex maximizing-function rigidity criterion: the all-odd product has exactly one optimizer, whereas an even side creates infinitely many optimizers. The spectral-hyperplane propagation proof makes the distinction between equality of scalar constants and equality of optimizing functions explicit. The published material inspected for this comparison did not present this all-dimensional parity criterion.

## Limitations
The theorem applies only to coordinatewise three-point boxes on products of cyclic groups with side lengths at least three. It does not classify the complete higher-dimensional maximizing face when an even coordinate exists; it proves only its nonuniqueness and gives an explicit continuum. The previously known scalar tensorization is not an independent novelty claim. The originality review cannot exclude an equivalent implicit rigidity argument in uninspected literature, particularly work on positive trigonometric polynomials and tensor-product extremizers. Independent mathematical verification has not been performed.

## References
1. D. V. Gorbachev and A. S. Manoshina, *Turan Extremum Problem for Periodic Function with Small Support*, initial public arXiv posting 19 November 2002, arXiv:math/0211291. https://arxiv.org/abs/math/0211291
2. M. N. Kolountzakis and S. Gy. Révész, *Turán's extremal problem for positive definite functions on groups*, initial public arXiv posting 10 December 2003, arXiv:math/0312218, particularly Corollary 2 on Cartesian products. https://arxiv.org/abs/math/0312218
3. S. Krenedits and S. Gy. Révész, *The Carathéodory–Fejér type extremal problem on locally compact Abelian groups*, arXiv:1304.0071 (2013), concerning point-value rather than box mass-optimizer classification. https://arxiv.org/abs/1304.0071
