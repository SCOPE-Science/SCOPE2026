# Sharp stabilization and complete ambiguity of binary weight-two linear \(k\)-mer multispectra

## Finding

For integers \(k\ge2\) and \(n\ge3k-2\), consider all binary **linear** words \(w\in\{0,1\}^n\) of Hamming weight exactly two. The observation \(\mathcal P_k(w)\) is the ordered-content, multiplicity-preserving length-\(k\) factor spectrum: for each \(u\in\{0,1\}^k\), record the number of starting positions \(i\in\{0,\ldots,n-k\}\) for which the contiguous word at positions \(i,\ldots,i+k-1\) is \(u\). The channel does **not** wrap around; it does **not** pool shorter read lengths or forget the order of letters inside a read.

Write any admissible source uniquely as \(w=0^a1\,0^b1\,0^c\), where \(a,b,c\ge0\) and \(a+b+c=n-2\). Put \(t=k-1\), and \(A=\min(a,t)\), \(B=\min(b,t)\), \(C=\min(c,t)\). Define an exceptional class of clipped triples by
\[
\mathcal E_k=\{(A,B,C): B=t,\ 0\le A,C<t,\ A+C=k-2\}.
\]
It has exactly \(k-1\) elements. **Complete fiber criterion:** two weight-two words of the same length \(n\ge3k-2\) have identical profiles if and only if their clipped gap triples are equal, **or both clipped gap triples belong to** \(\mathcal E_k\). No other collisions occur.

Let \(C_{n,k}\) be the number of distinct profile vectors. Then
\[
C_{3k-2,k}=3k^2-4k+2,\qquad
C_{n,k}=3k^2-4k+3\quad(n\ge3k-1).
\]
Hence \(3k-1\) is the sharp threshold for stabilization of the profile **count**; the exact maximum size of a zero-error code of length \(n\), weight two, under this deterministic observation is \(C_{n,k}\).

## Assumptions and scope

All letters are indexed and the alphabet is exactly \(\{0,1\}\). Each source has precisely two occurrences of \(1\). The output lists counts of **all** \(2^k\) ordered binary words of length \(k\), including zero counts. Distinct sources are compared at the same \(n\) and the same \(k\). The theorem covers every \(k\ge2\) and all \(n\ge3k-2\); it does not state formulas for the shorter range \(k\le n<3k-2\), other weights, or circular sequences.

## Proof

**Step 1: Clipped gaps determine a profile.** Every length-\(k\) window containing at least one \(1\) meets only the first \(k-1\) zero symbols in each of the three zero gaps. More formally, one can count windows containing both \(1\)s (if any) by the separation \(b+1\) and their available left and right padding up to \(k-1\); windows containing exactly one \(1\) are counted by the zero padding of that marked \(1\) toward the adjacent marker and the boundary, again up to \(k-1\). Thus the multiplicities of all nonzero-containing windows depend only on \((A,B,C)\). All remaining windows are \(0^k\), whose multiplicity is \(n-k+1\) minus the number of nonzero-containing windows. Therefore \((A,B,C)\) and \(n,k\) determine the entire vector.

**Step 2: Recovering the markers from graph imbalance.** Regard each observed \(k\)-mer as a directed edge from its length-\(k-1\) prefix to its length-\(k-1\) suffix. The word gives a path of \(n-k+1\) edges. Taking outdegree minus indegree of the edge-multiplicity vector telescopes to
\[
\delta_P-\delta_S,
\]
where \(P\) is the first \(t=k-1\) symbols and \(S\) the last \(t\) symbols of the source. In particular, when \(P\ne S\), the profile identifies \(P\) and \(S\) individually. A \(k\)-mer containing both markers occurs exactly when \(b\le k-2\); such a read displays their distance \(b+1\), so the profile recovers \(B=b\). If no read contains both, \(B=t\).

Now \(n\ge3k-2\) implies \(a+b+c\ge3t-1\). Since three numbers all at most \(t-1\) sum to at most \(3t-3\), **at least one gap is at least \(t\)**. Consequently, the prefix \(P\) and suffix \(S\) can never *both* contain both markers. For each \(P,S\), the leading and trailing zero counts identify \(A,C\) unless the respective window is all zeros, in which case that boundary gap is already known to be capped at \(t\). Hence if \(P\ne S\), the balance vector recovers \((A,C)\), and the two-marker read test recovers \(B\). The whole clipped triple is unique.

