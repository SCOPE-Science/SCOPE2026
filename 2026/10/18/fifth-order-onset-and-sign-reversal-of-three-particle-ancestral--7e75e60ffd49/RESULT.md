# Fifth-order onset and sign reversal of three-particle ancestral circulation

## Finding
Consider the three-site Fleming–Viot system described below. For the killing rates \(k(\varepsilon)=(1-\varepsilon,1,1+\varepsilon)\), its stationary survival-weighted ancestral current from site \(0\) to site \(2\) is
\[
\Delta_3(\varepsilon)=\frac{89}{56010528}\,\varepsilon^5+O(\varepsilon^7)\qquad(\varepsilon\to0).
\]
Thus its first nonzero Taylor term has *order five* and positive coefficient. For sufficiently small positive \(\varepsilon\), this three-particle current is positive, whereas the corresponding current for each fixed \(N\ge4\) is negative by the known cubic expansion of Lin and Lu [1]. The opposite near-neutral directions distinguish the smallest circulating population from every larger fixed population size.

## Assumptions and scope
The sites are \(I=\{0,1,2\}\), with single-particle motion rates \(q(i,j)=1\) for \(i\ne j\). There are exactly \(N=3\) particles. A particle at \(i\) is killed at rate \(k_i>0\), immediately takes the site and ancestral label of a uniformly chosen other particle, and all natural motion and copying clocks act continuously in time. For \(|\varepsilon|<1\), all three killing rates above are positive.

Write \(\Omega_3=\{c\in\mathbb N_0^3: c_0+c_1+c_2=3\}\). Its ten-state count process has stationary law \(\pi_\varepsilon\). Let \(h_\varepsilon(i,d)\), for \(i\in I\) and \(d\in\mathbb N_0^3\) with \(|d|=2\), be the probability that a distinguished founder initially at \(i\), with the other two particle counts \(d\), eventually supplies the entire surviving population's label. The stationary coefficients and signed current are
\[
F_{ij}(\varepsilon)=\sum_{\substack{c\in\Omega_3\\c_i>0}}\pi_\varepsilon(c)c_i h_\varepsilon(j,c-e_i),\qquad
\Delta_3(\varepsilon)=F_{02}(\varepsilon)-F_{20}(\varepsilon).
\]
The sign convention is current oriented \(0\to2\). No nonlocal-in-\(\varepsilon\) sign assertion is made.

## Proof
**1. Exact finite linear systems.** For distinct \(i,j\), the count generator \(L_\varepsilon\) has off-diagonal entries
\[
L_\varepsilon(c,c-e_i+e_j)=c_i+\tfrac12c_ic_jk_i(\varepsilon),
\]
and diagonals equal to minus row sums. Its stationary column satisfies \(L_\varepsilon^{\mathsf T}\pi_\varepsilon=0\) and \(\sum_c\pi_\varepsilon(c)=1\). The distinguished-founder function is the unique solution to \(T_\varepsilon h_\varepsilon=0\), normalized by \(h_\varepsilon(0,(2,0,0))=1/3\), with the eighteen-state operator
\[
\begin{aligned}
(T_\varepsilon h)(i,d)={}&\sum_{j\ne i}[h(j,d)-h(i,d)]
 +\sum_a d_a\sum_{b\ne a}[h(i,d-e_a+e_b)-h(i,d)]-k_i h(i,d)\\
&+\sum_a d_a k_a\left[h(i,d-e_a+e_i)
 +\tfrac12\sum_b(d_b-\mathbf1_{a=b})h(i,d-e_a+e_b)-h(i,d)\right].
\end{aligned}
\]
Terms with zero multiplicity are omitted. These operators are the event-by-event count and founder equations; the finite-chain uniqueness and fixation normalization follow from [1, §3]. The normalizations make their augmented matrices invertible for positive killing rates.

**2. Rational Taylor recurrence.** Set \(L_\varepsilon=L_0+\varepsilon L_1\) and \(T_\varepsilon=T_0+\varepsilon T_1\), and expand \(\pi_\varepsilon=\sum_{r\ge0}\pi_r\varepsilon^r\) and \(h_\varepsilon=\sum_{r\ge0}h_r\varepsilon^r\). For \(r\ge1\) their coefficients are uniquely determined by
\[
\begin{aligned}
L_0^{\mathsf T}\pi_r&=-L_1^{\mathsf T}\pi_{r-1},&\sum_c\pi_r(c)&=0,\\
T_0 h_r&=-T_1h_{r-1},&h_r(0,(2,0,0))&=0.
\end{aligned}
\]
At order zero the same left-hand operators have right side zero, with \(\sum_c\pi_0(c)=1\) and \(h_0(0,(2,0,0))=1/3\). These equations involve only rational \(10\times10\) and \(18\times18\) augmented inverses, so every displayed coefficient is exact.

