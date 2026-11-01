# Cubic spectral cutoff and peak law for mixed sixth character moments on \(SU(3)\)

## Finding
Let \(dg\) be probability Haar measure on \(SU(3)\). For every integer \(m\geq0\), let \(\chi_m\) be the unnormalized trace character of \(\operatorname{Sym}^m(\mathbb C^3)\). For every integer \(r\geq0\), define the natural mixed sixth character moment
\[
Q_m(r)=\int_{SU(3)}|\chi_m(g)|^4|\chi_r(g)|^2\,dg,
\qquad Q_m(-1)=0.
\]
Set \(\Delta_m(r)=Q_m(r)-Q_m(r-1)\). Then, exactly for all integer \(m,r\geq0\),
\[
\boxed{\Delta_m(r)=
\begin{cases}
(r+1)^2(m-r+1)+\binom{r+1}{3},&0\leq r\leq m,\\
\binom{2m-r+3}{3},&m\leq r\leq 2m,\\
0,&r>2m.
\end{cases}}
\]
The two expressions agree at \(r=m\); the binomial is zero when its top index is less than three. In particular, the moments increase strictly in \(r\) through \(r=2m\), and then saturate, sharply, at
\[
\boxed{Q_m(r)=\frac{(m+1)(m+2)(m^2+3m+3)}6 \quad(r\geq2m).}
\]
The diagonal sixth moment is
\[
\boxed{\int_{SU(3)}|\chi_m(g)|^6\,dg
=\frac12\binom{m+2}{2}\left(\binom{m+2}{2}+1\right).}
\]
For every \(m\geq1\), the nonnegative spectral coefficients \(\Delta_m(r)\), for \(0\leq r\leq2m\), are unimodal. Put
\[
t_m=\frac{4m-9+\sqrt{16m^2+48m+41}}{10}.
\]
If \(t_m\) is not an integer, the unique maximizer is \(r=\lceil t_m\rceil\). If it is an integer, the two consecutive maximizers are \(r=t_m\) and \(r=t_m+1\). Thus every maximizing index obeys \(r/m\to4/5\) as \(m\to\infty\).

## Assumptions and scope
All representations are finite-dimensional unitary \(SU(3)\) representations. We use **trace**, not dimension-normalized, characters; nevertheless \(\int|\chi_m|^2dg=1\) by Schur orthogonality. The labels \((j,j)\) below are Dynkin labels. Integers \(m,r\) are arbitrary and nonnegative; no asymptotic assumption or unmentioned normalization is used. The value \(m=0\) gives \(Q_0(r)=1\), \(\Delta_0(0)=1\), and \(\Delta_0(r)=0\) for \(r>0\), with the peak assertion restricted to \(m\geq1\).

## Proof
**1. Decompose the squared trace characters.** The Pieri rule for \(SU(3)\), equivalently for its three-row Schur functions after removing determinant columns, gives the multiplicity-free identity
\[
\chi_m\overline{\chi_m}=\sum_{i=0}^{m}\chi_{(i,i)}.
\]
Consequently
\[
Q_m(r)=\sum_{0\leq i,j\leq m}\sum_{0\leq k\leq r}N(i,j,k),
\quad
\Delta_m(r)=\sum_{0\leq i,j\leq m}N(i,j,r),
\]
where \(N(i,j,k)=\int\chi_{(i,i)}\chi_{(j,j)}\chi_{(k,k)}\,dg\) is a nonnegative integer (all \((j,j)\) irreducibles are self-dual).

**2. Specialize the known \(SU(3)\) tensor multiplicity formula.** The explicit general triple-coupling rule of Bégin--Mathieu--Walton [1, equations (4)--(5)] has \(k_0^{\max}=i+j+k\) and
\[
k_0^{\min}=\max\{2i,2j,2k,i+j+k-\min(i,j,k)\}
\]
when all three Dynkin-label pairs are \((i,i),(j,j),(k,k)\). Hence
\[
N(i,j,k)=\max\{0,1+\min(i,j,k,i+j-k,i+k-j,j+k-i)\}.
\]
This specialized identity is used as prior mathematics, not claimed as a new tensor-product theorem. It says that \(N(i,j,k)\) counts integers \(h\geq0\) with \(h\leq\min(i,j,k)\) and \(i+j-k,j+k-i,k+i-j\geq h\). Subtracting \(h\) from all three indices reduces the latter inequalities to the triangle inequalities for \((i-h,j-h,k-h)\).

