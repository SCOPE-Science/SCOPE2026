# Radius-two rigidity across binary hard-core shifts, with sharp forbidden-block horizons

## Finding

For each integer \(k\geq 2\), let \(X_k\subset\{0,1\}^{\mathbb Z}\) be the binary hard-core shift in which distinct sites carrying a \(1\) have separation at least \(k+1\). Equivalently, between consecutive ones there are at least \(k\) zeros. A centered radius-two local rule is a map \(f:\mathcal L_5(X_k)\to\{0,1\}\), inducing \((F_f(x))_i=f(x_{i-2},\ldots,x_{i+2})\). Two rules are counted as distinct when their values differ on an admissible five-block.

**Surjectivity rigidity.** For **every** \(k\geq2\), a centered radius-two endomorphism \(F_f:X_k\to X_k\) is surjective if and only if it is one of the five spatial shifts \(x\mapsto\sigma^j x\), \(-2\leq j\leq2\).

The precise local-map counts and sharp lengths of the first legal output word omitted by nonsurjective maps are:

| Separation exclusion \(k\) | Endomorphisms | Onto maps | First omitted legal output length, with multiplicity |
| --- | ---: | ---: | --- |
| \(2\) | 23 | 5 | \(1:1,\ 4:7,\ 5:4,\ 6:2,\ 8:2,\ 9:2\) |
| \(3\) | 9 | 5 | \(1:1,\ 5:2,\ 6:1\) |
| Every \(k\geq4\) | 6 | 5 | \(1:1\) |

In particular, the **sharp universal detection threshold** for a nonsurjective radius-two endomorphism over the entire family \(k\geq2\) is nine symbols. For \(k=2\), exactly the local-rule masks 96 and 258 require nine: their respective shortest missing output words are `100100001` and `100001001`. For \(k=3\), exactly mask 64 requires six, with witness `100001`.

## Assumptions and scope

All configurations are bilateral and the underlying alphabet is \(\{0,1\}\). Surjectivity is relative to the same \(X_k\), not the full binary shift. The radius is at most two; no restriction is placed on the local Boolean function beyond preserving \(X_k\). For a finite word \(w\), \(w\in\mathcal L_n(X_k)\) means its ones have pairwise separation at least \(k+1\). All such finite words extend to points of \(X_k\), by extending with zeros.

For reproducible rule masks, enumerate admissible five-blocks in ascending binary/lexicographic order and set \(f(w_j)\) to bit \(j\) of the nonnegative mask. For \(k=2\) the blocks in order are `00000,00001,00010,00100,01000,01001,10000,10001,10010`; for \(k=3\) they are `00000,00001,00010,00100,01000,10000,10001`.

The first omitted length of a nonsurjective \(F_f\) is the minimum \(n\geq1\) for which \(\mathcal L_n(F_f(X_k))\subsetneq\mathcal L_n(X_k)\). No such finite length exists for a surjective map.

## Proof

**1. Exact finite local preservation test.** The output belongs to \(X_k\) precisely when no two output ones occur at positive separation at most \(k\). Every possible violation is contained in an output block of length \(k+1\), depending on an input block of length \(k+5\). Consequently, \(f\) preserves \(X_k\) if and only if, for every \(v\in\mathcal L_{k+5}(X_k)\), the string
\[
(f(v_{0}\ldots v_4),f(v_{1}\ldots v_5),\ldots,f(v_k\ldots v_{k+4}))
\]
is in \(\mathcal L_{k+1}(X_k)\). This is an if-and-only-if statement because every finite admissible input extends bilaterally.

For \(k=2\), the nine admissible length-five neighborhoods give exactly \(2^9=512\) possible restricted local rules. For \(k=3\), seven neighborhoods give \(2^7=128\) rules. The executable `verify.py` enumerates every rule and applies the equivalent local preservation condition above, obtaining respectively 23 and 9 preserving rules.

**2. Exact unrestricted image language.** For each preserving rule, make a directed labeled graph whose vertices are the admissible four-blocks \(u\in\mathcal L_4(X_k)\). Each admissible five-block \(v\) gives an edge \(v_{0}v_{1}v_{2}v_{3}\to v_{1}v_{2}v_{3}v_{4}\), labeled \(f(v)\). A word is in \(\mathcal L_n(F_f(X_k))\) **if and only if** it labels an \(n\)-edge path beginning at some vertex: a path is an admissible input block of length \(n+4\), and can be extended in both directions with zeros. This equivalence is valid for every positive \(n\).

