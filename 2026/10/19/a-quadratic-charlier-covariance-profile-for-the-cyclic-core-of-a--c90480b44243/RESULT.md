# A quadratic Charlier covariance profile for the cyclic core of a uniform random mapping

## Finding
Let \(f:[n]\to[n]\) have independent uniformly distributed values. Let \(C_n\) be the number of vertices on directed cycles of \(f\), and let \(H_{n,d}=|\{v:|f^{-1}(v)|=d\}|\) for integer \(d\ge0\). Then for every *fixed* \(d\),
\[
\lim_{n\to\infty}\frac{\operatorname{Cov}(C_n,H_{n,d})}{\sqrt n}
=\frac{e^{-1}\sqrt{\pi/8}}{d!}\,(-d^2+3d-1).
\]
The limit is positive exactly at \(d=1,2\), and negative exactly at \(d=0\) and every \(d\ge3\). Hence these are also the eventual strict covariance signs for each fixed \(d\). The normalized profile equals the negative quadratic Poisson–Charlier polynomial, scaled by Poisson(1) masses. In particular both \(\sum_{d\ge0}e^{-1}(-d^2+3d-1)/d!=0\) and \(\sum_{d\ge0}d e^{-1}(-d^2+3d-1)/d!=0\), matching the deterministic total-vertex and total-indegree constraints.

## Assumptions and scope
Every mapping \(f:[n]\to[n]\) has probability \(n^{-n}\), including loops. Its directed functional graph has disjoint cycles with in-trees. The asymptotic quantifier fixes a nonnegative integer \(d\) before taking \(n\to\infty\); no uniformity over growing indegree thresholds is asserted. Set \(b_{n,k}(j)=\binom{k}{j}n^{-j}(1-1/n)^{k-j}\) for \(0\le j\le k\) and zero otherwise. The rising/integer conventions are fixed by this explicit binomial formula.

## Proof
**1. Conditional forest degree law.** Given \(C_n=c\), the cyclic vertex set is a uniformly chosen \(c\)-subset, carrying an independent uniform cyclic permutation; every other vertex lies in a uniformly random directed forest rooted in that subset. The rooted-forest extension of the Prüfer word construction represents its \(n-c-1\) nontrivial attachments by independent uniform letters from \([n]\) and a distinguished final root chosen uniformly from the \(c\) roots. Thus, for \(c<n\), the cyclic vertices consist of \(c-1\) ordinary roots with indegrees \(1+\operatorname{Bin}(n-c-1,1/n)\), one distinguished root with indegree \(2+\operatorname{Bin}(n-c-1,1/n)\), and \(n-c\) nonroot vertices with indegrees \(\operatorname{Bin}(n-c-1,1/n)\). These are marginal statements, not assertions of joint independence. Therefore
\[
 g_{n,d}(c):=\mathbb E[H_{n,d}\mid C_n=c]
 =(c-1)b_{n,n-c-1}(d-1)+b_{n,n-c-1}(d-2)+(n-c)b_{n,n-c-1}(d).
\]
For \(c=n\), every vertex has indegree one and \(g_{n,d}(n)=n\mathbf1_{\{d=1\}}\).

**2. Cyclic-core law.** Choose and cyclically permute \(c\) vertices, then attach the other \(n-c\) vertices to that cyclic set as a rooted forest. The enumeration yields
\[
 \Pr(C_n=c)=\frac{c(n)_{\underline c}}{n^{c+1}},\qquad 1\le c\le n,
\]
where \((n)_{\underline c}=n(n-1)\cdots(n-c+1)\). The elementary product bound \((n)_{\underline c}/n^c\le\exp[-c(c-1)/(2n)]\) gives uniformly integrable polynomial moments. A Riemann-sum argument gives \(X_n=C_n/\sqrt n\Rightarrow X\), with Rayleigh density \(x e^{-x^2/2}\) for \(x>0\), and convergence of every fixed positive moment. In particular \(\mathbb E X=\sqrt{\pi/2}\), \(\mathbb E X^2=2\), \(\mathbb E X^3=3\sqrt{\pi/2}\), whence \(\operatorname{Cov}(X,X^2)=\sqrt{\pi/2}\).

