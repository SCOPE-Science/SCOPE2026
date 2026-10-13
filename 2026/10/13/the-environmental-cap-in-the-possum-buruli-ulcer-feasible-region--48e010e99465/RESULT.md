# The environmental cap in the possum Buruli-ulcer feasible region is not invariant

## Finding

The model contains
\[
\dot E=\alpha_E I_m-\mu_EE
\]
and
\[
N_m=S_m+I_m.
\]
The source derives the mammal-population cap
\[
N_m\le
K_m:=
\frac{\Lambda_m}{\mu_m},
\]
but then defines its feasible region using
\[
E\le
E_{\mathrm{pub}}
:=
\frac{\alpha_E}{\mu_E}
\]
after writing
\[
\dot E
\le
\alpha_E-\mu_EE.
\]

That last inequality silently requires
\[
I_m\le1.
\]
The model has no such normalization. Its own admissible mammal range is instead
\[
0\le I_m\le K_m.
\]

For a rectangular cap \(E\le H\), the exact uniform inward-pointing condition is
\[
H\ge
H_*:=
\frac{\alpha_EK_m}{\mu_E}
=
\frac{\alpha_E\Lambda_m}{\mu_E\mu_m}.
\]
Therefore the published cap is positively invariant exactly in the special normalized regime
\[
\frac{\Lambda_m}{\mu_m}\le1.
\]

For the source's Table 1 parameters,
\[
\Lambda_m=2,\qquad
\mu_m=\frac1{365\cdot60},\qquad
\alpha_E=\mu_E=\frac1{14},
\]
so
\[
K_m=43800,
\qquad
E_{\mathrm{pub}}=1,
\qquad
H_*=43800.
\]

The state
\[
(S_m,I_m,S_v,I_v,E)
=
(1,2,1,1,1)
\]
is inside the source's stated population bounds, but
\[
\dot E
=
\frac1{14}>0
\]
on the boundary \(E=1\). Hence the trajectory immediately leaves the published feasible region.

A corrected positively invariant rectangular region uses
\[
E\le
\frac{\alpha_E\Lambda_m}{\mu_E\mu_m}.
\]

## Assumptions and scope

All demographic, shedding, and decay parameters are positive, as in the source model.

The claim concerns the source's rectangular feasible region and its positive invariance. It uses the mammal-population cap that the source derives immediately before defining that region.

The correction does not assert that the environmental variable reaches the corrected upper bound on a typical trajectory. It identifies the smallest constant \(E\)-height that guarantees inward pointing for every state allowed by the source's mammal cap.

The result does not independently reassess the local or global stability theorems later in the article.

## Proof

Write
\[
K_m=\frac{\Lambda_m}{\mu_m}.
\]
From the first two model equations,
\[
\dot N_m
=
\Lambda_m-\mu_mN_m-\delta_mI_m.
\]
Thus on the boundary
\[
N_m=K_m,
\]
\[
\dot N_m
=
-\delta_mI_m
\le0.
\]
Consequently
\[
0\le I_m\le K_m
\]
throughout the mammal-bounded rectangle.

Now consider a constant environmental top face
\[
E=H.
\]
There,
\[
\dot E
=
\alpha_EI_m-\mu_EH.
\]
This is nonpositive for every admissible infected-mammal value
\[
0\le I_m\le K_m
\]
if and only if its maximum over that interval is nonpositive:
\[
\alpha_EK_m-\mu_EH\le0.
\]
Equivalently,
\[
H\ge
\frac{\alpha_EK_m}{\mu_E}.
\]
This proves both sufficiency and necessity for a rectangular cap.

The source chooses
\[
H=E_{\mathrm{pub}}=\frac{\alpha_E}{\mu_E}.
\]
Substitution gives the worst-case boundary derivative
\[
\alpha_EK_m-\mu_EE_{\mathrm{pub}}
=
\alpha_E(K_m-1).
\]
Hence the source cap is uniformly inward-pointing exactly when
\[
K_m\le1.
\]