**Step 3: The balanced path case.** If \(P=S\), either both are \(0^t\), or both consist of precisely one \(1\) in an otherwise zero vertex. In the all-zero case \(A=C=t\); the two-marker-read test still determines \(B\), so the clipped triple is unique. In the single-marker case the boundary gaps must satisfy \(A=a<t\), \(C=c<t\), and equal placement of the \(1\) in the common prefix and suffix requires \(a+c=t-1=k-2\). The length condition forces \(b\ge t\), so \(B=t\). These are exactly the triples in \(\mathcal E_k\). There is no window containing both \(1\)s. For each location \(j\in\{0,\ldots,k-1\}\), the \(k\)-mer \(0^j1\,0^{k-1-j}\) appears exactly once: windows about the first marker supply those with at least \(a=j\) zeros before its marker, and windows about the second supply the complementary positions. More explicitly, the first marker contributes each window with \(0\le j\le a\), and the second contributes each window with \(a+1\le j\le k-1\), using \(c=k-2-a\). Thus every one-marker \(k\)-mer has multiplicity one, every two-marker \(k\)-mer has multiplicity zero, and \(0^k\) fills the remaining \(n-2k+1\) windows. Therefore **all** \(k-1\) exceptional clipped triples produce one and the same vector. Conversely, Step 2 and the balanced case prove there are no other coincidences, establishing the complete fiber criterion.

**Step 4: Enumeration and exact onset.** A clipped triple belongs to \(\{0,\ldots,t\}^3\). When \(n\ge3k-1\), its gap sum is \(n-2\ge3t\), and it is realizable exactly when at least one coordinate equals \(t\): if one coordinate is capped, set the three gaps initially to their clipped values and add the surplus to a capped coordinate; no uncapped triple can have the requisite sum because its coordinates are at most \(t-1\). The number of clipped triples is therefore
\[
(t+1)^3-t^3=3k^2-3k+1.
\]
The exceptional \(k-1\) triples collapse to one, subtracting \(k-2\), and giving \(3k^2-4k+3\).

At \(n=3k-2\), the sum is \(3t-1\), so the sole excluded capped triple is \((t,t,t)\), while every other capped triple remains realizable; no uncapped triple can sum that high. The same exceptional collapse applies. Exactly one fewer profile is obtained. Finally, a deterministic channel permits at most one representative from each output fiber in a zero-error code, and choosing one from every nonempty fiber attains this number. \(\square\)

## Verification

The standalone `verify.py` constructs every word with exactly two ones for \(2\le k\le11\) and \(3k-2\le n\le3k+8\), compares complete dictionaries of all length-\(k\) reads, and independently computes the clipped-gap equivalence labels. It checks both implications of the fiber criterion, the sharp boundary count, and the stable count: \(110\) parameter cases and \(31{,}240\) source words. The full statement for unbounded \(k,n\) follows from the proof, not these finite tests.

## Relationship to prior work

The coding meaning of multiplicity-preserving \(k\)-mer profile vectors and the de Bruijn edge-flow representation is established in H. M. Kiah, G. J. Puleo and O. Milenkovic, *Codes for DNA Sequence Profiles* (2015), Sections 2–3. That work gives general profile-space and asymptotic enumeration machinery rather than this exact sparse weight-two, **linear**, all-read-length law. Y. M. Chee et al., *Maximum Length RLL Sequences in de Bruijn Graph* (first public 2024-03-03), Sections 2 and 4, count RLL-supported windows and de Bruijn trails, rather than multisets of reads from exactly two-marker words. Jacquet, Knessl and Szpankowski's *Counting Markov Types* (2010) concerns Markov frequency matrices and asymptotic counts and is not an explicit evaluation of this restricted, boundary-sensitive weight-two observation. The locally derived sharp stabilization and fiber classification do not follow from the stated headline results of these sources without additional special-case analysis.

## Limitations

The classification requires linear non-wrapping windows, two markers, full ordered \(k\)-mer multiplicities and \(n\ge3k-2\). No characterization for smaller \(n\), additional symbols, more markers, cyclic spectra, or noisy / incomplete reads is asserted. General Markov-type or sparse sequencing literature could contain an equivalent unnamed specialization; novelty is based on examined primary text and record searches and has not received independent audit.

## References

1. Y. M. Chee, T. Etzion, T. L. Nguyen, D. H. Ta, V. D. Tran, V. K. Vu, *Maximum Length RLL Sequences in de Bruijn Graph*, arXiv:2403.01454v1, 2024-03-03, https://arxiv.org/html/2403.01454v1.
2. H. M. Kiah, G. J. Puleo, O. Milenkovic, *Codes for DNA Sequence Profiles*, arXiv:1502.00517v1, 2015-02-02, https://arxiv.org/html/1502.00517v1.
3. P. Jacquet, C. Knessl, W. Szpankowski, *Counting Markov Types*, DMTCS (2010), doi:10.46298/dmtcs.2768, https://geodesic.mathdoc.fr/articles/10.46298/dmtcs.2768/.
