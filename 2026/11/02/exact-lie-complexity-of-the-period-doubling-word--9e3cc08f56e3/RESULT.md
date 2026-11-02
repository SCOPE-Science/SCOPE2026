# Exact Lie complexity of the period-doubling word

## Finding

Let \(\mu\) be the binary length-two morphism \(\mu(0)=01\) and \(\mu(1)=00\), and let \(\mathbf p=\mu^\omega(0)=0100010101000100\cdots\) be its right-infinite fixed point. For a positive integer \(n\), define \(L_{\mathbf p}(n)\) to be the number of cyclic-rotation classes of binary words of length \(n\) **all of whose distinct rotations** occur as contiguous factors of \(\mathbf p\). Then, for every \(n\ge1\),

\[
L_{\mathbf p}(n)=
\begin{cases}
2,&n=2^k\ \text{or}\ n=3\cdot2^k\quad(k\ge0),\\
0,&\text{otherwise}.
\end{cases}
\]

The two classes when \(n=2^k\) are represented by \(\mu^k(0)\) and \(\mu^k(1)\); the two classes when \(n=3\cdot2^k\) are represented by \(\mu^k(000)\) and \(\mu^k(001)\). Distinct words related by rotation count once, while reversal or symbol complementation are not separately identified.

## Assumptions and scope

An occurrence of a finite word is a consecutive block at a nonnegative starting index of the right-infinite fixed point. A *conjugacy class* is the set of cyclic rotations of one length-\(n\) word. A *Lie class* is a conjugacy class contained in the factor language. The morphism acts letterwise on finite words, and \(\mu^0\) is the identity. The statement concerns all positive lengths over the fixed labeled alphabet \(\{0,1\}\).

## Proof

**1. Parity and forbidden blocks.** From \(\mathbf p=\mu(\mathbf p)\) and the definition of \(\mu\), for every \(j\ge0\) one has

\[
p_{2j}=0,\qquad p_{2j+1}=1-p_j.
\]

Thus every \(1\) in \(\mathbf p\) occurs at an odd global index, so \(11\) never occurs. Also \(0000\) never occurs: four consecutive zero positions necessarily include two consecutive odd global positions \(2j+1\) and \(2j+3\), and their vanishing would imply \(p_j=p_{j+1}=1\), contradicting the absence of \(11\). Consequently every finite factor containing two \(1\)'s has those two letters separated by an even number of positions.

**2. Initial Lie classes.** At length one, \(0\) and \(1\) both occur, so \(L_{\mathbf p}(1)=2\). The complete set of length-three factors is

\[
\{000,001,010,100,101\}.
\]

All five occur in the explicit prefix \(\mu^4(0)=0100010101000100\), and no other triple is possible because \(11\) is absent. The fully present rotation classes are exactly \([000]\) and \([001]=\{001,010,100\}\). Hence \(L_{\mathbf p}(3)=2\). At length two, the factor set \(\{00,01,10\}\) gives \(L_{\mathbf p}(2)=2\).

**3. Odd lengths.** Let \(n\ge5\) be odd and suppose every rotation of a length-\(n\) circular word \(w\) occurs in \(\mathbf p\). If \(w\) has at least two ones, choose two ones at cyclic directed separation \(d\). Rotating \(w\) to start at either chosen one produces linear factors in which those two ones have separations \(d\) and \(n-d\), respectively. Both must be even by step 1, although their sum is odd: contradiction. If \(w\) has at most one one, some rotation has at least \(n-1\ge4\) consecutive zeros, contradicting the absence of \(0000\). Therefore \(L_{\mathbf p}(n)=0\) for odd \(n\ge5\).

**4. A bijection at even lengths.** Fix \(m\ge2\). If \([y]\) is a Lie class of length \(m\), its representative \(y\) cannot be entirely ones, since \(11\) is absent; hence \(\mu(y)\) contains at least one one. Every even-position rotation of \(\mu(y)\) equals \(\mu(z)\) for a rotation \(z\) of \(y\), and occurs in \(\mathbf p\) at an even global index whenever \(z\) occurs. Every odd-position rotation of \(\mu(y)\) is the one-position shift of such a block. It also occurs because the letter immediately following any aligned length-\(2m\) block \(\mu(z)\) is \(p_{2(j+m)}=0\). Thus \([\mu(y)]\) is a Lie class of length \(2m\).

Conversely, take a Lie class \([w]\) at length \(2m\). Since \(0000\) is forbidden, \(w\) has at least one one. Since \(w\) is a factor, all its ones occupy the same parity of positions. Rotate so that they are in the odd positions; the resulting representative has a unique expression \(\mu(y)=0(1-y_0)0(1-y_1)\cdots0(1-y_{m-1})\). For each rotation \(z\) of \(y\), the block \(\mu(z)\) is a rotation of \(w\) and so occurs in \(\mathbf p\). Because \(\mu(z)\) contains a one in an odd relative position and every one in \(\mathbf p\) has odd global position, this occurrence must start at an even index. Desubstitution then shows \(z\) itself is a factor of \(\mathbf p\). Therefore \([y]\) is a Lie class.

