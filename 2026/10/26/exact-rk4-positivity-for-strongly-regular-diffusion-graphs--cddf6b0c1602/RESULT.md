# Exact RK4 positivity for strongly regular diffusion graphs

## Finding

**Theorem (one exact cutoff and a spectral-stability dichotomy).** Let \(G\) be any finite, simple, connected, noncomplete strongly regular graph with parameters \((v,k,\lambda,\mu)\), so \(0<k<v-1\) and \(\mu>0\). All graph edges have unit conductance. Let \(A\) be its adjacency matrix, \(L=kI-A\), and
\[
T(h)=I-hL+\frac{h^2L^2}{2}-\frac{h^3L^3}{6}+\frac{h^4L^4}{24},\qquad h\ge0.
\]
Let \(r>s\) be the two restricted eigenvalues of \(A\); equivalently, the two roots of \(z^2-(\lambda-\mu)z-(k-\mu)=0\). Define
\[
\alpha=k-r,\quad \beta=k-s,\quad
u=\frac{1-(k-s)/v}{r-s},\quad w=\frac1v+u,
\qquad M_j=w\beta^j-u\alpha^j\quad(j=1,2,3,4).
\]
Here \(0<\alpha<\beta\), \(u\ge0\), and \(M_1=1\). The cubic
\[
C_G(h)=1-\frac{M_2h}{2}+\frac{M_3h^2}{6}-\frac{M_4h^3}{24}
\]
is strictly decreasing on \([0,\infty)\) and has one positive root \(H_G\). Exactly
\[
T(h)\text{ is entrywise nonnegative}\quad\Longleftrightarrow\quad 0\le h\le H_G.
\]
For every \(h>0\), all diagonal entries and all entries indexed by distinct **nonadjacent** vertices are strictly positive. Every adjacent entry equals \(hC_G(h)\), and every one is strictly negative for \(h>H_G\). In particular, positivity has no later recovery, and \(H_G>1/k\), strictly improving on the forward-Euler positivity limit.

Let \(\rho\) be the unique positive zero of \(24-12z+4z^2-z^3\). The sharp Euclidean spectral-stability limit for \(T(h)\) is \(\rho/\beta\). Moreover,
\[
H_G=\rho/\beta\quad\Longleftrightarrow\quad
G\text{ is a complete multipartite graph with equal part sizes}.
\]
For every **primitive** strongly regular graph (both \(G\) and its complement connected), one has \(H_G<\rho/\beta\), a strict gap between entrywise positivity and spectral contractivity.

**Natural infinite-family corollary.** For the triangular/Johnson graph \(T_n=J(n,2)=L(K_n)\), \(n\ge5\), the cutoff is the unique positive zero of
\[
P_n(h)=24-(36n-72)h+(28n^2-88n+48)h^2
 -(15n^3-62n^2+68n-24)h^3.
\]
The RK4 positivity limit exceeds **twice** the forward-Euler positivity limit precisely for integer \(n\ge9\); it is smaller for \(5\le n\le8\), with no equality. The ratio of the RK4 horizon to the forward-Euler horizon tends to the unique positive root \(2.07786763\ldots\) of \(192-144x+56x^2-15x^3=0\).

## Assumptions and scope

