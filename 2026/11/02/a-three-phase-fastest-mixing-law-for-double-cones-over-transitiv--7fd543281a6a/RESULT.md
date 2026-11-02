# A three-phase fastest-mixing law for double cones over transitive graphs

## Finding
Let \(H\) be a connected, simple, undirected graph on \(n\ge3\) vertices, regular of degree \(d\ge1\), and both vertex- and edge-transitive. Form \(G=\overline{K_2}\vee H\): two nonadjacent apex vertices are joined to every vertex of \(H\), while the edges of \(H\) remain unchanged. Self-transition probabilities are allowed at every vertex. Among all real symmetric, entrywise nonnegative, row-stochastic transition matrices supported on \(G\) (off-diagonal nonzeros allowed only on its edges), minimize the second-largest eigenvalue modulus \(\mu(P)=\|P-\mathbf{1}\mathbf{1}^{T}/(n+2)\|_2\).

Write \(u=\lambda_2(L_H)>0\), \(v=\lambda_n(L_H)\), where \(L_H=dI-A_H\), and define
\[
q_* = \min\left\{\frac{2}{u+v},\frac1d\right\},\qquad
\kappa = \max\{|1-uq_*|,|1-vq_*|\}\in[0,1).
\]
Then a globally optimal transition matrix assigns probability \(a_*\) to **each** apex-to-base edge, and probability \(b_*=(1-2a_*)q_*\) to **each** base edge. The canonical apex probability \(a_*\) and global minimum \(\mu_*\) follow the complete three-phase law
\[
(a_*,\mu_*)=
\begin{cases}
\left(\dfrac1{n+1},\dfrac1{n+1}\right),
 &0\le\kappa\le\dfrac1{n-1},\\[4pt]
\left(\dfrac{1+\kappa}{n+2+2\kappa},\dfrac{n\kappa}{n+2+2\kappa}\right),
 &\dfrac1{n-1}<\kappa<\dfrac2{n-2},\\[4pt]
\left(\dfrac1n,\dfrac{n-2}{n}\kappa\right),
 &\kappa\ge\dfrac2{n-2}.
\end{cases}
\]
The last phase is empty when the threshold exceeds the permitted range \(\kappa<1\). At either phase boundary adjacent formulas agree. Within the two-edge-orbit symmetric family, the optimal apex probability is unique; no uniqueness assertion is made about base-edge probabilities or unrestricted asymmetric optimizers.

**Concrete complete classification.** If \(H=C_n\), set
\[
\kappa_n=\begin{cases}
\dfrac{1-\sin^2(\pi/n)}{1+\sin^2(\pi/n)},& n\text{ even},\\[4pt]
\dfrac{1-4\sin^2(\pi/(2n))}{1+4\sin^2(\pi/(2n))},& n\text{ odd}.
\end{cases}
\]
For the \(n\)-gonal bipyramid \(\overline{K_2}\vee C_n\), the exact optimal SLEM is \(1/4\) when \(n=3\), \(1/5\) when \(n=4\), \(5/(7\sqrt5+2)\) when \(n=5\), and \((1-2/n)\kappa_n\) for all \(n\ge6\). At \(n=5\), the apex probability is \((\sqrt5+1)/(7\sqrt5+2)\); at \(n\ge6\) it saturates \(1/n\). The \(n=3\) case was solved previously as \(K_5\) minus an edge; \(n=4\) belongs to the previously studied complete-tripartite family \(K_{2,2,2}\). These endpoints are included for completeness, not presented as independent new examples.

## Assumptions and scope
The optimization covers **all** symmetric stochastic matrices respecting the original edge support, not merely matrices assumed to be symmetric under graph automorphisms. Holding probabilities (diagonal entries) are free and nonnegative. Edges may have zero probability, although the constructed optimum has positive probabilities on every graph edge. There is no fixed total-conductance budget and no nonuniform stationary distribution. Regularity and vertex- and edge-transitivity of \(H\) ensure that averaging over graph automorphisms leaves exactly two off-diagonal edge classes.

