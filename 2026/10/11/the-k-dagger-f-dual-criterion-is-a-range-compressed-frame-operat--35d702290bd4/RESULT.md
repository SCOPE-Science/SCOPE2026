# The \(K^\dagger F\) dual criterion is a range-compressed frame-operator identity

## Finding
Faraj--Rossafi--Moalige--Kabbaj--Touri define a continuous \(K\)-frame by
\[
A\|K^*f\|^2
\le
\int_\Omega |\langle f,F(\omega)\rangle|^2\,d\mu(\omega)
\le
B\|f\|^2
\]
and then call it Parseval when \(A=B=1\). Under that convention, Lemma 3.2 of their paper is false.

Let
\[
S_Ff=
\int_\Omega \langle f,F(\omega)\rangle F(\omega)\,d\mu(\omega)
\]
be the frame operator and suppose that \(K\) has closed range. Then the precise condition for the proposed family \(K^\dagger F\) to be a continuous \(K\)-dual is
\[
S_FP_{R(K)}=KK^*.
\]
Equivalently,
\[
S_F(K^\dagger)^*=K.
\]

The displayed \(A=B=1\) inequalities do not imply this identity.

A one-point counterexample is
\[
\Omega=\{\omega_0\},\qquad
\mu(\{\omega_0\})=1,\qquad
H=\mathbb C,\qquad
K=\frac12 I_H,\qquad
F(\omega_0)=1.
\]
Its energy is
\[
\int_\Omega |\langle f,F(\omega)\rangle|^2\,d\mu(\omega)
=
\|f\|^2,
\]
while
\[
\|K^*f\|^2=\frac14\|f\|^2.
\]
Thus \(A=B=1\) satisfies the paper's displayed Parseval convention. Yet
\[
K^\dagger=2I_H,
\]
and the proposed reconstruction is
\[
\int_\Omega
\langle f,K^\dagger F(\omega)\rangle F(\omega)\,d\mu(\omega)
=
2f,
\]
not \(Kf=f/2\). Therefore \(K^\dagger F\) is not a continuous \(K\)-dual.

## Assumptions and scope
The result concerns the definitions and Lemma 3.2 as printed in *Dual continuous \(K\)-Frames in Hilbert spaces*. The paper's continuous \(K\)-frame display compares the lower term with \(\|K^*f\|\) and the upper term with \(\|f\|\), so equality of the two numerical constants does not collapse the two inequalities to one identity.

The definition line immediately before the Parseval convention writes a strict inequality between the two frame bounds while the next lines discuss equal bounds. The argument here uses the evident non-strict bound convention required by those subsequent sentences and by standard frame terminology.

The exact criterion below only needs \(F\) to be Bessel and \(K\) to have closed range. The one-point example is finite-dimensional and has no convergence or measurability issues.

## Proof
Let
\[
G(\omega)=K^\dagger F(\omega).
\]
Since \(K^\dagger\) is bounded when \(K\) has closed range, \(G\) is Bessel whenever \(F\) is Bessel.

Using the paper's dual convention,
\[
G\text{ is a continuous }K\text{-dual of }F
\]
if and only if, for every \(f\in H\),
\[
Kf=
\int_\Omega \langle f,G(\omega)\rangle F(\omega)\,d\mu(\omega).
\]
Because
\[
\langle f,K^\dagger F(\omega)\rangle
=
\langle (K^\dagger)^*f,F(\omega)\rangle,
\]
the reconstruction operator is
\[
S_F(K^\dagger)^*.
\]
Hence duality is equivalent to
\[
S_F(K^\dagger)^*=K.
\]

For a closed-range operator,
\[
(K^\dagger)^*K^*
=
(KK^\dagger)^*
=
P_{R(K)}.
\]
Therefore duality implies
\[
S_FP_{R(K)}
=
S_F(K^\dagger)^*K^*
=
KK^*.
\]

Conversely, assume
\[
S_FP_{R(K)}=KK^*.
\]
The range of \((K^\dagger)^*\) is contained in \(R(K)\), so
\[
P_{R(K)}(K^\dagger)^*=(K^\dagger)^*.
\]
Also
\[
K^*(K^\dagger)^*
=
(K^\dagger K)^*
=
P_{N(K)^\perp}.
\]
Thus
\[
S_F(K^\dagger)^*
=
S_FP_{R(K)}(K^\dagger)^*
=
KK^*(K^\dagger)^*
=
KP_{N(K)^\perp}
=
K.
\]
This proves the equivalence.

