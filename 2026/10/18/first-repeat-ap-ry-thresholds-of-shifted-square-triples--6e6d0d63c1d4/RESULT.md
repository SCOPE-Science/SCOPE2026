# First-repeat Apéry thresholds of shifted-square triples

## Finding
For every integer \(a\ge 2\), take the ordered coin triple
\[
A_a=(a,a+1,a+4),\qquad
D_a(N)=\#\{(x,y,z)\in\mathbb Z_{\ge0}^{3}:ax+(a+1)y+(a+4)z=N\}.
\]
Set \(S_1(A_a)=\{N\ge0:D_a(N)\ge2\}\), \(g_1(A_a)=\max(\mathbb Z_{\ge0}\setminus S_1(A_a))\), and \(n_1(A_a)=\#(\mathbb Z_{\ge0}\setminus S_1(A_a))\). For each \(0\le r<a\), define
\[
q_r=\lfloor r/4\rfloor,\quad s_r=r-4q_r,\quad
\delta_{a,r}=a+1-3\left(\left\lfloor\frac{r+a}{4}\right\rfloor-\left\lfloor\frac r4\right\rfloor\right),
\]
\[
c_{a,r}=q_r+s_r+\begin{cases}
\delta_{a,r},&0\le r<4,\\
\min\{3,\delta_{a,r}\},&4\le r<a.
\end{cases}
\qquad T_a(r)=r+a c_{a,r}.
\]
Then \(T_a(r)\) is *exactly the least nonnegative integer congruent to \(r\) modulo \(a\) admitting at least two distinct coefficient-triple representations*. Thus the entire first-repeat Apéry set is \(\{T_a(r):0\le r<a\}\), and
\[
g_1(A_a)=\max_{0\le r<a}T_a(r)-a,\qquad n_1(A_a)=\sum_{r=0}^{a-1}c_{a,r}.
\]
For \(a\ge14\), writing \(a=4k+d\) with \(k\ge3\), \(d\in\{0,1,2,3\}\), and necessarily \(d\ge2\) if \(k=3\), the two invariants have the closed quasipolynomial laws
\[
g_1(A_a)=4k^2+(20+d)k+\begin{cases}-1&d=0,\\3&d=1,\\7&d=2,\\14&d=3,\end{cases}
\]
\[
n_1(A_a)=2k^2+(20+d)k+\frac{d(d+7)}2-8.
\]
For \(2\le a\le13\), the complete small-base table of \((a,g_1(A_a),n_1(A_a))\) is
\[
(2,7,7),(3,9,9),(4,19,14),(5,22,19),(6,29,25),
(7,34,30),(8,55,40),(9,51,44),(10,59,51),
(11,76,61),(12,95,70),(13,89,75).
\]

## Assumptions and scope
Each representation counts a distinct triple of nonnegative coefficients, including when one coin is redundant (e.g., \(a=2\)). This is the \(p=1\) convention \(D_a(N)>1\), not the convention of exactly one representation. The definition includes \(N=0\); here \(D_a(0)=1\), so zero is among the first-repeat gaps. Every assertion holds for all integer \(a\ge2\); only the simplified quasipolynomials require \(a\ge14\). The primary MSC2020 is 11D07.

## Proof
**(1) Residue-and-height parameterization.** Fix \(0\le r<a\) and write \(N=r+at\), \(t\ge0\). Any representation satisfies \(y+4z=r+ah\) for a *unique* integer \(h\ge0\), since \(y+4z\ge0\) has residue \(r\) modulo \(a\). Conversely, choosing
\[
h\ge0,\quad 0\le z\le\lfloor(r+ah)/4\rfloor,\quad
y=r+ah-4z,\quad x=t-C_{h,z},
\]
where \(C_{h,z}=r+(a+1)h-3z\), gives every representation precisely once whenever \(t\ge C_{h,z}\). In particular all costs are nonnegative because \(C_{h,z}=h+y+z\), so no inadmissible negative thresholds occur.

**(2) Locate the first two costs.** For a fixed \(h\), the smallest cost is
\[
C_h=r+(a+1)h-3\left\lfloor\frac{r+ah}{4}\right\rfloor.
\]
It is realized uniquely by the largest permitted \(z\). The second smallest cost at that height, if it exists, is \(C_h+3\). For every \(a\ge2\),
\[
C_{h+1}-C_h\ge a+1-3\lceil a/4\rceil\ge0;
\]
the last inequality follows directly on the four residue classes of \(a\), with the small case \(a=2\) included. Thus the cheapest representation has cost \(C_0=q_r+s_r\). The next cheapest *distinct* representation is either the next \(z\) at height zero (possible exactly when \(r\ge4\), cost \(C_0+3\)) or the cheapest representation at height one (cost \(C_1=C_0+\delta_{a,r}\)). All higher heights cost at least \(C_1\). There are always at least two candidates (the cheapest cost at heights zero and one), so their second order statistic is exactly \(c_{a,r}\), including all ties. Therefore \(T_a(r)=r+a c_{a,r}\) is the first integer in residue \(r\) with \(D_a\ge2\).

**(3) Obtain the invariants.** Adding a coin of value \(a\) injects every representation of \(N\) into a distinct representation of \(N+a\). Hence \(D_a(r+at)\) is nondecreasing in \(t\). In residue \(r\), the first-repeat gaps are precisely \(r,r+a,\ldots,r+a(c_{a,r}-1)\), whose number is \(c_{a,r}\). The last such gap is \(T_a(r)-a\). Summing and maximizing respectively establishes the formulas for \(n_1\) and \(g_1\) (including \(r=0\)).

**(4) Simplify for large \(a\).** Write \(a=4k+d\), \(d\in\{0,1,2,3\}\), \(k\ge3\), with \(d\ge2\) whenever \(k=3\). If \(r=4q+s\), \(s\in\{0,1,2,3\}\), then \(\delta_{a,r}=k+d+1-3\mathbf 1_{s+d\ge4}\ge3\). Thus \(c_{a,r}=q+s+3\) whenever \(q\ge1\), and \(c_{a,s}=s+k+d+1-3\mathbf 1_{s+d\ge4}\) for \(q=0\). The four \(q=0\) corrections relative to \(q+s+3\) sum to \(a-8\). Direct residue summation gives
\[
\sum_{r=0}^{a-1}(q_r+s_r)=2k^2+(4+d)k+\frac{d(d-1)}2,
\]
so \(n_1=2k^2+(20+d)k+d(d+7)/2-8\).

For \(q\ge1\) we have \(T_a(4q+s)=q(a+4)+s(a+1)+3a\). The maximum over the available final residue blocks is at \(r=4k-1\) (\(q=k-1,s=3\)) for \(d=0,1,2\), giving \((k+5)a+4k-1\); for \(d=3\) it is at \(r=4k+2\) (\(q=k,s=2\)), giving \((k+5)a+4k+2\). Indeed for \(d=1,2\) the short final block is smaller than \(r=4k-1\) by \(2a-1\) and \(a-2\) respectively; when \(d=3\) the final-block winner is larger by \(3\). At height \(q=0\), the maximum threshold is at most \((k+4)a+3\), strictly smaller than the displayed winners. Subtracting \(a\) proves the \(g_1\) quasipolynomial. The starting bound is sharp: the displayed quasipolynomial predicts \(g_1=102\) at \(a=13\), but the exact residue thresholds give \(g_1=89\). The small-base table is obtained by direct substitution of the fully proved general threshold formula for each integer \(2\le a\le13\), not by extrapolation from experiments.

## Verification
The standalone `verify.py` enumerates capped denumerants independently by unbounded coin-change dynamic programming and compares the very first threshold in *every* residue class to \(T_a(r)\) for each \(2\le a\le400\): 80,199 distinct residue thresholds. It independently compares all small-base table entries and both quasipolynomials to the exact threshold expressions through \(a=1100\). Expected output consists of two lines beginning `PASS:`. The mathematical proof above, rather than finite computation, covers unbounded \(a\).

## Relationship to prior work
Liu and Xin [1], first publicly available in October 2022, solve the *classical* (zero-representation) Frobenius problem for shifted-square sequences including \((a,a+1,a+4)\). The new result concerns the different multiplicity threshold at two representations and gives all residue thresholds and the first-repeat genus. Liu, Xin, Ye, and Yin [2] likewise address the classical Frobenius number. Komatsu and Ying [3] obtain explicit \(p\)-Frobenius formulas for *arithmetic-progression triples* \((a,a+d,a+2d)\); our successive offsets are \(1,3\), hence nonarithmetic. General \(p\)-Apéry formulas [4] convert a full \(p\)-Apéry set into numerical invariants but do not determine this shifted-square set. Subwattanachai [5] obtains explicit multiplicity formulas under divisibility hypotheses absent from the displayed family for \(a\ge14\). The general method of [4] is used here; novelty, as far as inspected evidence shows, lies in the explicit second-cost classification for this natural nonprogression family and its exact stability threshold.

## Limitations
The result addresses precisely \(p=1\), three coins with square offsets \(0,1,4\), and integer \(a\ge2\); it asserts nothing for greater representation thresholds or more square offsets. The simplified formulas hold uniformly from \(a=14\); the twelve smaller bases are listed, with some accidental agreement with the same expressions. Published and indexed literature may contain equivalent formulas not located in the searches; novelty is assessed only against inspected sources. Verification by computation is finite and does not independently certify the infinite proof.

## References
[1] F. Liu and G. Xin, *On Frobenius Formulas of Power Sequences*, arXiv:2210.02722v1 (first posted 2022-10-06), https://arxiv.org/abs/2210.02722.

[2] F. Liu, G. Xin, S. Ye, and J. Yin, *The Frobenius Formula for \(A=(a,ha+d,ha+b_2d,\ldots,ha+b_kd)\)* (2023), arXiv:2304.09039, https://arxiv.org/abs/2304.09039. See the manuscript's statement of the ordinary Frobenius problem.

[3] T. Komatsu and H. Ying, *The p-numerical semigroup of the triple of arithmetic progressions*, arXiv:2206.13052 (first posted 2022-06-27), https://arxiv.org/abs/2206.13052.

[4] T. Komatsu, *On the determination of p-Frobenius and related numbers using the p-Apéry set*, arXiv:2111.11021 (2021), https://arxiv.org/abs/2111.11021.

[5] K. Subwattanachai, *Generalized Frobenius Number of Three Variables*, arXiv:2309.09149 (2023), https://arxiv.org/abs/2309.09149.
