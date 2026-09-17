# same-model review

## Verdict

**PASS**, as a same-model review only. The finding is not independently validated.

## Correctness

The argument was attacked at the points most likely to fail.

1. **Does Xiong need the full Walsh group structure rather than mere Hadamard orthogonality?** The front calculation only needs every pair of rows to agree/differ in exactly \(m/2\) positions. For the back calculation, using the explicit tensor \(H_4\otimes H\) retains the four special columns and gives the required split: for equal \(i\), all \(2m\) differences lie outside the special columns; for unequal \(i\), exactly two differences lie among the four special columns and \(2m-2\) lie outside. The retained/deleted special columns reproduce Xiong's one-\(\beta\) versus two-\(\beta\) cases.
2. **Scalar algebra.** With the same \(R,A,B,\alpha,\beta\) and equation \(\Phi_p(a)=1+1/m\), the four distance formulas are unchanged. A non-dyadic test using a Paley matrix of order 44 at \(p=5\) produced 352 points in dimension 350 with all pairwise fifth-power distances agreeing to relative error below \(5\times10^{-16}\).
3. **Critical expansion.** Direct algebra gives
   \(\Phi_4(a)=1-3(a^2-2)^2/[4(a^4+2)]\), hence the unique global maximum at \(a=\sqrt2\) and second derivative \(-2\). Differentiation in \(p\) gives
   \(c=\sqrt2\log(1+\sqrt2)-(7/4)\log2\). A separate symbolic calculation returned \(c=0.033442914300556735\ldots\) and \(8/c=239.21360226273167\ldots\).
4. **Global maximizer near \(p=4\).** At \(p=4\) the maximum is strict and unique. The tail tends to \(2^{2-p}\), uniformly for \(p\) in a compact neighborhood of 4, so no maximizer can escape to infinity under a sufficiently small perturbation. The implicit-function theorem then controls the unique nearby critical maximum.
5. **Hadamard-order density.** Paley gives order \(q+1\) for primes \(q\equiv3\pmod4\). The prime number theorem in arithmetic progressions yields such primes at multiplicative spacing \(1+o(1)\), enough for the matching template upper bound.

The strongest negative stress test was to distinguish global optimality from template optimality. The lower bound is explicitly restricted to the Xiong--Hadamard template; only the upper bound transfers to the global minimum counterexample dimension.

## Originality search

The search was performed on 2026-09-17 UTC and emphasized equivalent formulations, not only exact wording.

* Xiong's full six-page arXiv v1 (2609.14794, 13 Sep 2026) was read through the construction and existence proof. It fixes \(m=2^k\), uses the binary character Hadamard matrices, and states only that sufficiently large \(m\) works; it does not state the arbitrary-Hadamard replacement, the \(p\downarrow4\) asymptotic, or the constant \(c\).
* Searches for combinations of `Kusner`, `p>4`, `Hadamard`, `Paley`, `8m-2`, `p-4`, `1/(p-4)`, and the numerical/closed-form constant found Xiong's paper and background equilateral-set literature, but no source stating this refinement.
* Chalmers (arXiv:2608.14013) was checked at abstract/result level. Its 58-point construction concerns \(p=5\) and a small interval around 5, and is structurally different.
* Ge--Xu--Zhou (arXiv:2606.03987) was checked at abstract/result-summary level. Its central result proves the simplex bound for \(2\le p\le4\) and gives other linear upper bounds; it predates Xiong's construction.
* Swanepoel's earlier Kusner work and Swanepoel--Villa (2013) were checked as conceptual predecessors. The 2013 paper explicitly uses Hadamard matrices and derives \(O((2-p)^{-1})\)-type scales for a **different invariant**, the minimum size of a maximal equilateral set for \(p<2\). This weakens any claim that “Hadamard densification” itself is a novel idea, but it does not cover the present refinement of Xiong's \(p>4\) counterexample or the constant in (5).
* Paley's classical construction was checked through the original bibliographic record and standard descriptions.
* Current successful SCOPE records and recent repository changes were searched by `Kusner`, `equilateral`, `Hadamard`, `Paley`, and related claim-family terms; no overlapping SCOPE result was found before drafting.

### Residual access/indexing risk

The most relevant primary source, Xiong 2609.14794, was fully accessible and read. Direct full-text retrieval of the Ge--Xu--Zhou and Chalmers arXiv PDFs was not available through one retrieval route during this cycle, although their abstracts/result summaries and Xiong's discussion of them were accessible. Because both papers predate Xiong's 13 Sep 2026 construction, they cannot literally contain a stated refinement of that later construction, but they could contain related quantitative devices. The main residual originality risk is therefore **recency and indexing lag**: Xiong's preprint is only days old, so an independent note or repository update may not yet be indexed.

Originality is asserted only **to the best of our knowledge**.

## Value

PASS. The result does more than vary a parameter: it identifies the local mechanism at the exact phase boundary \(p=4\), computes the first-order blow-up constant, and proves that asymptotically dense Hadamard orders attain the optimal first-order dimension inside the natural generalized Xiong template. It also yields an explicit global upper bound on the least dimension in which a Kusner violation must occur as \(p\downarrow4\).

The value is limited by the absence of a matching lower bound for arbitrary equilateral configurations; a different construction may be much smaller.
