# A five-symbol dependence threshold for a hyperbolic toral half-circle sensor

## Finding

Consider the toral automorphism
\[
 A=\begin{pmatrix}1&1&0\\1&2&1\\0&1&2\end{pmatrix},\qquad
 T(x)=Ax\pmod{\mathbb Z^3},\qquad x\in\mathbb T^3.
\]
Draw \(X\) from Haar probability measure, and for every integer \(n\ge0\) define
\[
 U_n=(A^nX)_1\pmod1,\qquad
 S_n=\begin{cases}+1,&0\le U_n<1/2,\\-1,&1/2\le U_n<1.\end{cases}
\]
The stationary sign process has three exact properties.

1. For **any three distinct nonnegative times**, the corresponding signs are independent fair signs. For **any four consecutive times**, their signs are also independent.
2. For all \((s_0,s_1,s_2,s_3,s_4)\in\{-1,+1\}^5\), the exact five-symbol law is
   \[
   \boxed{\Pr(S_0=s_0,\ldots,S_4=s_4)=\frac1{32}\left(1+\frac{s_0s_1s_2s_4}{8265}\right).}
   \]
   Thus the first four consecutive observations cannot reveal the dependence, while the fifth can. The conditional prediction has the explicit form
   \[
    \Pr(S_4=s\mid S_0=s_0,\ldots,S_3=s_3)=\frac12\left(1+\frac{s\,s_0s_1s_2}{8265}\right).
   \]
3. More generally, let \(0\le n_0<n_1<n_2<n_3\) and \(v_n=e_1^{\mathsf T}A^n\in\mathbb Z^3\). There is a unique primitive integer relation \(\sum_{j=0}^3c_jv_{n_j}=0\), up to changing all signs simultaneously. Every \(c_j\) is nonzero, and
   \[
   \boxed{\mathbb E\left[\prod_{j=0}^3S_{n_j}\right]=
     \begin{cases}0,&\text{at least one }c_j\text{ is even},\\
     \displaystyle\frac1{3c_0c_1c_2c_3},&\text{all four }c_j\text{ are odd}.
     \end{cases}}
   \]
   The right-hand side is unaffected by the simultaneous sign reversal of four coefficients. Consequently, these four observations are independent **if and only if** some \(c_j\) is even. If all coefficients are odd their full four-sign law is \(2^{-4}(1+\rho\prod_j s_j)\), with \(\rho=1/(3\prod_jc_j)\).

## Assumptions and scope

The transformation acts on the real three-dimensional torus with Haar probability measure. Time indices are distinct nonnegative integers. Endpoints of half-circle cuts have Haar measure zero; the displayed convention fixes values there without affecting probabilities. The theorem concerns this explicit sign observable and makes no assertion of independence for arbitrary observables or of optimality across other automorphisms.

The matrix is symmetric positive definite, of determinant one, with characteristic polynomial
\[q(t)=t^3-5t^2+6t-1.\]
Its three eigenvalues are positive, distinct, and different from one; thus \(T\) is an invertible hyperbolic toral automorphism preserving Haar measure. Its sign process is stationary.

## Proof

**Three-time independence.** Set \(v_n=e_1^{\mathsf T}A^n\). The first rows are
\[
 v_0=(1,0,0),\quad v_1=(1,1,0),\quad v_2=(2,3,1),\quad
 v_3=(5,9,5),\quad v_4=(14,28,19).
\]
The first three have determinant one. Since \(A\) is real symmetric with three distinct positive eigenvalues \(\lambda_1,\lambda_2,\lambda_3\), this Krylov determinant also shows that \(e_1\) has a nonzero component along every eigenvector. If three distinct vectors \(v_{n_0},v_{n_1},v_{n_2}\) were dependent, a nonzero polynomial with at most three monomials,
\[p(t)=a_0t^{n_0}+a_1t^{n_1}+a_2t^{n_2},\]
would vanish at all three positive eigenvalues. Descartes' rule of signs bounds the number of positive roots of such a nonzero polynomial by two (including the case of some zero coefficients). Contradiction. Hence **every** three distinct rows are linearly independent over \(\mathbb R\). The integer row matrix with these rows defines a surjective continuous homomorphism \(\mathbb T^3\to\mathbb T^3\); its Haar pushforward is Haar measure. Therefore the three corresponding \(U\)-variables are independent uniform circle variables. In particular, any three \(S\)-variables are independent fair signs.

**Fourth-order circuit formula.** Any four distinct rows span \(\mathbb R^3\), with every triple independent. Their one-dimensional rational kernel therefore has a primitive integer generator \(c=(c_0,c_1,c_2,c_3)\), with no zero coefficient. Let \(g(u)=1\) on \([0,1/2)\) and \(g(u)=-1\) otherwise. Its Fourier coefficients are
\[
 \widehat g(m)=\begin{cases}\dfrac2{\pi im},&m\text{ odd},\\0,&m\text{ even},\end{cases}
\quad(m\ne0),\qquad \widehat g(0)=0.
\]
Smooth \(g\) by the circle Poisson kernel at radius \(0<r<1\). The smoothed functions have absolutely convergent Fourier expansions, are bounded in absolute value by one, and converge almost everywhere to \(g\). Haar integration kills every Fourier character except those with integer frequency vector \(m=(m_0,\ldots,m_3)\) satisfying \(\sum m_jv_{n_j}=0\). Precisely those frequencies are \(m=\ell c\), for \(\ell\in\mathbb Z\). If some \(c_j\) is even, all surviving terms contain an even Fourier frequency and vanish. If all \(c_j\) are odd, the only contributing \(\ell\) are odd. Letting the Poisson radius tend to one and using dominated convergence and the absolutely convergent \(\sum_{\ell\ne0}|\ell|^{-4}\) gives
\[
 \mathbb E\prod_{j=0}^3S_{n_j}
 =\frac{16}{\pi^4\prod_{j=0}^3c_j}
   \sum_{\substack{\ell\in\mathbb Z\\\ell\text{ odd}}}\frac1{\ell^4}
 =\frac{16}{\pi^4\prod c_j}\,\frac{\pi^4}{48}
 =\frac1{3\prod c_j}.
\]
All proper nonempty subsets of the four signs have zero mixed sign moment by three-time independence. Fourier–Walsh inversion on \(\{-1,+1\}^4\) then yields their full law and the equivalence between zero fourth moment and independence.

