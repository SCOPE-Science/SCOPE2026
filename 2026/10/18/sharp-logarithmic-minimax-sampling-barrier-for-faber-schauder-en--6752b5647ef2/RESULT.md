# Sharp logarithmic minimax sampling barrier for Faber–Schauder energy spaces

## Finding

For every fixed \(1<p<\infty\), exact point evaluations of a member of the unit ball of the Faber–Schauder energy space \(\mathcal E^p([0,1])\) permit uniform recovery only at the logarithmic rate \((\log_2 n)^{-1/p}\). More sharply, let \(\mathfrak R_n(p)\) be the smallest worst-case \(C([0,1])\) error over **all deterministic methods** using at most \(n\) sequential point evaluations, with evaluation sites chosen adaptively and the reconstruction allowed to be nonlinear. For every integer \(n\ge2\), put \(M_n=\lfloor\log_2(n-1)\rfloor\) and \(m_n=\lceil\log_2(n+1)\rceil\). Then

\[
\frac{1}{2\bigl((m_n+1)^{1/p}+3/2\bigr)}
\le \mathfrak R_n(p)
\le \frac{1}{2(M_n+1)^{1/p}}.
\]

Consequently the **sharp optimal-recovery coefficient** is

\[
\boxed{\lim_{n\to\infty}(\log_2 n)^{1/p}\mathfrak R_n(p)=\frac12.}
\]

If \(\Pi_N\) denotes ordinary dyadic piecewise-affine interpolation from exactly \(2^N+1\) grid values, then, for every integer \(N\ge0\),

\[
\frac1{2\bigl((N+1)^{1/p}+3/2\bigr)}
\le \|I-\Pi_N:\mathcal E^p\to C([0,1])\|
\le \frac1{2(N+1)^{1/p}},
\]

and hence \(\lim_{N\to\infty}N^{1/p}\|I-\Pi_N\|=1/2\). In particular, the canonical inclusion \(\mathcal E^p\hookrightarrow C([0,1])\) is compact. The upper estimate for \(\Pi_N\), and thus the qualitative compactness consequence, are deductions from Kim's published dyadic tail estimate; the new assertion is their sharpness and the matching information-theoretic lower bound for arbitrary adaptive point-sampling methods.

## Assumptions and scope

All functions are real-valued and continuous on \([0,1]\). The same bounds hold with complex scalars. Fix \(1<p<\infty\). For integers \(m\ge0\) and \(0\le k<2^m\), define the elementary tent

\[
e_{m,k}(t)=2^{-m/2-1}\max\{1-2|2^mt-k-1/2|,0\}.
\]

It is supported on the dyadic interval \([k2^{-m},(k+1)2^{-m}]\), zero at both endpoints, and has height \(2^{-m/2-1}\). The Faber–Schauder expansion is

\[
f(t)=f(0)+(f(1)-f(0))t+\sum_{m=0}^\infty\sum_{k=0}^{2^m-1}\theta_{m,k}(f)e_{m,k}(t),
\]

where the unique coefficient is

\[
\theta_{m,k}(f)=2^{m/2}\bigl(2f((2k+1)2^{-m-1})-f(k2^{-m})-f((k+1)2^{-m})\bigr).
\]

Put \(a_{m,k}(f)=2^{-m/2}\theta_{m,k}(f)\), \(Z_f^{(p)}(-1)=2^{1-1/p}|f(1)-f(0)|\), and

\[
Z_f^{(p)}(m)=\Bigl(\sum_{k=0}^{2^m-1}|a_{m,k}(f)|^p\Bigr)^{1/p},\quad m\ge0,
\qquad
H_f(j)=\sum_{m=j}^\infty\max_{0\le k<2^m}|a_{m,k}(f)|,\quad j\ge0.
\]

The energy norm from [1] is

\[
\|f\|_{\mathcal E^p}=\|f\|_\infty
+\Bigl(\sum_{m=-1}^\infty Z_f^{(p)}(m)^p\Bigr)^{1/p}
+\Bigl(\sum_{j=0}^\infty H_f(j)^p\Bigr)^{1/p}.
\]

Only exact function values are counted; computation and the complexity of representing the output are unrestricted. Adaptive methods are deterministic; no assertion is made for randomized average-error algorithms, noisy sampling, other coefficient norms, or recovery in a target norm other than the supremum norm. When the algorithm chooses a sampling site based on earlier observed values, the choice must be a deterministic function of that transcript.

## Proof

**Step 1: sharp upper envelope from the tail.** At any fixed point \(t\), at most one tent at a given level \(m\) is nonzero. Thus the uniform error after retaining the affine component and every tent of levels below \(N\) is bounded by

\[
\|f-\Pi_Nf\|_\infty\le \frac12\sum_{m=N}^\infty\max_k|a_{m,k}(f)|=\frac12H_f(N).
\]

This is also the dyadic truncation estimate of [1, Proposition 3.24]. The numbers \(H_f(j)\) are nonnegative and nonincreasing. It follows without hidden constants that

\[
(N+1)H_f(N)^p\le\sum_{j=0}^{N}H_f(j)^p\le\|f\|_{\mathcal E^p}^p.
\]

Consequently \(\|I-\Pi_N\|\le1/[2(N+1)^{1/p}]\). Furthermore, \(\Pi_N\) uses precisely \(2^N+1\) predetermined point values and has finite-dimensional range. Uniform norm-operator convergence \(\Pi_N\to I\) establishes compactness of the inclusion.

