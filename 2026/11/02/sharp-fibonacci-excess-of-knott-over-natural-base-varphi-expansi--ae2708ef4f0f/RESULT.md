# Sharp Fibonacci excess of Knott over natural base-\(\varphi\) expansions on Lucas intervals

## Finding
Let \(\varphi=(1+\sqrt5)/2\). Write \(K(N)\) for the number of Knott-admissible finite \(\{0,1\}\) expansions of the positive integer \(N\) in powers of \(\varphi\), and \(H(N)\) for the number of natural expansions (the Knott expansions whose rightmost nonzero power agrees with that of the unique Bergman expansion of \(N\)). Let \(F_0=0,F_1=1\), \(F_{n+2}=F_{n+1}+F_n\), and let \(L_n=F_{n-1}+F_{n+1}\) be the Lucas numbers. Set \(\Delta(N)=K(N)-H(N)\).

**Theorem.** For every integer \(j\ge1\),
\[
\min_{L_{2j}\le N\le L_{2j+1}}\Delta(N)=1,\qquad
\max_{L_{2j}\le N\le L_{2j+1}}\Delta(N)=F_{2j+1}.
\]
The minimum occurs only at \(N=L_{2j}\). The maximum is attained at the explicit integer \(N=2F_{2j+1}\), for which
\[
K(2F_{2j+1})=F_{2j+2},\quad
H(2F_{2j+1})=F_{2j},\quad
\Delta(2F_{2j+1})=F_{2j+1}.
\]
For context, the previously known difference is zero throughout the complementary odd Lucas intervals \([L_{2j+1}+1,L_{2j+2}-1]\).

## Assumptions and scope
An expansion is a finite expression \(N=\sum_i a_i\varphi^i\), with \(a_i\in\{0,1\}\) and finitely many nonzero digits, counted after suppressing leading and trailing zeros. A Knott expansion does not terminate in the three-digit suffix \(011\); a natural expansion is a Knott expansion with the same lowest nonzero exponent as the Bergman expansion (the unique expansion with no consecutive 1 digits). The quantities \(K,H\), and the Bergman expansion, follow the definitions and the recurrences in Dekking--van Loon (2023). All \(j\) are positive integers, and the intervals have inclusive integer endpoints. The statement is about differences of two finite expansion counts, not about all untruncated expansions (of which there are infinitely many).

## Proof
**1. The digit gap recurrence.** Let the Bergman expansion of \(N\) have nonzero digits in descending positions \(e_0>e_1>\cdots>e_m\), and put \(s_i=e_{m-i}-e_{m-i+1}-1\), \(1\le i\le m\). Thus \(s_1\) is the rightmost zero-gap, and each \(s_i\ge1\). Theorem 2.3 and Theorem 4.1 of Dekking--van Loon give recurrences for the two counts, using the same transition after the first gap. In particular, if \(s_1\) is odd, their difference \(d_i\) obeys
\[
d_0=0,\quad d_1=1,\qquad
d_i=\begin{cases}
(s_i/2+1)d_{i-1},&s_i\text{ even},\\
((s_i+3)/2)d_{i-1}-d_{i-2},&s_i\text{ odd}
\end{cases}\quad(2\le i\le m).
\]
Then \(\Delta(N)=d_m\). If \(s_1\) is even, both starting counts agree and \(\Delta(N)=0\).

Writing \(u=d_i\) and \(v=d_i-d_{i-1}\), the two types of next gap have **nonnegative** state transitions:
\[
\begin{array}{c|c|c}
\text{gap}&\text{span cost }c=s+1&(u',v')\\\hline
s=2a+1,\ a\ge0&2a+2&((a+1)u+v,\,au+v)\\
s=2a,\ a\ge1&2a+1&((a+1)u,\,au).
\end{array}
\]
The initial state after the first odd gap is \((u,v)=(1,1)\) at even span \(t=s_1+1\ge2\). The span at any stage is the sum of all processed costs; at the final stage it is \(e_0-e_m\).

**2. A universal Fibonacci envelope.** Define coordinatewise upper bounds
\[
P(2k)=(F_{k+1},F_k)\quad(k\ge1),\qquad
P(2k+1)=(2F_k,2F_{k-1})\quad(k\ge2).
\]
For every admissible state obtained after processing gaps of total span \(t\), we have \((u,v)\le P(t)\) coordinatewise. Initially \((1,1)\le P(s_1+1)\). To verify the induction step it suffices, by nonnegativity, to apply each transition to the bounding pair. For an odd gap, the required four coordinate inequalities, according as the old span is even or odd, are
\[
\begin{aligned}
(a+1)F_{k+1}+F_k&\le F_{k+a+2},&
 aF_{k+1}+F_k&\le F_{k+a+1},\\
(a+1)F_k+F_{k-1}&\le F_{k+a+1},&
 aF_k+F_{k-1}&\le F_{k+a}.
\end{aligned}
\]
For an even gap they are
\[
\begin{aligned}
(a+1)F_{k+1}&\le 2F_{k+a},&
 aF_{k+1}&\le2F_{k+a-1},\\
2(a+1)F_k&\le F_{k+a+2},&
 2aF_k&\le F_{k+a+1}.
\end{aligned}
\]
In the first two lines \(k\ge1\) for an even starting span and \(k\ge2\) for an odd starting span; odd-gap inequalities use \(a\ge0\), even-gap inequalities use \(a\ge1\). All eight inequalities follow by checking \(a=0,1,2\) where applicable and then using the fact that successive increments \(F_{r+1}-F_r=F_{r-1}\) are nondecreasing for \(r\ge2\), whereas the left-hand sides are affine in \(a\). Explicitly, at the last necessary base value \(a=2\), each right-hand forward increment is at least the corresponding left-hand slope, by \(F_{k+1}\le2F_k\), \(F_{k+2}\ge2F_k\), and the Fibonacci recurrence. This also verifies the boundary cases \(k=1\) and \(k=2\). Hence the envelope is valid for all spans reachable from an initial even span.

