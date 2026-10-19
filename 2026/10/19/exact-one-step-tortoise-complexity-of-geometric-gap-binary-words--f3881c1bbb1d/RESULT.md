# Exact one-step tortoise complexity of geometric-gap binary words

## Finding
For an integer \(b\ge2\), let \(x^{(b)}=x_0x_1\cdots\) be the binary word whose symbols equal \(1\) exactly at the positions \(b^j-1\), for integers \(j\ge0\), and equal \(0\) elsewhere. Let \(T\) move the leftmost \(1\) of a finite binary word to the right end, preserving all other symbols; set \(T(0^n)=0^n\). Write \(P_b(n)\) for the number of distinct \(T\)-images of length-\(n\) contiguous factors of \(x^{(b)}\).

For every integer \(n\ge1\),
\[
P_b(n)=\begin{cases}
2,&1\le n<b,\\
3,&b\le n\le b(b-1),\\
2+b^{k-1}+\min\!\bigl\{n-(b-1)b^k,\ (b-1)b^{k-1}\bigr\},
  &(b-1)b^k\le n\le(b-1)b^{k+1},\quad k\ge1.
\end{cases}
\]
The overlapping endpoint formulas agree, including the case \(b=2\). In particular the successive increments \(P_b(n+1)-P_b(n)\) have arbitrarily long zero-runs and arbitrarily long one-runs. More precisely,
\[
\liminf_{n\to\infty}\frac{P_b(n)}n=\frac1{b(b-1)},\qquad
\limsup_{n\to\infty}\frac{P_b(n)}n=\frac b{b^2-1}.
\]

## Assumptions and scope
Positions and factor starting positions are zero-based, factor length \(n\) is positive, and \(b\) is a fixed integer at least \(2\). We count **distinct image words**, not factor occurrences. The support points are \(a_j=b^j-1\), with increasing consecutive distances \(d_j=a_{j+1}-a_j=(b-1)b^j\). The theorem is about one application of the binary tortoise operator, not multiple iterations, ordinary factor complexity, or other source words.

## Proof
**Images and injectivity.** Every sufficiently long zero gap supplies \(0^n\) and all factors having exactly one \(1\); after applying \(T\), the latter all become \(0^{n-1}1\). These give exactly two image words with at most one \(1\). The image preserves the total number of ones. If a factor starts at \(t\) and contains at least three ones, with its first three ones at \(a_j,a_{j+1},a_{j+2}\), then the first two ones remaining in its image occupy positions \(a_{j+1}-t-1\) and \(a_{j+2}-t-1\). Their distance is \(d_{j+1}\). Since the distances are strictly increasing, the image determines \(j\), and its first remaining one determines \(t\). Consequently **distinct factors with at least three ones have distinct images**.

For a given \(j\ge0\), the starts of windows containing \(a_j,a_{j+1},a_{j+2}\) include exactly the integer interval
\[
J_j=[\max\{0,a_{j+2}-n+1\},\ a_j]
\]
when the interval is nonempty. Taking the union over \(j\) counts all starts of factors with at least three ones. Here and below a closed integer interval with lower endpoint greater than upper endpoint is empty.

**Images with exactly two ones.** Such a window has consecutive support points \(a_j,a_{j+1}\), with no preceding or following support point in the window. If \(t\) is its start, the nontrailing one in its image is at position \(r=a_{j+1}-t-1\). For \(j\ge1\) the possible values form the interval
\[
I_j=\left[
\max\{d_j-1,n-d_{j+1}-1\},\quad
\min\{n-2,d_{j-1}+d_j-2\}
\right].
\]
For \(j=0\), the upper endpoint is instead \(\min\{n-2,d_0-1\}\), since windows cannot start before zero. The union of these intervals counts distinct two-one images because the image is determined by \(r\). This reduction uses neither an asymptotic argument nor a computation.

**Initial lengths.** If \(n<b=d_0+1\), no factor contains two ones, proving \(P_b(n)=2\). If \(b\le n\le d_1=b(b-1)\), only the adjacent pair \(a_0,a_1\) fits, and it gives the single additional image \(0^{d_0-1}1 0^{n-d_0-1}1\) (equivalently, its nontrailing \(1\) is at position \(d_0-1\)); hence \(P_b(n)=3\). This image is well defined since \(n\ge d_0+1\).

**First geometric scale.** Suppose \(d_1\le n\le d_2\). The starts with at least three ones are \(J_0\); this set consists of the sole start \(t=0\) exactly when \(n>d_0+d_1\). Otherwise \(I_0\) consists of its sole possible image \(r=d_0-1\). Thus \(J_0\) and \(I_0\) always contribute exactly one image between them. Meanwhile
\[
I_1=[d_1-1,\ \min\{n-2,d_0+d_1-2\}]
\]
has \(\min\{d_0,n-d_1\}\) integer entries and does not intersect \(I_0\). All other intervals are empty. It follows that
\(P_b(n)=3+\min\{d_0,n-d_1\}\), the stated formula at \(k=1\).

