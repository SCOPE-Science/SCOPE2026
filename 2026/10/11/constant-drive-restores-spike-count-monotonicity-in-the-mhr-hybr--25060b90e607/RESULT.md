# Constant drive restores spike-count monotonicity in the MHR hybrid neuron
## Finding
Consider the Meng--Huguet--Rinzel hybrid neuron system under a constant input \(I(t)\equiv I_0\ge0\):
\[
\dot v=-v+v_{\mathrm{rest}}+I_0,\qquad
\dot\theta=\frac{f(v)-\theta}{\tau},
\]
where \(f(v)=a+\exp(b(v-c))\), \(a,b,c>0\), and \(\tau>1\). A reset is triggered exactly as in the source when \(h=\theta-v\) changes sign from the subthreshold side; at a reset,
\[
v^+=0,\qquad \theta^+=\theta^-+\Delta,\qquad \Delta>0.
\]
Write \(V=v_{\mathrm{rest}}+I_0\). Fix an initial voltage \(0\le v_0<V\). Then the total number of resets is a non-increasing function of the initial threshold. Precisely, if
\[
\theta_1>\theta_0>v_0
\]
and the trajectory from \((v_0,\theta_0)\) has exactly \(n<\infty\) resets, then the trajectory from \((v_0,\theta_1)\) has at most \(n\) resets. Moreover, whenever both trajectories have a \(k\)-th reset, its reset voltage is strictly larger for the trajectory started at \(\theta_1\).

Consequently, Conjecture 4.16 of arXiv:2609.32842v1 is true on the constant-drive subfamily under the paper's suggested restriction \(v_0<v_{\mathrm{rest}}+I_0\). The second suggested condition \(f(v)>v\) is not needed.

## Assumptions and scope
The statement uses the reset convention of Bartłomiejczyk, Belmonte-Beitia, and Signerska-Rynkowska: a contact with \(v=\theta\) causes a reset only when \(h=\theta-v\) changes sign; a grazing contact without a sign change is not counted. The source parameters satisfy \(v_{\mathrm{rest}}>0\), \(\Delta>0\), \(\tau>1\), and \(a,b,c>0\).

The input is constant. A constant function is periodic with every positive period, so this is a genuine subfamily of the source's periodic-input framework. The restriction \(0\le v_0<V\), where \(V=v_{\mathrm{rest}}+I_0\), guarantees that voltage is strictly increasing on every reset-free leg before it approaches \(V\). No claim is made here for nonconstant periodic forcing, where different spike times expose later legs to different forcing phases.

## Proof
Consider one reset-free leg starting at \((u,q)\) with \(0\le u<V\) and \(q>u\). Since
\[
\dot v=V-v,
\]
the voltage is strictly increasing and may be used as the independent variable until the next reset. Writing the threshold along the leg as \(\Theta_{u,q}(v)\), one obtains
\[
\frac{d\Theta}{dv}+\frac{\Theta}{\tau(V-v)}
=
\frac{f(v)}{\tau(V-v)}.
\]
Multiplication by \((V-v)^{-1/\tau}\) and integration from \(u\) to \(v\) gives
\[
\Theta_{u,q}(v)
=
\left(\frac{V-v}{V-u}\right)^{1/\tau}q
+
\frac{(V-v)^{1/\tau}}{\tau}
\int_u^v f(s)(V-s)^{-1-1/\tau}\,ds.
\]
Hence, for \(q_1>q_0\),
\[
\Theta_{u,q_1}(v)-\Theta_{u,q_0}(v)
=
\left(\frac{V-v}{V-u}\right)^{1/\tau}(q_1-q_0)>0
\]
for every \(u\le v<V\).

Define
\[
g_{u,q}(v)=\Theta_{u,q}(v)-v.
\]
Before the first reset on a leg, \(g_{u,q}\) is nonnegative; a reset occurs at the first zero at which its sign changes from positive to negative. If \(q_1>q_0\), then \(g_{u,q_1}(v)>g_{u,q_0}(v)\) for every \(v<V\). Therefore the higher-threshold leg cannot reset at a voltage at or below the first reset voltage of the lower-threshold leg. If both reset, its reset voltage is strictly larger for \(q_1\). If the lower-threshold leg never resets, then \(g_{u,q_0}\ge0\) for all finite times, so the higher-threshold leg never resets either.