**3. Apply the interval geometry.** For \(L_{2j}\le N\le L_{2j+1}\), the largest Bergman exponent is \(2j\), since \(\varphi^{2j}<L_{2j}\le N<\varphi^{2j+1}\). Proposition 5.1 of Dekking--van Loon establishes that the least Bergman exponent throughout this even Lucas interval is \(-2j\), with \(s_1\) odd. Thus the final span is exactly \(4j\), so the envelope yields
\[
0<\Delta(N)=u\le P(4j)_1=F_{2j+1}.
\]
Every additional gap strictly increases \(u\) from its starting value 1, because \(v\ge1\) is preserved by all transitions. Therefore \(\Delta(N)=1\) is possible only when the Bergman word has exactly two nonzero digits, necessarily at powers \(2j\) and \(-2j\). Their sum is \(L_{2j}\), proving the asserted unique minimum.

**4. The sharp witness.** For \(j\ge1\), consider the no-consecutive-ones digit word with nonzero powers
\[
2j,\quad 2j-2-4h\ (0\le h<j),\quad -2j.
\]
Its value is
\[
\varphi^{2j}+\varphi^{-2j}+
\sum_{h=0}^{j-1}\varphi^{2j-2-4h}
=L_{2j}+F_{2j}=2F_{2j+1}.
\]
Here the middle geometric series equals \(F_{2j}\) by Binet's formula; equivalently, multiply it by \(\varphi^4-1=\sqrt5\varphi^2\). Since \(2F_{2j+1}=L_{2j}+F_{2j}\le L_{2j}+L_{2j-1}=L_{2j+1}\), this integer lies in the stated interval. The uniqueness of the Bergman expansion identifies the displayed word as its Bergman word.

Its gap sequence, read from right to left, is \(1,3,\ldots,3,1\), with \(j-1\) copies of 3. Starting from \((u,v)=(1,1)\), each 3-gap acts by \((u,v)\mapsto(2u+v,u+v)\), giving \((F_{2j},F_{2j-1})\) after \(j-1\) copies. The final 1-gap sends this to \((F_{2j+1},F_{2j-1})\). Thus \(\Delta=F_{2j+1}\), attaining the bound. The individual count recurrences with starting values \((K_0,K_1)=(1,2)\) and \((H_0,H_1)=(1,1)\) give \(K=F_{2j+2}\) and \(H=F_{2j}\) at the same word. This finishes the proof.

## Verification
The standalone dependency-free Python file `checks/verify.py` verifies all eight matrix-transition inequalities for thousands of span/cost pairs, constructs Bergman words by a high-precision greedy comparison with an exact \(\mathbb Z[\varphi]\) coordinate check, computes both published gap recurrences, and exhaustively checks the even Lucas intervals for \(1\le j\le8\). These finite computations check boundary cases and the formulas for 2,213 integers but are **not** substituted for the infinite Fibonacci-envelope proof. Running `python3 checks/verify.py` prints the exact table and `CHECK_OK`.

## Relationship to prior work
Dekking and van Loon (2023), arXiv:2304.11387v1, introduce the Knott/natural distinction and prove their separate gap recurrences (Theorems 2.3 and 4.1) as well as the Lucas-interval digit geometry (Proposition 5.1). They provide Fibonacci/Lucas special-point values but do not state the sharp **difference extremum across every even Lucas interval**. Shallit (arXiv:2305.02672v6, Sections 8--9) builds linear representations for both counts, derives several special-point identities and a mean growth law, but does not state this extremal difference. The present result uses the published recurrences as premises and introduces a universal two-coordinate Fibonacci envelope plus its sharp witness. Earlier work by Dekking and van Loon (arXiv:2111.07544) treats canonical/Bergman digit structures, not the Knott-minus-natural extremal statistic.

## Limitations
This theorem gives exact minimum and maximum differences on the specified intervals, not the full value distribution or the complete set of maximum-attaining integers. No claim is made about the optimality of any exponent outside these intervals, general nonbinary digit alphabets, or bibliographic priority beyond the inspected material. The arithmetic checker is a finite cross-check and the result has not undergone independent mathematical validation.

## References
1. M. Dekking and A. van Loon, *Counting base phi representations*, arXiv:2304.11387v1 (first public 2023-04-22), Theorems 2.3, 4.1 and Proposition 5.1, https://arxiv.org/pdf/2304.11387.
2. J. Shallit, *Proving Properties of phi-Representations with the Walnut Theorem-Prover*, arXiv:2305.02672v6 (2024-09-06), Sections 8--9, https://arxiv.org/pdf/2305.02672.
3. M. Dekking and A. van Loon, *On the representation of the natural numbers by powers of the golden mean*, arXiv:2111.07544v1 (2021-11-15), Section 5, https://arxiv.org/abs/2111.07544.
