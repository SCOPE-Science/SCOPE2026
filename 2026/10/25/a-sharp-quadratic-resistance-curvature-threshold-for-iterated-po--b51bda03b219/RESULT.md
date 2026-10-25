# A sharp quadratic resistance-curvature threshold for iterated polygon pyramids

## Finding

Let \(n\ge 3\) and \(r\ge 1\) be integers. Start with a convex \(n\)-gon and take \(r\) successive pyramids, obtaining a convex \((r+2)\)-polytope \(P_{n,r}\). Its one-skeleton is the graph join \(G_{n,r}=K_r\vee C_n\). Give **every graph edge unit conductance**, write \(R_{uv}\) for effective resistance, and define the node resistance curvature by
\[
\kappa(v)=1-\frac12\sum_{u\sim v}R_{uv}.
\]
The \(r\) apex vertices have the common value
\[
\kappa_A(n,r)=\frac{n+1}{2(n+r)}-\frac12\sum_{j=1}^{n-1}\frac1{r+2-2\cos(2\pi j/n)},
\]
while the \(n\) polygon vertices have the common value
\[
\kappa_C(n,r)=\frac{1-r\kappa_A(n,r)}n\ge\frac1{n+r}>0.
\]
The graph has strictly positive resistance curvature at **every** vertex if and only if
\[
\boxed{\;2r\ge n(n-3)-2.\;}
\]
The apex curvature is never zero for the stated integer parameters. For \(n\ge5\), the least number of successive pyramids needed to achieve everywhere-strict positivity is therefore exactly \((n(n-3)-2)/2\). Equivalently, for fixed \(r\ge1\), the greatest admissible polygon size is
\[
\boxed{\left\lfloor\frac{3+\sqrt{17+8r}}2\right\rfloor.}
\]
The threshold is asymptotic to \(n^2/2\) as \(n\to\infty\).

## Assumptions and scope

All resistances refer to the **unweighted** simple one-skeleton, so all edge conductances are precisely one; Euclidean lengths of polytope edges play no role. The polygon may have any convex realization. The join notation denotes the graph-theoretic operation, not a Cartesian graph product. The distinction between strict curvature positivity for these fixed conductances and existence of *some* positive conductance assignment is essential: the latter is a different invariant.

## Proof

Put \(N=n+r\) and \(\lambda_j=2-2\cos(2\pi j/n)\) for \(1\le j<n\). The cycle Laplacian has nonzero eigenvalues \(\lambda_j\), all in \((0,4]\). The graph-join Laplacian decomposes orthogonally into an \((r)\)-dimensional eigenspace of eigenvalue \(N\), the constant eigenspace of eigenvalue zero, and the nonconstant rim Fourier eigenspaces, with eigenvalues \(r+\lambda_j\). An apex-to-rim difference of unit basis vectors has squared projection \((n+1)/n\) onto the \(N\)-eigenspace, and squared projection \(1/n\) onto each nonconstant Fourier eigenspace. Hence
\[
R_{A,C}=\frac{n+1}{nN}+\frac1n\sum_{j=1}^{n-1}\frac1{r+\lambda_j}.
\]
The resistance between two distinct apexes is \(R_{A,A}=2/N\). Inserting these values into the definition of curvature gives the stated exact \(\kappa_A\) formula.

Foster's identity \(\sum_{\{u,v\}\in E(G)}R_{uv}=N-1\) implies \(\sum_{v\in V(G)}\kappa(v)=1\), so by the two vertex orbits \(r\kappa_A+n\kappa_C=1\). For \(n\ge4\), every \(\lambda_j\le4\le n\), whence \(\sum_{j=1}^{n-1}(r+\lambda_j)^{-1}\ge(n-1)/N\). It follows that \(\kappa_A\le1/N\) and therefore \(\kappa_C\ge1/N\). When \(n=3\), the whole graph is \(K_N\) and both curvatures equal \(1/N\).

To determine the sign of the apex curvature, assume \(n\ge4\) and set
\[
F_n(r)=\sum_{j=1}^{n-1}\frac{n-\lambda_j}{r+\lambda_j},\qquad B=n(n-3).
\]
The exact identity \(2N\kappa_A=2-F_n(r)\) follows by writing \(N/(r+\lambda_j)=1+(n-\lambda_j)/(r+\lambda_j)\). All weights \(w_j=n-\lambda_j\) are nonnegative. The cycle trace identities \(\sum_j\lambda_j=2n\) and \(\sum_j\lambda_j^2=6n\) give
\[
\sum_jw_j=B,\qquad\sum_jw_j\lambda_j=2B.
\]
Thus the \(w_j\)-weighted mean of the \(\lambda_j\)'s is exactly two.

