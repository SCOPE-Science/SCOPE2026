# A null-set defect in the weak-disjointness criterion for continuous \(g\)-frames

## Finding
Theorem 2.2(v) of Khedmati--Abdollahpour claims that two continuous \(g\)-frames are weakly disjoint if and only if
\[
\{h\oplus k:
\Gamma_\omega(h\oplus k)=0
\text{ for every }\omega\in\Omega\}
=
\{0\},
\]
where
\[
\Gamma_\omega(h\oplus k)
=
\Lambda_\omega h+\Theta_\omega k.
\]

Under this literal pointwise reading, the criterion is false. Weak disjointness is defined by the intersection of analysis-operator ranges in an \(L^2\)-type coefficient Hilbert space, so it cannot depend on values at individual points of measure zero. The displayed pointwise criterion does depend on such values.

Let
\[
\Omega=[0,1]
\]
with Lebesgue measure and let
\[
H=K=\mathbb C,\qquad K_\omega=\mathbb C.
\]
Define
\[
\Lambda_\omega z=z
\]
for all \(\omega\), and define
\[
\Theta_0z=0,\qquad
\Theta_\omega z=-z
\]
for \(0<\omega\le1\).

Both \(\Lambda\) and \(\Theta\) are Parseval continuous \(g\)-frames. Their analysis ranges coincide in the coefficient \(L^2\)-space, so they are not weakly disjoint. Yet the printed pointwise kernel is trivial.

The exact correction is to replace “for every \(\omega\)” by “for almost every \(\omega\)”. With that change, the criterion is equivalent to weak disjointness.

## Assumptions and scope
The measure space is the finite nonatomic space \([0,1]\) with Lebesgue measure. The coefficient Hilbert spaces are all \(\mathbb C\).

The source defines weak disjointness by
\[
\operatorname{Ran}T_\Lambda^*
\cap
\operatorname{Ran}T_\Theta^*
=
\{0\}.
\]
Its coefficient space is an \(L^2\)-type Hilbert space, and the paper also explicitly uses almost-everywhere equality when defining weak equality of continuous \(g\)-frames. Thus null-set changes are invisible to the analysis-operator ranges.

The finding concerns only part (v) of Theorem 2.2 under its printed pointwise quantifier. No claim is made here about parts (i)--(iv).

## Proof
For every \(z\in\mathbb C\),
\[
\int_0^1|\Lambda_\omega z|^2\,d\omega
=
\int_0^1|z|^2\,d\omega
=
|z|^2.
\]
Likewise,
\[
\int_0^1|\Theta_\omega z|^2\,d\omega
=
\int_{(0,1]}|-z|^2\,d\omega
=
|z|^2.
\]
Hence both families are Parseval continuous \(g\)-frames.

The analysis operator for \(\Lambda\) sends \(h\) to the \(L^2\)-class of the constant function
\[
\omega\longmapsto h.
\]
The analysis operator for \(\Theta\) sends \(k\) to the class of
\[
\omega\longmapsto
\begin{cases}
0,&\omega=0,\\
-k,&0<\omega\le1.
\end{cases}
\]
This class is the same as the constant function \(-k\). Therefore
\[
\operatorname{Ran}T_\Lambda^*
=
\operatorname{Ran}T_\Theta^*,
\]
a nonzero one-dimensional subspace of \(L^2([0,1])\). The frames are not weakly disjoint.

Now consider the combined family. At the exceptional point,
\[
\Gamma_0(h\oplus k)=h.
\]
For \(0<\omega\le1\),
\[
\Gamma_\omega(h\oplus k)=h-k.
\]
If \(\Gamma_\omega(h\oplus k)=0\) for every \(\omega\), then the value at \(0\) gives \(h=0\), and the values on \((0,1]\) then give \(k=0\). Thus the printed pointwise kernel is \(\{0\}\).

In contrast,
\[
\Gamma_\omega(1\oplus1)=0
\]
for almost every \(\omega\), with the sole exception \(\omega=0\). Hence
\[
T_\Gamma^*(1\oplus1)=0
\]
in the coefficient Hilbert space.

