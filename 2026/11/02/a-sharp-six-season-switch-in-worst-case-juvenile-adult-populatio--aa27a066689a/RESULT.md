# A sharp six-season switch in worst-case juvenile–adult population growth

## Finding

A two-stage population with a fixed inventory of six fertility seasons can have a **parameter-dependent worst ordering**, even though the best ordering never changes. The first possible such reversal occurs at six seasons, and its threshold is exact.

Let the six fertility levels be \(f_j=a+jd\), for \(j=1,\ldots,6\), with \(a\geq0\) and \(d>0\). Let juvenile maturation probability satisfy \(0<s\leq1\), and adult survival probability satisfy \(0<p<1\). The population projection in fertility season \(j\) is
\[
M_j=\begin{pmatrix}0&f_j\\s&p\end{pmatrix}.
\]
For a permutation \(\pi=(\pi_1,\ldots,\pi_6)\), repeat the calendar indefinitely, and write \(P_\pi=M_{\pi_6}\cdots M_{\pi_1}\). Its asymptotic per-season growth factor is \(G_\pi=\rho(P_\pi)^{1/6}\).

Define the three calendars
\[
A=(1,2,4,6,5,3),\qquad B=(1,2,4,5,6,3),\qquad C=(1,5,3,4,2,6),
\]
and the dimensionless maturation-to-persistence ratio \(\chi=sd/p^2\). Among **all** \(6!\) permutations, the smallest growth factor is uniquely attained by the cyclic-rotation/reversal class of \(A\) when \(\chi<1/2\), by that of \(B\) when \(\chi>1/2\), and by exactly both classes when \(\chi=1/2\). The largest growth factor is always uniquely attained by the cyclic-rotation/reversal class of \(C\). Thus the sharp crossover is \(sd=p^2/2\), independent of \(a\).

The length six is minimal for any reversal of a pairwise ranking caused by changing the common positive maturation and adult-survival parameters with fixed positive fertility levels. For every period of length at most five, any two calendar growth factors have a parameter-independent order (possibly equal), so no such reversal occurs.

## Assumptions and scope

This is a deterministic, density-independent, two-stage juvenile–adult population. Every season has the same juvenile-to-adult maturation probability \(s\) and adult carryover probability \(p\), and seasons differ only in adult fertility \(f_j\). A fixed multiset of six equally spaced, strictly positive fertility rates is permuted and then repeated. Both growth extrema concern the spectral radius of one complete six-season monodromy, rather than within-cycle transient abundance, a finite-time endpoint for arbitrary initial age structures, or growth under stochastic calendars. Here equivalence under cyclic rotation and reversal is used only for the **spectral radius**; transient trajectories need not be equivalent.

## Proof

**1. Trace reduction.** Every matrix has determinant \(\det M_j=-sf_j\). Hence all six-calendar monodromies have the same strictly positive determinant \(\Delta=s^6\prod_{j=1}^{6}f_j\). Every such product is a strictly positive matrix. For a fixed \(\Delta\), its Perron eigenvalue
\[
\lambda_+(T)=\frac{T+\sqrt{T^2-4\Delta}}2
\]
is strictly increasing in its trace \(T>2\sqrt\Delta\). Therefore ranking the traces ranks all asymptotic growth factors.

**2. Cyclic matching expansion.** Expansion of the trace as a sum of closed two-state paths gives a weighted matching polynomial of the six-cycle. A season not covered by a dimer contributes adult persistence \(p\), while an occupied dimer contributes \(sf_j\); dimers cannot overlap. For the circular word \((i,j,k,l,m,n)\), introduce
\[
\begin{aligned}
B&=ik+il+im+jl+jm+jn+km+kn+ln,\\
H&=ik+im+km+jl+jn+ln,\\
C&=ikm+jln.
\end{aligned}
\]
These are integer statistics of the six rank labels, not parameters of the biological model. Expansion at \(f_j=a+jd\) yields the exact polynomial
\[
\begin{aligned}
T_\pi={}&p^6+sp^4(6a+21d)\\
&+s^2p^2(9a^2+63ad+d^2B_\pi)\\
&+s^3(2a^3+21a^2d+ad^2H_\pi+d^3C_\pi).
\end{aligned}
\]
Cyclic rotation and reversal preserve the weighted cycle-matching polynomial, so these operations leave \(T_\pi\) unchanged.

**3. Complete finite extremal classification.** A full enumeration of all \(720\) labeled words, quotienting by the dihedral symmetries into exactly \(60\) size-\(12\) orbits, gives the following exact global bounds:
\[
93\le B_\pi\le117,\qquad65\le H_\pi\le85,\qquad54\le C_\pi\le126.
\]
The only dihedral orbit with \(B_\pi=93\) is the orbit of \(A\); the only orbit with \(B_\pi=117\) is the orbit of \(C\). The values for the three designated representatives are
\[
(B_A,H_A,C_A)=(93,65,56),\quad
(B_B,H_B,C_B)=(94,65,54),\quad
(B_C,H_C,C_C)=(117,85,126).
\]
Among all calendars other than \(A\)'s orbit, the only one simultaneously attaining \(B_\pi=94\) and \(C_\pi=54\) is \(B\)'s orbit. As \(H_\pi\ge65\), \(C_\pi\ge54\), and every non-\(A\) orbit has \(B_\pi\ge94\), the trace of \(B\) is strictly below that of every orbit except possibly \(A\). All three \(B,H,C\) statistics are simultaneously maximized only by \(C\), making it the unique maximizing orbit for all admissible parameters. The accompanying CSV enumerates **every** orbit and its statistics, and the standalone checker verifies the complete enumeration by independent exact integer computations rather than sampling parameters.

