# Two Poisson windows for saturation of mixed modal relations

## Finding
Let \(W_n=\{1,\ldots,n\}\) and sample two independent reflexive binary relations \(A_n,B_n\) on \(W_n\): every diagonal pair is present, and every off-diagonal ordered pair is independently present in either relation with probability \(p_n\). Write
\[
C_n=(A_n\circ B_n)\cup(B_n\circ A_n),\qquad
Z_n=|W_n^2\setminus C_n|,
\]
and \(X_n=|W_n^2\setminus(A_n\circ B_n)|\), \(Y_n=|W_n^2\setminus(B_n\circ A_n)|\), with relational composition denoting a two-step walk. These are exact counts of missing ordered pairs, not counts of missing individual edges.

**First (mixed-closure) window.** If \(np_n^2=\log n+t\) for fixed \(t\in\mathbb R\), then
\[
Z_n\xrightarrow{d}\operatorname{Poisson}(e^{-2t}),\qquad
\frac{X_n}{ne^{-t}}\xrightarrow{\Pr}1,\qquad
\frac{Y_n}{ne^{-t}}\xrightarrow{\Pr}1.
\]
For each sampled pair \((A_n,B_n)\), there are exactly \(2^{Z_n}\) reflexive third relations \(R\) making the trimodal Kripke frame validate
\[
(\mathsf{mix})\quad\Box q\longrightarrow\Box_1\Box_2q\land\Box_2\Box_1q.
\]
Consequently, its number of admissible third-relation expansions converges in distribution to \(2^P\), where \(P\sim\operatorname{Poisson}(e^{-2t})\), and the probability of **a unique expansion** tends to \(\exp(-e^{-2t})\).

**Second (ordered-composition) window.** If \(np_n^2=2\log n+t\), then
\[
(X_n,Y_n)\xrightarrow{d}(P_1,P_2),
\]
where \(P_1,P_2\) are independent \(\operatorname{Poisson}(e^{-t})\) variables. Hence the probability that **both** compositions already equal \(W_n^2\) tends to \(\exp(-2e^{-t})\), while \(C_n=W_n^2\) with probability tending to one.

For each fixed \(c\in(1,2)\) with \(p_n=\sqrt{c\log n/n}\), one has simultaneously
\[
\Pr(C_n=W_n^2)\longrightarrow1,\qquad
\frac{X_n}{n^{2-c}}\xrightarrow{\Pr}1,\qquad
\frac{Y_n}{n^{2-c}}\xrightarrow{\Pr}1.
\]
Thus there is a genuine intermediate regime: the mixed interaction forces a unique universal third accessibility relation even though neither ordered two-step relation is universal. All claims concern *arbitrary reflexive trimodal Kripke frames validating the stated axiom*, not necessarily Cartesian products of component frames.

## Assumptions and scope
The two relations are sampled independently; edges with different colours may coexist on the same ordered pair. All loops in each sampled relation are deterministically present. The two composition orders are kept distinct. Here \(n\to\infty\), logarithms are natural, and the displayed critical-window equalities determine \(p_n\in[0,1]\) for all sufficiently large \(n\). All limiting probabilities and distributions refer to this Bernoulli sampling measure. The modal formula is required to hold at every world under *every* valuation of its propositional letter. We make no assertion about conditional sampling of the entire triple uniformly from all satisfying triples.

## Proof
**1. Exact modal correspondence and expansion count.** For any relations \(A,B,R\), the usual Kripke clauses show that \(\Box q\to\Box_1\Box_2q\) is valid under all valuations exactly when \(A\circ B\subseteq R\), and likewise for the other order. Necessity follows by choosing the truth set of \(q\) to be \(R(w)\) at a world witnessing noncontainment. Thus \((\mathsf{mix})\) is equivalent to \(C\subseteq R\). Since \(A\) and \(B\) are reflexive, \(C\) is reflexive. The third relation may include each of the \(Z=|W^2\setminus C|\) remaining off-diagonal ordered pairs independently, proving the exact expansion count \(2^Z\).

