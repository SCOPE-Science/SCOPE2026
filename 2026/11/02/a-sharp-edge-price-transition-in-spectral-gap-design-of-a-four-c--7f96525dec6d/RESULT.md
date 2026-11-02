# A sharp edge-price transition in spectral-gap design of a four-cycle

## Finding

Consider a four-vertex ring with edges \(01,12,23,30\). The first three edges have unit price per conductance; the closing edge has price \(\tau>0\). If the available total price is \(B>0\), the **maximum unnormalized Laplacian algebraic connectivity**, over all nonnegative edge conductances chosen independently, is exactly
\[
\Lambda(B,\tau)=\begin{cases}
\dfrac{4B}{5+\tau+2\sqrt\tau},&0<\tau\le9,\\[2mm]
\dfrac{B}{5},&\tau\ge9.
\end{cases}
\]
For \(0<\tau<9\), the unique reflection-invariant optimum has
\[
(w_{01},w_{12},w_{23},w_{30})=
\left(\frac\Lambda2,\frac{\Lambda(1+\sqrt\tau)}4,\frac\Lambda2,\frac{\Lambda(1+1/\sqrt\tau)}4\right).
\]
All four conductances are positive, and **every** global optimum, even if asymmetric, has a positive closing-edge conductance. The displayed symmetric optimum has a double Fiedler eigenvalue.

For \(\tau>9\), the **unique unrestricted optimum** is
\[
(w_{01},w_{12},w_{23},w_{30})=
\left(\frac{3B}{10},\frac{2B}{5},\frac{3B}{10},0\right).
\]
At the exact transition \(\tau=9\), an entire interval of reflection-invariant optimizers exists: setting \(\lambda=B/5\), for every \(1/2\le s\le3/2\),
\[
(w_{01},w_{12},w_{23},w_{30})=
\lambda\left(s,s+\frac12,s,\frac12-\frac s3\right).
\]
This is the complete reflection-invariant optimal set at equality; no complete classification of possibly asymmetric optimizers at \(\tau\le9\) is asserted.

## Assumptions and scope

There are exactly four labelled vertices \(0,1,2,3\); the only available undirected edges are \(01,12,23,30\), with independent conductances \(w_e\ge0\). The Laplacian is \(L=\sum_e w_e(e_i-e_j)(e_i-e_j)^\top\), with unnormalized Euclidean eigenvalues \(0=\lambda_1(L)\le\lambda_2(L)\le\cdots\). Prices are \(1,1,1,\tau\), and feasibility requires \(w_{01}+w_{12}+w_{23}+\tau w_{30}\le B\). Disconnected designs have zero algebraic connectivity. No restrictions of symmetry, irreducibility beyond graph support, or positive holding weights are imposed.

## Proof

**Symmetry reduction.** Reflect the vertices by \(0\leftrightarrow3\), \(1\leftrightarrow2\). This exchanges edge \(01\) with \(23\), and preserves edge costs. The function \(\lambda_2(L)\) equals the minimum Rayleigh quotient on the zero-sum subspace, hence is concave in conductances. Reflecting and averaging a feasible design cannot reduce the gap. Therefore a global optimum exists with \(w_{01}=w_{23}=a\), \(w_{12}=b\), \(w_{30}=c\).

**Spectrum.** Decompose the zero-sum subspace into reflection-even and reflection-odd subspaces. The reflection-even eigenvalue is \(2a\); the odd subspace has the symmetric block
\[
M=\begin{pmatrix}a+2c&-a\\-a&a+2b\end{pmatrix}.
\]
Thus \(\lambda_2(L)\ge1\) precisely when \(a\ge1/2\) and \(M-I\succeq0\). Write \(U=a+2b-1\), \(V=a+2c-1\). Since \(a>0\), the semidefinite condition requires \(U,V>0\), \(UV\ge a^2\). Its cost is
\[
2a+b+\tau c=\frac{1+\tau+(3-\tau)a+U+\tau V}{2}.
\]
By arithmetic–geometric mean, \(U+\tau V\ge2a\sqrt\tau\), with equality exactly at \(U=a\sqrt\tau\) and \(V=a/\sqrt\tau\). Therefore every feasible gap-one symmetric design costs at least
\[
\frac{1+\tau+(3-\tau+2\sqrt\tau)a}{2}.
\]
For \(0<\tau\le9\), the coefficient of \(a\) is \((3-\sqrt\tau)(1+\sqrt\tau)\ge0\), and \(a\ge1/2\). The minimum is \((5+\tau+2\sqrt\tau)/4\), attained by \(a=1/2\), \(b=(1+\sqrt\tau)/4\), \(c=(1+1/\sqrt\tau)/4\). Homogeneity in the budget yields the claimed spectral gap and scaled conductances. For strict inequality \(\tau<9\), equality in these two bounds fixes \(a,U,V\) uniquely; hence the displayed design is the unique reflection-invariant optimum. Its even eigenvalue and smaller odd eigenvalue both equal its gap.

