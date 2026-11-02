# The outer-independent total Roman polynomial of rectangular rook graphs

## Finding

Let \(m,n\ge 2\), let \(G=K_m\square K_n\), and put \(N=mn\) and \(K=\min\{m,n\}\). For a map \(f:V(G)\to\{0,1,2\}\), write \(w(f)=\sum_{v\in V(G)}f(v)\). Define its outer-independent total Roman weight polynomial by
\[
\mathcal F_{m,n}(z)=\sum_{f\text{ satisfying (i)--(iii) below}}z^{w(f)}.
\]
Put \(A_{m,n}(k)=\binom{m}{k}\binom{n}{k}k!\). Then, **for all** \(m,n\ge2\),
\[
\boxed{\mathcal F_{m,n}(z)=
\sum_{k=0}^{K}A_{m,n}(k)z^{N-k}
\sum_{s=0}^{k}(-1)^s\binom{k}{s}(1+z)^{N-k-s(m+n-s-1)}
-\mathbf 1_{\{m=n=2\}}(4z^3+2z^4).}
\]
Thus every coefficient is the exact number of labeled valid functions of that weight, not merely the optimal weight.

The minimum weight is
\[
\boxed{\gamma_{oitR}(G)=
\begin{cases}
4,&m=n=2,\\
mn-\lfloor K/2\rfloor,&\text{otherwise}.
\end{cases}}
\]
The exact number \(B_{m,n}\) of minimum-weight functions is, with \(q=\lfloor K/2\rfloor\),
\[
\boxed{B_{m,n}=
\begin{cases}
9,&m=n=2,\\
A_{m,n}(2q)\dfrac{(2q)!}{q!},&K=2q,\ (m,n)\ne(2,2),\\
A_{m,n}(2q)\dfrac{(2q)!}{q!}
+A_{m,n}(2q+1)\dfrac{(2q+1)!}{q!}(m+n-2q-2),&K=2q+1.
\end{cases}}
\]
Every minimum function is classified by the zero-matchings and defender covers described in the proof. For example, \(B_{2,3}=12\), \(B_{3,3}=108\), \(B_{3,4}=504\), and \(B_{4,4}=288\).

## Assumptions and scope

The rook graph has vertices \((i,j)\in[m]\times[n]\), with two distinct vertices adjacent precisely when they share their first or second coordinate. There are no loops. A map \(f\) is an *outer-independent total Roman dominating function* precisely when

(i) the zero set \(Z=\{v:f(v)=0\}\) is independent;

(ii) every vertex in \(Z\) has a neighbor of label \(2\); and

(iii) every vertex of positive label has a neighbor of positive label.

These conditions are imposed on labeled graphs with fixed row and column identities. We count distinct functions, without quotienting by graph automorphisms. The polynomial uses the weight exponent, not the number of zeros or the number of defenders.

## Proof

**1. Zero sets are rook matchings.** No two zero squares share a row or column, so the zero set is a matching in the incidence graph \(K_{m,n}\). A matching of size \(k\) is obtained by choosing \(k\) rows and \(k\) columns and a bijection between them; the number is \(A_{m,n}(k)\). Necessarily \(0\le k\le K\).

**2. The totality condition and its sole exception.** Any square of positive label has \(m+n-2\) neighbors, of which at most two can be zero (at most one in its row and one in its column). If \(m+n\ge5\), the positive square has a positive neighbor. Hence condition (iii) is then automatic once (i) holds. The sole remaining board is \(2\times2\). There a two-zero matching leaves the other two squares nonadjacent, so (iii) fails. For each of the two such zero matchings, Roman defense condition (ii) allows exactly three assignments of labels \(1,2\) on the other two squares: two of total weight \(3\) and one of weight \(4\). These are exactly the \(4z^3+2z^4\) assignments subtracted in the formula. All other feasible zero sets on \(2\times2\) automatically satisfy (iii).

**3. Inclusion-exclusion counts every function.** Fix a zero matching \(Z\) of size \(k\). Without imposing (ii), the \(N-k\) remaining squares each have labels \(1\) or \(2\), yielding \(z^{N-k}(1+z)^{N-k}\). For any chosen \(s\)-subset \(S\) of the zero squares, suppose every square in \(S\) lacks a neighbor labeled \(2\). Then label \(2\) is forbidden in the union of the neighborhoods of these \(s\) squares. Because their rows and columns are distinct, this union contains exactly
\[
sn+sm-s^2-s=s(m+n-s-1)
\]
nonzero squares: the \(s\) selected zero squares are removed from the union, and the other zero squares lie outside it. Every square in that union must receive label \(1\), while every remaining nonzero square may receive label \(1\) or \(2\). Its weight polynomial is
\[
z^{N-k}(1+z)^{N-k-s(m+n-s-1)}.
\]
Inclusion-exclusion over the \(k\) zero squares gives the inner sum in the asserted formula. Multiplication by \(A_{m,n}(k)\), summation over \(k\), and the \(2\times2\) exception prove the complete polynomial.

