# Universal low-seat PAV tie spectra on Steiner triple-system ballots, with a six-seat design boundary

## Finding

Let \(v\ge7\) be an admissible Steiner triple-system order, \(v\equiv1,3\pmod6\). Form an approval election with one candidate for each of the \(v\) points and exactly one voter approving each of the system's \(v(v-1)/6\) triples. For any committee \(W\), write \(\tau(W)\) for the number of triples contained entirely in \(W\).

For proportional approval voting (PAV), every committee of cardinality \(k\) has exact score
\[
\operatorname{PAV}(W)=\frac{k(v-1)}2-\frac12\binom{k}{2}+\frac13\tau(W).
\]
Thus PAV winners are precisely the committees maximizing \(\tau(W)\). For \(k=3,4,5\), the **complete score multiplicities**, independent of the Steiner-system isomorphism class, are as follows. In each table row, \(N_j\) is the number of committees having \(\tau(W)=j\); unlisted levels have multiplicity zero.

| Seats | \(N_0\) | \(N_1\) | \(N_2\) |
| --- | ---: | ---: | ---: |
| \(3\) | \(v(v-1)(v-3)/6\) | \(v(v-1)/6\) | \(0\) |
| \(4\) | \(v(v-1)(v-3)(v-6)/24\) | \(v(v-1)(v-3)/6\) | \(0\) |
| \(5\) | \(v(v-1)(v-3)(v-7)(v-9)/120\) | \(v(v-1)(v-3)(v-7)/12\) | \(v(v-1)(v-3)/8\) |

The exact PAV winner counts are \(v(v-1)/6\), \(v(v-1)(v-3)/6\), and \(v(v-1)(v-3)/8\) for \(k=3,4,5\), respectively. The proportion of winning five-seat committees is exactly \(15/((v-2)(v-4))\). For \(v=7\), all five-seat committees tie for victory; for \(v=9\), exactly \(3/7\) do; otherwise the formula applies without qualifications.

**The five-seat universality boundary is sharp in the seat count:** at six seats, two explicit Steiner triple systems on the same \(15\) candidates have distinct PAV winner counts and score distributions. The Bose system given below has exactly \(420\) PAV-winning six-seat committees (all with \(\tau=3\)); the projective system \(\mathrm{PG}(3,2)\) has exactly \(105\) (all with \(\tau=4\)). Their full distributions are
\[
(N_0,N_1,N_2,N_3,N_4)_{\mathrm{Bose}}=(315,2100,2170,420,0),
\]
\[
(N_0,N_1,N_2,N_3,N_4)_{\mathrm{PG}}=(420,1680,2800,0,105).
\]
Both have exactly \(315\) five-seat PAV winners.

The common scoring reduction holds more generally for every Thiele weight function with \(w(0)=0\), with coefficient \(\Delta_3=w(3)-3w(2)+3w(1)\). At fixed committee size, a positive, negative, or zero coefficient makes the maximizing, minimizing, or all \(\tau(W)\) levels winning, respectively; the three-to-five-seat table therefore classifies every such rule's scores and ties. This includes nondecreasing concave weights with each of the three signs.

## Assumptions and scope

A Steiner triple system \((V,\mathcal B)\) has \(|V|=v\), distinct three-point blocks, and each unordered pair of points in exactly one block. There is one, equally weighted, sincere approval ballot \(B\) for each \(B\in\mathcal B\). We examine set-valued optimal Thiele committees, not sequential/greedy variants or a chosen tie-breaker. All formulas apply for every \(v\ge7\) with \(v\equiv1,3\pmod6\) and each such design. The six-seat comparison is restricted to the two specified systems of order \(15\).

## Proof

Each point occurs in \(r=(v-1)/2\) blocks, and there are \(b=v(v-1)/6\) blocks. For \(t\in\{0,1,2,3\}\), Newton interpolation gives
\[
w(t)=w(1)\binom{t}{1}+[w(2)-2w(1)]\binom{t}{2}+[w(3)-3w(2)+3w(1)]\binom{t}{3}.
\]
Summing over ballots \(B\), the sums of \(\binom{|B\cap W|}{1}\), \(\binom{|B\cap W|}{2}\), and \(\binom{|B\cap W|}{3}\) are exactly \(kr\), \(\binom k2\), and \(\tau(W)\): the first follows from point replication, the second from unique coverage of every pair, and the third from the definition. PAV has \((w(1),w(2),w(3))=(1,3/2,11/6)\), whence the claimed scoring equation and positive coefficient \(1/3\).

