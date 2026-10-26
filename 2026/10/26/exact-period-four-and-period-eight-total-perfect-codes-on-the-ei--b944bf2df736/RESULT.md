# Exact period-four and period-eight total perfect codes on the eight-row torus

## Finding
For every integer \(t\ge 3\), let \(T_t=C_8\square C_t\) be the Cartesian product of simple cycles, with distinguished coordinates \((i,j)\in\mathbb Z_8\times\mathbb Z_t\). An *efficient open dominating set* (also called a *total perfect code*) is a vertex set \(D\) such that every vertex has exactly one neighbor in \(D\). Let \(N(t)\) be the number of such sets on the fixed, coordinate-labeled graph. Then
\[
N(t)=\begin{cases}
144,&8\mid t,\\
16,&4\mid t\text{ and }8\nmid t,\\
0,&4\nmid t.
\end{cases}
\]
Every code is periodic under translation along the \(C_t\)-direction, with *least* period exactly \(4\) or \(8\): there are exactly \(16\) four-periodic patterns and \(128\) eight-periodic patterns on every \(T_t\) with \(8\mid t\). In particular, \(C_8\square C_t\) admits an efficient open dominating set if and only if \(4\mid t\). This settles the circumference-eight case of the toroidal-existence conjecture stated by Kuziak, Peterin and Yero (2014), without settling other circumferences.

## Assumptions and scope
All graphs are finite, simple, undirected and vertex-labeled by their specified residues. The cycle \(C_t\) has \(t\ge3\) vertices, so each vertex of \(T_t\) has four distinct neighbors. Translations of a code count as different subsets unless the actual subsets coincide. A code has exactly \(2t\) vertices by summing the exact-one-neighbor constraint over all \(8t\) vertices; its selected induced subgraph is a matching, but no matching or parallelism restriction is assumed.

## Proof
Write \(b_j\in\{0,1\}^8\) for the binary membership vector in column \(j\in\mathbb Z_t\), with bit \(i\) equal to one exactly when \((i,j)\in D\). The efficient-open-domination condition at \((i,j)\) is precisely
\[
(b_{j-1})_i+(b_{j+1})_i+(b_j)_{i-1}+(b_j)_{i+1}=1,
\]
where the bit indices are modulo eight. Given \(a=b_{j-1}\) and \(b=b_j\), this uniquely determines \(c=b_{j+1}\) by
\[
c_i=1-a_i-b_{i-1}-b_{i+1}.
\]
Thus a successor \((a,b)\mapsto(b,c)\) exists exactly when each of these eight integers is zero or one. This is an *exact deterministic partial map* on \(2^{16}=65{,}536\) possible ordered pairs of eight-bit vectors. A code on the torus with \(t\) columns is in bijection with a state fixed by the \(t\)-fold partial iterate: the initial state uniquely fixes all columns, and closing it after \(t\) steps supplies precisely the required cyclic boundary equations.

For a reproducible, finite exhaustive certificate, encode an eight-bit column as an integer from \(0\) to \(255\), the state \((a,b)\) as \(256a+b\), and let \(L\) and \(R\) be the two cyclic one-bit rotations of \(b\). A successor exists if and only if \(a,L,R\) are pairwise disjoint bitmasks; then \(c=255\mathbin{\mathrm{xor}}(a\mathbin{\mathrm{or}}L\mathbin{\mathrm{or}}R)\). The complete enumeration in `verify_transfer.py` checks all \(65{,}536\) states, constructs all defined successors (exactly \(1{,}156\)), and follows every deterministic component to termination or a directed cycle. It finds exactly twenty directed cycles: four of length four and sixteen of length eight. The least decimal state of each directed cycle is listed below, providing a short checkable cycle fingerprint:

| Cycle length | Minimum encoded state on each cycle |
|---|---|
| \(4\) | `51, 102, 4369, 8738` |
| \(8\) | `281, 305, 332, 356, 562, 610, 664, 712, 792, 816, 864, 1632, 2337, 2376, 3105, 6210` |

