# A period-four unlabelled census of balanced semigeneric tripartite digraphs

## Finding

Let \(n\geq 1\). Consider finite oriented graphs whose nonadjacency relation partitions the vertices into exactly three classes of \(n\) vertices each. Every pair from different classes has exactly one directed edge. For any two distinct vertices from one class and two distinct vertices from another, the number of edges directed from the first class to the second is even. Isomorphisms may permute the three classes. Let \(V_n\) be the number of isomorphism classes of these digraphs.

Put
\[
P_n=\binom{n+3}{3},\quad
Q_n=\begin{cases}n/2+1&n\text{ even},\\0&n\text{ odd},\end{cases}\quad
H_n=(\lfloor n/2\rfloor+1)(\lceil n/2\rceil+1),\quad
E_n=\begin{cases}1&4\mid n,\\0&4\nmid n.\end{cases}
\]
Then the exact answer for every \(n\geq1\) is
\[
\boxed{V_n=\frac{P_n^3+3P_nQ_n^2+4Q_n^3}{48}+\frac{Q_n(H_n+E_n)}4+\frac{P_n+Q_n}{6}.}
\]
Its first six values are \(2,28,170,929,3668,12468\). The function \(V_n\) is a quasipolynomial of degree nine and **minimal quasipolynomial period four**, with
\[
V_n=\frac{n^9}{10368}+O(n^8).
\]
In contrast, if the three classes are named and must be preserved setwise, their unlabelled orientation count is
\[
\boxed{U_n=\frac{P_n^3+3P_nQ_n^2+4Q_n^3}{8},}
\]
a quasipolynomial of minimal period two. Thus forgetting the class names introduces a genuinely new modulus-four correction.

## Assumptions and scope

Graphs are finite, irreflexive, and antisymmetric; no unordered pair has two opposing edges. The three classes are intrinsic because they are exactly the equivalence classes of the nonadjacency relation, but they are not externally named for \(V_n\). The parity condition is imposed separately on every rectangle between each pair of classes; it imposes no additional relation between the three edge blocks. The statement concerns isomorphism classes of finite induced structures, not the automorphism group of the infinite limit or labelled structures. The structural background is the semigeneric homogeneous directed graph.

## Proof

Label the vertex classes temporarily \(A,B,C\), each by \(\{1,\ldots,n\}\), and encode edge orientation from the first to the second class by \(M_{ij}(x,y)\in\mathbf F_2\) for \(i<j\). Rectangle parity says the XOR of the four entries of each \(2\times2\) rectangle is zero. Equivalently,
\[
M_{ij}(x,y)=u_{ij}(x)+v_{ij}(y)\pmod2.
\]
The pair of binary vectors is unique up to simultaneously complementing both. Therefore each of the three edge blocks has exactly \(2^{2n-1}\) admissible matrices, and the three blocks are independent.

Write \(c(\sigma)\) for the number of cycles of \(\sigma\in S_n\), and \(\varepsilon(\sigma)=1\) if every cycle of \(\sigma\) is even, zero otherwise. A rank-one binary edge block fixed by the side-preserving pair \((\sigma,\tau)\) has
\[
f(\sigma,\tau)=2^{c(\sigma)+c(\tau)-1}\bigl(1+\varepsilon(\sigma)\varepsilon(\tau)\bigr)
\]
possibilities. Indeed, invariance forces \(u(\sigma x)+u(x)=v(\tau y)+v(y)=\delta\), with a common constant \(\delta\in\mathbf F_2\); \(\delta=1\) is possible exactly when both permutations have only even cycles. Each case leaves \(2^{c(\sigma)+c(\tau)-1}\) matrices after removing the common-vector gauge.

For three side-preserving permutations \((\sigma_1,\sigma_2,\sigma_3)\), the fixed configurations number \(\prod_{i<j}f(\sigma_i,\sigma_j)\). In the resulting product of correction factors,
\[
\prod_{i<j}(1+\varepsilon_i\varepsilon_j)
=1+\varepsilon_1\varepsilon_2+\varepsilon_1\varepsilon_3+\varepsilon_2\varepsilon_3+4\varepsilon_1\varepsilon_2\varepsilon_3.
\]
The cycle-index identities
\[
\frac1{n!}\sum_{\sigma\in S_n}4^{c(\sigma)}=[z^n](1-z)^{-4}=P_n,
\quad
\frac1{n!}\sum_{\substack{\sigma\in S_n\\\varepsilon(\sigma)=1}}4^{c(\sigma)}=[z^n](1-z^2)^{-2}=Q_n
\]
then give \(U_n=(P_n^3+3P_nQ_n^2+4Q_n^3)/8\).

