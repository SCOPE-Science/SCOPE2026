# Complete tripartite graphical-group character degrees from symplectic pullback ranks

## Finding

For every finite field \(\mathbb F_q\) and every three positive integers \(a,b,c\), we give an explicit finite product-and-sum formula for the rank of every alternating matrix whose entries within each of three diagonal blocks of sizes \(a,b,c\) vanish. When \(q\) is odd, this simultaneously determines the full complex irreducible-character degree distribution of the two-step nilpotent graphical group of the complete tripartite graph \(K_{a,b,c}\). Unlike universal-vertex coning formulas, the result includes three arbitrarily large parts, such as \(K_{3,3,3}\).

Put \(n=a+b+c\) and \(m=ab+ac+bc\). Let \(\mathcal A_{a,b,c}(q,z)=\sum_{j\geq0}A_j(q)z^j\), where \(A_j(q)\) is the number of allowed alternating matrices of rank \(2j\). To specify the answer, for \(0\leq r\leq\min(d,e)\), define
\[
M_q(d,e;r)={d\brack r}_q\prod_{i=0}^{r-1}(q^e-q^i),\qquad
{d\brack r}_q=\prod_{i=0}^{r-1}\frac{q^{d-i}-1}{q^{r-i}-1}.
\]
Empty products are one. Write
\[
S_q(v)=q^{v^2}\prod_{i=1}^{v}(q^{2i}-1),\quad
I_q(v,u)=\prod_{i=0}^{u-1}\frac{q^{2v-i}-q^i}{q^u-q^i},\quad
N_q(v,t)=\frac{S_q(v)}{S_q(t)S_q(v-t)}.
\]
The domains are \(v\geq0\), \(0\leq u\leq v\), and \(0\leq t\leq v\). These are, respectively, the order of a symplectic group, the number of isotropic \(u\)-planes in a symplectic \(2v\)-space, and the number of nondegenerate \(2t\)-planes therein. For \(0\leq t\leq\min(v,\lfloor h/2\rfloor)\), set
\[
H_q(v,h;t)=\sum_{u=0}^{\min(v,h-2t)} I_q(v,u)N_q(v-u,t)
\prod_{i=0}^{2t+u-1}(q^h-q^i).
\]
Then the complete rank enumerator is
\[
\boxed{\mathcal A_{a,b,c}(q,z)
=\sum_{r=0}^{\min(a,b)}\ \sum_{s=0}^{\min(a+b-2r,c)}\
\sum_{t=0}^{\min(r,\lfloor(c-s)/2\rfloor)}
M_q(a,b;r)M_q(a+b-2r,c;s)q^{2rs}
H_q(r,c-s;t)\,z^{r+s+t}.}
\]
All factors are explicit integers; the expression is valid in even and odd characteristic. In particular, \(\mathcal A_{a,b,c}(q,1)=q^m\).

For odd \(q\), if \(G=G_{K_{a,b,c}}(\mathbb F_q)\) is the graphical class-two group, its number of ordinary complex irreducible representations of degree \(q^j\) is exactly
\[
\boxed{\operatorname{ch}_{q^j}(G)=q^{n-2j} A_j(q).}
\]
There are no other irreducible character degrees, and the degree-squared identity is \(\sum_j\operatorname{ch}_{q^j}(G)q^{2j}=q^{n+m}=|G|\).

For the first symmetric three-wide example, \(K_{3,3,3}\) over \(\mathbb F_3\), the rank-half enumerator has coefficients
\[
(A_0,A_1,A_2,A_3,A_4)=(1,44954,322403328,344675474208,7280599562496).
\]
The corresponding character multiplicities at degrees \(1,3,9,27,81\) are \(19683,98314398,78344008704,9306237803616,21841798687488\), respectively.

## Assumptions and scope

The graph is the **complete simple tripartite graph** with part sizes \(a,b,c\geq1\); all its cross-part edges have independent arbitrary field weights, including zero. The allowed matrix is \(B\in M_n(\mathbb F_q)\), alternating (meaning \(B^T=-B\) and all diagonal entries are zero, also in characteristic two). Matrix ranks are ordinary ranks over \(\mathbb F_q\) and are always even. No restrictions on \(q\) are needed for the matrix formula. The character-theoretic assertion assumes odd \(q\) so that the class-two exponent-\(p\) model and the standard finite orbit-method formula apply. This assertion concerns ordinary complex characters, not modular representations or conjugacy-class sizes.

