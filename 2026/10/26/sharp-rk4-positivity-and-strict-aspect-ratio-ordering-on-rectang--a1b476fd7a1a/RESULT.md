# Sharp RK4 positivity and strict aspect-ratio ordering on rectangular rook graphs
## Finding
For every pair of integers \(2\le p<q\), let \(G=K_p\mathbin{\square}K_q\) be the unweighted Cartesian-product graph and let \(L\) be its combinatorial Laplacian. The classical explicit fourth-order Runge–Kutta diffusion end step is
\[
T_{p,q}(h)=I-hL+\frac{h^2L^2}{2}-\frac{h^3L^3}{6}+\frac{h^4L^4}{24},\qquad h\ge0.
\]
Set
\[
\begin{aligned}
a_{p,q}&=\frac p2+q-1,\\
b_{p,q}&=\frac{p^2}{6}+\frac{(p+q)(q-1)}2,\\
c_{p,q}&=\frac{p^3}{24}+\frac{p^2(q-1)}6+\frac{pq(q-1)}4+\frac{q^2(q-1)}6,\\
f_{p,q}(h)&=1-a_{p,q}h+b_{p,q}h^2-c_{p,q}h^3.
\end{aligned}
\]
There is exactly one positive root \(H_{p,q}\) of \(f_{p,q}\). **The end step is entrywise nonnegative exactly for \(0\le h\le H_{p,q}\)**, and every \(h>H_{p,q}\) gives strictly negative transition entries between vertices differing only in their first, smaller-coordinate factor. Because all row sums equal one, this is also the exact row-stochasticity interval.