Next consider a permutation of the vertex set interchanging two classes and fixing the third setwise. Denote by \(\alpha\) and \(\beta\) its two bijections between the exchanged classes, by \(\sigma=\beta\alpha\) the induced permutation of one class under the square, and by \(\gamma\) its permutation of the third class. The orientation block between exchanged classes must obey a complement-transpose equation. After relabelling, this is \(M(x,y)=1+M(\sigma y,x)\). For \(M(x,y)=u(x)+v(y)\), it is equivalent to \(v(x)=u(x)+t\) for some constant \(t\), and \(u(\sigma x)=u(x)+1\). Thus the block has no fixed choices unless all cycles of \(\sigma\) are even; if they are, exactly \(2^{c(\sigma)}\) choices remain. The other two orientation blocks are exchanged. Picking one determines the other, and invariance under the square forces this selected block to be fixed by \((\sigma,\gamma^2)\). The number of configurations fixed by this class transposition is consequently
\[
\mathbf1_{\{\varepsilon(\sigma)=1\}}
2^{2c(\sigma)+c(\gamma^2)-1}\bigl(1+\varepsilon(\gamma^2)\bigr).
\]
As the class bijections vary, \(\sigma\) is uniform in \(S_n\), independently of \(\gamma\). The required cycle-index identities are
\[
\frac1{n!}\sum_{\gamma\in S_n}2^{c(\gamma^2)}
=[z^n]\frac1{(1-z)^2(1-z^2)}=H_n,
\]
and
\[
\frac1{n!}\sum_{\substack{\gamma\in S_n\\\varepsilon(\gamma^2)=1}}2^{c(\gamma^2)}
=[z^n]\frac1{1-z^4}=E_n.
\]
For the second identity, a cycle of \(\gamma^2\) has even length precisely when the corresponding cycle of \(\gamma\) has length divisible by four. Therefore the mean fixed-configuration count in each of the three class-transposition cosets is
\[
T_n=\frac{Q_n(H_n+E_n)}2.
\]

Finally, consider a cyclic permutation of the three classes. Three applications of it induce conjugate permutations \(\xi\in S_n\) on all three classes. The three edge blocks cycle among themselves; their orientation order is reversed twice around this cycle, so no net complement remains. A fixed configuration is determined by one block invariant under the conjugate pair \((\xi,\xi)\), with
\[
2^{2c(\xi)-1}(1+\varepsilon(\xi))
\]
choices. The class bijections make \(\xi\) uniform, giving mean fixed-configuration count in each of the two three-cycle cosets
\[
C_n=\frac{P_n+Q_n}{2}.
\]

The acting group is \(S_n^3\rtimes S_3\). By Burnside's lemma over its six class-permutation cosets,
\[
V_n=\frac{U_n+3T_n+2C_n}{6},
\]
which yields the displayed formula.

The quantities \(P_n\), \(Q_n\), and \(H_n\) are polynomial on each residue class modulo two; \(E_n\) has period four. The term \(Q_nE_n/4\) is positive when \(4\mid n\), but vanishes for \(n\equiv2\pmod4\), and cannot be represented by one polynomial on the even integers: any polynomial vanishing at all \(n\equiv2\pmod4\) vanishes identically, conflicting with its values at \(4\mid n\). All remaining terms have period dividing two, proving **minimal period four**. Likewise, the difference between the even-residue polynomial for \(U_n\) and its odd-residue polynomial \(P_n^3/8\) is \(Q_n^2(3P_n+4Q_n)/8\), a nonzero polynomial on the even progression. Hence \(U_n\) has minimal period two. The degree-nine leading term comes from \(P_n^3/48\), since \(P_n=n^3/6+O(n^2)\).

## Verification

The accompanying `verify.py` independently represents every allowed configuration by \(3(2n-1)\) binary variables, writes the fixed-configuration equations for each class permutation and every within-class permutation, and computes the exact affine-system rank over \(\mathbf F_2\). For all \(n=1,2,3,4\), direct Burnside coset averages agree exactly with the three formulas \(U_n,T_n,C_n\) and hence with \(V_n\). It additionally checks integrality and the two equivalent expressions over more sizes. Run `python3 verify.py` in the folder containing that script. Finite verification is not used as an infinite proof.

## Relationship to prior work

The even-rectangle characterization and the semigeneric homogeneous directed graph were established earlier, including in Cherlin's classification and Jasiński–Laflamme–Nguyen Van Thé–Woodrow's study of Ramsey expansions. A published exact Stirling-layer profile for the semigeneric complete multipartite digraph counts **injectively labelled tuple patterns**, not the present balanced three-class isomorphism quotient by full side permutations. Previously established two-class permutation character and isomorphism formulas solve the bipartite case, but do not determine the three-class transposition/three-cycle fixed characters. The theorem here isolates the previously uncovered three-class fixed-point character and its sharp modulus-four phenomenon. These comparisons do not guarantee complete bibliographic uniqueness.

## Limitations

The isomorphism census is specialized to exactly three equal-sized parts, with all three parts nonempty. No assertion is made about different part sizes, more than three parts, or asymptotics when the number of parts increases. Some specialized or unindexed classification may contain implicit equivalent formulas; the originality conclusion is qualified accordingly. The included finite computation checks sizes at most four exhaustively, while the proof applies to all positive sizes.

## References

1. G. Cherlin, *Homogeneous Directed Graphs: The Imprimitive Case*, in *Logic Colloquium '85* (1987). Author's readable manuscript: https://sites.math.rutgers.edu/~cherlin/Paper/43HDG-Imprimitive.pdf (a later revision; historical first-public calendar day is not inferred from its revision).
2. J. Jasiński, C. Laflamme, L. Nguyen Van Thé, R. Woodrow, *Ramsey precompact expansions of homogeneous directed graphs*, arXiv:1310.6466v1, first publicly posted 2013-10-24, Section 10 on the semigeneric directed graph. https://arxiv.org/abs/1310.6466
3. C. Jahel, *Unique ergodicity of the automorphism group of the semigeneric directed graph*, arXiv:1902.04903 (2019). https://arxiv.org/abs/1902.04903
