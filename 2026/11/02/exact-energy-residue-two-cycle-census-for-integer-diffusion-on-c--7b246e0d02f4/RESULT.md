# Exact energy-residue two-cycle census for integer diffusion on cliques

## Finding

For each integer \(n\ge2\), consider labelled vertices \(1,\ldots,n\) of the simple complete graph \(K_n\), with integer heights \(x_i\) evolving synchronously by
\[
F(x)_i=x_i+\sum_{j\ne i}\operatorname{sgn}(x_j-x_i),\qquad \operatorname{sgn}(0)=0.
\]
The conserved total is \(S=\sum_i x_i\). Let \(A_{n,r}\), for \(r\in\{0,\ldots,n-1\}\), be the following explicit finite integer. Sum over every positive composition \((m_1,\ldots,m_k)\) of \(n\), and write \(M_j=m_1+\cdots+m_j\):
\[
A_{n,r}=\sum_{\substack{k\ge1,\ m_1+\cdots+m_k=n\\m_j\ge1}}
\frac{n!}{\prod_{j=1}^{k}m_j!}
\sum_{\substack{1\le g_j\le m_j+m_{j+1}-1\ (1\le j<k)\\
\sum_{j=1}^{k-1}(n-M_j)g_j\equiv r\pmod n}}1.
\]
For \(k=1\), the inner sum is one when \(r=0\) and zero otherwise. At every integer total \(S\), the number of distinct primitive temporal two-cycle orbits is **exactly**
\[
\boxed{C_n(S)=\frac{A_{n,S\bmod n}-\mathbf 1_{n\mid S}}{2}.}
\]
There is one fixed configuration when \(n\mid S\) and none otherwise. Every periodic orbit has primitive period one or two. Consequently the complete periodic-state count in an integer energy shell depends only on \(S\bmod n\), rather than on the magnitude of \(S\).

The recurrent states also have a sharp geometric boundary. For every \(n\ge4\),
\[
\max_i x_i-\min_i x_i\le2n-4
\]
for every periodic state; equality holds precisely when the ordered height classes have multiplicities \((1,n-2,1)\) and both successive height gaps equal \(n-2\). Such extreme states exist only for \(n\mid S\), where exactly \(n(n-1)\) different primitive two-cycles have a maximal-spread phase. In the other phase of each such orbit the spread is exactly two.

For illustration, the periodic-state counts \((A_{5,0},\ldots,A_{5,4})\) are \((401,370,300,300,370)\). The corresponding two-cycle orbit counts are \((200,185,150,150,185)\). This is an exact energy-residue dependence, not a numerical approximation.

## Assumptions and scope

All vertices are labelled; distinct label assignments count as distinct states. The state space is \(\mathbb Z^n\), with negative heights allowed, as in the integer-valued diffusion process. The graph has no loops and all updates are simultaneous. One temporal two-cycle is counted once, not once per phase. This is *not* conventional degree-threshold parallel chip firing, where a vertex fires according to its own degree. The theorem counts states already periodic at the specified conserved total; it does not enumerate their attraction basins or transient lengths.

## Proof

**1. Conservation and comparison ordering.** Pairwise contributions to \(\sum_i F(x)_i\) cancel, so total \(S\) is conserved. Put \(d_i(x)=F(x)_i-x_i\). If \(x_i<x_j\), then \(d_i(x)>d_j(x)\): their mutual contribution gives a difference of two, and each other vertex contributes a nonnegative difference. If \(x_i=x_j\), then \(d_i(x)=d_j(x)\). Thus equal-height vertices remain equal after every update, and the displacement is strictly decreasing across distinct ordered height classes.

If \(F^2(x)=x\), write \(y=F(x)\). Since \(d(y)=-d(x)\), an initially strict inequality \(x_i<x_j\) implies \(d_i(y)<d_j(y)\), hence \(y_i>y_j\). Conversely, if all unequal pairs reverse their strict order in one update (and initially equal pairs remain equal), every pair's sign in the update sum reverses, so \(d(y)=-d(x)\) and \(F^2(x)=x\). Therefore the exact condition for immediate period dividing two is strict reversal of every unequal pair.

**2. No longer periodic orbit.** For any consecutive states \(x,y=F(x),z=F(y)\), define the two-time potential \(P(x)=\sum_i x_i F(x)_i\). Pairwise cancellation gives
\[
P(y)-P(x)=-\sum_{i<j}(y_i-y_j)
\bigl(\operatorname{sgn}(x_i-x_j)+\operatorname{sgn}(y_i-y_j)\bigr)\le0.
\]
Each summand is nonpositive separately. Along a periodic orbit the potential must be constant, so each term is zero. An unequal pair cannot merge permanently during a periodic orbit, because identical heights on a clique remain identical forever. Thus every strict pair must reverse its sign at each step; Step 1 gives \(F^2(x)=x\). The only fixed states are constant vectors: a nonconstant vector has two distinct heights and their displacements cannot both be zero. This reconstructs the relevant finite-graph potential argument independently of any numerical experiment.

