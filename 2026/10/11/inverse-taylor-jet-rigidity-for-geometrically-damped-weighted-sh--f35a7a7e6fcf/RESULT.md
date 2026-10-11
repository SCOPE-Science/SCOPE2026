# Inverse Taylor-jet rigidity for geometrically damped weighted shifts

## Finding
Let \(c=(c_j)_{j\ge1}\) and \(d=(d_j)_{j\ge1}\) be bounded sequences of nonnegative real numbers. For \(0<q<1\) define compact forward weighted shifts on \(\ell_2(\mathbb N_0)\) by
\[
T_c(q)e_0=e_1,\qquad T_c(q)e_j=c_jq^je_{j+1}\quad(j\ge1),
\]
and put \(\rho_c(q)=w(T_c(q))\), where \(w\) is numerical radius. Suppose for some integer \(k\ge1\) that \(c_j=d_j>0\) whenever \(1\le j<k\), while \(c_k\ne d_k\). Then
\[
\boxed{\rho_d(q)-\rho_c(q)=\frac{d_k^2-c_k^2}{4}\left(\prod_{j=1}^{k-1}c_j^2\right)q^{k(k+1)}+o(q^{k(k+1)})}\qquad(q\downarrow0).
\]
The empty product is one. The coefficient is nonzero; thus the first detectable difference is exactly at order \(k(k+1)\), and its sign agrees with \(d_k-c_k\).

For strictly positive bounded sequences, equality of the analytic germs of \(\rho_c\) and \(\rho_d\) therefore forces \(c=d\). There is also a recursive reconstruction: set \(c^{<k}_j=c_j\) when \(j<k\) and \(c^{<k}_j=0\) when \(j\ge k\). Given the already recovered first \(k-1\) entries, obtain the next one from
\[
\boxed{c_k^2=\frac{4}{\prod_{j=1}^{k-1}c_j^2}\,[q^{k(k+1)}]\big(\rho_c(q)-\rho_{c^{<k}}(q)\big)}.
\]
Here the bracket extracts an ordinary Taylor coefficient at zero. All these radius functions admit local holomorphic continuations of their real parameter values. In the four-periodically modulated example whose edges begin \((1,sq,q^2,tq^3,\ldots)\), fixing positive \(s\) and replacing \(t\) with \(v\) produces the leading difference \(s^2(v^2-t^2)q^{12}/4\).

## Assumptions and scope
The Hilbert space is complex and separable; the shift coefficients are bounded, real and nonnegative, the first edge has fixed weight one, and the remaining edge indexed \(j\ge1\) has weight \(c_jq^j\). Boundedness ensures operator-norm analyticity near zero. Strict positivity of the initial shared coefficients is needed for a nonvanishing first-difference constant; total positivity is required for recovery of the *whole* sequence. For sequences containing a zero, coefficients after the first zero need not be detectable from the connected leading component. No numerical-data stability is asserted: recovering high indices demands increasingly high Taylor orders.

## Proof
Write \(J_c(q)=(T_c(q)+T_c(q)^*)/2\) for real \(q\). The diagonal unitary \(e_j\mapsto e^{ij\theta}e_j\) rotates the shift, so \(w(T_c(q))=\|J_c(q)\|\). The bipartite sign unitary \(e_j\mapsto(-1)^je_j\) conjugates \(J_c(q)\) to \(-J_c(q)\); hence its norm is its largest eigenvalue. At zero, the only nonzero block has entries \(1/2\) linking \(e_0\) and \(e_1\), and its largest eigenvalue \(1/2\) is simple, with unit vector \(v=(e_0+e_1)/\sqrt2\).

Let \(M\ge1\) bound both coefficient sequences. On the closed complex disc \(\lvert q\rvert\le r=1/(8M)\), define the *holomorphic complex-symmetric* tridiagonal family \(J_h(q)\) by its matrix coefficients \(1/2\) on edge zero and \(h_jq^j/2\) on edge \(j\ge1\), without conjugating \(q\). This agrees with the self-adjoint \(J_h(q)\) for real \(q\). Uniformly over the segment \(h_j(u)=(1-u)c_j+ud_j\), \(0\le u\le1\), the perturbation from \(J_0\) has norm at most \(M\lvert q\rvert\). On the circle \(\lvert z-1/2\rvert=1/4\), the unperturbed resolvent has norm at most four, so its perturbation inverse has norm at most eight. The contour therefore defines an analytic rank-one Riesz projection \(P_u(q)\) and simple analytic eigenvalue \(\lambda_u(q)\); \(\|P_u(q)\|\le2\) and \(\|P_u(q)-P_0\|\le8M\lvert q\rvert\). For positive real \(q<r/4\) this is the largest eigenvalue and hence \(\rho_{h(u)}(q)\).

