# Exact weight-three capacities of binary nonadjacent pair decks

## Finding

Let \(n\ge 3\) and let \(\mathcal W_{n,3}\) be all indexed, **linear** binary words of length \(n\) containing exactly three ones. For a word \(x=x_1\cdots x_n\), its **nonadjacent two-deck** consists of the symbol multiplicities and the four ordered multiplicities
\[
G_{ab}(x)=\#\{(i,j):1\le i<j\le n,\ j-i\ge2,\ x_i=a,\ x_j=b\},\qquad a,b\in\{0,1\}.
\]
Put \(K_3(n)=|\{(G_{00}(x),G_{01}(x),G_{10}(x),G_{11}(x)):x\in\mathcal W_{n,3}\}|\). These are also the optimum zero-error code sizes when the only received data are this complete nonadjacent two-deck and the prescribed word composition.

**Theorem.** The initial values are \(K_3(3),\ldots,K_3(7)=1,4,10,17,31\). For every \(n\ge8\),
\[
\boxed{K_3(n)=\begin{cases}
14n-66,&n\text{ odd},\\[2pt]
(27n-130)/2,&n\text{ even}.
\end{cases}}
\]
Moreover, the run-type table in the proof gives **all** attainable profiles, rather than just their number. The onset \(n=8\) is sharp for this two-branch linear expression: at \(n=6,7\) its extrapolations are respectively \(16,32\), whereas the actual capacities are \(17,31\).

In particular, an unrestricted choice of three marker positions has \(\binom n3=\Theta(n^3)\) possibilities, but the nonadjacent pair observation distinguishes only \(\Theta(n)\) of them; its optimal zero-error information is \(\log_2 n+O(1)\) bits rather than \(3\log_2 n+O(1)\) bits.

## Assumptions and scope

Words are indexed and linear, not identified under rotation, reversal or complementation. The two-deck records **multiplicities**, not just the set of observed patterns. A pair is admitted only if at least one coordinate lies strictly between its selected positions. The full composition is known; within \(\mathcal W_{n,3}\) it is fixed. No channel noise or unknown read coordinates beyond the enforced gap is assumed. All formulas count distinct received profiles, not the number of source words and not the number of profiles in an unrestricted-weight source space.

## Proof

Write \(z=n-3\). For \(n\ge8\), \(z\ge5\). Let \(k\) and \(\ell\) be the numbers of maximal runs of ones and zeros, respectively, in the **linear** word. Let \(J=G_{01}\). Of the three possible unordered pairs of one-positions, exactly \(3-k\) are adjacent, so
\[
G_{11}=\binom32-(3-k)=k.
\]
Similarly, \(G_{00}=\binom z2-(z-\ell)\). Since exactly \(\binom{n-1}{2}\) ordered coordinate pairs satisfy the gap condition, \(G_{10}=\binom{n-1}{2}-G_{00}-J-G_{11}\). Hence **two source words have identical observations if and only if they have the same \((k,\ell,J)\)**. The run counts are separately recoverable from the two diagonal coordinates.

There are at most three one-runs, and their lengths form a positive composition of three. Alternating the positive zero- and one-runs gives precisely eight possible run-count pairs. If the zero-runs have lengths \(a_i\), then the number of unrestricted \(01\) subsequences is \(\sum_i c_i a_i\), where \(c_i\) is the number of ones after zero-run \(i\). To obtain \(J\), subtract one for each adjacent \(01\) transition. This leads to the following **exact attainable sets**, where a closed integer interval contains every integer between its endpoints.

| \((k,\ell)\) | Attainable values of \(J\), for \(z\ge5\) | Number |
|---|---|---:|
| \((1,1)\) | \(\{0,3z-1\}\) | \(2\) |
| \((1,2)\) | \(\{3a-1:1\le a\le z-1\}\) | \(z-1\) |
| \((2,1)\) | \(\{z-1,2z-1\}\) | \(2\) |
| \((2,2)\), even \(z\) | \([0,3z-3]\) | \(3z-2\) |
| \((2,2)\), odd \(z\) | \([0,3z-3]\setminus\{z-1,z+1,\ldots,2z-2\}\) | \((5z-5)/2\) |
| \((2,3)\) | \([2,3z-6]\) | \(3z-7\) |
| \((3,2)\) | \([z-1,2z-3]\) | \(z-1\) |
| \((3,3)\) | \([1,3z-6]\) | \(3z-6\) |
| \((3,4)\) | \([3,3z-9]\) | \(3z-11\) |

We now justify every row, including absence of unseen interior gaps.

For \((1,1)\), the only words are \(0^z1^3\) and \(1^30^z\). For \((1,2)\), the words are \(0^a1^30^{z-a}\) with \(1\le a\le z-1\). For \((2,1)\), the words are \(1^u0^z1^v\), where \(\{u,v\}=\{1,2\}\). The indicated formulas follow by direct pair counting.

For \((2,2)\), the two start/end orientations and the two compositions of three ones yield the **union** of these four sets:
\[
[0,z-2],\quad\{1,3,\ldots,2z-3\},\quad
\{z,z+2,\ldots,3z-4\},\quad[2z-1,3z-3].
\]
Indeed, these come respectively from \(1^20^a10^b\), \(10^a1^20^b\), \(0^a1^20^b1\), and \(0^a10^b1^2\), with \(a+b=z\) and \(a,b\ge1\). If \(z\) is even, the middle progressions together with the outer intervals cover the full interval. If \(z\) is odd, exactly the even integers \(z-1,z+1,\ldots,2z-2\) are absent.

