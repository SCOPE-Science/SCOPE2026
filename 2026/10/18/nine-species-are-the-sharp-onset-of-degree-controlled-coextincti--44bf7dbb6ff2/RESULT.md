# Nine species are necessary for a variance reversal between connected degree-matched coextinction networks

## Finding

Consider finite, simple, **connected** bipartite networks with positive plant and pollinator guild sizes. Pollinators disappear independently with common probability \(q\in(0,1)\). A plant disappears precisely when all its pollinator neighbors disappear. Two networks are degree-matched when the degree multisets agree separately in the two guilds. Write \(Z_G(q)\) for the number of plants that disappear.

The smallest total order of a **connected degree-matched pair** whose extinction-count variances reverse their strict ordering is nine. A connected pair at this order, with pollinator labels \(a,b,c,d,e\), has plant neighborhoods
\[
 G:\ \{a\},\ \{a,b\},\ \{b,c,d\},\ \{b,c,e\},\qquad
 H:\ \{a\},\ \{b,c\},\ \{a,b,c\},\ \{a,d,e\}.
\]
Both have plant degrees \((1,2,3,3)\) and pollinator degrees \((1,1,2,2,3)\). Their means agree, equaling \(q+q^2+2q^3\), and
\[
\operatorname{Var} Z_G(q)-\operatorname{Var} Z_H(q)=2q^2(1-q)^2(1-2q).
\]
The ordering is strict on either side of \(1/2\) and reverses there. In particular the reversal does not require changing how the network splits into connected components.

## Assumptions and scope

The experiment is independent, uniform, one-sided pollinator loss. All plants are initially present, there is no rewiring or demographic feedback, and the observable counts species rather than abundance or the probability that every plant persists. Guilds are not interchangeable. The novelty at issue is attainment by two connected networks, not the unrestricted threshold or the elementary relation between variance and neighbor overlap.

## Proof

For plant \(i\) with neighbor set \(N_i\) and degree \(d_i\), its extinction indicator has expectation \(q^{d_i}\), and the product of the indicators for \(i,j\) has expectation \(q^{|N_i\cup N_j|}\). Thus with \(h_k\) the number of unordered plant pairs whose joint neighborhood has size \(k\), degree matching gives
\[
\tfrac12(\operatorname{Var}Z_G-\operatorname{Var}Z_H)=F(q)=\sum_k(h_k(G)-h_k(H))q^k.
\]
Indeed the single-plant variances and the products of single-plant expectations agree after matching degrees. For the displayed pair the ordered union-size lists are \((2,4,4,4,4,4)\) and \((3,3,3,3,5,5)\), giving the stated factorization. In \(G\), pollinator \(b\) links the plants with multiple neighbors and \(a\) links the singleton plant to them. In \(H\), \(a\) links three plants and the set \(\{a,b,c\}\) links these to the plant with neighborhood \(\{b,c\}\). Every pollinator lies in one of these neighborhoods; both graphs are connected.

For the lower bound one can use the stronger unrestricted lower bound (with disconnected pairs permitted). Here are its finite checks for completeness. If there are at most two plants, the pair histogram is determined by the degree data. For \(m\) plants and \(n\) pollinators with no isolates, \(F(0)=F(1)=0\). Also, the sum of the pair-union sizes is \((m-1)\sum_i d_i-\sum_a\binom{c_a}{2}\), where \(c_a\) is pollinator degree; hence \(F'(1)=0\). Therefore \(F=q(1-q)^2 Q\), with \(\deg Q\le n-3\) unless \(F=0\). When \(n\le3\) this already precludes reversal. The remaining ordered shapes through eight are listed below. Enumerate all \(m\)-tuples of nonempty \(n\)-bit masks, retain those with all columns used, group by the sorted degrees in each guild, and compare distinct pair-union histograms in lexicographic order. Exact division of their difference by \(q(1-q)^2\) gives these quotient coefficients, in ascending powers:

| Shape | Labeled matrices | Distinct histogram comparisons | Possible nonzero quotients |
|---|---:|---:|---|
| \((3,4)\) | 2161 | 5 | \((0,-1),(-1,-1)\) |
| \((4,4)\) | 41503 | 48 | \((0,-1),(0,-2),(-1,-1),(-1,0),(-1,1),(-2,-2),(-1,-2)\) |
| \((3,5)\) | 16081 | 17 | \((0,0,-1),(0,-1,-1),(-1,-1,-1),(0,-1,0),(0,-1,-2)\) |

These are strictly negative on the open interval, including \(-1+q<0\); swapping the graphs only changes the overall sign. Since the procedure covers all connected graphs among the listed shapes, this also proves the desired connected lower bound.

## Verification

The accompanying unchanged Python 3 certificate `verify_coextinction_variance.py` verifies the exact quotient table and connectivity of both witnesses. It also checks the matrix counts by inclusion–exclusion and computes moments from the full 32-state probability space at rational test rates. The table and witness factorization, not the test rates, establish the claims for every real \(q\in(0,1)\).

## Relationship to other results

*Nine-species threshold for reversed coextinction-richness variance in degree-matched mutualistic networks* (Resultary `877cc9367875`, Finding and Assumptions) establishes the same unrestricted cutoff. Surviving and extinct richness differ by complementation and have identical variance. Its graph B is isomorphic to \(G\) above, while its graph A has two connected components. That result covers the cutoff without a connectivity constraint and gives the same two variance curves, but does not exhibit the two curves in a connected pair. The connected realization \(H\) above preserves the matched degrees and exact variance curve of the disconnected graph A. No priority is inferred from the catalogue dates.

*Eleven pollinators are necessary for a three-plant coextinction …* (Resultary `ba6e6aa4edd2`, Finding) studies the connected three-plant case, not the four-plant witness here. The independent neighbor-loss rule is a static probability version of the removal rule used by Memmott, Waser and Price (2004), DOI `10.1098/rspb.2004.2909`. No claim is made about general plant–pollinator dynamics.
