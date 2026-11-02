# A universal negative isolation–connected-motif covariance law for random chord diagrams

## Finding

For every integer \(n\ge 2\), consider the uniform random perfect matching of \(2n\) labeled points in circular order. Its intersection graph has one vertex per chord, with edges between crossing chords. Let \(I_n\) count isolated vertices of this graph. Fix a **connected** simple graph \(H\) on \(r\) vertices, where \(2\le r\le n\), that is realizable as the intersection graph of \(r\) chords. Let \(X_{H,n}\) count unordered sets of \(r\) chords whose **induced** intersection graph is isomorphic to \(H\). Put \(p_H=\Pr(G_r\cong H)>0\), and define

\[
q_{n,k}=\frac{(2k-1)!!\,(2n-2k-3)!!}{(2n-1)!!},\qquad 0\le k\le n-1,
\]

where \((-1)!!=1\), and adopt \(\binom{a}{r}=0\) for \(a<r\). Then

\[
\mathbb E X_{H,n}=p_H\binom nr,
\]

and the following exact finite sum holds:

\[
\boxed{\operatorname{Cov}(I_n,X_{H,n})
=p_H\sum_{k=0}^{n-1}(2n-2k-1)q_{n,k}
\left[\binom kr+\binom{n-1-k}{r}-\binom nr\right]<0.}
\]

In particular, the normalized covariance \(\operatorname{Cov}(I_n,X_{H,n})/\mathbb E X_{H,n}\) depends **only on \(n\) and \(r\)**, not on the shape of the connected circle graph \(H\). For each fixed \(r\ge 2\),

\[
\boxed{\frac{\operatorname{Cov}(I_n,X_{H,n})}{\mathbb E X_{H,n}}
=-\frac rn+O_r(n^{-2})}\qquad(n\to\infty),
\]

or equivalently

\[
\operatorname{Cov}(I_n,X_{H,n})
=-\frac{p_H}{(r-1)!}n^{r-1}+O_H(n^{r-2}).
\]

The connectedness condition cannot simply be dropped. For the disconnected graph \(H=2K_1\), its induced count is \(\binom n2-X_{K_2,n}\), so its covariance with \(I_n\) is strictly **positive** for every \(n\ge2\).

## Assumptions and scope

The matching is uniform among \((2n-1)!!\) matchings of labeled endpoints, with chord intersections determined by alternating endpoints. All subgraph counts here are *unlabeled induced counts* (not ordered embeddings). The graph \(H\) is connected and realized with positive probability on exactly \(r\) chords. The theorem makes no assertion about general disconnected motifs. The large-\(n\) expansion holds with fixed \(r\) and fixed \(H\), not growing motif size.

## Proof

**Uniform induced motif law.** Any randomly selected set of \(r\) chords in a uniform \(n\)-chord diagram has the same relative endpoint-pairing law as a uniform diagram on \(r\) chords: assign temporary independent chord names, expose their endpoint order, then erase the names. Thus any prescribed \(r\)-chord subset induces \(H\) with probability \(p_H\). Summation over the \(\binom nr\) subsets proves the expectation formula.

**Conditioning on an isolated chord.** Fix endpoints \(a<b\) and let \(2k=b-a-1\) be the number of endpoints strictly between them. The event that \(\{a,b\}\) is a chord having no crossings is exactly that all other \(2k\) internal endpoints pair among themselves, and the other \(2(n-1-k)\) endpoints pair among themselves. Its probability is \(q_{n,k}\). Conditional on this event, the two smaller diagrams are independent and uniform on \(k\) and \(n-1-k\) chords. Since chords from different arcs do not cross, a connected induced subgraph with at least two vertices must lie entirely inside one arc. Therefore

\[
\mathbb E[X_{H,n}\mid\{a,b\}\text{ is isolated}]
=p_H\left(\binom kr+\binom{n-1-k}{r}\right).
\]

For each \(k\), exactly \(2n-2k-1\) pairs of labeled endpoints satisfy \(a<b\) and \(b-a-1=2k\). Sum the identity \(\operatorname{Cov}(I_n,X_{H,n})=\sum_{a<b}\Pr(\{a,b\}\text{ isolated})[\mathbb E(X_{H,n}\mid\{a,b\}\text{ isolated})-\mathbb E X_{H,n}]\) to obtain the displayed finite sum.

**Strict sign.** The nonnegative Vandermonde terms give

