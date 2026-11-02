# Sharp five-step extinction resonance in the zero-determinant border-collision map

## Finding
For real parameters \(a>0\), \(b>0\), and \(d>0\), consider the continuous, positively homogeneous planar map
\[
F_{a,b,d}(x,y)=\begin{cases}
(-bx+y,0),&x\leq0,\\
(-ax+y,-dx),&x>0.
\end{cases}
\]
The following are equivalent:

1. There exists an integer \(N\geq1\) such that \(F_{a,b,d}^{N}(z)=(0,0)\) for **every** \(z\in\mathbb R^2\).
2. The right-branch determinant satisfies \(d=ab\).

On this *entire* resonance surface, the least such integer is **exactly five**:
\[
\boxed{F_{a,b,ab}^{5}\equiv(0,0),\qquad F_{a,b,ab}^{4}\not\equiv(0,0).}
\]
Outside the resonance surface, the explicit starting point \((1,0)\) never reaches the origin in finite time. In particular, this is an **if and only if** classification of uniform finite-time extinction throughout the strictly negative left- and right-trace quadrant of the zero-left-determinant border-collision normal form. It holds even when the right-branch determinant \(d=ab\) is arbitrarily large.

## Assumptions and scope
The full phase space is \(\mathbb R^2\), with no restriction on the initial condition. One iteration is one application of the stated, unforced map, including at the switching line \(x=0\), where both formulas coincide. The real parameters are fixed with \(a,b,d>0\). Write \(c=ab-d\), which may be negative, zero, or positive. The claim concerns *exact arrival in finitely many iterates*, not necessarily eventual smallness or the stability type of nonextinct orbits.

The correspondence with the standard border-collision parameters is \(\tau_L=-b\), \(\delta_L=0\), \(\tau_R=-a\), \(\delta_R=d\), and \(\mu=0\). The parameter quadrant and the zero-forcing requirement are part of the statement.

## Proof
**Step 1: An exact two-step cancellation on the positive coordinate ray.** For \(u>0\), one right step gives \((-au,-du)\), whose first coordinate is strictly negative. The subsequent left step gives
\[
\boxed{F_{a,b,d}^{2}(u,0)=((ab-d)u,0)=(cu,0).}
\]
In particular, when \(d=ab\), every \((u,0)\) with \(u>0\) reaches the origin after exactly two applications. If \(u<0\), one left application sends \((u,0)\) to \((-bu,0)\) with positive first coordinate, so under \(d=ab\) it reaches the origin in at most three applications. The origin itself is fixed. Thus **every point on the coordinate axis** is annihilated within three steps at resonance.

**Step 2: All initial points enter that axis within two steps at resonance.** If \(x\leq0\), a single left step already yields \((-bx+y,0)\), and Step 1 gives extinction within four total steps. If \(x>0\), put \(v=y-ax\). The first right image is \((v,-abx)\). If \(v\leq0\), the next left image is
\[
F_{a,b,ab}^{2}(x,y)=(-bv-abx,0)=(-by,0).
\]
If \(v>0\), one more right step followed by a left step yields
\[
F_{a,b,ab}^{3}(x,y)=(ab^2x,0),
\]
whose first coordinate is positive. Hence when \(v\leq0\) extinction occurs within \(2+3=5\) applications; when \(v>0\) it occurs within \(3+2=5\). Thus \(F_{a,b,ab}^{5}\equiv0\) for every initial point.

**Step 3: Five applications are necessary.** For the open set of initial points satisfying \(x>0\) and \(0<y<ax\), the itinerary is strictly \(RLLRL\) until extinction. Its fourth iterate is
\[
F_{a,b,ab}^{4}(x,y)=(-ab^2y,-ab^3y),
\]
which is not zero because \(a,b,y>0\). In particular \((x,y)=(1,a/2)\) is a witness. Step 2 proves that the fifth iterate is zero. This establishes that the least uniform extinction exponent is five.

