# Fault-tolerant resolving bases and their exchanges in the Heawood graph

## Finding

The Heawood graph \(H\), the incidence graph of the seven-point Fano plane, has fault-tolerant metric dimension
\[\dim_2(H)=7.\]
There are exactly \(282\) minimum two-fold resolving sets. Two consist of one complete bipartition class. The other \(280\) have profiles (three points, four lines) or (four points, three lines), \(140\) of each. Their exact geometric classification is given below.

Let \(\mathcal R\) be their *token-jumping exchange graph*: two different size-seven sets are adjacent precisely if they intersect in six vertices, so one selected landmark is replaced by one unselected landmark. Then
\[|V(\mathcal R)|=282,\qquad |E(\mathcal R)|=784,\qquad \mathcal R=K_1\sqcup K_1\sqcup B,\qquad |V(B)|=280,\]
where the two isolated vertices are the full point class and full line class, and
\[\operatorname{rad}(B)=6,\qquad \operatorname{diam}(B)=7.\]
The large component has \(224\) vertices of eccentricity \(6\) and \(56\) vertices of eccentricity \(7\). The total degree distribution is two of degree \(0\), fifty-six of degree \(4\), and 224 of degree \(6\).

This distinguishes fault tolerance of a *fixed* landmark installation (every state survives deletion of any one landmark) from mobility of *optimal* installations: the two entirely one-sided optimal states cannot undergo a single legal exchange.

## Assumptions and scope

Label the points by \(P=\mathbb Z/7\mathbb Z\) and label the seven lines by \(L_j=\{j,j+1,j+3\}\) for \(j\in P\), with modular addition. In the graph, the fourteen vertices are the points and line symbols, with edges exactly at incidences. A set \(S\) is *two-fold resolving* if for each distinct pair \(u,v\in V(H)\), at least two landmarks \(w\in S\) have \(d_H(u,w)\ne d_H(v,w)\). This is equivalent to ordinary resolving surviving loss of any one landmark. Only subsets and exchanges in this fixed fourteen-vertex graph are asserted; no asymptotic claim is made.

Write \(A=S\cap P\) and \(B=S\cap\{L_0,\ldots,L_6\}\). If \(A\) is a three-point noncollinear triple, each line meets \(A\) in \(0\), \(1\), or \(2\) points. Write \(U_i(A)\) for the set of lines meeting \(A\) in exactly \(i\) points. Then \((|U_0|,|U_1|,|U_2|)=(1,3,3)\). The exact admissible four-line parts are
\[B=U_1(A)\cup\{\ell\},\quad \ell\in U_0(A)\cup U_2(A),\qquad\text{or}\qquad B=U_0(A)\cup U_2(A).\]
There are thus exactly five choices. Dually, if \(B\) is a nonconcurrent triple of lines, interchange points and lines in the preceding five-choice rule. All mixed minimum states arise in these two ways. The remaining minimum states are \(S=P\) and \(S=\{L_0,\ldots,L_6\}\).

A vertex of the large component has eccentricity \(7\) **if and only if** it has the first pattern above with \(\ell\in U_0(A)\), or the dual pattern. Hence there are exactly \(28+28=56\) peripheral vertices. This characterization refers to the large component; graph distances between different connected components are not finite.

## Proof

For two distinct points \(p,q\), only the two point-landmarks \(p,q\) distinguish them among all point-landmarks; among line-landmarks, exactly those incident with exactly one of \(p,q\) distinguish them. The dual statement holds for a pair of lines. For a point–line pair, every landmark distinguishes the vertices because their distances to every landmark have opposite parity. Therefore, once \(|S|\ge2\), the two-fold resolving condition is *exactly* the following two finite families of inequalities, one for every distinct point pair and one for every distinct line pair:
\[
|A\cap\{p,q\}|+|\{\ell\in B:\ |\ell\cap\{p,q\}|=1\}|\ge2,
\]
\[
|B\cap\{\ell,m\}|+|\{p\in A:\ |\{\ell,m\}\cap [p]|=1\}|\ge2,
\]
where \([p]\) denotes the three lines through \(p\). This is the dual of the point-pair inequality.

