# Minimum-size independence graphs of odd generalized dihedral groups

## Finding

Let \(A\) be a finite abelian group of odd order and assume
\[
d=d(A)\ge2.
\]
Put
\[
G=\operatorname{Dih}(A)=A\rtimes\langle s\rangle,
\qquad s^2=1,
\qquad a^s=-a
\]
in additive notation for \(A\).

For each prime \(p\mid |A|\), let \(A_p\) be the Sylow \(p\)-subgroup and define
\[
V_p=A_p/pA_p,
\qquad
r_p=\dim_{\mathbf F_p}V_p.
\]
Thus
\[
d=\max_p r_p.
\]
Set
\[
P=\{p:r_p=d\},
\qquad
Q=\{p:r_p=d-1\},
\qquad
\Phi=\Phi(A)=\prod_p pA_p.
\]
For \(a\in A\), write \(\bar a_p\) for its image in \(V_p\).

Then
\[
\boxed{d(G)=d+1.}
\]
Call a rotation \(a\in A\) **active** when
\[
\bar a_p\ne0
\qquad\text{for every }p\in P.
\]
The graph \(\Gamma_{d+1}(G)\), whose edges are the pairs extendible to a generating set of minimum cardinality, is completely described as follows.

- A rotation is non-isolated exactly when it is active.
- Every reflection is non-isolated.
- A rotation \(a\) and a reflection \(bs\) are adjacent exactly when \(a\) is active.
- Two distinct reflections \(as\) and \(bs\) are adjacent exactly when \(b-a\) is active.
- Two distinct rotations \(a,b\) are adjacent exactly when
  \[
  \bar a_p,\bar b_p\text{ are linearly independent in }V_p
  \quad(p\in P),
  \]
  and
  \[
  (\bar a_p,\bar b_p)\ne(0,0)
  \quad(p\in Q).
  \]

There are
\[
N
=|\Phi|\prod_{p\in P}(p^d-1)\prod_{p\notin P}p^{r_p}
=|A|\prod_{p\in P}(1-p^{-d})
\]
active rotations. Hence every reflection has degree
\[
\boxed{2N.}
\]

For an active rotation \(a\), define
\[
Q_0(a)=\{p\in Q:\bar a_p=0\}.
\]
The number of rotation neighbours of \(a\) is
\[
R(a)=|\Phi|
\prod_{p\in P}(p^d-p)
\prod_{p\in Q_0(a)}(p^{d-1}-1)
\prod_{p\in Q\setminus Q_0(a)}p^{d-1}
\prod_{r_p\le d-2}p^{r_p}.
\]
Therefore
\[
\boxed{\deg(a)=|A|+R(a)}
\]
for every active rotation, while inactive rotations have degree \(0\).

Finally,
\[
\boxed{|g|\mid\deg_{\Gamma_{d(G)}(G)}(g)\quad\text{for every }g\in G.}
\]
Thus Lucchini's degree-divisibility question has an affirmative answer for every generalized dihedral group with finite abelian odd kernel of generator rank at least two.

## Assumptions and scope

For a finite group \(X\), the graph \(\Gamma_u(X)\) has vertex set \(X\); two distinct elements are adjacent when they can be extended to a generating set of \(X\) of size \(u\). The parameter used here is \(u=d(X)\), the minimum number of generators.

The kernel \(A\) is finite abelian of odd order. No homocyclic, elementary-abelian, or single-prime assumption is imposed. The hypothesis \(d(A)\ge2\) isolates the higher-rank regime: the cyclic-kernel case gives a two-generated group and lies in the classical generating-graph setting.

The inversion action is fixed-point-free on \(A\setminus\{0\}\) because \(|A|\) is odd, so \(G\) is a generalized dihedral Frobenius group.

## Proof

We first record a completion criterion inside \(A\).

Let \(a_1,\ldots,a_k\in A\), where \(k\le d\). These elements can be completed by \(d-k\) further elements to a generating \(d\)-tuple of \(A\) if and only if, for every prime \(p\mid |A|\),
\[
\dim_{\mathbf F_p}\langle\bar a_{1,p},\ldots,\bar a_{k,p}\rangle
\ge r_p-d+k.
\tag{1}
\]
Indeed, a \(d\)-tuple generates \(A\) exactly when its images span every Frattini quotient \(V_p=A_p/pA_p\). Necessity of (1) follows because only \(d-k\) additional vectors remain. Conversely, if (1) holds, choose in each \(V_p\) enough additional vectors to obtain a spanning \(d\)-tuple, padding with zeros when fewer are needed. The Sylow components of each added vector may be chosen independently, and arbitrary lifts to \(A\) then complete the original tuple.

