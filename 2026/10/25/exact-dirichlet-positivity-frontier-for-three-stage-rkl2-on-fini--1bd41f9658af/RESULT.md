# Exact Dirichlet positivity frontier for three-stage RKL2 on finite paths

## Finding

Let \(N\geq 2\) be the number of interior nodes of a one-dimensional grid with homogeneous Dirichlet boundary data, and let \(M_N\) be the tridiagonal second-difference matrix with diagonal entries \(-2\) and first off-diagonal entries \(1\). Set \(c=\alpha\Delta t/\Delta x^2\geq0\). For the three-stage, second-order Runge–Kutta–Legendre method (RKL2), the update matrix is

\[
R_N(c)=I+cM_N+\frac{c^2}{2}M_N^2+\frac{c^3}{15}M_N^3.
\]

Within the bulk stability interval \(0\leq c\leq 5/4\), this update preserves componentwise nonnegativity for every nonnegative initial vector if and only if

\[
c\leq c_N:=\begin{cases}
\dfrac{15-\sqrt{30}}{13},&N=2,\\[5pt]
\dfrac{15-\sqrt{15}}{14},&N\geq3.
\end{cases}
\]

The cutoff is attained at the boundary-adjacent matrix entry. Above it, that entry is negative even though the step remains inside the bulk stability interval.

## Assumptions and scope

The spatial operator is the standard centered second difference for \(u_t=\alpha u_{xx}\), with \(\alpha>0\), mesh spacing \(\Delta x>0\), and fixed zero values at both exterior boundary nodes. There are \(N\geq2\) interior unknowns. The parameter \(c\) is dimensionless. The interval \(c\leq5/4\) is the RKL2 three-stage bulk CFL bound; it is used here as a common stability benchmark, not as the exact largest spectral-stability interval of every finite matrix \(M_N\). Positivity means preservation of the nonnegative orthant for every nonnegative input vector, equivalently entrywise nonnegativity of \(R_N(c)\).

## Proof

For the shifted Legendre polynomial \(P_3\),

\[
P_3(1+z)=1+6z+\frac{15}{2}z^2+\frac{5}{2}z^3.
\]

The RKL2 definition with three stages is the convex blend of \(I\) and \(P_3(I+2cM_N/5)\), with blend weight \(5/12\). Substitution and collection of powers gives exactly

\[
R_N(c)=I+cM_N+\frac{c^2}{2}M_N^2+\frac{c^3}{15}M_N^3.
\]

For \(N=2\), direct multiplication gives

\[
M_2^2=\begin{pmatrix}5&-4\\-4&5\end{pmatrix},\qquad
M_2^3=\begin{pmatrix}-14&13\\13&-14\end{pmatrix}.
\]

Thus the diagonal entries of \(R_2(c)\) equal
\[
q_e(c)=1-2c+\frac52c^2-\frac{14}{15}c^3,
\]
and its off-diagonal entries equal
\[
p_2(c)=c-2c^2+\frac{13}{15}c^3
      =\frac{c}{15}(15-30c+13c^2).
\]
The two roots of the quadratic factor are \((15\pm\sqrt{30})/13\). The larger root exceeds \(5/4\), so within \([0,5/4]\), \(p_2(c)\geq0\) exactly when \(c\leq(15-\sqrt{30})/13\). The diagonal term is positive throughout this interval: for \(0\leq c\leq5/4\), it is bounded below by \(1-2c+\frac52c^2-\frac{14}{15}(5/4)^3\), and on the relevant interval \(0\leq c\leq(15-\sqrt{30})/13<4/5\) the sharper bound \(q_e(c)\geq3/5-896/1875>0\) applies. This proves the \(N=2\) case.

For \(N\geq3\), the nonzero entries of \(M_N^2\) are: endpoint diagonal \(5\), interior diagonal \(6\), adjacent entries \(-4\), and distance-two entries \(1\). For \(M_N^3\), the endpoint diagonal is \(-14\), interior diagonal \(-20\), boundary-adjacent entries are \(14\), interior-adjacent entries (when present) are \(15\), distance-two entries are \(-6\), and distance-three entries are \(1\). Therefore the corresponding entries of \(R_N(c)\) are

