# A sharp edge-deletion reversal for fourth-order diffusion positivity on crown graphs

## Finding
For every integer \(n\ge3\), let \(C_n\) be the **crown graph** obtained by removing a perfect matching from the unweighted complete bipartite graph \(K_{n,n}\). Its combinatorial graph Laplacian is \(L\). The completed classical four-stage fourth-order Runge--Kutta (RK4) step for \(u'=-Lu\) is
\[
T_n(h)=I-hL+\frac{h^2L^2}{2}-\frac{h^3L^3}{6}+\frac{h^4L^4}{24},\qquad h\ge0.
\]
Then
\[
\boxed{T_n(h)\text{ is entrywise nonnegative}\quad\Longleftrightarrow\quad 0\le h\le\frac1{n-1}.}
\]
At the positive endpoint exactly the \(n\) unordered antipodal pairs corresponding to deleted matching edges have zero transition entries. Every other transition entry is strictly positive. Immediately beyond the endpoint, and at every larger timestep, each deleted-matching transition becomes negative; entrywise positivity never returns. Thus the exact RK4 positivity horizon **equals** the forward-Euler positivity horizon on this infinite regular family, even though the RK4 Euclidean spectral-stability horizon is strictly larger, namely \(\rho/[2(n-1)]\), where \(\rho\) is the unique positive root of \(z^3-4z^2+12z-24=0\).

Moreover, the intact \(K_{n,n}\) has RK4 positivity horizon \(\rho/(2n)\). Removing a perfect matching therefore **increases** the largest permissible absolute step at \(n=3\), but **strictly decreases** it at every \(n\ge4\), despite decreasing every vertex degree. This is a sharp graph-size reversal of positivity safety under edge deletion.

## Assumptions and scope
All graphs are finite, simple, unweighted and undirected, with the unnormalized combinatorial Laplacian. The scalar step \(h\) is nonnegative, all values are exact, and entrywise nonnegativity means preservation of the nonnegative cone for **every** nonnegative initial vector after one completed RK4 step. No positivity of internal RK stages is claimed. The crown graph has vertex set \(\{x_1,\ldots,x_n,y_1,\ldots,y_n\}\), with \(x_i\) adjacent to \(y_j\) if and only if \(i\ne j\). Its degree is \(n-1\). The case \(n=2\), which gives a disconnected matching, is excluded.

The result about removal of a matching compares two different graphs at the same integer \(n\), rather than comparing their normalized timestep ratios. In each graph, forward Euler is entrywise nonnegative exactly when \(0\le h\le1/\Delta\) (here the graphs are regular, with degree \(\Delta\)).

## Proof
Write \(m=n-1\), \(R_4(z)=1+z+z^2/2+z^3/6+z^4/24\), and
\[
a=R_4(-nh),\qquad b=R_4(-(n-2)h),\qquad c=R_4(-2mh).
\]
Let \(J\) denote the \(n\)-by-\(n\) all-ones matrix and \(Q=I_n-J/n\). The crown adjacency matrix is \(\bigl(\begin{smallmatrix}0&J-I_n\\J-I_n&0\end{smallmatrix}\bigr)\). The Laplacian has the orthogonal spectral projectors
\[
P_0=\frac1{2n}\begin{pmatrix}J&J\\J&J\end{pmatrix},\quad
P_{2m}=\frac1{2n}\begin{pmatrix}J&-J\\-J&J\end{pmatrix},\quad
P_n=\frac12\begin{pmatrix}Q&Q\\Q&Q\end{pmatrix},\quad
P_{n-2}=\frac12\begin{pmatrix}Q&-Q\\-Q&Q\end{pmatrix}.
\]
Their ranges are mutually orthogonal and sum to the entire vertex space, and their Laplacian eigenvalues are respectively \(0,2m,n,n-2\). Therefore
\[
T_n(h)=P_0+cP_{2m}+aP_n+bP_{n-2}.
\]
The four entry orbits are (i) a diagonal entry \(d\), (ii) an existing edge \(e=T_{x_i y_j}\) with \(i\ne j\), (iii) a distinct same-side pair \(s=T_{x_i x_j}\), and (iv) a deleted-matching/antipodal pair \(p=T_{x_i y_i}\). The projectors give
\[
\begin{aligned}
d&=\frac{1+c+m(a+b)}{2n},&
 e&=\frac{1-c-a+b}{2n},\\
s&=\frac{1+c-a-b}{2n},&
 p&=\frac{1-c+m(a-b)}{2n}.
\end{aligned}
\]
Exact polynomial simplification yields
\[
\boxed{p=\frac{(n-2)m}{6}\,h^3(1-mh)},\qquad
s=\frac{n-2}{24}h^2\bigl((7m^2+1)h^2-12mh+12\bigr).
\]
The quadratic factor in \(s\) has positive leading coefficient and discriminant \(-48(4m^2+1)<0\); hence \(s>0\) whenever \(h>0\). For \(z=mh\) and \(A_m=(2m^2-m+1)/(6m^2)>0\), the edge entry has the positivity decomposition
\[
\boxed{e=h\left[(1-z)(1+A_m z^2)+\frac{z^2}{3}\right].}
\]
Consequently \(e>0\) for \(0<h\le1/m\). Every diagonal entry is strictly positive for all \(h\ge0\): indeed, the scalar polynomial \(R_4(-t)>0\) for \(t\ge0\), as follows from the order-four Taylor formula for \(e^{-t}\) with a negative fifth-order remainder. Thus \(T_n(h)\) is positive definite (all four spectral multipliers are positive), so each diagonal entry is positive. The formula for \(p\) is positive below \(1/m\), vanishes at \(1/m\), and is **negative at every \(h>1/m\)**. This proves the if-and-only-if, the exact zero pattern, and no reentry.

For Euclidean spectral contractivity, note that \(R_4(-t)>0\) and \(R_4(-t)\le1\) precisely for \(0\le t\le\rho\). Indeed,
\[
R_4(-t)-1=\frac{t}{24}(t^3-4t^2+12t-24),
\]
and the cubic is strictly increasing because its derivative \(3t^2-8t+12\) is positive for all real \(t\). The largest Laplacian eigenvalue is \(2m\), proving the spectral threshold \(\rho/(2m)\). Also \(\rho>2\), so this threshold strictly exceeds the positivity threshold.

For the intact complete bipartite graph, the Laplacian has eigenvalues \(0,n,2n\). Its across-part entries equal \([1-R_4(-2nh)]/(2n)\), while each distinct within-part entry is \([1+R_4(-2nh)-2R_4(-nh)]/(2n)\). The latter is nonnegative for every \(h\ge0\), because the function \(t\mapsto R_4(-t)\) is strictly convex: its second derivative is \(1-t+t^2/2=((t-1)^2+1)/2>0\). Positivity therefore holds exactly for \(0\le h\le\rho/(2n)\). Finally the strictly increasing cubic takes values \(-40/27\) and \(3\) at \(t=8/3\) and \(t=3\), respectively, so \(8/3<\rho<3\). Comparing \(1/(n-1)\) with \(\rho/(2n)\) gives the asserted strict reversal between \(n=3\) and \(n=4\), with the latter ordering persisting for all larger \(n\).

## Verification
Execute `python verify.py` with Python 3 and SymPy. The self-contained checker reconstructs all four orbital expressions symbolically from the spectral functions, verifies the three crucial factor identities and discriminant, and independently forms exact rational Laplacian matrices for \(n=3,\ldots,11\) at five prescribed rational timesteps (including both sides of the sharp cutoff). It checks every matrix entry against the analytic orbit formula and every nonnegativity classification. Its successful run is documented in `VERIFICATION.md`. These finite tests supplement, and do not replace, the universally quantified analytic argument above.

## Relationship to prior work
Gottlieb, Shu and Tadmor (2001), and Gottlieb and Gottlieb (2003), established foundational strong-stability-preserving theory for Runge--Kutta discretizations, including linear constant-coefficient operators. Their relevant results address general method guarantees and examples rather than the exact crown-graph entrywise RK4 cutoff and edge-deletion comparison proved here. The crown graph itself is a standard distance-transitive construction. An existing classification of maximum-degree-two networks already accounts for the special case \(n=3\) (the six-cycle), but does not imply the infinite regular-degree family \(n\ge4\). The intact-biclique comparison is included with an independent direct proof to make its logical dependence explicit.

## Limitations
The theorem is for the completed **classical RK4 endpoint**, not for all fourth-order Runge--Kutta tableaux, general explicit SSP methods, nonlinear systems, weighted crowns, or intermediate RK stages. The present derivation proves no edge-deletion monotonicity beyond the stated complete-bipartite/matching-deletion comparison. The exact historical originality assessment remains subject to possible equivalent specialized literature not found in the documented searches. No independent mathematical audit has been performed.

## References
1. S. Gottlieb, C.-W. Shu and E. Tadmor, *Strong stability-preserving high-order time discretization methods*, SIAM Review **43** (2001), 89–112. DOI: `10.1137/S003614450036757X`. Electronically published 2001-02-02. Author-hosted full text: `https://www.math.umd.edu/~tadmor/pub/linear-stability/Gottlieb-Shu-Tadmor.SIREV-01.pdf`.
2. S. Gottlieb and L.-A. J. Gottlieb, *Strong stability preserving properties of Runge--Kutta time discretization methods for linear constant coefficient operators*, Journal of Scientific Computing **18** (2003), 83–109. DOI: `10.1023/A:1020338228736`. Author-hosted full text includes the article as pp. 16–42 of `https://www.cfm.brown.edu/people/sg/SGmcg1.pdf`.
3. E. W. Weisstein, *Crown Graph*, MathWorld, `https://mathworld.wolfram.com/CrownGraph.html` (graph definition and standard notation; undated secondary background, not used for first-public-date determination).
