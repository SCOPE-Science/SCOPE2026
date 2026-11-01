# Sharp schedule ordering and logarithmic relaxation for neutral periodic Blaschke compositions

## Finding

A finite neutral product of real quadratic Blaschke maps has an explicit, schedule-sensitive parabolic relaxation law. For every periodic word of length \(m\) with zero boundary Lyapunov exponent, its ordered prefix multipliers determine two positive constants \(B\) and \(C\) such that the Cayley-squared coordinate at completed periods satisfies

\[
Y_n=Bn+\frac{C}{B}\log n+L+O\!\left(\frac{\log n}{n}\right).
\]

At a fixed period starting phase, sorting the map parameters in nondecreasing order **uniquely maximizes both constants**, while nonincreasing order uniquely minimizes them, except for ties between equal parameters. Thus the rate of approach to the common fixed point depends sharply on scheduling even though the one-period linear multiplier is always exactly one.

## Assumptions and scope

For \(0\le a<1\), define the real quadratic Blaschke map

\[
T_a(x)=\left(\frac{x+a}{1+ax}\right)^2,\qquad 0\le x\le1.
\]

Choose an integer \(m\ge1\), an **ordered** word \((a_1,\ldots,a_m)\in[0,1)^m\), and an initial state \(x_0\in[0,1)\). Repeat the word indefinitely:

\[
x_{n+1}=T_{a_{1+(n\bmod m)}}(x_n),\qquad n\ge0.
\]

Write

\[
r_j=\frac{1+a_j}{2(1-a_j)},\quad R_j=\prod_{i=1}^j r_i^2,\quad R_0=1,
\]