The complete finite check is more than sampling: the program visits every possible state and proves that no other directed cycle exists. Because the map is deterministic, any valid toroidal code must lie on one of these directed cycles. For any \(t\ge3\), the fixed states of the \(t\)-fold iterate are exactly the states lying on cycles whose lengths divide \(t\). Each cycle of length \(\ell\) contributes \(\ell\) different initial states and hence \(\ell\) different labeled codes. Therefore
\[
N(t)=4\cdot4\,\mathbf1_{4\mid t}+16\cdot8\,\mathbf1_{8\mid t},
\]
which is the formula asserted above. The least-period assertion follows from the same cycle classification. A four-periodic code exists (four length-four cycles), so the existence equivalence follows.

## Verification
`verify_transfer.py` is a standalone Python 3 exact-integer verifier. Run `python3 verify_transfer.py`: the last line is `VERIFY_OK`, with state/transition counts, the twenty canonical cycle minima and period-specific totals. It uses no symbolic mathematics system or external libraries. Independent `verify_exact_cover.py` constructs the open neighborhood of each vertex directly, recursively searches exact partitions of the toroidal vertex set, and counts codes for \(t=3,4,5,6,8,12\) as \(0,16,0,0,144,16\), respectively. These checks do not use the column recurrence. Outputs from actual executions are supplied as `transfer_output.txt` and `exact_cover_output.txt`. The infinite-family proof uses the finite *complete* state classification and the bijection, not extrapolation from the six independent test sizes.

## Relationship to prior work
Dejter's *Perfect domination in regular grid graphs* (first publicly submitted 2007-11-27; 2008 journal publication) characterizes the existence of **parallel** total perfect codes on products of cycles, giving existence when both cycle lengths are multiples of four. It does not, as described in the accessible source abstracts and subsequently in the 2014 and 2016 primary treatments, rule out nonparallel codes at other sizes or count all labeled codes for circumference eight.

Kuziak, Peterin and Yero, *Efficient open domination in graph products* (2014), Section 5.1, Conjecture 5.3, posit that \(C_r\square C_t\) has an efficient open dominating set exactly when both lengths are divisible by four. They verify the existence criterion for first factor \(r\in\{3,4,5,6,7\}\), but not \(r=8\). Kraner Šumenjak, Peterin, Rall and Tepeh (first arXiv version 2015-08-17; journal 2016), Section 2, restate this conjecture and the prior restricted conclusions. Their graph-product characterizations concern different second factors and do not imply the present exact circumference-eight census. The formula here settles the next fixed-width instance and adds an exact least-period classification and labeled count.

## Limitations
This does not settle the existence conjecture for all \(r\). Exact census and least periods are proved only for the fixed factor \(C_8\) and arbitrary \(t\ge3\). The 2007/2008 source's full text was not accessible during the present literature comparison despite open-access attempts; its abstract and its description by the two subsequently inspected papers were compared. An independently unindexed or later equivalent classification remains possible. The exhaustive certificate is finite, transparent and reproducible, but is not an independent external audit.

## References
1. I. J. Dejter, *Perfect domination in regular grid graphs*, arXiv:0711.4343, initial public submission 2007-11-27; *Australasian Journal of Combinatorics* **42** (2008), 99–114. https://arxiv.org/abs/0711.4343
2. D. Kuziak, I. Peterin and I. G. Yero, *Efficient open domination in graph products*, *Discrete Mathematics & Theoretical Computer Science* **16** (2014), 105–120, especially Conjecture 5.3 and Theorem 5.5. https://doi.org/10.46298/dmtcs.1267
3. T. Kraner Šumenjak, I. Peterin, D. F. Rall and A. Tepeh, *Partitioning the vertex set of G to make G square H an efficient open domination graph*, arXiv:1508.04029, first public submission 2015-08-17; *DMTCS* **18** (2016), article 1503. https://arxiv.org/abs/1508.04029
