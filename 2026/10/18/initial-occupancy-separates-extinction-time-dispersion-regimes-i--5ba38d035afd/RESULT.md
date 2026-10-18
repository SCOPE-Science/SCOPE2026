# Initial occupancy separates extinction-time dispersion regimes in a three-patch metapopulation

## Finding
In a homogeneous, continuous-time, three-patch colonization--extinction model, changing colonization intensity has qualitatively different effects on the coefficient of variation of global extinction time according to the number of initially occupied patches. From one or two occupied patches, squared coefficient of variation rises to a unique finite maximum and then decreases to one; from three occupied patches, it increases monotonically to one from below. From one initial patch it exceeds one at every positive colonization rate; from two it crosses one at an explicit positive threshold; from three it remains below one. In contrast, all three mean extinction times increase strictly with colonization.

## Assumptions and scope
There are exactly three distinguishable habitat patches, each either occupied or empty, supporting one species. Each occupied patch empties independently at exponential rate \(\mu>0\). Each ordered occupied--empty pair causes successful colonization at exponential rate \(\lambda\ge0\), independently. The all-empty configuration is absorbing, with no external immigration. Let \(X_t\in\{0,1,2,3\}\) count occupied patches. Transition rates are \(k\to k-1\) at \(k\mu\), and \(k\to k+1\) at \(k(3-k)\lambda\), for feasible \(k\). Write \(T_j=\inf\{t:X_t=0\}\) starting at \(X_0=j\). Put \(x=\lambda/\mu\ge0\) and \(F_j(x)=\operatorname{Var}(T_j)/(\mathbb E T_j)^2\). All expectations are finite because the transient state space is finite and extinction occurs with positive probability in bounded time.

The means are
\[
\begin{aligned}
\mu\mathbb E T_1&=(2x^2+3x+3)/3,\\
\mu\mathbb E T_2&=(4x^2+8x+9)/6,\\
\mu\mathbb E T_3&=(4x^2+8x+11)/6.
\end{aligned}
\]
The exact squared coefficients of variation are
\[
\begin{aligned}
F_1(x)&=\frac{4x^4+16x^3+37x^2+27x+9}{(2x^2+3x+3)^2},\\
F_2(x)&=\frac{16x^4+64x^3+152x^2+128x+45}{(4x^2+8x+9)^2},\\
F_3(x)&=\frac{16x^4+64x^3+152x^2+128x+49}{(4x^2+8x+11)^2}.
\end{aligned}
\]
In particular, \(F_1(x)>1\) for \(x>0\); \(F_2(x)>1\) exactly when \(x>(1+\sqrt{10})/2\); and \(F_3(x)<1\) for all \(x\ge0\). The unique maximum of \(F_1\) occurs at the positive root \(\xi\) of \(8x^4+52x^3+18x^2-69x-27\), approximately \(\xi=1.100965423\). The unique maximum of \(F_2\) occurs at \(1+\sqrt{31}/2\), approximately \(3.783882181\). \(F_3\) has no finite maximum and increases strictly. All three have limit one at infinity.

## Proof
The transient generator, indexed by occupied-patch counts \(1,2,3\), is
\[
Q=\mu\begin{pmatrix}
-1-2x&2x&0\\2&-2-2x&2x\\0&3&-3
\end{pmatrix}.
\]
Let \(A=-Q/\mu\). If \(u_j=\mu\mathbb E T_j\), first-step conditioning gives \(Au=\boldsymbol1\). If \(v_j=\mu^2\mathbb E T_j^2\), then \(Av=2u\). The explicit inverse exists for every \(x\ge0\), since absorption is certain. Solving these two systems yields the stated three means and squared coefficients \(F_j=(v_j-u_j^2)/u_j^2\). This also establishes the formulas for arbitrary dimensional rate \(\mu>0\), because it cancels from the relative variance.

For the sign comparison with one, direct factorization gives
\[
F_1-1=\frac{x(4x^2+16x+9)}{(2x^2+3x+3)^2},\quad
F_2-1=\frac{4(4x^2-4x-9)}{(4x^2+8x+9)^2},\quad
F_3-1=-\frac{24(2x+3)}{(4x^2+8x+11)^2}.
\]
The numerator of \(F_2-1\) has its unique nonnegative zero at \((1+\sqrt{10})/2\). Differentiate to obtain
\[
\begin{aligned}
F_1'(x)&=-\frac{8x^4+52x^3+18x^2-69x-27}{(2x^2+3x+3)^3},\\
F_2'(x)&=-\frac{16(2x+1)(4x^2-8x-27)}{(4x^2+8x+9)^3},\\
F_3'(x)&=\frac{48(2x+1)(6x+13)}{(4x^2+8x+11)^3}.
\end{aligned}
\]
The polynomial in the numerator of \(-F_1'\) has coefficient signs \(+,+,+,-,-\) in descending order; by Descartes' rule of signs it has at most one positive zero, and the signs at zero and infinity show at least one. It follows that \(F_1\) first strictly increases, then strictly decreases. The derivative of \(F_2\) changes from positive to negative at its unique nonnegative zero \(1+\sqrt{31}/2\). The derivative of \(F_3\) is everywhere positive. Leading coefficients show that all three functions approach one; their starting values follow by substitution. Finally all three mean expressions have strictly positive derivatives in \(x\ge0\), establishing monotone mean persistence despite the distinct variance profiles.

## Verification
The companion \(verify.py\) uses exact rational Gaussian elimination to solve the two moment systems directly at a range of rational colonization ratios. At each ratio it separately evaluates the closed rational formulas. It checks the generator rates, mean and second-moment identities, and the coefficient-of-variation formulas; it also checks the differential and factorization identities using direct exact polynomial arithmetic. The supplied proof is symbolic and valid for the entire nonnegative parameter half-line; finite tests are independent corroboration rather than an infinite proof.

## Relationship to prior work
Etienne and Heesterbeek (2000) develop finite-patch metapopulation persistence in terms of the mean time to global extinction and reserve design. Their subsequent 2001 work studies how local extinction and colonization rates affect persistence. The present distinction is instead among three initial occupancy counts and the *relative variability* of extinction time as colonization rises, with explicit turning and dispersion thresholds in the three-patch model. These outcomes follow from standard absorbing Markov-chain moment recursions, which are not claimed as novel. Keeling (2000) studies metapopulation moments and coupling using a different moment-closure setting. We make no claim to have excluded all older presentations of these exact rational identities under contact-process terminology.

## Limitations
Only three homogeneous patches, complete-mixing linkwise colonization, independent exponential local extinctions, fixed rates and no external recolonization are treated. The analysis gives the first two extinction-time moments and their parameter dependence, not the full survival distribution. The mathematical claim does not establish optimal interventions in heterogeneous or spatially embedded landscapes. Bibliographic overlap with older complete-graph contact-process or phase-type moment calculations remains an unresolved possibility; independent verification of originality is outstanding.

## References
- R. S. Etienne and J. A. P. Heesterbeek (2000), "On optimal size and number of reserves for metapopulation persistence," *Journal of Theoretical Biology* 203:33–50, doi:10.1006/jtbi.1999.1060.
- R. S. Etienne and J. A. P. Heesterbeek (2001), "Rules of thumb for conservation of metapopulations based on a stochastic winking-patch model," *The American Naturalist* 158:389–407, doi:10.1086/321986.
- M. J. Keeling (2000), "Metapopulation moments: coupling, stochasticity and persistence," *Journal of Animal Ecology* 69:725–736, doi:10.1046/j.1365-2656.2000.00430.x.
