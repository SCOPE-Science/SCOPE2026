# Sharp fourth-cumulant rigidity and two-barrier ordering in periodic random walks

## Finding

**Theorem.** Fix an integer \(n\ge3\) and positive edge conductances \(c_0,\ldots,c_{n-1}\), repeated periodically on \(\mathbb Z\). A continuous-time walker at \(x\) jumps to \(x+1\) at rate \(c_{x\bmod n}\) and to \(x-1\) at rate \(c_{(x-1)\bmod n}\). Put \(r_j=c_j^{-1}\) and \(R=\sum_{j=0}^{n-1}r_j\). For \(j=0,\ldots,n-1\), define \(u_j=r_j-R/n\), \(S_j=\sum_{i=0}^{j-1}u_i\), \(\overline S=n^{-1}\sum_jS_j\), and \(E=\sum_j(S_j-\overline S)^2\). The displacement's stationary-independent, long-time cumulant rates satisfy

\[
\kappa_2=\frac{2n}{R},\qquad
\frac{\kappa_4}{\kappa_2}=1+\frac{12nE}{R^2}.
\]

More explicitly, defining \(B=\sum_{0\le i<j<n}r_ir_j(j-i)(n-j+i)\), one has

\[
\kappa_4=\frac{2n^3}{R}-\frac{24nB}{R^3}.
\]

Thus at fixed total edge resistance \(R\), effective diffusion \(D=\kappa_2/2=n/R\) is unchanged by edge order or dispersion, whereas the normalized fourth cumulant satisfies the **sharp all-profile inequality**

\[
1\le\frac{\kappa_4}{\kappa_2}<n^2.
\]

Equality at the lower bound holds **if and only if** all rates are equal. The upper bound is the sharp supremum over all strictly positive conductances, approached when one edge resistance dominates all others; it is never attained by a finite strictly positive profile.

For exactly two identical slow edges with resistances \(1+\delta\) (\(\delta>0\)) and all other resistances one, let \(d\in\{1,\ldots,\lfloor n/2\rfloor\}\) be their shortest circular edge separation. Then

\[
\frac{\kappa_4(d)}{\kappa_2}=1+\frac{4\delta^2}{(n+2\delta)^2}\bigl[n^2-1-3d(n-d)\bigr].
\]

At fixed \(n\) and \(\delta\), this is strictly decreasing in the distinct allowed distances \(d\). Adjacent slow edges maximize \(\kappa_4\); maximally separated slow edges minimize it. For \(n=3\), there is only one allowed separation, so no nontrivial ordering comparison.

## Assumptions and scope

The lattice is the infinite universal cover \(\mathbb Z\) of an \(n\)-cycle; **unwrapped** displacement, not position reduced modulo \(n\), is counted. Every \(c_j\) is a finite strictly positive number. No drift, killing, resetting, or time dependence is present. Rates are symmetric **on each undirected edge**, but may vary between edges. For an arbitrary fixed initial site, \(\kappa_p:=\lim_{t\to\infty}t^{-1}\operatorname{cum}_p(X_t-X_0)\). The limit exists because the tilted finite-state generator has an analytic simple principal eigenvalue near zero; transients do not affect the per-time limit. Both odd cumulant rates through third order vanish; in fact the local principal eigenvalue is even.

The fourth *cumulant rate* is not a fourth central moment and does not claim finite-time Gaussianity. The normalized ratio has time-dimension-free units because lattice steps have length one.

## Proof

**1. Tilted spectral reduction.** On the \(n\) residue classes set

\[
(L_k f)(j)=c_je^k f(j+1)+c_{j-1}e^{-k}f(j-1)-(c_j+c_{j-1})f(j).
\]

Residue indices are modulo \(n\). The analytic eigenvalue \(\lambda(k)\) continuing the simple eigenvalue \(0\) of \(L_0\) is the scaled cumulant-generating function. Let \(C=\prod_jc_j\). In a determinant expansion, a permutation term acquires a nonzero net power of \(e^k\) only by completing a directed circuit around the entire periodic cycle; every other contribution has net exponent zero. Hence, for all \(n\ge3\),

\[
\det(zI-L_k)=\det(zI-L_0)-2C[\cosh(nk)-1]. \tag{1}
\]

The cases \(n=3\) and \(n\ge4\) follow from the same full-winding permutation argument; no multiple-edge convention for \(n=2\) is needed.

**2. Rooted-forest coefficients.** The matrix-tree and all-minors matrix-forest expansions of the cycle Laplacian yield

\[
\frac{\det(zI-L_0)}C=nRz+Bz^2+O(z^3). \tag{2}
\]

Indeed, deleting edge \(i\) yields a spanning tree of weight \(Cr_i\) with \(n\) choices of root, accounting for \(nR\). Deleting two distinct edges \(i<j\) creates components of sizes \(j-i\) and \(n-j+i\); their product counts choices of two component roots and yields the coefficient \(B\). This derivation also verifies that edges are counted exactly once.

Expanding (1)–(2) at \(z=\lambda(k)\) and equating powers gives

\[
\lambda(k)=\frac nR k^2+\left[\frac{n^3}{12R}-\frac{nB}{R^3}\right]k^4+O(k^6).
\]

Taking two and four derivatives at zero gives the two formulas for \(\kappa_2\) and \(\kappa_4\). Equation (1) is even in \(k\), yielding vanishing odd cumulants.

