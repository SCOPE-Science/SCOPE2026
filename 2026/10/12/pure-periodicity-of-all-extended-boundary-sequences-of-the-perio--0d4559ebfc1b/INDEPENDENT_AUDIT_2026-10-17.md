# Independent mathematical audit

## correctness

PASS

Let k=ceil(log₂ℓ), P=2^k. Each ℓ-window has at most one hole index j+1≡0(mod P), while its nonhole symbols depend only on index mod P. For fixed starting residue i mod P, if both windows contain holes their valuations depend on q and q+Δ where Δ=(d+b−a)/P>0. The complete parity-pair set is {(0,0),(0,1),(1,0)} for odd Δ and all four for even Δ, with each pattern attained on arbitrarily large integer q through congruence choices. Shifting d by 2P preserves all nonholes, hole positions and Δ parity; hence entire boundary sets agree for every d>=ℓ, not just eventually. At most 4 patterns per each of P residues give 4P bound. Independently compared direct substitution/valuation prefixes with residue formula and shift for ℓ<=12; those finite tests are secondary to the all-width proof.

## originality

PASS

Rigo–Stipulanti–Whiteland introduce extended boundary sequences and prove broad automaticity, with different Thue–Morse, Fibonacci and Sturmian examples. Their inspected main result is weaker than pure periodicity for the canonical period-doubling word, uniform across all window widths and with an explicit linear period. Guo–Lü–Wen discuss ordinary width-one boundary sequences, and full text was unavailable; possible overlap for ℓ=1 is acknowledged, but the all-width theorem is not claimed as a consequence of an isolated width-one result.

## value

PASS

Extended boundary sets are a natural language-combinatorial invariant measuring all two-window endpoint pairs. Pure periodicity in separation of an aperiodic automatic word is a structural strengthening over mere 2-automaticity, and the theorem supplies a uniform exact construction and linear-size/period bounds for every width, rather than a sparse finite census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
