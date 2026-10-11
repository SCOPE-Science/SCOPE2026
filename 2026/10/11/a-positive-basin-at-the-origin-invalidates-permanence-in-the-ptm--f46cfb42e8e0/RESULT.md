# A positive basin at the origin invalidates permanence in the PTM host–parasitoid map

## Finding

Consider the discrete map
\[
H_{n+1}=\rho_1H_n\tanh(P_n),\qquad
P_{n+1}=\rho_2H_n\bigl(1-\tanh(P_n)\bigr),
\]
\[
G_{n+1}=\alpha_0G_n+\alpha H_n+(1-\alpha)P_n.
\]
For \(\rho_1,\rho_2>0\), \(\alpha\in[0,1]\), and \(0<\alpha_0<1\), the origin is locally asymptotically stable. Consequently there are strictly positive solutions converging to the boundary equilibrium, so the model is not permanent in the sense of admitting a common positive asymptotic lower bound for all positive solutions.

A fully explicit counterexample to the published permanence theorem is obtained at
\[
(\rho_1,\rho_2,\alpha,\alpha_0)=\left(2,1,\frac12,\frac12\right).
\]
For every strictly positive initial point satisfying
\[
V_0:=3H_0+P_0+G_0<\frac116,
\]
one has
\[
V_{n+1}\le\frac34V_n,
\]
and therefore \((H_n,P_n,G_n)\to(0,0,0)\) geometrically.

The same equations also show that the environmental coordinate is one-way coupled: the entire \((H,P)\) trajectory is independent of \(G_0\), \(\alpha\), and \(\alpha_0\). For two trajectories with the same \((H_0,P_0)\),
\[
G_n-\widetilde G_n=\alpha_0^n(G_0-\widetilde G_0).
\]

## Assumptions and scope

The claim concerns Model (9) as printed by Salih and Al-Saidi, interpreted as the discrete update map rather than the difference field \(T-I\). Parameters satisfy the source-domain conditions \(\rho_1,\rho_2>0\), \(\alpha\in[0,1]\), and \(0<\alpha_0<1\). The contradiction uses the source's own permanence hypotheses \(\rho_1>1\), \(0<\rho_2\le\rho_1\), and \(0<\alpha_0<1\).

No claim is made about persistence after modifying the model to feed \(G\) back into the host–parasitoid equations, nor about global dynamics outside the local basin of the origin.

## Proof

Let \(T\) denote the update map. Its Jacobian at the origin is
\[
DT(0,0,0)=
\begin{pmatrix}
0&0&0\\
\rho_2&0&0\\
\alpha&1-\alpha&\alpha_0
\end{pmatrix}.
\]
This matrix is lower triangular, so its discrete multipliers are exactly
\[
0,\qquad 0,\qquad \alpha_0.
\]
For \(0<\alpha_0<1\), every multiplier has modulus less than one; the standard discrete linearization theorem therefore makes the origin locally asymptotically stable.

There is also a direct elementary certificate inside the published theorem's parameter region. Set
\[
(\rho_1,\rho_2,\alpha,\alpha_0)=\left(2,1,\frac12,\frac12\right),
\qquad V=3H+P+G.
\]
For a strictly positive state with \(V<1/16\), one has \(P<1/16\) and
\[
0<\tanh P<P.
\]
Hence
\[
H'=2H\tanh P\le 2HP\le\frac18H,
\qquad
P'=H(1-\tanh P)\le H,
\]
and
\[
G'=\frac12G+\frac12H+\frac12P.
\]
Therefore
\[
V'=3H'+P'+G'
\le \frac158H+\frac12P+\frac12G
\le \frac34(3H+P+G)=\frac34V.
\]
The set \(0<V<1/16\) is thus forward invariant and \(V_n\le(3/4)^nV_0\). Because \(H,P,G>0\) implies \(H',P',G'>0\), every point in this open positive set generates a strictly positive solution that converges to the origin. Such a solution has coordinatewise asymptotic lower bound zero, contradicting any permanence assertion with a universal positive lower bound.

Finally, the first two update equations do not contain \(G\), \(\alpha\), or \(\alpha_0\). Thus the \((H,P)\) subsystem is autonomous. For two states sharing the same \((H,P)\), subtraction of the third equation gives
\[
\Delta G_{n+1}=\alpha_0\Delta G_n,
\]
hence \(\Delta G_n=\alpha_0^n\Delta G_0\).

## Verification

The bundled `verify.py` uses exact rational arithmetic to check the explicit parameter hypotheses and every coefficient in the contraction estimate:
\[
\frac158\le\frac94,\qquad
\frac12\le\frac34,\qquad
\frac12\le\frac34.
\]
It also checks that the discrete Jacobian is lower triangular with diagonal \((0,0,\alpha_0)\). Running the script with the Python standard library prints `VERIFY_OK`.

The finite checker is not used to infer convergence from sampled iterates; convergence follows from the analytic one-step contraction proved above.

## Relationship to prior work

Salih and Al-Saidi introduce the three-dimensional map by adjoining the environmental/PTM coordinate to a two-dimensional host–parasitoid map. Their Theorem 1 states that positive solutions are permanent under \(\rho_1>1\), \(0<\rho_2\le\rho_1\), and \(0<\alpha_0<1\). Their paper also writes the Jacobian of the difference field \(T-I\), whose vertical eigenvalue is \(\alpha_0-1\), rather than the multiplier \(\alpha_0\) of the discrete update map.

A 2024 follow-up on a related host–parasitoid model explicitly compares its stability analysis with the 2022 model and reproduces the earlier fixed-point/eigenvalue summary, but does not supply the positive-basin counterexample or repair the permanence statement. Earlier host–parasitoid literature studies persistence and stability for different two-dimensional models and does not imply the three-dimensional theorem correction here.

Focused searches of the indexed research database, the exact DOI/title, permanence terminology, map equations, and related host–parasitoid literature found no statement equivalent to the explicit positive-basin contradiction.

## Limitations

The result disproves the published universal permanence claim and establishes local attraction of the origin; it does not classify all basins, all positive equilibria, or all chaotic invariant sets. The one-way skew-product observation does not say that \(G\) is numerically uninteresting: it says only that \(G\) cannot feed back into \(H\) or \(P\) in the printed equations.

The literature search cannot rule out an unindexed correction or informal note. The 2024 follow-up was inspected at its model description, comparison table, and references rather than exhaustively for every downstream application.

## References

1. S. H. Salih and N. M. G. Al-Saidi, “3D-Chaotic discrete system of vector borne diseases using environment factor with deep analysis,” *AIMS Mathematics* 7 (2022), 3972–3987, DOI 10.3934/math.2022219. Public article date: 13 December 2021.
2. S. H. Salih, N. M. G. Al-Saidi, A. Malik, and S. J. Obaiys, “Analyzing Stability and Controlling Chaos in a Unique Host Parasitoid Discrete Dynamical System with Applications in Artificial Intelligence,” *Mathematical Modelling of Engineering Problems* 11 (2024), DOI 10.18280/mmep.110817.
3. Q. Din, “Global behavior of a host-parasitoid model under the constant refuge effect,” *Applied Mathematical Modelling* 40 (2016), 2815–2826, DOI 10.1016/j.apm.2015.09.012.
