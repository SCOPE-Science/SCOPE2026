# The mean-square stability theorem analyzes a different SDE than the stochastic-immigration model

## Finding

The stochastic immigration model printed in Alebraheem, Mohammed, Tayel, and Aziz (2024) is
\[
dN_1=f_1(N_1,N_2)\,dt+\sigma_1(t,N_1)N_1\,dW_1,
\]
\[
dN_2=f_2(N_1,N_2)\,dt+\sigma_2(t,N_2)N_2\,dW_2,
\]
where
\[
\sigma_1(t,N_1)\in\left\{\epsilon,\frac{\epsilon}{N_1}\right\},
\qquad
\sigma_2(t,N_2)\in\left\{\delta,\frac{\delta}{N_2}\right\}.
\]

Let
\[
P^*=(N_1^*,N_2^*)
\]
be the positive deterministic equilibrium displayed in the paper. For every
\[
\epsilon>0,\qquad \delta>0,
\]
the point \(P^*\) is not an equilibrium of the original stochastic system in any of the four immigration cases.

The reason is structural. A constant solution of an Itô SDE must have both zero drift and zero diffusion. The deterministic drift vanishes at \(P^*\), but the original diffusion does not. In centered variables
\[
U_1=N_1-N_1^*,\qquad U_2=N_2-N_2^*,
\]
the four original diffusion vectors are

\[
G_{\mathrm I}(U)
=
\begin{pmatrix}
\epsilon(U_1+N_1^*)\\
\delta(U_2+N_2^*)
\end{pmatrix},
\]

\[
G_{\mathrm {II}}(U)
=
\begin{pmatrix}
\epsilon(U_1+N_1^*)\\
\delta
\end{pmatrix},
\]

\[
G_{\mathrm {III}}(U)
=
\begin{pmatrix}
\epsilon\\
\delta
\end{pmatrix},
\]

and

\[
G_{\mathrm {IV}}(U)
=
\begin{pmatrix}
\epsilon\\
\delta(U_2+N_2^*)
\end{pmatrix}.
\]

Every one of these is nonzero at \(U=0\) when the immigration intensities are positive.

Section 4 of the source instead writes the noise terms as
\[
\sigma_1(t,N_1)(N_1-N_1^*)\,dW_1,
\qquad
\sigma_2(t,N_2)(N_2-N_2^*)\,dW_2.
\]
Those coefficients vanish at \(P^*\). This is not the centered form of equations (2.1)–(2.2); it is a different stochastic differential equation. Therefore the source's Theorem 4.3 proves mean-square stability only for that altered equation and cannot supply the claimed small-immigration stability criterion for the original stochastic-immigration model.

There is an exact local quantitative obstruction. If the original process starts at \(P^*\), Itô's formula gives
\[
\mathbb E\|N_t-P^*\|^2
=
q\,t+o(t)
\qquad
(t\downarrow0),
\]
where
\[
q=
\begin{cases}
\epsilon^2(N_1^*)^2+\delta^2(N_2^*)^2,&\text{Case I},\\
\epsilon^2(N_1^*)^2+\delta^2,&\text{Case II},\\
\epsilon^2+\delta^2,&\text{Case III},\\
\epsilon^2+\delta^2(N_2^*)^2,&\text{Case IV}.
\end{cases}
\]
Each coefficient is strictly positive when \(\epsilon,\delta>0\).

For the paper's numerical parameter set,
\[
r=1.5,\quad k=3,\quad \alpha=2.5,\quad m=0.65,\quad c=0.75,\quad b=1.25,
\]
the deterministic equilibrium is
\[
N_1^*=\frac{101}{150},
\qquad
N_2^*=\frac{31}{75}.
\]
At the source's small-noise values
\[
\epsilon=0.25,\qquad \delta=0.12,
\]
the four exact short-time mean-square slopes are approximately
\[
0.0307962711,\quad
0.0427361111,\quad
0.0769,\quad
0.06496016.
\]

## Assumptions and scope

The claim concerns equations (2.1)–(2.4) and the Section-4 mean-square stability analysis exactly as printed.

A stochastic equilibrium here means a constant solution of the Itô SDE. This is the notion required by the source's own use of asymptotic mean-square stability of a trivial solution after centering.

The argument does not claim that the original process has no invariant probability distribution near the deterministic equilibrium. Persistent-noise systems can fluctuate around a deterministic equilibrium without converging to it in mean square. The finding is specifically that the deterministic point \(P^*\) is not an equilibrium of the original nonzero-noise SDE and therefore cannot have the asymptotic mean-square stability asserted by Theorem 4.3 for equations (2.1)–(2.2).

## Proof

