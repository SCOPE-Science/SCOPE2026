# Two-scale low-temperature crossover in field-induced entanglement of a three-qubit XXX ring

## Finding

Consider the periodic antiferromagnetic three-qubit \(XXX\) ring with exchange \(J>0\), uniform field \(B\), and temperature \(T>0\). Let \(C(T,B)\) be the concurrence of any reduced pair. Following the source notation, set
\[
q=e^{3J/T},
\qquad
q_0=4+3\sqrt2.
\]

The source's exact entanglement condition implies that no field can produce pairwise thermal entanglement when
\[
q\le q_0.
\]
Equivalently, there is a temperature ceiling
\[
T_*=\frac{3J}{\log(4+3\sqrt2)}.
\]
For
\[
0<T<T_*,
\]
the source condition is equivalent to a single activation threshold
\[
B_*(T)=
\frac{T}2
\operatorname{arcosh}\!\left(
\frac{(q+2)^2}{q^2-8q-2}
\right),
\]
with
\[
C(T,B)>0
\quad\Longleftrightarrow\quad
|B|>B_*(T).
\]
This exact threshold is a direct rewriting of the published condition and is included only to state the domain of the new asymptotic result.

The first new scale is the low-field activation layer:
\[
\boxed{
B_*(T)\sim
\sqrt6\,T e^{-3J/(2T)}
}
\qquad
(T\downarrow0).
\]
Thus an arbitrarily small but nonzero fixed field eventually lies above the activation threshold, whereas the exactly zero-field Gibbs state remains unentangled.

The second scale occurs around the zero-temperature saturation transition
\[
B_c=\frac{3J}2.
\]
For every fixed
\[
s\in\mathbb R,
\]
the concurrence has the universal boundary-layer limit
\[
\boxed{
\lim_{T\downarrow0}
C\!\left(
T,\frac{3J}2+sT
\right)
=
\frac{2}{3(2+e^{2s})}.
}
\]
This profile interpolates continuously between the source's three zero-temperature limits. In particular,
\[
s\to-\infty
\quad\Longrightarrow\quad
C\to\frac13,
\]
\[
s=0
\quad\Longrightarrow\quad
C\to\frac29,
\]
and
\[
s\to+\infty
\quad\Longrightarrow\quad
C\to0.
\]

For every fixed field strictly above saturation,
\[
B>\frac{3J}2,
\]
the same low-temperature analysis gives the Arrhenius law
\[
\boxed{
C(T,B)
\sim
\frac23
e^{-2(B-3J/2)/T}
}
\qquad
(T\downarrow0).
\]
For every fixed field satisfying
\[
0<|B|<\frac{3J}2,
\]
one instead has
\[
C(T,B)\to\frac13.
\]

Hence two parametrically different field scales coexist as \(T\downarrow0\): an exponentially narrow scale
\[
B_*(T)\asymp T e^{-3J/(2T)}
\]
where entanglement first switches on, and a linear scale
\[
B-\frac{3J}2=O(T)
\]
where its magnitude crosses from the entangled ground-state value to an exponentially activated high-field tail.

## Assumptions and scope

The Hamiltonian is the periodic three-site \(XXX\) specialization of the source's \(XXZ\) ring with a uniform \(z\)-directed magnetic field. The exchange is antiferromagnetic,
\[
J>0.
\]
Boltzmann's constant is one.

The concurrence is the Wootters concurrence of any two-site reduced density matrix. Periodicity and permutation symmetry make all pairs equivalent in this isotropic three-site model.

The activation formula is not asserted as new; it is an explicit inversion of the source's published field criterion. The new claim consists of its exponentially small low-temperature scale and the distinct \(O(T)\) universal saturation crossover.

The limits keep \(J\) fixed. The double-scaling limit keeps \(s\) fixed while
\[
B=\frac{3J}2+sT
\]
and \(T\downarrow0\).

## Proof

For the \(XXX\) specialization, write
\[
x=\frac JT,
\qquad
b=\frac{|B|}T,
\qquad
q=e^{3x},
\qquad
A=2q+1.
\]
The source's reduced-state formula becomes
\[
u=
\frac32 e^{3b}
+
\frac12 A e^b,
\]
\[
v=
\frac32 e^{-3b}
+
\frac12 A e^{-b},
\]
\[
y=-(q-1)\cosh b,
\]
and
\[
Z=
2\cosh(3b)+2A\cosh b.
\]
Therefore
\[
C(T,B)
=
\frac{4}{3Z}
\left[
(q-1)\cosh b-\sqrt{uv}
\right]_+.
\]

The source also gives the exact sign condition
\[
\cosh(2b)>
\frac{(q+2)^2}{q^2-8q-2}.
\]
The denominator is positive exactly when
\[
q>q_0=4+3\sqrt2.
\]
Since \(\cosh(2b)\) is strictly increasing for \(b>0\), inversion gives the stated unique activation threshold.

For the low-temperature activation scale, define
\[
R(q)=
\frac{(q+2)^2}{q^2-8q-2}.
\]
As \(q\to\infty\),
\[
R(q)
=
1+\frac{12}q+O(q^{-2}).
\]
Using
\[
\operatorname{arcosh}(1+\epsilon)
=
\sqrt{2\epsilon}\,[1+O(\epsilon)]
\]
gives
\[
B_*(T)
=
\frac T2
\sqrt{\frac{24}q}\,[1+O(q^{-1})]
=
\sqrt6\,T e^{-3J/(2T)}[1+o(1)].
\]

