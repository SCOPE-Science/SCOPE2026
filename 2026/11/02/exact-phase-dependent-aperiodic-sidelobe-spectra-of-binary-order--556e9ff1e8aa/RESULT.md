# Exact phase-dependent aperiodic sidelobe spectra of binary order-five de Bruijn cycles

## Finding
Let \(\mathcal B_5\) consist of the \(2,048\) binary de Bruijn cycles of order five, counted modulo cyclic rotation. Each is a cyclic word of length \(32\) in which every binary five-letter word occurs exactly once. For \(W\in\mathcal B_5\) and an indexed cut \(j\in\{0,\ldots,31\}\), write \(w^{(j)}=w_jw_{j+1}\cdots w_{j+31}\), taking circular indices. Put \(a_i=(-1)^{w_i^{(j)}}\) and define the **aperiodic** autocorrelation and peak sidelobe level by
\[
A_{W,j}(t)=\sum_{i=0}^{31-t}a_i a_{i+t}\quad(1\le t\le31),\qquad
P(W,j)=\max_{1\le t\le31}|A_{W,j}(t)|.
\]

The complete distribution of \(P(W,j)\) over the \(65,536=2,048\cdot32\) cycle-cut pairs is as follows. Unlisted levels have count zero.

| \(P(W,j)\) | Number of cuts |
|---:|---:|
|4|40|
|5|972|
|6|3,612|
|7|10,338|
|8|12,284|
|9|12,582|
|10|6,264|
|11|8,240|
|12|2,590|
|13|3,840|
|14|776|
|15|1,756|
|16|470|
|17|1,004|
|18|216|
|19|392|
|20|80|
|21|80|
|**Total**|**65,536**|

Define the best achievable sidelobe after choosing a cut, \(Q(W)=\min_{0\le j<32}P(W,j)\). Its complete distribution across cycles is

| \(Q(W)\) | Number of cycles |
|---:|---:|
|4|32|
|5|344|
|6|476|
|7|666|
|8|236|
|9|174|
|10|20|
|11|8|
|12|20|
|15|64|
|16|8|
|**Total**|**2,048**|

Thus the smallest possible rooted aperiodic peak sidelobe level is \(4\), attained at exactly \(40\) cuts of \(32\) cycles. Exactly \(24\) of those cycles possess one cut attaining \(4\), and the other \(8\) possess two. In contrast, exactly \(8\) cycles have optimum \(Q(W)=16\). No cycle optimum equals \(13\) or \(14\).

## Assumptions and scope
A de Bruijn cycle is considered up to rotation but *not* up to complementation or reversal. A cut is indexed, so each cycle contributes \(32\) rooted linear strings. The correlation sums are **non-wrapping**: only \(32-t\) pairs contribute at shift \(t\). The signs are \(+1\) for the bit zero and \(-1\) for the bit one. These normalizations matter: the periodic autocorrelation includes an additional wrap-around term and is rotation invariant, whereas \(P(W,j)\) generally depends on the cut. The theorem is an exact finite classification for binary order five; no higher-order statement is asserted.

## Proof
**Exhaustive parametrization.** Regard the \(32\) binary five-letter words as states indexed by integers \(0,\ldots,31\). A successor of state \(x\) has the form \(2(x\bmod16)+b\) for some \(b\in\{0,1\}\). In any de Bruijn cycle, the two states \(u\) and \(16+u\), which have the same trailing four bits \(u\), must have different appended bits; otherwise both would have the same successor and the cyclic list of states could not be a single permutation. Consequently every possible successor permutation of this form is uniquely specified by a Boolean table \(f:\{0,\ldots,15\}\to\{0,1\}\), through
\[
S_f(x)=2(x\bmod16)+\bigl((x\mathbin{\mathrm{div}}16)\mathbin{\mathrm{xor}} f(x\bmod16)\bigr).
\]
There are exactly \(2^{16}=65,536\) such tables. A table produces a de Bruijn cycle if and only if the orbit of state \(0\) under \(S_f\) visits all \(32\) states before returning to \(0\). For a successful table, the leading bit of each visited state records the corresponding bit of the uniquely rooted cycle beginning at the sole occurrence of five zeros. Conversely every de Bruijn cycle determines exactly this table. Therefore testing all \(65,536\) tables, without any early truncation, is a complete and nonredundant search.