A strongly regular graph has constant degree \(k\), exactly \(\lambda\) common neighbors for every adjacent vertex pair, and exactly \(\mu\) common neighbors for every nonadjacent pair. The graph is required to be finite, undirected, simple, connected, noncomplete, and unweighted. Thus \(\mu>0\), \(k\ge\mu\), and \(k>\lambda\). The result concerns the **completed classical four-stage, fourth-order explicit Runge–Kutta step** for the linear diffusion equation \(x'(t)=-Lx(t)\), not intermediate-stage positivity, nonlinear SSP coefficients, other integrators, directed generators, or arbitrary weighted strongly regular graphs. No assertion is made about non-strongly-regular graphs or nonuniform edge conductances. The vertex count \(v\) must not be confused with the spectral scalar \(w\).

## Proof

**1. Exact adjacency algebra and nonedge positivity.** The strongly regular identity is
\[
A^2=(k-\mu)I+(\lambda-\mu)A+\mu J,
\qquad AJ=kJ.
\]
Consequently \(T(h)\) belongs to the span of \(I,A,J\), and its off-diagonal entries depend only on adjacency. For distinct nonadjacent \(x,y\), direct multiplication gives
\[
T(h)_{xy}=\frac{\mu h^2}{24}
\left[12-4(2k-\lambda+\mu)h+D h^2\right],
\]
where
\[
D=3k(k-\lambda+\mu)+(k-\mu)+(\lambda-\mu)^2>0.
\]
The discriminant of the bracket is exactly
\[
-16\left[5k(k-\lambda+\mu)+3(k-\mu)+2(\lambda-\mu)^2\right]<0.
\]
The quadratic is therefore strictly positive for all real \(h\). Its prefactor is strictly positive for \(h>0\). The diagonal is also positive because \(T(h)=R_4(-hL)\) is positive definite: for every real \(z\),
\[
R_4(-z)=\left(1-\frac z2\right)^2+
\frac{z^2\left[(z-2)^2+2\right]}{24}>0.
\]
Hence only entries at edges can obstruct positivity.

**2. Spectral-projector signs at edges.** Let \(E_0=J/v\), \(E_r\), and \(E_s\) be the orthogonal adjacency spectral projections for eigenvalues \(k,r,s\). The two nonzero Laplacian eigenvalues are \(\alpha=k-r\) and \(\beta=k-s\), with \(0<\alpha<\beta\). For adjacent distinct \(x,y\), solving the two projector equations gives
\[
(E_r)_{xy}=u=\frac{1-(k-s)/v}{r-s},\qquad
(E_s)_{xy}=-\left(\frac1v+u\right)=-w.
\]
The complement adjacency matrix \(\bar A=J-I-A\) is regular of degree \(v-k-1\), with restricted eigenvalue \(-1-s\). Since no eigenvalue exceeds the regular degree, \(k-s\le v\), so \(u\ge0\); equality holds precisely when \(\bar G\) is disconnected. For a connected noncomplete strongly regular graph, this latter condition is equivalent to \(G\) being complete multipartite with equal part sizes. Since \(L_{xy}=-1\), one has \(w\beta-u\alpha=1\). Writing \(U=u\alpha\) and \(V=w\beta\), this is \(0\le U<V\) and \(V-U=1\). Thus for every integer \(j\ge1\),
\[
-(L^j)_{xy}=M_j=V\beta^{j-1}-U\alpha^{j-1}>0.
\]
In particular \(T(h)_{xy}=hC_G(h)\), with the polynomial in the finding.

**3. Unique zero, with a global derivative certificate.** Set \(z=\alpha/\beta\in(0,1)\) and \(t=U/V\in[0,1)\). The positive coefficients \(M_j\) satisfy
\[
\frac{M_3^2}{M_2M_4}
=\frac{(1-tz^2)^2}{(1-tz)(1-tz^3)}
\le\frac{(1+z)^2}{1+z+z^2}<\frac43.
\]
The first inequality follows by differentiating the left expression in \(t\), whose derivative is
\[
\frac{z(1-z)^2(1-t^2z^4)}{(1-tz)^2(1-tz^3)^2}>0;
\]
the last follows from
\[
\frac43-\frac{(1+z)^2}{1+z+z^2}
=\frac{(1-z)^2}{3(1+z+z^2)}>0.
\]
Now \(C_G'(h)=-M_2/2+M_3h/3-M_4h^2/8\), a concave quadratic. Its maximum is
\[
-\frac{M_2}{2}+\frac{2M_3^2}{9M_4}
<-\frac{M_2}{2}+\frac{8M_2}{27}<0.
\]
Therefore \(C_G\) is strictly decreasing, \(C_G(0)=1\), and its negative cubic leading coefficient forces exactly one positive root. This, together with Step 1, proves the exact positivity interval and permanent failure above it.

**4. Euler and spectral comparisons.** The forward-Euler matrix \(B=I-L/k=A/k\) is stochastic and nonnegative. The fourth-order polynomial obeys the exact identity
\[
T(1/k)=\frac38I+\frac13B+\frac14B^2+\frac1{24}B^4.
\]
Every edge entry is at least \(1/(3k)>0\); hence strict monotonicity of \(C_G\) gives \(H_G>1/k\). The scalar RK4 stability polynomial \(R_4(-z)\) is positive for \(z\ge0\) and is at most one exactly for \(0\le z\le\rho\), because \(R_4(-z)-1=-z[24-12z+4z^2-z^3]/24\) and the bracket is strictly decreasing on the real line. The nonzero Laplacian eigenvalues are \(\alpha<\beta\), so the spectral-stability horizon is \(\rho/\beta\). At its endpoint, \(R_4(-\beta h)=1\) and \(0<R_4(-\alpha h)<1\), whence every edge entry is
\[
T(\rho/\beta)_{xy}=
\frac1v(1-1)+u\left(R_4(-\alpha\rho/\beta)-1\right).
\]
It is negative when \(u>0\), giving \(H_G<\rho/\beta\). When \(u=0\), the edge entry is \([1-R_4(-\beta h)]/v\), nonnegative precisely up to spectral stability, while Step 1 handles all other entries. This proves the stated dichotomy.

**5. The triangular-family threshold.** The graph \(T_n\) has parameters \((\binom n2,2(n-2),n-2,4)\); inserting these into the adjacency algebra gives the displayed \(P_n\), and its nonedge entries are
\[
\frac{h^2}{6}\left[12-(12n-8)h+(7n^2-10n+4)h^2\right]>0.
\]
Because \(k=2(n-2)\), twice the Euler step is \(h=1/(n-2)\). Direct substitution gives
\[
P_n\left(\frac1{n-2}\right)
=\frac{n^3-10n^2+12n+24}{(n-2)^3}.
\]
The numerator is negative at integers \(5,6,7,8\), positive at \(9\), and strictly increasing thereafter because its derivative is positive on \([9,\infty)\). The sign of the decreasing cubic gives the exact cutoff at nine. Writing \(m=n-2\) and \(x=2m h\), the cubic becomes
\[
24-18x+\left(7+\frac6m-\frac4{m^2}\right)x^2
-\left(\frac{15}{8}+\frac{7}{2m}-\frac{2}{m^3}\right)x^3.
\]
Its unique positive zero converges to the unique positive zero of \(192-144x+56x^2-15x^3\), proving the stated limiting gain.

## Verification

Run `python verify_srg_rk4.py` with Python 3 and SymPy installed. The program independently derives the \(I,A,J\) algebraic expression, tests the exact nonedge discriminant and triangular specialization, verifies the cubic-ratio certificate symbolically, and performs exact rational RK4 matrix checks on 23 strongly regular graph examples (9,976 off-diagonal comparisons). It separately verifies the doubled-Euler substitution. The printed success message is a reproducible finite check, **not** a substitute for the universal projector/discriminant proof given above.

## Relationship to prior work

Gottlieb, Shu, and Tadmor (2001) developed the SSP time-discretization framework, including the distinction between high-order linear stability and stronger convexity-based properties. Gottlieb and Gottlieb (2003) analyzed SSP Runge–Kutta schemes for linear constant-coefficient operators; the argument here instead determines the sharp **completed classical RK4 matrix-positivity** cutoff on each connected strongly regular graph. Brouwer and Haemers' *Spectra of Graphs* (2011 preprint; 2012 book) supplies the standard strongly regular spectral algebra and primitive/imprimitive classification, not the RK4 numerical-positivity result. Known exact results for complete multipartite diffusion, five-cycles, and rectangular rook networks cover some special graph instances but neither imply the primitive strongly regular graph theorem nor classify the strict spectral-stability gap for the whole family. The proof above separately establishes the positive nonedge invariant and cubic monotonicity that are not supplied by a generic eigenvalue stability inequality.

## Limitations

The claim concerns an exact linear time-discretization endpoint on finite simple undirected unit-edge strongly regular graphs. It does not make a universal SSP guarantee for nonlinear operators, positivity of RK4 intermediate stages, weighted or directed graph generators, or graphs with four or more Laplacian eigenvalues. The literature comparison found no covering result among inspected relevant sources, but a specialized equivalent statement may exist outside accessible/indexed publications. Self-review is not independent audit.

## References

1. S. Gottlieb, C.-W. Shu, E. Tadmor, *Strong Stability-Preserving High-Order Time Discretization Methods*, SIAM Review **43** (2001), 89–112; DOI 10.1137/S003614450036757X; original online publication 2001-02-02; author-hosted full text: https://www.math.umd.edu/~tadmor/pub/linear-stability/Gottlieb-Shu-Tadmor.SIREV-01.pdf.
2. S. Gottlieb, L.-A. J. Gottlieb, *Strong Stability Preserving Properties of Runge–Kutta Time Discretization Methods for Linear Constant Coefficient Operators*, Journal of Scientific Computing **18** (2003), 83–109; DOI 10.1023/A:1020338228736; author-hosted text: https://www.cfm.brown.edu/people/sg/SGmcg1.pdf (relevant work starts at PDF page 17).
3. A. E. Brouwer, W. H. Haemers, *Spectra of Graphs*, monograph dated 2011-02-01, chapter 9, Springer (2012); https://aeb.win.tue.nl/2WF02/spectra.pdf; DOI 10.1007/978-1-4614-1939-6.
