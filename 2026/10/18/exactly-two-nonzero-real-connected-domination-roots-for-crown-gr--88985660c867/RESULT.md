# Exactly two nonzero real connected-domination roots for crown graphs, with parity-dependent logarithmic convergence

## Finding
For every integer \(n\ge3\), the connected domination polynomial \(D_c(H_n;x)\) of the crown graph \(H_n=K_{n,n}-M_n\) has a root at zero of multiplicity exactly four and **exactly two additional real zeros** \(\rho_n^-\) and \(\rho_n^+\). They are simple and satisfy
\[
\rho_n^-<-2<\rho_n^+<-1.
\]
Furthermore,
\[
\lim_{n\to\infty}\rho_n^+=-\sqrt2,
\]
and, for \(\epsilon_n=-\rho_n^--2>0\),
\[
\epsilon_n=\frac{\log n+\log c_n+o(1)}{n},\qquad
c_n=\begin{cases}
2(\sqrt2-1),&n\text{ even},\\
2(\sqrt2+1),&n\text{ odd}.
\end{cases}
\]
Thus the root left of \(-2\) approaches \(-2\) at logarithmic-over-linear speed with two different parity constants, whereas the other approaches the distinct limit \(-\sqrt2\). The analytic root assertions, not the previously available all-set enumeration, constitute the finding.

## Assumptions and scope
All graphs are finite, simple, undirected. The crown graph \(H_n\) has vertices \(a_1,\ldots,a_n,b_1,\ldots,b_n\), with \(a_i b_j\) an edge precisely when \(i\ne j\). A vertex subset \(S\) is **connected dominating** if it dominates all vertices and induces a connected subgraph. Define
\[
D_c(H_n;x)=\sum_{S\text{ connected dominating}}x^{|S|}.
\]
The parameter \(n\) is any integer at least three; the assertions concern real polynomial zeros counted with multiplicity, with the two nonzero real zeros distinct. No conclusion is claimed about the locations of the nonreal zeros. The limit statements hold along all integers, with a separate constant according to parity.

## Proof
**1. Enumeration identity used as input.** The established classification of connected dominating sets of crown graphs says that a set is connected dominating precisely when it includes at least two vertices from each bipartition class, except that for every pair of distinct indices \(i,j\), the four-set \(\{a_i,a_j,b_i,b_j\}\) is disconnected. For completeness, if a selected shore is empty then connectivity fails; if it is a singleton, its deleted-matching partner on the opposite shore is either undominated or isolated in the induced graph. With at least two selected vertices in both shores every omitted vertex is dominated, and disconnectedness is possible only when exactly the same two indices are selected in each shore. Counting gives the known identity
\[
D_c(H_n;x)=\bigl((1+x)^n-1-nx\bigr)^2-\binom n2 x^4.
\]
Write \(C_n=\binom n2\), and define the degree-\(n-2\) polynomial
\[
R_n(x)=\sum_{j=2}^n\binom nj x^{j-2}
=\frac{(1+x)^n-1-nx}{x^2}
\]
where the quotient is interpreted by polynomial continuation at \(x=0\). Then
\[
D_c(H_n;x)=x^4\bigl(R_n(x)^2-C_n\bigr).
\]
Since \(R_n(0)=C_n>\sqrt{C_n}\) for \(n\ge3\), the root at zero has multiplicity exactly four. All nonzero real roots solve \(R_n(x)=\pm\sqrt{C_n}\).

**2. Integral representation and shape.** The integral form of the second-order Taylor remainder for \(u\mapsto(1+u)^n\) gives, for every real \(x\),
\[
R_n(x)=n(n-1)\int_0^1(1-t)(1+tx)^{n-2}\,dt.
\]
At the points needed below,
\[
R_n(-1)=n-1,\qquad
R_n(-2)=\begin{cases}(n-1)/2,&n\text{ odd},\\ n/2,&n\text{ even}.
\end{cases}
\]
For every \(n\ge3\),
\[
0<R_n(-2)<\sqrt{C_n}<R_n(-1).
\]
Indeed, \((n-1)/2<\sqrt{n(n-1)/2}\), \(n/2<\sqrt{n(n-1)/2}\) for even \(n\ge4\), and \(\sqrt{n(n-1)/2}<n-1\) for \(n>2\).

When \(n\) is **odd**, \(n-3\) is even, so
\[
R_n'(x)=n(n-1)(n-2)\int_0^1 t(1-t)(1+tx)^{n-3}\,dt>0
\]
for all real \(x\). Its leading coefficient is one and its degree \(n-2\) is odd, hence \(R_n\) increases strictly from \(-\infty\) to \(+\infty\). It takes \(-\sqrt{C_n}\) exactly once, to the left of \(-2\), and \(+\sqrt{C_n}\) exactly once, between \(-2\) and \(-1\). Both crossings are transverse, so both zeros are simple.

When \(n\) is **even**, \(n\ge4\), the exponent \(n-2\) in the integral representation is even, so \(R_n(x)>0\) for every real \(x\). Moreover
\[
R_n''(x)=n(n-1)(n-2)(n-3)
\int_0^1 t^2(1-t)(1+tx)^{n-4}\,dt>0,
\]
so \(R_n\) is strictly convex. It tends to \(+\infty\) at both ends and is below \(\sqrt{C_n}\) at \(-2\) but above it at \(-1\). Therefore the horizontal level \(\sqrt{C_n}\) is crossed exactly twice, once strictly to the left of \(-2\), once in \((-2,-1)\). Strict convexity and the fact that the level lies above the minimum ensure simple crossings. The negative level \(-\sqrt{C_n}\) is never attained. These arguments exhaust every possible real root.

