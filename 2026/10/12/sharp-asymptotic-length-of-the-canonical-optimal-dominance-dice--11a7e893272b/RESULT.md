# Sharp asymptotic length of the canonical optimal-dominance dice subcycle
## Finding
For each integer \(N\ge2\), consider the canonical \(N\)-sided dice \(K_0,K_1,\ldots,K_N\) introduced in the cited nontransitive-dice construction, with \(K_0=K_N\). Die \(K_k\) has \(k\) faces labeled \(k\) and \(N-k\) faces labeled \(k+N\). Let \(g_N\) be the smallest number of dice in an order-preserving subcycle of this canonical cycle for which every cyclic comparison has probability at least the sharp \(N\)-sided dominance probability
\[
p_N=\begin{cases}
\frac34-\frac1{2N}-\frac1{4N^2},&N\text{ odd},\\[3pt]
\frac34-\frac1{2N},&N\text{ even}.
\end{cases}
\]
Then
\[
\frac{g_N}{\sqrt N}\longrightarrow
C:=\sqrt2\sum_{r=0}^{\infty}\frac{\sqrt{r+1}-\sqrt r}{r+1}
=2.630472693388697\ldots.
\]

Let \(n(N)\) denote the unrestricted minimum number of \(N\)-sided dice attaining the same sharp dominance probability. Then
\[
\frac{\pi}{\sqrt2}\le
\liminf_{N\to\infty}\frac{n(N)}{\sqrt N}
\le
\limsup_{N\to\infty}\frac{n(N)}{\sqrt N}
\le C.
\]
The result therefore replaces the source's coarse square-root constants by an exact asymptotic constant for its canonical subcycles and an explicit universal lower constant.

## Assumptions and scope
An order-preserving subcycle is obtained by deleting dice from \(K_0,K_1,\ldots,K_N\) while retaining their cyclic order. The quantity \(g_N\) concerns this canonical family only. The quantity \(n(N)\) is the unrestricted minimum from the source and may be smaller; no claim is made that \(n(N)/\sqrt N\) converges or that its limit equals \(C\).

For consecutive retained indices \(0\le a<b\le N\), independence and the two-point form of the dice give
\[
\Pr\{K_a<K_b\}=1-\frac{(N-a)b}{N^2}.
\]
Thus the comparison is acceptable exactly when
\[
(N-a)b\le T_N,
\qquad
T_N=\begin{cases}
\frac{(N+1)^2}{4},&N\text{ odd},\\[3pt]
\frac{N(N+2)}{4},&N\text{ even}.
\end{cases}
\]

## Proof
Define the greedy successor
\[
F_N(a)=\min\!\left\{N,\left\lfloor\frac{T_N}{N-a}\right\rfloor\right\}.
\]
Every admissible next index \(b\) after \(a\) satisfies \(b\le F_N(a)\), and \(F_N\) is increasing. Hence, by induction, the greedy path beginning at \(0\) is at least as far to the right after every fixed number of steps as any admissible path. Consequently \(g_N\) is exactly the hitting time of \(N\) under repeated application of \(F_N\).

First let \(N=2m\). Center the greedy index by writing \(k=m+j\). Until the endpoint is reached, one step of the exact integer recurrence is
\[
j^+=j+1+\left\lfloor\frac{j(j+1)}{m-j}\right\rfloor.
\]
For odd \(N=2m+1\), use the same centering \(k=m+j\); then
\[
j^+=j+1+\left\lfloor\frac{j^2}{m+1-j}\right\rfloor.
\]
Both recurrences have the same square-root-scale local form. For fixed \(r\ge0\), the set of centered integers on which the increment equals \(r+1\) has, on its negative and positive components together,
\[
2\sqrt m\bigl(\sqrt{r+1}-\sqrt r\bigr)+O_r(1)
\]
points. For the even case this follows by solving
\[
\frac{j(j+1)}{m-j}=r,
\]
whose two roots have separation
\[
\sqrt{(r+1)^2+4rm};
\]
the total width of the \(r\)-th band is the difference of two consecutive root separations. For the odd case the corresponding root separation is
\[
\sqrt{r^2+4r(m+1)},
\]
and the same leading width results.

