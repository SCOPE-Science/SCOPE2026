# same-model review

## Verdict

**PASS (same-model review only).** The contribution is assessed separately for correctness, originality to the best of our knowledge, and value. This is not independent validation or peer review.

## Correctness audit

The proof was attacked at the points most likely to conceal a circular boundedness assumption.

1. **No use of the target assumption in the accumulator dichotomy.** The identity
   \(S_{k+1}^2=S_k^2(1+\|d_k\|^2/\eta^2)\) is an exact algebraic consequence of Algorithm 1 in the deterministic setting. If \(S_k\) is bounded, it directly bounds every increment and, more strongly, makes \(\sum_k\|d_k\|^2<\infty\). This branch does not invoke Wang--Yurtsever Assumption 1.
2. **Unbounded accumulator branch.** If \(S_k\to\infty\), monotonicity of \(S_k\) gives a finite first index with \(S_k\ge L\eta\). From that index onward \(\alpha_k\le1/L\), so the deterministic proximal-gradient descent inequality yields \(F_{k+1}\le F_k-(L/2)\|d_k\|^2\). Boundedness below of \(F\) then bounds each tail increment. Only finitely many pre-threshold increments remain, and each is finite because the proximal subproblem is strongly convex and has a unique finite minimizer.
3. **Convex optimizer-distance inequality.** Starting from the two proximal optimality conditions and monotonicity of \(\partial h\), the proof obtains
   \[
   \|x_{k+1}-x^*\|^2-\|x_k-x^*\|^2
   \le (\alpha_kL/2-1)\|x_{k+1}-x_k\|^2.
   \]
   The critical step uses Baillon--Haddad cocoercivity for convex \(L\)-smooth \(f\), followed by an exact one-variable quadratic maximization. This inequality was also stress-tested numerically on randomized quadratic-plus-\(\ell_1\) composites.
4. **Bounded-\(S\) convex branch.** Square summability, not summability, of the increments is sufficient because the distance recurrence is in squared norm and its positive drift is proportional to \(\|d_k\|^2\). Thus there is no hidden use of finite path length.
5. **Unbounded-\(S\) convex branch.** Once \(S_k\ge L\eta\), the same distance inequality has coefficient at most \(-1/2\), so optimizer distance is nonincreasing thereafter. The finite prefix is harmless.

The included compact script tests the one-step inequality on 10,000 randomized scalar quadratic-plus-\(\ell_1\) instances and simulates 200 accumulator trajectories for 2,000 steps each. Some random choices produce extremely large early steps, which is consistent with the theorem: the claim is existence of a finite bound for each run, not a small universal bound independent of the early trajectory. The proof does not depend on the computation.

### Correctness limitations

The argument does not cover stochastic gradients, convex nonsmooth \(f\), inexact proximal solves, or the accelerated Algorithm 2. It also does not provide a simple a priori numerical value of \(D\) in the unbounded-accumulator branch because the finite pre-threshold trajectory may be large.

## Originality audit

### Internal SCOPE overlap

At the beginning of the cycle and again before publication, the repository was searched for optimization, proximal-gradient, AdaGrad, gradient-mapping, bounded-iterate, and condition-number language, together with recent commits and current Phase II paths. No current SCOPE record covering this claim was found. GitHub text/code search can lag or miss semantic equivalents, so this is evidence against collision rather than a guarantee.

### External literature checked

- **Wang--Yurtsever, arXiv:2605.05944v1.** The full arXiv HTML was inspected. Algorithm 1 has exactly the accumulator identity used here. Its Assumption 1 explicitly requires bounded increments and, for convex \(F\), bounded optimizer distances. Its deterministic smooth Theorem 1 and deterministic convex-smooth Corollary 2 explicitly cite that assumption. The submission history currently shows only v1, dated 7 May 2026. No statement in the inspected paper makes Assumption 1 automatic in the deterministic smooth regimes.
- **Ye--Ma--Yang--Zhou, arXiv:2510.06079.** The abstract and accessible full-paper records were inspected. This work explicitly targets removal of bounded-iterate assumptions for nonconvex composite optimization, but it proposes a different adaptive proximal-gradient algorithm based on local upper/lower curvature estimates. It does not cover the exact gradient-mapping-accumulation rule analyzed here.
- **Bojovic--Salzo--Pontil, arXiv:2606.29893.** The accessible abstract/discussion was inspected. It explains a failure of classical gradient-accumulating AdaGrad on composite objectives and notes that gradient-mapping accumulation avoids that particular pathology. It does not state the boundedness-removal theorem proved here.
- Searches were made for the exact source title and arXiv identifier combined with `bounded iterates`, `Assumption 1`, `redundant`, and `gradient mapping accumulation`, and for synonymous formulations such as bounded successive differences and automatic/self-bounding iterates. No covering statement was located.
- Broader adaptive proximal-gradient literature was checked for stronger general results. Methods without bounded-iterate assumptions exist, but the located ones use different stepsize rules or line-search/curvature mechanisms. Those results do not imply that the specific Wang--Yurtsever accumulator automatically satisfies its own Assumption 1.

### Equivalence and stronger-result check

The claim was checked against standard forward--backward theory. For a prescribed stepsize \(\alpha\le 1/L\), boundedness/Fejer properties are standard. That alone does not imply the present theorem because Algorithm 1 permits arbitrarily large initial stepsizes and the threshold crossing is endogenous. The new point is the two-branch argument connecting the accumulator update to eventual safe stepsizes or square-summable motion. No stronger located theorem was found that directly specializes to this exact adaptive recursion and removes both parts of Assumption 1.

### Uninspected sources and residual risk

No specific inaccessible paper was identified as likely to contain the exact theorem. The main residual risks are ordinary indexing/citation-graph incompleteness and the possibility that an equivalent argument appears in a source using different adaptive-stepsize terminology. A Semantic Scholar route from the arXiv page did not expose a usable citation record through the available interface, so citation-graph coverage was incomplete. This is recorded as residual uncertainty, not as evidence of originality.

Given the explicit assumption in the current primary source, the exact algorithm-specific proof above, and the absence of located equivalent coverage, originality is assessed **PASS to the best of our knowledge**.

## Value audit

The result removes a named boundedness hypothesis from two deterministic smooth guarantees of a recent universal adaptive proximal-gradient method without altering the algorithm. This matters because bounded-iterate assumptions are explicitly recognized as a limitation in contemporary parameter-free composite optimization, and alternative methods have been designed to avoid them. The theorem also supplies a reusable structural explanation: the same accumulator that controls the stepsize yields either square-summable motion or eventual entry into the classical safe stepsize regime.

The contribution does not improve the optimal first-order complexity scale and is narrower than algorithms designed from the outset to work without boundedness assumptions. Its value is therefore structural and assumption-sharpening rather than a new complexity record. Within that scope it is assessed as substantive rather than a routine parameter variation.
