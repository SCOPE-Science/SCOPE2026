# Two ramification divisors and the full permutation fixed-locus profile of the Hamilton K3 surface

## Finding

Let \(X=V(\sigma_1,\sigma_2,\sigma_3)\subset\mathbb P^5_{\mathbb C}\), where \(\sigma_j\) is the degree-\(j\) elementary symmetric polynomial in the six homogeneous coordinates. The natural permutation action induces a finite quotient of generic degree \(720\):
\[
q:X\longrightarrow X/S_6\simeq\mathbb P(4,5,6),\qquad [x_1:\cdots:x_6]\longmapsto [u:v:w]=[\sigma_4:\sigma_5:\sigma_6].
\]
Here \(\mathbb P(4,5,6)\) means the **coarse** projective weighted space; in particular its non-well-formed weights are intentional, and its divisorial ramification need not be detected by the polynomial discriminant alone.

**Theorem.** The complete reduced branch divisor is the union of two distinct irreducible curves
\[
B_{\mathrm{red}}=V(v)\cup V(\Delta),\qquad
\Delta=\operatorname{Disc}_t(t^6+ut^2-vt+w),
\]
with generic inertia group of order \(2\) along each component. Explicitly,
\[
\begin{aligned}
\Delta={}&-1024u^6w+256u^5v^2-13824u^3w^3+43200u^2v^2w^2\\
&-22500uv^4w+3125v^6-46656w^5.
\end{aligned}
\]
For each partition of the six coordinate labels into three unordered pairs (a *perfect matching* \(M\)), let \(Q_M\) be the conic parametrized, in the order of the matching pairs, by
\[
(a,-a,b,-b,c,-c),\qquad a^2+b^2+c^2=0.
\]
Then there are fifteen pairwise distinct smooth conics and, as Cartier divisors on the smooth K3 surface,
\[
\operatorname{div}_X(\sigma_5)=\sum_M Q_M.
\]
Every \(Q_M\) is fixed by the corresponding permutation of cycle type \((2,2,2)\), whose generic stabilizer is exactly its order-two subgroup. For \(1\le i<j\le6\), let \(C_{ij}=X\cap V(x_i-x_j)\); these are fifteen smooth connected genus-four curves and
\[
\operatorname{div}_X(\Delta)=2\sum_{i<j}C_{ij}.
\]
The generic stabilizer along each \(C_{ij}\) is its transposition. **No other conjugacy type contributes a fixed curve or an additional divisorial branch component.**

For completeness, the entire geometric fixed-locus profile on \(X\), indexed by permutation cycle type, is:

| Cycle type | Fixed locus on \(X\) |
| --- | --- |
| \((1^6)\) | all of \(X\) |
| \((2,1^4)\) | one smooth connected genus-four curve |
| \((2^2,1^2)\) | eight reduced points |
| \((3,1^3)\) | six reduced points |
| \((2^3)\) | one smooth conic |
| \((4,1^2)\) | two reduced points |
| \((3,2,1)\) | empty |
| \((3^2)\) | six reduced points |
| \((4,2)\) | four reduced points |
| \((5,1)\) | four reduced points |
| \((6)\) | two reduced points |

## Assumptions and scope

Everything is over \(\mathbb C\). All fixed loci are fixed loci of the action on **projective points**, rather than vectors: \(g[x]=[x]\) means \(gx=\lambda x\) for some nonzero scalar \(\lambda\). The initiating literature proves that \(X\) is a smooth K3 surface. Newton identities turn its defining equations into \(p_1=p_2=p_3=0\), where \(p_k=\sum_i x_i^k\), and its hyperplane class \(H\) satisfies \(H^2=6\). All group-theoretic assertions refer to the coordinate-permutation subgroup \(S_6\), not the full abstract automorphism group.

## Proof

**Invariant quotient.** The homogeneous coordinate ring of \(X\) is \(\mathbb C[x_1,\ldots,x_6]/(\sigma_1,\sigma_2,\sigma_3)\). Since finite-group invariants over characteristic zero are exact, the fundamental theorem on symmetric polynomials gives
\[
\mathbb C[X]^{S_6}=\mathbb C[\sigma_4,\sigma_5,\sigma_6],
\]
with weights \(4,5,6\). The quotient is its Proj. The permutation action is generically free because for a generic set of six distinct nonzero roots, no nonidentity permutation scales the ordered root vector. The generic degree is \(|S_6|=720\).

**Eigenvalue calculation of every fixed locus.** Suppose the disjoint cycles of \(g\) have lengths \(\ell_1,\ldots,\ell_c\). Its \(\lambda\)-eigenspace is obtained by placing successive \(\lambda\)-multiples around each cycle of length divisible by the order of \(\lambda\). Thus that eigenspace has vector dimension the number of such cycles. For \(\lambda=1\) the equations become \(\sum_i\ell_i a_i^k=0\) for \(k=1,2,3\). For \(\lambda\) of order two, only \(p_2=0\) remains; for order three, only \(p_3=0\); and for order greater than three all three equations vanish automatically on the eigenspace.

