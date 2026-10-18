# Symmetry-breaking habitat allocation on a four-patch corridor

## Finding
Fix four habitat patches on the undirected path \(1-2-3-4\), with strictly positive area fractions \(a_i\) satisfying \(\sum_{i=1}^4 a_i=1\). Suppose the linearized patch-colonization matrix is the symmetric nonnegative matrix \(W(a)\), with \(W_{ij}(a)=(a_i a_j)^{3/8}\) when \(|i-j|=1\), and zero otherwise. There is an area allocation whose spectral radius strictly exceeds that of **every** reflection-symmetric allocation \((a_1,a_2,a_3,a_4)=(u,v,v,u)\). The strict global maximum is attained at positive areas, so every globally optimal allocation breaks the reflection symmetry of the corridor; reflected optimizers necessarily come in distinct pairs.

For the mean-field occupancy system \(\dot y_i=-y_i+\tau(1-y_i)\sum_{j}W_{ij}(a)y_j\), the empty state has Jacobian \(-I+\tau W(a)\). Consequently, the corresponding minimal colonization coefficient \(\tau_c(a)=1/\rho(W(a))\) at the **linear invasion threshold** is strictly smaller under some asymmetric allocation than under any symmetric one. This does not assert stochastic finite-population persistence.

A fully explicit positive witness is \(r=(5,10,11,10)\), \(S=\sum_i r_i^8=414749506\), and \(a_i=r_i^8/S\). Its Perron-Rayleigh test vector \(x_i=r_i^4/\sqrt S\) gives
\[
\rho(W(a))\ge\frac{2\sum_{i=1}^{3}(r_ir_{i+1})^7}{S^{7/4}}>\frac{161}{250},
\]
whereas every symmetric allocation satisfies \(\rho(W(a))<161/250\). Both strict inequalities admit integer-only certificates.

Among connected simple paths of one, two, three, or four patches, four is the smallest order at which this symmetry-breaking phenomenon occurs for the same elasticity: on the two- and three-vertex paths the unique optimal area allocation is reflection-symmetric.

## Assumptions and scope
Habitat area is divisible and freely allocated across all existing vertices; its sum is fixed to one and every area is strictly positive. The path edges are the only possible dispersal contacts and all have equal baseline strength. The exponent \(3/8\) is attached to **each** endpoint's area, so a contact carries the product power \((a_i a_j)^{3/8}\). Extinction is normalized to unit rate and colonization multiplies by \(\tau>0\). The local invasion threshold is the linear stability boundary of the mean-field equations, not a stochastic extinction-time statement or a full global-dynamics theorem.

The graph remains a four-patch path: vertices are not deleted even if a limiting optimization considers zero-area boundaries. All actual witnessing allocations have positive areas.

## Proof
**1. Area optimization as a nonlinear graph eigenproblem.** For a connected graph \(G\), generalize the contact matrix to \(W_{ij}(a)=A_{ij}(a_i a_j)^{\alpha/2}\), with total area one and \(\alpha>0\). Define \(p=2/(1+\alpha)\). For \(0<\alpha<1\), \(p>1\). If \(x\) is a nonnegative unit Euclidean vector, set \(z_i=a_i^{\alpha/2}x_i\). Hölder's inequality gives
\[
\sum_i z_i^p\le (\sum_i a_i)^{\alpha/(1+\alpha)}(\sum_i x_i^2)^{1/(1+\alpha)}=1.
\]
The Rayleigh quotient is \(x^T W(a)x=2\sum_{ij\in E(G)}z_iz_j\). Conversely, for any \(z_i\ge0\) with \(\sum_i z_i^p=1\), choose \(a_i=z_i^p\) and \(x_i=z_i^{p/2}\); then \(\sum_i x_i^2=1\) and \(z_i=a_i^{\alpha/2}x_i\). Thus
\[
\max_{a\in\Delta}\rho(W(a))=\max_{z_i\ge0,\ \sum_i z_i^p=1}\,2\sum_{ij\in E(G)}z_iz_j.
\]
Here \(\Delta\) is the *closed* area simplex, used only to establish existence. For connected \(G\) and \(p>1\), any maximizing \(z\) must have every coordinate positive: if a zero coordinate neighbors a positive one, adding \(\varepsilon\) at the zero coordinate and rescaling by \((1+\varepsilon^p)^{-1/p}\) increases the objective by a positive term of order \(\varepsilon\) against a loss of order \(\varepsilon^p\). Any proper nonempty support has such a boundary edge. Hence a positive optimal area allocation exists in the original domain.

