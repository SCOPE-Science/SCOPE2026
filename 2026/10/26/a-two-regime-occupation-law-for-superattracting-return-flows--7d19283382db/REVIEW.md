# Review

## Correctness — PASS

The proof reduces the return-map asymptotic to \(u_{n+1}=p u_n-\log c+O(e^{-\delta u_n})\), establishes the cycle-count law in each duration regime, and then uses \(b_n\to b_0\) to obtain the occupation-time asymptotic. The example's return map is reconstructed from the slow/fast branches, and the exact solution of \(\dot y=-y^2\) gives the stated duration scale. The symbolic check verifies the return-map coefficients; the analytic proof establishes the infinite-time claim.

## Originality — PASS

The closest source for the example gives a qualitative statistical-attraction statement and the return-map expansion, but not the class-level occupation law. The later bounded-return-time paper studies related return-time properties and a homoclinic-loop setting, but the inspected sections do not state this two-regime rate theorem. Targeted database and literature searches found adjacent results on other return maps and occupation statistics, not an equivalent statement for the stated class. This is a best-knowledge originality assessment, not a proof of global novelty.

## Value — PASS

The result separates two natural flight-time mechanisms that can share the same superattracting return-map order. It gives the leading growth of excursion counts and the exact leading coefficient of the time fraction outside a target neighbourhood, refining qualitative statistical attraction into a usable observation-time law. Its scope and unproved extensions are stated explicitly.

## Closest literature and limitations

- Oljača, Ashwin, and Rasmussen (2022), DOI 10.1007/s10884-022-10196-5: source of the piecewise-smooth example and its qualitative statistical-attraction analysis.
- Newman, Ashwin, and Rasmussen (2025), DOI 10.1088/1361-6544/adbe21: related bounded-return-time and homoclinic-loop analysis; only relevant sections were used for comparison.
- Karabacak and Ashwin (2011), DOI 10.1017/S0305004110000642: background on statistical attractors and time averages.

Residual risk remains that an unindexed source contains a comparable general occupation law.

Self-review: passed. Independent audit: not yet performed.
