# A parity law for the second conjugate-gradient iterate on discrete Poisson paths

## Finding
For every integer \(k\ge2\), standard exact-arithmetic conjugate gradients (CG), started at zero for a one-dimensional Dirichlet Poisson system, has a **sharp parity-dependent sign law** at its second iterate for a natural family of nonnegative, discrete-hat right-hand sides. An arbitrarily weak isolated positive load produces a *negative* second-iterate component when the remote hat has two peak entries, but a *positive* one when the hat has one peak entry. In the two-peak case the isolated-load amplitude has a unique exact positivity-recovery threshold, which approaches one as the hat widens.

For every integer \(n\ge2k+4\), let \(A_n\in\mathbb R^{n\times n}\) be the tridiagonal matrix with diagonal \(2\) and immediate off-diagonals \(-1\). Let \(r>0\), and use one-based indices to set
\[
 b=(r,0,0,1,2,\ldots,k-1,k,k,k-1,\ldots,2,1,0,\ldots,0)^\mathsf T.
\]
The two entries at height \(k\) make a length-\(2k\) plateau hat; there is at least one trailing zero. Denote by \(x^{(2)}\) the **second CG iterate** from \(x^{(0)}=0\). Put
\[
 A_k=\frac{8k^3+12k^2+22k-30}{3},\quad
 B_k=\frac{4k^3+6k^2+2k}{3},\quad
 C_k=\frac{4k^3-18k^2+26k}{3},
\]
\[
 N_k(r)=2r^4-2r^3+A_kr^2-B_kr-C_k.
\]
There is exactly one \(r_k\in(0,1)\) with \(N_k(r_k)=0\). The exact sign law is
\[
 \operatorname{sgn}(x^{(2)}_1)=\operatorname{sgn}N_k(r)
 =\begin{cases}-1,&0<r<r_k,\\0,&r=r_k,\\+1,&r>r_k.\end{cases}
\]
The thresholds satisfy \(r_k=1-2/k+O(k^{-2})\). For the shortest plateau hat \(k=2\), \(r_2\approx0.633525020339\). For every \(n\ge8\), the integer right-hand side
\[
 b=(1,0,0,2,4,4,2,0,\ldots,0)^\mathsf T
\]
produces the **exact negative value** \(x^{(2)}_1=-58/171\).

For comparison, let \(n\ge2k+3\) and replace the plateau by the length-\(2k-1\) peaked hat
\[
 b=(r,0,0,1,2,\ldots,k-1,k,k-1,\ldots,2,1,0,\ldots,0)^\mathsf T.
\]
Then
\[
 \lim_{r\downarrow0}\frac{x^{(2)}_1}{r}=\frac{k}{3}>0.
\]
For the plateau hat the corresponding limit is strictly negative:
\[
 \lim_{r\downarrow0}\frac{x^{(2)}_1}{r}
 =-\frac{k(2k^2-9k+13)}{6(3k-4)}<0.
\]
This last odd-hat assertion is a **small-amplitude sign result**, not a classification of all amplitudes. In both cases the exact solution \(A_n^{-1}b\) is strictly positive in every coordinate for every \(r>0\).

## Assumptions and scope
All operations are exact real arithmetic. CG is the unpreconditioned standard method solving \(A_nx=b\), initialized with \(x^{(0)}=0\), with residual \(b\) and ordinary Euclidean inner products. The matrix \(A_n\) is symmetric positive definite and inverse-positive. The scale of its entries is fixed at diagonal \(2\), neighbor entries \(-1\). Hat profiles and the isolated load have the exact positions displayed; appending zeros does not change the second iterate's first coordinate. No claim is made about arbitrary right-hand sides or subsequent iterations.

## Proof
**1. A two-dimensional Krylov identity.** For any symmetric positive definite matrix \(A\) and any nonzero \(b\) for which \(b\) and \(Ab\) are linearly independent, write
\[
 m_0=b^\mathsf Tb,\quad m_1=b^\mathsf TAb,\quad
 m_2=(Ab)^\mathsf TAb,\quad m_3=(Ab)^\mathsf TA(Ab),
 \qquad D=m_1m_3-m_2^2.
\]
The two-step CG iterate minimizes \(x^\mathsf TAx/2-b^\mathsf Tx\) in \(\operatorname{span}\{b,Ab\}\). Solving the \(2\times2\) Galerkin normal equations gives
\[
 x^{(2)}=\frac{m_0m_3-m_1m_2}{D}\,b
            -\frac{m_0m_2-m_1^2}{D}\,Ab.
\]
The strict Cauchy--Schwarz inequality in the \(A\)-inner product gives \(D>0\). In either proposed load, \(b_2=0\), but \((Ab)_2=-r\ne0\), so independence is automatic. Since \(b_1=r\) and \((Ab)_1=2r\),
\[
 x^{(2)}_1=\frac{r}{D}\left[m_0m_3-m_1m_2
                  -2(m_0m_2-m_1^2)\right].
\]

