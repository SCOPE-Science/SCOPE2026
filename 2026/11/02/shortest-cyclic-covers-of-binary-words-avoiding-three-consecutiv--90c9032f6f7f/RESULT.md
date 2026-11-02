# Shortest cyclic covers of binary words avoiding three consecutive zeros through order sixteen

## Finding

For every integer \(3\le n\le16\), define \(\mathcal L_n\) to be the set of *ordinary linear* length-\(n\) binary words having no consecutive factor \(000\). Define \(U_n\) as the minimum length of a nonempty binary circular word such that every member of \(\mathcal L_n\) is present as a cyclic length-\(n\) window. Additional windows and repeated windows are permitted. The exact values are:

| \(n\) | \(|\mathcal L_n|\) | Additional windows | \(U_n\) |
|---:|---:|---:|---:|
| 3 | 7 | 0 | 7 |
| 4 | 13 | 1 | 14 |
| 5 | 24 | 4 | 28 |
| 6 | 44 | 9 | 53 |
| 7 | 81 | 21 | 102 |
| 8 | 149 | 45 | 194 |
| 9 | 274 | 93 | 367 |
| 10 | 504 | 188 | 692 |
| 11 | 927 | 373 | 1300 |
| 12 | 1705 | 730 | 2435 |
| 13 | 3136 | 1414 | 4550 |
| 14 | 5768 | 2716 | 8484 |
| 15 | 10609 | 5182 | 15791 |
| 16 | 19513 | 9833 | 29346 |

Moreover, for every order in this table an optimal circular covering word exists that also avoids \(000\) cyclically. This last property is a construction-existence statement, not a classification of all optimal covers.

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\). Windows are indexed and overlap in the usual de Bruijn manner; rotation does not change whether a circular word is a cover. The forbidden triple concerns the *linear target factors*: for example a target may begin and end in zeros even if wrapping that target around itself would introduce \(000\). We do **not** restrict the competitors to avoid \(000\); allowing forbidden windows makes the lower bound stronger. Circular words of length smaller than \(n\) are understood periodically and are subject to the same covering definition. Only \(3\le n\le16\) is asserted.

## Proof

**1. Translate a cover into a circulation.** Fix an order \(n\) from the table. Use the full binary de Bruijn directed graph with vertices \(V=\{0,1\}^{n-1}\). Every length-\(n\) word \(e=e_0\cdots e_{n-1}\) is the arc from its first \(n-1\) bits to its last \(n-1\) bits. Its incidence multiplicity in an arbitrary circular covering word is \(c_e\). Put \(a_e=1\) when \(e\in\mathcal L_n\), otherwise \(a_e=0\), and \(x_e=c_e-a_e\). By coverage, \(x_e\ge0\). Conservation of the closed walk says, for every vertex \(v\),

\[
\sum_{e:\operatorname{tail}(e)=v}x_e-\sum_{e:\operatorname{head}(e)=v}x_e
=\operatorname{indeg}_a(v)-\operatorname{outdeg}_a(v).
\]

The total number of additional windows is \(\sum_e x_e\), so the covering length is \(|\mathcal L_n|+\sum_e x_e\). This reduction also applies to covers that traverse forbidden edges.

**2. A universal dual bound.** Assign integer potentials \(p_v\) to all \(2^{n-1}\) graph vertices, satisfying

\[
p_{\operatorname{head}(e)}-p_{\operatorname{tail}(e)}\le1
\quad\text{for every arc }e\in\{0,1\}^n.
\]

Multiplication by the nonnegative \(x_e\), summation over all arcs, and flow conservation yield

\[
\sum_e x_e\ge
\sum_{v\in V}p_v\bigl(\operatorname{outdeg}_a(v)-\operatorname{indeg}_a(v)\bigr).
\]

Notice that these potential inequalities are imposed on the **full** graph, including all forbidden arcs: this certifies optimality against unrestricted coverings rather than merely against coverings avoiding the forbidden triple.

