# The canonical \(K\)-dual norm theorem has a reciprocal constant and nonunique minimizers

## Finding
Theorem 2.4 of Li--Leng--Huang states that if a \(K\)-\(g\)-frame \(\Lambda\) has optimal lower frame bound \(A\), then every \(K\)-dual Bessel \(g\)-sequence \(\Gamma\) satisfies
\[
A\le\|T_\Gamma\|^2,
\]
and that there is a unique \(K\)-dual whose squared synthesis norm equals \(A\). Both assertions fail as written.

The correct universal norm floor is
\[
\boxed{\|T_\Gamma\|^2\ge A^{-1}}.
\]
A Douglas reduced \(K\)-dual attains \(A^{-1}\), but the full class of \(K\)-duals can contain many distinct minimizers with exactly that norm.

The normalization error is already visible in one dimension. Let
\[
H=\mathbb C,\qquad K=I,\qquad \Lambda_1=2I.
\]
Then
\[
\|\Lambda_1f\|^2=4\|f\|^2,
\]
so the optimal lower frame bound is \(A=4\). The duality equation forces
\[
\Gamma_1=\tfrac12I,
\]
and therefore
\[
\|T_\Gamma\|^2=\tfrac14=A^{-1},
\]
contradicting the printed inequality \(A\le\|T_\Gamma\|^2\).

The uniqueness clause also fails after correcting the reciprocal. On \(H=\mathbb C^2\), take
\[
F=(e_1,e_1,2e_2).
\]
Its frame operator is \(\operatorname{diag}(2,4)\), so its optimal lower bound is \(A=2\). For every real \(t\), define
\[
g_1(t)=\frac12e_1+te_2,\qquad
g_2(t)=\frac12e_1-te_2,\qquad
g_3(t)=\frac12e_2.
\]
Then \(G_t=(g_1(t),g_2(t),g_3(t))\) is a dual frame of \(F\), and
\[
S_{G_t}=\operatorname{diag}\left(\frac12,\frac14+2t^2\right).
\]
Consequently
\[
\|T_{G_t}\|^2=\frac12=A^{-1}
\]
for every
\[
|t|\le\frac1{2\sqrt2}.
\]
Thus there are infinitely many norm-minimizing duals. The Douglas reduced dual is the special member \(t=0\); uniqueness belongs to the reduced-solution condition, not to operator-norm minimization alone.

## Assumptions and scope
Let \(H\) be a complex Hilbert space, \(K\in\mathcal L(H)\), and let \(\Lambda=(\Lambda_i)\) be a \(K\)-\(g\)-frame with synthesis operator \(T_\Lambda\). Write
\[
S_\Lambda=T_\Lambda T_\Lambda^*.
\]
The optimal lower \(K\)-\(g\)-frame bound is
\[
A=\sup\{\lambda>0:\lambda KK^*\le S_\Lambda\}.
\]
A \(K\)-dual \(\Gamma\) is a Bessel \(g\)-sequence satisfying
\[
K=T_\Lambda T_\Gamma^*.
\]
These are exactly the Hilbert-space conventions used in the source.

The counterexamples are ordinary frames, viewed as scalar-valued \(g\)-frames, and take \(K=I\). They are therefore special cases of the theorem rather than changes of setting.

The repaired uniqueness statement is deliberately narrower than the printed one. Douglas factorization supplies a unique reduced factor after a range normalization. It does not imply that the factor of smallest operator norm is unique among all factors.

## Proof
Define
\[
\mu_0=\inf\{\mu>0:KK^*\le\mu S_\Lambda\}.
\]
For every \(\mu>0\),
\[
KK^*\le\mu S_\Lambda
\quad\Longleftrightarrow\quad
\mu^{-1}KK^*\le S_\Lambda.
\]
By optimality of \(A\), this gives
\[
\mu_0=A^{-1}.
\]
This is the reciprocal step that is reversed in the source proof.

Now let \(\Gamma\) be any \(K\)-dual. Since
\[
K=T_\Lambda T_\Gamma^*,
\]
we have
\[
KK^*
=T_\Lambda T_\Gamma^*T_\Gamma T_\Lambda^*
\le
\|T_\Gamma\|^2T_\Lambda T_\Lambda^*
=
\|T_\Gamma\|^2S_\Lambda.
\]
Therefore
\[
A^{-1}=\mu_0\le\|T_\Gamma\|^2.
\]
Douglas factorization gives a reduced solution \(C_0\) of \(K=T_\Lambda C\) satisfying
\[
\|C_0\|^2=\mu_0=A^{-1}.
\]
The corresponding reduced \(K\)-dual therefore attains the sharp bound.

For the scalar counterexample, \(\Lambda_1=2I\) has frame energy \(4\|f\|^2\), hence \(A=4\). The equation
\[
f=\Lambda_1^*\Gamma_1f=2\Gamma_1f
\]
forces \(\Gamma_1=\tfrac12I\). Its synthesis norm squared is \(1/4\), not \(4\).

