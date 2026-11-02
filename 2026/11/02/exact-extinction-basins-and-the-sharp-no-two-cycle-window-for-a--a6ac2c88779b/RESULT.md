# Exact extinction basins and the sharp no-two-cycle window for a cubic Allee map

## Finding

For the Allee–logistic population map \(F_k(x)=k x^2(1-x)\), the full initial-condition basins are explicitly determined throughout the sharp period-two-free interval \(4<k\le16/3\). With
\[
\ell=\frac{1-\sqrt{1-4/k}}{2},\qquad u=\frac{1+\sqrt{1-4/k}}{2},\qquad
R=\frac{1-\ell+\sqrt{(1-\ell)(1+3\ell)}}{2},
\]
the extinction basin within \([0,1]\) is \([0,\ell)\cup(R,1]\), the active-state basin is \((\ell,R)\), and the only remaining initial states are \(\ell\) (fixed) and \(R\) (mapped in one step to \(\ell\)). In particular the active basin is **bounded on both sides**: sufficiently high initial density also goes extinct.

For a uniform initial state on \([0,1]\), the exact fraction that eventually becomes extinct is
\[
P_{\mathrm{ext}}(k)=1+\ell-R=\frac{1+3\ell-\sqrt{(1-\ell)(1+3\ell)}}{2}.
\]
It decreases strictly as \(k\) increases, from the right-limit \((5-\sqrt5)/4\) as \(k\downarrow4\) to \((7-\sqrt{21})/8\) at \(k=16/3\).

The parameter \(k=16/3\) is sharp for the period-two exclusion: all \(4<k\le16/3\) have no prime-two orbit, while each \(16/3<k\le27/4\) has one. The theorem does not claim the basins above that threshold.

## Assumptions and scope

This is the special case \(m=1/2\), \(h=1\), \(r=2k\) of the GAL family in Pires–Andrade–Herrmann (2026): its Allee factor is \(G(x)=x/2\). The state space is the full biological interval \([0,1]\). The sharp global basin classification uses \(4<k\le16/3\). The comparison statement about existence of a prime-two cycle uses \(16/3<k\le27/4\), where \(F_k([0,1])\subseteq[0,1]\) because its maximum is \(4k/27\). The term probability refers solely to selecting the initial state uniformly in \([0,1]\), not to environmental stochasticity.

## Proof

