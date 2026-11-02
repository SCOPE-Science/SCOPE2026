# The one-third rule for the largest Bernoulli disjoint-occurrence gap

## Finding

Let \(n\ge1\) be an integer. Let \(S_n\) count the ones among \(n\) independent fair bits, and let \(H_{n,k}=\{S_n\ge k\}\) for integer \(0\le k\le n\). In the usual witness definition of disjoint occurrence, define the BK gap
\[
G_n(k)=\Pr(H_{n,k})^2-\Pr(H_{n,k}\circ H_{n,k}).
\]
**Theorem.** For every \(n\ge1\), the map \(k\mapsto G_n(k)\) has the unique maximizer
\[
\boxed{k_n^*=\left\lceil\frac n3\right\rceil.}
\]
In particular its exact maximum is
\[
\boxed{G_n(k_n^*)=\Pr(S_n\ge k_n^*)^2-\Pr(S_n\ge2k_n^*).}
\]
The deficit of this largest BK gap also has the exact exponential rate
\[
\boxed{\lim_{n\to\infty}-\frac1n\log\bigl(1-G_n(k_n^*)\bigr)
=D(1/3\|1/2)=\frac53\log2-\log3.}
\]
Here \(D\) denotes binary relative entropy, and the logarithm is natural.

## Assumptions and scope

The cube has \(n\) independent, identically distributed Bernoulli-\(1/2\) coordinates. The two events in the BK inequality are identical increasing *Hamming-weight threshold* events. A witness fixes enough one-coordinates to force the threshold event regardless of unobserved coordinates. The maximum is over *all integer threshold values* \(0\le k\le n\), not arbitrary increasing events. The case \(n=1\) is included, with \(k=1\).

## Proof

**1. Exact gap and difference.** For \(1\le k\le n\), two disjoint witnesses of \(H_{n,k}\) exist exactly when there are at least \(2k\) one-coordinates. Hence
\[
G_n(k)=a_k^2-a_{2k},\qquad a_j=\Pr(S_n\ge j),
\]
where \(a_j=0\) for \(j>n\). For the empty threshold, \(G_n(0)=0\). Write \(b_j=\Pr(S_n=j)\) and set \(b_j=0\) outside \(0\le j\le n\). Since \(a_{k+1}=a_k-b_k\), exact subtraction yields
\[
G_n(k+1)-G_n(k)=b_{2k}+b_{2k+1}-b_k(a_k+a_{k+1}).\tag{1}
\]
Every \(b_k\) in the working range \(0\le k\le n\) is strictly positive.

**2. Strict increase before one third.** Take \(1\le k<k_*:=\lceil n/3\rceil\). Then \(3k+1\le n\). Symmetry and unimodality of the fair binomial mass sequence imply \(b_{2k}\ge b_k\) and \(b_{2k+1}\ge b_k\). Because \(a_k+a_{k+1}<2\), (1) is strictly positive. At \(k=0\), (1) equals \(b_0(n-1+b_0)>0\), since \(b_1=nb_0\) and \(a_0+a_1=2-b_0\). Thus all steps before \(k_*\) increase strictly.

**3. The first decreasing step.** Put \(F_n(k)=a_k+a_{k+1}\). For \(k\le\lfloor n/2\rfloor\), fair-binomial symmetry gives \(F_n(k)\ge1\). Also put
\[
T_n(k)=\frac{b_{2k}+b_{2k+1}}{b_k}
=\frac{\binom{n+1}{2k+1}}{\binom nk},\qquad 2k\le n.
\]
The sign in (1) is the sign of \(T_n(k)-F_n(k)\).

If \(n=3m+1\) with \(m\ge1\), at \(k_*=m+1\) a direct factorial calculation gives
\[
T_{3m+1}(m+1)=\frac{(3m+2)m(m+1)}{(2m+3)(2m+2)(2m+1)}<1.
\]
If \(n=3m+2\) with \(m\ge0\), at \(k_*=m+1\),
\[
T_{3m+2}(m+1)=\frac{3(m+1)}{2(2m+3)}<1.
\]
In both cases \(F_n(k_*)\ge1\), except no exceptional issue arises for \(n=2\), where equality \(F_2(1)=1\) holds. The step is strictly negative.