**3. The root in \((-2,-1)\).** Put \(y_n=-\rho_n^+\in(1,2)\). For \(1\le y\le2\), the exact expression
\[
\frac{R_n(-y)}{n}=\frac1y+\frac{(1-y)^n-1}{ny^2}
\]
shows uniform convergence to \(1/y\), because the last term has absolute value at most \(2/n\). The equation \(R_n(-y_n)=\sqrt{C_n}\) and \(\sqrt{C_n}/n\to1/\sqrt2\) therefore give \(1/y_n\to1/\sqrt2\). Hence \(\rho_n^+\to-\sqrt2\).

**4. The root to the left of \(-2\).** Set \(y_n=-\rho_n^->2\) and \(\epsilon_n=y_n-2>0\), and put \(t_n=1+\epsilon_n\). We first prove \(\epsilon_n\to0\). For any fixed \(\delta>0\), the term \((1-y)^n\) in \(R_n(-y)\) at \(y=2+\delta\) dominates every linear-in-\(n\) term. It tends to \(+\infty\) for even \(n\), and to \(-\infty\) for odd \(n\), with magnitude larger than \(\sqrt{C_n}\). As \(R_n(-2)\in(0,\sqrt{C_n})\), the uniqueness in step 2 forces \(2<y_n<2+\delta\) for all sufficiently large \(n\). Thus \(y_n\to2\).

For even \(n\), using \(R_n(-y_n)=+\sqrt{C_n}\) in the numerator formula gives
\[
t_n^n=y_n^2\sqrt{C_n}+1-ny_n.
\]
Since \(y_n\to2\) and \(\sqrt{C_n}/n\to1/\sqrt2\),
\[
\frac{t_n^n}{n}\longrightarrow 2(\sqrt2-1)>0.
\]
For odd \(n\), using \(R_n(-y_n)=-\sqrt{C_n}\) instead gives
\[
t_n^n=y_n^2\sqrt{C_n}+ny_n-1,
\]
so
\[
\frac{t_n^n}{n}\longrightarrow2(\sqrt2+1)>0.
\]
On each parity subsequence, with the corresponding positive constant \(c_n\), we have \(t_n^n/n=c_n+o(1)\). Taking logarithms yields
\[
n\log(1+\epsilon_n)=\log n+\log c_n+o(1).
\]
Because \(\epsilon_n\to0\), this first implies \(\epsilon_n=O(\log n/n)\). Consequently \(n\epsilon_n^2\to0\) and replacing \(\log(1+\epsilon_n)\) by \(\epsilon_n+O(\epsilon_n^2)\) yields exactly
\[
n\epsilon_n=\log n+\log c_n+o(1).
\]
This completes the proof.

## Verification
A standalone standard-library Python program, `verify_crown.py`, constructs each crown graph, independently enumerates every vertex subset and tests both domination and connectivity by bitmask traversal. For all six integers \(3\le n\le8\), its entire vector of coefficients agrees with the displayed enumerator; the six exhaustive universes range from \(2^6\) through \(2^{16}\) subsets. Numerical bisection additionally checks the predicted strict root intervals for selected orders up to \(301\) and illustrates parity-sensitive convergence. The infinite-family theorem does **not** rely on finite computations or floating-point evaluations: its proof is the integral positivity/convexity argument and the exact asymptotic equations above. Run `python3 verify_crown.py` with Python 3.8 or newer to replay all finite checks.

## Relationship to prior work
The all-set crown connected-domination polynomial used in step 1 has already been obtained by a direct enumeration; neither that expression, its coefficients, nor the known connected domination number \(4\) is claimed here as a new result. Mojdeh and Emadi (2018) studied connected domination polynomials for many graph families, including complete bipartite graphs, which are not crowns because their matching edges are present. Yoosuf and Kuttipulackal (2021) considered other graph constructions. Kumar, Pomeroy and Tran (2025) obtained results involving crown graphs and their connected domination number, but not a real-root classification for this polynomial. Shao and Zhao (2026) established global density and substitution phenomena for connected domination roots using cycles and joins of cycles; those results neither locate the two crown real roots nor give their parity-sensitive convergence constants. The new theorem supplies an exact real-root classification and a logarithmic asymptotic with explicit even/odd constants for a natural, non-clique-blow-up graph family.

## Limitations
No assertion is made about the nonreal roots, their empirical spectral measure, or the complete complex zero-locus limit set. The polynomial identity is prior enumerative input; the specific new content is the all-order real-root theorem and its two-root asymptotics. A search of accessible literature and mathematical-record databases found no covering real-root statement, but absence from an index cannot establish absolute priority. The asserted infinite-family properties follow from the exact analytic inequalities and limits proved above.

## References
1. P. Shao and C. Zhao, *On the Roots of Connected Domination Polynomials*, arXiv:2609.06569 (first version 6 September 2026, then under a different title), https://arxiv.org/abs/2609.06569.
2. D. A. Mojdeh and A. S. Emadi, *Connected Domination Polynomial of Graphs*, Fasciculi Mathematici 60 (2018), DOI: 10.1515/fascmath-2018-0007.
3. R. Yoosuf and P. Kuttipulackal, *The connected domination polynomial of some graph constructions*, Journal of Physics: Conference Series 1850 (2021), 012043, DOI: 10.1088/1742-6596/1850/1/012043.
4. A. Kumar, J. Pomeroy and L. Tran, *Binomial Edge Ideals of Crown Graphs*, arXiv:2507.03889, https://arxiv.org/abs/2507.03889.
5. E. W. Weisstein, *Connected Domination Number*, MathWorld, https://mathworld.wolfram.com/ConnectedDominationNumber.html (crown minimum of four is tabulated).