\[
\binom kr+\binom{n-1-k}{r}\le\binom{n-1}{r}<\binom nr,
\]

for every \(0\le k\le n-1\) and \(2\le r\le n\), with the convention on vanishing binomials. Every coefficient \((2n-2k-1)q_{n,k}\) is strictly positive, as is \(p_H\), proving strict negativity.

**Fixed-motif asymptotics.** Write \(s=\min\{k,n-1-k\}\). The two configurations \(s=0\) correspond to the \(2n\) possible cyclically adjacent endpoint pairs; each is an isolated chord with probability \((2n-1)^{-1}\). Their *total* contribution to the covariance equals

\[
-\frac{2n}{2n-1}p_H\binom{n-1}{r-1}.
\]

For \(s\ge1\), note \(q_{n,s+1}/q_{n,s}=(2s+1)/(2n-2s-3)\), which is at most \(1/2\) for \(1\le s\le \lfloor n/4\rfloor\) once \(n\) is sufficiently large. Moreover \(q_{n,1}=((2n-1)(2n-3))^{-1}\), the sequence decreases up to the middle, and beyond the first quarter it is exponentially small. Consequently

\[
\sum_{s=1}^{\lfloor(n-1)/2\rfloor}(s+1)q_{n,s}=O(n^{-2}).
\]

A nonadjacent isolated chord whose smaller side has \(s\) chords removes at most \((s+1)\binom{n-1}{r-1}\) potential connected motifs compared with the unconditional expected count. Since there are at most \(4n\) candidate chord positions per \(s\), the combined nonadjacent contribution is \(O_H(n^{r-2})\). (At the middle value the multiplicity is smaller, so the bound remains valid.) The adjacent term is \(-p_H n^{r-1}/(r-1)!+O_H(n^{r-2})\). Divide by \(p_H\binom nr\) to obtain the normalized expansion.

## Verification

Run \(`python3 verify_motif.py`\) with Python 3 and no third-party dependencies. It independently enumerates all \(3\), \(15\), \(105\), \(945\), and \(10395\) matchings for \(n=2,3,4,5,6\); classifies connected induced motifs on at most four vertices; compares exact rational covariance values and expectations with the theorem; confirms the disconnected two-isolate counterexample; and checks the exact normalized sign for \(2\le n\le69\), \(2\le r\le\min(n,10)\). It reports `PASS: 684 exact assertions`. Finite enumeration is a reproducibility check, not the proof for unrestricted \(n\).

## Relationship to prior work

Acan's work defines the uniform chord-intersection model and investigates degrees and isolated vertices, including the monolithic regime. Flajolet and Noy derive limit laws for component counts and crossings; Paguyo develops marginal convergence rates for simple chords and crossings. The classical Touchard–Riordan theory concerns crossing enumeration. None of the specifically inspected relevant sections gives the displayed isolation/connected-*induced*-motif covariance, its graph-shape invariance, or the uniform strict sign. Earlier counting results for simple chords and pairwise crossings concern a different statistic: isolated chords need not join adjacent endpoints. This theorem does not assert priority over uninspected literature or claim that underlying matching-count identities are new.

## Limitations

The law requires connected \(H\), a uniform perfect matching, and induced rather than arbitrary (noninduced) motif counts. In particular, it does not imply negative covariance for arbitrary disconnected motifs. Its asymptotic error has fixed \(H\); uniformity for growing motifs is not shown. Historical originality is qualified by potentially uninspected older chord-enumeration literature, including Stoimenow's 2000 paper. No independent mathematical audit has been performed.

## References

- H. Acan, *On a uniformly random chord diagram and its intersection graph*, arXiv:1501.01489v1, 7 January 2015. https://arxiv.org/abs/1501.01489
- P. Flajolet and M. Noy, *Analytic Combinatorics of Chord Diagrams*, INRIA RR-3914 (2000). https://algo.inria.fr/flajolet/Publications/FlNo00.pdf
- J. E. Paguyo, *Convergence rates of limit theorems in random chord diagrams*, arXiv:2104.01134. https://arxiv.org/abs/2104.01134
- H. Acan and B. Pittel, *Formation of a giant component in the intersection graph of a random chord diagram*, arXiv:1406.2867. https://arxiv.org/abs/1406.2867
- A. Stoimenow, *On the number of chord diagrams*, *Discrete Mathematics* 218 (2000), 209–233, doi:10.1016/S0012-365X(99)00347-7 (full text not inspected).
