# Arithmetic coinvariants of the Kummer node--trope incidence correspondence

## Finding

Let \(k=\mathbb F_q\) have odd characteristic and let \(C/k\) be **any smooth genus-two curve**. Write \(J\) for its Jacobian, and take the classical Kummer quartic \(K=J/\{\pm1\}\) in its twice-theta embedding. Its finite Galois sets of sixteen geometric nodes and sixteen trope planes are \(N\) and \(T\). Define the canonical integral incidence homomorphism

\[
I:\mathbb Z[T]\longrightarrow\mathbb Z[N],\qquad
[t]\longmapsto\sum_{n\in N,\ n\text{ lies on }t}[n].
\]

The map is injective and has rationally invertible matrix; its integral Smith invariant factors are

\[
(1^{\times 6},2^{\times4},4^{\times5},12).
\]

Consequently its finite Galois-module cokernel \(Q=\operatorname{coker} I\) has order \(3\cdot2^{16}\), with abstract underlying group

\[
Q\cong(\mathbb Z/2\mathbb Z)^4\oplus(\mathbb Z/4\mathbb Z)^5\oplus\mathbb Z/12\mathbb Z.
\]

The two sixteen-element Galois sets have the same number of rational points over every extension: \(\#N(\mathbb F_{q^m})=\#T(\mathbb F_{q^m})\) for each \(m\ge1\), and therefore identical finite-etale zeta functions. However, the **arithmetic integral incidence obstruction** \(Q_F=Q/(F-1)Q\) distinguishes some cases with identical node and trope zeta functions. Here \(F\) is geometric Frobenius; replacing it by arithmetic Frobenius gives the same coinvariant quotient because \(F-1\) and \(F^{-1}-1\) have the same image.

Its complete classification is indexed by the eleven cycle types of Frobenius on the six geometric Weierstrass points; every listed cycle type occurs for some smooth genus-two curve over a sufficiently large odd finite field:

| Branch Frobenius type | Nodes and tropes (each) | Nontrivial invariant factors of \(Q_F\) | Order \(\#Q_F\) |
|---|---|---|---:|
| `1+1+1+1+1+1` | `1^16` | `(2)^4 (4)^5 (12)` | 196608 |
| `2+1+1+1+1` | `1^8 2^4` | `(2)^2 (4)^4 (12)` | 12288 |
| `3+1+1+1` | `1^4 3^4` | `(4)^3 (12)` | 768 |
| `2+2+1+1` | `1^4 2^6` | `(2)^2 (4)^3 (12)` | 3072 |
| `4+1+1` | `1^2 2 4^3` | `(2)^2 (4) (12)` | 192 |
| `3+2+1` | `1^2 2 3^2 6` | `(4)^2 (12)` | 192 |
| `5+1` | `1 5^3` | `(4) (12)` | 48 |
| `2+2+2` | `1^4 2^6` | `(2)^4 (4)^2 (12)` | 3072 |
| `4+2` | `1^2 2 4^3` | `(2)^2 (4) (12)` | 192 |
| `3+3` | `1 3^5` | `(2)^2 (4) (12)` | 192 |
| `6` | `1 3 6^2` | `(2)^2 (12)` | 48 |


In particular, Frobenius types `2+2+1+1` and `2+2+2` each give cycle type \(1^4 2^6\) on **both** the node and trope schemes. Yet the incidence coinvariant groups are nonisomorphic:

\[
Q_F\cong(\mathbb Z/2\mathbb Z)^2\oplus(\mathbb Z/4\mathbb Z)^3\oplus\mathbb Z/12\mathbb Z
\quad\text{versus}\quad
(\mathbb Z/2\mathbb Z)^4\oplus(\mathbb Z/4\mathbb Z)^2\oplus\mathbb Z/12\mathbb Z.
\]

This is a concrete arithmetic refinement not determined by either permutation zeta function.

## Assumptions and scope

The base field is any finite field of odd characteristic; no genericity hypothesis on the genus-two curve or the six branch points is imposed beyond geometric distinctness. The six Weierstrass points form a Frobenius-stable set. The quartic embedding uses a rational symmetric theta characteristic; one exists over a finite field in this genus (for each cycle partition of six letters, a Weierstrass point or a partition into complementary triples is Frobenius-fixed). The node and trope configurations are intrinsic; different rational theta choices merely change their simultaneous labels.

We are studying the free integral permutation modules on the geometric **singular points and trope planes** and their incidence map, not the Neron--Severi lattice of the minimal K3 resolution, the zeta function of the K3 surface, or an arithmetic Brauer group. The classification concerns ordinary cokernel coinvariants \(Q_F\), not a claim that \(Q_F\) equals the fixed subgroup \(Q^F\) as a Galois module. Their cardinalities do agree because \(Q\) is finite.

## Proof

**1. Standard labels and incidence.** Number the geometric Weierstrass points by \(E=\{1,\ldots,6\}\). Label the sixteen nodes by a distinguished \(P_0\) and fifteen \(P_{ij}\) for unordered pairs \(\{i,j\}\subset E\); these correspond to the sixteen points of \(J[2]\). Label tropes by six \(T_i\) and ten \(T_{A\mid B}\), with \(A\sqcup B=E\), \(\#A=\#B=3\), and \(A\mid B=B\mid A\). Their incidence is exactly

\[
\begin{split}
T_i &: \{P_0\}\cup\{P_{ij}:j\ne i\},\\
T_{A\mid B} &: \{P_{ij}:\{i,j\}\subseteq A\ \text{or}\ \{i,j\}\subseteq B\}.
\end{split}
\]

These are the classical Kummer labels; the six odd theta characteristics give the \(T_i\), and the ten even ones give the \(T_{A\mid B}\). The labels are functorial for permutation of the Weierstrass points, so their incidence matrix \(M\), with nodes as rows and tropes as columns, satisfies \(P_N(\sigma)M=MP_T(\sigma)\) for all \(\sigma\in S_6\).

**2. Rational isomorphism and integral obstruction.** Every node is on six tropes and every pair of distinct nodes lies together on precisely two tropes. Thus

\[
MM^{\mathsf T}=4I_{16}+2J_{16},
\]

where \(J_{16}\) is the all-ones matrix. Its eigenvalues are \(36\) once and \(4\) fifteen times. Hence \(\lvert\det M\rvert=6\cdot2^{15}=3\cdot2^{16}\), which proves injectivity and a rational Galois-module isomorphism. Over \(\mathbb Z\), build the matrix explicitly from the preceding incidence rule and perform elementary unimodular integer row and column reductions. Its exact Smith diagonal is

\[
\operatorname{SNF}_{\mathbb Z}(M)=
\operatorname{diag}(1,1,1,1,1,1,2,2,2,2,4,4,4,4,4,12).
\]

This computation is reproduced exactly by `verify.py` and independently cross-checked against the determinant identity; in particular there is no inference from merely a rational-rank test. As the rational Galois characters agree, the point-count equality and identical zeta functions follow for all finite extensions. (The two \(S_6\)-sets themselves are **not** isomorphic under the full \(S_6\): nodes have a globally fixed \(P_0\), whereas tropes have no globally fixed element. This does not preclude a noncanonical isomorphism of sets under any one cyclic Frobenius subgroup.)

**3. Exact arithmetic coinvariants.** For a Frobenius permutation \(\sigma\in S_6\), let \(P_N(\sigma)\) be its integral permutation matrix on nodes. Since \(M\) is equivariant, the coinvariants of the finite group \(Q\) admit the exact presentation

\[
Q_F\cong\mathbb Z^{16}/\bigl(M\mathbb Z^{16}+(P_N(\sigma)-I_{16})\mathbb Z^{16}\bigr).
\]

Take the Smith normal form of the **explicit \(16\times32\) integer matrix** \([M\mid P_N(\sigma)-I_{16}]\). Cycle-conjugate \(\sigma\)'s yield isomorphic groups, so the eleven partitions of six exhaust the cases. The full eleven-row table is the resulting set of invariant factors. Every computation is over \(\mathbb Z\), using exact Smith reductions, not modular heuristics or floating-point ranks. The accompanying verifier also directly checks all 720 permutations of six letters for incidence equivariance and matching node/trope cycle profiles. It is consequently exhaustive for this finite Galois-action classification.

**4. Equal zeta functions, different integral obstruction.** In the two named Frobenius types, directly inspect the table or the saved Smith calculation. Both finite etale schemes have four fixed points and six two-cycles, so all their extension point-count sequences match. Their coinvariant groups contain respectively two versus four direct \(\mathbb Z/2\mathbb Z\) invariant factors, with correspondingly different \(\mathbb Z/4\mathbb Z\) factors. The Smith invariants uniquely classify finite abelian groups, proving the distinction.

## Verification

Run `python verify.py` after installing `sympy>=1.12` (see `requirements.txt`). The script constructs all sixteen nodes and tropes from six labels, constructs their \(16\times16\) incidence matrix, and checks both matrix products, the determinant, and all Smith factors. It enumerates all 720 elements of \(S_6\) to check equivariance, then constructs and checks the complete eleven-class \(16\times32\) Smith classification. Its final output is `VERIFY_OK: 720 equivariant incidence actions, Kummer 16x16 Smith form, 11 exact Frobenius coinvariant groups`. No outsourced certificate or independent audit is asserted.

## Relationship to prior work

The geometric Kummer \((16,6)\) configuration and its explicit labels are classical; Kumar, *K3 Surfaces Associated with Curves of Genus Two*, §4.2, supplies precisely the node and trope labeling used above. Mehran's *Double Covers of Kummer Surfaces* is an earlier treatment of Kummer geometry and integral lattice structures, but it addresses double covers and period lattices, not the integral incidence coinvariant table. The general \((16,6,2)\) biplane identity also makes rational invertibility an unsurprising consequence of established incidence design theory. The proposed added arithmetic content is the exact **integral** incidence cokernel and its Frobenius-coinvariant classification, especially the distinction between two zeta-indistinguishable Frobenius types.

## Limitations

These are combinatorial Galois-module invariants attached to actual Kummer configurations, not assertions that the surface's Picard group, Brauer group, or entire zeta function differs accordingly. For the comparison, equality of finite-etale zeta functions does not imply equality of incidence coinvariant groups; the argument does not assert converses. The standard symmetric-design identity alone determines the determinant but does not, without additional integer reductions, determine the full Smith factors. Searches of accessible sources did not locate the specific arithmetic classification; historical uniqueness is unproved, and tables in older design-theory literature could contain the Smith invariants or equivalent coinvariant calculations. Characteristic two and non-Jacobian Kummer forms are outside scope.

## References

1. A. Kumar, *K3 Surfaces Associated with Curves of Genus Two*, arXiv:math/0701669, §4.2, especially the explicit node and trope labels and their Picard intersection relations; original preprint 24 January 2007. https://arxiv.org/abs/math/0701669
2. A. Mehran, *Double Covers of Kummer Surfaces*, arXiv:math/0611752, original preprint 24 November 2006; geometry and lattice context, not a claim of the present Smith classification. https://arxiv.org/abs/math/0611752
3. *Degenerations of Gushel--Mukai fourfolds, with a view towards irrationality proofs*, *European Journal of Mathematics* (2018), §4, Definitions 4.10 and Remark 4.11, recalls precisely the \((16,6,2)\) Kummer configuration. https://doi.org/10.1007/s40879-018-0227-z
