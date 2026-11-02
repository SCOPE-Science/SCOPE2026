# Four-way rare–Gaussian factorization and a hidden covariance in random-to-top shuffling

## Finding

Fix any real \(c>0\), set \(r_n=\lfloor cn\rfloor\), and perform \(r_n\) independent uniform random-to-top moves on an initially ordered deck \((1,\ldots,n)\). At the end, let \(K_n\) be the number of cards selected at least once, \(F_n\) the number of fixed positions, and \(D_n\) the number of descents. The set \(S_n\) of moved labels occupies the first \(K_n\) positions in a uniform random order; the remaining labels appear in increasing order. Let \(U_n\) be the number of fixed positions among those first \(K_n\) positions, let \(J_n=n-\max S_n\) be the fixed-position suffix length, and let \(A_n\) be the number of descents internal to the first \(K_n\) positions. Thus \(F_n=U_n+J_n\) exactly.

Put
\[
\alpha=1-e^{-c},\qquad \tau^2=e^{-c}-(1+c)e^{-2c}>0.
\]
Then, as \(n\to\infty\),
\[
\boxed{
\left(U_n,J_n,\frac{A_n-(K_n-1)/2}{\sqrt n},\frac{K_n-n\alpha}{\sqrt n}\right)
\ \Longrightarrow\ (X,Y,G,H),
}
\]
where the FOUR variables on the right are mutually independent and
\[
X\sim\operatorname{Poisson}(\alpha),\qquad
\Pr(Y=j)=\alpha(1-\alpha)^j\quad(j=0,1,\ldots),\qquad
G\sim N(0,\alpha/12),\quad H\sim N(0,\tau^2).
\]
Consequently, with \(F=X+Y\),
\[
\left(F_n,\frac{D_n-n\alpha/2}{\sqrt n},\frac{K_n-n\alpha}{\sqrt n}\right)
\Longrightarrow (F,G+H/2,H),
\]
where \(F\) is independent of the Gaussian pair, and the two coordinates of that Gaussian pair have covariance \(\tau^2/2\). In particular, despite this asymptotic independence after Gaussian normalization, the **unscaled** covariance has a nonzero, strictly negative limit:
\[
\boxed{\lim_{n\to\infty}\operatorname{Cov}(F_n,D_n)
=\frac{\tau^2}{2}\left(1-\alpha^{-2}\right)<0.}
\]
The result is joint, not a claim about independent versions of the three deck statistics.

## Assumptions and scope

The parameter \(c\) is fixed and positive; the deck starts as the identity, each move selects one of the \(n\) labels uniformly and independently, and a selected label is moved to position one. A descent is an adjacent strictly decreasing pair in the resulting one-line deck. The normalization is \(\sqrt n\), not the stationary-mixing scale. The geometric distribution above counts failures before the first success. For large \(n\), \(r_n\ge1\), so \(K_n\ge1\). Statements concern \(n\to\infty\) with no coupled limit in \(c\).

## Proof

**1. Finite uniform-prefix coupling.** Conditional on \(K_n=k\), the selected set \(S_n\) is a uniform \(k\)-subset of \([n]\). Its cards appear at the top ordered by their most recent selection, and symmetry of the uniformly sampled labels makes this order a uniform permutation of \(S_n\), independent of \(S_n\). Unselected cards remain in their original relative order. The bottom cards fixed in their original positions are precisely the labels larger than \(\max S_n\); hence \(J_n=n-\max S_n\) and \(F_n=U_n+J_n\). For \(0\le j\le n-k\),
\[
\Pr(J_n=j\mid K_n=k)=\frac{\binom{n-j-1}{k-1}}{\binom nk}.
\]
For a set \(S\) of size \(k\), write \(M=|S\cap[k]|\). Uniform ordering gives, for each nonnegative integer \(\ell\),
\[
\mathbb E[(U_n)_\ell\mid S_n=S,K_n=k]=\frac{(M)_\ell}{(k)_\ell},
\]
with the ratio taken as zero when \(\ell>k\). These formulas are exact finite identities.