Moreover, **fix an integer \(N\ge6\)**. For every pair of integers \(2\le p<p'<N/2\), writing \(q=N-p\) and \(q'=N-p'\), the positivity horizons satisfy
\[
H_{p,q}<H_{p',q'}.
\]
Thus making the two factors more balanced, while retaining their unequal sizes and fixed sum, strictly improves the admissible RK4 timestep. In the scaled regime \(p/(p+q)\to r\in[0,1/2)\),
\[
(p+q)H_{p,q}\longrightarrow z_r,
\]
where \(z_r\) is the unique positive root of
\[
1-\left(1-\frac r2\right)z+\left(\frac12-\frac r2+\frac{r^2}{6}\right)z^2-\frac{(2-r)(r^2-2r+2)}{24}z^3=0.
\]
This formula includes \(z_0=1.5960716379\ldots\) for fixed \(p\) and growing \(q\). The aspect-ratio ordering concerns the distinct-size graphs; the balanced case is not asserted as a new classification here.

## Assumptions and scope
Each \(K_m\) is the unweighted complete graph with \(m\) vertices, every edge of the Cartesian product has unit conductance, and \(L=D-A\) is its symmetric combinatorial Laplacian. The classical fourth-order explicit Runge–Kutta stability polynomial is applied to \(u'=-Lu\) with nonnegative initial coordinates. Only the **completed** timestep is required to be nonnegative, not every internal Runge–Kutta stage. We assume \(p,q\) are integers and \(2\le p<q\); the fixed-sum ordering compares two unequal factor pairs. No statement about directed generators, other integrators, or arbitrary product graphs is intended.

## Proof
**Spectral projectors and all four entry types.** Define \(P_m=\mathbf1\mathbf1^{\mathsf T}/m\) and \(Q_m=I_m-P_m\). Since \(L(K_m)=mQ_m\), write \(r_t(h)=\sum_{j=0}^4(-th)^j/j!\). The four commuting spectral projectors give the exact identity
\[
T=P_p\otimes P_q+r_pQ_p\otimes P_q+r_qP_p\otimes Q_q+r_{p+q}Q_p\otimes Q_q.
\]
For vertices \((i,j)\) and \((k,\ell)\), the four possible entries, in the order first-coordinate difference only, second-coordinate difference only, both coordinates different, and identical vertices, are respectively
\[
\begin{aligned}
A&=\frac{1+(q-1)r_q-r_p-(q-1)r_{p+q}}{pq}=h f_{p,q}(h),\\
B&=\frac{1+(p-1)r_p-r_q-(p-1)r_{p+q}}{pq},\\
C&=\frac{1-r_p-r_q+r_{p+q}}{pq},\\
D&=\frac{1+(p-1)r_p+(q-1)r_q+(p-1)(q-1)r_{p+q}}{pq}.
\end{aligned}
\]
Expanding the polynomial factors yields
\[
A-B=\frac{(p-q)h^2}{24}\Big(12-8(p+q)h+(3p^2+5pq+3q^2)h^2\Big).
\]
The quadratic in parentheses has positive leading coefficient and discriminant \(-16(5p^2+7pq+5q^2)<0\). Thus \(B>A\) for every \(h>0\), since \(p<q\).

For pairs differing in both coordinates,
\[
C=h^2\left(1-\frac{p+q}{2}h+\frac{2p^2+3pq+2q^2}{12}h^2\right).
\]
The quadratic has positive leading coefficient and discriminant \(-(5p^2+6pq+5q^2)/12<0\). Consequently \(C>0\) for every \(h>0\). For the diagonal entries, \(r_t(h)>0\) for every \(t,h\ge0\), since
\[
24r_t(h)=[((th)^2-2th)]^2+8(th-3/2)^2+6>0.
\]
Each diagonal entry is a sum of positive scalar \(r_t\) values with nonnegative spectral-projector diagonal coefficients; hence \(D>0\). In summary, **all possible entrywise positivity failures are detected by the single polynomial \(A=h f_{p,q}(h)\)**.

**Unique sharp threshold and no reentry.** The coefficients \(a,b,c\) are strictly positive. Expansion and factorization establish
\[
\begin{aligned}
144(3ac-b^2)={}&5p^4+30p^3(q-1)+6p^2(q-1)(11q-6)\\
&+36pq(q-1)(2q-1)+36q^2(q-1)^2>0.
\end{aligned}
\]
Therefore the quadratic \(3ch^2-2bh+a\) has negative discriminant \(4(b^2-3ac)<0\) and positive leading coefficient. This implies \(f'(h)=-a+2bh-3ch^2<0\) for all real \(h\). Since \(f(0)=1\) and \(f(h)\to-\infty\) as \(h\to+\infty\), it has a unique positive root \(H_{p,q}\), is nonnegative precisely up to that root, and strictly negative afterward. The entry \(A\) provides the stated sharp witness; stochastic row sums follow from \(L\mathbf1=0\).

**Fixed-vertex-count strict improvement under balancing.** Treat \(p\) temporarily as a real variable with \(2\le p<N/2\), put \(q=N-p\), and hold \(N\) fixed. Direct differentiation gives
\[
24\,\frac{\partial f_{p,N-p}(h)}{\partial p}\frac1h
=12+(-12N+8p)h+(6N^2-8Np-2N+3p^2+4p)h^2=:Z_{p,N}(h).
\]
For \(N\ge6\) and \(2\le p\le N/2\), the leading coefficient is at least \(11N^2/4>0\). The discriminant of \(Z\), regarded as a quadratic in \(h\), is
\[
-16(9N^2-12Np-6N+5p^2+12p)<0.
\]
The expression in parentheses is decreasing in \(p\in[2,N/2]\) and is at least \(17N^2/4>0\) at \(p=N/2\). Hence \(Z_{p,N}(h)>0\) for every real \(h\), and \(\partial_p f_{p,N-p}(h)>0\) whenever \(h>0\). Evaluate at the unique positive root for the first factor pair: the cubic for the more balanced pair is strictly positive there, and its strict decrease forces its root to be strictly larger. This establishes the claimed comparison for all eligible unequal integer pairs. (The explicit continuous endpoint comparison at equality of the two factor sizes is a consequence, but not included in the new unequal-size claim.)

**Large-network scaling.** Write \(N=p+q\), \(r=p/N\), and \(h=z/N\). Divide \(a,b,c\) respectively by \(N,N^2,N^3\). As \(N\to\infty\), their limits are \(1-r/2\), \(1/2-r/2+r^2/6\), and \((2-r)(r^2-2r+2)/24\). Every limiting cubic remains strictly decreasing on the positive real line: take the limit of the positive-coefficient derivative discriminant certificate above, or directly check its derivative quadratic discriminant is negative on \(0\le r<1/2\). Uniform convergence on compact \(z\)-intervals together with strict monotonicity and opposite signs at zero and a sufficiently large fixed argument gives convergence of the unique positive roots to \(z_r\).

**Comparison with forward Euler.** Forward Euler is nonnegative for \(0\le h\le1/(p+q-2)\). Put \(P=I-L/(p+q-2)\), which is row-stochastic and nonnegative. The scalar identity
\[
R_4(P-I)=\frac38 I+\frac13 P+\frac14P^2+\frac1{24}P^4
\]
proves nonnegativity at that Euler endpoint; its \(A\)-type edge entries are strictly positive because \(P/3\) contributes a positive amount. By strict decrease of \(f\), the sharp RK4 horizon therefore satisfies \(H_{p,q}>1/(p+q-2)\).

## Verification
A standalone exact symbolic-and-rational checker is included as `verify.py` and depends on SymPy (see `requirements.txt`). Running `python verify.py` from the extracted folder gives

`VERIFY_OK 9 symbolic identities, 36 exact full RK4 matrices, 19134 exact vertex-pair entries; all finite endpoint tests`

It verifies the four spectral entries against direct rational RK4 matrix powers for 36 exact graph/timestep instances, including **every ordered vertex pair** in those matrices, and symbolically checks the critical quadratic discriminants, derivative identity, and positivity certificate. It also samples rational parameter boundaries. These finite checks **do not prove** the infinite-family claims; the preceding exact algebraic identities and sign arguments do.

## Relationship to prior work
Gottlieb, Shu and Tadmor (2001) systematically develop strong-stability-preserving timestep restrictions, offering an important framework for positivity guarantees. Their theory does not provide an entrywise necessary-and-sufficient criterion, factor-aspect monotonicity, or exact sharp roots for the distinct-factor rook graphs considered here. Gottlieb and Gottlieb (2003) study strong-stability preservation for linear constant-coefficient problems, again at a general stability-method level rather than these spectral-projector comparisons. Mehdizadeh Khalsaraei (2015) sharpens classical RK4 positivity conditions for advection and related semidiscretized systems, but its inspected method-specific positivity statements do not classify rook-graph heat diffusion. Horváth (1998) provides earlier general positivity theory; the accessible abstract does not resolve whether it might imply stronger general results relevant here. Related fourth-order implicit Padé or Gauss methods have a different stability function and their graph-specific positivity classifications do not imply the present polynomial RK4 classification. The balanced Hamming-graph and complete-multipartite cases concern different parameter domains/graph families and are not reclassified here.

## Limitations
This is an end-step, linear diffusion and simple unweighted graph result. It does not guarantee positivity of internal RK4 stages, nonlinear systems, weighted/directed rook graphs or other graph products. The asymptotic limits concern sequences with the stated aspect ratio. The source comparison is not an exhaustive proof of novelty; especially, the inaccessible full text of Horváth (1998) and other potentially specialized material may entail undiscovered overlap. Independent mathematical review has not been performed.

## References
1. S. Gottlieb, C.-W. Shu, and E. Tadmor, *Strong Stability-Preserving High-Order Time Discretization Methods*, SIAM Review 43 (2001), 89–112, DOI:10.1137/S003614450036757X. Original source identifies online publication on 2001-02-02. Authorized open version: https://math.umd.edu/~tadmor/pub/linear-stability/Gottlieb-Shu-Tadmor.SIREV-01.pdf.
2. S. Gottlieb and L.-A. J. Gottlieb, *Strong Stability Preserving Properties of Runge–Kutta Time Discretization Methods for Linear Constant Coefficient Operators*, Journal of Scientific Computing 18 (2003), 83–109, DOI:10.1023/A:1020338228736. Open authors' version: https://www.cfm.brown.edu/people/sg/SGmcg1.pdf.
3. M. Mehdizadeh Khalsaraei, *Positivity of an Explicit Runge–Kutta Method*, Ain Shams Engineering Journal 6 (2015), 1217–1223, DOI:10.1016/j.asej.2015.05.018.
4. Z. Horváth, *Positivity of Runge–Kutta and Diagonally Split Runge–Kutta Methods*, Applied Numerical Mathematics 28 (1998), 309–326, DOI:10.1016/S0168-9274(98)00050-6 (full text not inspected).
