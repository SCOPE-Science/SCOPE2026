# Exact minimal-excess times for alternating mixed-radix additive complements

## Finding
Let \(r_0,r_1,\ldots\) be arbitrary integers with \(r_i\ge 2\), and let \(Q_0=1\) and \(Q_k=\prod_{j=0}^{k-1}r_j\) for \(k\ge 1\). Partition mixed-radix digits into two sets: \(A\) consists of all finite sums \(\sum_{j\text{ even}}d_jQ_j\), and \(B\) consists of all finite sums \(\sum_{j\text{ odd}}d_jQ_j\), where \(0\le d_j<r_j\). Write \(A(n)=|A\cap[0,n]|\), \(B(n)=|B\cap[0,n]|\) for integers \(n\ge 0\).

**Theorem.** For every \(n\ge 0\),
\[
 A(n)B(n)-n=1\quad\Longleftrightarrow\quad
 n=tQ_k-1\ \text{for some }k\ge 0\ \text{and }1\le t<r_k.
\]
The indicated expressions for \(n\) are distinct. Consequently for every \(K\ge 0\),
\[
 \#\{0\le n<Q_K:A(n)B(n)-n=1\}=1+\sum_{k=0}^{K-1}(r_k-1).
\]
For constant radix \(r_i=b\ge2\), there are exactly \(1+K(b-1)\) equality points below \(b^K\); when \(b=2\), the equality points are precisely \(n=2^k-1\), for \(k\ge0\).

## Assumptions and scope
The radices may vary arbitrarily and need not be bounded. All expansions are finite, all digits are integers in the stated ranges, and all counting arguments take place at nonnegative integer \(n\). The sets contain zero. Every nonnegative integer has a unique representation as \(a+b\) with \(a\in A\) and \(b\in B\), by uniqueness of its mixed-radix expansion. Thus \(A(n)B(n)\ge n+1\), and the theorem characterizes every instance of equality.

## Proof
For \(k\ge0\), let \(A_k\) and \(B_k\) be the finite digit sets using positions strictly below \(k\), with cardinalities \(\alpha_k\) and \(\beta_k\). Mixed-radix uniqueness gives \(\alpha_k\beta_k=Q_k\). Their largest elements satisfy \(\max A_k+\max B_k=Q_k-1\), and their pairs represent every integer from \(0\) through \(Q_k-1\) exactly once.

