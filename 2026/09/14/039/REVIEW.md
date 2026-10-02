# Review status

Fresh independent audit completed on 2026-10-01 UTC.

Disposition: **passed**.

- Correctness: **PASS** — I independently checked that the displayed 22 triples are linear, have degree sequence twelve 5s and one 6, and contain no six-edge loose path by enumerating all 6-edge subsets and testing the intersection graph/13-vertex condition. A separate fresh enumeration rebuilt the punctured cyclic STS(13) pair, found exactly 144 linearly addable cross triples, and verified that each creates a P6. The n=9,10,11,12 witnesses are linear; the stated packing bounds prove n=9,10,12 optimal, and the n=11 degree/pair-deficit argument rules out 18 edges.
- Originality: **PASS** — The inspected linear-path Turan literature does not cover this explicit k=3, P6 linear-host witness or imply density 22/13. The principal exact theorem of Furedi-Jiang-Seiver is for uniformity at least 4, while the recent linear 3-graph paper located concerns P5.
- Scientific value: **PASS** — The 22-edge witness improves the density from 5/3 to 22/13 and therefore invalidates a concrete proposed extremal block picture. That is a meaningful structural counterexample, and the auxiliary rigidity/small-order facts sharpen the boundary without claiming an unfinished global classification.

See `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json` for structured source comparisons and residual risks.
