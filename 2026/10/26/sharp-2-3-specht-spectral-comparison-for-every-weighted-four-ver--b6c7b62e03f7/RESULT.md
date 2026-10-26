# Sharp \(2/3\) Specht spectral comparison for every weighted four-vertex graph

## Finding

Let \(G\) be any undirected graph on four labeled vertices with arbitrary nonnegative symmetric edge rates, including zero rates. For a nontrivial partition \(\nu\vdash4\), let \(\lambda_\nu(G)\) be the smallest eigenvalue of the interchange generator Laplacian on the irreducible real Specht module \(V_\nu\). If two nontrivial partitions \(\sigma,\tau\vdash4\) satisfy \(\sigma\unrhd\tau\) in dominance order, then

\[
\lambda_\tau(G)\ge\frac23\lambda_\sigma(G).
\]

The constant \(2/3\) is best possible uniformly over weighted graphs and comparable nontrivial pairs: for the unit-weight star on four vertices, \(\lambda_{(2,1,1)}=2\) and \(\lambda_{(2,2)}=3\). More specifically,

\[
\inf_{G:\lambda_{(2,2)}(G)>0}\frac{\lambda_{(2,1,1)}(G)}{\lambda_{(2,2)}(G)}=\frac23.
\]

The continuous six-parameter family of **all** weighted four-vertex graphs is included, not just unweighted or quasi-complete graphs.

## Assumptions and scope

Label vertices \(1,2,3,4\), set \(w_{ij}=w_{ji}\ge0\) for \(i<j\), and write
\[
L(G,\nu)=\sum_{i<j}w_{ij}\bigl(I-\rho_\nu((ij))\bigr),\qquad W=\sum_{i<j}w_{ij}.
\]
The representations are orthogonal, and the smallest eigenvalue includes zero eigenvalues of disconnected cases. The trivial partition \((4)\) is excluded from both partitions in the comparison. Define opposite-edge bundles
\[
a=w_{12}+w_{34},\quad b=w_{13}+w_{24},\quad c=w_{14}+w_{23},\quad W=a+b+c,
\]
and the nonnegative discriminant
\[
\Delta=a^2+b^2+c^2-ab-bc-ca.
\]

## Proof

**1. The \((2,2)\) spectral gap.** The permutation representation of the symmetric group on its three perfect matchings of four points decomposes as the trivial representation plus \(V_{(2,2)}\). A transposition in the opposite-edge bundle \(a\) exchanges the two matchings other than \(12|34\), and similarly for the bundles \(b,c\). The resulting matching-state Laplacian is
\[
Q=\begin{pmatrix}
b+c&-c&-b\\-c&a+c&-a\\-b&-a&a+b
\end{pmatrix}.
\]
Its characteristic polynomial is
\[
\det(tI-Q)=t\bigl(t^2-2Wt+3(ab+bc+ca)\bigr).
\]
Because \(W^2-3(ab+bc+ca)=\Delta\), its two eigenvalues on \(V_{(2,2)}\) are \(W\pm\sqrt\Delta\). Therefore
\[
\lambda_{(2,2)}(G)=W-\sqrt\Delta.
\]

**2. The conjugate hook.** The representation \(V_{(2,1,1)}\) is the tensor product of the sign character with \(V_{(3,1)}\). Since every transposition has sign \(-1\), its Laplacian is \(2WI-L(G,(3,1))\), whence
\[
\lambda_{(2,1,1)}(G)=2W-\Lambda,
\]
where \(\Lambda\) denotes the **largest** eigenvalue of the ordinary four-vertex graph Laplacian restricted to the three-dimensional sum-zero space. In the orthonormal Hadamard basis
\[
\tfrac12(1,1,-1,-1),\quad\tfrac12(1,-1,1,-1),\quad\tfrac12(1,-1,-1,1),
\]
that restricted Laplacian has matrix
\[
M=\begin{pmatrix}
W-a&w_{14}-w_{23}&w_{13}-w_{24}\\
w_{14}-w_{23}&W-b&w_{12}-w_{34}\\
w_{13}-w_{24}&w_{12}-w_{34}&W-c
\end{pmatrix}.
\]
In particular, \(\operatorname{tr}M=2W\), and, with \(T=a^2+b^2+c^2\),
\[
\operatorname{tr}(M^2)\le(W-a)^2+(W-b)^2+(W-c)^2+2T=W^2+3T.
\]
The inequality follows because each off-diagonal entry is the difference of two nonnegative rates with sum equal to the corresponding bundle.

