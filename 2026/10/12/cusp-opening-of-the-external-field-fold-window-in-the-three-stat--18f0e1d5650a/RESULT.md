# Cusp opening of the external-field fold window in the three-state SOS tree model

## Finding

For the three-state solid-on-solid model with translation-invariant external field on the Cayley tree, use the source convention in which \(k\ge2\) and every vertex has \(k+1\) neighbours. On the translation-invariant branch \(z_0=1\), Rahmatullaev and Karshiboev reduce the boundary-law equation to
\[
a x=\left(\frac{1+x}{b+x}\right)^k,\qquad
a=\frac{2\theta^{k+1}}{\lambda},\qquad
b=\frac{1+\theta^2}{2\theta^2}.
\]
For
\[
\theta<\theta_c(k)=\frac{k-1}{\sqrt{k^2+6k+1}},
\]
their scalar equation has two folds, producing external-field thresholds \(\lambda_1^*(\theta)<\lambda_2^*(\theta)\).

The two fold curves meet at
\[
\boxed{\lambda_c(k)=2\left(\frac{k+1}{\sqrt{k^2+6k+1}}\right)^{k+1}}.
\]
Moreover, for every fixed integer \(k\ge2\),
\[
\boxed{
\lambda_2^*(\theta)-\lambda_1^*(\theta)
=
K_k\bigl(\theta_c(k)-\theta\bigr)^{3/2}
+O\!\left(\bigl(\theta_c(k)-\theta\bigr)^{5/2}\right)
}
\]
as \(\theta\uparrow\theta_c(k)\), where
\[
\boxed{
K_k=
\frac{\lambda_c(k)(k^2+6k+1)^{9/4}}
{3(k+1)^2\sqrt{k(k-1)}}
>0.
}
\]
At the meeting point the scalar equation has the triple positive root
\[
x_c=\frac{k+1}{k-1}.
\]

## Assumptions and scope

The Hamiltonian, temperature parameter \(\theta=e^{\beta J}\), external-field parameter \(\lambda\), and boundary-law normalization are exactly those of Rahmatullaev--Karshiboev. Only the always-present translation-invariant subbranch \(z_0=1\) is considered. The source's full two-variable boundary-law system can have additional solutions, especially in the binary-tree analysis, so the statement is not a global phase-diagram classification.

The big-\(O\) statement is for each fixed integer \(k\ge2\); no uniformity in \(k\) is claimed.

## Proof

Define
\[
F(x,b)=-\log x+k\log(1+x)-k\log(b+x).
\]
Thus \(F(x,b)=\log a\). The folds are the stationary points of \(F\) as a function of \(x\). The source gives their quadratic equation
\[
x^2+\bigl[2-(b-1)(k-1)\bigr]x+b=0
\]
and the critical value
\[
b_0=\left(\frac{k+1}{k-1}\right)^2.
\]
At \(b=b_0\) the two stationary roots coalesce at
\[
x_c=\frac{k+1}{k-1}.
\]
Since \(b_0=x_c^2\),
\[
a_c
=
\frac1{x_c}\left(\frac{1+x_c}{b_0+x_c}\right)^k
=
x_c^{-(k+1)}.
\]
Using \(a=2\theta^{k+1}/\lambda\) and
\[
\theta_c=\frac{k-1}{\sqrt{k^2+6k+1}},
\]
we obtain
\[
\lambda_c
=
\frac{2\theta_c^{k+1}}{a_c}
=
2\left(\frac{k+1}{\sqrt{k^2+6k+1}}\right)^{k+1}.
\]

For the opening law, put \(\varepsilon=b-b_0>0\). Direct differentiation at \((x_c,b_0)\) gives
\[
F_x=F_{xx}=0,\qquad
F_{xb}=
\frac{(k-1)^4}{4k(k+1)^2},
\qquad
F_{xxx}=
-\frac{(k-1)^4}{2k^2(k+1)^2}.
\]
The exact fold discriminant from the source is
\[
D=(b-1)(k-1)^2(b-b_0)
=
4k\varepsilon+(k-1)^2\varepsilon^2,
\]
hence the two stationary points satisfy
\[
x_{1,2}
=
x_c+\frac{k-1}{2}\varepsilon
\mp\sqrt{k\varepsilon}+O(\varepsilon^{3/2}).
\]
Expanding \(F_x\) around the cusp and integrating between the two stationary points yields
\[
F(x_2,b)-F(x_1,b)
=
\frac{(k-1)^4}{3\sqrt{k}(k+1)^2}\,
\varepsilon^{3/2}
+O(\varepsilon^{5/2}).
\]
For the remainder order, write \(r=\sqrt{\varepsilon}\). The exact quadratic formula has
\[
x_{1,2}=x_c+c_1r^2\mp r\sqrt{k+c_2r^2},
\]
with constants \(c_1,c_2\) depending only on \(k\). Hence
\[
F(x_2,b_0+r^2)-F(x_1,b_0+r^2)
\]
is an odd analytic function of \(r\). Since its linear term vanishes at the double stationary point, after the cubic term the next possible order is \(r^5=\varepsilon^{5/2}\).

