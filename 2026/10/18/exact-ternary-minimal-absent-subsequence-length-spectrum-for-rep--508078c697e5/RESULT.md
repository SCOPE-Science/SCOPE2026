# Exact ternary minimal-absent-subsequence length spectrum for repeated increasing blocks

## Finding

For every integer \(k\ge1\), write \(B_k=(012)^k\) over the ordered alphabet \(\{0,1,2\}\). An *absent scattered subsequence* of \(B_k\) is a word that cannot be obtained by deleting positions from \(B_k\); it is *minimal absent* if all of its proper subsequences occur. Let \(L_k(m)\) be the number of distinct such words of length \(m\). The exact bivariate length spectrum is

\[
F(s,t)=\sum_{k\ge1}\sum_{m\ge0}L_k(m)s^kt^m=\frac{st^2P(s,t)}{D(s,t)},
\]

with polynomials

\[
\begin{aligned}
P(s,t)={}&6-8st+6st^2+3s^2t^2+6s^2t^3+s^2t^4\\
&-9s^3t^4+6s^3t^5+9s^4t^6-s^4t^7-3s^5t^8,\\
D(s,t)={}&1-3st+3s^2t^2-s^2t^3-s^3t^3-3s^3t^4\\
&+3s^4t^5-s^4t^6-3s^5t^7+s^6t^9.
\end{aligned}
\]

In particular, writing \(T_k=\sum_{m\ge0}L_k(m)\),

\[
\sum_{k\ge1}T_ks^k=\frac{6s-2s^2+10s^3-3s^4+8s^5-3s^6}{1-3s+2s^2-4s^3+2s^4-3s^5+s^6}.
\]

The first eight totals are \(6,16,46,127,349,960,2640,7264\), and \(T_k\ge2^{\lfloor(k-1)/3\rfloor}\). In contrast, the shortest absent subsequences have length \(k+1\) and number \(\binom{k+3}{2}\).

## Assumptions and scope

All statements concern finite *linear* words, not cyclic factors or contiguous missing substrings. The integer \(k\) is arbitrary with \(k\ge1\), and the coefficient formula applies to all integer lengths \(m\ge0\). The three alphabet symbols are distinct and their displayed order is used to define the periodic word. Word counts distinguish different symbol strings but do not count separate position embeddings.

For a nonempty word \(u=u_1\cdots u_m\), define its number of *weak descents* by

\[
H(u)=\sum_{i=1}^{m-1}[u_i\ge u_{i+1}],
\]

where a bracket is one when the condition is true and zero otherwise. Set \(H(\varepsilon)=0\). The theorem also characterizes the complete minimal-absent language as follows: \(u\) is minimal absent from \(B_k\) if and only if \(H(u)=k\) and deletion of **each** one of its letters reduces \(H\) by exactly one.

## Proof

**Greedy embedding.** The earliest embedding position of the first letter \(u_1\) in the infinite word `012012...` is \(1+u_1\). If the current and next symbols are \(a,b\in\{0,1,2\}\), the next embedding position advances by \(b-a+3[a\ge b]\), an integer from one to three. Summing telescopically, the earliest position of the final letter is

\[
p(u)=1+u_m+3H(u).
\]

As \(1\le 1+u_m\le3\), this position lies in \(B_k\), whose last position is \(3k\), exactly when \(H(u)\le k-1\). Thus absence is equivalent to \(H(u)\ge k\).

**Minimality and the local rule.** Removing an endpoint erases its adjacent weak-descent indicator. Removing an interior letter \(b\) from a triple \((a,b,c)\) changes \(H\) by

\[
\delta(a,b,c)=[a\ge b]+[b\ge c]-[a\ge c]\in\{0,1\}.
\]

The last containment follows by considering the three relative orders and ties (it also follows directly from transitivity of the total order). Therefore deleting one letter decreases \(H\) by at most one. A word absent from \(B_k\) is minimal absent precisely when its weak-descent number is \(k\) and every single deletion decreases this number by one; checking one-letter deletions suffices because subsequence containment is transitive. Consequently it has at least two letters, its initial and terminal pairs satisfy \(u_1\ge u_2\) and \(u_{m-1}\ge u_m\), and every interior triple satisfies \(\delta=1\). These conditions are both necessary and sufficient.

**Nine-state transfer matrix.** Index nine states by the ordered pairs \(\mathcal S=\{(a,b):a,b\in\{0,1,2\}\}\), in lexicographic order `00,01,02,10,11,12,20,21,22`. Let \(\alpha\) and \(\beta\) both be the column vector whose \((a,b)\)-entry is \([a\ge b]\). Define the nine-by-nine matrix