For three seats, a committee either is one of the \(b\) blocks or contains none. For four seats, at most one block fits: two distinct blocks cannot share two points, and if they share one then their union has five points. Each block belongs to exactly \(v-3\) four-subsets, so \(N_1=b(v-3)\). For five seats, at most two blocks fit: any three distinct blocks have union of at least six points by pairwise intersections of size at most one. Exactly two fit if and only if the five-set is the union of a pair of blocks meeting at one point. Every point belongs to \(r\) blocks, so the number of these five-sets is \(N_2=v\binom r2=v(v-1)(v-3)/8\); the representation by such a block-pair is unique. Double-counting incidences between a five-subset and a block contained in it gives \(N_1+2N_2=b\binom{v-3}{2}\). Subtracting from \(\binom v5\) gives \(N_0\). These arguments prove all rows for every admissible order, including the vanishing cases \(v=7,9\). Dividing \(N_2\) by \(\binom v5\) gives the PAV winner proportion.

For the six-seat boundary, first label fifteen points by pairs \((x,i)\in\mathbb Z_5\times\mathbb Z_3\). The Bose design has the five vertical blocks \(\{(x,0),(x,1),(x,2)\}\) and, for each unordered distinct pair \(\{x,y\}\subseteq\mathbb Z_5\) and \(i\in\mathbb Z_3\), the block \(\{(x,i),(y,i),(3(x+y)\bmod5,i+1\bmod3)\}\). There are \(5+3\binom52=35\) blocks, with each pair of points in exactly one block: same-level distinct pairs determine their unique third point, different-level points with identical first coordinates lie in a vertical block, and other different-level pairs uniquely determine their same-level companion through the invertible equation \(2m=x+y\pmod5\). Second, take the fifteen nonzero vectors in \(\mathbb F_2^4\), with all triples \(\{a,b,a+b\}\) for distinct nonzero vectors \(a,b\); each point pair likewise uniquely determines a block.

The accompanying finite exhaustive certificate computes the induced-block count for all \(\binom{15}{6}=5005\) six-subsets in each explicitly specified design and obtains the two frequency vectors above. It checks all \(\binom{15}{2}=105\) pair incidences independently, so it does not assume the constructions are Steiner systems. A six-point set can contain at most four blocks: each point lies in at most two contained blocks (three through one point would require seven distinct points), so double-counting at most \(6\cdot2\) point-block incidences bounds the number of blocks by four. Thus the computed maximum levels three and four are global within the two systems; by the already proved PAV score identity, their winner counts are \(420\) and \(105\).

## Verification

The standalone program `verify_sts_thiele.py` builds the Bose and projective systems from the definitions, together with the Fano and affine-plane examples of orders \(7\) and \(9\). It checks every point pair belongs to exactly one block, enumerates all three-, four-, five-, and six-subsets in the listed systems, and compares each three-to-five-seat induced-block histogram to the closed formulas. It also computes raw PAV scores by exact rational arithmetic independently of the interpolated expression for every three-to-five-seat committee. The entire certificate is finite; the proof above, rather than extrapolation from tests, establishes the infinite-order formulas.

## Relationship to prior work

Janeczko and Faliszewski, *Ties in Multiwinner Approval Voting* (public 2023-05-02, arXiv:2305.01769), define Thiele/PAV committee scores and establish hardness of counting winning committees in general elections (Sections 2 and 4); their paper does not give the Steiner-design ballot spectrum or the explicit six-seat boundary. Heinlein and Östergård, *Algorithms and complexity for counting configurations in Steiner triple systems* (2022), study classical incidence/configuration enumerations and emphasize the Pasch configuration's role. The point-replication and pair-coverage identities, and the fact that Pasch configurations can distinguish Steiner systems, are classical, not new claims. The contribution here is the exact social-choice interpretation: a complete Thiele/PAV score-and-tie census on block-design ballots through five seats, together with an explicit failure of design-independent PAV winner counts at six seats. Known enumeration techniques may recover the incidence counts, but neither inspected work states or studies this joint voting claim.

## Limitations

This is a structured-election result, not an algorithm for unrestricted multiwinner elections; counting or selecting winners for arbitrary committee sizes can be hard. The finite six-seat certificate establishes properties only of the two fifteen-point designs specified, not all order-fifteen systems. It does not assert that fifteen points are the minimum size for non-universality at six seats, nor that the abstract constituent counting identities are original. Scientific priority beyond the inspected sources and published index is not independently established.

## References

1. Ł. Janeczko and P. Faliszewski, *Ties in Multiwinner Approval Voting*, arXiv:2305.01769, first public 2023-05-02, https://arxiv.org/abs/2305.01769 .
2. D. Heinlein and P. R. J. Östergård, *Algorithms and complexity for counting configurations in Steiner triple systems*, Journal of Combinatorial Designs 30 (2022), 527–546, https://doi.org/10.1002/jcd.21839 .
3. J. I. Kokkala and P. R. J. Östergård, *Sparse Steiner triple systems of order 21*, Journal of Combinatorial Designs 29 (2021), 75–83, https://doi.org/10.1002/jcd.21757 (background on Pasch configurations).
