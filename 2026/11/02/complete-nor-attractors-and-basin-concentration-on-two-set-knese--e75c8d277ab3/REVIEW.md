# Scientific review

## Correctness — PASS

For synchronous **open-neighborhood** binary NOR on the two-set Kneser graph, the update map is a symmetric antitone polarity. This gives the exact identity \(F^3=F\), and a case distinction on the two-spoke representation of every edge family with a two-vertex cover determines all possible images. Each listed attractor is closed under \(F\). Individual basin multiplicities follow from explicit inverse-fiber conditions, not from numerical fitting. The closed formula for the distinguished basin follows by subtracting all others; Bonferroni bounds yield the asymptotic and the sharp \(n=6\) threshold. Separately implemented Python and C++ enumerations confirm all state-space populations for \(n=5,6\) and \(n=5,6,7\), respectively. These finite calculations do not replace the universal proof.

## Originality — PASS, qualified

Aledo–Martínez–Valverde's open-access 2015 survey supplies general minterm/maxterm background but not the exact basin census on \(KG(n,2)\). The examined 2017 and 2020 primary papers analyze local maps that incorporate a site's **own** bit; our update excludes it, which materially changes the conclusion and permits both fixed and two-periodic states. Previously known NOR period restrictions do not imply the seven attractor-shape rows or the inverse-fiber populations. Related results on binary XOR dynamics of the same Kneser graph concern a different map. Full text of the original 2012 article could not be examined, leaving a qualified historical-overlap risk; searches of research records and literature do not establish absolute novelty.

## Mathematical value — PASS

The result classifies every attractor and basin of a canonical infinite graph family and provides explicit polynomial attractor counts. It exhibits an exact \(n=6\) threshold at which one oscillatory basin becomes a strict majority, with the probability of all other basins of order \(2^{-\Theta(n^2)}\) even while the number of attractors grows. The complete inverse-fiber census is a motivated dynamical invariant and is not a selected computational slice.

## Closest literature and limitations

See Aledo et al., *Journal of Applied Mathematics* (2015), DOI 10.1155/2015/594294; Aledo et al., *Complexity* (2017), DOI 10.1155/2017/7209762; Aledo et al., *Complexity* (2020), DOI 10.1155/2020/9708347; and the 2012 maxterm/minterm antecedent, DOI 10.1016/j.mcm.2011.08.040 (abstract only). Finite verification reaches only \(n=7\); the proof is for all \(n\ge5\). The result excludes self-inclusive NOR, higher-set Kneser graphs, and other schedules. Independent expert review is still required before scientific publication.

Self-review: passed. Independent audit: not yet performed.