For the Table 1 values,
\[
K_m
=
2\cdot365\cdot60
=
43800.
\]
Because
\[
\alpha_E=\mu_E=\frac1{14},
\]
the published environmental cap is \(1\), while the minimal rectangular cap is \(43800\).

At
\[
(S_m,I_m,S_v,I_v,E)=(1,2,1,1,1),
\]
the mammal total is \(3<43800\). The source also has
\[
\frac{\Lambda_v}{\mu_v}
=
\frac5{1/14}
=
70,
\]
so the vector total \(2\) is within the vector-population cap established immediately before the feasible region. Finally,
\[
\dot E
=
\frac{2}{14}-\frac1{14}
=
\frac1{14}>0.
\]
Thus this admissible boundary point exits the published region instantly.

For the corrected top face
\[
E=H_*=
\frac{\alpha_EK_m}{\mu_E},
\]
one has
\[
\dot E
\le
\alpha_EK_m-\mu_EH_*
=
0.
\]
Together with the source's population-cap calculations and nonnegativity of the coordinate faces, this supplies the corrected rectangular invariant domain.

## Verification

The bundled `verify.py` checks the general top-face algebra symbolically and replays the Table 1 counterexample with exact rational arithmetic.

It verifies
\[
K_m=43800,
\qquad
\frac{\Lambda_v}{\mu_v}=70,
\qquad
E_{\mathrm{pub}}=1,
\qquad
H_*=43800,
\]
and
\[
\dot E(1,2,1,1,1)=\frac1{14}>0.
\]

It also verifies symbolically that the maximum environmental boundary derivative at the published cap is
\[
\alpha_E(K_m-1),
\]
while the maximum derivative at the corrected cap is exactly zero.

No simulation or finite parameter scan is used to prove the result.

## Relationship to prior work

Khan, Bonyah, Li, Muhammad, and Okosun define the target possum–vector–environment model and explicitly claim that the region with
\[
E\le\frac{\alpha_E}{\mu_E}
\]
is positively invariant and is the domain in which the model is epidemiologically and mathematically well posed. The same article later invokes that feasible region in its global disease-free stability discussion.

Earlier Buruli-ulcer modeling by Bonyah, Dontwi, and Nyabadza also treats an environmental bacterial compartment, but with its own bounded environmental dynamics and carrying-capacity structure. That model does not imply the incorrect unit-scale cap used in the possum model.

A closely related 2021 possum paper by Chu and coauthors was inspected at its article record and available preprint metadata because its title and authorship overlap strongly with the target model. The accessible material did not expose a published correction of the environmental cap. Full equation-level comparison could not be completed through the available source, so it remains an explicit residual literature risk rather than evidence of noncoverage.

Targeted searches by the target DOI, exact title, invariant-region language, the environmental equation, and correction or erratum terminology did not locate a published correction of this source-specific feasible-region claim.

## Limitations

The corrected height is the smallest constant cap that works uniformly over the source's mammal rectangle. A smaller absorbing set could be obtainable by exploiting coupled dynamics more sharply than a rectangular estimate.

The finding corrects the feasible-region argument and does not by itself prove or disprove the later equilibrium and stability theorems.

A closely related possum-model publication from 2021 could not be inspected equation by equation through the available source and therefore remains a residual comparison risk.

## References

1. M. A. Khan, E. Bonyah, Y.-X. Li, T. Muhammad, K. O. Okosun, “Mathematical modeling and optimal control strategies of Buruli ulcer in possum mammals,” AIMS Mathematics 6 (2021), 9859–9881. DOI: 10.3934/math.2021572.
2. E. Bonyah, I. Dontwi, F. Nyabadza, “A Theoretical Model for the Transmission Dynamics of the Buruli Ulcer with Saturated Treatment,” Computational and Mathematical Methods in Medicine (2014), Article 576039. DOI: 10.1155/2014/576039.
3. Y.-M. Chu, M. Farhan, Fatmawati, M. A. Khan, M. Y. Alshahrani, T. Muhammad, S. Islam, “Mathematical modeling and stability analysis of Buruli ulcer in Possum mammals,” Results in Physics 27 (2021), 104471. DOI: 10.1016/j.rinp.2021.104471.
