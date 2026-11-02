# Exact balanced coverage-depth layouts of the binary four-dimensional simplex code

## Finding
Let \(V=\mathbb F_2^4\setminus\{0\}\) and let \(\mathcal P=\{A,B,C\}\) be an unordered partition of \(V\) into three five-element sets. In each synchronous sampling round independently choose one vector uniformly from each of \(A,B,C\), with replacement across rounds. Let \(\tau_{\mathcal P}\) be the first round at which the span of all vectors sampled so far equals \(\mathbb F_2^4\). Then
\[
\min_{\mathcal P}\mathbb E\tau_{\mathcal P}=\frac{7491}{3596}.
\]
There are exactly \(336\) attaining unordered partitions. They are precisely those in which each five-element part is a projective cap (no three distinct vectors in a part satisfy \(u+v=w\)); they comprise a single orbit of \(\operatorname{GL}(4,2)\). An explicit attaining layout, using four-bit binary vectors encoded as integers from \(1\) through \(15\), is
\[
 A=\{1,2,4,8,15\},\quad B=\{3,5,7,10,11\},\quad C=\{6,9,12,13,14\}.
\]
Thus the optimal expected total number of simultaneous physical reads is \(3\mathbb E\tau=22473/3596\) for this fixed three-container model. The result is about balanced partition placement for this fixed simplex code, not about optimizing over all codes or any single-container scheme.

## Assumptions and scope
The binary \([15,4]\) simplex code has the fifteen nonzero vectors of \(\mathbb F_2^4\) as generator columns, each present once. Only partitions into three containers of size five are admissible. Each round produces exactly one uniform independent read from each container, and all three reads count toward the total read cost. Recovery occurs once the cumulative sampled columns have full binary rank four. All codewords and columns are labeled initially, but partitions are identified under permuting the names of the three containers. A five-cap is a five-element subset containing no projective line \(\{u,v,u+v\}\). An orbit under \(\operatorname{GL}(4,2)\) uses invertible linear changes of coordinates acting on all columns; no additional symmetry is presumed.

## Proof
Let \(\mathcal L\) be the lattice of all binary linear subspaces of \(\mathbb F_2^4\). For each \(U\in\mathcal L\), define
\[
 p_U=\prod_{X\in\{A,B,C\}}\frac{|X\cap U|}{5}.
\]
In each round the three observations all lie in \(U\) with probability \(p_U\). By Möbius inversion on the subspace lattice, if \(S_t\) is their accumulated span after \(t\) rounds, then
\[
 \Pr(S_t=\mathbb F_2^4)=\sum_{U\le\mathbb F_2^4}\mu(U,\mathbb F_2^4)\,p_U^t,
\]
where the Möbius coefficient for codimension \(c\) is \((-1)^c2^{\binom c2}\). Every proper subspace has \(p_U<1\); since \(\mathbb E\tau=\sum_{t\ge0}\Pr(\tau>t)\), summing the geometric series gives
\[
 \mathbb E\tau=-\sum_{U<\mathbb F_2^4}\frac{\mu(U,\mathbb F_2^4)}{1-p_U}.
\]
The proper coefficients sum to \(-1\). Lines (one-dimensional vector spaces) and the zero space cannot meet all three disjoint parts, so their \(p_U\) vanish. A two-dimensional subspace contains the three nonzero elements of a projective line and meets all three parts precisely when its line is rainbow (one element from each part); there are \(r\) such lines, each with \(p_U=1/125\). For each of the fifteen projective hyperplanes \(H\), put \(q_H=|A\cap H|\,|B\cap H|\,|C\cap H|\). Since \(|H\cap V|=7\), the only nonzero possibilities are \(q_H\in\{5,8,9,12\}\). Subtracting the constant contributions of all proper subspaces yields the exact objective
\[
 \boxed{\mathbb E\tau=1+\sum_{H}\frac{q_H}{125-q_H}-\frac r{62}.}
\]

