# Scientific review: exact cyclic-transect richness realization

## Correctness — PASS

The proof is self-contained conditional on the classical strong NP-completeness of 3-PARTITION. Its central identity counts every missed translated window once via its unique maximal cyclic absence run. Successive exact differences recover the entire pooled gap-length multiplicity sequence. A row must reserve one occupied separator cell per zero run, giving compulsory item size \(g+1\), and a feasible packing gives a constructive cyclic binary row. The two directions establish necessity and sufficiency, not just a relaxation. The reduction from 3-PARTITION uses \(n=B\) and \(s=m\), saturates total capacity, and is polynomial on the strongly NP-hard restricted instances because \(B\) is polynomially bounded. The exact-rational checker directly counted \(38{,}373\) small incidence matrices and also enumerated all capacity-bounded gap histograms for the stated smaller cases. Those finite tests do not prove the all-size theorem; the combinatorial argument does.

## Originality — PASS, with residual risk

Tjørve et al. (2008; DOI 10.1111/j.1365-2745.2008.01433.x) treat gridded species occupancy and wrapped-around spatial sampling, infer qualitative effects of occupancy and aggregation, and mention reverse inference. Storch (2016; DOI 10.1111/jvs.12428) explicitly contrasts sliding-window designs with other species–area sampling. Colwell et al. (2004; DOI 10.1890/03-0557) analyze exchangeable order of quadrat observations, not this spatial mean. Material readings of these sources found no exact pooled zero-gap spectrum, cross-species realizability iff bin packing, or corresponding strong NP-completeness. Semantic searches for the same curve, cyclic zero-run inversion, and packing equivalence identified related published work on bin packing, independent random species discovery, and incidence complexes; full text of Ota and Manada (2024; DOI 10.1587/transfun.2023TAP0015) reconstructs one circular word from all substring frequencies, not species assignment from aggregate zero-window counts. The 3-PARTITION theorem is credited as known, and no claim is made that run-length counting is a novel mathematical primitive. The 1997 Leitner–Rosenzweig study and a 2013 circular-run article were inspected only through accessible abstracts; undetected stronger prior coverage remains a scientific risk.

## Value — PASS

The exact mean richness of translated contiguous habitat blocks is a motivated spatial version of a species–area curve. The theorem identifies exactly what information such profiles preserve and shows that consistency of apparently well-behaved profiles is nonlocal: even monotone, concave, denominator-compatible observations can fail to correspond to any finite community. Its constructive boundary and strong hardness classification illuminate what spatial information can and cannot be inferred from an all-scale summary. This does not claim broad ecological generality, robust estimation with noisy data, or identifiability of individual species layouts.

## Boundaries

The results apply only to finite circular binary transects with each species present and the mean over all translations. The claim does not cover random independent quadrat subsets, irregular observation weights, open-boundary linear transects, or arbitrary two-dimensional windows. No independent validation or independent novelty audit has been performed.

Self-review: passed. Independent audit: not yet performed.