**3. Cyclic resistance-energy identity.** Let \(g(h)=h(n-h)\) for \(h\in\{0,\ldots,n-1\}\), extended periodically. Write \(u_j=r_j-R/n\), so \(\sum_ju_j=0\), and \(H_i=\sum_ju_jg(i-j)\). The cyclic second difference \(\Delta g(h)=g(h+1)-2g(h)+g(h-1)\) satisfies \(\Delta g(h)=-2+2n\mathbf1_{\{h=0\}}\); therefore \(\Delta H_i=2nu_i\). The cyclic first differences obey

\[
H_{i+1}-H_i=2n(S_{i+1}-\overline S),
\]

where \(S_n=S_0=0\). To verify the constant, sum all the first differences over the cycle; the right-hand side sums to zero. The uniform-resistance reference has

\[
B_{\mathrm{unif}}=\frac{n^2-1}{12}R^2,
\]

from the cyclic distance sum. Its mixed term with \(u\) cancels because \(\sum u=0\). Cyclic summation by parts then gives

\[
\begin{aligned}
B_{\mathrm{unif}}-B
&=-\tfrac12\sum_i u_iH_i\\
&=\frac1{4n}\sum_i(H_{i+1}-H_i)^2\\
&=n\sum_i(S_i-\overline S)^2=nE. \tag{3}
\end{aligned}
\]

Insert (3) into the cumulant formula to get the displayed nonnegative exact excess \(12nE/R^2\). Equality implies all \(S_i\) constant and hence all \(u_i=0\), and the converse is immediate.

**4. Sharp upper bound.** As every resistance is positive, \(B>0\) and

\[
\kappa_4/\kappa_2=n^2-12B/R^2<n^2.
\]

Choose \(r_0=M\) and \(r_1=\cdots=r_{n-1}=1\). Then \(B=O(M)\) but \(R^2=\Theta(M^2)\) as \(M\to\infty\), proving that \(n^2\) is the supremum. This limiting profile does not contradict strict positivity for any finite \(M\).

**5. Exactly two identical defects.** Substitute \(r_0=r_d=1+\delta\) and \(r_j=1\) elsewhere into the two-edge formula for \(B\), or into (3), obtaining

\[
B_{\mathrm{unif}}-B=\delta^2\left[\frac{n^2-1}{3}-d(n-d)\right],\qquad R=n+2\delta.
\]

This produces the stated exact normalized fourth cumulant. The function \(d(n-d)\) strictly increases for consecutive integers \(1\le d\le\lfloor n/2\rfloor\), so the extremizers and equality cases follow. Adjacent and diametrically farthest defects are unique up to rotations/reflections.

## Verification

The accompanying `verify.py` implements two independent routes using exact rational arithmetic: formal perturbation through order four of the full tilted generator (including all first- and third-order terms), and the combinatorial rooted-two-forest expression. It checks 42 heterogeneous profiles on sizes \(3\le n\le8\), homogeneous profiles, 90 additional cyclic-energy identities, and 240 exact two-defect formulas with strict separation order. Run `python verify.py` with SymPy installed. The analytic determinant, forest, and summation-by-parts arguments—not these finite enumerations—establish the all-size claims.

## Relationship to prior work

Derrida (1983) derived general-period drift and diffusion for hopping models; Zhang (2009) studied periodic-hopping diffusion limits. Those results account for the harmonic-resistance second cumulant and are not claimed as new. Gerry and Segal (2023) analytically found that the **fourth** cumulant reveals modulation in a two-rate, period-two chain and numerically studied longer modular chains. This establishes the central qualitative sensitivity to structure *before* the present calculation. The current theorem instead gives an exact formula for arbitrary \(n\ge3\) and any positive symmetric bond profile, a sharp global \([1,n^2)\) ratio with equality/supremum classification, and an exact all-distance two-bottleneck arrangement comparison. The period-two special case of the formula is already implied by their analytic calculation and is intentionally excluded from the theorem's stated domain.

Related disordered-walk work discusses fourth-order or modified Burnett coefficients, notably Hernández-García and collaborators (1990). Only its available abstract could be examined; this leaves a residual historical-priority risk for uninspected detailed fourth-order expressions or inequalities. No claim of exhaustive bibliographic uniqueness is made.

## Limitations

There is no extension here to biased hopping, random environments without exact periodicity, higher cumulants, interacting walkers, graph geometries beyond the one-dimensional periodized cycle, or arbitrary joint finite-time displacement laws. The upper constant is a supremum, not a finite strictly-positive-profile maximum. The exact ordering result assumes two identical slow bonds against a uniform baseline; it is not a full global rearrangement theorem for arbitrary inventories. General full-text equivalence with inaccessible historical work is not ruled out.

## References

- B. Derrida, “Velocity and diffusion constant of a periodic one-dimensional hopping model,” *Journal of Statistical Physics* **31**, 433–450 (1983), DOI: 10.1007/BF01019492.
- Y. Zhang, “Limit properties of periodic one dimensional hopping model,” arXiv:0906.3343 (first posted 2009-06-18).
- M. Gerry and D. Segal, “Random walks on modular chains: Detecting structure through statistics,” arXiv:2305.09759 (first posted 2023-05-16).
- L. Beghin, C. Macci, and B. Martinucci, “Random time-changes and asymptotic results for a class of continuous-time Markov chains on integers with alternating rates,” *Modern Stochastics: Theory and Applications* **8**, 63–91 (2021; online 2020), DOI: 10.15559/20-VMSTA169.
- E. Hernández-García et al., “Transport properties for random walks in disordered one-dimensional media,” *Physical Review B* **42**, 10653 (1990), DOI: 10.1103/PhysRevB.42.10653 (abstract compared; full text not verified).
