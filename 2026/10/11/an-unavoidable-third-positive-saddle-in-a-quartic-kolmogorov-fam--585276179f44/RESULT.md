# An unavoidable third positive saddle in a quartic Kolmogorov family
## Finding
For the quartic Kolmogorov family printed as equation (3) by Du and Huang, with real parameters \(a,b,A_{10},B_{10}\), the line \(y=1\) contains exactly three positive equilibria \(E_1=(1,1)\), \(E_m=(3/2,1)\), and \(E_2=(2,1)\), because \(P(x,1)=0\) and \(Q(x,1)=(x-1)(x-2)(2x-3)\). The middle equilibrium is parameter independent and has Jacobian \(J(E_m)=\begin{pmatrix}0&-19/16\\-1/2&13/6\end{pmatrix}\), determinant \(-19/32\), and eigenvalues \((26\pm\sqrt{1018})/24\); hence it is a hyperbolic saddle for every parameter choice and cannot undergo a local bifurcation within this family. Thus the published description of model (3) as having two positive equilibrium points omits an unavoidable interior saddle. This result does not assert that these are the only positive equilibria off the line \(y=1\), and it does not by itself invalidate the source’s local focal-value calculations at \((1,1)\) and \((2,1)\).

## Assumptions and scope
Consider the exact planar polynomial system
\[
\dot x=\frac16 x(y-1)\left(x^2-24ay-6A_{10}x+6A_{10}xy-7y^2+30ay^2-6a\right)=P(x,y),
\]
\[
\dot y=\frac13 y\left(3b+3B_{10}x-x^2+6x^3+9by-6B_{10}xy-26x^2y-2y^2-27by^2+39xy^2+3B_{10}xy^2-16y^3+15by^3\right)=Q(x,y),
\]
with \(a,b,A_{10},B_{10}\in\mathbb R\). The theorem concerns the positive equilibria lying on the horizontal line \(y=1\). It does not classify possible positive equilibria away from that line. “Hyperbolic saddle” refers to the ordinary planar linearization at the stated equilibrium.

## Proof
The first component has the factor \(y-1\), so
\[
P(x,1)=0
\]
for every real \(x\). In the second component, substituting \(y=1\) cancels every term containing \(b\) and every term containing \(B_{10}\), leaving
\[
Q(x,1)=2x^3-9x^2+13x-6=(x-1)(x-2)(2x-3).
\]
Therefore the line \(y=1\) contains exactly the three positive equilibria
\[
E_1=(1,1),\qquad E_m=(3/2,1),\qquad E_2=(2,1).
\]

Differentiate the displayed vector field. At \(E_m\), all four free parameters cancel and the Jacobian is
\[
J(E_m)=\begin{pmatrix}0&-19/16\\-1/2&13/6\end{pmatrix}.
\]
Hence
\[
\operatorname{tr}J(E_m)=13/6,\qquad \det J(E_m)=-19/32<0.
\]
The characteristic polynomial is
\[
\lambda^2-\frac{13}6\lambda-\frac{19}{32},
\]
whose roots are
\[
\lambda_\pm=\frac{26\pm\sqrt{1018}}{24}.
\]
Since one root is negative and the other positive, \(E_m\) is a hyperbolic saddle for every \(a,b,A_{10},B_{10}\). In particular, no variation of those parameters can make this equilibrium nonhyperbolic, so no local bifurcation of this equilibrium occurs within the printed four-parameter family.

For comparison, direct substitution also gives
\[
J(E_1)=J(E_2)=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\]
which is consistent with the source’s local focus/center analysis at those two points. The omitted saddle is therefore a distinct, structurally persistent third equilibrium rather than a relabeling of either analyzed point.

## Verification
The accompanying script `artifacts/verify_third_equilibrium.py` reconstructs the printed vector field symbolically, verifies \(P(x,1)=0\), factors \(Q(x,1)\), computes all three Jacobians on the line, checks \(\det J(E_m)=-19/32\), and verifies the two exact eigenvalues. Running the script from this package produces the recorded `artifacts/verification_output.txt` and ends in `VERIFY_OK`.

The proof itself is exact algebra. No numerical trajectory, finite sampling, or unproved computational search is used to establish the equilibrium or saddle statements.

## Relationship to prior work
Du and Huang introduce exactly this four-parameter model and state that model (3) has two positive equilibrium points, \((1,1)\) and \((2,1)\), after which their focal-value and small-limit-cycle analysis is organized around those two points. Direct full-text inspection of the model and its linearization section shows no treatment of \((3/2,1)\).

Earlier quartic Kolmogorov papers by overlapping authors study different vector fields and different prescribed positive-equilibrium configurations. A 2014 symmetric model uses the pair \((1,2)\) and \((2,1)\); a 2015 paper studies another quartic family with several prescribed positive singular points. Those results do not imply the factorization of \(Q(x,1)\) for the 2023 model or the parameter-independent saddle above. Exact-title, equation-fragment, equilibrium-coordinate, correction, and semantic database searches located the source and related quartic models but no inspected publication stating this missing equilibrium or its universal saddle type.

## Limitations
The result corrects the positive-equilibrium geometry on \(y=1\) only. It does not prove that the three displayed equilibria exhaust all positive equilibria of the full system away from that line. It also does not recompute the source’s focal values or its local small-amplitude limit-cycle bifurcations at \((1,1)\) and \((2,1)\); the existence of the saddle alone does not contradict those local calculations. A global phase-portrait or separatrix analysis would require additional work. Literature searches cannot exclude an equivalent observation in unindexed commentary or material using substantially different notation.

## References
1. C. Du and W. Huang, “Hopf bifurcation problems near double positive equilibrium points for a class of quartic Kolmogorov model,” *AIMS Mathematics* 8(11) (2023), 26715–26730. DOI: 10.3934/math.20231367.
2. C. Du, Y. Liu, and W. Huang, “Limit Cycles Bifurcations for a Class of Kolmogorov Model in Symmetrical Vector Field,” *International Journal of Bifurcation and Chaos* 24 (2014), article 1450040. DOI: 10.1142/S0218127414500400.
3. C. Du, Y. Liu, and X. Zhang, “Limit Cycles in a Class of Quartic Kolmogorov Model with Three Positive Equilibrium Points,” *International Journal of Bifurcation and Chaos* 25 (2015), article 1550080. DOI: 10.1142/S0218127415500807.
