# A terminal-overshoot renewal coupling for degree-biased recursive-tree destruction

## Finding

Let \(K_n\) be the number of degree-biased cuts required to erase a uniform random recursive tree with \(n\ge2\) vertices, under the vertex-deletion rule in [1]. Set \(H_j=\sum_{i=1}^j i^{-1}\), and let \(\zeta_1,\zeta_2,\ldots\) be independent positive-integer variables with
\[
\Pr(\zeta_i=k)=q_k=\frac{H_{k-1}}{k(k+1)},\qquad k\ge2.
\]
Put \(S_0=0\), \(S_j=\zeta_1+\cdots+\zeta_j\), and \(\tau_n=\min\{j\ge1:S_j\ge n-1\}\). Then there is a coupling of \(K_n\) and \(\tau_n\) such that
\[
K_n\ge \tau_n\ \text{almost surely},\qquad
\Pr(K_n\ne\tau_n)\longrightarrow0.
\]
In particular,
\[
d_{\mathrm{TV}}\bigl(\mathcal L(K_n),\mathcal L(\tau_n)\bigr)\longrightarrow0,
\qquad \frac{K_n(\log n)^2}{2n}\xrightarrow{\Pr}1.
\]
The coupling provides an explicit finite-size error bound. With \(R_n=n-S_{\tau_n-1}\), \(u(r)=\Pr(S_j=r\text{ for some }j\ge0)\), and any fixed integer \(M\ge3\) with \(n>M\),
\[
\Pr(K_n\ne\tau_n)
\le \frac1{H_{M-1}+1}
+\sum_{r=n-M+1}^{n-2}u(r).
\]
The finite-n bound and total-variation statement are stronger than merely a weak law for the cut count. They do not assert convergence of means or a specific second-order stable limit.

## Assumptions and scope

A uniform random recursive tree on labels \(1,\ldots,n\) is obtained by attaching each new label independently to a uniformly selected smaller label; label \(1\) is the root. Orient edges toward the root. At each degree-biased cut, select an edge uniformly, remove its parent endpoint and all descendants of that endpoint, and retain the connected component containing the original root; if the selected endpoint is the root, erase the whole tree. Stop when zero or one vertex remains. Conditional on the remaining size, the retained tree is again a uniform random recursive tree [1, Proposition 1.2]. Every logarithm here is natural.

The result concerns this precise degree-biased deletion rule, including instant root deletion. It does not concern the classical uniformly chosen nonroot-edge deletion rule. All probability statements refer to the randomness of the recursive tree and cuts, equivalently to its Markov size-decrement chain.

## Proof

**1. Exact decrement kernel.** The splitting property and one-cut enumeration of [1, Proposition 1.3] give, at a state of size \(m\ge2\), the probability of deleting \(k\) vertices:
\[
p_m(k)=\frac{m}{m-1}\frac{H_{k-1}}{k(k+1)}
\quad (2\le k<m),\qquad
p_m(m)=b_m:=\frac{H_{m-1}}{m-1}.
\]
The terminal event includes both deleting \(m-1\) vertices and deleting all \(m\) vertices. The kernel and splitting property imply a Markov chain for the remaining size, started at \(n\).

**2. Harmonic renewal tail.** Interchanging two absolutely convergent nonnegative sums gives
\[
Q_m:=\Pr(\zeta_i\ge m)
=\sum_{k=m}^{\infty}\sum_{a=1}^{k-1}\frac1{a k(k+1)}
=\frac{H_{m-1}+1}{m},\qquad m\ge2.
\]
Indeed, for \(a<m\) the inner telescoping sum is \(1/m\), while for \(a\ge m\) it is \(1/(a+1)\), leaving \(H_{m-1}/m+1/m\). Thus \(Q_2=1\), so \(q\) is a probability law. Also \(q_2,q_3>0\), hence its arithmetic span is one, and
\[
\mathbb E\zeta_i=\sum_{m\ge1}\Pr(\zeta_i\ge m)=\infty
\]
because \(Q_m\) has order \((\log m)/m\).

