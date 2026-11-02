# Exact one-step tortoise complexity throughout a Sturmian slope interval

## Finding
Let \(\alpha\) be any irrational real number with \(1/3<\alpha<2/5\), and define the characteristic mechanical word \(c_\alpha=c_0c_1\cdots\) by
\[
c_j=\lfloor(j+2)\alpha\rfloor-\lfloor(j+1)\alpha\rfloor\quad(j\ge0).
\]
For every \(n\ge0\), write \(F_n\) for the set of distinct length-\(n\) factors of \(c_\alpha\), and let \(T\) be the one-step Defant--Kravitz binary tortoise map. Then the number \(\rho_T(n)=|\{T(w):w\in F_n\}|\) is
\[
\rho_T(n)=\begin{cases}1,&n=0,\\2,&1\le n\le3,\\n-1,&n\ge4.\end{cases}
\]
More precisely, for every \(n\ge4\), exactly two tortoise-image fibers contain more than one factor, and both contain exactly two factors. If \(z_m=c_0\cdots c_{m-1}\) denotes the length-\(m\) prefix, these two fibers are exactly
\[
\{10z_{n-2},01z_{n-2}\},\qquad \{001z_{n-3},010z_{n-3}\}.
\]
Every other length-\(n\) factor has a unique tortoise image among the length-\(n\) factors. In particular this holds for the Fibonacci fixed point of \(0\mapsto01,1\mapsto0\), whose slope is \((3-\sqrt5)/2\).

## Assumptions and scope
The alphabet is the ordered binary alphabet \(0<1\), factors are contiguous, and \(T\) is applied **exactly once**. For \(w\) with at least two symbols equal to \(1\), write it uniquely as \(w=0^a1\,0^b1u\) with \(a,b\ge0\). The tortoise operation is
\[
T(w)=0^{a+b}1u1.
\]
For a word with exactly one \(1\), it moves that \(1\) to the end; words with no \(1\) remain unchanged. This is the binary specialization of the recursive tortoise map, not the hare map, nor an iterated or eventual sorting equivalence. The statement holds for all irrational slopes in the stated open interval, all factor lengths without asymptotic or length cutoff, and all starting positions.

## Proof
**1. Characteristic mechanical-word structure.** For each starting position \(i\ge0\), put \(x_i=\{(i+1)\alpha\}\). Then the length-\(m\) factor starting at \(i\) has the first \(k\) letters summing to \(\lfloor x_i+k\alpha\rfloor\), for \(1\le k\le m\). As a function of \(x\in[0,1)\), the vector of these \(m\) prefix sums changes only at the \(m\) distinct thresholds \(1-\{k\alpha\}\), \(1\le k\le m\). At each threshold a coordinate increases, so the \(m+1\) intervening intervals have pairwise distinct length-\(m\) binary itineraries. Density of irrational rotation makes all itineraries occur, proving \(|F_m|=m+1\). In a recurrent binary word with this factor count there is exactly one left-special length-\(m\) factor, since every factor has some left extension and \(|F_{m+1}|-|F_m|=1\).

The prefix \(z_m\) is left special: it is the itinerary of the phase \(x_0=\alpha\), which is not one of the preceding thresholds (equality would imply an integral positive multiple of irrational \(\alpha\)). Hence an open interval around \(\alpha\) has the same length-\(m\) itinerary. At positions \(i\ge1\), the preceding letter equals \(1\) exactly when \(x_i<\alpha\), and equals \(0\) exactly when \(x_i>\alpha\). Density gives occurrences of \(z_m\) with both predecessors. Therefore \(z_m\) is the **unique** left-special length-\(m\) factor.

**2. Short forbidden factors.** Every length-\(\ell\) factor has either \(\lfloor\ell\alpha\rfloor\) or \(\lceil\ell\alpha\rceil\) ones. Since \(2\alpha<1\), \(3\alpha>1\), and \(5\alpha<2\), no factor contains \(11\), \(000\), or \(10101\). The six binary length-five words avoiding those three obstructions are precisely
\[
00100,\ 00101,\ 01001,\ 01010,\ 10010,\ 10100.
\]
All occur, because \(|F_5|=6\). In particular, the only three-letter strings immediately preceding an occurrence of a length-at-least-two factor beginning with \(01\) are \(001\) and \(010\) (the five-letter window formed by these preceding letters and \(01\) is \(00101\) or \(01001\)). The characteristic word begins with \(01\).

**3. Every long-image collision belongs to two possible types.** For \(n\ge6\), every factor contains at least two \(1\)'s: otherwise it is all zeroes or is \(0^a10^b\), with \(a,b\le2\), of length at most five. Because \(11\) and \(000\) are forbidden, the initial zeros \(a\) of a factor \(0^a10^b1u\) lie in \(\{0,1,2\}\), and \(b\in\{1,2\}\). The image \(T(w)=0^{a+b}1u1\) uniquely specifies \(s=a+b\) from its first \(1\), and then specifies \(u\). At fixed length \(n\), a distinct pair with one image can only arise from two distinct pairs \((a,b)\) with the same sum. The only such sums are \(s=2\) (from \((0,2),(1,1)\)) and \(s=3\) (from \((1,2),(2,1)\)). The two possible pairs of factors therefore have shapes
\[
\{1001u,0101u\}=\{10z,01z\},\quad z=01u,\ |z|=n-2,
\]
and
\[
\{01001u,00101u\}=\{010z,001z\},\quad z=01u,\ |z|=n-3.
\]
In either case the common suffix \(z\) has two different immediate left extensions, so it must be the unique left-special factor \(z_{|z|}\). Thus there are **at most** two nontrivial fibers, each of size at most two.

