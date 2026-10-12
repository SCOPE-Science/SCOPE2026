# Poisson extremes for alternating streaks of two-point moving averages

## Finding

Let \(X_1,X_2,\ldots\) be independent identically distributed atomless real random variables, and let \(Y_i=(X_i+X_{i+1})/2\). For integers \(n\ge2\) and \(1\le r\le n-1\), call a starting position \(i\in\{1,\ldots,n-r\}\) an *alternating window of length* \(r\) if the \(r\) successive nonzero differences \(Y_{i+1}-Y_i,\ldots,Y_{i+r}-Y_{i+r-1}\) alternate strictly in sign, with either initial sign allowed. Write \(W_{n,r}\) for the number of such positions and \(H_n=\max\{r:W_{n,r}>0\}\) for the longest contiguous alternating streak measured in **comparisons**, not observations. Put
\[
q_r=\frac{1}{(\lfloor r/2\rfloor+1)!(\lceil r/2\rceil+1)!},\qquad p_r=2q_r,\qquad \lambda_{n,r}=(n-r)p_r.
\]
The exact single-window probability \(p_r\) is a special instance of the distribution-free descent-pattern framework of Bandt and Shiha (2007), Proposition 7, and is **not claimed as new**.

**Poisson-extreme theorem.** Write \(m=r+2\) and \(c_r=(\lfloor r/2\rfloor+2)^{-1}\). For all stated finite \(n,r\), using the standard total-variation convention \(d_{\mathrm{TV}}(P,Q)=\sup_A|P(A)-Q(A)|\),
\[
 d_{\mathrm{TV}}\bigl(\mathcal L(W_{n,r}),\operatorname{Poisson}(\lambda_{n,r})\bigr)
 \le 2(n-r)\left[\bigl(2m-1+4m^2\bigr)p_r^2+\frac{4q_{r+1}}{1-c_r}\right]. \tag{1}
\]
Consequently, for any integer sequences \(n\to\infty\) and \(r=r_n\to\infty\) with \(r_n=o(\sqrt n)\) and \(\sup_n\lambda_{n,r_n}<\infty\), this total-variation distance tends to zero. If additionally \(\lambda_{n,r_n}\to\lambda\in[0,\infty)\), then \(W_{n,r_n}\) converges in distribution to \(\operatorname{Poisson}(\lambda)\), and
\[
 \Pr(H_n<r_n)=e^{-\lambda_{n,r_n}}+o(1).\tag{2}
\]
Positive finite \(\lambda\) need not occur along every integer \(n\) because of the lattice size of the factorial step; (1) is an approximation to the actual varying mean regardless of that oscillation.

The following finite extreme-value bounds hold simultaneously for every \(n\ge2\), \(1\le r\le n-1\):
\[
 1-(1-p_r)^{\lfloor(n+1)/(r+2)\rfloor}\ \le\ \Pr(H_n\ge r)\ \le\ \min\{1,(n-r)p_r\}.\tag{3}
\]
In particular, with \(g(n)=\log n/\log\log n\) for sufficiently large \(n\),
\[
 \frac{H_n}{g(n)}\longrightarrow1\qquad\text{almost surely}.\tag{4}
\]
Thus the longest sustained turning streak has an unusually short \(\log n/\log\log n\) scale, despite the finite dependence range of the averaged sequence.

## Assumptions and scope

The innovations are iid with an atomless real law, which ensures the comparisons are nonzero almost surely. No moments or density are required, and the equality of the two averaging weights is essential. All occurrences are **contiguous** in the averaged sequence; this is not the longest alternating subsequence problem. Equation (1) is valid at every finite admissible \(n,r\), though its right-hand side can exceed one. The Poisson convergence only concerns growing thresholds of bounded expected frequency with \(r=o(\sqrt n)\). No assertion is made that \(H_n\) has a universal centered limit law along all sample sizes.

## Proof

