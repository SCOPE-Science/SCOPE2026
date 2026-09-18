# Optimality of the 9/22 rainbow-Schur construction under a parity restriction

## Statement

For a 3-coloring \(c:[n]\to\{1,2,3\}\), let
\[
R_n(c)=\{(x,y):x,y\ge1,\ x+y\le n,\ c(x),c(y),c(x+y)\text{ are pairwise distinct}\}.
\]
As usual, \((x,y)\) and \((y,x)\) are counted separately when \(x\ne y\), and the total number of ordered pairs giving a Schur triple is \(\binom n2\).

Call a coloring **parity-restricted** if, after a permutation of the colors, every even integer has color 3 and every odd integer has color 1 or 2. Let
\[
\Lambda_n^{\mathrm{par}}
=\max_c \frac{|R_n(c)|}{\binom n2},
\]
where the maximum is over parity-restricted colorings.

**Theorem.**
\[
\boxed{\lim_{n\to\infty}\Lambda_n^{\mathrm{par}}=\frac9{22}.}
\]
Thus the \(9/22\) construction of Hegde--Kumar--Pratibha is asymptotically optimal not merely within an interval ansatz, but among all colorings in which the even integers form one monochromatic color class and the odd integers use the other two colors arbitrarily.

More quantitatively, for \(n=2m\), if \(M_m\) denotes half of the largest possible rainbow count in this class, then
\[
M_m\le \frac9{22}m^2+\frac m4.
\]
The Hegde--Kumar--Pratibha construction gives
\[
M_m\ge \frac9{22}m^2-O(m).
\]

A stability consequence is that if a sequence of parity-restricted colorings has rainbow density \(9/22-o(1)\), and \(a_m\) of the \(m\) odd integers in \([2m]\) receive one of the two odd colors, then
\[
\operatorname{dist}\!\left(\frac{a_m}{m},\left\{\frac5{11},\frac6{11}\right\}\right)\longrightarrow0.
\]

## Context

Hegde, Kumar and Pratibha proved in arXiv:2609.18474 (submitted 16 September 2026) that the unrestricted 3-color rainbow-Schur density lies asymptotically between \(9/22\) and \(8/15\), and explicitly asked whether the lower value \(9/22\) is the true limit. Their lower-bound coloring is parity-restricted: all even integers receive one color, while the odd integers are split between the other two colors using intervals with breakpoints asymptotic to \(4n/11\) and \(10n/11\).

The theorem above shows that this natural parity mechanism has already been optimized completely. Consequently, any coloring that asymptotically beats \(9/22\) must leave the parity-restricted class.

## Proof

### 1. Exact reduction to a fixed-cardinality cut problem

First take \(n=2m\), and write the odd integers as
\[
o_i=2i-1,\qquad 1\le i\le m.
\]
Let \(A\subseteq[m]\) be the set of indices whose odd integer has color 1, and put \(a=|A|\); the remaining odd integers have color 2.

Define the graph \(H_m\) on vertex set \([m]\) by
\[
\{i,j\}\in E(H_m)\quad\Longleftrightarrow\quad i<j\ \text{ and }\ i+j\le m+1.
\]
Let \(\operatorname{cut}_{H_m}(A)\) denote the number of edges of \(H_m\) with one endpoint in \(A\) and one outside it.

There are two possible parity patterns for a rainbow Schur triple.

* **Exactly one odd summand.** For every pair \(i<j\) of oppositely colored odd indices, \(o_j-o_i=2(j-i)\) is even. Hence
  \[
  o_i+2(j-i)=o_j
  \]
  gives two ordered rainbow pairs, according to the order of the summands. Conversely every rainbow pair with exactly one odd summand is obtained this way. Therefore this case contributes
  \[
  2a(m-a).
  \]

* **Two odd summands.** Their sum is even and therefore has color 3. Oppositely colored \(o_i,o_j\) give a rainbow triple exactly when
  \[
  (2i-1)+(2j-1)\le2m,
  \]
  equivalently \(i+j\le m+1\). Each unordered pair contributes two ordered pairs, so this case contributes
  \[
  2\operatorname{cut}_{H_m}(A).
  \]

Thus
\[
\boxed{|R_{2m}(c)|=2\bigl(a(m-a)+\operatorname{cut}_{H_m}(A)\bigr).}\tag{1}
\]
For fixed \(a\), define
\[
h_m(a)=\max_{A\subseteq[m],\ |A|=a}\operatorname{cut}_{H_m}(A).
\]
Then
\[
M_m:=\frac12\max_c|R_{2m}(c)|
=\max_{0\le a\le m}\bigl(a(m-a)+h_m(a)\bigr).\tag{2}
\]

