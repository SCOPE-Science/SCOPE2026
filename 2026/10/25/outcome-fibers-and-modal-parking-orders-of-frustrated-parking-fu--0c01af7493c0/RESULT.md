# Outcome fibers and modal parking orders of frustrated parking functions

## Finding

For each integer \(n\ge1\), let \(\mathcal F_n\) be the set of successful frustrated-parking preference words. Cars \(1,\ldots,n\) arrive in numerical order at spots \(1,\ldots,n\); a car parks in its requested spot if vacant, and otherwise in the **largest still-vacant spot strictly above its request**, failing if no such spot exists. For \(\pi=(\pi_1,\ldots,\pi_n)\in S_n\), let \(N_n(\pi)\) count the words whose car \(i\) parks at spot \(\pi_i\). Define the set of right-to-left maximum positions
\[
R(\pi)=\{i\in\{1,\ldots,n\}:\pi_i>\pi_j\text{ for every }j>i\}.
\]
Then the **exact outcome-fiber formula** is
\[
N_n(\pi)=\prod_{i\in R(\pi)}(\pi_i-n+i).
\]
In particular, each permutation is realizable. If \(r=|R(\pi)|\) and \(k=n-r\), then
\[
N_n(\pi)\le (k+1)^{n-k}.
\]
Equality holds precisely when the first \(k\) entries of \(\pi\) are a permutation of \(1,\ldots,k\), and the final \(n-k\) entries are \(n,n-1,\ldots,k+1\) in that order. Consequently, the **maximum fiber size**, and the **number of distinct outcomes attaining that maximum**, are respectively
\[
M_n=\max_{0\le k<n}(k+1)^{n-k},\qquad
E_n=\sum_{\substack{0\le k<n\\(k+1)^{n-k}=M_n}}k!.
\]
The summands are disjoint because \(k\) equals the number of non-right-to-left maxima of the outcome. With the previously known total successful-word enumeration, a uniformly sampled successful word has outcome \(\pi\) with probability
\[
\Pr(\pi)=\frac{\prod_{i\in R(\pi)}(\pi_i-n+i)}{(2n-1)!!}.
\]
Thus the displayed \(M_n\) and its explicitly classified \(E_n\) outcomes give the exact mode of the full outcome distribution.

## Assumptions and scope

All preferences and spots are integers in \(\{1,\ldots,n\}\); cars enter in increasing index order, preferences are fixed in advance, and no preference word is admitted if even one car fails. The outcome convention here is the **parking spot of each successive car**: \(\pi_i\) is the spot occupied by car \(i\). This is the inverse of an alternative parking-order convention that records the car at each spot. To use that alternative \(\sigma\), substitute \(\pi=\sigma^{-1}\) in the formulas. The empty-product case is not needed because the last entry of any nonempty permutation is a right-to-left maximum. The case \(n=1\) is included.

## Proof

**Single-car predecessor lemma.** Fix an outcome permutation \(\pi\). Immediately before car \(i\) arrives, the vacant spots must be exactly \(U_i=\{\pi_i,\pi_{i+1},\ldots,\pi_n\}\), since previous cars occupied the complementary set. If \(\pi_i\) is not the largest element of \(U_i\), the only request that could place this car at \(\pi_i\) is \(a_i=\pi_i\): if that spot were occupied, the rule would select \(\max U_i>\pi_i\), or fail. There is exactly one such request.

If \(\pi_i=\max U_i\), the request \(a_i=\pi_i\) again works. Also any previously occupied spot \(a_i<\pi_i\) works: it forces the driver to take \(\max U_i=\pi_i\). No request at a vacant different spot, nor any request above \(\pi_i\), can work. Of the \(\pi_i-1\) smaller spots, exactly \(n-i\) remain vacant (every member of \(U_i\) other than its maximum is smaller). Therefore the number of allowed requests is
\[
1+(\pi_i-1)-(n-i)=\pi_i-n+i.
\]
This is positive because the maximum of an \((n-i+1)\)-element set of positive integers is at least \(n-i+1\).

**Multiplication.** In a fixed outcome \(\pi\), the set of occupied spots before each car is fixed. Any allowed request selected at every stage produces exactly that outcome, by induction on the arrival index. Conversely, every word producing \(\pi\) must use one of those requests at every stage. The allowed sets are independent across car indices, so multiplication of their cardinalities yields the asserted product. Taking \(a_i=\pi_i\) for all \(i\) also proves that every \(\pi\in S_n\) is achievable.