In the one-point example,
\[
S_F=I_H,\qquad
P_{R(K)}=I_H,\qquad
KK^*=\frac14I_H,
\]
so the criterion fails exactly as the direct reconstruction calculation shows.

## Verification
The publisher PDF was inspected at Definition 2.2, Definition 2.3, Lemma 3.2, and Theorem 3.4. Definition 2.2 calls \(A=B=1\) Parseval after the mixed \(K\)-frame inequalities. Lemma 3.2 then begins its proof by replacing those inequalities with the exact identity
\[
\|K^*f\|^2
=
\int_\Omega |\langle f,F(\omega)\rangle|^2\,d\mu(\omega),
\]
and later uses
\[
S_F=KK^*.
\]
Those equalities do not follow from the printed \(A=B=1\) convention.

The public preprint arXiv:2006.07328 contains the same definition and the same proof step, so the issue is not introduced by journal typesetting.

The counterexample and the equivalence criterion are symbolic operator calculations; no numerical experiment is used.

## Relationship to prior work
Xiang's 2019 work on Parseval \(K\)-frames uses the exact \(K\)-Parseval identity and proves the corresponding discrete statement that \(K^\dagger F\) is a dual \(K\)-Bessel sequence when \(K\) has closed range. That result supports the stronger hypothesis but does not validate the broader mixed-bound convention in the 2021 continuous paper.

Massit--Rossafi's 2024 paper *Equal-norm Parseval continuous \(K\)-frames in Hilbert spaces* explicitly supplements the \(A=B=1\) terminology with the identity
\[
\int_\Omega |\langle f,F(\omega)\rangle|^2\,d\mu(\omega)
=
\|K^*f\|^2.
\]
It then uses
\[
S_F=KK^*.
\]
This later convention is sufficient to repair Lemma 3.2. It is stronger than the exact criterion
\[
S_FP_{R(K)}=KK^*
\]
for the single conclusion that \(K^\dagger F\) is a \(K\)-dual.

Bellomonte's continuous \(K\)-frame duality theory formulates duals through operator factorization and does not identify equal numerical mixed bounds with the exact \(K\)-Parseval identity.

Targeted searches using the exact source title, arXiv identifier, theorem number, the formula \(K^\dagger F\), Parseval aliases, frame-operator identities, and correction terminology did not locate an indexed source stating the one-point counterexample or the range-compressed necessary-and-sufficient criterion above.

## Limitations
The finding corrects Lemma 3.2 under the source's printed definition and identifies the exact condition for the specific candidate dual \(K^\dagger F\).

It does not claim that every result in the source fails. Results whose proofs use the exact identity may remain valid after explicitly strengthening the Parseval hypothesis.

The later 2024 paper already adopts the stronger exact-identity convention, so the novelty here is not the existence of that sufficient convention; it is the explicit counterexample to the earlier mixed-bound formulation and the sharper range-compressed equivalence.

An unindexed note or informal correction may contain the same observation.

## References
1. H. Faraj, M. Rossafi, B. Moalige, S. Kabbaj and A. Touri, *Dual continuous \(K\)-frames in Hilbert spaces*, J. Math. Comput. Sci. 11 (2021), 7844--7856, DOI 10.28919/jmcs/6704; preprint arXiv:2006.07328v1.
2. Z.-Q. Xiang, *Some Properties of Canonical Dual \(K\)-Bessel Sequences for Parseval \(K\)-Frames*, Journal of Function Spaces 2019, Article 9862369, DOI 10.1155/2019/9862369.
3. H. Massit and M. Rossafi, *Equal-norm Parseval continuous \(K\)-frames in Hilbert spaces*, Annals of Mathematics and Computer Science 22 (2024), 45--53, DOI 10.56947/amcs.v22.281.
4. G. Bellomonte, *Continuous frames for unbounded operators*, Advances in Operator Theory 6 (2021), Article 41, DOI 10.1007/s43036-021-00136-3.
