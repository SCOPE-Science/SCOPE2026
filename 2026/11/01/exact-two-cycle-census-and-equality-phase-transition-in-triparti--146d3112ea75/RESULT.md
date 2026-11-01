# Exact two-cycle census and equality-phase transition in tripartite majority dynamics

## Finding

For every triple of positive integers \(a,b,c\), consider the labelled complete tripartite graph \(K_{a,b,c}\). Apply synchronous binary *open-neighborhood majority*: a vertex changes to the strict majority bit among its neighbors and retains its previous bit if the two neighbor opinions tie. Let \(N(a,b,c)\) be the number of primitive **temporal** two-cycle orbits (an unordered pair of distinct global configurations exchanged by one update). Put
\[
B(p,q)=\sum_{j=0}^{q}\binom qj\,\mathbf 1_{\{|2j-q|<p\}},\qquad p,q\ge1.
\]
Then the exact all-parameter census is
\[
\boxed{\displaystyle N(a,b,c)=\mathbf1_{\{a>\max(b,c)\}}+\mathbf1_{\{b>\max(a,c)\}}+\mathbf1_{\{c>\max(a,b)\}}+\mathbf1_{\{a=b\}}B(a,c)+\mathbf1_{\{a=c\}}B(a,b)+\mathbf1_{\{b=c\}}B(b,a).}
\]
The formula is symmetric under permuting the three parts. In particular:

* If \(a,b,c\) are pairwise distinct, then \(N(a,b,c)=1\), independently of how large or imbalanced they are.
* If precisely two sizes equal \(p\), while the third size \(q<p\), then \(N=2^q\). If instead \(q>p\), then \(N=1+B(p,q)\); in this regime parity matters. For example, \(N(1,1,2s)=1+\binom{2s}s\), whereas \(N(1,1,2s+1)=1\), for every integer \(s\ge1\).
* If \(a=b=c=p\), then \(N=3(2^p-2)\); this previously known balanced specialization is a consistency check, not the novel portion of the theorem.

Thus breaking all equality of the three part sizes leaves **exactly one** oscillatory orbit, whereas an equality of two part sizes can create exponentially many primitive two-cycles. The exact two-equal-size transition and the unequal-size classification are the subject of the new result.

## Assumptions and scope

All parts are nonempty, vertices are labelled, and all edges between distinct parts are present; there are no edges inside a part or loops. Time is discrete and all vertices update simultaneously from the previous global configuration. Opinions are \(0\) and \(1\). A tie of neighbors means precisely half of the neighbors hold opinion \(1\), at which point each vertex **keeps its own bit**, not a prescribed common tie-breaking bit. We count each two-cycle once, even though it consists of two distinct configurations. No assertion is made about the distribution of transient basin sizes or convergence times. The general fact that finite synchronous symmetric-threshold networks eventually have periods at most two is classical and is not claimed here.

## Proof

Let the three vertex parts be \(A,B,C\), with respective sizes \(a,b,c\). Write \(F\) for the synchronous majority update. All vertices of a given part have the same open neighborhood, consisting of the other two parts. The neighbors' opinion-one count and the vertex degree are therefore identical for every vertex of the part. At every update that part either becomes uniformly zero, becomes uniformly one, or, if its neighborhood is exactly tied, remains unchanged vertex by vertex.

**Lemma 1 (temporal form of a part).** On any two-cycle \(x\leftrightarrow y\), each part either has identical bit pattern at both phases (is *static*) or alternates from the all-zero pattern to the all-one pattern (is *toggling*). Indeed, a nonconstant change in a part must be caused by a strict external majority and hence produces a uniform part. A uniform part stays uniform under all subsequent updates, including a tie. Thus at both phases a changing part is uniform, and its two patterns must be opposite. A static part may be internally mixed.

**Lemma 2 (at least two parts toggle).** If no part toggles, the orbit is fixed. If just one part toggled while the other two were static, that toggling part would see identical neighbors in both phases. The same time-independent external majority or tie cannot make the entire part switch from zero to one and back to zero. Hence a primitive two-cycle has exactly two or exactly three toggling parts.

