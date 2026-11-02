# Two reactive traps on vertex-transitive networks: exact lifetime and resistance-optimal design

## Finding
For a finite connected vertex-transitive undirected network, two independent partial traps have a uniform-start mean capture time determined exactly by one Green-function diagonal and the effective resistance between trap sites. The optimal allocation of a fixed total reaction rate is **equal**, and the optimal placement maximizes effective resistance, independently of the reaction-rate budget.

Let \(G=(V,E)\) have \(n\ge2\) vertices, let \(L\) be its unit-conductance combinatorial Laplacian, and write \(G_0=L^+\) for the Moore–Penrose inverse. At distinct sites \(a,b\), install exponential killing rates \(\kappa_a,\kappa_b>0\). Put
\[
K=\kappa_a+\kappa_b,\quad P=\kappa_a\kappa_b,\quad g=\frac{\operatorname{tr}G_0}{n},\quad d=(G_0)_{aa}-(G_0)_{ab}=\frac12R_{\mathrm{eff}}(a,b).
\]
Then the mean lifetime from a **uniformly sampled** initial vertex is exactly
\[
\boxed{T=ng+n\frac{1-d^2P}{K+2dP}.}
\]
For fixed sites and budget \(K>0\), the unique minimum over strictly positive rates has \(\kappa_a=\kappa_b=K/2\). At this allocation,
\[
\boxed{T_{a,b}^{\mathrm{opt}}=\frac nK+ng-\frac n4R_{\mathrm{eff}}(a,b).}
\]
Thus every globally optimal pair is a maximum-effective-resistance pair, with no dependence on \(K\).

## Assumptions and scope
The finite graph is undirected, connected and vertex-transitive, with symmetric unit jump rates across each edge. The walk has generator \(-L\). The initial law is uniform on **all** vertices, including either trap; absorption occurs at independent exponential rates at precisely two distinct sites, with both rates positive. A weighted analogue holds whenever the symmetric generator has a common Green-function diagonal, although only vertex-transitive unit-edge graphs are asserted in the theorem. There is no discrete-time normalization or conditioning on avoiding the traps initially.

## Proof
Write \(\mathbf1\) for the all-ones vector and \(e_v\) for a vertex basis vector. The expected lifetime \(x\) from every initial site is the unique solution of
\[
(L+\kappa_a e_ae_a^\top+\kappa_b e_be_b^\top)x=\mathbf1.
\]
The matrix is symmetric positive definite: its quadratic form equals the sum of squared edge differences plus the two positive trap terms, and connectedness eliminates nonzero null vectors. Thus all means are finite.

Set \(c=n^{-1}\mathbf1^\top x\), \(t=\kappa_a x_a\) and \(u=\kappa_b x_b\). Summing the equations shows \(t+u=n\). Since \(G_0L=I-\mathbf1\mathbf1^\top/n\) and \(G_0\mathbf1=0\), applying \(G_0\) yields the exact vector identity
\[
x=c\mathbf1-tG_0e_a-uG_0e_b.
\]
Vertex transitivity implies a common diagonal \((G_0)_{vv}=g\), and symmetry gives \((G_0)_{ab}=g-d\). Evaluating at the traps therefore gives
\[
\frac t{\kappa_a}=c-ng+du,\qquad
\frac u{\kappa_b}=c-ng+dt.
\]
Subtracting shows
\[
(\kappa_a^{-1}+d)t=(\kappa_b^{-1}+d)u.
\]
Together with \(t+u=n\), this yields
\[
t=\frac{n\kappa_a(1+\kappa_bd)}{K+2dP},\qquad
u=\frac{n\kappa_b(1+\kappa_ad)}{K+2dP}.
\]
Substituting in \(c=ng+t/\kappa_a-du\) proves the first boxed formula. The resistance identity is \(R_{\mathrm{eff}}(a,b)=(e_a-e_b)^\top G_0(e_a-e_b)=2d\); positivity follows from connectedness and \(a\ne b\).

Holding \(K\) and \(d\) fixed, direct differentiation gives
\[
\frac{\partial T}{\partial P}=-\frac{nd(dK+2)}{(K+2dP)^2}<0.
\]
By the arithmetic-geometric mean inequality \(P\le K^2/4\), with equality only for equal rates, the optimizer is unique. At \(P=K^2/4\), factorization of the fraction gives \((1-dK/2)/K\); hence the second boxed formula and the maximum-resistance placement characterization.

As a concrete two-dimensional example, the \(3\times3\) square torus with all four nearest-neighbor jump rates equal to one has \(n=9\), \(g=2/9\), nearest-neighbor resistance \(4/9\), and diagonal resistance \(5/9\). There are only these two nonzero separation types. The exact optimum is therefore any diagonal pair, with \(T=9/K+3/4\). Neighboring sites instead give \(T=9/K+1\). These fractions follow from a rational inverse of \(L+\mathbf1\mathbf1^\top/9\), equivalently from \(G_0=L^+\).

## Verification
The included standalone `verify.py` constructs combinatorial Laplacians for cycles, complete graphs, Cartesian tori, and hypercubes; independently computes \(G_0\), the killed-generator inverse, and the two boxed formulas for unequal as well as equal rates. It also checks the exact \(3\times3\) torus resistances and optimization inequalities. These computations corroborate the finite examples; the algebraic argument proves the theorem for all finite connected vertex-transitive graphs.

Run `python verify.py` with Python 3 and NumPy. Numerical matrix inversions are not substituted for the proof.

## Relationship to prior work
Beveridge (2015), *A Hitting Time Formula for the Discrete Green's Function*, proves broad relationships between the Green function and ordinary single-target hitting times, including spectral formulas for the Green matrix; its theorem and sections 1–5 were compared directly. It does not assert the present two-partial-trap lifetime, optimal rate split, or maximum-resistance placement law. Lin, Julaiti and Zhang (2012) treat mean hitting times with one perfect trap; the accessible abstract identifies a different problem. Ghosh, Boyd and Saberi (2008) optimize graph **edge conductances** to minimize effective resistance, rather than optimize **trap positions and two killing rates** on a fixed graph. The resistance and pseudoinverse identities themselves are standard and are not claimed new. An earlier unlocated multiple-trap identity could imply the present formula; mathematical priority remains provisional. A prior source-started two-trap cycle result, while related, optimizes a different initial distribution and obtains an unequal allocation; it does not imply the uniform-start law for all vertex-transitive networks.

## Limitations
The theorem does not cover arbitrary nonuniform initial distributions, directed or nonreversible walks, three or more reactive sites, moving traps, or optimization of conductances. The mean capture time is a first moment, not the capture-time distribution. The proof is mathematical, with no experimental model validation. The result has not undergone independent scientific audit; historical originality remains open to further primary-literature review.

## References
- A. Beveridge, *A Hitting Time Formula for the Discrete Green's Function*, arXiv:1505.06989v1 (first posted 2015-05-26), https://arxiv.org/html/1505.06989v1.
- Y. Lin, A. Julaiti, Z. Zhang, *Mean first-passage time for random walks in general graphs with a deep trap*, Journal of Chemical Physics 137 (2012), https://doi.org/10.1063/1.4754735.
- A. Ghosh, S. Boyd, A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review 50 (2008), https://doi.org/10.1137/050645452.
