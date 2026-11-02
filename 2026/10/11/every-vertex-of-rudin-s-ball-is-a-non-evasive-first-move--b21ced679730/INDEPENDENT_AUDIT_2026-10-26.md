# Independent mathematical audit

## correctness

PASS

From the exact 41 tetrahedra displayed in Benedetti--Lutz §6, the independently written bitmask maximal-face recursion calculates the face vector (14,66,94,41), every first vertex 1..14 has non-evasive deletion AND link, and second-step admissible counts are (11,11,11,11,11,11,9,9,9,9,5,5,5,5). Exactly 122 ordered first-two deletion-query prefixes follow. The recursion memoizes exact canonical finite face sets, with 28,708 visited states; its one-vertex base and empty-face-only exclusion are correct. The full 41-facet source tree and verify.py source were read; no opaque code was executed. The separate checker is provided with complete source/results and recovers the original 28,708-state count. Finite exhaustive enumeration is a proof here because the claim concerns precisely the specified finite 14-vertex complex; it does not imply an infinite-family theorem.

## originality

PASS

The closest primary full text, Benedetti--Lutz Theorem 6.3, only supplies an existence witness for non-evasiveness beginning at vertex 3. Requiring all fourteen roots and counting exactly 122 admissible two-step prefixes is strictly stronger, not implied by that witness or by vertex-decomposability theorems (Rudin is not vertex-decomposable). Resultary finds the same evaluated record, which is excluded as independent prior art, and a separate eight-vertex-ball root result, which is not a general domination. Hachimori and Macaulay2 exact-object pages provide facets and global properties, not this profile. No published prior statement implying this exact classification was identified after actual full-text inspection of the closest theorem. Best-of-knowledge qualified PASS, not priority certification.

## value

PASS

Rudin’s non-shellable, non-vertex-decomposable yet non-evasive 3-ball is a classic computational/topological test case. Whether all vertices may initiate a recursive non-evasiveness proof is a natural robustness invariant directly related to the property distinguishing this object. The exact multiset (11^6,9^4,5^4) and 122 admissible ordered first-two queries quantify the earliest loss of uniform choice. The finite classification is exact for a standard object, not an arbitrary unmotivated small slice; no general theorem or downstream paper-sized consequence is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
