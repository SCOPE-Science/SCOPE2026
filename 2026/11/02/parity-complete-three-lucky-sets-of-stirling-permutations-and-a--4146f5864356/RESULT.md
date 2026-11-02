# Parity-complete three-lucky sets of Stirling permutations and a mixed-even construction

## Finding
For every integer \(n\ge3\) and \(2\le i<j\le2n-1\), suppose at least one of \(i,j\) is odd. Then there exists an order-\(n\) Stirling permutation whose **exact** lucky-car indices are \(\{1,i,j\}\) if and only if
\[
i\text{ is odd}\quad\text{or}\quad i<n.
\]
The number of distinct realizable triples in this parity sector is
\[
(n-1)(n-2)+hn-\frac{h(h+1)}2,\qquad h=\left\lfloor\frac{n-1}2\right\rfloor.
\]
Additionally, when both \(i,j\) are even, the inequality \(i+j\le2n\) is sufficient for exact realizability. This last statement is only a sufficient condition; the theorem does not classify the both-even sector.

## Assumptions and scope
An order-\(n\) Stirling permutation is a word \(w=(w_1,\ldots,w_{2n})\) containing every label \(1,\ldots,n\) exactly twice, such that all letters strictly between the two occurrences of \(k\) are greater than \(k\). Car \(t\) has preferred space \(w_t\) and takes the smallest unoccupied space at least \(w_t\) among \(2n\) spaces. It is *lucky* if it gets precisely \(w_t\). \(\operatorname{Lucky}(w)\) consists of car indices, not occupied-space indices.

For integers \(u\le v\), write \(B(u,v)=u,u,(u+1),(u+1),\ldots,v,v\); set \(B(u,v)\) to the empty word when \(u>v\). Concatenation is denoted by juxtaposition. If \(w\) has order \(m\), let \(\mathcal E_n(w)=w\,B(m+1,n)\) for \(n\ge m\). If \(w\) has order \(r\), let \(\mathcal L(w)\) denote the word obtained by increasing each letter by one and appending \(1,1\). Both operations produce Stirling permutations. The operation \(\mathcal E_n\) preserves all lucky indices, while \(\mathcal L\) preserves old lucky indices and adds \(2r+1\). These are the elementary constructions of Colmenarejo et al., Theorem 3.3, arXiv:2403.03280v1.

## Proof
**Necessary condition in the parity sector.** It remains to exclude \(i\) even with \(i\ge n\) and \(j\) odd. If \(i>n\), Proposition 3.8 of Colmenarejo et al. states that the second lucky index in a Stirling permutation must then be odd, contrary to \(i\) even. If \(i=n\) is even, their Lemma 4.3(a) says there cannot be a third lucky car. This proves necessity.

**Two-lucky input.** For \(i=2a+1\) odd, the order-\(r\) word
\[
U_{r,i}=B(2,a+1)\,1,1\,B(a+2,r)
\]
has exact lucky set \(\{1,i\}\) provided \(r\ge a+1\). For \(i=2a\) even and \(r\ge2a\), the order-\(r\) word
\[
V_{r,i}=B(1,a-1)\,a\,(2a),(2a)\,B(a+1,2a-1)\,B(2a+1,r)\,a
\]
has exact lucky set \(\{1,i\}\). These are explicit constructions from Theorem 4.1 of the cited paper; both may also be checked directly by observing that each new doubled block after its first visit has its preferred place already occupied.

**Case A: \(i,j\) odd.** Put \(m=(j+1)/2\). Then \(i\le2m-3\), so \(U_{m-1,i}\) exists. Take
\[
w=\mathcal E_n\big(\mathcal L(U_{m-1,i})\big).
\]
The two-lucky input contributes \(1,i\), and \(\mathcal L\) contributes exactly the new index \(2m-1=j\).

**Case B: \(i\) odd, \(j\) even.** Write \(i=2a+1\), \(j=2m-2\), with \(m\le n\). The order-\(m\) word
\[
w_0=B(3,a+2)\,1\,B(a+3,m)\,2,2,1
\]
is Stirling. Before the first \(1\), the doubled blocks occupy the consecutive spaces from \(3\) onward; the first \(1\) arrives in position \(2a+1=i\) and finds space \(1\) unoccupied. All remaining doubled blocks before the pair of \(2\)'s continue filling consecutive spaces from \(3\) upward, leaving exactly the hole \(2\). The first \(2\) arrives at position \(2m-2=j\) and takes that hole. The first car is lucky; every other car is unlucky because its preferred space is already occupied, including the second \(2\) and the last \(1\). Thus \(\operatorname{Lucky}(w_0)=\{1,i,j\}\). Apply \(\mathcal E_n\).

**Case C: \(i=2a\) even, \(j\) odd, \(i<n\).** Set \(m=\max(i+1,(j+1)/2)\le n\).

If \(m>i+1\), then \(j=2m-1\) and \(m-1\ge i\), so
\[
w_0=\mathcal L(V_{m-1,i})
\]
works by the two-lucky construction. If \(m=i+1\) and \(j=i+1\), use instead
\[
w_0=B(1,a-1)\,a\,(2a),(2a+1),(2a+1),(2a)\,a\,B(a+1,2a-1).
\]
The initial doubled blocks fill the earliest spaces; the first \(2a\), which arrives at index \(i\), and the first \(2a+1\), which arrives at index \(j=i+1\), each find their own preferred spaces free. All other cars after car one are unlucky, as a direct left-to-right occupancy check shows.