**3. A sharp trace bound.** For any symmetric \(3\times3\) matrix \(H\) with largest eigenvalue \(\Lambda_H\), the other two eigenvalue deviations from the mean sum to the negative of the largest deviation. Cauchy--Schwarz therefore gives
\[
\Lambda_H\le\frac{\operatorname{tr}H}{3}+
\sqrt{\frac23\left(\operatorname{tr}(H^2)-\frac{(\operatorname{tr}H)^2}{3}\right)}.
\]
Apply this with \(H=M\). Since \(3T=W^2+2\Delta\),
\[
\Lambda\le\frac{2W}{3}+\frac23\sqrt{W^2+3\Delta}.
\]
The identity \(2\Delta=(a-b)^2+(b-c)^2+(c-a)^2\) shows \(\Delta\ge0\). Nonnegativity of \(a,b,c\) also gives \(W^2-\Delta=3(ab+bc+ca)\ge0\), and hence
\[
\sqrt{W^2+3\Delta}\le W+\sqrt\Delta
\]
(the squared inequality reduces to \(\sqrt\Delta\le W\)). Thus
\[
\Lambda\le\frac{4W+2\sqrt\Delta}{3},\qquad
\lambda_{(2,1,1)}\ge\frac23(W-\sqrt\Delta)=\frac23\lambda_{(2,2)}.
\]
No division by a spectral gap was used, so this remains valid for disconnected graphs.

**4. All dominance pairs.** The nontrivial partitions of four form the dominance chain
\[
(3,1)\unrhd(2,2)\unrhd(2,1,1)\unrhd(1,1,1,1).
\]
The Aldous spectral-gap theorem gives \(\lambda_\nu\ge\lambda_{(3,1)}\) for each nontrivial \(\nu\), covering all comparisons whose larger partition is \((3,1)\). The sign representation has eigenvalue \(\lambda_{(1^4)}=2W\), which is at least the smallest eigenvalue of every other Specht Laplacian because every term \(w_{ij}(I-\rho_\nu((ij)))\) lies between \(0\) and \(2w_{ij}I\). Comparisons with the sign partition below therefore hold even with constant one. The only remaining distinct pair is \((2,2)\unrhd(2,1,1)\), covered by step 3. Comparisons of a partition with itself are automatic.

**5. Sharpness.** For the unit star with rates \(w_{12}=w_{13}=w_{14}=1\) and all others zero, \(a=b=c=1\), \(W=3\) and \(\Delta=0\). The standard Laplacian has eigenvalues \(0,1,1,4\), so \(\lambda_{(2,1,1)}=6-4=2\), while \(\lambda_{(2,2)}=3\). Their ratio is precisely \(2/3\). \(\square\)

## Verification

Run `python verify.py` from a directory with Python 3, SymPy and NumPy installed. This standalone verifier symbolically checks the matching-state polynomial, the Hadamard restriction, the trace inequalities' exact algebraic identities, and the star equality; it also checks 2053 seeded nonnegative edge-rate vectors numerically. The analytical trace argument, not the finite tests, proves the assertion for all real nonnegative rates.

## Relationship to prior work

Gil Alon, *Spectral comparison on Specht modules and mixing of the interchange process*, arXiv:2610.22151v1 (15 October 2026), Conjecture 1.5, proposes the same constant \(2/3\) for **all** graph sizes and all comparable partitions. His Theorem 4.4 proves the constant for quasi-complete graphs, and Theorem 4.5 already provides the star equality examples, including the four-vertex example; those parts are **not** new here. That work reports finite unweighted testing and weighted sampling, not a theorem for every weighted four-vertex graph. The contribution here is the universal **six-rate, four-vertex lower bound**, giving the first nontrivial complete graph-size case with a sharp uniform constant.

Alon and Kozma, *Ordering the Representations of \(S_n\) Using the Interchange Process*, Canadian Mathematical Bulletin 56 (2013), 13–30, analyzes the **constant-one** Aldous order and explicitly exhibits the failure of constant one between \((2,2)\) and \((2,1,1)\) on four-vertex stars (see Section 1 and Corollary 3.2). Its published results do not state the universal sharp \(2/3\) lower comparison for this pair. The Aldous theorem itself is attributed to Caputo, Liggett, and Richthammer (2010), and is used here only for the remaining pairs.

## Limitations

This establishes the conjectured comparison only for four vertices, not arbitrary order. It is an exact deterministic spectral statement for weighted interchange generators, not a quantitative mixing-time estimate. The trace estimate does not classify all equality graphs, beyond the demonstrated star. The claimed novelty is subject to unindexed or independently established spectral inequalities not found in the checked literature; independent validation has not been performed.

## References

1. G. Alon, *Spectral comparison on Specht modules and mixing of the interchange process*, arXiv:2610.22151v1 (first public 2026-10-15), https://arxiv.org/html/2610.22151v1 .
2. G. Alon and G. Kozma, *Ordering the Representations of \(S_n\) Using the Interchange Process*, Canadian Mathematical Bulletin 56 (2013), 13–30, DOI 10.4153/CMB-2011-147-2, https://arxiv.org/abs/1003.1710 .
3. P. Caputo, T. Liggett and T. Richthammer, *Proof of Aldous' Spectral Gap Conjecture*, Journal of the American Mathematical Society 23 (2010), 831–851; cited for the ordinary interchange-process gap theorem.
