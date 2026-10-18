# A sharp strict period-three criterion in the two-saddle border-collision map

## Finding

Consider the continuous border-collision normal form
\[
F(x,y)=\begin{cases}
(ax+y+1,-dx),&x\le0,\\
(bx+y+1,-ex),&x\ge0.
\end{cases}
\]
All parameters are real. Assume the **two-saddle region**
\[
\Phi=\{(a,d,b,e):a>|1+d|,\quad b<-|1+e|\}.
\]
Define
\[
T=a^2b-a(d+e)-bd,\quad J=d^2e,\quad D=1-T+J,
\]
\[
N_0=ab+ae+b+de-d+1,\qquad
N_1=ab+a+bd+de-e+1,
\]
\[
N_2=a^2+ad+a+d^2-d+1.
\]
**Theorem.** For every parameter point of \(\Phi\), a strict \(LLR\) primitive period-three orbit with Schur-stable third-return derivative exists if and only if
\[
\boxed{D>0,\quad N_0<0,\quad N_1<0,\quad |J|<1,\quad 1+T+J>0.}
\]
The orbit, unique for this cyclic itinerary, has successive first coordinates \(N_0/D,N_1/D,N_2/D\), and its first state is \((N_0/D,-eN_2/D)\). Every strict Schur-attracting primitive period-three orbit in \(\Phi\) has this itinerary up to cyclic rotation: no strict \(LRR\) orbit can be Schur-stable. At
\[
(a,d,b,e)=\left(\frac75,\frac13,-\frac{16}{5},-4\right),
\]
the strict \(LLR\) orbit is
\[
\left(-\frac{7845}{353},\frac{10360}{353}\right)
\longmapsto
\left(-\frac{270}{353},\frac{2615}{353}\right)
\longmapsto
\left(\frac{2590}{353},\frac{90}{353}\right)
\longmapsto
\left(-\frac{7845}{353},\frac{10360}{353}\right).
\]
This orbit is locally exponentially attracting and remains so under all sufficiently small parameter perturbations.

## Assumptions and scope

The symbol \(L\) means strictly \(x<0\), and \(R\) means strictly \(x>0\). The theorem concerns primitive cycles of exact least period three whose three states have nonzero first coordinate. *Schur-stable* means that both eigenvalues of the derivative of the three-step return map have modulus strictly below one. It does **not** classify cycles touching the switching line, eigenvalue-modulus-one cycles, global basins, or possible coexistence with other attractors. No claim is made that every parameter point in \(\Phi\) possesses a chaotic attractor. A strict Schur-stable cycle is a genuine locally exponentially attracting orbit because its three-piece return map is affine in an open neighborhood of the orbit.

## Proof

Write the branch derivatives and common affine forcing as
\[
A_L=\begin{pmatrix}a&1\\-d&0\end{pmatrix},\quad
A_R=\begin{pmatrix}b&1\\-e&0\end{pmatrix},\quad c=(1,0)^\mathsf T.
\]
A formal \(LLR\) three-cycle \(z_0,z_1,z_2\) satisfies \(z_1=A_Lz_0+c\), \(z_2=A_Lz_1+c\), and \(z_0=A_Rz_2+c\). Hence \((I-A_RA_L^2)z_0=A_R(A_Lc+c)+c\). Direct multiplication yields
\[
\operatorname{tr}(A_RA_L^2)=T,\quad
\det(A_RA_L^2)=J,\quad
\det(I-A_RA_L^2)=D.
\]
For \(D\ne0\), solving the two-by-two system gives first coordinates
\[
(x_0,x_1,x_2)=\left(\frac{N_0}{D},\frac{N_1}{D},\frac{N_2}{D}\right),\qquad
 y_0=-e\frac{N_2}{D}.
\]
These equations hold algebraically before admissibility is imposed. Because \(a>|1+d|\), one has \(a+d+1>0\), and therefore
\[
N_2=a(a+d+1)+(d^2-d+1)>0
\]
(the second summand is strictly positive for every real \(d\)).

For a real two-by-two matrix with trace \(T\) and determinant \(J\), the strict Jury–Schur inequalities are \(1-T+J>0\), \(1+T+J>0\), and \(1-J>0\). Together the first two imply \(J>-1\), so they are equivalent to \(D>0\), \(1+T+J>0\), and \(|J|<1\). A Schur-stable \(LLR\) cycle therefore has \(D>0\). Because \(N_2>0\), its strict itinerary holds exactly when \(N_0<0\), \(N_1<0\), and \(D>0\). These conditions are both necessary and sufficient, and the invertible return equation gives uniqueness for the itinerary.

