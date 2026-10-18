# Twelve-column symmetry stabilization for four-row grid independence complexes

## Finding

For every integer \(n\ge2\), let \(G_n=P_n\square P_4\) be the rectangular grid with four vertices in each of \(n\) columns, and let \(X_n=\operatorname{Ind}(G_n)\). Let the commuting involutions
\[
a(i,j)=(n+1-i,j),\qquad b(i,j)=(i,5-j)
\]
act on \(X_n\). The complete character of the action on \(\widetilde H_{n-1}(X_n;\mathbb Q)\), listed at \((1,a,b,ab)\), is
\[
\chi_n=(-1)^n
\begin{cases}
(z_n,z_{h-1},p_n,z_{h+2}),&n=2h,\\
(z_n,z_{h+1},p_n,z_h-z_{h+1}+z_{h+3}),&n=2h+1.
\end{cases}
\]
The two integer sequences are specified without hidden numerical data:
\[
(z_0,z_1,z_2,z_3,z_4,z_5)=(1,0,1,-1,2,-1),\quad z_{m+6}=z_m+2(-1)^m,
\]
\[
(p_0,p_1,p_2,p_3,p_4,p_5)=(1,0,-1,-1,0,1),\quad p_{m+6}=p_m
\]
for all integers \(m\ge0\).

**Twelve-column representation stabilization.** Define \(s_n=1\) for \(n\equiv1,2\pmod4\) and \(s_n=-1\) for \(n\equiv0,3\pmod4\). Then, for every \(n\ge2\),
\[
\boxed{\chi_{n+12}-\chi_n=(4,2s_n,0,-2s_n).}
\]
Write \(\mathbf Q_{\epsilon_a,\epsilon_b}\) for the one-dimensional rational character on which \(a\) and \(b\) act by \(\epsilon_a,\epsilon_b\in\{+1,-1\}\), respectively. The character identity is equivalent to the following (noncanonical) rational representation isomorphism:
\[
\widetilde H_{n+11}(X_{n+12};\mathbb Q)\cong
\widetilde H_{n-1}(X_n;\mathbb Q)\oplus W_n,
\]
where
\[
W_n\cong\begin{cases}
\mathbf Q_{+,+}\oplus2\mathbf Q_{+,-}\oplus\mathbf Q_{-,+},&s_n=1,\\
\mathbf Q_{+,+}\oplus\mathbf Q_{-,+}\oplus2\mathbf Q_{-,-},&s_n=-1.
\end{cases}
\]
These are isomorphisms of abstract representations; no homomorphism between the two homology groups is asserted.

## Assumptions and scope

All complexes use ordinary independent vertex subsets, including the empty subset as the augmentation simplex in reduced chain groups. Graphs are simple with unit horizontal and vertical adjacency. All homology groups in the theorem use rational coefficients. The acting group is the specified subgroup \(K=\langle a,b\rangle\cong C_2\times C_2\); when the grid is square, larger geometric symmetries are not included in this claim.

The homological-concentration input is Theorem 1.1 of Matsushita and Wakatsuki [1], which proves that for each \(n\ge2\), \(X_n\) is homotopy equivalent to a wedge of spheres of dimension \(n-1\). With \(n=6q+r\), \(0\le r<6\), their sphere count is
\[
\beta_n=\begin{cases}
2q,&r=1,\\
2q+2,&r=4,\\
2q+1,&r\in\{0,2,3,5\}.
\end{cases}
\]
In particular the rational representation is concentrated in degree \(n-1\), and its dimension is \(\beta_n\). This known nonequivariant fact is used but not claimed as new.

## Proof

