# Two spectral thresholds and all minimizers of the seven-cycle weighted Schatten-fourth radius

## Finding

Let \(W\) be an arbitrary complex weighted seven-cycle on \(\mathbb C^7\), \(We_j=a_je_{j+1\pmod7}\), normalized by \(\sum_{j=0}^6|a_j|^2=1\). For \(0\le t\le1\), put
\[
\mathcal R_{t,4}(W)=\max_{\theta\in\mathbb R}\|te^{i\theta}W+(1-t)e^{-i\theta}W^*\|_{\mathcal S_4},\quad A=t^4+(1-t)^4,\quad q=\frac{4t^2(1-t)^2}{A}.
\]
Thus \(0\le q\le2\). Define the two exact thresholds \(q_1=\sec(\pi/7)\) and \(q_2=\sqrt5-1=\sec(\pi/5)\). The sharp minimax value is
\[
\boxed{\min_{\sum|a_j|^2=1}\mathcal R_{t,4}(W)^4=A\,m(q),\qquad
m(q)=\begin{cases}
(1+q)/7,&0\le q\le q_1,\\
(4+2q-q^2)/(20-2q-q^2),&q_1\le q\le q_2,\\
(q+2)/(2(q+4)),&q_2\le q\le2.
\end{cases}}
\]

The minimizing squared-weight vectors \(x_j=|a_j|^2\), with indices modulo seven, are **exactly** the following. The complex phases of all weights are unrestricted.

For \(0\le q<q_1\), the unique vector is uniform: \(x_j=1/7\) for each \(j\). At \(q=q_1\) the complete equality set is the nonnegative two-dimensional Fourier slice
\[
x_j=\frac17+u\cos\frac{6\pi j}{7}+v\sin\frac{6\pi j}{7}\ge0,\qquad u,v\in\mathbb R.
\]
For \(q_1<q<q_2\), the seven minimizing vectors are precisely the cyclic rotations of
\[
\left(a,0,b,c,c,b,0\right),\quad d=20-2q-q^2,\quad a=\frac{4+2q-q^2}{d},\quad b=\frac4d,\quad c=\frac{2(2-q)}d.
\]
At \(q=q_2\), all minimizers are the cyclic rotations of the **closed line segments**
\[
(a,0,b+\tau\sin(\pi/5),c-\tau\sin(2\pi/5),c+\tau\sin(2\pi/5),b-\tau\sin(\pi/5),0),
\quad |\tau|\le\frac{c}{\sin(2\pi/5)},
\]
with \(a,b,c\) evaluated at \(q=q_2\). For \(q_2<q<2\), the seven minimizers are precisely the rotations of
\[
\left(a,0,b,0,b,0,a\right),\quad a=\frac1{q+4},\qquad b=\frac{q+2}{2(q+4)}.
\]
Finally, at \(q=2\), the complete equality family is the rotations of
\[
\left(s,0,\tfrac13,0,\tfrac13,0,\tfrac13-s\right),\qquad0\le s\le\tfrac13.
\]
In particular the seven-cycle has two distinct support transitions, first from full uniform support to five nonzero weights, then to four; both transition fibers are described exactly.

## Assumptions and scope

The theorem concerns arbitrary complex weights, including zero weights, a fixed directed cycle of size seven, and the Schatten-fourth norm with the convention \(\|B\|_{\mathcal S_4}^4=\operatorname{tr}((B^*B)^2)\). The normalization is the Frobenius squared norm \(\operatorname{tr}(W^*W)=1\); rescaling by \(r>0\) multiplies all fourth powers by \(r^4\). This is a global minimum over **all** seven-tuples of complex weights, not a permutation optimization for fixed weights.

## Proof

