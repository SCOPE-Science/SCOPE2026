# Complete Italian-domination polynomial and low-weight threshold for crown graphs
## Finding
For every integer \(n\ge4\), let the crown graph \(\operatorname{Cr}_n=K_{n,n}-M\) have labelled parts \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\), with edges \(a_ib_j\) if and only if \(i\ne j\). An Italian dominating function is a labeling \(f:V\to\{0,1,2\}\) for which every vertex labeled zero has total neighbor weight at least two. Write \(D_n(z)=\sum_f z^{\sum_v f(v)}\), with the sum over all such functions.

Put \(P(z)=1+z+z^2\), \(R(z)=z+z^2\), and \(T(F)=\sum_{j\ge4}[z^j]F(z)z^j\). Define
\[
\begin{aligned}
H_n&=T(P^n),\\
B_0&=R^n,\\
B_1&=nR^n,\\
B_2&=nRP^{n-1}+\binom n2R^2P^{n-2},\\
B_3&=n(n-1)RP^{n-1}+\binom n3P^n,\\
c_{22}&=n+\binom n2,\\
c_{23}&=n^2(n-1),\\
c_{33}&=\binom n3^2+n(n-1)^2(n-2)+n^2(n-1).
\end{aligned}
\]
Every symbol on the right denotes a polynomial in \(z\), and all exponents and binomial coefficients are ordinary nonnegative integer operations. Then the complete Italian-domination polynomial is
\[
\boxed{D_n(z)=H_n(z)^2+2\sum_{a=0}^{3}z^aT(B_a(z))+c_{22}z^4+2c_{23}z^5+c_{33}z^6.}
\]
In particular, the Italian domination number is \(\gamma_I(\operatorname{Cr}_n)=4\), and its exact minimum-function multiplicity is
\[
\boxed{[z^4]D_n(z)=\begin{cases}12,&n=4,\\n(n+1)/2,&n\ge5.\end{cases}}
\]
All coefficients, including the boundary correction at \(n=4\), are counts of functions on a labelled graph, without quotienting by graph automorphisms.

## Assumptions and scope
Graphs are finite, simple, undirected and labelled. Throughout, \(n\) is an arbitrary integer at least four, \(M=\{a_ib_i:1\le i\le n\}\) is the removed perfect matching, and the sum defining \(D_n\) contains every feasible \(\{0,1,2\}\)-labeling exactly once. Italian domination is also called Roman \(\{2\}\)-domination: a zero is permitted either one neighbor labeled two or at least two neighbors labeled one. It is not perfect Roman domination or an ordinary dominating-set polynomial. A truncation \(T\) removes only monomials of degrees zero through three. Values \(B_a\) depend on \(n\), which is suppressed in the displayed definition for readability.

## Proof
Write \(x_i=f(a_i)\), \(y_i=f(b_i)\), \(X=\sum_i x_i\), and \(Y=\sum_i y_i\). Because \(a_i\) is adjacent to every \(b_j\) except \(b_i\), and conversely, feasibility is *equivalent* to the pair of conditions, for every \(i\),
\[
 x_i=0\Longrightarrow Y-y_i\ge2,\qquad
 y_i=0\Longrightarrow X-x_i\ge2.\tag{1}
\]
We enumerate disjoint regimes according to the exact side totals \((X,Y)\). Each side total lies between zero and \(2n\).

**Both totals at least four.** In (1), subtracting any coordinate removes at most two from the opposite total. All zero vertices are therefore safe. Each part can carry any labeling of weight at least four, producing \(H_n^2\).

**Exactly one total below four.** By symmetry take \(X=a\le3\) and \(Y\ge4\). Every zero in \(A\) is safe. A zero at \(b_i\) requires \(a-x_i\ge2\). When \(a=0\), all \(b_i\) must be positive, giving \(B_0=R^n\). When \(a=1\), there is one selected unit position in \(A\), which has \(n\) choices, and again all \(b_i\) must be positive, giving \(B_1=nR^n\). When \(a=2\), either one coordinate of \(A\) is two, forcing the corresponding \(b_i\) positive, or two coordinates of \(A\) are one, forcing both corresponding \(b_i\) positive. These disjoint possibilities give \(B_2=nRP^{n-1}+\binom n2R^2P^{n-2}\). When \(a=3\), either one coordinate is two and another is one, forcing the \(b_i\) opposite the two to be positive, or three coordinates are one, allowing all \(b_i\) arbitrary. These give \(B_3=n(n-1)RP^{n-1}+\binom n3P^n\). Retaining only \(Y\ge4\) amounts to applying \(T\); multiplying by \(z^a\) restores the weight on \(A\). Reversing the two parts gives exactly the same four terms, disjoint from the first orientation, yielding \(2\sum_{a=0}^3 z^aT(B_a)\).

**Both totals at most three.** Since \(n\ge4\), if \(X\le1\), then every \(b_i\) must be positive by (1), forcing \(Y\ge n\ge4\), a contradiction. Thus \(X,Y\in\{2,3\}\). When a side has total two, condition (1) forces every positive coordinate on that side to have a positive matched coordinate on the opposite side. When a side has total three, it forces every coordinate labeled two to have a positive matched coordinate on the opposite side; coordinates labeled one impose no such condition. We enumerate the four possible pairs.