**4. Minimum weight.** Let \(k=|Z|\), and let \(t\) be the number of vertices carrying label \(2\). A defender labeled \(2\) is adjacent to at most two zeros (one in its row and one in its column), so \(t\ge\lceil k/2\rceil\). Thus
\[
w(f)=N-k+t\ge N-\lfloor k/2\rfloor\ge N-\lfloor K/2\rfloor.
\]
Write \(q=\lfloor K/2\rfloor\). If \(m+n\ge5\), choose any matching of \(2q\) zero squares. Pair those zeros arbitrarily; for each pair, place a single label-\(2\) square at either of the two cross-intersections of its row and column, and label every other nonzero square \(1\). Each zero is defended, and step 2 provides totality. This attains \(N-q\). On \(2\times2\), step 2 excludes weight \(3\), while the all-one function has weight \(4\).

**5. Exhaustive classification and count of minimum functions.** Suppose \(m+n\ge5\). Equality requires \(k\in\{2q,2q+1\}\), where the latter occurs only if \(K\) is odd; necessarily \(t=k-q\). For \(k=2q\), all \(q\) defenders must each cover exactly two different zeros and each zero must be defended exactly once. Thus the zeros are partitioned into \(q\) pairs, each served by one of two oriented cross-intersections. This gives \((2q)!/(2^q q!)\cdot2^q=(2q)!/q!\) assignments per zero matching.

For \(k=2q+1\), there must be exactly \(q+1\) defenders. Each covers one or two zeros, and the total coverage capacity exceeds the number of zeros by just one. Consequently there are exactly two disjoint possibilities:

(A) Every defender covers two zeros. The undirected zero-incidence edges form one path on three zeros and \(q-1\) disjoint edges. Selecting the triple, its middle vertex, a matching on the rest, and an orientation of every defender gives \(2(2q+1)!/(q-1)!\) assignments.

(B) One defender covers exactly one zero, while the other \(q\) defenders cover disjoint pairs of zeros. The single defender can be placed in one of the \(m+n-2k\) cross-extensions into an unused row or column. Choosing its zero, pairing the remaining zeros, and orienting the paired defenders gives \((2q+1)!(m+n-2k)/q!\) assignments.

Together these are
\[
\frac{(2q+1)!}{q!}\bigl(2q+m+n-2(2q+1)\bigr)
=\frac{(2q+1)!}{q!}(m+n-2q-2)
\]
assignments per zero matching. These choices are all distinct and exhaustive because the zero set and defender set determine the function uniquely. Multiplying by the respective zero-matching counts completes the formula for \(B_{m,n}\). Finally, on \(2\times2\), the all-one function and the eight functions with one zero and one adjacent defender attain weight \(4\), giving \(9\) optima.

## Verification

The standalone file `verify_oit_rook.py` computes the asserted coefficients by integer binomial arithmetic and independently enumerates functions using the original three conditions. Invoke `python3 verify_oit_rook.py`. Exhaustive ternary assignments were checked for \((m,n)=(2,2),(2,3),(2,4),(2,5),(3,3),(3,4)\). For \((3,5)\) and \((4,4)\), all zero matchings and all choices of label-\(2\) squares were enumerated, again checking the original three conditions; this is exhaustive because every valid zero set is a matching. All coefficients, minima, and numbers of minimizers agreed, and execution ended with `VERIFY_OK`. These finite tests support, but do not replace, the all-parameter proof.

## Relationship to prior work

The 2019 foundational paper by Cabrera Martínez, Kuziak, and Yero defines the outer-independent total Roman condition and studies scalar domination bounds and complexity. Their preprint of 10 December 2021, Section 3.3 and Theorem 3.4, explicitly gives the scalar formula \(mn-\lfloor\min\{m,n\}/2\rfloor\) for Cartesian products of complete graphs, but neither the full weight polynomial nor the number or structure of all optimal functions. That scalar formula is prior work for all boards with \(m+n\ge5\), not claimed here as new. The \(2\times2\) boundary requires the explicit totality correction above: two positive squares remaining after a full zero matching are nonadjacent. The present result supplies the missing cardinality distribution and exhaustive optimal-labeling counts.

Equivalent terminology includes rook graphs, the line graphs of complete bipartite graphs, and outer-independent/covering total Roman labelings. Complete multipartite *vertex* graphs and the ordinary outer-independent Roman variant have different neighborhoods or omit condition (iii); their enumerators do not directly imply this one. No claim of global publication priority is made.

## Limitations

The theorem concerns simple two-factor Cartesian products of complete graphs; it does not extend automatically to higher-dimensional Hamming graphs, the direct product, or arbitrary line graphs. Numerical checks were exhaustive only for the stated finite orders. Publication-priority uncertainty remains for unindexed work and general enumerators not located by the stated searches. No independent validation is asserted here.

## References

1. A. Cabrera Martínez, D. Kuziak, I. G. Yero, *Outer-independent total Roman domination in graphs*, Discrete Applied Mathematics 269 (2019), 107–119. DOI: 10.1016/j.dam.2018.12.018. Authorized manuscript: https://rodin.uca.es/handle/10498/30892.
2. A. Cabrera Martínez, D. Kuziak, I. G. Yero, *Relating the outer-independent total Roman domination number with some classical parameters of graphs*, arXiv:2112.05476v1, first posted 2021-12-10, especially Theorem 3.4; subsequently Mediterranean Journal of Mathematics 19 (2022), article 144. https://arxiv.org/html/2112.05476v1.
