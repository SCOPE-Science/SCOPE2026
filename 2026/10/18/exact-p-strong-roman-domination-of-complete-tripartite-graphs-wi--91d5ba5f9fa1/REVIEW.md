# Independent mathematical audit

## correctness

PASS

In a part all positive vertices see the same exterior zero set. If there is only one defender part, that part is all positive, and the exterior positive count cannot decrease the baseline-plus-one-ceiling lower bound. If two defender parts exist (even if a third also exists), choose one defender from each. Decreasing either selected part's positive count down to one removes a baseline unit per step and increases at most one ceiling by at most one. With t positive vertices in the third part, reducing t to zero changes each ceiling by at most ceil(t/p); for t>=2, 2 ceil(t/p)<=t, so only t=0 or 1 can improve the minimum. All-positive assignments are bounded below by W1; the three constructions are legal and attain their costs. For a>=4 and p=2a−2 the costs are (a+2,6,5). At total weight five every defender in this family sees a zero neighbor since each part has at least eight exterior vertices. Two positive defenders alone would both need label three. For two label-two defenders and a unit label, the latter must be outside both defender parts to bring both zero-neighbor counts down to p. These and only these assignments give 3a^3. Independent direct predicate replay (/workspace/branches/a0cfb095-52ec-4d11-bb69-f857fb501bc6/replay.py and replay.out) found optimum 4 with 42 minima for (2,2,2), p=3 from 4096 labelings, and zero below 5 and 192 at 5 for (4,4,4), p=6, from 6031 candidates of weight at most 5. The uploaded script and recorded output were inspected, not executed; the replay is not the general proof.

## originality

PASS

A distinct 2026/10/26 Resultary record exactly subsumes the value formula for 3<=p<=Δ−1 via its two-defender residue correction, but is catalogued later than this frozen record and does not enumerate the minimizers. This is equivalent coverage now, not evidence by itself of anterior priority. Earlier ordinary Roman results cover the routine p>=Δ branch, and earlier inspected p-strong results for bipartite graphs do not settle the third-part auxiliary-label regime. The substantive contribution assessed here is the three-regime characterization for 3<=p<=Δ−1 and the sharp balanced-family census, not the Roman boundary or a claim that the later multipartite formula differs on their common domain.

## value

PASS

An exact optimization for a natural family distinguishes a genuine third mode, where placing a positive vertex without choosing it as a defender saves two capacity units for a cost of one. The balanced family proves the regime is necessary for infinitely many instances and classifies all optimal labelings there. This is not justified by the routine ordinary Roman boundary alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