For the opposite cyclic itinerary \(LRR\), the return matrix is \(A_R^2A_L\), with trace \(T'=ab^2-ae-bd-be\) and determinant \(J'=de^2\). Solving its affine period-three equation, whenever \(D'=1-T'+J'\ne0\), gives the first coordinate of the putative initial \(L\)-state as
\[
x'_0=\frac{b^2+be+b+e^2-e+1}{D'}.
\]
Within \(\Phi\), \(b<0\) and \(b+e+1<0\). Consequently the numerator is
\[
b(b+e+1)+(e^2-e+1)>0.
\]
If the \(LRR\) return were Schur-stable, then \(D'>0\), forcing \(x'_0>0\). This contradicts the required initial \(L\)-state. Hence no strict \(LRR\) period-three cycle is Schur-stable in \(\Phi\).

A three-letter symbolic word with both branches belongs, up to cyclic rotation, to either \(LLR\) or \(LRR\). A word using only one branch cannot give a *Schur-attracting* primitive period-three orbit in \(\Phi\): that branch has a saddle eigenvalue of absolute value greater than one, and the derivative of its third iterate retains an unstable multiplier. This proves completeness of the strict Schur-attracting classification.

For the displayed rational parameters, \(a>|1+d|\) and \(b<-|1+e|\) hold strictly. Exact substitution yields \(T=-9/125\), \(J=-4/9\), \(D=706/1125\), \(1+T+J=544/1125\), and \(1-|J|=5/9\), all required positive. The displayed coordinates have the prescribed signs, and direct exact substitution confirms each successive map image. Since every condition is strict, the conclusion persists on an open parameter neighborhood.

## Verification

A standalone standard-library Python script `verify.py` checks the rational witness, its complete three-state return, the strict two-saddle inequalities, the trace and determinant, and the Schur margins using exact fractions. It also checks both symbolic itinerary formulas against admissible rational examples. Execute `python verify.py` in a directory containing that script. The analytic parameter-wide assertions are proved above; these finite calculations are only reproducible checks, not an exhaustive parameter-space proof.

## Relationship to prior work

Ghosh, McLachlan and Simpson (2024) introduced the two-saddle region \(\Phi\) in their treatment of chaotic-attractor bifurcations, including noninvertible cases. They analyzed stable low-period cycles, notably two- and four-cycles, but did not state this exact strict period-three classification across \(\Phi\). Fatoyinbo and Simpson (2022/2023) already showed a stable \(LLR\) cycle **outside** the two-saddle region: their illustrated example uses \((a,d,b,e)=(0.5,0.5,-2,-0.5)\), so \(a\) does not exceed \(|1+d|\). That prior existence result is not claimed here as new. Their exact \(LRR\)-cycle stability analysis uses a different sign of the border-collision offset and does not imply the present all-\(\Phi\) obstruction for \(LRR\) at positive offset. Prior general symbolic techniques for affine periodic orbits and the Jury test are standard ingredients; the contribution is their sharp synthesis into a necessary-and-sufficient two-saddle classification, with an explicit nonempty attracting locus and opposite-itinerary obstruction.

## Limitations

The theorem excludes switching-line collisions and return multipliers on the unit circle. It does not describe nonattracting period-three cycles, global invariant sets, coexistence with chaotic attractors, or all other period lengths. The exact semialgebraic inequalities are specific to the normalized affine forcing \((1,0)\) and the two-saddle parameter region; different offsets require re-normalization. Equivalent classifications in uninspected general literature remain a publication-priority risk. The supporting numerical and rational checks do not replace the analytic proof.

## References

1. I. Ghosh, R. I. McLachlan and D. J. W. Simpson, *The bifurcation structure within robust chaos for two-dimensional piecewise-linear maps*, arXiv:2402.05393v1 (first posted 2024-02-08), especially Eq. (1.1), Secs. 3, 8–9. https://arxiv.org/abs/2402.05393
2. H. O. Fatoyinbo and D. J. W. Simpson, *A synopsis of the non-invertible, two-dimensional, border-collision normal form with applications to power converters*, arXiv:2210.14445v1 (2022-10-26); Int. J. Bifurc. Chaos 33 (2023), 2330019, especially Figs. 3, 7 and Appendix A. https://arxiv.org/abs/2210.14445
3. D. J. W. Simpson, *Sequences of periodic solutions and infinitely many coexisting attractors in the border-collision normal form*, arXiv:1312.2651 (2013), for a distinct codimension-three coexistence mechanism. https://arxiv.org/abs/1312.2651
