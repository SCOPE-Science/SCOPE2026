# Affine rigidity of optimal nine-motif cyclic pair-sum labels

## Finding
Let \(G=\mathbb Z_{56}\), and call a nine-element subset \(S\subseteq G\) a weak \(B_2\)-set if its \(\binom{9}{2}=36\) sums \(s+s'\), taken over distinct unordered pairs \(\{s,s'\}\subset S\), are pairwise distinct modulo \(56\). Every such subset is an affine image of
\[
S_0=\{0,1,2,4,7,13,24,32,42\}.
\]
Precisely, every solution has the form \(uS_0+t\) for a unit \(u\in (\mathbb Z_{56})^\times\) and \(t\in G\). The action is free: all \(\varphi(56)\cdot56=1344\) affine maps produce different subsets. Consequently the full family of optimum nine-label cyclic pair-sum checks has exactly one affine equivalence class and \(1344\) members.

The minimum feasible modulus \(56\) and the displayed lexicographically first optimal subset were already recorded by Haanpää, Huima and Östergård and by OEIS A004135. The *affine classification, rigidity, and count* are the finding here, not the known minimum or the witness.

## Assumptions and scope
The pair elements must be distinct, and sums are computed in the additive group of residues modulo \(56\). Distinct unordered pairs must have distinct sums, but sums of repeated elements are not required to be different. An affine change of labels is \(x\mapsto ux+t\) with \(\gcd(u,56)=1\). This change preserves distinctness of unordered pair sums, since their values change by the invertible affine map \(z\mapsto uz+2t\).

The application is limited to the cyclic weak-\(B_2\) row-labeling ingredient for two-motif-error identification in the composite-DNA coding constructions of Ye et al. No classification of all error-correcting codes or all checksum architectures is claimed.

## Proof
**Step 1: a complete finite census normalized at zero.** Translation preserves the weak-\(B_2\) property, so every solution is a translate of one containing \(0\). An exact depth-first search visits each strictly increasing sequence \(0=a_0<a_1<\cdots<a_8<56\) at most once. At a prefix \(a_0,\dots,a_{k-1}\), it maintains all sums of distinct pairs already chosen. A new candidate \(x>a_{k-1}\) is admitted exactly when the \(k\) new residues \((x+a_i)\bmod56\) are all distinct from one another and all previously used pair sums. That condition is both necessary and sufficient to extend the prefix without an existing collision. A branch is skipped only if too few integers remain to reach nine elements. Thus every normalized solution appears at one terminal node and every terminal node is a normalized solution.

The executable `classify56.cpp` performs this exhaustive enumeration and records \(216\) terminal solutions after \(3,455,863\) visited recursion states. Separately, `verify_rigidity.cpp` reconstructs the sum set using a Boolean residue array and obtains the same \(216\) normalized solutions. The latter code stores all normalized solutions as 56-bit subset masks.

**Step 2: a full affine orbit.** The displayed \(S_0\) is checked directly: `pair_sums.tsv` lists all \(36\) distinct residue sums and their contributing pairs. For each of the \(24\) units \(u\bmod56\) and the \(56\) translations \(t\), the second verifier forms \(uS_0+t\) and stores the resulting subset mask. It finds \(1344\) distinct masks in this orbit and exactly \(216\) masks containing zero. The \(216\) zero-containing masks are compared as *sets* with the independently enumerated \(216\) normalized solutions and are equal.

**Step 3: completeness and freeness.** Any solution \(S\) has some element \(s\); the translate \(S-s\) contains zero, so Step 2 identifies it as an affine image of \(S_0\), and therefore \(S\) itself is an affine image. The affine group has exactly \(56\varphi(56)=1344\) elements. Since Step 2 produces \(1344\) distinct images, the stabilizer of \(S_0\) is trivial and the action on all solutions is free. Both the one-orbit classification and exact count follow.

## Verification
Compile and execute both standalone sources with a C++17 compiler:

```sh
g++ -std=c++17 -O2 -Wall -Wextra -pedantic classify56.cpp -o classify56
./classify56
g++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_rigidity.cpp -o verify_rigidity
./verify_rigidity
```

The second verifier must report `exhaustive_zero_containing=216 orbit_zero_containing=216 entire_affine_orbit=1344`, followed by `VERIFY_OK`. The alternative enumerator must give `normalized_sets=216 affine_orbits=1`. Source code enumerates every eligible finite prefix with no imposed time limit, randomization, or heuristic pruning. `pair_sums.tsv` is a human-readable check of the displayed representative. The proof of universal coverage depends on the explicit exhaustive recursion argument, not just the printed log.

## Relationship to prior work
Haanpää, Huima and Östergård (2004), the source table reproduced in OEIS A004135, and sequence A260998 already establish the minimum modulus \(Q_{9,2}=56\) and record the very same canonical example \(S_0\). These results settle existence and minimum modulus, **not** affine uniqueness or the number of optimal label systems in the inspected text. The distinct-pair-sum model is also the weak-\(B_2\) ingredient introduced into composite-DNA code constructions by Ye et al. (2025, Section 3.3, Definition 3.2 and Construction 3.5), who tabulated examples through eight symbols. The classical stronger Sidon property, which also constrains equal-index sums, is a different parameter and does not determine this classification.

## Limitations
This is a finite, computer-assisted exhaustive classification for exactly nine labels and modulus \(56\), not a general formula for arbitrary sizes or moduli. The complete text of the 2004 article was not retrieved; four annotated scanned source-table pages were inspected, leaving a residual possibility that an earlier full-paper result or an unindexed calculation already states the orbit classification. That access limitation concerns originality, not the finite verification. The finding has undergone only the stated self-review; independent scientific audit has not been performed.

## References
1. H. Haanpää, A. Huima, P. R. J. Östergård, *Sets in \(\mathbb Z_n\) with Distinct Sums of Pairs*, Discrete Applied Mathematics **138** (2004), 99–106, DOI: 10.1016/S0166-218X(03)00273-7.
2. OEIS A004135, *Additive bases: minimum cyclic group order for a set with distinct pair sums*, https://oeis.org/A004135; linked annotated source tables: https://oeis.org/A004135/a004135.pdf.
3. OEIS A260998, *Maximum subset size with distinct sums of pairs*, https://oeis.org/A260998.
4. Z. Ye, O. Sabary, R. Gabrys, E. Yaakobi, O. Elishco, *More on codes for combinatorial composite DNA*, Designs, Codes and Cryptography **93** (2025), 3437–3462, DOI: 10.1007/s10623-025-01634-8. First publicly posted as the journal version on 15 May 2025.
