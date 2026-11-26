# Period-resolved zeta census for edge-minimal irreducible Markov shifts

## Finding

Let \(\mathcal G_N\), for \(N\ge2\), be the family of strongly connected directed graphs with exactly \(N\) vertices and \(N+1\) edges, with loops allowed and parallel edges forbidden. For each period \(d\ge1\), the number of **distinct Artin–Mazur zeta functions** of the associated one-sided vertex Markov shifts is
\[
P_N(d)=T(\lfloor N/d\rfloor)+\mathbf1_{\{d<N<2d\}},\qquad
T(m)=\begin{cases}0&m\le1,\\ \frac12\sum_{j=1}^m\varphi(j)&m\ge2.\end{cases}
\]
Here \(\varphi\) is Euler's totient. The profiles are exactly \(1/(1-z^a-z^b)\) for
\[
1\le a\le b\le N,\quad a+b\ge N+1,\quad (a<b\ \text{or}\ a=b<N),\quad \gcd(a,b)=d.
\]
Every shift in the family is continuously orbit equivalent to the full two-shift. Consequently the distinct profiles count pairwise nonconjugate shifts even within this one continuous-orbit-equivalence class; this does not assert that equal zeta functions imply conjugacy.

In the mixing stratum \(d=1\), the number of profiles is \(T(N)=3N^2/(2\pi^2)+O(N\log N)\). With **exactly** \(N\) instead of exactly \(N-1\) vertices, \(N\ge3\), there are \(\varphi(N)\) new mixing profiles and \(\varphi(N)/2\) old profiles disappear, so the **net** increase in the count is \(\varphi(N)/2\).

## Proof

**The available length pairs.** All outdegrees are positive, so exactly one vertex \(p\) has two outgoing edges and every other vertex has outdegree one. Following the two outgoing edges from \(p\) and then the deterministic paths produces two simple cycles returning to \(p\): entering a repeat before returning would trap the path away from \(p\) and contradict strong connectivity. Every vertex is reachable from \(p\), so the cycles cover the graph. Any intersection before the return forces their remaining suffixes to coincide. The intersection is thus one common return path, possibly just \(p\). If it has \(t\) vertices and the cycle lengths are \(a\le b\), then \(t=a+b-N\ge1\) and \(b\le N\). The equal case \(a=b=N\) would require both forward branches to be single edges with the same endpoints, forbidden here.

Conversely, for an allowed pair put \(t=a+b-N\). At \(t=1\), join two cycles at a single vertex; two coincident loops cannot occur since \(N\ge2\). At \(t>1\), build one common return path of length \(t-1\) from a merging vertex to \(p\), and two internally disjoint forward paths from \(p\) to that vertex of lengths \(a-t+1,b-t+1\). These lengths are positive and cannot both equal one. This graph is strongly connected with no parallel edges, \(a+b-t=N\) vertices and \(a+b-t+1=N+1\) edges. Since the only strongly connected graph with all outdegrees one is a directed cycle, \(N+1\) is the smallest non-permutation budget.

**Period, zeta, and orbit equivalence.** Every simple directed cycle must contain \(p\) and follow one of the two first-return branches. The gcd of their lengths gives the period. Since the cycles intersect, the disjoint-cycle expansion is \(\det(I-zA)=1-z^a-z^b\). The trace-log identity for \(\zeta_A(z)=\exp(\sum_{r\ge1}\operatorname{tr}(A^r)z^r/r)\) makes it the reciprocal of this determinant. The coefficients recover the unordered pair, including the coefficient \(-2\) when the lengths coincide. At \(z=1\) the determinant is \(-1\), hence the Bowen–Franks group \(\mathbb Z^N/(I-A^{\mathsf T})\mathbb Z^N\) and its unit class are trivial. The two-state all-ones matrix has the same invariants, giving continuous orbit equivalence by the classification for irreducible non-permutation matrices.

**Arithmetic census.** For unequal lengths of period \(d\), write \((a,b)=(du,dv)\) with \(1\le u<v\le M=\lfloor N/d\rfloor\) and \(\gcd(u,v)=1\). The lower bound on their sum becomes \(u+v\ge M+1\). There are \(\sum_{v=2}^M\varphi(v)\) coprime pairs before imposing the sum constraint. For a fixed excluded sum \(s\in\{3,\ldots,M\}\), coprimality is \(\gcd(u,s)=1\); pairing \(u\) and \(s-u\) yields \(\varphi(s)/2\) excluded pairs. Subtraction gives \(T(M)\) for \(M\ge2\); for \(M\le1\) there are none. The equal-length pair \((d,d)\) adds one exactly when \(d<N<2d\). This proves the period formula. The mixing asymptotic follows from the classical summatory totient estimate \(\sum_{v\le N}\varphi(v)=3N^2/\pi^2+O(N\log N)\).

**Turnover between successive exact budgets.** A mixing pair at budget \(N\) but not \(N-1\) must have larger exponent \(b=N\), because for \(b<N\) the sum constraint at \(N\) implies the old one. Every coprime \((a,N)\), \(1\le a<N\), qualifies, giving \(\varphi(N)\) additions. An old pair is lost precisely when \(a+b=N\), which gives \(\varphi(N)/2\) losses by the same symmetry of coprime residues (no fixed point for \(N\ge3\)). Neither count is the net increase by itself. For example, going from \(N=2\) to \(N=3\) replaces \((1,2)\) with \((1,3),(2,3)\).

## Relationship to prior work and verification

R. Klech, [*Generating Functions and the Entropy Hierarchy of Strongly Connected Digraphs*](https://arxiv.org/abs/2609.17334), §4, in particular Lemmas 4.3 and 4.5, supplies the butterfly graph form and the two-return polynomial in the entropy/path setting. The graph form and polynomial shape are background. K. Matsumoto and H. Matui, [*Topological entropy in continuous orbit equivalence of one-sided topological Markov shifts*](https://arxiv.org/abs/2606.16283), Introduction, recall the existing classification used above. Their [*Continuous orbit equivalence of topological Markov shifts and dynamical zeta functions*](https://arxiv.org/abs/1403.0719) relates zeta under orbit cocycles, not by a census indexed by this edge budget. The result here is the distinct-profile count by period and the distinction between turnover and net change at successive budgets.

The companion `VERIFY_SPARSE.py` gives finite exact checks of primitive denominator sets for \(N=2,3,4\), primitive constructive examples through \(N=7\), and arithmetic period counts for \(2\le N\le150\). Its reported finite assertions are supplementary; the general period counts and turnover are proved above. This counts profiles, not labelled presentations or all zeta functions of the full continuous-orbit-equivalence class.
