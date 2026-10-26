# Padovan enumeration of minimal absent subsequences of alternating binary words

## Finding
For each integer \(k\ge1\), let \(w_k=(01)^k\). A binary word \(u\) is a **minimal absent scattered subsequence** (MAS) of \(w_k\) if \(u\) is not a scattered subsequence of \(w_k\), but deleting any one letter of \(u\) produces a scattered subsequence. Let \(a_k\) be the number of such words. Then
\[
\sum_{k\ge1} a_k z^k=\frac{z(3-z+2z^2)}{1-2z+z^2-z^3}.
\]
In particular \((a_1,a_2,a_3)=(3,5,9)\), and for all \(k\ge4\),
\[
a_k=2a_{k-1}-a_{k-2}+a_{k-3}.
\]
The initial counts are \(3,5,9,16,28,49,86,151,265\). These are the even-indexed subsequence \(a_k=P_{2k+3}\) of the classical Padovan sequence with \(P_0=P_1=P_2=1\) and \(P_j=P_{j-2}+P_{j-3}\) for \(j\ge3\).

By contrast, \(w_k\) has exactly \(k+2\) **shortest absent scattered subsequences** (SAS). Thus already over the binary alphabet the number of all minimal absent subsequences is exponentially larger than the number of shortest absent subsequences for this natural periodic family. The growth constant is the unique real root \(\lambda>1\) of \(\lambda^3-2\lambda^2+\lambda-1=0\), numerically \(\lambda\approx1.75487766625\); precisely \(a_k\sim C\lambda^k\), where \(R=1/\lambda\) and
\[
C=\frac{3-R+2R^2}{2-2R+3R^2}\approx1.67873560259.
\]

## Assumptions and scope
The ambient alphabet is exactly \(\{0,1\}\); all subsequences are **scattered** (indices need not be consecutive). The empty word is a subsequence. Minimality means every proper scattered subsequence of \(u\) occurs, which is equivalent to testing every one-letter deletion. Length and run count refer to \(u\), not to the host. No asymptotics in alphabet size are asserted.

## Proof
**1. Greedy embedding cost.** For any nonempty binary word \(u=u_1\cdots u_L\), write \(r\) for its number of maximal constant runs and put \(s=1\) if \(u_1=1\), otherwise \(s=0\). Its lexicographically earliest (greedy) occurrence in the infinite alternating word \(010101\cdots\) ends at one-indexed position
\[
c(u)=L+s+\#\{j\in\{2,\ldots,L\}:u_j=u_{j-1}\}=2L-r+s.
\]
Indeed, the first letter uses position \(1+s\), and each next letter advances by one position if the bit changes and two if it repeats. Greedy embedding is earliest among all embeddings; hence \(u\) occurs as a scattered subsequence of \(w_k\) exactly when \(c(u)\le2k\).

**2. Deletions.** Suppose \(L\ge2\). Deleting a letter in a singleton *interior* run merges its two neighbouring runs: the length falls by one and the run count by two, so \(c\) does not decrease. Deleting an initial singleton \(0\)-run (if another run remains) reduces length and run count each by one while changing \(s\) from zero to one, so again \(c\) does not decrease. Deleting the sole letter in a singleton *last* run (with at least two runs) decreases \(c\) by one. Every other one-letter deletion decreases \(c\) by two; in particular a singleton first run of ones decreases cost by two, and deletion within any run of length at least two decreases cost by two. This follows directly from the changes in \(L,r,s\) in the displayed formula. Single-letter candidates are present in \(w_k\) for \(k\ge1\), so they are never MAS.

Consequently a MAS has no singleton interior runs, does not begin with a singleton zero run, and has either: **type A**, last run length at least two, for which every deletion decreases cost by two; or **type B**, singleton last run, for which the smallest decrease is one. The converse also holds: such a word is MAS exactly when its own cost exceeds \(2k\) but the cost after every deletion does not. Therefore type A contributes costs \(2k+1\) and \(2k+2\), while type B contributes only cost \(2k+1\).

**3. Weighted run enumeration.** Assign the formal weight \(x^{c(u)}\) to each admissible word. An ordinary noninitial run of length \(\ell\) contributes \(x^{2\ell-1}\). Write \(Q=x^3/(1-x^2)\) for a run of length at least two and \(P=x/(1-x^2)\) for an unconstrained nonempty run. An initial run of ones requires an extra factor \(x\) in the cost, while an initial run of zeros must have length at least two unless it is the only run. Type A with one run contributes \((1+x)Q\); type A with at least two runs contributes \((Q+xP)Q/(1-Q)\), because each interior run has weight \(Q\). Thus
\[
A(x)=(1+x)Q+\frac{(Q+xP)Q}{1-Q}=\frac{x^3(1+x+x^2)}{1-x^2-x^3}.
\]
Type B has at least two runs, an initial factor \(Q+xP\), any number of interior factors \(Q\), and a final singleton factor \(x\). Hence
\[
B(x)=\frac{(Q+xP)x}{1-Q}=\frac{x^3(1+x)}{1-x^2-x^3}.
\]
The bijection between a binary word and its ordered run lengths guarantees that each admissible word is counted once.