## Proof

**1. Rank decomposition.** Order the three vertex parts and write every matrix uniquely as
\[
B=\begin{pmatrix}
0&X&Y\\ -X^T&0&Z\\ -Y^T&-Z^T&0
\end{pmatrix},\quad
X\in M_{a,b}(\mathbb F_q),\ Y\in M_{a,c}(\mathbb F_q),\ Z\in M_{b,c}(\mathbb F_q).
\]
The number of matrices \(X\) of rank \(r\) is \(M_q(a,b;r)\). Independent invertible changes of basis in the first two vertex parts carry \(X\) to its rank normal form without changing ranks or altering the set of possible \(Y,Z\). Split these parts into the \(r+r\) hyperbolic coordinates and their remaining \(a+b-2r\) coordinates, and split the columns of \((Y^T,Z^T)^T\) correspondingly into an arbitrary \(P\in M_{2r,c}\) and \(C\in M_{a+b-2r,c}\).

**2. Two Schur reductions.** The nondegenerate \(2r\)-dimensional alternating block can be eliminated by simultaneous row/column operations. The remaining alternating form, on the residual \(a+b-2r\) coordinates and the third part, has the block shape
\[
\begin{pmatrix}0&C\\-C^T&P^TJP\end{pmatrix}
\]
up to sign in the last block, where \(J\) is a fixed nondegenerate alternating matrix of size \(2r\). If \(s=\operatorname{rank}C\), a second hyperbolic elimination contributes rank \(2s\); the remaining form is exactly the restriction of \(P^TJP\) to \(\ker C\). Therefore
\[
\tfrac12\operatorname{rank}B=r+s+\tfrac12\operatorname{rank}(P|_{\ker C})^TJ(P|_{\ker C}).
\]
There are \(M_q(a+b-2r,c;s)\) choices of \(C\) of rank \(s\), and \(\dim\ker C=c-s\). Once \(C\) is fixed, every map \(\ker C\to\mathbb F_q^{2r}\) extends to precisely \(q^{2rs}\) matrices \(P\). Consequently it remains only to count the ranks of symplectic pullbacks from a vector space of dimension \(c-s\) into a symplectic space of dimension \(2r\).

**3. Symplectic-pullback count.** Let \(P:V\to W\) range over all maps from an \(h\)-space \(V\) into a \(2v\)-dimensional symplectic \(W\). If the alternating form \(P^TJP\) has rank \(2t\), the image \(R=\operatorname{im}P\) has dimension \(2t+u\) for some \(0\leq u\leq\min(v,h-2t)\); its restricted alternating form has radical \(R_0=R\cap R^\perp\) of dimension \(u\). First choose the totally isotropic \(R_0\), in \(I_q(v,u)\) ways. Then the induced quotient \(R/R_0\) is a nondegenerate \(2t\)-plane in the symplectic quotient \(R_0^\perp/R_0\) of dimension \(2(v-u)\), chosen in \(N_q(v-u,t)\) ways. Conversely the inverse image of that nondegenerate plane in \(R_0^\perp\) has a unique subspace \(R\) containing \(R_0\), namely its full preimage; this preimage has dimension \(2t+u\) and radical exactly \(R_0\). Finally, the number of surjective maps \(V\twoheadrightarrow R\) equals \(\prod_{i=0}^{2t+u-1}(q^h-q^i)\). Summing over \(u\) proves the expression for \(H_q(v,h;t)\). The isotropic and nondegenerate subspace counts follow by elementary symplectic basis completion and orbit-stabilizer, valid in every characteristic.

**4. Collect the ranks.** Multiplying the independent choices from steps 1–3 and recording \(j=r+s+t\) proves the boxed threefold sum. Because it partitions all matrices \((X,Y,Z)\), summing coefficients counts \(q^{ab+ac+bc}\) matrices exactly.

