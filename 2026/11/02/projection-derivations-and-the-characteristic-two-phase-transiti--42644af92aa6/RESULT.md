# Projection derivations and the characteristic-two phase transition in graded filiform Leibniz algebras

## Finding

For every field \(k\) and \(n\ge4\), let \(L_n(k)\) be the \(n\)-dimensional Leibniz algebra from the next section. Its **projection derivations** are the ordinary derivations \(D:L_n\to L_n\) satisfying \(D^2=D\). They admit the following complete, field-uniform classification.

Put \(s=\lfloor(n-1)/2\rfloor\), \(t=\lceil(n-1)/2\rceil\). The reduced algebraic variety \(\mathcal P_n=\{D\in\operatorname{Der}(L_n):D^2=D\}_{\mathrm{red}}\) is the disjoint union of the following affine spaces, defined over \(k\):

\[
\mathcal P_n\cong
\begin{cases}
\mathbb A^0\sqcup\mathbb A^1,&\operatorname{char}k\ne2,\\
\mathbb A^0\sqcup\mathbb A^1\sqcup\mathbb A^s\sqcup\mathbb A^{s+1},&\operatorname{char}k=2.
\end{cases}
\]

For \(k=\mathbb F_q\), define the exact **rank-enumerator** \(P_{n,q}(T)=\sum_{D^2=D}T^{\operatorname{rank}D}\), summing over all linear derivation maps, without quotienting by automorphisms. Then

\[
P_{n,q}(T)=
\begin{cases}
1+qT^{n-1},&q\text{ odd},\\
1+qT^{n-1}+q^{s+1}T^{s+1}+q^sT^{t+1},&q\text{ even}.
\end{cases}
\]

In particular, the total count is \(q+1\) when \(q\) is odd and \((q+1)(q^s+1)\) when \(q\) is even. Coincident powers of \(T\) are combined in this polynomial. This is a phase transition of both rank distributions and reduced component dimensions. For example, when \((n,q)=(4,2)\), there are precisely nine projection derivations, with ranks \(0,2,3\) occurring \(1,4,4\) times respectively.

## Assumptions and scope

Take the **right Leibniz** algebra on \(e_1,\ldots,e_n\) whose sole nonzero ordered basis brackets are

\[
[e_i,e_1]=e_{i+1}\quad(2\le i\le n-1).
\]

All other brackets are zero. The right Leibniz identity follows because all right multiplications commute, and the algebra is non-Lie and filiform: the descending brackets have \(\dim L^j=n-j\) for \(2\le j\le n\). The algebra is the familiar naturally graded model \(NGF_1\) after the change \(e_1^{\prime}=e_1-e_2\) in its presentation \([e_1,e_1]=[e_2,e_1]=e_3\); this works also in characteristic two. The derivation condition is \(D([x,y])=[D(x),y]+[x,D(y)]\) for every \(x,y\). We count the actual operators, not their conjugacy classes. The geometric assertion is about the **reduced** affine variety, not about a potentially nonreduced defining scheme.

## Proof

**1. Every derivation.** Set \(W=\langle e_2,\ldots,e_n\rangle\), which is the right annihilator \(\{y:[L,y]=0\}\). Every derivation preserves \(W\). On \(W\), let \(N e_i=e_{i+1}\) for \(i<n\), with \(N e_n=0\), and let \(H e_i=(i-2)e_i\). Because \([e_1,e_1]=0\), writing the first column of \(D\) gives \(D(e_1)=a e_1+b e_n\). Set \(M=D|_W\). Applying the derivation identity to \([w,e_1]=Nw\) yields

\[
MN-NM=aN.
\]

The identity \(HN-NH=N\) holds over every field, so \(M-aH\) commutes with \(N\). Since \(N\) is one full Jordan chain with cyclic vector \(e_2\), every commuting endomorphism is uniquely a polynomial in \(N\), of degree at most \(n-2\). Consequently

\[
D(e_1)=a e_1+b e_n,\qquad
D|_W=aH+f(N),\quad f(N)=\sum_{j=0}^{n-2}c_jN^j,
\]

with arbitrary \(n+1\) parameters. Conversely, these formulae satisfy the derivation rule on all ordered basis pairs, establishing existence and uniqueness.

**2. Restricting a projection.** If \(D^2=D\), comparison on \(e_1\) gives \(a^2=a\), hence \(a=0\) or \(a=1\). The diagonal of \(M\) is

\[
c_0,\;c_0+a,\;c_0+2a,\ldots,c_0+(n-2)a.
\]

Every diagonal entry of the triangular idempotent \(M\) is itself idempotent in \(k\), hence either zero or one. If \(a=0\), the polynomial \(f(N)\) is idempotent inside the local algebra \(k[N]/(N^{n-1})\). Its only idempotents are zero and one: if an idempotent is nilpotent it is zero; if its residue is one, its complement is nilpotent and therefore zero. Thus \(f(N)=c_0I\), \(c_0\in\{0,1\}\). The first-column equation is \(b(c_0-1)=0\). The \(a=c_0=0\) branch consists of \(D=0\), one point. The \(a=0,c_0=1\) branch has arbitrary \(b\) and is \(\mathbb A^1\). Its operators all have rank \(n-1\).

