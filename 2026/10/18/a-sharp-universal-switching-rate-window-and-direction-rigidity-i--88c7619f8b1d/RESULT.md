# A sharp universal switching-rate window and direction rigidity in a three-site flashing ratchet

## Finding
For the three-position two-environment continuous-time flashing ratchet defined below, the stationary probability current along each oriented bond of the clockwise cycle is
\[
J(s)=\frac{3s\,(w_1-w_0)(w_2-w_1)(w_2-w_0)}{2(As^2+Bs+C)},
\]
where
\[
\begin{aligned}
e_1&=w_0+w_1+w_2,\\
e_2&=w_0w_1+w_1w_2+w_2w_0,\\
e_3&=w_0w_1w_2,\\
A&=e_1(e_1^2+e_2),\\
B&=6e_1^3-3e_1e_2-27e_3,\\
C&=9e_1(e_1^2-2e_2).
\end{aligned}
\]
All three coefficients are strictly positive for positive weights. For pairwise-distinct weights the current keeps the same nonzero sign at every positive switching rate, and its absolute value has exactly one global maximum, attained at
\[
s_*=\sqrt{\frac CA}=3\sqrt{\frac{w_0^2+w_1^2+w_2^2}{w_0^2+w_1^2+w_2^2+3e_2}},
\qquad \frac32<s_*<3.
\]
The constants at both endpoints are optimal as unattained limits over pairwise-distinct positive weights. The maximum current magnitude is
\[
\max_{s>0}|J(s)|=\frac{3|(w_1-w_0)(w_2-w_1)(w_2-w_0)|}{2(B+2\sqrt{AC})}.
\]
If two weights coincide, the current is identically zero, so uniqueness of a maximizing switching rate is not claimed. With clockwise site increments of one, the mean unwrapped displacement velocity is \(3J(s)\), not \(J(s)\).

## Assumptions and scope
The state space is \(\{0,1,2\}\times\{\mathrm{ON},\mathrm{OFF}\}\). Fix any three strictly positive finite site weights \(w_i\) and any symmetric environment-switching rate \(s>0\). Within the ON environment a jump from site \(i\) to any other site \(j\) has rate \(w_j/w_i\). In the OFF environment each such jump has rate one. Environment switches preserve the site and occur at rate \(s\) in either direction. The three sites are identified modulo three, with clockwise orientation \(0\to1\to2\to0\). Both frozen environments are reversible; the combined process is irreducible and admits a unique strictly positive stationary distribution. The weights may be interpreted as \(w_i=\exp[-\beta E_i/2]\), so ON rates obey the usual detailed-balance ratio for site energies \(E_i\).

Let \(p_i\) and \(q_i\) be the stationary masses at site \(i\) in the ON and OFF environments, respectively. Both environment masses sum to \(1/2\). The claimed current is the net clockwise rate across one bond, for example
\[
J(s)=\frac{w_1}{w_0}p_0-\frac{w_0}{w_1}p_1+q_0-q_1.
\]
Stationarity makes this net flux identical across all three oriented bonds. This definition counts physical clockwise versus counterclockwise jumps, not the switching transitions.

## Proof
Let \(L\) be the transpose of the ON generator, acting on stationary column vectors: \(L_{ji}=w_j/w_i\) for \(j\ne i\), and \(L_{ii}=-\sum_{j\ne i}w_j/w_i\). The transpose of the OFF generator is \(\mathbf1\mathbf1^\top-3I\). Its stationary equation is
\[
(3+s)q=\tfrac12\mathbf1+sp,
\]
where \(\sum_i p_i=\sum_iq_i=1/2\). Substituting this equality into the ON stationary equation and setting \(h=3s/(s+3)\) gives the three-by-three system
\[
(hI-L)p=\frac h6\mathbf1.
\]
Since \(h>0\), the matrix is invertible: \(L\) is an irreducible Markov generator transpose with one zero eigenvalue and its other eigenvalues in the open left half-plane. Moreover \(q_0-q_1=h(p_0-p_1)/3\), so the current can be computed entirely from the resolvent of \(L\).

For an explicit, independently checkable elimination, use the homogeneity of the rates to normalize \(w_0=1\), and write \(w_1=x\), \(w_2=y\). The above linear system has matrix
\[
L=\begin{pmatrix}
-(x+y)&1/x&1/y\\
x&-(1+y)/x&x/y\\
y&y/x&-(1+x)/y
\end{pmatrix}.
\]
Applying Cramer's rule to \((hI-L)p=h\mathbf1/6\) and substituting \(q_0-q_1=h(p_0-p_1)/3\) yields
\[
J=\frac{3s(x-1)(y-x)(y-1)}{2(As^2+Bs+C)},
\]
with \(e_1=1+x+y\), \(e_2=x+y+xy\), \(e_3=xy\). Multiplying numerator and denominator by \(w_0^3\) restores general weights and proves the displayed flux identity. The symbolic three-by-three elimination is separately reconstructed in the included verification program and checked against the direct six-state generator.

