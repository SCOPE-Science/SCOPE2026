# A noncommuting frame operator breaks a controlled g-fusion characterization

## Finding
Theorem 3.8 of Ghosh--Samanta claims that a continuous \((T,U)\)-controlled \(g\)-fusion frame is equivalent to a continuous \((TU,I)\)-controlled \(g\)-fusion frame. The proof replaces
\[
\langle TSU f,f\rangle
\]
by
\[
\langle STU f,f\rangle
\]
without assuming that \(T\) commutes with the ordinary \(g\)-fusion frame operator \(S\).

The claim is false already on a one-point measure space. Let
\[
H=\mathbb C^2,\qquad X=\{\ast\},\qquad \mu(\{\ast\})=1,
\]
take
\[
F(\ast)=H,\qquad v(\ast)=1,
\]
and define
\[
\Lambda_\ast=
\begin{pmatrix}
1&0\\
0&\sqrt2
\end{pmatrix}.
\]
The ordinary \(g\)-fusion frame operator is
\[
S=
\Lambda_\ast^*\Lambda_\ast
=
\begin{pmatrix}
1&0\\
0&2
\end{pmatrix}.
\]

Choose
\[
T=U=
\begin{pmatrix}
2&1\\
1&2
\end{pmatrix}.
\]
These controls are positive and invertible. The \((T,T)\)-controlled form is
\[
\langle \Lambda_\ast Tf,\Lambda_\ast Tf\rangle
=
\langle TSTf,f\rangle,
\]
where
\[
TST=
\begin{pmatrix}
6&6\\
6&9
\end{pmatrix}.
\]
The two eigenvalues are
\[
\frac{15-3\sqrt{17}}2
\quad\text{and}\quad
\frac{15+3\sqrt{17}}2.
\]
Both are positive, so the family is a continuous \((T,T)\)-controlled \(g\)-fusion frame.

The claimed equivalent control pair is
\[
(TU,I)=(T^2,I),
\qquad
T^2=
\begin{pmatrix}
5&4\\
4&5
\end{pmatrix}.
\]
By the paper's definition, its mixed quadratic expression is
\[
\langle \Lambda_\ast f,\Lambda_\ast T^2f\rangle.
\]
For
\[
f=(1,i),
\]
this equals
\[
15+4i
\]
with the source's linear-first convention. It is nonreal, so no inequality of the form
\[
A\|f\|^2
\le
\langle \Lambda_\ast f,\Lambda_\ast T^2f\rangle
\le
B\|f\|^2
\]
can hold with positive real \(A,B\).

Thus Theorem 3.8 fails even with equal positive commuting controls. The obstruction is not noncommutativity of \(T\) and \(U\); it is noncommutativity of the control with the frame operator.

## Assumptions and scope
The example is a legitimate continuous \(g\)-fusion system on a one-point measure space. It has no measurability, integrability, closure, or infinite-dimensional subtleties.

The counterexample uses
\[
F(\ast)=H
\]
and one coefficient operator, so the continuous \(g\)-fusion notation reduces to an ordinary positive frame-operator calculation without changing the definition.

The repair asserted here is sufficient, not claimed necessary in every accidental special case: require
\[
TS=ST.
\]
Under the source's positive-control setting, this makes the operator identity used in the proof valid.

## Proof
For every \(f\in\mathbb C^2\),
\[
\langle \Lambda_\ast Tf,\Lambda_\ast Tf\rangle
=
\langle S Tf,Tf\rangle
=
\langle TSTf,f\rangle.
\]
Direct multiplication gives
\[
TST=
\begin{pmatrix}
6&6\\
6&9
\end{pmatrix}.
\]
Its characteristic polynomial is
\[
\lambda^2-15\lambda+18,
\]
so its eigenvalues are
\[
\lambda_\pm=
\frac{15\pm3\sqrt{17}}2.
\]
Therefore
\[
\lambda_-\|f\|^2
\le
\langle \Lambda_\ast Tf,\Lambda_\ast Tf\rangle
\le
\lambda_+\|f\|^2.
\]
This proves the \((T,T)\)-controlled frame property.

