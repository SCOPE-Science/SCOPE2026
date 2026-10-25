# Sharp degree-uniform harmonic sampling stability on the \(A_5\) root directions

## Finding
For the 15 positive-root directions \(X=\{(e_i-e_j)/\sqrt2:1\le i<j\le6\}\subset S^4\), the normalized exact-degree spherical-harmonic evaluation operator \(E_\ell:\mathcal H_\ell\to\mathbb C^{15}\) satisfies
\[
\sigma_{\min}(E_\ell)^2\ge\frac{21}{64}\qquad(\ell\ge3),
\]
with equality at degree \(\ell=4\). Every degree at least three interpolates arbitrary complex data on the 15 directions. The preceding ranks at degrees zero, one, and two are respectively \(1,5,14\); hence the eventual interpolation threshold is exactly three. The explicit five-sector/ two-sector spectral formulas below hold for every nonnegative degree.

## Assumptions and scope
Work in the real Euclidean hyperplane \(V=\{x\in\mathbb R^6:\sum_i x_i=0\}\), which has dimension five, and identify its unit sphere with \(S^4\). Here \(e_i\) are the coordinate vectors. Let \(\mathcal H_\ell\) be the finite-dimensional space of restrictions to \(S^4\) of homogeneous harmonic polynomials on \(V\) of degree \(\ell\), equipped with normalized probability-surface \(L^2\) inner product. Write \(h_\ell=\dim\mathcal H_\ell\), and define
\[
(E_\ell f)_{ij}=h_\ell^{-1/2}f((e_i-e_j)/\sqrt2),\qquad 1\le i<j\le6.
\]
The singular values are those of this operator, not of the unnormalized evaluation operator or a 30-row matrix. The 30 roots of \(A_5\) occur in antipodal pairs and carry only 15 independent values for any fixed parity.

## Proof
The spherical-harmonic addition theorem in ambient dimension five gives
\[
(E_\ell E_\ell^*)_{ij,kl}=P_\ell(\langle x_{ij},x_{kl}\rangle),\quad P_\ell(t)=\frac{C_\ell^{(3/2)}(t)}{C_\ell^{(3/2)}(1)}.
\]
Distinct unoriented edges of the complete graph on six vertices are either incident or disjoint. Their corresponding root inner products are respectively \(\pm1/2\) and \(0\). Put \(u_\ell=P_\ell(1/2)\), \(v_\ell=P_\ell(0)\).

When \(\ell\) is even, the Gram matrix equals \(I+u_\ell A+v_\ell B\), where \(A\) is the adjacency matrix of the triangular graph \(J(6,2)\) and \(B=J-I-A\) indicates disjoint edges. The familiar decomposition of the edge space into constant, standard, and \((4,2)\) components has dimensions \(1,5,9\). Their respective adjacency eigenvalue pairs \((A,B)\) are \((8,6)\), \((2,-3)\), and \((-2,1)\). Therefore the complete Gram spectrum is
\[
\begin{aligned}
\lambda_{0,\ell}&=1+8u_\ell+6v_\ell&&\text{(multiplicity 1)},\\
\lambda_{1,\ell}&=1+2u_\ell-3v_\ell&&\text{(multiplicity 5)},\\
\lambda_{2,\ell}&=1-2u_\ell+v_\ell&&\text{(multiplicity 9)}.
\end{aligned}
\]
When \(\ell\) is odd, the Gram matrix equals \((1-2u_\ell)I+u_\ell D^*D\), where \(D\) is an arbitrarily oriented vertex-edge incidence matrix of the complete graph on six vertices (orientation consistent with the chosen roots). The nonzero eigenvalues of \(D^*D\) all equal six, with multiplicity five, while its kernel has dimension ten. Thus
\[
\lambda_{1,\ell}=1+4u_\ell\quad\text{(multiplicity 5)},\qquad
\lambda_{2,\ell}=1-2u_\ell\quad\text{(multiplicity 10)}.
\]
This proves the spectral formulas and fixes all normalizations.

