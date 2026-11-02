# Independent mathematical audit

## correctness

PASS

The full-part support lemma is valid: every color missing among fully colored parts must appear in at least two distinct partial parts, since each partial part has a zero vertex that cannot see its own colors. Thus w>=tm+2(k-c)>=tm+2 max(0,k-tm). For k=qm+s<= (r-1)m this yields the exact lower envelope qm+min(2s,m); the constructions attain it, with the q+1 full-part surjection possible since (q+1)m>=k and some blank part remains. Equality forces q complete distinct-color parts plus exactly two occurrences of each residual color when 2s<m, or q+1 complete parts with an onto palette when 2s>m; tie cases are disjoint. Named-color counts A=choose(r,q) k!/s! times the part-pair load sum of falling factorials, B=choose(r,q+1) sum_j (-1)^j choose(k,j)(k-j)^((q+1)m), and the s=0 count follow without automorphism quotient. High-palette case follows degree<k. Independently enumerated all named functions in 30 small (r,m,k) cases, reproducing both minima and number of minimizers. Small checks supplement the general support proof.

## originality

PASS

Best-of-knowledge PASS specifically for the all-k>=3 balanced complete-multipartite singleton minimum AND labeled optimizer census. Lange's Oct 2026 primary work uses the identical singleton model and states exact families of cycles, prisms, Mobius ladders and generalized Petersen graphs; its full text could not be independently obtained, so no whole-document noncoverage claim is made. Kuzman's available full arXiv PDF defines subset-valued rather than singleton rainbow domination; the published complete-multipartite 2-rainbow function census also permits {1,2} labels. A related 2026 cylindrical singleton paper has another graph family. No inspected stronger statement entails the q*m+min(2s,m) phase split and full named optimizer formula for all k>=3. The prior k=1,2 special cases are explicitly not asserted novel.

## value

PASS

The balanced complete multipartite family is an elementary but natural regular graph model where every vertex outside a part shares a neighborhood, making palette redundancy and placement capacity structurally meaningful. The residue-dependent switch between duplicated residual colors and filling a further part, plus exact all-optimal-function enumeration, is a complete infinite-parameter classification useful for benchmarking algorithms and understanding singleton versus set-valued domination; it is not an arbitrary one-graph computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