The paper's deterministic drift vanishes at \(P^*\). The original stochastic coefficients, however, are
\[
g_1(N_1)=\sigma_1(t,N_1)N_1,
\qquad
g_2(N_2)=\sigma_2(t,N_2)N_2.
\]

For Case I,
\[
g_1(N_1^*)=\epsilon N_1^*,
\qquad
g_2(N_2^*)=\delta N_2^*.
\]

For Case II,
\[
g_1(N_1^*)=\epsilon N_1^*,
\qquad
g_2(N_2^*)=\delta.
\]

For Case III,
\[
g_1(N_1^*)=\epsilon,
\qquad
g_2(N_2^*)=\delta.
\]

For Case IV,
\[
g_1(N_1^*)=\epsilon,
\qquad
g_2(N_2^*)=\delta N_2^*.
\]

Since \(N_1^*,N_2^*,\epsilon,\delta\) are positive, none of these diffusion vectors vanishes. Thus the process started at \(P^*\) is not constant.

The correct centered form follows by substituting
\[
N_i=U_i+N_i^*
\]
into the original diffusion. For example, Case I gives
\[
\epsilon N_1\,dW_1
=
\epsilon(U_1+N_1^*)\,dW_1,
\]
not
\[
\epsilon U_1\,dW_1.
\]
For a proportional choice,
\[
\frac{\epsilon}{N_1}N_1\,dW_1
=
\epsilon\,dW_1,
\]
so centering leaves an additive noise, not a noise proportional to \(U_1\).

Section 4 instead inserts \(N_i-N_i^*\) directly into the stochastic term. This forces the noise to vanish at \(P^*\), which is exactly the property needed to create a trivial centered solution but is absent from the original model.

For the short-time calculation, set
\[
U_t=N_t-P^*
\]
and start from \(U_0=0\). Itô's formula gives
\[
d\|U_t\|^2
=
2U_t\cdot f(P^*+U_t)\,dt
+
\|G(P^*+U_t)\|^2\,dt
+
dM_t,
\]
where \(M_t\) is a local martingale. Taking expectations and using continuity of the coefficients,
\[
\frac{d}{dt}\mathbb E\|U_t\|^2\bigg|_{t=0+}
=
\|G(P^*)\|^2.
\]
This produces the four coefficients \(q\) stated above and proves
\[
\mathbb E\|U_t\|^2=q\,t+o(t).
\]

## Verification

The bundled script `verify.py` reconstructs the source's positive deterministic equilibrium from its formula and numerical parameters:
\[
N_1^*=\frac{101}{150},
\qquad
N_2^*=\frac{31}{75}.
\]

It then evaluates the four exact values of
\[
\|G(P^*)\|^2
\]
at
\[
\epsilon=\frac14,\qquad
\delta=\frac{3}{25},
\]
and verifies that all are strictly positive.

The general theorem is analytic. No finite simulation is used to infer the nonexistence of the deterministic point equilibrium.

## Relationship to prior work

The primary source, DOI 10.3934/math.2024725, prints the original stochastic immigration model in equations (2.1)–(2.4). It later states that it will study mean-square stability of those systems around their positive equilibrium but replaces the original factors \(N_i\) in the stochastic terms by \(N_i-N_i^*\) in equations (4.1)–(4.2). Its numerical discussion then interprets Theorem 4.3 as a stability criterion for systems (2.1)–(2.2).

Standard mean-square stability theory treats an equilibrium position only after both the drift and every diffusion coefficient vanish there. Senosiain and Tocino (2023), DOI 10.1007/s11075-022-01478-6, state this explicitly before defining stability in \(p\)-th mean and mean-square stability. Their work concerns general linear stochastic systems and does not identify the source-specific model switch above.

Exact-title, DOI, correction, equilibrium, and stochastic-immigration searches located the source and bibliographic mirrors but no published correction of equations (4.1)–(4.2).

## Limitations

The result does not establish a complete long-time classification of the original stochastic immigration model.

It does not rule out bounded moments, stochastic permanence, a stationary distribution, or concentration near \(P^*\) under small noise. Those are different questions from asymptotic mean-square stability of a deterministic point.

Theorem 4.3 may be mathematically relevant to the altered Section-4 SDE in which the noise is constructed to vanish at \(P^*\). The present finding is that this theorem does not apply to the original equations (2.1)–(2.2) as claimed.

## References

1. J. Alebraheem, M. Mohammed, I. M. Tayel, M. H. N. Aziz, “Stochastic prey-predator model with small random immigration,” AIMS Mathematics 9 (2024), 14982–14996. DOI: 10.3934/math.2024725.
2. M. J. Senosiain, A. Tocino, “A survey of mean-square destabilization of multidimensional linear stochastic differential systems with non-normal drift,” Numerical Algorithms 93 (2023), 1543–1559. DOI: 10.1007/s11075-022-01478-6.