If \(\operatorname{char}k\ne2\), the alternative \(a=1\) is impossible for \(n\ge4\): the three consecutive diagonal elements \(c_0,c_0+1,c_0+2\) cannot all lie in \(\{0,1\}\) over any field of characteristic other than two. This completes the odd-characteristic classification.

**3. The new characteristic-two branches.** Suppose \(\operatorname{char}k=2\) and \(a=1\). Then \(H^2=H\), and for \(j\ge1\), \(HN^j+N^jH=jN^j\). Frobenius squaring gives \((\sum_jc_jN^j)^2=\sum_jc_j^2N^{2j}\). Comparing each coefficient in \(M^2=M\) gives

\[
c_0\in\{0,1\},\qquad c_{2j}=c_j^2\ \text{for }2j\le n-2,
\]

while all coefficients \(c_j\) with odd \(j\in[1,n-2]\) are freely chosen. Their number is \(s=\lfloor(n-1)/2\rfloor\). The equation from \(D^2(e_1)=D(e_1)\) becomes

\[
b\bigl(c_0+(n-2\bmod2)\bigr)=0.
\]

Exactly one choice of \(c_0\) forces \(b=0\) (giving \(\mathbb A^s\)); the other leaves \(b\) freely variable (giving \(\mathbb A^{s+1}\)). The equations \(c_{2j}=c_j^2\) are polynomial graphs over the free odd coordinates, so these are reduced affine spaces over arbitrary characteristic-two fields. The \(a,c_0\) roots are distinct, hence the four branches are disjoint as geometric components of the reduced locus.

**4. Ranks and finite-field counts.** Each idempotent endomorphism is diagonalizable, so the rank is the multiplicity of eigenvalue one, which can be counted on the displayed triangular diagonal. On the \(a=1\) branch where \(b\) is free, the rank is \(s+1\), and there are \(q^{s+1}\) maps over \(\mathbb F_q\). On the branch \(b=0\), the rank is \(t+1\), and there are \(q^s\) maps. Adding the point and the \(q\) rank-\(n-1\) maps gives precisely the rank-enumerator and total formula. All arguments are characteristic-free except for the explicitly isolated distinction between characteristic two and other characteristics.

## Verification

The accompanying standalone script `VERIFY/check.py` reconstructs the original ordered basis brackets and directly checks the derivation identity and the equation \(D^2=D\) by finite-field matrix multiplication. It exhausts all derivation parameters for eleven combinations of \(n\) and \(q\), checks the full rank histograms, and independently exhausts all \(2^{16}\) linear maps when \((n,q)=(4,2)\), confirming that the listed parameterization contains every derivation. The tests include the true extension field \(\mathbb F_4\), implemented by its degree-two polynomial arithmetic. All eleven cases passed, with output in `VERIFY/output.txt`. The finite tests corroborate but do not replace the all-field proof above.

## Relationship to prior work

Rakhimov and Al-Hossain, *On derivations of some classes of Leibniz algebras*, first publicly posted May 12, 2012 (arXiv:1205.2779), classify the derivation algebra of the complex naturally graded model \(NGF_1\), including the derivation dimension \(n+1\). Their structure theorem is a direct antecedent; the present derivation parameterization is not claimed as independently new. Their Theorem 3 and its proof do not impose \(D^2=D\), count projection operators, or analyze characteristic two. Calderón, Camacho, Kaygorodov and Omirov (arXiv:1708.01753) classify abelian-group gradings of related filiform Leibniz algebras over the complex field; that characteristic-zero classification does not imply the modular, actual-operator counts above. In characteristic two, projection derivations correspond to \(\mathbb Z/2\mathbb Z\)-graded decompositions of this Leibniz algebra, giving an additional structural interpretation. A later 2014 study of derivations of naturally graded filiform Leibniz algebras has been checked at abstract level only; a stronger unlocated modular grading or projection classification remains a publication-priority risk.

## Limitations

The theorem is for the explicitly stated standard naturally graded right-Leibniz family and linear derivations, not all filiform Leibniz algebras. It classifies the **reduced** solution variety and absolute derivation maps, not nilpotent scheme structure, automorphism-conjugacy types, or all gradings by arbitrary groups. Computational checks cover finite small parameters; unrestricted values are proved symbolically. Historical priority beyond the inspected published sources remains provisional, and no independent mathematical audit has been performed.

## References

1. I. S. Rakhimov and N. Al-Hossain, *On derivations of some classes of Leibniz algebras*, first posted 2012-05-12, arXiv:1205.2779, https://arxiv.org/abs/1205.2779.
2. A. Calderón, L. Camacho, I. Kaygorodov and B. Omirov, *Abelian groups gradings on null-filiform and one-parametric filiform Leibniz algebras*, arXiv:1708.01753, https://arxiv.org/abs/1708.01753.
3. A. Al-Hossain and K. Al-Hossain, *Derivations of Some Filiform Leibniz Algebras*, *Pure and Applied Mathematics Journal* **3** (2014), 121–125, https://doi.org/10.11648/j.pamj.20140306.12.
