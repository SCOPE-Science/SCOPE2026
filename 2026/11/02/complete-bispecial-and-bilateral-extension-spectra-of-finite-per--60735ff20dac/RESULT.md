# Complete bispecial and bilateral-extension spectra of finite period-doubling palindromes

## Finding
Let \(\mu(0)=01\), \(\mu(1)=00\), and let \(Q_k\) be \(\mu^k(0)\) with its final symbol deleted, for every integer \(k\ge2\). A factor \(u\), including the empty word, is *bispecial* when each of \(0u,1u,u0,u1\) occurs in \(Q_k\). Write \(D_k(u)=\{ab\in\{0,1\}^2:aub\text{ occurs in }Q_k\}\).

Set \(V_0=00\) and \(V_{j+1}=\mu(V_j)0\). Then the complete list of bispecial factors is the disjoint union
\[
\mathcal B(Q_k)=\{\varepsilon\}\;\cup\;\{Q_j:1\le j\le k-2\}\;\cup\;\{V_j:0\le j\le k-3\}.
\]
In particular, \(|\mathcal B(Q_k)|=2k-3\). The *entire* two-sided extension spectrum is:

- For \(k=2\), \(D_k(\varepsilon)=\{01,10\}\). For \(k\ge3\), \(D_k(\varepsilon)=\{00,01,10\}\).
- For each \(0\le j\le k-3\), \(D_k(V_j)=\{01,10\}\).
- For each \(1\le j\le k-3\), \(D_k(Q_j)=\{00,01,10,11\}\).
- For \(j=k-2\ge1\), \(D_k(Q_j)=\{00,01,10,11\}\setminus\{bb\}\), where \(b\) is the residue of \(j\) modulo \(2\).

For \(k\ge3\), the bilateral orders (number of two-sided extensions minus three) therefore consist of \(k-2\) weak factors of order \(-1\), \(k-3\) strong factors of order \(+1\), and two ordinary factors of order \(0\). There are exactly \(2k-2\) missing two-sided extension pairs at bispecial factors, counted with their respective inner factors.

## Assumptions and scope
All occurrences are **contiguous**, with boundaries respected in the finite word. The empty factor is included, and every extension must itself be a factor of \(Q_k\). The statement does not assert that every minimal absent word arises from a bispecial inner factor. The binary alphabet and this particular period-doubling substitution are essential to the synchronization argument.

## Proof
First, \(Q_1=0\), and the fact that both images of \(\mu\) start in zero implies
\[
Q_{r+1}=\mu(Q_r)0.
\]
In each \(Q_r\), all letters in odd one-based positions are zero. There are no factors \(11\), \(0000\), or \(1001\): the first is excluded by the fixed zero at each odd position, the second follows inductively since four consecutive zeros would require two adjacent input ones, and the third would place its final one at an odd global position. Also \(Q_r\), for \(r\ge3\), begins and ends in \(010\). Consequently, \(000\), when present, can be preceded and followed only by one; it is not bispecial.

The small factors are checked directly. For \(Q_2=010\), the only bispecial factor is \(\varepsilon\), with \(D_2(\varepsilon)=\{01,10\}\). For \(Q_3=0100010\), the bispecial factors are \(\varepsilon,0,00\) with extension sets \(\{00,01,10\}\), \(\{00,01,10\}\), and \(\{01,10\}\), respectively. For every \(r\ge4\), direct factor inclusion from \(Q_4\) and the three avoidances above give \(D_r(0)=\{00,01,10,11\}\), \(D_r(00)=\{01,10\}\), and \(D_r(\varepsilon)=\{00,01,10\}\).

Now take any bispecial factor \(u\) of \(Q_r\) of length at least three. It cannot be \(000\); hence it contains a one. All occurrences of a factor containing a one have the same starting-position parity: every one of \(Q_r\) lies in an even position. A left-special factor must start at an odd position, since the letter before an even start is always zero. A right-special factor must end at an odd position, since the letter after an even end is always zero. Thus \(u\) starts and ends at odd positions, has odd length, and is uniquely of the form \(\mu(v)0\) for a nonempty factor \(v\) of \(Q_{r-1}\) containing zero.