**5. Character degrees in odd characteristic.** The graphical group for this graph has a vector-space quotient of dimension \(n\) by its commutator subgroup and center of dimension \(m\), with alternating commutator form given by the independent edge coordinates. By the class-two orbit-method character formula, each linear functional on that center whose associated alternating commutator form has rank \(2j\) gives \(q^{n-2j}\) irreducible complex characters, each of degree \(q^j\). Distinct edge functionals correspond bijectively to our matrices \(B\). This establishes the character formula, with the squared-degree identity following directly from \(\sum_j A_j=q^m\).

## Verification

The standalone script `artifacts/verify_tripartite.py` implements the closed formula using integer arithmetic. It independently enumerates every choice of cross-part matrix weights and computes alternating matrix ranks in 12 prime-field examples over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_5\), including \(K_{2,2,2}\) in characteristics two and three. A separate implementation of \(\mathbb F_4=\mathbb F_2[T]/(T^2+T+1)\) tests three extension-field examples. It also directly enumerates selected small symplectic pullbacks to verify the auxiliary formula. These are finite checks; the proof above, not these experiments, establishes the all-parameter theorem. Running `python3 artifacts/verify_tripartite.py` prints `VERIFY_OK_TRIPARTITE_RANK_DISTRIBUTION` on success.

As a larger arithmetic consistency calculation, the formula gives the displayed \(K_{3,3,3}\) coefficients; their sum is \(3^{27}\), and their degree-weighted multiplicity sum is \(3^{36}\). This arithmetic check is not a brute-force enumeration of \(3^{27}\) matrices.

## Relationship to prior work

O'Brien–Voll (2012, arXiv:1203.3050) supplies general class-two character enumeration through commutator-matrix ranks and presents, among other examples, a \(K_{2,2}\) calculation. The contribution here is an explicit all-ranks, all-three-part-sizes evaluation of the previously unevaluated constrained alternating matrix family. Klein–Lewis–Morales (2012, arXiv:1203.5804) studies ranks of *unrestricted* support-constrained matrices, not the alternating condition tying transposed entries. Fulman–Goldstein (2012, arXiv:1211.0504) develops complete alternating-matrix rank laws, but not this three-block-zero subspace.

Rossmann–Voll (2019, arXiv:1908.09589, Proposition 8.7) already computes **conjugacy-class zeta data** for complete multipartite graphical groups; that result is relevant but does not give this ordinary **character-degree distribution**. Rossmann (2021, arXiv:2107.05564, Question 1.10) explicitly distinguishes character-degree enumeration from conjugacy-class enumerators and formulates the former as a question for graphical groups. Previously available one-universal-vertex and independent-two-universal-vertex rank recurrences yield special cases where at least one part has size at most two; they do not directly evaluate all \(K_{a,b,c}\) with three large parts. The present method uses a symplectic pullback term that those narrower recurrences do not supply.

## Limitations

The formula concerns precisely three complete independent parts. It does not establish a comparable closed formula for four or more parts, missing cross edges, or arbitrary graphical groups. The matrix enumeration applies in all characteristics; the character-degree consequence is stated only for odd \(q\). No claim is made about modular character theory, isomorphism classification, geometric irreducibility, or whether alternative equivalent formulas have appeared earlier. The finite tests are not a proof. Historical priority is assessed against the specified accessible literature and searchable published findings, not certified exhaustive.

## References

1. E. A. O'Brien and C. Voll, *Enumerating classes and characters of p-groups*, arXiv:1203.3050, first public 14 March 2012; full manuscript, especially Theorem A and Example 4.4.
2. A. J. Klein, J. B. Lewis, and A. H. Morales, *Counting matrices over finite fields with support on skew Young diagrams and complements of Rothe diagrams*, arXiv:1203.5804, first public March 2012, abstract and Sections 1–3.
3. J. Fulman and L. Goldstein, *Stein's method and the rank distribution of random matrices over finite fields*, arXiv:1211.0504, first public November 2012.
4. T. Rossmann and C. Voll, *Groups, graphs, and hypergraphs: average sizes of kernels of generic matrices with support constraints*, arXiv:1908.09589, 2019, especially Proposition 8.7.
5. T. Rossmann, *Enumerating conjugacy classes of graphical groups over finite fields*, arXiv:2107.05564, 2021, especially Section 1.6 and Question 1.10.