## Proof
**1. Global symmetry reduction.** Let \(N=n+2\) and \(J=\mathbf1\mathbf1^T/N\). For a feasible matrix \(P\), \(\mu(P)=\|P-J\|_2\), a convex function of \(P\). Average \(P\) over the product of apex interchange with \(\operatorname{Aut}(H)\). The average is feasible and has no larger objective, since each conjugation fixes \(J\) and preserves the spectral norm. Vertex- and edge-transitivity reduce its off-diagonal entries to a common apex-base probability \(a\) and a common base-edge probability \(b\), satisfying exactly
\[
a\ge0,\quad b\ge0,\quad na\le1,\quad 2a+db\le1.
\]
Consequently, solving this two-variable family gives the unrestricted global optimum, without claiming that every unrestricted optimum must be symmetric.

**2. Complete invariant-subspace decomposition.** For such a matrix, the two apex diagonal entries equal \(1-na\), and each base diagonal entry equals \(1-2a-db\). The constant vector has eigenvalue \(1\). The antisymmetric apex vector has eigenvalue \(1-na\). The apex-versus-base contrast vector, with value \(n\) at both apexes and \(-2\) at every base vertex, has eigenvalue \(1-(n+2)a\). Finally, for every mean-zero base Laplacian eigenvector of eigenvalue \(\lambda\), its extension by zeros on the apexes has transition eigenvalue \(1-2a-b\lambda\). These mutually orthogonal subspaces exhaust \(\mathbb R^{n+2}\), giving the exact SLEM
\[
\mu(a,b)=\max\left\{|1-na|,\ |1-(n+2)a|,\ \max_{\lambda\in\operatorname{spec}(L_H)\setminus\{0\}}|1-2a-b\lambda|\right\}.
\]
In particular, the smaller base eigenspace and the larger base eigenspace, not only the radial eigenvalues, must be controlled.

**3. Solve the base-edge minimax without ignoring the holding constraint.** Since \(0\le a\le1/n\) and \(n\ge3\), set \(z=1-2a>0\). The base eigenvalue contribution is \(z\max_{\lambda}|1-(b/z)\lambda|\), and \(0\le b/z\le1/d\). Convexity of absolute value as a function of \(\lambda\) places the maximum at \(u\) or \(v\). The unconstrained equioscillating value is \(2/(u+v)\); imposing the base holding-probability constraint clips it at \(1/d\). This proves that \(b=zq_*\) minimizes the base contribution and that its exact minimum is \(z\kappa\). Positivity of \(u\) and the feasible positive choice of \(q_*\) ensure \(\kappa<1\). The holding constraint is genuinely active: for the triangular graph \(H=J(7,2)\), one has \(n=21\), \(d=10\), \(u=7\), and \(v=12\), so the unconstrained value \(2/19\) exceeds the permitted \(1/10\). The theorem correctly selects \(q_*=1/10\).

**4. Solve the apex minimax.** The remaining objective is
\[
f(a)=\max\left\{1-na,\ (n+2)a-1,\ \kappa(1-2a)\right\},\qquad 0\le a\le\frac1n.
\]
The first and third affine functions decrease, while the second increases. The two apex functions meet at \(a=1/(n+1)\), where both equal \(1/(n+1)\). Their intersection remains globally optimal exactly when \(\kappa(n-1)\le1\). Otherwise, the base and radial functions meet at \(a=(1+\kappa)/(n+2+2\kappa)\); this intersection is feasible precisely when \(\kappa(n-2)\le2\). Beyond that boundary both relevant decreasing functions are still descending at \(a=1/n\), so the apex row-sum boundary minimizes the maximum. Evaluating \(f\) in each case gives the stated law, including its equality endpoints. The decreasing/increasing intersections also establish uniqueness of \(a_*\) among symmetric optima.

**5. Cyclic backbones.** For \(C_n\), \(d=2\), \(u=4\sin^2(\pi/n)\) and \(v=4\sin^2(\pi\lfloor n/2\rfloor/n)\). Direct trigonometry gives \(u+v\ge4=2d\), so \(q_*=2/(u+v)\). The displayed expressions for \(\kappa_n\) follow. Exact evaluation gives \(\kappa_3=0\), \(\kappa_4=1/3\), and \(\kappa_5=1/\sqrt5\), putting these sizes in the first, first-boundary and intermediate phases. For every even \(n\ge6\), the inequality \(\kappa_n\ge2/(n-2)\) is equivalent to \(n-4\ge n\sin^2(\pi/n)\); for every odd \(n\ge7\), it is equivalent to \(n-4\ge4n\sin^2(\pi/(2n))\). Both follow from \(\sin t\le t\) and \(n(n-4)\ge12>\pi^2\) for \(n\ge6\). This proves the complete cycle classification, not merely numerical cases.

