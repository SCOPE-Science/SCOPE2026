# Exact size of the \((5,3,7;1)\) Reed--Solomon sunflower

## Finding
Let \(\mathbb F_7\) be the field of seven elements. For an ordered 5-tuple \(\alpha=(\alpha_1,\ldots,\alpha_5)\) of distinct field elements, let
\[
\operatorname{RS}_{5,3}(\alpha)=\{(f(\alpha_1),\ldots,f(\alpha_5)):f\in\mathbb F_7[x],\ \deg f<3\}\subseteq\mathbb F_7^5.
\]
Among these Reed--Solomon codes, the largest family whose pairwise intersections are all exactly the one-dimensional constant subspace \(\langle\mathbf 1\rangle\) has size
\[
10.
\]
Equivalently, the maximum size of a \((5,3,7;1)\) Reed--Solomon sunflower is exactly \(10\).

## Assumptions and scope
The evaluation points are ordered and pairwise distinct, and codes are identified as subspaces of the fixed coordinate space \(\mathbb F_7^5\). The center is the standard constant subspace \(\langle\mathbf 1\rangle\), as in the recent definition of Reed--Solomon sunflowers. The statement is an exact finite result for \((\ell,k,q)=(5,3,7)\); it is not an asymptotic theorem and does not claim an exact formula for other field sizes.

The length is the minimal value \(\ell=2k-1\) in the higher-dimensional regime \(k\ge3\). The unrestricted Grassmannian sunflower problem is different: the Reed--Solomon restriction is essential here.

## Proof
Every evaluation vector has distinct first two entries. Applying the unique affine map \(x\mapsto ax+b\) that sends those entries to \(0\) and \(1\) does not change the Reed--Solomon code. Conversely, for \(2(k-1)<\ell\), two evaluation vectors define the same Reed--Solomon code only when they differ by such an affine map. Therefore every distinct \([5,3]_7\) Reed--Solomon code has a unique normalized representative
\[
(0,1,a,b,c),
\]
where \(a,b,c\) are distinct elements of \(\{2,3,4,5,6\}\). Hence there are exactly
\[
5\cdot4\cdot3=60
\]
distinct codes, agreeing with the general count \((q-2)!/(q-\ell)!\).

For a normalized vector \(\alpha\), take the generator matrix
\[
G_\alpha=\begin{pmatrix}
1&1&1&1&1\\
\alpha_1&\alpha_2&\alpha_3&\alpha_4&\alpha_5\\
\alpha_1^2&\alpha_2^2&\alpha_3^2&\alpha_4^2&\alpha_5^2
\end{pmatrix}.
\]
For two codes \(C_\alpha,C_\beta\), exact finite-field row reduction gives
\[
\dim(C_\alpha\cap C_\beta)=6-\operatorname{rank}\!\begin{pmatrix}G_\alpha\\G_\beta\end{pmatrix}.
\]
Every code contains \(\mathbf 1\), so a pair is compatible for the required sunflower precisely when this intersection dimension is \(1\).

Construct the compatibility graph \(H\) whose 60 vertices are the distinct normalized Reed--Solomon codes and whose edges join compatible pairs. Direct exact arithmetic over \(\mathbb F_7\) gives 1200 edges with intersection dimension \(1\), while the remaining 570 unordered pairs have intersection dimension \(2\). In particular, \(H\) is 40-regular.

The following ten normalized evaluation vectors form a clique in \(H\):
\[
\begin{aligned}
&(0,1,6,5,4),\ (0,1,6,4,3),\ (0,1,5,3,4),\ (0,1,6,3,5),\ (0,1,5,6,2),\\
&(0,1,5,2,3),\ (0,1,4,2,5),\ (0,1,3,2,4),\ (0,1,2,6,4),\ (0,1,2,3,6).
\end{aligned}
\]
Thus a 10-petal sunflower exists.

For the upper bound, the accompanying verifier reconstructs all 60 codes from field arithmetic and enumerates every maximal clique of \(H\) by the Bron--Kerbosch algorithm with pivoting. The exact maximal-clique size histogram is
\[
30\text{ of size }6,\quad 1920\text{ of size }7,\quad 5070\text{ of size }8,\quad 1800\text{ of size }9,\quad 138\text{ of size }10.
\]
There is no maximal clique of size larger than \(10\), so no sunflower can have more than 10 petals. A second, independent branch-and-bound maximum-clique search, using greedy coloring only as a rigorous upper bound on each search node, also returns \(10\). Together with the explicit clique above, this proves the claimed optimum.

## Verification
Run `python3 verify_rs_sunflower_q7.py`. The script uses only the Python standard library. It independently regenerates all ordered 5-tuples of distinct elements of \(\mathbb F_7\), confirms that they collapse to exactly 60 row spaces, recomputes every pairwise intersection dimension, checks the displayed 10-code witness, enumerates all maximal cliques, and repeats the maximum computation with a different exact branch-and-bound routine. The expected final line is `VERIFY_OK`.

The exhaustive computation is the proof of the finite upper bound; it is not extrapolated to any infinite parameter family.

## Relationship to prior work
Con, Gruica, Montanucci, and Zullo introduced Reed--Solomon sunflowers and asked for the maximum possible size of an \((\ell,k,q;1)\) Reed--Solomon sunflower for \(k\ge3\). Their paper gives a generalized \(V\)-matrix criterion, counts the distinct Reed--Solomon codes, and proves asymptotic recursive and greedy lower bounds. It explicitly leaves the extremal size problem open for \(k\ge3\). The present result resolves the concrete minimal-length instance \((\ell,k,q)=(5,3,7)\) exactly.

For context, the unrestricted subspace-sunflower construction at \(\ell=2k-1\) can have \((q^{2k-2}-1)/(q^{k-1}-1)\) petals, which equals \(50\) at \((k,q)=(3,7)\). The exact Reed--Solomon optimum \(10\) therefore measures a substantial finite-field restriction rather than merely restating the unrestricted Grassmannian bound.

Focused searches using the phrases “Reed--Solomon sunflower”, the exact parameters \((5,3,7)\), generalized \(V\)-matrices, and the equivalent constant-dimension/intersection formulation found the motivating paper but no source stating this exact value. Repository similarity searches likewise returned nearby coding-theory results but no Reed--Solomon-sunflower instance with these parameters. This absence is supporting evidence only, not a proof of novelty.

## Limitations
The upper bound is an exhaustive finite computation specialized to \(\mathbb F_7\), length 5, dimension 3, and center \(\langle\mathbf1\rangle\). It does not classify the 138 maximum families up to symmetry, does not determine the optimum for \(q=8\) or larger fields, and does not improve the asymptotic exponents in the general theory. Literature searches cannot exclude an older equivalent computation under different terminology.

## References
1. R. Con, A. Gruica, M. Montanucci, and F. Zullo, “Sunflowers of Reed--Solomon Codes,” arXiv:2609.33512v1, first public 2026-09-27. In particular, see the definition and rank criterion in Section 2, the exact Reed--Solomon count in Corollary 3.3, the greedy bound in Proposition 3.23, and the extremal-size open question in Section 5.
