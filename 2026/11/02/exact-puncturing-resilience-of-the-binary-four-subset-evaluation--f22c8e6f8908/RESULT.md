# Exact puncturing resilience of the binary four-subset evaluation code

## Finding
For every integer \(k\ge 6\), consider the binary linear code
\[
\mathcal C_{k,4}=\left\{\left(\sum_{i\in X}a_i\bmod 2\right)_{X\in\binom{[k]}{4}}:a\in\mathbb F_2^k\right\}.
\]
It has length \(\binom{k}{4}\), dimension \(k-1\), and is minimal: no two distinct nonzero codewords have comparable supports. Define \(R(k)\) as the least number of coordinate positions whose puncturing produces a *nonminimal* code. Then
\[
\boxed{R(6)=2,\quad R(7)=6,\quad R(8)=12,\quad R(k)=\binom{k-2}{2}\ \ (k\ge9).}
\]
Every puncturing of fewer than \(R(k)\) coordinates preserves both minimality and dimension \(k-1\). For each \(k\ge6\), an attaining puncturing of exactly \(R(k)\) coordinates exists that still has dimension \(k-1\) but is nonminimal.

## Assumptions and scope
The field is \(\mathbb F_2\). Each coordinate is a distinct four-element subset \(X\subseteq[k]\). Puncturing removes a selected collection of coordinates, not message positions; no shortening or repeated coordinates are allowed. Codeword support means its set of nonzero retained coordinates. A binary code is minimal when no support of one nonzero codeword is properly contained in the support of a different nonzero codeword. The result concerns all integers \(k\ge6\) and arbitrary adversarial coordinate erasures.

## Proof
**1. Rank and the support-obstruction count.** The incidence vectors of all four-subsets span precisely the even-weight subspace of \(\mathbb F_2^k\) for \(k\ge6\). Indeed, differences of two four-subsets sharing three positions give every vector \(e_i+e_j\), by choosing three positions outside \(\{i,j\}\). Every column has even weight, so the kernel of the evaluation map is exactly \(\langle\mathbf1\rangle\), and the code has dimension \(k-1\).

Take two message vectors \(a,b\). Write \((A,B,C,D)\) for the counts of their coordinate pairs of types \(00,01,10,11\), respectively, so \(A+B+C+D=k\). The corresponding codewords are distinct and nonzero exactly when at least three of these counts are positive: with at most two types some nonzero linear combination of \(a,b\) is constant, and with at least three types none is constant.

For such a pair, the coordinates obstructing \(\operatorname{supp}(c_b)\subseteq\operatorname{supp}(c_a)\) are precisely the four-subsets \(X\) with \((a\cdot X,b\cdot X)=(0,1)\). Their count is
\[
\begin{aligned}
P(A,B,C,D)={}&AB\left(\binom{C}{2}+\binom{D}{2}\right)
+CD\left(\binom{A}{2}+\binom{B}{2}\right)\\
&+A\binom{B}{3}+B\binom{A}{3}+C\binom{D}{3}+D\binom{C}{3}.
\end{aligned}
\]
Here \(\binom nr=0\) for \(r>n\) or \(r<0\). To derive the formula, partition a selected four-subset by its four type multiplicities. A type-XOR of \(01\) can arise only through a \(3+1\) pattern involving the complementary pairs \(00/01\) or \(10/11\), or through a \(2+1+1\) pattern with the two singleton types forming one of those pairs. These are exactly the displayed terms.

