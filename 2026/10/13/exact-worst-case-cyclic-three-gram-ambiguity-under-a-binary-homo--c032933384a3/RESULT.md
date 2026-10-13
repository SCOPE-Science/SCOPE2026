# Exact worst-case cyclic three-gram ambiguity under a binary homopolymer constraint

## Finding
Let \(n\ge2\) and let \(\mathcal W_n\) be the set of binary words on labeled cyclic positions \(0,\ldots,n-1\), with all indices interpreted modulo \(n\), that contain neither \(000\) nor \(111\) as a cyclic length-three factor. Two such words are observationally indistinguishable when their six allowed cyclic three-gram *multiplicities* agree.

Every feasible observation has the form
\[
\mathbf p(s,a,b)=(a,s-b,b,a,s-a,b),\qquad s\ge1,\quad 0\le a,b\le s,\quad 2s+a+b=n,
\]
and its exact fiber cardinality is
\[
\boxed{|\mathbf p^{-1}(\mathbf p(s,a,b))|=\frac{n}{s}\binom{s}{a}\binom{s}{b}.}
\]
The exact largest reconstruction list for every \(n\ge2\) is
\[
\boxed{L(n)=\max_{\lceil n/4\rceil\le s\le\lfloor n/2\rfloor}\frac{n}{s}\binom{s}{\lfloor(n-2s)/2\rfloor}\binom{s}{\lceil(n-2s)/2\rceil}.}
\]
For each fixed \(s\), equality requires the two excursion counts to differ by at most one. The maximizing values of \(s\), including possible ties, are exactly the maximizers in this explicit one-dimensional expression. Sample exact maxima are \(L(12)=108\), \(L(16)=600\), and \(L(18)=1200\).

## Assumptions and scope
All words are **indexed**, rather than equivalence classes modulo rotation. The observer counts overlapping consecutive three-bit factors with wraparound, including their multiplicities. The prohibited factors are exactly \(000\) and \(111\). The result covers each integer length \(n\ge2\); at length two the only allowed words are \(01\) and \(10\). The formula is an exact finite maximum over at most \(\lfloor n/2\rfloor-\lceil n/4\rceil+1\) candidate integers; no simpler formula for the maximizing \(s\) is asserted.

## Proof
Use the restricted directed order-two de Bruijn graph with vertices \(00,01,10,11\) and directed edges \(001:00\to01\), \(010:01\to10\), \(011:01\to11\), \(100:10\to00\), \(101:10\to01\), \(110:11\to10\). A cyclic word is a closed directed walk of length \(n\). Balance at \(00\) forces the counts of \(001\) and \(100\) to agree; balance at \(11\) forces those of \(011\) and \(110\) to agree. Balance at the two remaining vertices then forces the stated profile, with \(s\) the number of traversals \(01\to10\) through either \(010\) or \(011,110\). Each closed word has \(s\ge1\), and the opposite cross-section \(10\to01\) likewise has \(s\) traversals. The word length is exactly \(2s+a+b\).

For existence and counting, mark a cyclic position at which the two-bit vertex is \(01\). There are exactly \(s\) such positions in any valid indexed word. Starting from such a position, the walk consists of \(s\) successive excursions from \(01\) to \(10\) and back. Each outward excursion either uses the single edge \(010\) or the two-edge detour \(011,110\). Exactly \(b\) of these \(s\) excursions take that detour. Each return excursion either uses \(101\) or the two-edge detour \(100,001\), and exactly \(a\) of these \(s\) returns take that detour. Choosing the \(a\) and \(b\) detour positions independently produces exactly \(\binom s a\binom s b\) words beginning at the marked \(01\), with no disconnectedness or Eulerian-support exception. This also proves feasibility of every parameter triple above.

Count pairs \((w,i)\) where \(w\in\mathcal W_n\) has the prescribed profile and its vertex at cyclic index \(i\) is \(01\). Counting first by \(w\) gives \(s\) marks per word. Counting first by \(i\) gives \(n\binom{s}{a}\binom{s}{b}\) possibilities, by cyclic translation and the excursion representation. Division by \(s\) proves the fiber formula, including boundary cases where either detour count vanishes.

For fixed \(s\), the constraint is \(a+b=n-2s\). The factor \(n/s\) is constant. If \(a\ge b+2\), moving to \((a-1,b+1)\) multiplies the product of binomial coefficients by
\[
\frac{a(s-b)}{(s-a+1)(b+1)}>1,
\]
because \(a\ge b+2\) and \(s\ge a\). Thus a maximizer satisfies \(|a-b|\le1\), and both balanced choices attain the same value. Existence of such a pair with \(0\le a,b\le s\) requires exactly \(2s\le n\le4s\), proving the stated range of \(s\) and hence the final formula.

## Verification
The supplied standard-library script `verify_fiber.py` enumerates all binary words for each length \(2\le n\le18\), independently constructs each observed cyclic three-gram vector, checks the exact count of every profile against the closed formula, and checks the optimized maximum. It reports `EXHAUSTIVE_OK n=2..18`, including \(L(12)=108\), \(L(16)=600\), and \(L(18)=1200\). These computations are finite cross-checks. The preceding double count and binomial balancing argument prove the result for all lengths.

## Relationship to prior work
Kiah, Puleo and Milenkovic developed the DNA-sequence-profile observation model, restricted de Bruijn graph techniques, and general enumeration via integer flows. That framework motivates the present cyclic homopolymer-free model, but their primary results concern distinct achievable profiles, general flow-counting methods and code rates, rather than the exact *largest preimage size* for every length under this cyclic six-edge constraint. Counting profiles and computing the largest fiber are mathematically different: the former counts distinct vectors and the latter maximizes the number of indexed words mapping to one vector. The classical directed Euler-tour counting principle provides a general route to individual fiber sizes, but by itself does not supply the explicit all-length global maximization and balanced-count reduction in this claim.

## Limitations
The claim does not determine a closed elementary expression for which integer \(s\) wins the one-dimensional maximum, or for its asymptotics. The observation is cyclic, not a linear string with endpoints, and counts full multiplicities, not merely presence. No error correction under noisy or missing observations is established. General Euler-circuit counting underlies the subject, and unknown historical special-case evaluations may exist; a search cannot establish absolute priority.

## References
1. H. M. Kiah, G. J. Puleo, and O. Milenkovic, *Codes for DNA Storage Channels*, arXiv:1410.8837v1 (first public 2014-10-31); expanded as *Codes for DNA Sequence Profiles*, arXiv:1410.8837v2. https://arxiv.org/abs/1410.8837 ; https://arxiv.org/html/1410.8837v2.
2. P. Jacquet and collaborators, *Counting Markov Types* (2010), on enumeration of Markov type classes and directed graph formulations. The cited work treats general type counts rather than the above sharp restricted maximum.
