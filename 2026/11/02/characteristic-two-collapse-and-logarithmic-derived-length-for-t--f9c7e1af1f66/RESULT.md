# Characteristic-two collapse and logarithmic derived length for truncated coordinate-axis algebras

## Finding

Let \(K\) be a field, let \(m\ge2\), and let \(d_1,\ldots,d_m\ge3\) be arbitrary integers. Consider
\[
 A=K[x_1,\ldots,x_m]/(x_ix_j\ (i\ne j),\;x_i^{d_i}\ (1\le i\le m)).
\]
Since \(A\) is commutative, all inner derivations vanish, so the Gerstenhaber Lie algebra \(HH^1(A)\) is \(L=\operatorname{Der}_K(A)\). Write \(L^{(0)}=L\), \(L^{(j+1)}=[L^{(j)},L^{(j)}]\). The complete derived-series dimension profile is:

* In every characteristic, \(\dim_K L=\sum_i(d_i-1)+m(m-1)\).
* If \(\operatorname{char}K=2\), then
\[
 \dim_K L^{(1)}=m(m-1)+\sum_i\left\lfloor\frac{d_i-1}{2}\right\rfloor,
 \qquad L^{(2)}=0.
\]
The abelianization has dimension \(\sum_i\lceil(d_i-1)/2\rceil\), and the derived length is exactly two.
* If \(\operatorname{char}K\ne2\), then
\[
 \dim_K L^{(1)}=m(m-1)+\sum_i(d_i-2),\qquad
 \dim_K L^{(j)}=\sum_i\max\{d_i-2^j,0\}\quad(j\ge2).
\]
The abelianization has dimension \(m\), and the derived length (the least \(j\) with \(L^{(j)}=0\)) is
\[
 \left\lceil\log_2(\max_i d_i)\right\rceil.
\]
In particular, metabelianity holds for all truncation lengths in characteristic two, whereas in every other characteristic it holds exactly when \(\max_i d_i\le4\). All statements are valid over arbitrary fields.

## Assumptions and scope

The polynomial algebra is commutative and unital. Every mixed product \(x_ix_j\) with \(i\ne j\) is zero. The truncation exponents need not be equal. The basis of \(A\) is \(1\) together with \(x_i^a\) for \(1\le i\le m\) and \(1\le a<d_i\). There are no further relations. The derived series uses vector-space spans of commutators, not lower central series. We do not assert results for a single branch (\(m=1\)) or for some \(d_i=2\); those regimes have additional derivations and are excluded.

## Proof

**1. Determine all derivations from relations.** Let \(D\in\operatorname{Der}_K(A)\). Its action on the generators determines it. Write \(D(x_i)\) in the displayed basis. For each pair \(i\ne j\), applying \(D\) to \(x_ix_j=0\) gives
\[
 D(x_i)x_j+x_iD(x_j)=0.
\]
The coefficient of \(x_j\) and the coefficient of \(x_i\), from the respective constant terms, force every constant term of every \(D(x_i)\) to vanish (here \(m\ge2\) matters). For each \(j\ne i\), comparing the coefficients of \(x_j^2,\ldots,x_j^{d_j-1}\) forces all \(x_j\)-branch coefficients of degrees below \(d_j-1\) in \(D(x_i)\) to vanish. Thus
\[
 D(x_i)=\sum_{a=1}^{d_i-1}\alpha_{ia}x_i^a
       +\sum_{j\ne i}\beta_{ij}x_j^{d_j-1}.
\]
Conversely every such assignment defines a derivation: it kills the mixed quadratic relations and also \(x_i^{d_i}\), since \(d_i x_i^{d_i-1}D(x_i)=0\) in \(A\), in all characteristics. Define \(E_{ia}(x_i)=x_i^a\), with other generator images zero, and \(C_{ij}(x_i)=x_j^{d_j-1}\), again zero on other generators. These form a basis of \(L\), proving its dimension.

**2. Compute the entire Lie bracket.** Brackets between distinct branches \(E_{ia},E_{jb}\) vanish if \(i\ne j\). For a fixed branch,
\[
 [E_{ia},E_{ib}]=(b-a)E_{i,a+b-1},
\]
where an index at least \(d_i\) means the zero derivation. The off-diagonal derivations span an abelian ideal \(C\): \([C_{ij},C_{kl}]=0\). Moreover,
\[
 [E_{ia},C_{kl}]=0\quad(a\ge2),\qquad
 [E_{i1},C_{kl}]=
 (\mathbf1_{i=l}(d_l-1)-\mathbf1_{i=k})C_{kl}.
\]
These follow directly by differentiating the one nonzero image of each derivation. In particular \([E_{k1},C_{kl}]=-C_{kl}\), so \(C\subseteq[L,L]\) in any characteristic.

**3. Characteristic two.** The bracket with \(E_{i1}\) is \([E_{i1},E_{ia}]=(a-1)E_{ia}\). In characteristic two, it produces exactly the even-index derivations \(E_{i,2},E_{i,4},\ldots\). No odd-index derivation can occur as a bracket of two same-branch derivations: if \(a+b-1\) is odd, then \(a,b\) have equal parity and \(b-a=0\) in \(K\). Hence
\[
 L^{(1)}=C\oplus\bigoplus_i\operatorname{span}\{E_{i,a}:2\le a<d_i,\ a\text{ even}\}.
\]
Two even-index branch derivations bracket to zero, and all these derivations commute with \(C\); also \(C\) is abelian. Thus \(L^{(2)}=0\), yielding the claimed dimensions. Since \(m\ge2\), \(C\ne0\), so \(L\) is nonabelian and its derived length is exactly two.

