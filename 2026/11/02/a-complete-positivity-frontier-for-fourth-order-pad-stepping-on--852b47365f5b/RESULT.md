# A complete positivity frontier for fourth-order Padé stepping on weighted three-spoke stars

## Finding
Let a four-vertex star have center vertex \(0\), leaf vertices \(1,2,3\), and strictly positive edge conductances \(a_1,a_2,a_3\). Define its weighted graph Laplacian \(L\) and the fourth-order diagonal Padé end-step matrix
\[
P(h)=\left(I+\frac h2 L+\frac{h^2}{12}L^2\right)^{-1}
\left(I-\frac h2 L+\frac{h^2}{12}L^2\right),\qquad h\ge0.
\]
Then **\(P(h)\) is entrywise nonnegative for every \(h\ge0\)** if and only if
\[
\boxed{\frac4{a_i}\ge \frac1{a_1}+\frac1{a_2}+\frac1{a_3}\quad(i=1,2,3).}
\]
These inequalities are sharp. If any one fails, at least one center-to-leaf entry crosses zero exactly once at a finite positive step and stays strictly negative thereafter. More generally, **for every choice of positive conductances, the entire set of steps at which \(P(h)\) is entrywise nonnegative is one closed interval \([0,H]\), where \(0<H\le\infty\)**. The endpoint \(H\) is completely determined by the explicit quartic and cubic polynomials below. Thus this four-state conservative system has no disconnected or re-entrant positivity windows, despite the higher-order method's lack of unconditional positivity for unrestricted systems.

## Assumptions and scope
All matrices are real and exact. The star has exactly three leaves, there are no other edges, each \(a_i>0\), and there is no artificial killing or boundary mass loss. The matrix convention is \(L_{00}=\sum_i a_i\), \(L_{ii}=a_i\), \(L_{0i}=L_{i0}=-a_i\), and all other off-diagonal entries vanish. The parameter \(h\) is a nonnegative real number. The map is the end-step stability function of the two-stage Gauss--Legendre Runge--Kutta method, not a statement about its internal stage signs.

For distinct leaf indices \(i,j,k\), abbreviate \(x=a_i\), \(y=a_j\), \(z=a_k\), and put
\[
D(h)=I+\frac h2 L+\frac{h^2}{12}L^2,\qquad \Delta(h)=432\det D(h)>0.
\]
Introduce the real polynomials
\[
\begin{aligned}
\Phi_i(h)={}&yz[3yz-x(y+z)]h^4+12yz(y+z-x)h^3\\
 &+12[2y^2+3yz+2z^2-x(y+z)]h^2\\
 &+72(y+z)h+144,\\
\Psi_{ij}(h)={}&z[3z(x+y)-xy]h^3\\
 &+12z(x+y+z)h^2+24(x+y+2z)h+72.
\end{aligned}
\]
The expressions are symmetric in the unspecified other leaf indices. For \(h>0\), define \(T_i\) to be the unique positive root of \(\Phi_i\), if it exists, and \(\infty\) otherwise. Define \(U_{ij}\) analogously for \(\Psi_{ij}\). The exact global positivity horizon is
\[
\boxed{H=\min\{T_1,T_2,T_3,U_{12},U_{13},U_{23}\}.}
\]
Every finite root appearing in this formula is unique and can be found by monotone-sign bracketing; no root-selection ambiguity occurs. The convention is \(\min\varnothing=\infty\).

## Proof
**1. Well-definedness, row sums, and diagonals.** The eigenvalues of \(L\) are nonnegative. The scalar denominator \(1+s/2+s^2/12\) is positive for \(s\ge0\), so \(D(h)\) is symmetric positive definite, whence \(\Delta(h)>0\). On each Laplacian eigenmode the update has eigenvalue
\[
 r(s)=\frac{1-s/2+s^2/12}{1+s/2+s^2/12}
 =\frac{(s-3)^2+3}{(s+3)^2+3}>0\quad(s\ge0).
\]
Thus \(P(h)\) is positive definite, in particular all its diagonal entries are strictly positive. Since \(L\mathbf1=0\), \(P(h)\mathbf1=\mathbf1\): the only possible obstruction to stochasticity is an off-diagonal sign.

**2. Exact entries.** Direct multiplication of \(D(h)P(h)=I-hL/2+h^2L^2/12\), or a fraction-free adjugate calculation, yields the six off-diagonal identities
\[
\boxed{P_{0i}(h)=\frac{3xh\Phi_i(h)}{\Delta(h)},\qquad
P_{ij}(h)=\frac{3xyh^2\Psi_{ij}(h)}{\Delta(h)}.}
\]
The accompanying verification script establishes these as symbolic identities in the independent indeterminates \(a_1,a_2,a_3,h\), rather than only for sample values. Since denominators and non-polynomial factors are positive at \(h>0\), these polynomial signs decide every off-diagonal entry exactly.

**3. A unique crossing for each entry.** Only the highest coefficient of \(\Psi_{ij}\) can be nonpositive; its remaining coefficients are strictly positive. If \(xy>3z(x+y)\), Descartes' rule of signs and opposite endpoint signs give exactly one positive zero, with positivity before and negativity after. Otherwise \(\Psi_{ij}(h)>0\) for every finite positive \(h\).

