# Full arclength absorption by flat branches for every parameter in a planar absolute-value family

## Finding
For any \(a<0\) and \(b\in\mathbb R\), consider
\[
 F_{a,b}(x,y)=(|x|-y+a,\ x-|y|+b).
\]
Let \(\Gamma_{a,b}\) be the compact invariant graph constructed in [1]. Its positive-length part is a finite union of line segments; finitely many isolated periodic points may additionally occur. Let \(W\) be the union of the relative interiors of the nondegenerate constant-image segments (plateaus). Put
\[
 U=\bigcup_{n=0}^{\infty}(F_{a,b}|_{\Gamma_{a,b}})^{-n}(W).
\]
**Theorem.** For every indicated pair of parameters,
\[
 \mathcal H^1(\Gamma_{a,b}\setminus U)=0.
\]
Thus a point chosen with arclength-absolutely-continuous distribution on the invariant graph eventually enters a plateau almost surely. Subsequently its orbit is the orbit of one of the finitely many plateau images. This strengthens the all-parameter open-and-dense conclusion of [1] and extends the parameter-restricted arclength conclusions of [2].

## Assumptions and scope
The invariant graphs and two properties of their explicit construction are taken from [1], rather than reproved here: (i) there are finitely many straight edges in the four directions horizontal, vertical, northeast and southeast; (ii) for all parameters, the union of preimages of relative plateau interiors is dense in every positive-length edge (Proposition 23 and Theorem C). Theorem B of [1] supplies the invariant graph. Lemma 22 of [1] establishes that each nonconstant local affine branch of the restriction to an edge multiplies arclength by either \(\sqrt2\) or \(2\). These are hypotheses from the explicitly cited source, not numerical observations.

The map identity \(\lambda F_{a,b}(p/\lambda)=F_{\lambda a,\lambda b}(p)\) for \(\lambda>0\) conjugates every \(a<0\) case by a positive dilation to \(a=-1\), without changing whether arclength-null sets occur. It suffices to prove the assertion at \(a=-1\). Isolated graph points have zero \(\mathcal H^1\) measure. We work on the disjoint union of the closed positive-length edge intervals with endpoints identified as necessary for describing the dynamics; integration and variation always treat these as a finite collection of intervals, so endpoints have zero arclength.

## Proof
**1. An expanding graph-with-holes lemma.** Let \(G\) be a finite union of compact edge intervals, with their Euclidean arclength measure \(m\), and let \(f:G\to G\) be continuous and piecewise affine. Assume each restriction to a partition interval either is constant or maps affinely into one target edge with arclength slope of absolute value at least \(\lambda>1\). Write \(W\) for the union of the interiors of all constant branches and suppose that \(U=\bigcup_{n\ge0}f^{-n}(W)\) intersects every nonempty open subinterval of every positive-length edge. Then \(m(G\setminus U)=0\).

To prove this lemma, ignore the finite partition boundaries, which have arclength zero. Define the killed transfer operator \(K\) on \(L^1(G,m)\), using only nonconstant branches \(I_j\), by
\[
 (Kh)(y)=\sum_j\frac{\mathbf 1_{f(I_j)}(y)}{s_j}
             h\big((f|_{I_j})^{-1}(y)\big),
 \qquad s_j=\big|\tfrac{d}{d\ell}(f|_{I_j})\big|\ge\lambda.
\]
(Here \(d/d\ell\) means the derivative in an arclength coordinate.) The target intervals may overlap, and that is why the contributions are summed. By change of variables \(K\) is positive and \(\|Kh\|_1\le\|h\|_1\). For a nonnegative \(h\),
\[
 \int_G Kh\,dm=\int_{G\setminus W}h\,dm.
\]
For any fixed integer \(r\), \(K^r\) has finitely many nonconstant affine inverse branches \(J\), each of whose slopes is at least \(\lambda^r\). Split at all relevant branch endpoints and preimages of graph vertices, so every branch image lies in one edge. Let \(\operatorname{Var}(h)\) be the sum of the one-dimensional total variations on the finitely many edges. For a branch interval \(J\) of length \(\ell(J)>0\), the extension by zero of its weighted image has variation bounded by
\[
 \frac1{s_J}\left(\operatorname{Var}_J(h)+|h(J^-)|+|h(J^+)|\right)
 \le\frac1{s_J}\left(3\operatorname{Var}_J(h)
                 +\frac2{\ell(J)}\int_J|h|\,dm\right).
\]
The second inequality follows by choosing a point in \(J\) where \(|h|\) is no larger than its mean and bounding both endpoint traces by that value plus \(\operatorname{Var}_J(h)\). The finitely many surviving branch domains are disjoint up to their endpoints. Therefore, with \(\ell_r\) the smallest positive branch-domain length,
\[
 \operatorname{Var}(K^r h)
  \le3\lambda^{-r}\operatorname{Var}(h)
   +\frac{2}{\lambda^r\ell_r}\|h\|_1.
\]
If there are no surviving branches at a given depth, then \(K^r=0\) and the lemma is immediate. Otherwise take \(r\) so large that \(\theta=3\lambda^{-r}<1\). This inequality, together with the analogous finite bounds for the powers \(K^j\), \(0\le j<r\), implies
\[
 \sup_{n\ge0}\left(\|K^n\mathbf 1\|_1
                  +\operatorname{Var}(K^n\mathbf 1)\right)<\infty.
\]
The compact embedding of bounded-variation functions into \(L^1\) on a finite union of compact intervals makes the sequence \(K^n\mathbf 1\) relatively compact in \(L^1\).

