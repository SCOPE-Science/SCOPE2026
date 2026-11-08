# A cubic-time reversal of fixed-point and two-cycle dependence in a random transposition shuffle

## Finding
Start with the identity permutation on \(n\ge6\) letters. At each discrete step independently select an ordered pair of letters uniformly from \(\{1,\ldots,n\}^2\) and exchange them; selecting the same letter twice does nothing. Write \(X_t\) and \(Y_t\) for the numbers of fixed points and disjoint two-cycles at step \(t\ge0\).

Define
\[
\begin{aligned}
 a&=n-1,&b&=\frac{n(n-3)}2,&c&=\frac{(n-1)(n-2)}2,\\
 d&=\frac{n(n-1)(n-5)}6,&e&=\frac{(n-1)(n-2)(n-3)}6,\\
 p&=(1-2/n)^3,&q&=(1-2/n)(1-4/n),\\
 r&=1-6/n+12/n^2,&s&=1-6/n.
\end{aligned}
\]
For every integer \(t\ge0\), with \(0^0=1\) if needed,
\[
\operatorname{Cov}(X_t,Y_t)=\frac12\left(dr^t-es^t-abp^t+acq^t\right).
\]
At \(t=0\) the covariance is zero, and at \(t=1\) it equals \(-2(n-1)/n^2<0\). For each \(n\ge6\), the integer-time covariance has exactly one negative-to-positive transition: there is a finite integer \(T_n\ge2\) such that it is nonpositive for \(1\le t<T_n\), strictly positive for \(t\ge T_n\), and at most one integer time \(t\ge1\) has zero covariance. Moreover,
\[
\lim_{n\to\infty}\frac{T_n}{n^3}=\frac{\log3}{8}.
\]
The strict inequality before the transition is not asserted at a possible isolated zero; the theorem determines the sign change and possible boundary equality.

## Assumptions and scope
The same ordered-pair-with-replacement shuffle is used at every step; this is not the non-lazy transposition-only chain or its continuous-time Poissonization. Labels are distinct and the process begins at the identity. \(X_t\) and \(Y_t\) count cycles of lengths one and two, not adjacent patterns. The theorem covers all integers \(n\ge6\) and \(t\ge0\), with an asymptotic statement as \(n\to\infty\).

## Proof
Let \(\chi_\lambda\) denote the irreducible character of the symmetric group indexed by the partition \(\lambda\) of \(n\). Standard permutation representations and the Pieri and Murnaghan--Nakayama rules give the class-function identities
\[
\begin{aligned}
X&=\chi_{(n)}+\chi_{(n-1,1)},\\
2Y&=\chi_{(n)}+\chi_{(n-2,2)}-\chi_{(n-2,1,1)},\\
2XY&=\chi_{(n)}+\chi_{(n-2,2)}-\chi_{(n-2,1,1)}
 +\chi_{(n-1,1)}+\chi_{(n-3,3)}-\chi_{(n-3,1,1,1)}.
\end{aligned}
\]
For completeness, the Frobenius characteristic of the fixed-point class function is \(s_{(n-1)}s_{(1)}\), that of twice the two-cycle count is \(s_{(n-2)}p_2\), and that of twice their product is \(s_{(n-3)}s_{(1)}p_2\). Here \(p_2=s_{(2)}-s_{(1,1)}\); applying the horizontal and vertical Pieri rules proves all three displays, including the cancellation of intermediate partitions in the last identity.

For a central random walk, character expectation is its dimension times the corresponding eigenvalue raised to time \(t\). Under the present shuffle the eigenvalue for \(\lambda\) is
\[
\theta_\lambda=\frac{n+2\sum_{(i,j)\in\lambda}(j-i)}{n^2}.
\]
The dimensions for the five nontrivial partitions displayed above, in order \((n-1,1),(n-2,2),(n-2,1,1),(n-3,3),(n-3,1,1,1)\), are \(a,b,c,d,e\). Their eigenvalues are respectively \(1-2/n\), \((1-2/n)^2\), \(1-4/n\), \(r\), and \(s\). Consequently
\[
\begin{aligned}
\mathbb EX_t&=1+a(1-2/n)^t,\\
2\mathbb EY_t&=1+b(1-2/n)^{2t}-c(1-4/n)^t,\\
2\mathbb E(X_tY_t)&=1+b(1-2/n)^{2t}-c(1-4/n)^t
+a(1-2/n)^t+dr^t-es^t.
\end{aligned}
\]
Subtracting the product of means proves the covariance formula; the cancellation of the linear terms leaves \(p=(1-2/n)^3\) and \(q=(1-2/n)(1-4/n)\).