**2. Rigorous bound on every reflection-invariant allocation.** Specialize to \(\alpha=3/4\), so \(p=8/7\). A reflection-invariant area vector gives a reflection-invariant nonnegative leading eigenvector, by positivity and continuity at the boundary. The reduction in step 1 bounds its spectral radius by the maximum of \(2(2uv+v^2)\) over \(2u^p+2v^p=1\), with \(u,v\ge0\). Set \(u/v=t^7\) for \(v>0\) (the case \(v=0\) gives zero). Then this symmetric Rayleigh maximum is
\[
F(t)=2^{-3/4}\frac{1+2t^7}{(1+t^8)^{7/4}},\qquad t\ge0.
\]
Its derivative has the sign of \(1-t-t^8\). Because \(t+t^8\) increases strictly from zero to infinity, \(F\) has one global maximum at the unique \(t_0>0\) satisfying \(t_0+t_0^8=1\). Exact rational arithmetic establishes
\[
\frac{8116}{10000}<t_0<\frac{8117}{10000}.
\]
Monotonicity of numerator and denominator separately yields the rational fourth-power bound
\[
 F(t_0)^4\le \frac{(1+2(8117/10000)^7)^4}{8(1+(8116/10000)^8)^7}<\left(\frac{161}{250}\right)^4.
\]
The final inequality is verified by cross-multiplication of positive rational denominators and is independently replayable in the included certificate.

**3. Explicit asymmetric strict improvement.** Let \(r=(5,10,11,10)\), \(S=\sum_i r_i^8=414749506\), choose \(a_i=r_i^8/S\), and use the unit vector \(x_i=r_i^4/\sqrt S\). A direct Rayleigh evaluation gives
\[
 x^T W(a)x=\frac{Q}{S^{7/4}},\qquad Q=2\sum_{i=1}^3(r_ir_{i+1})^7=781049340000000.
\]
The exact positive-integer comparison \(Q^4> (161/250)^4 S^7\) proves the Rayleigh value exceeds \(161/250\). By step 2, it exceeds the optimum over reflection-invariant allocations. Compactness, continuity, and positivity from step 1 imply a global optimal area vector exists, and none can be reflection-invariant. Since the path reverses vertices, it maps each maximizing allocation to a second distinct one.

**4. Minimality within paths.** For two patches the spectral radius equals \((a_1a_2)^{3/8}\), uniquely maximized at equal areas. For three patches it is \([a_2^{3/4}(a_1^{3/4}+a_3^{3/4})]^{1/2}\). Strict concavity of the exponent makes \(a_1=a_3=(1-a_2)/2\) optimal, and the product \(a_2(1-a_2)\) is maximized uniquely at \(a_2=1/2\). A one-vertex path has no nontrivial reflection reversal. Thus four is the least path order allowing an optimality-forcing symmetry break for this model and elasticity.

## Verification
Run `python3 verify.py` with the accompanying standard-library-only program. It uses exact `fractions.Fraction` comparisons for both bracket inequalities and for the integer Rayleigh certificate, and performs supplementary small-path arithmetic checks; the unique small-path optimizers are proved analytically above. Reported decimal approximations are descriptive only: \(F(t_0)\approx0.643650079\), while the explicit witness Rayleigh value is approximately \(0.647967441\). The strict result needs neither floating-point root solving nor exhaustive numerical search.

## Relationship to prior work
Hanski and Ovaskainen (2000) introduced metapopulation capacity as a landscape-matrix Perron eigenvalue and linked it to extinction-state stability. Bertuzzo et al. (2015), in full-text sections 2–4, use landscape capacity to compare evolving tree network geometries, not the constrained area allocation on a fixed four-patch corridor with this power law. Kang and Nikiforov (2014), whose primary paper's introduction and statements were examined, define the \(p\)-spectral graph radius and prove extremal forbidden-subgraph inequalities. Step 1 is an **exact reduction to their established graph invariant**, not an independent invention of a new spectral theory. Their quoted results concern comparisons among graphs and do not state or imply the concrete failure of reflection-symmetric optimization on a fixed four-vertex path. The claim is specifically the small-order strict symmetry-breaking certificate and its threshold interpretation, not that the full eigenvalue framework or nonlinear norm equivalence is new.

## Limitations
The contact matrix is an intentionally simplified area-elastic symmetric dispersal model; actual spatial kernels, directed connectivity, heterogeneous species responses, fixed minimum-area constraints, and other elasticities can behave differently. The theorem identifies non-symmetric global maximizers but does **not** classify their exact coordinates, uniqueness up to reflection, or the critical elasticity at which symmetry breaking starts. The rational witness need not itself be globally optimal. The proof does not infer stochastic persistence from a mean-field linear invasion criterion. A specialized nonlinear-graph-spectrum result elsewhere might contain an equivalent four-path observation; bibliographic originality remains conditional on the inspected literature.

## References
1. Hanski, I., and Ovaskainen, O. (2000), *The metapopulation capacity of a fragmented landscape*, Nature 404, 755–758. DOI: 10.1038/35008063; publicly indexed publication date 2000-04-13 (abstract accessible).
2. Kang, L., and Nikiforov, V. (2014), *Extremal Problems for the \(p\)-Spectral Radius of Graphs*, Electronic Journal of Combinatorics 21(3), P3.21. DOI: 10.37236/4113; open full text https://www.combinatorics.org/ojs/index.php/eljc/article/download/v21i3p21/pdf/ (introduction, definitions and principal theorems inspected).
3. Bertuzzo, E. et al. (2015), *Metapopulation capacity of evolving fluvial landscapes*, Water Resources Research. DOI: 10.1002/2015WR016946; open full text https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2015wr016946 (model, equations, results and discussion inspected).
