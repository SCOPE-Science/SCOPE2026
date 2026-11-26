# Sharp finite-chain cutoff for partial uphill current in symmetric two-species exclusion

## Finding

Consider the boundary-driven hard-core two-species reaction-diffusion chain of Casini, Giardinà and Vernia with diagonal diffusivity \(a>b>0\), off-diagonal diffusivity \(b\), and reaction parameter \(U\ge 2b\). Let \(N\ge1\) be the number of sites and \(L=N+1\). Suppose the total reservoir density falls by \(\delta>0\) from left to right, while the A-minus-B reservoir density rises from \(-m\) to \(+m\), where \(m>\delta/2\). Thus the right reservoir has the greater A density. Define
\[
\lambda=\operatorname{arcosh}\left(1+\frac{U}{a-b}\right),\qquad z=e^{-\lambda},\qquad
R=\frac{a+b}{a-b}\frac{\delta}{m},\qquad
F_L=L(1-z)\frac{1+z^{L-1}}{1-z^L}.
\]
The stationary discrete Fickian A-current is strictly left-to-right on every link, including the two reservoir links, if and only if \(F_{N+1}<R\). The function \(F_L\) increases strictly from \(F_2=2\) to infinity, so there is a unique real crossing for \(R>2\), yielding an exact integer chain-length cutoff. If \(F_{N+1}=R\), both reservoir-link currents are zero and every interior link (if any) has positive current. If \(F_{N+1}>R\), both reservoir-link currents are negative. When also \(R\ge2\), at least one interior link still has positive current. If \(R\le2\), all-link strict uphill current is impossible at any length; for \(R<2\) an interior positive current beyond the cutoff criterion is not guaranteed.

For \(a=1\), \(b=1/2\), \(U=1\), \(m=1/4\), \(\delta=3/10\), and average reservoir total density \(t=1/2\), the crossing lies strictly between \(N=3\) and \(N=4\): \(F_4=10/3<R=18/5<F_5=170/41\). The currents in order from the left reservoir are \((1,11,11,1)/240\) at \(N=3\) and \((-28,147,172,147,-28)/4100\) at \(N=4\).

## Assumptions and scope

Sites have states vacant, A or B, with at most one particle per site. An interior pair exchanges its two states at rate \(a\) and exchanges them after interchanging A and B (fixing vacancies) at rate \(b\). Additional single-site colour mutations from the two nearest-neighbour contributions have rates \(U-2b-h\) and \(h\), where \(0\le h\le U-2b\). Use the associated boundary generator in [1, Eqs. (41)–(43)]; if \(N=1\), both boundary operators act on the sole site and the bulk sum is empty. The stationary one-point equations are independent of \(h\). In the exact example, \(h=0\) and \(U=2b\).

Let \(\rho_j^A,\rho_j^B\) be the stationary one-point densities, with fictitious sites \(j=0,L\) encoding the reservoirs. Put \(T_j=\rho_j^A+\rho_j^B\) and \(M_j=\rho_j^A-\rho_j^B\). The data are
\[
T_0=t+\delta/2,\quad T_L=t-\delta/2,\quad M_0=-m,\quad M_L=m,
\qquad m+\delta/2\le t\le1-\delta/2.
\]
These bounds ensure nonnegative A, B and vacancy densities at the reservoirs. The current is the discrete constitutive component
\[
J_{A,j}=a(\rho_j^A-\rho_{j+1}^A)+b(\rho_j^B-\rho_{j+1}^B),\qquad 0\le j\le N.
\]
The A continuity equation also contains a reaction term. This current is not the total-particle current and is not a pure A-tracer crossing count of the swap-and-mutation transition.

## Proof

