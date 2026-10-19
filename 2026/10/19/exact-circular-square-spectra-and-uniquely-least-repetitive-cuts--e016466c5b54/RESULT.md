# Exact circular-square spectra and uniquely least-repetitive cuts of Thue–Morse blocks

## Finding

Let \(\mu(0)=01\), \(\mu(1)=10\), and \(T_m=\mu^m(0)\), with \(m\ge2\) and \(N=2^m\). A *circular square occurrence* of half-length \(h\) is a pair \((i,h)\), where \(0\le i<N\), \(1\le h\le N/2\), and the \(2h\) cyclic letters beginning at \(i\) form \(XX\) for a word \(X\) of length \(h\). Different starting positions or half-lengths give different occurrences. Let \(Q_m(h)\) count these pairs of half-length \(h\).

The entire length-resolved spectrum is
\[
Q_m(2^k)=\frac{2^{m-k}+2(-1)^{m-k}}3\quad(0\le k\le m-2),
\]
\[
Q_m(3\cdot2^k)=\frac{2^{m-k}-16(-1)^{m-k}}{12}\quad(0\le k\le m-3),
\]
and \(Q_m(h)=0\) for every other positive integer \(h\). In particular the number of all circular square occurrences and the sum of their half-lengths are, respectively,
\[
S_m=\frac{5\cdot2^m-6-2(-1)^m}{6},\qquad
H_m=\frac{2^m(21m-14)-40(-1)^m}{36}.
\]

For each cut \(c\in\{0,\ldots,N-1\}\), let \(L_m(c)\) be the number of ordinary (nonwrapping) square occurrences in the linear rotation \(T_m[c\ldots N-1]T_m[0\ldots c-1]\), with total square length at most \(N\). Then **exactly two cuts minimize this number**, namely \(c=0\) and \(c=N/2\). Their common minimum is \(S_m-R_m\), where
\[
R_m=\begin{cases}\frac{3m}{2}-2,&m\text{ even},\\[2pt]\frac{3(m-1)}{2},&m\text{ odd}.\end{cases}
\]
Moreover the exact mean over all cuts is
\[
\frac1N\sum_{c=0}^{N-1}L_m(c)
=\frac{(N+1)S_m-2H_m}{N}.
\]
Thus the canonical prefix and its complementary half-shift are the unique rotations with the smallest number of square occurrences; the explicit circular spectrum also determines the average under a uniformly chosen cut.

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\), with the usual Thue–Morse substitution, and cuts are indexed from zero. The two half-shift rotations are distinct (the latter is the bitwise complement of the former). Only squares whose entire length does not exceed the circle length are counted; a circular factor may wrap once. Ordinary linear squares in a cut are counted by occurrence, not by distinct content. No assertion is made for arbitrary factors of the infinite word or for arbitrary binary cycles.

## Proof

**A. Desubstitution and the circular square spectrum.** The infinite Thue–Morse word contains `00`, and hence its image under \(\mu^m\), namely \(T_mT_m\), as a contiguous factor aligned at a multiple of \(2^m\). Consequently every square of length at most \(N\) in the circle occurs in the infinite word. The classical Pansiot–Brlek classification (as restated and proved by reference in Brown–Rampersad–Shallit–Vasiga, Theorem 4.1) says its square roots have length \(2^k\) or \(3\cdot2^k\). The aligned-occurrence lemma of that article (Lemma 4.2) further says every square of either type with \(k\ge1\) begins at a multiple of \(2^k\) in the infinite word. Because our enclosing block is aligned at a multiple of \(2^m\), every cyclic square with even half-length starts at an even position of \(T_m=\mu(T_{m-1})\). Its inverse image is a cyclic square with half the half-length in \(T_{m-1}\), and conversely. This is a bijection even for squares touching the chosen boundary.