Set \(F_t=2\operatorname{Cov}(X_t,Y_t)\). Direct substitution gives \(F_0=0\), \(F_1=-4(n-1)/n^2\), and the strict ordering \(0\le s<q<p<r<1\). Put \(R=r/p>1\), \(Q=q/p\in(0,1)\), \(S=s/p\in[0,Q)\), and \(g_t=F_t/p^t\). For real \(u\ge1\), extend the formula for \(g_u\) by real powers and form
\[
h(u)=\frac{g_{u+1}-g_u}{Q^u}
=d(R-1)(R/Q)^u-ac(1-Q)+e(1-S)(S/Q)^u.
\]
For \(n=6\), the last term is zero and \(h\) is strictly increasing; for \(n\ge7\), it is a strictly convex sum of two positive exponential functions minus a constant. In all cases \(h(u)\to+\infty\), while
\[
F_2-pF_1=-\frac{4(n-1)}{n^5}
(5n^3-30n^2+52n-16)<0,
\]
so \(h(1)<0\). The last polynomial is \(5(n-6)^3+60(n-6)^2+232(n-6)+296>0\). Convexity (or monotonicity at \(n=6\)) therefore shows that \(h\) changes from negative to positive exactly once on \([1,\infty)\). The sequence \(g_t\) first decreases and then increases. Because \(g_1<0\) and \(g_t\sim dR^t\to+\infty\), the sequence crosses zero exactly once, with at most one equality at an integer. This proves the sign classification.

Finally, for fixed \(v>0\) and \(t=\lfloor vn^3\rfloor\),
\[
\frac{F_t}{n^3p^t}=\frac d{n^3}(r/p)^t-\frac{ab}{n^3}
+\frac{ac}{n^3}(q/p)^t-\frac e{n^3}(s/p)^t
\longrightarrow \frac{e^{8v}}6-\frac12.
\]
Indeed \(r/p=1+8/(n^3p)\), the two lower-ratio powers tend to zero exponentially in \(n\), and the dimension ratios tend to \(1/6\) and \(1/2\). The unique sign transition is therefore squeezed between any two cubic times with constants on opposite sides of \((\log3)/8\), establishing the claimed limit.

## Verification
Run `python3 verify.py` using Python 3 standard libraries. Its direct rational Markov-chain enumeration for \(n=6\) at times \(0,\ldots,5\) and \(n=7\) at times \(0,\ldots,3\) agrees exactly with the four-mode covariance identity. Exact rational arithmetic checks mode ordering, the time-one and forward-difference identities, and integer sign transitions for \(n=6,7,8,9,10\), with first positive times respectively \(19,29,45,66,93\). These finite checks are supplementary to the all-size proof.

## Relationship to prior work
The random-transposition walk and its mixing scale were developed by Diaconis and Shahshahani; Berestycki studied giant-cycle phase transitions, and Arcona established character expansions and single-cycle-count mixing results. The argument here combines a mixed class-function expansion with exact comparison of four spectral modes. In the examined material, the particular fixed-point/two-cycle covariance and its single late sign reversal on the cubic time scale were not stated. The general character-theoretic machinery predates this calculation and can generate related mixed moments; unlocated equivalent formulations remain a priority risk.

## Limitations
The effect occurs far beyond the usual \(n\log n\) mixing scale, when the unnormalized covariance is extremely small. It concerns only the specified lazy walk and the first two cycle counts; it does not establish a similar sign profile for other cycle lengths, initial states, or shuffle kernels. No claim of experimental measurability or historical priority beyond the documented source comparisons is made.

## References
- P. Diaconis and M. Shahshahani, *Generating a Random Permutation with Random Transpositions*, Stanford technical report, April 1980; *Z. Wahrscheinlichkeitstheorie verw. Gebiete* 57 (1981), 159–179, doi:10.1007/BF00535487.
- N. Berestycki, *Emergence of giant cycles and slowdown transition in random transpositions and k-cycles*, arXiv:1004.3530, initially submitted 2010-04-20.
- D. Arcona, *Representation Theory and Cycle Statistics for Random Walks on the Symmetric Group*, *Electronic Journal of Combinatorics* 33 (2026), P3.86, doi:10.37236/15089; arXiv:2512.13969.