**2. Moment identities for the two hat shapes.** The one-dimensional difference operator is \((Av)_j=2v_j-v_{j-1}-v_{j+1}\) with Dirichlet ghost values zero. The squared masses of the peak and plateau hats are, respectively,
\[
 S_o=k(2k^2+1)/3,\qquad S_e=k(k+1)(2k+1)/3.
\]
Directly summing the first differences and their neighbor products yields
\[
\begin{array}{c|c|c|c|c}
& m_0&m_1&m_2&m_3\\\hline
\text{one peak}&r^2+S_o&2r^2+2k&5r^2+6&14r^2-2r+12\\
\text{two peaks}&r^2+S_e&2r^2+2k&5r^2+4&14r^2-2r+6
\end{array}
\]
for all the stated \(n\), including minimal dimensions. For example the energy \(p^\mathsf T A p\) of either hat is \(2k\); the squared \(Ap\)-norm is \(6\) with a single kink or \(4\) with a plateau. The linear term \(-2r\) in \(m_3\) comes from the unique interaction between the isolated load's nearest-neighbor difference and the hat's leading boundary difference. These local calculations are reproducible as exact fractions by the accompanying checker.

**3. The two-peak frontier.** Substitution of the plateau moments into Step 1 gives exactly \(x^{(2)}_1=rN_k(r)/D\), with \(N_k\) stated above. Since
\[
 C_k=\frac{2k(2k^2-9k+13)}3>0,
 \quad N_k(0)=-C_k<0,
 \quad N_k(1)=2(k+1)(4k-5)>0,
\]
and
\[
 N_k''(r)=24(r-1/4)^2+2A_k-3/2>0
 \qquad(r\ge0,k\ge2),
\]
the polynomial first decreases and then strictly increases, with precisely one positive zero, located in \((0,1)\). The strict sign inequalities and boundary equality follow because \(r/D>0\).

For the asymptotics, uniformly for \(0\le r\le1\),
\[
 k^{-3}N_k(r)=\frac43(2r+1)(r-1)+O(k^{-1}).
\]
Thus the unique root tends to \(1\). Moreover \(N_k(1)=8k^2+O(k)\) and \(N_k'(1)=4k^3+O(k^2)\), while \(N_k''=O(k^3)\) on \([0,1]\); Taylor's formula in a neighborhood of \(1\) gives \(r_k=1-2/k+O(k^{-2})\). The finite witness follows by substituting \(k=2\), \(r=1/2\): \(x^{(2)}_1=-29/171\), and multiplying the entire right-hand side by two, exploiting CG's linear homogeneity for fixed \(A\).

**4. The single-peak comparison.** At \(r=0\), the single-peak moments have \(D=12(2k-3)\) and the numerator in Step 1 equals \(4k(2k-3)\). Continuity and \(D>0\) give \(\lim_{r\downarrow0}x^{(2)}_1/r=k/3\). For the plateau moments, \(D=12k-16\) and numerator \(-C_k\), giving the claimed negative limit.

**5. Positivity of the exact solution.** The explicit inverse Green matrix is
\[
 (A_n^{-1})_{ij}=\frac{\min(i,j)[n+1-\max(i,j)]}{n+1}>0
 \qquad(1\le i,j\le n).
\]
Every allowed \(b\) is nonnegative and nonzero, so every exact solution coordinate is strictly positive. This establishes a genuine transient sign defect rather than a negative exact solution.

## Verification
Run `python3 verify.py` with the included standalone Python standard-library file. It reconstructs the matrix-vector products and both CG iterations using rational arithmetic; checks the four moments, numerator, and Galerkin formula for \(2\le k\le35\), seven rational amplitudes and two amounts of zero padding; verifies strict moment determinants and sign endpoints; and certifies the integer witness \(-58/171\). The checker covers \(952\) exact test cases and does not replace the proof for unbounded \(k,n,r\).

## Relationship to prior work
Classical conjugate gradients and Krylov optimality are described by Shewchuk (1994). Beckermann and Kuijlaars (2002) investigate the **same Dirichlet finite-difference Poisson matrix**, and the dependence of CG convergence rates on the right-hand side, but study asymptotic energy-norm convergence for different forcing families. Those results do not give the present second-iterate, single-coordinate sign frontier for triangular versus plateau loads. The inverse-positive matrix property does not imply positivity of intermediate Krylov iterates. Published studies of non-negative CG methods motivate the distinction but do not, in their available summaries, state the present exact parity and amplitude threshold; see the risk described below.

## Limitations
The complete threshold classifies only the first coordinate of the second iterate for the two-peak load family. For the one-peak family, only the small-isolated-load sign is determined here. No claim is made about all components, all CG steps, floating-point behavior, arbitrary load placements, or uniqueness in all historical literature. A recent specialized nonnegative-CG manuscript was not available in full and remains a source of possible overlap. All finite tests are illustrations of the proven infinite-family identities, not exhaustive enumerations of all problems.

## References
1. Jonathan R. Shewchuk, *An Introduction to the Conjugate Gradient Method Without the Agonizing Pain*, edition 1, August 4, 1994, author's full text: https://www.cs.cmu.edu/~quake-papers/painless-conjugate-gradient.pdf .
2. Bernhard Beckermann and Arno B. J. Kuijlaars, *Superlinear CG Convergence for Special Right-Hand Sides*, Electronic Transactions on Numerical Analysis **14** (2002), pp. 1–19, full text: https://etna.ricam.oeaw.ac.at/vol.14.2002/pp1-19.dir/pp1-19.pdf .
3. Schmelzer and Stoll, *Non-Negative Conjugate Gradients*, arXiv:2607.22121 (2026), abstract record: https://arxiv.org/abs/2607.22121 (full text not inspected).
