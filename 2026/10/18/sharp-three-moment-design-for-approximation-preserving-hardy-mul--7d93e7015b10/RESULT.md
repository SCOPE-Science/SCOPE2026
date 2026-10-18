# Sharp three-moment design for approximation-preserving Hardy multipliers

## Finding
Fix an integer \(n\ge2\). Let \(\mu\) be a Borel probability measure on \(\mathbb T=\{\zeta\in\mathbb C:|\zeta|=1\}\) satisfying \(\widehat\mu(k)=\int_{\mathbb T}\zeta^{-k}\,d\mu(\zeta)=0\) for every \(1\le k\le n\). Put
\[
a=\widehat\mu(n+1),\qquad b=\widehat\mu(n+2),\qquad c=\widehat\mu(n+3).
\]
**Complete three-moment body.** A triple \((a,b,c)\in\mathbb C^3\) occurs for such a measure if and only if the upper-triangular Toeplitz matrix
\[
B(a,b,c)=\begin{pmatrix}a&b&c\\0&a&b\\0&0&a\end{pmatrix}
\]
is a contraction in Euclidean operator norm.

**Sharp aggregate optimum and all equality measures.** The exact maximum of the three first freely varying moment magnitudes is
\[
\max_\mu\bigl(|a|+|b|+|c|\bigr)=\frac{7+14\sqrt7}{27}=1.631130309440\ldots.
\]
Let \(r_*=(\sqrt7-1)/3\). Every maximizing triple, without exception, is
\[
|a|=r_*,\qquad |u|=1,\qquad b=(1-r_*^2)u,\qquad c=-(1-r_*^2)\overline a\,u^2.
\]
The two unrestricted phases of \(a\) and \(u\) give a two-torus of distinct maximizing measures. For each pair \((a,u)\), the **unique** realizing measure has exactly \(n+2\) positive atoms, at the \(n+2\) distinct unit-circle solutions \(\zeta_j\) of
\[
u z^{n+2}+a z^{n+1}-\overline a\,u z-1=0,\]
with explicit weights
\[
\mu=\sum_{j=1}^{n+2}w_j\delta_{\zeta_j},\qquad
w_j=\left(n+1+\frac{1-r_*^2}{|a+u\zeta_j|^2}\right)^{-1}.
\]
In particular, an optimal positive quadrature rule cannot use fewer than \(n+2\) distinct nodes.

**Hardy-multiplier formulation.** Let
\[
K_n(z)=z^n\int_{\mathbb T}\frac{d\mu(\zeta)}{1-z/\zeta}.
\]
For exactly the measures above with \(\widehat\mu(1)=\cdots=\widehat\mu(n)=0\), convolution by \(K_n\) is a normalized best-approximation-preserving Hadamard operator on \(H^\infty\). Therefore the same bound and equality classification apply to the first three free kernel coefficients \([z^{2n+1}]K_n\), \([z^{2n+2}]K_n\), and \([z^{2n+3}]K_n\).

## Assumptions and scope
The Fourier-moment convention is \(\widehat\mu(k)=\int\zeta^{-k}\,d\mu\). The assertion holds for every integer \(n\ge2\), with arbitrary positive Borel measures of total mass one, including discrete and continuous measures. The sharp equality formulas make sense for any phases \(|a|=r_*\) and \(|u|=1\). This theorem does **not** assert the same three-moment formula for \(n=0\) or \(n=1\): an extra lower-order moment interaction occurs for those indices. The operator norm on the matrix \(B\) is the ordinary spectral norm.

## Proof
**1. Moment feasibility.** Let \(m_j=\widehat\mu(j)\), \(m_0=1\), and \(m_{-j}=\overline{m_j}\). The truncated moment Toeplitz matrix \(T=(m_{j-i})_{0\le i,j\le n+3}\) is positive semidefinite. Order its indices as \(0,1,2\); then \(n+1,n+2,n+3\); then \(3,\ldots,n\). Since all moments of orders \(1,\ldots,n\) vanish, the resulting matrix is the orthogonal direct sum of an identity block and
\[
\begin{pmatrix}I_3&B(a,b,c)\\B(a,b,c)^*&I_3\end{pmatrix}.
\]
The latter is positive semidefinite precisely when \(I_3-B^*B\succeq0\), equivalently \(\|B\|_{\mathrm{op}}\le1\). Conversely, the truncated trigonometric moment theorem realizes every positive-semidefinite Toeplitz matrix with \(m_0=1\) by a positive probability measure on \(\mathbb T\); thus this condition is both necessary and sufficient.

**2. Reduction to three Schur coefficients.** Define the positive-real-part function
\[
F(z)=\int_{\mathbb T}\frac{1+z/\zeta}{1-z/\zeta}\,d\mu(\zeta)
=1+2\sum_{k\ge1}m_kz^k.
\]
Its Cayley transform \(S(z)=(F(z)-1)/(F(z)+1)\) satisfies \(|S(z)|\le1\). Since the first \(n\) moments vanish, the higher-order Schwarz lemma yields \(S(z)=z^{n+1}f(z)\) with \(f\) in the Schur class. As \(n\ge2\), the first three Taylor coefficients of \(f\) are precisely \(a,b,c\), since \(2(n+1)>n+3\). Conversely, each Schur function \(f\) gives a positive-real-part \(F=(1+z^{n+1}f)/(1-z^{n+1}f)\), and hence a representing probability measure realizing the prescribed first three coefficients. This supplies a second proof of the exact feasible-body claim.

