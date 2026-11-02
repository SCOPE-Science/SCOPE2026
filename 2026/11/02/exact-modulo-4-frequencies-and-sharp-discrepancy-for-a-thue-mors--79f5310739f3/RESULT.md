# Exact modulo-\(4\) frequencies and sharp discrepancy for a Thue–Morse Fibonacci recurrence

## Finding
Let \(s_2(n)\) denote the binary digit sum and define the integer sequence \(h_0=0\), \(h_1=1\), and
\[
h_n=(-1)^{s_2(n)}h_{n-1}+h_{n-2}\qquad(n\ge2).
\]
For an integer \(N\ge1\) and \(j\in\{0,1,2,3\}\), let
\[
H_j(N)=\#\{0\le n<N:h_n\equiv j\pmod4\}.
\]
There are absolute constants such that, simultaneously for all \(N\ge1\),
\[
H_0(N)=\frac N6+O(\sqrt N),\quad H_2(N)=\frac N6+O(\sqrt N),\quad
H_1(N)=\frac N3+O(\sqrt N),\quad H_3(N)=\frac N3+O(\sqrt N).
\]
Thus all four **natural** densities exist, and they are not uniformly distributed. The exponent \(1/2\) in the simultaneous error estimate is best possible: for no \(\varepsilon>0\) can all four errors be \(O(N^{1/2-\varepsilon})\).

More precisely, put \(a_j(r)=H_j(2^r)\), \(r\ge0\), and define
\[
E(z)=\sum_{r\ge0}(a_0(r)+a_2(r))z^r,\quad
U(z)=\sum_{r\ge0}(a_0(r)-a_2(r))z^r,
\]
\[
O(z)=\sum_{r\ge0}(a_1(r)+a_3(r))z^r,\quad
V(z)=\sum_{r\ge0}(a_1(r)-a_3(r))z^r.
\]
All four series have the following exact rational forms:
\[
\boxed{E(z)=\frac{1-z-z^2}{(1-z^2)(1-2z)},\qquad
U(z)=\frac{1+z+3z^2+2z^3}{1+z^2},}
\]
\[
\boxed{O(z)=\frac{z}{(1-z^2)(1-2z)},}
\]
\[
\boxed{V(z)=\frac{z(1-4z^2+7z^4+4z^5+4z^6-4z^7-16z^8-16z^9)}{(1-z^4)(1-3z^2+4z^4)}.}
\]
In particular every dyadic-prefix residue count is determined by these four fractions, using \(a_0=(E+U)/2\), \(a_2=(E-U)/2\), \(a_1=(O+V)/2\), and \(a_3=(O-V)/2\) coefficientwise.

## Assumptions and scope
All variables \(n,N,r\) are nonnegative integers subject to the ranges stated above, and congruences are ordinary integer congruences. Only modulus \(4\) is treated. An \(O\)-constant is independent of \(N\), the starting point of a dyadic block, and its starting pair of residues provided at least one coordinate is odd. The initial-value convention is essential.

## Proof
Write \(t_n=(-1)^{s_2(n)}\), and for \(s\in\{1,-1\}\) let
\[
B_s=\begin{pmatrix}s&1\\1&0\end{pmatrix}\pmod4.
\]
For each \(r\ge0\), let \(P_r(s)\) be the product of the matrices along the signed Thue–Morse block \((s t_0,\ldots,s t_{2^r-1})\), in the order acting on a column pair \((u,v)^\mathsf T\). The block-complement identity implies
\[
P_0(s)=B_s,\qquad P_{r+1}(s)=P_r(-s)P_r(s).
\]
For a starting pair \(w=(u,v)\in(\mathbb Z/4\mathbb Z)^2\), let \(C_r(s,w;j)\) count the occurrences of first-coordinate residue \(j\) after successive transitions through that block. Then
\[
C_0(s,(u,v);j)={\bf1}_{su+v\equiv j\ (4)},
\]
\[
C_{r+1}(s,w;j)=C_r(s,w;j)+C_r(-s,P_r(s)w;j).
\tag{1}
\]
These equations specify all \(2\cdot16\cdot4=128\) integer coordinates, without approximation.

Direct multiplication in \(\mathbb Z/4\mathbb Z\) gives \((P_2(1),P_2(-1))=(P_6(1),P_6(-1))\). Since the update is autonomous, \(P_{r+4}(s)=P_r(s)\) for every \(r\ge2\). Consequently, for each fixed \(r\bmod4\), advancing the full vector \(C_r\) by four levels is a fixed linear map \(T\). Evaluating (1) at the four base levels \(r=3,4,5,6\) proves, coordinate by coordinate,
\[
\boxed{C_{r+16}-18C_{r+12}+49C_{r+8}-288C_{r+4}+256C_r=0\qquad(r\ge3).}\tag{2}
\]
Indeed (2) is established at each base level by finite integer operations; application of the same four-level operator extends it inductively. The associated polynomial factors as
\[
X^4-18X^3+49X^2-288X+256=(X-16)(X-1)(X^2-X+16).
\]

