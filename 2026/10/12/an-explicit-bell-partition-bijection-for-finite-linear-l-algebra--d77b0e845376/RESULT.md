# An explicit Bell-partition bijection for finite linear L-algebras

## Finding
For the fixed chain
\[
L_n=\{x_0>x_1>\cdots>x_{n-1}\},\qquad e=x_0,
\]
there is an explicit recursive bijection \(\Phi_n\) between linear \(L\)-algebra structures on \(L_n\) and set partitions of the non-unit set \(\{x_1,\ldots,x_{n-1}\}\).

For \(n=1\), the unique algebra maps to the empty partition. For \(n\ge2\), let \(x_m\) be the smallest invariant element of a linear \(L\)-algebra \(X\). The published decomposition theorem associates to \(X\) its restriction \(X'\) to \(\{x_0,\ldots,x_{m-1}\}\) and the set
\[
A_X=\{x_m\cdot x_j:j>m\}\subseteq\{x_1,\ldots,x_{n-2}\},
\]
with \(|A_X|=n-m-1\). Put
\[
C_X=\{x_1,\ldots,x_{n-2}\}\setminus A_X,
\]
and let
\[
\iota_X:\{x_1,\ldots,x_{m-1}\}\longrightarrow C_X
\]
be the unique order-preserving bijection. Then
\[
\boxed{\Phi_n(X)=\{\iota_X(B):B\in\Phi_m(X')\}\cup\{A_X\cup\{x_{n-1}\}\}.}
\]

Thus the distinguished block containing the new least point \(x_{n-1}\) records exactly the extension parameter \(A_X\); deleting that block and standardizing the complement recovers the smaller algebra. This gives the explicit bijection asked for in Problem 4.6 of Dietzel--Menchón--Vendramin.

## Assumptions and scope
The result uses the definition of a linear \(L\)-algebra and the one-point extension/decomposition theorem of Dietzel--Menchón--Vendramin. It concerns algebra structures on a fixed finite chain, with the logical unit at the top. No new enumeration formula is claimed: the Bell-number count \(B_{n-1}\) is prior work. The new statement is the explicit recursive correspondence with set partitions.

## Proof
The source proves that if \(x_m\) is the smallest invariant element of \(X\), then \(X\) is uniquely determined by two pieces of data: the smaller linear algebra \(X'\) on the initial chain \(\{x_0,\ldots,x_{m-1}\}\), and a subset \(A_X\subseteq\{x_1,\ldots,x_{n-2}\}\) of cardinality \(n-m-1\). Conversely, every such pair has a unique extension to a linear \(L\)-algebra on \(L_n\).

Assume inductively that \(\Phi_m\) bijects linear \(L\)-algebras on \(L_m\) with partitions of \(\{x_1,\ldots,x_{m-1}\}\). Since \(|C_X|=m-1\), the unique order-preserving bijection \(\iota_X\) transports \(\Phi_m(X')\) to a partition of \(C_X\). Adding the block \(A_X\cup\{x_{n-1}\}\) therefore produces a partition of all non-unit points of \(L_n\).

For the inverse, start with a partition \(\pi\) of \(\{x_1,\ldots,x_{n-1}\}\). Let \(B\) be the unique block containing \(x_{n-1}\), and define
\[
A=B\setminus\{x_{n-1}\},\qquad
C=\{x_1,\ldots,x_{n-2}\}\setminus A,\qquad
m=|C|+1.
\]
Let \(\iota:\{x_1,\ldots,x_{m-1}\}\to C\) be the unique order-preserving bijection. Pull every block of \(\pi\setminus\{B\}\) back along \(\iota\); this gives a partition \(\pi'\) of \(\{x_1,\ldots,x_{m-1}\}\). By induction, \(\pi'\) determines a unique smaller algebra \(X'\). The published extension theorem then gives a unique algebra \(X\) having smallest invariant element \(x_m\), restriction \(X'\), and extension set \(A_X=A\).

The two constructions are inverse. In the forward direction, the block containing \(x_{n-1}\) immediately recovers \(A_X\), hence its complement \(C_X\), the value of \(m\), and the standardizing map \(\iota_X\). The recursive partition then recovers \(X'\), and uniqueness of the extension recovers \(X\). The reverse composition is identical in the other direction. This proves bijectivity for every \(n\) by induction.

## Verification
A bundled verifier independently implements the published one-point extension rule and the recursive partition map. It enumerates every set partition through \(n=8\), builds the corresponding multiplication table, verifies the \(L\)-algebra axioms and that the induced order is the prescribed chain, and checks exact round-trip recovery of the original partition. It checks \(1156\) partitions/tables and reports:

`VERIFY_OK 718575 exact assertions; 1156 partitions/tables checked through n=8`

The computation is a finite consistency check; the proof above establishes the result for all \(n\).

## Relationship to prior work
Dietzel, Menchón, and Vendramin proved that the number of linear \(L\)-algebra structures on an \(n\)-element chain is the Bell number \(B_{n-1}\), using a recursive one-point decomposition. Immediately afterward, their Problem 4.6 asks for an explicit bijection with set partitions. A September 2025 seminar presentation by Vendramin still displayed the same problem after stating the Bell-number theorem. Targeted searches for an explicit solution under the terms “linear \(L\)-algebra,” “Bell numbers,” “partitions,” and “explicit bijection” found the counting theorem and the later open-problem slide, but no equivalent construction.

The present map is not merely an abstract consequence of equal cardinalities: it identifies the block containing the newest least chain element with the source's concrete extension parameter, and recursively standardizes the complementary points.

## Limitations
The proof depends on the published uniqueness and decomposition results for finite linear \(L\)-algebras. The bundled exhaustive computation reaches only \(n=8\), so it is not itself a proof of the infinite family. The literature search cannot exclude an unindexed note, private communication, or a solution published after the September 2025 presentation. Independent audit has not been performed.

## References
C. Dietzel, P. Menchón, and L. Vendramin, *On the enumeration of finite L-algebras*, arXiv:2206.04955; Mathematics of Computation, DOI: 10.1090/mcom/3814.

L. Vendramin, *L-algebras: the Yang--Baxter equation and algebraic logic*, Panglobal Algebra and Logic Seminar, September 2025.
