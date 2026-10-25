# Universal vertices exactly attain the worst Crank–Nicolson positivity threshold

## Finding
For every connected unweighted simple graph \(G\) on \(N\ge3\) vertices, its second-order Crank–Nicolson diffusion update \(P_h\) preserves nonnegative data for every timestep
\[
0\le h\le \frac{2}{N-2}.
\]
This **uniform bound is sharp precisely for graphs having a universal vertex** (a vertex adjacent to all other vertices). Every graph without a universal vertex has a strictly larger individual positivity threshold. At the sharp uniform endpoint, precisely the universal vertices have zero holding-probability entries; all other diagonal entries and all off-diagonal entries are strictly positive. At a universal vertex the update's diagonal is exactly
\[
(P_h)_{vv}=\frac{2-(N-2)h}{2+Nh}\quad(h\ge0).
\]
Thus changing arbitrarily many edges among its neighbors does not change this entry or the network's maximal positivity timestep. For \(N=2\), positivity holds at every finite timestep.

## Assumptions and scope
\(G=(V,E)\) is connected, undirected, finite, simple and unweighted, \(|V|=N\ge3\). Define \(L_G=D_G-A_G\). For \(h\ge0\), put \(t=h/2\), \(C_G(t)=(I+tL_G)^{-1}\), and
\[
P_h=C_G(t)(I-tL_G)=2C_G(t)-I.
\]
A nonnegative update means all entries are nonnegative, equivalently the method maps every nonnegative input to a nonnegative output. Its row sums are one because \(L_G\mathbf1=0\). Define \(h_{\mathrm{pos}}(G)\) as the supremum of nonnegative timesteps, including the endpoint.

## Proof
**1. Positivity reduces to diagonal resolvent entries.** The matrix \(I+tL_G\) is a nonsingular irreducible symmetric \(M\)-matrix for \(t>0\), so its inverse is strictly positive entrywise. Therefore \(P_h=2C_G(t)-I\) has strictly positive off-diagonal entries for \(h>0\), and is nonnegative exactly when \((C_G(t))_{ii}\ge1/2\) for every vertex \(i\). At \(h=0\) it is the identity.

**2. Comparison with the complete graph and strict equality.** The complement-edge Laplacian \(E=L_{K_N}-L_G\) is positive semidefinite. Consequently \(I+tL_G\preceq I+tL_{K_N}\), hence
\[
C_G(t)\succeq C_{K_N}(t)=\frac{I+t\mathbf1\mathbf1^{\mathsf T}}{1+Nt}.
\]
The diagonal inequality gives \((C_G(t))_{ii}\ge (1+t)/(1+Nt)\) for every vertex. Moreover, for \(t>0\) equality for a particular vertex \(i\) occurs **if and only if** \(i\) is universal. Indeed, the positive-semidefinite difference of inverses has zero quadratic form on \(e_i\) precisely when \(E C_{K_N}(t)e_i=0\). One way to establish this criterion rigorously is to interpolate \(F(s)=(I+tL_{K_N}-stE)^{-1}\); then
\[
e_i^{\mathsf T}(C_G-C_{K_N})e_i=\int_0^1 t\,(F(s)e_i)^{\mathsf T}E(F(s)e_i)\,ds,
\]
which vanishes if and only if \(E^{1/2}C_{K_N}e_i=0\) (the integrand is continuous and nonnegative; the converse follows because if \(E C_{K_N}e_i=0\), this vector solves every interpolated linear system). Since \(E\mathbf1=0\) and \(C_{K_N}e_i=(e_i+t\mathbf1)/(1+Nt)\), equality means \(Ee_i=0\), i.e. there is no missing edge incident to \(i\). This is exactly universality.

**3. Sharp uniform threshold and equality class.** The complete-graph diagonal is at least \(1/2\) exactly when \(t\le1/(N-2)\). Therefore every graph is positive for \(h\le 2/(N-2)\). At the endpoint, the strict equality criterion gives zero entries of \(P_h\) precisely at universal vertices. If no universal vertex exists, all diagonals are strictly positive at this endpoint; continuity yields a positive margin beyond it. If there is a universal vertex, the next step supplies a negative diagonal for all larger timesteps.

**4. Exact universal-vertex entry.** Order vertices with universal \(v\) first and let \(H=G-v\). In block form
\[
I+tL_G=\begin{pmatrix}1+(N-1)t&-t\mathbf1^{\mathsf T}\\-t\mathbf1&(1+t)I+tL_H\end{pmatrix}.
\]
The lower-right block \(B\) satisfies \(B^{-1}\mathbf1=\mathbf1/(1+t)\). Its Schur complement is \((1+Nt)/(1+t)\), whence \((C_G)_{vv}=(1+t)/(1+Nt)\) for every \(t\ge0\). Multiplying by two and subtracting one yields \((P_h)_{vv}=(2-(N-2)h)/(2+Nh)\), negative whenever \(h>2/(N-2)\). Thus the bound is attained exactly by graphs with a universal vertex. For \(N=2\), direct substitution gives diagonal \(2/(2+2h)>0\) for all finite \(h\), proving the stated exceptional case.

## Verification
The accompanying `VERIFY.py` constructs exact integer Laplacians and rational resolvents, enumerates every connected labeled graph on three, four and five vertices, and tests random connected universal-vertex graph completions on six through eight vertices. It checks the sharp diagonal equality class and the universal-vertex formula at two distinct rational timesteps. This finite audit corroborates, but does not replace, the all-graph argument above. Run `python VERIFY.py` with SymPy installed. No network access is needed.

## Relationship to prior work
Crank–Nicolson time stepping in parabolic control is established in von Daniels–Hinze–Vierling (arXiv:1403.3010). Higueras–Roldán (arXiv:2301.01066) investigate sharp numerical positivity for one-dimensional Dirichlet heat-equation grids, not extremal graph-order thresholds. A publicly indexed mathematical record entitled *A resolvent-return law for Crank–Nicolson positivity on reversible Markov chains* gives the general return-resolvent criterion and sharp thresholds on reversible chains. That criterion is compatible with, but does not explicitly state in its accessible abstract, the present sharp **graph-order extremal inequality and universal-vertex equality characterization**. Its full text could not be inspected; this is a residual overlap risk rather than a claim that it fails to cover the theorem.

## Limitations
The theorem concerns the nonnegative entry property of the **single completed Crank–Nicolson step** for unweighted simple connected graphs and does not compare accuracy, decay speed, or long-time error. It gives an exact uniform worst-case threshold and equality characterization, not a closed formula for the larger individual thresholds of graphs lacking universal vertices. Multiple universal vertices are allowed. The mathematical argument is self-contained, but historical uniqueness remains subject to an external literature audit.

## References
- N. von Daniels, M. Hinze, M. Vierling, *Crank-Nicolson time stepping and variational discretization of control-constrained parabolic optimal control problems*, arXiv:1403.3010 (initial submission 2014-03-12), https://arxiv.org/abs/1403.3010.
- I. Higueras, T. Roldán, *A new insight on positivity and contractivity of the Crank–Nicolson scheme for the heat equation*, arXiv:2301.01066 (2023), https://arxiv.org/abs/2301.01066.
- *A resolvent-return law for Crank–Nicolson positivity on reversible Markov chains*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-a-resolvent-return-law-for-crank-nicolson-positivity-on-reversib--d475df91cd2a (accessible abstract only).