An occurrence of \(v\) in \(Q_{r-1}\) starting at position \(i\) corresponds exactly to an odd-aligned occurrence of \(\mu(v)0\) in \(Q_r\) starting at position \(2i-1\). The left and right context letters, when present, are complements of the corresponding context letters of \(v\). Boundary positions correspond as well. Therefore the left/right extension sets and the full two-sided extension sets agree under bitwise complement:
\[
D_r(\mu(v)0)=\{\overline a\,\overline b:ab\in D_{r-1}(v)\},
\]
with the analogous formula for unilateral extensions. In particular, \(\mu(v)0\) is bispecial exactly when \(v\) is bispecial. The only bispecial factors excluded by this desubstitution are \(\varepsilon,0,00\), already handled. Hence, for \(r\ge4\),
\[
\mathcal B(Q_r)=\{\varepsilon,00\}\cup\{\mu(v)0:v\in\mathcal B(Q_{r-1})\}.
\]
The base at rank three solves this recurrence, giving precisely the two named families and \(\varepsilon\). Their lengths are \(|Q_j|=2^j-1\) and \(|V_j|=3\cdot2^j-1\), so the union is disjoint and has \(2r-3\) elements.

The displayed extension-set formula likewise propagates the rank-three and rank-four exceptional tables. Complementing both bits preserves \(\{01,10\}\) and the full set; the single missing diagonal at \(Q_1\) in rank three alternates under repeated complements and persists only at the terminal generation \(Q_{r-2}\). This proves the table. Counting the lengths of the extension sets proves the final bilateral-order and missing-pair assertions.

## Verification
Run `python3 checker.py` without dependencies. It constructs \(Q_k\), exhaustively lists all distinct contiguous factors, obtains each actual two-sided extension set, and checks every identity above for ranks \(2\) through \(8\). This is a finite consistency check, not the proof for unbounded rank; the proof is the synchronization induction.

## Relationship to prior work
Frid and Avgustinovich (1999) develop bispecial-factor techniques and characterize bispecial factors and forbidden words for a class of **infinite** DOL words. Allouche, Baake, Cassaigne and Damanik (2003) study palindromic-factor complexity of infinite morphic sequences. Schaeffer and Shallit (2015) provide general logical methods for properties of factors of automatic words. Currie (2023) examines factor and pattern avoidance for the infinite period-doubling word. The present statement instead classifies bispecial factors and their exact bilateral extension sets in the *finite, last-letter-deleted* iterates, including truncation-dependent lost extensions. This distinction is structural; it is not an assertion that infinite-word bispecial factors were previously unknown.

## Limitations
The earlier DOL work has not been fully compared at chapter level because its full text was not accessible; this leaves a historical-priority risk. The result does not claim a full finite minimal-absent-word classification or any assertion about every finite prefix length. Independent mathematical audit has not been performed.

## References
- A. Frid and S. V. Avgustinovich, “On Bispecial Words and Subword Complexity of DOL Sequences”, in *Sequences and their Applications*, 1999, pp. 191–204, DOI: 10.1007/978-1-4471-0551-0_13.
- J.-P. Allouche, M. Baake, J. Cassaigne and D. Damanik, “Palindrome complexity”, *Theoretical Computer Science* 292 (2003), 9–31, DOI: 10.1016/S0304-3975(01)00212-2 (available online 6 December 2002).
- L. Schaeffer and J. Shallit, “Closed, Palindromic, Rich, Privileged, Trapezoidal, and Balanced Words in Automatic Sequences”, arXiv:1508.02074, first submitted 9 August 2015.
- J. D. Currie, “The Analog of Overlap-Freeness for the Period-Doubling Sequence”, *Journal of Integer Sequences* 26 (2023), Article 23.8.2; arXiv:2303.14539.
