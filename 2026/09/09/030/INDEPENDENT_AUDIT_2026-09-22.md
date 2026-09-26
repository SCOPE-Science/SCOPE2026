# Independent audit — 2026/09/09/030

Date: 2026-09-26. Disposition: retain accepted.

## Correctness — PASS

I generated all (inom{10}{3}) triples with gcd one: exactly 109. For every triple I independently iterated the mex recurrence through heap 500, recomputed the least candidate period by scanning (p=1,ldots,200), setting its cutoff to one after the last mismatch, and accepted a closing window only when (N_0+p+m-1le500). Every one of the 109 stored rows agrees in (N_0,p,M,h,nP). The totals are 99 pure, 10 impure, maximum cutoff 21, maximum period 45, and windowed nim-value distribution 6/45/58 for values 1/2/3. A repeated block of length (m) closes under the deterministic mex recurrence, so the table certifies infinite eventual tails. If a smaller period held on any later tail, it would also hold from (N_0), since the established period (p) propagates every index backwards into that tail; the finite mismatch excludes this. The early mismatch at (N_0-1) checks minimal cutoff for (p). A three-move mex is always at most 3, so the maximum-four exclusion is elementary and should not be read as a separate discovery.

## Originality — PASS, narrow

Manabe's 2026 paper gives a sufficient criterion for pure periodicity of three-move rulesets; Golomb's eventual-periodicity result and the subsequent algorithmic literature do not supply this complete 109-row table of exact least periods, preperiods and heap-500 statistics. I found no matching published table in the checked sources. The closing-window argument and recurrence themselves are standard; the contribution is the certified finite classification for this specified family.

## Scientific value — PASS, bounded

The exact 10 impure cases, the largest cutoff ({2,8,9}), and periods 45 and 22 for ({3,7,10}) and ({2,5,7}) offer small, reproducible examples against which three-move periodicity criteria can be tested. Heap-500 cold counts and witness positions are windowed statistics; no general formula is established.

## Sources

- Manabe, *Purely Periodic Three-move Subtraction Games*, arXiv:2609.05358: https://arxiv.org/abs/2609.05358
- Eppstein, *Faster Evaluation of Subtraction Games*, arXiv:1804.06515: https://arxiv.org/abs/1804.06515
- Candidate `RESULT.md` and `artifacts/census.json`; independent complete mex and least-period replay described above.