Consequently, if
\[
L(k)=\min\{P(A,B,C,D):A+B+C+D=k,\ \#\{m>0:m\in\{A,B,C,D\}\}\ge3\},
\]
then every erasure set of cardinality below \(L(k)\) preserves minimality. It also preserves the original rank: if a nonconstant message vanished on all retained coordinates, choose an independent message modulo \(\langle\mathbf1\rangle\); the erased support of the first message contains its entire positive obstruction against that second message, contradicting the lower bound \(L(k)\).

**2. Finite bases.** Directly exhaust the nonnegative four-tuples of sum \(k\) with at least three positive entries. The complete minima are

| \(k\) | Number of admissible quadruples | \(L(k)\) | Attaining quadruple \((A,B,C,D)\) |
|---|---:|---:|---|
| 6 | 50 | 2 | \((3,2,0,1)\) |
| 7 | 80 | 6 | \((3,3,0,1)\) |
| 8 | 119 | 12 | \((3,3,1,1)\) |
| 9 | 168 | 21 | \((1,1,0,7)\) |

These are exhaustive finite certificates, not inductive guesses; the accompanying `verify.py` reproduces the four nested integer loops and separately checks the result for every independent ordered binary message pair for \(6\le k\le9\).

**3. A three-subset growth lemma.** For a four-type multiplicity vector \(m=(m_0,m_1,m_2,m_3)\), regard types as elements of \(\mathbb F_2^2\). Let \(T_w(m)\) count three-element subsets whose type XOR is \(w\). Direct enumeration gives
\[
T_w(m)=\binom{m_w}{3}+m_w\sum_{u\ne w}\binom{m_u}{2}+\prod_{u\ne w}m_u.
\]
If at least three types occur and \(n=\sum m_i\ge7\), then
\[
T_w(m)\ge n-2\qquad\text{for every }w\in\mathbb F_2^2.
\]
For \(n=7\), an exhaustive check of all 80 admissible multiplicity vectors and all four values of \(w\) gives minimum \(5\). For the induction, if \(n\ge8\), remove an element from any type with multiplicity at least two. At least three types remain. Restoring one element of type \(t=w\) increases \(T_w\) by \(\sum_u\binom{m_u}{2}\ge1\), where \(m\) now denotes the reduced vector. Restoring type \(t\ne w\) increases it by \(m_wm_t+\prod_{u\notin\{w,t\}}m_u\ge1\): since at least three types are present, either the first product or the second is positive. The induction proves the bound.

**4. Infinite lower bound.** For \(k\ge10\), remove an element from a type having multiplicity at least two in any admissible quadruple. The reduced \((k-1)\)-tuple still contains at least three types. The number of new obstructing four-subsets containing the added element of type \(t\) is exactly \(T_{01+t}\) on the remaining \(k-1\) elements, so it is at least \(k-3\) by Step 3. By induction from the \(k=9\) base,
\[
P_k\ge L(k-1)+(k-3)\ge\binom{k-3}{2}+k-3=\binom{k-2}{2}.
\]
Thus \(L(k)\ge\binom{k-2}{2}\) for every \(k\ge9\).

**5. Attainment and retained rank.** For \(k\ge9\), use type counts \((1,1,0,k-2)\). Precisely the \(\binom{k-2}{2}\) four-subsets consisting of the unique \(00\) position, the unique \(01\) position and two \(11\) positions have parity output \((0,1)\). Delete those positions. The undeleted four-subsets with output \((1,0)\) and \((1,1)\) both occur (in each case in \(\binom{k-2}{3}\) ways), so the resulting two codewords are distinct, nonzero, and support-comparable. Moreover, the retained columns include every four-subset of the \((k-2)\)-element \(11\) group and the columns consisting of either special position plus three from that group. The former span the even-weight subspace on the large group, while the latter add two independent special coordinates; hence the retained rank is \(k-1\). The three small attaining quadruples in Step 2 yield the same nonminimality and full-rank conclusion, verified by exact binary row reduction in `verify.py`. Therefore \(R(k)=L(k)\) for all stated lengths.

## Verification
Run `python3 verify.py` using only the Python standard library. The script enumerates all finite basis quadruples, certifies the initial three-subset inequality, checks its predicted inequality for a larger range, independently uses Walsh/Krawtchouk counting for every eligible message pair through \(k=9\), and checks the explicit attaining puncturings and their binary ranks. A successful replay prints `VERIFY_OK`. The all-length conclusion follows from the two inductions in Step 3 and Step 4, not from a finite search.

## Relationship to prior work
Huang, Liao, Mesnager, Tang, and Yan introduce fixed-Hamming-weight derived codes; taking the full binary ambient message space and weight four yields the evaluation code studied here. Zhou, Li, Tang, and Ding previously studied complete weight-layer codes and their weight distributions. Alfarano, Borello, and Neri give the general cutting-blocking-set characterization of minimal codes. Xie, Wang, and Wu subsequently establish minimality and other parameters of complete weight-layer codes, including the four-subset case. These results identify or establish minimality of the unpunctured construction. The present theorem computes the first adversarial puncturing size that destroys minimality *while retaining full code dimension*, a different extremal invariant. No claim of independent priority confirmation is made.

## Limitations
The result concerns the full binary weight-four layer, not arbitrary four-uniform designs, other weights, nonbinary alphabets, coordinate additions, or probabilistic erasures. It gives the earliest failure threshold, not the complete classification of minimum failure patterns. The originality comparison is limited to inspected literature and indexed records; unindexed equivalent work remains possible. No independent mathematical audit has been performed.

## References
- D. Huang, Q. Liao, S. Mesnager, G. Tang, H. Yan, *On the Hamming Weight Functions of Linear Codes*, arXiv:2511.18250 (first posted November 23, 2025), https://arxiv.org/abs/2511.18250.
- Z. Zhou, X. Li, C. Tang, C. Ding, *Binary LCD Codes and Self-Orthogonal Codes From a Generic Construction*, IEEE Transactions on Information Theory 65 (2019), 16–27, https://doi.org/10.1109/TIT.2018.2823704.
- G. N. Alfarano, M. Borello, A. Neri, *A Geometric Characterization of Minimal Codes and Their Asymptotic Performance*, arXiv:1911.11738, https://arxiv.org/abs/1911.11738.
- X. Xie, M. Wang, T. Wu, *Minimality of Binary Codes From Weight Layers and Graph Cut Spaces*, arXiv:2610.35372 (first posted October 26, 2026), https://arxiv.org/abs/2610.35372.
