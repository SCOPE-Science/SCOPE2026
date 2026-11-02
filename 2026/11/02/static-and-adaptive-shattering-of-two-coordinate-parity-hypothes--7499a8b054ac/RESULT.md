# Static and adaptive shattering of two-coordinate parity hypotheses

## Finding
For each integer \(n\ge2\), let \(\mathcal P_n\) be the concept class on \(\mathbb F_2^n\) consisting of exactly the \(\binom n2\) functions \(f_{ij}(x)=x_i+x_j\pmod2\), one for each unordered distinct pair of coordinate indices. The exact dimensions for \(2\le n\le11\) are:

| \(n\) | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| \(\operatorname{VCdim}(\mathcal P_n)\) | 0 | 1 | 2 | 2 | 3 | 4 | 4 | 4 | 4 | 5 |
| \(\operatorname{Ldim}(\mathcal P_n)\) | 0 | 1 | 2 | 3 | 3 | 4 | 4 | 5 | 5 | 5 |

The **first adaptive-versus-static separation occurs at five coordinates**, and further separations occur at nine and ten. The family exhibits a striking reversal: its fixed-query shattering dimension remains four from seven through ten coordinates, whereas its adaptive dimension reaches five at nine coordinates.

For every \(n\ge2\) and \(d\ge1\), static shattering of \(d\) input vectors is equivalent to the existence of a subset \(A\subseteq\mathbb F_2^d\) with \(|A|\le n-1\) such that every nonzero vector is the sum of two **distinct** elements of \(A\). This is an all-order structural translation from VC shattering to additive two-bases; it does not assert an all-order numerical dimension formula.

## Assumptions and scope
The field is binary; hypotheses have support of cardinality **exactly two** (not at most two); the query domain consists of **all** binary input vectors. The output at a query is the binary parity of its two designated coordinates. Littlestone trees may adapt the next query to previous answers. VC supports use a fixed list of queries. The finding does not determine the dimensions beyond eleven coordinates.

## Proof
**Reduction to additive two-bases.** For \(d\) fixed queries \(x^{(1)},\ldots,x^{(d)}\), associate to coordinate \(i\) its \(d\)-bit signature \(v_i=(x^{(1)}_i,\ldots,x^{(d)}_i)\). The answer vector of hypothesis \(f_{ij}\) is \(v_i+v_j\). In order to realize the zero output vector, at least two coordinate signatures must agree. Let \(A\) be their distinct values: then \(|A|\le n-1\), and every nonzero vector must appear as the sum of two distinct members of \(A\). Conversely, if such a set \(A\) exists, assign its values to distinct coordinates, duplicate one member to realize zero, and pad the remaining positions arbitrarily. Reading the bits in each position supplies the \(d\) shattering queries. This proves the claimed equivalence with the indicated quantifiers.

**Static lower bounds.** For dimensions \(d=1,2,3,4,5\), valid two-bases are respectively the integer-encoded binary vectors

\[\begin{aligned}
A_1&=\{0,1\},\\
A_2&=\{0,1,2\},\\
A_3&=\{0,1,2,4,7\},\\
A_4&=\{0,1,2,4,8,15\},\\
A_5&=\{0,21,9,24,23,7,25,29,30,14\}.
\end{aligned}\]

For each displayed \(A_d\), the set of XORs of two distinct elements is exactly \(\mathbb F_2^d\setminus\{0\}\), as checked by the included independent verifier. Including one duplicate gives realizing classes on \(3,4,6,7,11\) coordinates. Monotonicity under adding coordinates gives all intermediate lower bounds.

**Static upper bounds.** The number of concepts is \(\binom n2\). More sharply, if \(d\ge1\) queries are shattered then the zero signature forces a repeated coordinate signature and hence
\[
2^d\le 1+\binom{n-1}{2}.
\]
This excludes dimension three at \(n=5\) and dimension five at \(n=9\), and the cardinality bound excludes the other entries except the potential dimension-five case at \(n=10\). For the latter, a five-query shattering support would produce a nine-element additive two-basis in \(\mathbb F_2^5\): if there are fewer than nine different signatures, they cover at most \(\binom82=28\) of the \(31\) nonzero patterns. Translating one chosen signature to zero, every nine-element candidate is \(\{0\}\) plus an eight-subset of \(\{1,\ldots,31\}\). The included exhaustive enumerator tests all \(\binom{31}{8}=7,888,725\) candidates and finds none covering the \(31\) nonzero vectors. The source uses a complete combination generator and explicit XOR differences; the executable output is recorded in the package.

**Adaptive dimensions.** Distinct pair hypotheses give the universal cardinality upper bound
\[
\operatorname{Ldim}(\mathcal P_n)\le\lfloor\log_2\binom n2\rfloor.
\]
Complete depth-three, depth-four and depth-five binary shattering trees for \(n=5,7,9\) are embedded in `shattering_trees.json`. A node contains a nonzero cut mask specifying a query vector (first coordinate zero; other bits supplied by the mask); its two children are the observed responses. Every leaf provides a concrete distinct edge hypothesis that matches the entire path. `verify.py` checks all \(8+16+32=56\) root-to-leaf witnesses by direct parity evaluation, without trusting the tree generator. The three bounds are therefore attained. The dimensions for \(n=2,3,4\) follow from the static lower bounds together with cardinality; the remaining cases follow by monotonicity of the class in \(n\) and their cardinality upper bounds.

## Verification
Execute `python3 verify.py` in the artifact directory to check all tree certificates, additive-basis witnesses, and arithmetic thresholds. Separately compile `no_nine_basis.cpp` using `g++ -O3 -std=c++17 no_nine_basis.cpp -o no_nine_basis` and execute `./no_nine_basis` to reproduce the exhaustive five-dimensional impossibility check. The recorded outputs appear in `checks.txt`. All proof-critical certificates are included rather than referenced externally.

## Relationship to prior work
Guingona, Kolesnikov, Nierwinski and Soucy (2021) determine equal VC and Littlestone dimensions for the **full** family of nonzero linear-combination zero sets. Their theorem does not imply equality or these numerical dimensions for the strictly restricted family of two-coordinate binary parities. Ghazi, Golowich, Kumar and Manurangsi (2021) give general dimension bounds under Boolean aggregation; the exact small-order sequence and additive-basis obstruction are not consequences of their reported bounds. The equivalence with finite binary additive two-bases means that some static covering facts may have earlier appearances in additive combinatorics; no priority claim is made for established generic definitions or techniques. Related published claims were compared by mathematical implication rather than title alone.

## Limitations
This is an exact finite-range theorem, not an all-order formula. The nonexistence of a nine-element additive two-basis is backed by complete finite enumeration, not a conceptual impossibility proof. Historical-priority risk remains, particularly for additive difference bases and edge-identification query trees.

## References
1. V. Guingona, A. Kolesnikov, J. Nierwinski, R. Soucy, *Littlestone and VC-Dimension of Families of Zero Sets*, arXiv:2109.04805v1 (first posted 2021-09-10), especially Section 3 and Theorem 3.10, https://arxiv.org/abs/2109.04805.
2. B. Ghazi, N. Golowich, R. Kumar, P. Manurangsi, *Near-tight Closure Bounds for the Littlestone and Threshold Dimensions*, Proceedings of Machine Learning Research 132 (2021), 686–696, Proposition 3, https://proceedings.mlr.press/v132/ghazi21a.html.