**Two toggling parts.** Suppose \(A,B\) toggle while \(C\) is static, and let its fixed bit pattern contain exactly \(j\) ones. The two toggling parts must alternate in opposite phases. If both were zero at one phase and one at the next, then each part's external number of ones would weakly *increase*, so it could not flip from one to zero in the second update. The case both one at one phase is the same with time reversed.

Write the respective toggling sizes \(p,q\) and the static size \(r\). Opposite phases show that the static part \(C\) sees exactly \(p\) neighbors in state one in one phase and exactly \(q\) in the other, out of \(p+q\) neighbors. If \(C\) has both opinions among its vertices, its preservation requires ties in both phases, hence \(p=q\). If \(C\) is uniformly zero, its remaining zero requires \(p,q\le(p+q)/2\); if uniformly one, remaining one requires \(p,q\ge(p+q)/2\). Both alternatives again force \(p=q\).

Now take \(p=q\) and let the phases be \(A=0^p,B=1^p\) and \(A=1^p,B=0^p\). The static part sees exactly \(p\) ones out of \(2p\) neighbors at both phases and therefore preserves **every** bit pattern. In the first phase, \(A\) must flip from zero to one: it sees \(p+j\) ones among \(p+r\) neighbors, requiring \(2(p+j)>p+r\). In the second, \(A\) must flip from one to zero: it sees \(j\) ones among \(p+r\) neighbors, requiring \(2j<p+r\). The same two conditions govern \(B\). Together they are exactly
\[
r-p<2j<r+p \quad\Longleftrightarrow\quad |2j-r|<p.
\]
For each allowed static bit pattern, these conditions are sufficient, and the two temporal phases are uniquely determined up to exchange. Thus for a selected pair of equal parts of size \(p\) and a remaining part of size \(r\), the contribution is precisely \(B(p,r)\). Different selected toggling pairs yield distinct orbits because the set of toggling parts is intrinsic.

**Three toggling parts.** Here every part is uniform at both phases, and all three uniform bits complement simultaneously. Configurations with all three bits equal cannot be one phase of a two-cycle, because unanimous states are fixed. After possibly swapping the two phases, precisely one part, say \(A\), is one and the other two are zero. In this phase, \(A\) sees no ones and therefore flips to zero. The zero part \(B\) sees \(a\) ones among its \(a+c\) neighbors, so it flips to one precisely when \(a>c\). Similarly, \(C\) flips to one precisely when \(a>b\). These strict inequalities are also sufficient to return to the first phase in the next update. Therefore there is exactly one such orbit if one part is strictly largest, and none if the largest size is tied.

Lemmas 1–2 show these cases exhaust **all** primitive two-cycles. Adding their mutually disjoint counts proves the displayed formula for every positive \(a,b,c\). If the three sizes are distinct, one is strictly largest and no equal-part contribution exists, giving one orbit. If exactly two sizes equal \(p\) with remaining size \(q<p\), all \(2^q\) bitstrings on the third part obey \(|2j-q|\le q<p\), giving \(2^q\) orbits. If \(q>p\), the unique-largest orbit is additional, yielding \(1+B(p,q)\). Finally, for \(p=q=r\), the allowed weights are \(1\le j\le p-1\) and \(B(p,p)=2^p-2\), yielding three equal-pair contributions. This completes the proof.

## Verification

Run `python3 verify_tripartite_recurrence.py` with Python 3 and only the standard library. It constructs each labelled adjacency update explicitly and exhaustively tests all \(2^{a+b+c}\) configurations for the \(89\) sorted triples \(1\le a\le b\le c\le8\) with \(a+b+c\le16\), totaling \(1{,}236{,}504\) configurations. It separately uses aggregated count dynamics, weighting each part-count triple by its binomial multiplicity, on \(1{,}137\) triples with \(a,b,c\le20\) and \(a+b+c\le38\). It compares exact primitive-cycle counts against the formula throughout. The recorded replay ends `ALL_CHECKS_PASS`; the file `verification_output.txt` contains the full concise output.