Write \([\varepsilon^r]\Delta_3=\alpha_r\). Substituting the unique solutions above into the defining flux yields the finite convolution
\[
\alpha_r=\sum_{a+b=r}\sum_{c\in\Omega_3}\pi_a(c)
\left[\mathbf1_{c_0>0}c_0h_b(2,c-e_0)
-\mathbf1_{c_2>0}c_2h_b(0,c-e_2)\right].
\]
The accompanying exact-rational verifier reconstructs all matrix entries from the event rules, solves these recurrences, and verifies their residual equations. Its result is
\[
(\alpha_0,\ldots,\alpha_7)=
\left(0,0,0,0,0,\frac{89}{56010528},0,-\frac{410017}{1524382530048}\right).
\]
In particular, the coefficients of orders one and three cancel exactly, but the fifth does not.

**3. Remainder and sign.** Each finite normalized linear system depends analytically on \(\varepsilon\) near zero, because its augmented determinant is nonzero there. Exchanging site names \(0\leftrightarrow2\) sends \(\varepsilon\mapsto-\varepsilon\) and \(\Delta_3\mapsto-\Delta_3\), so the analytic current is odd. The exact fifth-order coefficient therefore gives the stated \(O(\varepsilon^7)\) remainder and positivity for all sufficiently small \(\varepsilon>0\). Lin and Lu [1, Eq. (2.1)] prove the negative cubic current for every fixed \(N\ge4\); comparison supplies the sign reversal, without asserting a uniform neighborhood in \(N\).

## Verification
Run `python check_fv_quintic.py` using Python 3 and SymPy. This exact-arithmetic calculation asserts the complete founder and stationary residuals, computes every Taylor coefficient through order seven for \(N=3\), and independently checks the sign and normalization by solving the *two-color absorbing chain*, rather than the founder equation, at two positive perturbations. The two-color calculation also reproduces the exact three-particle benchmark \(\Delta_3(1,2,4)=421413160/139117744582101\) from [1, Eq. (1.10)]. The same Taylor machinery obtains \([\varepsilon^3]\Delta_4=-1/157300\), matching the separate \(N=4\) specialization of [1, Eq. (2.1)]. No random sampling or floating-point threshold is used to establish the theorem.

## Relationship to prior work
Lin and Lu [1] prove generic ancestral circulation already for three particles and derive a negative cubic perturbative coefficient for \(N\ge4\). Their Appendix A evaluates the three-particle case at the isolated killing vector \((1,2,4)\), and their Appendix B computes Taylor coefficients only through order three. Neither statement determines the first nonzero perturbative coefficient for \(N=3\). The cancellation of its cubic term alone does not determine whether the current vanishes on the entire symmetric perturbation family, nor its first nonzero order or direction. The present finite exact computation resolves this exceptional boundary and gives a sign opposite to the larger-population cubic regime. Background work on two-particle Fleming–Viot balance and large-population conditioned processes does not specify this three-particle fifth-order current.

## Limitations
This is a local Taylor result for exactly three particles on a unit-rate triangle and the single symmetric killing line. It does not characterize all killing vectors, a global sign interval, or asymptotics uniform in particle number. The coefficient is supported by a fully specified finite rational calculation; independent external validation has not been performed. Although no covering statement was found in the searched literature, differently indexed prior derivations remain possible.

## References
[1] Yaohui Lin and Tiankui Lu, *Ancestral circulation beyond two Fleming–Viot particles*, arXiv:2610.12589v1, first submitted 2026-10-08. https://arxiv.org/html/2610.12589v1; particularly §§2–3 and Appendices A–B.
[2] Mateusz Kwaśnicki, *Fleming–Viot couples live forever*, Probability Theory and Related Fields 188 (2024), 1385–1408. DOI 10.1007/s00440-023-01247-z. Two-particle background as cited in [1].