**Independent exhaustion.** The directed order-four binary de Bruijn graph has \(16\) vertices and \(32\) labeled edges. An Euler tour starting at vertex \(0000\) with first edge \(00000\), using each edge once and returning to the initial vertex, corresponds bijectively to a de Bruijn cycle rooted at its unique \(00000\) factor. The attached checker enumerates all such tours by depth-first branching on *both* unused outgoing edges. Its output set equals the set of successful Boolean-table cycles and has size \(2,048\). The two generation methods are independent implementations of the same mathematically complete family.

**Exact correlations.** For each generated cycle, inspect all \(32\) cuts and all \(31\) positive lags. One implementation computes \(A_{W,j}(t)\) directly by multiplying bipolar signs. An independent implementation counts mismatched bit pairs \(D_{W,j}(t)\) in the two length-\(32-t\) overlapping segments and uses the identity
\[
A_{W,j}(t)=(32-t)-2D_{W,j}(t).
\]
This identity follows since each matched pair contributes \(+1\) and each mismatched pair contributes \(-1\). The two implementations agree for every cut and lag-level maximum. Exact integer counters then give the two stated tables and the counts of optimal cuts per cycle. All loops are finite, their ranges are explicit in the attached Python file, and no probabilistic sampling or numerical tolerance is involved.

For a concrete example of the role of the root, the cycle rooted at five zeros with bits `00000111110111001101010010001011` has \(P(W,0)=6\), but \(P(W,1)=4\) and \(P(W,26)=4\). Its cyclic periodic correlation is of course identical at all three roots, demonstrating why periodic summaries do not determine the phase-dependent statement.

## Verification
Run `python3 verify_psl.py` with Python 3.10 or newer (standard library only). It requires no inputs and prints both distributions. The checker constructs all \(65,536\) successor tables and all Euler tours independently; both methods return the same \(2,048\) rooted cycles. It tests the bipolar-product and mismatch-count correlation implementations on every one of the \(65,536\) cycle-cut pairs. The expected histograms, the \(65,536\) and \(2,048\) totals, and the independent set comparison are all asserted. The checker was executed successfully in the packaged form.

## Relationship to prior work
Spinsante, Andrenacci, and Gambi (2011) examined all \(2,048\) order-five binary de Bruijn cycles as spreading codes and tabulated **periodic** autocorrelation sidelobe thresholds, notably the \(12\)-cycle and \(784\)-cycle subsets at periodic thresholds \(4\) and \(8\). Their system model also defines aperiodic correlation, but their order-five threshold table concerns the periodic correlation \(\theta_c(t)\), which is invariant under changing the root. The present claim instead classifies the non-wrapping maximum across all \(32\) cuts for every cycle, including its exact root-optimized distribution; the quoted periodic subsets do not imply these counts.

Fujisaki and Nabeshima (2011) studied **periodic** normalized autocorrelation extrema for de Bruijn sequences: their Definition 1 explicitly sums with indices taken modulo the period, and their Tables I and II classify periodic worst and second-worst extrema. Their full paper contains no rooted non-wrapping peak-sidelobe census. Dmitriev and Jedwab (2007) study general aperiodic peak-sidelobe behavior, especially binary maximum-length shift-register sequences, rather than this complete cycle-cut spectrum. The present result does not claim a new universal lower bound for all length-\(32\) binary strings.

## Limitations
This is an exact computationally exhaustive theorem only at binary order five. The proof's finite loops do not imply a formula for higher orders. Its originality assessment is based on the full accessible Spinsante–Andrenacci–Gambi and Fujisaki–Nabeshima primary articles and targeted searches, not a proof that no earlier table exists; unindexed historical work remains a priority risk. Independent mathematical audit has not been performed.

## References
- S. Spinsante, S. Andrenacci, and E. Gambi, *Binary De Bruijn sequences for DS-CDMA systems: analysis and results*, EURASIP J. Wireless Commun. Netw. 2011, article 4, first online 2011-06-06. https://doi.org/10.1186/1687-1499-2011-4
- H. Fujisaki and Y. Nabeshima, *On auto-correlation values of de Bruijn sequences*, NOLTA 2 (2011), 400–408, available online 2011-10-01. https://doi.org/10.1587/nolta.2.400
- D. Dmitriev and J. Jedwab, *Bounds on the growth rate of the peak sidelobe level of binary sequences*, Adv. Math. Commun. 1 (2007), 461–475. https://doi.org/10.3934/amc.2007.1.461
