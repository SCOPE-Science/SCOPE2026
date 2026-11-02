# Sharp third-order positivity boundary for longest runs in random compositions

## Finding

Choose uniformly among the \(2^{n-1}\) positive integer compositions of \(n\), for each integer \(n\ge1\). Let \(R\) be the number of parts and \(M\) the largest part. Define the conditional mass kernel
\[
K_n(r,m)=\Pr(M=m\mid R=r),\qquad 1\le r,m\le n.
\]
Its rows are ordered by increasing \(r\), and its columns by **decreasing** \(m\). Call a nonnegative matrix \(\mathrm{TN}_3\) if every square minor of orders one, two, and three is nonnegative.

**Theorem.** The complete conditional maximum-part kernel \(K_n\) is \(\mathrm{TN}_3\) if and only if \(1\le n\le9\). For **every** \(n\ge10\) a third-order minor using exactly the three part counts \(r=2,3,4\) and the three consecutive maximum sizes
\[
 m=\lfloor n/2\rfloor+2,\quad \lfloor n/2\rfloor+1,\quad \lfloor n/2\rfloor
\]
is strictly negative. The failure persists for all larger sizes and has different even/odd determinant polynomials.

To state those polynomials, write \(A_n(r,m)\) for the number of compositions with exactly \(r\) parts and maximum exactly \(m\). Each row of \(K_n\) is the corresponding row of \(A_n\) divided by \(\binom{n-1}{r-1}\). For even \(n=2q\), \(q\ge5\), the specified unnormalized minor is
\[
\det\begin{pmatrix}
2&2&1\\
3(q-3)&3(q-2)&3(q-1)\\
2(q-3)(q-4)&2(q-2)(q-3)&2(q-1)(q-2)
\end{pmatrix}
=-6(q^2-5q+2)<0.
\]
For odd \(n=2q+1\), \(q\ge5\), it is
\[
\det\begin{pmatrix}
2&2&0\\
3(q-2)&3(q-1)&3(q-1)\\
2(q-2)(q-3)&2(q-1)(q-2)&2q(q-1)
\end{pmatrix}
=-12(q-4)(q-1)<0.
\]
At the first obstruction \(n=10\), the count minor is
\[
\det\begin{pmatrix}2&2&1\\6&9&12\\4&12&24\end{pmatrix}=-12,
\]
so the corresponding conditional-probability determinant is \(-1/2268\).

## Assumptions and scope

Compositions are **ordered** sequences of positive parts whose sum is \(n\); the sample is uniform over all such sequences. Conditional on \(R=r\), each of the \(\binom{n-1}{r-1}\) compositions has equal mass. Empty/support-zero matrix cells are retained, and minors use strictly increasing row indices and strictly decreasing maximum-size labels. No assertion is made for unequal composition weights, independent component models, or any population sampling regime other than this finite uniform model.

The theorem is **not** a claim that the kernel is totally positive of order two for every \(n\), nor that the whole matrix has a prescribed sign at all orders. It classifies exactly third-order total nonnegativity in the stated orientation.

## Proof

First count bounded compositions. For \(m\ge0\), let \(B_n(r,m)\) count compositions of \(n\) into exactly \(r\) positive parts, each at most \(m\). The empty composition gives \(B_0(0,m)=1\), while \(B_n(0,m)=0\) for \(n>0\). All other impossible indices give zero. Removing the first part yields the exact recurrence
\[
B_n(r,m)=\sum_{t=1}^{\min(n,m)}B_{n-t}(r-1,m),\qquad r\ge1.
\]
Consequently
\[
A_n(r,m)=B_n(r,m)-B_n(r,m-1),
\quad K_n(r,m)=\frac{A_n(r,m)}{\binom{n-1}{r-1}},
\]
and equivalently
\[
B_n(r,m)=[z^{n-r}]\left(1+z+\cdots+z^{m-1}\right)^r.
\]
Positive row scalings preserve all signs of minors, so it suffices to examine \(A_n\).

For the **even infinite family**, let \(n=2q\) and use maximum sizes \(q+2,q+1,q\). For \(r=2\) there are two compositions with maximum \(m>q\), but just one with maximum \(m=q\). For \(r\in\{3,4\}\), two parts of size \(m\ge q\) cannot coexist because all remaining parts are positive. Choosing the position of the unique maximum and composing the residual \(2q-m\) into \(r-1\) positive parts therefore gives
\[
A_{2q}(r,m)=r\binom{2q-m-1}{r-2},\qquad
r=3,4,\quad m\in\{q,q+1,q+2\}.
\]
These counts give exactly the first displayed matrix. A direct three-by-three determinant expansion gives \(-6(q^2-5q+2)\), negative for every integer \(q\ge5\).

