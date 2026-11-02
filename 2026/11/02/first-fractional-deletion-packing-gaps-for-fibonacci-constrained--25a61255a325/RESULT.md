# First fractional deletion-packing gaps for Fibonacci-constrained binary words

## Finding

Let \(\mathcal S_n\) be the binary words of length \(n\) without the factor \(11\). For \(x\in\mathcal S_n\), let \(\Delta(x)\) be its set of distinct words obtained by deleting exactly one coordinate. Define \(A_n\) as the greatest size of a subset \(C\subseteq\mathcal S_n\) for which \(\Delta(x)\cap\Delta(x')=\varnothing\) whenever \(x\neq x'\) belong to \(C\). Define \(F_n\) as the optimal value of the fractional deletion-shadow packing program
\[
\max\sum_{x\in\mathcal S_n}p_x\quad\text{subject to}\quad p_x\ge0,\qquad\sum_{x:\,y\in\Delta(x)}p_x\le1\ \text{for every }y\in\bigcup_{x\in\mathcal S_n}\Delta(x).
\]

**Theorem.** In order of lengths \(n=1,2,\ldots,7\),
\[
(A_n)=(1,1,2,2,3,3,5),\qquad (F_n)=(1,1,2,2,3,4,6).
\]
In particular, \(n=6\) is the first fractional-integral separation for this natural constrained deletion channel. The gap persists at \(n=7\), with \(F_6/A_6=4/3\) and \(F_7/A_7=6/5\).

## Assumptions and scope

Positions are indexed, words are not identified under rotation or reversal, and a deletion may remove either binary symbol at any position, including an endpoint. Only the transmitted input must avoid adjacent ones; a received word need not obey the constraint. No restriction is imposed on leading or trailing bits. The length range is precisely \(1\le n\le7\). The empty word is the sole deletion output at length one.

## Proof

The number of possible input words is \(|\mathcal S_n|=F_{n+2}^{\mathrm{Fib}}\), where \(F_j^{\mathrm{Fib}}\) denotes the standard Fibonacci number (this notation is distinct from the packing optimum \(F_n\)). For each input word, form its distinct one-coordinate deletion outputs. Pairwise shadow disjointness is equivalent to single-deletion correction, and the displayed fractional program is its natural set-packing relaxation.

The supplied `artifacts/certificates.json` contains complete certificates for every length. For \(1\le n\le5\), each case contains a code of \(A_n\) words with disjoint shadows and a set of exactly \(A_n\) length-\(n-1\) outputs meeting the deletion shadow of **every** eligible input. Such an output transversal proves \(F_n\le A_n\), while the exhibited code gives \(A_n\le F_n\) and the reverse inequality for the integer optimum.

At \(n=6\), an eligible three-word code is
\[
\{\mathtt{000000},\mathtt{000101},\mathtt{010100}\}.
\]
The certificate gives nonnegative rational primal shadow-packing weights and dual output-cover weights, both of total weight \(4\), proving \(F_6=4\). To sharpen the integral bound, it also lists ten nonempty *conflict cliques* of input words, each pair of which shares a possible deletion output, with nonnegative weights in integer quarter-units. The weights sum to \(15/4\), and every eligible input belongs to cliques with total weight at least \(1\). Any deletion-correcting code contains at most one member of each conflict clique. Hence its cardinality is at most \(15/4<4\), proving \(A_6\le3\). The displayed code gives equality.

At \(n=7\), a five-word code is
\[
\{\mathtt{0000000},\mathtt{0000101},\mathtt{0010100},\mathtt{1010000},\mathtt{1010101}\}.
\]
The rational primal and dual shadow-packing certificates both have total weight \(6\). Fourteen weighted conflict cliques have total weight \(23/4\), and cover each eligible input to total weight at least \(1\). The same clique argument gives \(A_7\le\lfloor23/4\rfloor=5\), matching the exhibited code. Thus \(F_7=6\) and \(A_7=5\). These exact finite arguments prove the entire claimed profile and the first-separation assertion.

Here a conflict clique is not required to be the collection of parents of one fixed output: it is only required that every pair of distinct words in the clique have intersecting deletion shadows. Therefore the additional weighted-clique inequalities are valid for *integral* codes even though they are not among the original fractional program's individual-output constraints.

## Verification

Extract all embedded files without modifying their bytes. Run `python3 artifacts/verify.py artifacts/certificates.json`. The standard-library checker reconstructs every admissible input and deletion shadow, checks all explicit codewords, all exact rational packing and covering inequalities, the pairwise conflicts in each weighted clique, the total weights, and the required coverage of each input. Expected terminal marker: `VERIFY_OK`. Run `python3 artifacts/census.py` for a separate exact maximum-independent-set computation on the complete finite conflict graphs; expected terminal marker: `CENSUS_OK`.

The first checker proves both upper and lower bounds directly from short finite certificates, without relying on optimization logs or floating-point tolerances. The second checker is a supplementary reconstruction, not a substitute for the proof certificates.

## Relationship to prior work

Kulkarni and Kiyavash's November 2012 preprint introduced hypergraph fractional-transversal bounds for deletion codes and treated run-length-limited constrained sources in Section V. Their specialized formulation imposes starting and ending zero-runs and a different interior zero-gap condition; their general constrained-source theorem applies to this language, but its direct run-count transversal gives bounds \(121/15\) and \(73/6\) at lengths six and seven, far above the exact integer and fractional values here. Their numerical table covers the **unrestricted** input language, not these constrained optima.

Cullina, Kulkarni and Kiyavash (November 2012) studied general deletion-confusability graphs, constant-weight restrictions, and optimal colorings. Those results do not state or imply the complete constrained-source integer/fractional profiles above. Earlier run-length-limited deletion-code works by Bours, Cheng and collaborators, and Palunčić and collaborators address constructions or general bounds; the available descriptions do not establish the finite packing separations here, but some full texts were not inspected. Independent historical-priority review remains outstanding.

## Limitations

This theorem establishes only the stated seven-length initial profiles, not an asymptotic formula or a gap for every greater length. The numerical values are exact for the specific linear binary language avoiding `11`; different endpoint conventions, maximum-zero-run constraints, cyclic equivalence, and channels deleting only a specific symbol are different problems. Literature inspection reduces but does not eliminate historical-priority risk; no independent scientific audit has been performed.

## References

1. A. A. Kulkarni and N. Kiyavash, *Non-asymptotic Upper Bounds for Deletion Correcting Codes*, first arXiv posting 2012-11-13, https://arxiv.org/abs/1211.3128 . Relevant primary full text: Sections V, V-A and VI at https://ar5iv.labs.arxiv.org/html/1211.3128 .
2. D. Cullina, A. A. Kulkarni and N. Kiyavash, *Two Approaches to the Construction of Deletion Correcting Codes: Weight Partitioning and Optimal Colorings*, first arXiv posting 2012-11-16, https://arxiv.org/abs/1211.4056 . Relevant primary full text: Sections II-IV at https://ar5iv.labs.arxiv.org/html/1211.4056 .
3. P. A. H. Bours, *Construction of fixed-length insertion/deletion correcting runlength-limited codes*, IEEE Transactions on Information Theory 40 (1994), 1841-1856, https://doi.org/10.1109/18.340459 . Abstract examined; full text not examined.
4. L. Cheng, H. C. Ferreira and I. Broere, *Moment Balancing Templates for (d,k)-Constrained Codes and Run-Length Limited Sequences*, IEEE Transactions on Information Theory 58 (2012), 2244-2252, https://doi.org/10.1109/TIT.2011.2178089 . Abstract examined; full text not examined.
5. F. Palunčić, K. A. S. Abdel-Ghaffar, H. C. Ferreira and W. A. Clarke, *A Multiple Insertion/Deletion Correcting Code for Run-Length Limited Sequences*, IEEE Transactions on Information Theory 58 (2012), 1809-1824, https://doi.org/10.1109/TIT.2011.2172725 . Abstract examined; full text not examined.
