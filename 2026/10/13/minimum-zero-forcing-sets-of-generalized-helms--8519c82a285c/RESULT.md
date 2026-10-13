# Minimum zero forcing sets of generalized helms
## Finding
For integers \(m\ge 3\) and \(s\ge 2\), let \(H(m,s)\) be the generalized helm with center \(v_0\), cycle-spoke vertices \(v_1,\ldots,v_m\), and \(s\) pendant leaves at each spoke. Every minimum ordinary zero forcing set has size
\[
Z(H(m,s))=m(s-1)+1
\]
and is exactly one of the following two types.

1. **Center type.** The center \(v_0\) is selected, no spoke is selected, and exactly \(s-1\) leaves are selected from each pendant bundle.
2. **Saturated-bundle type.** For one index \(k\), every leaf in the \(k\)-th pendant bundle is selected, exactly \(s-1\) leaves are selected from every other bundle, and neither the center nor any spoke is selected.

Consequently the number of minimum zero forcing sets is
\[
z(H(m,s);Z(H(m,s)))=s^m+m s^{{m-1}}=s^{{m-1}}(s+m).
\]
Moreover every center-type minimum set has propagation time \(2\), every saturated-bundle minimum set has propagation time \(3\), and therefore the efficient minimum zero forcing sets are exactly the \(s^m\) center-type sets.

## Assumptions and scope
The graph is finite, simple, and undirected. Its vertex set is
\[
\{{v_0,v_1,\ldots,v_m\}}\cup\bigcup_{{i=1}}^m P_i,
\qquad P_i=\{{p_{{i,1}},\ldots,p_{{i,s}}\}}.
\]
The vertices \(v_1,\ldots,v_m\) form a cycle, \(v_0\) is adjacent to every \(v_i\), and every vertex of \(P_i\) is adjacent only to \(v_i\). A blue vertex may force its unique white neighbor. Propagation time is measured in parallel time steps, with every currently legal force available at a step applied simultaneously. The statement is restricted to \(m\ge3\) and \(s\ge2\); the traditional one-leaf helm \(s=1\) has different behavior.

## Proof
Write \(B\) for an initial blue set. First, every zero forcing set contains at least \(s-1\) leaves of every bundle \(P_i\). Indeed, if two leaves of one bundle remain white initially, their only possible forcing vertex is the common neighbor \(v_i\). As long as both are white, \(v_i\) has at least two white neighbors, so neither can ever be the unique white neighbor of a blue vertex. Thus
\[
|B\cap P_i|\ge s-1
\]
for every \(i\).

The mandatory leaf selections account for at least \(m(s-1)\) blue vertices. Equality cannot be zero forcing: if exactly \(s-1\) leaves are blue in every bundle and nothing else is blue, the selected leaves force all spokes, after which the center and one leaf in every bundle are white. Every spoke then has exactly two white neighbors, its omitted leaf and the center, so the process stalls. Hence
\[
Z(H(m,s))\ge m(s-1)+1.
\]

Both displayed types attain this bound. For a center-type set, one selected leaf in each bundle forces its spoke in the first step, and then every spoke forces the unique omitted leaf in its own bundle in the second step. For a saturated-bundle set with saturated bundle \(P_k\), the selected leaves first force every spoke. The spoke \(v_k\) then has the center as its unique white neighbor and forces \(v_0\). Once the center is blue, each other spoke has exactly its omitted pendant leaf white and forces it. Thus center type takes two steps and saturated-bundle type takes three.

It remains to show that no other minimum set exists. At minimum size, the lower bound \(|B\cap P_i|\ge s-1\) leaves exactly one selected vertex beyond the mandatory \(m(s-1)\) leaves. If that extra vertex is the center, the set is center type. If it is a pendant leaf, it saturates exactly one bundle and gives saturated-bundle type. If it is a spoke, then after all available pendant-to-spoke forces, the center and exactly one leaf of every bundle remain white. Each blue spoke has the center and its own omitted leaf as two white neighbors, so no spoke can force and the process stalls. Therefore a spoke cannot be the extra vertex of a minimum zero forcing set.

For counting, each center-type set is obtained by choosing the one omitted leaf independently in each of the \(m\) bundles, giving \(s^m\) sets. For saturated-bundle type, choose the saturated bundle in \(m\) ways and then choose the omitted leaf independently in the remaining \(m-1\) bundles, giving \(m s^{{m-1}}\) sets. These families are disjoint, yielding the stated total.

Finally, center type cannot finish in one step because every omitted leaf is at distance two from the initially blue pendant leaves through an initially white spoke. Saturated-bundle type cannot finish in two steps because the center is initially white and cannot be forced before the spokes become blue; only after the center becomes blue can the omitted leaves of the nonsaturated bundles become unique white neighbors of their spokes. Hence the stated propagation times are exact.

## Verification
A standalone exhaustive checker constructs \(H(m,s)\) directly, tests the zero forcing closure of every subset of size \(m(s-1)+1\) for ten parameter pairs through order \(22\), compares the result with the two-type classification, and independently computes parallel propagation time. It also exhausts all subsets of size one below the claimed minimum whenever that layer contains at most \(100{,}000\) subsets.

The packaged run reports:

`VERIFY_OK profiles=10 subset_checks=969903 classification_checks=2527 propagation_checks=2527 lower_checks=69801 max_order=22`

Finite enumeration is a stress test only; the proof above establishes the statement for all \(m\ge3\) and \(s\ge2\).

## Relationship to prior work
Anderton et al. proved the scalar formula \(Z(H(m,s))=m(s-1)+1\) for \(s>1\), proved the necessary bundle condition \(|B\cap P_i|\ge s-1\), exhibited one center-type minimum set, and established the graph propagation time \(2\). Those facts are treated as prior work. The result here completes the minimum-set structure: it identifies the second saturated-bundle family, excludes spoke-containing minima, counts both families, and determines the propagation time of every minimum set.

Boyer et al. introduced the zero forcing polynomial and explicitly framed \(z(G;Z(G))\) as the number of minimum zero forcing sets. Their inspected full text contains no occurrence of “helm,” so their general counting framework does not supply this family-specific coefficient.

## Limitations
The theorem does not classify nonminimum zero forcing sets, so it does not give the full zero forcing polynomial of \(H(m,s)\). It excludes the traditional one-leaf helm \(s=1\), whose minimum sets depend on the cyclic placement pattern. Exhaustive computation covers only the stated finite parameter range and is not used as an infinite proof. Literature searches cannot establish global novelty against sources not indexed or not publicly accessible.

## References
1. AIM Minimum Rank–Special Graphs Work Group, “Zero forcing sets and the minimum rank of graphs,” *Linear Algebra and its Applications* 428 (2008), 1628–1648. Available online 2007-11-26. DOI: 10.1016/j.laa.2007.10.009.
2. S. Anderton, R. Burden, M. Fontenot, N. Fredrickson, A. Kwon, S. Le, K. Mizozoe, E. Raign, A. Sangalli, H. Schuerger, and A. Schwartz, “The zero forcing numbers and propagation times of gear graphs and helm graphs,” arXiv:2310.18513v1, 2023.
3. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips, and C. Reinhart, “The zero forcing polynomial of a graph,” arXiv:1801.08910v1, 2018.