**Later geometric scales.** Fix \(k\ge2\) and \(d_k\le n\le d_{k+1}\). Abbreviate
\[
A=d_{k-2},\qquad B=d_{k-1}=bA,\qquad C=d_k=bB,\qquad D=d_{k+1}=bC.
\]
The triple-window intervals \(J_0,\ldots,J_{k-2}\) together cover **exactly every integer start from \(0\) through \(a_{k-2}\)**; their union therefore has \(a_{k-2}+1=b^{k-2}\) points. Indeed, their individual right endpoints are \(a_j\), and each interval begins no later than the previous right endpoint plus one. At the extremal index this follows from
\(d_{k-3}+d_{k-2}+d_{k-1}\le d_k\) whenever the terms exist, because \(1+b+b^2\le b^3\) for \(b\ge2\). The first interval reaches zero. The next interval \(J_{k-1}\) adds precisely
\[
u=\min\{A,\max\{0,n-(B+C)\}\}
\]
new starts; all later \(J_j\) are empty because their three-one spans exceed \(n\).

For images having exactly two ones, all intervals \(I_j\) except \(I_{k-1}\) and \(I_k\) are empty: for earlier indices the immediately preceding and following support points force a span shorter than \(n\), and for later indices the consecutive gap is at least \(D\ge n\). The two possible remaining intervals are
\[
I_{k-1}=[\max\{B-1,n-C-1\},\ A+B-2],\qquad
I_k=[C-1,\ \min\{n-2,B+C-2\}].
\]
They are disjoint because \(A+B\le C\), equivalent to \(b+1\le b^2\). Their respective numbers of entries are
\[
\ell_-=\max\{0,\min\{A,A+B+C-n\}\},\qquad
\ell_+=\min\{B,n-C\}.
\]
Directly from these expressions \(u+\ell_-=A\). Adding the two images with at most one \(1\), the injective triple-window images, and the two disjoint two-one-image sets yields
\[
P_b(n)=2+b^{k-2}+u+\ell_-+\ell_+
       =2+b^{k-1}+\min\{B,n-C\},
\]
as required.

**Asymptotic endpoints.** On each interval from \(d_k\) to \(d_{k+1}\), the formula first increases at unit rate until \(h_k=d_k+d_{k-1}=(b^2-1)b^{k-1}\), then stays constant. For sufficiently large \(k\), the ratio \(P_b(n)/n\) increases on the first subinterval and decreases on the second. Evaluating at \(d_k\) and \(h_k\), respectively, gives the two displayed limiting ratios. Both endpoint subsequences tend to infinity, proving the liminf and limsup.

## Verification
The accompanying `checker.py` independently computes (i) actual image sets of every factor in long finite prefixes, (ii) counts of the window-start and image-position interval unions, and (iii) the claimed closed form. It compares these methods for \(1400\) direct finite-factor cells and \(22648\) interval-count cells, including threshold boundaries. Its observed output is in `computation.txt`. Finite agreement is a regression check and **not** a proof for all lengths; the preceding interval argument proves the formula.

## Relationship to prior work
Campbell and Rampersad introduce tortoise complexity and study the Thue–Morse and paperfolding words, as well as bounded-gap comparisons. Those results do not specialize to the present unbounded geometric-gap word. Gheorghiciuc derives ordinary **factor** complexity for strictly increasing gap words and analyzes exponential occurrence positions. That source treats the same broad kind of sparse support, but counts untransformed factors; it does not determine collisions after the tortoise map. The present formula is an image-complexity computation, rather than a restatement of either count.

## Limitations
The theorem is for the specific support \(\{b^j-1:j\ge0\}\), integer \(b\ge2\), and a single tortoise application. It does not determine multi-iteration tortoise complexity or arbitrary increasing-gap sequences. Exhaustive computations cover only the stated finite ranges. The literature comparison is necessarily limited to accessible records and primary texts; independent review remains outstanding.

## References
1. John M. Campbell and Narad Rampersad, *Subword enumeration up to stack-sorting equivalence*, arXiv:2604.25811, first public 28 April 2026, https://arxiv.org/abs/2604.25811 . Sections 2–4 and the later examples establish the operator and the motivating complexity questions.
2. Irina Gheorghiciuc, *The subword complexity of a class of infinite binary words*, arXiv:math/0512256, first public 13 December 2005, https://arxiv.org/abs/math/0512256 . Theorems 1.2 and 2.1 treat ordinary factor complexity of increasing-gap words.