**3. Second-order conditional regression.** For fixed nonnegative \(j\), with \(t=c/n\), the binomial mass at \(j\), uniformly on \(1\le c\le n^{3/5}\), has expansion
\[
 b_{n,n-c-1}(j)=\frac{e^{-1}}{j!}\left[1+(1-j)t+\frac{j^2-3j+1}{2}t^2+\frac{1+j-j^2}{2n}\right]
 +O_j(t^3+t/n+n^{-2}).
\]
Terms with \(j<0\) are defined as zero and excluded from this expansion. Substitute the three masses into the exact formula for \(g_{n,d}\), collect powers and use the elementary factorial identities \(j/j!=1/(j-1)!\). The linear term in \(c\) cancels and the result is
\[
 g_{n,d}(c)=\frac{ne^{-1}}{d!}+
 \frac{e^{-1}(-d^2+3d-1)}{2d!}\left(\frac{c^2}{n}-1\right)
 +O_d\left(\frac cn+\frac{c^3}{n^2}+\frac1n\right).
\]
For each fixed \(d\), its remainder is \(o(1)\) in polynomial-moment mean on the natural range \(c=O(\sqrt n)\). On \(c>n^{3/5}\), use the trivial bound \(0\le g_{n,d}(c)\le n\) together with the exponential tail from step 2, so the contribution to the rescaled covariance vanishes. Conditional expectation yields
\[
 \operatorname{Cov}(C_n,H_{n,d})=\operatorname{Cov}(C_n,g_{n,d}(C_n))
 =\frac{e^{-1}(-d^2+3d-1)}{2d!}\operatorname{Cov}\left(C_n,\frac{C_n^2}{n}\right)+o(\sqrt n).
\]
Since \(\operatorname{Cov}(C_n,C_n^2/n)/\sqrt n\to\operatorname{Cov}(X,X^2)=\sqrt{\pi/2}\), this proves the asserted coefficient. The quadratic \(-d^2+3d-1\) has signs \(-,+,+,-,-,\ldots\) at nonnegative integer arguments, and no integer root.

## Verification
Run `python3 mapping_degree_profile_check.py` using Python's standard library. The script exhaustively enumerates all \(n^n\) mappings for \(2\le n\le6\) to compare conditional indegree counts and the cyclic-point law, checks exact small-degree conditional regressions, and recomputes exact finite covariances from the conditional formulas for several larger \(n\). It reports `CHECKS_OK 207`. This computation checks finite identities and signs at tested sizes; the asymptotic limit is established analytically above.

## Relationship to prior work
Hansen and Jaworski's 2006 preprint (later published as *Random mappings with exchangeable in-degrees*) relates cyclic-point statistics to exchangeable indegree sequences. Their 2010 work analyzes uniform mappings conditioned on cyclic-point count via rooted forests. These provide relevant general structural identities; the present result isolates a specific *whole indegree-histogram covariance profile* in a second-order asymptotic regime. The empty-box component belongs to a well-studied and previously analyzed class, and its isolated covariance is not claimed as separately new. The contribution assessed here is the joint Charlier profile and its resulting sign partition across fixed indegrees.

## Limitations
This gives leading covariances for fixed degrees only. It does not claim an all-size sign classification, monotonicity in sample size, independence, or joint Gaussian convergence. Other literature might implicitly encode the same coefficient through multivariate generating functions or general mapping-degree formulae; no independent priority assessment is claimed. Finite checks are supportive and are not a substitute for the proof.

## References
1. Jennie C. Hansen and Jerzy Jaworski, *A new random mapping model*, arXiv:math/0603529v1 (first public submission 2006-03-22), https://arxiv.org/abs/math/0603529.
2. Jennie C. Hansen and Jerzy Jaworski, *Random mappings with a given number of cyclical points*, *Ars Combinatoria* 94 (2010), 341–359, https://combinatorialpress.com/article/ars/Volume%20094/volume-94-paper-34.pdf.
