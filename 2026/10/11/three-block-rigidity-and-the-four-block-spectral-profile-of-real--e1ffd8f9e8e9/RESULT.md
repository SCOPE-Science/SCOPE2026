# Three-block rigidity and the four-block spectral profile of real Paley harmonic fusion planes

## Finding

Let \(q\ge5\) be a prime power with \(q\equiv1\pmod4\), and let \(\chi:\mathbb F_q\to\{0,\pm1\}\) be the quadratic character. In the real harmonic equi-isoclinic tight fusion frame of Fickus, Iverson, Jasper, and Mixon [1], choose a real orthonormal basis \(\Phi_a\in\mathbb R^{q\times2}\) for each plane indexed by \(a\in\mathbb F_q\). The joint Gram matrix on an index set \(A\subseteq\mathbb F_q\) is \(G_A=(\Phi_a^{\mathsf T}\Phi_b)_{a,b\in A}\). After fixed orthogonal changes of the plane bases, its diagonal blocks are \(I_2\), and for distinct indices its blocks are

\[
(G_A)_{ab}=\frac1{q-1}
\begin{pmatrix}1&\sqrt{q-2}\,\chi(a-b)\\
\sqrt{q-2}\,\chi(a-b)&-1\end{pmatrix}.
\]

**Universal three-plane spectrum.** For *every* three-element \(A\), the six eigenvalues of \(G_A\), counted with multiplicity, are

\[
1+\frac2{\sqrt{q-1}},\quad 1-\frac2{\sqrt{q-1}},\quad
1+\frac1{\sqrt{q-1}}\ (\text{twice}),\quad
1-\frac1{\sqrt{q-1}}\ (\text{twice}).
\]

Thus the sharp three-block restricted isometry constant for this frame is \(\delta_3=2/\sqrt{q-1}\).

**Complete four-plane profile at \(q=13\).** Set \(M_A=12(G_A-I_8)\) for each four-element \(A\subseteq\mathbb F_{13}\). There are precisely four possibilities for \(\det(tI_8-M_A)=P_A(t^2)\), each with the indicated number of distinct index sets:

| Number of sets | Representative \(A\) | \(P_A(Y)\) |
| ---: | --- | --- |
| 78 | \(\{0,1,2,3\}\) | \((Y-100)(Y-20)(Y-12)^2\) |
| 390 | \(\{0,1,2,4\}\) | \((Y-12)^2(Y^2-120Y+3408)\) |
| 195 | \(\{0,1,2,6\}\) | \((Y-56)^2(Y^2-32Y+64)\) |
| 52 | \(\{0,1,3,9\}\) | \((Y-108)(Y-12)^3\) |

In particular, the sharp four-block restricted isometry constant is

\[
\boxed{\delta_4=\frac{\sqrt{108}}{12}=\frac{\sqrt3}{2}.}
\]

Equality in the four-block bound holds for **exactly 52** unordered quartets: precisely \(A=b+a\{0,1,3,9\}\), with \(a\in\mathbb F_{13}^{\times}\) and \(b\in\mathbb F_{13}\). The affine action has a three-element stabilizer on this quartet, so there are \(13\cdot12/3=52\) distinct sets.

## Assumptions and scope

The matrices are the *real* quadratic-character instance of the harmonic construction in [1], not arbitrary tight fusion frames. Only prime powers congruent to one modulo four are covered by the universal triple statement; the complete four-block census is for \(q=13\). Define the block restricted isometry constant by

\[
\delta_k=\max_{|A|=k}\|G_A-I_{2k}\|_{\mathrm{op}}.
\]

Equivalently, \(\delta_k\) is the maximum distance of an eigenvalue of \(G_A\) from \(1\). This is the standard block-Gram formulation in the regime \(2k\le q\), and agrees with the projection formulation of [3] there. At \(q=5,k=3\), the Gram definition still applies even though six columns lie in five dimensions.

## Proof

**1. The normalized blocks.** Theorem 4.2 and equations (41), (42), and (44) of [1] give a harmonic real equi-isoclinic family for quadratic \(\chi\). The quadratic Gauss sum, divided by its magnitude, gives a fixed real sign; conjugating all two-dimensional plane bases by \(\operatorname{diag}(1,-1)\) if necessary removes it. Each off-diagonal block is thus the displayed real symmetric matrix. Setting

\[
U_{ab}=\frac1{\sqrt{q-1}}
\begin{pmatrix}1&\sqrt{q-2}\,\chi(a-b)\\
\sqrt{q-2}\,\chi(a-b)&-1\end{pmatrix}
\]

makes every \(U_{ab}\) a real orthogonal reflection, with \(U_{ab}^{\mathsf T}=U_{ab}=U_{ba}\) and \(\det U_{ab}=-1\). We have \((G_A-I_{2|A|})=T_A/\sqrt{q-1}\), where \(T_A\) has zero diagonal blocks and off-diagonal blocks \(U_{ab}\).

**2. The three-plane spectrum.** For indices \(a,b,c\), independently rotate the three plane bases so that two off-diagonal blocks of \(T_A\) become \(I_2\). The remaining block is the orthogonal holonomy \(H=U_{ab}U_{bc}U_{ca}\). As the product of three reflections in dimension two, \(H\) is again a reflection and has eigenvalues \(1,-1\). Diagonalizing \(H\) splits \(T_A\) into two scalar three-by-three signed triangle adjacency matrices. Their spectra are \(\{2,-1,-1\}\) and \(\{-2,1,1\}\), respectively. Scaling by \(1/\sqrt{q-1}\) and adding identity proves the universal statement.

