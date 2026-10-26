# Sharp classical RK4 positivity on every subdivided regular graph

## Finding
Let \(G\) be an arbitrary finite, connected, simple, \(d\)-regular graph, with integer \(d\ge 2\). Form its full edge subdivision \(S(G)\) by replacing each original edge by a path of length two, with unit conductances. Write \(L\) for the combinatorial Laplacian of \(S(G)\) and let \(T_h=I-hL+(hL)^2/2-(hL)^3/6+(hL)^4/24\) be the completed classical four-stage, fourth-order Runge–Kutta step for the heat equation \(u'=-Lu\). Then the following is the exact and nonreentrant entrywise-positivity range:

\[
\boxed{T_h\ge0\text{ entrywise}\quad\Longleftrightarrow\quad 0\le h\le\frac{2}{d+2}.}
\]

For every \(h>2/(d+2)\), at least one transition from an original vertex to a nonincident subdividing vertex is strictly negative. Thus the positivity threshold depends only on the original regular degree, not on the size, girth, eigenvalues or other geometry of \(G\).

The sharp forward-Euler nonnegativity threshold is \(1/d\). Consequently, RK4's permitted positive timestep divided by the forward-Euler one is \(2d/(d+2)\), strictly greater than one for \(d\ge3\). The exact Euclidean spectral-contractivity interval is \(0\le h\le\rho/(d+2)\), where \(\rho\) is the unique positive solution of \(\rho^3-4\rho^2+12\rho-24=0\) (approximately \(2.7852935634\)); this is strictly larger than the positivity interval.

## Assumptions and scope
All graphs are finite, simple, connected and unweighted; \(d\) is an integer at least two. Every original edge is subdivided exactly once. The Laplacian is \(L=D-A\), with no degree or normalized-Laplacian rescaling. Positivity means \(T_hx\ge0\) for every entrywise nonnegative input \(x\), equivalently every entry of \(T_h\) is nonnegative; this applies to a **completed** RK4 step, not to each intermediate Runge–Kutta stage. The claim holds for every real \(h\ge0\) and every qualifying \(G\). Graph connectivity is used to ensure a length-two path supplying a strict sharpness witness.

## Proof
Let \(V\) and \(E\) be the original vertex and edge sets, with \(|V|=n\), \(|E|=m\). Identify an edge with its new subdivision vertex. Let \(B\in\{0,1\}^{n\times m}\) be the **unoriented** vertex–edge incidence matrix, and \(A\) the adjacency matrix of \(G\). Set \(C=BB^{\mathsf T}=dI+A\), and \(Q=B^{\mathsf T}B\). Ordered by original vertices then edge-vertices, the Laplacian is

\[
 L=\begin{pmatrix}dI&-B\\-B^{\mathsf T}&2I\end{pmatrix}.
\]

Direct multiplication gives the following necessary blocks (these identities are also checked symbolically and against direct rational matrices in the accompanying program):

\[
\begin{aligned}
(L^2)_{VV}&=d^2I+C,&(L^2)_{VE}&=-(d+2)B,&(L^2)_{EE}&=4I+Q,\\
(L^3)_{VV}&=d^3I+(2d+2)C,&(L^3)_{VE}&=-(d^2+2d+4)B-CB,&(L^3)_{EE}&=8I+(d+4)Q,\\
(L^4)_{VV}&=(d^2I+C)^2+(d+2)^2C,&(L^4)_{VE}&=-(d+2)[(d^2+4)B+2CB],&
(L^4)_{EE}&=(4I+Q)^2+(d+2)^2Q.
\end{aligned}
\]

Each pair of different vertices of \(S(G)\) belongs to one of six incidence types. Below \(u,v\) denote original vertices and \(e,f\) denote original edges, viewed as subdivision vertices. For \(u\notin e\), put \(c(u,e)=|N_G(u)\cap e|\), an integer in \(\{0,1,2\}\). The off-diagonal entries are:

**(i) Nonincident original vertex and subdivision vertex.**
\[
(T_h)_{u,e}=\frac{c(u,e)h^3}{6}\left(1-\frac{(d+2)h}{2}\right).
\]

**(ii) Incident original vertex and subdivision vertex.** Writing \(e\ni u\),
\[
(T_h)_{u,e}=h F_d(h),\qquad F_d(h)=1-\frac{d+2}{2}h+\frac{d^2+3d+5}{6}h^2-\frac{(d+2)(d^2+2d+6)}{24}h^3.
\]

**(iii) Adjacent original vertices.** For \(u\sim v\), put \(t=|N_G(u)\cap N_G(v)|\ge0\). Then
\[
(T_h)_{u,v}=\frac{h^2}{24}\left(12-8(d+1)h+(3d^2+6d+4+t)h^2\right).
\]

**(iv) Nonadjacent distinct original vertices.** The entry is \((T_h)_{u,v}=h^4(A^2)_{uv}/24\ge0\).

**(v) Edge-vertices sharing an original endpoint.** If \(e=\{u,v\}\) and \(f=\{u,w\}\) with \(v\ne w\), set \(s=A_{v,w}\in\{0,1\}\). Then
\[
(T_h)_{e,f}=\frac{h^2}{24}\left(12-4(d+4)h+(d^2+5d+14+s)h^2\right).
\]

**(vi) Disjoint edge-vertices.** If \(e\cap f=\varnothing\), then
\[
(T_h)_{e,f}=\frac{h^4}{24}\sum_{a\in e}\sum_{b\in f}A_{ab}\ge0.
\]

For type (iii), the quadratic discriminant is \(-80d^2-160d-128-48t<0\). For type (v), it is \(-32d^2-112d-416-48s<0\). Their quadratic leading coefficients are positive; hence both types are strictly positive for \(h>0\). Types (iv) and (vi) are nonnegative for all \(h\ge0\).

For type (ii), put \(x=(d+2)h/2\), \(a_d=2(d^2+3d+5)/(3(d+2)^2)\), and \(b_d=(d^2+2d+6)/(3(d+2)^2)\). A direct rearrangement yields \(F_d(h)=1-x+x^2(a_d-b_dx)\), where \(a_d-b_d=1/3\). Whenever \(0\le h\le2/(d+2)\), we have \(0\le x\le1\), and therefore \(F_d(h)\ge1-x+x^2/3>0\).

The diagonal entries of \(T_h\) are strictly positive for every \(h\ge0\). Indeed \(L\) is symmetric positive semidefinite and its stability polynomial obeys, for all real \(z\),
\[
R_4(-z)=1-z+\frac{z^2}{2}-\frac{z^3}{6}+\frac{z^4}{24}=\left(1-\frac z2\right)^2+\frac{z^2((z-2)^2+2)}{24}>0.
\]
Thus \(T_h\) itself is positive definite. Together with the previous pair classes, this proves entrywise nonnegativity throughout \(0\le h\le2/(d+2)\).

For **sharpness**, choose a simple length-two path \(u\sim v\sim w\) in \(G\), possible because \(d\ge2\). Let \(e=\{v,w\}\) be the corresponding subdividing vertex. It is not incident to \(u\), and \(c(u,e)\ge1\) because \(u\sim v\). Type (i) then shows \((T_h)_{u,e}<0\) for every \(h>2/(d+2)\), with equality exactly at the threshold. This proves both necessity and absence of a later positivity window.

For the spectral statement, the positive vector taking value \(d\) at each original vertex and value \(2\) at each edge-vertex is an eigenvector with eigenvalue \(d+2\) of the **signless** Laplacian. The subdivision graph is connected and bipartite, so Perron–Frobenius and bipartite sign conjugacy imply \(\lambda_{\max}(L)=d+2\). Since \(R_4(-z)>0\) and \(R_4(-z)\le1\) for \(z\ge0\) if and only if \(z\le\rho\), with \(\rho\) the unique positive root of the strictly increasing cubic \(z^3-4z^2+12z-24\), spectral contractivity is equivalent to \(h(d+2)\le\rho\). Finally, \(R_4(-hL)\) preserves row sums because \(L\mathbf1=0\); forward Euler is entrywise nonnegative exactly when \(h\le1/d\), as original vertices have degree \(d\) and edge-vertices degree two.

## Verification
Run `python verify.py` from the directory containing `verify.py` and `requirements.txt` after installing SymPy. The deterministic script uses symbolic identities and exact integer/rational arithmetic. It checked 24 connected regular base graphs, 9,338 off-diagonal coefficient vectors against the incidence formulas, multiple exact timestep endpoints, row sums, strict negative witnesses and the maximal-Laplacian eigenvector; the recorded result was:

`VERIFY_OK 24 different regular base graphs; 9338 exact off-diagonal RK4 coefficient comparisons; rational steps and spectral eigenvector verified; all symbolic certificates verified`

This is finite corroboration, not an exhaustive proof over the infinite graph class. The proof above is the analytical certificate. The script is standalone and does not load any earlier result.

## Relationship to prior work
Gottlieb, Shu and Tadmor (2001) develop the foundational strong-stability-preserving Runge–Kutta framework, including linear-method restrictions; their paper does not give an exact endpoint-positivity classification for Laplacians of full subdivisions of regular graphs. Khalsaraei (2015) analyzes positivity of the classical method for special discretizations of advection and Burgers' equation, not this incidence-matrix graph class. Steinerberger (2018) studies the exact semigroup's small-time graph heat kernel and its distance dependence, which does not imply a globally sharp finite-step Taylor positivity interval. The present distinction is between *completed-step* entrywise nonnegativity and both spectral contractivity and general-purpose SSP conditions. Previously known cycle and complete-bipartite special cases are not treated as novel themselves.

## Limitations
The theorem assumes unit edge weights and equal original degrees, and does not apply automatically to arbitrary edge subdivisions of irregular graphs, normalized/random-walk Laplacians, arbitrary Runge–Kutta methods, or every internal stage of the classical RK4 scheme. A source-specific historical overlap is still possible in incompletely indexed network-diffusion literature; no independent review has been carried out.

## References
- S. Gottlieb, C.-W. Shu and E. Tadmor, “Strong Stability-Preserving High-Order Time Discretization Methods,” *SIAM Review* 43 (2001), 89–112. Published electronically 2001-02-02. DOI: 10.1137/S003614450036757X. Author-accessible full text: https://drum.lib.umd.edu/bitstreams/faa96f40-0fbb-4af0-84a3-5e3b80c908df/download.
- M. M. Khalsaraei, “Positivity of an explicit Runge–Kutta method,” *Ain Shams Engineering Journal* (2015), DOI: 10.1016/j.asej.2015.05.018. Accessible full text: https://www.researchgate.net/publication/282534406_Positivity_of_an_explicit_Runge-Kutta_method.
- S. Steinerberger, “Varadhan Asymptotics for the Heat Kernel on Finite Graphs,” *Discrete Applied Mathematics* (2018), arXiv:1801.02183, https://arxiv.org/abs/1801.02183.
