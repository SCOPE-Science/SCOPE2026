# Opposite cycle–source dependence and a critical three-cycle scale in loopless random mappings

## Finding
Let \(n\ge3\). Independently for each \(i\in[n]\), choose \(F(i)\) uniformly from \([n]\setminus\{i\}\). Let \(Z\) count vertices of indegree zero in the resulting functional digraph, and let \(C_k\) count directed simple cycles with \(k\) distinct vertices, for \(2\le k\le n\). Define \(b=(n-2)/(n-1)\) and \((n)_{\underline{k}}=n!/(n-k)!\).

For any specified directed \(k\)-cycle \(\Gamma\), the full conditional law of \(Z\) is determined by the exact factorial moments
\[
\mathbb E[(Z)_{\underline{t}}\mid\Gamma\subseteq F]
=(n-k)_{\underline t}\left(\frac{n-t}{n-1}\right)^t
\left(\frac{n-t-1}{n-1}\right)^{n-k-t},
\quad0\le t\le n-k.
\]
Here \((Z)_{\underline 0}=1\); these moments determine the finite probability generating function by \(\mathbb E[s^Z\mid\Gamma]=\sum_{t=0}^{n-k}\mathbb E[(Z)_{\underline t}\mid\Gamma](s-1)^t/t!\).

In particular the exact covariance is
\[
\operatorname{Cov}(Z,C_k)
=\frac{(n)_{\underline k}}{k(n-1)^k}
 b^{n-k-1}\bigl((n-k)-n b^k\bigr).
\tag{1}
\]
Its sign has a sharp, all-size dichotomy:
\[
\operatorname{Cov}(Z,C_2)>0,\qquad
\operatorname{Cov}(Z,C_k)<0\ \text{for every }3\le k\le n.
\tag{2}
\]
For each *fixed* \(k\), three distinct asymptotic regimes occur:
\[
\operatorname{Cov}(Z,C_2)\sim\frac{1}{2e n},\qquad
\operatorname{Cov}(Z,C_3)\sim-\frac{2}{3e n^2},\qquad
\operatorname{Cov}(Z,C_k)\sim-\frac{k-3}{2e n}\quad(k\ge4).
\tag{3}
\]
The three-cycle covariance uniquely decays an extra power of \(n\), compared with every other fixed admissible cycle length.

## Assumptions and scope
The mapping is sampled uniformly from all \((n-1)^n\) self-maps with no fixed points; its vertex choices are independent. A directed cycle of length two is allowed, and each cyclic rotation denotes the same cycle. Indegree zero, not outdegree zero, defines a source vertex. The sign statement holds for every integer \(n\ge3\), with \(2\le k\le n\); the asymptotics keep \(k\) fixed as \(n\to\infty\). The conditional factorial-moment statement concerns a *prescribed* cycle event, not conditioning on \(C_k\ge1\).

## Proof
Fix a directed cycle \(\Gamma\) using \(k\) specified vertices. Its probability is \((n-1)^{-k}\). In its presence all \(k\) cyclic vertices have positive indegree and the remaining \(n-k\) mapping choices are independent and loopless. Fix \(t\) distinct vertices among the complement. For each of those \(t\) vertices, avoiding all \(t\) targets has probability \((n-t)/(n-1)\), because its own label is already excluded as a possible image. For each of the other \(n-k-t\) free vertices, avoiding the same targets has probability \((n-t-1)/(n-1)\). The \(k\) prescribed cycle edges never enter the chosen targets. Multiply and sum over the \((n-k)_{\underline t}\) ordered lists to obtain the conditional factorial-moment formula. A finite-support random variable is determined by these moments through the stated generating-function inversion.

Exactly \((n)_{\underline k}/k\) different directed \(k\)-cycles are possible, so linearity gives
\[
\mathbb E C_k=\frac{(n)_{\underline k}}{k(n-1)^k}.
\]
A fixed vertex receives no image from any of the other \(n-1\) vertices with probability \(b^{n-1}\); it cannot map to itself. Hence \(\mathbb E Z=n b^{n-1}\). The \(t=1\) conditional factorial moment is \(\mathbb E[Z\mid\Gamma]=(n-k)b^{n-k-1}\). Multiplying by the probability of each cycle, summing over all cycles, and subtracting \(\mathbb E Z\mathbb E C_k\) proves (1).

Set \(g_n(k)=(n-k)-n b^k\). Direct rational algebra gives
\[
 g_n(2)=\frac{n-2}{(n-1)^2}>0,\qquad
 g_n(3)=\frac{3-2n}{(n-1)^3}<0.
\]
For integer \(k\ge1\),
\[
 g_n(k+1)-g_n(k)=-1+\frac{n}{n-1}b^k
 \le -1+\frac{n(n-2)}{(n-1)^2}
 =-\frac{1}{(n-1)^2}<0.
\]
Every other factor in (1) is strictly positive, including when \(k=n\), proving (2).

