# Complete minimum circular-attractor census of binary order-five de Bruijn cycles

## Finding

Every binary de Bruijn cycle of order five has a circular string attractor with exactly seven positions, and none has one with six or fewer. Up to cyclic rotation, there are exactly \(2048\) such cycles. Across these cycles, the number of seven-position minimum attractors ranges from \(216\) to \(368\); the lower extreme occurs in exactly four cycles and the upper extreme in exactly two. There are exactly \(120\) distinct attained counts, and the aggregate number of minimum attractors over the \(2048\) rotational classes is \(589120\). The complete cycle-by-cycle counts appear in `census.csv`.

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\). A binary order-five de Bruijn cycle is a cyclic word of length \(32\) in which every binary length-five factor appears precisely once at a cyclic starting position. Positions are indexed \(0,1,\ldots,31\) modulo \(32\). A circular attractor \(\Gamma\) meets at least one cyclic occurrence of every distinct nonempty factor of every length from \(1\) through \(32\). Cycles differing only by rotation are identified; reversing or complementing letters is *not* used to identify cycles. A unique length-five factor \(00000\) fixes the canonical rotation, so all reported words start with `00000`. Their optimal-attractor counts are invariant under rotation.

This is an exact finite classification at order five. It does not assert the same equality or count distribution at any other order.

## Proof

**Sharp seven-position lower bound.** Every one of the \(32\) cyclic length-five factors occurs once. A selected position is contained in exactly five length-five windows, hence \(s\) selected positions can intersect at most \(5s\) such windows. Therefore every circular attractor has at least \(\lceil32/5\rceil=7\) positions.

**Exhaustive enumeration of the objects.** Associate each cyclic starting position to the integer between \(0\) and \(31\) representing its length-five window. Consecutive windows \(x,y\) necessarily obey \(y=(2x+b)\bmod32\) for a bit \(b\in\{0,1\}\). The \(32\) distinct windows form a directed Hamilton cycle on the graph with precisely these transitions. Every such Hamilton cycle has a unique vertex \(0\), so rooting it there chooses a unique representative. Conversely, along any rooted Hamilton cycle, take the leading bit of each visited five-bit vertex. The overlap condition reconstructs those vertices as the length-five cyclic windows of the resulting word, so this is a bijection. The depth-first procedure `cycles()` in `verify.py` branches over both transition bits whenever the next five-bit vertex has not appeared, and requires a return edge to zero after all \(32\) vertices. These cases exhaust every rooted Hamilton cycle, with none repeated. The checker obtains exactly \(2048\), agreeing with the classical binary de Bruijn necklace count \(2^{2^{4}-5}\).

**Exhaustive enumeration of all candidate attractors.** Fix a circular set \(\Gamma\) of seven zero-based positions. It intersects all length-five windows if and only if every clockwise gap between consecutive selected positions is at most five. Necessity: a gap exceeding five leaves a length-five window unmarked. Sufficiency: any unmarked length-five window would create such a gap. The verifier enumerates *all* \(\binom{32}{7}\) subsets by `itertools.combinations` and retains exactly \(384\) satisfying this equivalence. There is no sampling.

**Reduction of the remaining checks to short factors.** Once \(\Gamma\) meets every length-five window, every cyclic factor of length at least five has an occurrence intersecting \(\Gamma\): in fact, its first five positions already contain a chosen position, for any occurrence. For each shorter factor \(u\) of length \(\ell\in\{1,2,3,4\}\), define its occurrence-position incidence mask

\[
H_u=\bigvee_{s:\,w[s\ldots s+\ell-1]=u}\;\bigvee_{j=0}^{\ell-1}2^{(s+j)\bmod32}.
\]

All word indices in the formula are circular. If \(C_\Gamma=\bigvee_{p\in\Gamma}2^p\), then \(\Gamma\) covers \(u\) if and only if the integer bitwise intersection \(C_\Gamma\mathbin{\&}H_u\) is nonzero. The verifier computes every occurrence mask directly from the \(32\) cyclic start positions. Consequently, checking the \(30\) distinct short factors using these masks is both necessary and sufficient for each of the \(384\) seven-position candidates.

