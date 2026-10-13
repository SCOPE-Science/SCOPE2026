# Fear changes the critical predator-extinction clock without moving the invasion boundary

## Finding

For the positive two-species fear--refuge system of Ramraj and Poornima [1], the *exact* invasion threshold is independent of the fear coefficient, but the universal predator-extinction time scale **at** the threshold depends strictly on fear. More precisely, write \(b=\beta(1-\delta)\) and let \(u_1\) be the positive root of \(a u_1(1+\alpha u_1)=r\). Set
\[
D_1=1+\alpha u_1,\quad
A=a+\frac{r\alpha}{D_1^2},\quad
B=b+\frac{rk}{D_1^2},\quad
Q=\eta+\frac{cbB}{A},\quad
\mathcal R=\frac{cb u_1}{m}.
\]
For **every** strictly positive initial state, the two populations converge to the prey-only equilibrium when \(\mathcal R\le1\), and to the unique positive equilibrium when \(\mathcal R>1\). No positive periodic orbit exists, regardless of admissible parameter values. At the nonhyperbolic equality \(\mathcal R=1\), both asymptotic constants exist, are strictly positive, and are *independent of the initial state*:
\[
\boxed{\lim_{t\to\infty}t\,v(t)=\frac1Q,\qquad
\lim_{t\to\infty}t\,[u_1-u(t)]=\frac{B}{AQ}.}
\]
Holding all other parameters fixed on the critical surface, \(\mathcal R\) does not change with \(k\), while \(Q\) is strictly increasing in \(k\), and \(B/(AQ)\) is strictly increasing in \(k\). Consequently greater fear reduces the critical predator tail amplitude but increases the leading critical prey deficit. No uniform claim is made as parameters approach the threshold.

## Assumptions and scope

The exact autonomous, **integer-order** equations are
\[
\dot u=u\left(\frac{r}{1+kv+\alpha u}-au-bv\right),\qquad
\dot v=v(cbu-m-\eta v).
\]
Assume \(r,a,k,\alpha,\beta,m,\eta>0\), \(0<c\le1\), \(0\le\delta<1\), and \(u(0),v(0)>0\). Thus \(b=\beta(1-\delta)>0\). Time has the source model's units. The result concerns the displayed deterministic model and **every** positive initial state, not a calibrated empirical ecosystem. The case \(\mathcal R=1\) is equivalently \(m=cb u_1\); the coefficients \(A,B,Q\) are evaluated at \((u_1,0)\). All stated parameter inequalities are strict except those explicitly shown.

## Proof

**1. Positivity, boundedness, and boundary states.** The nonnegative quadrant is invariant and positive states stay positive by the scalar exponential representation of both equations. The bounds \(\dot u\le u(r-au)\) and, after bounding \(u\le U\), \(\dot v\le v(cbU-m-\eta v)\) give global bounded solutions for all admissible parameters without an additional quadratic-form condition. On \(v=0\), the strictly decreasing prey per-capita growth \(f_0(u)=r/(1+\alpha u)-au\) has exactly one positive root \(u_1\). There are just two boundary equilibria: \((0,0)\) and \((u_1,0)\). On \(u=0\), \(\dot v=-v(m+\eta v)\), and \((0,0)\) is a saddle with stable manifold on \(u=0\).

**2. Global convergence when \(\mathcal R\le1\).** Scalar comparison with \(\dot U=U f_0(U)\) gives \(\limsup u(t)\le u_1\). For any \(\varepsilon>0\), the predator equation eventually satisfies \(\dot v\le v(cb(u_1+\varepsilon)-m-\eta v)\). If \(\mathcal R<1\), choose \(\varepsilon\) to make the linear coefficient negative; thus \(v(t)\to0\). If \(\mathcal R=1\), the logistic comparison yields \(\limsup v(t)\le cb\varepsilon/\eta\); letting \(\varepsilon\downarrow0\) gives the same conclusion. For sufficiently small \(\varepsilon\), once \(v(t)\le\varepsilon\), compare \(u\) from below with the autonomous equation
\[
\dot L=L\left(\frac{r}{1+k\varepsilon+\alpha L}-aL-b\varepsilon\right).
\]
Its unique positive attracting root tends to \(u_1\) as \(\varepsilon\to0\). This and the upper comparison give \(u(t)\to u_1\).

**3. The coexistence case.** Write \(F(u,v)=r/(1+kv+\alpha u)-au-bv\) and \(G(u,v)=cbu-m-\eta v\). Their derivatives satisfy \(F_u<0,F_v<0,G_u>0,G_v<0\) everywhere in the positive quadrant. On the positive predator nullcline \(v=(cbu-m)/\eta\), \(F\) decreases strictly as \(u\) increases. At \(u=m/(cb)\), its value is positive exactly when \(\mathcal R>1\); it becomes negative at large \(u\). Therefore there is exactly one positive equilibrium if and only if \(\mathcal R>1\). There the Jacobian has negative diagonal entries \(uF_u,vG_v\), opposite-signed off-diagonal entries, negative trace, and positive determinant; it is a local attractor. The positive-quadrant Dulac function \(H=1/(uv)\) gives
\[
\nabla\cdot[H(\dot u,\dot v)]
=\frac{-a-r\alpha/(1+kv+\alpha u)^2}{v}-\frac{\eta}{u}<0.
\]
Thus no positive periodic or homoclinic loop exists. A bounded positive trajectory cannot approach the saddle \((0,0)\) (its local stable manifold is the predator axis), nor \((u_1,0)\) when \(\mathcal R>1\) (its local stable manifold is the prey axis). A Poincaré--Bendixson limit graph involving boundary equilibria would require a directed return path; the only boundary heteroclinic arrow is \((0,0)\to(u_1,0)\), so such a cycle is impossible. The planar limit-set theorem therefore forces convergence to the unique interior equilibrium. In the \(\mathcal R\le1\) cases Step 2 already supplies convergence.