For the **odd infinite family**, let \(n=2q+1\). For \(m=q+1,q+2\), the maximum is unique for \(r=2,3,4\), and ordinary residual-composition counting gives the first two columns. At \(m=q\), two parts of size \(q\) are possible for \(r=3\): they leave a final part of size one, giving three additional compositions. The single-maximum configurations number \(3(q-2)\), and hence \(A_{2q+1}(3,q)=3(q-1)\). For \(r=4\), a second part of size \(q\) is impossible, and the same unique-maximum count gives \(2q(q-1)\). For \(r=2\), size \(q\) cannot be the maximum. The second displayed matrix follows and its determinant expands to \(-12(q-4)(q-1)\), strictly negative for \(q\ge5\).

For **\(1\le n\le9\)**, the preceding recurrence reduces the remaining claim to a finite exact list of integer inequalities. Enumerate every \(k\)-element subset of row indices and every \(k\)-element subset of column indices for \(k=1,2,3\); compute the resulting determinant with integer arithmetic. The complete checks, implemented in the accompanying standalone `verify.py`, yield:

| \(n\) | Order-one minors | Order-two minors | Order-three minors | Negative minors |
|---:|---:|---:|---:|---:|
| 1 | 1 | 0 | 0 | 0 |
| 2 | 4 | 1 | 0 | 0 |
| 3 | 9 | 9 | 1 | 0 |
| 4 | 16 | 36 | 16 | 0 |
| 5 | 25 | 100 | 100 | 0 |
| 6 | 36 | 225 | 400 | 0 |
| 7 | 49 | 441 | 1,225 | 0 |
| 8 | 64 | 784 | 3,136 | 0 |
| 9 | 81 | 1,296 | 7,056 | 0 |

These are **all** minors of the indicated orders: the exact number for order \(k\) is \(\binom nk^2\). The checker independently reconstructs the complete matrix by enumerating every cut subset of the \(n-1\) internal gaps before comparing it to the recurrence counts. The finitely many exact integer determinants establish the \(n\le9\) side; the symbolic odd/even formulas establish every \(n\ge10\), completing the proof.

## Verification

Run `python3 verify.py` using Python 3's standard library. The script reproduces the complete \(n\le9\) census by two independent counting methods, checks every minor of orders one through three, and checks both infinite-family formulas against exact enumerative counts for \(10\le n\le300\) as a supplementary arithmetic check. The latter finite test is **not** the proof for all larger \(n\); that proof is the polynomial determinant calculation above. The script was run successfully with 15,702 recorded exact comparisons/inequalities.

## Relationship to prior work

Classical longest-run papers, including Philippou and Makri, provide exact conditional run-length distributions given success counts. Their formulas determine this kernel by changing from successes to cut positions, but the cited paper does not state or evaluate the sharp third-order minor obstruction. Malandro derives bounded-composition generating functions and enumerations; those are foundational to the recurrence, not a new contribution here. Finch studies the part-count/maximum-part covariance in the same uniform-composition model. A published result entitled *Rigorous decorrelation of part count and maximum in uniform compositions* establishes first-order stochastic monotonicity as the number of parts increases; that condition imposes inequalities on cumulative distribution functions but **does not imply third-order nonnegativity** of the point-mass kernel. The contribution here is the explicit even/odd infinite obstruction and the exact boundary at \(n=10\), not a new formula for conditional distributions or a rediscovery of the monotone coupling.

## Limitations

The result concerns only minors of order at most three; it neither proves nor refutes a general order-two likelihood-ratio assertion for arbitrary \(n\). The small-size positive direction is a **finite exhaustive certificate**, not a symbolic classification of every individual minor. The infinite negative direction has a closed algebraic proof. Historical priority is not guaranteed by search or by the absence of a matching title: an older structural total-positivity result may implicitly subsume the theorem. There is no independent audit or formal proof-assistant certification.

## References

1. M. E. Malandro, *Integer compositions with part sizes not exceeding k*, arXiv:1108.0337 (first posted 2011-08-01), https://arxiv.org/abs/1108.0337.
2. A. N. Philippou and F. S. Makri, *Successes, runs and longest runs*, Statistics & Probability Letters 4 (1986), 211–215 (corrected version), https://doi.org/10.1016/0167-7152(86)90069-6.
3. S. Finch, *Covariance within Random Integer Compositions*, arXiv:2010.06643 (2020), https://arxiv.org/abs/2010.06643.
4. *Rigorous decorrelation of part count and maximum in uniform compositions*, publicly available research record, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-rigorous-decorrelation-of-part-count-and-maximum-in-uniform-comp--0ee24a72cd31.