For \(n=4\), the only positive-weight Fourier modes have eigenvalue two, so \(F_4(r)=4/(r+2)<2\) for all integers \(r\ge1\). For \(n\ge5\), put \(r_0=B/2-2\) and \(r_1=B/2-1=r_0+1\). These are integers with \(r_0\ge3\) and \(r_1\ge4\). Strict Jensen convexity of \(x\mapsto1/(r_0+x)\), applied with the weights \(w_j\), yields
\[
F_n(r_0)>\frac{B}{r_0+2}=2.
\]
For every \(x\in[0,4]\), convexity also gives the chord bound
\[
\frac1{r+x}\le\frac{1-x/4}{r}+\frac{x/4}{r+4}.
\]
Using the weighted mean two at \(r=r_1\) gives
\[
F_n(r_1)\le\frac B2\left(\frac1{r_1}+\frac1{r_1+4}\right)
=\frac{2(r_1+1)(r_1+2)}{r_1(r_1+4)}<2,
\]
where the final inequality is exactly \(r_1>2\). Since \(F_n(r)\) strictly decreases with positive \(r\), every integer \(r\le r_0\) gives \(\kappa_A<0\), and every integer \(r\ge r_1\) gives \(\kappa_A>0\). No integer is a zero, and the claimed threshold follows, including the \(n=3,4\) cases.

## Verification

The standalone `verify.py` implements two **independent exact** finite checks. It reconstructs full grounded graph-Laplacian inverses and their edge resistances for \(99\) parameter pairs, verifying both vertex orbits. Separately, it evaluates the Fourier sum by the exact cycle characteristic polynomial
\[
D_n(x)=\frac{2\bigl(T_n(1+x/2)-1\bigr)}x,
\quad\sum_{j=1}^{n-1}\frac1{x+\lambda_j}=\frac{D_n'(x)}{D_n(x)},
\]
and checks the sign threshold at \(446\) additional exact parameter settings. Run `python verify.py` with Python 3 and SymPy. These checks are finite corroboration; the proof of all-parameter validity is the analytical spectral and two-moment argument above.

## Relationship to prior work

De Loera, Eddy, Robertson, and Samper define unweighted resistance curvature for polytopal graphs and study general positivity and obstructions. Their 2025 study discusses ordinary polygon pyramids as natural nonpositive examples, but its statements do not give an exact all-dimensional repair threshold under iterated pyramiding. Earlier join-graph resistance formulas, especially Sedlák and Slavík's general join theorem, imply the electrical identities used here after specialization; those identities are **not** claimed to be novel. The contribution here is the exact **integer quadratic phase boundary** with strict signs and rim-positivity, proved by a two-moment convexity comparison. Devriendt's weighted-existence notion of resistance-positive graphs does not answer fixed-unit-conductance sign questions; the iterated-pyramid graphs in fact admit Hamiltonian cycles and positive weights regardless of this threshold.

## Limitations

This theorem concerns only polygon-based iterated pyramids and fixed unit conductances. It does not classify arbitrary polytope graphs, arbitrary base polytopes, or optimally chosen edge weights. The evidence supports a mathematical originality claim for the exact integer threshold, not comprehensive historical priority. General resistance formulas already cover the intermediate pairwise effective-resistance identities.

## References

- J. A. De Loera, J. Eddy, S. J. Robertson, and J. A. Samper, *Discrete Curvatures and Convex Polytopes*, arXiv:2510.11894v1 (13 October 2025), especially Definition 1.5 and Sections 1.3 and 3; https://arxiv.org/pdf/2510.11894.
- J. Sedlák and A. Slavík, *Resistance distances and Kirchhoff indices in graph joins*, Journal of Physics A 58 (2025), 505203, DOI:10.1088/1751-8121/ae2997, especially Theorem 2.3; https://doi.org/10.1088/1751-8121/ae2997.
- K. Devriendt, *Graphs with Nonnegative Resistance Curvature*, Annals of Combinatorics, first published 6 August 2025, DOI:10.1007/s00026-025-00774-x, especially Sections 1 and 3; https://link.springer.com/article/10.1007/s00026-025-00774-x.
- M. Guo, W. Sun, and Y. Yang, *Resistance Curvature: Recognition, Polyhedral Structure, and Graph Products*, arXiv:2608.20778v1 (21 August 2026), especially Section 4; https://arxiv.org/pdf/2608.20778.
