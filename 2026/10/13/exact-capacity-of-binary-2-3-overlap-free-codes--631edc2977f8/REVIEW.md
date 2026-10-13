# Self-review

## Correctness — PASS
The theorem fixes binary words of length \(n\ge6\), explicitly forbids overlaps of exactly lengths \(2\) and \(3\), and includes self-overlaps. Every code projects to a three-bit prefix/suffix boundary; the middle gives at most \(2^{n-6}\) choices per pair. The four-state binary De Bruijn adjacency yields a complete \(b=0,1,2,3,4\) upper-bound case split, and the concrete two-prefix/five-suffix product attains it. The standard-library checker independently enumerates all 256 prefix choices and confirms the kernel optimum 10; finite checks do not stand in for the all-length argument.

## Originality — PASS, residual risk disclosed
Stanovnik's general restriction boundary-lifting formula is credited, not presented as new. The inspected full text has only a known exact \((1,2)\) maximum, while Yang–Ding give counts of constructed families rather than an unrestricted exact \((2,3)\) maximum. The 2022 Blackburn et al. table proves a different \((1,3)\) maximum equal to six boundary words, whose length-one constraint is absent here; its upper bound therefore does not imply ten. Relevant accessible primary full texts were examined beyond abstracts. Inaccessible potentially related publications and alternate older graph formulations are residual bibliographic risks; searches do not certify absolute uniqueness.

## Value — PASS
The exact optimum of the first consecutive restricted-overlap interval starting after length one is a naturally motivated synchronization-code capacity, with a self-contained structural bound. Determining the six-boundary optimum gives a complete capacity formula for every length at least six, rather than only a lower-bound construction. No error-correcting property or all-interval generalization is claimed.

## Closest literature and limitations
See Stanovnik (arXiv:2411.02899), Yang–Ding (doi:10.1587/transfun.2025EAL2050), Blackburn et al. (arXiv:2211.10309), and the abstract of Cai–Wang–Feng (doi:10.1109/TIT.2023.3319010). The theorem is solely binary, for \(n\ge6\) and exact forbidden-overlap set \(\{2,3\}\). Independent verification and a comprehensive bibliographic originality certification are not claimed.

Self-review: passed. Independent audit: not yet performed.