**3. A finite exact algebra for four planes.** Let \(A=\{a_1,a_2,a_3,a_4\}\subset\mathbb F_{13}\). Define real symmetric four-by-four matrices \(C\) and \(S\) by \(C_{ii}=S_{ii}=0\), \(C_{ij}=1\), and \(S_{ij}=\chi(a_i-a_j)\) for unequal indices. On ordering all first and then all second plane coordinates,

\[
M_A=\begin{pmatrix}C&\sqrt{11}\,S\\\sqrt{11}\,S&-C\end{pmatrix}.
\]

Put \(K=C+i\sqrt{11}\,S\). The real symmetric matrix \(M_A\) represents the antilinear operation \(z\mapsto K\overline z\). Its eigenvalues occur in opposite pairs (multiplication of \(z\) by \(i\) reverses the eigenvalue); their squared values are exactly the eigenvalues of the Hermitian matrix

\[
H=KK^*=C^2+11S^2+i\sqrt{11}(SC-CS).
\]

Consequently, \(\det(tI_8-M_A)=\det(t^2 I_4-H)\). Every coefficient of the polynomial on the right is an integer, obtained exactly from the traces of \(H,H^2,H^3,H^4\) through Newton identities. In particular, with \(s_j=\operatorname{tr}(H^j)\) and \(e_0=1\),

\[
e_j=\frac1j\sum_{h=1}^j(-1)^{h-1}e_{j-h}s_h,
\qquad P_A(Y)=\sum_{j=0}^4(-1)^je_jY^{4-j}.
\]

All operations in this recurrence are exact integer operations, so no numerical eigenvalue approximation is needed. The checker implements the recurrence directly.

**4. Exhaustiveness and sharpness.** The standalone checker enumerates all \(\binom{13}{4}=715\) four-element subsets, constructs \(C,S,H\) with integer arithmetic in the basis \(\{1,i\sqrt{11}\}\), evaluates the four trace powers and characteristic coefficients, and verifies that the four factorizations above occur respectively \(78,390,195,52\) times. It checks explicitly that the exceptional collection equals the 52 distinct affine images of \(\{0,1,3,9\}\). This is a complete finite enumeration, not sample-based inference.

The maximal roots of \(P_A\) in the four rows are respectively \(100\), \(60+8\sqrt3\), \(56\), and \(108\). Because \(\|G_A-I_8\|_{\mathrm{op}}=\sqrt{\max\operatorname{roots}(P_A)}/12\), only the last row attains \(\sqrt{108}/12=\sqrt3/2\). This proves both sharpness and the complete equality classification.

## Verification

Run `python3 checker.py` using the Python 3 standard library. Its successful result is `CHECK_PASS 715 quartets, 286 triples, 10 five-field triples, four exact profiles`, preceded by the four exact coefficient profiles and their counts. The program performs complete enumeration, not a random experiment. The universal triple proof is algebraic and is independent of the finite checks; tests at \(q=5\) and \(q=13\) provide additional diagnostics. The four-block statement is finite and the exhaustive computation is part of its proof.

## Relationship to prior work

The harmonic real fusion planes and their off-diagonal block form are **from** [1], not newly constructed here. The conference-matrix representation in [2] gives another presentation of these objects but does not tabulate the four-plane principal block spectra. Work on totally symmetric Grassmannian codes [3] explains the significance of the block restricted isometry constants and constructs different, highly symmetric families; it leaves their block-erasure analysis for subsequent work. The present contribution is the three-block reflection-holonomy rigidity together with the complete, nonuniform four-block eigenvalue census, sharp constant, and optimizer classification in the explicitly given real 13-plane family. General frame-erasure theory [4] does not supply these quartic characteristic polynomials or their multiplicities.

## Limitations

No claim is made about arbitrary fusion frames, about all \(q\) for four-plane spectra, or about larger block sizes. The four-block theorem uses exhaustive exact computation and the provided source code as a finite certificate; it is not an infinite-family classification. The literature comparison is not an assertion that no equivalent conference-matrix spectrum calculation has ever appeared. All claims are mathematical and remain subject to independent verification.

## References

[1] M. Fickus, J. W. Iverson, J. Jasper, and D. G. Mixon, *Harmonic Grassmannian codes*, arXiv:2112.14267 (first available 28 December 2021), Theorem 4.2, equations (41), (42), and (44). https://arxiv.org/abs/2112.14267

[2] M. Fickus, J. W. Iverson, J. Jasper, and D. G. Mixon, *Equi-isoclinic subspaces, covers of the complete graph, and complex conference matrices*, arXiv:2212.12617 (23 December 2022), Proposition 8. https://arxiv.org/abs/2212.12617

[3] M. Fickus, J. W. Iverson, J. Jasper, and D. G. Mixon, *Totally symmetric Grassmannian codes*, arXiv:2406.19542 (first available 27 June 2024), discussion of block restricted isometry. https://arxiv.org/abs/2406.19542

[4] Q. Cheng, F. Lv, and W. Sun, *Frames of uniform subframe bounds with applications to erasures*, Linear Algebra Appl. **555** (2018), 186–200, doi:10.1016/j.laa.2018.05.025.
