# No switching or smoothed-treatment cycles under an exact Dulac threshold

## Finding

Consider the tumor--immune flow with a tumor-activated treatment response
\[
\dot x=cy-(1+\beta y)x+s h(y),\qquad
\dot y=ry\left(1-y-\frac{\alpha x}{1+\varepsilon y}\right)-qyh(y).
\]
For any positive \(c,\beta,r,\alpha,\varepsilon,s,q\), put
\[
a=\varepsilon(\beta+2r),\qquad b=\beta+\varepsilon+r(1-\varepsilon).
\]
**Theorem.** If \(b+2\sqrt a\ge0\), then the following statements hold simultaneously:

* For every \(C^1\), nondecreasing \(h:(0,\infty)\to[0,1]\), the system has no nonconstant periodic orbit in the strictly positive quadrant.
* For every threshold \(T_c>0\), the Filippov system obtained by taking \(h(y)=\mathbf 1_{\{y>T_c\}}\) has no nonconstant simple, piecewise-regular periodic orbit in the strictly positive quadrant, whether crossing or containing an attracting sliding segment.

This includes every \(0<\varepsilon\le1\), with no restrictions on the threshold, immune stimulation \(s\), suppression \(q\), or the positive values of \(c\) and \(\alpha\). The bound is sufficient, not asserted to be the actual existence boundary for oscillations.

## Assumptions and scope

