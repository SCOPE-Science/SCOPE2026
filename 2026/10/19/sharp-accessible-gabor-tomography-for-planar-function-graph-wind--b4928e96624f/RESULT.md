# Sharp accessible Gabor tomography for planar-function graph windows

## Finding
Let \(q\ge5\) be any odd prime power, let \(F:\mathbb F_q\to\mathbb F_q\) be planar, and put \(C_F=\{(x,F(x)):x\in\mathbb F_q\}\subseteq G=\mathbb F_q^2\). In \(H=\ell^2(G)\) of dimension \(N=q^2\), take a unit vector \(g\) supported on \(C_F\). Its full time-frequency orbit consists of the \(N^2\) rank-one projectors \(P_{h,\omega}=W_{h,\omega}gg^*W_{h,\omega}^*\), where \(W_{h,\omega}=M_\omega T_h\). Let \(\mathcal S_g\) be their Hilbert–Schmidt operator-frame operator, and let \(\mathcal K\) be the fixed Weyl-coordinate space whose translation coordinate is either \(h=(0,0)\) or \(h=(u,v)\) with \(u\ne0\).

The space \(\mathcal K\), of complex dimension \(q^4-q^3+q^2\), is the largest Weyl-coordinate space on which some projector orbit with graph support can be complete. In fact, there exists a graph-supported \(g\) making \(\mathcal S_g|_{\mathcal K}\) invertible if and only if \(F\) is planar. For every planar \(F\), the **sharp restriction-condition theorem** is
\[
\inf_{\substack{\|g\|_2=1,\\\operatorname{supp}g=C_F}}\operatorname{cond}(\mathcal S_g|_{\mathcal K})=(q+1)^2.
\]
The condition number is \(+\infty\) when the restriction is singular. **All and only** the optimizing windows have, for some \(x_0\in\mathbb F_q\),
\[
|g(x,F(x))|^2=\begin{cases}2/(q+1),&x=x_0,\\1/(q+1),&x\ne x_0,\end{cases}
\]
with arbitrary phases at the \(q\) occupied coordinates. For these windows, the largest and smallest positive eigenvalues of \(\mathcal S_g|_{\mathcal K}\) are, respectively, \(q^2\) and \(q^2/(q+1)^2\). Hence the associated analysis map restricted to \(\mathcal K\) has sharp singular-value condition number \(q+1\).

## Assumptions and scope
All sums and inner products on \(G\) and \(H\) use counting measure. Fix any nontrivial additive character \(\psi:\mathbb F_q\to\mathbb C\), and define
\[
(T_hf)(z)=f(z-h),\qquad (M_{(\alpha,\beta)}f)(x,y)=\psi(\alpha x+\beta y)f(x,y).
\]
A function \(F\) is **planar** if \(x\mapsto F(x)-F(x-u)\) is a bijection of \(\mathbb F_q\) for each \(u\ne0\). This property holds, for example, for \(F(x)=x^2\) in every odd characteristic. Write
\[
\mathcal S_g(X)=\sum_{h\in G}\sum_{\omega\in G}\langle X,P_{h,\omega}\rangle_{HS}P_{h,\omega},\quad
\langle X,Y\rangle_{HS}=\operatorname{tr}(XY^*),
\]
and
\[
\mathcal K=\operatorname{span}_{\mathbb C}\{W_{(u,v),\omega}: u\ne0\text{ or }(u,v)=(0,0),\ \omega\in G\}.
\]
This is a fixed complex operator subspace, not the full matrix algebra or a promise of full-state quantum informational completeness. The sharp theorem concerns finite-field sizes \(q\ge5\) only, and all complex phases are allowed.

## Proof
**1. Weyl diagonalization.** The \(N^2\) Weyl operators form a Hilbert–Schmidt orthogonal basis, all with squared norm \(N\). The commutator character of \(W_{h,\omega}\) diagonalizes conjugation by the entire Weyl orbit. Orthogonality of those \(N^2\) commutator characters gives
\[
\mathcal S_g(W_{h,\omega})=N|A_g(h,\omega)|^2W_{h,\omega},\qquad A_g(h,\omega)=\langle g,W_{h,\omega}g\rangle.
\]
This is the established Gabor-projector spectral mechanism; the new extremal problem below optimizes its eigenvalues under a relative-difference-set support restriction.

