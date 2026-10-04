# Finite-resultant correction for coprime values of homogeneous binary forms
## Finding
Let \(F,G\in\mathbb Z[X,Y]\) be nonconstant homogeneous forms of positive degrees and assume their homogeneous resultant \(R\) is nonzero. For a prime \(p\mid R\), define
\[
N_p=\#\{(a,b)\in\mathbb F_p^2:F(a,b)=G(a,b)=0\}.
\]
Then
\[
\#\{1\le m,n\le X:\gcd(F(m,n),G(m,n))=1\}
=C_{F,G}X^2+O_{F,G}(X\log X),
\]
where
\[
C_{F,G}=\frac1{\zeta(2)}\prod_{p\mid R}\frac{1-N_p/p^2}{1-1/p^2}.
\]
In particular, the infinite Ekedahl--Poonen product reduces to a finite correction, supported exactly among the resultant primes. No positivity condition on the highest-degree coefficients is needed.

## Assumptions and scope
The forms are fixed, integral, homogeneous, nonconstant, and of positive degree. The homogeneous resultant is assumed nonzero; equivalently for this binary setting, the two forms have no common projective zero over an algebraic closure. The count is over positive coordinate pairs in the square \([1,X]^2\). The implied constant may depend on \(F\) and \(G\).

For \(R=\pm1\), the product is empty and the constant is exactly \(1/\zeta(2)\). The theorem also allows a resultant prime at which every residue class is a common zero; then \(C_{F,G}=0\), as it should.

## Proof
Put \(M=\operatorname{rad}(|R|)\). If \(p\nmid R\), the reductions of \(F\) and \(G\) have no common projective zero over \(\overline{\mathbb F}_p\). Hence a simultaneous zero \((a,b)\in\mathbb F_p^2\) must be \((0,0)\). Therefore, for a primitive integer pair \((m,n)\), no prime outside \(M\) can divide both \(F(m,n)\) and \(G(m,n)\).

Consequently
\[
\gcd(F(m,n),G(m,n))=1
\]
if and only if \(\gcd(m,n)=1\) and, for every \(p\mid M\), the residue pair \((m,n)\bmod p\) is not a simultaneous zero of \(F\) and \(G\).

Let \(L(u,v)\) be the indicator of these finitely many local exclusions, and define
\[
B(Y)=\sum_{1\le u,v\le Y}L(u,v).
\]
The Chinese remainder theorem gives exactly
\[
\prod_{p\mid M}(p^2-N_p)
\]
good residue classes modulo \(M\). Counting each fixed residue class in a square gives
\[
B(Y)=\beta Y^2+O_{F,G}(Y+1),\qquad
\beta=\prod_{p\mid M}\left(1-\frac{N_p}{p^2}\right).
\]

Use Möbius inversion for coordinate primitivity. If \(d\) shares a prime factor with \(M\), then \(L(du,dv)=0\). If \(\gcd(d,M)=1\), homogeneity and invertibility of \(d\bmod p\) give \(L(du,dv)=L(u,v)\). Thus the desired count is exactly
\[
\sum_{\substack{d\le X\\\gcd(d,M)=1}}\mu(d)B(\lfloor X/d\rfloor).
\]
Substituting the estimate for \(B\), using \(\lfloor X/d\rfloor^2=X^2/d^2+O(X/d+1)\), and summing absolute errors yields \(O_{F,G}(X\log X)\). Extending the convergent main sum to infinity changes it by \(O(X)\), and
\[
\sum_{\gcd(d,M)=1}\frac{\mu(d)}{d^2}
=\prod_{p\nmid M}\left(1-\frac1{p^2}\right)
=\frac1{\zeta(2)}\prod_{p\mid M}\left(1-\frac1{p^2}\right)^{-1}.
\]
Multiplying by \(\beta\) proves the stated constant and error term.

## Verification
The proof is symbolic and does not depend on finite experimentation. The standalone checker verifies two nontrivial examples exactly on finite grids and reconstructs their counts by the Möbius/local formula. For \(F=X^2-Y^2\), \(G=X^2-4Y^2\), the resultant is \(9\), one has \(N_3=5\), and the leading constant simplifies to \(3/\pi^2\). For \(F=X^2+Y^2\), \(G=X^2-Y^2\), the resultant is \(4\), one has \(N_2=2\), and the constant is \(4/\pi^2\). The finite checks are corroborative only.

## Relationship to prior work
Tóth, arXiv:2609.28284v1, proves an error-term version of the Ekedahl--Poonen formula under a positivity property on the top-degree coefficients. His Theorem 1 permits a sharper logarithmic exponent when a better bound for the number of common zeros modulo large primes is available, but the positivity hypothesis remains. The present homogeneous-binary argument replaces that hypothesis by resultant rigidity and gives a finite local correction formula.

Bodin and Dèbes prove the general Ekedahl--Poonen density formula for coprime polynomial values (Israel J. Math. 257 (2023), 25--55, DOI:10.1007/s11856-023-2530-8). Their theorem gives the density but not this \(O(X\log X)\) sign-free quantitative statement; their explicit resultant discussion concerns the one-variable value problem.

## Limitations
The proof uses binary homogeneity essentially. For nonhomogeneous polynomials, scaling a coordinate pair does not preserve the finite local conditions, and primes outside a fixed resultant set need not reduce to coordinate primitivity. No uniformity is claimed as the coefficients, degrees, or resultant vary. The error term is elementary and is not claimed optimal.

## References
1. L. Tóth, *Counting \(k\)-tuples of positive integers such that the values of several polynomials of \(k\) variables are relatively prime*, arXiv:2609.28284v1, first posted 2026-09-23.
2. A. Bodin and P. Dèbes, *Coprime values of polynomials in several variables*, Israel Journal of Mathematics 257 (2023), 25--55, DOI:10.1007/s11856-023-2530-8; arXiv:2105.13883.
