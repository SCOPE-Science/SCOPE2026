# An arcsine concentration law for minimum-rank delegations between two gurus

## Finding

**Theorem (sharp rank-versus-concentration tradeoff).** Let \(n\ge 1\) non-casting voters occupy the interior vertices \(1,\ldots,n\) of the undirected path \(0-1-\cdots-n-(n+1)\). Vertices \(0\) and \(n+1\) cast votes. Each interior voter may delegate to either immediate neighbor and, independently with probability \(1/2\) each, ranks the left or right neighbor first. A *branching* assigns one outgoing edge to each interior voter so that all selected paths reach a casting voter. Its Borda cost is the sum of the chosen edge ranks (one or two). Write \(C_n^*\) for the minimum Borda cost minus \(n\), i.e. the minimum number of second-choice delegations, and \(K_n\) for the number of interior vertices ultimately represented by the left casting voter under a minimum-cost branching.

1. Every branching is determined by a cut \(k\in\{0,\ldots,n\}\): the first \(k\) interior voters delegate left, and the remaining \(n-k\) delegate right. If \(X_i=+1\) when voter \(i\) prefers right and \(X_i=-1\) otherwise, and \(S_0=0\), \(S_k=\sum_{i=1}^kX_i\), then its number of second-choice delegations is \(\#\{i:X_i=-1\}+S_k\). Thus the optimal cuts are exactly the times at which the simple symmetric walk \((S_k)_{k=0}^n\) attains its global minimum.

2. For the *leftmost optimal cut* \(K_n=\min\{k:S_k=\min_{0\le j\le n}S_j\}\), its exact distribution is
\[
\Pr(K_n=k)=2^{-n}b_k\binom{n-k}{\lfloor(n-k)/2\rfloor},\qquad 0\le k\le n,
\]
where \(b_0=1\) and \(b_k=\binom{k-1}{\lfloor(k-1)/2\rfloor}\) for \(k\ge1\).

3. **Regardless of how ties among minimum-cost branchings are resolved**, even by randomized tie-breaking depending on the entire preference profile, their cut location satisfies
\[
\frac{K_n}{n}\ \Longrightarrow\ \operatorname{Beta}(1/2,1/2),
\qquad \Pr(\operatorname{Beta}(1/2,1/2)\le x)=\frac{2}{\pi}\arcsin\sqrt{x}\quad(0\le x\le1).
\]
The two casting voters have voting weights \(K_n+1\) and \(n-K_n+1\). Consequently,
\[
\lim_{n\to\infty}\Pr\left(\frac{\max\{K_n+1,n-K_n+1\}}{n+2}\ge\frac34\right)=\frac23.
\]
By contrast, breadth-first delegation (BFD), which chooses shortest paths and breaks any equal-length tie by rank, has casting-voter weights differing by at most one, for every preference profile.

4. Let \(p_n=\mathbf 1_{\{2\mid n\}}2^{-n}\binom n{n/2}\) and \(A_n=n2^{1-n}\binom{n-1}{\lfloor(n-1)/2\rfloor}\). Then
\[
\mathbb E C_n^*=\frac n2-A_n+\frac{1-p_n}{2}
=\frac n2-\sqrt{\frac{2n}{\pi}}+\frac12+O(n^{-1/2}).
\]
For BFD the expected number of second-choice edges is exactly \(\lfloor n/2\rfloor\). Thus the gain in expected rank satisfaction from globally minimum-rank delegation is \(\sqrt{2n/\pi}+O(1)\), despite the nonvanishing probability of severe guru-weight concentration.

## Assumptions and scope

The network is a path with exactly the two endpoints casting directly and every interior vertex delegating. Every interior vertex has precisely two allowable outgoing edges, one to each neighbor, and ranks these two edges distinctly. Different voters' ranking orientations are mutually independent and equiprobable. Both endpoints are absorbing and have no outgoing edges. There are no abstainers or isolated voters. All branching edges have rank cost \(1\) or \(2\); every branching has exactly \(n\) edges, so minimizing total ranks is equivalent to minimizing the count of second-choice edges. The finite formula in item 2 uses the smallest optimal cut. Items 1, 3 and 4 do not require that tie-break. A casting-voter weight counts their own vote plus all votes reaching them. No statement about ballots cast, election outcomes, strategic incentives, or heterogeneous trust is made.

## Proof

**Step 1: branchings are cuts.** Each interior voter chooses a left or right arrow. If some adjacent pair points toward each other, it is a directed two-cycle and cannot reach a casting voter. Conversely, if the chosen arrows contain no such pair, all left arrows necessarily precede every right arrow, so the choices are \(\mathrm L^k\mathrm R^{n-k}\); each arrow chain then reaches an endpoint. Every feasible branching has this form. A left arrow is second-choice exactly when the corresponding \(X_i=+1\), and a right arrow is second-choice exactly when \(X_i=-1\). For cut \(k\), its excess cost is
\[
C(k)=\#\{i\le k:X_i=+1\}+\#\{i>k:X_i=-1\}
=\#\{i:X_i=-1\}+S_k.
\]
This proves item 1, including all possible minimizing branchings.

**Step 2: exact first-minimum law.** Let \(T\) be the earliest global minimum time of \(S_0,\ldots,S_n\). The event \(T=k\) requires \(S_j>S_k\) for all \(j<k\) and \(S_j\ge S_k\) for all \(j>k\). Reverse the first \(k\) increments and change their signs. They form an independent simple symmetric walk required to be strictly positive at all positive times through \(k\). The last \(n-k\) increments independently form a walk required to be nonnegative at all times. The reflection principle counts the nonnegative length-\(m\) sequences as \(\binom m{\lfloor m/2\rfloor}\). For positive length \(k\), strict positivity forces a first upward step and reduces to a nonnegative walk of length \(k-1\), counted by \(\binom{k-1}{\lfloor(k-1)/2\rfloor}\). The two independent segment counts give item 2, including \(k=0\) by the convention \(b_0=1\).

**Step 3: arcsine law independent of tie-break.** Piecewise-linearly interpolate \(S_{\lfloor nt\rfloor}/\sqrt n\) on \([0,1]\). The standard functional central limit theorem (Donsker) gives convergence in law in \(C[0,1]\) to standard Brownian motion. Brownian motion has almost surely a unique location of its minimum on this compact interval; at each such continuous path, the correspondence that selects *any* global minimizer is continuous in the location coordinate under uniform convergence. Therefore every selection from the finite walk's minimizing time set, including any random tie-break, has the same weak limit: the time of Brownian motion's minimum. Lévy's classical arcsine theorem identifies its distribution as the displayed beta law. The continuous limit assigns no mass to the thresholds \(1/4\) or \(3/4\). The maximum casting-voter share is \(\max\{K_n+1,n-K_n+1\}/(n+2)\), hence its limit event is \(\{U\le1/4\}\cup\{U\ge3/4\}\). The arcsine CDF gives probability \(2(2/\pi)\arcsin(1/2)=2/3\). Under BFD all voters use their nearest endpoint except the possible single central equal-distance voter; this creates a middle cut, so the endpoint weights differ by at most one.

**Step 4: exact cost expectation.** By Step 1,
\[
C_n^*=\#\{i:X_i=-1\}+\min_{0\le k\le n}S_k.
\]
The first summand has mean \(n/2\). By reflection symmetry of the walk, the minimum has the negative expectation of \(M_n=\max_{0\le k\le n}S_k\). For positive integers \(h\), the reflection principle implies \(\Pr(M_n\ge h)=\Pr(S_n\ge h)+\Pr(S_n>h)\). Summing over \(h\ge1\) yields
\[
\mathbb E M_n=\mathbb E|S_n|-\Pr(S_n>0).
\]
The elementary binomial identity \(\mathbb E|S_n|=n2^{1-n}\binom{n-1}{\lfloor(n-1)/2\rfloor}=A_n\), together with symmetry \(\Pr(S_n>0)=(1-p_n)/2\), gives the exact formula. Stirling's expansion of central binomial coefficients gives \(A_n=\sqrt{2n/\pi}+O(n^{-1/2})\) and \(p_n=O(n^{-1/2})\), proving the asymptotic expansion. In BFD every noncentral interior vertex delegates to its unique closer endpoint, while a central voter when \(n\) is odd delegates to their first-ranked neighbor. Exactly \(n\) (even case) or \(n-1\) (odd case) of the edge choices are unbiased against their predetermined direction, giving expected excess cost \(\lfloor n/2\rfloor\).

## Verification

The independent standard-library program `verify_branching.py` checks every one of the \(2^n\) possible preference profiles for each \(1\le n\le15\), totaling \(65{,}534\) profiles. It computes every cut's second-choice cost directly, independently computes the walk minimum, reconstructs the earliest-minimum histogram, compares it with the exact ballot formula, and compares the minimum and BFD expected costs against their closed forms using exact rational arithmetic. For \(1\le n\le8\), it additionally enumerates every possible edge-orientation assignment, detects directed cycles through path-following, and checks all \(4{,}096\) profile/feasible-branching pairs against the independent walk characterization. Run `python3 verify_branching.py` from the directory containing the program. These tests support the finite algebra and boundary conventions; the all-size and limiting claims follow from the preceding mathematical proof, not from finite enumeration.

## Relationship to prior work

Brill, Delemazure, George, Lackner and Schmidt-Kraepelin introduced ranked-delegation sequence rules and BordaBranching as minimum-rank confluent forests; they empirically identify a tension between minimizing local ranks and balancing voting weights (AAAI 2022, §§2–3.3, 5–6). Utke and Schmidt-Kraepelin analyze *mixed* Borda branching, random walks on the delegation graph, and efficient computations for **a fixed ranked instance** (NeurIPS 2023, §§2–6). Neither work, in the inspected relevant portions, states the two-terminal path's simple-walk minimizer correspondence, the law after **independent random ranking preferences**, the finite first-minimum ballot distribution, or the asymptotic two-thirds concentration event. Donsker's invariance principle and the random-walk/Brownian arcsine law are classical and are used explicitly, not claimed as new. The addition is their proved application to a Borda-cost-optimal delegation mechanism and the sharp rank-versus-concentration comparison with BFD. General minimum-cost branching algorithms solve each realized instance but do not themselves supply the random-preference law and its macroscopic concentration probability.

## Limitations

The exact ballot distribution assumes independent fair first-choice ranks and leftmost optimal-cut tie-breaking. The limiting arcsine result is tie-break invariant **within the set of minimum-rank branchings**, not for arbitrary delegation rules. It does not assert that positional tie-breaking satisfies anonymity or copy-robustness; nor is the random-preferring regime the same as the 2023 paper's randomized mixture over optimum branchings for each fixed profile. Only two terminal gurus on a path are analyzed. Heterogeneous ranking probabilities, more gurus, added edges, or nonpath graphs can change the law. The statistical model is theoretical rather than a calibrated empirical description of voters. Published priority beyond inspected sources remains an open bibliographic risk, and no independent proof audit has been carried out.

## References

1. M. Brill, T. Delemazure, A.-M. George, M. Lackner and U. Schmidt-Kraepelin, *Liquid Democracy with Ranked Delegations*, first arXiv release 2021-12-14, arXiv:2112.07509v1; AAAI 2022, https://ojs.aaai.org/index.php/AAAI/article/view/20417/20176.
2. M. Utke and U. Schmidt-Kraepelin, *Anonymous and Copy-Robust Delegations for Liquid Democracy*, arXiv:2307.01174 (2023); NeurIPS 2023, https://proceedings.neurips.cc/paper_files/paper/2023/file/dbb5180957513805ebeea787b8c66ac9-Paper-Conference.pdf.
3. W. Feller, *An Introduction to Probability Theory and Its Applications*, vol. I, 3rd ed., 1968, chapters on random walks and the arcsine law; classical reflection-principle and fluctuation identities.
4. R. A. Doney, *On the Maxima of Random Walks and Stable Processes and the Arc-Sine Law*, Bulletin of the London Mathematical Society 19 (1987), 177–182, https://doi.org/10.1112/blms/19.2.177.