We next reduce generation in \(G\) to generation in \(A\). Any generating set of \(G\) contains a reflection. Choose one of them, say \(a_0s\). Replacing every other reflection \(a_is\) by the rotation
\[
(a_is)(a_0s)=a_i-a_0
\]
does not change the generated subgroup. Thus a set containing \(a_0s\) generates \(G\) precisely when the resulting rotations generate \(A\).

A generating set of \(G\) of size \(n\) therefore yields at most \(n-1\) rotations generating \(A\), so \(n-1\ge d\). Conversely, one reflection together with any \(d\)-element generating set of \(A\) generates \(G\). Hence
\[
d(G)=d+1.
\]

Consider first one prescribed rotation \(a\). It can lie in a generating set of size \(d+1\) exactly when \(a\) can be completed to \(d\) generators of \(A\). Applying (1) with \(k=1\) shows that the only non-vacuous conditions occur when \(r_p=d\), and then the condition is \(\bar a_p\ne0\). This proves the active-rotation criterion. Every reflection can be extended by a fixed \(d\)-element generating set of \(A\), so every reflection is non-isolated.

For a rotation-reflection pair \(a,bs\), normalize the reflection to the chosen base reflection. The remaining prescribed rotation is still \(a\), so (1) with \(k=1\) gives adjacency exactly when \(a\) is active.

For two reflections \(as,bs\), normalize \(as\) as the base. The second reflection contributes the rotation \(b-a\). Thus the pair is adjacent exactly when \(b-a\) is active.

For two rotations \(a,b\), apply (1) with \(k=2\). If \(r_p=d\), the required rank is \(2\), so \(\bar a_p\) and \(\bar b_p\) must be linearly independent. If \(r_p=d-1\), the required rank is \(1\), so they must not both vanish. If \(r_p\le d-2\), no condition remains. This gives the full adjacency classification.

Counting active rotations prime by prime gives
\[
N
=|\Phi|\prod_{p\in P}(p^d-1)\prod_{p\notin P}p^{r_p}.
\]
Every reflection is adjacent to all \(N\) active rotations. It is also adjacent to exactly \(N\) other reflections, since translation by its parameter is a bijection on \(A\) and the difference must be active. Hence every reflection has degree \(2N\).

Fix an active rotation \(a\). It is adjacent to all \(|A|\) reflections. For a rotation \(b\), the number of possible residues \(\bar b_p\) is:

- \(p^d-p\) when \(p\in P\), because \(\bar b_p\) must avoid the one-dimensional span of \(\bar a_p\);
- \(p^{d-1}-1\) when \(p\in Q_0(a)\), because \(\bar b_p\ne0\);
- \(p^{d-1}\) when \(p\in Q\setminus Q_0(a)\), because the rank-one condition is already supplied by \(a\);
- \(p^{r_p}\) when \(r_p\le d-2\), because there is no restriction.

Each residue choice has \(|\Phi|\) total lifts over all primes. Multiplication of these independent counts yields the displayed formula for \(R(a)\), and therefore \(\deg(a)=|A|+R(a)\).

It remains to prove the divisibility statement. Reflections have order \(2\) and degree \(2N\). Inactive rotations have degree \(0\), which is divisible by every positive integer. Let \(a\) be active. Since \(|a|\mid |A|\), it is enough to show \(|a|\mid R(a)\).

Write
\[
A_p\cong\bigoplus_{j=1}^{r_p}C_{p^{\lambda_{p,j}}},
\qquad \lambda_{p,j}\ge1.
\]
Then
\[
v_p(|\Phi(A_p)|)=\sum_j(\lambda_{p,j}-1).
\]
If \(r_p\le d-2\), the factor contributed to \(R(a)\) is \(|A_p|\), so it contains the full \(p\)-part of \(|a|\). If \(r_p=d-1\) and \(\bar a_p\ne0\), the same is true. If \(r_p=d-1\) and \(\bar a_p=0\), then \(a_p\in pA_p\), hence its order has exponent at most \(\max_j\lambda_{p,j}-1\), while
\[
\sum_j(\lambda_{p,j}-1)\ge \max_j\lambda_{p,j}-1.
\]
Finally, if \(r_p=d\), activity gives \(\bar a_p\ne0\). Since \(d\ge2\),
\[
v_p(p^d-p)=1,
\]
so the \(p\)-adic valuation in \(R(a)\) is at least
\[
\sum_j(\lambda_{p,j}-1)+1
\ge \max_j\lambda_{p,j},
\]
which again contains the full order of \(a_p\). Thus \(|a|\mid R(a)\), and consequently \(|a|\mid\deg(a)\).

