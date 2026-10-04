# The proper power graph of \(C_2^2\times C_3^2\times C_5^2\) has domination number \(11\)

## Finding

For \(G=C_2^2\times C_3^2\times C_5^2\), the domination number of the proper power graph is exactly \(\gamma(\mathcal P^*(G))=11\). This is the smallest-order nilpotent group with three distinct prime divisors whose three Sylow subgroups are all noncyclic, and the value attains the general nilpotent upper bound from the 2025 domination-number theory beyond the two-prime regime determined there exactly.

An explicit dominating set of size \(11\) is given below, and an exact exhaustive search proves that no dominating set of size \(10\) exists.

## Assumptions and scope

Let
\[
G=C_2^2\times C_3^2\times C_5^2.
\]
The proper power graph \(\mathcal P^*(G)\) has vertex set \(G\setminus\{e\}\); two distinct vertices are adjacent exactly when one is a positive power of the other. The exponent of \(G\) is \(30\). Each Sylow subgroup \(C_p^2\) has exactly \(p+1\) order-\(p\) subgroups, so the three line counts are \(3,4,6\). The group has order \(900\), hence \(899\) nonidentity vertices.

## Proof

Every nontrivial cyclic subgroup is obtained uniquely by choosing a nonempty subset of \(\{2,3,5\}\) and one order-\(p\) line for each chosen prime. Conversely, the product of the selected lines is cyclic because their orders are pairwise coprime. Therefore the number of nontrivial cyclic subgroups is
\[
(1+3)(1+4)(1+6)-1=139.
\]

Two nonidentity elements are adjacent precisely when their generated cyclic subgroups are comparable by inclusion. Generators of the same cyclic subgroup have the same closed neighborhood, so domination reduces exactly to the \(139\)-vertex comparability graph of these nontrivial cyclic subgroups.

For the upper bound, choose one distinguished line in each of the three Sylow factors. Select one generator from every other prime-order line, for
\[
(3-1)+(4-1)+(6-1)=10
\]
vertices, and add one generator of the order-\(30\) subgroup obtained from the three distinguished lines. Any cyclic subgroup either contains a selected nondistinguished prime-order line or is contained in the selected distinguished order-\(30\) subgroup. Thus \(11\) vertices dominate.

For the lower bound, `verify.py` builds all \(139\) subgroup types as nonempty partial assignments in coordinate alphabets of sizes \(3,4,6\). It constructs all comparability neighborhoods and performs an exact branch-and-bound decision search for a dominating family of size at most \(10\). Each branch exhausts every possible dominator of a chosen uncovered target. The pruning rule is rigorous: if \(u\) targets remain and a new vertex can cover at most \(m\) of them, then fewer than \(\lceil u/m\rceil\) remaining choices cannot succeed. A state is memoized only after all of its branches fail.

The exhaustive decision returns no dominating family of size \(10\). Therefore
\[
\gamma(\mathcal P^*(G))=11.
\]

## Verification

The standalone standard-library verifier reconstructs the full reduced graph, checks the explicit size-\(11\) witness, and closes the size-\(10\) decision problem. Its output is:

```text
VERIFY_OK
group_order=900
proper_power_vertices=899
cyclic_subgroup_types=139
dominating_witness_size=11
no_dominating_family_size_10=true
branch_nodes=1022864
```

It also cross-checks \((1+3)(1+4)(1+6)-1=139\) subgroup types and \(4\cdot9\cdot25-1=899\) nonidentity elements.

## Relationship to prior work

The finite-group power graph is established in the early power-graph literature. Bera, Dey, Patra, and Sahoo (2025) study domination in proper power graphs. Their general results bound domination by prime-order subgroup counts, and their nilpotent theorem gives a sharper upper bound. Their abstract states exact determination for nilpotent groups whose order has at most two distinct prime divisors.

For the present three-prime group, their nilpotent upper bound specializes to
\[
1+(3-1)+(4-1)+(6-1)=11.
\]
The new content is the matching lower bound. Their direct-product lower bound is phrased in terms of component counts and does not yield \(11\) under the natural two-factor decompositions here. Targeted database and public-web searches using the exact group, order, value \(11\), elementary-abelian Sylow language, and subgroup-count formulations did not locate a prior statement of this equality.

The order \(900=2^2 3^2 5^2\) is minimal for the boundary condition: a noncyclic Sylow \(p\)-subgroup has order at least \(p^2\), and the three smallest distinct primes are \(2,3,5\). Equality gives precisely the group studied here.

## Limitations

The lower bound is a finite exhaustive computation, not a general formula for all products of elementary abelian Sylow subgroups. No claim is made that every three-prime nilpotent group attains the same upper bound. An unindexed or unpublished note could contain the same special case despite the searches performed.

## References

1. P. J. Cameron and S. Ghosh, “The power graph of a finite group,” *Discrete Mathematics* 311 (2011), 1220–1222.
2. P. J. Cameron, “The power graph of a finite group. II,” *Journal of Group Theory*. DOI: 10.1515/JGT.2010.023. Public record dated 2011-01-13.
3. S. Bera, H. K. Dey, K. L. Patra, and B. K. Sahoo, “On the domination number of proper power graphs of finite groups,” *Discrete Mathematics* 348 (2025), Article 114557. DOI: 10.1016/j.disc.2025.114557.
