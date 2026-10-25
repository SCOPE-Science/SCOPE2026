# The six-cycle is the first cycle to lose fourth-order Gauss positivity

## Finding

Consider heat diffusion on the unweighted undirected cycle \(C_n\), for every integer \(n\ge3\), with its combinatorial Laplacian \(L_n\). At any dimensionless step \(h\ge0\), let the **completed two-stage, fourth-order Gauss–Legendre step** be
\[
T_n(h)=(12I+6hL_n+h^2L_n^2)^{-1}(12I-6hL_n+h^2L_n^2).
\]
Then \(T_n(h)\) is entrywise nonnegative for **every** \(h\ge0\) if and only if \(n\in\{3,4,5\}\). For every \(n\ge6\), its adjacent-vertex entry is strictly negative for all sufficiently large \(h\).

The first failing cycle, \(C_6\), admits the complete **sharp step-size characterization**
\[
T_6(h)\ge0\text{ entrywise}\quad\Longleftrightarrow\quad0\le h\le\rho,
\]
where \(\rho\in(6,7)\), approximately \(6.36885080963102\), is the **unique positive root** of
\[
5h^4-12h^3-102h^2-144h-72=0.
\]
Beyond \(\rho\), **precisely the entries between adjacent vertices** are negative; all remaining entries stay strictly positive for every \(h>0\). This is a statement about the **completed endpoint matrix** only, not the internal Runge–Kutta stages.

## Assumptions and scope

\(C_n\) is a unit-conductance simple undirected cycle (three vertices form a triangle). Label vertices cyclically by \(0,\ldots,n-1\), so the off-diagonal entries of \(L_n\) are \(-1\) for adjacent vertices, the diagonal entries are \(2\), and row sums vanish. The step \(h\) is dimensionless; a physical common edge rate \(a>0\) replaces \(h\) by \(ah\). We require *entrywise*, not merely spectral, nonnegativity for every nonnegative initial vector. In the phrase "unconditionally positive" the parameter is all finite \(h\ge0\).

## Proof

**1. Spectral well-definition and positive diagonals.** Put \(f(x)=(x^2-6x+12)/(x^2+6x+12)\) for \(x\ge0\). The numerator is \((x-3)^2+3>0\), and the denominator is positive. Therefore \(T_n(h)=f(hL_n)\) is real symmetric **positive definite** for every finite \(h\ge0\); in particular, all diagonal entries are strictly positive. Also \(T_n(h)\mathbf1=\mathbf1\).

**2. Exact five- and six-cycle kernels.** For \(C_5\) set
\[
E_5(h)=25h^4+150h^3+360h^2+360h+144.
\]
Direct polynomial matrix multiplication (equivalently, diagonalization of the circulant Laplacian) gives the complete first row of \(T_5(h)\) as the circular arrangement of the three distance-class values
\[
\frac{25h^4+30h^3+72h^2+72h+144}{E_5(h)},\quad
\frac{72h(h+2)}{E_5(h)},\quad
\frac{12h^2(5h+6)}{E_5(h)}.
\]
At distances \(0,1,2\), respectively, each is nonnegative for \(h\ge0\) and the diagonal is strictly positive. For \(C_3\) and \(C_4\), they are respectively a complete graph and a complete bipartite graph. In either case, their two nonzero spectral levels yield positive off-diagonal entries. More generally, for complete multipartite graphs the elementary spectral-projector formula \(f(hL)\) gives strictly positive off-diagonal entries for \(h>0\). This small-size baseline is not claimed to be new.

For \(C_6\), set
\[
D_6(h)=(h^2+6h+12)(3h^2+6h+4)(4h^2+6h+3).
\]
For circular distance \(d=0,1,2,3\), direct polynomial multiplication gives exactly the four entries
\[
\begin{aligned}
T_6(h)_{0,0}&=\frac{12h^6+44h^5+121h^4+168h^3+276h^2+288h+144}{D_6(h)},\\
T_6(h)_{0,1}&=-\frac{2h(5h^4-12h^3-102h^2-144h-72)}{D_6(h)},\\
T_6(h)_{0,2}&=\frac{2h^2(13h^3+48h^2+72h+36)}{D_6(h)},\\
T_6(h)_{0,3}&=\frac{2h^3(19h^2+48h+24)}{D_6(h)}.
\end{aligned}
\]
All denominators are positive for \(h\ge0\); the distance-0, 2 and 3 numerators are positive for \(h>0\). The quartic \(q(h)=5h^4-12h^3-102h^2-144h-72\) has exactly one positive root by Descartes' rule of signs (one sign change); \(q(6)<0<q(7)\). Thus the distance-1 value is nonnegative precisely on \(0\le h\le\rho\), and negative thereafter. Cyclic symmetry supplies all matrix entries, proving the exact six-cycle statement.

