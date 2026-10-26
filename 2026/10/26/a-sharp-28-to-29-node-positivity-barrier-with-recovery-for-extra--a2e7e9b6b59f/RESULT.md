# A sharp 28-to-29 node positivity barrier with recovery for extrapolated backward Euler on complete graphs

## Finding
For the unweighted complete graph \(K_n\), the two-level second-order Richardson extrapolate of backward Euler is a stochastic, entrywise nonnegative time-step matrix for **every** nonnegative step size precisely when \(2\le n\le28\). From \(n=29\) onward the method has an exact bounded **negative-diagonal window**, followed by **recovery of entrywise nonnegativity** for sufficiently large steps.

For \(n\ge29\), let \(\alpha_n<\beta_n\) denote the two positive roots of
\[
H_n(x)=x^3+(6-n)x^2+(4n+4)x+4n.
\]
The full timestep classification is
\[
T_n(h)\ge0\ \text{entrywise}
\iff
h\in[0,\alpha_n/n]\cup[\beta_n/n,\infty).
\]
At intermediate steps \(\alpha_n/n<h<\beta_n/n\), **all** diagonal entries are strictly negative while all off-diagonal entries remain strictly positive. In the first failing case \(n=29\), the two positive dimensionless endpoints are approximately \(10.4352065911560\) and \(13.3946905220462\).