**4. Sharp crossover.** Substituting the \(A\) and \(B\) statistics into the trace gives
\[
T_A-T_B=s^2p^2d^2(-1+2sd/p^2).
\]
Every prefactor is positive. The sign changes precisely at \(\chi=1/2\), giving the claimed unique minima on either side and exactly two minimizing classes at equality.

**5. Minimal calendar length.** For any cyclic calendar with at most five seasons, the matching expansion has at most two dimers. Its degree-two term is \(s^2p^{n-4}\) times the sum of products of nonadjacent fertility levels when \(n\ge4\); all other terms depend only on the fertility multiset, not its ordering. Hence the sign of the trace difference of any two calendars cannot change as the common positive \(s,p\) vary. For \(n\le3\) every trace is order-independent. Each calendar product has fixed determinant under reordering, and its Perron eigenvalue increases with trace, establishing the no-reversal assertion. The six-season pair \(A,B\) supplies the first counterexample.

## Verification

The standalone `check_six_season.py` generates all \(720\) permutations and \(60\) dihedral orbits, independently recomputes the cycle statistics, checks the full `orbit_certificate.csv`, verifies all stated unique extrema, and evaluates both the direct rational-matrix product and the stated trace polynomial for all permutations under four rational parameter choices. It checks the sharp crossover both above, below and at equality and tests the absence of reversals at periods two through five in exact examples. The analytical cycle-matching expansion proves the all-real-parameter result; finite checks verify a **complete finite** enumeration rather than substituting sampled parameter values for an infinite-domain proof.

For instance, with \(a=d=1\), \(p=1/2\), and respectively \(s=1/16,1/8,1/4\), the ratios \(\chi\) are \(1/4,1/2,1\). The exact traces of \(A\) and \(B\) change their order: at \(s=1/16\), \(T_A=325/1024<T_B=651/2048\); at \(s=1/8\), \(T_A=T_B=295/256\); at \(s=1/4\), \(T_B=21/4<T_A=337/64\). In each case \(C\) is the unique maximizing orbit.

## Relationship to prior work

Periodic population matrices and their cyclic reorderings are standard. Mertens and colleagues (first publicly published September 1, 2006) analyze transient sensitivity and starting-phase effects under cyclic permutations. Here the comparison is instead **between arbitrary reorderings** of a fixed fertility inventory, based on asymptotic growth, and includes a complete six-season classification and parameter-switch boundary. Cushing and Ackleh develop periodic matrix reproduction numbers, and Caswell's periodic matrix sensitivity framework addresses general products rather than this exact rearrangement. Key and Volkmer obtain bounds on products of companion matrices, not the fixed-inventory permutation extremizers. De Luca and Zamboni analyze related cyclic continuant rearrangements, but their ordinary/semiregular continuants do not state this fertility-weighted two-stage monodromy crossover. This is a claim of distinction from the material actually inspected, not a guarantee that the result is absent from all historical mathematical or population-model literature.

## Limitations

The conclusion requires exactly six distinct fertility levels in arithmetic progression for the explicit extremizers, shared survival parameters, and deterministic repeating calendars. It does not apply without proof to arbitrary fertility multisets, nonlinear density dependence, harvesting, stochastic environments, or transient abundance. A complete priority review of the original 2006 periodic-matrix article and all generalized continuant literature was not possible; historical originality remains provisional. No independent scientific validation has been performed.

## References

- Mertens, S. K., Yearsley, J. M., van den Bosch, F., and Gilligan, C. A. (2006), *Transient population dynamics in periodic matrix models: Methodology and effects of cyclic permutations*, *Ecology* 87:2338–2348. DOI: 10.1890/0012-9658(2006)87[2338:TPDIPM]2.0.CO;2. First published 2006-09-01.
- Cushing, J. M., and Ackleh, A. S. (2011), *A net reproductive number for periodic matrix models*, *Journal of Biological Dynamics*. DOI: 10.1080/17513758.2010.544410.
- Key, E. S., and Volkmer, H. (2014), *A note on the spectral radius of a product of companion matrices*. DOI: 10.13001/1081-3810.2862.
- Caswell, H. (2019), *Periodic Models*, in *Sensitivity Analysis: Matrix Methods in Demography and Ecology*, Chapter 8. DOI: 10.1007/978-3-030-10534-1_8.
- De Luca, A., and Zamboni, L. Q. (2021), *On the extremal values of the cyclic continuants of Motzkin and Straus*. arXiv:2108.11313.
