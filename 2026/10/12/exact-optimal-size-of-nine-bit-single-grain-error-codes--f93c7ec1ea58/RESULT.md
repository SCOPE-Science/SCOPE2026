# Exact optimal size of nine-bit single-grain-error codes

## Finding
For binary words of length \(9\) transmitted through a channel that may perform **zero or one** adjacent overwrite, replacing a symbol by its immediately preceding stored symbol, the maximum cardinality of a zero-error code is exactly
\[
M(9,1)=78.
\]
An explicit \(78\)-word code is supplied in `witness.txt`, together with `verify_witness.py`. The exact finite upper bound is established through the reproducible integer optimization in `solve_upper.py`.

## Assumptions and scope
A codeword \(b=(b_1,\ldots,b_9)\) is a binary vector. A received word equals \(b\), or equals \(b\) with exactly one coordinate \(i\in\{2,\ldots,9\}\) replaced by the **original** value \(b_{i-1}\). The first coordinate is never overwritten. This is the standard single-grain overwrite/error-ball model, with no restriction on the input distribution. Two inputs may belong to one code precisely when their sets of possible received words are disjoint. There is no claim about errors in two or more positions, errors of longer span, or a stochastic medium.

For a nine-bit word represented by an integer \(x\) with the first bit most significant, denote the bit at place \(2^i\) by \(\beta_i(x)\), with \(i\in\{0,\ldots,8\}\). Its possible-output set is exactly
\[
B(x)=\{x\}\cup\bigl\{x\mathbin{\mathrm{xor}}2^i: 0\le i\le7,\ \beta_i(x)\ne\beta_{i+1}(x)\bigr\}.
\]
For integer labels the xor symbol denotes bitwise exclusive-or; all words are padded to nine bits, including leading zeroes.

## Proof
**Symmetry reduction.** Every output preserves the first bit. The input space therefore decomposes into the independent first-bit-zero and first-bit-one channels. Complementing all nine bits is a bijection between them, preserving overwrite relations. Let \(\alpha\) be the maximum number of codewords in the first-bit-zero channel. Then \(M(9,1)=2\alpha\).

**Exact finite conflict graph.** The first-bit-zero channel has \(256\) possible inputs, represented by integers \(0,\ldots,255\). Associate to each input the output set \(B(x)\). Join two distinct inputs precisely when their output sets intersect. Direct set construction gives \(2816\) conflict edges. For every edge \(\{u,v\}\), introduce binary variables \(z_u,z_v\) and require \(z_u+z_v\le1\). Maximizing \(\sum_{u=0}^{255}z_u\) over these \(256\) binary variables and all \(2816\) constraints is *exactly* the graph independence number: every feasible integral assignment selects pairwise distinguishable codewords, and every distinguishable code determines such an assignment.

The complete optimization is implemented without pruning possible inputs or restricting code families in `solve_upper.py`. The SciPy/HiGHS mixed-integer solver terminated with global optimality status, integral primal objective \(39\), matching integer-program dual bound \(39\), and zero relative MIP gap. The actual minimization objective and its dual bound were both \(-39\) (up to floating-point report precision). Thus this exhaustive finite optimization establishes \(\alpha\le39\), subject to the numerical solver's correct execution. The script independently rebuilds and checks the complete constraint matrix, exact integral solution, and returned bound; no finite extrapolation is involved.

**Matching construction.** The \(39\) integers in `witness.txt` represent first-bit-zero codewords. Form a second set by complementing all nine bits: \(x\mapsto 511\mathbin{\mathrm{xor}}x\). The supplied independent `verify_witness.py` rebuilds possible received words using nine-component tuples and checks that no two of the resulting \(78\) codewords share a received word. Its exact integer check finds \(396\) distinct received words across those \(78\) disjoint output sets. Therefore \(\alpha\ge39\) and \(M(9,1)\ge78\). Combining both directions proves the stated value.

## Verification
Place `witness.txt`, `verify_witness.py` and `solve_upper.py` in the same directory. Run `python3 verify_witness.py`; only the Python standard library is needed, and it reports `WITNESS_OK` with \(78\) words. Run `python3 solve_upper.py` with Python, NumPy, and SciPy (SciPy at least version 1.11); it builds all \(256\) inputs and \(2816\) incompatible pairs and reports `UPPER_BOUND_OK` only if the mixed-integer solver returns a certified optimum of \(39\). Optimization runtime depends on the machine and solver version; the included script permits up to 240 seconds and reports an error rather than a spurious successful upper bound if optimization does not finish.

A separate formulation using packing constraints for each received word was also examined. It established a fractional relaxation value of approximately \(47.343\) for the first-bit-zero half but did **not** finish the corresponding integer optimization; it supplies no second proof of optimality. The proof of the numerical upper bound relies on the complete conflict-graph integer optimization, not this unfinished alternative.

## Relationship to prior work
Mazumdar, Barg, and Kashyap introduced the binary granular recording model in their 2010 preprint. Sharov and Roth analyzed the overlapping and nonoverlapping models, bounds, constructions, and several exact short-block cases. Kashyap and Zémor supplied improved upper bounds. Gabrys, Yaakobi, and Dolecek's full-length manuscript, Table II, explicitly records for length nine the previously reported bounds \(64\le M(9,1)\le112\); their table is not an exact determination. This finding closes that finite gap with \(M(9,1)=78\). The models agree for a single permitted grain error, so the same optimum applies to either single-error interpretation. None of those earlier authors' general bounds or constructions is claimed as new.

## Limitations
The statement concerns only binary length-nine words and at most one overwrite. Its upper bound is a complete but computer-assisted finite optimization, not a short symbolic upper-bound inequality or a separately machine-checked integer certificate. The check uses a recognized global mixed-integer optimizer; numerical or implementation defects remain a residual risk. Independent scientific audit has not been performed. Published literature is broad. In particular, Sharov and Roth's separate 2015 constructions paper discusses lengths up to 18, but the complete author-hosted PDF could not be obtained for a final theorem-level comparison; an earlier exact enumeration cannot be excluded. No claim is made about asymptotic code rates or larger lengths.

## References
1. A. Mazumdar, A. Barg and N. Kashyap, *Coding for High-Density Recording on a 1-D Granular Magnetic Medium*, arXiv:1012.1895 (initial public version 2010-12-08), https://arxiv.org/abs/1012.1895.
2. A. Sharov and R. M. Roth, *Bounds and Constructions for Granular Media Coding*, IEEE Transactions on Information Theory 60 (2014), 2010–2027, DOI:10.1109/TIT.2014.2301811.
3. N. Kashyap and G. Zémor, *Upper Bounds on the Size of Grain-Correcting Codes*, arXiv:1302.6154 (2013), https://arxiv.org/abs/1302.6154.
4. R. Gabrys, E. Yaakobi and L. Dolecek, *Correcting Grain-Errors in Magnetic Media*, arXiv:1307.7087 (initial public version 2013-07-26), https://arxiv.org/abs/1307.7087; IEEE Transactions on Information Theory 61 (2015), 2256–2272.
5. A. Sharov and R. M. Roth, *New Bounds and Constructions for Granular Media Coding*, IEEE Transactions on Information Theory 61 (2015), 4227–4238.
