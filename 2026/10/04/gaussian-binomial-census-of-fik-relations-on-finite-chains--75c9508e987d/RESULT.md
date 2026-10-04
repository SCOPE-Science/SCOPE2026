# Gaussian-binomial census of FIK relations on finite chains
## Finding

Let
\[
C_n=(\{1,\ldots,n\},\leq)
\]
be the \(n\)-world intuitionistic chain. A binary modal relation
\[
R\subseteq C_n\times C_n
\]
is **forward-confluent** in the sense of FIK when
\[
i\leq i'
\ \text{and}\
iRj
\quad\Longrightarrow\quad
\exists j'\,
\bigl(
i'Rj'
\ \text{and}\
j\leq j'
\bigr).
\]

For each source world \(i\), write
\[
S_i=\{j:iRj\}.
\]

Then \(R\) is forward-confluent if and only if the following two conditions hold:

1. the set of indices with nonempty fibers is a suffix
\[
\{s,s+1,\ldots,n\}
\]
for some \(s\), or is empty; and
2. on that suffix, the maxima
\[
m_i=\max S_i
\]
are weakly nondecreasing.

There is no further restriction on the internal elements of a nonempty fiber.

Consequently, if exactly \(k\) source fibers are nonempty, then the number of forward-confluent relations is
\[
\begin{bmatrix}
n+k-1\\
k
\end{bmatrix}_{2},
\]
and the exact total number is
\[
\boxed{
F_n=
\sum_{k=0}^{n}
\begin{bmatrix}
n+k-1\\
k
\end{bmatrix}_{2}.
}
\]

The first values are
\[
F_1=2,\qquad
F_2=11,\qquad
F_3=198,\qquad
F_4=13377,
\]
\[
F_5=3523028,\qquad
F_6=3661468103.
\]

The asymptotic size is also explicit:
\[
\boxed{
F_n
\sim
C\,2^{n(n-1)},
\qquad
C=
\prod_{j=1}^{\infty}
(1-2^{-j})^{-1}
=
3.462746619455064\ldots
}
\]

Since there are
\[
2^{n^2}
\]
binary relations on an \(n\)-point set, the proportion that are FIK-forward-confluent on the chain satisfies
\[
\frac{F_n}{2^{n^2}}
\sim
C\,2^{-n}.
\]

Thus forward confluence has a particularly simple row-normal form on chains and removes asymptotically only about \(n\) binary degrees of freedom from an arbitrary modal relation.

## Assumptions and scope

Gao and Olivetti use the standard bi-relational semantics for FIK. A frame
\[
(W,\leq,R)
\]
consists of an intuitionistic preorder and a modal relation satisfying forward confluence:
\[
x\leq x',
\ xRz
\quad\Longrightarrow\quad
\exists z'\,
\bigl(
x'Rz'
\ \text{and}\
z\leq z'
\bigr).
\]

The present result specializes the intuitionistic preorder to a finite chain but leaves the modal relation completely arbitrary subject to forward confluence.

The count is for labelled worlds and labelled relations. No quotient by order automorphisms is taken; a finite chain has only the identity order automorphism anyway.

The Gaussian binomial coefficient is evaluated at
\[
q=2.
\]
The identity used below is the standard complete-homogeneous specialization
\[
h_k(1,q,\ldots,q^{n-1})
=
\begin{bmatrix}
n+k-1\\k
\end{bmatrix}_q.
\]

## Proof

Assume first that \(R\) is forward-confluent.

