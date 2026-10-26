# Exact two-deletion circular traces for a single elongated run

## Finding

For integers \(a\ge3\) and \(k\ge3\), take the binary circular word represented by
\[
W_{a,k}=0^a(10)^{k-1}1.
\]
Its circumference is \(a+2k-1\). Delete exactly two *distinct positions* while preserving the clockwise order of the surviving letters, and identify the outputs under cyclic rotation (but **not** reflection or bit complementation). Write \(T_s(a,k)\) for the number of different resulting necklaces when exactly \(s\) of the two deleted bits are ones, for \(s\in\{0,1,2\}\).

The entire composition-refined two-deletion output spectrum is
\[
\begin{aligned}
T_0(a,k)&=1+\binom{k}{2},\\
T_1(a,k)&=1+(k-2)^2+H_a(k),\\
T_2(a,k)&=\binom{k-1}{2}-\mathbf 1_{\{a=3\}}\left\lfloor\frac{k-3}{2}\right\rfloor,
\end{aligned}
\]
where
\[
H_a(k)=\begin{cases}
\left\lceil (k-2)/2\right\rceil,&a=3,\\
k-2,&a\ge4.
\end{cases}
\]
Consequently the number of distinct necklaces in the entire exact-two-deletion sphere is
\[
\boxed{\;B_2(a,k)=\begin{cases}
2k^2-6k+8,&a=3,\\
2k^2-5k+5,&a\ge4.
\end{cases}\;}
\]
The change between a special run of length three and one of length at least four begins at \(k=4\), and the difference is exactly \(k-3\). This is a count of *distinct possible outputs*, not their probabilities or their multiplicities as deletion events.

## Assumptions and scope

The input is a binary necklace, i.e. an equivalence class of nonempty binary words under cyclic rotation. The trace operation deletes two distinct occurrences without changing the relative clockwise order; traces are again necklaces. Deletion events acting at different positions can yield the same necklace. The starting point of the displayed representative is immaterial. The two parameters satisfy the integer restrictions \(a\ge3\), \(k\ge3\); no formula is asserted for \(a=1,2\), \(k=1,2\), arbitrary necklaces, random numbers of deletions, or more than two deletions.

The word \(W_{a,k}\) has precisely \(k\) zero runs and \(k\) one runs. Enumerate its circular runs as
\[
Z_0,O_0,Z_1,O_1,\ldots,Z_{k-1},O_{k-1},
\]
where \(Z_0\) has length \(a\) and all other runs have length one. Subscripts are run positions, not symbol exponents. In particular the ones \(O_0\) and \(O_{k-1}\) flank \(Z_0\) in the circle. A run signature means the cyclic sequence of pairs (letter, positive run length); its cyclic rotations, but not reversal, represent exactly one necklace.

## Proof

The number \(s\) of deleted ones is recoverable from the output: it has exactly \(k-s\) ones. Accordingly, the three spectrum parts are pairwise disjoint. Every occurrence of an element of a one-letter run has the same deletion effect; an occurrence in the distinguished long zero run can be chosen in \(\binom a2\) different ways if both deletions occur there, but all such choices yield a single necklace. We now exhaust the unordered pairs of deletion positions, retaining distinct *outcomes*.

**(A) No ones deleted.** The pair consists either of two positions of \(Z_0\), of one position of \(Z_0\) and one singleton zero run, or of two singleton zero runs. The three cases give respectively \(1\), \(k-1\), and \(\binom{k-1}{2}\) outputs. In the second case a sole length-two one run records the deleted singleton zero run relative to the remaining distinguished zero run; in the third case the unchanged length-\(a\) zero run anchors the one run of length three, or the two one runs of length two. For \(a=3\), deleting two positions in \(Z_0\) leaves an alternating circle; this still lies in a different run-pattern class from the other cases. Distinct singleton-run choices in each case have distinct oriented cyclic run signatures. Their sum is \(1+\binom{k}{2}\).

**(B) Exactly one one deleted.** Delete a zero in \(Z_0\) first. If the deleted one is \(O_0\) or \(O_{k-1}\), the two possibilities coalesce to the same output: one zero run of length \(a\), all other runs singleton. Deleting a singleton zero \(Z_i\) and either neighboring one also gives that same output. This contributes just **one** class.

If the zero comes from \(Z_0\) and the one comes from the interior set \(\{O_1,\ldots,O_{k-2}\}\), the resulting circle has exactly two nonsingleton zero runs of lengths \(a-1\) and \(2\). For \(a\ge4\), the first is strictly larger, anchors the oriented circle, and the \(k-2\) choices are distinct. For \(a=3\), the two runs are both of length two. Swapping which one is treated as the distinguished run identifies the \(k-2\) positions under reversal of the *index of the marked run* (not under reversal of the word), giving \(\lceil(k-2)/2\rceil\) distinct circles. This yields \(H_a(k)\).

In all remaining cases the deleted zero comes from a singleton \(Z_i\) and the deleted one is neither neighboring one. These are \((k-1)(k-2)\) pairs and produce a length-two one run together with a reduction of the number of runs by four. If the deleted one is interior, there are \((k-2)(k-3)\) possible pairs and their outcomes are distinct, because the unchanged unique length-\(a\) zero run records the oriented positions of both the new length-two zero and the length-two one. If it is a boundary one, there are \(2(k-2)\) pairs, but the choices at the two sides of \(Z_0\) correspond in pairs to the same output: a unique zero run of length \(a+1\), with one length-two one run in one of \(k-2\) oriented positions. Thus this last case gives \((k-2)(k-3)+(k-2)=(k-2)^2\) different outputs. Its run count is two less than that of the previous two cases, so there is no uncounted overlap. The total is \(1+H_a(k)+(k-2)^2\).