## Assumptions and scope
Fix an integer \(n\ge2\). Set \(J=\mathbf 1\mathbf 1^{\mathsf T}\) and \(L_n=nI-J\), the graph Laplacian of \(K_n\) when each undirected edge has unit conductance. Consider exact integration of the linear Markov/diffusion equation \(u'(t)=-L_nu(t)\). For real \(h\ge0\), one backward-Euler step is \((I+hL_n)^{-1}\), and two backward-Euler half steps yield \((I+hL_n/2)^{-2}\). Their standard Richardson combination is
\[
T_n(h)=2(I+hL_n/2)^{-2}-(I+hL_n)^{-1}.
\]
The conclusion concerns entrywise matrix positivity and preservation of all nonnegative vectors, not scalar decay-mode positivity and not positivity of intermediate extrapolation tableaux. All inverses exist for \(h\ge0\). There are no upper bounds on \(n\) or on \(h\).

## Proof
Let \(P_0=J/n\) and \(P_\perp=I-J/n\). They are complementary orthogonal projectors, and \(L_n=nP_\perp\). Thus
\[
T_n(h)=P_0+R(x)P_\perp,\qquad x=nh,
\quad R(x)=\frac{2}{(1+x/2)^2}-\frac1{1+x}
=\frac{-x^2+4x+4}{(x+2)^2(x+1)}.
\]
Since \(R(0)=1\) and \(R(x)=1-x+x^2/2+O(x^3)\), the method is second order and fixes the constant mode. In particular, \(T_n(h)\mathbf1=\mathbf1\), so the row sums are one.

Every off-diagonal element is exactly
\[
(T_n(h))_{ij} =\frac{1-R(x)}{n}
=\frac{x(x^2+6x+4)}{n(x+2)^2(x+1)} \quad(i\ne j).
\]
It is zero only at \(h=0\) and strictly positive for \(h>0\). Every diagonal element is
\[
(T_n(h))_{ii}=\frac{1+(n-1)R(x)}n
=\frac{H_n(x)}{n(x+2)^2(x+1)},
\qquad
H_n(x)=x^3+(6-n)x^2+(4n+4)x+4n.
\]
The denominator is positive, so matrix nonnegativity is equivalent to \(H_n(x)\ge0\) for \(x\ge0\).

For \(0\le x\le 2+2\sqrt2\), the numerator of \(R(x)\) is nonnegative; hence the diagonal is positive for every \(n\ge2\). For \(x>2+2\sqrt2\), \(R(x)<0\), so the diagonal \([1+(n-1)R(x)]/n\) is smallest in sign when \(n\) increases. It therefore suffices to establish \(H_{28}(x)>0\) for every \(x\ge0\). The useful exact identity is
\[
H_{28}(x)=x(x-11)^2-5x+112.
\]
For \(0\le x\le22\) this is at least \(112-5x\ge2>0\); for \(x\ge22\), \((x-11)^2\ge121>5\), so it is again strictly positive. Thus all dimensions \(2\le n\le28\) preserve positivity at every step.

For every \(n\ge29\), evaluation at one dimensionless step gives
\[
H_n(12)=2640-92n<0,
\qquad H_n(0)=4n>0,
\qquad\lim_{x\to\infty}H_n(x)=+\infty.
\]
By continuity there is at least one positive root on each side of \(12\). The nonzero coefficients of \(H_n\) have sign pattern \(+,-,+,+\), with exactly two sign changes, for every \(n\ge29\). Descartes' rule of signs gives **at most** two positive roots, counted with multiplicity. Therefore there are exactly two distinct and simple positive roots \(0<\alpha_n<12<\beta_n\). Since the leading coefficient is positive, \(H_n\) is negative only between those roots and nonnegative outside. The displayed complete nonnegativity classification follows for all \(h\ge0\).

## Verification
A standalone exact-arithmetic checker, `verify.py`, reconstructs the scalar rational function and the diagonal cubic symbolically, checks the dimension-28 positive decomposition and the dimension-29 negative witness, and independently forms complete resolvent matrices for seven graph orders and three dimensionless steps per order. The run returned `VERIFY_OK symbolic identities=4 exact full-matrix cases=21 orders=7`. The proof for all dimensions and all real step sizes relies on the projector identity, positivity decomposition, and root-count argument rather than those finite tests. Run with `python verify.py` using Python 3 and SymPy as specified in `requirements.txt`.

## Relationship to prior work
Constantinescu and Sandu (2008 technical report, subsequently published in 2010) construct and analyze extrapolated Euler-based time steppers. Their two-level Aitken–Neville formula gives the Richardson combination here; this construction and second-order accuracy are **prior work**. Their inspected technical report discusses extrapolation, accuracy and linear stability, not an explicit node-count classification for nonnegative complete-graph Markov steps.

The publicly available result *Richardson acceleration creates a sharp positivity barrier for backward Euler* establishes that for two half-steps the scalar amplification \(R(x)\) becomes negative beyond \(x=2+2\sqrt2\). That result is **not** a graph-matrix positivity theorem. On \(K_n\), the relevant diagonal is \([1+(n-1)R(x)]/n\), which can stay nonnegative even when the decay-mode amplification is negative. The present sharp threshold at 29 and the exact two-interval positivity set follow from the graph's projectors and a nontrivial cubic sign classification. Other published work studies Crank–Nicolson and Padé positivity mechanisms for distinct rational propagators, not this extrapolated backward-Euler complete-graph classification.

## Limitations
The theorem applies only to the unweighted complete-graph Laplacian and the displayed second-order two-level Richardson formula. It does **not** assert universal positivity for all graphs with at most 28 vertices; arbitrary Markov generators can have different eigenprojectors and behavior. Likewise it does not classify variants with more Richardson levels, unequal extrapolation coefficients, or floating-point rounding. The argument is exact and does not establish anything about nonlinear strong-stability preservation. Full independent mathematical review has not been performed. Unindexed papers or alternate terminology could conceal overlapping coverage.

## References
1. E. M. Constantinescu and A. Sandu, *Achieving Very High Order for Implicit Explicit Time Stepping: Extrapolation Methods*, Virginia Tech Computer Science Technical Report TR-08-13, dated 18 July 2008. https://eprints.cs.vt.edu/archive/00001037/01/ExImex.pdf
2. E. M. Constantinescu and A. Sandu, *Extrapolated Implicit-Explicit Time Stepping*, SIAM Journal on Scientific Computing 31 (2010), 4452–4477, DOI: 10.1137/080732833.
3. *Richardson acceleration creates a sharp positivity barrier for backward Euler*, publicly available mathematical note, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-richardson-acceleration-creates-a-sharp-positivity-barrier-for-b--c9c2b9f6d7e1.
4. *A resolvent-return law for Crank–Nicolson positivity on reversible Markov chains*, publicly available mathematical note, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-a-resolvent-return-law-for-crank-nicolson-positivity-on-reversib--d475df91cd2a.