For \(\lambda=1\), at most two cycles give no projective solution by the first two weighted power sums, since all \(\ell_i\) are positive integers. For three cycles, the only partitions \((4,1,1)\), \((3,2,1)\), \((2,2,2)\) give nonzero scalar multiples of \(a^6\) when the last variable is eliminated by the linear power sum and the quadratic/cubic resultants are taken; the remaining \(a=0\) gives only the zero vector. For four cycles of weights \((3,1,1,1)\), normalize the length-three coordinate to one: the other three are distinct roots of \(t^3+3t^2+6t+10\), giving six points. For weights \((2,2,1,1)\), put \(s=a+b\), \(r=ab\), and \(h=cd\) for the two double-cycle and two singleton coordinates. The power sums give \(c+d=-2s\), \(h=3s^2-2r\), and \(6s(2s^2-3r)=0\). The locus \(s=0\) has two projective solutions; the locus \(s\ne0\) has four, hence six \(\lambda=1\) solutions. For five cycles \((2,1,1,1,1)\), the invariant eigenspace cuts \(X\) in a smooth hyperplane curve; six identity cycles give \(X\) itself.

The remaining eigenvalues now give the table without a genericity assumption. For example, the \(-1\) eigenspace of a triple transposition is \(\mathbb P^2\) with coordinates \((a,b,c)\); its sole surviving condition is \(a^2+b^2+c^2=0\). A double transposition has two \(-1\)-eigenpoints, producing eight fixed points in total. A pair of three-cycles has two primitive cube-root eigenspaces, each a \(\mathbb P^1\) cut by a reduced cubic, hence six points. The other rows follow by the listed cycle-length rule. Since \(X\) is smooth in characteristic zero, fixed-point schemes of finite-order automorphisms are smooth; consequently every listed zero-dimensional point is reduced. The transposition-fixed curve is connected by the connectedness theorem for ample hyperplane sections, hence smooth irreducible; by adjunction on the K3 surface its genus is \(1+H^2/2=4\).

**Divisors and the branch.** The fifteen matchings define fifteen distinct linear projective planes; each plane meets \(X\) in the displayed smooth conic. All odd power sums vanish identically on these planes, so \(\sigma_5\) vanishes along every \(Q_M\). Since \(\sigma_5\) is a section of \(\mathcal O_X(5H)\), the divisor of zeros has degree \(5H^2=30\). The fifteen distinct conics contribute total degree \(15\cdot2=30\); equality of effective Cartier divisors follows. The discriminant identity
\[
\Delta(\sigma_4,\sigma_5,\sigma_6)=\prod_{i<j}(x_i-x_j)^2
\]
gives the other divisor formula. Generic points on \(C_{ij}\) have a single repeated root and stabilize by a single transposition. Generic points on a matching conic have six distinct roots in opposite pairs, stabilized projectively by the triple transposition and no additional permutation. Therefore both images are divisorial branch loci of inertia order two. The relevant curves form one orbit in each of the two conjugacy types, so their images are irreducible. Their images are distinct, because a generic matching-conic point has no repeated roots and thus \(\Delta\ne0\). By the complete fixed-locus classification, there are no other divisorial fixed loci; the stated branch divisor is complete.

## Verification

The standalone file `check_hamilton_inertia.py` computes the depressed-sextic discriminant exactly, enumerates all fifteen matchings and the elementary-symmetric restrictions, checks the three-cycle-group resultants and both four-cycle-group cases, and independently checks the Burnside Euler identity using all eleven conjugacy classes. Run `python check_hamilton_inertia.py` with SymPy installed. The expected output is `HAMILTON_SEXTIC_BRANCH_EXACT_OK`. The universal claim is proved above by invariant theory and eigenspace geometry; finite sampling is not used as a proof.

## Relationship to prior work

Raman's 2026 paper introduces and studies the Hamilton normal-form K3 surface and its symmetric action, focusing on incompatibility of different sextic solutions. It does not provide this exhaustive projective fixed-locus table, the two irreducible branch components, or the fifteen-conic factorization. Brandhorst and Hofmann classify finite automorphism groups of K3 surfaces up to deformation through lattice-theoretic data, not the two explicit ramification components for this projective model. The coarse weighted quotient has a non-well-formed weight system, which accounts for ramification along the odd coefficient even when the sextic discriminant is nonzero.

## Limitations

This determines the reduced divisorial branch support and generic inertia, **not** the full scheme structure of the branch discriminant, higher inertia at codimension-two intersections, singularities of the branch curves, quotient singularities, or the full abstract automorphism group of \(X\). The tables classify geometric fixed loci of the displayed permutation action only. A parallel formula under different terminology in earlier classical invariant-theory literature remains a bibliographic risk; independent scientific audit has not been performed.

## References

1. Sidhanth Raman, *The geometry of solutions to the general sextic*, arXiv:2609.30422v1, first posted 24 September 2026, https://arxiv.org/html/2609.30422v1.
2. Simon Brandhorst and Tommy Hofmann, *Finite subgroups of automorphisms of K3 surfaces*, Forum of Mathematics, Sigma 11 (2023), e54, https://doi.org/10.1017/fms.2023.50.
