# Square-zero Smith strata are universal across length-two chain rings

## Finding

Let \(R\) be a finite **commutative chain ring of length exactly two**: its unique maximal ideal is \((\pi)\ne0\), with \(\pi^2=0\); its residue field is \(k=R/(\pi)\cong\mathbb F_q\). The following formula applies to every \(n\ge1\), without a hypothesis on the characteristic of \(R\).

For a square-zero matrix \(X\in M_n(R)\), write \(r\) for the number of unit entries, and \(t\) for the number of nonzero radical entries, in its Smith normal form. Define \(N_{n,r,t}(R)\) as the number of matrices with this exact pair of invariant counts. Then with \(s=n-2r\),

\[
N_{n,r,t}(R)=
\begin{cases}
\displaystyle
\genfrac{[}{]}{0pt}{}{n}{r}_q
\genfrac{[}{]}{0pt}{}{n-r}{r}_q
\lvert\operatorname{GL}_r(k)\rvert\,
q^{2r(n-r)}
\genfrac{[}{]}{0pt}{}{s}{t}_q^{\!2}
\lvert\operatorname{GL}_t(k)\rvert,
&0\le r\le\lfloor n/2\rfloor,\ 0\le t\le s,\\
0,&\text{otherwise}.
\end{cases}
\]

Here the Gaussian coefficient \(\genfrac{[}{]}{0pt}{}{a}{b}_q\) counts \(b\)-dimensional subspaces of \(k^a\), and \(\lvert\operatorname{GL}_j(k)\rvert=\prod_{i=0}^{j-1}(q^j-q^i)\), with the empty product equal to one. **Every formally feasible pair occurs.** The formula is a full Smith-stratified enumeration, not only a count by reduction rank or a formula for unrestricted matrices.

Moreover, among all square-zero matrices with fixed reduction rank \(r\), the conditional distribution of \(t\) is the ordinary rank distribution of a uniformly chosen \(s\times s\) matrix over \(k\). It follows that the distribution for \(R=\mathbb F_q[\varepsilon]/(\varepsilon^2)\) agrees exactly with that of every mixed-characteristic length-two chain ring having the same residue-field size; in particular it agrees for \(\mathbb F_2[\varepsilon]/(\varepsilon^2)\) and \(\mathbb Z/4\mathbb Z\).

For \(n=2,q=2\), the four nonzero strata are \((r,t)=(0,0),(0,1),(0,2),(1,0)\) with respective multiplicities \(1,9,6,12\), totaling \(28\). For \(n=3,q=2\), the six multiplicities in lexicographic order of \((r,t)\) are \(1,49,294,168,336,336\), totaling \(1184\).

## Assumptions and scope

The ring is commutative, finite, local, with ideals exactly \(0\subset(\pi)\subset R\). Consequently \(|R|=q^2\), \(\pi R\cong k\) as additive groups and one-dimensional \(k\)-spaces, and every matrix admits Smith diagonal entries associated to \(1\), \(\pi\), or \(0\). Left-right equivalence used to define a Smith normal form is not similarity; the constraint \(X^2=0\) remains on the original matrix, not on its Smith diagonal. The theorem classifies **counts** by Smith invariants; it does not claim a similarity-orbit classification.

For an arbitrary \(r\), denote by \(A=\overline X\in M_n(k)\) the reduction modulo \(\pi\). Its rank is exactly the number \(r\) of unit Smith entries. Set \(s=n-2r\). The pair \((r,t)\) is meaningful even in characteristic two and when \(R\) contains no coefficient-field copy of \(k\).

## Proof

**1. Reduction and feasibility.** Since \(X^2=0\), its reduction satisfies \(A^2=0\), and therefore \(\operatorname{im}A\subseteq\ker A\). Hence \(2r\le n\). Conversely every rank-\(r\) square-zero matrix over \(k\) has a basis \(U\oplus C\oplus W\), of respective dimensions \(r,s,r\), in which

\[
A\sim J=\begin{bmatrix}0&0&I_r\\0&0&0\\0&0&0\end{bmatrix}.
\]

There are exactly

\[
B_{n,r}(q)=\genfrac{[}{]}{0pt}{}{n}{r}_q\genfrac{[}{]}{0pt}{}{n-r}{r}_q\lvert\operatorname{GL}_r(k)\rvert
\]

such field matrices: choose the image \(U\) (first Gaussian factor), the kernel \(K\supset U\) of codimension \(r\) (second Gaussian factor), and an isomorphism \(k^n/K\to U\) (last factor). No similarity-orbit assumption beyond the elementary normal form is needed.

**2. Fiber computation without choosing a coefficient field.** Reduction induces a surjection \(\operatorname{GL}_n(R)\to\operatorname{GL}_n(k)\). Thus conjugation by an invertible lift carries the fiber over any rank-\(r\) matrix \(A\) bijectively to the fiber over \(J\). The displayed \(J\) has entries \(0,1\in R\) and satisfies \(J^2=0\) in \(R\) itself, even for mixed-characteristic \(R\). Every lift of \(J\) is uniquely

\[
X=J+\pi B,\qquad B\in M_n(k),
\]

where multiplication by \(\pi\) identifies \(k\) with \((\pi)\). The notation means entrywise multiplication of arbitrary representative lifts; the result is independent of the representatives because \(\pi^2=0\). We have

\[
X^2=\pi(JB+BJ),
\]

and since \(k\to(\pi)\), \(b\mapsto\pi b\), is an additive-group isomorphism, this vanishes exactly when \(JB+BJ=0\) over \(k\).