**4. Exact algebraic rate at the critical threshold.** Let \(w=u-u_1\), \(D=1+\alpha u+kv\), and \(D_1=1+\alpha u_1\). Using \(r/D_1=au_1\), subtraction and common denominators give the *exact* identity
\[
\dot w=-u\,[A(u,v)w+B(u,v)v],\quad
A(u,v)=a+\frac{r\alpha}{DD_1},\quad
B(u,v)=b+\frac{rk}{DD_1}.
\]
At \(m=cbu_1\), \(\dot v=v(cb w-\eta v)\). Since \(v>0\), the ratio \(p=w/v\) is defined for all finite times and obeys the **linear nonautonomous** equation
\[
\dot p=-[uA(u,v)+cbw-\eta v]p-uB(u,v).
\]
By Step 2, \((u,v)\to(u_1,0)\); hence the damping coefficient tends to \(u_1A>0\) and the forcing tends to \(-u_1B\). Variation of constants for a scalar stable linear equation gives \(p(t)\to-B/A\), with no assumption on the sign of \(w(0)\). Consequently
\[
\frac{d}{dt}\frac1{v(t)}=\eta-cb\,p(t)\longrightarrow Q>0.
\]
Integrating and dividing by \(t\) proves \(t v(t)\to1/Q\). Multiplying by \(-p(t)\) yields \(t(u_1-u(t))\to B/(AQ)\), completing the critical-rate proof.

**5. The fear contrast.** At fixed \(r,a,\alpha,b,c,m,\eta\) satisfying \(m=cbu_1\), neither \(u_1\), \(A\), nor \(\mathcal R\) depends on \(k\). But \(\partial B/\partial k=r/D_1^2>0\), so
\[
\frac{\partial Q}{\partial k}=\frac{cbr}{AD_1^2}>0,
\qquad \frac{\partial}{\partial k}\frac{B}{AQ}
=\frac{A\eta r}{D_1^2(A\eta+cbB)^2}>0.
\]
(The latter is obtained from \(B/(AQ)=B/(A\eta+cbB)\).) This proves both strict comparative statics.

## Verification

The accompanying `verify.py` checks the exact rational identity for the prey equation, the critical ratio equation, and both derivatives by symbolic algebra. It also checks the positive rational test \(r=2\), \(a=\alpha=k=b=c=m=\eta=1\), for which \(u_1=1\), \(\mathcal R=1\), \(A=B=3/2\), \(Q=2\), and both predicted scaled limits are \(1/2\). Run `python -m pip install -r requirements.txt` then `python verify.py`; success prints `VERIFY_OK`. These computations check algebra but do not replace the global comparison and planar arguments. The proof itself covers all admissible real parameters, not a finite sample.

## Relationship to prior work

Ramraj--Poornima [1, §§3--4, 6--7] proved positivity and conditional boundedness, calculated local equilibria, and observed convergence numerically; they explicitly left rigorous global stability for future work. The present global classification removes that conditional bound and resolves the nonhyperbolic threshold by exact, initial-condition-independent decay constants. The negative Dulac divergence is a classical method, not a claimed new technique. Hsu--Huang [2] studied global equilibria of generalized Holling--Tanner systems with a different predator equation \(\dot y=y(\delta-\beta y/x)\); their theorems do not supply the fear-dependent coefficient above. Umrao--Lamba--Srivastava [3] and Chatterjee [4] establish stability and bifurcations for differently structured fear/predation models, but neither of their examined models is this coupled-denominator flow nor yields the displayed critical tail. Searching these model equations, synonyms for transcritical slowdown, published records, and predecessor claims did not locate exact coverage; this is a scoped literature comparison, not proof of all-world uniqueness.

## Limitations

This is a theorem for the printed deterministic ODE with positive density-dependent predator loss \(\eta>0\) and prey loss \(a>0\), no spatial structure, noise, delays, or memory. The reciprocal-time limits require **strictly positive** predator initial density and the exact critical equality; they do not imply the same law away from the threshold or finite-time calibration accuracy. Effects of fear on transient dynamics far from equilibrium, inferred model parameters, and biological timescales require separate data and validation. Source [1] reports numerical predictions, but this analysis does not establish their empirical accuracy. Independent verification has not been performed.

## References

1. G. Ramraj and T. Poornima, *Fear-driven predator–prey dynamics with prey refuge: analytical framework and physics-informed neural network approach*, Frontiers in Artificial Intelligence **9**, 1868693 (published 2026-08-10). DOI: 10.3389/frai.2026.1868693. Full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC13500610/.
2. S.-B. Hsu and T.-W. Huang, *Global Stability for a Class of Predator-Prey Systems*, SIAM J. Appl. Math. **55** (1995), 763–783. DOI: 10.1137/S0036139993253201; author-hosted full text: https://www.math.nthu.edu.tw/~sbhsu/Hsu1995.pdf.
3. A. K. Umrao, S. Lamba, and P. K. Srivastava, *Nonlinear dynamics in a fear-driven predator–prey system: bistability, bifurcations, hydra effect, and optimal harvesting*, Math. Methods Appl. Sci. **48** (2025), 2194–2223; first published 2024-08-31. DOI: 10.1002/mma.10431.
4. *Complex Dynamics of a Predator–Prey System With Fear Effect in Prey*, Journal of Applied Mathematics (2026). DOI: 10.1155/jama/7538186.
