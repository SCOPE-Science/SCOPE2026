# Exact finite-blocklength optimum for the triangular binary memory channel

## Finding
For every integer \(n\ge 2\), consider a binary length-\(n\) code in which two distinct words \(x,y\) must have at least one position \(i\in\{1,\ldots,n-1\}\) such that their aligned two-bit blocks \(x_ix_{i+1}\) and \(y_iy_{i+1}\) are different and both belong to \(\{00,01,10\}\). Let \(M_F(n)\) be the largest size of such a code. Then
\[
M_F(2)=3,\qquad M_F(3)=5,\qquad M_F(4)=9,
\]
and, for every integer \(n\ge5\),
\[
M_F(n)=M_F(n-1)+M_F(n-2)+M_F(n-3).
\]
In particular,
\[
\sum_{n\ge 2}M_F(n)z^n=\frac{z^2(3+2z+z^2)}{1-z-z^2-z^3}.
\]
The initial values through length twelve are \(3,5,9,17,31,57,105,193,355,653,1201\). An explicit optimal code is the entire set \(R_n\) of binary length-\(n\) words containing no \(111\), not beginning with \(11\), and not ending with \(11\).

## Assumptions and scope
The input alphabet is exactly \(\{0,1\}\); words have labeled linear (noncyclic) positions, and no restriction on code linearity is imposed. Distinguishability uses the *existence* of an aligned coordinate pair where two different observed pair symbols are adjacent in the triangle graph with vertex set \(\{00,01,10\}\), while \(11\) is isolated. Thus all three distinct pairs among \(00,01,10\) are distinguishable, whereas no pair involving \(11\) is. This is the triangular one-memory channel \(F\) of Cohen, Fachini and Körner. The formula is for finite block length, not merely the exponential growth rate.

## Proof
**1. Reduction to words avoiding \(111\).** Let \(D_n\) be the set of binary length-\(n\) words containing no three consecutive ones. Suppose a codeword \(x\) contains \(111\) in positions \(j,j+1,j+2\). Change its middle one to zero, obtaining \(z\). The only two local blocks of \(x\) changed by this operation were both \(11\), which cannot be the distinguishing side of any channel edge. Consequently, every word distinguishable from \(x\) is also distinguishable from \(z\). Moreover \(x,z\) are nondistinguishable, so \(z\) cannot already belong to the code. The codeword can therefore be replaced without changing cardinality or the pairwise-distinguishability property. Every replacement decreases the total number of ones; iteration places any code into \(D_n\) without changing its size.

**2. Nondistinguishability inside \(D_n\).** Take distinct \(x,y\in D_n\). If they differ at an interior coordinate \(i\in\{2,\ldots,n-1\}\), suppose without loss of generality that \(x_i=0\) and \(y_i=1\). In each adjacent two-bit position, the corresponding block of \(x\) is not \(11\) and differs from that of \(y\). To avoid a distinguishing edge, *both* blocks of \(y\) must therefore equal \(11\). This forces \(y_{i-1}y_iy_{i+1}=111\), a contradiction. Hence two nondistinguishable words in \(D_n\) have identical interior coordinates.

If their interiors agree, a difference at the first position is invisible exactly when the common second bit is one: in that case one leading block is \(11\), while the other is \(01\); if the second bit is zero, the two leading blocks are \(00\) and \(10\), a distinguishing edge. Similarly, a difference at the final position is invisible exactly when the common penultimate bit is one. These statements also hold when both endpoints differ; for \(n=3\) they concern the two distinct, possibly overlapping consecutive-pair positions.

