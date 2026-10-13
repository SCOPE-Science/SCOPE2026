# Exact length-six two-grain codes in the non-overlapping granular channel
## Finding
For binary words of length \(6\) in the non-overlapping granular channel, the exact optimum for correcting up to two grain errors is
\[
M(6,2)=10.
\]
There are exactly \(16\) labeled maximum codes. The intersection of all \(16\) maximum codes is exactly
\[
\{001100,011001,100110,110011\}.
\]
No other length-six word occurs in every maximum code.

## Assumptions and scope
A grain pattern is a set \(E\subseteq\{2,3,4,5,6\}\) with \(|E|\le 2\) and no two consecutive elements. For an original word \(x=(x_1,\ldots,x_6)\), the received word \(\phi_E(x)\) has coordinate \(j\) equal to \(x_{j-1}\) when \(j\in E\), and equal to \(x_j\) otherwise. Thus every replacement uses the original predecessor bit, as in the non-overlapping grain model. The error ball is \(\Phi_2(x)=\{\phi_E(x):E\}\). A code corrects two grain errors when the balls of distinct codewords are disjoint. The result is only for binary length \(6\) and at most two non-overlapping grains.

## Proof
Construct the compatibility graph on all \(64\) binary words of length \(6\), joining two words exactly when their two-grain error balls are disjoint. A two-grain-correcting code is therefore exactly a clique in this graph. The verifier constructs the allowed grain patterns independently in two ways, constructs every error ball independently in two ways, and checks equality of the two constructions word by word. The resulting graph has \(1432\) edges.

An exhaustive Bron--Kerbosch enumeration of maximal cliques has size histogram
\[
4:420,\quad 5:3017,\quad 6:6964,\quad 7:8359,\quad 8:5013,\quad 9:573,\quad 10:16.
\]
Hence no clique has size greater than \(10\), and exactly \(16\) cliques have size \(10\). Independently, an increasing-order clique enumeration counts exactly \(16\) ten-cliques, and a separate branch-and-bound maximum-clique search again returns maximum size \(10\). Direct intersection of the sixteen enumerated maxima gives exactly the four stated common words.

## Verification
Run `python artifacts/verify.py`. It reconstructs the twelve allowed grain patterns, all \(64\) error balls, the compatibility graph, the complete maximal-clique census, an independent maximum-clique search, an independent ten-clique count, and the common-core calculation. The saved replay output begins with `VERIFY_OK` and reports `maximum=10`, `labeled_maxima=16`, `independent_10cliques=16`, and `core=001100,011001,100110,110011`.

## Relationship to prior work
Mazumdar, Barg, and Kashyap introduced the one-dimensional granular recording model in public work from 2010. Kashyap and Zémor later gave nonasymptotic upper bounds for the same non-overlapping model. Their published numerical table lists, for length \(6\) and two grains, an upper bound \(16\) together with a previously known lower bound \(10\). Thus the equality \(M(6,2)=10\) closes that explicit finite gap rather than merely reproducing a listed exact value. The inspected sources do not provide a complete enumeration of length-six optimum codes or the four-word intersection statement.

## Limitations
This is a finite exact result at one parameter pair; it does not establish a formula for other lengths or numbers of grains. Exhaustive computation proves the finite claims only because all \(64\) possible transmitted words and every allowed grain pattern are explicitly enumerated. Literature search cannot exclude an obscure or unindexed prior enumeration, so residual originality risk remains for the census and common-core statement.

## References
1. A. Mazumdar, A. Barg, and N. Kashyap, *Coding for High-Density Recording on a 1-D Granular Magnetic Medium*, arXiv:1012.1895v1 (public 2010-12-08); later IEEE Transactions on Information Theory 57 (2011).
2. N. Kashyap and G. Zémor, *Upper Bounds on the Size of Grain-Correcting Codes*, ISIT 2013. Public full text inspected at `https://ece.iisc.ac.in/~nkashyap/Papers/isit2013_grains_paper.final.pdf`.
