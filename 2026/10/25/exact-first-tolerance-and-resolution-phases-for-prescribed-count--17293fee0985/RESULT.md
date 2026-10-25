# Exact first-tolerance and resolution phases for prescribed-count composite DNA windows

## Finding

Fix integers \(w\ge3\) and \(1\le m\le w-1\). In a resolution-\(k\) composite DNA alphabet, each position encodes a nonnegative quadruple of nucleotide counts summing to \(k\). Each synthesized base is sampled independently using that quadruple divided by \(k\). A composite word is admitted at tolerance \(\varepsilon\in[0,1)\) when, **separately for each length-\(w\) window**, the probability that the synthesized window contains exactly \(m\) bases of type G or C is at least \(1-\varepsilon\).

Let \(N_{n,k,w,m}(\varepsilon)\) count the admissible length-\(n\) composite words, and let
\[C_{k,w,m}(\varepsilon)=\lim_{n\to\infty}\frac{1}{n}\log_2 N_{n,k,w,m}(\varepsilon).\]
The limit exists for all the parameters in this result by the finite weighted-state presentation described below; it is finite and positive.

**Exact zero tolerance.** For every \(k\ge1\) and \(n\ge w\),
\[\boxed{N_{n,k,w,m}(0)=\binom{w}{m}(k+1)^n,\qquad C_{k,w,m}(0)=\log_2(k+1).}\]

**The first permitted nonzero deviation.** For every \(k\ge3\), let \(r_k=2k/(k+1)\). For all \(n\ge w\),
\[\boxed{N_{n,k,w,m}(1/k)=\binom{w}{m}\sum_{j=0}^{\lfloor(n+w-1)/w\rfloor}\binom{n-(w-1)(j-1)}{j}(2k)^j(k+1)^{n-j},}\]
where the \(j=0\) summand is understood as \((k+1)^n\). Equivalently, defining \(Z_{n,w}(r)\) as the weighted independence polynomial of marks on \(\{1,\ldots,n\}\) separated by at least \(w\),
\[N_{n,k,w,m}(1/k)=\binom{w}{m}(k+1)^n Z_{n,w}(r_k).\]
Thus
\[\boxed{C_{k,w,m}(1/k)=\log_2(k+1)+\log_2\lambda_w(r_k),\quad \lambda_w(r)^w=\lambda_w(r)^{w-1}+r,\quad \lambda_w(r)>1.}\]
For every fixed \(w\), the jump above the zero-tolerance capacity tends to \(\log_2\lambda_w(2)\). At \(w=4\), this limiting jump is approximately \(0.6263821405\) bits per composite symbol. For all \(0\le\varepsilon<1/k\), there is no jump: \(C_{k,w,m}(\varepsilon)=\log_2(k+1)\).

**Resolution–tolerance crossover for all prescribed counts.** For integers \(0\le a\le k\), set
\[W_k(a)=\sum_{i=0}^{a}(i+1)(k-i+1)=\frac{(a+1)(a+2)(3k+3-2a)}{6}.\]
For every \(k\ge1\) and \(0\le\varepsilon<1/(w+1)\),
\[\boxed{W_k(\lfloor k\varepsilon/w\rfloor)\le 2^{C_{k,w,m}(\varepsilon)}\le W_k(\lfloor k\varepsilon\rfloor).}\]
For any fixed \(c>0\) and \(\alpha>0\), these bounds imply
\[\boxed{C_{k,w,m}(ck^{-\alpha})=(3-2\min\{\alpha,1\})\log_2 k+O_{w,c}(1).}\]
For each fixed \(\varepsilon\in(0,1)\), \(C_{k,w,m}(\varepsilon)/\log_2\binom{k+3}{3}\to1\) as \(k\to\infty\), whereas at \(\varepsilon=0\) the ratio tends to \(1/3\). All limits in \(k\) are taken **after** the infinite-blocklength capacity limit at fixed \(k\).

## Assumptions and scope

The resolution \(k\) is a positive integer; individual symbols are the full nucleotide-count quadruples, not just their GC probabilities. Exactly \((i+1)(k-i+1)\) composite symbols have GC synthesis probability \(i/k\). The samples at distinct sites within one synthesized strand are independent. The probability requirement is imposed **window by window**, not on the probability that every window in an entire strand simultaneously succeeds. Each window is required to contain **exactly** \(m\) GC bases, rather than to fall inside a nontrivial interval. The classification and crossover apply for \(w\ge3\), \(1\le m\le w-1\); the explicit first-tolerance formula assumes \(k\ge3\). End effects require \(n\ge w\). No biochemical secondary-structure, sequencing-channel, or finite-read-depth guarantees are asserted.