and impose the *neutral* condition \(R_m=1\), equivalent to \(\prod_{j=1}^m T_{a_j}'(1)=1\). The time index \(n\) in the following theorem counts **complete periods**, not individual maps. Let

\[
Y_n=\left(\frac{1+x_{mn}}{1-x_{mn}}\right)^2,\quad B=\frac12\sum_{j=1}^m\frac1{R_j},\quad C=\frac1{16}\sum_{j=1}^m\frac1{R_j^2}.
\]

Both constants are strictly positive.

**Theorem.** There is a finite real constant \(L\), depending on the initial point and ordered word, such that for \(n\to\infty\)

\[
Y_n=Bn+\frac{C}{B}\log n+L+O\!\left(\frac{\log n}{n}\right),
\qquad
1-x_{mn}\sim\frac2{\sqrt{Bn}}.
\]

For a fixed multiset satisfying \(R_m=1\), the values of both \(B\) and \(C\) are maximal exactly for nondecreasing order \(a_1\le\cdots\le a_m\) and minimal exactly for nonincreasing order, modulo interchange of equal entries. These inequalities refer to the specified starting phase and period-boundary observations.

**Explicit separation.** Take \(a=1/7\) and \(b=1/2\), so \(r_a=2/3\), \(r_b=3/2\). For each fixed integer \(k\ge1\), the two period-\(2k\) schedules \(a^kb^k\) and \((ab)^k\) both satisfy neutrality, but

\[
B_{a^kb^k}=\frac{13}{10}\left[\left(\frac94\right)^k-1\right],\quad
B_{(ab)^k}=\frac{13k}{8},\quad
\frac{B_{a^kb^k}}{B_{(ab)^k}}=\frac4{5k}\left[\left(\frac94\right)^k-1\right].
\]

The schedule-dependent leading boundary-distance constants therefore separate exponentially as the *fixed* block length \(k\) is increased. This is an asymptotic in completed periods for each fixed \(k\); no joint limit is asserted.

## Proof

**1. Exact conjugate recurrence.** With \(u=(1+x)/(1-x)>0\), the intermediate Möbius map \(v=(x+a)/(1+ax)\) satisfies

\[
\frac{1+v}{1-v}=\frac{1+a}{1-a}\,u=2r(a)u,\quad
r(a)=\frac{1+a}{2(1-a)}.
\]

Since \(T_a(x)=v^2\), its Cayley coordinate becomes

\[
\frac{1+T_a(x)}{1-T_a(x)}=r(a)u+\frac1{4r(a)u}.
\]

Squaring gives the **exact**, not asymptotic, one-step recurrence for \(y=u^2\):

\[
y\longmapsto F_t(y)=ty+\frac12+\frac1{16ty},\qquad t=r(a)^2>0.
\]

In particular, every finite orbit starting in \([0,1)\) remains in that interval and has finite \(y\ge1\).

**2. One-period asymptotic and global growth.** Set \(t_j=r_j^2\). For large input \(y\), the partial composition through step \(j\) admits

\[
y_j=R_jy+A_j+D_j/y+O(y^{-2}),\qquad (A_0,D_0)=(0,0),
\]

with

\[
A_j=t_jA_{j-1}+\frac12,\quad
D_j=t_jD_{j-1}+\frac1{16t_jR_{j-1}}.
\]

These recurrences follow by expanding the exact reciprocal in \(F_{t_j}\). Neutrality \(R_m=1\) yields

\[
G(y):=F_{t_m}\circ\cdots\circ F_{t_1}(y)
=y+B+C/y+O(y^{-2}),
\]

where the formulas above telescope to

\[
A_m=\frac12\sum_{j=1}^mR_j^{-1}=B,\qquad
D_m=\frac1{16}\sum_{j=1}^mR_j^{-2}=C.
\]

More strongly, positivity of the last term in every exact step, propagated through positive factors \(t_j\), gives \(G(y)>y+B\) for every finite \(y>0\). Thus \(Y_n\ge Y_0+nB\), so no separate compactness or local-entry hypothesis is needed: every eligible initial condition tends to the common boundary fixed point.

**3. Logarithmic correction and limiting constant.** The previous bound and the one-period expansion give

\[
Y_{n+1}-Y_n=B+C/Y_n+O(Y_n^{-2}),\qquad
Y_n=Bn+O(\log n).
\]

For \(n\ge1\), put \(Z_n=Y_n-Bn-(C/B)\log n\). A direct difference yields

\[
Z_{n+1}-Z_n
=\frac{C}{Y_n}-\frac{C}{B}\log(1+1/n)+O(n^{-2})
=O\!\left(\frac{\log n}{n^2}\right).
\]

These increments are absolutely summable, proving existence of a finite limit \(L\) and the sharper bound \(Z_n=L+O((\log n)/n)\) by summing the tail. Because \(1-x_{mn}=2/(\sqrt{Y_n}+1)\), the stated square-root boundary law follows.

**4. Sharp reordering.** Fix a multiset of \(t_j\) with product one. Swapping two adjacent values \(p,q\) at positions \(i,i+1\) leaves *every* prefix product \(R_j\) unchanged except \(R_i\); that prefix changes from \(R_{i-1}p\) to \(R_{i-1}q\). If \(p>q\), moving \(q\) first strictly increases both \(R_i^{-1}\) and \(R_i^{-2}\). Hence it strictly increases both \(B\) and \(C\). Iterating adjacent swaps proves that nondecreasing order is the unique maximizing order up to ties, and reversing them gives the unique minimizing order. Since \(r(a)\) increases strictly with \(a\), ordering the \(t_j\) and ordering the \(a_j\) are equivalent.

**5. Separation example.** For \(a=1/7\), \(b=1/2\), the factors \(t_a=4/9\) and \(t_b=9/4\) are reciprocals. Writing \(q=4/9\), the grouped prefix products are \(q,q^2,\ldots,q^k,q^{k-1},\ldots,1\), while the alternating prefix products are \(q,1,q,1,\ldots,q,1\). Summing their reciprocals gives the exact formulas for \(B\). For the four-map case, the grouped coefficients are \(B=169/32\), \(C=9409/4096\), whereas alternating has \(B=13/4\), \(C=97/128\). This confirms different leading and logarithmic coefficients despite identical map counts and unit multipliers.

## Verification

The standalone Python-standard-library program `verify.py` reconstructs the exact change of variables, compares formal one-period coefficients against the reciprocal-prefix formulas, exhaustively compares all six balanced four-step words, checks the two explicit grouped/alternating identities for nine block lengths, and checks numerical stabilization of the logarithm-subtracted remainder. It completed 172 finite checks successfully. The global asymptotic and rearrangement conclusions follow from the analytical proof, not from those finite checks.

## Relationship to prior work

González-Tokman and Oldfield (2026) examine the same real family, up to reflection of the original complex Blaschke map, with random map choices; their Theorem 3.2 classifies stochastic boundary synchronization and critical intermittency. Their Remark 3.8 invokes classical deterministic parabolic behavior. The present theorem treats *fixed periodic neutral words* and supplies exact ordered-prefix growth coefficients, a logarithmic term, a sharp rearrangement theorem, and a block-schedule separation, none stated in the inspected sections of that source. The family is conjugate by \(z\mapsto-z\) to their convention \(-((z-a)/(1-az))^2\).

Jones (1997), especially Section 5.1, establishes classical parabolic iterate power laws; that general phenomenon is not claimed here as new. Evdoridou, Fagella, Rippon, and Stallard (2026) study nonautonomous inner-function mixing and entropy; their Theorems A–E concern mostly *centred* maps and a summable degree-two sequence, not the present critical non-centred periodic composition or its ordering constants. The exact coefficient and sorting claims should still undergo independent historical-priority review, particularly against specialized parabolic-composition and Fatou-coordinate literature.

## Limitations

The statement is for real initial values \(x_0\in[0,1)\), nonnegative parameters \(a_j<1\), exactly periodic schedules, and precisely neutral product. It does not assert convergence for arbitrary complex initial conditions, random iid schedules at zero Lyapunov exponent, nonperiodic words, uniformity as the period length increases, or transient optimality at intermediate phases. Sorting optimizes the *specified phase* of complete-period observations; cyclic shifts can change the coefficient. The arbitrary initial-state constant \(L\) is shown to exist but is not expressed in closed form. Historical priority remains subject to specialist verification.

## References

1. C. González-Tokman and R. Oldfield, *The transition between synchronization and chaos for random Blaschke products*, arXiv:2607.15488v1, first submitted 16 July 2026, https://arxiv.org/abs/2607.15488 . Primary full-text sections inspected: introduction, Section 3, Theorem 3.2, Remark 3.8.
2. V. Evdoridou, N. Fagella, P. Rippon, and G. Stallard, *Non-autonomous dynamics of inner functions: mixing and entropy*, arXiv:2609.31476v2, 15 October 2026, https://arxiv.org/abs/2609.31476 . Primary HTML introduction and Theorems A–E inspected.
3. G. L. Jones, *The exponent of convergence of a finite Blaschke product*, Annales Academiae Scientiarum Fennicae Mathematica 22 (1997), 245–254, especially Section 5.1.
4. N. Haydn and S. Isola, *Parabolic Rational Maps*, Journal of the London Mathematical Society 63 (2001), 673–689, doi:10.1017/S0024610701001958; abstract inspected as background, not a full-text coverage determination.