The stationary one-point equations [1, Eqs. (28)–(30)] give
\[
\Delta T_j=0,\qquad (a-b)\Delta M_j-2UM_j=0\quad(1\le j\le N),
\]
where \(\Delta f_j=f_{j-1}-2f_j+f_{j+1}\). This Dirichlet problem has the unique solution
\[
T_j=t+\delta/2-\delta j/L,\qquad
M_j=m\frac{\sinh(\lambda(j-L/2))}{\sinh(\lambda L/2)}.
\]
In particular \(|M_j|\le m\le T_j\le1\). Substitution yields
\[
J_{A,j}=\tfrac12\left(\frac{(a+b)\delta}{L}-(a-b)(M_{j+1}-M_j)\right),\qquad
M_{j+1}-M_j=\frac{2m\sinh(\lambda/2)\cosh(\lambda(j+1/2-L/2))}{\sinh(\lambda L/2)}.
\]
By symmetry and strict increase of \(\cosh\) on the positive half-line, the two boundary links tie for the largest increment, \(mF_L/L\), and every interior link has strictly smaller increment. For \(N=1\) there are just the two boundary links. Hence the sign of the minimum current is the sign of \(R-F_L\), with strict improvement on every interior link. The telescoping identity
\[
\sum_{j=0}^{N}J_{A,j}=\tfrac12(a-b)m(R-2)
\]
shows that when \(F_L>R\ge2\), the sum of interior currents is strictly positive: the total is nonnegative and both boundary terms are strictly negative. This guarantees an interior positive current, including the case \(R=2\) and \(L>2\). The argument gives no such guarantee for \(R<2\).

With \(c=\lambda/2>0\), the formula extends to real \(L\ge2\) as \(F_L=2L\sinh c\,\cosh((L-1)c)/\sinh(Lc)\). Its logarithmic derivative is
\[
\frac{d}{dL}\log F_L=\frac1L-\frac{c\cosh c}{\sinh(Lc)\cosh((L-1)c)}>0,
\]
since \(\sinh(Lc)>Lc\) and \(\cosh((L-1)c)\ge\cosh c\). Also \(F_2=2\), and \(F_L\sim L(1-z)\) at infinity.

In the exact example the reservoirs have \((\rho^A_0,\rho^B_0)=(1/5,9/20)\) and \((\rho_L^A,\rho_L^B)=(3/10,1/20)\). The imbalance recurrence is \(M_{j+1}-6M_j+M_{j-1}=0\), with \(z=3-2\sqrt2\). Solving it gives the threshold values and currents in the finding.

For illustration of the scope of the last sign statement, take instead \(\delta=1/100\), keeping \(a,b,U,m,t\) as in the example, and take \(N=2\). Then \(R=3/25\), and \(M_1=-m/7\), \(M_2=m/7\). The smallest increment is \(2m/7\), so even the maximal (interior) current is \(\tfrac12(1/200-1/28)=-43/2800<0\). This example has physical reservoirs and \(\rho_L^A>\rho_0^A\).

## Verification

The unchanged supporting `check.py` and `checker_output.txt` concern the numerical example with \(R=18/5\), not a universal assertion of positive interior current when \(F_L>R\). The checker solves the finite recurrence with rational arithmetic through \(N=60\), compares to full stationary Markov one-point means at \(N=1,2,3,4\), and samples the real-length functional. The formulas, cutoff and stated sign regimes follow from the exact argument above.

## Relationship to prior work and limitations

Casini, Giardinà and Vernia [1] construct the model and derive its closed one-point equations. They analyze local uphill current in the continuum equations in Sec. 5 and prove a hydrodynamic limit in Sec. 6. Their work supplies the starting finite-chain closure. The contribution here is the evaluated sharp finite-length sign criterion on **all** links, its strict length monotonicity, and the resulting boundary reversal even with a positive sum of discrete constitutive A-currents. The continuum calculation does not give the exact integer crossing or the signs on the reservoir links. The total-current and boundary-layer results of [2] concern a different two-layer model. This work addresses a symmetric diffusivity matrix and the specified opposing reservoir gradients; it does not classify raw microscopic transfer counts, fluctuations, or general asymmetric parameters. Literature-wide priority is not established.

## References

[1] F. Casini, C. Giardinà and C. Vernia, *Uphill in reaction-diffusion multi-species interacting particles systems*, arXiv:2210.01514v1; DOI 10.1007/s10955-023-03141-3.

[2] S. Floreani, C. Giardinà, F. den Hollander, S. Nandan and F. Redig, *Switching Interacting Particle Systems: Scaling Limits, Uphill Diffusion and Boundary Layer*, *Journal of Statistical Physics* 186, 33 (2022), DOI 10.1007/s10955-022-02878-7.
