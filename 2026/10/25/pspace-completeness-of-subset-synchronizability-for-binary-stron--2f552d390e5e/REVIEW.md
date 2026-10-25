# Review

## Correctness

PASS. The subset graph has at most \(2^n\) vertices, so reachability of a singleton is decidable in polynomial space. The primary proof establishes hardness first for strongly connected automata and then reduces the alphabet to two letters while preserving subset synchronizability and strong connectivity. The reduction sizes are polynomial in the explicit input.

## Originality

PASS relative to the earliest verified source date. The unrestricted problem's PSPACE-completeness does not imply the result for the restricted class. The primary source explicitly proves the binary, strongly connected case by two reductions. The nearest related literature concerns unrestricted subset synchronization, other automata restrictions, or reset-length/threshold questions rather than this same decision problem under both constraints. A later paper restates the theorem but postdates the 2014 public version.

## Value

PASS. The result identifies a meaningful worst-case complexity boundary under two meaningful constraints—binary input and strong connectivity—that often arise in finite-state models. It distinguishes subset synchronization from ordinary synchronization of the whole state set, which is polynomial-time decidable for complete DFAs.

## Closest literature and limitations

The closest foundational result is PSPACE-completeness of unrestricted subset synchronizability, cited by Vorel to Natarajan (1986) and Sandberg (2005). Vorel's 2014 preprint supplies the restriction-preserving reductions. The result is about decision complexity, not a universal lower bound on shortest reset-word length.

Self-review: passed. Independent audit: not yet performed.
