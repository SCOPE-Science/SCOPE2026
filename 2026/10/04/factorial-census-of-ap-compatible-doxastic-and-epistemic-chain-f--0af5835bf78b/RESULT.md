# Factorial census of AP-compatible doxastic and epistemic chain frames
## Finding

Fix the finite chain
\[
C_n=\{0<1<\cdots<n-1\}
\]
with \(n\ge 1\). For a binary relation \(R\) on \(C_n\), impose Balbiani's two conditions:

1. \(R\) is **doxastic**: \(iRj\) implies \(i\le j\);
2. \(R\) is **\(\mathbf{AP}\)-compatible**: if \(i\le k\) and \(kRj\), then \(iRj\).

Then \(R\) is uniquely encoded by a vector
\[
(c_0,\ldots,c_{n-1}),\qquad c_j\in\{-1,0,\ldots,j\},
\]
where
\[
iRj\quad\Longleftrightarrow\quad i\le c_j
\]
and \(c_j=-1\) means that the \(j\)-th incoming column is empty.

Consequently the exact number of \(\mathbf{AP}\)-compatible doxastic relations on \(C_n\) is
\[
\prod_{j=0}^{n-1}(j+2)=(n+1)!.
\]

Within this family:

- founded frames, equivalently doxastic basic frames, are exactly the nonempty relations, so their number is
\[
(n+1)!-1;
\]
- epistemic frames are exactly the visionary, equivalently futuristic, doxastic frames; in the chain parametrization these are precisely the relations with
\[
c_{n-1}=n-1,
\]
so their number is
\[
n!.
\]

Thus the exact fraction of \(\mathbf{AP}\)-compatible doxastic chain frames that are epistemic is
\[
\frac{1}{n+1}.
\]

## Assumptions and scope

The underlying intuitionistic preorder is the fixed labelled chain \(C_n\). Relations are counted on this fixed chain, not modulo order isomorphism. Since a finite chain has no nontrivial order automorphism, the labelled and order-isomorphism counts coincide here.

The terminology basic, visionary, futuristic, doxastic, founded, epistemic, and \(\mathbf{AP}\)-compatible is exactly Balbiani's. In particular, a doxastic frame is founded when it is basic, and is epistemic when it is visionary or, equivalently for doxastic frames, futuristic.

No claim is made about arbitrary finite preorders, where incoming downsets need not be initial segments and the enumeration is no longer factorial.

## Proof

For each \(j\in C_n\), let
\[
I_j=\{i\in C_n:iRj\}.
\]
Doxasticity gives
\[
I_j\subseteq\{0,\ldots,j\}.
\]
If \(k\in I_j\) and \(i\le k\), then \(i\le k\) and \(kRj\); \(\mathbf{AP}\)-compatibility therefore gives \(iRj\). Hence \(I_j\) is a downset of the finite chain \(\{0,\ldots,j\}\). Every such downset is uniquely either empty or an initial segment
\[
\{0,\ldots,c_j\}
\]
for a unique \(c_j\in\{0,\ldots,j\}\). Writing \(c_j=-1\) for the empty case yields the claimed vector parametrization.

Conversely, any choice \(c_j\in\{-1,0,\ldots,j\}\) defines a relation by \(iRj\) iff \(i\le c_j\). Since \(c_j\le j\), doxasticity holds. Since every incoming column is downward closed, \(\mathbf{AP}\)-compatibility holds. The choices are independent, and the \(j\)-th coordinate has \(j+2\) possibilities, proving
\[
\#\mathcal D_n^{\mathbf{AP}}=(n+1)!.
\]

For basicity, suppose \(R\ne\varnothing\) and choose \(vRt\). For arbitrary \(s\in C_n\), let \(u=\max\{s,v\}\). Then
\[
s\le u,\qquad u\ge v,\qquad vRt,
\]
so \(s\,(\le\circ\ge\circ R)\,t\). Thus every state satisfies the basic-frame condition. The empty relation plainly fails it. Therefore, among doxastic frames, founded is equivalent on a chain to nonemptiness, giving \((n+1)!-1\) founded relations.

Now suppose \(R\) is \(\mathbf{AP}\)-compatible. If the frame is visionary, then for every \(s\) there are \(u,t\) with \(s\le u\) and \(uRt\); \(\mathbf{AP}\)-compatibility gives \(sRt\). Thus visionary is equivalent here to seriality. For the top point \(n-1\), doxasticity permits only one possible successor, namely \(n-1\) itself. Hence seriality forces
\[
(n-1)R(n-1),
\]
which in the column parametrization is exactly \(c_{n-1}=n-1\).

Conversely, if \(c_{n-1}=n-1\), then every \(s\in C_n\) satisfies \(sR(n-1)\), so \(R\) is serial and hence visionary. Balbiani proves that on every doxastic frame, visionary and futuristic coincide; therefore this is exactly the epistemic condition. Fixing the last coordinate leaves
\[
\prod_{j=0}^{n-2}(j+2)=n!
\]
independent choices.

## Verification

A direct exhaustive checker enumerates all binary relations for \(1\le n\le4\), tests the definitions of doxasticity, \(\mathbf{AP}\)-compatibility, basicity, visionaryness, and futuristicness literally, and obtains:

\[
\begin{array}{c|cccc}
n & \mathbf{AP}\text{-doxastic} & \text{founded} & \text{visionary} & \text{futuristic}\\
\hline
1&2&1&1&1\\
2&6&5&2&2\\
3&24&23&6&6\\
4&120&119&24&24
\end{array}
\]

These match \((n+1)!\), \((n+1)!-1\), and \(n!\). The finite enumeration is only a consistency check; the proof above establishes the formulas for every \(n\ge1\).

## Relationship to prior work

Balbiani introduces the two-modality intuitionistic doxastic and epistemic semantics, defines the six frame properties used here, and proves in particular that doxastic visionary frames are exactly doxastic futuristic frames. The same paper identifies \(\mathbf{AP}\)-compatibility by the closure condition
\[
\le\circ R\subseteq R
\]
and relates \(\mathbf{AP}\)-compatible doxastic and epistemic frames to the relational semantics of intuitionistic doxastic and epistemic logic.

The article develops correspondence, axiomatization, and completeness, but does not classify or count the admissible relations on finite chains. Searches for finite-chain, linear-order, factorial, and exact-count formulations did not locate this parametrization in the source or in the checked literature databases.

The present result is a finite structural sharpening of those definitions: on a chain the entire relation is reduced to independent column cutoffs, and the epistemic condition becomes a single extremal constraint on the top column.

## Limitations

The factorial formulas depend essentially on the underlying order being a chain. For a general finite preorder, incoming \(\mathbf{AP}\)-closed columns can be arbitrary downsets subject to doxasticity, and the simple product formula need not survive.

The originality search found no equivalent finite-chain census, but an unindexed combinatorial observation could exist. The result concerns frame enumeration and does not by itself yield new completeness or decidability theorems for the associated logics.

## References

[1] Philippe Balbiani, “Intuitionistic epistemic logic with two modal operators,” *Synthese* 206, article 169 (2025). DOI:10.1007/s11229-025-05226-w.