**3. Every longer cycle loses adjacent positivity.** On any connected undirected graph with Laplacian \(L\) and Moore–Penrose inverse \(L^+\), spectral expansion on the orthogonal complement of constants yields, entrywise,
\[
f(hL)=I-\frac{12}{h}L^++O(h^{-2})\qquad(h\to\infty).
\]
The identity follows because \(f(x)=1-12x/(x^2+6x+12)=1-12/x+O(x^{-2})\) for positive \(x\), while \(f(0)=1\). On a unit-resistance cycle, the effective resistance between vertices at circular distance \(d\) equals \(d(n-d)/n\). Writing \(R_{ij}\) for this resistance, the double-centering identity \(L^+=-\tfrac12 H R H\) with \(H=I-\mathbf1\mathbf1^\mathsf T/n\) shows
\[
(L_n^+)_{0,1}=\frac{n^2-1}{12n}-\frac{n-1}{2n}=\frac{(n-1)(n-5)}{12n}.
\]
Indeed the sum of the resistances from any fixed cycle vertex is \((n^2-1)/6\). For **every** \(n\ge6\), the displayed pseudoinverse entry is strictly positive. Thus
\[
(T_n(h))_{0,1}=-\frac{(n-1)(n-5)}{nh}+O(h^{-2})<0
\]
for all sufficiently large \(h\) (the implied threshold may depend on \(n\)). This completes the if-and-only-if cycle-size classification.

## Verification

The attached `artifacts/verify_cycle.py` (requiring SymPy) reconstructs the matrices from the exact rational functions, proves the \(C_5\) and \(C_6\) orbit identities symbolically, checks all \(36\) cyclic entries at six rational step values against a separate direct inversion, and checks the pseudoinverse formula on eleven sample sizes. It prints `PASS` when these tests succeed. The all-\(n\) statement is proved by the preceding effective-resistance identity and spectral expansion; **finite checks alone are not its proof**.

## Relationship to prior work

Horváth's 2004-online paper develops general RK positivity thresholds and invariant-cone guarantees. Zappavigna, Colaneri, Kirkland and Shorten (2012) exhibit positivity failure of diagonal Padé approximants on certain higher-dimensional positive systems, with sufficient conditions for preserving positivity. Horváth, Song and Terlaky (2014) study invariance of polyhedra under discretization. The published eight-state Markov obstruction concerns loss for **arbitrarily small steps**, whereas the present cycle classification concerns **large steps on symmetric unit-weight cycles**. Known complete-multipartite and strongly-regular-graph baseline results account for the always-positive short cycles; these are not claimed as new here. None of those inspected results states or implies the \(C_6\) cutoff polynomial together with the all-cycle size dichotomy.

## Limitations

For \(n\ge7\), only **eventual** negativity is proved, not the exact nonnegativity interval nor uniqueness of any zero. Statements concern equal-weight symmetric combinatorial cycles and the finished endpoint update, not general weighted cycles, nonsymmetric generators, nonlinear systems, floating-point roundoff, or intermediate RK stage positivity. The exact six-cycle result is analytic, but external independent validation has not been performed. Specialized older cyclic-diffusion literature may still contain related formulas.

## References

1. Z. Horváth, *On the positivity step size threshold of Runge–Kutta methods*, *Applied Numerical Mathematics* 53 (2005), 341–356, first available online 27 October 2004, DOI: 10.1016/j.apnum.2004.08.026.
2. A. Zappavigna, P. Colaneri, S. Kirkland and R. Shorten, *Essentially Negative News About Positive Systems*, *Linear Algebra and its Applications* 436 (2012), 3425–3442; authorized preprint: https://mural.maynoothuniversity.ie/id/eprint/3761/1/SK_Essentially_Negative.pdf.
3. Z. Horváth, Y. Song and T. Terlaky, *Steplength thresholds for invariance preserving of discretization methods of dynamical systems on a polyhedron*, arXiv:1406.6755 (2014), https://arxiv.org/abs/1406.6755.
4. *Eight-state barrier for Markov positivity of the [2/2] Padé map*, published research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-eight-state-pade-markov-positivity-barrier--4aad2a3f58ab.