**1. Exact reduction.** Put \(x_j=|a_j|^2\), \(u=t\), \(v=1-t\) and \(Z_\theta=ue^{i\theta}W+ve^{-i\theta}W^*\). In the seven-cycle, every potentially phase-dependent trace word of length four has nonzero net displacement modulo seven, hence zero trace. Direct multiplication yields
\[
\operatorname{tr}((Z_\theta^*Z_\theta)^2)
=(u^4+v^4)\sum_jx_j^2+4u^2v^2\sum_jx_jx_{j+1}.
\]
The expression is independent of \(\theta\) and of all complex weight phases. It remains to minimize
\[
F_q(x)=\sum_jx_j^2+q\sum_jx_jx_{j+1}
\]
over the simplex \(x_j\ge0\), \(\sum_jx_j=1\).

**2. Uniform regime.** Let \(G_q=I+(q/2)\operatorname{Adj}(C_7)\). Then \(F_q(x)=x^TG_qx\), and its smallest eigenvalue is \(1-q\cos(\pi/7)\). Since \(G_q\mathbf1=(1+q)\mathbf1\), decomposing \(x=\mathbf1/7+y\) with \(\sum y_j=0\) gives \(F_q(x)=(1+q)/7+y^TG_qy\). For \(q<q_1\), positivity is strict on zero-sum vectors, hence only the uniform minimizer. At \(q=q_1\), the kernel is exactly the real span of Fourier frequencies three and four, yielding the stated complete nonnegative Fourier slice.

**3. Reduction to a five-vertex face for \(q>q_1\).** If all seven entries of a minimizer were positive, a zero-sum negative eigenvector of \(G_q\) would decrease the energy. Six positive entries likewise form an induced path of six vertices: the alternating sine vector \(z_k=(-1)^{k+1}\sin(k\pi/7)\), \(1\le k\le6\), has sum zero and negative quadratic energy \((1-q\cos(\pi/7))\|z\|^2\). Hence an optimizer has at most five nonzero entries.

If exactly five entries are positive, examine the two missing vertices. Adjacent missing vertices leave a path of length five. For \(1<q<2\), stationarity on that path forces the symmetric pattern \((a,b,c,b,a)\) with
\[
a=\frac{q^2+2q-4}{q^2+16q-20},\quad b=\frac{4(q-1)}{q^2+16q-20},\quad c=-\frac{(q-2)^2}{q^2+16q-20}.
\]
If the common denominator vanishes, the stationarity equations have no normalized solution; otherwise either \(b<0\) or \(c<0\), contradicting strict positivity. The other nonadjacent pattern, missing vertices three steps apart, leaves a three-vertex path and a two-vertex path. In the three-path, stationarity forces equal endpoint masses \(a>0\) and central mass \(b>0\) with \((2-2q)a=(2-q)b\), impossible for \(1<q<2\). Thus the only possible five-positive-support configuration is one isolated vertex plus a four-vertex path, obtained when the two missing vertices are two steps apart.

If four entries are positive, the three absent vertices either contain a pair two steps apart, so the vector lies in one of those same five-vertex faces, or the absent set is (up to rotation) \(\{0,1,4\}\). In the latter case, the four surviving vertices form two disjoint edges, and their energy is at least \((2+q)/8\). If at most three entries are positive, the energy is at least \(\sum x_j^2\ge1/3\).

**4. Optimizing each surviving face.** On a face with pattern \((a,0,b,c,c,b,0)\), the induced graph is a singleton and a four-path. For \(q<q_2=1/\cos(\pi/5)\), the face Gram matrix is strictly positive definite. Its unique constrained minimizer, obtained from \(G_{\mathrm{face}}x=\lambda\mathbf1\), is the positive vector shown above; because \(\sum x_j=1\), its energy equals \(a=(4+2q-q^2)/(20-2q-q^2)\). This is strictly below \(1/3\), and below the exceptional two-edge-face lower bound, throughout \(q_1<q<q_2\). As every global minimum must lie on one of these faces or on a worse lower-support face, this is the global value and complete equality family.

