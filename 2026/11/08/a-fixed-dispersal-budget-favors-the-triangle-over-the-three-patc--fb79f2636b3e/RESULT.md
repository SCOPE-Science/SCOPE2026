# A fixed dispersal budget favors the triangle over the three-patch corridor at every exponential horizon

## Finding
Consider three habitat patches, all occupied initially, with independent local extinction clocks of rate one and recolonization clocks on undirected edges: an occupied endpoint recolonizes an empty endpoint at that edge's rate. Empty occupancy is absorbing. Compare the complete triangle with rate \(r\) on each of its three edges against the three-vertex path with rate \(3r/2\) on each of its two edges; the sum of undirected edge rates is \(3r\) in either system. Let \(\tau_\triangle\) and \(\tau_\mathrm{path}\) be times of global extinction.

For every \(r>0\) and \(s>0\), **the triangle strictly improves exponentially discounted persistence**:
\[
\mathbb E[e^{-s\tau_\mathrm{path}}]-\mathbb E[e^{-s\tau_\triangle}]
=\frac{3r^2s(15r^2+14rs+34r+3s^2+14s+7)}{2D_\triangle(s)D_\mathrm{path}(s)}>0.
\]
Here \(D_\triangle\) and \(D_\mathrm{path}\) are positive polynomials defined in the proof. Equivalently, for an independent exponential deadline \(E_s\) of rate \(s\), \(\Pr(\tau_\triangle>E_s)>\Pr(\tau_\mathrm{path}>E_s)\). The exact mean persistence advantage is
\[
\mathbb E\tau_\triangle-\mathbb E\tau_\mathrm{path}
=\frac{r^2(15r^2+34r+7)}{24(2r+1)(3r+2)}>0.
\]
As \(r\to\infty\), the ratio of mean extinction times tends to \(32/27\). At fixed \(r>0\), with \(S_G(t)=\Pr(\tau_G>t)\), the earliest nonzero short-time difference is
\[
S_\triangle(t)-S_\mathrm{path}(t)=\frac{3r^2}{80}t^5+O_r(t^6).
\]

## Assumptions and scope
There are exactly three patches, with symmetric edge transmission and unit extinction rate at each occupied patch. Every transition is an independent Poisson clock; a vacant patch's rate of recolonization is the sum of the rates of its occupied neighbors. There is no outside immigration. The two networks have equal total **undirected** edge-rate budget, not equal rate per edge. Both are initially fully occupied. The inequalities require \(r>0,s>0\). At \(r=0\), the two models coincide. Rescaling all clocks extends the formulas to any common local extinction rate \(\mu>0\) after replacing \(r\) by the dimensionless ratio \(r/\mu\) and scaling time by \(\mu\).

## Proof
For any transient subgenerator \(Q\), write \(\mathbf1\) for the all-ones vector and select the initial full-occupancy state by row vector \(e_F^\top\). First-step conditioning gives the Laplace transform \(L(s)=\mathbb E[e^{-s\tau}]=1-s e_F^\top(sI-Q)^{-1}\mathbf1\). For the triangle, symmetry reduces nonempty states to the number \(1,2,3\) of occupied sites; in that order the subgenerator is
\[
Q_\triangle=\begin{pmatrix}-1-2r&2r&0\\2&-2-2r&2r\\0&3&-3\end{pmatrix}.
\]
Its determinant and extinction transform are
\[
D_\triangle(s)=\det(sI-Q_\triangle)=s^3+(6+4r)s^2+(11+8r+4r^2)s+6,
\quad L_\triangle(s)=\frac6{D_\triangle(s)}.
\]
For the path put \(a=3r/2\). The five symmetry classes are: one occupied center, one occupied endpoint, a connected occupied pair, the two occupied endpoints with vacant center, and full occupancy. Their subgenerator is
\[
Q_\mathrm{path}=\begin{pmatrix}
-1-2a&0&2a&0&0\\
0&-1-a&a&0&0\\
1&1&-2-a&0&a\\
0&2&0&-2-2a&2a\\
0&0&2&1&-3
\end{pmatrix}.
\]
Set \(D_\mathrm{path}(s)=\det(sI-Q_\mathrm{path})\). Cramer's rule, or direct solution of the five first-step equations, yields
\[
L_\mathrm{path}(s)=\frac{6(2r+s+1)(3r+s+2)}{D_\mathrm{path}(s)}.
\]
The exact determinant identity
\[
D_\mathrm{path}(s)=(2r+s+1)(3r+s+2)D_\triangle(s)
-\frac{r^2s}{4}(15r^2+14rs+34r+3s^2+14s+7)
\]
then gives the displayed strict transform inequality. Both subgenerators are transient finite-state Markov generators, so \(sI-Q\) is a nonsingular \(M\)-matrix with positive determinant for \(s\ge0\); alternatively, their determinant polynomials have strictly positive coefficients for \(r>0\). Thus every displayed denominator is positive. For independent \(E_s\sim\operatorname{Exp}(s)\), \(\Pr(\tau>E_s)=1-L(s)\), proving the exponential-horizon interpretation. Taking the limit of \((L_\mathrm{path}(s)-L_\triangle(s))/s\) as \(s\downarrow0\) proves the mean difference.