At a reset with voltage \(r\), the post-reset state is
\[
(0,r+\Delta).
\]
Thus if two corresponding reset voltages satisfy \(r_1>r_0\), the next legs begin at the same voltage \(0\) with ordered thresholds \(r_1+\Delta>r_0+\Delta\). Because the forcing is constant, the dynamics of the next leg depends only on this post-reset state and not on the absolute reset time. The one-leg comparison therefore iterates: whenever both trajectories have a \(k\)-th reset, the higher-initial-threshold trajectory has strictly larger \(k\)-th reset voltage.

Now suppose the lower-initial-threshold trajectory has exactly \(n<\infty\) resets. If the higher-initial-threshold trajectory has fewer than \(n\), the claim is immediate. Otherwise, after their \(n\)-th resets the higher-threshold trajectory starts the next leg at the same voltage \(0\) and at a strictly larger threshold. The lower-threshold trajectory has no further reset, so the one-leg no-reset comparison implies that the higher-threshold trajectory also has no further reset. Hence it has at most \(n\) resets.

## Verification
The integrating-factor formula was differentiated back to the threshold equation. Its dependence on the initial threshold is exactly the positive factor
\[
\left(\frac{V-v}{V-u}\right)^{1/\tau},
\]
so the comparison does not depend on a numerical approximation or on an unproved sign condition for \(f(v)-v\). The reset step was checked against the source's sign-change convention: grazing zeros do not enter the induction because no reset is recorded there.

The only global step is induction over the reset sequence. It is valid specifically because constant forcing makes every post-reset leg autonomous; for nonconstant forcing, the same post-reset state reached at different times can see different input phases, and the argument does not apply.

## Relationship to prior work
Bartłomiejczyk, Belmonte-Beitia, and Signerska-Rynkowska prove in Proposition 4.14 of arXiv:2609.32842v1 only the zero-spike case: increasing the initial threshold cannot create a reset when the lower-threshold trajectory has none. They then state Conjecture 4.16 asserting monotonicity of the total spike count for arbitrary finite counts and note that extra assumptions such as \(v_0<v_{\mathrm{rest}}+A\) or \(f(v)>v\) might be needed. The present argument proves the full finite-count monotonicity on the constant-drive subfamily under the analogous voltage restriction and shows that the second suggested condition is unnecessary there.

Meng, Huguet, and Rinzel introduced the underlying dynamic-threshold reduced model and its post-spike threshold increment in their 2012 Type III excitability study. Available primary-source material for that paper describes steady-current phasic behavior and the reset mechanism but does not state the reset-count ordering proved here.

## Limitations
The proof does not establish Conjecture 4.16 for genuinely time-dependent periodic inputs. Its key induction uses autonomy after each reset, and that property is lost when the forcing phase changes with the reset time. The initial-voltage condition \(v_0<V\) is essential to this proof because it makes voltage a strictly increasing coordinate on the first leg. No claim is made for initial voltages \(v_0\ge V\).

A bounded literature search did not locate an implication-equivalent theorem under adaptive-threshold or integrate-and-fire terminology. An equivalent older comparison result may nevertheless exist under different terminology; this is the principal residual originality risk.

## References
1. P. Bartłomiejczyk, J. Belmonte-Beitia, and J. Signerska-Rynkowska, “Subthreshold oscillations and spiking in hybrid neuron models with a dynamic threshold,” arXiv:2609.32842v1, first public 2026-09-26. See equations (5)--(8), Proposition 4.14, Lemma 4.15, and Conjecture 4.16.
2. X. Meng, G. Huguet, and J. Rinzel, “Type III excitability, slope sensitivity and coincidence detection,” Discrete and Continuous Dynamical Systems 32 (2012), 2729--2757, DOI 10.3934/dcds.2012.32.2729.