Now examine the saturation field. Put
\[
b=\frac32x+s
\]
with fixed \(s\in\mathbb R\) and send \(x\to\infty\). Then
\[
Z
=
e^{(9/2)x+s}
\left(
e^{2s}+2+o(1)
\right),
\]
and
\[
|y|
=
\frac12
e^{(9/2)x+s}
[1+o(1)].
\]
Meanwhile
\[
u
=
e^{(9/2)x+s}
\left(
1+\frac32e^{2s}+o(1)
\right),
\]
\[
v
=
e^{(3/2)x-s}
[1+o(1)],
\]
so
\[
\sqrt{uv}
=
e^{3x}
\sqrt{1+\frac32e^{2s}}\,[1+o(1)].
\]
Consequently
\[
\frac{\sqrt{uv}}{|y|}
\to0.
\]
The positive part is therefore eventually inactive, and substitution gives
\[
C
\to
\frac{4}3
\frac{1/2}{e^{2s}+2}
=
\frac{2}{3(2+e^{2s})}.
\]

For fixed
\[
B>\frac{3J}2,
\]
one has
\[
3b>3x+b.
\]
Hence
\[
Z\sim e^{3b},
\qquad
|y|\sim\frac12e^{3x+b},
\qquad
\sqrt{uv}=o(|y|),
\]
which yields
\[
C(T,B)
\sim
\frac23e^{3x-2b}
=
\frac23e^{-2(B-3J/2)/T}.
\]

For fixed
\[
0<B<\frac{3J}2,
\]
the other partition-function term dominates:
\[
Z\sim2e^{3x+b},
\qquad
|y|\sim\frac12e^{3x+b},
\qquad
\sqrt{uv}=o(|y|),
\]
and therefore
\[
C(T,B)\to\frac13.
\]
At equality
\[
B=\frac{3J}2,
\]
the boundary-layer formula with \(s=0\) gives
\[
C\to\frac29.
\]

## Verification

`verify_three_qubit_xxx_boundary_layers.py` reconstructs the full \(8\times8\) thermal density matrix from the periodic \(XXX\) Hamiltonian, traces out one qubit, and computes Wootters concurrence directly.

It compares the direct matrix result with the source closed form on a deterministic grid of fields and temperatures. It also checks the exact activation threshold, the low-field asymptotic
\[
B_*(T)\sim\sqrt6\,T e^{-3J/(2T)},
\]
the universal saturation profile, and the fixed high-field Arrhenius law.

The numerical replay is supplementary. The asymptotic statements are proved analytically above.

## Relationship to prior work

Wang, Fu, and Solomon derive the reduced density matrix, concurrence, exact finite-temperature field condition, and the three zero-temperature values for the periodic three-qubit \(XXZ\) model. Their \(XXX\) analysis establishes magnetic-field-induced entanglement and identifies the zero-temperature transition at
\[
|B|=\frac{3J}2.
\]
The exact activation threshold written above is simply their field inequality solved for \(|B|\).

The new point is the singular way in which the positive-temperature field diagram approaches those zero-temperature limits. The activation threshold near zero field is exponentially smaller than \(T\), while the saturation transition is rounded on the linear \(O(T)\) field scale with an explicit universal profile.

Jafari and Langari later analyze three-qubit \(XXZ\) and Ising models with Dzyaloshinskii--Moriya interactions. Their magnetic-field section concerns the Ising--DM model and does not supply the periodic \(XXX\) boundary-layer profile above.

Yang and Zhou study an open three-qubit chain in a nonuniform magnetic field. That geometry and field pattern differ from the periodic uniform-field ring, and their reported thresholds do not imply the two-scale asymptotics here.

Targeted searches for the saturation scaling variable
\[
\frac{B-3J/2}T,
\]
the profile
\[
\frac{2}{3(2+e^{2s})},
\]
and the exponentially small activation scale did not locate an equivalent statement.

## Limitations

The result is specific to pairwise concurrence in the periodic three-qubit antiferromagnetic \(XXX\) ring with a uniform field.

The activation threshold itself is prior-source content after algebraic inversion and is not claimed as an original theorem.

The double-scaling profile describes the neighborhood of the saturation field with
\[
B-\frac{3J}2=O(T).
\]
It does not give a uniform approximation simultaneously near the exponentially smaller zero-field activation edge.

The high-field Arrhenius law fixes \(B>3J/2\) before sending \(T\downarrow0\). Interchanging the field and temperature limits changes the relevant asymptotic regime.

A residual literature risk remains because later work on finite Heisenberg clusters may contain an equivalent low-temperature crossover under different Hamiltonian normalizations.

## References

1. X. Wang, H. Fu, and A. I. Solomon, “Thermal entanglement in three-qubit Heisenberg models,” arXiv:quant-ph/0105075, first public 16 May 2001; *Journal of Physics A: Mathematical and General* 34 (2001), 11307–11320, DOI: 10.1088/0305-4470/34/50/312.
2. R. Jafari and A. Langari, “Three-Qubit Ground State and Thermal Entanglement of \(XXZ\) Model With Dzyaloshinskii-Moriya Interaction,” arXiv:0903.2556, first public 14 March 2009; later published in *International Journal of Quantum Information* 9 (2011), 1057–1079.
3. G.-H. Yang and L. Zhou, “Thermal Entanglement of a Three-Qubit Heisenberg Chain with a Nonuniform Magnetic Field,” *Communications in Theoretical Physics* 49 (2008), 1635–1638, DOI: 10.1088/0253-6102/49/6/62.
