# First-match time controls crossings in a uniform chord diagram

## Finding
Fix an integer \(n\ge2\). Choose uniformly a perfect matching of ordered endpoints \(1,\ldots,2n\), drawn as chords of a circle. Let \(T\) be the earliest right endpoint of any chord and let \(C\) count unordered pairs of crossing chords. For every \(2\le t\le n+1\),
\[
\boxed{\mathbb E[C\mid T=t]=\frac{2n^2-6n+t^2+t-2}{12}.}
\]
This is a strictly increasing quadratic regression: its adjacent increment is \((t+1)/6\). Since \(\mathbb EC=n(n-1)/6\), the conditional crossing excess is exactly
\[
\boxed{\mathbb E[C\mid T=t]-\mathbb EC=\frac{t(t+1)-(4n+2)}{12}.}
\]
It changes sign at the unique positive real boundary \((\sqrt{16n+9}-1)/2\). Zero excess at an integer \(t\) occurs exactly for \(n=[t(t+1)-2]/4\), where \(t\equiv1,2\pmod4\) and the admissible ranges hold. Moreover,
\[
\operatorname{Cov}(C,T)=\frac{\operatorname{Cov}(T^2,T)+\operatorname{Var}(T)}{12}>0,
\quad
\operatorname{Cov}(C,T)\sim \frac{\sqrt\pi}{6}n^{3/2},
\quad
\operatorname{Corr}(C,T)\sim\frac{\sqrt{5\pi}}{2\sqrt{4-\pi}}n^{-1/2}.
\]

## Assumptions and scope
All \((2n-1)!!\) perfect matchings are equally likely. Chords \((a,b)\) and \((c,d)\), with their endpoints in increasing order within each pair, cross if \(a<c<b<d\) or \(c<a<d<b\). The first closing time \(T\) is supported on \(\{2,\ldots,n+1\}\). These finite identities require no asymptotic assumptions. The asymptotic equivalents are as \(n\to\infty\) for this uniform matching law, not arbitrary exchangeable paired sequences.

## Proof
Condition on \(T=t\). The first \(t-1\) endpoints belong to distinct open chords; endpoint \(t\) closes one of them, with its earlier partner uniformly distributed over the first \(t-1\) positions. Write \(a=t-1\) and \(b=n-a=n-t+1\). The \(a\) early chords include one completed at \(t\), while the other \(a-1\) have right endpoints later than \(t\); the other \(b\) chords have both endpoints later than \(t\).

Every pair of early chords crosses with probability \(1/2\): for two still-open chords, their late closing order is equiprobable; if one first closes at \(t\), its earlier partner is uniformly ranked among the openings, so the other early chord crosses with probability \(1/2\). Every early--late pair crosses with probability \(1/3\) when the early chord remains open, because its closing endpoint and the two endpoints of the late chord occur in uniformly random relative order and crossing means the closing endpoint lies between the latter two. The completed early chord crosses no late chord. Every pair of late chords crosses with probability \(1/3\), by symmetry of the three possible pairings of four endpoints. Consequently,
\[
\mathbb E[C\mid T=t]
=\frac12\binom{t-1}{2}+\frac13(t-2)(n-t+1)+\frac13\binom{n-t+1}{2}
=\frac{2n^2-6n+t^2+t-2}{12}.
\]
Unconditionally, any two specified chords cross with probability \(1/3\), giving \(\mathbb EC=\binom n2/3\), and subtraction yields the crossing-excess formula. The polynomial is strictly increasing on the support. The exact zero characterization follows by reducing \(t(t+1)\equiv2\pmod4\). Taking covariance of the conditional expectation with \(T\) gives the finite covariance identity, strictly positive because \(T\) is nondegenerate and \(t^2+t\) is strictly increasing.

For the asymptotics, the exact first-closure survival function is
\[
\Pr(T>t)=\prod_{j=1}^{t-1}\frac{2n-2j}{2n-j},\quad 1\le t\le n+1.
\]
It implies \(\Pr(T>t)\le\exp[-t(t-1)/(4n)]\), hence uniform integrability of every fixed power of \(T/\sqrt n\). Acan--Hitczenko prove \(T/(2\sqrt n)\Rightarrow X\), with \(\Pr(X>x)=e^{-x^2}\) for \(x\ge0\). Thus \(\mathbb ET\sim\sqrt{\pi n}\), \(\mathbb ET^2\sim4n\), \(\mathbb ET^3\sim6\sqrt\pi n^{3/2}\), and \(\operatorname{Var}(T)\sim(4-\pi)n\). In particular \(\operatorname{Cov}(T^2,T)\sim2\sqrt\pi n^{3/2}\). The known crossing variance \(\operatorname{Var}(C)=n(n-1)(n+3)/45\), proved by Flajolet--Noy, gives the displayed correlation equivalent.

## Verification
Execute \(\texttt{python3 verify.py}\) using the accompanying standard-library-only script. It exhaustively enumerates every matching with \(2\le n\le7\), compares the exact conditional means, independent global first and second crossing moments, first-closure moment and covariance identities, and checks monotonicity algebraically for larger sizes. These are finite checks corroborating the general combinatorial proof; they do not replace it.

## Relationship to prior work
Acan and Hitczenko (first public version 2014) studied the first repeated-card time in a memory game, identifying its Rayleigh limit and its identification with the first chord closure. Acan (2015) studied uniformly random chord diagrams and intersection-graph statistics, including crossing-related features. Flajolet and Noy (2000) determined the unconditional crossing moments and limiting normal law. The present result relates these two previously separate observables through an exact conditional regression and sharp sign transition; it does not re-claim their marginal laws. Earlier joint-enumeration methods could in principle imply the relationship, so historical priority requires independent assessment.

## Limitations
The result is an exact conditional mean statement, not conditional stochastic domination, conditional Gaussian convergence, or statistical independence. The correlation vanishes despite the positive finite covariance. All results concern uniform matchings, and no claim of independent priority verification is made. The earliest relevant probability paper has verified primary classification 60F05 and first public date 2014-11-21.

## References
- H. Acan and P. Hitczenko, *On a memory game and preferential attachment graphs*, arXiv:1411.5751v1, posted 2014-11-21; *Advances in Applied Probability* 48 (2016), 585–609. Primary MSC 60F05.
- H. Acan, *On a uniformly random chord diagram and its intersection graph*, arXiv:1501.01489v1, posted 2015-01-07; *Discrete Mathematics* 340 (2017), 1657–1668.
- P. Flajolet and M. Noy, *Analytic Combinatorics of Chord Diagrams*, FPSAC 2000, pp. 191–201; unconditional crossing variance also reproduced in M. Noy's seminar notes, https://algo.inria.fr/seminars/sem99-00/noy1.html.
- D. J. Velleman and G. S. Warrington, *What to Expect in a Game of Memory*, *American Mathematical Monthly* 120 (2013), 787–805.