Both state variables are strictly positive, all seven named parameters are strictly positive, and solutions are interpreted classically for smooth activation and in the Filippov sense for the step activation. A piecewise-regular Filippov cycle is a simple closed curve composed of finitely many ordinary trajectory arcs, transversal crossing points, and possibly sliding arcs, with isolated tangent endpoints allowed. These include the standard crossing and sliding limit cycles considered in the motivating work. For \(C^1\) activation, nondecreasing means \(h'(y)\ge0\) for every \(y>0\). The threshold case has two vector fields \(F_-\) below \(y=T_c\) and \(F_+\) above it.

## Proof

**1. An exact quadratic criterion.** Set \(P(y)=ay^2+by+1\), with \(a>0\). If \(b\ge0\), then \(P(y)>0\) for every \(y>0\). Otherwise, its minimum on the positive half-line is \(1-b^2/(4a)\). Thus \(b+2\sqrt a\ge0\) is exactly the condition that \(P(y)\ge0\) for all \(y>0\). At equality, the only zero is the single positive value \(y=-b/(2a)\), hence a horizontal line of two-dimensional measure zero.

**2. Smooth monotone activation.** The positive multiplier
\[
B(x,y)=\frac{1+\varepsilon y}{ry}
\]
has weighted divergence
\[
\nabla\cdot(BF_h)
=-\frac{P(y)}{ry}
-\frac q r\Bigl(\varepsilon h(y)+(1+\varepsilon y)h'(y)\Bigr).
\]
The treatment recruitment \(s h(y)\) vanishes from this divergence because it has no \(x\)-dependence. Both displayed terms are nonpositive throughout the positive quadrant, and the divergence is strictly negative off at most one horizontal line. If a smooth nonconstant periodic trajectory existed, uniqueness makes it a Jordan curve. Its bounded interior lies in the positive quadrant and has positive area. The divergence theorem would give a strictly negative area integral but zero normal flux through the orbit, an impossibility.

**3. The discontinuous threshold, including sliding.** In the two open regions the same multiplier yields
\[
\nabla\cdot(BF_-)=-\frac{P(y)}{ry},\qquad
\nabla\cdot(BF_+)=-\frac{P(y)}{ry}-\frac{q\varepsilon}{r}.
\]
Across the switch \(\Sigma=\{y=T_c\}\), with the upward unit normal \(n\), the jump is
\[
B(F_+-F_-)\cdot n=-\frac{q(1+\varepsilon T_c)}r<0.
\]
Because \(F_{+,y}=F_{-,y}-qT_c\) on \(\Sigma\), an escaping sliding segment requiring \(F_{-,y}<0<F_{+,y}\) is impossible. Every genuine sliding segment is attracting, namely \(F_{-,y}\ge0\ge F_{+,y}\).

Suppose a piecewise-regular Jordan periodic orbit \(\Gamma\) existed, and let \(\Omega\) be its bounded interior. Apply the ordinary divergence theorem separately to the portions of \(\Omega\) below and above \(\Sigma\), omitting the finitely many crossing and tangent endpoints of zero arc length. Along every ordinary trajectory arc of \(\Gamma\), the weighted outward normal flux vanishes. Each sliding arc contributes a **nonnegative** flux from the side inside \(\Omega\): if the interior lies below the switch, its outward normal points upward and \(F_{-,y}\ge0\); if it lies above, the normal points downward and \(F_{+,y}\le0\). Each interior interval of \(\Omega\cap\Sigma\) contributes the **positive** combined interface flux
\[
B(F_--F_+)\cdot n=\frac{q(1+\varepsilon T_c)}r>0.
\]
Consequently the sum of boundary and internal-interface fluxes is nonnegative. But the sum of the two bulk divergence integrals is strictly negative, because \(P(y)\ge0\) and its possible zero line has area zero. This contradicts the two separate divergence theorems. The argument includes pure crossing cycles, pure smooth cycles restricted to either side, and cycles with attracting sliding arcs.

## Verification

The standalone `CHECK.py` uses SymPy to reconstruct both the smooth weighted-divergence identity and the two discontinuous one-sided divergences, including the exact normal jump. Running `python3 CHECK.py` returns `CHECK_OK`. This tests algebraic identities, not infinite-time trajectories; the universal no-cycle conclusion rests on the preceding Green-theorem proof and positivity argument.

For the parameter slice \(\beta=3/2\), \(\varepsilon=6\), the sufficient condition is \(0<r\le(123+12\sqrt{91})/50\), approximately \(r\le4.74945408\). The motivating article's oscillation illustrations use \(r=5\) on this slice, outside the certified region. This is a comparison of parameter locations, **not** a claim that the sufficient boundary is a bifurcation threshold.

## Relationship to prior work

Peng and Xiang (2023), Sections 2--7, defined the switched tumor--immune model, described its sliding geometry, and calculated the corresponding Dulac expressions for the **two separate smooth subsystems** in Section 5. The contribution here is a unified no-cycle statement for the complete switched field, requiring control of both the nonzero normal jump and sliding arcs, and its robust extension to **every** smooth nondecreasing treatment activation. Individual subsystem no-cycle tests do not generally exclude switching cycles. The exact one-inequality region retains all positive therapy intensities and threshold locations.

Da Cruz and Torregrosa (2020) give a piecewise Dulac theorem under the additional requirement of continuity of the weighted normal components across the switching line. Li, Chen, Chen and Wu (2021) likewise address refracted systems. The present step-controlled model has the **nonzero** weighted normal jump displayed above and therefore is not covered by those normal-continuity hypotheses; their work provides important related methodology. The uncontrolled smooth antigenicity model of Li, Xie, Chen and Zhang (2021) is related but lacks the above monotone treatment family.

## Limitations

The inequality is a sufficient oscillation-exclusion certificate, not a necessary condition. Failure of the inequality does not establish any oscillation. The theorem does not characterize equilibria, global attractors, clinical efficacy, or arbitrary nonmonotone therapies. The Filippov assertion is made for simple periodic cycles with finite piecewise-regular decomposition; it does not claim a general theorem for all pathological discontinuous differential inclusions. The linked full source was examined; potentially relevant but inaccessible or different-controller literature leaves normal residual originality risk. Independent audit has not been performed.

## References

1. H. Peng and C. Xiang, “A Filippov tumor-immune system with antigenicity,” *AIMS Mathematics* **8** (2023), 19699--19718, DOI: 10.3934/math.20231004. Public version dated 2023-06-12. Full text: https://www.aimspress.com/aimspress-data/math/2023/8/PDF/math-08-08-1004.pdf
2. L. P. C. da Cruz and J. Torregrosa, “A Bendixon--Dulac theorem for some piecewise systems,” *Nonlinearity* **33** (2020), 2455--2480, DOI: 10.1088/1361-6544/ab6812. Open preprint: https://mat.uab.cat/departament/Publ/prep/p07_18.pdf
3. S. Li, H. Chen, T. Chen, and K. Wu, “A note on the Bendixson--Dulac theorem for refracted systems with multiple zones,” *Journal of Nonlinear Modeling and Analysis* **3** (2021), 275--281, DOI: 10.12150/jnma.2021.275.
4. J. Li, X. Xie, Y. Chen, and D. Zhang, “Complex dynamics of a tumor-immune system with antigenicity,” *Applied Mathematics and Computation* **400** (2021), 126052, DOI: 10.1016/j.amc.2021.126052.
