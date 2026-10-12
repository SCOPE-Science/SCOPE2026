# Three-representation thresholds for four consecutive odd coin denominations

## Finding
For each **odd integer** \(a\ge9\), let \(A_a=\{a,a+2,a+4,a+6\}\), and let \(r_a(N)\) be the number of vectors \((x_0,x_1,x_2,x_3)\in\mathbb Z_{\ge0}^4\) with \(N=\sum_{i=0}^{3}(a+2i)x_i\). The largest nonnegative integer with **at most two** representations has the exact value
\[
 g_2(A_a)=
 \begin{cases}
 a\big(\lfloor a/3\rfloor+3\big)+2,&a\equiv1\pmod3,\\
 a\big(\lfloor a/3\rfloor+2\big)+4,&a\equiv0\pmod3,\\
 a\big(\lfloor a/3\rfloor+3\big)+4,&a\equiv2\pmod3.
 \end{cases}
\]
In particular, every integer strictly larger than \(g_2(A_a)\) has at least three distinct multiplicity-vector representations. The maximizing residue in the three-representation Apéry set is unique: \(2\pmod a\) when \(a\equiv1\pmod3\), and \(4\pmod a\) otherwise.

More precisely, write \(C(s)=\lceil s/3\rceil\), \(U=C(a+2)\), \(V=C(a+3)\). For each \(0\le j<a\), let \(M_j\) be the smallest nonnegative integer congruent to \(2j\pmod a\) with \(r_a(M_j)\ge3\). All these thresholds are explicitly
\[
 M_j=\begin{cases}
 a(2+U),&j=0,\\
 a(2+V)+2,&j=1,\\
 a(2+U)+4,&j=2,\\
 a\max\{3,C(j+3)\}+2j,&3\le j<a.
 \end{cases}
\]
Thus \(g_2(A_a)=\max_j M_j-a\).

## Assumptions and scope
The four denominations are positive, distinct, and have greatest common divisor one since \(a\) is odd. Distinct representations mean distinct nonnegative coefficient vectors, not different orderings of coins. Every quantifier is unrestricted beyond odd \(a\ge9\) and integer \(N\ge0\). The subscript \(2\) denotes at most two representations; some older literature instead denotes this invariant by \(F_3\), meaning failure of at least three representations.

## Proof
**1. A bounded partition lemma.** For \(t,J\in\mathbb Z_{\ge0}\), let \(Q(t,J)\) count vectors \((x_0,x_1,x_2,x_3)\in\mathbb Z_{\ge0}^4\) with \(\sum_i x_i=t\) and \(\sum_i i x_i=J\). Equivalently, \(Q(t,J)\) counts multisets of \(t\) digits in \(\{0,1,2,3\}\) having sum \(J\). It vanishes unless \(0\le J\le3t\). For \(t\ge2\),
\[
 Q(t,J)\ge2\quad\Longleftrightarrow\quad 2\le J\le3t-2.
\]
For \(t\ge3\),
\[
 Q(t,J)\ge3\quad\Longleftrightarrow\quad3\le J\le3t-3.
\]
For the first equivalence, direct calculation at \(t=2\) gives counts \((1,1,2,2,2,1,1)\) for \(J=0,\ldots,6\). If it holds at \(t\), padding a multiset by a zero preserves its distinct representations for \(2\le J\le3t-2\), while padding by a three handles \(3t-1\le J\le3t+1\), establishing the case \(t+1\); outside the stated interval there is at most one multiset by symmetry of digit complementation. For the second equivalence, the direct counts for \(t=3\) are \((1,1,2,3,3,3,3,2,1,1)\). Padding by zero handles \(3\le J\le3t-3\), and padding by three handles \(3t-2\le J\le3t\) at stage \(t+1\). Outside the interval counts are at most two by the complement symmetry and the explicit low-end values \(Q(t,0)=Q(t,1)=1\), \(Q(t,2)=2\) for \(t\ge2\). Also \(Q(t,J)\ge1\) exactly for \(0\le J\le3t\), by using \(0,1,2,3\) digits.

**2. Split each residue into disjoint coin-count layers.** Fix \(0\le j<a\). Any \(N\equiv2j\pmod a\) has a unique integer \(T\) with \(N=aT+2j\). In any representation, set \(t=\sum_i x_i\), \(J=\sum_i i x_i\), so \(N=at+2J\). Because \(a\) is odd, \(J=j+ka\) for a unique integer \(k\ge0\), and then \(t=T-2k\). Consequently
\[
 r_a(aT+2j)=\sum_{k\ge0}Q(T-2k,j+ka),
\]
where arguments outside the nonnegative domain contribute zero. Different summands correspond to different coin counts and do not duplicate representations. In layer \(k\ge1\), any representation requires
\[
 T\ge2k+\left\lceil\frac{j+ka}{3}\right\rceil.
\]
The right-hand side grows strictly with \(k\).