\[
\begin{aligned}
q_e(c)&=1-2c+\frac52c^2-\frac{14}{15}c^3,\\
q_i(c)&=1-2c+3c^2-\frac43c^3,\\
p_b(c)&=c-2c^2+\frac{14}{15}c^3
       =\frac{c}{15}(15-30c+14c^2),\\
p_i(c)&=c-2c^2+c^3=c(1-c)^2,\\
p_2(c)&=\frac{c^2}{2}-\frac25c^3
       =c^2\left(\frac12-\frac{2c}{5}\right),\\
p_3(c)&=\frac{c^3}{15}.
\end{aligned}
\]
Here \(p_b\) is the first off-diagonal entry next to either boundary, \(p_i\) is an interior first off-diagonal entry, and \(p_2,p_3\) are the distance-two and distance-three entries. Terms whose distance exceeds the path length are absent.

The roots of \(15-30c+14c^2\) are \((15\pm\sqrt{15})/14\). Its larger root exceeds \(5/4\); hence \(p_b(c)\geq0\) on the bulk interval exactly up to \(c_3=(15-\sqrt{15})/14\). All other off-diagonal entries are nonnegative on \([0,5/4]\): \(p_i(c)=c(1-c)^2\), \(p_2(c)=c^2(1/2-2c/5)\), and \(p_3(c)=c^3/15\). The diagonal entries are positive for \(0\leq c\leq c_3<4/5\): the bound \(q_e(c)\geq3/5-896/1875>0\) holds, and \(q_i'(c)=-2(1-c)(1-2c)\) shows that the minimum of \(q_i\) on \([0,4/5]\) is \(q_i(1/2)=7/12>0\). Thus every entry is nonnegative for \(c\leq c_3\). For \(c_3<c\leq5/4\), \(p_b(c)<0\), so the matrix is not entrywise nonnegative. This proves the result for every \(N\geq3\).

Finally, a linear map preserves every nonnegative vector if and only if its matrix is entrywise nonnegative: necessity follows by applying it to each coordinate vector, and sufficiency follows by summing nonnegative matrix entries against nonnegative coordinates. The stated thresholds are therefore both necessary and sufficient.

## Verification

The polynomial expansion was checked symbolically from the RKL2 definition. Exact integer-matrix multiplication for \(N=2,3,4,5\) gives the boundary and interior coefficients displayed above; the banded-matrix argument establishes the same formulas for all \(N\geq3\). The critical factors are \(15-30c+13c^2\) for \(N=2\) and \(15-30c+14c^2\) for \(N\geq3\); their lower roots are respectively approximately \(0.7325211096\) and \(0.7947869038\). The proof is symbolic and finite-dimensional, not an inference from numerical experiments. It makes no claim about nonlinear operators, nonuniform grids, other boundary conditions, or RKL2 stage counts other than three.

## Relationship to prior work

Tan, Aslam, and Bertozzi prove that RKL1 and RKL2 are monotone through their bulk stability bounds for the constant-coefficient heat equation with boundaryless, periodic, or homogeneous Neumann conditions. Their theorem explicitly restricts those boundary conditions, so it does not imply entrywise positivity for the finite Dirichlet matrices considered here. Earlier work by Dawes reports regions of RKL nonmonotonicity under Dirichlet conditions. The result here supplies an exact algebraic cutoff for the three-stage RKL2 method and identifies a dimension transition between two interior nodes and three or more; it does not claim that Dirichlet nonmonotonicity itself is new. The full Dawes article was not accessible in the materials reviewed, so exact prior coverage of these particular thresholds cannot be ruled out absolutely.

## Limitations

The result concerns only the linear one-dimensional centered Dirichlet Laplacian and three-stage RKL2 within the bulk CFL interval. It does not establish a threshold for arbitrary stage number, nonuniform meshes, multidimensional domains, variable coefficients, nonlinear diffusion, or other boundary treatments. A relevant earlier paper reports Dirichlet nonmonotonicity, and its full text was not accessible for direct comparison; this remains the principal originality risk. The claim is an exact finite-matrix classification, not a general theorem for all parabolic discretizations.

## References

1. Z. Tan, T. D. Aslam, and A. L. Bertozzi, “Explicit Monotone Stable Super-Time-Stepping Methods for Finite Time Singularities,” arXiv:2507.17062, first submitted 2025-07-22, especially equations (10)–(11) and Theorem 7(b). https://arxiv.org/abs/2507.17062
2. A. S. Dawes, “Some properties of the Runge-Kutta-Legendre super-time-stepping explicit methods,” *Computers & Fluids* 214 (2021), 104762. https://doi.org/10.1016/j.compfluid.2020.104762
3. T. Skaras, T. Saxton, C. D. Meyer, and T. D. Aslam, “Super-time-stepping schemes for parabolic equations with boundary conditions,” *Journal of Computational Physics* 425 (2021), 109879. https://doi.org/10.1016/j.jcp.2020.109879
