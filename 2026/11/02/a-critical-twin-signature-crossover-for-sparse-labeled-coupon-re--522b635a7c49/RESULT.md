# A critical twin-signature crossover for sparse labeled coupon recovery

## Finding

Consider independent draws of uniform \(k_n\)-subsets of \([n]\), each revealing the unordered set of the selected coupons and the unordered set of their unknown, pairwise distinct labels. Let \(Q_{\mathrm I}\) and \(Q_{\mathrm {II}}\) be the numbers of draws needed to identify every coupon's label when, respectively, the label alphabet is known or unknown. For the integer sequence \(1\le k_n<n\), put \(p_n=k_n/n\) and assume
\[
p_n\longrightarrow0,\qquad p_n\log n\longrightarrow c\in[0,\infty).
\]
Set \(r_n=-\log(1-p_n)\). For every real \(x\), define \(t_n(x)=\lfloor(\log n+x)/r_n\rfloor\), which is nonnegative for all sufficiently large \(n\), and \(\lambda=e^{-x}\), \(\mu=\tfrac12\lambda^2(e^c-1)\).

Let \(Z_n(t)\) be the number of coupons absent from all of the first \(t\) draws, and \(P_n(t)\) the number of unordered pairs of distinct coupons with the same **nonzero** binary incidence signature across these draws. Then
\[
(Z_n(t_n(x)),P_n(t_n(x)))\ \Longrightarrow\ (Z,P),\qquad
Z\sim\operatorname{Poisson}(\lambda),\quad P\sim\operatorname{Poisson}(\mu),\quad Z\perp P.
\]
In particular, the two recovery-time laws have the sharp critical profiles
\[
\begin{aligned}
\lim_{n\to\infty}\Pr\{r_nQ_{\mathrm I}-\log n\le x\}&=e^{-\lambda}(1+\lambda)e^{-\mu},\\
\lim_{n\to\infty}\Pr\{r_nQ_{\mathrm {II}}-\log n\le x\}&=e^{-\lambda}e^{-\mu}.
\end{aligned}
\]
Thus the ordinary uncovered-coupon obstruction acquires an **independent nonzero-twin obstruction** at the critical group-size scale \(k_n\asymp n/\log n\). For \(c=0\), the twin obstruction vanishes, recovering the one-missing-coupon and zero-missing-coupon profiles. The assertion holds without requiring \(k_n\to\infty\) in the \(c=0\) case.

## Assumptions and scope

Draws are independent from one time to the next; each draw is exactly one uniformly selected \(k_n\)-element subset of \([n]\), with no replacement *within* the draw. The unknown coupon-to-label mapping is an arbitrary bijection and does not influence the distribution of recoverability. The parameters obey \(p_n\to0\), \(p_n\log n\to c<\infty\), and \(x\) is fixed. All logarithms are natural. The \(c=0\) endpoint includes fixed positive group sizes; no conclusion is asserted for \(c=\infty\), for \(p_n\) converging to a nonzero constant, or for nonuniform group selection.

A coupon's incidence signature is the length-\(t\) zero-one column whose entry at draw \(j\) records membership of that coupon. Type I recovery means all columns are pairwise different; Type II recovery means all columns are pairwise different and nonzero. This previously established deterministic equivalence is used, not claimed as new. Consequently, for every \(n,t\), exactly
\[
\{Q_{\mathrm I}\le t\}=\{Z_n(t)\le1,\ P_n(t)=0\},\qquad
\{Q_{\mathrm {II}}\le t\}=\{Z_n(t)=0,\ P_n(t)=0\}.
\]

## Proof

**Step 1: the exact finite first moments.** Write \(p=k/n\), \(a=1-p\). For two fixed distinct coupons, the probabilities that one draw contains neither, or both, are respectively
\[
b_{00}=\frac{(n-k)(n-k-1)}{n(n-1)},\qquad b_{11}=\frac{k(k-1)}{n(n-1)}.
\]
The rows are independent, so for each integer \(t\ge0\),
\[
\mathbb E Z_n(t)=na^t,\qquad
\mathbb E P_n(t)=\binom n2\big((b_{00}+b_{11})^t-b_{00}^t\big).
\]
The second formula subtracts the all-zero common signature from equal-signature pairs. At \(t=t_n(x)\), since \(r_n\to0\), \(na^{t}\to\lambda\), and \(tp_n^2\to c\). Further, \(b_{00}=a^2(1+O(p_n/n))\) and \(b_{11}/b_{00}=p_n^2(1+o(1))\) when \(k_n\to\infty\). In all cases \(t p_n/n=O(\log n/n)\). The exact formula (interpreting \(b_{11}=0\) for \(k_n=1\)) implies
\[
n^2 b_{00}^{t}\to\lambda^2,\qquad
\mathbb E P_n(t)\to\tfrac12\lambda^2(e^c-1)=\mu.
\]
For \(c=0\), therefore, \(P_n(t)\to0\) in probability by Markov's inequality, even if \(k_n\) stays bounded.

