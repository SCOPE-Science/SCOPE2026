# Scientific review

**Claim reviewed.** For homogeneous binary habitat patches with local independent recolonization/extinction and a common Poisson catastrophe that independently clears occupied patches with fixed probability, three simultaneous stationary joint-occupancy moments uniquely identify the severity and normalized local/catastrophe rates. A complete feasible moment region, two-patch impossibility, and exact local conditioning formula accompany this same inverse theorem.

## Correctness — PASS

The finite irreducible generator gives \([j(a+b)+c\{1-(1-q)^j\}]p_j=ja p_{j-1}\). Setting \(s=cq/(a+b+cq)\) yields \(p_1=x(1-s)\), \(1-p_1^2/p_2=sq/2\), and \(1-p_1p_2/p_3=s(q-q^2/3)\). These equations have the claimed unique inverse. Their parameter inequalities are necessary and sufficient: choosing any time scale reconstructs strictly positive rates; varying \(q\) locally while preserving \(sq\) proves nonidentification with two sites. The Jacobian is verified by factorization, not by numerical sampling. The standalone exact checker constructs the finite generators for three and four sites, independently solves stationary linear systems, and checks 216 rational parameter choices (10,975 exact assertions). A finite checker supports the algebraic proof but does not replace it.

**Limits and risks.** The result does not establish inference under unknown detection, heterogeneous sites, random shock severities, nonstationary measurements or finite-sample noise. Absolute rates cannot be recovered without an external time scale. Approaching vanishing catastrophe severity is ill-conditioned.

## Originality — PASS within inspected evidence

Kapodistria, Phung-Duc and Resing, *Linear birth/immigration-death process with binomial catastrophes* (EURANDOM Preprint Series 2015-006, dated March 16, 2015), derive a classical **forward** factorial-moment formula (3.5), and prove an ordering in Lemma 5.2 for fixed effective catastrophe rate with varying shock severity; an algebraic continuation of this formula matches the present homogeneous finite-patch moment recursion. This forward formula is not new. The final claim instead establishes an explicit **inverse**, an if-and-only-if attainable spatial-moment domain, sharp three-site identifiability and a conditioning determinant. The directly inspected sections did not assert these results. Economou (2004), Artalejo et al. (2007), and Dorazio et al. (2010) supply related probability and ecological-inference frameworks, but full text of the first two journal articles could not be checked. Literature and published mathematical-result searches using severity, common shock, stationary joint occupancy, and moment inversion aliases found no covering claim. These negative searches are not proof of novelty.

**Residual priority risk.** The result is an elementary inversion of a known moment structure. A stronger general identification theorem, especially in older inaccessible catastrophe-process or ecological-inference literature, might subsume it. Only a provisional self-review originality assessment is supported.

## Value — PASS

Ecological occupancy observations often confound catastrophic-event frequency and per-event removal severity. With two simultaneous patches this confounding is exact, even under noise-free stationary data; a third patch separates these mechanisms in a fully explicit model. The sharp site count, testable attainable region, and quantitative ill-conditioning address model design and identifiability rather than an arbitrary numerical slice. The result does not claim field-data effectiveness, statistical efficiency, or a general metacommunity theorem.

Self-review: passed. Independent audit: not yet performed.
