# Exact RK4 positivity for three-subset Johnson diffusion: the sharp 34-point crossover

## Finding

Let \(n\ge6\) be an integer. On the Johnson graph \(J(n,3)\), whose vertices are the three-element subsets of \(\{1,\ldots,n\}\) and whose edges join subsets differing in exactly one element, let \(L\) be the unit-conductance combinatorial Laplacian. The completed classical four-stage, fourth-order Runge–Kutta diffusion step is
\[
T_n(h)=I-hL+\frac{h^2L^2}{2}-\frac{h^3L^3}{6}+\frac{h^4L^4}{24},\qquad h\ge0.
\]
Put
\[
h_3(n)=\frac{2}{3n-4},\qquad
f_n(h)=24-(60n-192)h+(76n^2-440n+608)h^2
-(65n^3-524n^2+1328n-1024)h^3.
\]
The polynomial \(f_n\) has exactly one positive root, denoted \(h_1(n)\). The **complete entrywise-positivity classification** is
\[
T_n(h)\ge0\ \text{entrywise}\quad\Longleftrightarrow\quad
0\le h\le H_n,\qquad
H_n=\begin{cases}
2/(3n-4),&6\le n\le33,\\
h_1(n),&n\ge34.
\end{cases}
\]
For \(6\le n\le33\), distance three is the first off-diagonal class to reach zero and remains negative after that threshold. For \(n\ge34\), distance one is the first class to reach zero and remains negative after its threshold. Other classes may also become negative at larger timesteps. At the sharp endpoint exactly one of these two off-diagonal distance classes vanishes, and all remaining entries are positive. There is no reentrant interval of nonnegativity at larger steps.

As a consequence, \(H_n>1/[3(n-3)]\), the forward-Euler nonnegativity limit on this graph.

## Assumptions and scope

