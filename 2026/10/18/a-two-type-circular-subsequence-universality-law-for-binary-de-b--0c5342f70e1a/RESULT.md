# A two-type circular subsequence-universality law for binary de Bruijn cycles

## Finding

Let \(n\ge3\), \(N=2^n\), and let \(B\) be any binary de Bruijn cycle of order \(n\): every binary word of length \(n\) occurs at exactly one of its \(N\) cyclic starts. Let \(B_i\) be its length-\(N\) linearization starting at cyclic position \(i\), for \(0\le i<N\). The *subsequence-universality index* \(u(v)\) is the largest integer \(k\) such that every binary word of length \(k\) occurs as a scattered subsequence of the linear word \(v\).

Exactly two factors of \(B\) of length \(n\) are alternating (one starting in each letter). Call \(B\) **adjacent-type** if their *starting positions* are consecutive cyclic positions; otherwise call it **separated-type**. Define the circular greedy-arch throughput \(K(B)\) as the number of completed binary arches over one period when the three-state greedy arch scanner is initialized in its periodic state. Then

\[
K(B)=\begin{cases}
\lceil N/3\rceil,& \text{if }n\text{ is odd and }B\text{ is adjacent-type},\\
\lceil N/3\rceil,& \text{if }n\text{ is even and }B\text{ is separated-type},\\
\lfloor N/3\rfloor,& \text{otherwise}.
\end{cases}
\]

Every linearization has \(u(B_i)\in\{K(B)-1,K(B)\}\). More strongly, the **entire exact distribution** of these indices is independent of the de Bruijn cycle except for its displayed type. Put

\[
D_n=\begin{cases}
(2^{n+1}-3n-2)/9,&n\text{ even},\\
(2^{n+1}-6n+2)/9,&n\text{ odd}.
\end{cases}
\]

Then the number of cyclic starts with index \(K(B)-1\) is

\[
H(B)=\begin{cases}
D_n+n,&K(B)=\lceil N/3\rceil,\\
D_n,&K(B)=\lfloor N/3\rfloor,
\end{cases}
\]

and the remaining \(N-H(B)\) starts have index \(K(B)\). These formulas apply to **every** binary de Bruijn cycle of order \(n\ge3\), without a choice of construction or preferred rotation.

## Assumptions and scope

Positions and factors are cyclic modulo \(N\), whereas scattered subsequences and their universality indices are evaluated within each length-\(N\) **linear** cut, without wrapping. The labels \(0\) and \(1\) are fixed; no probabilistic or genericity hypothesis is used. An *arch* is the shortest next nonempty substring containing both letters, read greedily after the preceding completed arch. The number of completed arches equals \(u(v)\), by the greedy universal-subsequence criterion [1, Lemma 3.1].

A *repeat event* is a position \(j\) with \(B_{j-1}=B_j\). Consecutive repeat events at cyclic distance \(L\ge1\) define a **repeat gap** of length \(L\). Write \(E_L\) for the number of these gaps. In a binary de Bruijn cycle each pair \(00\) and \(11\) occurs \(2^{n-2}\) times, so there are exactly \(2^{n-1}\) repeat events.

## Proof

**1. Exact repeat-gap distribution.** A repeat gap of length \(L\) is equivalent to a cyclic factor of length \(L+2\) having equal first two symbols, alternating internal adjacent symbols, and equal last two symbols. For any fixed \(L\), exactly two binary strings have this shape. When \(L+2\le n\), each occurs exactly \(2^{n-(L+2)}\) times because every \(n\)-factor of a de Bruijn cycle appears once. Therefore

\[
E_L=2^{n-L-1}\quad(1\le L\le n-2).
\]

These account for \(\sum_{L=1}^{n-2}2^{n-L-1}=2^{n-1}-2\) gaps; exactly two gaps remain, each of length at least \(n-1\). A gap of length \(L\) contains \(\max\{0,L-n+1\}\) occurrences of alternating length-\(n\) factors. The cycle contains precisely two such factors. Hence no gap has length above \(n+1\), and the remaining two lengths must be either

\[
(n,n)\quad\text{(separated-type)}
\qquad\text{or}\qquad
(n-1,n+1)\quad\text{(adjacent-type)}.
\]

For the latter type the two alternating factors occur at consecutive cyclic starts within the length-\(n+1\) alternating block; in the former they lie in distinct gaps. This proves a complete, order-independent classification of repeat-gap lengths.

**2. Arch throughput.** Use the deterministic scanner with state \(\varnothing,0,1\). Reading symbol \(a\) when in state \(\varnothing\) sets state \(a\); reading \(a\) in state \(a\) leaves the state unchanged; reading \(a\) in state \(1-a\) completes one arch and resets to \(\varnothing\). Reading either \(00\) or \(11\) forces the same final state regardless of the entry state. The cycle contains repeat events, so the scanner has a unique periodic state trajectory.

Immediately after a repeat event at \(j\), its state is \(B_j\). Along the next repeat gap of length \(L\), the input alternates up to the next repeated pair; the scanner completes exactly \(\lfloor L/2\rfloor\) arches. Thus

\[
K(B)=\sum_{L\ge1}E_L\lfloor L/2\rfloor.
\]

Substituting the distributions from step 1 gives

\[
\begin{aligned}
K_{\rm sep}&=\sum_{L=1}^{n-2}2^{n-L-1}\lfloor L/2\rfloor+2\lfloor n/2\rfloor,\\
K_{\rm adj}&=\sum_{L=1}^{n-2}2^{n-L-1}\lfloor L/2\rfloor
+\lfloor(n-1)/2\rfloor+\lfloor(n+1)/2\rfloor.
\end{aligned}
\]