While the increment is \(r+1\), a monotone greedy orbit crosses a band in its width divided by \(r+1\), up to \(O_r(1)\) entrance and exit effects. Hence, for every fixed \(R\), the number of greedy steps spent in the bands \(0\le r\le R\) is
\[
2\sqrt m\sum_{r=0}^{R}
\frac{\sqrt{r+1}-\sqrt r}{r+1}+O_R(1).
\]
The omitted outer region is negligible after the square-root normalization. Indeed, when \(|j|\ge A\sqrt m\), the increment is bounded below by a constant multiple of \(j^2/m\). A dyadic decomposition of the ranges \(A\sqrt m\le |j|\le m\) therefore bounds the number of outer steps by
\[
O\!\left(\frac{\sqrt m}{A}+\log m\right).
\]
Letting first \(m\to\infty\), then \(R\to\infty\) and \(A\to\infty\), gives
\[
g_N\sim 2\sqrt m
\sum_{r=0}^{\infty}\frac{\sqrt{r+1}-\sqrt r}{r+1}.
\]
Since \(N\sim2m\), this is exactly \(g_N\sim C\sqrt N\). The series converges because its summand is asymptotic to \(1/(2r^{3/2})\).

It remains to extract the universal lower constant for \(n(N)\). The source proves that a cycle of \(n\) independent random variables has dominance probability at most
\[
a_n=1-\frac{1}{4\cos^2(\pi/(n+2))}.
\]
Write \(\delta_N=3/4-p_N\). Since a sharp \(N\)-sided cycle of length \(n(N)\) must satisfy \(p_N\le a_{n(N)}\), the identity
\[
\frac34-a_n=\frac14\tan^2\!\left(\frac{\pi}{n+2}\right)
\]
gives the exact lower estimate
\[
n(N)+2\ge
\frac{\pi}{\arctan(2\sqrt{\delta_N})}.
\]
Here \(\delta_N=1/(2N)\) for even \(N\), while \(\delta_N=1/(2N)+1/(4N^2)\) for odd \(N\). Therefore
\[
\liminf_{N\to\infty}\frac{n(N)}{\sqrt N}\ge\frac{\pi}{\sqrt2}.
\]
Finally \(n(N)\le g_N\), because every canonical subcycle is an admissible \(N\)-sided cycle, proving the upper bound by \(C\).

## Verification
The accompanying `verify.py` reconstructs the greedy recurrence from the comparison threshold, checks greedy optimality against dynamic programming for every \(2\le N\le150\), and reproduces the five shortest-canonical-subcycle lengths explicitly reported in the source:
\[
(10,6),\ (100,24),\ (10^4,260),\ (10^6,2628),\ (10^8,26304).
\]
It also evaluates the convergent constant numerically and checks the approach of both even and odd greedy ratios to the stated scale. These finite computations are regression checks only; the limit theorem follows from the band-width and tail estimates above.

## Relationship to prior work
Komisarski proves the sharp dominance probability \(p_N\), introduces \(n(N)\), establishes only square-root-order bounds for it, and gives an explicit shortened canonical subcycle. The paper also reports the shortest canonical-subcycle lengths for \(N=10,100,10^4,10^6,10^8\), including \(26304\) at \(N=10^8\), but it does not state an asymptotic constant for those shortest subcycles. The greedy recurrence above exactly reproduces all five reported values and explains their approach to \(2.630472693388697\ldots\).

Later work on balanced nontransitive triples characterizes attainable rational winning probabilities and possible side counts for three dice. That problem fixes a three-cycle and varies the dice, whereas the present result studies the length needed to attain Komisarski's sharp many-die dominance level, so neither statement implies the other.

## Limitations
The exact constant \(C\) is proved for the shortest order-preserving subcycle of the canonical two-point dice family, not for the unrestricted minimum \(n(N)\). The unrestricted result is the two-sided asymptotic bracket displayed above. Closing the gap between \(\pi/\sqrt2\approx2.22144\) and \(C\approx2.63047\), or proving a limit for \(n(N)/\sqrt N\), remains open here. A differently phrased analysis of the same greedy recurrence outside the searched nontransitive-dice literature remains a residual originality risk.

## References
1. A. Komisarski, *Nontransitive Random Variables and Nontransitive Dice*, The American Mathematical Monthly 128 (2021), 423–434, DOI 10.1080/00029890.2021.1889921. Published online 27 April 2021.
2. D. Kim, R. Kim, W. Lee, Y. Lim, and Y. So, *Balanced Nontransitive Dice: Existence and Probability*, The Electronic Journal of Combinatorics 31 (2024), #P1.21, DOI 10.37236/11918.