Determinize the labeled graph by its exact reachable-vertex subsets. In parallel, read the output through the \(k+1\)-state hard-core legality counter: after each `1` the counter is zero, and only after \(k\) zeros can another `1` be read. The initial counter permits either symbol. Start with the full subset of graph vertices. On each legal next output symbol, update the subset by the union of the corresponding labeled successor sets. If the subset is empty, the consumed legal word has no input predecessor. Otherwise, continue until no new `(subset,counter)` pair occurs. Since \(F_f(X_k)\) is a compact, shift-invariant subset of \(X_k\), equality of all finite-word languages is equivalent to equality of the two infinite subshifts. This graph is finite; exhaustive closure therefore proves either surjectivity for all lengths or the shortest omitted word, with no infinite extrapolation. Breadth-first traversal certifies minimality of every reported witness.

The exact reachable closures for the 23 preserving rules at \(k=2\) find five surjective rules, whose masks are `8,48,162,260,448`, and the remaining 18 shortest omitted lengths have the first histogram above. The two extremal masks and words are as stated. At \(k=3\), the surjective masks are `4,8,16,66,96`, and the remaining four have lengths \(1,5,5,6\). Direct comparison of each of the five surjective local truth tables with the coordinate projections verifies that they are precisely the five shifts \(\sigma^j\) for \(-2\leq j\leq2\). `classification.csv` contains every exact mask and witness.

**3. Entire infinite tail of the exclusion hierarchy.** Let \(k\geq4\). Every admissible five-block has at most one `1`, so precisely six five-blocks occur: `00000` and the five single-`1` blocks. The value on `00000` must be zero, since otherwise the all-zero input would map to the forbidden all-one configuration. A configuration with a single input `1` produces, at the five output positions within radius two, exactly the values prescribed by the five single-`1` blocks. If two of those values were one, the output would have two ones at distance at most four, contradicting \(k\geq4\). Thus at most one of the five single-`1` values can be one. The only six preserving maps are the zero map and the five shifts. All shifts are onto, while the zero map omits the one-letter word `1`. This argument holds for **every** integer \(k\geq4\), independently of any finite enumeration.

The preceding cases together prove the uniform rigidity theorem and the globally sharp nine-letter obstruction.

## Verification

Run `python3 verify.py` from the directory containing `verify.py` and `classification.csv`. The checker uses only Python's standard library. It re-enumerates all \(512\) and \(128\) local masks for \(k=2,3\), and all \(64\) masks at the boundary \(k=4\); tests the complete local preservation conditions; traverses each entire reachable subset/counter graph; validates the precise counts, extremal masks, and words; and requires the regenerated `classification.csv` to match byte for byte.

In a separate direct language check, every preserving rule for \(k=2,3\) is tested by enumerating **all** admissible finite inputs of length \(n+4\), for all output lengths through its first missing word; surjective candidates are checked through nine and six output symbols respectively. These finite enumerations independently validate all reported first-missing lengths, while complete subset closure—not the bounded direct checks—proves the absence of *any* missing word for each surjective rule.

## Relationship to prior work

Ahmadi Dastjerdi and Jangjoo (arXiv:1108.3242, originally public 2011-08-16) develop the dynamical and topological theory of \(S\)-gap shifts; \(X_k\) is their cofinite-gap case \(S=\{k,k+1,\ldots\}\). Their treatment includes sliding block codes and proves general structure theorems, including a conjugacy between cofinite-gap shifts and certain two-gap shifts (Theorem 4.1). That conjugacy changes the local coding neighborhood and supplies no fixed-radius endomorphism census or length-nine obstruction. Their companion paper (arXiv:1108.3414) computes entropy, zeta functions and Bowen–Franks groups for sofic gap shifts, which do not imply this classification. Baker and Ghenciu (arXiv:1411.7167) discuss specification, Gibbs properties and entropy of \(S\)-gap shifts, rather than radius-two self-map rigidity.

The present theorem distinguishes the uniform onto-map structure of every exclusion range \(k\geq2\) from the richer small-exclusion case and quantifies a sharp three-stage change in finite detection horizons. General symbolic-dynamics algorithms for finite-state image languages are standard; the new assertions are the exact full-family rigidity and sharp counts/witnesses, not the existence of such algorithms.

## Limitations

This is a theorem for centered radius at most two. Higher-radius surjective non-shift maps are not excluded. The local-mask catalog is tied to the stated lexicographic order. The listed first omitted length is about **spatial output words**, not temporal trajectories or the finite-time iteration of a rule. Complete historical priority is not certified; an equivalent unindexed classification could exist. No independent external scientific audit has been performed.

## References

1. D. Ahmadi Dastjerdi and S. Jangjoo, *Dynamics and Topology of S-gap Shifts*, arXiv:1108.3242, 2011. https://arxiv.org/abs/1108.3242
2. D. Ahmadi Dastjerdi and S. Jangjoo, *Computations on Sofic S-gap Shifts*, arXiv:1108.3414, 2011. https://arxiv.org/abs/1108.3414
3. S. Baker and A. E. Ghenciu, *Dynamical properties of S-gap shifts and other shift spaces*, arXiv:1411.7167, 2014. https://arxiv.org/abs/1411.7167
