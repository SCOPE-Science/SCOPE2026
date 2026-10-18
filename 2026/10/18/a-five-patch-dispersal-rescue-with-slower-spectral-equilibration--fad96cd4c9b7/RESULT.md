# A five-patch dispersal rescue with slower spectral equilibration

## Finding
For any finite connected simple undirected graph \(J\) of maximum degree at most three, define the dispersal-survival matrix
\[
C_q(J)=\frac{qI+A_J}{4},\qquad 0\le q\le\frac12,
\]
where \(A_J\) is the zero-diagonal adjacency matrix. All column sums are at most \(7/8\), so these entries are consistent with fractions of offspring surviving and arriving in patches. Let \(M_{F,q}(J)=F C_q(J)\), with fecundity \(F>0\). For a primitive nonnegative matrix \(M\), define its damping ratio as its Perron eigenvalue divided by the greatest modulus among its other eigenvalues.

On vertices \(\{1,2,3,4,5\}\), take
\[
E(G)=\{12,13,23,15,34\},\qquad E(H)=E(G)\cup\{45\}.
\]
Both graphs are connected and already contain a triangle before the added link. Let
\[
\alpha=\frac{1+\sqrt{13}}2,\quad
\varphi=\frac{1+\sqrt5}2,
\]
and let \(\beta\) be the unique root of \(t^3-2t^2-2t+2\) in \((12/5,5/2)\). Then \(\beta>\alpha\), and, **for every** \(q\in[0,1/2]\),
\[
\rho(C_q(H))>\rho(C_q(G)),\qquad
\mathcal D(C_q(H))=\frac{\beta+q}{2-q}
<\frac{\alpha+q}{\varphi-q}=\mathcal D(C_q(G)).
\]
Thus a new dispersal link increases the dominant growth multiplier while **decreasing** the damping ratio, the conventional spectral measure of relative convergence to the dominant patch composition. For each such \(q\), every fecundity in the nonempty interval
\[
\frac4{\beta+q}<F<\frac4{\alpha+q}
\]
changes the linear population from subcritical to supercritical. In particular, at \(q=1/2\), \(F=7/5\), one has
\[
\rho(M_{F,q}(G))=\frac{7(2+\sqrt{13})}{40}<1
<\frac{7(2\beta+1)}{40}=\rho(M_{F,q}(H)),
\]
while \(\mathcal D(G)>2>\mathcal D(H)\).

**Sharp graph order within the already-cycling class:** For the same \(C_q\), every single-edge addition to any connected nonbipartite simple graph on at most four vertices strictly increases the damping ratio, for all \(q\in[0,1/2]\). Hence five is the smallest number of patches for which a network that already contains an odd cycle can exhibit the displayed growth–damping tradeoff.

## Assumptions and scope
The model is the deterministic, density-independent update \(x_{t+1}=M_{F,q}(J)x_t\) for nonnegative patch abundances \(x_t\). Local fecundity and the existing dispersal entries are unchanged by adding the new link; previously lost emigrants may instead reach another patch. An undirected edge corresponds to equal transfer fractions in the two directions. Only simple graphs, a common diagonal-to-edge transfer ratio \(0\le q\le1/2\), and the specified equal patch parameters are claimed. The matrix is primitive for the exhibited graphs because each contains a triangle; for \(q=0\) the triangle still supplies aperiodicity.

## Proof
**1. Spectral reduction and physical normalization.** The eigenvalues of \(M_{F,q}(J)\) are \(F/4\) times those of \(qI+A_J\). Consequently \(F\) and the denominator four cancel from the damping ratio. In each exhibited graph every vertex has degree at most three. An outgoing column of \(C_q\) sums to \((q+\deg(v))/4\le7/8\), hence there is no required creation of dispersers during transport.

**2. Exact five-patch characteristic polynomials.** Direct determinant expansion gives
\[
\det(tI-A_G)=t(t^2-t-3)(t^2+t-1),
\]
\[
\det(tI-A_H)=t(t+2)(t^3-2t^2-2t+2).
\]
The largest eigenvalue of \(A_G\) is \(\alpha\). Its subdominant modulus after shifting by \(q\in[0,1/2]\) is \(\varphi-q\). The remaining eigenvalues have smaller modulus on this interval; the competing positive eigenvalue \((\sqrt5-1)/2\) ties exactly at \(q=1/2\). The cubic for \(H\) has precisely one root in each of \((-3/2,-1)\), \((0,1)\) and \((12/5,5/2)\), as its endpoint signs alternate. Thus the Perron eigenvalue is \(\beta\), and the subdominant shifted modulus is always \(2-q\), supplied by the eigenvalue \(-2\). This proves the two damping-ratio formulas.

**3. Strict damping reversal for the entire parameter interval.** Both denominators are positive. Their cross-multiplied difference is
\[
(\alpha+q)(2-q)-(\beta+q)(\varphi-q)
=2\alpha-\beta\varphi+q(2-\alpha-\varphi+\beta).
\]
The elementary radical and polynomial-root bounds
\[
\frac{23}{10}<\alpha<\frac{47}{20},\quad
\frac32<\varphi<\frac{13}{8},\quad
\frac{12}{5}<\beta<\frac52
\]
show that the constant coefficient is greater than \(43/80\) and the coefficient of \(q\) is greater than \(17/40\). Therefore the displayed difference is strictly positive for every \(q\ge0\) in the specified range.

