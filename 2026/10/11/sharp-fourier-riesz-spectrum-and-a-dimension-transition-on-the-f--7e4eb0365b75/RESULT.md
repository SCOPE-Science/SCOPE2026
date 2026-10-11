# Sharp Fourier Riesz spectrum and a dimension transition on the finite-field Veronese cone

## Finding
Let \(q\ge3\) be any odd prime power, \(m\ge4\), and \(F=\mathbb F_q\). Write \(X=\{vv^{\mathsf T}:v\in F^m\}\), viewed as a subset of the additive group of symmetric \(m\times m\) matrices. Fix any nontrivial additive character \(\psi:F\to\mathbb C\) of unit modulus. For each unordered edge \(e=\{i,j\}\), \(1\le i<j\le m\), and \(t\in F^\times\), put \(\phi_{e,t}(vv^{\mathsf T})=\psi(tv_iv_j)\). Include the constant function \(\phi_0=1\). Equip functions on \(X\) with normalized counting inner product and put \(E=\binom m2\), \(N=q^m+1\), \(u=(1+q^{m-1})/N\), \(v=(1+q^{m-2})/N\). Define
\[
 a=1+(q-2)u,\quad b=(q-1)u,\quad c=(q-1)v,\quad
 B=a+2(m-2)b+\binom{m-2}{2}c,\quad h=u\sqrt{E(q-1)},
\]
\[
 L_\pm=\frac{1+B\pm\sqrt{(1-B)^2+4h^2}}2.
\]
The complete spectrum of the Gram matrix of these \(1+E(q-1)\) unit-norm functions (including multiplicities) is
\[
\begin{array}{c|c}
\text{eigenvalue}&\text{multiplicity}\\\hline
L_-&1\\
L_+&1\\
\displaystyle\lambda_{\rm f}=\frac{q^{m-1}(q-1)}{N}&E(q-2)\\
\displaystyle\lambda_{\rm s}=\frac{q^{m-2}(q-1)[m(q-1)-2q+3]}{N}&m-1\\
\displaystyle\lambda_{\rm c}=\frac{q^{m-2}(q-1)}{N}&E-m.
\end{array}
\]
All entries of this multiset are strictly positive, so the Fourier family is linearly independent. The sharp upper Riesz bound is always \(L_+\). The sharp lower bound undergoes the *exact integer transition*
\[
\lambda_{\min}=\begin{cases}
\lambda_{\rm c},&4\le m\le4(q^2-q+1),\\
L_-,&m\ge4(q^2-q+1)+1.
\end{cases}
\]
Thus its sharp squared condition number is \(L_+/\lambda_{\min}\). For each fixed odd \(q\) and \(m\to\infty\),
\[
L_+\sim\frac{(q-1)m^2}{2q^2},\quad
L_-\sim\frac{4(q-1)}m,\quad
\frac{L_+}{\lambda_{\min}}\sim\frac{m^3}{8q^2}.
\]
The proof below identifies all sharp equality coefficient spaces.

## Assumptions and scope
The field has odd characteristic, \(m\ge4\), and the ambient Hilbert space is \(L^2(X)\) with uniform probability measure. The family forms a Riesz sequence and therefore a basis of its own span; it is **not** claimed to span all of \(L^2(X)\). The normalized Gram matrix uses no scaling other than uniform averaging on \(X\); no assumptions about the particular nontrivial additive character are needed. The cone includes the zero matrix. The thresholds apply to integers \(m\) and prime powers \(q\), not to a continuous interpolation.

## Proof
**Point-counting identity.** The map \(v\mapsto vv^{\mathsf T}\) has the fiber \(\{0\}\) over zero and exactly two elements \(\{v,-v\}\) over every nonzero point of \(X\); hence \(|X|=(q^m+1)/2\). For any function \(f\) of the matrix \(vv^{\mathsf T}\),
\[
 \frac1{|X|}\sum_{A\in X}f(A)
 =\frac{f(0)+\sum_{v\in F^m}f(vv^{\mathsf T})}{q^m+1}.
\]

