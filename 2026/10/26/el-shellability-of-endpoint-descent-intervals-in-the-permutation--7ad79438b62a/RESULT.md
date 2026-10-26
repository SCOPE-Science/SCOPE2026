# EL-shellability of endpoint-descent intervals in the permutation pattern poset

## Finding

For every \(n\ge 2\) and \(2\le k\le n\), let \(\pi_{n,k}\) be the permutation whose first entry is \(k\) and whose remaining entries list \(1,2,\ldots,k-1,k+1,\ldots,n\) in increasing order (the final segment is empty when \(k=n\)). Then the interval \([1,\pi_{n,k}]\) in the permutation-pattern poset is EL-shellable. Reverse-complement symmetry gives the same conclusion for the family whose unique descent is at the final position.

## Assumptions and scope

The permutation-pattern order is defined by \(\sigma\le\pi\) when \(\pi\) has a subsequence whose standardization is \(\sigma\). A finite graded poset is EL-shellable if its cover relations can be labeled so that every interval has a unique strictly increasing maximal chain and that chain is lexicographically first. The claim concerns only the endpoint-descent family above; it does not assert shellability for every permutation with one descent.

## Proof

Write \(K=k-1\) and \(B=n-k\). Let \(\iota_\ell=12\cdots\ell\). For \(1\le a\le K\) and \(0\le b\le B\), define
\[
\tau_{a,b}=(a+1),1,2,\ldots,a,(a+2),(a+3),\ldots,(a+b+1),
\]
where the final segment is empty if \(b=0\). Every pattern of \(\pi_{n,k}\) is either an increasing permutation \(\iota_\ell\), with \(1\le\ell\le n-1\), or exactly one of the \(\tau_{a,b}\). Indeed, a subsequence avoiding the first entry of \(\pi_{n,k}\) is increasing; a subsequence using that entry chooses \(a\) values below \(k\) and \(b\) values above \(k\), yielding \(\tau_{a,b}\) after standardization.

The order relations are:
- \(\iota_s\le\iota_t\) exactly when \(s\le t\);
- \(\iota_s\le\tau_{A,B'}\) exactly when \(s\le A+B'\), because the longest increasing subsequence of \(\tau_{A,B'}\) has length \(A+B'\);
- \(\tau_{a,b}\le\tau_{A,B'}\) exactly when \(a\le A\) and \(b\le B'\). A pattern with a descent must use the first entry of the target; the numbers of selected entries below and above that first entry are then respectively \(a\) and \(b\).

The rank of an element is its length minus one. Thus the cover relations are precisely
\[
\iota_s\lessdot\iota_{s+1},\qquad
\iota_{a+b}\lessdot\tau_{a,b},\qquad
\tau_{a,b}\lessdot\tau_{a+1,b},\qquad
\tau_{a,b}\lessdot\tau_{a,b+1},
\]
whenever the indicated elements exist and the indices stay within the stated bounds.

Label these covers as follows:
- \(\iota_s\lessdot\iota_{s+1}\) receives label \(s\);
- \(\iota_{a+b}\lessdot\tau_{a,b}\) receives label \(n\);
- \(\tau_{a,b}\lessdot\tau_{a+1,b}\) receives label \(a+1\);
- \(\tau_{a,b}\lessdot\tau_{a,b+1}\) receives label \(K+b+1\).

All labels other than \(n\) are at most \(n-1\). Consider any interval. An interval between two increasing permutations is a chain, and its labels increase strictly. An interval \([\tau_{a,b},\tau_{A,B'}]\) is a rectangle in the product order on the two indices. Its unique increasing chain first increments \(a\) until \(A\), then increments \(b\) until \(B'\): the \(a\)-labels increase within \(\{2,\ldots,K\}\), while the \(b\)-labels increase within \(\{K+1,\ldots,K+B'\}\). Any path taking a \(b\)-step before an \(a\)-step has a descent in its label sequence, and the \(a\)-first path is lexicographically first.

Finally consider \([\iota_s,\tau_{A,B'}]\), and put \(R=A+B'\). Its unique increasing chain is
\[
\iota_s\lessdot\iota_{s+1}\lessdot\cdots\lessdot\iota_R\lessdot\tau_{A,B'}.
\]
The last edge exists because \(\iota_R\lessdot\tau_{A,B'}\). This chain has increasing labels \(s,s+1,\ldots,R-1,n\) and is lexicographically first. Every other maximal chain branches from the identity chain at an earlier rank, receives label \(n\) on that branch, and must then use at least one grid edge with label at most \(n-1\); hence its labels decrease. There are no intervals with a descent-containing lower endpoint and an increasing upper endpoint. These cases exhaust all intervals, so the labeling is an EL-labeling and \([1,\pi_{n,k}]\) is EL-shellable.

Reverse-complement is an automorphism of the permutation-pattern poset and moves a descent at the first position to a descent at the final position, proving the symmetric case.

## Verification

The proof reconstructs the complete element set, all order relations, every cover type, and the increasing-chain condition for every interval; it is not an extrapolation from finite enumeration. The boundary cases \(k=2\), \(k=n\), and \(n=2\) are included: the index rectangle may degenerate to a chain, but the same labeling argument still applies. No computation or external certificate is needed for the infinite statement.

## Relationship to prior work

Smith's *Intervals of permutations with a fixed number of descents are shellable* proves shellability when both endpoints have the same number of descents and states as Conjecture 4.4 that \([1,\pi]\) is shellable for every one-descent \(\pi\) avoiding \(456123\) and \(356124\). The present family avoids both patterns: after its first entry, every entry is increasing, whereas each forbidden pattern has a descent after its first entry. Smith's same-descent theorem does not directly apply because \(1\) has zero descents and \(\pi_{n,k}\) has one. The result proves this infinite endpoint-descent subfamily of the conjecture, not the full conjecture.

McNamara and Steingrímsson prove that layered-permutation intervals without nontrivial disconnected subintervals are shellable and conjecture a broader criterion for separable permutations. For \(k\ge3\), \(\pi_{n,k}\) contains the pattern \(312\) and is not layered, so that layered-permutation theorem does not cover the family.

## Limitations

No claim is made for one-descent permutations whose descent is internal, and no proof is supplied for all permutations avoiding \(456123\) and \(356124\). The literature comparison is not a proof that no unindexed equivalent result exists. Independent review has not been performed.

## References

1. Jason P. Smith, *Intervals of permutations with a fixed number of descents are shellable*, arXiv:1405.2560 (first public version 2014-05-11); published in *Discrete Mathematics* 339 (2016), 118–126, DOI 10.1016/j.disc.2015.08.004.
2. Peter R. W. McNamara and Einar Steingrímsson, *On the topology of the permutation pattern poset*, arXiv:1305.5569 (first public version 2013-05-23).