**1. Parity-chain representation.** An exact cancellation gives \(Y_{j+1}-Y_j=(X_{j+2}-X_j)/2\). If a specified window has alternating signs, comparisons with indices of one parity all point upwards and comparisons with indices of the other parity all point downwards, or the other way around. Thus there are two disjoint iid chains, of \(\lfloor r/2\rfloor+1\) and \(\lceil r/2\rceil+1\) distinct innovations, each constrained to one specific strict total order. Both prescribed orientations have probability \(q_r\), so the window probability is \(p_r=2q_r\). This also proves \(q_{r+1}/q_r=(\lfloor r/2\rfloor+2)^{-1}=c_r\), with subsequent ratios bounded above by \(c_r\).

**2. Two-window control.** Let \(I_i\) indicate a length-\(r\) alternating window starting at \(i\). Its entire dependence is through the \(m=r+2\) innovations \(X_i,\ldots,X_{i+r+1}\). Hence \(I_i\) and all \(I_j\) with \(|j-i|\ge m\) are independent. For \(1\le d<r\), the two sign runs overlap. Their conjunction is exactly one alternating run of length \(r+d\), so
\[
\Pr(I_i=I_{i+d}=1)=2q_{r+d}.\tag{5}
\]
For \(d=r\) and \(d=r+1\), the innovation windows share respectively two and one variables. The following bounded-rank-density fact handles this boundary overlap: for an event \(A\) determined solely by the relative ranks of \(m\) iid atomless observations, the conditional joint law of any \(s\) specified coordinates given \(A\) has density at most \((m)_s=m!/(m-s)!\) relative to their unconditional iid law. Indeed, a particular full ordering has unconditional probability \(1/m!\), whereas conditioned on the \(s\) specified numerical values its probability is at most \(1/(m-s)!\): the unobserved labels remain uniformly permuted. Bayes' rule therefore bounds the conditional density of the shared coordinates given any full ordering by \((m)_s\); conditioning on \(A\) only mixes these full-order laws. Since disjoint innovation sets are independent once their shared coordinates are fixed, this yields
\[
 \Pr(I_i=I_{i+d}=1)\le m^2p_r^2\qquad(d=r,r+1).\tag{6}
\]
Equations (5) and (6) cover all dependent distinct pairs.

**3. Poisson bound.** Use dependence neighborhoods \(B_i=\{j:|j-i|<m\}\) for the \(N=n-r\) indicators. The local-dependence Chen--Stein theorem of Arratia, Goldstein and Gordon (1989), Theorem 1, applies with \(b_3=0\). With \(b_1=\sum_i\sum_{j\in B_i}\mathbb E I_i\mathbb E I_j\) and \(b_2=\sum_i\sum_{j\in B_i,j\ne i}\mathbb E(I_iI_j)\), the preceding bounds give
\[
 b_1\le N(2m-1)p_r^2,\qquad b_2\le 4N\sum_{d=1}^{r-1}q_{r+d}+4Nm^2p_r^2
 \le N\left[\frac{4q_{r+1}}{1-c_r}+4m^2p_r^2\right].
\]
The theorem bounds total variation by at most \(2(b_1+b_2)\), yielding (1) conservatively under the stated convention. Because \(q_{r+1}/q_r=O(1/r)\), \(p_r=\lambda_{n,r}/(n-r)\), and \(m=r+2\), its right side is \(O(\lambda_{n,r}/r+\lambda_{n,r}^2r^2/n)\) under the displayed asymptotic assumptions. Equation (2) follows from \(\{H_n<r\}=\{W_{n,r}=0\}\).

