# The zero-saturation limit destroys the disease-free equilibrium in the printed COVID-19 model

## Finding

The printed SIS-B COVID-19 model contains the treatment transfer
\[
T_b(I)=\frac{aI}{b+I},
\]
where \(a>0\) is the maximum treatment capacity and \(b\) is the saturation parameter.

The source's Theorem 3.4 sets
\[
b=0
\]
and then claims that the disease-free equilibrium
\[
x_0=
\left(
\frac{A}{\mu_1+\gamma+\delta},
0,
0
\right)
\]
is globally asymptotically stable whenever
\[
\mathcal R_0<1.
\]

The specialization \(b=0\) is singular at the disease-free boundary.

For every \(b>0\),
\[
T_b(0)=0
\]
and
\[
T_b'(0)=\frac ab.
\]
For every fixed \(I>0\),
\[
\lim_{b\downarrow0}T_b(I)=a.
\]
Hence the pointwise limit that preserves the disease-free value is
\[
T_*(0)=0,
\qquad
T_*(I)=a
\quad
(I>0),
\]
which is discontinuous. The rational expression itself is undefined at
\[
b=I=0.
\]

Let
\[
k_2=\mu_1+\gamma+\delta,
\qquad
S_0=\frac{A}{k_2}.
\]
Along states with
\[
S=S_0,\qquad B=0,\qquad I>0,
\]
the \(b=0\) treatment is exactly \(a\). Taking \(I\downarrow0\) in the three printed equations gives
\[
(S',I',B')
\longrightarrow
(a,-a,0).
\]
Thus no continuous extension of the positive-\(I\) \(b=0\) vector field can make \(x_0\) an equilibrium.

If one instead defines
\[
T_0(0)=0
\]
by hand so that \(x_0\) remains a formal equilibrium, then the vector field is discontinuous at \(x_0\). The paper's classical continuously differentiable ODE framework, Jacobian calculation, next-generation linearization, and LaSalle argument are then unavailable at that point.

The contradiction also appears inside the source's own \(b=0\) rewriting. Equation (3.9) has a correction vector whose first component contains the constant \(a\). At
\[
(S,I,B)=(S_0,0,0)
\]
it gives
\[
M(S_0,0,0)=(a,0)^\mathsf T,
\]
so the printed infected subsystem has derivative
\[
(I',B')=(-a,0),
\]
rather than zero.

Finally, the paper's reproduction-number formula contains an explicit factor \(b\) in its numerator:
\[
\mathcal R_0=
\frac{A b\left(\varepsilon\pi+\beta(1-\delta)(1-\gamma)\mu_3\right)}
{\mu_3(\mu_1+\gamma+\delta)\left[b(\mu_2+\mu_I)+a\right]}.
\]
At fixed \(a>0\), setting \(b=0\) forces
\[
\mathcal R_0=0.
\]
That collapse is part of the same singular limit and cannot be interpreted as the reproduction number of a smooth disease-free linearization of the \(b=0\) system.

## Assumptions and scope

The claim assumes
\[
a>0.
\]
The remaining epidemiological parameters are in the nonnegative or positive ranges stated by the source, with
\[
\mu_1+\gamma+\delta>0.
\]

The finding concerns the exact ODE system printed by the source and its Theorem 3.4.

It does not claim that an idealized fixed-capacity treatment law is mathematically impossible. Such a law can be studied with an explicit boundary rule, a nonsmooth formulation, or another solution concept. Those are different mathematical models from the continuously differentiable system used in the source's analysis.

It also does not claim that backward bifurcation must persist under every regular unsaturated-treatment model. The conclusion is that the source's particular operation \(b=0\) at fixed \(a>0\) does not produce the smooth disease-free system required by its proof.

## Proof

For \(b>0\), define
\[
T_b(I)=\frac{aI}{b+I}.
\]
Then
\[
T_b(0)=0
\]
and
\[
T_b'(I)=\frac{ab}{(b+I)^2},
\]
so
\[
T_b'(0)=\frac ab.
\]

At each fixed \(I>0\),
\[
\lim_{b\downarrow0}T_b(I)=a,
\]
while
\[
T_b(0)=0
\]
for every \(b>0\). Therefore the pointwise limit is discontinuous at \(I=0\).

Now set
\[
S_0=\frac{A}{\mu_1+\gamma+\delta}.
\]
For \(b=0\) and \(I>0\), the transfer term simplifies to
\[
T_0(I)=a.
\]
At \(S=S_0\) and \(B=0\), the source's equations become
\[
S'
=
\frac{A}{1+\alpha I}
-\beta(1-\gamma)(1-\delta)S_0I
-(\mu_1+\gamma+\delta)S_0
+a,
\]
\[
I'
=
\beta(1-\gamma)(1-\delta)S_0I
-(\mu_2+\mu_I)I
-a,
\]
and
\[
B'=\varepsilon I.
\]
Since
\[
(\mu_1+\gamma+\delta)S_0=A,
\]
taking \(I\downarrow0\) gives
\[
S'\to a,
\qquad
I'\to-a,
\qquad
B'\to0.
\]

A continuous vector field agreeing with these positive-\(I\) values must therefore take value
\[
(a,-a,0)
\]
at \(x_0\), so \(x_0\) cannot be its equilibrium.

Conversely, assigning the treatment value \(0\) at \(I=0\) makes the right-hand side vanish at \(x_0\), but then the treatment function jumps from \(0\) to \(a\) immediately to the right. The vector field is not continuous, much less continuously differentiable.

The source's equation (3.9) reaches the same conclusion without taking a separate limit. Its infected correction term is
\[
M(S,I,B)
=
\begin{pmatrix}
[\beta(1-\gamma)(1-\delta)I+\pi B](S_0-S)+a\\
0
\end{pmatrix}.
\]
At \(x_0\),
\[
M(S_0,0,0)
=
\begin{pmatrix}
a\\
0
\end{pmatrix}.
\]
The remaining linear term vanishes at \(I=B=0\), so the printed right-hand side is
\[
(-a,0)^\mathsf T.
\]

For comparison, the standard smooth saturated-treatment form
\[
\frac{rI}{1+\sigma I}
\]
has the regular unsaturated limit
\[
\sigma\to0
\quad\Longrightarrow\quad
rI.
\]
For \(b>0\), the source's treatment can be reparameterized as
\[
\frac{aI}{b+I}
=
\frac{(a/b)I}{1+(1/b)I}.
\]
Thus fixed-\(a\) \(b\downarrow0\) is not the same regular limit: both corresponding coefficients diverge.

## Verification

The bundled `verify.py` uses symbolic algebra to verify four identities:

\[
\lim_{I\downarrow0}T_b(I)=0
\quad\text{for fixed }b>0,
\]
\[
\lim_{I\downarrow0}T_0(I)=a
\quad\text{on the positive-\(I\) branch},
\]
\[
\lim_{I\downarrow0}(S',I',B')
=
(a,-a,0)
\]
at \(S=S_0\), \(B=0\), and
\[
\lim_{b\to\infty}
\frac{rbI}{b+I}
=
rI.
\]

It also verifies that the source's displayed reproduction-number expression is identically zero after substituting \(b=0\) with \(a>0\).

These are exact symbolic checks; no finite simulation is used in the proof.

## Relationship to prior work

The motivating article explicitly defines the treatment transfer as
\[
aI/(b+I),
\]
states that its vector field is continuously differentiable, derives a disease-free equilibrium and reproduction number, and later sets \(b=0\) in Theorem 3.4 to claim global disease-free stability. Its own \(b=0\) equation (3.9) retains the constant \(a\) in the infected correction vector.

Earlier saturated-treatment literature uses regular forms such as
\[
rI/(1+\sigma I).
\]
Xiao, Deng, and Liu describe this treatment as continuous and differentiable, with \(r\) the cure rate and \(\sigma\) the saturation or delayed-treatment parameter; at \(\sigma=0\) it reduces to linear treatment.

That 2015 article cites Zhang and Liu's 2008 paper as an early source for the same smooth saturated-treatment form. The 2008 paper is therefore prior art for the regular treatment parameterization, not for the source-specific singularity identified here.

More general treatment-function literature likewise analyzes epidemic models by specifying treatment laws with well-defined behavior at the disease-free state. These works reinforce that the disease-free linearization depends on the local behavior of the treatment function, but they do not state the present source-specific contradiction.

Searches using the motivating DOI and title, the exact \(b=0\) specialization, the treatment formula, reproduction-number collapse, and correction or erratum terminology did not locate a published correction of Theorem 3.4.

## Limitations

A discontinuous or hybrid capacity-limited treatment model can be defined by adding an explicit rule at \(I=0\). The present result does not analyze such a reformulated system.

For each fixed \(b>0\), the source's rational treatment function is smooth at \(I=0\). The defect appears in the singular endpoint \(b=0\) used for Theorem 3.4.

A non-indexed author correction could exist outside the searched literature.

The full text of Zhang and Liu's 2008 paper was not available in the inspected open sources; its role here is limited to bibliographic provenance for the smooth saturated-treatment family. The 2015 open full text supplies the explicit formula and regularity comparison used in this report.

## References

1. A. A. Thirthar, H. Abboubakar, A. Khan, T. Abdeljawad, “Mathematical modeling of the COVID-19 epidemic with fear impact,” AIMS Mathematics 8 (2023), 6447–6465. DOI: 10.3934/math.2023326. Published 4 January 2023.
2. D. Xiao, G. Deng, Z. Liu, “Stability and Bogdanov-Takens Bifurcation of an SIS Epidemic Model with Saturated Treatment Function,” Mathematical Problems in Engineering 2015 (2015), 745732. DOI: 10.1155/2015/745732.
3. X. Zhang, X. Liu, “Backward bifurcation of an epidemic model with saturated treatment function,” Journal of Mathematical Analysis and Applications 348 (2008), 433–443. DOI: 10.1016/j.jmaa.2008.07.042.
4. S. Sharma, F. Singh, “Backward bifurcation in a cholera model with a general treatment function,” SN Applied Sciences 3 (2021), 235. DOI: 10.1007/s42452-021-04189-0.