**2. Exact one-point probabilities.** Fix \(a\ne b\). The event \((a,b)\notin C_n\) requires \((a,b)\notin A_n\cup B_n\). For each \(j\notin\{a,b\}\), both independent witnesses \(A_n(a,j)B_n(j,b)\) and \(B_n(a,j)A_n(j,b)\) must be absent. Edges used for distinct intermediate vertices are disjoint. Therefore
\[
\Pr((a,b)\notin C_n)=(1-p_n)^2(1-p_n^2)^{2(n-2)},
\]
whereas
\[
\Pr((a,b)\notin A_n\circ B_n)=(1-p_n)^2(1-p_n^2)^{n-2}.
\]
The same formula holds for the reverse composition. Diagonal pairs are never missing. In particular,
\[
\mathbb EZ_n=n(n-1)(1-p_n)^2(1-p_n^2)^{2(n-2)},
\]
\[
\mathbb EX_n=\mathbb EY_n=n(n-1)(1-p_n)^2(1-p_n^2)^{n-2}.
\]

**3. Uniform joint absence estimate.** Fix nonnegative integers \(r,s\) and prescribe \(r\) distinct ordered off-diagonal pairs to be absent from \(A_n\circ B_n\), and \(s\) distinct ordered off-diagonal pairs to be absent from \(B_n\circ A_n\). A pair may appear once in each prescribed list. Write \(h=r+s\), and let \(T\) be the set of their endpoints, so \(|T|\le2h\). For every intermediate vertex \(j\notin T\), there are precisely \(h\) distinct elementary two-edge witness events, each of probability \(p_n^2\). Any two distinct witness events use at least three distinct random edges (even if prescribed pairs share a tail or head). Bonferroni's inequalities give the uniform probability
\[
1-hp_n^2+O_h(p_n^3)
\]
that all witnesses via this \(j\) are absent. Different outside intermediates involve disjoint random edge variables. The finitely many prescribed constraints with intermediate vertices in \(T\), including the forced-loop cases, have joint probability \(1+O_h(p_n)\), and use only edges within \(T\), disjoint from outside constraints. Therefore, whenever \(p_n=O(\sqrt{\log n/n})\),
\[
\Pr(\text{all \(h\) prescribed absences})
=(1+O_h(p_n))\bigl(1-hp_n^2+O_h(p_n^3)\bigr)^{n-|T|}
=(1+o(1))e^{-hnp_n^2},
\]
uniformly over the prescribed lists. The same proof applies when each prescribed absence means *simultaneous absence from both compositions*: there are two elementary witnesses per prescribed ordered pair, hence \(h\) is replaced by twice the number of prescribed pairs.

**4. First window and intermediate separation.** At \(np_n^2=\log n+t\), each ordered \(k\)-tuple of distinct missing pairs for \(C_n\) has joint probability \((1+o(1))n^{-2k}e^{-2kt}\). There are \((n(n-1))_k\sim n^{2k}\) such tuples; consequently all fixed factorial moments of \(Z_n\) tend to \((e^{-2t})^k\). The Poisson moment criterion gives the claimed convergence, and \(2^{Z_n}\) follows by the continuous mapping theorem on the discrete integer-valued domain. For a single composition, the joint absence estimate with \(h=2\) makes the ratio of the probability of two distinct holes to the square of the one-hole probability tend uniformly to one. Since \(\mathbb EX_n\sim ne^{-t}\to\infty\), this gives \(\operatorname{Var}(X_n)=o((\mathbb EX_n)^2)\), and hence concentration; similarly for \(Y_n\). For \(np_n^2=c\log n\) with fixed \(1<c<2\), \(\mathbb EZ_n\sim n^{2-2c}\to0\), whereas \(\mathbb EX_n=\mathbb EY_n\sim n^{2-c}\to\infty\); Markov's inequality and the same second-moment argument prove the intermediate regime.