## Proof

**1. The exact-zero state space.** Let \(p_j\) be the GC probability at site \(j\), and let \(X_j\) be its independent Bernoulli GC indicator. For any site in any window, condition on the other \(w-1\) indicators. Writing \(Y\) for their sum,
\[\Pr(Y+X_j=m)=(1-p_j)\Pr(Y=m)+p_j\Pr(Y=m-1)\le\max\{p_j,1-p_j\}.\]
This is at most \(1-\min\{p_j,1-p_j\}\). If the prescribed count occurs with probability one, each \(p_j\) is therefore either zero or one. The deterministic GC labels \(b_j=p_j\in\{0,1\}\) must have exactly \(m\) ones in every window of length \(w\); subtracting consecutive window sums yields \(b_{j+w}=b_j\). The initial length-\(w\) binary pattern has \(\binom{w}{m}\) possibilities and determines all labels. Both GC-extreme bins contain exactly \(k+1\) full composite symbols, independently at each position. This gives the exact zero-tolerance count.

**2. Rigidity at the first tolerance.** The conditional inequality above shows that, at tolerance \(1/k\), every GC probability belongs to \(\{0,1/k,1-1/k,1\}\). For \(k\ge3\), the closest deterministic label \(b_j\in\{0,1\}\) is unique. Call a site *marked* when its GC probability is \(1/k\) or \(1-1/k\). If two marked sites occur in one window, their joint Bernoulli count, conditioned on all other sites, has maximum point probability strictly smaller than \(1-1/k\): for equal error orientations, the maximum is bounded by \(\max\{(1-1/k)^2,2(1-1/k)/k\}<1-1/k\); for opposite orientations, it is at most \((1-1/k)^2+1/k^2<1-1/k\). Convolving with the other sites cannot increase the largest point mass. Hence **every window contains at most one mark**.

If a window contains no mark, its physical GC count equals the number of ones in its deterministic-label pattern. If it contains one mark, the physical count equals that number with probability \(1-1/k\) and differs by one with probability \(1/k\). Because \(1/k<1-1/k\), a window meets the tolerance exactly when its deterministic-label sum is \(m\). Thus deterministic labels are periodic modulo \(w\), with \(m\) ones per period, and marked sites are separated by at least \(w\) positions. Conversely these two conditions ensure every window meets the required success probability. A site with no mark has \(k+1\) choices; a marked site has \(2k\), regardless of its deterministic label. An allowed set of \(j\ge1\) marked positions corresponds to \(j\) points separated by \(w\), counted by \(\binom{n-(w-1)(j-1)}j\). Multiplying weights and summing proves the stated finite-length formula.

The weighted mark polynomial satisfies \(Z_{n,w}(r)=Z_{n-1,w}(r)+rZ_{n-w,w}(r)\) for \(n\ge w\), with \(Z_{n,w}(r)=1+nr\) for \(0\le n<w\). Its primitive nonnegative finite-state recurrence has exponential growth factor equal to the unique \(\lambda>1\) with \(\lambda^w=\lambda^{w-1}+r\). Taking base-two logarithms and letting \(n\to\infty\) proves the capacity and its \(k\to\infty\) jump. For \(0\le\varepsilon<1/k\), the conditional inequality excludes every marked site, so the zero-tolerance count applies.

**3. Uniform positive-tolerance bounds.** Suppose \(0\le\varepsilon<1/(w+1)\). By the conditional inequality, each \(p_j\) is within \(\varepsilon\) of a unique deterministic label \(b_j\). In any length-\(w\) window, the probability that at least one synthesized base differs from its deterministic label is at most \(w\varepsilon\), by the union bound. If the deterministic labels in that window did not sum to \(m\), exact physical count \(m\) would require at least one error and would have probability at most \(w\varepsilon<1-\varepsilon\), contradiction. Thus the labels again have a periodic length-\(w\) pattern with \(m\) ones. At each site, the allowed near-extreme bin choices number exactly \(W_k(\lfloor k\varepsilon\rfloor)\), regardless of whether the label is zero or one. Therefore, for every \(n\ge w\),
\[N_{n,k,w,m}(\varepsilon)\le\binom{w}{m}W_k(\lfloor k\varepsilon\rfloor)^n.\]
For a lower bound, fix any one balanced binary period and permit only symbols whose GC probability differs from its deterministic label by at most \(\varepsilon/w\). Every window has probability at least \(1-\varepsilon\) of matching every deterministic label, hence of containing exactly \(m\) GC bases. This gives
\[N_{n,k,w,m}(\varepsilon)\ge W_k(\lfloor k\varepsilon/w\rfloor)^n.\]
The bounds survive the \(n\to\infty\) capacity limit. Since \(W_k(a)\) is uniformly comparable, for \(0\le a\le k/(w+1)\), to \(k(1+a)^2\) with constants depending only on \(w\), the claimed crossover follows. For fixed \(\varepsilon>0\), monotonicity permits a smaller fixed positive tolerance below \(1/(w+1)\), yielding \(C\ge3\log_2k-O_{w,\varepsilon}(1)\); the full-alphabet upper bound \(C\le\log_2\binom{k+3}{3}=3\log_2k+O(1)\) proves the normalized limit.