**3. A terminal-only disagreement coupling.** When the remaining tree has \(m\ge2\) vertices, draw the next independent \(\zeta\) with law \(q\). If \(\zeta<m\), remove \(\zeta\) vertices. If \(\zeta\ge m\), delete the whole tree with conditional probability \(b_m/Q_m\). Otherwise, draw a fresh \(k\in\{2,\ldots,m-1\}\) with probabilities \(q_k/(1-Q_m)\), and remove \(k\) vertices. For \(m=2\), necessarily \(b_m=Q_m=1\), so the latter branch never occurs.

This is exactly the required cutting law: the full-deletion probability is \(Q_m(b_m/Q_m)=b_m\), and for every \(2\le k<m\),
\[
\Pr(\text{delete }k)
=q_k+(Q_m-b_m)\frac{q_k}{1-Q_m}
=q_k\frac{1-b_m}{1-Q_m}
=\frac{m}{m-1}q_k=p_m(k).
\]
The second equality uses \(1-b_m=(m-1-H_{m-1})/(m-1)\) and \(1-Q_m=(m-1-H_{m-1})/m\). This construction can be iterated using the splitting property, so it has the complete law of the tree-cutting count.

Until the first time the independent partial sums \(S_j\) reach \(n-1\), all proposed jumps are smaller than the remaining size and are followed verbatim. At that first crossing, the process ends in the same step if \(\zeta=m-1\) (only the root remains) or if \(\zeta\ge m\) and the full-deletion option is accepted. A rejection of this final overshoot is the sole way the counts can differ. Consequently \(K_n\ge\tau_n\) pathwise, and the probability of disagreement is at most the overshoot-rejection probability
\[
\delta_m:=1-\frac{b_m}{Q_m}
=\frac{m-1-H_{m-1}}{(m-1)(H_{m-1}+1)}
\le\frac1{H_{m-1}+1}.
\]
Here \(m=R_n=n-S_{\tau_n-1}\). On \(R_n\ge M\), the bound is at most \((H_{M-1}+1)^{-1}\). On \(R_n<M\), the last renewal position before the crossing belongs to \(\{n-M+1,\ldots,n-2\}\), so a union bound proves the finite-size inequality stated in the finding.

**4. Vanishing terminal discrepancy.** The ordinary lattice Blackwell renewal theorem states that for an aperiodic positive-integer renewal law with mean \(\mu\in(0,\infty]\), its renewal mass satisfies \(u(r)\to1/\mu\), with the convention \(1/\infty=0\) [3]. Our law has arithmetic span one and infinite mean. Hence \(u(r)\to0\); for fixed \(M\), the finite sum in the bound tends to zero. Now let \(M\to\infty\), using \(H_{M-1}\to\infty\), to obtain \(\Pr(K_n\ne\tau_n)\to0\). The coupling inequality for total variation yields the first conclusion.

**5. First-order scale.** Write \(\zeta^{(n)}=\zeta\mathbf1_{\{\zeta\le n\}}\). From the explicit mass function,
\[
\mathbb E\zeta^{(n)}
=\sum_{k=2}^{n}\frac{H_{k-1}}{k+1}
=\frac12(\log n)^2+O(\log n),\qquad
\mathbb E[(\zeta^{(n)})^2]
=\sum_{k=2}^{n}\frac{kH_{k-1}}{k+1}
=O(n\log n).
\]
Fix \(c>0\) and put \(j_n=\lfloor 2cn/(\log n)^2\rfloor\). Independence and Chebyshev's inequality give
\[
\frac1n\sum_{i=1}^{j_n}\zeta_i^{(n)}\xrightarrow{\Pr}c,
\]
while \(\Pr(\max_{i\le j_n}\zeta_i>n)\le j_n Q_{n+1}=O((\log n)^{-1})\to0\). Therefore \(S_{j_n}/n\to c\) in probability. Choosing \(c\) on either side of one and using monotonicity of \(S_j\) gives \(\tau_n/(2n/(\log n)^2)\to1\) in probability. The total-variation coupling transfers this statement to \(K_n\).