**The transition face.** At \(\tau=9\), the coefficient of \(a\) vanishes. Equality then requires \(U=3a\), \(V=a/3\), giving \(b=a+1/2\), \(c=1/2-a/3\) for unit gap. Nonnegativity and the even-mode condition are equivalent to \(1/2\le a\le3/2\), so these and only these reflection-invariant designs attain gap one at cost five. Multiply by \(B/5\).

**Expensive-edge optimum without symmetry assumptions.** Take the mean-zero vector \(z=(-3/2,-1/2,1/2,3/2)\), with \(\|z\|^2=5\). Its squared jumps along \(01,12,23,30\) are \(1,1,1,9\). For any feasible conductances and any \(\tau\ge9\),
\[
\lambda_2(L)\le \frac{z^\top Lz}{5}
=\frac{w_{01}+w_{12}+w_{23}+9w_{30}}5\le\frac B5.
\]
The proposed path design with three nonzero weights \((3B/10,2B/5,3B/10)\) has eigenvalues \(0,B/5,3B/5,6B/5\), attaining the bound. For \(\tau>9\), equality forces \(w_{30}=0\) and requires \(z\) to be a Fiedler eigenvector. The four equations in \(Lz=(B/5)z\) force the three path weights uniquely to the displayed values. This proves global, unrestricted uniqueness for \(\tau>9\).

For \(0<\tau<9\), the above attainable gap strictly exceeds \(B/5\), while every design with \(w_{30}=0\) obeys the same Rayleigh upper bound \(B/5\). Hence all unrestricted optima must retain the closing edge. Budget saturation follows from positive homogeneity of the gap and positivity of the attained optimum.

## Verification

The standalone standard-library script `verify.py` independently constructs weighted Laplacians and diagonalizes them by Jacobi rotations. Its run returned `VERIFY_OK exact_rational_sqrt_cost_cases=135 boundary_family_cases=11 independent_spectra=120 arbitrary_feasible_comparisons=4200`. The first two groups check exact rational identities; the remaining groups test spectra and arbitrary asymmetric feasible allocations. These finite calculations are cross-checks, **not** proofs of global optimality, which follows from the displayed block reduction, semidefinite inequality and Rayleigh certificate.

## Relationship to prior work

Ghosh and Boyd (2006) formulate algebraic-connectivity bounds using convex optimization. Göring, Helmberg and Reiss (2011) develop related spectral-width optimization and graph-realization semidefinite duality. Göring, Helmberg and Wappler discuss graph realizations and connectivity in general semidefinite frameworks, and Fiedler's earlier work treats optimal tree connectivity. These frameworks motivate weighted edge-budget spectral design; the inspected material does not give the complete priced four-cycle transition, including its critical interval of optimizers and unrestricted high-price uniqueness. A general optimization formulation is not itself the closed-form all-price phase diagram.

## Limitations

The theorem concerns a four-vertex ring with three identically priced edges, one exceptional edge, and the unnormalized Laplacian. It does not classify all potentially asymmetric optimizers for \(\tau\le9\), generalize to longer cycles, or establish absolute priority over all specialized literature. The 1990 Fiedler source was examined only through bibliographic and abstract information; specialized results might contain overlapping formulations. No independent mathematical audit has been performed.

## References

1. A. Ghosh and S. Boyd, *Upper bounds on algebraic connectivity via convex optimization*, Linear Algebra and its Applications 418 (2006), 693–707; publicly available online May 5, 2006. https://stanford.edu/~boyd/papers/pdf/eigbounds_laplacian.pdf
2. F. Göring, C. Helmberg, and M. Reiss, *On Minimizing the Spectral Width of Graph Laplacians and Associated Graph Realizations*, preprint 2011. https://www.tu-chemnitz.de/mathematik/preprint/2011/PREPRINT_04.pdf
3. F. Göring, C. Helmberg, and M. Wappler, *Embedded in the Shadow of the Separator*, SIAM Journal on Optimization 19 (2008), 472–501. https://www-user.tu-chemnitz.de/~helmberg/GoeHelWap_R07_SIOPT.pdf
4. M. Fiedler, *Absolute algebraic connectivity of trees*, Linear and Multilinear Algebra 26 (1990), 85–106. https://doi.org/10.1080/03081089008817967
