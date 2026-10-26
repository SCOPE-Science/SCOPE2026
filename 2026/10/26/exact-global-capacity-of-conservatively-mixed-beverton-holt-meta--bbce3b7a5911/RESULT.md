# Exact global capacity of conservatively mixed Beverton–Holt metapopulations

## Finding

**Theorem (maximum abundance and exact deficiency).** In the positive, conservative, dispersal-before-demography Beverton–Holt system specified below, the largest total positive-equilibrium population over **all** strictly positive column-stochastic dispersal matrices has an explicit formula, is attained by a strictly positive rank-one matrix, and obeys an exact quadratic–rational deficit identity. The optimizers form a relatively open convex polytope of affine dimension \((p-1)^2\). The optimum strictly exceeds the summed isolated carrying capacities precisely when the patches do not all share the same intrinsic growth rate.

For patch indices \(i=1,\ldots,p\), define
\[
 a_i=K_i/r_i,\qquad s_i=\sqrt{1+r_i},\qquad
 B=\sum_i a_i s_i,\qquad C=\sum_i a_i(2+r_i),\qquad q=C/B>2,
\]
\[
 t=\frac{2}{q+\sqrt{q^2-4}}\in(0,1),\quad \tau=t^2,\quad
 y_i^*=a_i\left(\frac{s_i}{t}-1\right)>0,\quad
 N^*=\sum_i y_i^*=\frac Bt-\sum_i a_i.
\]
For every admissible dispersal matrix \(D\), write \(x(D)\) for its unique positive equilibrium, \(y(D)=Dx(D)\), and \(N(D)=\sum_i x_i(D)\). Then
\[
 \boxed{\ (1-\tau)\bigl(N^*-N(D)\bigr)
 =\tau\sum_{i=1}^{p}\frac{(r_i/K_i)\bigl(y_i(D)-y_i^*\bigr)^2}{1+(r_i/K_i)y_i(D)}\ }. \tag{1}
\]
In particular \(N(D)\leq N^*\), with equality exactly when \(y(D)=y^*\). Define \(x_i^*=g_i(y_i^*)=s_i t y_i^*\). All maximizing dispersal matrices are exactly
\[
 \boxed{\ \{D:\ D_{ij}>0,\ \sum_iD_{ij}=1\text{ for each }j,\ Dx^*=y^*\}\ }. \tag{2}
\]
This set is nonempty: \(D^*_{ij}=y_i^*/N^*\) works for every column. It has affine dimension \((p-1)^2\) relative to the space of real matrices. Finally,
\[
 N^*\geq\sum_iK_i,\qquad
 N^*=\sum_iK_i\ \Longleftrightarrow\ r_1=\cdots=r_p.
\]

## Assumptions and scope

Fix an integer \(p\geq2\), arbitrary strictly positive local carrying capacities \(K_i\) and intrinsic growth parameters \(r_i\), and a time-independent strictly positive column-stochastic \(p\times p\) matrix \(D\). A unit of population in source patch \(j\) is redistributed to destination \(i\) with fraction \(D_{ij}\); hence dispersal conserves total abundance. Dispersal precedes local recruitment in each time step:
\[
 x_i(t+1)=g_i\bigl((Dx(t))_i\bigr),\qquad
 g_i(z)=\frac{(1+r_i)z}{1+(r_i/K_i)z},\quad z\geq0.
\]
Initial states are strictly positive. The limiting total abundance is the sum of coordinates of the positive fixed point; no stochastic, mortality-during-dispersal, spatial-network, or dispersal-cost constraint is imposed.

## Proof

**1. Well-defined unique attracting positive equilibrium.** The map \(F(x)=g(Dx)\) is monotone and strictly subhomogeneous on the positive cone: for every \(c>1\) and \(x>0\), \(F(cx)<cF(x)\) coordinatewise. The strictly positive matrix \(A=\operatorname{diag}(1+r_i)D\) has Perron root greater than one: since \(\sum_i(Au)_i=\sum_j u_j\sum_i(1+r_i)D_{ij}>\sum_j u_j\) for any positive Perron vector \(u\), its eigenvalue exceeds one. Hence a sufficiently small positive multiple of \(u\) is a strict lower solution. The local maps are uniformly bounded by \((1+r_i)K_i/r_i\), so a sufficiently large positive vector is an upper solution. Monotone iteration yields a positive fixed point. Two distinct positive fixed points contradict strict subhomogeneity by scaling the smaller vector to first touch the larger; applying the same lower/upper iteration sandwiches every positive trajectory. Thus the equilibrium is unique and globally attracting in the strictly positive cone.

