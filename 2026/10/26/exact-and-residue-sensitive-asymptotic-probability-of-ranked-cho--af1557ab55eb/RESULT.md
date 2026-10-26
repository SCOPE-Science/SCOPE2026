# Exact and residue-sensitive asymptotic probability of ranked-choice center squeeze

## Finding
Fix three alternatives on the single-peaked axis \(L<C<R\). Independently draw each of \(n=2r+1\) voters' strict rankings uniformly from the four rankings that are single-peaked on this axis. Let \(E_n\) be the event that instant-runoff voting (IRV, also called the Hare rule) **fails to elect the unique Condorcet winner regardless of every permitted first-elimination tie break**. For every positive odd \(n\), write \(p_n=\Pr(E_n)\). Then
\[
p_n=\frac{1}{4^n}\sum_{\substack{a,b,c\in\mathbb Z_{\ge0},\ a+b+c=n\\ a,c\le r,\ b<a,\ b<c}}
\frac{n!}{a!\,b!\,c!}\,2^b.
\]
This is an exact formula at every finite electorate size. In particular, \(p_1=p_3=0\), \(p_5=15/256\), \(p_7=35/2048\), and \(p_9=2835/65536\). For positive odd \(n\to\infty\) along each residue class \(s=n\bmod3\),
\[
\boxed{\displaystyle p_n\sim\frac{3\sqrt 3}{2\pi n}\left(\frac{27}{32}\right)^{n/3}K_s,\qquad
K_0=5,\quad K_1=6\,2^{-1/3},\quad K_2=8\,2^{-2/3}.}
\]
Thus the exact logarithmic rate is \(\lim_{n\to\infty,\ n\text{ odd}}n^{-1}\log p_n=-\frac13\log(32/27)\); the leading coefficient has an intrinsic three-class lattice dependence. The deterministic three-candidate center-squeeze mechanism is known; the stated finite-population risk and sharp residue-dependent constants are the contribution assessed here.

## Assumptions and scope
An electorate contains an odd, positive number \(n=2r+1\) of labeled, independent voters. The *axis is fixed and known*. Each voter selects independently and with probability \(1/4\) one of the ordered preference lists \(L\succ C\succ R\), \(C\succ L\succ R\), \(C\succ R\succ L\), and \(R\succ C\succ L\). This is the uniform fixed-axis single-peaked culture, also called Walsh's culture at three alternatives. It is not uniform over the six unrestricted rankings; it is not uniform over peak locations. IRV removes a candidate with the fewest currently first-ranked ballots, transfers these ballots to the highest remaining candidate, and elects a surviving majority choice. If any elimination tie occurs, every legal elimination order is considered. Event \(E_n\) means *every* such legal sequence elects someone other than the unique pairwise-majority Condorcet winner. The theorem does not assign a probability to an unspecified random tie-breaking convention.

## Proof
Let \(a,b,c\) be the numbers of ballots peaking respectively at \(L,C,R\). Every voter with an \(L\)-peak prefers \(L\) to \(C\), and every other voter prefers \(C\) to \(L\); similarly, exactly the \(c\) right-peaked voters prefer \(R\) to \(C\). Therefore \(C\) is the unique Condorcet winner exactly when \(a,c\le r\). If \(a>r\), then \(L\) is already a first-choice majority winner; if \(c>r\), then \(R\) is. Such a candidate cannot lose IRV.

When \(C\) is the Condorcet winner, eliminating either extreme first transfers that extreme's ballots to \(C\), which then defeats the remaining extreme in the final majority contest. Consequently an IRV failure happens precisely when the center is eliminated first. This happens under *all* legal tie-breaking orders precisely when \(b<a\) and \(b<c\). If \(b\) ties an extreme for fewest votes, at least one legal elimination removes that extreme first and elects \(C\). This proves the exact event characterization, including boundaries. Independent uniform rankings yield the peak-count law
\[
\Pr((a,b,c))=\frac{n!}{a!b!c!}\left(\frac14\right)^a
\left(\frac12\right)^b\left(\frac14\right)^c,
\]
since two of the four allowed rankings peak at \(C\). Summing over the established event proves the finite formula.

For the asymptotic, put \(u=a-b\ge1\), \(v=c-b\ge1\), and \(t=n/3\). Then \(b=(n-u-v)/3\), \(a=b+u\), \(c=b+v\), and integrality requires \(u+v\equiv n\pmod3\). Define \(R_n(u,v)=\Gamma(t+1)^3/(a!b!c!)\) when the integer counts are nonnegative and satisfy \(a,c\le r\), and \(R_n(u,v)=0\) otherwise. The exact formula becomes
\[
p_n=\frac{n!}{\Gamma(n/3+1)^3}\,2^{-5n/3}
\sum_{\substack{u,v\ge1\\u+v\equiv n\ (\mathrm{mod}\ 3)}}
2^{-(u+v)/3}R_n(u,v).
\]
Log-convexity of \(\Gamma\), applied to \(a+1,b+1,c+1\) with arithmetic mean \(t+1\), gives \(0\le R_n(u,v)\le1\). For any fixed positive \(u,v\) in the required residue class, all original constraints hold for sufficiently large \(n\) of that class, and the elementary fixed-offset gamma-ratio asymptotic gives \(R_n(u,v)\to1\). Since \(\sum_{u,v\ge1}2^{-(u+v)/3}<\infty\), dominated convergence gives a limiting sum \(K_s\).