**Step 2: normalized single-tent identity.** Fix \(m\ge0\) and \(0\le k<2^m\), and let \(g=e_{m,k}\). By Faber–Schauder biorthogonality its only nonzero coefficient is \(\theta_{m,k}(g)=1\). Its affine coefficient vanishes. Hence

\[
\|g\|_\infty=2^{-m/2-1},\quad
\|Z_g^{(p)}\|_{\ell_p}=2^{-m/2},\quad
H_g(j)=\begin{cases}2^{-m/2}&0\le j\le m,\\0&j>m.\end{cases}
\]

In particular,

\[
\|g\|_{\mathcal E^p}=2^{-m/2}\bigl((m+1)^{1/p}+3/2\bigr),
\qquad
\left\|\frac{g}{\|g\|_{\mathcal E^p}}\right\|_\infty
=\frac1{2\bigl((m+1)^{1/p}+3/2\bigr)}.
\]

When \(m=N\), the tent is identically zero at the dyadic level-\(N\) interpolation nodes. Therefore \(\Pi_Ng=0\). This proves the claimed lower operator-norm bound for every \(N\), not only asymptotically.

**Step 3: an adaptive information obstruction.** Fix an arbitrary deterministic procedure making at most \(n\) sequential point queries. Feed the procedure the identically zero function. Record the resulting list of query sites and its final output \(y\). Let \(m=\lceil\log_2(n+1)\rceil\). Since \(2^m>n\), at least one of the \(2^m\) open dyadic level-\(m\) intervals contains none of those query sites. Call its index \(k\). Define \(h=e_{m,k}/\|e_{m,k}\|_{\mathcal E^p}\). Both \(h\) and \(-h\) vanish at every query site of the zero-function transcript. By induction over queries, the procedure receives an identical sequence of answers on \(h\), \(-h\), and the zero function; adaptivity cannot distinguish them. It must therefore return the same output \(y\) for both signs. The triangle inequality gives

\[
\max\{\|h-y\|_\infty,\|-h-y\|_\infty\}\ge\|h\|_\infty
=\frac1{2\bigl((m+1)^{1/p}+3/2\bigr)}.
\]

Because the procedure was arbitrary, this proves the lower bound for \(\mathfrak R_n(p)\). Choose \(N=M_n=\lfloor\log_2(n-1)\rfloor\) to spend at most \(n\) queries on \(\Pi_N\); Step 1 proves the upper bound.

**Step 4: extract the exact constant.** Both \(m_n\) and \(M_n\) equal \(\log_2 n+O(1)\). Multiplying the bounds from Steps 1 and 3 by \((\log_2 n)^{1/p}\) and applying the squeeze theorem yields the asserted limit \(1/2\). The matching asymptotic for \(\Pi_N\) follows directly from Steps 1–2.

## Verification

The proof uses the explicit tent normalization, coefficient biorthogonality, nonincreasing tail sequence, the zero-transcript adversary, and the elementary asymptotics of base-two logarithms. These are exact arguments; no finite experiment is used as an infinite-dimensional certificate. A standalone standard-library checker supplied with the finding tests the finite tent identities, interpolation-node vanishing, and numerical lower/upper envelopes for multiple levels and exponents. These diagnostics do not replace the four proof steps.

## Relationship to prior work

Kim [1] introduced the exact energy norm and proved the uniform dyadic truncation estimate employed in Step 1; neither the upper estimate nor qualitative compact embedding is claimed as new. The contribution here is an exact asymptotic **optimal-recovery constant and lower bound against every deterministic adaptive point-query method** in this specific norm. Byrenheid–Stasyuk–Ullrich [2] study sampling recovery of borderline classes in \(L_q\), for finite \(q\), with different smoothness spaces and quantitative targets; their results do not state an exact supremum-norm information radius for this new energy class. Derevianko–Ullrich [3] analyze adaptive sampling using higher-order Faber splines under higher mixed regularity, rather than the zero-smoothness-tail norm used here. General theorems on logarithmic smoothness and information radii may offer alternate derivations; equivalence with existing information-based approximation results has not been independently certified.

## Limitations

The result concerns exact, deterministic worst-case recovery of functions on \([0,1]\) from point samples. It does not prove optimality for randomized algorithms under a probabilistic error criterion, noisy evaluations, or direct approximation of a pathwise integral. The sharp value depends on the precise original energy-norm normalization; equivalent renormings can change the constant. A historical priority risk remains from possible general optimal-recovery results for Besov-type or logarithmic-modulus spaces after a norm-preserving identification. No independent scientific audit has been performed.

## References

[1] Donghan Kim, *Pathwise integration beyond Young via Faber--Schauder energy spaces*, arXiv:2606.13331, first made public 2026-06-11, especially Definition 3.19 and Proposition 3.24. https://arxiv.org/abs/2606.13331

[2] Glenn Byrenheid, Serhii Stasyuk, and Tino Ullrich, *Sampling recovery for non-compact subclasses of \(L_\infty\)*, arXiv:2210.01704 (2022). https://arxiv.org/abs/2210.01704

[3] Nadiia Derevianko and Tino Ullrich, *Adaptive sampling recovery of functions with higher mixed regularity*, arXiv:2004.03556 (2020). https://arxiv.org/abs/2004.03556
