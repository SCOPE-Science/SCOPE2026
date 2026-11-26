# All minimum 1-limited dominating sets of circular ladders

## Finding

Let \(G=C_n\square K_2=\operatorname{GP}(n,1)\), with \(n\ge 3\). Its minimum 1-limited domination number is \(n\). The number of distinct minimum subsets of the labelled vertex set is
\[
2+4\mathbf{1}_{4\mid n}.
\]
The two universal minimizers are the two layers. When \(4\mid n\), the other four minimizers select both vertices of two consecutive columns, then neither vertex of the next two, repeating this pattern cyclically. All four shifts are counted separately. There are no other minimizers.

## Definitions and scope

Column \(i\in\mathbb Z/n\mathbb Z\) consists of vertices \(u_i,v_i\). Edges are the spokes \(u_iv_i\) and the layer edges \(u_iu_{i+1}\), \(v_iv_{i+1}\). For \(n\ge3\) these give three distinct neighbours at each vertex. A set \(D\) is 1-limited dominating if each vertex outside \(D\) has at least one neighbour in \(D\) and each vertex in \(D\) has at most one neighbour outside \(D\). Counts refer to vertex-labelled subsets, not subsets modulo symmetry or to distinct edge sets.

## Proof

Write \(D^c=V(G)\setminus D\). Counting crossing edges from both sides gives \(|D^c|\le e(D,D^c)\le |D|\), hence \(|D|\ge n\). A whole layer attains equality. At equality every vertex has exactly one neighbour of the opposite membership bit. Conversely any binary labelling with exactly one opposite-labelled neighbour at every vertex gives an admissible set of size \(n\), since its opposite-class edges pair the two classes.

Suppose the two membership bits in some column differ. The spoke is then the unique opposite-class edge at each of its endpoints. The corresponding layer bits in the two neighbouring columns must agree with their respective bits at this column, so the neighbouring spokes cross as well. Induction around the cycle gives two opposite constant layers, with two possible assignments.

If no spoke crosses, let \(x_i\) be the common bit in column \(i\). The two layer neighbours of each vertex must have opposite membership bits from one another, so \(x_{i+2}=1-x_i\) at every index. Given \(x_0,x_1\), this determines a sequence with least period four: \((x_0,x_1,1-x_0,1-x_1)\). Thus cyclic closure requires \(4\mid n\); in that case the four choices for the two bits are exactly the four shifts of the repeated word \((0,0,1,1)\), and all satisfy the neighbour condition. This proves the classification for the full range \(n\ge 3\).

## Reproduction

Run `python3 verify.py`. The verifier evaluates all two-column states and three-column transitions and checks the cyclic strongly connected components. It also separately enumerates the original vertex labellings for \(3\le n\le 8\) and checks the full solution sets against the stated templates. The proof above, not finite sampling, establishes the classification for arbitrary \(n\).

## Relationship to prior work and limitations

The half-order bound is a direct edge count, and layer-constant perfect two-colourings are included in the established quotient-matrix existence theory. The additional result for circular ladders is the exhaustive labelled census and the period-four obstruction, not the bound or existence. Karami's Theorem 1 in [arXiv:2606.14190v1](https://arxiv.org/abs/2606.14190) classifies attainable quotient matrices and includes the matrix with two same-class and one opposite-class neighbour for every admissible generalized Petersen graph. That occurrence theorem does not enumerate the labellings. Full historical priority, including a comparison with all of Alaeiyan and Karami's [2016 paper](https://doi.org/10.1007/s12044-016-0285-4), is not established here.

This result is confined to the prism. The companion result *All perfect matching cuts of generalized Petersen graphs with inner step two* treats a different family and is not part of this claim. The later [complete 1-limited domination polynomial for circular ladders](https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-complete-one-limited-domination-polynomial-of-circular-ladders--4d83cdec888e) contains the same minimum coefficient as part of a broader enumeration. No classification of larger admissible sets is asserted here.