**Four consecutive signs.** Cayley–Hamilton gives
\[A^3-5A^2+6A-I=0.\]
After multiplication by \(e_1^{\mathsf T}A^n\), the coefficient vector for \((v_n,v_{n+1},v_{n+2},v_{n+3})\) is \((-1,6,-5,1)\). It is primitive with an even component. Thus the fourth-order moment is zero at every consecutive four-time block, so those four signs are jointly independent.

**The first five-sign law.** The five rows displayed above yield the following primitive relations on the five four-element subsets, in chronological subset order:
\[
\begin{array}{c|c}
\{0,1,2,3\}&(-1,6,-5,1)\\
\{0,1,2,4\}&(-5,29,-19,1)\\
\{0,1,3,4\}&(-6,31,-19,5)\\
\{0,2,3,4\}&(-1,31,-29,6)\\
\{1,2,3,4\}&(-1,6,-5,1)
\end{array}
\]
Every row is checked by direct integer substitution; the coefficients are primitive because their greatest common divisor is one. Thus exactly one four-element subset has nonzero moment:
\[
\mathbb E[S_0S_1S_2S_4]=\frac1{3(-5)(29)(-19)(1)}=\frac1{8265}.
\]
The full fifth-order moment is zero. Indeed, any nonzero Fourier contribution to \(\mathbb E[S_0S_1S_2S_3S_4]\) would require five **odd** integers \(m_0,\ldots,m_4\) with \(\sum m_iv_i=0\). Reduction modulo two would force \(\sum_{i=0}^4v_i=0\pmod2\), but this sum equals \((1,1,1)\pmod2\), contradiction. This is rigorously justified first for Poisson-smoothed observations (where Fourier sums are absolutely convergent), followed by dominated convergence. All one-, two-, and three-sign moments are zero; all four-sign moments but the displayed one vanish; the five-sign moment vanishes. Fourier–Walsh inversion therefore yields exactly the claimed five-sign formula and its conditional prediction. Since all four consecutive signs are independent and the five-block is not, the claimed first window length is sharp.

## Verification

The accompanying standard-library file `VERIFY_CHECKER.py` reconstructs the integer row vectors, validates the Cayley–Hamilton identity and all five primitive four-row relations, computes the nonzero fourth moment as an exact rational number, and checks the proposed five-sign law by exact finite enumeration of all sign patterns and their marginals. It also checks three-row nonsingularity for time indices below twelve, solely as an additional finite diagnostic, and compares with discrete-Fourier moments on two finite grids. Executing `python3 VERIFY_CHECKER.py` prints `VERIFY_OK`. None of those finite checks substitutes for the preceding all-time positive-root argument or Fourier proof.

## Relationship to prior work

Hyperbolic toral automorphisms, their Haar-invariant statistics and entropy are classical. Sun (2011) studies ergodic measures and entropy for linear toral automorphisms. Pollicott (2012) analyzes periodic-point growth of commuting higher-dimensional hyperbolic toral automorphisms; his three-dimensional example has the same real eigenvalue multiset as this matrix. The full-text material inspected for those papers does not give this half-circle observation process, its all-time four-point circuit parity criterion, or its exact five-symbol law. The sparse Fourier-resonance method is related to the general arithmetic-lacunarity framework surveyed by Aistleitner, Berkes, and Tichy (2023). That general framework is not itself claimed as new: the contribution here is the explicit dynamical instance, its complete fourth-order criterion, and the first non-Bernoulli block with exact rational probabilities.

## Limitations

The observation is a discontinuous binary partition of a smooth hyperbolic toral system; the same conclusion is not asserted for smooth sensors, perturbations of the matrix, or other half-interval locations. The theorem does not classify the whole infinite-order symbolic law or prove a universal minimum window length among all hyperbolic toral automorphisms. The computations corroborate but do not establish infinite-time claims. Published examples not recovered in the bibliographic searches could contain equivalent formulas, so independent historical priority review remains appropriate.

## References

1. P. Sun, *Entropy and Ergodic Measures for Toral Automorphisms*, arXiv:1103.1115v1, first publicly submitted 2011-03-06. https://arxiv.org/abs/1103.1115
2. M. Pollicott, *A Note on the Growth of Periodic Points for Commuting Toral Automorphisms*, 2012, DOI:10.5402/2012/165808. https://doi.org/10.5402/2012/165808
3. C. Aistleitner, I. Berkes, R. F. Tichy, *Lacunary sequences in analysis, probability and number theory*, arXiv:2301.05561 (2023). https://arxiv.org/abs/2301.05561