For \((2,3)\), the pattern is \(0^a1^u0^b1^v0^c\), where \(\{u,v\}=\{1,2\}\) and \(a,b,c\ge1\) sum to \(z\). On writing \(a=1+x\), \(b=1+y\), its attainable \(J\) values are
\[
S_t=\{2+3x+y,\ 3+3x+2y:x,y\ge0,\ x+y\le t\},\qquad t=z-3.
\]
For \(t=2\), direct substitution gives \(S_2=[2,9]\). If \(S_t=[2,3t+3]\), then \(S_{t+1}\) retains this interval and also contains \(3t+4,3t+5,3t+6\), supplied by the second expression at \((x,y)=(t-1,2),(t,1),(t+1,0)\), respectively. Both expressions are bounded above by \(3t+6\) when \(x+y\le t+1\). Induction establishes \(S_t=[2,3t+3]=[2,3z-6]\) for all \(z\ge5\).

For \((3,2)\), every word is \(10^a10^{z-a}1\), with \(1\le a\le z-1\); it has \(J=z+a-2\). For \((3,3)\), the start-zero orientation \(0^a10^b10^c1\) gives \([z,3z-6]\), and the start-one orientation \(10^a10^b10^c\) gives \([1,2z-5]\). To see their interval filling, put \(a=1+x,b=1+y,c=1+v\), with \(x+y+v=z-3\); the variable part is \(2x+y\), which attains every integer from \(0\) to \(2(z-3)\). The two intervals overlap for \(z\ge5\), yielding \([1,3z-6]\).

For \((3,4)\), the word is \(0^a10^b10^c10^d\), with four positive zero-run lengths summing to \(z\). After subtracting their minimum values, \(J=3+3x+2y+v\), with \(x,y,v\ge0\) and \(x+y+v\le z-4\). Every integer from \(0\) through \(3(z-4)\) has a representation \(3x+2y+v\) within that budget (use quotient and remainder on division by three). Therefore the full interval is \([3,3z-9]\).

The eight run-type pairs are disjoint in observation space because \(k\) and \(\ell\) are recovered from the diagonal counts. Summing their cardinalities gives
\[
K_3(z+3)=\begin{cases}
14z-24,&z\text{ even},\\[2pt]
(27z-49)/2,&z\text{ odd},
\end{cases}
\]
which is exactly the stated formula. For \(3\le n\le7\), enumerating the \(\binom n3\) available source words by the same pair definition gives the displayed five exact values; `VERIFY.py` contains a reproducible, independent enumerator for these finite cases. This completes the proof.

## Verification

Run `python3 VERIFY.py` in the same directory as this document. The script uses only the Python standard library. It independently enumerates every weight-three binary word through length \(80\), computes its deck from a running count of eligible earlier positions, reconstructs the run types, and compares the observed sets with the symbolic table and final formula. It also computes literal nonadjacent pairs independently through length \(14\) to cross-check the optimized accumulator. During preparation, the program completed these checks for \(1{,}663{,}740\) source words through length \(80\); it reported no mismatches. The proof above, not the bounded enumeration, establishes the theorem for all \(n\).

## Relationship to prior work

Golm, Nahvi, Gabrys and Milenkovic introduced the gapped \(k\)-deck reconstruction problem and derived collision bounds for general parameters. Rigo, Stipulanti and Whiteland studied exactly the one-gap binomial relation used here; in particular their Lemma 2.1 characterizes equivalence in terms of ordinary binomial and adjacent-factor equivalence. Their paper focuses on factor languages of infinite words such as Thue–Morse and Sturmian sequences. Neither inspected source states the exact fixed-weight-three spectrum, the eight run-type attainable sets or the parity-dependent all-length capacity. The result is **compatible with**, and partly motivated by, their structural equivalence framework, but its sharp finite-length enumeration requires the separate run-composition and interval arguments above. The ungapped \(k\)-deck counts of Chrisnata and collaborators address a different observation channel, with adjacent pairs included.

## Limitations

The exact formulas apply only to binary linear sources of Hamming weight exactly three and to ordered pairs with separation at least two. They do not enumerate arbitrary-weight or circular sources, larger gap constraints or longer gapped subsequences. Bounded computational checks are not an independent proof of infinite length. Priority relative to unindexed literature remains uncertain; no independent external mathematical audit has been conducted.

## References

1. R. Golm, M. Nahvi, R. Gabrys, and O. Milenkovic, *The Gapped k-Deck Problem*, arXiv:2201.12671 (first public 2022-01-29), https://arxiv.org/abs/2201.12671 .
2. M. Rigo, M. Stipulanti, and M. A. Whiteland, *Gapped Binomial Complexities in Sequences*, ISIT 2023, pp. 1294–1299, DOI 10.1109/ISIT54713.2023.10206676, full text https://orbi.uliege.be/bitstream/2268/302524/1/isit2023.pdf .
3. J. Chrisnata et al., *On the Number of Distinct k-Decks: Enumeration and Bounds*, Advances in Mathematics of Communications, DOI 10.3934/amc.2021032, https://www.aimsciences.org/article/doi/10.3934/amc.2021032 .
