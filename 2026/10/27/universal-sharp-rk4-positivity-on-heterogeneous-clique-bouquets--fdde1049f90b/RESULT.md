# Universal sharp RK4 positivity on heterogeneous clique bouquets

## Finding
Let \(t\ge2\), let \(s_1,\ldots,s_t\) be arbitrary positive integers, and form the simple connected graph \(G=K_1\vee(K_{s_1}\sqcup\cdots\sqcup K_{s_t})\). Write \(n=1+\sum_i s_i\). If \(L\) is its unweighted combinatorial Laplacian, then classical fourth-order Runge--Kutta on \(y'=-Ly\) has completed-step matrix
\[
T(h)=I-hL+\frac{h^2L^2}{2}-\frac{h^3L^3}{6}+\frac{h^4L^4}{24}.
\]
Let \(\rho=2.785293563405\ldots\) denote the unique positive root of \(\rho^3-4\rho^2+12\rho-24=0\). Then
\[
T(h)\ge0\text{ entrywise}\quad\Longleftrightarrow\quad 0\le h\le\frac{\rho}{n}
\quad\Longleftrightarrow\quad\|T(h)\|_{2\to2}\le1.
\]
At the upper endpoint every hub-to-leaf entry is zero, while all entries between two distinct leaves are strictly positive; for every larger step the hub-to-leaf entries are negative. The threshold is independent of the number and individual sizes of the clique petals. For \(t\ge2\) with at least one \(s_i\ge2\), these are graphs containing triangles that are not complete multipartite.

## Assumptions and scope
All graphs are finite, simple and unweighted. The join symbol \(\vee\) adds an edge from the unique hub to every other vertex, and \(\sqcup\) is a disjoint union. The result concerns the completed RK4 step for the *linear* diffusion equation, not positivity of every intermediate RK stage or arbitrary nonlinear dynamics. Initial data are arbitrary coordinatewise nonnegative vectors. The matrix is symmetric and stochastic in row/column sums; entrywise nonnegativity is exactly positivity preservation of all such initial data. The operator norm is the usual Euclidean induced norm.

## Proof
Define \(r(x)=1-x+x^2/2-x^3/6+x^4/24\), and let \(m=n-1\). The Laplacian has orthogonal eigenspaces: constants at eigenvalue \(0\); a one-dimensional hub-versus-leaf mean space at \(n\); the \((t-1)\)-dimensional space of vectors constant on each clique with weighted leaf mean zero at \(1\); and the \((s_i-1)\)-dimensional zero-sum space within petal \(i\) at \(s_i+1\). All nonzero eigenvalues are at most \(n\), with \(n\) attained.

Write \(r_1=r(h)\), \(r_n=r(nh)\), \(r_i=r((s_i+1)h)\), and
\[
B=\frac{m-nr_1+r_n}{nm}
=\frac{h^2}{2}\left[1-\frac{n+1}{3}h+\frac{n^2+n+1}{12}h^2\right].
\]
The spectral projectors give the following complete list of entries, where \(c\) is the hub and \(u,v\) are leaves: 
\[
T_{cc}=\frac1n+\frac mn r_n,\qquad
T_{cu}=\frac{1-r_n}{n};
\]
\[
T_{uv}=B\quad(u,v\text{ in distinct petals});\qquad
T_{uv}=B+\frac{r_1-r_i}{s_i}\quad(u\ne v\text{ in petal }i);
\]
\[
T_{uu}=B+\frac{r_1-r_i}{s_i}+r_i\quad(u\text{ in petal }i).
\]
The bracket in \(B\) is positive for every real step because its discriminant is \(-(2n^2+n+2)/9<0\); thus \(B>0\) for \(h>0\). Also \(24r(x)=(x^2-2x+2)^2+4((x-2)^2+1)>0\) for all real \(x\). Hence the hub diagonal is positive.

The scalar \(r\) decreases then increases because \(r''(x)=1-x+x^2/2>0\), and \(r'\) has exactly one real zero. The defining equation for \(\rho\) gives the exact reflection identity
\[
24\{r(x)-r(\rho-x)\}=2(\rho-2)x(\rho-x)(\rho-2x).
\]
For \(0\le x\le\rho/2\), the right side is nonnegative. Therefore \(r(x)\ge r(y)\) whenever \(x\le y\le\rho-x\): on this interval the maximum of the unimodal function \(r\) is attained at an endpoint, and the reflection identity selects the left endpoint. With \(x=h\) and \(y=(s_i+1)h\), the inequalities \(s_i+1\le n-1\) and \(h\le\rho/n\) ensure \(h\le y\le\rho-h\), so \(r_1-r_i\ge0\). All leaf entries are thus nonnegative, and distinct-leaf entries are strictly positive for \(h>0\).

Finally \(r(x)-1=x(x^3-4x^2+12x-24)/24\). The cubic factor is strictly increasing, since its derivative \(3x^2-8x+12>0\), and has the unique positive zero \(\rho\). Thus \(T_{cu}\ge0\) exactly for \(0\le h\le\rho/n\), and \(T_{cu}<0\) thereafter; positivity cannot return. All eigenvalues of \(T(h)\) are \(r(h\lambda)\) for Laplacian eigenvalues \(\lambda\), and \(r(x)>0\), so \(\|T(h)\|_{2\to2}\le1\) exactly when \(h\lambda_{\max}\le\rho\), i.e. \(h\le\rho/n\).

## Verification
The included standalone program `verify.py` symbolically verifies the reflection and positivity identities, the across-block discriminant/sum-of-squares certificate, the projector entry formulas against exact matrix powers on fifteen heterogeneous clique-bouquet graphs, and additional high-precision positivity and sharp-failure samples on both sides of the boundary. Run `python verify.py` with SymPy and mpmath as declared in `requirements.txt`. All infinite-family conclusions are proved above; the finite matrix tests only corroborate the identities.

## Relationship to prior work
The classic strong-stability-preserving analysis of Gottlieb--Shu--Tadmor and Gottlieb--Gottlieb gives general time-step guarantees and properties for linear discretizations, not this graph-dependent sharp equality with spectral stability. Horváth studies general positivity radii and step-size thresholds, but an exact heterogeneous clique-bouquet computation was not located in the inspected accessible material. Existing exact RK4 positivity results for complete multipartite graphs, trees and strongly regular graphs do not imply the present genuinely nonmultipartite cyclic cases. The spectral decomposition of windmill/friendship graphs is classical; the new statement concerns the matrix sign of the completed RK4 propagator.

## Limitations
The theorem is restricted to unit-weight clique bouquets sharing exactly one universal hub; it does not assert the result for arbitrary graphs possessing a universal vertex. It concerns completed-step positivity only, not intermediate RK stage positivity, and does not certify other time integrators. Originality remains subject to specialized literature not found or not fully accessible in the documented searches. No independent validation has been performed.

## References
- S. Gottlieb, C.-W. Shu, and E. Tadmor, *Strong stability-preserving high-order time discretization methods*, SIAM Review 43 (2001), 89--112, DOI: 10.1137/S003614450036757X. First public electronic publication: 2001-02-02.
- S. Gottlieb and L.-A. J. Gottlieb, *Strong stability preserving properties of Runge--Kutta time discretization methods for linear constant coefficient operators*, Journal of Scientific Computing 18 (2003), 83--109, DOI: 10.1023/A:1020338228736.
- Z. Horváth, *Positivity of Runge--Kutta and diagonally split Runge--Kutta methods*, Applied Numerical Mathematics 28 (1998), 309--326, DOI: 10.1016/S0168-9274(98)00050-6.
- F. Wen, Q. Huang, X. Huang and F. Liu, *The spectral characterization of wind-wheel graphs*, Indian Journal of Pure and Applied Mathematics 46 (2015), 613--631, DOI: 10.1007/s13226-015-0141-8 (graph-structural context, not a numerical-positivity theorem).