Summing the finite geometric-arithmetic series yields the two neighboring integers \(\lfloor 2^n/3\rfloor\) and \(\lceil2^n/3\rceil\). The separated type takes the larger one when \(n\) is even; the adjacent type takes the larger one when \(n\) is odd.

**3. Every rooted index is at most one smaller.** At any cut, the periodic scanner starts in some state \(q\). A scanner started instead at \(\varnothing\) produces the arch count \(u(B_i)\); if \(q\ne\varnothing\), starting at \(q\) is equivalent to reading one extra initial symbol before \(B_i\). Adding one leading symbol can increase the maximum number of disjoint full-alphabet arches by at most one, and cannot decrease it. Therefore \(K(B)-1\le u(B_i)\le K(B)\).

**4. Counting the deficient cuts.** Consider the \(L\) cut positions strictly after a repeat event at \(j\) through the next event at \(j+L\). At the position \(j+d\), for \(1\le d<L\), the stationary scanner immediately before the cut has a nonempty state opposite the first input precisely when \(d\) is odd. If \(d\) is even it starts as \(\varnothing\), so no arch is lost. For odd \(d\), compare the stationary and empty-state scanners until the next repeat event synchronizes them. Their completed-arch difference at that point is one exactly when \(L-d\) is odd, equivalently when \(L\) is even. The cut at \(d=L\) never loses an arch. Hence an even repeat gap contributes exactly \(L/2\) deficient cuts and an odd repeat gap contributes none:

\[
H(B)=\sum_{\substack{L\ge1\\L\text{ even}}}E_L\,L/2.
\]

The fixed short-gap contribution is

\[
\sum_{\substack{2\le L\le n-2\\L\text{ even}}}
(L/2)2^{n-L-1}=D_n.
\]

If \(n\) is even, two exceptional gaps of length \(n\) add \(n\) precisely for separated-type cycles; otherwise their \(n-1,n+1\) replacements are odd and add zero. If \(n\) is odd, the exceptional pair \(n-1,n+1\) adds \(n\) precisely for adjacent-type cycles; otherwise two odd gaps of length \(n\) add zero. The type that adds \(n\) is exactly the larger-throughput type from step 2. Thus \(H(B)=D_n+n\) in the larger case and \(D_n\) in the smaller case. The number of nondeficient cuts is \(N-H(B)\), proving the theorem.

## Verification

`verify.py` uses a directed-Euler-trail depth-first enumeration to generate *every* binary de Bruijn cycle with orders \(3,4,5\) (respectively \(2,16,2048\) cycles). It independently checks the de Bruijn factors, the complete repeat-gap distribution, the adjacency class of the two alternating factors, all cyclic-cut greedy arch counts, and the predicted formulas. The total number of evaluated rooted cuts is \(65,808\). For orders \(3\) and \(4\) it also checks every universality index by enumerating all candidate scattered subsequences, without using the arch-count formula. Further tests use two independent constructions: Fredricksen–Kessler–Maiorana concatenation for orders \(3\) through \(10\), and randomized Eulerian constructions for \(105\) cycles of orders \(6,7,8\). Reproduce using `python3 verify.py` with the standard Python library.

The successful verifier message begins `VERIFY_OK complete_binary_debruijn_cycles_n3_to5=2066`. Finite checks corroborate the theorem; all-order validity follows from the preceding proof, not from experiments.

## Relationship to prior work

Abraham, Brockman, Sapp and Godbole [1] study *omnisequences* and establish the greedy arch criterion (their Waddle Lemma); their Section 2 contrasts substring-universal cycles with subsequence-universal words. Their results do not provide a cyclic-rotation-resolved subsequence-universality distribution for binary de Bruijn cycles. Ruskey, Sawada and Williams [2] construct fixed-weight binary de Bruijn variants, a different coverage problem that does not determine the rooted scattered-subsequence indices of an unrestricted binary de Bruijn cycle. Bille, Gørtz and Skjoldjensen [3] study automata accepting subsequences and size-delay tradeoffs; their automaton bounds do not imply the arithmetic two-type law. The new element here is the complete repeat-gap classification and its consequence for every cyclic cut.

## Limitations

The classification is for the binary alphabet and orders \(n\ge3\). It does not claim a comparable formula for larger alphabets, arbitrary universal cycles, or the number of de Bruijn cycles in either type. The two types need not both occur at each order (for instance, order \(3\) has only adjacent-type cycles). The claim concerns finite linear cuts of length exactly \(2^n\), not a circular definition of scattered embedding. An earlier equivalent formulation outside the inspected literature remains possible. No independent scientific audit has been performed.

## References

[1] S. Abraham, G. Brockman, S. Sapp and A. P. Godbole, *Omnibus Sequences, Coupon Collection, and Missing Word Counts*, arXiv:0905.4517, first posted 2009-05-27, Sections 2–4; https://arxiv.org/abs/0905.4517.

[2] F. Ruskey, J. Sawada and A. Williams, *De Bruijn Sequences for Fixed-Weight Binary Strings*, SIAM Journal on Discrete Mathematics 26 (2012), 605–617, DOI:10.1137/100808782; https://doi.org/10.1137/100808782.

[3] P. Bille, I. L. Gørtz and F. R. Skjoldjensen, *Subsequence Automata with Default Transitions*, arXiv:1510.08748, first posted 2015-10-29; https://arxiv.org/abs/1510.08748.
