# Scientific review

## Correctness — PASS

Every finite word is canonically represented by one restricted-growth encoding of its equality partition; this changes neither Abelian border equality nor its number of distinct letters. The exhaustive finite proof enumerates all \(678570\) partitions at length \(11\) and each smaller Bell-number family, computes the entire longest-prefix-border array by two distinct C++ procedures, and keeps the smallest realizing alphabet for every distinct array. An independent Python implementation reproduces all eleven exact rank rows. Both verifier files and the full table are included. The inference to all larger lengths is only the valid prefix-persistence statement, not an extrapolated maximal-rank claim.

## Originality — PASS

Habib, Shamil and Rahman, *Counting and Verifying Abelian Border Arrays of Binary Words* (arXiv:2111.00259), establish the binary formula and partition-based upper bounds for larger alphabets but no exact higher-alphabet first-appearance thresholds. Blanchet-Sadri, Chen and Hawes, *Dyck Words, Lattice Paths, and Abelian Borders* (arXiv:1708.06461), study border incidences in binary and partial words rather than minimum alphabet rank of the complete prefix-border array. Indexed comparisons of related Parikh and adjacent-pair invariants do not imply the rank table. Residual risk: an equivalent unindexed census may exist; the older binary article was only abstract-accessible.

## Mathematical value — PASS

Minimum alphabet rank is the direct alphabet-resource invariant for reconstructing a word from the array of longest Abelian borders of all prefixes. The computed sharp thresholds \(4,8,11\) identify where binary, ternary and quaternary realizations first become insufficient, determining the first three transition points not evaluated in the inspected primary general-alphabet work. The complete initial distribution and the persistence of genuine five-letter requirements at all greater lengths are structurally meaningful even though a general enumeration remains open.

## Reproducibility and limitations

The finite conclusion holds for every array of length at most \(11\) over any finite alphabet, because all actual letter-equality partitions are enumerated. Build and run `verify.cpp` with C++17 and run `verify_independent.py` with standard Python 3. The program outputs must end with `VERIFY_OK` and `INDEPENDENT_VERIFY_OK`. The maximal rank beyond length eleven, the general alphabet-dependence, and publication priority outside the inspected literature remain undetermined.

Self-review: passed. Independent audit: not yet performed.
