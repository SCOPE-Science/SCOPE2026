# Two equilibrium balance identities invalidate the reported R3 Hopf base point
## Finding
For the delayed predator–prey disease-treatment system (1.5) in Almuallem, Mollah, and Sarwardi, every interior equilibrium obeys two elementary balance identities that are independent of the gestation delay. If \(x^*>0\) and \(w^*>0\), then
\[
0<x^*<K,\qquad z^*=\frac{b+c}{\beta}.
\]
With the paper's R3 values \(K=1\), \(b=0.2\), \(c=0.1\), and \(\beta=0.1\), the second identity requires \(z^*=3\). The reported R3 point
\[
E^*=(0.227,0.5,1.5,0.4)
\]
is therefore not an equilibrium of the printed model. In particular,
\[
\dot w=0.4(0.1\cdot1.5-0.2-0.1)=-\frac{3}{50}
eq0.
\]
The paper's earlier numerical point \((3.36,6.97,8.85,1.01)\), stated for the same parameter vector, is also impossible because it violates both \(x^*<K=1\) and \(z^*=3\).

## Assumptions and scope
The claim concerns the equations and parameter values as printed in the 2025 article. All biological parameters used here are positive. An “interior equilibrium” means a constant state with \(x^*,y^*,z^*,w^*>0\). Because an equilibrium is constant, the delayed terms equal the corresponding current-state terms, so the identities below hold for every delay \(\tau\ge0\).

The conclusion is deliberately limited. It shows that the two displayed numerical interior-equilibrium tuples are not equilibria of the printed system and therefore cannot serve as base points for the reported R3 local-stability or Hopf calculations. It does not prove that the model has no other positive equilibrium, and it does not exclude a Hopf bifurcation after a corrected equilibrium and linearization are supplied.

## Proof
The treatment equation printed as Eq. (1.4), and again in system (1.5), is
\[
\dot w=\beta zw-bw-cw=w(\beta z-b-c).
\]
At an interior equilibrium \(w^*>0\). Hence \(\dot w=0\) forces
\[
\beta z^*-b-c=0,
\]
which is equivalent to \(z^*=(b+c)/\beta\). Substitution of R3 gives
\[
z^*=\frac{0.2+0.1}{0.1}=3.
\]
The reported value \(z^*=1.5\) cannot satisfy this identity. Direct substitution into the same equation yields the exact nonzero residual \(-3/50\).

A second independent identity follows from the prey equation. Dividing the equilibrium equation by \(x^*>0\) gives
\[
r\left(1-\frac{x^*}{K}ight)=\frac{m y^*}{a_1+(x^*)^2}+\frac{n z^*}{a_2+(x^*)^2}.
\]
The right-hand side is strictly positive at an interior equilibrium, so \(1-x^*/K>0\) and therefore \(0<x^*<K\). The article's earlier numerical tuple has \(x^*=3.36\) while the same parameter vector has \(K=1\), so that tuple cannot be an interior equilibrium either.

For the R3 tuple, exact-rational substitution into all four nondelayed equilibrium residuals gives approximately
\[
(0.1892983,-0.3452294,-1.4301674,-0.06),
\]
so the failure is not confined to rounding of the treatment coordinate.

## Verification
The accompanying `verify_equilibrium.py` uses exact rational arithmetic. It checks the two structural identities, computes the treatment residual \(-3/50\) at the reported R3 point, evaluates the full four-component residual vector from the printed equations, and verifies that the earlier tuple violates \(x^*<K\). Successful execution prints `VERIFY_OK`.

The model equation, the symbolic formula \(z^*=(b+c)/\beta\), the two numerical tuples, the R3 parameter vector, and the captions tying the R3 tuple to local stability and Hopf simulations were checked in the article's full text. The official article page gives the publication date 26 June 2025 and lists MSC 92D25 first.

## Relationship to prior work
The source article itself symbolically states \(z^*=(b+c)/\beta\), but its two subsequent numerical interior-equilibrium tuples do not satisfy that identity. Exact-title, exact-coordinate, correction/erratum, equilibrium-balance, and Hopf-base-point searches did not locate a published correction of this inconsistency. Semantic searches of the published finding database likewise returned dynamical-systems results on other models rather than this source-specific equilibrium defect.

Mondal, Sarkar, and Sk (2023) study treatment of infected predators in a different three-compartment model with a saturating treatment term and no separate treatment compartment \(w\). Their equilibrium analysis therefore does not imply, repair, or cover the balance identity failure in system (1.5), though it confirms that equilibria and Hopf calculations are central outputs in this modeling literature.

## Limitations
The analysis is a consistency result for the printed equations and printed parameter values. An unreported implementation with different parameters or a different treatment equation could explain the plotted trajectories, but it would be a different numerical problem and does not make the displayed R3 tuple an equilibrium of system (1.5). No claim is made about the existence, location, or stability of a corrected interior equilibrium beyond the two necessary identities proved above.

## References
1. N. A. Almuallem, H. Mollah, and S. Sarwardi, “A study of a prey-predator model with disease in predator including gestation delay, treatment and linear harvesting of predator species,” *AIMS Mathematics* 10(6) (2025), 14657–14698. DOI: 10.3934/math.2025660.
2. B. Mondal, A. Sarkar, and N. Sk, “Treatment of infected predators under the influence of fear-induced refuge,” *Scientific Reports* 13 (2023), 16623. DOI: 10.1038/s41598-023-43021-0.
