# The rational translation character of the scale-four six-cube Vietoris–Rips complex

## Finding

Let \(Q_6=(\mathbb F_2)^6\) be the Hamming six-cube. Write \(X=\operatorname{VR}_{\le4}(Q_6)\) for the inclusive scale-four Vietoris–Rips complex, and let the translation group \(T=(\mathbb F_2)^6\) act on it. Define the reduced rational homology representation
\[
V=\widetilde H_7(X;\mathbb Q)\oplus\widetilde H_{15}(X;\mathbb Q).
\]
The trace \(\chi(t)=\operatorname{tr}(t\mid V)\) depends only on the Hamming weight \(w\) of \(t\). Its seven values, at weights zero through six, are respectively
\[
\boxed{(253,\ 9,\ 9,\ 53,\ 53,\ 1,\ 1).}
\]
For each \(a\in T\), let the rational one-dimensional sign character be \(\psi_a(t)=(-1)^{a\cdot t}\). The multiplicity \(m(a)\) of this character depends only on \(k=\operatorname{wt}(a)\) and is given by
\[
\boxed{m_k=(36,\ 1,\ 0,\ 6,\ 6,\ 0,\ 1),\qquad k=0,1,\ldots,6.}
\]
In particular, \(\dim_{\mathbb Q}V^T=36\), and no sign character of dual Hamming weight two or five occurs. The multiplicities sum to \(253=239+14\), agreeing with the published rational Betti numbers.

## Assumptions and scope

Hamming distance counts differing binary coordinates. A face is a finite set whose pairwise Hamming distances are at most four. The group \(T\) acts by bitwise addition, and its characters are indexed using the **original six Hamming coordinates** (not the alternate basis used in some folded-cube representations). Coefficients in the representation statement are rational. The result determines the character on the **direct sum** of two homology degrees, not their two separate characters. No integral torsion or equivariant homotopy classification is asserted.

The published rational homology computation of Galetto, Montaño and Wellner (2026), Appendix C.3, states that the only nonzero reduced rational homology is in degrees seven and fifteen, with ranks \(239\) and \(14\). We use that reported computation as an input for identifying the virtual Lefschetz character with the character of \(V\). The virtual reduced Lefschetz character established below is unconditional and does not require that input.

## Proof

**Forbidden graph.** Construct a graph \(G\) with vertex set \(T\) and edge \(\{x,y\}\) exactly when the Hamming weight of \(x+y\) is five or six. Then \(X=\operatorname{Ind}(G)\). Every vertex of \(G\) has seven neighbors. Define for any induced subgraph on vertex set \(S\) the signed independence sum
\[
Z(S)=\sum_{I\subseteq S\,\text{independent}}(-1)^{|I|}.
\]
It satisfies \(Z(\varnothing)=1\) and, for any vertex \(v\in S\),
\[
Z(S)=Z(S\setminus\{v\})-Z\bigl(S\setminus(\{v\}\cup N_G(v))\bigr).
\]
Exact bit-mask recursion on all sixty-four vertices gives \(Z(T)=253\). Both the stated recurrence and its complete finite computation are reproduced in the accompanying `CHECK.py`.

**Nonidentity translations.** A nonzero \(t\in T\) partitions the sixty-four vertices into thirty-two two-element orbits \(\{x,x+t\}\). A \(t\)-stable face must be a union of these orbits. If \(\operatorname{wt}(t)\ge5\), every orbit contains a forbidden edge, so only the empty stable face remains. Otherwise, form a quotient graph on the thirty-two orbits, excluding orbits whose internal pair is forbidden and joining two eligible orbits when any original forbidden edge joins them. Stable faces correspond bijectively to independent collections of quotient vertices.

For a stable face containing \(j\) orbits, translation acts on its \(2j\) vertices by \(j\) transpositions and thus acts on the oriented simplex with sign \((-1)^j\). Including the chain-degree sign \((-1)^{2j-1}\), its contribution to the reduced Lefschetz number is \((-1)^{j+1}\); the empty face in reduced degree minus one contributes \(-1\). Therefore, with \(F_t\) the signed independent-set sum of the eligible quotient graph,
\[
\widetilde L(t)=-F_t.
\]
For the identity, the same formula gives \(\widetilde L(0)=-Z(T)=-253\).