**3. Sharp optimization.** If \(|a|=1\), Schwarz's lemma gives \(b=c=0\). Otherwise put \(r=|a|<1\). One Schur step writes
\[
f(z)=\frac{a+zg(z)}{1+\overline a\,zg(z)},
\qquad g(z)=u+vz+O(z^2),\qquad |u|\le1,
\]
where Schwarz--Pick gives \(|v|\le1-|u|^2\). Consequently
\[
b=(1-r^2)u,\qquad c=(1-r^2)(v-\overline a\,u^2).
\]
Writing \(s=|b|\), where \(0\le s\le1-r^2\), gives the **global** bound
\[
|a|+|b|+|c|\le1+r-r^2+s-\frac{s^2}{1+r}.
\]
For \(0\le r\le1/2\), the right side is maximized at \(s=(1+r)/2\) and equals at most \(5/4+5r/4-r^2\le13/8\). For \(1/2\le r\le1\), it is maximized at \(s=1-r^2\), yielding \(h(r)=1+2r-r^2-r^3\). Its unique maximum on this interval occurs at
\[
r=r_*=(\sqrt7-1)/3,
\qquad h(r_*)=(7+14\sqrt7)/27>13/8.
\]
Thus every global equality case forces \(r=r_*\) and \(|u|=1\). By equality in Schwarz's lemma, \(g\equiv u\), and so **the whole function** is uniquely forced:
\[
f(z)=\frac{a+uz}{1+\overline a\,uz},
\quad |a|=r_*,\quad |u|=1.
\]
Expansion gives the displayed formulas for \(b\) and \(c\). Conversely every such \(f\) is Schur and reaches the bound.

**4. All nodes, weights and uniqueness.** For a maximizing pair \((a,u)\), put
\[
Q(z)=z^{n+1}\frac{a+uz}{1+\overline a\,uz}.
\]
This is a finite Blaschke product of degree \(n+2\). Its level-one equation \(Q(\zeta)=1\) is exactly the displayed degree-\(n+2\) polynomial; the boundary argument of a finite Blaschke product is strictly increasing, so these are \(n+2\) distinct unit-circle points. The function \(F=(1+Q)/(1-Q)\) has simple poles at those points. Comparing each pole with the Herglotz kernel \((1+z/\zeta)/(1-z/\zeta)\) gives mass
\[
w_\zeta=\left[\zeta Q'(\zeta)/Q(\zeta)\right]^{-1}
=\left[n+1+\frac{1-r_*^2}{|a+u\zeta|^2}\right]^{-1}>0.
\]
Herglotz representation is unique, so there are no other representing measures. Each maximizing moment matrix is positive definite on the monomial span of degrees \(0,\ldots,n+1\), or equivalently these \(n+2\) support atoms are already necessary. Different phase pairs yield distinct moments, hence distinct measures.

**5. Approximation-preserving kernels.** Since \(K_n/z^n=(F+1)/2\), the conditions \(K_n=z^n+O(z^{2n+1})\) and \(\mathrm{Re}(K_n/z^n)\ge1/2\) are equivalent to the above positive-moment constraints by the Herglotz theorem. The characterization of best-approximation-preserving convolution kernels in Abdullayev--Savchuk--Savchuk therefore transfers the result verbatim.

## Verification
The standalone script `verify.py` checks the exact algebraic critical-point identity symbolically and, independently, constructs the level-one polynomial roots, positive Herglotz weights and Fourier moments for \(99\) combinations of \(n=2,\ldots,12\) and independent phase choices. Its observed maximum moment error was below \(8\times10^{-15}\), and every calculated root was on the unit circle within \(3\times10^{-15}\). The finite tests are consistency checks, not substitutes for the all-degree proof above. Run `python verify.py` with NumPy and SymPy installed; its recorded output is in `verification_output.txt`.

## Relationship to prior work
Abdullayev, Savchuk and Savchuk (2022), Theorem 2.1, establish the general positive-real-part criterion for best-approximation-preserving Hadamard kernels, along with separate Landau-type coefficient inequalities. Their theorem is used as a starting point rather than claimed anew. The classical Schur algorithm and Carathéodory--Toeplitz moment theorem give broad coefficient-feasibility frameworks; the present result supplies a specific three-free-coefficient body, its sharp aggregate extremal value, complete equality-phase family and concrete unique positive quadrature at every degree. Bultheel, Cruz-Barroso and Díaz Mendoza (2021) treat positive unit-circle quadrature through quasi-paraorthogonal polynomials; their accessible results give general quadrature theory, not this three-moment design optimization. A historical occurrence of the same exact extremal sum under a different formulation remains possible.

## Limitations
The assertion is restricted to three successive free moments with \(n\ge2\), positive unit-circle measures and normalized Hadamard kernels. It does not claim sharp bounds on arbitrary Hardy-function coefficients, best approximation errors, all higher moments, or stability of the atomic nodes under perturbations. The exact extremal constant is obtained through standard Schur reductions and so an older equivalent sharp coefficient-sum theorem is a substantive bibliographic risk. No independent scientific audit has been performed.

## References
- F. G. Abdullayev, V. V. Savchuk and M. V. Savchuk, *Best approximation-preserving operators over Hardy space*, arXiv:2206.11841v1 (public 23 June 2022), especially Theorem 2.1 and Section 3. https://arxiv.org/html/2206.11841v1
- A. Bultheel, R. Cruz-Barroso and C. Díaz Mendoza, *Zeros of quasi-paraorthogonal polynomials and positive quadrature*, arXiv:2110.10460 (public 20 October 2021). https://arxiv.org/abs/2110.10460
- Classical Schur coefficient algorithm, Carathéodory--Toeplitz truncated trigonometric moment theorem and Herglotz representation theorem (standard background).