**1. Exact state transfer.** The admissible independent subsets of a four-vertex column are the eight bit masks
\[
\mathscr S=(0,1,2,4,5,8,9,10),
\]
where bit \(j\) represents row \(j+1\). Let \(\mathbf1\) be the length-eight all-ones column vector, let \(e_0^{\mathsf T}\) select the empty-mask coordinate, and set
\[
T_{A,B}=\begin{cases}(-1)^{|B|},&A\cap B=\varnothing,\\0,&A\cap B\ne\varnothing.\end{cases}
\quad (A,B\in\mathscr S).
\]
Here \(|B|\) counts the occupied positions. The signed independence sum with \(m\) columns is \(z_m=e_0^{\mathsf T}T^m\mathbf1\). Direct multiplication of the displayed integer matrix gives
\[
(T^6-I)\mathbf1=(2,1,1,1,0,1,0,0)^{\mathsf T}=:v,\qquad Tv=-v.
\]
The first six values of \(z\) are as displayed in the finding; multiplying the two identities by \(e_0^{\mathsf T}T^m\) proves \(z_{m+6}=z_m+2(-1)^m\) for every \(m\ge0\). These small integer matrix identities can also be verified by `python3 artifacts/verify.py`.

**2. Signed equivariant Hopf trace.** For \(g\in K\) and an independent set \(S\subseteq V(G_n)\) with \(gS=S\), let \(\operatorname{sgn}(g|S)\) be the sign of the vertex permutation restricted to \(S\). Define
\[
Z_g=\sum_{\substack{S\subseteq V(G_n)\text{ independent}\\gS=S}}
(-1)^{|S|}\operatorname{sgn}(g|S).
\]
On reduced simplicial chains, an invariant simplex \(S\) contributes \((-1)^{|S|-1}\operatorname{sgn}(g|S)\) to the alternating trace, including the augmentation basis from \(S=\varnothing\). Hence the reduced Hopf trace equals \(-Z_g\). Since reduced homology is concentrated in degree \(n-1\),
\[
\chi_n(g)=(-1)^n Z_g.
\]
This identity fixes both the degree shift and the orientation signs; it is not an unsigned fixed-face count.

**3. Identity and row reversal.** For \(g=1\) the state transfer yields \(Z_1=z_n\). Under \(b\), a columnwise invariant independent mask is either empty or the pair of extreme rows \(\{1,4\}\). The nonempty mask contributes sign \(-1\) from the transposition of its vertices, while its two selected vertices contribute cardinality sign \(+1\). Two neighboring columns cannot both use this mask. The resulting signed path independence sequence is \(Z_b=p_n\), with \(p_0=1\), \(p_1=0\), and recurrence \(p_m=p_{m-1}-p_{m-2}\). This has the period-six values specified above.

**4. Longitudinal reversal.** Under \(a\), each noncentral paired set of columns is exchanged and contributes signed weight \((-1)^{|A|}\) per left column, because \((-1)^{2|A|}\) comes from cardinality and \((-1)^{|A|}\) from swapped vertices. If \(n=2h\), the two central adjacent columns are exchanged and consequently both must be empty; this gives \(Z_a=z_{h-1}\). If \(n=2h+1\), the central column may be any admissible mask, and its cardinality supplies the usual terminal transfer weight; hence \(Z_a=z_{h+1}\).

**5. Half-turn.** Let \(r(A)\) reverse the four row positions in a mask. For \(n=2h\), the two central columns of a half-turn invariant set have masks \(A\) and \(r(A)\), so adjacency is equivalent to \(A\cap r(A)=\varnothing\). The boundary vector \(\alpha_A=\mathbf1_{A\cap r(A)=\varnothing}\) satisfies the exact identity
\[
\alpha=T^2\mathbf1.
\]
The same paired-column sign as above gives \(Z_{ab}=e_0^{\mathsf T}T^h\alpha=z_{h+2}\).

For \(n=2h+1\), the central column must be row-reversal invariant. Its only allowed masks are \(\varnothing\) and \(\{1,4\}\). The second contributes \(-1\), since its cardinality is even but its two vertices are exchanged. It is admissible precisely when the neighboring mask does not meet \(\{1,4\}\). Thus the net boundary vector is
\[
\beta_A=\mathbf1_{A\cap\{1,4\}\ne\varnothing}
=\left(\mathbf1-T\mathbf1+T^3\mathbf1\right)_A.
\]
The latter equality follows by multiplying the eight displayed states, not by an asymptotic argument. It follows that
\[
Z_{ab}=e_0^{\mathsf T}T^h\beta=z_h-z_{h+1}+z_{h+3}.
\]
Together with Step 2, these cases establish the four exact character entries for all \(n\ge2\).