For fixed \(k\), \(\mathbb E C_k=1/k+O_k(n^{-1})\) and \(b^{n-k-1}=e^{-1}(1+O_k(n^{-1}))\). Taylor expansion yields \(g_n(k)=k(3-k)/(2n)+O_k(n^{-2})\); at the critical length \(k=3\), its exact expression above instead gives \(g_n(3)=-2/n^2+O(n^{-3})\). At \(k=2\), \(g_n(2)=1/n+O(n^{-2})\). Substituting into (1) proves (3).

For contrast, if self-images are instead allowed with probability \(1/n\), then a fixed marked \(k\)-cycle has \(\mathbb E[Z\mid\Gamma]=(n-k)(1-1/n)^{n-k}\), while \(\mathbb E Z=n(1-1/n)^n\). For every \(k\ge2\), strict Bernoulli inequality \((1-1/n)^k>1-k/n\) makes this covariance strictly *negative*. Thus the positive two-cycle dependence in (2) is a genuine consequence of excluding self-loops, not a universal mapping property.

## Verification
Run `python verify.py` using Python 3 and only its standard library. The checker exhaustively enumerates every loopless mapping on \(n=3,4,5,6,7\) vertices, independently computes indegrees and all cycle counts, and compares exact rational means and covariances with (1). It separately enumerates maps constrained to contain prescribed cycles and checks every feasible conditional factorial moment. Finally it checks the exact signs and base rational identities for all \(3\le n\le200\), with every \(2\le k\le n\). It reports 40,314 passed exact assertions. These finite checks corroborate, but do not substitute for, the infinite-parameter proof above.

For illustration, \(\operatorname{Cov}(Z,C_2)=3/16\) and \(\operatorname{Cov}(Z,C_3)=-3/16\) at \(n=3\). At \(n=4\) the covariances for lengths two, three, four are \(8/81\), \(-40/729\), and \(-64/729\).

## Relationship to prior work
The classical random-mapping framework and its cycle/tree generating functions are developed by Flajolet and Odlyzko, *Random Mapping Statistics* (EUROCRYPT 1989 / LNCS 434, 1990), especially Section 5.1. That section explicitly discusses excluding length-one cycles, but not the displayed mixed source-count/cycle-length covariance or its exceptional three-cycle asymptotics. Hansen and Jaworski, *A New Random Mapping Model* (arXiv:math/0603529v1, March 22, 2006), describe independent-choice mappings with diagonal bias and the component structure of such models. Their introduction and final discussion, and the relevant published statements inspected, do not present this prescribed-cycle source-count factorial-moment law. These observations are comparisons with inspected text, not proof of historical priority. General marked generating-function methods could in principle recover this statement with further work.

## Limitations
The result concerns the uniform independent loopless model, not arbitrary dependent or nonuniform maps. It does not assert conditional stochastic domination of the source count given \(C_k\ge1\), or uniform-in-\(k\) asymptotics. Prior claims concerning cyclic *vertices* versus indegree-zero vertices, and claims concerning fixed points versus indegree-zero vertices in diagonally biased maps, do not imply the present cycle-length-resolved classification without an additional marked-cycle computation. Historical priority remains uncertain: complete texts of some early studies of local random-mapping structure, notably Harris (1960) and Berg–Jaworski (1992), were not available for decisive full-text comparison. A finite exact calculation alone is not evidence that this result is new.

## References
- Philippe Flajolet and Andrew M. Odlyzko, *Random Mapping Statistics*, Advances in Cryptology — EUROCRYPT '89, LNCS 434 (1990), pp. 329–354. DOI: https://doi.org/10.1007/3-540-46885-4_34 ; lawful author copy: https://www-users.cse.umn.edu/~odlyzko/doc/arch/random.mappings.pdf
- Jennie C. Hansen and Jerzy Jaworski, *A New Random Mapping Model*, arXiv:math/0603529v1 (publicly posted 2006-03-22), https://arxiv.org/abs/math/0603529
- Bernard Harris, *Probability Distributions Related to Random Mappings*, Annals of Mathematical Statistics 31 (1960), 1045–1062. DOI: https://doi.org/10.1214/aoms/1177705677 (historical source, full-text comparison unresolved).
- S. Berg and J. Jaworski, *Probability Distributions Related to the Local Structure of a Random Mapping*, in *Random Graphs* (1992), pp. 1–21 (historical source, full-text comparison unresolved).