### 2. An exact recursion for the threshold graph

Vertex 1 of \(H_m\) is adjacent to every other vertex, vertex \(m\) is adjacent only to vertex 1, and the graph induced by \(\{2,\ldots,m-1\}\), after shifting labels down by one, is \(H_{m-2}\). It follows that
\[
\boxed{
 h_m(a)=\max\left\{
 \begin{array}{ll}
 h_{m-2}(a)+a, & 0\le a\le m-2,\\[2mm]
 h_{m-2}(a-1)+\max(a,m-a), & 0\le a-1\le m-2,\\[2mm]
 h_{m-2}(a-2)+(m-a), & 0\le a-2\le m-2
 \end{array}\right. .}\tag{3}
\]
Indeed, the three lines correspond respectively to putting neither endpoint \(1,m\) in \(A\), putting exactly one in \(A\), and putting both in \(A\). The two possibilities in the middle case contribute \(a\) or \(m-a\), whence the maximum. The initial values are \(h_0(0)=0\) and \(h_1(0)=h_1(1)=0\). Also
\[
h_m(a)=h_m(m-a)\tag{4}
\]
by complementing the cut.

### 3. Uniform asymptotics for the constrained maximum cut

Define a symmetric function \(H:[0,1]\to\mathbb R\) by \(H(x)=H(1-x)\) and, for \(0\le x\le1/2\),
\[
H(x)=
\begin{cases}
 x-\dfrac32x^2, & 0\le x\le\dfrac13,\\[2mm]
 \dfrac{1-x}{2}-\dfrac38(1-x)^2, & \dfrac13\le x\le\dfrac12.
\end{cases}\tag{5}
\]
Put
\[
\Phi_m(a)=m^2H(a/m),\qquad \Phi_0(0)=0.
\]
Replace \(h_{m-2}\) by \(\Phi_{m-2}\) on the right side of (3), and call the resulting maximum \(B_m(a)\). Direct substitution into the two quadratic pieces of (5) gives the sharp comparison
\[
\boxed{|\Phi_m(a)-B_m(a)|\le\frac12}\tag{6}
\]
for every \(m\ge2\) and \(0\le a\le m\).

For completeness, by symmetry it is enough to take \(a\le m/2\). Away from the single transition at \(a\approx m/3\), the Bellman residual \(\Phi_m(a)-B_m(a)\) is especially simple:
\[
0\quad(a=0),\qquad -\frac12\quad(1\le a\le\lfloor m/3\rfloor),\qquad 0\quad(a\ge\lfloor m/3\rfloor+2).
\]
At \(a=\lfloor m/3\rfloor+1\), when that index is at most \(m/2\), the residual is respectively
\[
\frac18,\quad-\frac18,\quad-\frac38
\]
according as \(m\equiv0,1,2\pmod3\). These formulas are obtained by inserting the appropriate quadratic expression from (5) into the three terms of (3). In the first region the middle term is maximal; in the second region the third term is maximal, apart from harmless ties at the transition.

Let
\[
E_m=\max_{0\le a\le m}|h_m(a)-\Phi_m(a)|.
\]
Equations (3) and (6), together with the elementary fact that replacing each entry of a finite maximum by a quantity within \(E\) changes the maximum by at most \(E\), give
\[
E_m\le E_{m-2}+\frac12.
\]
Since \(E_0=E_1=0\),
\[
\boxed{|h_m(a)-m^2H(a/m)|\le\frac12\left\lfloor\frac m2\right\rfloor}\tag{7}
\]
uniformly in \(a\). In particular,
\[
h_m(a)=m^2H(a/m)+O(m)\tag{8}
\]
uniformly over all side sizes.

### 4. The continuum optimization

Combining (2) and (8),
\[
M_m=m^2\max_{0\le x\le1}G(x)+O(m),
\qquad
G(x)=x(1-x)+H(x).\tag{9}
\]
The function is symmetric about \(1/2\). For \(0\le x\le1/3\),
\[
G(x)=2x-\frac52x^2,
\]
which is increasing throughout that interval. For \(1/3\le x\le1/2\),
\[
G(x)
=x(1-x)+\frac{1-x}{2}-\frac38(1-x)^2
=-\frac{(x-1)(11x+1)}8.
\]
This quadratic is maximized at
\[
x=\frac5{11},
\]
where
\[
G(5/11)=\frac9{22}.
\]
By symmetry the other maximizer is \(6/11\). Hence
\[
M_m=\frac9{22}m^2+O(m).\tag{10}
\]
The explicit error in (7) immediately gives the stated upper bound
\[
M_m\le\frac9{22}m^2+\frac m4.
\]

The lower bound is also realized directly by the known construction: color the odd indices asymptotically in
\[
[0,4/11]\cup(10/11,1]
\]
with one odd color, the middle interval with the other odd color, and every even integer with the third color. Its odd-color density is \(5/11\). The cross-color term \(a(m-a)\) contributes
\[
\frac{30}{121}m^2+O(m),
\]
while the cut edges \(i+j\le m+1\) contribute
\[
\left(\int_0^{1/11}\frac6{11}\,dx+
\int_{1/11}^{4/11}\left(\frac7{11}-x\right)dx\right)m^2+O(m)
=\frac{39}{242}m^2+O(m).
\]
Their sum is \(9m^2/22+O(m)\), proving (10) from both sides.

Finally, by (1),
\[
\max_c|R_{2m}(c)|=\frac9{11}m^2+O(m).
\]
Since \(\binom{2m}{2}=2m^2-m\), the parity-restricted rainbow density tends to \(9/22\) along even \(n\). Adding or deleting one endpoint changes the number of available Schur triples, and hence the extremal rainbow count, by only \(O(n)\); therefore the same limit holds for odd \(n\).

### 5. Stability of the odd-color balance

If parity-restricted colorings have rainbow density \(9/22-o(1)\), equation (7) forces
\[
G(a_m/m)=\frac9{22}-o(1).
\]
The continuous function \(G\) has precisely the two global maximizers \(5/11\) and \(6/11\). Compactness therefore gives
\[
\operatorname{dist}\!\left(a_m/m,\{5/11,6/11\}\right)\to0.
\]
This proves the stated stability consequence. It does not assert uniqueness of the arrangement of the odd colors.

## Verification

`artifacts/verify.py` uses exact integer/rational arithmetic to:

1. compare recursion (3) against brute-force cuts for all fixed side sizes through \(m=12\);
2. verify the exact low-density identity
   \[
   h_m(a)=am-\frac{3a^2-a}{2}\qquad(3a\le m)
   \]
   through \(m=300\);
3. check the Bellman residual bound (6) through \(m=1000\);
4. check the induced error bound (7) through \(m=1000\); and
5. compute finite weighted optima approaching \(9/22\).

These computations are sanity checks; the theorem is proved by the exact recursion, the Bellman comparison, and the one-variable optimization above.

## Relation to prior literature and limitations

Parczyk and Spiegel introduced the multiplicity version of the anti-Ramsey Schur problem and obtained asymptotic bounds \(0.4\le\Lambda_{n,3}\le0.66364\). Hegde--Kumar--Pratibha subsequently improved these to
\[
\frac9{22}\le\liminf\Lambda_{n,3}\le\limsup\Lambda_{n,3}\le\frac8{15}
\]
and asked whether the unrestricted limit is \(9/22\).

The result here does **not** solve that unrestricted problem. It proves exact asymptotic optimality inside the broad parity-restricted class containing their lower-bound construction. Thus it identifies a structural obstruction: an improvement on \(9/22\) cannot keep every even integer in a single color while forbidding that color on all odds.

Originality is claimed only **to the best of our knowledge**. Searches covered “rainbow Schur triples”, the \(9/22\) construction, parity/odd-even colorings, monochromatic evens, threshold-graph and max-cut reformulations, and synonymous anti-Ramsey Schur terminology. No prior source located states the parity-restricted optimum, the reduction (1)--(3), or the stability consequence. The principal source is extremely recent, so an unindexed contemporaneous follow-up remains a residual risk. No closely matching inaccessible paper was identified whose unseen theorem statement is a specific material threat to the claim.

## References

1. S. Hegde, H. Kumar, Pratibha, *A somewhat sure note on an un-Schur problem*, arXiv:2609.18474 (2026). https://arxiv.org/abs/2609.18474
2. O. Parczyk, C. Spiegel, *An Unsure Note on an Un-Schur Problem*, Electronic Journal of Combinatorics 33(1), P1.45 (2026). https://doi.org/10.37236/13554