**3. The first three residues.** For \(j=0\), the layer \(k=0\) contributes exactly one representation for every \(T\ge0\). Thus at least three occur exactly when some layer \(k\ge1\) contributes at least two, or at least two new layers appear. The earliest \(k=1\) layer containing two representations has \(T=2+C(a+2)\) by the first lemma; all \(k\ge2\) are unavailable before that time. Therefore \(M_0=a(2+U)\). For \(j=1\), the \(k=0\) layer likewise has at most one representation, and the earliest layer \(k=1\) with at least two occurs at \(T=2+C(a+3)\); again layers \(k\ge2\) appear later. Therefore \(M_1=a(2+V)+2\). For \(j=2\), the layer \(k=0\) has exactly two representations whenever \(T\ge2\), while the first \(k=1\) representation occurs at \(T=2+C(a+2)\). Thus \(M_2=a(2+U)+4\).

**4. Every remaining residue.** For \(3\le j<a\), the \(k=0\) layer first reaches three representations at
\[
 T_j=\max\{3,C(j+3)\}.
\]
A \(k\ge1\) layer cannot appear this early, since its earliest possible \(T\) is at least \(2+C(j+a)>T_j\) for \(a\ge9\). Hence \(M_j=aT_j+2j\), as claimed. The description is genuinely exact: in every residue, values below the displayed threshold have fewer than three representations, and the threshold has at least three.

**5. Locate the unique maximum.** Since \(U=C(a+2)\ge3\), for \(3\le j<a\) we have \(T_j\le U\), whence \(M_j\le aU+2(a-1)<M_2\). Also \(M_0=M_2-4\). Thus the largest threshold is either \(M_1\) or \(M_2\). If \(a\equiv1\pmod3\), then \(V=U+1\), so \(M_1-M_2=a-2>0\); otherwise \(V=U\) and \(M_2-M_1=2>0\). This also proves uniqueness of the maximizing residue.

**6. Transfer to the global bound.** Adding one coin of denomination \(a\) injects the representations of \(N\) into those of \(N+a\); thus \(r_a(N+a)\ge r_a(N)\). Each residue has its first three-representation integer \(M_j\), and every later integer in that residue is representable at least three ways. Exactly \(M_j-a\) fails the threshold in that residue, so \(g_2(A_a)=\max_j M_j-a\). Substituting \(U,V\) gives the displayed three-case formula.

## Verification
The separately supplied exact-integer program `verify.py` constructs denumerants by a four-coin dynamic program, capped at three for efficient exact comparison. It checks every odd \(a\) from \(9\) through \(201\), the proposed first-three-representation thresholds in every residue, absence of earlier qualifying numbers, the unique maximizing residue, and a finite interval above the global bound. Results are recorded in `verification_output.txt`. These finite tests corroborate but do not establish the unrestricted theorem, which follows from the preceding proof.

## Relationship to prior work
Mohammed's 2017 thesis [1, Chapter 6, Theorem 6.2.1] proves the **two-representation threshold** \(F_2(a,a+d,a+2d,a+3d)=a\lfloor a/3\rfloor+d(a+1)\), where \(F_2\) excludes numbers having fewer than two representations. This is a different invariant from the three-representation threshold proved here; neither its formula nor the older shortest-path statements imply the stated complete next Apéry layer. Komatsu and Ying [2] explicitly describe the difficulty of positive-parameter Frobenius formulas for four or more members of an arithmetic progression and establish formulas for triples. The 2026 work of Komatsu, Hyun and Song [3] proves formulas for consecutive odd *blocks whose number of denominations grows with the first denomination*, specifically the blocks \(\{2h+1,2h+3,\ldots,4h+1\}\) and \(\{2h+1,2h+3,\ldots,4h+3\}\). Neither is the fixed four-element family for any odd \(a\ge9\). Its isolated short-block special cases motivate the exclusion of \(a=5,7\) from the claim here. The result is a next-representation-layer structural classification, not a restatement of the earlier two-representation theorem.

## Limitations
No formula is asserted for non-odd \(a\), for arbitrary common difference, or for multiplicity thresholds above three representations. Prior bibliographic comparisons are finite, not a proof of absence from all worldwide literature; an unindexed equivalent is possible. The separate computer checks cover only \(9\le a\le201\) and are not a proof for larger parameters.

## References
[1] D. H. Mohammed, *Generalised Frobenius numbers: geometry of upper bounds, Frobenius graphs and exact formulas for arithmetic sequences*, Cardiff University PhD thesis, 2017, Chapter 6. First compliant repository deposit 2017-02-21. https://orca.cardiff.ac.uk/id/eprint/98161/1/Final%20Thesis.pdf

[2] T. Komatsu and H. Ying, *The p-Numerical Semigroup of the Triple of Arithmetic Progressions*, arXiv:2206.13052v1 (posted 2022-06-27); *Symmetry* **15** (2023), 1328. https://doi.org/10.3390/sym15071328

[3] T. Komatsu, S. Hyun and K. Song, *p-numerical semigroup of the sequence of consecutive odd integers*, arXiv:2608.14053v1 (posted 2026-08-14), Theorems 1.2 and 1.3 and Remark 1.4. https://arxiv.org/abs/2608.14053
