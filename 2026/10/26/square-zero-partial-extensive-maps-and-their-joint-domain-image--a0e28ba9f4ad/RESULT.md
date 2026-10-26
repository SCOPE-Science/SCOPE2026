# Square-zero partial extensive maps and their joint domain-image rank distribution

## Finding

For each integer \(n\ge 1\), let \(X_n=\{1,\ldots,n\}\), and let \(\mathcal{POE}_n\) be the semigroup of partial transformations \(f:D\to X_n\) that preserve the weak order and are extensive: \(x<y\) in \(D\) implies \(f(x)\le f(y)\), and \(f(x)\ge x\). Composition is ordinary partial-map composition and \(0\) is the empty map. Write \(d=|D|\) (domain size, often called width) and \(r=|\operatorname{im}f|\) (image rank).

The number \(Z_{n,d,r}\) of elements satisfying \(f^2=0\), of domain size \(d\) and image rank \(r\), is

\[
Z_{n,d,r}=\frac{n!}{(d+1)!\,r!\,(n-d-r)!}\binom{d-1}{r-1}
\]

for the exact range \(1\le r\le d\), \(d+r\le n\). Additionally \(Z_{n,0,0}=1\); every other triple has count zero. In particular, the domain-size marginal and total are

\[
\sum_r Z_{n,d,r}=\frac1n\binom nd\binom n{d+1}\quad(0\le d<n),\qquad
\sum_{d,r}Z_{n,d,r}=\frac1{n+1}\binom{2n}n.
\]

Thus square-zero elements form a Catalan family with a Narayana distribution by domain size, further refined by the image rank. The largest possible image rank is \(\lfloor n/2\rfloor\). At that rank its multiplicity is \(\frac1{m+1}\binom{2m}m\) when \(n=2m\), and \(\frac{m+1}{m+2}\binom{2m+2}{m+1}\) when \(n=2m+1\).

## Assumptions and scope

The underlying set is a *labeled finite chain*; maps need not be injective and need not have full domain. Rank always means image cardinality, not domain size. The square \(f^2\) is empty precisely when \(D\cap\operatorname{im}f=\varnothing\). This is a statement about nilpotency index at most two; it is not an enumeration of all nilpotent transformations of arbitrary index. The empty transformation contributes exactly once.

## Proof

**Step 1: unique queue encoding.** Fix a square-zero \(f\) and scan \(1,2,\ldots,n\). Record \(+1\) at each point of \(D\), record \(-k\) at each point \(y\in\operatorname{im}f\), where \(k=|f^{-1}(y)|\ge1\), and record \(0\) otherwise. This is well defined because \(D\cap\operatorname{im}f=\varnothing\). All preimages of a given image point are consecutive in the ordered domain, since \(f\) is weakly order-preserving. Extensiveness and disjointness force each source \(x\in D\) to be strictly less than its image. Hence all prefix sums of the encoded word are nonnegative, and its full sum is zero.

Conversely, consider an arbitrary word of length \(n\) with letters \(+1\), \(0\), and negative integers \(-k\) with \(k\ge1\), whose prefix sums are nonnegative and whose total sum is zero. Interpret each \(+1\) as a new source, each \(-k\) as a new sink that receives the \(k\) oldest unassigned sources, and each zero as an unused point. All assigned sources precede their sinks. Blocks assigned to successive sinks are consecutive, so the resulting partial map is weakly order-preserving and extensive, and sources and sinks are disjoint. It is therefore square-zero. Both constructions are inverse, and the counts of \(+1\) and of negative steps are \(d\) and \(r\), respectively.

**Step 2: rooted plane trees.** Reverse the length-\(n\) word, negate each letter, and append one final \(-1\). The new word has length \(n+1\), all letters are at least \(-1\), every proper prefix sum is nonnegative, and its total sum is \(-1\). It is therefore exactly the preorder outdegree-minus-one sequence of a rooted *ordered plane tree* with \(n+1\) vertices. The original \(d\) sources give \(d\) leaves, the final appended letter gives one additional leaf, the original \(r\) sinks give \(r\) branching vertices of outdegree at least two, and the remaining \(n-d-r\) unused positions give unary vertices. This establishes a canonical bijection, including the empty map.

**Step 3: exact count by the cycle lemma.** Set \(u=n-d-r\). For \(d\ge1\), a tree on \(n+1\) vertices in the stated class has \(d+1\) leaves, \(u\) unary vertices, and \(r\) branching vertices. A branching vertex of outdegree \(k+1\) contributes excess \(k\ge1\), and the sum of all such excesses is \(d\). The number of ordered positive \(r\)-tuples with sum \(d\) is \(\binom{d-1}{r-1}\). The number of ways to place the vertex-type and branching-degree data in an arbitrary length-\(n+1\) word is

