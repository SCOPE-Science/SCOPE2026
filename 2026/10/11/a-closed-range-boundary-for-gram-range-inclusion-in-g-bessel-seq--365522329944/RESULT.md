# A closed-range boundary for Gram-range inclusion in \(g\)-Bessel sequences

## Finding
Two successive papers by Zhang and Li use the same incorrect range lemma. For a \(g\)-Bessel sequence with synthesis operator \(T\) and Gram operator
\[
G=T^*T,
\]
the discrete Lemma 2.1 and the continuous Lemma 2.4 assert
\[
R(T^*)\subseteq R(G).
\]

The reverse inclusion
\[
R(G)\subseteq R(T^*)
\]
is automatic, but the displayed inclusion is false for a general Bessel sequence.

Take
\[
H=\ell^2(\mathbb N),
\qquad
V_n=\mathbb C,
\qquad
\Lambda_nx=\frac{x_n}{n}.
\]
In the continuous paper, use \(\Omega=\mathbb N\) with counting measure, a case explicitly included in its framework. Then
\[
\sum_{n=1}^{\infty}\|\Lambda_nx\|^2
=
\sum_{n=1}^{\infty}\frac{|x_n|^2}{n^2}
\le
\|x\|^2,
\]
so the family is \(g\)-Bessel.

Its synthesis, analysis, and Gram operators are
\[
T(c_n)=\left(\frac{c_n}{n}\right),
\qquad
T^*=T,
\qquad
G(c_n)=\left(\frac{c_n}{n^2}\right).
\]
Set
\[
x=\left(\frac1n\right)_{n\ge1}
\]
and
\[
y=Tx=\left(\frac1{n^2}\right)_{n\ge1}.
\]
Since \(x\in\ell^2\), one has
\[
y\in R(T^*).
\]
If \(y\) belonged to \(R(G)\), then
\[
\frac{z_n}{n^2}=\frac1{n^2}
\]
would force
\[
z_n=1
\]
for every \(n\), but \((1,1,\ldots)\notin\ell^2\). Therefore
\[
R(T^*)\not\subseteq R(G).
\]

The exact correction is
\[
R(T^*)=R(T^*T)
\quad\Longleftrightarrow\quad
R(T)\text{ is closed}.
\]
Thus the claimed range inclusion becomes valid exactly at the frame-sequence closed-range boundary.

## Assumptions and scope
The example is a legitimate discrete \(g\)-Bessel sequence and, by taking counting measure on \(\mathbb N\), also a legitimate continuous \(g\)-Bessel sequence.

All coefficient spaces are one-dimensional. The continuous family satisfies the paper's uniform block bound because
\[
\sup_n\|\Lambda_n\|=1.
\]

The result corrects the two range lemmas. It does not claim that the papers' later frame-sequence criterion is false; in fact the corrected closed-range statement explains why the range equality used there is valid for frame sequences.

## Proof
For any bounded operator \(T\),
\[
R(T^*T)\subseteq R(T^*)
\]
is immediate.

Suppose first that \(R(T)\) is closed. Then
\[
H_{\mathrm{target}}=R(T)\oplus N(T^*).
\]
If
\[
y=T^*u\in R(T^*),
\]
write
\[
u=Tx+u_0
\]
with
\[
u_0\in N(T^*).
\]
Then
\[
y=T^*Tx.
\]
Hence
\[
R(T^*)\subseteq R(T^*T),
\]
and equality follows.

Conversely, suppose
\[
R(T^*)\subseteq R(T^*T).
\]
Douglas' range-inclusion theorem, applied with
\[
A=T^*,
\qquad
B=T^*T,
\]
gives a constant \(\lambda>0\) such that
\[
AA^*\le\lambda BB^*.
\]
Writing
\[
P=T^*T,
\]
this becomes
\[
P\le\lambda P^2.
\]
Functional calculus implies that every nonzero spectral value \(t\) of \(P\) satisfies
\[
t\ge\lambda^{-1}.
\]
Therefore \(P\), and hence \(T\), is bounded below on
\[
N(T)^\perp.
\]
A bounded operator is bounded below on \(N(T)^\perp\) exactly when its range is closed. Thus \(R(T)\) is closed.

For the explicit diagonal example,
\[
T=\operatorname{diag}(1,1/2,1/3,\ldots)
\]
has nonclosed range, and the vector
\[
(1,1/4,1/9,\ldots)
\]
exhibits the strict range inclusion directly.

## Verification
The complete discrete Lemma 2.1 and its proof were inspected in the 2019 full text. The proof uses
\[
H=R(T)+N(T^*)
\]
without first knowing that \(R(T)\) is closed. In general the valid orthogonal decomposition uses
\[
\overline{R(T)}
\]
instead.

The complete continuous Lemma 2.4 and its proof were inspected in the 2020 full text. It repeats the same range assertion and the same unsupported decomposition step.

Both papers later characterize \(g\)-frame sequences through closed range of the synthesis operator. Under that additional hypothesis, the disputed inclusion is valid and becomes equality, exactly as the operator proof above shows.

The counterexample and the closed-range equivalence are exact. No finite truncation, numerical approximation, or experimental extrapolation is used.

## Relationship to prior work
The operator identity
\[
R(T^*)=R(T^*T)
\quad\Longleftrightarrow\quad
R(T)\text{ is closed}
\]
is standard Hilbert-space operator theory and follows directly from Douglas' range-inclusion theorem. It is used here as the repair, not claimed as a new operator theorem.

The 2020 paper explicitly describes itself as a continuous analogue of the 2019 \(g\)-sequence paper. Full-text comparison shows that the false range lemma was inherited from the earlier discrete treatment. The accepted correction therefore addresses both statements together rather than treating the continuous version as independent.

Targeted searches for both exact source identifiers, lemma labels, Gram-range aliases, and correction language did not locate an indexed erratum or a published source giving this explicit \(g\)-Bessel counterexample.

## Limitations
The finding corrects the two auxiliary range lemmas. It does not invalidate every downstream theorem: statements that separately assume or derive closed range can still be valid.

The exact operator equivalence is standard; the contribution here is its application to identify the precise missing hypothesis in the two published \(g\)-frame range lemmas and to give a single explicit frame-theoretic witness.

A nonindexed erratum, thesis remark, or informal correction may contain the same observation.

## References
1. Y. Zhang and Y.-Z. Li, *G-Frame and Riesz Sequences in Hilbert Spaces*, Numerical Functional Analysis and Optimization 40(11) (2019), 1268--1290, DOI 10.1080/01630563.2019.1599912.
2. Y. Zhang and Y.-Z. Li, *Continuous \(g\)-frame and \(g\)-Riesz sequences in Hilbert spaces*, Mathematical Methods in the Applied Sciences 43(7) (2020), 4257--4271, DOI 10.1002/mma.6191.
3. R. G. Douglas, *On majorization, factorization, and range inclusion of operators on Hilbert space*, Proceedings of the American Mathematical Society 17 (1966), 413--415.