For \(\Phi_i\), hold \(y,z>0\) fixed and increase \(x\). Its coefficient of \(h^4\) changes from positive to negative at \(x=3yz/(y+z)\), its coefficient of \(h^3\) at \(x=y+z\), and its coefficient of \(h^2\) at \(x=(2y^2+3yz+2z^2)/(y+z)\). These critical values satisfy
\[
\frac{3yz}{y+z}\le\frac34(y+z)<y+z<\frac{2y^2+3yz+2z^2}{y+z}.
\]
The coefficients of \(h\) and the constant coefficient are always strictly positive. Consequently the nonzero coefficient signs, read in descending powers of \(h\), have either no sign change or exactly one. If \(3yz-x(y+z)<0\), the leading coefficient is negative and exactly one positive zero follows by Descartes and continuity; if it is nonnegative, all coefficients are nonnegative and no positive zero exists. The same positivity-before/negativity-after description applies. Therefore the intersection of six off-diagonal nonnegativity intervals is exactly \([0,H]\).

**4. The unconditional criterion.** By the preceding paragraph, every center-leaf entry remains nonnegative for all steps exactly when
\[
3a_ja_k\ge a_i(a_j+a_k)\quad(i=1,2,3).
\]
Multiplying by the positive product \(a_1a_2a_3\) shows these are exactly the boxed reciprocal-conductance inequalities. They also force every leaf-leaf polynomial's highest coefficient to be positive: for example, \(a_i(a_j+a_k)\le 3a_ja_k\) implies \(a_ia_j<3a_k(a_i+a_j)\). Thus all six entries stay nonnegative. Conversely, failure of even one reciprocal inequality gives a center-leaf polynomial with negative leading coefficient and therefore a finite positivity horizon. This proves necessity and sufficiency.

**5. Sharp critical asymptotics.** Write \(G_i=3a_ja_k-a_i(a_j+a_k)\). Since the leading term of \(\Delta(h)\) is \(4a_1^2a_2^2a_3^2h^6\), when \(G_i\ne0\),
\[
P_{0i}(h)=\frac{3G_i}{4a_1a_2a_3}\frac1h+O(h^{-2}).
\]
On the sharp boundary \(G_i=0\), the leading term vanishes, but \(a_j+a_k-a_i>0\) and
\[
\boxed{P_{0i}(h)=\frac{9(a_j+a_k-a_i)}{a_1a_2a_3}\frac1{h^2}+O(h^{-3}).}
\]
Equivalently, with \(r_i=1/a_i\) and Laplacian Moore--Penrose inverse \(L^+\), the effective-resistance identity for a star gives \((L^+)_{0i}=(\sum_jr_j-4r_i)/16\). The leading large-step sign is therefore \(-\operatorname{sgn}(L^+_{0i})\), in agreement with \(P(h)=I-12L^+/h+O(h^{-2})\) off the constant mode. These asymptotic statements concern fixed positive conductances and \(h\to\infty\).

## Verification
The standalone file `verify_pade_star.py` uses exact SymPy arithmetic to check the row-sum identity and symmetry, all six rational off-diagonal formulas, the critical boundary coefficient, and the following exact example. It additionally performs 540 direct full-matrix, row-sum and spectral comparisons over heterogeneous positive conductances and step sizes. Its deterministic run printed all checks passed. Only the algebraic proof above, not random tests, establishes the statements for all conductances and steps.

For \((a_1,a_2,a_3)=(3,1,1)\), the unique nontrivial crossing is the center-to-first-leaf entry:
\[
\Phi_1(h)=-3(h^2-2h-4)(h^2+6h+12),\qquad H=1+\sqrt5.
\]
All other off-diagonal entries remain strictly positive for \(h>0\). Hence \(P(h)\) is stochastic exactly for \(0\le h\le1+\sqrt5\), and develops a negative transition coefficient for every greater step.

For \((a_1,a_2,a_3)=(3/2,1,1)\), all steps remain stochastic and the critical center-to-first-leaf entry is asymptotic to \(3/h^2\).

## Relationship to prior work
Zappavigna, Colaneri, Kirkland and Shorten (2010) give general step-size sufficient conditions for positivity of higher diagonal Padé transforms on Metzler systems. Their later paper (2012) gives explicit non-positivity counterexamples, including a nonconservative eight-state nilpotent chain. Those results motivate, but do not contain, the exact all-step three-spoke-star conductance region and the finite-horizon classification here. A published mathematical record on the conservative eight-state Padé barrier establishes a different small-step dimension obstruction and an unusual disconnected positivity window on a directed pure-birth generator; it does not address these reversible four-state stars. The present analysis treats the exact rational method, an explicitly parameterized natural graph family, and the sign of *every* off-diagonal entry.

## Limitations
The classification concerns the symmetric four-vertex three-spoke star only. No general arbitrary-star or arbitrary-graph theorem follows from the argument, and the numerical tests cannot be extrapolated to such families. Entrywise positivity of the end-step is distinct from internal-stage positivity, error bounds, monotone decay in every norm, and positivity in floating-point arithmetic. Literature coverage cannot be asserted exhaustive; specialized prior results on Padé sign patterns for small weighted graphs remain a residual originality risk.

## References
1. A. Zappavigna, P. Colaneri, S. Kirkland, R. Shorten, *On the preservation of co-positive Lyapunov functions under Padé discretization for positive systems*, MTNS (2010). Public copy: https://mural.maynoothuniversity.ie/id/eprint/2195/ (repository first deposited October 15, 2010).
2. A. Zappavigna, P. Colaneri, S. Kirkland, R. Shorten, *Essentially Negative News About Positive Systems*, Linear Algebra and its Applications 436 (2012), 3425–3442. Open author manuscript: https://mural.maynoothuniversity.ie/id/eprint/3761/ .
3. *Eight-state barrier for Markov positivity of the [2/2] Padé map*, public mathematical research record (2026): https://github.com/Resultary/2026/tree/main/2026/9/20/SCOPE-eight-state-pade-markov-positivity-barrier--4aad2a3f58ab .
