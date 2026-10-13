# Sharp complementary quantum-walk contrasts on the four-vertex path

## Finding

Let \(P_4\) be the simple path with vertices \(1-2-3-4\). Its complement has edges \(\{1,3\},\{1,4\},\{2,4\}\), and is itself a path. Write \(A=A(P_4)\), \(B=A(P_4^c)=J-I-A\), \(U(t)=e^{itA}\), and \(V(t)=e^{itB}\). For all ordered pairs \((u,v)\) and all real \(t\), define

\[
\begin{aligned}
f_{uv}(t)&=\left|V_{uv}(t)-e^{-it}U_{uv}(-t)\right|,\\
g_{uv}(t)&=\left||U_{uv}(t)|-|V_{uv}(t)|\right|,\\
\sigma_{uv}(t)&=|U_{uv}(t)|+|V_{uv}(t)|,\\
\rho_{uv}(t)&=|U_{uv}(t)|\,|V_{uv}(t)|.
\end{aligned}
\]

**Theorem.** Every ordered pair belongs to exactly one of two classes, with all four sharp suprema given below:

| Vertex-pair class | \(\sup_t f_{uv}\) | \(\sup_t g_{uv}\) | \(\sup_t \sigma_{uv}\) | \(\sup_t \rho_{uv}\) |
|---|---:|---:|---:|---:|
| Same degree class | \(1\) | \(2/(1+\sqrt5)\) | \(2\) | \(1\) |
| Opposite degree classes | \(2/\sqrt5\) | \(2/\sqrt5\) | \(2\sqrt{2/5}\) | \(2/5\) |

Here the first class means either both vertices are in \(\{1,4\}\), or both are in \(\{2,3\}\), including diagonal pairs. The second class means one vertex lies in each set. All suprema are over \(t\in\mathbb R\). The values are exact even when approached only asymptotically along sequences of times.

## Assumptions and scope

The model is the continuous-time adjacency quantum walk with unit edge couplings; no Laplacian or normalized adjacency convention is used. Matrices act on the one-excitation four-dimensional Hilbert space. The phase \(e^{-it}\) in \(f\) corresponds exactly to the identity \(A(P_4^c)=J-I-A(P_4)\). There are no other graphs, longer paths, perturbations, different edge weights, or multi-excitation dynamics in the assertion.

## Proof

Let \(R\) reverse the four vertices. Both \(A\) and \(B\) commute with \(R\). On the symmetric sector with orthonormal basis \((e_1+e_4)/\sqrt2,(e_2+e_3)/\sqrt2\), and the antisymmetric sector with basis \((e_1-e_4)/\sqrt2,(e_2-e_3)/\sqrt2\), respectively, their blocks are

\[
A_+=\begin{pmatrix}0&1\\1&1\end{pmatrix},\quad
A_-=\begin{pmatrix}0&1\\1&-1\end{pmatrix},\quad
B_+=\begin{pmatrix}1&1\\1&0\end{pmatrix},\quad
B_-=-I_2-A_-.
\]

Set \(r=\sqrt5/2\), \(c=\cos(rt)\), \(s=\sin(rt)\), \(C=\cos(t/2)\), and \(S=\sin(t/2)\). Each traceless part of a block squares to \(5I_2/4\), hence its exponential is the cosine of \(rt\) times the identity plus \(i\sin(rt)/r\) times the traceless part. Resolving vertex coordinates gives, up to exchanging the two members in a displayed pair, the following complete amplitudes:

\[
\begin{array}{c|cc}
\text{pair type}&U_{uv}(t)&V_{uv}(t)\\\hline
u=v=1\text{ or }4&cC+sS/\sqrt5&cC-sS/\sqrt5\\
u=v=2\text{ or }3&cC-sS/\sqrt5&cC+sS/\sqrt5\\
\{u,v\}=\{1,4\}&i(cS-sC/\sqrt5)&i(cS+sC/\sqrt5)\\
\{u,v\}=\{2,3\}&i(cS+sC/\sqrt5)&i(cS-sC/\sqrt5)\\
\{u,v\}=\{1,2\}\text{ or }\{3,4\}&2isC/\sqrt5&-2sS/\sqrt5\\
\{u,v\}=\{1,3\}\text{ or }\{2,4\}&-2sS/\sqrt5&2isC/\sqrt5
\end{array}
\]

All amplitudes are symmetric in \(u,v\). For diagonal same-degree pairs put \(a=|cC|\), \(b=|sS|/\sqrt5\); for nondiagonal same-degree pairs put \(a=|cS|\), \(b=|sC|/\sqrt5\). In both cases, the two moduli are \(|a+b|,|a-b|\), where the signs inside the absolute values may be absorbed into the underlying signed factors. Thus

\[
g=2\min(a,b),\qquad \sigma=2\max(a,b),\qquad \rho=|a^2-b^2|.
\]

For every opposite-degree pair the two moduli are \(2|sC|/\sqrt5\) and \(2|sS|/\sqrt5\), giving