By the cost/deletion classification,
\[
a_k=[x^{2k+1}]\bigl(A(x)+B(x)\bigr)+[x^{2k+2}]A(x).
\]
Multiply the two rational functions by \(1-x^2+x^3\). Their common denominator becomes \(1-2x^2+x^4-x^6\). The odd-degree numerator from \(A+B\) gives \(2-z+z^2\), and the even-degree numerator from \(A\) gives \(1+z^2\) when \(z=x^2\), both shifted by one in the coefficient index. Summing yields
\[
\sum_{k\ge1}a_kz^k=\frac{z(3-z+2z^2)}{1-2z+z^2-z^3}.
\]
This also proves the stated recurrence and initial values.

**4. Shortest-absent classification.** Every binary word of length \(k\) has greedy cost at most \(2k\), so \(w_k\) contains every binary word of length \(k\). For a candidate of length \(k+1\), absence is equivalent to \(2(k+1)-r+s>2k\), i.e. \(r<2+s\). If it begins with zero this forces one run, giving \(0^{k+1}\). If it begins with one this forces one or two runs, giving \(1^{k+1}\) and \(1^i0^{k+1-i}\) for each \(1\le i\le k\). They are all absent and all shorter words occur. There are exactly \(k+2\).

**5. Exponential growth and Padovan indexing.** The denominator \(1-2z+z^2-z^3\) has a unique smallest-modulus zero \(R\in(0,1)\), the positive reciprocal of the unique real root \(\lambda>1\) of \(\lambda^3-2\lambda^2+\lambda-1=0\); the two remaining zeros have modulus greater than \(R\). The rational generating function has a simple pole at \(R\), with residue giving the stated positive leading constant \(C\). Thus \(a_k\sim C\lambda^k\). Squaring the plastic constant \(\rho\), the real root of \(\rho^3-\rho-1=0\), yields \(\lambda=\rho^2\); its Padovan recurrence sampled every other index gives the identical order-three recurrence and initial counts, proving \(a_k=P_{2k+3}\).

## Verification
Run `python3 verify.py` in a directory containing the attached standalone Python 3 program. It directly enumerates every binary candidate word of lengths 1 through \(2k+1\), for each \(1\le k\le8\), and independently tests greedy subsequence membership after each single-letter deletion. It checks agreement with the structural classification, the first nine rational-generating-function coefficients, the SAS count, and the recurrence for \(1\le k\le100\). Actual output: `VERIFY_OK hosts=8 candidates= 349504 formula_checks=100 counts= [3, 5, 9, 16, 28, 49, 86, 151, 265]`. The infinite claim is established by the preceding proof, not by exhaustive checking over a finite range.

## Relationship to prior work
Kosche, Koß, Manea and Siemer (first public 2021) introduced general MAS/SAS characterizations and showed in Proposition 3.6 that the quantities can separate exponentially versus polynomially in a construction using an alphabet of at least four symbols. The theorem above demonstrates an explicit **binary** separation for the alternating host, and additionally supplies an exact generating function and growth constant. Adamson and collaborators (first public 2024) give tight bounds for **all absent subsequences of fixed length** as a function of universality index, not a formula for the *minimal* absent subsequences of this host. Manea, Ringleb, Siemer and Winkler (2025) provide general enumeration algorithms, rather than the identified fixed-family count. The numerical Padovan sequence is classical (OEIS A000931); the claim is its MAS interpretation and the simultaneous sharp SAS comparison, not numerical-sequence novelty. Published related research on maximal SAS counts among all binary words does not imply the total MAS count for this specific host.

## Limitations
This theorem concerns only exact alternating binary hosts, not arbitrary binary words or factors (contiguous substrings). It does not characterize hosts maximizing total MAS among words of a given length. Database and literature retrieval can miss unindexed equivalent specializations, particularly implicit consequences of generic algorithms.

## References
1. Maria Kosche, Tore Koß, Florin Manea, Stefan Siemer, *Absent Subsequences in Words*, arXiv:2108.13968 (first public August 31, 2021), especially Theorem 3.1 and Proposition 3.6. https://arxiv.org/abs/2108.13968
2. Duncan Adamson, Pamela Fleischmann, Annika Huch, Florin Manea, Paul Sarnighausen-Cahn, Max Wiedenhöft, *Tight Bounds for the Number of Absent Subsequences*, arXiv:2407.18599 (first public July 26, 2024). https://arxiv.org/abs/2407.18599
3. Florin Manea, Tina Ringleb, Stefan Siemer, Maximilian Winkler, *Efficiently Finding All Minimal and Shortest Absent Subsequences in a String*, arXiv:2504.21471 (first public April 30, 2025; later supporting comparison). https://arxiv.org/abs/2504.21471
4. OEIS A000931, Padovan numbers, https://oeis.org/A000931 .
