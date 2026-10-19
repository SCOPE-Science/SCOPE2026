# Correctness

**PASS.** For the real-analytic lift \(G_K(x)=x+K\sin(2\pi x)\), the lift commutes with integer translations and has increment between \(-K\) and \(K\). Its points \(1/4\) and \(3/4\) undergo exactly \(+K\) and \(-K\) displacement per active iteration, so the strong law and the random rotation interval theorem of Li–Lloyd–Romaña give the precise interval \([-pK,pK]\). Identity steps induce an exact equality between sample and deterministic Bowen metrics for the active-clock count; because the counts visit every integer, this proves \(h_{\rm top}^{(r)}=p h_{\rm top}(g_K)\), without interchanging an unverified limsup. The quarter interval maps monotonically over \(K+1\) integer translates of itself, giving a separated full-branch horseshoe and entropy at least \(\log(K+1)\). The Lipschitz bound \(1+2\pi K\) gives the matching logarithmic-order upper estimate. All conclusions are analytical; the finite checker only corroborates elementary steps.

# Originality

**PASS, with a residual bibliographic risk.** Li, Lloyd and Romaña, arXiv:2606.16498v1, Theorem 2.3 prove strict positivity of quenched entropy from nondegenerate random rotation intervals. Their Section 5, Question 2 explicitly leaves quantitative hypotheses to be investigated and notes their proof supplies no bound depending only on width. Their Example 4.1 computes \(\log3\) entropy for a different piecewise-affine Bernoulli cocycle, not the fixed-width entropy-collapse family. Classical deterministic circle-map rotation entropy bounds apply to one deterministic endomorphism and cannot imply a *uniform random* lower bound under vanishing generator frequency. The literature comparisons establish no identified stronger covering statement, although the separate identity-step time-change mechanism is standard and an implicit equivalent example cannot be excluded.

# Mathematical value

**PASS.** The precise open boundary is whether a positive interval width alone can quantitatively bound random entropy from below. The explicit two-analytic-map construction rules this out even at any prescribed nonzero width, while retaining strictly positive entropy at every parameter. The quantitative \(\Theta_\Delta(\log K/K)\) estimates distinguish diminishing recurrence density from the number of monotone branches; this is a motivated obstruction to improving the qualitative positivity theorem without recurrence or distortion hypotheses, not an arbitrary parameter table.

# Limitations and closest literature

The active map's derivative bound increases with \(K\), the identity is deliberately included, and no assertion concerns a uniformly smooth/expanding family, positive lower-bounded active frequency, or annealed/full-skew-product entropy. Relevant background: Z. Li, S. Lloyd, S. Romaña (2026), arXiv:2606.16498, Theorems 2.1 and 2.3, Example 4.1, Section 5 Question 2; Z. Li and S. Lloyd (2026), arXiv:2603.18617; L. Alsedà, J. Llibre, F. Mañosas and M. Misiurewicz (1988), DOI:10.1088/0951-7715/1/3/004. An implicit pre-existing random idle-step specialization remains the principal bibliographic uncertainty; independent validation is not performed.

Self-review: passed. Independent audit: not yet performed.
