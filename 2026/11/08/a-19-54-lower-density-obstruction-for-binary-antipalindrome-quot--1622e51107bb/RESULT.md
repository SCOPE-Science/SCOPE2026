# A \(19/54\) lower-density obstruction for binary antipalindrome quotients

## Finding

Let \(\mathcal A\) consist of all positive integers whose canonical binary expansions have even length and whose second half is the reverse bitwise complement of the first half. Define
\[
\mathcal Q_{\mathcal A}=\{N\in\mathbb Z_{>0}:N=A/B\text{ for some }A,B\in\mathcal A\}.
\]
Then the set of positive integers not representable as such quotients has lower natural density at least \(19/54\):
\[
\boxed{\liminf_{X\to\infty}\frac{\#([1,X]\cap(\mathbb Z_{>0}\setminus\mathcal Q_{\mathcal A}))}{X}\ge\frac{19}{54}.}
\]
Equivalently, the upper natural density of \(\mathcal Q_{\mathcal A}\) is at most \(35/54\). In fact, an explicit, parity-separated set of forbidden integers defined below has **exact** lower density \(19/54\). No assertion is made that the lower density of the full complement is exactly this value.

## Assumptions and scope

All binary strings are canonical, without leading zeros. An antipalindrome has length \(2h\) for some positive integer \(h\), with bits \(s_1\cdots s_h(1-s_h)\cdots(1-s_1)\), where \(s_1=1\). The numerator and denominator are arbitrary members of \(\mathcal A\), with no upper bound on their lengths. Quotients are counted only when they are positive integers. Densities refer to ordinary counting measure on the positive integers, not logarithmic density.

For each integer \(j\ge0\), define the disjoint parity-restricted obstructions
\[
E_j=\{n\in2\mathbb Z_{>0}:2\cdot4^j\le n\le4^{j+1}\},\qquad
O_j=\{n\in2\mathbb Z_{>0}+1:\tfrac32\,4^j<n<\tfrac83\,4^j\}.
\]
Write \(F=\bigcup_{j\ge0}(E_j\cup O_j)\). The theorem proves both \(F\cap\mathcal Q_{\mathcal A}=\varnothing\) and \(\underline d(F)=19/54\).

## Proof

**1. The leading-ones/terminal-zeros identity.** Let \(T\in\mathcal A\) have length \(2h\), and let \(r(T)\) denote the length of its initial run of \(1\)'s. The reverse-complement structure implies that precisely \(r(T)\) terminal digits are zero. This remains true when the first half consists entirely of ones: the trailing half then consists entirely of zeros, and the preceding digit is one. Consequently,
\[
\nu_2(T)=r(T).
\]
Set \(m(T)=T/2^{2h-1}\in[1,2)\). If \(r(T)=1\), the normalized leading bits are \(10\), so \(1\le m(T)<3/2\). If \(r(T)\ge2\), the normalized leading bits are \(11\), so \(3/2\le m(T)<2\).

**2. The two quotient-shell restrictions.** Suppose \(N=A/B\) is a positive integer, with \(A,B\in\mathcal A\) of lengths \(2a,2b\). Then
\[
N=4^{a-b}\frac{m(A)}{m(B)},\qquad \nu_2(N)=r(A)-r(B)\ge0.
\]
If \(N\) is odd, \(r(A)=r(B)\). If this common length is one, both mantissas are in \([1,3/2)\); if it is at least two, both are in \([3/2,2)\). Hence for every such odd quotient,
\[
\frac23\,4^d<N<\frac32\,4^d\quad\text{for some integer }d=a-b.
\]
If \(N\) is even, \(r(A)>r(B)\). The first differing leading binary digit of the two normalized mantissas is a one in \(m(A)\) and a zero in \(m(B)\), even if the first half of \(B\) consists entirely of ones. Thus \(m(A)>m(B)\). As \(m(A)<2\) and \(m(B)\ge1\),
\[
4^d<N<2\cdot4^d\quad\text{for some integer }d=a-b.
\]
These open windows are disjoint when indexed by successive powers of four: the gap between successive even-quotient windows contains \([2\cdot4^j,4^{j+1}]\), while the gap between successive odd-quotient windows contains \([\tfrac32\,4^j,\tfrac83\,4^j]\). Therefore \(F\cap\mathcal Q_{\mathcal A}=\varnothing\).

**3. Exact density of the forbidden set.** The parity restrictions make the shells disjoint. Direct counting gives
\[
|E_j|=4^j+1\quad(j\ge0),\qquad |O_0|=0,\qquad
|O_j|=\frac{7\cdot4^j-4}{12}\quad(j\ge1).
\]
For \(k\ge1\), all earlier shells lie below \(X_k=\tfrac32\,4^k\), and none of the new shell's elements lies at or below \(X_k\). Summation gives the **exact integer identity**
\[
\#(F\cap[1,X_k])=\frac{19}{36}4^k+\frac{2k}{3}-\frac79.
\]
It follows that \(\lim_{k\to\infty}\#(F\cap[1,X_k])/X_k=19/54\), proving \(\underline d(F)\le19/54\).

For the reverse inequality, let \(4^k\le X<4^{k+1}\) and put \(t=X/4^k\in[1,4)\). The contribution of all complete earlier shells is \(\tfrac{19}{36}4^k+O(k)\), uniformly in \(t\); the partially encountered even and odd gaps contribute respectively
\[
\frac{4^k}{2}\max(0,t-2)+O(1),\qquad
\frac{4^k}{2}\min\!\left(\frac76,\max\!\left(0,t-\frac32\right)\right)+O(1).
\]
Thus, uniformly for \(1\le t<4\),
\[
\frac{\#(F\cap[1,X])}{X}=
\frac{\frac{19}{36}+\frac12\max(0,t-2)+\frac12\min(\frac76,\max(0,t-\frac32))}{t}
+O\!\left(\frac{k+1}{4^k}\right).
\]
The leading function decreases on \([1,3/2]\), increases on \([3/2,8/3]\), and decreases on \([8/3,4]\); its global minimum on \([1,4]\) occurs at \(t=3/2\), with value \(19/54\). Hence \(\underline d(F)=19/54\). Since \(F\) is a subset of the complement, the claimed lower-density bound follows.

## Verification

The standalone Python 3 checker in `CHECK.py` constructs every binary antipalindrome of lengths \(2,4,\ldots,16\), verifies that the leading-one count equals the \(2\)-adic valuation for all \(255\) distinct values, and tests the required quotient shells for every integer quotient among \(65{,}025\) ordered pairs. It also independently enumerates both forbidden parity classes at the first eight exact shell boundaries, checking the displayed finite-count identity. The expected output is `CHECK_OUTPUT.txt`; the program requires no additional packages or network access. These checks do not replace the proof for arbitrary lengths or infinitely many shells.

## Relationship to prior work

Bai, Meleshko, Riasat and Shallit [1], first posted on 2022-02-28, introduce these exact binary antipalindrome quotients, prove decidability (Theorem 14), and conjecture density zero for the representable set (Conjecture 5). In its antipalindrome section, Theorem 18 and Corollary 19 prove a lower density \(1/60\) for nonrepresentable integers using a narrower three-leading-bit and residue-class restriction. The present parity-separated valuation/shell argument yields \(19/54\), which is strictly larger than \(1/60\), and its exact explicit-shell density is not obtained from that weaker numerical bound. The corresponding palindrome quotient results (including other digit-cylinder bounds) concern a different numerator/denominator class and do not imply this assertion. OEIS A351172 and A351173 [2] tabulate the representable and nonrepresentable sets, respectively; their initial terms are consistent with the obstruction. Broad mathematical-index and equivalent-formulation searches revealed no stronger covering result among accessible materials, but completeness of the literature cannot be guaranteed.

## Limitations

The bound is one-sided and does not prove the conjectured zero density of representable antipalindrome quotients. The value \(19/54\) is the exact lower density of the exhibited forbidden subset \(F\), not asserted to be sharp for the full complement. The conclusion concerns binary antipalindromes and **integer** ratios only; it does not cover arbitrary rational ratios or other bases. Independent validation has not been performed.

## References

[1] J. H. Bai, J. Meleshko, S. Riasat and J. Shallit, *Quotients of Palindromic and Antipalindromic Numbers*, arXiv:2202.13694v1 (first posted 2022-02-28), especially Sections 2.4, 3.2 and 3.4, Theorem 18, Corollary 19 and Conjecture 5. Full text: https://arxiv.org/html/2202.13694v1. Published as *INTEGERS* 22 (2022), article A96.

[2] *On-Line Encyclopedia of Integer Sequences*, A351172 and A351173, sets of representable and nonrepresentable positive integer quotients of binary antipalindromes, https://oeis.org/A351172 and https://oeis.org/A351173.