## Verification
The standalone `verify.py` reconstructs the transition matrices and checks their full eigenspectra against the invariant-subspace formula. On 43 examples (cycles, complete graphs, balanced complete bipartite graphs, hypercubes, the Petersen graph, triangular graphs and rook graphs), independent linear programs minimize the original four spectral endpoint constraints subject to both stochasticity constraints. The tests compare their attained values with the three-phase formulas. A deterministic selection of unrestricted asymmetric feasible matrices is checked against the proven optimum as a nonexhaustive diagnostic. Six examples also exercise the base holding-probability constraint, where the clipped rather than equioscillating base-edge optimizer is required. Exact rational matrix checks are provided for small cycles. Run `python verify.py` with Python 3, NumPy, SciPy, and SymPy available. The proof, not the finite checks, establishes the theorem for all permitted graphs.

## Relationship to prior work
Boyd, Diaconis, and Xiao (2004) developed the general convex/semidefinite fastest-mixing formulation. Their Table 1, graph (d), already contains the \(n=3\) bipyramid \(K_5\) with one missing edge and SLEM \(1/4\); this finite special case is **not claimed as new**. Boyd, Diaconis, Parrilo, and Xiao (2007 preprint; 2009 journal) proved symmetry reduction, edge-transitive formulas and an exact **single-hub wheel** formula in their Section 5.3.3. Their Section 5.3.2 also provides a spectral reduction for all complete multipartite graphs: it encompasses \(H=K_n\) and the \(n=4\) cyclic double cone \(K_{2,2,2}\), though not the cyclic family with \(n\ge5\). The present result concerns the different two-nonadjacent-hub join, whose antisymmetric apex mode introduces a second apex obstruction and a three-regime optimum. The earlier papers provide tools from which this theorem can be derived, but the inspected statements do not state or imply its all-backbone double-cone formulas without the additional spectral analysis and minimax argument given here.

For a cyclic backbone with \(n\ge6\), the cited single-wheel formula is \(\mu_{\mathrm{wheel}}=(1-1/n)\kappa_n\), whereas this double-cone result gives \(\mu_{\mathrm{double}}=(1-2/n)\kappa_n\). Hence the two-hub construction improves the optimum by exactly \(\kappa_n/n\), and its leading large-\(n\) mixing spectral gap is doubled. This comparison is an implication of the present formulas and the published wheel formula, not a claim of novelty for the single-wheel case.

## Limitations
The conclusion concerns discrete-time **symmetric** stochastic chains with uniform stationary distribution, free holding probabilities, and vertex- and edge-transitive connected regular backbones. It does not classify every asymmetric optimal transition matrix, nor determine whether all base-edge probabilities are unique when a different spectral mode is the active bottleneck. Graphs with only vertex-transitivity, nonuniform edge pricing, irreversible transition rules, or a prescribed nonuniform stationary measure require separate analysis. The proof is complete in its stated scope; specialized historical coverage outside the inspected primary papers remains possible. 
## References
- S. Boyd, P. Diaconis and L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689, DOI: 10.1137/S0036144503423264, https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf. See particularly Section 2 and Table 1, graph (d).
- S. Boyd, P. Diaconis, P. Parrilo and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955v1 (first posted 2007-09-06), https://arxiv.org/abs/0709.0955; SIAM Journal on Optimization 20 (2009), 792–819, DOI: 10.1137/070689413. See Sections 2, 3 and 5.3, especially the single-wheel calculation.
- S. Boyd, P. Diaconis, P. Parrilo and L. Xiao, *Symmetry Analysis of Reversible Markov Chains*, Internet Mathematics 2 (2005), 31–71, DOI: 10.1080/15427951.2005.10129100, https://web.stanford.edu/~boyd/papers/pdf/symmetry.pdf. This is background on orbit decompositions rather than the two-hub optimization law.
