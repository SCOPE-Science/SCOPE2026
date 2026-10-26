# Exact squared-Jacobi tangencies in Zernike disk concentration

## Finding
Let \(\beta>-1\) be real, let \(k\ge1\) be an integer, and let \(P_j^{(a,b)}\) denote the standard Jacobi polynomial with \(P_j^{(a,b)}(1)=\binom{j+a}{j}\). Define the normalized cumulative radial energies, for \(0\le t\le1\), by
\[
E_{k,\beta}(t)=(2k+\beta+1)\int_0^t u^\beta[P_k^{(0,\beta)}(2u-1)]^2\,du,
\]
\[
E_{k-1,\beta+2}(t)=(2k+\beta+1)\int_0^t u^{\beta+2}[P_{k-1}^{(0,\beta+2)}(2u-1)]^2\,du.
\]
Then the exact identity
\[
\boxed{E_{k,\beta}(t)-E_{k-1,\beta+2}(t)=
\frac{(2k+\beta+1)(\beta+1)}{k^2}
 t^{\beta+1}(1-t)^2[P_{k-1}^{(1,\beta+1)}(2t-1)]^2}
\tag{1}
\]
holds throughout \(0\le t\le1\). In particular, one normalized radial energy always dominates the other. For \(k=1\), the inequality is strict on \((0,1)\); for \(k\ge2\), the two energies are equal at exactly \(k-1\) points in \((0,1)\), the shifted Gauss--Jacobi zeros of \(P_{k-1}^{(1,\beta+1)}\). Every interior equality has quadratic contact and no exchange of spectral ordering.

For the uniform unit ball in \(\mathbb R^d\), \(d\ge2\) integer, the fixed-total-degree \(n\) Zernike basis has radial factors
\[
R_{n,m}^{(d)}(r)=r^m P_{(n-m)/2}^{(0,m+d/2-1)}(2r^2-1),
\]
where \(m\ge0\), \(m\le n\), and \(n-m\) is even. A centered-ball concentration operator compressed to exact polynomial degree \(n\) has eigenvalue \(\Lambda_{n,m}^{(d)}(t)=E_{(n-m)/2,\,m+d/2-1}(t)\), where \(t\) is the squared aperture radius. Thus for every admissible adjacent pair \(m,m+2\),
\[
\boxed{\Lambda_{n,m}^{(d)}(t)\ge\Lambda_{n,m+2}^{(d)}(t)}
\]
with precisely \((n-m)/2-1\) interior equality radii, all tangential, independent of the dimension except for their locations.

## Assumptions and scope
The Jacobi parameters satisfy \(\beta>-1\), \(k\in\mathbb Z_{\ge1}\). Jacobi polynomials have the classical Jacobi weight \((1-x)^a(1+x)^b\) on \((-1,1)\). The normalized energies both run from zero to one: shifted Jacobi orthogonality gives
\[
\int_0^1u^\beta[P_k^{(0,\beta)}(2u-1)]^2\,du
=\int_0^1u^{\beta+2}[P_{k-1}^{(0,\beta+2)}(2u-1)]^2\,du
=\frac1{2k+\beta+1}.
\]
A radial mask on the ball preserves angular-harmonic degree; within any fixed total degree, the radial multiplicity per angular type is one. Both signs of an angular index on the disk have the same radial concentration eigenvalue. The statement concerns one degree slice, not the full direct sum of all degrees.

## Proof
Write
\[
A(u)=P_k^{(0,\beta)}(2u-1),\qquad
B(u)=P_{k-1}^{(0,\beta+2)}(2u-1),\qquad
Q(u)=P_{k-1}^{(1,\beta+1)}(2u-1).
\]
**First contiguous identity.** The polynomial \(F=A-uB\) vanishes at \(u=1\), since \(A(1)=B(1)=1\). For every polynomial \(h\) of degree at most \(k-2\), the two orthogonality statements imply
\[
\int_0^1u^{\beta+1}F(u)h(u)\,du=
\int_0^1u^\beta A(u)\,u h(u)\,du-
\int_0^1u^{\beta+2}B(u)h(u)\,du=0.
\]
Therefore \(F/(1-u)\) has degree at most \(k-1\) and is orthogonal to all degree-at-most-\(k-2\) polynomials for weight \(u^{\beta+1}(1-u)\); it is proportional to \(Q\). At zero, the Jacobi endpoint values give
\[
A(0)=(-1)^k\binom{k+\beta}{k},\qquad
Q(0)=(-1)^{k-1}\binom{k+\beta}{k-1}.
\]
Consequently
\[
\boxed{A-uB=-\frac{\beta+1}{k}(1-u)Q.}\tag{2}
\]
The same orthogonality argument works when \(k=1\), with the polynomial test space empty; the endpoint normalization then fixes the constant.

