# Review of Exact odd-sequence lengths for the Mersenne-power binary Collatz family

## Correctness
PASS. The source transformation was reconstructed from its definitions. On the invariant subring \(\mathbb F_2[y]\), with \(y=M_1\) and \(z=y+1=x(x+1)\), the two linear-factor valuations are equal to the \(z\)-valuation. The proof derives an exact factorization \(B_n=1+z^t y^qQ\), follows every one-factor step, computes the final higher-valuation step, and obtains \(B_n\mapsto B_{n+t}\) after exactly \(t\) steps. The index increases, cannot overshoot the next power of two, and has strictly increasing two-adic valuation at block boundaries, so the telescoping count is exact. The finalized exact verifier replays all starting indices through \(R=8\); that computation is corroboration, not the infinite proof.

## Originality
PASS. The motivating paper itself states the exact family-length assertion as Conjecture 3.1 and supplies only computations. Exact web searches for the conjecture wording, \(M_1^{2^R-j}+1\), and the \(j+1\) length found the source paper and summaries repeating it as a conjecture, not a proof. Related 2024--2025 polynomial-Collatz papers concern a different single-factor map or general eventual periodicity and do not imply the simultaneous \(x\)- and \(x+1\)-stripping formula here. published-finding corpus searches for the exact claim and aliases returned no equivalent or stronger finding; the closest hits concern unrelated characteristic-two dynamics or valuations. The current ledger contains no occurrence of the source identifier or Collatz terminology.

## Value
PASS. This resolves an explicit infinite-family conjecture in a recent number-theory paper, replacing a computational pattern by a structural transition law. The block formula is mathematically informative beyond the bare length: it explains why the index advances by exactly the number of odd steps and why the next-power-of-two distance is the invariant controlling termination. The result is therefore not a parameter substitution, finite table extension, or routine recomputation.

## Closest literature and limitations
The closest source is Gallardo--Rahavandrainy, arXiv:2510.07530v1 / DOI 10.33044/REVUMA.5555, which states the claim as Conjecture 3.1 and gives examples for \(9\le n\le16\). Alon--Behajaina--Paran (2024) and Behajaina--Paran (2025) study different polynomial Collatz maps or broader stopping/periodicity questions. The main residual originality risk is an unindexed independent proof posted after the checked sources. The theorem does not address the source's Conjectures 3.2 or 3.3.

Same-model review: passed. Independent audit: not yet performed.