**6. Stabilization and representation splitting.** For every \(m\ge0\), the exact recurrence implies \(z_{m+6}=z_m+2(-1)^m\) and \(z_{m+12}=z_m+4(-1)^m\), while \(p_{m+12}=p_m\). In the two parity cases for \(n\), the half-length \(h\) increases by six when \(n\) increases by twelve. Substitution into the four character entries gives
\[
\chi_{n+12}-\chi_n=(4,2s_n,0,-2s_n).
\]
The rational irreducible representations of \(C_2\times C_2\) are exactly its four one-dimensional sign characters. Taking the four Fourier coefficients of the difference character yields, in the order \((+,+),(+,-),(-,+),(-,-)\), multiplicities \((1,2,1,0)\) for \(s_n=1\) and \((1,0,1,2)\) for \(s_n=-1\). Semisimplicity over \(\mathbb Q\) proves the stated noncanonical decomposition.

## Verification

The self-contained `artifacts/verify.py` implements the eight-state transfer using exact Python integers. It verifies both matrix-vector identities \((T^6-I)\mathbf1=v\) and \(Tv=-v\), the two central boundary-vector identities, the complete recurrence and character formulas against all four signed traces of explicitly enumerated independent sets for every \(2\le n\le7\) (24 automorphism cases), and representation-stabilization identities for each \(2\le n<480\) (478 parameter cases). Independently, it constructs mod-two augmented simplicial boundaries for \(n=2,3,4,5\) and confirms that homology is concentrated in dimension \(n-1\) with the literature's ranks. The script prints `VERIFY_OK` on success.

The infinite result follows from Steps 1–6 and the cited homological-concentration theorem, not from finite enumeration or a computation timeout.

## Relationship to prior work

Matsushita and Wakatsuki [1, Theorem 1.1] classify the nonequivariant homotopy type, providing the wedge count and concentration used here. Okura [2, Appendix A, Proposition A.1] already computes the ordinary reduced Euler characteristic of four-row grids; accordingly the identity trace and the \(z\)-sequence are prior mathematics rather than independent discoveries. Bousquet-Mélou, Linusson, and Nevo [3] develop signed independence enumeration and transfer matrices for square-grid families. The result above refines these nonequivariant data by distinguishing the natural two commuting reflections, their composite, and their rational top-homology representation, including the explicit twelve-column decomposition. A general transfer-matrix method by itself does not supply the stated boundary identities or symmetry-module formula.

## Limitations

The result concerns ordinary independence complexes of open-ended four-row grids, the specified four-element symmetry subgroup, and rational representations. It does not claim a canonical inter-length map, an integral splitting, an equivariant homotopy equivalence, or a classification of any larger symmetry group in special square cases. Existing published work could contain an equivalent calculation under a different symmetry or transfer-matrix formulation; no globally exhaustive novelty certification is asserted. The accompanying finite verification is corroborating evidence and not a replacement for the parameter-uniform proof.

## References

1. T. Matsushita and S. Wakatsuki, *Independence complexes of \((n\times4)\) and \((n\times5)\)-grid graphs*, arXiv:2203.16391, first public 2022-03-30. https://arxiv.org/abs/2203.16391
2. K. Okura, *Simple homotopy types of independence complexes of graphs involving grid graphs*, arXiv:1908.09356, Appendix A, Proposition A.1. https://arxiv.org/abs/1908.09356
3. M. Bousquet-Mélou, S. Linusson, and E. Nevo, *On the independence complex of square grids*, arXiv:math/0701890 (2007). https://arxiv.org/abs/math/0701890
