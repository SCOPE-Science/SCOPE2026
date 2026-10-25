# Exact remanent word language of the pentagon: eighteen states and a rational census

## Finding

For the undirected five-cycle with independently oriented edges, label a traversal along an edge by \(0\) when it follows that edge's chosen \(0\)-direction and by \(1\) when traversed oppositely. All vertices are allowed as starts and endpoints. Let \(\mathcal R(C_5)\) consist of the finite binary words realizable by some walk **for every orientation** of the five-cycle.

**Theorem.** The minimal complete deterministic finite automaton recognizing \(\mathcal R(C_5)\) has exactly \(18\) states, including one rejecting sink. If \(a_m=|\mathcal R(C_5)\cap\{0,1\}^m|\) for every integer \(m\ge0\), then

\[
\sum_{m\ge0}a_m z^m
=\frac{(1+z)(1-z^2+z^7)}{(1-z)(1-3z^2+2z^4-z^7)}.
\]

The initial values are \(1,2,4,6,10,14,22,32,50,74,114,170,258,386,580,870,1300,1954\). The pentagon language is genuinely finer than the analogous triangle language: \(00100\) and \(11011\) are realized under every triangle orientation but are absent from \(\mathcal R(C_5)\).

## Assumptions and scope

The underlying graph is the simple undirected cycle with vertices \(\mathbb Z/5\mathbb Z\) and edges \(e_i=\{i,i+1\}\), indices taken modulo \(5\). An orientation is encoded by \(\omega\in\{0,1\}^5\). If \(\omega_i=b\), traversing edge \(e_i\) from \(i\) to \(i+1\) reads \(b\), while traversing it from \(i+1\) to \(i\) reads \(1-b\). Thus the two opposite directions of a given edge always bear complementary labels. Define \(L_\omega\) as the set of words readable by **at least one walk** in that labeled graph, with no prescribed starting or terminal vertex. Then \(\mathcal R(C_5)=\bigcap_{\omega\in\{0,1\}^5}L_\omega\), including the empty word. The theorem concerns this exact ordered-word and opposite-label convention; it makes no claim about other graph encodings.

## Proof

For each orientation \(\omega\), each subset \(S\) of the five vertices and each letter \(b\in\{0,1\}\), let \(T_{\omega,b}(S)\) be the set of endpoints of one \(b\)-labeled traversal beginning in \(S\). Set \(S_\omega(\varepsilon)=\mathbb Z/5\mathbb Z\) and \(S_\omega(wb)=T_{\omega,b}(S_\omega(w))\). Induction on word length gives

\[
w\in\mathcal R(C_5)\quad\Longleftrightarrow\quad
S_\omega(w)\ne\varnothing\ \text{for all}\ \omega\in\{0,1\}^5.
\]

Consequently, determinization of the product of all \(32\) oriented walk automata recognizes this **entire infinite language**, with an absorbing rejecting sink as soon as any orientation's reachable set becomes empty. An exact breadth-first closure calculation, completely reconstructed by `verify.py`, has \(23\) reachable nonsink tuples and one reachable sink. This is a finite exhaustive closure over transition subsets, not a sample of words.

Refine the initial accepting-versus-rejecting partition by the two successor blocks until stable (the Myhill–Nerode partition-refinement algorithm). The successive class counts are \(2,4,7,9,11,13,16,18\), after which refinement is unchanged. Every class has a reachable representative, and distinct final classes have distinguishing suffixes by the refinement theorem. The resulting complete **minimal** automaton has initial state \(0\), accepts every state except sink \(5\), and has the following two transitions per state (the columns are input \(0\) and input \(1\)):

| State | \(0\) | \(1\) | State | \(0\) | \(1\) |
|---:|---:|---:|---:|---:|---:|
| 0 | 1 | 2 | 9 | 11 | 5 |
| 1 | 3 | 2 | 10 | 12 | 4 |
| 2 | 1 | 4 | 11 | 3 | 13 |
| 3 | 5 | 6 | 12 | 14 | 10 |
| 4 | 7 | 5 | 13 | 11 | 15 |
| 5 | 5 | 5 | 14 | 5 | 16 |
| 6 | 8 | 4 | 15 | 17 | 5 |
| 7 | 3 | 9 | 16 | 14 | 4 |
| 8 | 5 | 10 | 17 | 3 | 15 |