For nonuniqueness, the frame \(F=(e_1,e_1,2e_2)\) satisfies
\[
\sum_{j=1}^3|\langle x,f_j\rangle|^2
=2|x_1|^2+4|x_2|^2,
\]
so \(A=2\). For the displayed \(G_t\), direct substitution gives
\[
\sum_{j=1}^3\langle x,g_j(t)\rangle f_j=x
\]
for every \(x\in\mathbb C^2\); hence every \(G_t\) is a dual. Its synthesis norm squared is the largest eigenvalue of its frame operator, and
\[
S_{G_t}
=g_1(t)g_1(t)^*+g_2(t)g_2(t)^*+g_3(t)g_3(t)^*
=\operatorname{diag}\left(\frac12,\frac14+2t^2\right).
\]
Thus \(\|T_{G_t}\|^2=1/2\) throughout the stated interval. Since the sharp lower bound is \(A^{-1}=1/2\), all those distinct duals are minimizers.

The analysis range of \(F\) is
\[
R(T_F^*)=\{(a,a,b):a,b\in\mathbb C\}.
\]
For \(t=0\), \(R(T_{G_0}^*)\subseteq R(T_F^*)\), whereas for \(t\ne0\) the first two coordinates of \(T_{G_t}^*e_2\) are \(t\) and \(-t\), so the inclusion fails. Hence the reduced-range condition distinguishes the Douglas solution even though the operator norm does not.

## Verification
The primary source was inspected at Lemma 1.7, Definition 2.1, Theorems 2.2--2.4, and Remark 2.5. Theorem 2.4 explicitly identifies
\[
A=\inf\{\mu:\|K^*f\|^2\le\mu\|T_\Lambda^*f\|^2\},
\]
although the left-hand optimal lower-bound definition makes the infimum equal to \(A^{-1}\). The same proof then transfers the uniqueness of the Douglas reduced factor to a uniqueness assertion for all \(K\)-duals having the displayed norm.

The scalar witness independently checks the reciprocal without relying on any nonstandard lemma. The two-dimensional witness independently checks the uniqueness issue by exact matrix algebra. The identity
\[
S_{G_t}=\operatorname{diag}\left(\frac12,\frac14+2t^2\right)
\]
was also symbolically recomputed from the three rank-one outer products.

No numerical sampling, finite exhaustive search, or timeout inference is used. The only general operator input is the standard Douglas factorization theorem already invoked by the source.

## Relationship to prior work
The paper's Lemma 1.7 states the Douglas factorization result with a unique reduced solution and the norm formula
\[
\|C_0\|^2=\inf\{\mu:BB^*\le\mu AA^*\}.
\]
That lemma supports the corrected value \(A^{-1}\), but its uniqueness concerns the reduced solution subject to the accompanying range/kernel normalization. It does not make every minimum-operator-norm factor unique.

A 2019 Hilbert \(C^*\)-module generalization reproduces the same reciprocal identification and the same uniqueness wording in its Theorem 3.2. A 2022 Hilbert \(C^*\)-module paper again reproduces the statement as Theorem 1.7. These later appearances show that the normalization issue propagated rather than being silently corrected.

Related later work on canonical \(K\)-dual generators studies minimal-norm representations and nonuniqueness of \(K\)-duals in other structured settings. The present claim is narrower: it corrects the exact theorem above, gives the sharp reciprocal constant, and separates uniqueness of the Douglas reduced dual from uniqueness of all operator-norm minimizers.

Targeted searches for the DOI, theorem number, reciprocal formulation, Douglas reduced-solution formulation, and nonunique minimum-norm duals did not locate an indexed published correction of Theorem 2.4. Closely related indexed findings concern weaving bounds, reconstruction ranges, perturbations, and other dual-frame optimization questions; none implies this source-specific correction.

## Limitations
The finding does not claim that canonical duals are never unique, nor that the Douglas reduced solution is nonunique. The reduced solution remains unique under its standard range normalization.

The counterexample only disproves uniqueness when the characterization is stated solely in terms of the synthesis-operator norm. Additional hypotheses can force uniqueness in special classes.

A residual literature risk remains that an unindexed erratum, thesis remark, or informal correction records the same reciprocal and uniqueness defects.

## References
1. D. Li, J. Leng and T. Huang, *Generalized frames for operators associated with atomic systems*, Banach Journal of Mathematical Analysis 12 (2018), 206--221, DOI 10.1215/17358787-2017-0050. First published online 5 December 2017. Theorem 2.4.
2. H. Labrigui, A. Touri and S. Kabbaj, *Some Generalizations of K-g-Frames in Hilbert C*-Module*, arXiv:1901.03703v1, 11 January 2019. Theorem 3.2.
3. H. Faraj, M. Rossafi, S. Kabbaj, H. Labrigui and A. Touri, *On the K-g-Frames in Hilbert C*-Modules*, Asian Journal of Mathematics and Applications (2022), article 10. Theorem 1.7.
