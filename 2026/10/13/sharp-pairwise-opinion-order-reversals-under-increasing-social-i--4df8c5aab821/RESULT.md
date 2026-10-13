# Sharp pairwise opinion-order reversals under increasing social influence

## Finding

In the symmetric, fixed-intrinsic-opinion social-influence equilibrium, there is a sharp finite ceiling on how often a specified pair's **opinion ordering** can change as the common strength of social influence grows. The ceiling is \(n-2\) for a connected network with \(n\ge2\) agents. Every value up to this ceiling is attainable, and the full ceiling can be attained at any prescribed positive influence-strength values on the simple unweighted path \(P_n\). This takes place even though aggregate opinion variance decreases strictly with influence strength whenever the intrinsic opinions are nonconstant.

Precisely, let \(G\) be an undirected connected weighted graph with \(n\ge2\) vertices and positive symmetric edge weights, \(L\) its weighted combinatorial Laplacian, and \(s\in[0,1]^n\) its fixed intrinsic-opinion vector. Set
\[
z(t)=(I+tL)^{-1}s,\qquad t>0.
\]
For two distinct vertices \(u,v\), if \(z_u(t)-z_v(t)\) is not identically zero, then it changes strict sign at most \(n-2\) times on \((0,\infty)\). For every \(n\ge3\) and every \(0<\eta_1<\cdots<\eta_{n-2}\), there is an intrinsic-opinion vector in \((0,1)^n\) on the unweighted path with \(u=1,v=2\) such that the changes occur exactly at \(t=\eta_1,\ldots,\eta_{n-2}\), all simple.

Also, writing \(\bar s=n^{-1}\sum_i s_i\), the aggregate squared deviation
\[
V(t)=\sum_{i=1}^n (z_i(t)-\bar s)^2
\]
is strictly decreasing for nonconstant \(s\). A change of signed pairwise ordering is therefore **not** evidence of an increase in aggregate squared variation.

## Assumptions and scope

The graph is fixed, finite, connected, undirected, with symmetric positive edge weights. A single nonnegative scalar \(t\) multiplies **all** edge weights. Each individual retains its fixed intrinsic opinion in \([0,1]\). The equilibrium solves \(z_i=(s_i+t\sum_j w_{ij}z_j)/(1+t\sum_jw_{ij})\), or equivalently \((I+tL)z=s\). The parameter \(t\) indexes distinct equilibria, **not** elapsed time. A *strict sign reversal* means that the continuous difference is positive immediately on one side of a value and negative immediately on the other. Tangencies and identically equal opinions are not counted.

## Proof

**Universal bound.** Because \(L\) is real symmetric and \(G\) connected, its distinct eigenvalues consist of the simple eigenvalue \(0\) and \(m\le n-1\) distinct positive eigenvalues \(\lambda_1,\ldots,\lambda_m\). Let \(Q_j\) be orthogonal projection onto the eigenspace for \(\lambda_j\); the projection onto the kernel sends any vector to its constant mean. For \(d=e_u-e_v\), orthogonality to constants gives
\[
f(t):=z_u(t)-z_v(t)=\sum_{j=1}^{m}\frac{d^T Q_j s}{1+t\lambda_j}.
\]
Taking a common denominator gives
\[
f(t)=\frac{N(t)}{\prod_{j=1}^{m}(1+t\lambda_j)},\qquad \deg N\le m-1\le n-2.
\]
The denominator is strictly positive for all \(t\ge0\). Unless \(N\) vanishes identically, every strict sign reversal requires a distinct real root of this nonzero polynomial. Hence there are at most \(n-2\) reversals. If the difference vanishes identically, it has no strict reversal and the count is zero.

**Sharp realization and freely chosen crossing locations.** On the unweighted path \(P_n\) with vertices numbered from one endpoint, the positive Laplacian eigenvalues \(\lambda_k=2-2\cos(k\pi/n)\), \(1\le k\le n-1\), are pairwise distinct. Associated orthonormal eigenvectors have coordinates
\[
u^{(k)}_i=\sqrt{2/n}\cos((i-\tfrac12)k\pi/n).
\]
Their first-edge differences satisfy
\[
u^{(k)}_1-\nu^{(k)}_2
=2\sqrt{2/n}\sin(k\pi/n)\sin(k\pi/(2n))>0,
\qquad 1\le k\le n-1.
\]
Thus selecting the coefficients of \(s\) along the nonconstant eigenvectors lets us prescribe independently the \(n-1\) residues of \(z_1(t)-z_2(t)\). Choose the rational function
\[
F(t)=\frac{\prod_{j=1}^{n-2}(t-\eta_j)}{\prod_{k=1}^{n-1}(1+t\lambda_k)}.
\]
All poles are distinct negative real numbers, and \(F\) is proper; therefore a real partial-fraction expansion \(F(t)=\sum_{k=1}^{n-1}c_k/(1+t\lambda_k)\) exists and is unique. Set
\[
s=\sum_{k=1}^{n-1}\frac{c_k}{u^{(k)}_1-u^{(k)}_2}u^{(k)}.
\]
Then \(z_1(t)-z_2(t)=F(t)\). The vector is nonconstant. An affine transformation \(s\mapsto a s+b\mathbf1\), where \(a>0\) is sufficiently small, puts all entries strictly between zero and one. It multiplies the difference by \(a\), preserving every simple positive root and each strict sign reversal. This proves sharpness for every prescribed collection of positive locations.