For the length census, let \(M\) be the \(18\)-by-\(18\) integer transition-count matrix in the displayed table, let \(e_0\) be the initial-state basis vector and let \(f\) be the accepting-state indicator vector. Then \(a_m=e_0^{\mathsf T}M^m f\) and

\[
F(z)=e_0^{\mathsf T}(I-zM)^{-1}f.
\]

Write \(P(z)=(1+z)(1-z^2+z^7)\) and \(Q(z)=(1-z)(1-3z^2+2z^4-z^7)\). The denominator of \(F\) divides \(\det(I-zM)\), of degree at most \(18\), with constant coefficient \(1\); its adjugate numerator has degree at most \(17\). Therefore the numerator of \(QF-P\), put over \(\det(I-zM)\), has degree at most \(26\). Direct exact-integer multiplication of the displayed transition matrix verifies that the first \(27\) coefficients, for degrees \(0\) through \(26\), of \(QF-P\) vanish. The numerator must therefore be identically zero, proving the stated rational function for **every** length.

Finally, the same direct subset transitions for the three-cycle and five-cycle show that both \(00100\) and \(11011\) are accepted by all \(8\) triangle orientations but rejected by at least one of the \(32\) pentagon orientations (for example, mask \(5\) rejects \(00100\)). This establishes the explicit strict distinction.

## Verification

Run `python3 verify.py` in the directory containing the accompanying standalone Python script. It requires only the Python standard library and prints `VERIFY_OK`. The script constructs all \(32\) orientation transition functions from the original five edges, performs **complete reachable-product closure**, independently computes the accepting partition refinement and compares the exact \(18\)-state quotient to the table. It verifies the first \(27\) formal-series coefficients required by the degree-bound argument, and directly evaluates all \(8{,}191\) binary words of lengths \(0\) through \(12\) under each orientation for cross-checking. It also tests the triangle/pentagon separating words. The actual execution record is `verify_output.txt`.

## Relationship to prior work

Pujol's 2026 *Graph-based automata* introduces the orientation-intersection (remanent-language) viewpoint and reports that it contains chromatic information. This finding adopts that motivating perspective but establishes a specific **minimal DFA size, explicit quotient transition structure and complete length-enumerator rational function** for the five-cycle. Generic closure of regular languages under finite intersection ensures regularity but does not supply these exact invariants. The published abstract available during the comparison does not settle the five-cycle values; the paper's full text was not available for a conclusive comparison, so this is an acknowledged originality risk.

Earlier research on reversible finite automata and oriented-cycle homomorphism duality concerns related objects but does not, in the accessible descriptions, state the same pentagon orientation-intersection census.

## Limitations

The result concerns one concrete graph, not a classification of remanent languages of all odd cycles. Its exact symbolic encoding assigns complementary binary letters to opposite directions; alternative edge-label conventions define different languages. No new general automata-minimization algorithm is asserted. Existing, potentially unindexed formulations and the inaccessible complete motivating preprint could contain equivalent coverage. The calculations use exhaustive finite **automaton states**, which suffice for the infinite-language theorem; finite word enumeration by itself would not.

## References

1. Cyril Pujol, *Graph-based automata*, arXiv:2609.08843, first submitted 2026-09-08. https://arxiv.org/abs/2609.08843
2. Maria Radionova and Alexander Okhotin, *A hierarchy of reversible finite automata*, arXiv:2411.14538, first submitted 2024-11-21. https://arxiv.org/abs/2411.14538
3. Santiago Guzmán-Pro and César Hernández-Cruz, *Duality pairs and homomorphisms to oriented and unoriented cycles*, arXiv:2003.05605, first submitted 2020-03-12. https://arxiv.org/abs/2003.05605