**2. Geometry of accessible shifts.** If \(h=(0,v)\) with \(v\ne0\), the graph and its translate are disjoint, so all \(q^2\) values \(A_g(h,\omega)\) vanish, independently of the weights. There are \(q(q-1)+1\) allowed shifts, giving \(\dim\mathcal K=q^2[q(q-1)+1]\). When \(u\ne0\), intersections \(C_F\cap(C_F+(u,v))\) are solutions of \(F(x)-F(x-u)=v\). They consist of exactly one point for each \(v\) precisely when \(F\) is planar. In that case, if the occupied amplitudes \(g_x=g(x,F(x))\) are nonzero,
\[
|A_g((u,v),\omega)|=|g_xg_{x-u}|,
\]
independently of \(\omega\). For a nonplanar map, some \(u\ne0\) has a derivative that is not bijective; one value \(v\) is omitted, forcing an entire missing Weyl row inside \(\mathcal K\), for every graph-supported window. Conversely, when \(F\) is planar, the displayed spike window below has all allowed ambiguity coefficients nonzero. This proves the existence equivalence and largest fixed accessible Weyl-space assertion.

**3. Sharp probability lemma.** Let \(p_x=|g_x|^2>0\), so \(\sum_xp_x=1\), and write the two least masses as \(0<a\le b\). Put \(t=1/(q+1)\). We prove that if \(ab\ge t^2\), then
\[
\sum_xp_x^2\le(q+3)t^2,
\]
with equality only when the masses are \(t,t,\ldots,t,2t\), in any order. Indeed the remaining \(q-2\) masses are at least \(b\). By concentration at the largest coordinate and convexity,
\[
\sum_xp_x^2\le a^2+(q-2)b^2+[1-a-(q-2)b]^2.
\]
The right side decreases as \(b\) grows across its feasible interval \(b\le(1-a)/(q-1)\); it is therefore at most the expression with \(b_0=\max\{a,t^2/a\}\). If \(a\ge t\), then \(b_0=a\), and the resulting bound
\[
(q-1)a^2+[1-(q-1)a]^2
\]
decreases for \(t\le a\le1/q\), taking value \((q+3)t^2\) exactly at \(a=t\).

If \(a<t\), put \(z=(q+1)a\), so \(0<z<1\) and \(b_0=t/z\). Feasibility of \(a+(q-1)b_0\le1\) forces \(z\ge z_0\), where
\[
z_0=\frac{q+1-\sqrt{q^2-2q+5}}2.
\]
An exact algebraic subtraction gives
\[
a^2+(q-2)b_0^2+[1-a-(q-2)b_0]^2-(q+3)t^2
=\frac{(z-1)B_q(z)}{z^2(q+1)^2},
\]
with
\[
B_q(z)=2z^3-2qz^2+(q^2+q-6)z-q^2+3q-2.
\]
For \(q\ge5\), one has \(B_q'(z)>0\) on \([0,1]\): indeed \(B_q''(z)=12z-4q<0\) and \(B_q'(1)=q(q-3)>0\). The relation \(z_0^2-(q+1)z_0+(q-1)=0\) yields
\[
B_q(z_0)=(q-1)((q+2)z_0-q)>0.
\]
To verify the last inequality, note that \(x=q/(q+2)<1\) satisfies \(x^2-(q+1)x+(q-1)=(q^2-2q-4)/(q+2)^2>0\); since the quadratic has its lower zero \(z_0\) in \((0,1)\), it follows that \(x<z_0\). Thus \(B_q(z)>0\) for \(z\in[z_0,1]\), and \(z-1<0\) makes the displayed deficit strictly negative. The probability lemma, including its equality condition, follows.

**4. No window can do better.** Under planarity, the smallest ambiguity magnitude among nonzero-horizontal shifts is exactly \(\sqrt{ab}\), because every unordered distinct pair of graph sites occurs as a translate overlap. If \(ab<t^2\), this is smaller than \(t\). Otherwise the probability lemma applies. At zero shift and \(\omega=(\alpha,0)\) with \(\alpha\ne0\), the ambiguity coefficient is the ordinary Fourier coefficient \(\widehat p(\alpha)=\sum_xp_x\psi(\alpha x)\). Parseval gives
\[
\sum_{\alpha\ne0}|\widehat p(\alpha)|^2=q\sum_xp_x^2-1\le(q-1)t^2.
\]
Thus at least one allowed ambiguity coefficient has magnitude at most \(t\). At \((h,\omega)=(0,0)\), \(|A_g|=\|g\|_2^2=1\), and no ambiguity magnitude can exceed one. Therefore the restriction-frame condition number is at least \(1/t^2=(q+1)^2\).