**4. Both pairs exist.** Fix \(m\ge2\). The prefix \(z_m\) starts with \(01\) and is left special, so both \(0z_m\) and \(1z_m\) are factors. Recurrence lets us choose occurrences with a preceding letter. Since \(000\) is forbidden, an occurrence of \(0z_m\), whose first symbols are \(001\), must be preceded by \(1\); hence \(10z_m\) occurs. Since \(11\) is forbidden, \(1z_m\) is preceded by \(0\); hence \(01z_m\) occurs. This produces the first asserted pair with \(m=n-2\). Moreover, the length-five factor list shows that the three preceding letters before an occurrence of \(z_m\) are necessarily \(001\) or \(010\); these respectively give immediate predecessors \(1\) and \(0\). Both occur since \(z_m\) is left special. Therefore \(001z_m\) and \(010z_m\) occur, giving the second asserted pair with \(m=n-3\ge2\). Each pair has equal tortoise images by the formula in the assumptions. The two images are different: their initial zero-run lengths are respectively two and three. With \(|F_n|=n+1\), exactly two mergers give \(\rho_T(n)=n-1\) for \(n\ge6\).

**5. Small lengths.** For \(n=1,2,3,4,5\), the entire factor sets, forced by the same Sturmian factor counts and the short forbidden patterns, are respectively
\[
\{0,1\},\ \{00,01,10\},\ \{001,010,100,101\},
\]
\[
\{0010,0100,0101,1001,1010\},
\]
\[
\{00100,00101,01001,01010,10010,10100\}.
\]
Directly applying \(T\) gives the image counts \(2,2,2,3,4\). At \(n=4,5\) precisely the same two specified two-element fibers occur; at \(n=3\) there is one three-element fiber. The empty word contributes one image at \(n=0\). This proves every assertion.

## Verification
Two standalone Python programs using only the standard library accompany this result. `verify_substitution.py` constructs **exact** factor sets of the Fibonacci word via all permitted adjacent substitution-block pairs, checking lengths \(1\) through \(180\), their image counts, and their complete nontrivial fibers. `verify_rotation.py` uses independent exact rational enclosures of three irrational slopes in the open interval, builds mechanically coded prefixes using certified floors, and implements the original stack process rather than the split-word formula. It checks factor and fiber identities for lengths \(1\) through \(90\). The recorded outputs are in `verify_substitution.out` and `verify_rotation.out`. These finite computations are corroboration, not a replacement for the unrestricted proof.

## Relationship to prior work
Defant and Kravitz introduced the tortoise operation for finite words. Campbell and Rampersad (arXiv:2604.25811, first public version April 28, 2026) introduced its fixed-length factor-complexity analogue and established a bounded-loss result for linearly complex words with bounded gaps; they determined exact one-step tortoise complexity for the paperfolding and Thue--Morse words and explicitly raised questions about Sturmian generalizations. Their general estimate does not determine the constant loss, collision multiplicities, or explicit fibers for this continuum of characteristic Sturmian words. The standard Sturmian factor count gives \(n+1\) but does not on its own determine one-step tortoise equivalence. The result here gives all lengths and full fiber structure on an entire natural slope interval.

## Limitations
The claim is restricted to characteristic mechanical words with irrational \(\alpha\in(1/3,2/5)\), ordered alphabet \(0<1\), and **one** tortoise application. It makes no statement about rational endpoints, arbitrary intercepts, slopes outside the interval, repeated tortoise applications, or hare equivalence. The code verifies finite ranges only, while the proof establishes the unrestricted formula. Priority against unindexed formulations cannot be ruled out without independent literature review.

## References
1. J. M. Campbell and N. Rampersad, *Subword enumeration up to stack-sorting equivalence*, arXiv:2604.25811v2 (2026), Sections 3--7. First public version: April 28, 2026. https://arxiv.org/html/2604.25811v2
2. C. Defant and N. Kravitz, *Stack-sorting for words*, Australasian J. Combin. **77** (2020), 51--68; preprint arXiv:1809.09158. https://arxiv.org/abs/1809.09158
3. J.-P. Allouche and J. Shallit, *Automatic Sequences: Theory, Applications, Generalizations*, Cambridge University Press (2003), Chapter 10 (Sturmian words and Fibonacci factor complexity).
4. Encyclopedia of Mathematics, *Fibonacci word* (fixed point and \(n+1\) factor complexity). https://encyclopediaofmath.org/wiki/Fibonacci_word