**2. Gaussian occupancy fluctuation.** With \(r_n\) independent uniform selections, \(K_n\) is the number of occupied boxes in the standard occupancy problem. Standard multinomial occupancy concentration yields \(K_n/n\to\alpha\) in probability. For completeness, poissonize with independent \(N_i\sim\operatorname{Poisson}(c)\): the pairs \((\mathbf1_{\{N_i>0\}},N_i)\) have covariance entries \(e^{-c}(1-e^{-c})\), \(ce^{-c}\), and \(c\). Conditioning on \(\sum_iN_i=r_n\), the full-span two-dimensional lattice local central limit theorem gives
\[
\frac{K_n-n\alpha}{\sqrt n}\Longrightarrow N\bigl(0,e^{-c}(1-e^{-c})-(ce^{-c})^2/c\bigr)=N(0,\tau^2).
\]
The support differences \((1,1)\) and \((0,1)\) span the integer lattice, so there is no hidden periodicity; the bounded discrepancy \(r_n-cn\) does not change the center or limit. This also follows from the classical occupancy theorem in the cited shuffle paper.

**3. Uniform conditional Poisson and geometric limits.** Whenever \(k/n\to\alpha\in(0,1)\), the finite maximum formula gives \(\Pr(J_n=j\mid K_n=k)\to\alpha(1-\alpha)^j\), uniformly for fixed \(j\) and \(k/n\) in a shrinking neighborhood of \(\alpha\). Conditional on \(J_n=j,K_n=k\), the selected set consists of \(n-j\) and a uniform \((k-1)\)-subset of \([n-j-1]\). Hence \(M/k\to\alpha\) in probability by the hypergeometric variance estimate; this is uniform for fixed \(j\) and central \(k\). The factorial-moment formula, bounded above by one at each fixed order, therefore tends to \(\alpha^\ell\). It follows that \(U_n\) tends conditionally to \(\operatorname{Poisson}(\alpha)\), with the limit not depending on \(j\) or central \(k\). These conditional limits, geometric tightness, and the occupancy CLT imply joint independence of \(U_n,J_n\), and the scaled occupancy fluctuation.

**4. Joint Gaussian independence.** Write \(A_n\) for descents of the random ordered prefix. Its relative-rank permutation is uniform on \(k\) letters, independent of the selected set; thus \(A_n\) is conditionally Eulerian and \(\{A_n-(k-1)/2\}/\sqrt n\) converges to \(N(0,\alpha/12)\) when \(k/n\to\alpha\). To establish independence from \(U_n\), condition on any \(\ell\) designated fixed prefix positions. The remaining \(k-\ell\) positions are filled by a uniform bijection of the remaining values. Deleting the fixed entries and relabeling the remaining values by rank changes the descent count by at most \(3\ell\). Therefore the centered, \(\sqrt n\)-scaled descent characteristic function has the same Gaussian limit uniformly over the designated positions and selected sets. Combining this with the exact conditional factorial moments gives, for \(z\in[0,1]\), real \(t\), fixed \(j\), and central \(k\),
\[
\mathbb E\left[z^{U_n}\exp\left(it\frac{A_n-(k-1)/2}{\sqrt n}\right)\middle|J_n=j,K_n=k\right]
\longrightarrow e^{\alpha(z-1)}e^{-\alpha t^2/24}.
\]
Indeed expand the probability generating function in falling factorial moments; the absolute values are dominated by \(\sum_{\ell\ge0}|z-1|^\ell/\ell!\), since each conditional factorial expectation is at most one. The limit factors independently of the suffix and occupancy fluctuation, proving the asserted four-way convergence.

**5. From prefix descents to all descents.** For \(K_n<n\), all descents outside the first \(K_n\) positions consist of the single boundary indicator \(B_n=\mathbf1_{\{\text{last moved label}>\text{smallest unmoved label}\}}\). For \(K_n=n\), set \(B_n=0\). Thus \(D_n=A_n+B_n\) and \(|B_n|\le1\). Slutsky's theorem gives the displayed joint law for \(F_n,D_n,K_n\).

**6. Nonzero unscaled covariance.** The finite conditional mean is
\[
 g_n(k)=\mathbb E(F_n\mid K_n=k)=\frac{k}{n}+\frac{n-k}{k+1}.
\]
For all \(1\le k\le n\), a direct endpoint-descent calculation gives
\[
\operatorname{Cov}(U_n,A_n\mid K_n=k)=\frac{1-k}{n(n-1)},\qquad
\operatorname{Cov}(J_n,A_n\mid K_n=k)=0.
\]
To verify the first identity, for an internal prefix position fixing its value changes the expected contributions of the two incident descents by opposite amounts. Only the first and last positions remain. The first contributes \(-1/(2n)\), and the last contributes \(((n-k)/(n-1)-1/2)/n\). Their sum is the claimed expression; the case \(k=1\) is zero separately.