**Step 2: the uncovered signatures are Poisson.** For every fixed positive integer \(h\),
\[
\mathbb E (Z_n(t))_h=(n)_h\left(\frac{(n-k_n)_h}{(n)_h}\right)^t.
\]
For fixed \(h\), the one-draw avoidance probability satisfies
\[
\frac{(n-k_n)_h}{(n)_h}=a^h\exp\big(O_h(p_n/n)\big).
\]
Since \(tp_n/n=O(\log n/n)\to0\), the factorial moment converges to \(\lambda^h\). Hence \(Z_n(t)\Rightarrow\operatorname{Poisson}(\lambda)\). Together with Step 1, this completes the joint claim when \(c=0\), with the second coordinate identically zero in the limit.

**Step 3: relative deconditioning of finitely many columns for \(0<c<\infty\).** In this case \(k_n\sim cn/\log n\) and \(t=O(\log^2n)\). Replace each fixed-cardinality row temporarily by independent Bernoulli-\(p_n\) entries. For any fixed \(h\), the probability of a particular membership pattern with \(s\) selected among the \(h\) specified coupons in a true row is
\[
\frac{(k_n)_s(n-k_n)_{h-s}}{(n)_h};
\]
under the independent-entry row it is \(p_n^s(1-p_n)^{h-s}\). Their ratio lies between
\[
\exp\{-C_h(1/k_n+1/(n-k_n))\}
\quad\text{and}\quad
\exp\{C_h(1/k_n+1/(n-k_n))\}
\]
for all sufficiently large \(n\), uniformly over the \(2^h\) membership patterns, by writing all falling factorials as products. Multiplying over \(t\) rows gives a uniform probability ratio \(1+o(1)\), since \(t/k_n+t/(n-k_n)=O(\log^3n/n)\to0\). This holds for **every** event determined by the incidence signatures of any fixed number of coupons, including events with probability of order \(n^{-h}\). It is stronger than an additive total-variation comparison and is the key to transferring factorial moments.

**Step 4: Poisson birthday collisions in the independent-entry comparison model.** The \(n\) signature columns are now independent random words in \(\{0,1\}^{t}\). A word \(w\) of Hamming weight \(|w|\) has probability \(u_w=p_n^{|w|}(1-p_n)^{t-|w|}\). The zero word has probability \(u_0=a^t\), with \(nu_0\to\lambda\). For any fixed \(h\ge2\), put \(s_h=\sum_{w\ne0}u_w^h\). Direct product expansion yields
\[
s_h=a^{ht}\left[\left(1+\left(\frac{p_n}{a}\right)^h\right)^t-1\right].
\]
Because \(tp_n^2\to c\),
\[
n^2s_2\longrightarrow\lambda^2(e^c-1)=2\mu,
\qquad n^hs_h\longrightarrow0\quad\text{for every fixed }h\ge3.
\]
For the latter, \(tp_n^h=(tp_n^2)p_n^{h-2}\to0\). Consider fixed mixed factorial moments \(\mathbb E(Z)_a(P)_b\), where \(P\) counts unordered pairs sharing the same **nonzero** word. Expand as choices of \(a\) ordered distinct zero-word indices and \(b\) ordered distinct edges. A component of \(h\ge3\) vertices in the graph formed by selected pair edges forces a common nonzero word, contributes probability \(s_h\), and its index choices contribute \(O(n^h)\); hence every term with such a component vanishes. The remaining choices use distinct zero-word vertices and \(b\) disjoint two-vertex components. Their combined contribution tends to
\[
(n)_{a+2b}u_0^a s_2^b/2^b\ \longrightarrow\ \lambda^a\mu^b.
\]
The limiting mixed factorial moments are exactly those of independent \(\operatorname{Poisson}(\lambda)\) and \(\operatorname{Poisson}(\mu)\) variables. The Poisson laws are moment-determinate, and the first-moment bounds give tightness. Thus the independent-entry comparison model has the claimed joint limit.

