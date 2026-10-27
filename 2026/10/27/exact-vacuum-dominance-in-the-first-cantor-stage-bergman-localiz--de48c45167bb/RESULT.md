# Exact vacuum dominance in the first Cantor-stage Bergman localization

## Finding
Let \(R>0\). In the unweighted Bergman space \(A^2(\mathbb D)\) with normalized area measure, let \(T_R\) be compression of multiplication by the indicator of the radial set
\[
\Omega_R=\left\{z\in\mathbb D:\frac{|z|^2}{1-|z|^2}\in[0,R/3]\cup[2R/3,R]\right\}.
\]
Every nonconstant monomial has strictly smaller localization eigenvalue than the constant monomial, at every \(R>0\). Consequently the exact operator norm is
\[
\|T_R\|=\lambda_0(R)=\frac{2R(R^2+3R+3)}{(R+1)(R+3)(2R+3)}.
\]
The maximizing unit vectors are exactly the constant functions multiplied by unimodular scalars.

## Assumptions and scope
Here \(dA/\pi\) denotes probability-normalized area on the disk and \(T_R=P_{A^2}M_{\mathbf1_{\Omega_R}}|_{A^2}\). The parameter \(R\) ranges over every positive real number. This is the first middle-third Cantor iterate (two bands), not a statement about higher Cantor depths or arbitrary disconnected radial regions.

## Proof
The normalized monomials \(e_k(z)=\sqrt{k+1}\,z^k\), \(k=0,1,\ldots\), form an orthonormal basis. Rotational invariance diagonalizes \(T_R\). With \(s=|z|^2\) and \(x=s/(1-s)\), the variable \(s=x/(1+x)\) and the two radial bands become the disjoint intervals \([0,a]\cup[b,c]\subset(0,1)\), where
\[
 a=\frac R{R+3},\qquad b=\frac{2R}{2R+3},\qquad c=\frac R{R+1}.
\]
Thus \(0<a<b<c<1\), and the eigenvalue corresponding to \(e_k\) is
\[
\lambda_k(R)=(k+1)\int_{[0,a]\cup[b,c]}s^k\,ds=a^{k+1}+c^{k+1}-b^{k+1}.
\]
Put \(S=[0,a]\cup[b,c]\), \(L=a+c-b\), and define the cumulative signed discrepancy
\[
H(t)=|S\cap[0,t]|-Lt,\qquad 0\le t\le1.
\]
The piecewise affine function \(H\) increases on \(S\), decreases on its complement, and satisfies \(H(0)=H(1)=0\). Its only possible interior minimum below zero is at \(b\). Direct exact algebra gives
\[
H(b)=a-b(a+c-b)=\frac{R(4R^2+9R+9)}{(R+1)(R+3)(2R+3)^2}>0.
\]
It follows that \(H(t)>0\) for every \(0<t<1\), except possibly at isolated endpoints, and in fact the strict inequality holds throughout the open interval. For \(k\ge1\), integration by parts yields the exact nonnegative deficit identity
\[
\lambda_0(R)-\lambda_k(R)=k(k+1)\int_0^1H(t)t^{k-1}\,dt>0.
\]
Therefore the constant mode is the unique top eigenspace. Since \(T_R\) is positive, bounded, self-adjoint, and diagonal in the monomial basis, its norm is \(\lambda_0(R)\). Simplifying \(a+c-b\) gives the displayed rational expression. The strict gap for every individual \(k\ge1\), together with \(\lambda_k\to0\) because \(c<1\), establishes complete equality classification.

## Verification
The proof uses only exact integral identities and the displayed positive-polynomial factorization. The standalone program `checker.py` checks the factorization in rational arithmetic, the finite formula, and strict mode inequalities for multiple rational \(R\) and degrees. These finite checks supplement, but do not replace, the all-\(R\), all-degree proof.

## Relationship to prior work
Abreu, Mouayn, and Voigtlaender (2022, arXiv:2201.11705) introduce the middle-third hyperbolic annular Cantor localization operator and obtain general eigenvalue formulas and two-sided operator-norm bounds at arbitrary iteration depth. Their Section 4.3 uses the zeroth eigenvalue as a lower bound. The present result identifies the actual maximizing eigenmode and exact operator norm at depth one, which is not implied by the existence of a zeroth-eigenvalue lower bound. For disconnected radial symbols, higher angular modes need not be dominated by the constant mode, so this conclusion is specific to the geometry proved here.

## Limitations
The theorem covers only the first middle-third iterate in the unweighted Bergman disk space. It does not claim spectral dominance for arbitrary Cantor depth, general weighted Bergman indices, or other radial masks. Published equivalents might exist under different terminology; independent historical verification remains open.

## References
Abreu, L. D., Mouayn, Z., and Voigtlaender, F., *A fractal uncertainty principle for Bergman spaces and analytic wavelets*, arXiv:2201.11705 (first public version 2022-01-27), especially Sections 2 and 4.
