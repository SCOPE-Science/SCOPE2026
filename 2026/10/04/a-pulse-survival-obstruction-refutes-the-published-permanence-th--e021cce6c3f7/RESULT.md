# A pulse-survival obstruction refutes the published permanence theorem for an impulsive mackerel model

## Finding

Consider the impulsive prey-predator fishery model
\[
\dot x_1
=
x_1\left(
a_1-d_1
-\left(\frac{a_1}{k_1}+u_1\right)x_1
-\frac{b x_2}{k_2+x_1}
\right),
\]
\[
\dot x_2
=
x_2\left(
B+\frac{rbx_1}{k_2+x_1}-Ax_2
\right),
\qquad t\ne nT,
\]
with
\[
x_1(nT^+)=(1-\gamma)x_1(nT),
\qquad
x_2(nT^+)=(1-\omega)x_2(nT),
\]
where
\[
A=\frac{a_2}{k_3}+u_2,
\qquad
B=a_2-d_2.
\]

Theorem 3.8 of the source gives sufficient conditions for permanence, meaning that both populations eventually remain between fixed positive lower and upper bounds. Those stated conditions are not sufficient.

A necessary condition for permanence of the short-mackerel population is
\[
(1-\omega)e^{(B+rb)T}>1.
\]
If this condition fails, then
\[
x_2(t)\to0
\]
for every positive initial condition.

Using the source's own biological parameter values
\[
a_1=a_2=20,\quad
b=0.1,\quad
d_1=0.2,\quad
d_2=0.4,\quad
k_1=0.2,\quad
k_2=0.6,\quad
k_3=0.3,\quad
r=0.5,\quad
u_1=u_2=0.1
\]
and choosing
\[
\gamma=0.1,\qquad
\omega=0.5,\qquad
T=0.01,
\]
all hypotheses explicitly listed in Theorem 3.8 are satisfied, but
\[
(1-\omega)e^{(B+rb)T}
=
\frac12e^{0.1965}
\approx0.6085676604<1.
\]
Therefore the short-mackerel population tends to zero and the system is not permanent. This is a direct counterexample to the published theorem.

The proof also reveals the missing biological constraint: repeated harvesting must leave enough short mackerel after one period to overcome even their maximal possible per-capita growth. The theorem's condition \(T>T_{\max}\) does not enforce that pulse-survival requirement.

## Assumptions and scope

All parameters are positive, with
\[
0<\gamma<1,\qquad 0<\omega<1,\qquad T>0.
\]
The result concerns the equations printed as (2.1)–(2.4) in the source and the permanence definition printed immediately before Theorem 3.8.

The counterexample uses the source's Table-1 biological parameters and changes only the admissible impulsive-control values \(\gamma,\omega,T\).

The result does not claim that every corrected permanence theorem must use exactly the necessary condition above as a sufficient condition. It proves that any valid permanence theorem for the printed system must exclude the regime
\[
(1-\omega)e^{(B+rb)T}\le1.
\]

## Proof

First, \(x_1\) is bounded independently of \(x_2\). Set
\[
c_1=a_1-d_1,
\qquad
C_1=\frac{a_1}{k_1}+u_1>0.
\]
Between impulses,
\[
\dot x_1
\le
c_1x_1-C_1x_1^2,
\]
and each impulse decreases \(x_1\). Hence every positive solution has a finite upper bound
\[
x_1(t)\le M
\]
for all sufficiently large \(t\), and one may take a bound derived from the scalar logistic comparison.

For the short-mackerel equation,
\[
0\le
\frac{rbx_1}{k_2+x_1}
<rb.
\]
Therefore
\[
\dot x_2
\le
(B+rb)x_2
\]
between impulses. Let
\[
q=(1-\omega)e^{(B+rb)T}.
\]
For every integer \(n\),
\[
x_2((n+1)T^+)
\le
q\,x_2(nT^+).
\]
If \(q<1\), iteration gives geometric decay of the pulse values, and the same differential inequality bounds the between-pulse values. Thus
\[
x_2(t)\to0.
\]

If \(q=1\), use the eventual bound \(x_1\le M\). Then
\[
\frac{rbx_1}{k_2+x_1}
\le
\frac{rbM}{k_2+M}
=:rb-\eta
\]
with \(\eta>0\). For all sufficiently large pulse intervals,
\[
x_2((n+1)T^+)
\le
(1-\omega)e^{(B+rb-\eta)T}x_2(nT^+),
\]
and the multiplier is strictly below one. Again \(x_2(t)\to0\).

Consequently permanence requires
\[
(1-\omega)e^{(B+rb)T}>1.
\]