For \((X,Y)=(2,2)\), the supports coincide and are either one coordinate on each side labeled two (\(n\) possibilities) or two matched positions on each side labeled one (\(\binom n2\) possibilities), giving \(c_{22}=n+\binom n2\).

For \((X,Y)=(2,3)\), write the side of weight two as either a single two or two ones, and the side of weight three as either one two plus one one or three ones. The four intersection-compatible counts are respectively \(n(n-1)\), \(n\binom{n-1}{2}\), \(2\binom n2\), and \(\binom n2(n-2)\). Their sum is \(n^2(n-1)=c_{23}\). Swapping the sides doubles this term.

For \((X,Y)=(3,3)\), both sides have three ones (\(\binom n3^2\) possibilities), exactly one side has a two and a one (\(n(n-1)^2(n-2)\) possibilities total), or both sides have a two and a one. In the last case, fix the ordered two/one indices \((i,j)\) in \(A\); the two index in \(B\) must be \(i\) or \(j\), and the two index in \(A\) must be positive in \(B\). There are exactly \(n\) valid ordered placements in \(B\): \((i,q)\) with \(q\ne i\), or \((j,i)\). Thus this case contributes \(n^2(n-1)\). The total is \(c_{33}\).

The three cases exhaust every nonnegative pair \((X,Y)\) and have no overlap, proving the polynomial identity for all \(n\ge4\). Every term has total weight at least four: for the high-high term at least eight, for a low-high term at least four, and for the low-low terms at least four. Hence \(\gamma_I\ge4\), while \(c_{22}>0\) shows the minimum is four. At weight four, the low-low contribution is \(c_{22}=n(n+1)/2\); the only additional low-high solutions occur when \(n=4\), \(X=0\), \(Y=4\), with all \(b_i=1\), or symmetrically. This gives two extra functions, completing the minimum classification.

## Verification
The included standalone `verify.py` constructs the graph from its deleted matching and independently checks every zero-labeled vertex against its actual neighbors for each of the \(3^{2n}\) labelings at each \(n=3,4,5,6\). For \(n=4,5,6\), it compares every coefficient with the stated formula. An independent dynamic program enumerates all pairs of side totals and tests the original local conditions (1) for each possible paired-coordinate labeling, checking every coefficient at \(n=3,\ldots,10\) and comparing the stated formula at \(n=4,\ldots,10\). The distinct \(n=3\) case is a cross-check only, not part of the theorem. The total number of directly examined labelings is \(597{,}780\). Run `python3 verify.py`. The expected final line is `VERIFY_OK direct_graph_labelings=597780 n=3..6 independent_pair_DP_n=3..10 full_coefficient_matches_n=4..10`. These finite experiments supplement, but do not establish, the all-parameter proof above.

## Relationship to prior work
Shao and Zhao (first publicly submitted 2026-09-09) introduced a systematic study of the complete Italian-domination polynomial on paths, trees, and cycles, including a general deficit formulation and special closed coefficients. The relevant sections, tables, and conclusions of the primary manuscript address those graph families rather than the family of crown graphs with \(n\ge4\). The exceptional \(\operatorname{Cr}_3\cong C_6\) is deliberately excluded because it lies within the cycle results. A related public mathematical record gives an all-weight Roman \(\{2\}\)-domination enumerator on *complete multipartite* graphs. This does not imply the formula here: for \(n\ge3\), a crown graph is not complete multipartite, since \(a_i\) is nonadjacent to \(b_i\) but adjacent to each \(b_j\) for \(j\ne i\). Another record determines minimum *perfect Roman* functions on crown graphs; these obey a stronger rule than Italian domination and constitute only a proper subclass of all Italian functions. Other available crown-graph classifications concern restrained dominating vertex sets, not three-valued functions. The present contribution is the exact all-coefficient formula with a low-side coupling correction, not the pre-existing terminology or a general polynomial evaluation algorithm.

## Limitations
The theorem assumes \(n\ge4\) with one deleted *perfect* matching and labelled vertices. It makes no claim for arbitrary deletions, other bipartite sizes, or other Roman/Italian variants. Existing algorithms can always enumerate labelings by brute force, but that alone is not the closed all-parameter formula proved here. The mathematical literature is not fully indexed; an unlocated stronger result under another name may affect historical priority. Independent mathematical assessment has not been performed.

## References
1. P. Shao and C. Zhao, “Counting Weight-k Italian Dominating Sets on Trees and Cycles,” arXiv:2610.00108v1, submitted 2026-09-09, https://arxiv.org/pdf/2610.00108v1.
2. M. Chellali, T. W. Haynes, S. T. Hedetniemi and A. A. McRae, “Roman {2}-domination,” Discrete Applied Mathematics 204 (2016), 22–28, DOI 10.1016/j.dam.2015.11.013.
3. A published mathematical record, “Weight enumerator of all Roman {2}-dominating functions on complete multipartite graphs” (related prior result, complete multipartite case).
4. A published mathematical record, “Perfect Roman domination of crown graphs” (related prior result, stronger zero-defence condition).