\[
M(s)_{(a,b),(b',c)}=[b=b']\,[\delta(a,b,c)=1]s^{[b\ge c]}.
\]

An admissible word starts at a weak-descent pair, contributing \(st^2\); each additional symbol transfers from \((a,b)\) to \((b,c)\) and contributes \(t\) and another factor \(s\) exactly when \(b\ge c\); it must terminate at a weak-descent pair. Thus the complete enumerator is the formal power series

\[
F(s,t)=st^2\,\alpha^{\mathsf T}(I-tM(s))^{-1}\beta.
\]

The inverse exists as a matrix of formal power series in \(t\), so this identity covers all lengths without a convergence assumption. Direct symbolic determinant and adjugate expansion gives

\[
\det(I-tM(s))=D(s,t),\qquad
\alpha^{\mathsf T}\operatorname{adj}(I-tM(s))\beta=P(s,t),
\]

with \(D,P\) exactly as displayed in the Finding. Substitution \(t=1\) is legitimate coefficientwise in \(s\): a minimal absent word with \(k\) weak descents has no two consecutive strict increases, so it has at most \(k+1\) increases and hence length at most \(2k+2\). This proves both generating functions.

**Polynomial versus exponential.** The shortest absent strings have length \(k+1\), so each of their \(k\) adjacent comparisons must be a weak descent; they are exactly the weakly decreasing ternary words of length \(k+1\), numbering \(\binom{k+3}{2}\). To prove exponential growth of all minimal absent strings, begin with state-pair `00`. Each of the two four-symbol continuations `1100` and `2100` follows permitted transfer edges, returns to state `00`, and contributes exactly three new weak descents. After \(r\) independent such choices, append \(q\in\{0,1,2\}\) zeros, where \(k=1+3r+q\). The resulting \(2^r\) distinct words satisfy the start/end and triple conditions and have exactly \(k\) weak descents. Hence \(T_k\ge2^{\lfloor(k-1)/3\rfloor}\). The elementary length bound also gives an exponential upper bound \(T_k\le\sum_{m=2}^{2k+2}3^m\). No optimal exponential base is asserted here.

## Verification

Two complementary checks accompany the result. `verify_mas.py` uses direct greedy position-subsequence tests rather than the weak-descent characterization; it exhaustively checks ternary candidate words through the largest admissible length for each \(1\le k\le6\), verifies the local criterion word by word, and compares the complete length counts with a separately implemented integer transfer recurrence through \(k=8\). `verify_rational.py` computes the nine-by-nine determinant and adjugate contraction exactly over \(\mathbb Z[s,t]\) and checks both rational functions with SymPy. Both programs output explicit success markers when their assertions pass. These are finite reproducibility checks; the universal quantifiers follow from the preceding proof and matrix identity, not from sample enumeration.

## Relationship to prior work

Kosche, Koß, Manea and Siemer [1] introduce minimal absent scattered subsequences and prove general characterizations. Their Proposition 3.6 constructs exponentially many minimal absent subsequences for repeated increasing permutations under the explicit assumption of an even alphabet of size at least four. The present result concerns the omitted ternary alphabet and supplies the **complete two-parameter enumerator** and an explicit exponential witness family. General characterization of minimal absence does not itself state these coefficients. Manea, Ringleb, Siemer and Winkler [2] develop general optimal enumeration algorithms, but their algorithmic results do not specify the closed length distribution for this family.

The analogous binary repeated word admits a different length formula and generating function; it does not imply the displayed ternary rational function. The present conclusion does not claim novelty for the general definitions, greedy matching principle, or shorter absent-subsequence count in [1].

## Limitations

The formulas apply only to the increasing ternary block repeated exactly \(k\) times. They are not asserted for arbitrary permutations from block to block, or alphabets of size four or larger. There may be unindexed or undiscovered equivalent formulas; priority should be independently investigated. No independent audit has been performed. The lower exponential construction does not identify an optimal growth constant.

## References

[1] M. Kosche, T. Koß, F. Manea and S. Siemer, *Absent Subsequences in Words*, arXiv:2108.13968 (first public 31 August 2021), especially Section 3, Proposition 3.6. https://arxiv.org/abs/2108.13968 .

[2] F. Manea, T. Ringleb, S. Siemer and M. Winkler, *Efficiently Finding All Minimal and Shortest Absent Subsequences in a String*, arXiv:2504.21471 (2025). https://arxiv.org/abs/2504.21471 .