If
\[
S_i\ne\varnothing
\]
and
\[
i\leq i',
\]
choose any
\[
j\in S_i.
\]
Forward confluence gives some
\[
j'\in S_{i'}
\]
with
\[
j\leq j'.
\]
Hence
\[
S_{i'}\ne\varnothing.
\]
Therefore the nonempty fibers form a suffix of the source chain.

Now suppose both
\[
S_i,S_{i'}\ne\varnothing
\]
with
\[
i\leq i'.
\]
Take
\[
j=\max S_i.
\]
Forward confluence supplies
\[
j'\in S_{i'}
\]
with
\[
j\leq j'.
\]
Thus
\[
\max S_i
\leq
\max S_{i'}.
\]
So the fiber maxima are weakly nondecreasing.

Conversely, suppose the nonempty fibers form a suffix and their maxima are weakly nondecreasing. If
\[
i\leq i'
\quad\text{and}\quad
iRj,
\]
then \(S_i\ne\varnothing\), hence \(S_{i'}\ne\varnothing\). Put
\[
j'=\max S_{i'}.
\]
Since
\[
j\leq \max S_i\leq\max S_{i'},
\]
we have
\[
i'Rj'
\quad\text{and}\quad
j\leq j'.
\]
Thus forward confluence holds.

This proves the row-normal form.

Now fix the number \(k\) of nonempty source fibers. Their source positions are forced: they are the last \(k\) worlds. Write their maxima in source order as
\[
1\leq m_1\leq\cdots\leq m_k\leq n.
\]

For a fixed maximum \(m\), the number of nonempty subsets of \(\{1,\ldots,n\}\) having maximum exactly \(m\) is
\[
2^{m-1},
\]
because \(m\) must be present while each smaller point can be chosen independently.

Therefore the number with exactly \(k\) nonempty fibers is
\[
\sum_{1\leq m_1\leq\cdots\leq m_k\leq n}
2^{(m_1-1)+\cdots+(m_k-1)}.
\]
This is
\[
h_k(1,2,4,\ldots,2^{n-1}),
\]
hence
\[
\begin{bmatrix}
n+k-1\\k
\end{bmatrix}_{2}.
\]

Summing over
\[
0\leq k\leq n
\]
gives
\[
F_n=
\sum_{k=0}^{n}
\begin{bmatrix}
n+k-1\\k
\end{bmatrix}_{2}.
\]

For the asymptotic, use the product formula
\[
\begin{bmatrix}
n+k-1\\k
\end{bmatrix}_{2}
=
2^{k(n-1)}
\frac{
\prod_{j=n}^{n+k-1}(1-2^{-j})
}{
\prod_{j=1}^{k}(1-2^{-j})
}.
\]

The term with
\[
k=n
\]
satisfies
\[
2^{-n(n-1)}
\begin{bmatrix}
2n-1\\n
\end{bmatrix}_{2}
=
\frac{
\prod_{j=n}^{2n-1}(1-2^{-j})
}{
\prod_{j=1}^{n}(1-2^{-j})
}
\longrightarrow
\prod_{j=1}^{\infty}(1-2^{-j})^{-1}
=
C.
\]

For every
\[
k\leq n-1,
\]
the product ratio is bounded by \(C\), so
\[
2^{-n(n-1)}
\begin{bmatrix}
n+k-1\\k
\end{bmatrix}_{2}
\leq
C\,2^{-(n-k)(n-1)}.
\]
Summing these bounds gives a quantity tending to zero. Hence
\[
F_n\sim C\,2^{n(n-1)}.
\]

Dividing by the total number
\[
2^{n^2}
\]
of binary relations yields
\[
F_n2^{-n^2}
\sim
C\,2^{-n}.
\]

## Verification

The bundled checker performs two independent calculations.

First, for
\[
1\leq n\leq4,
\]
it enumerates every one of the
\[
2^{n^2}
\]
binary relations on the labelled chain and tests the published forward-confluence condition directly. It independently tests the suffix-plus-monotone-maxima normal form and confirms exact equivalence relation by relation.

The resulting exact counts are
\[
2,\ 11,\ 198,\ 13377.
\]

Second, it evaluates the Gaussian-binomial formula recursively through
\[
n=12
\]
and checks agreement with the direct counts wherever exhaustive enumeration is feasible. It also checks the fixed-\(k\) counts against explicit weakly increasing maximum sequences for small \(n\).

The finite enumeration is not used as a proof for arbitrary \(n\). The theorem follows from the direct row characterization and the standard Gaussian-binomial identity.

## Relationship to prior work

Balbiani, Gao, Gencer, and Olivetti introduced FIK as the intuitionistic modal logic of forward-confluent bi-relational frames and proved a finite model property through their proof calculus.

Gao and Olivetti's 2026 paper returns to FIK from the proof-theoretic and complexity side. It states the same forward-confluence frame condition, emphasizes the role of finite countermodel search, and proves an \(\mathsf{EXPSPACE}\) upper bound using a shallow calculus.

The checked papers do not enumerate forward-confluent relations on finite chains, give a chain normal form for relation rows, or connect the finite frame count with Gaussian binomial coefficients.

The closest prior internal comparison is a classification of expansive total relations between finite strict chains. That result imposes nonempty rows and strict growth of both row minima and maxima. FIK forward confluence is structurally different: it permits an empty prefix of rows, places no condition on row minima or internal elements, and requires only weak growth of maxima across the nonempty suffix.

The census is therefore not a special case of that expansive-relation classification.

## Limitations

The theorem counts relations only when the intuitionistic preorder is a chain. General finite posets can have branching witnesses, and the single-maximal-element reduction no longer applies.

The count concerns frames, not modal theories modulo bisimulation or logical equivalence.

The asymptotic constant describes labelled chain frames. It does not imply an asymptotic statement for arbitrary finite intuitionistic preorders.

No lower bound on the computational complexity of FIK validity is derived from the census. Its value is as an exact finite-frame structural baseline for model generation and complexity experiments.

## References

[1] Han Gao and Nicola Olivetti, “Taming Complexity in Intuitionistic Modal Logic: The Case of FIK and Its Shallow Calculus,” arXiv:2606.31877, first posted 30 June 2026; *Electronic Proceedings in Theoretical Computer Science* 447 (2026), 407–426. DOI:10.4204/EPTCS.447.23.

[2] Philippe Balbiani, Han Gao, Çiğdem Gencer, and Nicola Olivetti, “A Natural Intuitionistic Modal Logic: Axiomatization and Bi-Nested Calculus,” *Leibniz International Proceedings in Informatics* 288 (CSL 2024), Article 13. DOI:10.4230/LIPIcs.CSL.2024.13; arXiv:2309.06309.

[3] Richard P. Stanley, *Enumerative Combinatorics*, Volume 1, second edition, Cambridge University Press, 2012.