**Step 4: Off resonance, one orbit persists forever.** Start at \(z_0=(1,0)\). Step 1 gives \(F^2(z_0)=(c,0)\). If \(c>0\), repeated applications of Step 1 yield
\[
F^{2n}(z_0)=(c^n,0)\ne(0,0),\qquad n\ge0.
\]
Each intermediate odd iterate is nonzero as well. If \(c<0\), a negative-axis point \((u,0)\), with \(u<0\), undergoes the three-step itinerary \(LRL\) and returns to \((-bcu,0)\), still strictly negative because \(-bc>0\). Hence
\[
F^{2+3n}(z_0)=(c(-bc)^n,0)\ne(0,0),\qquad n\ge0.
\]
All intervening states are nonzero, since the first component of each applicable image is nonzero before its return. Thus no finite iterate annihilates all states when \(c\ne0\). Combining the four steps proves both directions and sharpness.

## Verification
The standalone script `check_exact.py` uses exact rational arithmetic to check the five-step identity on \(30\) rational parameter pairs and \(289\) initial rational lattice points per pair; constructs witnesses for the sharp fourth-iterate obstruction; verifies the explicit nonextinction subsequences for off-resonance parameters; and uses symbolic matrix algebra to reconstruct the cancellation \(A_LA_RA_L=(ab-d)A_L\). The independently computed checks total \(11{,}817\) and print `EXACT_ARITHMETIC_REGRESSION_OK` on success. Run with Python 3 and SymPy installed: `python3 check_exact.py`.

The checker is a finite regression, not a substitute for the all-real-parameter proof in Steps 1–4. In particular, no finite grid is used to deduce the global equivalence.

## Relationship to prior work
Simpson's zero-determinant normal-form study [1, §§1, 4.1, 5.3] introduces the four-parameter map and explicitly states that the zero-forcing case \(\mu=0\) is outside its analysis. Its formula for the nonzero multiplier of an \(LR\) cycle contains the algebraic factor \(\tau_L\tau_R-\delta_R\), also visible in the present resonance condition, but it does **not** assert the global all-initial-condition five-step extinction or its converse. The new assertion is not the vanishing of that known scalar factor in isolation; it is the complete finite-time dynamical classification and sharp annihilation index.

Simpson's earlier analysis of stability on switching surfaces [2, §§1, 6] develops broad criteria for asymptotic stability of homogeneous maps and investigates different noninvertible sign configurations. Those asymptotic statements do not determine uniform **exact** five-step arrival in the stated negative-trace, zero-left-determinant regime.

An already published result on the homogeneous max-plus border-collision map [3] establishes a different global extinction law for \(\tau_L=0\), \(\tau_R\ge0\). That theorem does not imply the present result: here \(\tau_L=-b<0\) and \(\tau_R=-a<0\), and neither branch has the same nilpotent left matrix as in [3]. The present if-and-only-if resonant surface is not a specialization of the max-plus theorem's parameter domain.

General border-collision theory [4] supplies background, but no novelty is asserted for the normal form or for the matrix-trace identity itself. The literature comparison is bounded by the sources inspected and cannot rule out every unindexed equivalent result.

## Limitations
This is a classification of *finite-time annihilation*, not a full phase portrait away from the resonance surface. Some persistent off-resonance orbits may converge asymptotically toward zero; persistence does not mean divergence. The result is restricted to \(a,b,d>0\), \(\mu=0\), and exact piecewise linearity. It does not establish robustness to forcing, smoothing, or numerical perturbations. Its apparent publication novelty remains subject to independent priority verification.

## References
1. D. J. W. Simpson, *The two-dimensional border-collision normal form with a zero determinant*, arXiv:2408.04790v1, first public 2024-08-08, especially §§1 and 4–6. https://arxiv.org/abs/2408.04790
2. D. J. W. Simpson, *The stability of fixed points on switching manifolds of piecewise-smooth continuous maps*, arXiv:1612.02932v1, first public 2016-12-09, especially §§1 and 6. https://arxiv.org/abs/1612.02932
3. *Sharp extinction and persistence at the homogeneous max-plus border collision*, publicly indexed mathematical result, 2026-10-11. https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-extinction-and-persistence-at-the-homogeneous-max-plus-bor--a2b1d9a86864
4. S. Banerjee and C. Grebogi, *Border collision bifurcations in two-dimensional piecewise smooth maps*, Physical Review E 59 (1999), 4052–4061. https://doi.org/10.1103/PhysRevE.59.4052
