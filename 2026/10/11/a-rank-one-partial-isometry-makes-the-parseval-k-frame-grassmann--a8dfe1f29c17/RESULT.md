# A rank-one partial isometry makes the Parseval \(K\)-frame Grassmannian map choice-dependent

## Finding
Theorem 3.3 of Sadri--Rahimlou claims a natural one-to-one correspondence between Parseval \(K\)-frames in the stated finite-dimensional setting and the \(m\)-dimensional subspaces of \(H\). Its proof chooses a unitary \(U_F\) satisfying
\[
f_j=KPU_Fe_j
\]
and defines
\[
\Phi(F)=U_F^*KPU_FH=U_F^*R(K).
\]
For a general closed-range \(K\), this assignment is not well-defined: the same frame can admit two allowed choices of \(U_F\) that give different subspaces.

Let
\[
H=\mathbb C^2,\qquad
a=\frac{e_1+e_2}{\sqrt2},\qquad
K=\frac1{\sqrt2}\begin{pmatrix}1&0\\1&0\end{pmatrix}.
\]
Then \(K\) is a rank-one partial isometry. In particular,
\[
K^\dagger=K^*,\qquad
R(K^\dagger)=\operatorname{span}\{e_1\},
\]
so the projection required in the theorem is
\[
P=P_{e_1}=\begin{pmatrix}1&0\\0&0\end{pmatrix},
\]
and \(KP=K\) has rank \(m=1\).

Put
\[
U=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix},\qquad
Q=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad
V=QU.
\]
Both \(U\) and \(V\) are unitary. Since \(KQ=K\),
\[
KPU=KPV=\begin{pmatrix}\frac12&\frac12\\\frac12&\frac12\end{pmatrix}.
\]
Thus both choices produce literally the same ordered frame
\[
F=\left(\frac a{\sqrt2},\frac a{\sqrt2}\right).
\]
For every \(x\in H\),
\[
\sum_{j=1}^2|\langle x,f_j\rangle|^2
=
|\langle x,a\rangle|^2
=
\|K^*x\|^2,
\]
so \(F\) is a Parseval \(K\)-frame.

However,
\[
U^*R(K)=\operatorname{span}\{e_1\},
\qquad
V^*R(K)=\operatorname{span}\{e_2\}.
\]
The proposed value \(\Phi(F)\) therefore depends on which admissible unitary representation of the same \(F\) is chosen.

## Assumptions and scope
The example satisfies the hypotheses displayed in Theorem 3.3: \(H\) is finite dimensional, \(K\) has closed range, \(P\) is the orthogonal projection onto \(R(K^\dagger)\), and \(KP\) has rank \(m=1\). The two frame vectors are nonzero and lie in \(KPH=R(K)\).

The conclusion addressed here is specifically the claimed natural correspondence constructed in the proof. The source treats unitarily equivalent frames as identical, but the counterexample does not rely on that convention: the two choices \(U\) and \(V\) generate the same ordered frame \(F\) entry by entry.

## Proof
The Moore--Penrose inverse of the rank-one partial isometry \(K\) is \(K^*\). Hence
\[
R(K^\dagger)=R(K^*)=\operatorname{span}\{e_1\},
\]
which gives the displayed \(P\) and \(KP=K\).

The matrix \(Q\) fixes \(e_1\) and changes sign on \(e_2\). Because the second column of \(K\) is zero,
\[
KQ=K.
\]
Consequently,
\[
KPV=KPQU=KQU=KU=KPU.
\]
The common synthesis matrix has both columns equal to \(a/\sqrt2\), proving that \(U\) and \(V\) are two valid choices for precisely the same frame.

Since
\[
K^*x=\langle x,a\rangle e_1,
\]
the Parseval identity follows exactly:
\[
\|K^*x\|^2=|\langle x,a\rangle|^2
=
2\left|\left\langle x,\frac a{\sqrt2}\right\rangle\right|^2.
\]

Finally, \(Ua=e_1\) and \(Qa=(e_1-e_2)/\sqrt2\), while \(UQa=e_2\). Because \(U=U^*\) and \(V^*=UQ\),
\[
U^*R(K)=\operatorname{span}\{e_1\},
\qquad
V^*R(K)=\operatorname{span}\{e_2\}.
\]
These are distinct points of the one-dimensional Grassmannian, so the map in the proof is not well-defined.

There is a canonical subspace determined by the frame:
\[
R(T_F^*).
\]
Indeed, if \(T_F=KPU_F\), then
\[
T_F^*=U_F^*PK^*=U_F^*K^*,
\]
because \(R(K^*)=R(K^\dagger)\) is the range of \(P\). Therefore
\[
R(T_F^*)=U_F^*R(K^*),
\]
and the left side is independent of every auxiliary unitary choice. Its dimension is \(\operatorname{rank}(T_F)=m\). This supplies a canonical Grassmannian invariant, but no assertion is made that replacing the source map by this invariant automatically restores the source's full bijection.

## Verification
The published theorem states the correspondence, defines \(\Phi(F)=U_F^*KPU_FH\), and immediately declares the map well-defined. The preceding theorem supplies the representation \(f_j=KPe'_j\), but it does not make the representing orthonormal basis unique.

All matrix identities in the counterexample are exact. Direct multiplication gives
\[
K^\dagger=K^*,\quad KP=K,\quad KQ=K,\quad KPU=KPV.
\]
The two candidate images are computed exactly and are orthogonal one-dimensional subspaces. No finite search, floating-point computation, or numerical approximation is used as evidence for the claim.

## Relationship to prior work
The source presents Theorem 3.3 as a \(K\)-frame generalization of an earlier finite-frame correspondence in Casazza--Kovačević. The obstruction here is specific to the operator-valued generalization: the synthesis factorization determines \(KPU_F\), but the proposed image uses the action of \(U_F^*\) on \(R(K)\). When \(R(K)\) and \(R(K^*)\) differ, freedom on the kernel directions of \(KP\) can change that image without changing the frame.

Targeted searches for the exact title, arXiv identifier, theorem number, Grassmannian/correspondence language, synthesis-factorization formulation, nonnormal \(K\), and choice-dependence did not locate an indexed source giving this counterexample or the same source-specific correction. A later paper on continuous Parseval \(K\)-frames is related in topic but its publicly visible scope concerns continuous \(K\)-frames and equal-norm extensions, not this finite-dimensional correspondence.

## Limitations
The finding disproves the correspondence as constructed for general closed-range \(K\). It does not claim that no different correspondence can be established under additional hypotheses, nor that the canonical invariant \(R(T_F^*)\) is by itself a bijective replacement.

A residual literature risk remains that an unindexed erratum, thesis remark, or informal correction may contain the same observation.

## References
1. V. Sadri and G. Rahimlou, *Equal-norm parseval K-frames in Hilbert Spaces*, arXiv:2104.11656v1, 23 April 2021.
2. V. Sadri and G. Rahimlou, *Equal-norm Parseval K-frames in Hilbert spaces with a new inequality*, Journal of Inequalities and Applications 2022, article 127, DOI 10.1186/s13660-022-02862-5.
3. P. G. Casazza and J. Kovačević, *Equal-norm tight frames with erasures*, Advances in Computational Mathematics 18 (2003), 387--430.
4. M. Rossafi and H. Massit, *Equal-norm Parseval continuous K-frames in Hilbert spaces*, Annals of Mathematics and Computer Science 22 (2024), DOI 10.56947/amcs.v22.281.
