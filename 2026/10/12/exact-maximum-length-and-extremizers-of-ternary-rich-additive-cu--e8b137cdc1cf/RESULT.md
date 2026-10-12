# Exact maximum length and extremizers of ternary rich additive-cube-free words

## Finding

Among all finite words over the weighted alphabet \(\{0,1,2\}\), with symbols carrying their usual integer weights, the maximum length of a word that is both palindromically rich and additive-cube-free is **\(104\)**. Exactly **\(8\)** labeled words attain this maximum. Under reversal and digitwise reflection \(a\mapsto2-a\), the eight extremizers form exactly **two orbits**, each of cardinality four.

The eight full, explicit words appear in `representatives.txt` and in the `REP` records of `additive_counts.txt`. They are certified by the executable enumeration and independently checked without use of its palindromic tree.

## Assumptions and scope

A palindrome is a word equal to its reversal. A finite word \(w\) of length \(n\) is **rich** when it contains exactly \(n+1\) distinct palindromic factors, counting the empty word. A **ternary additive cube** is a factor \(XYZ\) where \(X,Y,Z\) are consecutive blocks of the same positive length and their integer letter sums are equal: \(\sum X=\sum Y=\sum Z\). A word is additive-cube-free if it has no such factor. Symbols must be the *actual integers* zero, one and two; arbitrary alphabet permutations do not in general preserve additive cubes. No cyclic-word convention is used.

Both properties are factorial: every factor of an admissible word is admissible. In particular, checking all prefixes and all new-ending additive cubes suffices for exhaustive prefix-tree enumeration.

## Proof

**1. Exact richness extension test.** The standard characterization of a rich word is that every nonempty prefix has a unioccurrent palindromic suffix (Droubay--Justin--Pirillo, as recalled in Andrade--Mol, Theorem 2.1). When one letter is appended, at most one distinct palindrome can be new; if present, it is necessarily the longest palindromic suffix. Thus a rich prefix remains rich precisely when its extension creates this new palindrome. In `additive_enum.cpp`, a palindromic tree maintains the distinct palindromes, their longest suffix links, and transitions. At an extension, `p[cur].next[ch]!=0` means the candidate longest palindromic suffix already existed, so that branch is rejected; otherwise a new node represents the unique new palindrome. On returning from recursion, that node and its incoming transition are removed. The longest suffix is maintained by following suffix links until the appended symbol matches the outward letter.

**2. Exact additive-cube extension test.** Let \(S(j)\) denote the integer sum of the first \(j\) symbols. Every newly introduced forbidden factor must end at the last letter. For each positive block length \(k\) with \(3k\le n\), put \(a=n-3k\). Such a factor exists exactly when

\[
S(a+k)-S(a)=S(a+2k)-S(a+k)=S(a+3k)-S(a+2k).
\]

The function `appended_cube` checks all these possible \(k\) using exact integer prefix sums. Consequently no earlier forbidden factor can be missed, and no admissible extension can be rejected by an approximate test.

**3. Complete enumeration.** The depth-first procedure starts with the empty word, tries *all three labeled letters* at every node, and retains a branch if and only if the two tests above succeed. Induction on prefix length proves that the retained nodes at depth \(n\) are exactly the rich additive-cube-free words of length \(n\). In particular this is not an enumeration modulo alphabet relabeling. The executable enumerates through depth \(105\), visiting exactly **\(404535\)** admissible prefix nodes, with the final counts

\[
N(100)=90,\quad N(101)=80,\quad N(102)=36,\quad N(103)=12,\quad N(104)=8,\quad N(105)=0.
\]

All earlier \(N(n)\) are included in `additive_counts.txt`. Since any word longer than \(104\) has a length-\(105\) prefix, \(N(105)=0\) proves the universal upper bound. The eight words at depth \(104\) prove sharp attainment and certify their complete labeled classification.

**4. Natural symmetries.** Reversal preserves all palindromes and transforms an additive-cube factor into the reversed block order, so preserves the property. Replacing every letter \(a\) by \(2-a\) changes a length-\(k\) block sum from \(u\) to \(2k-u\), preserving equality of sums; it also preserves richness. Direct comparison of the eight enumerated words shows two disjoint orbits of size four under these two commuting involutions. `verify_additive.py` separately checks these set equalities.

## Verification

Compile and execute `additive_enum.cpp` with a C++17 compiler, redirecting its output into `additive_counts.txt`, then run `python3 verify_additive.py additive_counts.txt`. The first executable asserts that depth \(105\) is empty and exactly eight leaves occur at depth \(104\). The Python checker independently brute-forces all \(3^n\) labeled words for \(0\le n\le10\), applying direct palindrome enumeration and direct additive-cube tests, and compares every count. It also directly checks the richness and additive-cube-freeness of all eight length-\(104\) words, all three one-letter extensions, reversal/reflection closure, and two orbits. Expected final output is `VERIFY_OK max_len=104 labeled=8 symmetry_orbits=2 independently_bruteforced_lengths=0..10`.

The general upper bound is proved by a *complete bounded search*, not by extrapolation from a sample. The directly checked small cases provide an independently implemented cross-check of the enumerator logic.

## Relationship to prior work

Andrade and Mol, *Avoiding abelian and additive powers in rich words* (first public arXiv submission August 27, 2024), prove constructions for avoiding additive powers and report that the longest **abelian-cube-free** rich ternary word has length \(180\). The present requirement is genuinely stronger: equality of Parikh vectors implies equality of integer sums, so a word avoiding additive cubes also avoids abelian cubes, but not conversely. Their value \(180\) gives only a nonsharp upper bound for the present question and does not determine the bound \(104\), the eight weighted-alphabet extremizers, or the reversal/reflection orbits. The current finite census complements, rather than alters, their infinite-word theorems and open questions.

## Limitations

The result is specific to the integer alphabet \(\{0,1,2\}\) with its ordinary weights and to additive cubes (three equal-length blocks). It does not classify other integer triples, abelian-cube-free extremizers, or the existence of infinite additive-cube-free rich words over larger alphabets. Exhaustive search is independently reproducible but priority cannot be established conclusively from index searches; unindexed equivalent enumerations remain possible. The scientific verification is not an independent audit.

## References

1. J. Andrade and L. Mol, *Avoiding abelian and additive powers in rich words*, arXiv:2408.15390, first posted August 27, 2024; especially Sections 1, 2.3 and 5. https://arxiv.org/abs/2408.15390
2. X. Droubay, J. Justin, and G. Pirillo, *Episturmian words and some constructions of de Luca and Rauzy*, Theoretical Computer Science **255** (2001), 539–553 (rich-word prefix characterization; cited in Reference 1).
3. M. Rubinchik and A. M. Shur, *EERTREE: An Efficient Data Structure for Processing Palindromes in Strings*, European Journal of Combinatorics **68** (2018), 249–265 (palindromic-tree data structure; cited in Reference 1).