If \(m=i+1\) and \(j\ge i+3\), necessarily \(j\le2i+1\). Form the order-\(i\) word on labels \(2,\ldots,i+1\)
\[
v=B(2,a)\,(a+1)\,(2a+1),(2a+1)\,(a+1)\,B(a+2,2a).
\]
The word \(v\) has exactly two lucky indices, \(1,i\), when parked on an unbounded row of spaces: its first doubled blocks occupy consecutive places from \(2\), its first largest label is the unique additional lucky car at index \(i\), and its final doubled blocks are already blocked at their preferred spots. It occupies precisely spaces \(2,\ldots,2i+1\), leaving space \(1\) free. Its prefix of length \(i+2\) consists of complete nested blocks; all subsequent blocks are adjacent doubles. Thus every **even** cut of \(v\) at or after \(i+2\), including the cut after \(j-1\) letters, lies between complete blocks. Insert one \(1\) at that cut and another \(1\) at the end. The result is Stirling, and its first inserted \(1\), at index \(j\), is lucky because space \(1\) is still free. Earlier lucky indices remain \(1,i\); after the insertion, all other preferred labels are \(\ge2\), and their parking outcomes relative to occupied spaces \(\ge2\) are unchanged. The final \(1\) is unlucky. Again apply \(\mathcal E_n\).

**Case D: \(i,j\) even, with \(i+j\le2n\).** Put \(i=2a\), \(j=2b\), where \(1\le a<b\), and \(m=a+b\le n\). The order-\(m\) word
\[
w_0=B(1,a-1)\,a\,B(2a+1,m)\,(2a),(2a)\,a\,B(a+1,2a-1)
\]
is Stirling. The initial blocks and first \(a\) occupy spaces \(1,\ldots,2a-1\). The first car of the \(B(2a+1,m)\) segment arrives at index \(2a=i\) and finds its preferred space \(2a+1\) free; the entire segment fills spaces \(2a+1,\ldots,2b\), leaving space \(2a\) empty. The first \(2a\) arrives at index \(2b=j\) and fills that hole. All other cars except car one are unlucky, by the same contiguous-occupancy check. Hence the lucky indices are exactly \(\{1,i,j\}\). Apply \(\mathcal E_n\).

**Enumeration.** In the parity sector, odd \(i\) can be \(3,5,\ldots,2n-3\) and accounts for \(\sum_{a=1}^{n-2}2(n-a-1)=(n-1)(n-2)\) triples. Even \(i=2a<n\) with odd \(j>i\) accounts for \(\sum_{a=1}^{h}(n-a)=hn-h(h+1)/2\), with \(h=\lfloor(n-1)/2\rfloor\). These cases are disjoint. This completes the proof.

## Verification
The included standalone `verify.py` independently implements parking, validates the Stirling interval condition, and implements all four constructions. It checks all eligible pairs for each order \(3\le n\le60\), totaling \(112{,}520\) constructive cases. It also exhaustively generates all \((2n-1)!!\) Stirling permutations for each \(3\le n\le8\) by independently inserting maximum adjacent pairs, comparing every exact triple in the parity sector and confirming that all claimed both-even sufficient cases are realized. The observed three-lucky totals for orders \(3,4,5,6,7,8\) are respectively \(5,11,23,35,54,72\); the parity-sector counts are \(4,9,19,29,45,60\). Run with `python3 verify.py`. These finite tests corroborate, but do not substitute for, the general proof.

## Relationship to prior work
Colmenarejo et al., *On the Lucky and Displacement Statistics of Stirling Permutations*, arXiv:2403.03280v1, introduced admissible lucky sets, solved the two-element problem (Theorem 4.1), and posed the three-element classification problem (Section 4.2). The present odd-odd construction follows their Theorems 3.3 and 4.1, and the two obstructions in the necessity argument are their Proposition 3.8 and Lemma 4.3. Their Proposition 4.4 already handles the subfamily \(\{1,n-1,2n-2\}\) for even \(n\), a specialization of Case B. New content here is the full parity-sector classification and enumeration, including previously untreated odd-even and even-odd indices, and a broad both-even sufficient family. Harris and Martinez, *Parking functions with a fixed set of lucky cars*, arXiv:2410.08057v1, studies unrestricted parking functions; its every-subset admissibility does not imply admissibility under the Stirling repeated-letter and nesting constraints.

## Limitations
The theorem does not give a necessary condition for both-even triples. The finite verification through order eight does not establish any classification beyond the proved parity sector or the proved both-even sufficient region. Unindexed prior work could affect attribution; the argument has not undergone independent mathematical review.

## References
1. L. Colmenarejo, A. Dawkins, J. Elder, P. E. Harris, K. J. Harry, S. Kara, D. Smith, and B. E. Tenner, *On the Lucky and Displacement Statistics of Stirling Permutations*, arXiv:2403.03280v1 (2024), https://arxiv.org/html/2403.03280v1 .
2. P. E. Harris and L. Martinez, *Parking functions with a fixed set of lucky cars*, arXiv:2410.08057v1 (2024), https://arxiv.org/abs/2410.08057 .