These inequalities give a finite case classification using the seven explicitly listed lines. Enumerate \(A\) and \(B\) independently among subsets of the seven labels. The number of solutions for total cardinalities \(0,1,2,3,4,5,6,7\), respectively, is
\[(0,0,0,0,0,0,0,282).\]
At cardinality seven, the count grouped by \(|A|=0,1,2,3,4,5,6,7\) is
\[(1,0,0,140,140,0,0,1).\]
For \(|A|=3\), the seven collinear triples admit no valid four-line choice. The other twenty-eight three-point triples admit exactly five, namely the explicitly stated \(U_i(A)\) choices; their duals account for the other 140 mixed states. These assertions are also a compact finite proof: the cases are exhaustive over at most \(2^{14}\) point-and-line incidence assignments, and the explicit predicate and exact loops are given in `verify_geometry.py`. That script enumerates **all** smaller cardinalities and verifies equality between the geometric family and the complete solution set, rather than sampling states.

For exchange adjacency, order the 282 set masks increasingly and join two exactly when their intersection has size six. The first verification code regenerates the distance table of \(H\), tests every subset up to size seven, constructs exchanges by removing and inserting landmarks, and runs breadth-first search from every vertex of the nontrivial component. The second code instead computes the displayed incidence inequalities, generates the geometric classification independently, forms exchanges by pairwise set intersection, and independently computes all shortest paths. Both check the same exhaustive list of 282 states, 784 edges, two isolates, connected 280-state component, and giant-component eccentricity distribution \(6^{224}7^{56}\). The second additionally tests exactly which geometric states have eccentricity seven. The certificate gives every state mask, every undirected exchange edge, and each giant-component eccentricity. These finite computations, with the complete domain specified and checked, constitute exhaustive finite verification; they do not claim a general theorem about projective planes of larger order.

## Verification

Run, using Python 3 from the directory containing all the accompanying files:

```bash
python verify_distances.py
python verify_geometry.py
```

The first script creates `reconfiguration_certificate.json` deterministically; the second checks that certificate. The recorded outputs `verify_distances.stdout` and `verify_geometry.stdout` both end with `VERIFY_OK`. The certificate is an independent replayable representation of the full state-and-edge set, not a substitute for inspecting the definition and the two exhaustive algorithms. Its SHA-256 is `bdab9a6ad701d378ceb4e18a4bd79f8e1afe78ffac338b3ac75c1b2be94aaf7a`.

## Relationship to prior work

Héger and Takáts [1] treat ordinary one-fold resolving sets of projective-plane incidence graphs; their Remark 11 determines the Fano plane's ordinary metric dimension to be five. Bailey [2] independently tabulates the same ordinary value for the Heawood graph. Estrada-Moreno, Rodríguez-Velázquez and Yero [3] introduce the two-fold metric invariant and its general monotonicity, but do not classify these Fano configurations or exchanges. Bailey [4] develops one-fold resolving theory for symmetric-design incidence graphs, again without these two-fold exchange distances. The present theorem concerns the exact minimum two-fold basis family and its one-landmark exchange geometry, neither implied by the ordinary five-landmark optimum nor by general monotonicity.

## Limitations

All statements concern the precisely specified fourteen-vertex Heawood incidence graph, not arbitrary projective planes or different reconfiguration rules. The value of the ordinary metric dimension and the general definition of two-fold resolving sets are prior work. The exhaustive calculations are finite, not asymptotic. An exact prior-publication equivalence may exist outside the inspected primary literature and search records; independent external scientific review has not been performed.

## References

[1] T. Héger and M. Takáts, *Resolving Sets and Semi-Resolving Sets in Finite Projective Planes*, Electronic Journal of Combinatorics 19(4) (2012), P30, first public preprint 2012-07-23. https://arxiv.org/abs/1207.5469 ; https://www.combinatorics.org/ojs/index.php/eljc/article/view/v19i4p30

[2] R. F. Bailey, *The metric dimension of small distance-regular and strongly regular graphs*, preprint first posted 2013-12-17, arXiv:1312.4973. https://arxiv.org/abs/1312.4973

[3] A. Estrada-Moreno, J. A. Rodríguez-Velázquez and I. G. Yero, *The k-metric dimension of a graph*, preprint first posted 2013-12-24, arXiv:1312.6840. https://arxiv.org/abs/1312.6840

[4] R. F. Bailey, *On the metric dimension of incidence graphs*, preprint first posted 2017-07-10, arXiv:1707.02899. https://arxiv.org/abs/1707.02899
