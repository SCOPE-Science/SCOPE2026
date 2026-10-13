# Positive semidefinite zero forcing sets of wheel graphs
## Finding
Let \(n\ge 5\), let \(m=n-1\), and let \(W_n\) be the wheel obtained from the rim cycle \(R=C_m\) by adding a universal hub \(h\). A set \(S\subseteq V(W_n)\) is a positive semidefinite zero forcing set if and only if exactly one of the following two structural conditions holds:

1. \(h\in S\) and \(|S\cap R|\ge 2\);
2. \(h\notin S\) and \(S\cap R\) contains three consecutive rim vertices, with indices interpreted cyclically.

Consequently, the minimum positive semidefinite zero forcing number is the previously known value
\[
Z_+(W_n)=3,
\]
and the minimum sets are precisely the hub together with any two rim vertices, or three consecutive rim vertices without the hub. Therefore the exact number of minimum sets is
\[
\binom{m}{2}+m=\binom{n}{2}.
\]

The characterization also gives the complete cardinality enumerator. Let \(Q_m(x)\) be the weight enumerator of cyclic binary words of length \(m\) avoiding three consecutive ones. With the state order \(00,01,10,11\), put
\[
T(x)=
\begin{pmatrix}
1&x&0&0\\
0&0&1&x\\
1&x&0&0\\
0&0&1&0
\end{pmatrix}.
\]
Then \(Q_m(x)=\operatorname{tr}(T(x)^m)\), and the positive semidefinite zero forcing polynomial is
\[
\mathcal Z_+(W_n;x)
=x\bigl((1+x)^m-1-mx\bigr)
+(1+x)^m-\operatorname{tr}(T(x)^m).
\]

## Assumptions and scope
Graphs are finite, simple, and undirected. The positive semidefinite color-change rule is the standard component rule: at a stage with blue set \(B\), consider each connected component \(C\) of the white-induced graph. A blue vertex may force a white vertex when it has exactly one neighbor in \(C\). The theorem uses the convention that \(W_n\) has \(n\) vertices, with rim \(C_{n-1}\), and is stated for \(n\ge5\) so that the rim has length at least four.

The polynomial counts every positive semidefinite zero forcing set by its cardinality. The scalar equality \(Z_+(W_n)=3\) is prior work and is not part of the originality claim.

## Proof
Write the rim vertices as \(v_0,\ldots,v_{m-1}\), with indices modulo \(m\).

Suppose first that \(h\in S\). If no rim vertex is blue, then the white rim is the whole cycle and the hub has more than one white neighbor, so no force is possible. If exactly one rim vertex is blue, then the other \(m-1\) rim vertices form one white path. The unique blue rim vertex has two white rim neighbors, while the hub has \(m-1\) white neighbors, so again no first force is possible.

Now assume \(h\in S\) and at least two rim vertices are blue. Every component of the white-induced graph is a path of consecutive white rim vertices. For any nonempty such path component, an endpoint is adjacent along the rim to a blue rim vertex outside the component. That blue rim vertex has exactly one neighbor in the chosen white component, so it can force the endpoint. Repeating this endpoint peeling clears every white path component. Thus the hub-containing sets are positive semidefinite zero forcing exactly when at least two rim vertices are initially blue.

Suppose next that \(h\notin S\). If all rim vertices are blue, any rim vertex has the hub as its unique white neighbor and immediately forces it, so the set succeeds; it also contains three consecutive rim vertices. Otherwise at least one rim vertex is white. Because the white hub is adjacent to every white rim vertex, the white-induced graph is then connected. A blue rim vertex \(v_i\) has the hub as a white neighbor and may additionally have one or both rim neighbors white. Hence \(v_i\) has exactly one white neighbor if and only if both \(v_{i-1}\) and \(v_{i+1}\) are blue. Equivalently, a first force exists if and only if three consecutive rim vertices are blue, in which case the middle one forces the hub. After the hub becomes blue, the first case applies because at least three rim vertices are already blue. If no three consecutive rim vertices are blue, no blue vertex has a unique neighbor in the single white component, so the process is stuck immediately. This proves the characterization.

For the polynomial, hub-containing forcing sets are obtained by choosing at least two of the \(m\) rim vertices, giving
\[
x\bigl((1+x)^m-1-mx\bigr).
\]
Hub-free forcing sets are exactly rim subsets containing a cyclic run of three selected vertices. Their weight enumerator is all rim subsets minus the cyclic binary words avoiding \(111\), namely
\[
(1+x)^m-Q_m(x).
\]
The four-state transfer matrix records the last two bits while appending a zero with weight \(1\) or a one with weight \(x\), with the transition that would create \(111\) deleted. Closing the walk by taking the trace enforces the cyclic boundary condition, so \(Q_m(x)=\operatorname{tr}(T(x)^m)\). Adding the two disjoint hub cases yields the stated polynomial.

## Verification
A standalone exhaustive checker independently implements the positive semidefinite component rule, the structural criterion, direct coefficient counting, and the transfer-matrix polynomial. It verifies every subset of every wheel from \(W_5\) through \(W_{14}\), checks the full coefficient vector in each order, checks the transfer-matrix trace against direct cyclic \(111\)-avoidance, and checks the minimum-set count.

The exact replay output is:

`VERIFY_OK n_range=5..14 subset_checks=32736 criterion_checks=32736 coefficient_checks=200 basis_checks=20 max_order=14`

This finite computation corroborates the theorem but is not used as a proof of the infinite statement.

## Relationship to prior work
Barioli, Barrett, Fallat, Hall, Hogben, Shader, van den Driessche, and van der Holst introduced positive semidefinite zero forcing in their 2010 work on zero forcing parameters and minimum-rank problems. Peters subsequently treated wheels directly: Proposition 3.10 of *Positive semidefinite maximum nullity and zero forcing number* proves \(M_+(W_n)=Z_+(W_n)=3\) for wheels, using a lower bound from a \(K_4\) minor together with an upper bound.

The scalar wheel value is therefore established prior work. The result here is a structural refinement: it classifies every initial set that succeeds, determines every minimum set and their exact number, and gives the full cardinality generating polynomial. The same-object wheel proposition does not contain these stronger statements.

## Limitations
The proof is specific to wheels and uses the universal hub together with the path-component structure left on the rim after the hub is blue. The theorem is stated for \(n\ge5\); the small complete-graph convention at \(W_4\) is deliberately excluded. The originality comparison is best-of-knowledge: the directly relevant wheel theorem was inspected in full context, and broad searches under positive semidefinite zero forcing, wheel, basis, reconfiguration, polynomial, and all-set terminology found no equivalent classification, but poorly indexed enumerative work remains a residual risk.

## References
1. F. Barioli, W. Barrett, S. M. Fallat, H. T. Hall, L. Hogben, B. Shader, P. van den Driessche, and H. van der Holst, *Zero forcing parameters and minimum rank problems*, Linear Algebra and its Applications 433 (2010), 401–411, arXiv:1003.2028v1, https://doi.org/10.1016/j.laa.2010.03.008.
2. T. Peters, *Positive semidefinite maximum nullity and zero forcing number*, Electronic Journal of Linear Algebra 23 (2012), 815–830, https://doi.org/10.13001/1081-3810.1559.