**3. Count the lattice triangles when \(0\leq r\leq m\).** For each \(0\leq h\leq r\) put \(M=m-h\), \(q=r-h\) and \(d=m-r=M-q\geq0\). The number of pairs \(0\leq a,b\leq M\) with \(|a-b|\leq q\leq a+b\) is
\[
(M+1)^2-(M-q)(M-q+1)-\frac{q(q+1)}2.
\]
Indeed, the two disjoint forbidden off-diagonal triangles total \((M-q)(M-q+1)\) pairs, and the forbidden region \(a+b<q\) contains \(q(q+1)/2\) pairs and is disjoint from the former. Summing over \(h\), and substituting \(q=r-h\), gives
\[
\Delta_m(r)=\sum_{q=0}^{r}\left((d+q+1)^2-d(d+1)-\frac{q(q+1)}2\right)
=(r+1)^2(d+1)+\binom{r+1}{3}.
\]
This proves the first branch.

**4. Count the opposite range.** If \(m\leq r\leq2m\), for a fixed \(h\), \(q=r-h\geq M=m-h\), so \(|a-b|\leq q\) holds automatically. The number of pairs with \(a+b\geq q\) equals \(\binom{2M-q+2}{2}\) when \(q\leq2M\), and is zero otherwise. Thus
\[
\Delta_m(r)=\sum_{h=0}^{2m-r}\binom{2m-r-h+2}{2}
=\binom{2m-r+3}{3}.
\]
For \(r>2m\), there are no admissible triangles. Every displayed coefficient through \(2m\) is positive, proving strict growth and the exact cutoff.

**5. Saturation, diagonal, and peak.** For each fixed pair \(i,j\), the triangular-profile multiplicities satisfy \(\sum_{k\geq0}N(i,j,k)=(\min(i,j)+1)^2\). Hence
\[
Q_m(2m)=\sum_{i,j=0}^{m}(\min(i,j)+1)^2
=\sum_{u=1}^{m+1}u^2(2m-2u+3)
=\frac{(m+1)(m+2)(m^2+3m+3)}6.
\]
At the diagonal, summing the first branch gives the stated half-triangular-number formula. For \(0\leq r<m\), subtracting successive values in the first branch yields
\[
\Delta_m(r+1)-\Delta_m(r)
=\frac{-5r^2+(4m-9)r+6m-2}{2}.
\]
The quadratic has one negative root and one positive root \(t_m\), with \(0<t_m<m\) for every \(m\geq1\). The second branch decreases strictly from \(r=m\) onward. The sign change of the displayed quadratic gives the unique or tied maximizers stated above. Expansion of the square root shows \(t_m=(4/5)m-3/10+O(m^{-1})\).

## Verification
Run \(\texttt{python3 checker.py}\) from a directory containing the supplied standalone checker. It independently enumerates all triple-coupling multiplicities, computes exact Haar integrals by Weyl's torus constant-term formula for small indices (without calling the coupling formula), checks the piecewise polynomial for many values, and checks the diagonal identity. The completed checker passed 540 assertions. Exact finite computations test the derivation but are not proofs for unbounded indices.

## Relationship to prior work
Bégin--Mathieu--Walton [1] established the general \(SU(3)\) triple tensor-product multiplicity formula used in Step 2. Martins--Suffak--de Guise [2] develops \(SU(3)\) Clebsch--Gordan coefficients, Weyl symmetries and multiplicity-free coupling techniques; its inspected sections do not evaluate this mixed sixth-moment family. The new assertion is the evaluated **two-parameter Haar-moment profile**, its two cubic branches, sharp saturation, and spectral peak near four-fifths of the base symmetric-power degree—not a new formula for individual Clebsch--Gordan coefficients. Its deduction depends crucially on the known general coupling rule and a separate lattice-triangle summation.

## Limitations
The classification concerns the one-parameter family of symmetric powers of the defining three-dimensional \(SU(3)\) representation and the mixed moment with two equal degrees. It does not classify all triple-degree mixed moments, general highest-weight families, or other compact groups. Existing general tensor-product formulas determine individual summands and present a potential indirect historical-priority relation; no assertion of independently verified priority is made.

## References
[1] L. Bégin, P. Mathieu, and M. A. Walton, "\(\widehat{su}(3)_k\) fusion coefficients," *Modern Physics Letters A* **7** (1992), 3255–3266; preprint arXiv:hep-th/9206032 (first submitted 1992-06-08), especially equations (4)–(5). https://arxiv.org/html/hep-th/9206032v1

[2] A. C. N. Martins, M. W. Suffak, and H. de Guise, "\(SU(3)\) Clebsch–Gordan coefficients and some of their symmetries," arXiv:1909.09055 (first submitted 2019-09-19). https://ar5iv.labs.arxiv.org/html/1909.09055