It remains to minimize this finite rational expression without assumptions about symmetry of an optimum. Represent each nonzero vector by its four-bit integer in \(\{1,\dots,15\}\). Each hyperplane is \(H_u=\{v\ne0:\operatorname{parity}(u\mathbin{\&}v)=0\}\), indexed by nonzero normal \(u\). Each projective line is \(\{a,b,a\oplus b\}\). To enumerate unordered three-way equal partitions exactly once, select the unique first block containing vector \(1\) by choosing four of the other fourteen vectors, then select the second block containing the smallest remaining vector and choose its other four entries from the remaining nine, and take the last five vectors as the third. This enumerates exactly
\[
 \binom{14}{4}\binom{9}{4}=126126
\]
partitions, with no duplicate or missing partition.

Use the exact common denominator \(L=475427160=\operatorname{lcm}(62,120,117,116,113)\). For a hyperplane product \(q\in\{5,8,9,12\}\), its integer contribution to \(L(\mathbb E\tau-1)\) is \(Lq/(125-q)\), and each rainbow line subtracts \(L/62\). A full enumeration, implemented in the included standalone `verify_exhaustive.py`, finds exactly thirteen rational expectation values; the smallest is \(7491/3596\), attained by exactly \(336\) partitions. For every one of the \(336\), all fifteen hyperplane products equal \(9\), and exactly five lines are rainbow. This gives the attained objective directly:
\[
 1+15\frac9{116}-\frac5{62}=\frac{7491}{3596}.
\]
The same independent enumeration of all \(\binom{15}{5}=3003\) five-element subsets finds exactly \(1008\) projective five-caps; it finds exactly \(336\) three-cap partitions, and the two sets of partitions coincide. Finally, exhaustively applying all \(20160\) invertible four-by-four binary matrices to the displayed witness yields exactly those \(336\) partitions, establishing one symmetry orbit. Each enumerated object and arithmetic computation is fully specified, finite and checked with integer arithmetic, so the exhaustive argument is a proof for this fixed fifteen-column instance, not a numerical estimate or an extrapolation.

## Verification
Run `python3 verify_exhaustive.py` from the same directory to check the entire exact \(126126\)-partition census, the \(1008\) caps, the \(336\) optimizers, the \(20160\)-element linear group and the strict second-best objective. Run `python3 verify_markov.py` to independently compute the witness expectation by exact rational dynamic programming on the \(67\) vector subspaces, using all \(125\) possible round triples at each state. The latter calculation returns \(7491/3596\) without using projective-hyperplane enumeration, Möbius coefficients, or the optimization scoring formula. Both checks use only the Python standard library and were executed against the included files. The recorded outputs are in `CHECKS.txt`.

## Relationship to prior work
Kong, Elishco, Wang and Duman (arXiv:2610.02931v1, October 2, 2026) formulate synchronous distributed coverage depth, derive general exact recovery expressions, and study code layouts, providing bounds for balanced simplex-code distributions. The statement here specializes that model to an exact, nontrivial balanced three-container placement problem at binary rank four, and classifies every minimizing layout by projective geometry. Bertuzzo, Ravagnani and Yaakobi (arXiv:2603.06489, March 6, 2026) treat coverage depth and simplex-code formulas in the single-container setting; a single-container formula cannot by itself select an optimal three-container placement. The separate exact rank-two projective-direction placement classification does not logically imply the present four-dimensional, three-container classification. These comparisons do not establish absolute publication priority.

## Limitations
The optimization is restricted to the fixed binary \([15,4]\) simplex generator multiset, three containers, exactly five columns per container and independent uniform synchronous sampling. The finite proof supplies no universal balanced-placement theorem for other ranks, fields or numbers of containers. Its numerical optimum is for elapsed sampling rounds; simultaneous total reads equal three times that quantity. The relevant full primary preprint text was not independently available for complete section-by-section comparison; the primary arXiv abstract and source-linked summaries were consulted, so a matching uninspected result remains a literature-priority risk. Independent mathematical validation has not been performed.

## References
1. X. Kong, O. Elishco, C. Wang, T. M. Duman, *The Coverage Depth Problem in Distributed DNA Data Storage*, arXiv:2610.02931v1 (first publicly posted October 2, 2026). https://arxiv.org/abs/2610.02931
2. M. Bertuzzo, A. Ravagnani, E. Yaakobi, *The DNA Coverage Depth Problem: Duality, Weight Distributions, and Applications*, arXiv:2603.06489 (March 6, 2026). https://arxiv.org/abs/2603.06489
