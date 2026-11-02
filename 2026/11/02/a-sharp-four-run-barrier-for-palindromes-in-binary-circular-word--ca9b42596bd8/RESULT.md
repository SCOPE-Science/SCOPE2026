# A sharp four-run barrier for palindromes in binary circular words

## Finding

For a nonempty binary circular word \(W\) of length \(n\), let \(\mathcal P(W)\) be the set of its distinct nonempty palindromic contiguous factors of lengths at most \(n\), allowing wraparound but not more than one full traversal, and put \(P(W)=|\mathcal P(W)|\). A *run* is a maximal cyclic block of one symbol. For positive integers \(a,b,c,d\), let \(W=0^a1^b0^c1^d\), with \(n=a+b+c+d\). Then

\[
P(W)=\begin{cases}
n+\min(a,c)+\min(b,d), & a\ne c,\ b\ne d,\\
n+a+\lfloor b/2\rfloor+\lfloor d/2\rfloor, & a=c,\ b\ne d,\\
n+b+\lfloor a/2\rfloor+\lfloor c/2\rfloor, & a\ne c,\ b=d,\\
n+\lfloor a/2\rfloor+\lfloor b/2\rfloor, & a=c,\ b=d.
\end{cases}
\]

Thus every binary circular word of length \(n\) with at most four runs satisfies \(P(W)\le\lfloor3n/2\rfloor\). This bound is sharp for every \(n\ge3\), already among two-run words. Among *exactly four-run* words the maximum equals \(4\) at \(n=4\), equals \(8\) at \(n=6\), and equals \(\lfloor3n/2\rfloor\) at \(n=5\) and every \(n\ge7\).

For exactly four runs, equality with \(\lfloor3n/2\rfloor\) occurs precisely when exactly one pair of opposite runs has equal length and, if \(n\) is even, the other two unequal run lengths are both even. This description applies whenever equality is possible. If \(n=2m+1\ge5\), the number of ordered positive run-length quadruples \((a,b,c,d)\) attaining equality is \(2m(m-1)\); if \(n=2m\ge4\), it is \((m-1)(m-2)-2\lfloor(m-1)/2\rfloor\). For each of these equality classes, the number of distinct binary necklaces is half the ordered quadruple count, because rotation exchanges the two zero runs and the two one runs, and no equality tuple has period two runs.

The four-run bound is a sharp threshold in run complexity: for every integer \(t\ge2\), the six-run circular word

\[
W_t=0^{2t}1\,0^{2t-1}1\,0^{2t-2}1
\]

has length \(6t\) and exactly \(10t-2\) distinct circular palindromic factors. Therefore \(P(W_t)>\lfloor3|W_t|/2\rfloor\) for every \(t\ge3\); six runs are necessary and, for infinitely many lengths, sufficient to exceed the four-run barrier. The six-run family is a known near-extremal construction in earlier circular-palindrome work; the new assertion is the exact four-run classification and consequent run barrier.

## Assumptions and scope

A factor of a circular word \(W\) is a contiguous factor of \(WW\) starting in its first copy, and its allowed length lies in \(\{1,\dots,n\}\). Two factors are counted once when their binary strings are identical, even if they occur at different starting positions. The word \(W\) is considered modulo cyclic rotation, but not modulo complementation. All run lengths are positive integers. The one-run case is a constant word and has \(P(W)=n\). A binary circular word with two or more runs has an even number of runs.

## Proof

**Two runs.** For \(W=0^a1^b\) on a circle, any factor of length at most \(n=a+b\) crosses at most two symbol changes, so any palindrome has one or three runs. The one-run palindromes are \(0^i\), \(1\le i\le a\), and \(1^j\), \(1\le j\le b\), giving \(n\). A three-run palindrome must contain a whole internal run; it is either \(0^i1^b0^i\) with \(1\le i\le\lfloor a/2\rfloor\), or \(1^j0^a1^j\) with \(1\le j\le\lfloor b/2\rfloor\). The halves of the outer run must be disjoint to keep length at most \(n\). The types are disjoint, hence

\[
P(0^a1^b)=n+\lfloor a/2\rfloor+\lfloor b/2\rfloor\le\lfloor3n/2\rfloor.
\]

If \(n\) is odd, equality holds for all positive \(a,b\); if \(n\) is even and at least four, equality holds when \(a,b\) are both even. Thus two runs realize the ceiling for all \(n\ge3\).

**Four runs: exhaustive palindrome classification.** A length-at-most-\(n\) factor of \(0^a1^b0^c1^d\) crosses at most four run boundaries. Since a binary palindrome starts and ends with the same symbol, it has either one, three, or five runs.

The one-run types contribute \(\max(a,c)+\max(b,d)\). The three-run types centered on a full one run have the forms \(0^i1^b0^i\) and \(0^i1^d0^i\), with \(1\le i\le\min(a,c)\), giving \(\min(a,c)(1+\mathbf 1_{b\ne d})\) distinct factors. Symmetrically, the types centered on a full zero run contribute \(\min(b,d)(1+\mathbf 1_{a\ne c})\).

