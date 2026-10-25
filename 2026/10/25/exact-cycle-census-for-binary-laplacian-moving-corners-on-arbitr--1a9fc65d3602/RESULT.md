# Exact cycle census for binary Laplacian moving corners on arbitrary rectangles

## Finding

For positive integers \(D,E\), put \(V_{D,E}=\mathbb F_2^{D\times E}\), and let \(U,V\) be the inward coordinate shifts, truncated at the two edges. Define the binary diagonal-Laplacian moving-corner map
\[
T_{D,E}=(I+U^2)(I+V^2).
\]
For every integer \(r\ge0\), set \(a_r=2^{r+1}\), \([s]_+=\max(s,0)\), and
\[
K_r(D,E)=\sum_{t\ge0}\min\{a_r,[D-ta_r]_+\}\min\{a_r,[E-ta_r]_+\}.
\]
Only finitely many summands are nonzero. **The exact fixed-point census** is
\[
\boxed{\#\operatorname{Fix}(T_{D,E}^{2^r})=2^{K_r(D,E)}.}
\]
Let \(R\) be the smallest nonnegative integer with \(2^{R+1}\ge\max(D,E)\). Every configuration is periodic, with period dividing \(2^R\); moreover \(2^R\) is the exact order of the operator. The numbers of configurations with *least* periods \(1,2,4,\ldots,2^R\) are
\[
A_0=2^{K_0(D,E)},\qquad
A_r=2^{K_r(D,E)}-2^{K_{r-1}(D,E)}\quad(1\le r\le R).
\]
There are exactly \(A_r/2^r\) distinct cycles of length \(2^r\), and the complete dynamical zeta function is
\[
\boxed{\zeta_{D,E}(z)=\prod_{r=0}^{R}(1-z^{2^r})^{-A_r/2^r}.}
\]
For dyadic rectangles \(D=2^k\), \(E=2^\ell\) with \(\max(D,E)\ge4\), a uniformly chosen binary seed has the maximum period \(2^R\) with the **exact probability**
\[
\boxed{1-2^{-DE/2}.}
\]
Thus almost every seed in a growing dyadic window attains the full operator order; the exceptional fraction is explicitly exponential in the window area.

## Assumptions and scope

The two shifts commute and act on basis states by \(Ue_{i,j}=e_{i+1,j}\) for \(i+1<D\), and zero otherwise, and \(Ve_{i,j}=e_{i,j+1}\) for \(j+1<E\), and zero otherwise, with zero-based indices. The map is over \(\mathbb F_2\). In the four-diagonal-neighbor discrete Laplacian, the \(D\times E\) window moving outward with the northeast propagation corner has this autonomous update: the four diagonal contributions give \((I+U^2)(I+V^2)\) and the central coefficient \(-4UV\) vanishes modulo two. This is **co-moving corner dynamics**, not periodic recurrence of the complete configuration on the infinite lattice.

No symmetry, support shape, or random-seed hypothesis is required. Rectangles of side length one are included. The zeta function counts all finite-state corner configurations including the zero state. In the dyadic assertion, the uniform distribution is over all \(2^{DE}\) binary corner states.

## Proof

**Step 1 (Frobenius reduction).** For \(q=2^r\), commutativity and characteristic two give
\[
T_{D,E}^{q}-I=U^{2q}+V^{2q}+U^{2q}V^{2q}.
\]
Write \(a=2q\) and identify the corner vector space with the truncated polynomial algebra
\[
\mathcal R=\mathbb F_2[u,v]/(u^D,v^E),
\]
where the shifts act by multiplication by \(u,v\). Thus \(T^q-I\) is multiplication by \(u^a+v^a+u^av^a\).

**Step 2 (residue-chain decomposition).** For \(0\le i<a\), let \(d_i\) be the number of integers of the form \(i+at\) in \(\{0,\ldots,D-1\}\); similarly, for \(0\le j<a\), let \(e_j\) count \(j+at<E\). These numbers may be zero. The monomials split \(\mathcal R\) into invariant subspaces indexed by \((i,j)\), each identified with
\[
\mathcal R_{i,j}=\mathbb F_2[X,Y]/(X^{d_i},Y^{e_j}),
\]
where \(X=u^a\), \(Y=v^a\). The summand is zero when either chain length is zero.

**Step 3 (exact kernel in one chain pair).** On a nonzero summand, the relevant multiplication operator is \(M_{X+Y+XY}\). Since \(1+X\) is a unit of the truncated algebra, the substitution \(Y\mapsto(1+X)Y\), \(X\mapsto X\) is an algebra automorphism. It carries \(X+Y\) to \(X+Y+XY\), so these multiplication operators have equal kernel dimension. For any finite-dimensional algebra, the rank of multiplication by \(f\) equals the dimension of its principal ideal, and therefore its nullity equals \(\dim(\mathcal R_{i,j}/(f))\). Setting \(Y=X\) yields
\[
\mathcal R_{i,j}/(X+Y)\cong\mathbb F_2[X]/(X^{\min(d_i,e_j)}),
\]
so
\[
\dim\ker M_{X+Y+XY}=\min(d_i,e_j).
\]
There is no appeal to a Jordan decomposition or numerical rank estimate.

**Step 4 (summing all chains).** The number of horizontal chains of length at least \(t+1\) is \(\min\{a,[D-ta]_+\}\), and likewise vertically. Using
\[
\min(d_i,e_j)=\sum_{t\ge0}\mathbf1_{d_i\ge t+1}\mathbf1_{e_j\ge t+1}
\]
and summing over residue pairs gives precisely \(K_r(D,E)\). A linear map over \(\mathbb F_2\) with kernel dimension \(K_r\) has \(2^{K_r}\) fixed vectors, proving the main formula.

**Step 5 (least periods and exact operator order).** If \(a\ge\max(D,E)\), the two nilpotent shifts \(U^a,V^a\) vanish, hence \(T^{2^r}=I\). If \(a<\max(D,E)\), at least one of the distinct monomials \(u^a,v^a,u^av^a\) survives in \(\mathcal R\), so \(T^{2^r}\ne I\). Thus the operator's exact order is \(2^R\). Every orbit length of this finite permutation divides that power of two. Nested fixed-point sets give the displayed exact-period differences and cycle counts. The zeta product is the standard finite-permutation periodic-orbit identity and follows directly by collecting cycles of each length.

**Step 6 (dyadic half-rank phenomenon).** Write \(M=\max(D,E)=2^k\ge4\) and \(m=\min(D,E)=2^\ell\). Here \(R=k-1\), and for the next smaller power \(2^{R-1}\), the parameter in Step 1 is \(a=M/2\). If \(m\le M/2\), the sole nonzero summand of \(K_{R-1}\) is \((M/2)m=DE/2\). If \(m=M\), exactly two summands contribute, each equal to \((M/2)^2\), giving the same \(DE/2\). Hence exactly \(2^{DE/2}\) states have nonmaximal period, out of \(2^{DE}\). Subtraction proves the probability formula.

## Verification

The self-contained `artifacts/verify_corner.py` performs exact bitwise linear-algebra checks. It independently builds the operator matrix from the local four-term rule and row-reduces \(T^{2^r}-I\) over \(\mathbb F_2\), comparing the nullity with \(K_r\). It also enumerates every state in small windows and counts periodic points directly, as well as checking the dyadic half-rank identity. It completed **405 exact rank comparisons, 60 exhaustive finite-state counts, and the dyadic checks** without failure. The universal proof is Steps 1–6; finite checks alone do not establish it.

For example, on a \(5\times7\) rectangle the three fixed-point dimensions are \(K_0=10\), \(K_1=19\), \(K_2=35\), giving exact least-period counts \(2^{10}\), \(2^{19}-2^{10}\), and \(2^{35}-2^{19}\) at periods \(1,2,4\) respectively.

## Relationship to prior work

Nowak-Kępczyk, *Frobenius Revivals in Laplacian Cellular Automata: Replication, Entropy, and Information Recovery* (arXiv:2511.17389v2), derives the binary moving-corner factorization and the **order of the entire square-window operator**, and explicitly notes that individual seeds can have shorter periods. The present result answers the seed-level counting question exactly, for **all rectangular window dimensions**, and supplies the cycle census, zeta function, and dyadic full-period probability. The source's operator-order bound does not itself give these counts.

Classical representation theory, including Glasby–Praeger–Xia (arXiv:1711.06860), studies the Jordan structure of products of unipotent Jordan blocks. In particular, their general theory contains the familiar minimum-chain-length nullity calculation. That algebraic ingredient is not claimed as new. The substantive contribution here is its explicit residue-chain synthesis into a closed *corner-dynamical* fixed-point and least-period census, valid for all rectangle sizes, together with the exact dyadic full-period law. Published related studies of prime-power modular Laplacian evolution concern full-lattice dilation and modulus changes, not this co-moving finite-state cycle enumeration.

## Limitations

The result concerns characteristic two and the diagonal four-neighbor moving-corner rule. It is not a classification of the full infinite-lattice Laplacian's periodic states, nor of the ternary corner operator or mixed-modulus schedules. The exact formula counts all binary corner states; it does not count only seeds of a prescribed Hamming weight or support shape. Historical priority for this particular dynamical application remains a bibliographic risk; the underlying algebra is classical. No independent audit has been performed.

## References

1. M. Nowak-Kępczyk, *Frobenius Revivals in Laplacian Cellular Automata: Replication, Entropy, and Information Recovery*, arXiv:2511.17389v2 (first posted 2025-11-21; revised 2026-10-12). https://arxiv.org/abs/2511.17389
2. S. P. Glasby, C. E. Praeger, B. Xia, *'Norman involutions' and tensor products of unipotent Jordan blocks*, arXiv:1711.06860v2 (2018). https://arxiv.org/abs/1711.06860
3. *Prime-power digit factorization in modular Laplacian dynamics*, publicly accessible mathematical record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/9/19/SCOPE-prime-power-digit-factorization-modular-laplacian--c49cdde3a491
4. *Boundary-controlled parity reduction in modular Laplacian dynamics*, publicly accessible mathematical record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/9/19/SCOPE-boundary-parity-reduction-modular-laplacian--329faea3aeba