With \(q=2^{-1/3}\), for \(s\in\{0,1,2\}\),
\[
K_s=\sum_{\substack{j\ge2\\j\equiv s\ (\mathrm{mod}\ 3)}}(j-1)q^j.
\]
For \(s=0\), this is \(\sum_{k\ge1}(3k-1)2^{-k}=5\). For \(s=1\), this is \(2^{-1/3}\sum_{k\ge1}3k2^{-k}=6\,2^{-1/3}\). For \(s=2\), this is \(2^{-2/3}\sum_{k\ge0}(3k+1)2^{-k}=8\,2^{-2/3}\). Finally Stirling's formula yields
\[
\frac{n!}{\Gamma(n/3+1)^3}\sim\frac{3^{n+3/2}}{2\pi n}.
\]
Combining with \(2^{-5n/3}\) proves the stated residue-class asymptotic. Each residue contains arbitrarily large odd integers, and all \(K_s>0\), giving the common logarithmic rate.

## Verification
Execute `python verify_center_squeeze.py` using Python's standard library, with no external data or package dependencies. The script evaluates the finite expression with exact integers, independently enumerates all \(4^n\) strict single-peaked ballot profiles for \(n=1,3,5,7\), determines their Condorcet winners by pairwise majority, and checks every first-round tie-breaking choice under IRV. It confirms favorable counts \((0,0,60,280)\) for these sizes and reports exact reduced probabilities through \(n=31\). It also checks finite truncations of the three analytic geometric series for \(K_s\). The deterministic all-\(n\) proof above establishes the theorem; the enumerations are independent finite cross-checks and not substitutes for the limit proof. The exact program output is in `verification_certificate.json`.

## Relationship to prior work
Black (1948) established the median-voter and single-peaked majority framework. The center-squeeze situation in three-candidate ranked-choice voting is explicitly analyzed in Correa-Lopera (2025), Proposition 3 and its proof: when the Condorcet center has the smallest first-place share, it is eliminated. The present result does **not** claim novelty for this observation. Tomlinson, Ugander and Kleinberg investigate moderation under a different continuous one-dimensional spatial model with a number of candidates varying, not this fixed three-alternative uniform-ballot population. Mousseau, Surugue and Wilczynski (2026) define the same uniform single-peaked ballot culture and analyze agreement for positional scoring rules; their cited quantitative bounds concern these rules rather than the IRV center-squeeze probability and its exact sharp coefficient. Lackner and Lackner (2017) count single-peaked profiles and distributions, not IRV failure conditional on a fixed axis. The distinct object here is the **finite-count exact risk plus the residue-specific sharp large-electorate asymptotic**. These comparisons do not constitute a proof of absolute bibliographic uniqueness.

## Limitations
The model fixes exactly three alternatives, an odd electorate, sincere and independent rankings, a common fixed single-peaked axis, and uniform probability over the four admissible ballots. The event demands failure for every possible first-elimination tie break; it does not count profiles where IRV failure is possible only under some tie-breaking choices. The formula and asymptotic need not hold under uniform peaks, anonymous impartial culture, unrestricted impartial culture, correlated or nonidentically distributed voters, or larger agendas. A broader comparison with older comprehensive voting-paradox compilations may reveal equivalent formulas under alternative terminology; independent bibliographic examination remains valuable. The original deterministically identified center squeeze is explicitly prior work.

## References
1. D. Black, “On the Rationale of Group Decision-Making,” *Journal of Political Economy* 56 (1948), 23–34, https://doi.org/10.1086/256633.
2. G. Correa-Lopera, “Ranked-choice voting versus first-past-the-post: how polarization shapes their performance,” *Public Choice* (2025), https://doi.org/10.1007/s40505-025-00297-x, especially Proposition 3 and appendix proof.
3. K. Tomlinson, J. Ugander, J. Kleinberg, “The Moderating Effect of Instant Runoff Voting,” arXiv:2303.09734, https://arxiv.org/abs/2303.09734.
4. V. Mousseau, H. Surugue, A. Wilczynski, “Agreement among Voting Rules under Single-Peaked Preference Distributions,” *Frontiers in Artificial Intelligence and Applications* (2026), https://doi.org/10.3233/FAIA251226.
5. M.-L. Lackner, M. Lackner, “On the likelihood of single-peaked preferences,” *Social Choice and Welfare* 48 (2017), 717–745, https://doi.org/10.1007/s00355-017-1033-0.