**4. Tail bounds and almost-sure scale.** The upper bound in (3) is the union bound over \(n-r\) possible starting indices. For the lower bound, select \(\lfloor(n+1)/(r+2)\rfloor\) starts whose length-\(r+2\) innovation intervals are disjoint; their occurrence events are independent. Stirling's formula gives
\[
 -\log q_r=r\log r+O(r).\tag{7}
\]
For fixed \(\varepsilon\in(0,1)\), set \(r_\pm=\lfloor(1\pm\varepsilon)\log n/\log\log n\rfloor\). At dyadic sizes \(n=2^k\), (3) and (7) give \(\Pr(H_n\ge r_+)\le n^{-\varepsilon+o(1)}\) and \(\Pr(H_n<r_-)\le\exp(-n^{\varepsilon+o(1)})\), both summable over \(k\). The first Borel--Cantelli lemma gives the assertions along dyadic \(n\); monotonicity of \(H_n\) and \(g(2^{k+1})/g(2^k)\to1\) fill the gaps, proving (4).

## Verification

Run the included `verify.py` with a standard Python 3 interpreter. It enumerates the \((r+2)!\) equally likely rank permutations for every \(1\le r\le7\), checks the exact single-window probability, then enumerates rank permutations for \(2\le n\le8\) to check both sides of (3) and the complete finite histogram. It additionally checks exact joint probabilities of overlapping alternating windows for ten small configurations. All \(1{,}641{,}300\) enumerated permutations passed exact integer/rational checks. The infinite Poisson and almost-sure statements are proved above, not deduced from enumeration; the program is not a substitute for reviewing the local-dependence theorem or the rank-density lemma.

## Relationship to prior work

Bandt and Shiha (2007), Section 6 and Proposition 7, *already* give the distribution-free combinatorial evaluation framework for every fixed descent pattern of equal-weight moving averages. The parity-factorial probability in the present proof is an immediate specialization and is not an originality claim. The new contribution assessed here is the **growing-window Poisson approximation with explicit dependence error and the almost-sure longest-streak scale**, requiring control of neighboring rare patterns rather than only their marginals. Arratia, Goldstein and Gordon (1989) supply the general Chen--Stein estimate; the overlap and rank-conditioning bounds specific to this moving-average model are derived above. Bender, Helton and Richmond (2003) study nearly periodic *iid* permutation rise/fall patterns, a different observation mechanism with exponential rather than factorial sign-word probabilities. Houdré and Restrepo (2010) study the *longest alternating subsequence*, which need not be contiguous and consequently is a different extremal problem.

## Limitations

The theorem is for equal-weight two-point smoothing of iid atomless innovations. Unequal coefficients, correlated innovations, weak nonstationarity, and higher-order averaging kernels are not handled. The Poisson error bound need not be sharp for finite \(n\), and its asymptotic implication requires \(r=o(\sqrt n)\) and bounded mean. No universal nondegenerate limiting law for a deterministically centered \(H_n\) is asserted, because the factorial window probabilities cause lattice oscillations. Historical originality cannot be established by search alone; other specialized longest-run theorems might imply the same limit. Independent scientific validation is outstanding.

## References

1. C. Bandt and F. Shiha, *Order Patterns in Time Series*, Journal of Time Series Analysis **28** (2007), 646--665, doi:10.1111/j.1467-9892.2007.00528.x, especially Section 6, Proposition 7. Author-provided complete text at https://www.researchgate.net/publication/4993765_Order_Patterns_in_Time_Series.
2. R. Arratia, L. Goldstein and L. Gordon, *Two Moments Suffice for Poisson Approximations: The Chen--Stein Method*, Annals of Probability **17** (1989), 9--25, doi:10.1214/aop/1176991491, especially Theorem 1. Author-hosted text at https://dornsife.usc.edu/larry-goldstein/wp-content/uploads/sites/221/2023/06/AGG.pdf.
3. E. A. Bender, W. J. Helton and L. B. Richmond, *Asymptotics of Permutations with Nearly Periodic Patterns of Rises and Falls*, Electronic Journal of Combinatorics **10** (2003), R40, doi:10.37236/1733.
4. C. Houdré and R. Restrepo, *A Probabilistic Approach to the Asymptotics of the Length of the Longest Alternating Subsequence*, arXiv:1005.1893 (2010).