**5. Second window and independence.** At \(np_n^2=2\log n+t\), expand any mixed factorial moment \(\mathbb E[(X_n)_r(Y_n)_s]\). Configurations in which the selected pairs in the two lists are all different contribute \((1+o(1))n^{2(r+s)}\cdot n^{-2(r+s)}e^{-(r+s)t}\to e^{-(r+s)t}\). Configurations with at least one pair repeated *between* the two lists have \(O_{r,s}(n^{2(r+s)-2})\) possibilities and the uniform joint bound makes their total contribution \(O_{r,s}(n^{-2})\). Thus every fixed mixed factorial moment tends to \((e^{-t})^{r+s}\), those of independent Poisson variables. Joint convergence follows. Finally \(\mathbb EZ_n\sim n^{-2}e^{-2t}\to0\), so \(C_n=W_n^2\) with probability tending to one.

## Verification
The standalone `check_mixed_modal.py` exhaustively enumerates all ordered pairs of reflexive relations on \(n=1,2,3\) labelled worlds and independently computes compositions both via row-bitsets and direct existential quantification. It tests every possible reflexive third relation and every valuation against the modal axiom. The distributions of \(Z_n\) on \(n=2,3\) are respectively \(\{0:9,1:6,2:1\}\) among \(16\) ordered relation pairs and \(\{0:2342,1:576,2:786,3:280,4:93,5:18,6:1\}\) among \(4096\) pairs. The totals of allowed third relations are respectively \(25\) and \(11006\). The program also checks the exact first-moment formulas at \(p=1/2\) with rational arithmetic. Run `python3 check_mixed_modal.py` with a standard Python 3 installation. These exhaustive finite checks corroborate the correspondence and counts, not the infinite Poisson limits; the latter are proved in Steps 3–5.

## Relationship to prior work
Aghamov, Kudinov, Nguyen, and Piribauer (2026), Proposition 3.2 and Corollary 3.3, establish the classical deterministic relational meaning of \((\mathsf{mix})\) for the relevant trimodal Kripke logics. The present two-window random expansion law is not claimed to extend their neighborhood-product completeness theorem, nor are arbitrary sampled relations claimed to be Cartesian-product accessibility relations. Their work supplies the natural interaction axiom and exact frame class, rather than either probability law.

Heckel and Riordan (2012) establish threshold results for **existence of a suitable two-colouring** in undirected random graphs, using coloured two-step paths. Their graph-colouring optimization question is different from two independent directed Bernoulli relations whose colours are fixed in advance and may overlap. The first/second Poisson windows and the count of admissible third-modal relations do not follow directly from the stated rainbow-connection theorems. The factorial-moment method and rare-witness estimates are standard probabilistic tools; no priority is claimed for those methods.

## Limitations
The construction is a specific independent-edge reflexive finite Kripke model; it does not cover arbitrary neighborhood frames, Cartesian products, or dependent edge-colour models. The finite verifier stops at three worlds, so finite enumeration alone cannot prove the asymptotic statements. Literature comparison cannot certify absolute priority: a general older theorem about zero entries of Boolean matrix products or random coloured directed diameter could subsume some or all of the distributional calculations. The displayed convergence of \(2^{Z_n}\) is **in distribution**; no assertion of convergence of its expectation is made.

## References
1. R. Aghamov, A. Kudinov, M. T. Nguyen, J. Piribauer, *On Modal Logics of Full Products of Neighborhood Frames*, arXiv:2606.31852, version first posted June 30, 2026, especially Proposition 3.2 and Corollary 3.3. https://arxiv.org/html/2606.31852v1
2. A. Heckel, O. Riordan, *The Hitting Time of Rainbow Connection Number Two*, Electronic Journal of Combinatorics **19** (2012), #P37, doi:10.37236/2708. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v19i4p37/pdf/
