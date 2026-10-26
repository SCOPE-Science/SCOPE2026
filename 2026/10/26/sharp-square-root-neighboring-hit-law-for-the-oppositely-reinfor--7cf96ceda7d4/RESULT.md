# Sharp square-root neighboring-hit law for the oppositely reinforced elephant walk

## Finding
Let \(S_s\) be the opposite-memory elephant random walk described below, started from zero at an even time \(k\ge 2\). Its first time \(H_k\) at the adjacent site \(-1\) has finite mean for each fixed \(k\), with the exact late-start scale
\[
\lim_{\substack{k\to\infty\\k\in2\mathbb N}}\frac{\mathbb E_k[H_k-k]}{\sqrt{k}}
=\frac{\sqrt{6/\pi}}{3} B\!\left(\frac16,\frac12\right)
=3.35633835981971\ldots.
\]
Here \(B\) denotes Euler's beta function. By reflection symmetry, the same theorem holds for first arrival at \(+1\). An exact time-and-space shift identifies the one-dimensional Friedman urn walk with this elephant process; hence its first return to the origin has finite expectation, as conjectured by Balaji and Mahmoud.

## Assumptions and scope
For each even integer \(k\ge2\), construct the discrete-time Markov chain \((S_s)_{s\ge k}\), started at \(S_k=0\), with jumps \(\pm1\) and transition
\[
\Pr(S_{s+1}=x+1\mid S_s=x)=\frac{s-x}{2s},\qquad
\Pr(S_{s+1}=x-1\mid S_s=x)=\frac{s+x}{2s}.
\]
Only reachable states with the appropriate parity and \(|x|\le s\) are used. Let \(R_k=\inf\{r\ge1:S_{k+r}=0\}\) be its next-zero excursion length, \(\mu(k)=\mathbb E_k R_k\), and \(H_k=\inf\{s>k:S_s=-1\}\). The bound and limit below concern passage to an adjacent level from the zero state, not an invariant distribution or homogeneous-state positive recurrence.

For the urn application, begin with exactly one white and zero blue balls. After each uniform draw, replace the sampled ball and add one ball of the opposite color. Define \(F_n\) as white draws minus blue draws among the first \(n\) draws, and \(T=\inf\{n\ge2:F_n=0\}\). The first draw is white, so \(F_1=1\).

## Proof
**1. Known, uniform excursion-tail input.** Bertoin's Theorem 4.1 [2] applies to opposite-memory walks, including \(p=0\), started from zero at any even time \(k\ge2\). In that case his normalization is \(a_j=j-1\) for \(j\ge2\), and \(A_j=\sum_{r=1}^j(r-1)^2\). His theorem gives, uniformly when \(k\le n\),
\[
\Pr_k(R_k>n)\sim\sqrt{\frac2\pi}\frac{k}{\sqrt{A_{k+n}-A_k}}
\qquad(n\to\infty).
\]
Consequently, for some finite universal \(C\), whenever \(n\ge k\ge2\),
\[\Pr_k(R_k>n)\le Ck n^{-3/2}.\tag{1}\]
For the complementary regime, condition on the first jump of the excursion. On the positive side, the outward jump probability at position \(x>0\) is \((s-x)/(2s)\le1/2\); on the negative side the reflected process obeys the identical inequality. A monotone coupling with a simple symmetric random walk starting from \(1\) shows the excursion duration is stochastically no greater than the corresponding symmetric-walk return time. The elementary reflection/ballot bound gives
\[\Pr_k(R_k>n)\le C(n+1)^{-1/2},\qquad n\ge1.\tag{2}\]
Summing (1) and (2) over \(n\ge0\) with the split at \(k\) yields
\[\mu(k)=\mathbb E_k R_k\le C\sqrt{k}<\infty.\tag{3}\]
The finite exceptional values not covered by the asymptotic uniformity in (1) are absorbed into \(C\).

**2. Sharp excursion mean.** For each fixed \(t>0\), the same theorem, with \(n=\lfloor kt\rfloor\), gives
\[
\sqrt{k}\Pr_k(R_k>\lfloor kt\rfloor)
\longrightarrow\sqrt{\frac6{\pi[(1+t)^3-1]}}.
\]
For \(t\le1\), (2) dominates the rescaled tail by \(Ct^{-1/2}\); for \(t\ge1\), (1) dominates it by \(Ct^{-3/2}\). Both are integrable on their respective ranges, so the tail-integral identity and dominated convergence show
\[
\lim_{\substack{k\to\infty\\k\text{ even}}}\frac{\mu(k)}{\sqrt k}
=\sqrt{\frac6\pi}\int_0^\infty\frac{dt}{\sqrt{(1+t)^3-1}}
=\frac{\sqrt{6/\pi}}3 B\!\left(\frac16,\frac12\right)=:c_*.
\tag{4}
\]
The beta identity follows from \(u=(1+t)^{-3}\).