Now evaluate the hypotheses of the source theorem. For its Table-1 biological parameters,
\[
A=\frac{2003}{30},
\qquad
B=\frac{98}{5},
\qquad
M_3=\frac{rb}{k_2}=\frac1{12},
\]
and
\[
\frac{b}{k_2A}=\frac5{2003}.
\]
With
\[
\gamma=\frac1{10},
\qquad
\omega=\frac12,
\qquad
T=\frac1{100},
\]
condition (3.2) is
\[
\frac25>\frac1{12},
\]
condition (3.6) is \(20>0.4\), and condition (3.11) is
\[
20>
\frac15+\frac{98}{2003}.
\]
Condition (3.12) becomes
\[
\log\!\left(\frac{10}{9}\right)
>
\frac5{2003}\log 2.
\]
The source defines
\[
T_{\max}
=
\frac{
\log(10/9)-(5/2003)\log2
}{
99/5-98/2003
}
\approx0.0052468158,
\]
so
\[
T=0.01>T_{\max}.
\]
Finally,
\[
A=\frac{2003}{30}
>
\frac{98}{5}+\frac1{12}
=
B+M_3.
\]
Thus every listed hypothesis of Theorem 3.8 holds.

Nevertheless,
\[
q
=
\frac12
\exp\!\left[
\left(\frac{98}{5}+\frac1{20}\right)\frac1{100}
\right]
=
\frac12e^{393/2000}
\approx0.6085676604<1.
\]
The first part of the proof therefore gives
\[
x_2(t)\to0,
\]
which contradicts the positive lower bound required by permanence.

There is also an independent algebraic mismatch in the published comparison argument. The model contains
\[
\frac{rbx_1}{k_2+x_1},
\]
whose exact supremum over \(x_1\ge0\) is \(rb\). Lemma 3.4 instead defines
\[
M_3
=
\sup_{x_1\ge0}
\frac{rbx_1}{1+k_2x_1}
=
\frac{rb}{k_2}.
\]
These are different functions. When \(k_2>1\), the printed \(M_3\) is even smaller than the true supremum of the model's gain term and therefore cannot serve as its global upper bound.

## Verification

The bundled `verify.py` evaluates every stated hypothesis of Theorem 3.8 for the counterexample and verifies
\[
T_{\max}<T.
\]
It also computes the pulse-survival multiplier
\[
q=(1-\omega)e^{(B+rb)T}
\]
and confirms
\[
q\approx0.6085676604<1.
\]

The extinction conclusion itself is analytic: it follows from a scalar pulse-to-pulse inequality and does not depend on finite simulation.

## Relationship to prior work

Prathumwan, Trachoo, Maiaugree, and Chaiya (2021), DOI 10.3934/math.2022001, define the exact impulsive fishery system considered here. Their Theorem 3.8 states permanence under conditions (3.2), (3.6), (3.11), (3.12), \(T>T_{\max}\), and \(A>B+M_3\). The proof first invokes a positive impulsive logistic comparison for \(x_2\), but the theorem statement does not require the lower-period condition needed for that comparison to have a positive periodic state.

Banerjee and Das (2016), DOI 10.1155/2016/9268257, analyze a different impulsive two-prey/one-predator model. Their full text treats boundedness, uniform persistence, and eradication thresholds through comparison systems and Floquet theory. It does not contain the present mackerel model, the pulse-survival obstruction above, or this counterexample.

Song and Li (2007), DOI 10.1016/j.chaos.2006.01.019, study another Holling-II impulsive two-prey/one-predator system and report critical impulse periods separating eradication and permanence. The accessible abstract supports the general relevance of pulse-period thresholds but does not imply the source-specific necessary condition or counterexample proved here.

## Limitations

The result refutes Theorem 3.8 as stated; it does not give a complete replacement set of sufficient conditions for permanence.

The strict condition
\[
(1-\omega)e^{(B+rb)T}>1
\]
is necessary, not claimed sufficient. Other mechanisms can still prevent permanence even when it holds.

The source's numerical examples use other control triples. This counterexample addresses the general theorem over its stated parameter domain rather than disputing those particular simulations.

## References

1. D. Prathumwan, K. Trachoo, W. Maiaugree, I. Chaiya, “Preventing extinction in Rastrelliger brachysoma using an impulsive mathematical model,” AIMS Mathematics 7 (2022), 1–24. DOI: 10.3934/math.2022001. First published 29 September 2021.
2. S. Banerjee, A. Das, “Impulsive Control on Seasonally Perturbed General Holling Type Two-Prey One-Predator Model,” Discrete Dynamics in Nature and Society (2016), Article 9268257. DOI: 10.1155/2016/9268257.
3. X. Song, Y. Li, “Dynamic complexities of a Holling II two-prey one-predator system with impulsive effect,” Chaos, Solitons & Fractals 33 (2007), 463–478. DOI: 10.1016/j.chaos.2006.01.019.