This map on classes is injective as well: any rotation taking \(\mu(y)\) to another word of the form \(\mu(z)\) must move an even number of positions, since both have a nonempty one-support lying entirely in odd positions. Even rotations correspond precisely to rotations of \(y\). We have proved the class bijection

\[
[y]\longmapsto[\mu(y)],\qquad L_{\mathbf p}(2m)=L_{\mathbf p}(m)\quad(m\ge2).
\]

Together with the directly checked equality \(L_{\mathbf p}(2)=L_{\mathbf p}(1)=2\), this doubling identity holds for every \(m\ge1\).

**5. Classification.** Every positive \(n\) has a unique representation \(n=2^k r\) with \(r\) odd. Repeatedly applying the bijection reduces \(L_{\mathbf p}(n)\) to \(L_{\mathbf p}(r)\). The only odd positive lengths with nonzero values are \(r=1,3\), both with value two. Iterating the same bijection on the explicit base representatives gives exactly the four stated families of representatives. This proves all claims for every length.

## Verification

The standalone Python 3 script `verify.py` uses two independently implemented descriptions of the fixed point: iteration of \(\mu\) and the identity \(p_i=\nu_2(i+1)\bmod2\). It checks equality on the first \(65536\) symbols and computes complete finite factor languages and all rotation classes for every \(1\le n\le192\), including exact equality with the doubling-map images for all even lengths.

The finite factor languages in that computation are *complete*, not sampling approximations. For \(2^{m-1}<n\le2^m\) (and also \(n=1\) with \(m=0\)), every length-\(n\) factor of the infinite fixed point is contained in \(\mu^m(ab)\) for an adjacent letter pair \(ab\) of the fixed point. All three possible pairs \(00,01,10\) occur in \(\mu^4(0)\); hence every such length-\(n\) factor already occurs in the explicit finite word \(\mu^{m+4}(0)\). The script uses this provable coverage bound, rather than assuming a long prefix is exhaustive.

The execution reports `VERIFY_OK`. The infinite-length theorem follows from the parity and desubstitution proof above, **not** from finite computation.

## Relationship to prior work

Bell and Shallit (first public preprint February 7, 2021) introduced Lie complexity, proved an upper bound by adjacent factor-complexity differences, and established automaticity of Lie complexity for automatic words. Their examples explicitly compute the values for the Thue–Morse, ternary Thue–Morse variant, Cantor, Fibonacci and Tribonacci words; they do not provide the above period-doubling formula. The general automaticity theorem predicts a finite automaton but does not specify its output states or supported lengths for this fixed point.

Cassaigne, Fici, Sciortino and Zamboni (2014, revised 2016) studied *cyclic complexity*, which counts classes with **at least one** representative occurring. Their period-doubling example establishes cyclic complexity \(c_{\mathbf p}(2^k)=2\). This is a different count and only a subsequence of lengths; it neither identifies the all-rotations classes at those lengths nor settles the triple-dyadic or zero cases. De Luca and Fici (2022) give exact Lie complexity for Sturmian words, and Li (2022) proves further general inequalities and automaticity results, but neither addresses this period-doubling fixed point.

The specific new conclusion is the all-length formula and unique two-class constructive description under the stronger all-rotations condition, not the automaticity theorem or the earlier cyclic-complexity special case.

## Limitations

This is an exact result for one canonical binary automatic sequence (and any relabeling with the same factor language), not a universal classification for automatic or Toeplitz sequences. The result does not provide a formula for ordinary cyclic complexity at arbitrary lengths. Finite verification covers lengths through \(192\), while the proof covers all positive lengths. No independent scientific audit has been performed. The possibility of an unindexed or differently phrased earlier equivalent is a residual priority risk.

## References

1. J. P. Bell and J. Shallit, *Lie Complexity of Words*, arXiv:2102.03821v1, first posted February 7, 2021. https://arxiv.org/abs/2102.03821
2. J. Cassaigne, G. Fici, M. Sciortino and L. Q. Zamboni, *Cyclic Complexity of Words*, arXiv:1402.5843, first posted February 24, 2014. https://arxiv.org/abs/1402.5843
3. A. De Luca and G. Fici, *On the Lie Complexity of Sturmian Words*, arXiv:2206.00995, first posted June 2, 2022. https://arxiv.org/abs/2206.00995
4. S. Li, *A Note on the Lie Complexity and Beyond*, arXiv:2207.05859, first posted July 12, 2022. https://arxiv.org/abs/2207.05859