For the repaired statement, suppose first that
\[
\operatorname{Ran}T_\Lambda^*
\cap
\operatorname{Ran}T_\Theta^*
=
\{0\}
\]
and that
\[
\Gamma_\omega(h\oplus k)=0
\]
almost everywhere. Then
\[
T_\Lambda^*h=-T_\Theta^*k
\]
lies in both analysis ranges. It must be zero. Since the analysis operator of a continuous \(g\)-frame is injective, \(h=k=0\).

Conversely, suppose the almost-everywhere kernel is trivial. If
\[
T_\Lambda^*h=T_\Theta^*k,
\]
then
\[
\Gamma_\omega(h\oplus(-k))=0
\]
almost everywhere. The repaired kernel condition gives \(h=k=0\), and hence the intersection of the two ranges is trivial. This is exactly weak disjointness.

## Verification
The complete statement and proof of Theorem 2.2 were inspected in the open preprint. The theorem prints the condition
\[
\Gamma_\omega(h\oplus k)=0
\quad\text{for }\omega\in\Omega,
\]
not an almost-everywhere condition.

In the converse part of the proof, equality of two analysis vectors gives
\[
T_\Gamma^*(h\oplus(-k))=0.
\]
That is an equality in the \(L^2\)-type coefficient Hilbert space and therefore means only almost-everywhere vanishing. The proof then invokes the printed pointwise kernel condition, which does not follow from this \(L^2\) equality.

The paper's preliminaries define the analysis operator pointwise by
\[
(T_\Lambda^*h)(\omega)=\Lambda_\omega h
\]
inside the coefficient Hilbert space and separately define weak equality of continuous \(g\)-frames by equality almost everywhere. These conventions make the null-set distinction explicit.

The counterexample uses exact formulas and no numerical approximation.

## Relationship to prior work
The same paper cites earlier work on disjoint \(g\)-frames and continuous frames as the basis for its definitions. The discrete \(g\)-frame setting has no analogous null-set ambiguity because coefficient equality is coordinatewise.

Abdollahpour's earlier work on disjoint and weakly disjoint \(g\)-frames characterizes the discrete notions through analysis-operator ranges. The continuous theorem attempts to transfer that structure to a measure-indexed coefficient space. The transfer requires almost-everywhere, rather than pointwise, kernel equality.

Later continuous \(g\)-frame literature continues to formulate analysis and synthesis operators in \(L^2\)-type coefficient spaces, where representatives differing on null sets define the same vector.

Exact-title, arXiv-identifier, theorem-number, weak-disjointness, pointwise-kernel, almost-everywhere-kernel, correction, and erratum searches did not locate an indexed correction of Theorem 2.2(v) or a checked source containing this counterexample.

## Limitations
If the phrase
\[
\Gamma_\omega(h\oplus k)=0,\quad\omega\in\Omega
\]
was intended informally to mean almost-everywhere equality, then the mathematical content of the repaired statement is the intended theorem and the defect is one of quantification. Under the literal printed pointwise reading, however, the equivalence is false.

The counterexample deliberately changes one operator value on a singleton. Its role is to show that the printed criterion is not invariant under null-set modifications, whereas weak disjointness is.

No claim is made about stronger disjointness notions in the remaining parts of Theorem 2.2.

## References
1. Y. Khedmati and M. R. Abdollahpour, *Disjointness of continuous \(g\)-frames and Riesz-type continuous \(g\)-frames*, arXiv:1802.03616v1, 10 February 2018.
2. M. R. Abdollahpour, *Dilation of dual \(g\)-frames to dual \(g\)-Riesz bases*, Banach Journal of Mathematical Analysis 9(1) (2015), 54--66, DOI 10.15352/bjma/09-1-5.
3. J. P. Gabardo and D. Han, *Frames associated with measurable spaces*, Advances in Computational Mathematics 18 (2003), 127--147.
