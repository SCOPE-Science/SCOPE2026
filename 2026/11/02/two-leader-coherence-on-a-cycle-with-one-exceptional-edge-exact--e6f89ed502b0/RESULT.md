# Two-leader coherence on a cycle with one exceptional edge: exact location rule and sharp strong-link transition

## Finding

Let \(n\ge3\) be an integer. Give the consecutive edges \(\{i,i+1\}\), \(1\le i<n\), of the cycle \(C_n\) unit conductance and give its closing edge \(\{1,n\}\) conductance \(1/x\), where \(x>0\) is the exceptional edge's resistance. Select exactly two distinct noise-free leaders \(a<b\). For the weighted Laplacian \(L_G\) and follower set \(F=\{1,\ldots,n\}\setminus\{a,b\}\), minimize the total grounded coherence
\[
J(a,b)=\operatorname{tr}\big((L_G)_{FF}^{-1}\big).
\]
Put \(\ell=b-a\), \(m=n-\ell\), \(A=a-1\), and \(B=n-b\); thus \(A+B=m-1\). The **exact objective for every pair** is
\[
\boxed{J(a,b)=\frac{\ell^2+m^2-2}{6}
+\frac{(x-1)\big((m-1)(2m-1)-6AB\big)}{6(m-1+x)}.}
\tag{1}
\]
All global minimizers are classified as follows.

**Strong exceptional link, \(0<x<1\).** Let \(k=\lfloor n/2\rfloor\). The *only* optimal unordered leader pairs are
\[
\boxed{\{1,1+k\}\quad\text{and}\quad\{n-k,n\}.}
\tag{2}
\]
Their common optimal value, with \(m=n-k\), is
\[
\boxed{J_* = \frac{k^2-1}{6}+
\frac{m(m-1)(m-2+3x)}{6(m-1+x)}.}
\tag{3}
\]
The two displayed pairs are distinct for every \(n\ge3\).

**Uniform cycle, \(x=1\).** Precisely the pairs having \(b-a\in\{\lfloor n/2\rfloor,\lceil n/2\rceil\}\) are optimal. In other words, the two circular arcs have edge counts as equal as possible.

**Weak exceptional link, \(x>1\).** For each integer \(1\le\ell\le n-1\), put \(m=n-\ell\), \(t=m-1\), and
\[
\boxed{H_{n,x}(\ell)=\frac{\ell^2+m^2-2}{6}
+\frac{(x-1)\big(t(2m-1)-6\lfloor t^2/4\rfloor\big)}{6(t+x)}.}
\tag{4}
\]
Find **all** integer minimizers \(\ell\) of this explicit \(n-1\)-entry list. For each such \(\ell\), take every
\[
\boxed{A\in\{\lfloor t/2\rfloor,\lceil t/2\rceil\},\qquad
(a,b)=(A+1,A+1+\ell).}
\tag{5}
\]
These and only these are the globally optimal leader pairs, with minimum equal to \(\min_{1\le\ell<n}H_{n,x}(\ell)\). All ties are retained, including parity ties and isolated price-transition ties. The entire classification for \(x>1\) uses \(O(n)\) rational-function evaluations and \(O(1)\) additional workspace; it requires no matrix inversions or combinatorial search over pairs.

There is a sharp location transition at the unit-conductance point: for a stronger closing edge, optimal leaders are incident to that edge and balanced along the ordinary path; for a weaker closing edge, for every fixed separation they are centered as evenly as possible about the exceptional edge's complementary arc. For example, with \(n=8\), resistance \(x=2\) gives pairs \(\{2,6\}\) and \(\{3,7\}\), whereas \(x=5\) gives only \(\{2,7\}\).

## Assumptions and scope

The vertex set is \(\{1,\ldots,n\}\). There are no other edges, edge conductances are positive, and both leaders are pinned noiselessly. Follower dynamics can be \(d z_F=- (L_G)_{FF}z_F\,dt+dW_F\) with independent unit-covariance Brownian noise, for which total stationary variance is \(J(a,b)/2\). Multiplying the objective by a common positive factor does not change its minimizers. A grounding inverse exists because each follower component meets at least one pinned leader. This is **not** a claim about noisy leaders, switching leader sets, arbitrary edge weights, or a different performance metric.

## Proof

**Step 1: Dirichlet Green diagonals.** Consider a resistive chain between two pinned endpoints. Let the total resistance be \(T>0\), and let the resistance from the first endpoint to an interior vertex be \(s\). The unique piecewise-affine Green solution to unit current injection at that vertex has the diagonal value \(s(T-s)/T\), equivalently the parallel combination of its two resistance-to-ground paths. Thus the trace of the inverse grounded Laplacian on that chain is the sum of \(s(T-s)/T\) over its interior vertices.

**Step 2: Split the cycle at the two leaders.** The ordinary arc from \(a\) to \(b\) has \(\ell\) unit-resistance edges. Its contribution is
\[
\frac1\ell\sum_{j=1}^{\ell-1}j(\ell-j)=\frac{\ell^2-1}{6}.
\]
The complementary arc from \(b\) through \(n\), the exceptional edge, and then \(1\) to \(a\) contains \(B=n-b\) unit edges before the exceptional edge and \(A=a-1\) unit edges after it. Its total resistance is \(T=A+B+x=m-1+x\). Its interior cumulative resistances, read from \(b\), are \(j\) for \(1\le j\le B\) and \(B+x+h\) for \(0\le h<A\). Therefore its Green trace is exactly
\[
\sum_{j=1}^{B}\frac{j(T-j)}{T}
+\sum_{h=0}^{A-1}\frac{(B+x+h)(T-B-x-h)}{T}.
\]
Using the elementary sums of consecutive integers and squares gives
\[
\frac{m^2-1}{6}+
\frac{(x-1)\big((m-1)(2m-1)-6AB\big)}{6(m-1+x)}.
\]
Adding the ordinary arc proves (1), including the adjacent-leader boundary \(m=1\).

