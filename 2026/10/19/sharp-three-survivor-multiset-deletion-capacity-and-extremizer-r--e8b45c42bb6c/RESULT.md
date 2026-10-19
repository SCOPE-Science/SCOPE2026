# Sharp three-survivor multiset deletion capacity and extremizer rigidity for alphabets of size at least five

## Finding

Let \(q\ge 5\), and let \(S_q(n,n-3)\) be the maximum number of \(q\)-symbol multisets of cardinality \(n\) whose survivors after any \(n-3\) deletions uniquely identify the original multiset. For every \(n\ge q+2\),
\[
S_q(n,n-3)=\begin{cases}
q+1,&q+2\le n\le2q,\\
q,&n\ge2q+1.
\end{cases}
\]
The jump thresholds are strict: at \(n=q+1\), there exist \(q+2\) compatible codewords, so the \(q+1\) plateau cannot start earlier.

At \(n=2q\), there is exactly one maximum codebook on a fixed labeled alphabet: the \(q\) constant-symbol multisets together with the multiset containing exactly two copies of every symbol. At \(n=2q-1\), there are exactly \(q^2\) maximum codebooks on a fixed labeled alphabet. They are specified by choosing a distinguished symbol \(s\), taking the light multiset with one copy of \(s\) and two of every other symbol, taking pure constant-symbol multisets for each symbol other than \(s\), and choosing the last member to be either the pure \(s\)-multiset or \(n-1\) copies of \(s\) plus one copy of an arbitrary other symbol. Here \(q\) choices of the last member are possible for each \(s\).

## Assumptions and scope

A \(q\)-symbol multiset of size \(n\) is a vector \(x=(x_1,\ldots,x_q)\in\mathbb Z_{\ge0}^q\) with \(\sum_i x_i=n\). Deletion decreases nonnegative coordinates; exactly \(n-3\) deletions leave a size-three vector. For \(x,y\), write \(I(x,y)=\sum_i\min(x_i,y_i)\), their multiplicity-counted intersection. Two vectors share an attainable three-symbol output exactly when \(I(x,y)\ge3\). Thus a valid codebook requires \(I(x,y)\le2\) for every two distinct members. The theorem concerns all integers \(q\ge5\) and \(n\ge q+2\), with precisely three survivors; the exhibited lower-threshold code at \(n=q+1\) is not asserted optimal. A 'labeled codebook' is an unordered subset of input vectors with coordinates fixed to their particular alphabet symbols.

## Proof

**(1) Heavy/light dichotomy.** Call \(x\) heavy if some coordinate satisfies \(x_i\ge3\), and otherwise light. For each heavy member choose a coordinate of multiplicity at least three. Two distinct heavy members cannot choose the same coordinate, since they would have \(I(x,y)\ge3\). Consequently a codebook contains at most \(q\) heavy members.

If \(x,y\) are light, every coordinate of both is at most two. The coordinatewise identity \(\min(a,b)+\max(a,b)=a+b\) gives
\[
I(x,y)=2n-\sum_i\max(x_i,y_i)\ge2n-2q.
\]
For \(n\ge q+2\), this is at least four, contradicting the required upper bound two. Hence a codebook contains at most one light member and has cardinality at most \(q+1\). If \(n\ge2q+1\), no light input vector exists because its coordinate sum would be at most \(2q\); in that case the bound improves to \(q\).

**(2) Matching constructions and phase endpoints.** Let \(e_i\) denote the \(i\)-th coordinate vector. For all \(n\), the \(q\) pure multisets \(ne_1,\dots,ne_q\) have pairwise intersection zero. If \(q+2\le n\le2q\), set \(h=n-q\) and form \(z\) with exactly \(h\) coordinates equal to two and the remaining \(q-h\) coordinates equal to one. The vector \(z\) has sum \(n\) and intersects each \(ne_i\) in at most two, so adjoining \(z\) creates a \(q+1\)-member codebook. This matches the upper bound. For \(n\ge2q+1\), the pure vectors match the bound \(q\).

At \(n=q+1\), take the \(q\) pure vectors and two further light vectors of size \(q+1\) having mutual intersection exactly two. Such light vectors exist for all \(q\ge2\): if \(q=2m\), double all symbols of either half, and add one singleton from the opposite half in each of the two multisets. If \(q=2m+1\), double each of two size-\(m+1\) subsets that meet in exactly one symbol, assigning zero to the other symbols. Each new multiset intersects every pure vector in at most two. This gives \(q+2\) codewords; no optimality claim is made at this shorter length.