It remains to count the two primitive odd half-lengths, one and three. Write \(V_j\) for the number of cyclic transitions between unlike neighboring symbols of \(T_j\), defining \(T_0=0\) and \(V_0=0\). Within each image \(\mu(a)=a\overline a\) there is one transition; between neighboring images there is a transition exactly when the two source letters agree. Thus \(V_j=2^j-V_{j-1}\), yielding
\[
V_j=\frac{2^{j+1}-2(-1)^j}{3}.
\]
An identical adjacent pair in \(T_m\) starts at an odd index and occurs precisely across a transition in cyclic \(T_{m-1}\). Hence \(Q_m(1)=V_{m-1}\).

A six-letter square of half-length three is either `010010` or `101101`. Neither can begin at an even image boundary (direct substitution gives contradictory middle bits). At an odd index its inverse image is, respectively, `1100` or `0011` in cyclic \(T_{m-1}\). Each of those four-letter words starts at an odd image position and is equivalent to an alternating three-letter word, `010` or `101`, in cyclic \(T_{m-2}\). Let \(A_j\) count cyclic alternating triples in \(T_j\). Each equal adjacent pair in \(T_{j-1}\) gives precisely two alternating triples in \(T_j\), so
\[
A_j=2(2^{j-1}-V_{j-1})=\frac{2^j-4(-1)^j}{3}.
\]
It follows that \(Q_m(3)=A_{m-2}\). Applying the desubstitution bijection repeatedly gives the two stated arrays \(Q_m(h)\). Summing counts and their half-lengths gives \(S_m\) and \(H_m\) by finite geometric sums.

**B. A fixed finite local crossing lemma.** Given a cyclic square \((i,h)\), say it *crosses cut* \(c\) precisely when \(0<(c-i)\bmod N<2h\). Let \(X_m(c)\) count these crossed squares. Then \(L_m(c)=S_m-X_m(c)\). Group the square occurrences by adjacent dyadic levels of half-length: level-pair \(k,k+1\), with \(k\) even, comprises half-lengths \(2^k,3\cdot2^k,2^{k+1},3\cdot2^{k+1}\) whenever permitted by the length bound.

First consider the unscaled group \(h\in\{1,2,3,6\}\) in cyclic \(T_q\). Let \(G_q(j)\) count its squares crossing cut \(j\) and \(D_q(j)\) its squares starting at \(j\). For every \(q\ge5\), the exact finite local lemma is
\[
G_q(j)\le3,\qquad G_q(j)+D_q(j)\le3,\qquad
G_q(j)=3\ \Longleftrightarrow\ 16\mid j.
\]
Here divisibility is on ordinary cut indices \(0\le j<2^q\). To verify this *for all* \(q\), partition \(T_q=\mu^4(T_{q-4})\) into 16-letter images. The truth of these three local assertions at an offset \(r\in\{0,\ldots,15\}\) within an image depends only on the preceding, current, and following source letters: the longest contributing square has length 12 and crosses a cut only if its start lies in the preceding 11 positions. Circular Thue–Morse source triples are exactly among `001`, `010`, `011`, `100`, `101`, `110` (never `000` or `111`, since the doubled finite block occurs in the overlap-free infinite word). Direct substitution of these six triples under \(\mu^4\) gives a fixed \(6\times16\) case check: in every row the crossing count at \(r=0\) is three; at every other offset it is at most two; and crossing count plus starts-at-cut count never exceeds three. The 96 exhaustive cases are reproduced by the standalone checker. For \(q=3,4\), direct inspection of the length-eight and length-sixteen words yields \(G_q\le3\), \(G_q+D_q\le3\), and \(G_q(j)=3\) exactly at the two positions \(0,2^{q-1}\). At \(q=2\), the sole permitted type is \(h=1\); there are exactly two squares and at most one can cross any cut, with equality at \(0,2\).