Because
\[
\lambda_1^*=2\theta^{k+1}e^{-F(x_2,b)},
\qquad
\lambda_2^*=2\theta^{k+1}e^{-F(x_1,b)},
\]
the same leading logarithmic gap is multiplied by \(\lambda_c\). Finally,
\[
b(\theta)-b_0
=
\theta_c^{-3}\bigl(\theta_c-\theta\bigr)
+O\!\left((\theta_c-\theta)^2\right),
\]
so
\[
\lambda_2^*-\lambda_1^*
=
\lambda_c\,
\frac{(k-1)^4}{3\sqrt{k}(k+1)^2}
\theta_c^{-9/2}
\bigl(\theta_c-\theta\bigr)^{3/2}
+O\!\left((\theta_c-\theta)^{5/2}\right),
\]
which is the stated coefficient \(K_k\).

The vanishing of \(F_x\) and \(F_{xx}\), together with \(F_{xxx}\ne0\), also shows that the scalar boundary-law equation has a triple root at the cusp.

## Verification

The accompanying `verify.py` checks, using only the Python standard library, the exact rational identities defining \(b_0\), \(x_c\), \(F_{xb}\), \(F_{xxx}\), and the relation \(-2F_{xb}/F_{xxx}=k\) for many integer values of \(k\). It also evaluates the source's exact fold formulas near \(\theta_c\) for representative degrees and confirms convergence of
\[
\frac{\lambda_2^*(\theta)-\lambda_1^*(\theta)}
{K_k(\theta_c-\theta)^{3/2}}
\]
to \(1\). These finite checks are corroborative; the proof above is analytic for every fixed integer \(k\ge2\).

For \(k=2\),
\[
\lambda_c(2)=\frac{54\sqrt{17}}{289},
\qquad
K_2=\sqrt{2}\,17^{3/4},
\]
which independently matches the exact endpoint obtained by expanding the source's explicit binary-tree formulas.

## Relationship to prior work

Rahmatullaev--Karshiboev derive the scalar equation, the critical temperature \(\theta_c(k)\), and the two fold fields \(\lambda_1^*(\theta)\), \(\lambda_2^*(\theta)\). Their general-\(k\) statement leaves the fold meeting point in the implicit \(a_i,x_i\) representation. In the special case \(k=2\), they separately compute the common endpoint \(54\sqrt{17}/289\) and identify a triple solution.

The result above supplies the general exact cusp field and the all-\(k\) \(3/2\)-opening law with explicit amplitude. A related Potts-model paper by Bogachev--Rozikov develops external-field phase diagrams and explicitly uses cusp terminology for a different interaction, but it does not imply this SOS boundary-law coefficient. A later paper by Karshiboev treats periodic Gibbs measures for the same SOS interaction; its stated results concern the translation-invariant-versus-two-periodic classification rather than the local opening of the translation-invariant fold window.

## Limitations

The result does not classify all translation-invariant solutions of the full two-variable system, does not address nontranslation-invariant solutions, and does not establish extremality, stability, or thermodynamic dominance. Generic cusp theory makes a \(3/2\) opening plausible, but the exact coefficient above depends on the specific SOS scalar reduction and must be derived from it. An equivalent calculation could exist in weakly indexed literature under different boundary-law coordinates.

## References

1. M. M. Rahmatullaev and O. Sh. Karshiboev, “Gibbs measures for SOS models with external field on a Cayley tree,” arXiv:2110.00730, first public 2 October 2021; journal version: “Gibbs measures for the three-state SOS model with external field on a Cayley tree,” *Positivity* 26, 74 (2022), DOI 10.1007/s11117-022-00940-y.
2. L. V. Bogachev and U. A. Rozikov, “On the uniqueness of Gibbs measure in the Potts model on a Cayley tree with external field,” *J. Stat. Mech.* (2019) 073205, arXiv:1903.11440.
3. O. Sh. Karshiboev, “Periodic Gibbs measures for the three-state SOS model on a Cayley tree with a translation-invariant external field,” *Theor. Math. Phys.* 212 (2022), 1276–1283, DOI 10.1134/S0040577922090094.
