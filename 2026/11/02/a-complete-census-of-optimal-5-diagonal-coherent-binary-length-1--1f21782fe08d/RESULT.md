# A complete census of optimal \(5\)-diagonal-coherent binary length-\(12\) codes

## Finding

Fix the ordered coordinate split \(\mathbb F_2^{12}=\mathbb F_2^6\oplus\mathbb F_2^6\) and its diagonal \(\Delta_6=\{(u,u):u\in\mathbb F_2^6\}\). Following the intersection bound of Kim [1], a binary linear code \(C\) with \(d(C)\geq5\) is **\(5\)-diagonal-coherent** when \(|C\cap\Delta_6|=2^{k_2(6,3)}=8\), where \(k_2(n,d)\) is the largest possible dimension of a binary length-\(n\) linear code with minimum distance at least \(d\).

**Theorem.** The largest dimension of such a code is \(4\), and the unrestricted binary optimum is also \(\kappa(12,5)=4\). Among the labeled binary dimension-\(4\) subspaces of \(\mathbb F_2^{12}\), exactly \(2160\) are \(5\)-diagonal-coherent. Their complete Hamming-weight enumerators and multiplicities are:

| \(W_C(z)\) | Number of labeled codes | Minimum distance |
|---|---:|---:|
| \(1+4z^5+4z^6+4z^7+3z^8\) | \(1440\) | \(5\) |
| \(1+6z^5+4z^6+3z^8+2z^9\) | \(480\) | \(5\) |
| \(1+12z^6+3z^8\) | \(240\) | \(6\) |

In particular, \(240\) meet the optimal \([12,4,6]\) parameters; all \(2160\) attain the largest dimension compatible with minimum distance at least \(5\). The theorem counts actual subspaces with fixed coordinate labels and fixed diagonal, *not* permutation-equivalence classes.

## Assumptions and scope

Weights are ordinary binary Hamming weights. The distance of a linear code is the minimum weight of a nonzero word. Coordinates of \((a,b)\) are paired between the two fixed six-coordinate blocks. An intersection of size \(8\) is forced to be \(\iota(U)=\{(u,u):u\in U\}\), with \(U\) a binary \([6,3,3]\) code: the intersection preimage has distance at least \(3\), and \(k_2(6,3)=3\). Conversely any dimension-\(4\) code containing \(\iota(U)\) and of distance at least \(5\) has precisely this intersection.

## Proof

**1. The possible diagonal cores.** For a binary \([6,3,3]\) code \(U\), a rank-three parity-check matrix has six distinct nonzero columns in \(\mathbb F_2^3\); conversely any such columns yield this parameter set. The \(7\) choices of omitted nonzero column, \(6!\) orderings, and \(|\mathrm{GL}(3,2)|=168\) equivalent parity-check row bases give exactly \(7\cdot 6!/168=30\) labeled cores. Their common weight enumerator is \(W_U(z)=1+4z^3+3z^4\); the dual has the same weight distribution. Choose a canonical core with parity-check columns in integer binary notation \((1,2,4,3,5,6)\), omitting \(7\).

**2. Classify every extension by a coset.** Put \(D=\iota(U)\). Every dimension-four code containing \(D\) is uniquely \(C=D\cup(x+D)\), where \(x\) represents one of \(2^9-1=511\) nonzero cosets of \(D\). Write \(x=(a,b)\), \(t=a+b\), and \(I=\{i:t_i=0\}\). For every \(u\in U\), coordinate-by-coordinate counting gives the exact identity

\[
\operatorname{wt}\bigl((a,b)+(u,u)\bigr)
=\operatorname{wt}(t)+2\operatorname{wt}\bigl((a+u)|_I\bigr).
\]

For fixed \(t\in\mathbb F_2^6\), there are exactly \(2^{6-3}=8\) distinct cosets, indexed by \(a+U\). Thus \(d(C)\geq5\) exactly when all eight words in \(x+D\) have weight at least \(5\).

**3. Only three cases survive.** The canonical \(U\) has dual weight-three supports \(\{7,25,42,52\}\) as six-bit masks. If \(\operatorname{wt}(t)=6\), every word of \(x+D\) has weight \(6\); all \(8\) cosets qualify. If \(\operatorname{wt}(t)=5\), the one remaining coordinate takes each bit value in exactly half of the words of \(U\); all \(6\cdot8=48\) cosets qualify, with coset enumerator \(4z^5+4z^7\).

For \(\operatorname{wt}(t)=3\), the restriction \(U|_I\) is all of \(\mathbb F_2^3\) unless \(I\) is one of the four dual weight-three supports. On each exceptional \(I\), the restriction is the even-weight binary length-three code; the four cosets with odd parity on \(I\) qualify, each with enumerator \(6z^5+2z^9\). This gives \(4\cdot4=16\) additional cosets.