**Step 3: Optimize position for a fixed separation.** For fixed \(\ell\), \(m\) and \(A+B=m-1\) are fixed. In (1) only the product \(AB\) varies with location. If \(x<1\), its coefficient is positive, and minimizing the objective forces \(AB=0\), so \(A=0\) or \(B=0\). If \(x>1\), its coefficient is negative, and minimizing forces \(AB=\lfloor(m-1)^2/4\rfloor\), realized only by the two floor/ceiling splits. If \(x=1\), location is irrelevant at fixed \(\ell\). Thus (4)–(5) and the uniform-cycle classification follow immediately after minimizing the remaining scalar \(\ell\).

**Step 4: Optimize the separation in the strong-link regime.** For \(0<x<1\), substitution \(AB=0\) into (1) gives the real-variable extension
\[
Q_{n,x}(\ell)=\frac{\ell^2+(n-\ell)^2-2}{6}
+\frac{(x-1)(n-\ell-1)(2n-2\ell-1)}{6(n-\ell-1+x)}
\]
for \(1\le\ell\le n-1\). Its second derivative is
\[
Q_{n,x}''(\ell)=\frac23+
\frac{(x-1)x(2x-1)}{3(n-\ell-1+x)^3}>0.
\]
Indeed the second term is nonnegative if \(x\le1/2\); if \(1/2<x<1\), its absolute value is strictly less than \(1/3\), since \(n-\ell-1+x\ge x\) and \((1-x)(2x-1)<x^2\).

For \(n=2k\) (\(k\ge2\)), direct subtraction gives
\[
Q(k)-Q(k-1)=
-\frac{x(2k^2+4kx-2k+x-1)}{6(k+x)(k+x-1)}<0.
\]
Also \(Q(k+1)-Q(k)>0\): after multiplying by the positive denominator \(6(k+x-2)(k+x-1)\), its negative is the quadratic
\[
E_k(x)=2k^2x-4k^2+4kx^2-14kx+12k-7x^2+15x-8.
\]
This polynomial is convex on \([0,1]\), with \(E_k(0)=-4(k-1)(k-2)\le0\) and \(E_k(1)=-2k(k-1)<0\), so \(E_k(x)<0\) throughout \(0<x<1\).

For \(n=2k+1\), \(Q(k+1)-Q(k)=(1-x)(2k^2+4kx-2k-x)/[6(k+x)(k+x-1)]>0\). If \(k\ge2\), the other neighbor difference is
\[
Q(k)-Q(k-1)=-\frac{2k^2x+2k^2+4kx^2+6kx+2k+7x^2+x}{6(k+x)(k+x+1)}<0;
\]
for \(k=1\), there is no smaller feasible separation. Strict convexity then makes \(\ell=\lfloor n/2\rfloor\) the sole minimizing integer. The fixed-separation equality condition from Step 3 gives precisely the two pairs in (2). The terminal Green trace with \(AB=0\) simplifies to \(m(m-1)(m-2+3x)/(6(m-1+x))\), proving (3).

Every equality condition has been included. This proves all regimes for every finite \(n\ge3\) and real \(x>0\).

## Verification

Run `python3 verify.py` from the directory containing the standalone verification files. The program forms each weighted cycle's full Laplacian, deletes the selected leader rows/columns, exactly inverts the rational follower matrix by Gauss–Jordan elimination, and directly compares the resulting trace with (1). It also exhaustively compares all pairs against the reduced candidates and tests (2). The included `verify_output.txt` records **1,476** exact grounded inverse comparisons, **72** global candidate classifications, and **32** strong-link closed-form classifications, all passing. This finite check is corroboration, not the proof for arbitrary real \(x\) or unbounded \(n\).

## Relationship to prior work

Fitch and Leonard (2014), especially Sections V-C/V-D and Appendices B/C, give optimal *unweighted* cycle and path leader locations and a broader joint-centrality viewpoint. Patterson, McGlohon and Dyagilev (2014, expanded 2016) give exact polynomial-time algorithms for *arbitrarily weighted* paths and rings using a minimum-weight-path construction, with \(O(kn^3)\) complexity for \(k\)-leader ring coherence. Those results include the present special graphs as inputs but do not state the all-parameter strong-edge endpoint theorem, the strict fixed-separation reflection transition, or the explicit \(O(n)\) scalar location classification. The source's general algorithm establishes numerical computability rather than these additional structural implications. The uniform-cycle and path-break limiting cases are established prior endpoints, not claimed as new.

## Limitations

The scope is exactly two noise-free leaders and a single exceptional cycle edge. For weaker exceptional links, the answer is an explicit length-\(n-1\) scalar argmin rather than a universal simple closed expression for the best separation; isolated ties in that list must be retained. No claim of absolute historical priority or independent audit is made. There may be specialized literature expressing an equivalent one-defect classification not encountered in the inspected sources. The optional stationary-variance interpretation presumes independent unit-intensity follower noise.

## References

1. K. E. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569, first posted July 7, 2014. https://arxiv.org/abs/1407.1569
2. S. Patterson, N. McGlohon, and K. Dyagilev, *Efficient, Optimal k-Leader Selection for Coherent, One-Dimensional Formations*, arXiv:1412.6595, first posted December 20, 2014. https://arxiv.org/abs/1412.6595
3. S. Patterson, N. McGlohon, and K. Dyagilev, *Optimal k-Leader Selection for Coherence and Convergence Rate in One-Dimensional Networks*, arXiv:1604.07094, first posted April 24, 2016. https://arxiv.org/abs/1604.07094
