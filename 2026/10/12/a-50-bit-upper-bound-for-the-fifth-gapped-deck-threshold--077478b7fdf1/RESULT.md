# A 50-bit upper bound for the fifth gapped-deck threshold
## Finding
For a binary word \(w\) and a binary pattern \(p\), let
\[
\binom{w}{p}_{1}
\]
denote the number of occurrences of \(p\) as a subsequence of \(w\) whose selected positions are pairwise separated by at least one unused position. Following Golm, Nahvi, Gabrys, and Milenkovic, let \(G(k)\) be the least length at which two distinct binary words have equal values of \(\binom{w}{p}_{1}\) for every pattern \(p\) of length at most \(k\).

Then
\[
G(5)\le 50.
\]

An explicit confusable pair is
\[
u=\mathtt{01100110101010011001101001101001100110101010011001}
\]
and
\[
v=\mathtt{01101001100110101010011001100110101010011001101001}.
\]
Thus the published general bound \(G(5)\le122\) can be replaced at the first unresolved parameter by \(G(5)\le50\).

## Assumptions and scope
The gap convention is the one used in the source paper: adjacent selected positions are forbidden, so successive selected indices differ by at least \(2\). Equality is required for every binary pattern of lengths \(1,2,3,4,5\), not merely for patterns of length \(5\).

The result is an upper bound only. It does not assert that \(50\) is the exact value of \(G(5)\).

## Proof
The source paper gives the length-\(24\) pair
\[
x=\mathtt{110011010101001100110100},
\qquad
y=\mathtt{110100110011010101001100}
\]
as an example witnessing the exact value \(G(4)=24\). Define
\[
u=\mathtt0\,x\,y\,\mathtt1,
\qquad
v=\mathtt0\,y\,x\,\mathtt1.
\]
Both words have length \(50\), and they are distinct.

It remains to prove equality of all \(1\)-gapped binomial coefficients through order \(5\). For a prefix of length \(j\), let \(N_j(p)\) be the number of gapped occurrences of a pattern \(p\). If \(p=qb\), where \(b\) is the final bit and \(q\) is nonempty, exact partition according to whether the last position is used gives
\[
N_j(qb)=N_{j-1}(qb)+[w_j=b]\,N_{j-2}(q).
\]
For a one-letter pattern \(b\),
\[
N_j(b)=N_{j-1}(b)+[w_j=b].
\]
These recurrences start from zero counts on the empty prefix and compute every required coefficient with integer arithmetic.

Applying them to the displayed \(u\) and \(v\) gives identical vectors for all
\[
2+4+8+16+32=62
\]
binary patterns of lengths \(1\) through \(5\). The bundled certificate records the common vector. As an independent check, the verifier also enumerates every admissible nonadjacent index tuple directly and obtains the same \(62\) counts. Therefore \(u\) and \(v\) have the same gapped \(5\)-deck, proving \(G(5)\le50\).

## Verification
Run `python3 verify.py` beside `certificate.json`. The program reconstructs the source length-\(24\) pair, verifies its gapped \(4\)-deck equality, constructs the two length-\(50\) words, and checks all \(62\) required pattern counts in two independent ways: by the exact prefix recurrence and by direct enumeration of all nonadjacent index tuples.

For each pattern length \(\ell\), it also checks that the total multiplicity is
\[
\binom{50-\ell+1}{\ell},
\]
the number of \(\ell\)-subsets of positions with no two consecutive. The calculation is finite and exact; no numerical tolerance or extrapolation is used.

## Relationship to prior work
Golm, Nahvi, Gabrys, and Milenkovic introduced \(G(k)\), reported the exact values
\[
G(2)=6,\qquad G(3)=13,\qquad G(4)=24,
\]
and gave a construction implying
\[
G(k)\le4(2^k-1)-2.
\]
At \(k=5\) this is \(122\). Their paper explicitly notes that the general bound is loose already at \(k=4\) and then develops asymptotic improvements, but it gives no sharper finite bound for \(k=5\).

Rigo, Stipulanti, and Whiteland subsequently recast the same equivalence in the language of gapped binomial coefficients and studied complexity functions of infinite sequences. Their full text characterizes the binary \((1,2)\)-equivalence and studies Thue--Morse and Sturmian factors; it does not provide a finite \(G(5)\) collision or a bound of \(50\).

Targeted searches for “gapped k-deck G(5) exact value”, “gapped 5-deck smallest binary collision”, “gapped k-deck exact values 6 13 24”, “2-gapped subsequence reconstruction G_2(5)”, the two explicit length-\(50\) witnesses, and equivalent gapped-binomial terminology did not locate a statement implying this bound.

## Limitations
The lower bound for \(G(5)\) is not improved here, so the exact value remains open. The construction uses a particular published \(G(4)\) pair; it does not establish a general recurrence \(G(k+1)\) from \(G(k)\).

Searches cannot exclude an unindexed computation or unpublished observation of a length-\(50\) or shorter collision.

## References
1. J. Golm, M. Nahvi, R. Gabrys, and O. Milenkovic, “The Gapped \(k\)-Deck Problem,” arXiv:2201.12671, first public version 2022-01-29; IEEE ISIT 2022, pp. 49--54, DOI 10.1109/ISIT50566.2022.9834537.
2. M. Rigo, M. Stipulanti, and M. A. Whiteland, “Gapped Binomial Complexities in Sequences,” IEEE ISIT 2023, pp. 1294--1299, DOI 10.1109/ISIT54713.2023.10206676.