Define \(\pi:D_n\longrightarrow R_n\) by setting the first bit to zero when the second bit equals one, setting the final bit to zero when the penultimate bit equals one, and keeping every other bit unchanged. This map only changes ones to zeros, so its image remains in \(D_n\), and both ends cease to be \(11\). Every \(r\in R_n\) is fixed by \(\pi\). For \(n\ge3\), the preceding argument proves the exact equivalence
\[
\text{the words }x,y\in D_n\text{ are nondistinguishable}
\quad\Longleftrightarrow\quad\pi(x)=\pi(y).
\]
Thus the fibers of \(\pi\) are disjoint confusability cliques, one for every word of \(R_n\). A code contained in \(D_n\) uses at most one word per fiber, while \(R_n\) contains precisely one representative of each fiber and is itself pairwise distinguishable. Therefore \(M_F(n)=|R_n|\) for all \(n\ge3\). At \(n=2\), the three mutually adjacent symbols \(00,01,10\) are an optimal code, also equal to \(R_2\).

**3. Exact count.** Use the four last-pair states in the order \(00,01,10,11\). The allowed extension matrix for avoiding \(111\) is
\[
T=\begin{pmatrix}
1&1&0&0\\
0&0&1&1\\
1&1&0&0\\
0&0&1&0
\end{pmatrix}.
\]
The allowed first and last pairs are all states except \(11\), so, with \(u=(1,1,1,0)\),
\[
|R_n|=uT^{n-2}u^{\mathsf T}\qquad(n\ge2).
\]
Direct multiplication gives the first four values \(3,5,9,17\). The characteristic polynomial of \(T\) is \(\lambda(\lambda^3-\lambda^2-\lambda-1)\). The Cayley–Hamilton identity gives the three-term recurrence for all \(n\ge6\); the already checked value \(17=9+5+3\) establishes it also at \(n=5\). Summation of the recurrence gives the asserted rational generating function. The construction of \(R_n\) and the upper bound in Step 2 prove exact optimality at every length.

## Verification
Two standalone Python programs are included and require only the Python standard library. Run `python3 verify_pairs.py` and `python3 verify_transfer.py`. The first tests the full pairwise channel relation on every \(111\)-avoiding word for lengths \(3\) through \(11\), checks the canonical-fiber characterization, and independently checks the \(111\)-reduction step through length \(8\). The second independently counts admissible boundary-avoiding words by a four-state transfer matrix, checks the recurrence through length \(100\), and matches brute-force enumeration through length \(17\). Both completed successfully. These finite tests supplement rather than replace the all-length symbolic proof.

## Relationship to prior work
Cohen, Fachini and Körner introduced the same triangle \(F\) and proved its Shannon–Markov capacity is the logarithm of the positive growth constant solving \(t^3=t^2+t+1\); their 2014 publicly released manuscript treats asymptotic growth, not the finite-size exact sequence above. Their reduction of \(111\) is the starting point here. The additional structural observation that nondistinguishability becomes an equivalence relation after this reduction produces an exact finite-blocklength packing, rather than only exponential-order bounds. Cao, Cai, Guo and Yeung subsequently studied one-memory channel capacities; their full article was not available for a complete comparison. No claim is made to a new capacity exponent or a complete classification of all optimal codes in the unrestricted space.

## Limitations
The result is specific to the exact three-edge triangle \(F\) with isolated \(11\); it does not automatically extend to other graphs, cyclic block boundaries, larger alphabets, or multiple memory cells. The proof supplies one canonical family of optimal codes, not an enumeration of every optimal code. An equivalent finite-blocklength result might be present in literature not available in full text, notably the 2018 one-memory study; novelty beyond the inspected 2014 manuscript is subject to that bibliographic risk. Independent external validation has not been performed.

## References
1. G. Cohen, E. Fachini and J. Körner, *Zero-error capacity of binary channels with memory*, arXiv:1402.0349, first publicly submitted 2014-02-03, https://arxiv.org/html/1402.0349v2 (Theorem 1 and proof); IEEE Trans. Information Theory 62 (2016), 3–7.
2. Q. Cao, N. Cai, W. Guo and R. W. Yeung, *On Zero-Error Capacity of Binary Channels With One Memory*, IEEE Trans. Information Theory 64 (2018), 6771–6778, DOI:10.1109/TIT.2018.2830362. Abstract/metadata consulted; complete article unavailable for direct comparison.
