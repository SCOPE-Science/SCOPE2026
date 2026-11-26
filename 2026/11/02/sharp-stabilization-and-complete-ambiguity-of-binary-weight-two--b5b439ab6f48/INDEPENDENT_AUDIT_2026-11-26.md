# Independent mathematical audit

## correctness

PASS

For fixed n,k, every marker-containing window is determined by its padding limits up to t=k−1, and the all-zero count is the remainder. The prefix-minus-suffix imbalance of the (k−1)-factor path recovers both boundary strings whenever unequal and thus recovers the outer clipped gaps. A window can contain both markers iff b≤k−2 (a substring of length at most k can be extended to a k-window since n≥k), and it gives the internal gap. When the imbalance is zero, equal boundary strings can contain at most one marker because the two boundary windows are disjoint. All-zero boundaries identify A=C=t. Equal single-marker boundaries require a+c=t−1 and force b≥t in the claimed length range. For these exceptions the first marker realizes offsets 0 through a and the second a+1 through t, each once, giving exactly the same profile. The all-zero boundary case cannot share that profile: it has either a two-marker window or, with B=t, two single-marker windows at each offset. At n−2≥3t all triples with a capped gap are feasible by adding the surplus to a capped coordinate, and no uncapped triple is feasible. At n−2=3t−1 only (t,t,t) is lost. Subtracting t−1 for the exceptional merge gives the two counts and proves a sharp stabilization threshold of 3k−1; the fiber theorem already applies at 3k−2. The exception label has just one element for k=2. One representative from each fiber gives the exact code size under this deterministic channel. The supplied partition script was inspected, not executed; the proof is independent of its finite range.

## originality

PASS

The de Bruijn flow representation and profile definition are known. An indexed theorem for k=3 overlaps exactly in the binary case, even on the exceptional merge and deficient length. The supported distinct result is the linear fixed-weight-two fiber classification and sharp count for arbitrary k, not separate novelty for k=3. The relevant k-abelian equivalence keeps additional boundary information and splits exactly the exceptional labels when k>2. No broader statement giving the entire frozen claim was established in the compared sources.

## value

PASS

The result answers two exact questions for a natural sparse observation problem: which sources cannot be distinguished and the maximal possible distinguishable family. The boundary imbalance and the exceptional balanced merge explain why including shorter factors changes the answer. The one-profile deficit at the boundary proves a genuine cutoff rather than just a sufficient stabilization bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