\[
\begin{aligned}
g&=\frac{2|s|}{\sqrt5}\big||C|-|S|\big|,\\
\sigma&=\frac{2|s|}{\sqrt5}(|C|+|S|),\\
\rho&=\frac45s^2|CS|.
\end{aligned}
\]

For the complex contrast, define \(D(t)=V(t)-e^{-it}U(-t)\). The antisymmetric block is identically zero because \(B_-=-I_2-A_-\). Direct exponentiation of the symmetric blocks, in Pauli coordinates, yields

\[
D_+(t)=e^{-it/2}\left[2ic\sin t\,I_2+\frac{4is}{\sqrt5}\cos t\,\sigma_x-\frac{2s}{\sqrt5}\sin t\,\sigma_z\right].
\]

Each matrix element of \(D\) in the original vertex basis equals half an appropriate entry of \(D_+\), with possible sign. Consequently,

\[
f_{uv}(t)=\begin{cases}
|\sin t|\sqrt{c^2+s^2/5},&\text{same degree class},\\[3pt]
(2/\sqrt5)|s\cos t|,&\text{opposite degree classes}.
\end{cases}
\]

The displayed formulas immediately imply all upper bounds. In particular, for same-degree pairs \(a,b\ge0\) satisfy \(a+\sqrt5\,b\le1\) by Cauchy--Schwarz, so \(2\min(a,b)\le2/(1+\sqrt5)\). Equality in this bound on the phase torus occurs when the relevant paired coordinates have squared magnitudes \(1/(1+\sqrt5)\) and \(\sqrt5/(1+\sqrt5)\). For opposite-degree pairs use \(|C|+|S|\le\sqrt2\) and \(|CS|\le1/2\). The remaining bounds use \(|c|,|s|,|C|,|S|\le1\).

Finally, \(\sqrt5\notin\mathbb Q\) implies that \(t\mapsto(rt\bmod2\pi,t/2\bmod2\pi)\) is dense in the two-torus. All formulas above are continuous on this torus. Hence independent choices of \((c,s)\) and \((C,S)\) optimizing each inequality can be approached at actual times: for instance, \(|s|=1\) and \(|C|=|S|=1/\sqrt2\) give the opposite-degree sum/product extrema, whereas \(|c|=|C|=1\) gives the same-degree sum/product extrema. The explicit balancing choices give the same-degree difference extremum, and the formulas for \(f\) attain their stated bounds on the phase torus. This proves **sharpness as suprema over real times**, completing the proof.

## Verification

The standalone `verify.py` computes both matrix exponentials independently by scaled complex Taylor series and repeated squaring, then compares every ordered matrix entry with the four closed-form expressions for 201 deterministic times. It checks 12,864 scalar comparisons and also evaluates all four proposed bounds for both classes on 116,733 torus-grid phase pairs. Running `python3 verify.py` produces the `VERIFY_OK` line. These checks corroborate formulas; torus density and the all-time sharp bounds are proved analytically above rather than inferred from a grid.

## Relationship to prior work

Coutinho, Guo and Schmeits [1], publicly available May 17, 2025, study peak state transfer and spectral upper bounds for continuous-time quantum walks, with finite small-graph classifications. Those bounds address **individual** state-transfer amplitudes and do not state the exact four simultaneous graph/complement comparisons for all pairs of the four-vertex path. In later work dated October 6, 2026, Cooper and collaborators [2] introduce exactly these four complement-comparison functions and give general graph bounds, including degree-based inequalities. Their general inequalities are not equalities on the opposite-degree pairs of this graph: the bound \(f\le1\) is strictly above \(2/\sqrt5\). Their Section 10 asks for tight bounds on paths; the present calculation explicitly resolves the four-vertex case. Their known pretty-good-transfer observations can already account for some trivial \(\sigma=2\) and \(\rho=1\) endpoints; these are included here for completeness, not as separate new findings. The substantive exact data include the opposite-degree \(\sigma\) and \(\rho\) extrema and the same-/opposite-degree \(g\) values.

## Limitations

This is a complete **four-vertex** benchmark, not a theorem for all paths. Supremum need not be a maximum at any finite time. The numerical checker cannot establish irrational torus density or infinite-time optimality; those require the analytic proof. An implicit equivalent evaluation within a general spectral formula or an unindexed existing calculation remains possible. No device-level noise, control protocol, or claimed physical advantage is established.

## References

[1] G. Coutinho, K. Guo and V. Schmeits, *Peak state transfer in continuous quantum walks*, arXiv:2505.11986v1, first public May 17, 2025, especially Sections 2--3 and 6.4.

[2] J. Cooper, H. De Vera, H. Monterde, S. A. Talebpour and X. Wang, *Quantum walks and graph operations*, arXiv:2610.07673v1, first public October 6, 2026; Sections 6--8 and 10 (later comparison literature).

[3] M. Kempton and J. Tolbert, *Isospectral reductions and quantum walks on graphs*, Algebraic Combinatorics 7 (2024), 225--243, doi:10.5802/alco.333 (background on graph spectral reductions).
