# A norm identity does not characterize continuous \(K\)-duality

## Finding
Theorem 3.2 of Rahimlou--Ahmadi--Jafarizadeh--Nami states that each of two scalar norm identities is equivalent to the full continuous \(k\)-dual reconstruction conditions in Theorem 3.1. Both equivalences fail.

Let
\[
H_0=H=\mathbb C^2,
\qquad
k=P=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix}.
\]
Take the two-point measure space
\[
X=\{1,2\}
\]
with counting measure and define
\[
f(1)=g(1)=e_1,
\qquad
f(2)=g(2)=e_2.
\]
The mappings \(f\) and \(g\) are Parseval continuous frames, hence continuous Bessel mappings.

For every
\[
h=(a,b)\in\mathbb C^2,
\]
the first scalar condition from Theorem 3.2 gives
\[
\sum_{j=1}^2
\langle h,g(j)\rangle
\langle f(j),kh\rangle
=
|a|^2
=
\|kh\|^2.
\]
Because
\[
k=k^*,
\]
the second scalar condition holds as well:
\[
\sum_{j=1}^2
\langle h,f(j)\rangle
\langle g(j),k^*h\rangle
=
|a|^2
=
\|k^*h\|^2.
\]

However,
\[
T_f(\langle h,g\rangle)
=
\sum_{j=1}^2\langle h,e_j\rangle e_j
=
h.
\]
The continuous \(k\)-dual identity in Theorem 3.1 would require this vector to equal
\[
kh.
\]
At \(h=e_2\),
\[
T_f(\langle e_2,g\rangle)=e_2
\]
while
\[
ke_2=0.
\]
Therefore \(f,g\) are not a continuous \(k\)-dual pair even though both scalar conditions in Theorem 3.2 hold.

## Assumptions and scope
The example uses complex finite-dimensional Hilbert spaces and a finite counting measure, so it is a special case of the continuous setting in the source.

No frame pathology is involved: both mappings are ordinary Parseval frames. The only noninvertible object is the operator \(k\), which is allowed by the theorem.

The structural statements below use the standard complex polarization identity. They identify exactly what the two scalar identities determine.

## Proof
Let
\[
M=T_fT_g^*:H_0\to H.
\]
The first scalar identity of Theorem 3.2 can be written
\[
\langle Mh,kh\rangle
=
\langle kh,kh\rangle
\qquad
(h\in H_0).
\]
Equivalently,
\[
\langle (M-k)h,kh\rangle=0
\qquad
(h\in H_0).
\]
The corresponding quadratic form is identically zero. By complex polarization,
\[
(M-k)^*k=0.
\]
Taking adjoints gives
\[
k^*(M-k)=0.
\]
Hence
\[
R(M-k)\subseteq N(k^*).
\]
Since
\[
N(k^*)=\overline{R(k)}^\perp,
\]
this is equivalent to
\[
P_{\overline{R(k)}}M=k.
\]

Thus the scalar identity fixes only the component of the reconstruction operator visible inside the closed range of \(k\). Any defect with range in \(\overline{R(k)}^\perp\) is invisible.

In the explicit example,
\[
M=I,
\qquad
k=P.
\]
Therefore
\[
M-k=I-P
\]
has range
\[
\operatorname{span}\{e_2\}
=
R(k)^\perp.
\]
This is exactly the invisible defect predicted by the operator identity.

For the second scalar condition, put
\[
N=T_gT_f^*:H\to H_0.
\]
The same polarization argument yields
\[
k(N-k^*)=0,
\]
equivalently
\[
R(N-k^*)\subseteq N(k)
=
\overline{R(k^*)}^\perp.
\]
In the example,
\[
N=I
\]
and the defect is again the complementary projection.

Consequently the first scalar identity becomes sufficient for full \(k\)-duality if one additionally knows
\[
R(M)\subseteq\overline{R(k)}.
\]
Indeed, then \(R(M-k)\) lies both in \(\overline{R(k)}\) and in its orthogonal complement, so \(M=k\). A dense range for \(k\) is another sufficient special case.

Dually, the second scalar identity becomes sufficient if
\[
R(N)\subseteq\overline{R(k^*)},
\]
and injectivity of \(k\) is a simple special case.

## Verification
The earliest public preprint was inspected at Theorem 3.1, Theorem 3.2, Definition 3.3, and the beginning of Theorem 3.4. Theorem 3.1 defines the dual pair through the full vector reconstruction identities. Theorem 3.2 replaces those identities by scalar norm equalities.

In the proof of Theorem 3.2(i), the source correctly reaches
\[
k^*kh
=
T_g\langle kh,f\rangle.
\]
This is only the adjoint reconstruction identity tested on vectors of the form \(kh\). The proof does not justify extending it to arbitrary vectors of \(H\), which is exactly where the counterexample fails.

The 2020 journal version was also inspected at the same theorem and proof. It retains the same statement and argument.

The counterexample uses only exact orthogonal-projection identities and the two-vector Parseval expansion; no numerical experiment or approximation is involved.

## Relationship to prior work
Later treatments of continuous \(K\)-frames encode duality by a full operator factorization or reconstruction identity rather than by a single norm identity. For example, Bellomonte's continuous \(K\)-frame framework uses an actual \(K\)-dual reconstruction formula and, in the closed-range setting, constructs range-adapted duals.

A close published result on dual \(g\)-frames shows that an orthogonality test can leave a defect invisible on a particular spectral subspace. That mechanism is analogous but does not cover the present theorem: here the invisible subspace is \(R(k)^\perp\), the source is different, and the exact projected identity
\[
P_{\overline{R(k)}}T_fT_g^*=k
\]
is specific to continuous \(k\)-duality.

Targeted searches for the exact source, Theorem 3.2, scalar norm characterizations of continuous \(K\)-duality, and corrections did not locate an indexed correction of this theorem.

## Limitations
The finding corrects Theorem 3.2 only. It does not reassess Theorem 3.1 or the later statement that a genuine continuous \(k\)-dual pair produces the expected frame bounds.

The range conditions above are sufficient repairs tailored to each scalar identity; no claim is made that they are the only possible extra hypotheses.

A nonindexed erratum, thesis remark, or informal correction may contain the same observation.

## References
1. G. Rahimlou, R. Ahmadi, M. A. Jafarizadeh and S. Nami, *Continuous \(k\)-frames and their duals*, arXiv:1901.03803v1, first public version 12 January 2019.
2. G. Rahimlou, R. Ahmadi, M. A. Jafarizadeh and S. Nami, *Continuous \(k\)-Frames and their Dual in Hilbert Spaces*, Sahand Communications in Mathematical Analysis 17(3) (2020), 145--160, DOI 10.22130/scma.2019.115719.691.
3. G. Bellomonte, *Continuous frames for unbounded operators*, Advances in Operator Theory 6 (2021), Article 41, DOI 10.1007/s43036-021-00136-3.