The boundary fails with exact conditional probability \(\Pr(B_n=0\mid K_n=k)=1/(n-k+1)\) for \(k<n\), since the last moved card is uniform in the selected set and the expected count of selected labels below the smallest unselected label is \(k/(n-k+1)\). The same identity holds by convention for \(k=n\). Because \(K_n/n\to\alpha<1\), \(B_n\to1\) in probability. The second moments of \(F_n\) are uniformly bounded: \(\mathbb E[(U_n)_\ell\mid S_n]\le1\) for \(\ell\le2\), the suffix has a uniform geometric tail when \(K_n\ge\alpha n/2\), and the exceptional occupancy event has exponentially small probability by bounded-difference concentration. Hence \(\operatorname{Cov}(F_n,B_n)\to0\).

Using the law of total covariance and \(\mathbb E(A_n\mid K_n=k)=(k-1)/2\), we obtain
\[
\operatorname{Cov}(F_n,D_n)=\frac12\operatorname{Cov}(g_n(K_n),K_n)
+\frac{1-\mathbb EK_n}{n(n-1)}+o(1).
\]
For \(k\) of order \(n\), \(g_n'(k)=1/n-(n+1)/(k+1)^2\) and \(g_n''(k)=O(n^{-2})\). The occupancy variance is \(n\tau^2+o(n)\), its centered absolute third moment is \(O(n^{3/2})\) by bounded-difference concentration, and the atypical occupancy tails are exponentially small. Taylor's theorem therefore gives
\[
\operatorname{Cov}(g_n(K_n),K_n)=\tau^2(1-\alpha^{-2})+o(1),
\]
which proves the claimed strictly negative covariance limit.

## Verification

The standalone standard-library script `checks/checker.py` exhaustively compares complete finite random-to-top trajectory distributions with the distinct-selected-set/uniform-prefix construction for small sizes. It also checks exact hypergeometric means, suffix laws, conditional factorial moments, Eulerian order invariance, the exact conditional fixed-point/descent covariance, and the boundary-failure probability. Run `python checks/checker.py` from the package root. Its expected output is preserved in `checks/verification_output.txt`. The analytical occupancy CLT and mixed factorial-moment argument prove the limiting statements; finite checks are corroboration, not a substitute.

## Relationship to prior work

Clay's 2026 work gives the separate Poisson–geometric fixed-point limit, the separate Gaussian descent limit, and the uniform-prefix representation. Those components and the classical occupancy CLT are **not** claimed as new. The present result establishes their *joint* four-component factorization and determines a nonzero raw covariance invisible in the separate weak limits. Athanasiadis–Diaconis study hyperplane-walk functions, especially descent-set mixing, rather than this joint critical-time law; Pehlivan's work treats top-to-random card-position/guessing questions. A separate public mathematical record concerning uniform-permutation fixed-point/descent covariance treats a stationary uniform permutation, not a linear-time random-to-top deck. The joint theorem is not implied by marginal weak convergence; the new conditioning and bounded-deletion argument supplies the missing dependence analysis.

## Limitations

The theorem concerns fixed \(c>0\) and uniform card-selection probabilities. It does not establish a multivariate convergence rate, the full joint finite distribution, biased move-to-front shuffles, or a scaling in which \(c\) tends to zero or infinity with \(n\). The covariance limit requires a second-moment argument beyond weak convergence, and its proof is provided explicitly. Novelty is assessed against accessible sources rather than independently certified across all historical literature.

## References

1. A. Clay, *On the statistics of random-to-top shuffles*, arXiv:2603.09008, first submitted 2026-03-09, https://arxiv.org/abs/2603.09008. Relevant parts: Sections 3–6, especially the uniform-prefix construction, fixed-point limit, and descent CLT.
2. C. A. Athanasiadis and P. Diaconis, *Functions of random walks on hyperplane arrangements*, arXiv:0912.1686, 2009, https://arxiv.org/abs/0912.1686. Relevant parts: Section 5 on permutation walks and descent sets.
3. L. Pehlivan, *No Feedback Card Guessing for Top to Random Shuffles*, arXiv:1006.1321, 2010, https://arxiv.org/abs/1006.1321. Relevant parts: Introduction and card-position formulas.
4. A published mathematical record, *Boundary localization of fixed-point–descent dependence in a uniform permutation*, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-boundary-localization-of-fixed-point-descent-dependence-in-a-uni--6e228e1e9495. Compared only for its stated uniform-permutation covariance claim.
