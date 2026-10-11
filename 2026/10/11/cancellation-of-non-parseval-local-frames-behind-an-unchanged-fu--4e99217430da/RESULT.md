# Cancellation of non-Parseval local frames behind an unchanged fusion frame operator

## Finding
Part (1) of Corollary 4.12 in Köhldorfer--Balazs, *On the relation of the frame-related operators of fusion frame systems*, claims that equality of the global and fusion frame operators forces the block-diagonal local defect to vanish on the range of fusion analysis. That implication fails for redundant fusion frames.

For a fusion frame system \((V_i,v_i,\varphi^{(i)})\), let
\[
\mathcal K=\bigoplus_i^{\ell^2}V_i,\qquad
C_Vf=(v_iP_{V_i}f)_i,\qquad
R=\operatorname{Ran}C_V.
\]
Let \(S_i\) be the local frame operators and put
\[
M=\bigoplus_i (I_{V_i}-S_i).
\]
The source correctly derives
\[
S_V-S_{v\varphi}=C_V^*MC_V.
\]
It then treats the vanishing of this operator, together with self-adjointness of \(M\), as forcing \(M|_R=0\). In fact, the exact implication is only
\[
P_RM|_R=0,
\]
equivalently \(MR\subseteq R^\perp\). Positive and negative local defects can cancel after synthesis without vanishing separately.

**Exact counterexample.** Take \(H=\mathbb C\), two identical fusion subspaces \(V_1=V_2=H\), weights \(v_1=v_2=1\), and local singleton frames
\[
\varphi^{(1)}=\{1/\sqrt2\},\qquad
\varphi^{(2)}=\{\sqrt{3/2}\}.
\]
The local frame operators are \(S_1=\tfrac12 I\) and \(S_2=\tfrac32 I\). Each is a valid local frame, and \(1/2,3/2\) are common lower/upper bounds. The fusion and global frame operators satisfy
\[
S_V=2I=S_{v\varphi}.
\]
However, \(C_V z=(z,z)\) and
\[
M=\begin{pmatrix}1/2&0\\0&-1/2\end{pmatrix},\qquad
M C_Vz=(z/2,-z/2),
\]
which is nonzero for every nonzero \(z\). Thus the claimed vanishing on \(R\) is false under every stated hypothesis of Corollary 4.12(1).

## Assumptions and scope
A fusion frame system consists of a fusion frame \((V_i,v_i)\) and local frames \(\varphi^{(i)}\) with uniform positive frame bounds. Consequently, the direct sum of local frame operators is bounded and self-adjoint. The fusion analysis operator is bounded below and has closed range \(R\), so its orthogonal projection \(P_R\) exists.

The counterexample is one-dimensional and uses only two fusion blocks. The fusion frame is redundant: its coefficient analysis range is a proper one-dimensional subspace of \(\mathbb C^2\). This is precisely the setting in which global cancellation becomes possible.

The finding concerns the first assertion of Corollary 4.12(1). Its stated fusion-Riesz-basis special case remains valid, because the analysis range is then the whole coefficient space. This result does not assert failure of other parts of the corollary, which may be protected by one-sided bounds.

## Proof
For any fusion frame system, the source's exact operator identity gives
\[
S_V-S_{v\varphi}=C_V^*MC_V.
\]
Since \(C_V(H)=R\), the right-hand side vanishes if and only if
\[
\langle Mr,s\rangle=0\qquad\text{for every }r,s\in R.
\]
Indeed, represent \(r=C_Vf\) and \(s=C_Vg\) and polarize the operator identity, or directly pair it with \(f,g\). These conditions are equivalent to
\[
P_RM|_R=0,
\]
which is equivalent to \(M(R)\subseteq R^\perp\). No inference to \(Mr=0\) is licensed without more structure.

For the example, the local frame operator of a scalar singleton \(\{c\}\) is multiplication by \(|c|^2\). Thus \(S_1=\tfrac12 I\), \(S_2=\tfrac32 I\). The fusion frame consists of two copies of \(H\) and satisfies
\[
\sum_{i=1}^2v_i^2\|P_{V_i}z\|^2=2|z|^2.
\]
The global frame is \(\{1/\sqrt2,\sqrt{3/2}\}\) and likewise has energy
\[
\left|\left\langle z,1/\sqrt2\right\rangle\right|^2+
\left|\left\langle z,\sqrt{3/2}\right\rangle\right|^2=2|z|^2.
\]
Therefore both frame operators equal \(2I\). But
\[
R=\operatorname{span}\{(1,1)\},\qquad
M(z,z)=(z/2,-z/2)\in R^\perp
\]
and this vector is nonzero when \(z\ne0\). In particular, the orthogonal projection onto \(R\) is
\[
P_R=\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix},
\]
so \(P_RMP_R=0\) while \(MP_R\ne0\). This proves failure of the source assertion.