**Character sums and Gram entries.** The basic finite-field identity is \(\sum_{x,y\in F}\psi(sxy)=q\) for every \(s\ne0\), obtained by summing first over \(y\). For two distinct edges sharing vertex \(i\), the difference of their phases has the form \(v_i(sv_j-tv_k)\), and its sum over \(F^m\) is \(q^{m-1}\). The difference for two disjoint edges factors into two independent bilinear sums and equals \(q^{m-2}\). Two different frequencies on the same edge also yield \(q^{m-1}\). Therefore, with coefficient coordinates \(0\) and \((e,t)\), the Gram matrix has diagonal entries \(1\), \(G_{0,(e,t)}=u\), and the off-diagonal entries \(u\) whenever two frequencies use the same or intersecting edges, but \(v\) when their edges are disjoint. These values are real, positive, and independent of character choice.

**Orthogonal spectral decomposition.** The subspace of coefficient vectors whose frequency coefficients sum to zero *separately on every edge* has dimension \(E(q-2)\) and Gram eigenvalue \(1-u=\lambda_{\rm f}\). On its orthogonal complement, edge-frequency coefficients are constant on each edge, leaving one scalar coordinate and the \(E\)-dimensional complex edge space. The edge block is \(aI+bA+cD\), where \(A\) is adjacency in the Johnson graph \(J(m,2)\) (two edges intersect) and \(D\) is adjacency of disjointness.

Let \(I\) denote the unsigned vertex-edge incidence matrix of the complete graph. Then \(I^{\mathsf T}I=2I_E+A\) and \(II^{\mathsf T}=(m-2)I_m+J_m\). The edge space decomposes orthogonally into its constant line, the star space \(\{y_{ij}=w_i+w_j:\sum_i w_i=0\}\) of dimension \(m-1\), and the cycle-type space \(\{y:\sum_{j\ne i}y_{ij}=0\ \forall i\}\) of dimension \(E-m\). The adjacency eigenvalues of \(A\) on these three spaces are \(2(m-2)\), \(m-4\), and \(-2\). Since \(D=J_E-I_E-A\), substitution gives \(\lambda_{\rm s}=a+(m-4)b-(m-3)c\) and \(\lambda_{\rm c}=a-2b+c\), which simplify to the displayed formulas. The scalar function couples only to the constant edge line. Relative to the orthonormal coefficient basis \(\delta_0\) and \((E(q-1))^{-1/2}\mathbf1\) on edge-frequency coordinates, this remaining block is precisely
\[
 K=\begin{pmatrix}1&h\\h&B\end{pmatrix},
\]
with eigenvalues \(L_-\) and \(L_+\). This proves the full spectrum and all multiplicities.

**Strict positivity and sharp upper bound.** To prove independence without relying on numerical spectra, suppose a linear combination of the restricted characters vanishes on \(X\). Evaluate it on rank-one matrices \(vv^{\mathsf T}\) with at most one nonzero entry in \(v\); this fixes its baseline. Next choose \(v_i=1\), \(v_j=r\), all remaining entries zero. For every edge \(\{i,j\}\) the difference from the baseline is \(\sum_{t\in F^\times}c_{ij,t}(\psi(tr)-1)=0\) for all \(r\in F\). Distinct additive characters of \(F\) are a basis of functions on \(F\), forcing each \(c_{ij,t}=0\), and then the constant coefficient vanishes. Hence the Gram matrix is positive definite. Since every Gram entry is strictly positive, Perron–Frobenius makes the unique largest eigenvalue the positive eigenvalue \(L_+\) of the constant-coupled block.

**Exact lower-bound transition.** Direct subtraction gives \(\lambda_{\rm f}-\lambda_{\rm c}=q^{m-2}(q-1)^2/N>0\) and \(\lambda_{\rm s}-\lambda_{\rm f}=q^{m-2}(q-1)^2(m-3)/N>0\). Thus the only candidates for the minimum are \(L_-\) and \(\lambda_{\rm c}\). Put \(z=q^{m-2}\) and \(M=4(q^2-q+1)\). Exact expansion gives
\[
\det(K-\lambda_{\rm c}I)
 =\frac{z(m-1)(q-1)^2}{2(q^m+1)^2}\bigl[m(q-2)+4+z(M-m)\bigr].
\]
We have \(L_-<1<L_+\) and \(0<\lambda_{\rm c}<1\); therefore the sign of this determinant is positive exactly when \(\lambda_{\rm c}<L_-\). For \(m\le M\), the bracket is positive. For \(m=M+1\) it is negative because \(q^{M-1}>(M+1)(q-2)+4\) for every odd \(q\ge3\). It stays negative as \(m\) grows: the exponentially increasing term \(q^{m-2}(m-M)\) dominates the linearly growing \(m(q-2)+4\), with domination preserved under the step \(m\mapsto m+1\). This establishes both strict regimes and the claimed exact crossover.