\[
\frac{(n+1)!}{(d+1)!\,r!\,u!}\binom{d-1}{r-1}.
\]

The cycle lemma for sequences with entries at least \(-1\) and total \(-1\) says exactly one out of the \(n+1\) cyclic starting positions yields the preorder word of a rooted plane tree. Dividing the displayed number by \(n+1\) proves the formula. If \(d=r=0\), the only possibility is a path of unary vertices ending in a leaf, so the empty map contributes one. If \(d<r\) or \(d+r>n\), the stipulated vertex counts are impossible. This proves both sharp boundaries.

**Step 4: Narayana and Catalan marginals.** Let \(H(z,t)\) enumerate rooted plane trees with \(n+1\) vertices (weight \(z^n\)) and with \(d\) leaves other than the final preorder leaf (weight \(t^d\)). By the standard plane-tree edge/leaf decomposition, equivalently the usual Narayana generating function,

\[
H=z(1+H)(1+tH).
\]

Lagrange inversion gives

\[
[z^nt^d]H=\frac1n\binom nd\binom n{d+1}
\]

for \(n\ge1\), which is the domain-size marginal established through the bijection. Evaluating at \(t=1\) produces the Catalan number \(\frac1{n+1}\binom{2n}n\). The image-rank bound follows from \(r\le d\) and \(d+r\le n\); the counts at equality are obtained by inserting \(r=\lfloor n/2\rfloor\) into the exact formula, with one admissible \(d\) for even \(n\) and two for odd \(n\).

## Verification

Run `python3 verify_square_zero_poe.py` with Python 3. This program (a) exhaustively generates all partial weakly increasing extensive maps whose square is zero for each \(1\le n\le10\), independently counts every pair \((d,r)\), and checks the formula; (b) uses an independent queue-state dynamic program to enumerate all valid words and compares their coefficient tables; and (c) checks the exact formula's Narayana marginals and Catalan total through \(n=100\). Expected terminal marker: `VERIFY_OK_SQUARE_ZERO_POE_BIVARIATE_TREE`. Finite checks support, but do not replace, the general combinatorial proof.

## Relationship to prior work

Laradji and Umar (2004) established Catalan/Narayana counts for related order-decreasing order-preserving transformation semigroups and studied partial transformations via Schröder numbers. These are different sets of maps and statistics; the classical Catalan and Narayana sequences are not claimed as new. Dimitrova and Koppitz (2012) treated the semiband \(\mathcal{POE}_n\) itself, including maximal subsemigroups, maximal subsemibands and structural rank, but did not state this joint square-zero domain-size/image-rank formula. Garba (1994) studied nilpotent-generated subsemigroups of the broader partial order-preserving transformation semigroup; that structural work is acknowledged. Laradji and Umar's later lattice-path bijections for partial order-preserving maps are another related framework, but their inspected results do not give this specific joint two-parameter distribution. The asserted contribution is this distribution and its explicit queue-to-plane-tree realization, not general Catalan/Narayana enumeration or standard tree-counting facts.

## Limitations

The result counts elements, not conjugacy classes, and treats square-zero maps only, not elements with arbitrary higher nilpotency index. The algebraic application of the classical tree-enumeration formula is new only insofar as not already covered by earlier equivalent statements; thorough historical-priority verification cannot rule out unindexed equivalences. Prior papers' differently phrased results may require further comparison by a specialist.

## References

1. A. Laradji and A. Umar, “Combinatorial results for semigroups of order-decreasing partial transformations,” *Journal of Integer Sequences* 7 (2004), Article 04.3.8; published 17 October 2004. https://cs.uwaterloo.ca/journals/JIS/VOL7/Umar/um.pdf
2. I. Dimitrova and J. Koppitz, “On the monoid of all partial order-preserving extensive transformations,” *Communications in Algebra* 40 (2012), 1821–1826; published online 15 May 2012. https://doi.org/10.1080/00927872.2011.557813
3. A. Laradji and A. Umar, “Lattice paths and order-preserving partial transformations,” preprint (2013), https://arxiv.org/abs/1304.7574
4. G. U. Garba, “Nilpotents in semigroups of partial order-preserving transformations,” *Proceedings of the Edinburgh Mathematical Society* 37 (1994), 361–377. https://doi.org/10.1017/S001309150001885X