**2. Common-marginal construction.** For \(b_i=r_i/K_i=1/a_i\), differentiation gives
\[
 g_i'(z)=\frac{s_i^2}{(1+b_i z)^2}.
\]
Because \(C-2B=\sum_i a_i(s_i-1)^2>0\), the number \(q\) exceeds two; the smaller positive root \(t\) of \(t+t^{-1}=q\) lies strictly between zero and one. The proposed positive \(y_i^*\) satisfies \(1+b_i y_i^*=s_i/t\), so \(g_i'(y_i^*)=t^2=\tau\) for every patch. Direct expansion gives
\[
 \sum_i(g_i(y_i^*)-y_i^*)
 =\sum_i a_i(s_i t-1)(s_i/t-1)
 =C-B(t+t^{-1})=0. \tag{3}
\]
Therefore \(\sum_i x_i^*=\sum_i y_i^*=N^*\), where \(x_i^*=s_i t y_i^*\). With \(D^*_{ij}=y_i^*/N^*\), conservation and (3) imply \(D^*x^*=y^*\), hence \(g(D^*x^*)=x^*\). Thus the proposed maximum is attained by an admissible matrix.

**3. Exact tangent remainder.** For any \(z\geq0\), elementary fraction algebra (no approximation) gives
\[
 g_i(y_i^*)+\tau(z-y_i^*)-g_i(z)
 =\frac{\tau b_i(z-y_i^*)^2}{1+b_i z}. \tag{4}
\]
At any positive equilibrium with \(y=Dx\), column stochasticity yields \(\sum_i y_i=\sum_i x_i=N\), while \(x_i=g_i(y_i)\). Sum (4), use (3), and use \(\sum_i(y_i-y_i^*)=N-N^*\). The result is precisely identity (1). Its denominators are positive and \(0<\tau<1\), so equality requires each \(y_i=y_i^*\), then \(x_i=x_i^*\). Conversely, any strictly positive column-stochastic \(D\) with \(Dx^*=y^*\) has equilibrium \(x^*\). These are all maximizers.

**4. Full optimizer dimension.** The linear equations \(\mathbf1^{\mathsf T}D=\mathbf1^{\mathsf T}\) contribute \(p\) independent column conditions. Given those, the \(p\) conditions \(Dx^*=y^*\) have exactly one redundant component (summing both sides), and the other \(p-1\) are independent because \(x^*>0\). The affine solution dimension is therefore \(p^2-p-(p-1)=(p-1)^2\). Since \(D^*>0\), its intersection with the positive-matrix cone is a nonempty relatively open convex polytope (bounded in that affine space).

**5. Carrying-capacity comparison.** For every patch, \(g_i(K_i)=K_i\), hence \(\sum_i(g_i(K_i)-K_i)=0\). Apply the summed identity (4) at the reference vector \(z_i=K_i\) (this step needs no assumption that \(K\) is an equilibrium of a common mixing matrix). One obtains
\[
 (1-\tau)\left(N^*-\sum_iK_i\right)
 =\tau\sum_i\frac{b_i(K_i-y_i^*)^2}{1+b_iK_i}\geq0. \tag{5}
\]
Equality holds exactly when \(K_i=y_i^*\) for all \(i\). The marginal condition then gives \(\tau=g_i'(K_i)=1/(1+r_i)\), which is possible only for common \(r_i\). Conversely, if all \(r_i=r\), then \(t=(1+r)^{-1/2}\) and directly \(y_i^*=K_i\). This completes the proof.

## Verification

A standalone standard-library Python file `verify.py` verifies the algebra in the exact field \(\mathbb Q(\sqrt5)\) for \(p=2\), \(K=(3,8)\), and \(r=(3,8)\). Here
\[
 t=(3-\sqrt5)/2,\quad y^*=\left(2+\sqrt5,\ (7+3\sqrt5)/2\right),
 \quad N^*=(11+5\sqrt5)/2>11=\sum_iK_i.
\]
It also runs 780 deterministically seeded configurations for patch counts one through six, each comparing a random positive conservative dispersal matrix with its corresponding rank-one maximizer and checking equilibrium, tangency, the exact-deficit formula numerically, and the sharp equal-growth boundary. Execute `python3 verify.py`. These finite computations test implementation and examples; the universal statements follow from the proof, not from numerical enumeration.

## Relationship to prior work

Rafael Bravo de la Parra, *Dispersal and Total Population Size in Discrete-Time Metapopulation Models* (2026), supplies the discrete-time, conservative, dispersal-before-demography framework; proves global stability of positive equilibria under its regularity assumptions; and analyzes how dispersal can increase or decrease total equilibrium abundance. In the Beverton–Holt setting it gives explicit two-patch sign conditions and a finite-dispersal construction. It does not in the inspected introduction, principal result descriptions, two-patch section, and conclusion supply an exact all-matrix global maximum over an arbitrary number of patches, the matrix-optimizer locus, or the deficit identity (1).

Grumbach and coauthors (2023) study asymptotic total population versus dispersal strength in discrete- and continuous-time two-patch models, with specified scalar dispersal families. Jorba-Cuscó and coauthors (2024) study optimization in a two-patch continuous-time diffusion setting. Segura, Marvá, and Franco (2025) consider number and topology of patches with prescribed dispersal families. These settings do not directly imply a global bound across every strictly positive conservative mixing matrix in the present discrete-time model. The proof's common-tangent optimization is elementary once the correct pre-growth vector is introduced, and older equivalent presentations may exist under other terminology.

## Limitations

The result optimizes **equilibrium total abundance**, not growth rate, resilience, transient abundance, or fitness under costs. It assumes unconstrained strictly positive migration with unit survival and Beverton–Holt demographic response after dispersal; sparse, geographically constrained, time-dependent, state-dependent, or lossy dispersal may have other optima. There is no claim of independent audit or absolute bibliographic priority; an equivalent older general concavity or resource-allocation theorem could exist. The numerical checks are finite and are not proofs of the theorem.

## References

1. Rafael Bravo de la Parra (2026). *Dispersal and Total Population Size in Discrete-Time Metapopulation Models*. Mathematics 14(19), 3624. DOI: 10.3390/math14193624. First online: 2026-10-07. https://www.mdpi.com/2227-7390/14/19/3624
2. Grumbach and coauthors (2023). *Effect of dispersal on asymptotic total population size in discrete- and continuous-time two-patch models*. Journal of Mathematical Biology. https://link.springer.com/article/10.1007/s00285-023-01984-8
3. Jorba-Cuscó and coauthors (2024). *Optimal dispersal and diffusion-enhanced robustness in two-patch metapopulations*. https://pmc.ncbi.nlm.nih.gov/articles/PMC10904506/
4. Segura, Marvá, and Franco (2025). *Dispersal in multi-patch metapopulations: The impact of patch number and network topology*. Journal of Theoretical Biology. https://pubmed.ncbi.nlm.nih.gov/41344394/