**Second contiguous identity.** Integration by parts, with vanishing boundary term \(u^{\beta+2}(1-u)Q(u)h(u)\) at both endpoints, yields for every polynomial \(h\) of degree at most \(k-2\),
\[
\int_0^1 u^{\beta+2}[Q-(1-u)Q']h\,du
=\int_0^1 u^{\beta+1}(1-u)Q[(\beta+2)h+uh']\,du=0.
\]
The bracket is a degree-at-most-\(k-1\) polynomial. As \(Q(1)=k\) and \(B(1)=1\), orthogonality identifies it as
\[
\boxed{Q-(1-u)Q'=kB.}\tag{3}
\]
In particular, inserting (3) into (2) gives
\[
A=\frac{[(\beta+2)u-(\beta+1)]Q-u(1-u)Q'}{k},
\qquad B=\frac{Q-(1-u)Q'}{k}.
\]
Subtracting the squares of these two expressions and factoring by (2) produces the derivative identity
\[
\boxed{u^\beta(A^2-u^2B^2)
=\frac{\beta+1}{k^2}\frac{d}{du}
\{u^{\beta+1}(1-u)^2Q^2\}.}\tag{4}
\]
Integrate (4) from zero to \(t\), noting that the boundary expression vanishes at zero because \(\beta>-1\), and multiply by \(2k+\beta+1\). This proves (1).

**Contacts and spherical-ball interpretation.** The Jacobi weight for \(Q\) is positive on \((0,1)\) for \(\beta>-1\); by the classical zeros theorem \(Q\) has exactly \(k-1\) distinct simple interior roots. All other factors of (1) are strictly positive inside \((0,1)\). Each zero is therefore exactly double as a zero of the energy difference. In \(d\) dimensions, polar separation produces the weight \(r^{2m+d-1}dr\), equivalently \(\frac12u^{m+d/2-1}du\), establishing the displayed eigenvalue identification and the dimension-uniform count.

## Verification
The standalone `check.py` verifies both contiguous identities and the differentiated factorization symbolically for \(1\le k\le5\) and integer parameters \(0\le\beta\le3\). It additionally checks the integrated formula by independent numerical quadrature for four noninteger parameter values, four degrees, and four interior radii. Run `python check.py` with SymPy and SciPy installed. Finite verification is diagnostic; the preceding orthogonality argument covers every \(\beta>-1\), every integer \(k\ge1\), and every allowed dimension.

## Relationship to prior work
The exact Zernike--Jacobi representation, normalization and radial disk quadrature are standard and are explicitly developed by Greengard and Serkh (2018). Janssen (2019) derives sharp radial-derivative bounds using nonnegative Chebyshev connection coefficients. These are not claims of new Zernike definitions, endpoint formulas, or Jacobi-zero simplicity. The result here concerns a distinct integral-order comparison: an exact nonnegative square for the *difference of two normalized cumulative mode energies*, with a complete interior tangency count. The inspected source sections do not state this identity or its uniform angular-dominance consequence.

The classical contiguous identities (2) and (3) are elementary polynomial relations; their independent proof is included to expose the integral square mechanism rather than claim their individual novelty. Unlike angular spectral crossings on spheres, the ball-Zernike neighboring angular modes do not reverse order.

## Limitations
This theorem compares neighboring admissible angular degrees at fixed total polynomial degree; it does not classify every coincidence between non-neighboring degrees, compare modes from different total degrees, give operator-norm concentration bounds for the whole polynomial space, or address nonconcentric masks. The first-source date is based on the dated publicly released Zernike report, not a claim of publication priority. An unindexed older expression of the integral square identity remains possible, and no independent novelty audit has been performed.

## References
1. P. Greengard and K. Serkh, *Zernike Polynomials: Evaluation, Quadrature, and Interpolation*, Yale Technical Report YALEU/DCS/TR-1539, February 20, 2018. https://engineering.yale.edu/application/files/3517/3685/9497/TR1539.pdf. Relevant material: Section 2.3; Appendix A on Jacobi relations, normalization, and higher-dimensional polynomials.
2. A. J. E. M. Janssen, *Sharp bound on the radial derivatives of the Zernike circle polynomials (disk polynomials)*, arXiv:1910.07250, first submitted October 16, 2019. https://arxiv.org/abs/1910.07250. Relevant material: Sections 1--4, Zernike definition, Chebyshev connection expansion, derivative bounds.
3. NIST Digital Library of Mathematical Functions, Chapter 18 (orthogonal polynomials, Jacobi normalization, orthogonality, and zeros), https://dlmf.nist.gov/18.