**4. Dominant-growth threshold.** Since \(\beta>12/5>\alpha\), the indicated open interval for \(F\) is nonempty, and multiplying the two Perron eigenvalues by \(F/4\) places one strictly below and the other strictly above one. At \(q=1/2\), \(F=7/5\), the first inequality follows from \(13<(26/7)^2\), whereas the second follows from \(\beta>12/5\), giving \(7(\beta+1/2)/20>203/200>1\). Positive initial abundance vectors consequently decay for \(G\) and grow asymptotically for \(H\), by Perron–Frobenius theory.

**5. Sharpness for fewer already-cycling patches.** A connected nonbipartite simple graph on at most four vertices contains a triangle. At order three it is complete, so no edge can be added. At order four it must be, successively by edge count, a triangle with one pendant vertex (the paw), a diamond, or the complete graph. Any single-edge addition advances from paw to diamond or diamond to complete graph.

The paw adjacency polynomial is \((t+1)(t^3-t^2-3t+1)\). Its cubic roots lie, respectively, in \((-149/100,-147/100)\), \((31/100,32/100)\), and \((217/100,218/100)\). Write the extreme positive and negative roots as \(u\) and \(w\). Throughout \(0\le q\le1/2\), the paw damping ratio is \((u+q)/(-w-q)\). The diamond has eigenvalues \((1+\sqrt{17})/2\), \((1-\sqrt{17})/2\), \(-1\), and \(0\), and damping ratio
\[
\frac{(1+\sqrt{17})/2+q}{(\sqrt{17}-1)/2-q}.
\]
At \(q=0\), the paw's ratio is less than \(218/147\), while the diamond's exceeds \(25/16\). At \(q=1/2\), the paw's ratio is below \(268/97\), while the diamond's exceeds \(31/11\). In both cases the latter is larger. After multiplying the positive denominators, the comparison is affine in \(q\), so strictness at these two endpoints establishes strictness throughout the interval. Similarly, the diamond's ratio is less than \(3\) at each endpoint, while the complete graph's ratio \((3+q)/(1-q)\) equals \(3\) and \(7\) there. The same affine-cross-product argument proves strict increase from diamond to complete graph for the entire interval. This exhausts all smaller eligible graphs.

## Verification
The standalone standard-library program `verify.py` independently constructs both five-vertex adjacency matrices, evaluates their exact characteristic polynomials using Newton identities, checks rational root-isolation signs, and tests all required strict arithmetic bounds. It exhaustively generates every labeled graph with at most four vertices and verifies the connected nonbipartite graph classification and the characteristic polynomial before and after every possible edge addition. Run with `python3 verify.py` from the directory containing this document. This finite enumeration only checks the small-order sharpness classification; the continuum of parameters is proved algebraically above.

## Relationship to prior work
Shima, Noonburg and Phillips (2010) proposed the damping ratio of a dispersal connectivity matrix as a landscape-connectivity indicator. Artzy-Randrup and Stone (2010) demonstrated the structural importance of directed cycles and adjacency spectral radius for metapopulation invasion. Stott and colleagues (2011) explain precisely what damping ratios measure and why they do not determine every finite-time transient. These ingredients motivate comparing dominant growth against relative equilibration. The present result supplies a specific physically substochastic five-patch pair, an open fecundity interval, a whole self-recruitment interval, and a proof of sharp minimal patch count among already nonbipartite networks. Related graph-synchronization studies concern Laplacian eigenvalues, not the adjacency-based population matrix used here.

## Limitations
This is a linear deterministic invasion/decline statement, not a theorem of stochastic survival or nonlinear population regulation. A smaller damping ratio means slower **asymptotic relative spectral convergence** in modes with nonzero subdominant amplitude, not necessarily slower observed equilibration after every initial condition or at every finite time. The five-patch example is not asserted to be the only minimizer, nor are high-degree graphs or arbitrary transport probabilities classified. A bibliographic uncertainty remains because the full Shima–Noonburg–Phillips (2010) article could not be examined; its accessible abstract does not settle the exact overlap question.

## References
- Shima, J. S., Noonburg, E. G., and Phillips, N. E. (2010), “Life history and matrix heterogeneity interact to shape metapopulation connectivity in spatially structured environments,” *Ecology* 91, 1215–1224. DOI: 10.1890/08-2058.1. First online: 2010-04-01.
- Artzy-Randrup, Y., and Stone, L. (2010), “Connectivity, cycles, and persistence thresholds in metapopulation networks,” *PLoS Computational Biology* 6, e1000876. DOI: 10.1371/journal.pcbi.1000876.
- Stott, I., Townley, S., Carslake, D., and Hodgson, D. J. (2011), “A framework for studying transient dynamics of population projection matrix models,” *Ecology Letters*. DOI: 10.1111/j.1461-0248.2011.01659.x.
- Atay, F. M., and Bıyıkoğlu, T. (2005), “Graph operations and synchronization of complex networks,” *Physical Review E* 72, 016217. DOI: 10.1103/PhysRevE.72.016217.