All graphs are finite, simple, undirected, unweighted and connected. There are \(\binom n3\) vertices and graph degree \(d=3(n-3)\). The graph distance between two vertices \(X,Y\) is \(3-|X\cap Y|\), taking values in \(\{0,1,2,3\}\). The diffusion equation is \(u'=-Lu\); nonnegativity means that every matrix entry of the **completed endpoint** operator \(T_n(h)\) is nonnegative, equivalently that the completed step sends every nonnegative initial vector to a nonnegative vector. Intermediate RK stages are not part of this assertion.

## Proof

**1. Exact entries by distance.** Let \(A_j\) denote the \(0\)-\(1\) matrix of Johnson distance \(j\), so \(A_0=I\) and \(A_1=A\). Put \(Q=A-dI=-L\). Directly counting adjacent three-subsets of a set at distance \(j\) from a fixed set gives the intersection numbers
\[
b_j=(3-j)(n-3-j),\quad c_j=j^2,\quad
a_j=d-b_j-c_j,\quad 0\le j\le3,
\]
with \(c_0=b_3=0\). They imply the multiplication identities
\[
Q A_j=b_{j-1}A_{j-1}+(a_j-d)A_j+c_{j+1}A_{j+1},
\]
where out-of-range terms are absent. Iterating this identity four times from \(Q^0=A_0\) and summing \(T_n(h)=\sum_{m=0}^4h^mQ^m/m!\), write
\(T_n(h)=\sum_{j=0}^3 t_j(n,h)A_j\). Its off-diagonal coefficients are exactly
\[
\begin{aligned}
t_1(n,h)&=\frac h{24}\left[24-(60n-192)h+(76n^2-440n+608)h^2\\
&\hspace{50pt}-(65n^3-524n^2+1328n-1024)h^3\right],\\
t_2(n,h)&=\frac{h^2}{6}\left[12+(68-24n)h+(25n^2-124n+124)h^2\right],\\
t_3(n,h)&=3h^3\big[2-(3n-4)h\big].
\end{aligned}
\]
These are coefficients per ordered pair, not totals over the distance orbits. They determine all off-diagonal entries.

**2. The diagonal and distance-two entries never fail.** For each real \(x\ge0\), the scalar RK4 polynomial is strictly positive because
\[
24\left(1-x+\frac{x^2}{2}-\frac{x^3}{6}+\frac{x^4}{24}\right)
=(x^2-2x)^2+8(x^2-3x+3)>0.
\]
Since \(L\) is real symmetric positive semidefinite, its orthogonal spectral resolution expresses each diagonal entry of \(T_n(h)\) as a convex combination of these positive scalar values; hence \(t_0(n,h)>0\) for all \(h\ge0\). The quadratic bracket in \(t_2/h^2\) has positive leading coefficient and discriminant
\[
(68-24n)^2-48(25n^2-124n+124)
=-16(39n^2-168n+83)<0\qquad(n\ge6).
\]
Therefore \(t_2(n,h)>0\) for every \(h>0\).

**3. A unique edge-positivity cutoff.** Write \(f_n(h)=24-Ah+Bh^2-Ch^3\) with
\[
A=60n-192,\quad B=76n^2-440n+608,\quad C=65n^3-524n^2+1328n-1024.
\]
All three coefficients are positive for \(n\ge6\). With \(m=n-6\ge0\), exact expansion gives
\[
3AC-B^2=5924m^4+77296m^3+366592m^2+755264m+572864>0.
\]
Thus \(f'_n(h)=-A+2Bh-3Ch^2<0\) on the real line, because its maximum is \(-A+B^2/(3C)<0\). As \(f_n(0)=24\) and \(f_n(h)\to-\infty\) when \(h\to\infty\), \(f_n\) has exactly one positive root and \(t_1(n,h)\) is positive before, zero at and negative after that root.

**4. Exact crossover.** The distance-three coefficient is nonnegative precisely on \(0\le h\le h_3(n)\). At that endpoint, direct substitution yields
\[
t_1\big(n,h_3(n)\big)
=-\frac{2 F(n)}{3(3n-4)^4},\qquad
F(n)=5n^3-180n^2+496n-384.
\]
For \(6\le n\le33\), put \(z=(n-6)/27\in[0,1]\). The exact Bernstein-basis identity
\[
F(n)=-2808(1-z)^3-3(12924)z(1-z)^2
-3(44910)z^2(1-z)-351z^3<0
\]
shows that the edge coefficient remains positive when the distance-three coefficient first reaches zero. For \(n\ge34\), put \(m=n-34\ge0\). Then
\[
F(n)=5m^3+330m^2+5596m+4920>0.
\]
The strictly decreasing edge cubic therefore vanishes before \(h_3(n)\). In each case the other distance class is strictly positive at the first cutoff. At all larger timesteps the first-failing class is strictly negative by the global sign properties already established, so positivity cannot return. This proves the classification and the absence of additional boundary ties.

**5. Forward-Euler comparison.** At \(h_{\mathrm{FE}}=1/d\), writing \(P=A/d\) gives
\[
T_n(1/d)=\tfrac38 I+\tfrac13 P+\tfrac14 P^2+\tfrac1{24}P^4.
\]
All entries are nonnegative, and adjacent-pair entries are strictly positive since \(P\) has positive edge entries. Moreover \(h_3(n)>1/d\) for \(n\ge6\), so the distance-three entries are also strictly positive at \(1/d\), while distance-two and diagonal entries are strictly positive. Continuity, combined with their strict positivity, proves \(H_n>1/d\).

## Verification

Run `python verify.py` with `sympy` and `numpy` installed (versions are not mathematically material; see `requirements.txt`). The program reconstructs the Johnson distance-matrix multiplication algebra, verifies the three off-diagonal RK4 polynomial identities and the discriminant/positivity certificates, and compares those identities against directly constructed integer graph Laplacians and exact rational RK4 matrices for \(6\le n\le12\). At three rational timesteps for each tested graph it checks the entire first row, covering every distance class. The observed execution output was:

`VERIFY_OK: 3 symbolic distance-transition identities, 6 sign/threshold certificates, 2100 independent exact rational matrix entries, sharp n=34 switch`

These finite checks independently test formulas but do not replace the symbolic all-\(n\) proof above.

## Relationship to prior work

Hora's 2004 work studies spectral limits of Johnson-graph adjacency operators and explains the Bernoulli–Laplace interpretation; it supplies motivation and standard distance-regular algebra, not RK4 endpoint positivity. Bresten and collaborators' 2013 SSP work develops multistep Runge–Kutta methods and optimized general SSP coefficients, rather than the completed **classical RK4** step on \(J(n,3)\). Blanes, Iserles and Macnamara study graph-Laplacian-based positivity-preserving integrators and the limitations of universally and unconditionally positive classical schemes; the graph-specific, step-restricted positivity criterion here is not a consequence of their unconditional results. Earlier exact RK4 claims for Hamming graphs, complete multipartite graphs, weighted stars, and strongly regular graphs do not subsume the diameter-three Johnson family. No matching exact Johnson three-subset threshold was found in the searches described in `AUDIT.json`.

## Limitations

The theorem concerns the completed standard RK4 endpoint for **unit-weight** Johnson graphs with exactly three elements per vertex and integers \(n\ge6\); it makes no claim about arbitrary Johnson parameter \(k\), weighted or directed models, intermediate RK stages, or positivity for general nonlinear equations. The numerical crossover is exact for this graph family; it is not asserted to be universal for other distance-regular graphs. Self-review has been performed, but an independent mathematical audit has not.

## References

1. A. Hora, *Asymptotic Spectral Analysis on the Johnson Graphs in Infinite Degree and Zero Temperature Limit*, Interdisciplinary Information Sciences **10** (2004), 1–10, doi:10.4036/iis.2004.1 (publicly available on J-STAGE March 5, 2004).
2. C. Bresten, S. Gottlieb, Z. Grant, D. Higgs, D. I. Ketcheson and A. Németh, *Explicit Strong Stability Preserving Multistep Runge–Kutta Methods*, arXiv:1307.8058 (initial public submission July 30, 2013).
3. S. Blanes, A. Iserles and S. Macnamara, *Positivity-preserving methods for ordinary differential equations*, arXiv:2102.08242 (initial public submission February 16, 2021).