**Sharp record-count bound.** Let \(k=n-|R(\pi)|\) be the number of non-right-to-left-maximal entries. If \(i\in R(\pi)\), every previous position that is itself a right-to-left maximum has value larger than \(\pi_i\): right-to-left maxima decrease strictly from left to right. Thus any earlier occupied spot smaller than \(\pi_i\) necessarily belongs to one of the \(k\) nonmaximum positions. As the predecessor lemma identifies the corresponding factor with one plus the number of those smaller occupied spots, each factor is at most \(k+1\). There are \(n-k\) factors, proving the bound.

Equality means **every** record factor has exactly \(k\) earlier occupied smaller positions. In particular, before the *first* right-to-left maximum there must be all \(k\) nonmaximum positions, and their values must all be smaller than that first maximum. Therefore the first \(k\) positions are exactly the nonmaxima, the remaining \(n-k\) positions are all maxima and consequently strictly decreasing. Every nonmaximum value is smaller than every maximum value, because it is smaller than the first (largest) suffix maximum and, to obtain equality for the last (smallest) suffix maximum, it must be smaller than that one as well. Hence the initial values are precisely \(\{1,\ldots,k\}\), and the suffix is \(n,n-1,\ldots,k+1\). Conversely, any such permutation has \(k\) arbitrary leading nonmaxima, followed by \(n-k\) right-to-left maxima, each with exactly \(k\) smaller occupied spots preceding it, so its fiber is \((k+1)^{n-k}\).

**Modal outcome classification.** Maximizing over the necessarily unique \(k\) gives \(M_n\). For every maximizing \(k\), there are exactly \(k!\) permutations of the indicated form, and forms with different \(k\) do not overlap because their numbers of nonmaxima differ. Summing yields \(E_n\). Finally, Hallam–Molebash–Porter proved \(|\mathcal F_n|=(2n-1)!!\); divide each fiber size by this known total to obtain the probability formula. The double-factorial total is not claimed as new.

## Verification

The accompanying standard-library program `verify.py` directly simulates every preference word in \(\{1,\ldots,n\}^n\) for each \(1\le n\le7\). It compares the outcome fiber of every permutation to the independent right-to-left-maxima product, checks successful totals, tests sharpness and equality at every fixed record count, and reconstructs every modal outcome. Its recorded stdout is `verify_output.txt`. Reproduce using `python3 verify.py`; the final line should read `VERIFY_OK`. Finite testing does not replace the all-\(n\) proof above.

## Relationship to prior work

Hallam, Molebash, and Porter introduced the frustrated-driver rule and derived its total count, plus refinements by lucky cars/spots; their 2026 paper supplies the setting but, in the inspected sections, not the exact fiber for **a prescribed final permutation**, nor the modal outcome classification. Franks, Harris, Harry, Kretschmann, and Vance counted fibers for parking sequences/assortments that choose the first available forward spot; their fixed-order methodology is a motivating precedent, but its rule differs from choosing the **last available** forward spot. Related work on MVP parking and interval Fubini rankings also studies different parking dynamics. The new assertion is the permutation-specific factorization and all extremal outcome permutations, not the already-known total successful count.

## Limitations

The result assumes unit-length cars, one spot per car, and the exact farthest-available frustrated rule; it does not cover general graph parking, variable car lengths, or other parking variants. It determines the fibers and modes but does not supply a compact closed form for the maximizing integer \(k\) beyond the explicit finite maximization, which is exact for every \(n\). Prior-publication coverage was compared using accessible related primary literature and published research records; equivalent formulations under other terminology or nonindexed publications remain a bibliographic risk. There has been no independent external mathematical audit.

## References

1. Joshua Hallam, Jenson Molebash, and Chris Porter, *Parking with Frustrated Drivers*, arXiv:2609.35638v1 (first public September 28, 2026), https://arxiv.org/abs/2609.35638.
2. Spencer J. Franks, Pamela E. Harris, Kimberly Harry, Jan Kretschmann, and Megan Vance, *Counting Parking Sequences and Parking Assortments Through Permutations*, arXiv:2301.10830, https://arxiv.org/abs/2301.10830.
3. *On the Outcome Map of MVP Parking Functions*, arXiv:2207.13041, https://arxiv.org/abs/2207.13041.
4. *Counting ell-interval Fubini rankings through their parking outcome*, arXiv:2603.00693, https://arxiv.org/abs/2603.00693.