**3. Exact matching lower and upper certificates.** The embedded file `CERT.json` supplies, for each \(n=3,\ldots,16\), an integer augmentation vector \((x_e)_e\), integer vertex potentials \((p_v)_v\), and a binary circular witness. The independent reader `verify.py` regenerates every required edge indicator \(a_e\), checks that all augmentations are nonnegative, checks every balance equation, checks every full-graph potential inequality, and checks that the dual sum equals \(\sum_e x_e\). The common values, from order three to sixteen, are

\[
(0,1,4,9,21,45,93,188,373,730,1414,2716,5182,9833).
\]

The same verifier checks the complete indexed cyclic length-\(n\) window multiset of each supplied witness, requiring it to be *exactly* \((a_e+x_e)_e\). It also checks \(x_e=0\) for every forbidden arc. Thus each witness achieves the certified lower bound while avoiding \(000\) cyclically.

**4. Existence from the graph structure.** Independently of the stored witnesses, the required-edge graph is strongly connected on its used vertices. Any admissible vertex can reach the all-ones vertex by appending ones; the all-ones vertex reaches any admissible vertex by appending the vertex's bits, and the intervening windows remain free of \(000\). The nonnegative augmentations of step 3 preserve this support and balance every vertex. Therefore the resulting directed multigraph has an Eulerian circuit, whose edge labels form the claimed circular cover. For orders three and four, `verify.py` additionally brute-force checks all shorter indexed circular binary words; this is a cross-check and is not substituted for the all-order dual proofs.

**5. Why extra windows are necessary.** At every \(n\ge4\), there are admissible vertices whose first two bits are \(00\) but whose last two are not, and vice versa. Their required in-degrees and out-degrees differ, so a circular word using every target exactly once is impossible. The computed values quantify the smallest necessary repetitions, with no forbidden windows required in an optimum through order sixteen.

## Verification

Place `CERT.json` and `verify.py` in the same directory and run:

```text
python3 verify.py
```

The verifier uses only the Python standard library and prints `VERIFY_OK` after all fourteen rational-free integer certificates, cyclic witness multisets, and small-case brute-force tests pass. The certificate uses zlib-compressed base64 vectors: unsigned one-byte augmentation multiplicities indexed by the binary value of each length-\(n\) arc, and signed little-endian two-byte vertex potentials indexed by the binary value of each length-\(n-1\) vertex. The binary witness string is stored explicitly for every order. All decoding details are implemented in `verify.py`; no optimization solver or remote files are required to replay the proof.

## Relationship to prior work

Burstein and Kitaev (2003) study unavoidable sets of word *patterns* and construct universal cycles of patterns by Hamiltonian overlap graphs; this is not an exact minimum-length covering of literal \(000\)-avoiding words. Moreno and Matamala (2004; arXiv version 2007) study lexicographically minimal de Bruijn sequences in restricted *periodic* languages, with each allowable factor appearing once. Their adjective “minimal” concerns lexicographic order, not the shortest cover permitted to repeat windows. Chee and collaborators (2024) maximize the number of distinct windows in run-length-limited walks, whereas the present task requires every *linearly* admissible window and minimizes length while permitting repeats. In particular, the ordinary linear target set is larger than the necklace-closed, cyclically admissible set; an exact-once cycle for the latter does not supply the values in the table.

## Limitations

The exact profile stops at order sixteen. No closed expression for all orders, classification of all optimal covers, or analogous result for other forbidden patterns is claimed. The stored potentials and witnesses are finite exact certificates, not extrapolations or asymptotic theorems. Prior-art searches reduce but do not eliminate the possibility of unindexed exact tables or an older equivalent theorem. No external independent review is claimed.

## References

1. A. Burstein and S. Kitaev, *On Unavoidable Sets of Word Patterns*, arXiv:math/0311399v1, first posted 2003-11-23. https://arxiv.org/abs/math/0311399
2. E. Moreno and M. Matamala, *Minimal de Bruijn Sequence in a Language with Forbidden Substrings*, WG 2004, pp. 168–176; public arXiv version posted 2007-11-12. https://arxiv.org/abs/0711.1695
3. Y. M. Chee, T. Etzion, T. L. Nguyen, D. H. Ta, V. D. Tran and V. K. Vu, *Maximum Length RLL Sequences in de Bruijn Graph*, arXiv:2403.01454. https://arxiv.org/abs/2403.01454