**(C) Two ones deleted.** First suppose at least one deleted one borders \(Z_0\). All pairs which join \(Z_0\) with both neighboring singleton zeros yield one class with a length-\(a+2\) zero run. The remaining pairs of this type yield a length-\(a+1\) zero run and a second length-two zero run. Identifying the two choices of side of \(Z_0\) gives precisely \(k-3\) classes, indexed by the oriented separation of these two nonsingleton runs. Thus the boundary cases contribute \(k-2\) necklaces.

If both deleted ones are interior, choose them from \(O_1,\ldots,O_{k-2}\). There are \(\binom{k-2}{2}\) choices. If they are not adjacent, the two merged singleton-zero pairs give two runs of length two, each located relative to the length-\(a\) anchor; these signatures are distinct. If they are adjacent, the three newly joined singleton-zero runs form a zero run of length three. When \(a\ge4\), this is distinguished from \(Z_0\), and all choices remain distinct. At \(a=3\), however, the two length-three zero runs are interchangeable under a rotation; the \(k-3\) adjacent interior pairs are identified in reflection pairs of their *distance indices*. Exactly \(\lfloor(k-3)/2\rfloor\) duplications result. They do not collide with the boundary cases because those have a zero run of length at least \(a+1\). The contribution is therefore \(\binom{k-2}{2}-\mathbf1_{\{a=3\}}\lfloor(k-3)/2\rfloor\). Adding the boundary part and using \(k-2+\binom{k-2}{2}=\binom{k-1}{2}\) proves the expression for \(T_2\).

Finally, add the three disjoint \(T_s\). For \(a\ge4\), straightforward algebra gives \(2k^2-5k+5\). For \(a=3\), the loss relative to this is
\[
\left\lfloor\frac{k-2}{2}\right\rfloor+
\left\lfloor\frac{k-3}{2}\right\rfloor=k-3,
\]
so the total is \(2k^2-6k+8\), as claimed. Every counting step is by an exhaustive classification of the effects of two deletions on cyclic run signatures; no asymptotic or computational extrapolation enters the proof.

## Verification

The attached dependency-free Python program `check.py` independently constructs all two-position deletion traces using (i) canonical lexicographically least string rotations and (ii) the canonical cyclic list of letter-and-run-length pairs. It asserts that both encodings give the same three \(T_s\), checks the structural formulas, and checks invariance under a nontrivial source rotation. Its complete finite test domain is \(3\le a\le8\) and \(3\le k\le22\), comprising \(120\) parameter pairs. The script prints `CIRCULAR_TWO_DELETION_PASS` only if all assertions succeed.

For example, the three composition-refined counts at \(k=4\) are \((7,6,3)\) for \(a=3\), summing to \(16\), and \((7,7,3)\) for \(a=4\), summing to \(17\). At \(k=8\) the corresponding counts are \((29,40,19)\), summing to \(88\), and \((29,43,21)\), summing to \(93\).

The checker exhausts each *finite tested case* but does not certify the infinite family. The all-parameter proof is the run-signature argument above.

## Relationship to prior work

Narayanan and Ren introduced circular trace reconstruction, including random circular shifts of deletion traces (first arXiv posting 2020-09-02). Their central results concern trace sample complexity and reconstruction, rather than counts of possible traces after exactly two deletions of the displayed near-alternating family. Bar-Lev, Etzion and Yaakobi (first arXiv posting 2022-06-16) analyze linear deletion spheres and fixed-length Levenshtein balls; they explicitly discuss dependence on runs and alternating segments. Their displayed deletion-sphere definitions count ordinary linear outputs, not circular-output rotation classes; hence their formulas and extremal bounds do not directly evaluate \(T_s(a,k)\). The later work *New Bounds for Circular Trace Reconstruction* (2026) gives general expressions for probabilities of individual circular traces and asymptotic sample complexity, but the inspected result does not evaluate the exact two-deletion support-size spectrum for this family. Such general probability identities can in principle decide support membership, but extracting the closed-form polynomial counts still requires the run-collision classification proved here.

The novelty claim is limited to the explicit exact two-deletion rotation-quotient enumeration and the length-three versus length-four transition above. No new general trace-reconstruction sample-complexity theorem is claimed.

## Limitations

No assertion is made about other source families or arbitrary deletion counts. In particular \(a=2\), small \(k\), longer deletion radii, and linear (noncircular) equivalence have different boundary behavior. The all-parameter conclusion relies on the run-signature proof; the checker tests only bounded parameter values. An equivalent count under different terminology could exist, and no priority claim is made.

## References

1. S. Narayanan and M. Ren, *Circular Trace Reconstruction*, arXiv:2009.01346, first publicly submitted 2020-09-02. https://arxiv.org/abs/2009.01346
2. D. Bar-Lev, T. Etzion and E. Yaakobi, *On the Size of Balls and Anticodes of Small Diameter under the Fixed-Length Levenshtein Metric*, arXiv:2206.07995, first publicly submitted 2022-06-16. https://arxiv.org/abs/2206.07995
3. *New Bounds for Circular Trace Reconstruction*, ITCS 2026, 30, https://drops.dagstuhl.de/storage/00lipics/lipics-vol362-itcs2026/html/LIPIcs.ITCS.2026.30/LIPIcs.ITCS.2026.30.html