Next,
\[
T^2=
\begin{pmatrix}
5&4\\
4&5
\end{pmatrix}.
\]
For
\[
f=
\begin{pmatrix}
1\\
i
\end{pmatrix},
\]
one has
\[
\Lambda_\ast f=
\begin{pmatrix}
1\\
\sqrt2\,i
\end{pmatrix},
\qquad
\Lambda_\ast T^2f=
\begin{pmatrix}
5+4i\\
\sqrt2(4+5i)
\end{pmatrix}.
\]
Hence, with the convention used in the source,
\[
\langle \Lambda_\ast f,\Lambda_\ast T^2f\rangle
=
15+4i.
\]
This is not a real number and therefore cannot satisfy the defining order inequality.

Finally, the source proof writes
\[
\langle TSU f,f\rangle
=
\langle STU f,f\rangle.
\]
If
\[
TS=ST,
\]
the equality is valid. The proof of Theorem 3.8 then goes through.

## Verification
The first public full text was inspected at the definition of a continuous \((T,U)\)-controlled \(g\)-fusion frame, Theorem 3.8, its complete proof, Corollary 3.9, and Theorem 3.10.

Theorem 3.8 explicitly performs the step
\[
TSU\longmapsto STU
\]
without a commutation hypothesis. The same document later states Theorem 3.10 with the explicit assumption
\[
S_{gF}T=TS_{gF},
\]
showing that this commutation is a substantive hypothesis elsewhere in the source.

The matrix witness was checked exactly:
\[
TST=
\begin{pmatrix}
6&6\\
6&9
\end{pmatrix},
\qquad
T^2=
\begin{pmatrix}
5&4\\
4&5
\end{pmatrix},
\]
and the target mixed form at \(f=(1,i)\) is nonreal.

No numerical approximation, finite search, or asymptotic argument is used.

## Relationship to prior work
Controlled-frame constructions commonly require compatibility between the control and the frame operator so that the mixed operator is positive and self-adjoint. Later controlled \(K\)-\(g\)-fusion literature makes such commutation assumptions explicitly when defining or manipulating controlled frame operators.

A 2024 paper by the same authors on continuous controlled \(K\)-\(g\)-fusion frames again uses the same controlled framework. Its preliminary discussion includes a blanket claim that positive operators commute, but positivity alone does not imply commutation and therefore cannot justify the operator interchange used in Theorem 3.8.

A 2025 Hilbert-\(C^*\)-module treatment explicitly assumes that the two controls commute with each other and with every local frame operator before defining the controlled frame operator. This is compatible with the repair above but does not state the present finite-dimensional counterexample to Theorem 3.8.

Targeted scientific searches for the exact source, Theorem 3.8, the \((TU,I)\) characterization, noncommuting control/frame operators, and errata did not locate an indexed correction containing this counterexample.

## Limitations
The result corrects Theorem 3.8 only. It does not reassess every later theorem in the preprint that uses products or square roots of control operators.

The condition
\[
TS=ST
\]
is given as a clean sufficient repair. No claim is made that it is logically necessary in every exceptional configuration where the two mixed forms happen to agree.

An unindexed erratum, thesis remark, or informal correction may contain the same observation.

## References
1. P. Ghosh and T. K. Samanta, *Continuous controlled generalized fusion frames in Hilbert spaces*, arXiv:2110.11234v1, first public version 4 October 2021.
2. P. Ghosh and T. K. Samanta, *Construction of continuous controlled K-g-fusion frames in Hilbert spaces*, Acta et Commentationes Universitatis Tartuensis de Mathematica 28(1) (2024), 41--62, DOI 10.12697/ACUTM.2024.28.04.
3. S. Touaiher, R. El Jazzar and M. Rossafi, *Properties and Characterizations of Controlled K-g-Fusion Frames within Hilbert \(C^*\)-Modules*, International Journal of Analysis and Applications 23 (2025), 111, DOI 10.28924/2291-8639-23-2025-111.