**4. Capacity existence.** At fixed \(k,w,m,\varepsilon\), the alphabet of GC bins is finite. A state records the last \(w-1\) bins, and an edge appends a bin if its \(w\)-window success probability passes the threshold; the edge weight is the number of full composite symbols in the appended bin. The total admissible count is a positive-vector weighted walk count. Its exponential growth is the spectral radius of the finite nonnegative matrix; an admissible periodic deterministic GC pattern supplies a positive cycle. Thus the limit defining \(C\) exists.

## Verification

The standalone script `verification_long_window.py` reconstructs every GC probability exactly as a rational coefficient of \(\prod_j((k-i_j)+i_jz)/k^w\), builds the weighted finite-state counts directly, and checks the zero-tolerance identity, both finite-length bounds, the sub-\(1/k\) plateau, and the exact first-threshold finite-length formula. It uses no floating-point probability comparisons. Running the embedded script from its own package path yielded `VERIFY_OK` and `ONSET_VERIFY_OK`, checking respectively 291 and 168 parameter/blocklength cases (459 case checks in total). These are finite consistency checks, not a substitute for the proofs for all parameters.

## Relationship to prior work

Bodur, Walter and Wachter-Zeh [1] define the independent composite-DNA probabilistic GC framework and give weighted finite-state capacity matrices for any fixed window and resolution (their Theorem 15). The present statement is an **analytic evaluation of the exact-count first-tolerance threshold**, including a complete finite-word classification and a closed \(w\)-step characteristic equation, plus a resolution-dependent capacity theorem uniform in every fixed \(w\) and prescribed count. Their general finite matrix determines any individual numerical capacity in principle but does not itself state these parameter-uniform structural formulas or high-resolution phase laws.

The earlier two-position exact-count phase theorem [2] already establishes corresponding \(w=2,m=1\) phenomena. **This subcase is not claimed as new.** The result here is asserted as new only for all longer windows \(w\ge3\). Nguyen, Wang, Cai, Zhang and Yakhini [3] study deterministic worst-case composite-DNA constraints; those do not include positive-tolerance exact-count window probabilities. A generic independent-set spacing recurrence is standard; the contribution lies in proving that it is precisely the allowed composite-DNA structure at the first threshold.

## Limitations

No claim is made for a single global probability of all windows simultaneously succeeding, for tolerance at or above the first threshold other than the stated uniform bounds, or for nonzero-width GC acceptance intervals. The first-threshold classification excludes \(k=2\), where the two nearest-endpoint classes meet and distinct configurations may behave differently. The capacity is an infinite-blocklength combinatorial count, not an error-correcting rate or a physical synthesis guarantee. A broader general weighted-automaton representation is already known; the claimed novelty is the explicitly evaluated longer-window threshold and resolution universality, subject to residual risk of equivalent work not indexed by the searches recorded below.

## References

[1] H. Bodur, F. Walter, A. Wachter-Zeh, *Probabilistic GC-Constraints for Composite DNA*, arXiv:2610.09998, first submitted 2026-10-07, especially Definitions 1, 2, 5 and Theorem 15; https://arxiv.org/html/2610.09998v1.

[2] *A resolution–tolerance phase law for probabilistic two-position composite-DNA GC constraints*, earlier two-position result, identifier `0a044f66` (scientific scope: \(w=2,m=1\)).

[3] T. T. Nguyen, C. Wang, K. Cai, Y. Zhang, Z. Yakhini, *Constrained Coding for Composite DNA: Channel Capacity and Efficient Constructions*, arXiv:2501.10645, first submitted 2025-01-18; https://arxiv.org/abs/2501.10645.