More explicitly, \(\mathbb E\tau_\triangle=(4r^2+8r+11)/6\), whereas \(\mathbb E\tau_\mathrm{path}=(81r^4+270r^3+513r^2+372r+88)/(24(2r+1)(3r+2))\). Their leading terms are \(2r^2/3\) and \(9r^2/16\), proving the limit \(32/27\). Finally, \(S_G(t)=e_F^\top e^{tQ_G}\mathbf1\). Direct multiplication of the stated subgenerators shows identical coefficients through degree four, while \(e_F^\top(Q_\triangle^5\mathbf1-Q_\mathrm{path}^5\mathbf1)=9r^2/2\). Division by \(5!\) proves the short-time coefficient.

## Verification
Run `python verify.py` with SymPy installed according to `requirements.txt`. The checker independently constructs the full seven-state generators from transition rules, reconstructs both reduced generators, verifies the Cramer numerators, determinant identity, strictly positive numerator factorization, mean formula and fifth-order expansion symbolically; it also performs exact-rational full/reduced resolvent checks for twenty rate pairs and compares time-series derivatives. The packaged run passed 100 assertions. The proof above is algebraic for all positive real \(r,s\); the finite sample grid is a consistency check, not an infinite proof.

## Relationship to prior work
Gilarranz and Bascompte (2011 online) compare large discrete-generation ecological networks with the same *number* of edges, using regional abundance. Barbillon et al. (2014 preprint) develop exact finite-state discrete-time extinction-colonization methods and compare network classes at fixed generation horizons. Grilli, Barabás and Allesina (2015) connect continuous-time metapopulation models to SIS dynamics and study spectral persistence approximations on random landscapes. Mountford et al. (2012 preprint) prove asymptotic large-graph contact-process lifetime results. None of their inspected statements gives this fixed **sum of edge rates** three-patch comparison or its strict all-exponential-deadlines Laplace order. Standard contact-process attractiveness under *edgewise* increasing rates cannot compare these two budgets: two path rates are higher than corresponding triangle rates. The formula is a finite-model specialization not asserted to imply a general graph-topology theorem.

## Limitations
Strict Laplace-transform order **does not itself prove pointwise survival-probability order at every deterministic time**; this result claims only exponential random deadlines, discounted persistence scores, mean time, and the local series coefficient. The model omits spatial heterogeneity, rescue travel times, catastrophes and costs that vary by route. An independent mathematical or historical-priority audit has not been performed. Exact formulas may conceivably occur in older finite-state reliability treatments not found in the inspected literature.

## References
- L. J. Gilarranz and J. Bascompte, *Spatial network structure and metapopulation persistence*, Journal of Theoretical Biology 297 (2012), 11–16; publicly available online 2011-12-08. DOI: https://doi.org/10.1016/j.jtbi.2011.11.027
- T. Mountford, J.-C. Mourrat, D. Valesin and Q. Yao, *Exponential extinction time of the contact process on finite graphs*, arXiv:1203.2972, 2012-03-13. https://arxiv.org/abs/1203.2972
- P. Barbillon et al., *Network impact on persistence in a finite population dynamic diffusion model*, arXiv:1404.4287, 2014-04-16. https://arxiv.org/abs/1404.4287
- J. Grilli, G. Barabás and S. Allesina, *Metapopulation Persistence in Random Fragmented Landscapes*, PLOS Computational Biology 11 (2015), e1004251. https://doi.org/10.1371/journal.pcbi.1004251
