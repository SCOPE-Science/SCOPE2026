# A power-saving upper bound for odd binary-convolution-perfect composites

## Finding
Let \(A(a)=\{i\geq0:\text{the binary digit of }a\text{ at }i\text{ is }1\}\), and put
\[
H(a,b)=\max_{s\geq0}\#\{(i,j)\in A(a)\times A(b):i+j=s\}.
\]
Call an odd composite integer \(n\) *binary-convolution-perfect* when \(H(a,b)=1\) for every nontrivial factorization \(n=ab\), with \(1<a\leq b<n\). Write \(\Pi_{\mathrm{odd}}(X)\) for the number of such integers at most \(X\).

**Theorem.** With \(\vartheta=1-\frac16\log_2(4/3)=0.93082708345\ldots\), one has
\[
\Pi_{\mathrm{odd}}(X)=O\!\left(X^{\vartheta}\log(2X)\right)\quad(X\to\infty).
\]
In particular, odd binary-convolution-perfect composites have natural density zero, with a power saving.

## Assumptions and scope
Integers \(a,b\) in the proof are odd and at least \(3\), with \(a\leq b\). Put \(t=\lfloor\log_2a\rfloor\), \(B=\lfloor\log_2b\rfloor\), and \(k=t+B\), so \(1\leq t\leq B\). The bound counts composites, **not** odd primes (the latter have no nontrivial factorization). The implied constant is absolute. No assumptions about prime distributions or numerical experiments are made.

## Proof
Every counted composite \(n\) has some nontrivial odd factor pair \(n=ab\) with \(a\leq b\) and \(H(a,b)=1\). Hence it suffices to bound the total number of binary-orthogonal pairs \((a,b)\) with \(3\leq a\leq b\) odd and \(ab\leq X\). Since \(a\geq2^t\), \(b\geq2^B\), we have \(2^k\leq ab\leq X\).

**Case 1: \(t\leq B/2\).** Because \(a\) is odd and has highest one-bit at position \(t\), its bit support contains \(0\) and \(t\). If \(b\) has one-bits at both \(j\) and \(j+t\), then the distinct pairs \((t,j)\) and \((0,j+t)\) contribute to the same convolution coefficient. This violates \(H(a,b)=1\). Thus the bit pattern of \(b\) is an independent set in the graph on \(\{0,\ldots,B\}\) with edges \(\{j,j+t\}\), for \(0\leq j\leq B-t\).

This graph is the union of \(t\) disjoint paths. If the paths have \(v_1,\ldots,v_t\) vertices, they admit disjoint matchings with total size
\[
m=\sum_{r=1}^t\lfloor v_r/2\rfloor\geq\frac{(B+1)-t}{2}\geq\frac B4.
\]
Each matching edge permits only three of its four binary labelings (the labeling \((1,1)\) is forbidden), independently of other matching edges; every unmatched vertex allows either bit. Thus for each possible \(a\), there are at most
\[
2^{B+1}(3/4)^m\leq 2^{B+1}(3/4)^{B/4}
\]
possible \(b\). There are at most \(2^t\) candidates for \(a\). Since \(B\geq2k/3\), the pair count for fixed \((t,B)\) is at most
\[
2^{t+B+1}(3/4)^{B/4}\leq2^{1+k-(B/4)\log_2(4/3)}\leq 2^{1+\vartheta k}.
\]

**Case 2: \(B/2<t\leq B\).** When \(H(a,b)=1\), all convolution coefficients are at most one. There are at most \(k+1\) possible coefficient positions, namely \(0,\ldots,k\). Counting the ordered pairs of one-bits gives
\[
|A(a)|\,|A(b)|\leq k+1.
\]
Consequently one of the two factors has at most \(\sqrt{k+1}\) one-bits. Both factors have binary length at most \(B+1\), with \(B<2k/3\). Set \(r=\lceil\sqrt{k+1}\rceil\). The number of positive integers of binary length at most \(B+1\) and at most \(r\) one-bits is bounded by
\[
\sum_{j=0}^{r}\binom{B+1}{j}\leq(r+1)(B+2)^r\leq(k+2)^{r+1}.
\]
Here the binomial sum is interpreted with coefficients zero for indices exceeding \(B+1\). After choosing which factor is sparse, the other has at most \(2^{B+1}\) possible binary strings. Thus the pair count for fixed \((t,B)\) is at most
\[
2^{B+2}(k+2)^{r+1}\leq2^{\frac23k+2+O(\sqrt{k}\log(k+2))}.
\]
Because \(\vartheta>2/3\), this is \(O(2^{\vartheta k})\), with an absolute constant uniformly valid for all positive integers \(k\). No claim that sparsity is sufficient for orthogonality is used.

There are at most \(k+1\) pairs of nonnegative integers \((t,B)\) with \(t+B=k\). Setting \(L=\lfloor\log_2 X\rfloor\), the preceding bounds yield
\[
\Pi_{\mathrm{odd}}(X)\leq C\sum_{k=1}^{L}(k+1)2^{\vartheta k}
=O\!\left((L+1)2^{\vartheta L}\right)
=O\!\left(X^{\vartheta}\log(2X)\right).
\]
As \(\vartheta<1\), division by \(X\) tends to zero. This completes the proof.

## Verification
The standalone `verify.py` checks the matching inequality for all \(1\leq t\leq B/2\) and \(2\leq B<70\), checks the stated exponent numerically, and independently enumerates all odd composites below \(10^4\) and \(10^5\), testing *every* nontrivial factor pair directly using one-bit sums. The resulting counts are \(130\) and \(522\), matching the two corresponding published counts. The program prints `VERIFY_OK` on success. These finite tests check examples and arithmetic; the general theorem follows from the proof above.

## Relationship to prior work
Iizumi's 2026 article introduced the binary convolution framework, proved the representation-function and difference-set equivalences (Theorems 1 and 2), defined binary-convolution-perfect integers (Definition 6), computed finite counts (Table 3), and **explicitly asked** in Question 9.5.2 for a quantitative bound on the number of odd binary-convolution-perfect composites. The displayed theorem supplies a power-saving answer to that counting question. It uses the source's definitions, and its counting argument is additional rather than a reformulation of the source's difference-set equivalence.

The distinction from finite binary-weight product classifications is substantive: those classify specific small Hamming-weight patterns, while this proof controls *all* possible odd factor pairs of a given total bit length. Earlier published work on low-weight products or one-bit-convolution sumsets might contain an implicit comparable count; independent literature review is warranted.

## Limitations
The exponent \(\vartheta\) is not claimed optimal. The upper bound does not give an asymptotic formula, a sharp constant, or a count of odd BCT-perfect *primes*. In the original article the full counting question also allows other forms including even BCT-perfect integers; those are not covered here. Computational enumeration is finite and is not part of the infinite proof. Priority cannot be established solely by unsuccessful searches; the accessible HTML text was read but a separately downloadable publisher PDF was unavailable.

## References
1. M. Iizumi, *Binary convolution height: Structural invariants of integer factorisations*, Research in Mathematics 13 (2026), article 2727395, first published online September 11, 2026. DOI: https://doi.org/10.1080/27684830.2026.2727395. In particular Definitions 1, 5, 6; Theorems 1, 2; Table 3; and Question 9.5.2.
2. T. Tao and V. Vu, *Additive Combinatorics*, Cambridge University Press, 2006 (standard finite-set representation functions, background only).