Write \(B=(B_{ab})\) in the three blocks \(U,C,W\). Direct block multiplication gives precisely

\[
B_{WU}=B_{WC}=B_{CU}=0,\qquad B_{WW}=-B_{UU}.
\]

The independent blocks are \(B_{UU}\), \(B_{UC}\), \(B_{UW}\), \(B_{CC}\), and \(B_{CW}\). Their total dimension is \(2r(n-r)+s^2\). In particular, \(B_{CC}\in M_s(k)\) is **completely unrestricted** and every choice has exactly \(q^{2r(n-r)}\) compatible choices of the other blocks.

**3. Identifying the radical Smith entries.** The \(U\)-row/\(W\)-column block of \(X\) is \(I_r+\pi B_{UW}\), a unit matrix. Use elementary row and column operations over \(R\) to clear this block and remove \(r\) unit pivots. The only potentially nonzero residual block is then \(\pi B_{CC}\): all others either vanish by the displayed linear equations or are products containing \(\pi^2\), hence zero. Therefore the remaining nonzero Smith diagonal entries are associates of \(\pi\), and their number is exactly \(\operatorname{rank}_k(B_{CC})\). In particular \(0\le t\le s\).

The number of \(s\times s\) matrices over \(k\) of rank exactly \(t\) is

\[
R_{s,t}(q)=\genfrac{[}{]}{0pt}{}{s}{t}_q^2\lvert\operatorname{GL}_t(k)\rvert.
\]

Indeed, choose its image and its kernel (two Gaussian factors) and then an isomorphism between its quotient domain and image (general linear factor). Multiplying \(B_{n,r}(q)\), the compatible-block fiber size \(q^{2r(n-r)}\), and \(R_{s,t}(q)\) proves the formula. Choosing any rank-\(t\) block \(B_{CC}\), all other free blocks zero, proves that every feasible stratum is attained.

**4. Conditional universality.** The number of all lifts with fixed \(r\) is \(B_{n,r}(q)q^{2r(n-r)+s^2}\), since \(\sum_tR_{s,t}(q)=q^{s^2}\). Division of the exact stratum formula by this value gives

\[
\Pr\bigl(t\mid r,X^2=0\bigr)=\frac{\genfrac{[}{]}{0pt}{}{s}{t}_q^2\lvert\operatorname{GL}_t(k)\rvert}{q^{s^2}}.
\]

All factors involve only \(n\) and \(q\); no ring-characteristic term occurs. This proves the claimed universality and completes the proof.

## Verification

Run `python3 verify.py` from an extracted copy of this package. The verifier enumerates every lift \(A+\varepsilon B\) over the dual-number rings for \((n,q)=(2,2),(3,2),(2,3),(2,4)\), checks square-zero products, independently recovers Smith multiplicities by the rank of the corresponding doubled field-linear map, and compares every stratum to the formula. It separately exhausts all matrices over \(\mathbb Z/4\mathbb Z\) and \(\mathbb Z/9\mathbb Z\) in dimension two, using image cardinalities to recover their Smith multiplicities without relying on the dual-number encoding. Formula normalization checks cover \(1\le n\le8\) and field sizes \(2,3,4,5,7,8,9\). All tested cases passed. The executable checks are finite tests, not substitutes for the proof for arbitrary \(n,q,R\).

## Relationship to prior work

Ekhad and Zeilberger [1], building on Kirillov's 1995 work, enumerate square-zero **upper-triangular matrices over a field**. Their imposed triangular pattern and field coefficient ring differ from the present full-matrix count with Smith strata over length-two chain rings. Danchev, García and Gómez Lozano [2] prove existence of potent-plus-square-zero decompositions of matrices over finite rings with square-zero radical; no count or Smith-stratified distribution follows from their stated existence theorem. Byrne, Horlemann, Khathuria and Weger [3] describe counts for **unrestricted** finite-chain-ring matrices by module type, but the nonlinear constraint \(X^2=0\) requires the additional fiber and rank calculation proved here. These distinctions concern the mathematical implications of the compared results, not merely their titles.

## Limitations

Only the equation \(X^2=0\) over **commutative chain rings of length exactly two** is classified here. The formula does not assert the same universality for rings with radical length three or more, non-chain rings, noncommutative rings, or nilpotency index larger than two. It gives no similarity-orbit counts. Historical literature on Hall-polynomial enumeration and nilpotent endomorphisms may contain equivalent statements under different terminology; an exhaustive bibliographic priority determination is not claimed. Verification over listed small rings cannot certify untested cases independently.

## References

[1] S. B. Ekhad and D. Zeilberger, *An Explicit Formula for the Number of Solutions of X²=0 in Triangular Matrices Over a Finite Field*, arXiv:math/9512224v1, publicly posted 1995-12-19. Full two-page preprint: https://arxiv.org/pdf/math/9512224 .

[2] P. Danchev, E. García and M. Gómez Lozano, *Decompositions of Matrices into Potent and Square-Zero Matrices*, arXiv:2102.10460v1 (2021), especially Theorem 2.6. https://arxiv.org/pdf/2102.10460 .

[3] E. Byrne, A.-L. Horlemann, K. Khathuria and V. Weger, *Density of Free Modules over Finite Chain Rings*, arXiv:2106.09403 (first posted 2021), especially the chain-ring preliminaries and Proposition 15 on unrestricted matrix types. https://arxiv.org/pdf/2106.09403 .