A five-run palindrome starting and ending in zero must be centered on a full zero run and have the two full one runs equal, so it exists only when \(b=d\). If \(a\ne c\), the two central-zero lengths distinguish the families and the counts are \(\lfloor a/2\rfloor+\lfloor c/2\rfloor\); if \(a=c\), those families coincide and the count is just \(\lfloor a/2\rfloor\). The factor-length restriction yields the half-run bounds because the two outer pieces come from the same cyclic zero run. The analogous five-run palindromes starting and ending in one exist only when \(a=c\), contributing \(\lfloor b/2\rfloor+\lfloor d/2\rfloor\) when \(b\ne d\), or just \(\lfloor b/2\rfloor\) when \(b=d\). No two families with different run counts, starting symbols, or unequal central-run lengths overlap. Summing these disjoint contributions gives the displayed four-case identity.

**Sharp bound and equality.** When both opposite pairs are unequal, \(\min(a,c)\le(a+c-1)/2\) and \(\min(b,d)\le(b+d-1)/2\), so \(P(W)\le\lfloor3n/2\rfloor-1\). When \(a=c\), \(b\ne d\), the formula becomes \(n+a+\lfloor b/2\rfloor+\lfloor d/2\rfloor\). Because \(n=2a+b+d\), this equals \(\lfloor3n/2\rfloor\) exactly when \(b,d\) are not both odd. For even \(n\), the unequal pair has equal parity, so this condition means both are even; for odd \(n\), it is automatic. Exchange the letters for \(b=d\), \(a\ne c\). If both opposite pairs are equal, the formula is \(n+\lfloor a/2\rfloor+\lfloor b/2\rfloor<\lfloor3n/2\rfloor\). Equality is therefore exactly as stated.

For odd \(n=2m+1\), fixing \(a=c=p\), where \(1\le p\le m-1\), leaves \(2(m-p)\) ordered positive choices for \((b,d)\). Their sum is \(m(m-1)\); exchanging zero and one gives another \(m(m-1)\), disjoint because odd \(n\) forbids both opposite equalities. For even \(n=2m\), the same fixed-equal-pair case requires \(b=2u,d=2v\) for distinct positive \(u,v\) with \(u+v=m-p\). Summing \(m-p-1-\mathbf1_{2\mid(m-p)}\) over \(p=1,\dots,m-2\) and doubling gives the stated formula. The counts vanish at \(n=4,6\); direct substitution in the four-run formula gives their exceptional maxima \(4\) and \(8\).

**Six-run witness and optimality of the run threshold.** Put \(A=2t\), \(B=2t-1\), \(C=2t-2\), three pairwise distinct positive zero-run lengths, separated by three singleton one runs. The one-run palindromes number \(A+1=2t+1\). Three-run palindromes of the form \(0^i1 0^i\) number \(B=2t-1\), since the largest smaller member of an adjacent pair of zero-run lengths is \(B\). Three-run palindromes of the form \(1 0^r1\) number exactly three, one for each \(r\in\{A,B,C\}\). Five-run palindromes starting and ending in zero are \(0^i1 0^r1 0^i\), with \(r\) one of the three central zero-run lengths; their allowable outer lengths have respective maxima \(C,C,B\). They are distinct and contribute \(2C+B=6t-5\). Five-run palindromes starting in one and seven-run palindromes require two distinct zero-run lengths to be equal, so none exist. Since a length-at-most-\(6t\) factor crosses at most six boundaries, there are no more possibilities. Therefore \(P(W_t)=(2t+1)+(2t-1)+3+(6t-5)=10t-2\). At length \(6t\), the four-run ceiling is \(9t\), and the excess is \(t-2\). At most four runs are ruled out by the preceding theorem, while six-run witnesses exist for every \(t\ge3\).

## Verification

The accompanying standalone Python program enumerates circular palindromes directly from all starts and allowed lengths and independently by expanding around centers. Its checked outcomes are `VERIFY_OK direct_definition_instances=3836 symbolic_compositions=1502486 six_run_cases=20`. Exhaustive direct checks include every positive four-run composition through length \(18\) and every two-run composition through length \(29\); the larger symbolic census tests run-length equality cases through length \(79\). Additional deterministic random four-run instances and six-run witnesses up to length \(126\) were checked. The exact proof above, rather than these finite checks, establishes the statements for all allowed lengths. Run `python3 verify_circular_four_run.py` with Python 3; no third-party dependencies are needed.

## Relationship to prior work

Simpson's 2014 circular-palindrome bound is \(P(W)<5n/3\) for arbitrary circular words and includes a six-run family with count \(5n/3-2\) for infinitely many \(n\). This is broader in domain but weaker than the conditional \(3n/2\) bound: the general inequality does not imply the exact four-run identity, its equality cases, or the run-complexity threshold. The six-run family itself is not asserted to be new. OEIS A247000 records the unrestricted binary maxima for initial lengths and representative words, without the all-length four-run parameterization. Available records were searched for this run-stratified identity and equivalent formulations; none was found, but this is not a uniqueness proof. The complete full text of Simpson's paper could not be retrieved for a decisive comparison, so independent historical-priority checking remains important.

## Limitations

The exact identity covers only binary circular words having precisely four constant-symbol runs. The upper bound for at most four runs and the infinite six-run construction do not determine the unrestricted circular-palindrome maximum, or the maximum for exactly six runs. All palindromes are ordinary reversal palindromes, not reverse-complement palindromes, and lengths are capped at one traversal. The mathematical proof and computational checks are not independent peer review.

## References

1. Jamie Simpson, *Palindromes in circular words*, Theoretical Computer Science 550 (2014), 66–78, first available online 22 July 2014. https://doi.org/10.1016/j.tcs.2014.07.012
2. OEIS Foundation, A247000, *Maximal number of palindromes in a circular binary word of length n*. https://oeis.org/A247000
