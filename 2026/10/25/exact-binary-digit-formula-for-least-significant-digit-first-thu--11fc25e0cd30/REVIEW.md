# Self-review

**Correctness — PASS.** The canonical residual transition follows exactly from binary digit-sum parity and division with carry. An explicit eventual-aperiodicity contradiction proves distinct reachable pairs are distinguishable. The depth-by-depth residue intervals and their separation above first coordinate one justify every term of the closed formula; the exceptional coordinate-two cases and both sharp extrema have been individually considered. Two independent computational checks (reachability and output-partition minimization) replay successfully.

**Originality — PASS within examined sources.** The closest Thue–Morse paper, Moradi–Rampersad–Shallit, arXiv:2512.10017v5, §4.2, Theorems 19–20, addresses **MSD-first** shifted Thue–Morse, not the LSD-first count; its general LSD construction does not imply the exact residue formula. Moradi–Popoli–Shallit–Vukusic, arXiv:2603.18858v1, studies LSD-first Fibonacci-word shifts in Zeckendorf representation; the 2021 Charlier–Cisternino–Massuir paper treats \(m\mathcal T+r\) rather than shift-output residuals. Relevant comparable historical results on **MSD-first** Thue–Morse shifts were excluded rather than subsumed. Semantic research-record searches produced no equivalent exact LSD formula. Remaining priority risk: possible unindexed equivalent statement.

**Mathematical value — PASS.** Precise minimal-state complexity under shifts is a natural descriptional-complexity invariant. The binary-digit formula settles it for every shift, including sharp fluctuations at a fixed binary length. This is a strong complement to the known polynomial state growth in the opposite input orientation, and more informative than a generic logarithmic bound or a short lookup table.

Scientific limitations: only binary Thue–Morse, LSD-first, arbitrary trailing-zero encodings; no other automatic sequence, base, or MSD automaton covered. Self-review are not independent validation.

Self-review: passed. Independent audit: not yet performed.