**Decreasing global variance.** Since \(\mathbf1^T L=0\), the mean of \(z(t)\) equals \(\bar s\). In any orthonormal eigenbasis \(\{u^{(k)}\}_{k=0}^{n-1}\), with positive eigenvalues repeated according to multiplicity, write \(s-\bar s\mathbf1=\sum_{k=1}^{n-1}a_ku^{(k)}\). Then
\[
V(t)=\sum_{k=1}^{n-1}\frac{a_k^2}{(1+t\lambda_k)^2},\qquad
V'(t)=-2\sum_{k=1}^{n-1}\frac{a_k^2\lambda_k}{(1+t\lambda_k)^3}<0
\]
for every \(t\ge0\) when \(s\) is nonconstant. This does not restrict the sign pattern of any one coordinate difference beyond the polynomial degree bound above.

## Verification

The complete proof is analytical for arbitrary finite \(n\) and positive symmetric edge weights. A reproducible exact-arithmetic check is supplied as `verification.py` (Python 3 plus SymPy); execute `python verification.py` beside this document. It solves exact rational interpolation problems on the unweighted paths with \(n=3,4,5,6\), constructs intrinsic opinions in \([0,1]\), checks the exact rational differences, and verifies the prescribed simple positive roots.

In particular, for the five-vertex path with intrinsic opinions
\[
s=(59/152,\,65/152,\,9/76,\,1,\,0)^T
\]
one obtains exactly
\[
z_1(t)-z_2(t)=
\frac{(t-1)(t-2)(t-3)}{152(t^2+3t+1)(5t^2+5t+1)}.
\]
Thus three strict reversals occur at \(t=1,2,3\). The finite computations illustrate and check the construction; they do **not** replace the eigenprojection and partial-fraction proof for arbitrary graph order.

## Relationship to prior work

The equilibrium model and the distinction between intrinsic and expressed opinions are established by Bindel, Kleinberg and Oren, whose 2011 publicly recorded talk and 2012 preprint focus on equilibrium disagreement, the price of anarchy, and network design rather than pairwise-order crossing counts as common influence strength varies [1,2]. Dandekar, Goel and Lee analyze aggregate network disagreement and biased-assimilation polarization, not this parameterized ranking question [3]. A later analysis of Friedkin–Johnsen boundary response ranks source and target centrality under heterogeneous susceptibility, which is distinct from comparing two expressed opinions along a scalar-influence family [4]. Numerical network opinion-formation studies also consider changing susceptibility but do not supply the sharp all-orders crossing classification [5].

The ingredients—spectral projectors, rational-resolvent denominators, partial fractions, and spectral contraction—are classical and not claimed new. The assessed claim is their exact sharp combination for the stated social-influence problem, including independently prescribed pairwise reversal locations on a path while global squared variation decreases. Equivalence to a more general previously published parametric-resolvent theorem cannot be ruled out without an independent literature audit.

## Limitations

The theorem is for undirected connected graphs with symmetric positive weights, uniform scalar rescaling of all ties, and fixed real-valued intrinsic opinions. It does not cover heterogeneous parameter changes, directed influence matrices, nonlinear dynamics, strictly binary intrinsic opinions, trajectories as elapsed time evolves, real-world empirical polarization, or predictions about political opinions. The constructed profile is tailored to its crossing locations and may be sensitive to perturbation; no robustness margin is claimed. The maximum of \(n-2\) counts crossings of a **fixed pair**, not the number of distinct global rankings of all agents. Novelty has not been independently audited.

## References

[1] S. Oren, *How Bad is Forming Your Own Opinion*, Institute for Advanced Study talk, November 7, 2011, https://www.ias.edu/video/csdm/oren (dated public presentation of the underlying model).

[2] D. Bindel, J. Kleinberg, and S. Oren, *How Bad is Forming Your Own Opinion?*, arXiv:1203.2973, first preprint version March 13, 2012, https://arxiv.org/abs/1203.2973.

[3] P. Dandekar, A. Goel, and D. Lee, *Biased Assimilation, Homophily and the Dynamics of Polarization*, arXiv:1209.5998, 2012, https://arxiv.org/abs/1209.5998.

[4] M. Boudourides, *Boundary-Value Friedkin–Johnsen Dynamics and Influence-Based Centralities on Networks*, arXiv:2602.08704, 2026, https://arxiv.org/abs/2602.08704.

[5] *Graphical analysis of agent-based opinion formation models*, PLOS ONE, 2024, https://pmc.ncbi.nlm.nih.gov/articles/PMC11139329/.