Write \(U=\sum_iw_i^2\). Elementary expansions give
\[
A=e_1(U+3e_2),\quad C=9e_1U,\quad B=6\sum_iw_i^3+15\sum_{i\ne j}w_i^2w_j.
\]
Thus \(A,B,C>0\). With \(V=(w_1-w_0)(w_2-w_1)(w_2-w_0)\), direct differentiation gives
\[
J'(s)=\frac{3V(C-As^2)}{2(As^2+Bs+C)^2}.
\]
If \(V\ne0\), \(J(s)\) has fixed sign, its absolute value tends to zero as \(s\downarrow0\) or \(s\to\infty\), and its unique critical point \(s_*\) is the unique global maximum of \(|J|\). Evaluating at that point gives the stated maximum.

Finally,
\[
U-e_2=\tfrac12\sum_{i<j}(w_i-w_j)^2>0
\]
for pairwise-distinct weights, while \(e_2>0\). Hence \(U<U+3e_2<4U\) and \(3/2<s_*<3\). For the lower sharpness limit take \(w=(1,1+\varepsilon,1+2\varepsilon)\) and let \(\varepsilon\downarrow0\). For upper sharpness take \(w=(1,R,R^2)\) and let \(R\to\infty\). If any two weights coincide, the Vandermonde factor \(V\) vanishes and the stationary current is zero identically.

## Verification
The included `verification.py` uses exact SymPy rational algebra. It checks the independent three-by-three symbolic resolvent against the closed expression, then reconstructs the complete six-state stationary generator and verifies the formula for 60 weight/rate pairs (including all-equal and two-equal boundary cases). It separately checks the analytic derivative factorization and strict optimizer bounds. Execute `python verification.py` with a working SymPy installation. The checks reproduce finite rational calculations, while the quantified all-positive-weights theorem is established by the displayed general algebra and inequalities.

## Relationship to prior work
Roldán and Parrondo (arXiv:1004.2831, first posted 16 April 2010) specified precisely the continuous-time six-state flashing scheme used here, in a selected three-height potential, for estimating dissipation. Their stationary-current discussions include weak-potential scaling and the vanishing-current fast-switching limit; their reported formulas concern entropy estimators rather than the present arbitrary-three-weight flux factorization or universal optimum over switching rates. The same three-position six-state ratchet is used as a simulation/inference benchmark by Seifner and collaborators (2023), especially their Section 5.1 and Appendix J; it is not presented there as a current-optimization theorem. The earlier minimal Brownian ratchet of Lee et al. (2003) is a distinct three-state discrete-time scheme. Work on continuous flashing-ratchet transport and quasi-steady-state effective potentials treats related mechanisms, but neither its continuum-limit approximations nor results for other generators imply the exact three-weight optimizer derived here. This claim is therefore restricted to the specified microscopic rates and does not assert general current-direction rigidity under switching.

## Limitations
The result is an exact six-state finite Markov-chain theorem, not an optimization theorem for arbitrary ratchet networks. Switching must be symmetric and spatially independent; ON rates must be the stated detailed-balance ratios, and OFF rates must equal one. Other rate conventions change the optimizer. No assertion is made about entropy-production optimality, large-state limits, arbitrary potentials on longer rings, biased driving, or a complete historical uniqueness proof. A plausible broader 2018 treatment of switched sawtooth potentials was not available for full-text comparison; that residual originality risk warrants independent review.

## References
1. É. Roldán and J. M. R. Parrondo, *Estimating dissipation from single stationary trajectories*, arXiv:1004.2831 (first posted 2010-04-16), Phys. Rev. Lett. 105, 150607 (2010). https://arxiv.org/pdf/1004.2831
2. M. Seifner et al., *Neural Markov Jump Processes*, Proceedings of ICML, PMLR 202 (2023), especially Section 5.1 and Appendix J. https://proceedings.mlr.press/v202/seifner23a/seifner23a.pdf
3. Y. Lee, A. Allison, D. Abbott, and H. E. Stanley, *Minimal Brownian ratchet: an exactly solvable model*, Phys. Rev. Lett. 91, 220601 (2003). https://doi.org/10.1103/PhysRevLett.91.220601
4. E. Levien and P. C. Bressloff, *Quasi-steady-state analysis of coupled flashing ratchets*, Phys. Rev. E 92, 042129 (2015). https://doi.org/10.1103/PhysRevE.92.042129
