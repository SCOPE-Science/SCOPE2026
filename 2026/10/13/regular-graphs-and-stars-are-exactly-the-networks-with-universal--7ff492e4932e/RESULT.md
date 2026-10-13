# Regular graphs and stars are exactly the networks with universal Moran–Geary ranking agreement

## Finding

**Theorem.** Let \(G=(V,E)\) be a finite, connected, undirected, simple, unweighted graph with \(n=|V|\ge2\) and \(m=|E|\). For every nonconstant real node-attribute vector \(x\), define the usual **globally normalized** Moran and Geary statistics \(I_G(x)\) and \(C_G(x)\) as below. Then the implication
\[
I_G(x)>I_G(y)\ \Longrightarrow\ C_G(x)\le C_G(y)
\]
holds for **every** pair of nonconstant *strictly positive* node-attribute vectors \(x,y\) if and only if \(G\) is regular or a star \(K_{1,n-1}\). On a regular graph the exact relation is \(C_G=(n-1)(1-I_G)/n\); on a star it is \(C_G=1/2-(n-1)I_G/2\).

For every other connected simple graph, there exist strictly positive node-attribute vectors \(x,y\) with the **same arithmetic mean and the same variance**, yet \(I_G(x)>I_G(y)\) and \(C_G(x)>C_G(y)\). Four vertices is the smallest order permitting this strict discordance. On the four-vertex path in vertex order, the explicit vectors
\[
x=(1,1,4,2),\qquad y=(1,2,1,4)
\]
have the same sum \(8\) and sum of squares \(22\), but
\[
(I_G(x),C_G(x))=(-2/9,13/12),\qquad
(I_G(y),C_G(y))=(-4/9,11/12).
\]
The theorem compares all real-valued node profiles; it makes no analogous assertion about only binary-valued profiles.

## Assumptions and scope

Let \(A\) denote the symmetric zero-diagonal adjacency matrix, \(D=\operatorname{diag}(d_1,\ldots,d_n)\) its degree matrix, \(L=D-A\) its combinatorial Laplacian, \(\mathbf{1}\) the all-ones vector, and \(P=I_n-\mathbf{1}\mathbf{1}^{\mathsf T}/n\) the orthogonal projector onto \(\mathbf{1}^{\perp}\). For a nonconstant attribute vector \(x\), let \(z=Px\ne0\). We use the explicit definitions
\[
I_G(x)=\frac{n}{2m}\frac{z^{\mathsf T}Az}{z^{\mathsf T}z},\qquad
C_G(x)=\frac{n-1}{2m}\frac{z^{\mathsf T}Lz}{z^{\mathsf T}z}.
\]
Thus every edge is counted once in \(z^{\mathsf T}Lz=\sum_{\{u,v\}\in E}(x_u-x_v)^2\). The weight matrix is raw symmetric binary adjacency, **not** row-normalized. Larger Moran \(I\) and smaller Geary \(C\) conventionally represent stronger positive spatial autocorrelation. The defined strict discordance is larger values of **both** indices on one profile than the other.

## Proof

**1. An order lemma for quadratic Rayleigh quotients.** On a finite-dimensional real inner-product space \(H\), let \(F\) and \(K\) be symmetric linear operators, with Rayleigh quotients \(f(u)=\langle u,Fu\rangle\) and \(k(u)=\langle u,Ku\rangle\) for unit \(u\). Assume \(F\) is not scalar and that no unit vectors \(u,v\) satisfy both \(f(u)>f(v)\) and \(k(u)>k(v)\). Then \(K=\alpha I+\beta F\), with \(\beta\le0\).

First, \(k\) must be constant on each level set of \(f\). Indeed, if \(f(u)=f(v)=t\) but \(k(u)>k(v)\), and \(t\) is less than the maximum eigenvalue of \(F\), perturb \(u\) slightly towards an eigenvector with larger eigenvalue, preserving \(k(u')>k(v)\) while obtaining \(f(u')>t=f(v)\). Such an upward perturbation always exists for a nonmaximal level of a quadratic Rayleigh quotient: if \(u\) is not stationary this follows to first order; if stationary at a nonmaximal eigenvalue, add a small component in a higher eigenspace. If \(t\) is the maximum, perturb \(v\) towards a lower eigenspace, obtaining \(f(u)>f(v')\) while \(k(u)>k(v')\). Both cases contradict the hypothesis.

