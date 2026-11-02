# Scientific review: exact symmetric ternary insertion-covering codes

## Correctness (C): PASS

The alphabet-permutation orbits of all \(81\) four-symbol words are exhausted: one forced size-three constant orbit and thirteen size-six orbits. The covering predicate is equivalent to checking one representative from each of the \(41\) target-word orbits, since both subsequence deletion and covering commute with global symbol relabelings. All possible selections with up to five nonconstant orbits (\(2380\) subsets) fail, and exactly \(37\) of the \(1716\) six-orbit selections cover. The reversal counts and \(31\)-word witness are checked by two independently structured standalone programs. The finite proof and exact scope are stated in `RESULT.md`.

## Originality (O): PASS with residual risk

The closest published primary works develop unrestricted insertion covering, large-alphabet bounds and asymptotic densities; Pikhurko–Verbitsky–Zhukovskii explicitly credit an exact three-symbol **source-length-three** example, which is stronger coverage for that earlier parameter but does not imply this source-length-four symmetric classification. The word *symmetric* in Pikhurko–Verbitsky–Zhukovskii refers to coordinate permutations, which is not alphabet-label invariance. Xie–Sun–Ge and Lenz–Rashtchian–Siegel–Yaakobi have no identified corresponding exact \(S_3\)-invariant length-four optimum or enumeration. Indexed mathematical-record searches for the exact parameter, the symmetry constraint, alternative terminology, and the counts were performed. An unindexed prior small-parameter computation is the principal unresolved priority risk; no claim of exhaustive world-literature certification is made.

## Value (V): PASS

The channel is invariant under relabeling the alphabet, but a code need not be; requiring a codebook to respect that natural symmetry is a meaningful design constraint. The theorem gives the exact cost (minimum \(39\)), enumerates all \(37\) optimal symmetric designs, and shows through a directly checked \(31\)-word asymmetric construction that symmetry entails a nontrivial penalty of at least eight words. It is a complete extremal classification rather than a routine substitution into a general lower bound.

## Limits and comparison

The unconditional optimum is not determined; only the explicit upper bound \(31\) is used. No larger-alphabet or longer-block conclusions are claimed. Independent mathematical audit and definitive publication-priority verification remain outstanding.

Self-review: passed. Independent audit: not yet performed.