**(3) Rigidity at the upper transition.** Consider a maximum \(q+1\)-member codebook at \(n=2q\). The heavy/light upper bound forces exactly \(q\) heavy and one light member. The light member must be \(z=(2,\ldots,2)\). Because every heavy member has an assigned triple-occupied coordinate and these assignments are injective, all \(q\) coordinates appear as assignments to exactly one heavy member. A heavy member assigned coordinate \(i\) already has intersection at least two with \(z\) there; positive multiplicity in any other coordinate would add at least one, contradicting \(I\le2\). Hence the heavy member is \(ne_i\). The codebook is uniquely forced, and part (2) proves that it exists.

At \(n=2q-1\), again every maximum codebook has exactly \(q\) heavy members and one light member. The light member is \(z_s\) with entry one in one distinguished coordinate \(s\) and entry two elsewhere. Every coordinate \(i\) supports a distinct assigned heavy member. When \(i\ne s\), the heavy member already intersects \(z_s\) in two copies at \(i\); any other positive coordinate would make intersection at least three. Thus it equals \(ne_i\). The heavy member assigned to \(s\) intersects \(z_s\) in one copy at \(s\), so there is room for at most one unit of positive mass outside \(s\): it must be either \(ne_s\) or \((n-1)e_s+e_j\) with exactly one \(j\ne s\). Conversely, each of these choices is compatible with all other pure heavy vectors (its intersection with a pure \(j\)-vector is only one) and with \(z_s\) (intersection exactly one or two). Thus, for each of the \(q\) possible \(s\), there are exactly \(q\) choices of the final member; the resulting codebooks are distinct because each has a unique light vector. This proves the \(q^2\) enumeration.

## Verification

The accompanying standalone `check.py` uses only the Python standard library. It enumerates all multiset vectors for \(2\le q\le6\) and \(q+2\le n\le2q+1\), checks the light-light collision inequality and explicit capacity constructions, independently exhausts all four-member ternary codebooks at lengths five and six (finding nine and one maximum codebooks), and enumerates every possible heavy vector compatible with the forced light vector at the two rigidity thresholds through alphabet size six. It also verifies the two-light construction at \(n=q+1\) for \(2\le q\le15\). The recorded run analyzed 30,007 vectors and passed. The infinite statement follows from the preceding proof; these finite tests are consistency checks, not extrapolation.

## Relationship to prior work

Kreindel, Essayag and Zabokritskiy, *Multiset Deletion Codes: Cyclic Constructions, Bounds, and Exact Results*, arXiv:2601.05636v2, §4.4, Proposition 12, give \(S_q(n,n-3)\le q+\binom q2\) for \(n\ge q+2\) by singleton/pair certificates. Their stronger-looking Reiman-type bound is shown there to be weaker in this regime. The sharper \(q+1\) and \(q\) values, complete phase boundaries and near-transition extremizer enumeration are not implied by that published certificate bound. The corresponding smaller-alphabet capacity formulae at \(q=3,4\) have been obtained previously and are **not claimed as new here**. The present asserted scope is the uniform \(q\ge5\) theorem together with structural rigidity.

The original multiset deletion metric appears in Kovačević and Tan, *Codes in the Space of Multisets—Coding for Permutation Channels with Impairments*, arXiv:1612.08837. Their general coding bounds do not by themselves determine these high-deletion capacities. Kreindel et al., arXiv:2603.18322, study polynomial constructions and deletion-ball geometry rather than the exact three-survivor phase diagram. No universal all-\(q\ge5\) theorem with the two extremizer counts was identified in the examined records; this is a bounded literature comparison, not a certificate of historical priority.

## Limitations

The theorem determines capacities only when exactly three symbols survive and \(q\ge5\), with \(n\ge q+2\); at \(n=q+1\) it gives only a lower bound. It does not classify optimal codebooks at interior lengths of the \(q+1\) plateau or in the \(q\)-sized phase. The enumerated counts are for labeled alphabets and unordered sets of multiset codewords. A possible earlier unindexed special-purpose extremal-set theorem remains an originality risk. No independent external validation was performed.

## References

- A. Kreindel, I. B. Essayag, A. L. Zabokritskiy, *Multiset Deletion Codes: Cyclic Constructions, Bounds, and Exact Results*, arXiv:2601.05636v1 (9 January 2026) and v2 (13 July 2026), particularly §4.4, Proposition 12.
- D. Kovačević and V. Y. F. Tan, *Codes in the Space of Multisets—Coding for Permutation Channels with Impairments*, arXiv:1612.08837 (2016).
- A. Kreindel, I. B. Essayag, A. L. Zabokritskiy, *Polynomial Constructions and Deletion-Ball Geometry for Multiset Deletion Codes*, arXiv:2603.18322 (2026).