Diagonalize \(F\) with orthonormal eigenbasis \(e_i\). Since \(f((e_i+e_j)/\sqrt2)=f((e_i-e_j)/\sqrt2)\), constancy of \(k\) at equal \(f\)-values forces all off-diagonal entries \(\langle e_i,Ke_j\rangle\) to vanish. Within any eigenspace of \(F\), the value of \(k\) is constant on its unit sphere, so \(K\) has a scalar value \(\mu_i\) for each distinct eigenvalue \(\lambda_i\) of \(F\). A unit vector mixing two eigenspaces realizes any convex combination of their \(\lambda\)-values and the matching convex combination of their \(\mu\)-values. If there are three or more distinct eigenvalues, comparison of each interior eigenvalue with a mixture of the extreme ones makes all points \((\lambda_i,\mu_i)\) collinear. For two eigenvalues collinearity is automatic. Thus \(K=\alpha I+\beta F\); the forbidden-order condition requires \(\beta\le0\).

**2. Reduction to centered matrices.** Apply the lemma to \(F=PA P\) and \(K=PLP\), restricted to the centered subspace \(H=\mathbf{1}^{\perp}\). Positive scaling in the definitions of Moran and Geary preserves the compared order. Any two unit centered vectors can be shifted by the same sufficiently large positive constant to produce strictly positive attribute vectors; they automatically have a common mean and common variance. Thus the universal ranking implication for positive attributes applies exactly to all unit vectors in \(H\).

If \(F\) is scalar on \(H\), write \(PAP=\lambda P\). Taking the centered difference vector \(e_i-e_j\) gives \(-2A_{ij}=2\lambda\) for all distinct indices. Hence every off-diagonal adjacency entry is the same. Connectedness forces \(G\) to be complete, so it is regular.

Otherwise the order lemma implies \(PLP=\alpha P+\beta PAP\) on all of \(\mathbb R^n\). Using \(L=D-A\), we obtain
\[
PDP=\alpha P+\gamma PAP,\qquad \gamma=\beta+1.
\]
Consequently the symmetric matrix \(B=D-\alpha I_n-\gamma A\) has \(PBP=0\). The elementary orthogonal block decomposition \(\mathbb R^n=\operatorname{span}(\mathbf1)\oplus\mathbf1^\perp\) shows that every such symmetric matrix has the form \(B=\mathbf1v^{\mathsf T}+v\mathbf1^{\mathsf T}\) for some \(v\). Comparing diagonal entries gives \(v_i=(d_i-\alpha)/2\). Comparing off-diagonal entries therefore yields, for all \(i\ne j\),
\[
d_i+d_j-2\alpha=-2\gamma A_{ij}.
\]
In particular, the degree sum of the endpoints of every edge is a single constant; the degree sum over every nonedge is also a single constant.

**3. Classifying graph structure.** If a connected graph has constant degree sum \(s\) along each edge, following any path shows vertex degrees alternate between \(d\) and \(s-d\). An odd cycle enforces \(d=s/2\) throughout the connected graph, making it regular. In the bipartite case, connectedness makes all vertices in one bipartition degree \(a\), and all in the other degree \(b\). If \(a=b\) the graph is regular. If \(a\ne b\), both bipartition classes cannot contain at least two vertices: within-class nonedges would then have distinct degree sums \(2a\) and \(2b\), contradicting the nonedge condition just proved. Hence one bipartition has one vertex; connectedness makes the graph a star. This proves necessity.

For sufficiency, a \(d\)-regular graph satisfies \(L=dI_n-A\) and \(2m=nd\). Direct substitution gives
\[
C_G(x)=\frac{n-1}{n}\bigl(1-I_G(x)\bigr)
\]
for every nonconstant \(x\). On a star, a direct centered quadratic-form identity is \(PDP=P+(1-n/2)PAP\), as follows by substituting its degree sequence (one degree \(n-1\), all others degree \(1\)) into the off-diagonal identity above, or by expanding its quadratic forms. Therefore \(PLP=P-(n/2)PAP\) and, since \(m=n-1\),
\[
C_G(x)=\frac12-\frac{n-1}{2}I_G(x).
\]
Both affine slopes are negative; the universal ranking implication follows.