**Finite exhaustion and counts.** Applying this exact test to each of the \(2048\) rooted Hamilton cycles yields at least one surviving seven-position subset in every case. Its count per cycle is written in `census.csv`; the program asserts every reported numerical extreme and aggregate, including the minimum \(216\) appearing four times, the maximum \(368\) appearing twice, \(120\) distinct count values, and total \(589120\). Combined with the lower bound, every survivor is a minimum circular attractor and no other minimum attractors have been omitted. This finishes the exhaustive finite proof.

As explicit extremal witnesses, the four minimum-count canonical cycles are

`00000100111110101101110010100011`, `00000101001000110101110011111011`,
`00000110001010011101101011111001`, and `00000110111110011101011000100101`.

The two maximum-count canonical cycles are

`00000100011010011101111100101011` and `00000110101001111101110010110001`.

## Verification

Run `python3 verify.py` in the directory containing that file. It writes a deterministic complete `census.csv` and prints all checked invariants. Standard Python alone suffices; no external library, solver, network connection, precomputed data, or other source files are needed. `verify_output.txt` contains the actual recorded output. Its CSV digest, `8bb608eb66f3bfac0152475146822a21df2a5ecb9665f2f9193ef22ec4291ea2`, is separately checked by rerunning the program. As a check independent of the short-factor mask equivalence implementation, the verifier directly enumerates the distinct circular factors at *every length* from one to \(32\) for all \(384\) seven-subsets on each of the six extremal cycles, and confirms identical decisions.

The exact claims rest on complete deterministic enumeration plus the mathematical completeness arguments above, not on random samples or asymptotic extrapolation.

## Relationship to prior work

Banbara and collaborators (first publicly available February 18, 2026) classify smallest *linear* attractors for several substitution word families and demonstrate why full extremizer counts have independent mathematical content. They do not examine order-five de Bruijn cycles. Mantaci and collaborators (2021) introduce circular attractors but study de Bruijn words in their *linear* form, deriving asymptotic bounds; their Proposition 41 does not classify circular minimizers. Romana (2023) supplies a general circular-attractor verification algorithm and complexity results, not an all-cycle order-five census. Whittington (2024, Section 5) explicitly discusses the difficulty of transferring sharp attractor covers among de Bruijn sequences and proves a result for the Lyndon-generated representative at prime orders with a chosen *linear unfolding*. That result neither quantifies nor enumerates minimum circular attractors across all \(2048\) order-five cycles.

The present finding is a complete finite answer for the circular order-five family and the multiplicity of its extremizers, not a claimed resolution of the general de Bruijn attractor problem.

## Limitations

The upper bound is established by an exhaustive finite certificate for order five only. No explicit simple formula for the optimal-attractor count of an arbitrary higher-order de Bruijn cycle is proved. The verification program is standard-library deterministic but has not undergone independent external audit. Possible earlier equivalent tables using different vocabulary remain a scientific priority risk.

## References

- M. Banbara, H. Bannai, P. Guo, D. Köppl, T. Mieno, Y. Okamoto, *The Smallest String Attractors of Fibonacci and Period-Doubling Words*, arXiv:2602.16152 (initial posting 2026-02-18); also CPM 2026, LIPIcs 37, article 33.
- S. Mantaci, A. Restivo, G. Romana, G. Rosone, M. Sciortino, *A Combinatorial View on String Attractors*, Theoretical Computer Science 850 (2021), 236–248, doi:10.1016/j.tcs.2020.11.006, Section 6.2, Proposition 41.
- G. Romana, *Algorithmic View on Circular String Attractors*, ICTCS 2023, pp. 169–180, full proceedings PDF at https://ictcs2023.unipa.it/wp-content/uploads/2023/08/ICTCS2023_PAPER_9885.pdf.
- P. Whittington, *Online String Attractors*, arXiv:2407.15599 (2024), Section 5, Theorem 5.22 and ensuing open questions.