**4. Other characteristics.** If \(\operatorname{char}K\ne2\), every \(E_{ia}\) with \(a\ge2\) lies in \([L,L]\). When \(a-1\ne0\) in \(K\), this follows from \([E_{i1},E_{ia}]=(a-1)E_{ia}\). In the remaining case, \(a\ge4\) and \([E_{i2},E_{i,a-1}]=(a-3)E_{ia}\), with \(a-3=-2\ne0\) in \(K\). Neither \(E_{i1}\) nor any other diagonal degree-one element can arise as a bracket. Therefore
\[
 L^{(1)}=C\oplus\bigoplus_i F_{i,2},
 \qquad F_{i,r}=\operatorname{span}\{E_{ia}:r\le a<d_i\}.
\]
Here \([C,F_{i,2}]=[C,C]=0\). For any \(r\ge2\), the formula in step 2 implies
\[
 [F_{i,r},F_{i,r}]=F_{i,2r}.
\]
Indeed the least possible nonzero output index is \(2r\), obtained from \([E_{ir},E_{i,r+1}]=E_{i,2r}\). For an index \(t=2r+1\), \([E_{ir},E_{i,r+2}]=2E_{it}\), whose coefficient is nonzero. For every \(t\ge2r+2\), the two candidate commutators with input indices \((r,t-r+1)\) and \((r+1,t-r)\) have scalar coefficients \(t-2r+1\) and \(t-2r-1\), differing by \(2\), so at least one is nonzero. All used indices lie below \(d_i\) whenever the output index \(t\) does. Thus successive derived terms are precisely \(L^{(j)}=\bigoplus_iF_{i,2^j}\) for every \(j\ge2\). Counting the displayed basis yields the formula. The first vanishing occurs when \(2^j\ge\max_i d_i\), establishing the logarithmic derived length.

## Verification

The attached `verify.py` uses only the Python standard library. It constructs the presented quotient algebra over each of \(\mathbb F_2,\mathbb F_3,\mathbb F_5\), independently solves the linear equations obtained by differentiating every defining relation (without assuming the basis above), checks the Leibniz identity for each resulting derivation against every pair of algebra basis vectors, forms all matrix commutators, and computes successive derived-subspace ranks by modular Gaussian elimination. It checks length vectors \((3,5)\), \((4,7)\), \((3,9)\), and \((3,4,6)\) over each prime field, twelve cases total. The actual command `python verify.py` returned twelve `CHECK_OK` lines followed by `VERIFY_OK`. The unlimited parameter conclusion comes from the preceding proof, not from finite computations.

As a structural illustration, the two algebras with length vectors \((3,9)\) and \((6,6)\) have equal algebra dimension \(11\) and equal first-cohomology dimension \(12\). In odd characteristic their derived lengths are respectively \(4\) and \(3\); in characteristic two their abelianization dimensions are respectively \(5\) and \(6\). Thus these Lie-theoretic invariants distinguish truncation geometries that raw dimensions do not.

## Relationship to prior work

Rubio y Degrassi, Schroll, and Solotar (arXiv:1903.12145, initially public March 28, 2019) study the Lie algebra \(HH^1\) and give general sufficient conditions for solvability, along with a quiver-path description of the Gerstenhaber bracket. Those structural tools motivate looking beyond binary solvability, but their inspected results do not assert this complete derived series for variable-length truncated coordinate axes. Suárez-Álvarez (arXiv:2402.11962, first public February 19, 2024) analyzes explicit derivations and brackets for a different, infinite-dimensional noncommutative deformation \(yx-xy=x^N\) over characteristic zero; its hypotheses do not imply the present finite commutative positive-characteristic theorem.

A published mathematical research record on automorphisms of equal-length truncated coordinate-cross algebras gives a closely related group-theoretic description. It may imply aspects of the equal-length specialization upon passage to infinitesimal automorphisms, which are not separately claimed as novel. The variable-length all-characteristic derived-series theorem, including the exact sharp characteristic-two collapse, is the contribution assessed here. Its relationship to unpublished or differently named fiber-product derivation formulas remains a publication-priority caveat.

## Limitations

No statement is made about general nonmonomial deformations, mixed products not identically zero, fields of unknown positive characteristic (the characteristic must be specified to select the appropriate formula), or the excluded \(m=1\) and \(d_i=2\) boundaries. General algorithms for Hochschild brackets or explicit automorphism groups could conceivably encode parts of this special case without the statement appearing verbatim. The supplied code checks finite primes and finite length vectors; it is not a formal proof for all fields. No independent mathematical audit has been performed.

## References

1. L. Rubio y Degrassi, S. Schroll, A. Solotar, “The first Hochschild cohomology as a Lie algebra,” arXiv:1903.12145 (first version March 28, 2019), https://arxiv.org/abs/1903.12145.
2. M. Suárez-Álvarez, “On the derivations and automorphisms of the algebra \(k\langle x,y\rangle/(yx-xy-x^N)\),” arXiv:2402.11962 (first version February 19, 2024), https://arxiv.org/abs/2402.11962.
3. “Automorphisms of truncated coordinate-cross algebras over arbitrary fields,” published-finding corpus research record, identifier `2026/10/4/SCOPE-automorphisms-of-truncated-coordinate-cross-algebras-over-arbitr--625ba30274cb` (complete published RESULT.md inspected; equal-truncation automorphism theorem, no stated unequal-truncation Lie-derived ranks).