**Step 5: transfer and recoverability.** Each term in any fixed mixed factorial moment above depends on no more than \(a+2b\) specified coupon columns. Step 3 compares its true fixed-cardinality-row probability with the independent-entry probability by a factor \(1+o(1)\), uniformly in the chosen indices and event. The entire nonnegative factorial-moment sum inherits the same relative comparison, so the true joint factorial moments converge to \(\lambda^a\mu^b\). This proves the joint Poisson limit for \(c>0\). The deterministic recovery equivalences in the assumptions give the two limiting distribution functions by evaluating \(\Pr(Z\le1,P=0)\) and \(\Pr(Z=0,P=0)\). Finally, \(t_n(x)=\lfloor(\log n+x)/r_n\rfloor\) matches the event \(r_nQ-\log n\le x\) exactly, which completes the proof.

## Verification

The standalone script `verify.py` exhaustively enumerates all ordered sequences of one, two, or three fixed-size rows for \(3\le n\le6\) and every \(1\le k<n\). It checks the two recoverability predicates, separation of zero-word and nonzero-word collisions, the first two factorial moments of the zero count, and the exact nonzero-twin expectation using rational arithmetic. It also evaluates the exact finite-\(n\) intensities near the proposed crossover. The supplied `verification_output.txt` records the executed program's results: 57,768 exact assertions passed. These enumerations do not certify the infinite limit; the proof above supplies the fixed-\(h\) factorial-moment argument and uniform deconditioning bound.

Reproduce with a standard Python 3 interpreter using `python verify.py`; no third-party packages or network access are required.

## Relationship to prior work

Tan, Limor, Bar-Lev, Gabrys, Yakhini and Siegel (2025), arXiv:2507.15231v1, introduced and modeled the labeled coupon collector, deriving finite and deterministic conditions and numerical expectation methods. Berrebi, Yaakobi, Yakhini and Bar-Lev (2025), arXiv:2502.02968v1, treated partial recovery and random sample sizes, including exact finite Markov calculations. Barak-Pelleg and Berend (2025), arXiv:2510.23249v1, proved asymptotic expectations for fixed group size two. Tan, Bar-Lev, Gabrys, Yakhini and Siegel (2026), arXiv:2610.32251v1, completely characterized deterministic minima via separating systems, including the incidence-column criterion used in this proof.

The present assertion is **not** a new separating-system criterion, an optimal deterministic construction, a fixed-\(k\) expected-time formula, or a general theorem about all random fingerprint designs. Its specific claim is the independent zero/nonzero-twin Poisson crossover and the paired limiting recovery-time profiles when \((k_n/n)\log n\to c\). The usual coupon-covering Poisson limit by itself does not give the second collision intensity; a naive no-twin approximation is false for \(c>0\). The Poisson occupancy calculation is classical in spirit, but requires a nonzero-word extraction and relative (not additive) deconditioning for fixed-size dependent rows.

Relevant older studies of deterministic separating systems by Rényi, Katona and Wegener concern optimal numbers of tests rather than these distributional limits. A broader unindexed random fingerprint or occupancy theorem may contain the crossover implicitly; independent literature verification is still warranted.

## Limitations

The endpoint \(c=\infty\) and constant-density samples are excluded. Convergence is weak, with no claimed error rate or uniformity over \(x\) or \(c\). The factorial-moment comparison requires \(c>0\) for its Bernoulli-row proxy; the \(c=0\) case is handled separately using first moments. No assertion of priority over all historical random separating-system or sparse-word occupancy literature is made; the primary-source comparison was bounded to the identified works. The result has not undergone independent mathematical review.

## References

- S. S. Berrebi, E. Yaakobi, Z. Yakhini and D. Bar-Lev, *The Labeled Coupon Collector Problem with Random Sample Sizes and Partial Recovery*, arXiv:2502.02968v1, February 5, 2025. https://arxiv.org/html/2502.02968v1
- A. Tan, O. Limor, D. Bar-Lev, R. Gabrys, Z. Yakhini and P. H. Siegel, *The Labeled Coupon Collector Problem*, arXiv:2507.15231v1, July 21, 2025. https://arxiv.org/pdf/2507.15231
- D. Barak-Pelleg and D. Berend, *On Conjectures concerning the Labeled Coupon Collector Problem*, arXiv:2510.23249v1, October 27, 2025. https://arxiv.org/html/2510.23249v1
- A. Tan, D. Bar-Lev, R. Gabrys, Z. Yakhini and P. H. Siegel, *The Minimum Number of Samples in the Labeled Coupon Collector Problem*, arXiv:2610.32251v1, October 23, 2026. https://arxiv.org/html/2610.32251v1
- I. Wegener, *On separating systems whose elements are sets of at most k elements*, Discrete Mathematics 28 (1979), 219–222. https://doi.org/10.1016/0012-365X(79)90101-8