**(1) Fixed points, hump and the remote extinction boundary.** Apart from \(0\), positive fixed points solve \(k x(1-x)=1\), giving \(0<\ell<1/2<u\le3/4\). The derivative is \(F'_k(x)=k x(2-3x)\); therefore the map is increasing up to \(2/3\) and decreasing thereafter, with maximum \(4k/27\). Division of \(F_k(x)-\ell\) by \(x-\ell\), using \(k\ell(1-\ell)=1\), gives
\[
F_k(x)-\ell=-k(x-\ell)\bigl(x^2+(\ell-1)x-\ell(1-\ell)\bigr).
\]
The quadratic has exactly one positive zero other than \(\ell\); it is \(R\), as stated. Since \(u\le3/4<4/5\) and \(F_k(4/5)=16k/125>64/125>1/2>\ell\), the decreasing right branch crosses \(\ell\) at \(R>4/5\). Meanwhile the hump has height \(4k/27\le64/81<4/5\). Thus \(F_k([\ell,R])\subseteq[\ell,R]\); the minimum \(\ell\) is attained at its endpoints, and the maximum is less than \(R\). In fact \(F_k(x)>\ell\) throughout \((\ell,R)\).

**(2) A sharp no-prime-two calculation.** Suppose \(x,y\in(0,1)\) form a nontrivial two-cycle, and label so that \(t=y/x>1\). From \(y=kx^2(1-x)\), \(x=ky^2(1-y)\), obtain \(x^3(1-x)=y^3(1-y)\). It follows exactly that
\[
x=\frac{t^2+t+1}{t^3+t^2+t+1},\qquad
 y=\frac{t(t^2+t+1)}{t^3+t^2+t+1},\qquad
 k=\frac{(t^3+t^2+t+1)^2}{t^2(t^2+t+1)}.
\]
Subtracting \(16/3\) yields
\[
k-\frac{16}{3}=\frac{(t-1)^2(3t^4+12t^3+14t^2+12t+3)}{3t^2(t^2+t+1)}>0.
\]
There is no nontrivial two-cycle for \(k\le16/3\). Conversely, the displayed continuous parameter function tends to \(16/3\) as \(t\downarrow1\) and to infinity as \(t\to\infty\); for every \(k>16/3\) the intermediate-value theorem supplies such a two-cycle. Both cycle points lie strictly between zero and one by their positive explicit formulas.

**(3) Exhaustive convergence in the forward-invariant middle interval.** The classical interval-iteration theorem of Coppel states that for a continuous self-map of a compact interval with no points of least period two, every forward orbit converges to a fixed point. Apply it to the invariant interval \([\ell,R]\). Its only fixed points are \(\ell\) and \(u\). Moreover \(F'_k(\ell)=(2-3\ell)/(1-\ell)>1\), so no orbit staying strictly above \(\ell\) can converge to \(\ell\): near that fixed point it is strictly pushed away, and \(F_k((\ell,R))\subset(\ell,R)\). Thus every \(x\in(\ell,R)\) tends to \(u\). The endpoint \(R\) maps to \(\ell\) exactly.

**(4) Extinction beyond both basin boundaries.** For \(0<x<\ell\), \(F_k(x)/x=kx(1-x)<1\) because \(x<\ell<1/2\) and \(k\ell(1-\ell)=1\). The resulting decreasing nonnegative orbit can have only the fixed limit \(0\). For \(R<x\le1\), strict decrease of the right branch gives \(F_k(x)<\ell\), so extinction follows after one step. The state \(0\) is fixed. These cases exhaust \([0,1]\).

**(5) Exact initial-condition risk and monotonicity.** The extinction basin consists of two intervals of total length \(\ell+(1-R)\). Write \(D(\ell)=\sqrt{(1-\ell)(1+3\ell)}\). Then
\[
P_{\mathrm{ext}}=\tfrac12(1+3\ell-D(\ell)),\qquad
\frac{dP_{\mathrm{ext}}}{d\ell}=\frac12\left(3-\frac{1-3\ell}{D(\ell)}\right)>0
\]
for \(1/4\le\ell<1/2\); since \(\ell\) strictly decreases with \(k\), the probability decreases with \(k\). Substitution of \(\ell\to1/2\) and \(\ell=1/4\) gives the quoted exact endpoint values.

## Verification

Every displayed factorization and the positive two-cycle parameter identity admit exact polynomial checking. A separate, self-contained Python program `verify.py` uses rational algebra (SymPy) for all identities, checks invariant-interval inequalities with exact rational constants, and tests initial-state basins on rational parameter examples. Finite numerical examples are diagnostic only; the proof of convergence for all initial states uses the interval theorem, not sampling. The statements about all \(k\) in a continuum are algebraic and analytic.

## Relationship to prior work

Pires, Andrade and Herrmann (2026), arXiv:2606.05351v1, introduce and analyze the generalized Allee–logistic family, including stationary bifurcations, time scalings and chaos. The present statement concerns **exact basins for all initial population densities** and the closed-form initial-condition extinction fraction in its cubic parameter slice, as well as the sharp exclusion of nonconstant period-two orbits. It does not claim invention of the cubic map, the already-known fixed-point formulas, Coppel's convergence principle, or general period-doubling theory. Earlier beta-density population maps (Aleixo–Rocha–Pestana, 2009) include the cubic profile and predate the new GAL formulation, and Rocha–Taha (2019) study Allee bifurcations in another general logistic family. The accessible descriptions of those papers do not explicitly give the above exact two-sided basin and uniform-initial-condition probability; their unavailable complete text leaves a historical overlap risk.

## Limitations

The explicit global basin classification is proved only for \(4<k\le16/3\). Existence of period-two orbits above \(16/3\) refutes the all-orbits-to-fixed-points statement, but does not classify basins, attractors or chaotic dynamics there. Uniform initial distribution is a chosen geometric reference measure, not a demographic model. The source's global phenomenology and some antecedent works have independent priority; no independent mathematical audit of this result has occurred. The Coppel convergence principle is used as a cited standard theorem.

## References

1. M. A. Pires, J. S. Andrade Jr., H. J. Herrmann, *Tricriticality and chaos in a generalized Allee-logistic map* (first public June 3, 2026), arXiv:2606.05351v1, https://arxiv.org/abs/2606.05351.
2. W. A. Coppel, *The solution of equations by iteration*, Mathematical Proceedings of the Cambridge Philosophical Society **51** (1955), 41–43, DOI: 10.1017/S030500410002990X.
3. S. Aleixo, J. L. Rocha, D. D. Pestana, *Dynamical behaviour on the parameter space: new populational growth models proportional to beta densities* (2009), http://hdl.handle.net/10400.21/1364.
4. J. L. Rocha, A.-K. Taha, *Allee's effect bifurcation in generalized logistic maps*, International Journal of Bifurcation and Chaos **29** (2019), 1950039, DOI: 10.1142/S0218127419500391.