## Verification

The included replay performs exhaustive finite checks in two genuinely higher-rank examples that exercise different branches of the theorem.

For
\[
A=C_9\times C_3,
\]
it enumerates all three-element subsets of \(G\), tests generation by exact additive subgroup closure after the generalized-dihedral normalization, and reconstructs the whole graph \(\Gamma_3(G)\). It finds \(13608\) minimum generating triples and degree distribution
\[
0^3,\qquad 45^{24},\qquad 48^{27}.
\]
The nonzero isolated rotations are exactly the elements in \(3A\setminus\{0\}\).

For
\[
A=C_3\times C_3\times C_5,
\]
the same exhaustive procedure finds \(60480\) minimum generating triples and degree distribution
\[
0^5,\qquad 69^8,\qquad 75^{32},\qquad 80^{45}.
\]
Here \(r_3=2\) and \(r_5=1\), so the two active-rotation degree strata distinguish whether the \(5\)-component vanishes, directly checking the \(Q_0(a)\) term.

The replay also checks the predicted adjacency relation for every pair and verifies that the order of every vertex divides its degree. It returns `VERIFY_OK`.

Finite enumeration is not used in the universal proof.

## Relationship to prior work

Lucchini introduced the fixed-size graphs \(\Gamma_u(G)\) and explicitly asked whether the order of every element divides its degree in \(\Gamma_{d(G)}(G)\). The paper notes that the divisibility is known for the ordinary generating graph of a two-generated group and gives an example showing that it can fail for \(\Gamma_u(G)\) when \(u\) is not the minimum generator number.

Freedman, Lucchini, Nemmi and Roney-Dougal subsequently studied **rank-independence**, meaning that every noncyclic pair extends to a generating set of minimum size. They classify the groups with that global property. For \(d(G)\ge3\), their theorem forces a semidirect product with an elementary-abelian Sylow subgroup and a cyclic scalar complement. The elementary-abelian generalized-dihedral case is therefore compatible with that classification.

The present theorem addresses the complementary situation where a generalized-dihedral kernel may be non-elementary or may have several Sylow ranks. Such groups generally fail the rank-independence property, so the later classification does not determine which pairs remain adjacent. The formulas above classify every pair anyway, expose the new \(r_p=d-1\) obstruction, give exact degree strata, and prove the degree-divisibility question throughout the whole odd abelian-kernel family of rank at least two.

A separate line of work on minimal Cayley graphs of generalized dihedral groups studies a Cayley graph attached to one fixed irredundant generating set. That is a different graph construction and does not determine pair co-occurrence in minimum generating sets.

Targeted searches using fixed-size independence graph, rank graph, generalized dihedral, odd abelian kernel, Frattini quotient, pair completion, and degree-divisibility terminology did not locate the displayed adjacency or degree formulas.

## Limitations

The kernel is required to be abelian of odd order and the complement has order \(2\) acting by inversion. The proof uses both the Sylow-Frattini decomposition of a finite abelian group and the fact that a reflection normalizes other reflections to rotations by subtraction.

The theorem does not address generalized dihedral groups over abelian groups with nontrivial \(2\)-torsion, nor semidirect products with a larger complement.

The cyclic-kernel case \(d(A)=1\) is excluded from the novelty domain because then \(G\) is two-generated and the order-divides-degree statement belongs to the classical generating-graph theorem.

The result settles Lucchini's divisibility question only for this generalized-dihedral family, not for arbitrary finite groups.

The later rank-independence classification covers the elementary-abelian scalar special case at the level of a global adjacency property; the new content here is the exact graph and degree structure for arbitrary odd abelian kernels, including non-elementary and mixed-Sylow cases.

## References

1. A. Lucchini, “The independence graph of a finite group,” arXiv:2004.14651v1, first public version 30 April 2020; *Monatshefte für Mathematik* 193 (2020), 845–856, DOI 10.1007/s00605-020-01445-0.
2. S. D. Freedman, A. Lucchini, D. Nemmi, C. M. Roney-Dougal, “Finite groups satisfying the independence property,” arXiv:2208.04064v1, first public version 8 August 2022; *International Journal of Algebra and Computation* 33 (2023), 509–545, DOI 10.1142/S021819672350025X.
3. I. García-Marco, K. Knauer, “Coloring minimal Cayley graphs,” arXiv:2405.19543v1, first public version 29 May 2024; *European Journal of Combinatorics* 125 (2025), 104108, DOI 10.1016/j.ejc.2024.104108.