Let \(\pi=(1,2,1,2)/6\). All genuine recurrence-block starting pairs are **primitive** modulo \(2\), meaning that their coordinates are not both even. For every such starting pair, both signs and all four base levels, a second exact calculation gives
\[
\boxed{(T^3-2T^2+17T-16I)C_r(s,w)=3840\,2^r\pi.}\tag{3}
\]
The factor \(3840\) is \((16-1)(16^2-16+16)\). Equation (2) makes the right side of (3) precisely the projection onto the eigenvalue \(16\) of the four-step transfer. All other roots have modulus at most \(4\), and the polynomial has no repeated roots. It follows uniformly for the finite set of primitive pairs and both signs that
\[
C_r(s,w;j)=2^r\pi_j+O(2^{r/2})\qquad(r\ge0).\tag{4}
\]
The attached standalone checker reproduces every one of the finite identities (2) and (3) from (1), including all 128 coordinates of (2); there is no inference from a finite sample of input indices.

The true recurrence can be started at \(n=0\) by the auxiliary pair \((h_{-1},h_{-2})=(1,-1)\). Indeed the first two transitions yield \(h_0=0,h_1=1\). For every aligned block \(q2^r\le n<(q+1)2^r\), the identity \(t_{q2^r+i}=t_qt_i\) makes its counts an instance of (4). The preceding-value pair is always primitive: modulo \(2\), all transition matrices equal the invertible Fibonacci matrix, so a nonzero parity pair can never become zero. Decomposing \([0,N)\) into at most one aligned block of each power-of-two length, and summing the geometric error \(\sum_{2^r\le N}O(2^{r/2})=O(\sqrt N)\), proves the full natural-density estimate.

Finally, for the original starting pair \((1,-1)\), compute \(C_r(1,(1,3);j)\) through level \(22\) using (1). Substitution into the four displayed rational fractions gives exact equality for every initial coefficient through that level. Their denominators all divide
\[
(1-16z^4)(1-z^4)(1-z^4+16z^8),
\]
which is precisely the denominator corresponding to (2). Hence the finite base identities and (2) prove the four fractions for **every** \(r\), not merely for the tested levels.

For sharpness, let \(Q(z)=1-3z^2+4z^4\) and let \(J(z)\) be the numerator of \(V(z)\). Polynomial division gives
\[
J(z)\equiv-\frac{(1+z)(1-7z^2)}4\pmod{Q(z)}.
\]
Because \(Q\) has none of the roots \(-1\) or \(\pm1/\sqrt7\), the factor \(Q\) does not cancel. All four of its complex roots have modulus \(2^{-1/2}\), so \(V\) has a noncancelled singularity at that modulus. Thus its coefficients \(a_1(r)-a_3(r)\) cannot satisfy \(O(2^{r(1/2-\varepsilon)})\) for any \(\varepsilon>0\); otherwise the power series would have larger radius of convergence. The optimality assertion follows on taking \(N=2^r\).

## Verification
Run `python checker.py` using Python 3 and the Python standard library. The program reconstructs the signed block matrices, tests the four base 128-coordinate recurrence identities, the primitive-state eigenprojection, the four exact generating functions, the absence of pole cancellation, and a separate direct computation of all \(2^{16}\) initial terms modulo \(4\). Expected final marker: `VERIFY_OK`. The matrix identities, together with the explicit induction above, are the infinite proof; direct enumeration is only a cross-check.

## Relationship to prior work
Lipka and Ulas introduced this Thue–Morse-coefficient Fibonacci recurrence and proved that its reduction modulo each positive modulus is automatic. In particular, their Example 3.6 constructs a large automaton modulo \(4\); they did not give the four natural densities, the explicit dyadic count generating functions, or the optimal discrepancy exponent displayed here. Their automaticity theorem motivates the finite-state approach, but automaticity alone does not determine these quantitative statistics. The primary source was inspected in its arXiv full text, including the relevant modular section and concluding questions. Standard automatic-sequence theory supplies context but is not used as an unproved substitute for the spectral computation.

## Limitations
The result concerns this particular signed recurrence modulo \(4\); it does not imply uniform residue distribution for general moduli or analogous recurrences. The optimality assertion rules out smaller **power-law exponents**, not every possible smaller bound along selected subsequences. The exact algebra is reproducible through the accompanying code; mathematical priority beyond the inspected literature is not independently certified.

## References
1. E. Lipka and M. Ulas, *A Fibonacci type sequence with Prouhet–Thue–Morse coefficients*, arXiv:2109.15243v1 (first posted 2021-09-30), especially Section 3, Examples 3.5–3.6 and Theorem 3.4. https://arxiv.org/abs/2109.15243
2. E. Lipka and M. Ulas, same work, *Journal of Difference Equations and Applications* 28 (2022), 695–715, DOI:10.1080/10236198.2022.2065918.