**4. Strict witnesses and minimality.** If a connected graph is neither regular nor a star, necessity shows that universal antitonicity fails. Hence the order lemma supplies unit centered vectors with both strict inequalities. Adding a sufficiently large common constant yields positive vectors with equal means and equal variances while preserving both Rayleigh quotients. At orders \(2\) and \(3\), every connected simple graph is regular or a star. At order \(4\), the path is neither, and the integer vectors in the finding supply the indicated exact strict reversal. This establishes minimality and completes the proof.

## Verification

The companion standard-library program `verify_moran_geary.py` independently evaluates the defining statistics with exact rational arithmetic, verifies the displayed four-vertex witness including its equal sums and equal squared norms, exhaustively enumerates every **labeled connected** simple graph of orders \(2\) through \(6\), and checks a separate exact centered-quadratic-form criterion against regular-or-star recognition. It additionally checks the two claimed affine identities on star and cycle graphs for orders \(3\) through \(9\). The executed output was:

`VERIFY_OK witness_P4=2 equal_mean_variance=1 connected_graph_census=[(2, 1, 1), (3, 4, 4), (4, 38, 8), (5, 728, 18), (6, 26704, 152)] star_cycle_identities=14`

The finite census and sample identities corroborate, but do **not** establish, the all-orders theorem; its proof is the quadratic-form and degree-sum argument above. Reproduce with `python3 verify_moran_geary.py`.

## Relationship to prior work

Moran (1950) and Geary (1954) introduced the respective spatial autocorrelation statistics. De Jong, Sprenger, and van Veen (1984) gave a spectral treatment of their extreme values over centered profiles. Luo, Griffith, and Wu (2017, Section 2, equation (4)) explicitly expressed Geary's statistic as a degree-weighted quadratic ratio minus a multiple of Moran's statistic; that foundational identity is **prior work**, not claimed here as a discovery. Bavaud (2024) showed that balanced or weight-compatible spatial weights make related normalized formulations equivalent. This does not settle the universal ranking question for raw unweighted adjacency with uniform node weights: such weights need not be balanced, and stars are a nonregular exceptional family.

The theorem instead characterizes **all connected simple graph topologies** on which the two raw-adjacency statistics order **every pair of real attribute profiles** oppositely, including a nonregular class; it also gives a smallest strict real-valued counterexample. Related finite classifications restricted to binary attributes do not imply an equivalence for every real-valued field. The inspected sources did not exhibit the stated graph classification, but this literature comparison does not certify global priority.

## Limitations

The theorem concerns deterministic point estimates of classical, globally normalized Moran and Geary statistics on connected, simple, undirected, unweighted graphs; it does not cover row-standardized spatial weights, directed graphs, unequal observation weights, permutation test significance, uncertainty, or empirically estimated networks. The strict counterexample needs real-valued attributes (not a binary-attribute threshold); no claim about binary realizations on a four-vertex path is made. A previously published stronger characterization in broader matrix or autocorrelation literature remains an originality risk.

## References

1. Moran, P. A. P. (1950). “Notes on Continuous Stochastic Phenomena.” *Biometrika* 37, 17–23. DOI: 10.1093/biomet/37.1-2.17.
2. Geary, R. C. (1954). “The Contiguity Ratio and Statistical Mapping.” *The Incorporated Statistician* 5, 115–146. DOI: 10.2307/2986645.
3. de Jong, P., Sprenger, C., and van Veen, F. (1984). “On Extreme Values of Moran's I and Geary's c.” *Geographical Analysis* 16, 17–24. DOI: 10.1111/j.1538-4632.1984.tb00797.x.
4. Luo, Q., Griffith, D. A., and Wu, H. (2017). “The Moran Coefficient and the Geary Ratio: Some Mathematical and Numerical Comparisons.” In *Spatial Data Handling in Big Data Era*, 279–294. DOI: 10.1007/978-3-319-22786-3_23.
5. Bavaud, F. (2024). “Measuring and Testing Multivariate Spatial Autocorrelation in a Weighted Setting: A Kernel Approach.” *Geographical Analysis*. DOI: 10.1111/gean.12390.
6. Yamada, H. (2023). “Geary's c and Spectral Graph Theory: A Complement.” *Mathematics* 11, 4228. DOI: 10.3390/math11204228.