All other cases fail. For \(\operatorname{wt}(t)=4\), the two-coordinate restriction of \(U\) is surjective, so some extension word has weight \(4\). For \(\operatorname{wt}(t)=2\), every four-coordinate puncture of \(U\) has dimension three and covering radius one, so a word of weight at most \(4\) exists. For \(\operatorname{wt}(t)=1\), every five-coordinate puncture of \(U\) has covering radius one, so a word of weight at most \(3\) exists. For \(t=0\), the six-column parity-check set consists of all nonzero three-bit syndromes except one; the absent syndrome is the sum of two present columns, so \(U\) has covering radius two and some coset word has weight at most \(4\). The puncture assertions are finite: the attached verifier checks all \(15\) four-coordinate and \(6\) five-coordinate projections directly; the four-coordinate assertion also follows from the dual minimum distance \(3\) and the Griesmer bound for length-four dimension-two distance-three codes.

Adding \(W_D(z)=W_U(z^2)=1+4z^6+3z^8\) gives exactly the three displayed weight enumerators. The counts per core are \(48,16,8\); since the core is recovered uniquely as \(C\cap\Delta_6\), codes obtained from distinct cores cannot coincide. Multiplication by the \(30\) labeled cores yields \(1440,480,240\) and total \(2160\).

**4. Dimension optimality without a table lookup.** We exhibit a dimension-four code of distance six by adjoining \(x=(\mathbf1_6,\mathbf0_6)\) to \(D\), which gives coset weight identically six. It remains to exclude binary linear \([12,5,\geq5]\) codes. If such a code existed, adjoining an overall parity coordinate would produce an even \([13,5,\geq6]\) code \(E\). Its dual cannot have a weight-one word: deleting a fixed-zero coordinate would give a \([12,5,\geq6]\) code, violating the Griesmer bound \(13\). Nor can its dual contain a weight-two word: the corresponding two coordinates agree on \(E\), and shortening them to zero would give a \([11,\geq4,\geq6]\) code, violating the Griesmer bound \(12\). Also \(E\) cannot contain a word \(w\) of weight ten: projection onto the three positions outside its support has kernel exactly \(\langle w\rangle\), since any other nonzero word supported inside \(w\) would be complemented by \(w\) to a nonzero word of weight at most four; the projection would have dimension four in a three-dimensional space.

Consequently, apart from zero, \(E\) has only weights \(6,8,12\). Writing their numbers as \(A_6,A_8,A_{12}\), the code size and the vanishing dual weight-one and weight-two coefficients in the first two MacWilliams identities give

\[
A_6+A_8+A_{12}=31,\qquad
13+A_6-3A_8-11A_{12}=0,
\]
\[
78-6A_6-2A_8+54A_{12}=0.
\]

The unique rational solution is \((A_6,A_8,A_{12})=(68/3,7,4/3)\), impossible for integer multiplicities. Thus \(\kappa(12,5)=4\), which is attained by the enumerated coherent codes.

## Verification

The included standalone Python 3 program `verify_diagonal.py` reconstructs the canonical \([6,3,3]\) core from six parity-check columns, enumerates its \(512\) doubled-core cosets, verifies the difference-mask criterion independently, checks every punctured-code covering claim, enumerates all \(30\) labeled cores by simultaneous coordinate permutations, and computes the weight enumerators and distinctness of all \(2160\) output subspaces. It prints `DIAGONAL_D5_VERIFY_OK` upon successful completion. A deterministic digest of the entire sorted labeled-code list is provided in `certificate.json`. The proof of \(\kappa(12,5)=4\) above is symbolic rather than a finite search.

## Relationship to prior work

Kim's October 24, 2026 preprint [1] introduces the diagonal-intersection bound, classifies the \(d\geq3\) extremal situation, and states the higher-distance no-loss problem (Problem 6.30). It gives an existence computation for \(m=7,d=5\), but does not give the \(m=6,d=5\) complete labeled-code census, three full weight enumerators, or the proof that all \(2160\) classified extensions have optimal dimension. The new result resolves this specific finite case and does not assert the general open problem. Standard code-parameter tables address the existence of \([12,4,5]\)-type codes, not their intersection with the designated diagonal or the classification under that constraint. The comparison is of mathematical statements, not merely paper titles.

## Limitations

This is an exact classification for a fixed length, minimum-distance threshold, and fixed pairing of labeled coordinates. It does not classify the \(2160\) codes up to coordinate equivalence, settle higher lengths or fields, or answer Problem 6.30 in general. The independent mathematical and literature-priority audits have not been performed.

## References

[1] Jon-Lark Kim, *Extremal diagonal-coherent binary codes: shortened Hamming cores, deep holes, and the 64 I-Ching hexagrams*, first public October 24, 2026, arXiv:2610.33676, Sections 6.1 and 6.9, particularly Proposition 6.2 and Problem 6.30. https://arxiv.org/abs/2610.33676

[2] Standard Griesmer and MacWilliams identities for binary linear codes; see, e.g., W. C. Huffman and V. Pless, *Fundamentals of Error-Correcting Codes*, Cambridge University Press, 2003.
