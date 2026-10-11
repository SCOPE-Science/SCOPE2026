# An isometry/co-isometry reversal in a controlled \(K\)-frame invariance theorem

## Finding
Theorem 3.6 of Rajput--Sahu, later published with Mishra, states that a \\(C\\)-controlled \\(K\\)-frame remains a \\(C\\)-controlled \\(K\\)-frame for the whole module after applying an isometry \\(T\\), under the displayed range and commutation assumptions. The statement is false already in the scalar Hilbert-space specialization.

Let \\(H=\\ell^2(\\mathbb N)\\) with orthonormal basis \\((e_j)_{j\\ge 1}\\), let \\(C=K=I\\), and let \\(T\\) be the unilateral shift \\(Te_j=e_{j+1}\\). Then \\((e_j)\\) is a Parseval \\(C\\)-controlled \\(K\\)-frame, \\(T\\) is an isometry, \\(C,K,T\\) commute, \\(R(T^*K^*)=R(K^*T^*)=H\\), and \\(R(TK)=R(T)\\) is closed and orthogonally complemented. Nevertheless, for \\(f=e_1\\),
\[
\sum_{j\\ge 1}|\\langle f,Te_j\\rangle|^2=0
\quad\\text{{while}}\\quad
\\|K^*f\\|^2=1,
\]
so \\((Te_j)\\) has no positive lower \\(K\\)-frame bound.

The proof identifies the defect: it writes \\(\\|x\\|=\\|T^*x\\|\\) from the assumption that \\(T\\) is an isometry. An isometry gives \\(T^*T=I\\), not \\(TT^*=I\\). The displayed identity is guaranteed when \\(T\\) is a co-isometry. Replacing “isometry” by “co-isometry” therefore repairs that proof under its remaining assumptions. The earlier uncontrolled operator-invariance theorem in Mahmoudieh--Abbaspour Tabadkan--Arefijamaal uses precisely the co-isometry hypothesis and the corresponding valid identity.

For \\(C=K=I\\), the exact boundary inside the class of isometries is especially transparent: \\((Te_j)\\) is a frame for \\(H\\) if and only if \\(T\\) is surjective, hence unitary.
## Assumptions and scope
A Hilbert space is the special case of a Hilbert \\(C^*\\)-module over the scalar algebra, so a Hilbert-space counterexample falsifies the stated module theorem. The counterexample uses the standard unilateral shift on \\(\\ell^2(\\mathbb N)\\), whose range is the closed codimension-one subspace \\(e_1^\\perp\\).

The repair asserted here is source-local: replacing “isometry” by “co-isometry” makes the displayed proof valid under the theorem's other hypotheses. No necessity claim is made for co-isometry for arbitrary \\(C\\) and \\(K\\). Necessity is claimed only in the explicitly stated specialization \\(C=K=I\\) within the class of isometries.
## Proof
For the original family \\((e_j)\\),
\[
\sum_{j\\ge1}|\\langle f,e_j\\rangle|^2=\\|f\\|^2=\\|K^*f\\|^2,
\]
so it is Parseval. The unilateral shift satisfies \\(T^*T=I\\), hence is an isometry. Since \\(K=C=I\\), all commutation requirements are automatic. Also \\(T^*\\) is onto, so
\[
R(T^*K^*)=R(T^*)=H=R(K^*T^*),
\]
and \\(R(TK)=R(T)=e_1^\\perp\\) is orthogonally complemented.

Yet \\(Te_j=e_{j+1}\\), and therefore \\(e_1\\) is orthogonal to every transformed atom. This gives zero transformed frame energy at a vector with nonzero \\(K^*\\)-norm and proves failure.

The source proof uses, after declaring \\(T\\) an isometry, the equality
\[
\\|C^{1/2}K^*f\\|^2=\\|T^*C^{1/2}K^*f\\|^2.
\]
That equality follows from \\(TT^*=I\\), because then \\(T^*\\) is an isometry. Thus it is valid for a co-isometry \\(T\\), not for an arbitrary isometry. With “co-isometry” substituted, the remainder of the displayed lower-bound argument proceeds as written, while the controlled Bessel upper bound is supplied by the preceding proposition.

Finally, when \\(C=K=I\\) and \\(T\\) is an isometry,
\[
\sum_{j\\ge1}|\\langle f,Te_j\\rangle|^2=\\|T^*f\\|^2=\\|P_{R(T)}f\\|^2.
\]
This has a positive lower frame bound on all of \\(H\\) exactly when \\(R(T)=H\\). A surjective isometry is unitary, proving the stated exact boundary.
## Verification
Every counterexample hypothesis is checked symbolically. No finite sampling or numerical extrapolation is used. The critical operator identities are \\(T^*T=I\\) for an isometry, \\(TT^*=I\\) for a co-isometry, surjectivity of the backward shift \\(T^*\\), and \\(TT^*=P_{R(T)}\\) for an isometry with closed range.

The published 2022 theorem page was inspected directly and still states “isometry” while using the norm-preservation identity for \\(T^*\\). The earlier 2020 uncontrolled theorem was checked at its theorem statement and proof; it states “co-isometry” and uses the same norm-preservation mechanism correctly.
## Relationship to prior work
Mahmoudieh, Abbaspour Tabadkan, and Arefijamaal proved an earlier operator-invariance theorem for ordinary \\(K\\)-frames with a co-isometry hypothesis. Their proof uses \\(\\|K^*x\\|=\\|T^*K^*x\\|\\), which is valid because a co-isometry has isometric adjoint. Their following remark also records a surjectivity boundary under a dense-range hypothesis.

The present finding does not claim the general range-theoretic characterization of all operators preserving all \\(K\\)-frames; related literature already studies those range conditions. The claim is the source-specific failure of the controlled theorem under its printed isometry hypothesis, the explicit unilateral-shift witness, and the co-isometry repair of its proof.
## Limitations
The counterexample lives in the scalar Hilbert-space specialization rather than a genuinely noncommutative module; this is sufficient to disprove the general statement. The repair is a sufficient correction matching the proof and the earlier theorem. It is not asserted to be the only possible repair for arbitrary \\(C\\), \\(K\\), and \\(T\\).

No claim is made that every later paper using controlled \\(K\\)-frames inherits this defect; only the inspected theorem and its stated proof are assessed.
## References
1. E. Rajput and N. K. Sahu, *Controlled \\(K\\)-frames in Hilbert \\(C^*\\)-modules*, arXiv:1903.09928v1, 24 March 2019; revised as arXiv:1903.09928v2.
2. E. Rajput, N. K. Sahu, and V. N. Mishra, *Controlled \\(K\\)-frames in Hilbert \\(C^*\\)-modules*, Korean Journal of Mathematics 30 (2022), 91--107, doi:10.11568/kjm.2022.30.1.91.
3. M. Mahmoudieh, G. Abbaspour Tabadkan, and A. Arefijamaal, *Sum of \\(K\\)-Frames in Hilbert \\(C^*\\)-Modules*, Filomat 34 (2020), 1771--1780, doi:10.2298/FIL2006771M.