Define \(S=G\setminus U\). The change-of-variables formula yields
\[
 \int_GK^n\mathbf 1\,dm
 =m\{x:\ f^j(x)\notin W\text{ for }0\le j<n\}
 \downarrow m(S).
\]
Suppose for contradiction that \(m(S)>0\). The Cesàro averages
\[
 h_N=\frac1N\sum_{n=0}^{N-1}K^n\mathbf 1
\]
have a subsequence converging in \(L^1\) to a nonnegative function \(h\) of bounded variation with \(\int h\,dm=m(S)>0\). Since
\[
 Kh_N-h_N=\frac{K^N\mathbf 1-\mathbf 1}{N},
\]
and \(K\) is an \(L^1\)-contraction, the limit obeys \(Kh=h\).

Invariance of the integral in the killed-operator identity forces \(\int_W h\,dm=0\). Consequently the probability measure obtained by normalizing \(h\,dm\) is actually invariant under \(f\): no mass enters a constant branch, and the nonconstant-branch change-of-variables identity is exactly the full pushforward identity. In particular its mass on every \(f^{-n}(W)\), and hence on \(U\), is zero.

Yet a nonnegative nonzero bounded-variation density is strictly positive almost everywhere on some nonempty open subinterval \(J\) of an edge: choose a point where the regulated representative is continuous and positive. Since \(U\) is open and dense in every edge, \(U\cap J\) contains a nonempty open subinterval. That subinterval has strictly positive \(h\,dm\)-mass, a contradiction. This establishes the lemma.

**2. Apply the lemma to the invariant graph.** The first cited paper identifies all branches and proves the needed density of plateau preimages, uniformly over \(b\). On every non-plateau branch its Lemma 22 gives the arclength multiplier \(\sqrt2\) or \(2\), so the lemma applies with \(\lambda=\sqrt2\) and, for example, \(r=4\), since \(3(\sqrt2)^{-4}=3/4<1\). Finitely many points outside the positive-length edge union do not affect the arclength assertion. The parameter conjugation extends it from \(a=-1\) to every \(a<0\). This proves the theorem. \(\square\)

## Verification
The proof's nonstandard step is the displayed variation inequality for the killed transfer operator; its endpoint-trace estimate, finite-branch requirement and compactness argument are explicit above. All infinite-time and all-parameter quantifiers are proved analytically. The standalone program `check_branches.py` independently recomputes every quadrant derivative matrix and all four invariant direction images exactly over the integers, confirming that every nonzero branch stretch is \(\sqrt2\) or \(2\) and the four-step variation coefficient is \(3/4\). This finite calculation checks one critical premise and is not offered as a proof of the source's graph enumeration or its dense-preimage theorem. The graph construction and density statement are taken from the inspected primary paper, not verified afresh for each individual parameter.

## Relationship to prior work
[1] constructs all the graphs and proves the all-parameter **open and dense** plateau-preimage conclusion (Theorem C; Lemmas 21–24 and Proposition 23), but states the full-arclength assertion as a suspicion. [2] supplies full-arclength assertions only in the explicitly stated parameter regions \(-b/a<-2\) and \(-b/a\in[-112/137,-13/16]\cup[603/874,563/816]\), using parameter-dependent special return maps (Theorem 3 of the 2026 revision, formerly Theorem 2 in v1, and Propositions 10–11). An earlier finite-parameter calculation on \(a=-1\), \(2\le b\le4\) also gives a stronger dimension result within that restricted range. No novelty is claimed for those special cases. The present theorem instead derives full arclength uniformly in all remaining real parameter regions, including the positive-entropy regimes, by a general killed-transfer argument.

## Limitations
This is an **arclength-on-the-graph** statement, not a statement that almost every initial point in the ambient plane is eventually absorbed into a plateau. It does not classify individual orbits in the exceptional null set, determine its Hausdorff dimension outside previously analyzed ranges, prove parameter-uniform escape rates, or assert that all plateau-image limit sets are periodic when \(-b/a\) is irrational. The proof uses the primary paper's finite invariant-graph construction, its expansion lemma and its density proposition; it does not independently reconstruct the entire published classification. Priority against unindexed or more abstract survivor-set theorems remains a residual literature risk.

## References
[1] A. Cima, A. Gasull, V. Mañosa and F. Mañosas, *Invariant graphs and dynamics of a family of continuous piecewise linear planar maps*, arXiv:2410.01052 (first public 2024-10-01); Qualitative Theory of Dynamical Systems **24**, article 70 (2025), DOI:10.1007/s12346-025-01221-1.

[2] A. Cima, A. Gasull, V. Mañosa and F. Mañosas, *Entropy and omega-limit sets on invariant graphs for a class of planar piecewise linear maps*, arXiv:2503.02411v4 (revised 2026-07-29; first posted 2025-03-04 with the title *Further results for a family of continuous piecewise linear planar maps*), especially Theorem 3 and Propositions 10–11.