Both routines also check a **known auxiliary** fixed-state formula as a regression test; fixed-state enumeration is not a new claim here. The exhaustive experiments establish only the checked finite ranges. The preceding structural argument establishes the stated all-positive-integer formula.

## Relationship to prior work

Adams, Brass, Stokes, and Troxell (2011) study complete multipartite graphs but use **irreversible** majority conversion, proving bounds and exact seed-conversion numbers. In irreversible dynamics a zero-to-one change is permanent, so primitive temporal two-cycles cannot occur; their theorems do not imply the reversible census here. Kuhlman, Mortveit, Murrugarra, and Kumar (2011), Theorem 3.1 and Appendix A, establish general restrictions to periods one and two for synchronous threshold networks but do not give a tripartite parameter-dependent cycle count. Benjamini, Chan, O'Donnell, Tamuz, and Tan (2014) likewise formulate synchronous majority with tie retention, discuss the classical Goles–Olivos two-period theorem, and study infinite and random graph contexts; their general theorem does not compute the present counts.

Voutsadakis (2004) gives an efficient limit-cycle algorithm for threshold and symmetric Boolean networks over a **complete graph** whose vertex functions depend on the overall number of ones. His count compression does not directly apply here: a vertex in one tripartite part sees the ones in the *other two parts*, not simply the total number of ones in the full vertex set. The inspected paper does not give the present closed three-parameter tripartite binomial formula.

There are two especially close but **different** published graph-family classifications. *Majority C-colorings of complete multipartite graphs* (2026) classifies static local-majority colorings: it implies the fixed configurations on complete tripartite graphs, and that fixed-state fact is not offered as new here. *Sharp period-four census for complete multipartite parity automata* (2026) gives primitive-orbit counts for **XOR parity** rather than strict majority; its linear finite-field dynamics does not imply the nonlinear majority census. The previously established balanced specialization \(K_{p,p,p}\), with \(3(2^p-2)\) temporal two-cycles, also lies inside the displayed identity but is not included in the novelty claim. The new scope is every **unequal** positive triplet and the sharp equal-size versus unequal-size transition, rather than the general period-two bound, known fixed-state count, balanced case, or parity-rule orbit counts.

## Limitations

The classification is for the specified synchronous, binary, tie-retaining strict-majority rule on exactly three nonempty complete parts. It does not classify other update rules, larger numbers of parts, asynchronous schedules, external forcing, transient entry times, or attraction basins. All equality cases are included mathematically, but the equal-three-parts formula was previously known. Literature comparison includes directly inspected primary work and targeted meaning/alias searches, not an exhaustive proof that no obscure equivalent formulation exists. An older unindexed threshold-network result may still cover the three-size law; no independent external audit has been performed.

## References

1. S. S. Adams, Z. Brass, C. Stokes, and D. S. Troxell, *Irreversible k-threshold and majority conversion processes on complete multipartite graphs and graph products*, arXiv:1102.5361v1, first public 25 February 2011.
2. C. J. Kuhlman, H. S. Mortveit, D. Murrugarra, and V. S. A. Kumar, *Bifurcations in Boolean Networks*, arXiv:1108.2974v1, 15 August 2011, especially Theorem 3.1 and Appendix A.
3. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz, and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486v1, 11 May 2014.
4. G. Voutsadakis, *On the limit cycle structure of threshold Boolean networks over complete graphs*, International Journal of Neural Systems 14 (2004), 209–215; lawful author-hosted full text at https://www.voutsadakis.com/RESEARCH/PUBLISHED/limcyc.pdf.
5. *Majority C-colorings of complete multipartite graphs*, publicly available published-finding corpus scientific record, 4 October 2026. The static-coloring result is distinct from temporal two-cycle enumeration.
6. *Sharp period-four census for complete multipartite parity automata*, publicly available published-finding corpus scientific record, 11 October 2026. The XOR update is distinct from strict majority.