If \(n=3m\), \(m\ge1\), the boundary is more delicate: \(T_{3m}(m)=(3m+1)/(2m+1)<3/2\). Let \(F_m:=F_{3m}(m)\). Direct binomial evaluation gives \(F_1=11/8>4/3=T_3(1)\) and \(F_2=99/64>3/2\). We show \(F_{m+1}>F_m\) by adding three independent fair bits. If \(q_j=\Pr(S_{3m}=j)\), conditioning on the old total and the independent \(\operatorname{Bin}(3,1/2)\) block gives exactly
\[
8(F_{m+1}-F_m)=-q_{m+1}+3q_m+5q_{m-1}+q_{m-2},\tag{2}
\]
with \(q_j=0\) for negative \(j\). Indeed, only old totals \(m+1,m,m-1,m-2\) contribute, with respective changes \(-1/8,3/8,5/8,1/8\). Since \(q_{m+1}/q_m=2m/(m+1)<2\), the right side is strictly positive. Consequently for \(m\ge2\), \(F_m\ge F_2>3/2>T_{3m}(m)\); the case \(m=1\) was checked separately. Therefore the first step at \(k_*\) is always strictly decreasing for \(n\ge2\).

**4. All later steps decrease.** As long as \(2k+3\le n+1\) (equivalently, the next \(T_n(k+1)\) is nonzero), factorial cancellation yields
\[
\frac{T_n(k+1)}{T_n(k)}
=\frac{(n-2k)(n-2k-1)}{2(2k+3)(n-k)}.\tag{3}
\]
For \(k\ge k_*\) and \(k\le n/2\), the numerator is at most \(n^2/9\), whereas the denominator is at least \(2n^2/3\); hence (3) is at most \(1/6\). The first-step calculations also give \(T_n(k_*)<3/2\) when \(2k_*\le n\), so every subsequent \(T_n(k)\), when defined and nonzero, is less than \(1\). Because \(F_n(k)\ge1\) up to \(k\le n/2\), (1) is negative throughout this range. If \(2k>n\), then \(b_{2k}+b_{2k+1}=0\), so (1) is strictly negative directly. This proves strict decrease for every \(k\ge k_*\). Finally \(n=1\) follows from \(G_1(0)=0\) and \(G_1(1)=1/4\).

**5. Deficit exponent.** At the unique maximizer write \(L_n=\Pr(S_n<k_*)\) and \(R_n=\Pr(S_n\ge2k_*)\). Then the exact identity
\[
1-G_n(k_*)=2L_n-L_n^2+R_n
\]
has two nonnegative, exponentially small contributions. Since \(k_*/n\to1/3\) and \(2k_*/n\to2/3\), the standard fair-binomial large-deviation estimate gives both \(-n^{-1}\log L_n\to D(1/3\|1/2)\) and \(-n^{-1}\log R_n\to D(2/3\|1/2)=D(1/3\|1/2)\). The log of their positive sum has the same exponent, establishing the claimed rate. This uses only the elementary Stirling/large-deviation exponent, not a sharp prefactor.

## Verification

The included standalone exact-integer program `verification/check_bk_optimizer.py` checked the exact numerator of \(G_n(k)\), its first differences and the unique optimizing integer for all \(1\le n\le1100\). It also checked the three-bit coupling identity (2) for \(1\le m\le150\), and sample entropy-exponent values. The program reports **1,311,695 assertions passed**. These finite checks do not prove the infinite claim: Steps 1–5 are the complete analytic argument.

## Relationship to prior work

The van den Berg–Kesten inequality gives nonnegativity of the gap. Cerf and Tesio analyze equality and witness mechanisms. Tesio's October 2026 paper gives two quantitative lower bounds and analyzes OR, majority and macroscopic Hamming thresholds in its examples, but its inspected theorem, proofs and examples do not optimize the actual *finite-dimensional* BK gap over all threshold integers. The new statement is a sharp discrete optimization *within* identical fair Hamming thresholds, not a new general BK inequality. Its strict finite-size optimizer is stronger than a mere statement about limiting windows or large-deviation rates, neither of which rules out exceptional finite thresholds.

## Limitations

The theorem does not characterize maximizers over all pairs of increasing events, biased coordinate laws, unequal event thresholds or non-product measures. The entropy corollary gives only the exponential rate, not a universal pre-exponential coefficient. The exact finite-dimensional maximizer is proved internally but has not undergone independent validation; historical priority remains contingent on unlocated stronger binomial-tail optimization results.

## References

- Pierre Tesio, *How much do increasing events occur disjointly?*, arXiv:2610.32658v1 (first posted 23 October 2026), https://arxiv.org/html/2610.32658v1 (especially Sections 1 and 6).
- Raphaël Cerf and Pierre Tesio, *The case of equality in BK*, arXiv:2607.02272v2, https://arxiv.org/html/2607.02272v2.
- J. van den Berg and J. Kesten, *Inequalities with applications to percolation and reliability*, Journal of Applied Probability 22 (1985), 556–569 (the BK inequality).
