# Total perfect codes on prism and Möbius ladders: an individual-code classification

## Finding

Let \(n\ge3\). The prism \(P_n=C_n\square K_2\) and Möbius ladder \(M_{2n}\) have two rows of \(n\) labeled vertices, rungs, consecutive rail edges, and closing rail edges joining the same row for \(P_n\) and opposite rows for \(M_{2n}\). A total perfect code \(D\) is a vertex subset for which \(|N(v)\cap D|=1\) at every vertex, including those in \(D\). The neighborhoods are open.

Encode each column by two bits, giving symbols \(0,1,2,3\) for neither vertex, the first row only, the second row only, and both rows. Every total perfect code is a restriction of one of the following lifted patterns, defined by periodic repetition on the doubly infinite ladder:

- The three cyclic rotations of \((0,0,3,0,0,3)\) distinct as words occur in both families exactly when \(3\mid n\).
- The six cyclic rotations of \((0,1,1,0,2,2)\) occur for prisms exactly when \(6\mid n\) and for Möbius ladders exactly when \(n\equiv3\pmod6\).

The restrictions of permitted patterns are distinct. Thus the exact labeled code counts \((c_P(n),c_M(n))\) are \((9,3)\) for \(n\equiv0\pmod6\), \((3,9)\) for \(n\equiv3\pmod6\), and \((0,0)\) otherwise. Each code has \(2n/3\) vertices. No requirement of extending the code to a coloring or partition is imposed in this classification.

## Proof

Lift the bits \((x_i,y_i)\) from the finite ladder to the doubly infinite ladder using ordinary periodicity for a prism and using a row swap after each shift by \(n\) for a Möbius ladder. This is equivalent to the appropriate seam at both rows, including at \(n=3\). The equations at each lifted column are
\[
x_{i-1}+x_{i+1}+y_i=1,\qquad y_{i-1}+y_{i+1}+x_i=1.
\]
Setting \(s_i=x_i+y_i\) and \(d_i=x_i-y_i\) gives
\[
s_{i-1}+s_i+s_{i+1}=2,\qquad d_{i+1}=d_i-d_{i-1}.
\]
Subtracting consecutive sum equations gives \(s_{i+3}=s_i\); two more applications of the difference recurrence give \(d_{i+3}=-d_i\). Therefore a shift by three swaps rows and a shift by six fixes both rows.

The three entries of one period of \(s\) are a permutation of either \((2,0,0)\) or \((0,1,1)\). In the first case \(d_i=0\) throughout and the pattern has least period three and is fixed by the row swap. In the second case, starting at the zero, the two following \(d_i\) must be equal, both \(+1\) or both \(-1\); after three positions the sign reverses. These are exactly the six rotations of the displayed second word; they have least period six, since the zeros require any period to be divisible by three, while a shift by three changes a nonzero sign. Both displayed words satisfy the neighborhood equations, and these cases exhaust the possibilities.

The ordinary seam fixes a phase under shift by \(n\), whereas the Möbius seam requires shift by \(n\) to equal row swap. The least periods and the effect of shift by three give exactly the stated conditions. The first three columns determine all the lifted bits (alternating with the row-swapped block). Therefore restrictions remain distinct for all \(n\ge3\). Finally, summing the number of selected neighbors over all \(2n\) vertices counts each selected vertex three times, giving the stated code size.

## Prior work and scope

These are efficient open dominating sets, also called \((1,1)\)-regular sets. Kuziak, Peterin and González Yero, [*Efficient open domination in graph products*](https://dmtcs.episciences.org/en/articles/1267/download), Theorem 4.3 and §5.2, characterize existence in general Cartesian prisms and give the divisible-by-three case for cycle prisms. Minyard and Sepanski [arXiv:2410.05422](https://arxiv.org/abs/2410.05422), Theorems 4.2 and 6.1, give 3-balanced coloring existence results; Dejter [arXiv:2503.20055v6](https://arxiv.org/html/2503.20055v6), Theorem 36 and Corollary 37, constructs code partitions for the indicated Möbius ladders. The existence criterion is not a contribution here.

A related [catalogued census of neighborhood 3-balanced colorings](https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-six-periodic-rigidity-of-neighborhood-3-balanced-colorings-on-pr--766f520bafef) counts the unordered partitions into three total perfect codes by dividing the labeled color counts by six. Its color-class projections classify codes that appear in such partitions; an individual code is not required by definition to appear in one. The direct binary recurrence here applies to every individual code. No priority claim is made for the partition census. Counts are not taken modulo graph symmetries.

## Verification

Run `python3 CHECK.py`. The checker formulates total perfect codes as exact covers by open neighborhoods using graph edges, independently of the recurrences. It compares the full code sets with the admissible words for the two graph families at every width from 3 to 15. These finite checks do not replace the general proof.