Take \(n\ge1\). There are unique \(k\ge0\), \(1\le d<r_k\), and \(0\le u<Q_k\) with \(n=dQ_k+u\). Suppose first that \(k\) is even. All the digits of \(B\) occur below \(k\), hence \(B(n)=\beta_k\), while counting the \(d\) complete lower-digit blocks and the partial block gives \(A(n)=d\alpha_k+A_k(u)\). It follows that
\[
 A(n)B(n)-(n+1)=\beta_k A_k(u)-(u+1).
\]
Here \(A_k(u)=\#\{a\in A_k:a\le u\}\). The right-hand product counts pairs \((a,b)\in A_k\times B_k\) with \(a\le u\); the unique representations of \(0,\dots,u\) yield \(u+1\) pairs. If \(u=Q_k-1\), all pairs qualify and equality holds.

For \(k\ge2\) even and \(u<Q_k-1\), write the unique representation \(u=a+b\) with \(a\in A_k,b\in B_k\). If \(b<\max B_k\), the additional pair \((a,\max B_k)\) has first coordinate \(a\le u\) but sum exceeding \(u\). If \(b=\max B_k\), use \((\max A_k,\max B_k)\): because the largest lower digit position \(k-1\) belongs to \(B_k\), \(\max B_k\ge Q_{k-1}>\max A_k\), and hence \(\max A_k\le u\), whereas this pair sums to \(Q_k-1>u\). Thus the counted product is strictly greater than \(u+1\). For \(k=0\), \(A_0=B_0=\{0\}\), \(u=0=Q_0-1\), so equality always holds.

For odd \(k\), interchange \(A\) and \(B\): now \(A(n)=\alpha_k\), \(B(n)=d\beta_k+B_k(u)\), and
\[
 A(n)B(n)-(n+1)=\alpha_kB_k(u)-(u+1).
\]
The same argument applies because position \(k-1\) now belongs to \(A_k\), and \(\max A_k\ge Q_{k-1}>\max B_k\). Consequently, for every \(n\ge1\), equality is equivalent to \(u=Q_k-1\); \(n=0\) is also an equality point.

The equality points arising from a leading digit \(d\) in position \(k\) therefore have \(n=(d+1)Q_k-1\). When \(d+1<r_k\) this is a listed point with coefficient \(t=d+1\); when \(d+1=r_k\), it is \(Q_{k+1}-1\), listed at level \(k+1\) with \(t=1\). Conversely, at \(tQ_k-1\) the lower \(k\) digits are all maximal, so the same calculation gives equality. Strict growth of the \(Q_k\) makes the intervals \([Q_k-1,Q_{k+1}-1)\) disjoint, and within the interval the coefficients \(1\le t<r_k\) are distinct. This proves uniqueness of the indexed return times.

For a fixed \(K\), the return times below \(Q_K\) consist of \(Q_K-1\) and the \(r_k-1\) listed times at each level \(k<K\), giving the displayed count. The constant-base and binary formulas follow immediately. \(\square\)

## Verification
The included `verify.py` constructs the two sets from each finite radix list, checks all representations in the indicated finite range for existence and uniqueness, computes both counting functions, and compares all equality times with the theorem's predicted set. Tested total ranges are \(2^{15}=32768\), \(3^8=6561\), \(4^6=4096\), \(5^6=15625\), and five nonconstant-radix examples with products \(720,60,168,112,720\). All nine cases pass. Run `python3 verify.py`. Finite checks corroborate but do not replace the unrestricted proof above.

## Relationship to prior work
The alternating mixed-radix decomposition is established in Fang-Yu Ma, *A Note on Additive Complements* (2022), especially Lemma 3.1 and the construction (3.1). Ma proves that the counting-function excess equals one infinitely often and studies the limiting ratio; the complete if-and-only-if equality locus and its counting formula are not among the inspected results. Zihan Zhang, *A Sharp Bound for Additive Complements* (2026), Section 6, analyzes the base-four digit example \(A=\{\sum\epsilon_j4^j:\epsilon_j\in\{0,1\}\}\), \(B=2A\), and observes equality at \(4^k-1\). The theorem above determines every equality index for this example—indeed all \(2^k-1\)—and treats arbitrary radices. Ruzsa (2015/2017) notes the existence of digit-separated constructions with infinitely many equality points. Structural results for perfect additive complements by Fang and Sándor (2022) address different counting-function extrema.

## Limitations
No new representation construction or global sharp \(3/2\) threshold is claimed. The novelty claim is limited to the complete equality-time classification and exact frequency for this established mixed-radix construction; an earlier unindexed treatment could exist. The result gives no comparable classification for arbitrary additive complements outside this structured family. The verifier is finite and does not establish infinite validity on its own.

## References
1. Zihan Zhang, *A Sharp Bound for Additive Complements*, arXiv:2610.29963v1 (2026-10-21), Section 6, https://arxiv.org/pdf/2610.29963.
2. Fang-Yu Ma, *A Note on Additive Complements*, arXiv:2205.04128v1 (2022-05-09), Lemma 3.1 and (3.1), https://arxiv.org/pdf/2205.04128.
3. Imre Z. Ruzsa, *Exact additive complements*, arXiv:1510.00812v1 (2015-10-03), Section 1, https://arxiv.org/pdf/1510.00812.
4. Jin-Hui Fang and Csaba Sándor, *On function SX of additive complements*, arXiv:2210.09680v1 (2022-10-18), https://arxiv.org/abs/2210.09680.