Put \(y_u(q)=P_u(q)v\), and for real positive \(q<r/4\) put \(x_u(q)=y_u(q)/\|y_u(q)\|\). The denominator is at least \(3/4\). For \(j\ge2\), every term in the contour-resolvent Neumann expansion reaching coordinate \(e_j\) from \(v\), initially supported at \(e_0,e_1\), must cross edges \(1,2,\ldots,j-1\). Thus its Taylor order is at least \(S_j=j(j-1)/2\). Cauchy estimates from \(\|P_u(q)\|\le2\) yield the uniform bound
\[
\lvert x_{u,j}(q)\rvert\le6(q/r)^{j(j-1)/2}\quad(j\ge2,\ 0<q<r/4,\ 0\le u\le1).
\]
For \(j=1\), the same inequality with exponent zero is trivially true. The eigenvector recurrence for \(j\ge2\),
\[
\lambda_u(q)x_{u,j}(q)=\frac{h_{j-1}(u)q^{j-1}}2x_{u,j-1}(q)+\frac{h_j(u)q^j}2x_{u,j+1}(q),
\]
together with \(\lambda_u(0)=1/2\), \(x_{u,1}(0)=1/\sqrt2\), and the order bound on the next coordinate, proves inductively, uniformly in \(u\) for each fixed \(j\),
\[
x_{u,j}(q)=\frac{\prod_{\ell=1}^{j-1}h_\ell(u)}{\sqrt2}\,q^{j(j-1)/2}+o\!\left(q^{j(j-1)/2}\right),\qquad j\ge1.
\]

The Hellmann–Feynman formula is legitimate because the isolated eigenvalue stays simple along \(u\in[0,1]\) and the derivative series converges in operator norm:
\[
\frac{d\lambda_u(q)}{du}=\sum_{j\ge k}(d_j-c_j)q^jx_{u,j}(q)x_{u,j+1}(q).
\]
For \(j=k\), the preceding eigenvector expansion gives
\[
\frac{d_k-c_k}{2}\left(\prod_{\ell<k}c_\ell^2\right)h_k(u)q^{k(k+1)}+o\!\left(q^{k(k+1)}\right).
\]
All later edges contribute a lower-order remainder, uniformly in \(u\): their absolute sum is bounded by a constant times \(\sum_{j\ge k+1}q^j(q/r)^{j^2}\), which is \(o(q^{k(k+1)})\). Integrate in \(u\) and use \(\int_0^1(d_k-c_k)h_k(u)\,du=(d_k^2-c_k^2)/2\). This proves the displayed exact coefficient. The same argument permits zero coefficients, provided the shared earlier ones are positive. Comparing with the finitely truncated sequence gives the recursive formula. Finally, if two strictly positive sequences had equal radius germs but differed, their least differing index would give a nonzero Taylor coefficient, a contradiction.

## Verification
The analytic proof handles infinitely many weights; no finite experiment is used to infer an infinite statement. The attached standalone Python 3 checker evaluates largest eigenvalues of finite tridiagonal sections using 100-digit decimal characteristic-polynomial bisection. For first differing indices \(k=1,2,3,4\), it checks positivity and the predicted normalized difference coefficient at \(q=0.05\) and \(q=0.025\), as well as improved agreement at the smaller parameter. It prints `INVERSE_JET_FINITE_TRIDIAGONAL_CHECK_OK`. These checks test numerical consistency only, and are not a certificate for all indices or for infinite sequences. The exact proof comes from analytic spectral projections, coordinate vanishing orders, and Hellmann–Feynman integration.

## Relationship to prior work
Ghosh, Birbonshi and Ojha (2026) study the two-parameter period-four geometric sequence \((1,sq,q^2,tq^3,\ldots)\), provide numerical-radius bounds, and describe its radius by a smallest positive root of an entire function. Its public first version was posted on 2026-08-18. Their original full text was not obtainable for comparison; the dated abstract and a secondary analytical synopsis were inspected, so the possibility of implicit overlap remains a material limitation.

Chien and Nakazato (2009), in an inspected six-page primary paper, give a determinantal/hypergeometric characterization and a Taylor expansion for the *single fixed* pure geometric sequence. Their displayed low-order expansion does not state an inverse-uniqueness theorem for arbitrary bounded positive modulations. Chakraborty, Ojha and Birbonshi (2022) develop determinantal formulas for shifts with eventually two-periodic fixed tails; their inspected primary text does not state the present graded inverse-germ law. Stout's general determinant representation is an important antecedent, but its existence alone does not assert the triangular cancellation order or injective reconstruction formulated here. The claim is specifically the first-difference law and its inverse consequence, not novelty of numerical radius, geometric shifts, determinants, analytic perturbation theory, or the specific period-four family.

## Limitations
The asymptotics are local as \(q\to0\); they do not furnish useful finite-precision inverse stability or a radius formula at general fixed \(q\). Strict positivity is essential for the global injectivity conclusion. The original 2026 motivating manuscript could not be read in full; a hidden equivalent corollary there or in less visible inverse Jacobi literature cannot be ruled out. The analytic continuation pertains to the isolated eigenvalue branch and need not represent a numerical radius for nonreal \(q\).

## References
- A. Ghosh, R. Birbonshi, S. Ojha, *On the numerical radius of a class of weighted shift operators*, arXiv:2608.17486v1 (first submitted 2026-08-18), https://arxiv.org/abs/2608.17486 . Primary full text not inspected.
- M.-T. Chien, H. Nakazato, *The numerical radius of a weighted shift operator with geometric weights*, Electronic Journal of Linear Algebra **18** (2009), 58–63, DOI: 10.13001/1081-3810.1293, https://journals.uwyo.edu/index.php/ela/article/download/587/587 . Primary text inspected.
- B. Chakraborty, S. Ojha, R. Birbonshi, *Numerical radii of weighted shift operators using determinantal polynomials*, Operators and Matrices **16** (2022), 1155–1174, DOI: 10.7153/oam-2022-16-75, https://files.ele-math.com/articles/oam-16-75.pdf . Primary text inspected.
- Q. F. Stout, *The numerical range of a weighted shift*, Proceedings of the American Mathematical Society **88** (1983), 495–502. Cited for historical determinant representation through the primary 2009 and 2022 literature; original full text not inspected.
