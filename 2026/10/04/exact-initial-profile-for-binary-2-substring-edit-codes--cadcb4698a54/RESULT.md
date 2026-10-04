# Exact initial profile for binary \(2\)-substring-edit codes
## Finding
For the binary at-most-one \(2\)-substring-edit channel, define \(A_2(n)\) to be the largest size of a code \(C\subseteq\{0,1\}^n\) such that no received string can be produced from two distinct codewords by at most one \(2\)-substring edit. The exact initial profile is
\[
(A_2(1),A_2(2),A_2(3),A_2(4),A_2(5),A_2(6),A_2(7),A_2(8))=(1,1,1,1,2,3,5,8).
\]
An attaining length-\(8\) code is
\[
\{11111111,11100000,11001010,10001101,01101001,01010110,00011100,00000011\}.
\]

## Assumptions and scope
A \(2\)-substring edit replaces a contiguous substring \(u\) by a string \(v\), where \(|u|,|v|\le 2\) and at least one of \(u,v\) is nonempty. The empty \(u\) case is a burst insertion and the empty \(v\) case is a burst deletion. The error ball \(D(x)\) used here includes the no-error output because the channel allows at most one edit. The claim is only for the binary alphabet and lengths \(1\le n\le8\); it asserts no formula for larger lengths.

## Proof
For each \(n\), form a graph \(G_n\) with vertex set \(\{0,1\}^n\). Join two words exactly when their at-most-one-edit balls are disjoint. A set of codewords corrects one \(2\)-substring edit if and only if it is a clique of \(G_n\), so \(A_2(n)=\omega(G_n)\).

The supplied verifier constructs every ball in two independent finite ways. The first directly enumerates every removed substring length \(a\in\{0,1,2\}\), every valid start position, and every binary replacement of length at most \(2\). The second enumerates every possible target word of lengths from \(n-2\) through \(n+2\) and tests prefix/suffix consistency with one replacement. Equality of the two ball constructions is checked for every source word.

The verifier then constructs \(G_n\) exactly and runs an exhaustive maximum-clique branch-and-bound search. Its pruning bound greedily colors the current candidate subgraph; because each color class is independent, the number of colors bounds the size of any clique extending the current partial clique. The recursion therefore cannot prune an improving clique. For every \(1\le n\le8\), the returned clique size matches the displayed profile. The explicit length-\(8\) set above is separately checked to have pairwise disjoint balls, supplying the matching lower bound at the largest tested length.

## Verification
Run `python3 verify.py` from the package root. It reconstructs the channel from the definition, checks agreement of the two ball implementations for all \(510\) source words across lengths \(1\) through \(8\), rebuilds all eight compatibility graphs, re-solves their clique numbers, and verifies the explicit length-\(8\) witness. The recorded output in `artifacts/verification_output.txt` begins with `VERIFY_OK profile=1,1,1,1,2,3,5,8`.

## Relationship to prior work
Tang et al. define the same \(k\)-substring-edit channel and its confusability sets, prove relations to burst-deletion channels, and construct binary codes with asymptotically \(2\log n\) redundancy for constant \(k\). Their paper treats asymptotic construction rather than the exact short-blocklength profile above. Li et al. subsequently improve the asymptotic redundancy to nearly \(\log n+k\), again without an exact finite table in the inspected title/abstract/proceedings material. Searches for the exact length-\(8\) value, the full profile, replacement-error aliases, finite tables, and stronger finite statements did not locate a published result implying this profile.

## Limitations
The computation is exhaustive only through length \(8\). The numerical pattern \(2,3,5,8\) over lengths \(5\) through \(8\) is not claimed to continue. Failed literature searches are not a proof of novelty; an unindexed finite table or unpublished computation could still duplicate the values. Independent audit has not been performed.

## References
1. Y. Tang, S. Motamen, H. Lou, K. Whritenour, S. Wang, R. Gabrys, and F. Farnoud, “Correcting a substring edit error of bounded length,” 2023 IEEE International Symposium on Information Theory, pp. 2720–2725, DOI 10.1109/ISIT54713.2023.10206790.
2. Y. Tang et al., “Correcting a Substring Edit Error of Bounded Length,” IEEE Transactions on Communications 73(1), 12–21, DOI 10.1109/TCOMM.2024.3420721.
3. Y. Li, Y. Tang, H. Lou, R. Gabrys, and F. Farnoud, “Asymptotically Optimal Codes Correcting One Substring Edit,” 2024 IEEE International Symposium on Information Theory, pp. 470–475, DOI 10.1109/ISIT57864.2024.10619199.
4. Y. Li, Y. Tang, H. Lou, R. Gabrys, and F. Farnoud, “Optimal Codes Correcting a Substring Edit,” IEEE Transactions on Information Theory 71(7), 5178–5191, DOI 10.1109/TIT.2025.3562730.