**Equality spaces and asymptotics.** Frequency-difference, star, and cycle-type edge spaces are equality spaces for their respective eigenvalues as above. The remaining two coefficient eigenspaces are spanned by \(h\delta_0+(L_\pm-1)(E(q-1))^{-1/2}\mathbf1\). In particular, the upper-bound equality space is always the \(L_+\) line, while the lower-bound equality space is the cycle-type space below the transition and the \(L_-\) line above it. Finally, for fixed \(q\), \(u=1/q+O(q^{-m})\), \(v=1/q^2+O(q^{-m})\), so \(B\sim(q-1)m^2/(2q^2)\) and \(\det K\sim2(q-1)^2m/q^2\). Dividing by \(L_+\sim B\) gives \(L_-\sim4(q-1)/m\), and the squared condition-number asymptotic follows.

## Verification
The accompanying standalone `verify_veronese.py` independently builds the Gram matrices from finite-field character sums, rather than injecting the derived Gram entries. It tests \((q,m)=(3,4),(3,5),(5,4),(7,4),(9,4)\), where the \(q=9\) field is implemented through an irreducible quadratic polynomial over \(\mathbb F_3\). It compares every eigenvalue (with multiplicity), tests the frequency-difference, star, and cycle eigenspaces, and symbolically verifies the critical determinant factorization and integer threshold for additional odd \(q\). The direct finite tests support but do not replace the proof for all odd prime powers.

## Relationship to prior work
Eldar and Bölcskei (2001 preprint, 2003 journal publication) develop geometrically uniform and compound geometrically uniform finite frames, with Gram symmetry and general Fourier diagonalization. This supplies a frame-theoretic foundation but neither concerns the rank-one symmetric Veronese cone nor yields the specific five-piece spectrum and sharp dimension transition. Iosevich and Koh (2008) investigate finite-field restriction/extension on nondegenerate quadratic level sets, and explain the role of quadratic Gauss sums. Their surfaces and endpoint extension bounds differ from the present singular rank-one quadratic image and its explicitly selected off-diagonal coordinate characters. Standard Johnson graph incidence diagonalization is established linear algebra; its combination with the particular bilinear character averages here yields the complete rank-one-cone spectrum and the sharp crossing of two different lowest spectral modes. There is a residual historical-priority risk from unlocated variants of association-scheme or finite harmonic-frame formulas.

## Limitations
The claim is restricted to odd characteristic, the full set of nonzero frequencies on *all* off-diagonal entries, and dimension \(m\ge4\). No claims are made for diagonal coordinate characters, sparse edge subsets, general symmetric matrices, or noise models beyond Gram/Riesz conditioning. The exact crossover is an integer assertion and does not imply an analogous transition for every other Fourier subfamily. An equivalent formulation elsewhere in the literature cannot be ruled out from these comparisons.

## References
1. Y. C. Eldar and H. Bölcskei, *Geometrically Uniform Frames*, arXiv:math/0108096v1 (first posted 2001-08-13); IEEE Trans. Inform. Theory **49** (2003), 993–1006, DOI: 10.1109/TIT.2003.809602.
2. A. Iosevich and D. Koh, *Extension theorems for the Fourier transform associated with non-degenerate quadratic surfaces in vector spaces over finite fields*, arXiv:0804.4505v1 (posted 2008-04-28).
3. M. Thill, V. Muthukumar and B. Hassibi, *Frames from generalized group Fourier transforms and \(\mathrm{SL}_2(\mathbb F_q)\)*, ICASSP 2014, DOI: 10.1109/ICASSP.2014.6854538 (contextual comparison only; available metadata/abstract, not relied upon as a full-text exclusion).