**3. A geometric number of zero excursions.** At each return to zero, the subsequent jump is negative or positive with probability \(1/2\) each. Negative ends the search for \(-1\), while a positive jump begins a complete positive excursion back to zero. Reflection symmetry makes the conditional duration of a positive excursion equal in distribution to \(R_k\). Construct independent fair choices, plus hypothetical successive positive-excursion return times \(K_0=k\), \(K_{j+1}=K_j+R_{K_j}^{(j)}\), where the conditional law of \(R_{K_j}^{(j)}\), given \(K_j\), is the ordinary next-zero duration. All the \(K_j\) are even. The number \(N\) of positive excursions before a negative initial jump is geometric with \(\Pr(N=j)=2^{-(j+1)}\), independent of their durations. Therefore
\[
\mathbb E_k(H_k-k)=1+\sum_{j\ge0}2^{-(j+1)}\mathbb E\mu(K_j).\tag{5}
\]
Write \(u_j=\mathbb E K_j\). By (3) and Jensen,
\[
u_{j+1}\le u_j+C\sqrt{u_j},\qquad
\sqrt{u_j}\le\sqrt{k}+Cj/2.
\]
Thus \(\mathbb E\mu(K_j)\le C(\sqrt{k}+Cj/2)\). The geometric sum in (5) is finite and gives \(\mathbb E_k(H_k-k)<\infty\). For each fixed \(j\), the same inequality shows \((K_j-k)/k\to0\) in \(L^1\) as \(k\to\infty\). Equation (4), uniformly across all even return epochs at least \(k\), and the bound (3), imply
\[
\frac{\mathbb E\mu(K_j)}{\sqrt{k}}\longrightarrow c_*.
\]
The summable majorant \(C2^{-(j+1)}(1+Cj/2)\) permits dominated convergence in (5). Since \(\sum_{j\ge0}2^{-(j+1)}=1\), the asserted sharp limit follows.

**4. Exact shift of the Friedman walk.** At time \(n\ge1\), the urn has \((n-F_n)/2+1\) white balls and \((n+F_n)/2\) blue balls. Hence
\[
\Pr(F_{n+1}=x+1\mid F_n=x)=\frac{n+2-x}{2(n+1)}.
\]
Set \(S_s=F_{s-1}-1\) for \(s\ge2\). With \(s=n+1\) and \(S_s=x-1\), the preceding equation reduces exactly to \((s-S_s)/(2s)\), and \(S_2=0\). A first return \(F_n=0\) is precisely \(S_{n+1}=-1\), giving \(T=H_2-1\) and, by the already proved finiteness, \(\mathbb ET<\infty\).

## Verification
The standalone `VERIFY.py` uses rational arithmetic to compare the urn first-return survival probabilities with the shifted elephant nearest-level survival probabilities through a finite horizon; it also independently checks the urn's Eulerian-number one-time marginals. Run with `python VERIFY.py`, using only the Python standard library. These finite tests confirm the shift and combinatorial probabilities but do not establish (1), (4), or the infinite-time limit, which depend on the cited uniform theorem and the analytical summability argument.

## Relationship to prior work
Balaji and Mahmoud [1, Section 5] conjecture finite mean for the one-dimensional Friedman first return, based on simulations, and supply the urn's Eulerian marginal law. Bertoin [2, Theorem 4.1 and Eq. (5.6)] proves the crucial uniform zero-excursion tail and fixed-ratio tail profile; that result is used, not re-claimed, here. The new object is the adjacent-level hitting time rather than first return to zero, obtained by summing a random geometrically terminated sequence of time-dependent zero excursions; its precise mean asymptotic and the exact urn shift answer the posed question. Coletti and Papageorgiou [3, Theorem 3.2] discuss positive recurrence of the ordinary elephant walk and provide an asserted starting-time-uniform first-return bound. Their assertion has a different target and, interpreted uniformly in starting time, conflicts with [2, Eq. (5.6)]; it is not used as a premise or claimed as a proof of the present scale.

## Limitations
The sharp asymptotic concerns only the fully opposite-memory case and even late starts from zero. The Friedman consequence assumes one initial white ball, opposite-color unit reinforcement and the first return from the initial origin. No exact value of \(\mathbb ET\), two-dimensional finite-mean conclusion, uniform mixing law, or invariant probability distribution is asserted. The key excursion-tail theorem is quoted as an established result, rather than reproved. Older equivalent treatments of the adjacent-level entrance time have not been excluded exhaustively; independent validation has not been performed.

## References
[1] S. Balaji and H. Mahmoud, *Urn-driven random walks*, arXiv:2504.14813, first submitted 2025-04-21; Section 5 and Section 4. https://arxiv.org/abs/2504.14813

[2] J. Bertoin, *Counting the zeros of an elephant random walk*, arXiv:2105.09569v2 (2022), Theorem 4.1, Eq. (5.6), Section 5. https://arxiv.org/html/2105.09569v2

[3] C. F. Coletti and I. Papageorgiou, *Asymptotic Analysis of the Elephant Random Walk*, arXiv:1910.03142v4 (2020), Theorems 3.1–3.2. https://arxiv.org/html/1910.03142v4