To prove a UNIFORM lower bound for infinitely many degrees, use \(C_\ell^{(3/2)}(x)=P_{\ell+1}'(x)\), where the prime denotes differentiation of the classical Legendre polynomial, and \(C_\ell^{(3/2)}(1)=(\ell+1)(\ell+2)/2\). The identity
\[
(1-x^2)P_m'(x)=m\bigl(P_{m-1}(x)-xP_m(x)\bigr)
\]
and the classical bound \(|P_m(x)|\le1\) for \(-1\le x\le1\) imply
\[
|u_\ell|\le\frac4{\ell+2},\qquad |v_\ell|\le\frac2{\ell+2}.
\]
For all \(\ell\ge64\), the five possible spectral formulas consequently give the common lower bound
\[
\lambda\ge 1-\frac{44}{\ell+2}\ge1-\frac{44}{66}=\frac13>\frac{21}{64}.
\]
(The absolute-value coefficient sum 44 is the largest among the five branches.) This is an analytic bound for ALL degrees \(\ell\ge64\), not a finite extrapolation.

For each integer degree \(3\le\ell\le63\), the accompanying standard-library exact-rational checker computes \(P_{\ell+1}(0)\), \(P_{\ell+1}(1/2)\), and the corresponding derivatives from the three-term Legendre recurrence, forms every spectral branch as a rational number, and confirms \(\lambda\ge21/64\). It finds equality only for the fivefold even standard eigenvalue at degree four:
\[
(\lambda_{0,4},\lambda_{1,4},\lambda_{2,4})=
\left(\frac9{16},\frac{21}{64},\frac{91}{64}\right).
\]
The same formulas give the ranks at the three lower degrees: degree zero has eigenvalues \((15,0,0)\), degree one has \((3,0)\), and degree two has \((0,15/8,5/8)\), in their listed symmetry sectors. Thus every degree \(\ell\ge3\) has rank 15, with a sharp degree-uniform singular-value bound, and degrees zero through two are not surjective. This completes the proof.

## Verification
Run `python3 CHECK.py` (Python 3 standard library only). It checks every rational eigenvalue in degrees 3 through 63 inclusive, reproduces the exact extremizer and low-degree ranks, and prints the analytic tail inequality. The proof separately derives that tail inequality for all integer degrees at least 64. No numerical root finding, floating-point spectral inference, or external certificate is used.

## Relationship to prior work
Spherical-harmonic reproducing kernels, harmonic-index designs, and Fisher-type bounds are standard; Bannai–Okuda–Tagami (2013) give the relevant exact-degree harmonic-index framework and addition theorem. Narcowich–Petrushev–Ward (2006) investigate localized spherical tight frames, a different class of global constructions. The present claim addresses the fixed \(A_5\) root configuration and a sharp uniform lower singular-value bound simultaneously for every degree at least three. The Johnson-graph decomposition is classical; the claimed new content is its quantitative use with an exact finite certificate and an analytic all-degree tail, not the decomposition itself.

## Limitations
This theorem is restricted to the 15 root lines of \(A_5\) in \(S^4\), normalized as above; it does not establish the same bound for other ranks, arbitrary perturbed point configurations, or a full-frame bound on the harmonic domain (which has much larger dimension in high degrees). The claim concerns surjectivity onto the 15 samples, not injectivity on \(\mathcal H_\ell\). Earlier uncatalogued association-scheme tabulations might imply the same eigenvalue bound, so independent literature-priority assessment remains necessary.

## References
- E. Bannai, T. Okuda, M. Tagami, *Spherical designs of harmonic index t*, arXiv:1308.5101, first posted 2013-08-23, https://arxiv.org/abs/1308.5101.
- F. J. Narcowich, P. Petrushev, J. D. Ward, *Localized tight frames on spheres*, SIAM Journal on Mathematical Analysis 38 (2006), 574–594, https://doi.org/10.1137/040614359.
- NIST Digital Library of Mathematical Functions, orthogonal polynomials, https://dlmf.nist.gov/18 (standard recurrence identities).