At \(q=q_2\), the four-path matrix is positive semidefinite with one-dimensional null vector proportional to \((\sin(\pi/5),-\sin(2\pi/5),\sin(2\pi/5),-\sin(\pi/5))\), whose coordinates sum to zero. The full face equality set is therefore the displayed line segment obtained by adding that vector to its stationary point and imposing nonnegativity. Its endpoints have one more zero coordinate. There are no additional global minimizers outside the seven faces.

For \(q_2<q<2\), the same four-path null-direction becomes strictly negative while remaining zero-sum. Hence a minimizing vector cannot have all four path masses positive, and must lie in a lower-dimensional face. If an endpoint of the path is deleted, the remaining three-path plus singleton has no all-positive stationary point for \(q>1\), by the three-path identity in Step 3; further deletions yield energy at least \(1/3\). Deleting an interior path vertex instead yields one adjacent pair and two isolated vertices, with positive definite energy
\[
(2+q)a^2+2b^2,\qquad 2a+2b=1.
\]
Its unique minimum has \(a=1/(q+4)\), \(b=(q+2)/(2(q+4))\), and energy \((q+2)/(2(q+4))<1/3\). The exceptional four-support pattern of two disjoint edges has energy at least \((2+q)/8\), strictly larger. This proves the last open-regime formula and rigidity.

At \(q=2\), the sharp value reaches \(1/3\). The same support argument rules out supports of size five or more (a five-positive path also has a four-path negative direction, while a three-path component forces an endpoint to vanish at stationarity). Among four-supported configurations, equality is possible only for one edge and two isolated vertices: the two isolates each have mass \(1/3\), and the two edge masses sum to \(1/3\). All three-supported equality cases are independent triples of equal mass, already included as endpoints. This gives the stated complete final segment family.

The three formulas agree at both thresholds, by the defining spectral equations, completing the proof.

## Verification

The included standalone program `checks/verify.py` verifies the phase-independent trace identity by direct complex matrix multiplication, checks all closed-form candidate energies, enumerates the exceptional four-support pattern, and compares with seeded random simplex samples across the parameter range. It returned `DIAGNOSTICS_OK 54579`. This is finite corroboration, **not** a substitute for the analytic support and stationary-point arguments above. The critical eigenvalue formulas, endpoint domains, and inequalities can be checked directly from the displayed quadratic forms.

## Relationship to prior work

Pal and Chandok (first public version dated 2026-10-08) investigate weighted Schatten numerical radii and generalized Aluthge inequalities. Their full text develops inequalities for general operators, including matrix examples, but does not establish a seven-cycle fixed-Frobenius minimax classification or the two spectral support thresholds here. Frakis, Kittaneh, and Soltani (2025) likewise investigate bounds via the Aluthge transform, not this simplex minimum. Prior numerical-radius work for weighted cyclic matrices addresses the ordinary numerical radius and permutation optimization rather than fourth Schatten minimization over unrestricted weights. Fourth-power minimax calculations for shorter cycles have different support geometry; the second spectral threshold and the intervening five-site regime require an additional face analysis.

## Limitations

The result is specific to a seven-cycle, fourth Schatten power, and Frobenius normalization. It does not assert an analogous phase diagram for every odd cycle, for operator-norm numerical radii, or for all Schatten exponents. The analysis is exact for this natural finite family; its publication priority against obscure earlier quadratic-programming or copositivity formulations is not independently established.

## References

1. K. Pal and S. Chandok, *On weighted Schatten p-numerical radii via generalized Aluthge transformation*, arXiv:2610.11336v1 (first posted 2026-10-08), https://arxiv.org/abs/2610.11336.
2. A. Frakis, F. Kittaneh, and S. Soltani, *p-Numerical radii of operators via the t-Aluthge transform*, Linear and Multilinear Algebra 73 (2025), 1448–1461; reference [7] in Pal–Chandok.
3. C.-T. Chang and K.-Z. Wang, *Maximizing numerical radii of weighted shifts under weight permutations*, Journal of Mathematical Analysis and Applications 394 (2012), 592–602, DOI 10.1016/j.jmaa.2012.04.039.