**3. Exact bounded-gap parametrization.** Give a state \(k\) increasing distinct heights \(h_1<\cdots<h_k\), occurring with multiplicities \(m_1,\ldots,m_k\). Put \(M_0=0\) and \(M_j=\sum_{i=1}^j m_i\). Each vertex in class \(j\) moves by
\[
d_j=(n-M_j)-M_{j-1}.
\]
Hence \(d_{j+1}-d_j=-(m_j+m_{j+1})\). Writing the positive adjacent gaps as \(g_j=h_{j+1}-h_j\), the updated adjacent gap is \(g_j-(m_j+m_{j+1})\). The strict-reversal criterion from Step 1 is equivalent to
\[
1\le g_j\le m_j+m_{j+1}-1\qquad(1\le j<k).
\]
These inequalities characterize *all* states with \(F^2(x)=x\), including the one-class constant states.

**4. Counting at fixed total.** For fixed \((m_1,\ldots,m_k)\) and gaps \((g_1,\ldots,g_{k-1})\), the initial height \(h_1\) must satisfy
\[
S=nh_1+\sum_{j=1}^{k-1}(n-M_j)g_j.
\]
There is precisely one integer choice of \(h_1\) if the displayed gap sum is congruent to \(S\) modulo \(n\), and no choice otherwise. The numbers of labelled class assignments are \(n!/\prod m_j!\), with no overcounting because ordered height classes are unique. Summing proves the formula for \(A_{n,S\bmod n}\). Exactly one state is fixed when \(n\mid S\). All other periodic states pair into disjoint two-cycles, which proves the division by two and integrality of \(C_n(S)\).

**5. Sharp spread and extreme cycles.** If \(k\ge2\), the spread satisfies
\[
\sum_{j<k}g_j\le \sum_{j<k}(m_j+m_{j+1}-1)
=2n-m_1-m_k-k+1.
\]
For \(k=2\), this is at most \(n-1\). For \(k\ge3\), it is at most \(2n-4\), with equality only at \(k=3\), \(m_1=m_3=1\) and both gaps at their maximum. For \(n\ge4\), the \(k=2\) bound is strictly smaller, so this characterizes equality. The corresponding heights are \((h,h+n-2,h+2n-4)\), and their total is \(n(h+n-2)\), necessarily divisible by \(n\). Choosing the unique bottom and top vertices yields exactly \(n(n-1)\) such states for each integer \(S\) divisible by \(n\). Their updated values are \((h+n-1,h+n-2,h+n-3)\) on these three classes, with spread two. Since \(n\ge4\), the second phase is never another maximal-spread state. Hence the \(n(n-1)\) extreme states lie on \(n(n-1)\) distinct primitive two-cycles. This proves the asserted sharp boundary and its exact orbit multiplicity.

## Verification

The embedded standalone `verify.py` directly applies the original vertexwise sign-comparison rule twice to each sorted normalized integer profile of spread at most \(2n-4\) (spread at most one for \(n=2\)), multiplying by its labelled multiplicity. This is independent of the composition-gap enumeration routine. Every normalized profile was examined for \(2\le n\le9\): exactly 379,706 profiles, including nonperiodic ones. An additional 324,504 normalized profiles with spread outside the asserted recurrence bound were tested for sizes \(2\le n\le7\), with none periodic. For every residue class in each tested clique size it agreed with the formula, and for \(4\le n\le9\) it also checked the exact number of extreme states. Explicit extremal two-step orbits were checked through \(n=29\), giving 26 additional witnesses. Run `python3 verify.py`; the embedded `verification_output.txt` records `CLIQUES_DIFFUSION_EXACT_CENSUS_VERIFIED`. These finite computations corroborate but are not used to promote any infinite statement: Steps 1–5 prove the theorem for all \(n\).

## Relationship to prior work

Duffy, Lidbetter, Messinger and Nowakowski introduced the diffusion game and established an abstract necessary-and-sufficient two-step order-reversal condition (“property plus”) and special two-level complete-graph cases. We claim no priority for the underlying update rule, that reversal principle, or eventual two-periodicity. Long and Narayanan subsequently proved eventual period at most two on arbitrary finite graphs using a two-time potential; the potential mechanism is explicitly acknowledged in Step 2. The new quantitative target is the **exact number of labelled temporal two-cycles at each conserved integer total on every clique size**, together with the sharp recurrent-spread boundary and its energy-restricted extreme-orbit count. These counts are not a restatement of a period bound or of ordinary parallel degree-threshold chip firing.

## Limitations

The exact sums may be computationally expensive for large \(n\); no asymptotic formula is asserted. The theorem does not count transient starting states, transient times, or nonnegative states at small conserved total. The state space is the integer diffusion game, so intermediate and recurrent coordinates may be negative. Earlier abstract order-reversal theory is a crucial starting point, and inaccessible or unindexed older enumeration sources could contain an equivalent formula. The verification is an independent computational implementation, not independent peer review.

## References

1. C. Duffy, T. F. Lidbetter, M. E. Messinger, and R. J. Nowakowski, *A Variation on Chip-Firing: the Diffusion Game*, arXiv:1609.05792, publicly posted 2016-09-19; particularly Theorems 3.1 and 3.7.
2. J. Long and B. Narayanan, *Diffusion on Graphs Is Eventually Periodic*, arXiv:1704.04295, publicly posted 2017-04-13; the two-time potential argument. This is subsequent supporting literature rather than the source establishing the original update rule.
3. T.-Y. Jiang, *On the Period Lengths of the Parallel Chip-Firing Game*, arXiv:1003.0943, publicly posted 2010-03-04; contextual comparison with the distinct degree-threshold parallel firing rule.