**Exact finite quotient evaluations.** Coordinate permutations send any translation of a given Hamming weight to any other of the same weight and induce complex automorphisms. It therefore suffices to check one representative of each positive weight. A direct recursive evaluation and an independent enumeration by cardinality parity agree on the following table:

| Translation weight | Eligible two-point orbits | Even independent quotient sets | Odd independent quotient sets | Signed sum |
|---:|---:|---:|---:|---:|
| 1 | 32 | 42153 | 42144 | 9 |
| 2 | 32 | 42153 | 42144 | 9 |
| 3 | 32 | 22101 | 22048 | 53 |
| 4 | 32 | 22101 | 22048 | 53 |
| 5 | 0 | 1 | 0 | 1 |
| 6 | 0 | 1 | 0 | 1 |

Thus \(\widetilde L(t)\) equals the negative of the displayed seven-value character. The cited rational homology concentration places every nonzero reduced rational group in an odd degree, hence \(\widetilde L(t)=-\operatorname{tr}(t\mid V)\). This proves the claimed trace values.

**Fourier decomposition.** Because \(T\) is elementary abelian of exponent two and \(\mathbb Q\) has characteristic zero, all irreducible rational representations of \(T\) are the sign characters \(\psi_a\). Orthogonality gives
\[
m(a)=\frac1{64}\sum_{t\in T}(-1)^{a\cdot t}\chi(t).
\]
Substitution of the seven signed sums gives \(m(a)=36,1,0,6,6,0,1\) according as the dual weight of \(a\) is zero through six. These are nonnegative integers, and their dimension sum is
\[
36+6+20\cdot0+20\cdot6+15\cdot6+6\cdot0+1=253.
\]
The trivial character has multiplicity thirty-six, as claimed.

## Verification

The accompanying self-contained `CHECK.py` uses the original Hamming coordinates throughout. It constructs every forbidden edge, checks degree seven at each vertex, evaluates the sixty-four-vertex signed independence sum using exact inclusion–exclusion, independently counts even and odd independent subsets of each relevant thirty-two-orbit quotient, and performs the complete sixty-four-term Walsh–Fourier transform. Running `python3 CHECK.py` produces `Q6_RIPS_SCALE4_TRANSLATION_CHECKS_OK`. A separate C++ quotient enumeration, independently implemented, produced the same parity counts for all six nonidentity weight representatives. The homology-degree concentration is taken from the cited primary literature rather than recomputed here.

## Relationship to prior work

Adams and Virk (first public preprint September 12, 2023) study hypercube Vietoris–Rips homology and specifically ask in Question 8.7 for the homology action of cube symmetries. Galetto, Montaño and Wellner (June 18, 2026) completely determine the full hyperoctahedral representation in the regimes of scales at most three and the penultimate scale, and separately report rational Betti numbers for this six-cube scale-four case. The case here is outside those representation-theoretic regimes. Existing exact computational records report the signed face count \(253\) and a folded-cube reduction, but these scalar data do not determine the nonidentity translation traces or the sign-character multiplicities. Related translation-representation results for hypercube Čech complexes concern a different functor and scale. No equivalent classification was found in the checked accessible literature and research records; inaccessible or unindexed equivalences remain possible.

## Limitations

The representation is determined only for the translation subgroup and only on the direct sum of degrees seven and fifteen; neither separate degree character nor the full coordinate-permutation action is determined. The cited rational Betti-number computation was not independently reproduced, so this paper's character-of-actual-homology interpretation depends on that published computational input, while the virtual reduced Lefschetz trace computation is self-contained. There is no claim about integral torsion, homotopy type, integral representation lattices, or general cube dimensions. No independent mathematical audit has been performed.

## References

1. Henry Adams and Žiga Virk, *Lower bounds on the homology of Vietoris–Rips complexes of hypercube graphs*, first public arXiv preprint September 12, 2023, arXiv:2309.06222v1, especially Introduction and Question 8.7.
2. Federico Galetto, Jonathan Montaño and Zoe Wellner, *Homology of Vietoris–Rips complexes of hypercube graphs via group actions*, first public arXiv preprint June 18, 2026, arXiv:2606.20784v1, especially Main Theorem and Appendix C.3.
3. TheoremDB, Problem P2816, *Integral torsion in scale-four hypercube Rips complexes*, and claim R390, *The n=6 complex is an independence complex of Q_6 with antipodal edges*, consulted October 17, 2026.