**C. Dyadic group bounds and unique maximizing cuts.** Desubstitution maps all squares at two scales \(k,k+1\), for even \(k\), to the primitive two-scale group in \(T_{m-k}\). If a cut has the form \(c=2^k j+r\), \(0\le r<2^k\), the number from this group crossing it is \(G_{m-k}(j)\) when \(r=0\), and \(G_{m-k}(j)+D_{m-k}(j)\) when \(r>0\). Thus each full level-pair contributes at most three crossed squares. For odd \(m\), there are \((m-1)/2\) level-pairs, and for even \(m\), \((m-2)/2\) level-pairs and a single top dyadic scale with at most one crossed square. Therefore \(X_m(c)\le R_m\) for every cut.

The cuts \(c=0,N/2\) attain every group bound, hence attain \(R_m\). They are the only cuts doing so: at the lowest level-pair the equality positions for \(m\ge5\) are multiples of \(16\). Assuming all preceding lower pairs are maximal forces divisibility by \(2^{k+2}\) before examining the pair at even level \(k\); its equality criterion forces divisibility by \(2^{k+4}\) as long as \(m-k\ge5\). At the last pair, \(m-k=3\) or \(4\), the checked small-word equality criterion forces divisibility by \(2^{m-1}\). The remaining positions modulo \(N\) are only \(0,N/2\). The cases \(m=2,3,4\) follow directly from the small-word checks and, for even \(m\), the unique last scale. This proves the claimed exact minimum and uniqueness.

**D. Average over cuts.** A particular circular square of length \(2h\le N\) survives exactly \(N-2h+1\) of the \(N\) possible cuts. Double counting all pairs (square, preserving cut) yields the displayed exact mean \(((N+1)S_m-2H_m)/N\).

## Verification

Running `python verify.py` from this package recomputes all six-by-sixteen fixed local configurations, all small boundary cases, full independent square spectra and rotation statistics for every level \(2\le m\le10\), and the predicted counts at larger levels through \(m=15\). Its checked successful output is:

`VERIFY_OK local_6x16_cases=96 full_spectrum_levels=9 cyclic_square_occurrences=1694 cut_profiles=2044 larger_period_checks=115`

The standalone finite case analysis justifies the universal local lemma because each possible neighborhood reduces to one of the six length-three source factors at one of sixteen offsets. Experimental agreement at larger word lengths is corroboration, not a substitute for the induction.

## Relationship to prior work

Pansiot and Brlek's classification of all square *types* in the infinite Thue–Morse word, and Brown, Rampersad, Shallit and Vasiga's exact location and \(2\)-regularity results, are established prior work and are used explicitly in Part A. Their full positional framework makes the present counting problem tractable but does not directly supply the circular dyadic multiplicities, the all-cut mean, or the sharp two-cut minimization. The new comparison is about aggregated circular occurrence counts and an extremal assertion over all rotations, not about new possible primitive square roots.

The circular power-avoidance work of Aberkane and Currie treats the existence of suitably avoiding factors of the infinite Thue–Morse word; it is not a classification of the rotations of the particular prefix blocks \(T_m\). The earlier paper's full text was not obtained here, so possible historical overlap is a residual risk, rather than a proved negative.

## Limitations

The formulas apply only to dyadic Thue–Morse prefix blocks. The proof relies on the classical square-type theorem, not an independent reproving of that theorem. The local case table is finite and exhaustively reproduced by accompanying standard-library Python; the global conclusion uses a separate mathematical induction. No independent expert audit or priority certification has been performed. A differently phrased earlier rotational extremal theorem could exist outside the inspected material.

## References

- S. Brown, N. Rampersad, J. Shallit, T. Vasiga, *Squares and overlaps in the Thue–Morse sequence and some variants*, RAIRO Theoretical Informatics and Applications 40 (2006), 473–484. DOI: `10.1051/ita:2006030`. Public full text: `https://www.numdam.org/item/10.1051/ita:2006030.pdf`. See particularly Theorem 4.1, Lemma 4.2, Theorems 4.3 and 4.5.
- A. Aberkane and J. D. Currie, *The Thue–Morse word contains circular power free words of every length*, Theoretical Computer Science 332 (2005), 573–581. DOI: `10.1016/j.tcs.2004.12.024`. Accessible description/abstract only.