## Verification

The accompanying standalone file `verify.py` checks with exact rational arithmetic the identities for \(q_k\), \(Q_m\), \(p_m(k)\), the overshoot/replacement mixture and the full count distributions on small trees. It separately verifies that the two recursions give probability laws and that the proposed pathwise order is reflected by their finite cumulative distributions. The universal statements in the proof are analytic: a finite computation does not establish a renewal limit or an infinite family of inequalities.

Run from the extracted package directory using `python3 verify.py`; the checker uses only Python's standard library. All files required for these checks are included in the package.

## Relationship to prior work

Eslava, López and Ortiz [1] introduce this exact degree-biased recursive-tree cutting model, establish the splitting property and decrement kernel, and show an upper stochastic comparison with a harmonic-jump *barrier* walk. Their main asymptotic is for that comparison walk, and their Remark 3.3 identifies the instant-deletion atom as an obstacle to a direct unconditional-jump approximation. The present proof does not claim the kernel or the upper comparison as new. Instead it uses the instant-deletion atom constructively: the first overshoot is accepted with probability tending to one whenever the residual size diverges. The result is a direct total-variation approximation of the actual cut count, and hence its first-order law.

Iksanov and Möhle [2] introduced a renewal coupling for the **uniform-edge** recursive-tree cutting chain; its decrement mass is proportional to \(1/[k(k+1)]\), not the harmonic-weighted mass above. Their different cutting model and its coupling do not yield the current exact terminal-overshoot rule. Iksanov and Möhle [4] also study general absorption recursions with normalized truncation probabilities; the instant-deletion mass \(b_m\) in this degree-biased model does not satisfy their normalized-truncation hypothesis. Blackwell's renewal theorem [3] is standard and supplies only the vanishing renewal mass, not this probabilistic coupling. These distinctions are statements about mathematical implication rather than title similarity.

## Limitations

Only the number of cuts, not the entire cut-tree, deleted-subtree sequence or root geometry, is coupled. The total-variation error is proved to vanish, but no explicit numerical rate is asserted because the renewal mass bound is left in its exact finite form. The weak law does not imply convergence of expectations or an identified centered stable-fluctuation limit for \(K_n\). This theorem is limited to the precise degree-biased rule of [1]; replacing it with a different bias or survivor convention changes the decrement law. Priority relative to all potentially unindexed renewal-and-tree literature requires further historical assessment, and no independent validation is claimed.

## References

[1] L. Eslava, S. I. López, M. L. Ortiz, *A degree-biased cutting process for random recursive trees*, arXiv:2408.05168, first public submission 2024-08-09; revised version 2025-11-21. https://arxiv.org/abs/2408.05168 and https://arxiv.org/pdf/2408.05168.

[2] A. Iksanov, M. Möhle, *A probabilistic proof of a weak limit law for the number of cuts needed to isolate the root of a random recursive tree*, Electronic Communications in Probability **12** (2007), 28–35. DOI: 10.1214/ECP.v12-1253. Full-text mirror: https://studylib.net/doc/10598850/a-probabilistic-proof-of-a-weak-limit-law.

[3] D. Blackwell, *A renewal theorem*, Duke Mathematical Journal **15** (1948), 145–150; see the lattice/infinite-mean statement in *Blackwell renewal theorem*, Encyclopedia of Mathematics, https://encyclopediaofmath.org/wiki/Blackwell_renewal_theorem.

[4] A. Iksanov, M. Möhle, *On a random recursion related to absorption times of death Markov chains*, arXiv:0710.5826, first public submission 2007-10-31, especially the normalized decrement assumption (2). https://arxiv.org/abs/0710.5826.
