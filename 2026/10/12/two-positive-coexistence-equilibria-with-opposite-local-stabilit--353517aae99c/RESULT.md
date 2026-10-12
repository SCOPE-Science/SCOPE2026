# Two positive coexistence equilibria with opposite local stability in a stage-specific predator model

## Finding

The full three-species discrete-time exploitative competition map of Seno and Goyal (2026) can possess **two distinct strictly positive fixed points at the same parameter values**, one locally asymptotically stable and the other linearly unstable. More precisely, at \(r=26\), \(a=1/10\), and \(b=3/10\), the map below has one fixed point with prey coordinate \(h\in(49/10,5)\) and all Jacobian eigenvalues strictly inside the unit disk, and another with \(h\in(9,19/2)\) whose Jacobian has a real eigenvalue larger than one. These two fixed points, with their respective stability properties, persist on an open neighborhood of the parameter triple.

This proves **at least two**, not exactly two, coexistence equilibria. It makes no claim of global stability or coexistence of two attracting equilibria.

## Assumptions and scope

For positive prey density \(h\), juvenile-stage predator pressure \(x\), adult-stage predator pressure \(y\), and parameters \(r>1\), \(a,b>0\), consider the original map
\[
(h_+,x_+,y_+)=\left(\frac{rhe^{-x-y}}{1+he^{-y}},\;\frac{arhe^{-y}(1-e^{-x})}{1+he^{-y}},\;bh(1-e^{-y})\right).
\]
The object is the complete three-variable fixed-point system, not the prey-only or either two-species boundary subsystem. The special parameters have single-predator invasion ratios \(\mathcal R_J=a(r-1)=5/2\) and \(\mathcal R_A=b(r-1)=15/2\), satisfying the source's necessary positive-coexistence ordering. The result addresses local discrete-time linear stability in the positive orthant.

## Proof

At any positive fixed point, the first equation implies \(r=e^x(h+e^y)\). Substituting that identity into the other two gives
\[
 ah=\phi(x):=\frac{x}{e^x-1},\qquad bh=\psi(y):=\frac{y}{1-e^{-y}}.
\]
For positive arguments, \(\phi\) decreases strictly from one to zero and \(\psi\) increases strictly from one to infinity, by direct differentiation and \(e^t>1+t\) for \(t\ne0\). Consequently the parameterized positive fixed-point locus is defined uniquely by continuous functions \(x=x(h)>0\) and \(y=y(h)>0\) for \(1/b<h<1/a\). For the specified \(a,b\), this is \(10/3<h<10\). A positive fixed point is therefore equivalent to \(F(h)=r\), where
\[
 F(h):=e^{x(h)}\bigl(h+e^{y(h)}\bigr).
\]

The included rational-arithmetic checker proves the four strict comparisons
\[
 F(49/10)>26>F(5),\qquad F(9)<26<F(19/2).
\]
Continuity gives distinct positive fixed points in the disjoint intervals \((49/10,5)\) and \((9,19/2)\). The proof of the comparisons is not floating-point sampling: `verify.py` uses monotonicity to bracket the implicit roots of \(\phi(x)=ah\), \(\psi(y)=bh\) by rational bisection, bounds exponentials by 70-term rational Taylor sums with explicit geometric remainder bounds, and checks all signs by exact fractions.

Write \(D=1+he^{-y}\) at either fixed point. Direct differentiation of all three original recurrence equations, then substitution of the fixed-point identities, yields the exact full-system Jacobian
\[
 J=\begin{pmatrix}
 D^{-1}&-h&-hD^{-1}\\
 x/(hD)&ah&-xD^{-1}\\
 y/h&0&bhe^{-y}
 \end{pmatrix}.
\]
Let \(\det(\lambda I-J)=\lambda^3+c_1\lambda^2+c_2\lambda+c_3\). For a real monic cubic the strict Schur/Jury conditions are
\[
 1+c_1+c_2+c_3>0,\quad1-c_1+c_2-c_3>0,\quad1-c_2+c_1c_3-c_3^2>0,\quad 1+c_3>0,\quad1-c_3>0.
\]
On the first branch the same exact-rational interval calculation encloses the five left sides, respectively, within the disjoint positive decimal intervals \((0.06469796,0.06469802)\), \((4.66663570,4.66663576)\), \((0.14403432,0.14403441)\), \((0.14898069,0.14898073)\), and \((1.85101927,1.85101932)\). Decimal bounds are outward rounded representations of rational inequalities checked by the code, not inputs to its computation. Thus all three multipliers have modulus less than one.

On the second branch the same exact interval calculation gives
\[
 -0.02071010<\det(I-J)<-0.02071004.
\]
The real monic characteristic polynomial is negative at \(\lambda=1\) and tends to positive infinity as \(\lambda\to+\infty\), so it has a real root \(\lambda>1\). The second fixed point is linearly unstable.

Both computed determinants \(\det(I-J)\) are nonzero (positive at the first branch, negative at the second). Applying the implicit-function theorem to the smooth fixed-point equations therefore continues each equilibrium separately to a neighborhood of the parameter triple. Strict Schur stability and the strict real-multiplier instability condition are open properties. Shrinking the parameter neighborhood if necessary preserves positivity, separation, and the opposite local stability properties.

## Verification

Run `python verify.py` from the directory containing this document. It requires only the Python standard library and uses `fractions.Fraction` throughout its inequality checks. Its terminal status is `VERIFY_OK`. Certified prey enclosures are approximately \(4.98708530664<h<4.98708531857\) for the stable equilibrium and \(9.35663866997<h<9.35663872957\) for the unstable one. The proof relies on the analytical monotonicity and continuity arguments, the exact fixed-point Jacobian, the Schur/Jury criterion, and rational sign certificates; numerical approximations alone would not be a proof.

## Relationship to prior work

Seno and Goyal (2026, Eq. (27) and Appendix I) formulate this three-dimensional map, identify necessary conditions for full coexistence, and analyze boundary equilibria and numerical behaviors. Their positive-boundary equilibrium uniqueness arguments do not imply uniqueness of the full three-species equilibrium. Their Appendix I fixed-point reduction agrees with the identities above, but does not establish the two distinct strictly positive fixed points and their contrasting local spectra for the parameter triple used here. Earlier multi-parasitoid and stage-specific coexistence literature addresses related ecological mechanisms; qualitative coexistence and parameter-dependent multiplicity in different models do not imply this exact full-map construction. The claim is limited to the specific published map and its nearby parameters.

## Limitations

No upper bound on the number of positive equilibria is proved; there may be additional fixed points. Only local asymptotic stability of one branch and linear instability of a second branch are established; a stable and an unstable fixed point do not demonstrate bistability. No global basin, period, collision, ecological inference, or statistical estimation result is claimed. Published article text is the mathematical source, and the computational component verifies only the explicitly documented finite collection of rational inequalities.

## References

Seno, H., and Goyal, A. (2026), *Discrete-time exploitative competition model of different stage-specific predators*, Journal of Mathematical Biology 93, Article 11, https://doi.org/10.1007/s00285-026-02427-w. Public article date: July 3, 2026.

May, R. M., and Hassell, M. P. (1981), *The dynamics of multiparasitoid-host interactions*, American Naturalist, https://doi.org/10.1086/283704 (contextual comparison only; full article not independently inspected here).

Hackett-Jones, E., Cobbold, C., and White, A. (2009), *Coexistence of multiple parasitoids on a single host due to differences in parasitoid phenology*, Theoretical Ecology, https://doi.org/10.1007/s12080-008-0025-1 (contextual comparison; abstract examined).