If \(MR\subseteq R\), then the compression condition forces \(MR\subseteq R\cap R^\perp=\{0\}\). If \(M\) has a fixed sign, the vanishing quadratic form on \(R\) implies \(M^{1/2}r=0\) (for the nonnegative sign, and after negating for the other), hence \(Mr=0\). If the fusion frame is a fusion Riesz basis, then \(R=\mathcal K\), and the compressed equality forces \(M=0\). These are sufficient hypotheses restoring the stronger source conclusion.

**Classification of invisible local defects.** Let \(H=\mathbb C^d\) and \(V_i=H\) for \(1\le i\le m\) with \(m\ge2\) and \(v_i>0\). For positive definite local frame operators \(S_i\), direct calculation gives
\[
S_V=\left(\sum_i v_i^2\right)I_d,
\qquad
S_{v\varphi}=\sum_i v_i^2S_i.
\]
These agree exactly when
\[
\sum_i v_i^2T_i=0,\qquad T_i=S_i-I_d,\qquad I_d+T_i>0.
\]
Choose arbitrary self-adjoint \(T_1,\ldots,T_{m-1}\) satisfying positivity and set
\[
T_m=-\frac1{v_m^2}\sum_{i=1}^{m-1}v_i^2T_i,
\]
requiring the last positivity condition. Every such tuple is realized: if \((e_k)_{k=1}^d\) is an orthonormal basis, the vectors
\[
\varphi^{(i)}_k=S_i^{1/2}e_k
\]
form a local Riesz basis with frame operator exactly \(S_i\). The real vector space of self-adjoint \(d\times d\) matrices has dimension \(d^2\); positivity imposes only open convex inequalities. Thus the complete realizable family is a nonempty relatively open convex subset of a real linear space of dimension \((m-1)d^2\). The original two-block example is one point in that set.

## Verification
The publisher's open-access article and preprint were inspected at the fusion-frame-system definition, the frame-operator identity, Corollaries 4.10--4.12, and the complete proof of Corollary 4.12. The two journal PDF pages containing the statement and its proof were also inspected as rendered page images.

The critical printed step explicitly invokes only self-adjointness after obtaining a zero quadratic form. A self-adjoint indefinite operator can have nonzero off-diagonal blocks relative to \(R\oplus R^\perp\). In the example, the defect sends \(R\) into \(R^\perp\), and all operator identities can be verified using exact halves.

The proof of the replacement criterion is intrinsic to the analysis range and does not require a computational certificate. The finite-dimensional classification uses exact operator identities, the spectral theorem for positive definite matrices, and dimension counting; it is valid for all finite \(d\ge1\), \(m\ge2\), and positive weights.

## Relationship to prior work
Köhldorfer--Balazs formulate block-diagonal frame-operator identities for fusion frame systems and derive the disputed converse in Corollary 4.12(1). Their accompanying fusion-Riesz-basis conclusion is a genuine special case because surjectivity of fusion analysis eliminates the cancellation directions.

Casazza--Kutyniok--Li develop fusion frame systems and distributed processing with uniform local frame bounds, establishing the foundational framework used here. Leng's finite-dimensional fusion-frame-system constructions motivate flexible realizations of local systems but do not, in the checked material, resolve the specific false inference from aggregate operator equality to a zero local defect.

The new distinction is between zero compression of a block-diagonal self-adjoint operator and zero restriction to the analysis range. Equality of a global operator can hide indefinite local deviations whenever the fusion frame is redundant. The exact repeated-whole-space classification quantifies this freedom without asserting a general classification for arbitrary overlapping fusion subspaces.

## Limitations
Only part (1) of Corollary 4.12 is contradicted. The special conclusion for fusion Riesz bases remains true. In other statements, an additional one-sided sign or invariant-range hypothesis can support a stronger conclusion even when the displayed proof method is too broad.

The dimension \((m-1)d^2\) describes local frame operators for repeated full-dimensional subspaces, not the moduli space of local frames themselves, since many frames share the same operator. No necessity of the sufficient sign or invariant-range hypotheses is asserted.

This result does not claim that identical aggregate operators imply identical local reconstructions; nor does it compare all reconstruction algorithms. The possible existence of an unindexed theorem-specific correction remains a literature risk.

## References
1. L. Köhldorfer and P. Balazs, *On the relation of the frame-related operators of fusion frame systems*, Sampling Theory, Signal Processing, and Data Analysis 21 (2023), Article 9, DOI 10.1007/s43670-023-00049-7 (first public 9 February 2023); preprint arXiv:2303.15129v1.
2. P. G. Casazza, G. Kutyniok and S. Li, *Fusion frames and distributed processing*, Applied and Computational Harmonic Analysis 25 (2008), 114--132, DOI 10.1016/j.acha.2007.10.001.
3. J. Leng, *Construction of Fusion Frame Systems in Finite Dimensional Hilbert Spaces*, Abstract and Applied Analysis (2014), Article 836731, DOI 10.1155/2014/836731.