**5. All equality cases.** Achieving this bound forces \(ab\ge t^2\) and \(|\widehat p(\alpha)|\ge t\) for every \(\alpha\ne0\); equality in the Parseval average and the probability lemma forces the unique mass pattern \(p_{x_0}=2t\), \(p_x=t\) otherwise. Conversely, for this pattern every nonzero-horizontal shift has \(|A_g|\ge t\), while \(|A_g(0,(\alpha,0))|=t\) for \(\alpha\ne0\). For \(\beta\ne0\), planarity implies the bent character-sum identity
\[
\left|\sum_x\psi(\alpha x+\beta F(x))\right|^2=q,
\]
since expanding its square by the difference \(u\) yields cancellation for each \(u\ne0\). Consequently
\[
|A_g(0,(\alpha,\beta))|
=t\left|\sum_x\psi(\alpha x+\beta F(x))+
\psi(\alpha x_0+\beta F(x_0))\right|
\ge t(\sqrt q-1)>t
\]
for \(\beta\ne0\) and \(q\ge5\). Phases of \(g_x\) do not affect zero-shift ambiguity or the magnitude of a singleton translate overlap, so all site phases are free. This proves both sharpness and the complete optimizer classification.

## Verification
Run `python3 check_planar.py` and `python3 check_algebra.py` with Python 3 standard library. It independently enumerates all Weyl ambiguity coordinates for the graph \(F(x)=x^2\) over \(\mathbb F_3\), \(\mathbb F_5\), \(\mathbb F_7\), and \(\mathbb F_9\), including an explicit implementation of the extension field. It compares the complete uniform-window eigenvalue multiplicities and the claimed spike-window minimum, and demonstrates an inaccessible horizontal shift for the nonplanar cubic graph over \(\mathbb F_5\). A separate full projector-Gram calculation in dimension \(N=9\) agrees with the predicted nonzero eigenvalues. The symbolic factorization and lower-root sign argument in the proof were also checked by exact polynomial algebra. These checks corroborate, but cannot establish, the uniform-all-fields theorem.

## Relationship to prior work
Feichtinger, Kozek, and Luef develop the Weyl spreading representation for finite abelian groups. Bojarovska and Flinth's Theorem 2.3 gives the Gabor-projector frame bounds in terms of ambiguity coefficients for an informationally complete cyclic Gabor system. Goldberger, Kang, and Okoudjou compute the full projector-Gram eigenvalues and identify its rank by nonzero ambiguity coefficients. Pott, Schmidt, and Zhou's Proposition 4.4 characterizes planar-function graphs as relative difference sets and records the corresponding character-sum flatness. These existing results cover the spectral mechanism and support combinatorics used here; the present contribution is the **sharp constrained minimax value and all optimizers** for graph-supported windows on their forced maximal accessible operator space. The spectral enumeration of the uniform graph indicator is an elementary consequence of those established inputs and is not asserted as an independently novel contribution.

For comparison, the uniform graph indicator has projector-frame eigenvalue \(q^2\) once, \(q\) with multiplicity \(q(q-1)\), \(1\) with multiplicity \(q^3(q-1)\), and \(0\) with multiplicity \((q-1)(q^2+1)\). In contrast, the optimizer removes the extra \(q-1\) zeros and reaches the forced maximum rank \(q^4-q^3+q^2\).

## Limitations
The restriction-space result is about complex-linear operator tomography on \(\mathcal K\), not injectivity on the whole quantum state space and not nonlinear pure-state phase retrieval. The minimax and uniqueness theorem is proved for odd \(q\ge5\), not the exceptional small field \(q=3\) or even characteristic. Arbitrary nonlinear maps outside the planar class cannot reach the fixed accessible dimension. The generic projector spectral formula and the planar graph/difference-set equivalence are preexisting facts. Independent historical-priority certification is not claimed; an equivalent constrained frame optimization in unindexed literature cannot be excluded.

## References
1. H. G. Feichtinger, W. Kozek, F. Luef, *Gabor analysis over finite Abelian groups*, arXiv:math/0703228v1 (2007-03-08), https://arxiv.org/abs/math/0703228.
2. A. Pott, K.-U. Schmidt, Y. Zhou, *Semifields, relative difference sets, and bent functions*, arXiv:1401.3294v1 (2014-01-14), https://arxiv.org/abs/1401.3294; Proposition 4.4.
3. I. Bojarovska, A. Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800v1 (2015-03-19), https://arxiv.org/abs/1503.05800; Theorem 2.3.
4. A. Goldberger, S. Kang, K. A. Okoudjou, *Towards a classification of incomplete Gabor POVMs in \(\mathbb C^d\)*, arXiv:2106.01509v1 (2021-06-02), https://arxiv.org/abs/2106.01509; Theorem 1 and Gram spectrum.
