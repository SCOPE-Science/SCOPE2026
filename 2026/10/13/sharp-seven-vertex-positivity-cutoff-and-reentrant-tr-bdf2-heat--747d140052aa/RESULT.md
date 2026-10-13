# Sharp seven-vertex positivity cutoff and reentrant TR-BDF2 heat stepping on cycles

## Finding
Let \(n\ge3\) be an integer, and let \(L_n=2I-S-S^{-1}\) be the combinatorial Laplacian of the undirected cycle \(C_n\), where \(S\) is its cyclic shift. Apply the standard L-stable TR-BDF2 step, with parameter \(\gamma=2-\sqrt2\), to the semidiscrete heat equation \(u'=-L_nu\). Its one-step matrix is
\[
T_n(h)=(I-\alpha h L_n)(I+\beta hL_n)^{-2},\qquad
\alpha=\sqrt2-1,\quad \beta=1-1/\sqrt2,\quad h\ge0.
\]
For \(h>0\), define \(c(h)=1+1/((2-\sqrt2)h)>1\), and write \(U_m\) for the Chebyshev polynomial of the second kind, normalized by \(U_0(c)=1\), \(U_1(c)=2c\), and \(U_{m+1}(c)=2cU_m(c)-U_{m-1}(c)\). Set
\[
F_n(c)=c-\sqrt2+\frac{n(1+\sqrt2)}{U_{n-1}(c)}.
\]
**Exact positivity test:** for every \(n\ge3\) and \(h>0\),
\[
T_n(h)\text{ is entrywise nonnegative}\quad\Longleftrightarrow\quad F_n(c(h))\ge0.
\]
Whenever the diagonal is nonnegative, every off-diagonal entry is strictly positive. In particular, any failure of positivity includes a negative diagonal entry.

**Sharp size dichotomy:** for \(3\le n\le7\), \(T_n(h)\) is entrywise nonnegative for every \(h\ge0\), and strictly positive for every \(h>0\). For each \(n\ge8\), \(F_n\) has exactly two zeros \(1<c_{n,\mathrm L}<5/4<c_{n,\mathrm R}<\sqrt2\). With
\[
h_{n,-}=\frac1{(2-\sqrt2)(c_{n,\mathrm R}-1)},\qquad
h_{n,+}=\frac1{(2-\sqrt2)(c_{n,\mathrm L}-1)},
\]
we have \(0<h_{n,-}<h_{n,+}\) and the **complete reentrant positivity law**
\[
T_n(h)\ge0\text{ entrywise}\quad\Longleftrightarrow\quad
0\le h\le h_{n,-}\ \text{or}\ h\ge h_{n,+}.
\]
For example, \(h_{8,-}\approx4.631334936\) and \(h_{8,+}\approx10.406445652\). The failure intervals \((h_{n,-},h_{n,+})\) strictly expand with \(n\). Their endpoints satisfy
\[
\lim_{n\to\infty}h_{n,-}=2+\frac{3\sqrt2}{2},\qquad
\lim_{n\to\infty}\frac{h_{n,+}}{n^2}
=\frac{2}{(2-\sqrt2)\xi_*^2},
\]
where \(\xi_*>0\) is the unique solution of \(\xi_*/\sinh\xi_*=3-2\sqrt2\). Numerically the second constant is approximately \(0.2379000\).

## Assumptions and scope
The cycle has \(n\ge3\) vertices, nearest-neighbor transition rates exactly one in each direction, periodic boundaries, no reaction term, exact arithmetic, and an arbitrary positive timestep \(h\). The claim is about nonnegativity of the **final one-step matrix**, not the internal stages, numerical accuracy, or arbitrary variable-coefficient generators. The matrix fixes constants and has row sums one for all \(h\), but it need not be a stochastic matrix in the intermediate failure window.

## Proof
**1. Rational step and cycle resolvent.** The standard TR-BDF2 stability function at \(\gamma=2-\sqrt2\) is \(R(z)=(1+\alpha z)/(1-\beta z)^2\) [1, Section 3]. Put \(a=\beta h\) and \(G=(I+aL_n)^{-1}\). As \(aL_n=G^{-1}-I\),
\[
T_n(h)=(1+\sqrt2)G^2-\sqrt2G.
\]
There is a unique \(q\in(0,1)\) satisfying \(a=q/(1-q)^2\). Writing \(C=(1-q)/(1+q)\), the periodic resolvent entries at cyclic distance \(k\in\{0,\ldots,n-1\}\) are
\[
G_k=C\frac{q^k+q^{n-k}}{1-q^n}>0.
\]
This follows by periodizing the geometric Green kernel \(Cq^{|j|}\) on the infinite nearest-neighbor lattice, or by substitution in the cyclic resolvent equation.

**2. The diagonal is the first entry to lose positivity.** Differentiating \(G=(I+aL_n)^{-1}\) yields \(G^2=G+a\partial_aG\). Since \(a\partial_a=q(1-q)(1+q)^{-1}\partial_q\), write \(B_k=(G^2)_k/G_k\). Direct differentiation gives
\[
B_k=1-\frac{2q}{(1+q)^2}+
\frac{1-q}{1+q}\left(
W_k+\frac{nq^n}{1-q^n}\right),\quad
W_k=\frac{kq^k+(n-k)q^{n-k}}{q^k+q^{n-k}}.
\]
Let \(t=-\log q>0\) and \(m=|n-2k|\). Then \(W_k=n/2-(m/2)\tanh(mt/2)\). The function \(m\mapsto m\tanh(mt/2)\) is strictly increasing for \(m>0\), so \(W_k>W_0\) for every \(k\ne0\) modulo \(n\). Consequently \(B_k>B_0\) off the diagonal. Because \(T_k=G_k[(1+\sqrt2)B_k-\sqrt2]\) and \(G_k>0\), \(T_n(h)\) is entrywise nonnegative exactly when its diagonal is nonnegative; a nonnegative diagonal implies strictly positive off-diagonal entries.

**3. Exact scalar reduction.** At \(k=0\), the preceding expression simplifies to
\[
B_0=\frac{1+q^2}{(1+q)^2}
+\frac{2n(1-q)q^n}{(1+q)(1-q^{2n})}.
\]
Multiplying \((1+\sqrt2)B_0-\sqrt2\) by the positive factor \((1+q)^2/(2q)\) gives
\[
\frac{q+q^{-1}}2-\sqrt2
+(1+\sqrt2)\frac{n\sinh t}{\sinh(nt)}.
\]
Since \(c=(q+q^{-1})/2=1+1/(2a)=c(h)\) and \(U_{n-1}(c)=\sinh(nt)/\sinh t\), this is exactly \(F_n(c(h))\). The matrix at \(h=0\) is \(I\).

**4. Sharp seven-vertex cutoff.** For fixed \(c=\cosh t>1\), the quantity \(n/U_{n-1}(c)=n\sinh t/\sinh(nt)\) strictly decreases as the positive integer \(n\) increases, because \(\sinh(nt)/n\) strictly increases. Thus \(F_n(c)\) strictly decreases in \(n\). For \(c\ge\sqrt2\), every \(F_n(c)>0\).

It remains to prove \(F_7(c)>0\) on \(1\le c\le\sqrt2\). Use \(U_6(c)=64c^6-80c^4+24c^2-1\ge7\) for \(c\ge1\) (the last inequality follows from its expansion in powers of \(c-1\), all of whose nonconstant coefficients are positive). Put \(s_0=283/200>\sqrt2\) and
\[
Q(c)=(c-s_0)U_6(c)+7(1+s_0).
\]
As \(U_6(c)\ge7\), \((c-\sqrt2)U_6(c)+7(1+\sqrt2)\ge Q(c)\). On the rational intervals \([1,6/5]\), \([6/5,13/10]\), and \([13/10,283/200]\), all eight degree-seven Bernstein coefficients of the affine restriction of \(Q\) are strictly greater than two. Their exact minima are respectively \(1667336/390625\), \(165684017/65625000\), and \(4853759/1562500\); the accompanying dependency-free checker reconstructs all 24 coefficients with rational arithmetic. Because Bernstein basis functions are nonnegative and sum to one, \(Q(c)>2\) throughout these intervals. Hence \(F_7(c)>0\) and therefore \(F_n(c)>0\) for every \(3\le n\le7\).

For \(n=8\), evaluate at \(c=5/4=\cosh(\log2)\). The exact value \(U_7(5/4)=21845/128\) gives
\[
F_8(5/4)=\frac54-\sqrt2+(1+\sqrt2)\frac{1024}{21845}
< -\frac{16383}{436900}<0,
\]
where the strict upper bound uses \(\sqrt2>7/5\). By strict decrease in \(n\), every \(n\ge8\) has \(F_n(5/4)<0\).

**5. Exactly one failure interval.** For \(c>1\), \(U_{n-1}(c)=2^{n-1}\prod_{j=1}^{n-1}(c-\cos(j\pi/n))\). Every factor reciprocal is positive and completely monotone for \(c>1\); their product \(1/U_{n-1}(c)\) has strictly positive second derivative. Hence \(F_n\) is strictly convex. Moreover \(F_n(1)=2\), \(F_n(\sqrt2)>0\), and \(F_n(c)>0\) for \(c\ge\sqrt2\). For \(n\ge8\), strict convexity and the negative value at \(5/4\) give exactly two roots in \((1,\sqrt2)\), and negativity precisely between them. Since \(c(h)\) decreases continuously from infinity to one, the displayed reentrant timestep intervals follow. Strict decrease of \(F_n\) with \(n\) makes their failure windows strictly nested.

**6. Endpoint limits.** At any fixed \(c>1\), \(n/U_{n-1}(c)\to0\) as \(n\to\infty\), so the larger root tends to \(\sqrt2\) and the first timestep endpoint tends to \(1/((2-\sqrt2)(\sqrt2-1))=2+3\sqrt2/2\). For the smaller root, set \(c=\cosh(\xi/n)\): then \(F_n(c)\to 1-\sqrt2+(1+\sqrt2)\xi/\sinh\xi\), uniformly on bounded positive \(\xi\)-intervals. The quotient \(\xi/\sinh\xi\) strictly decreases from one to zero, so its unique positive crossing occurs at \(\xi_*\) as stated. Root bracketing therefore gives \(n\operatorname{arcosh}(c_{n,\mathrm L})\to\xi_*\). Using \(\cosh(\xi/n)-1\sim\xi^2/(2n^2)\) yields the quadratic limit for \(h_{n,+}\).

## Verification
The standalone `verify.py` uses only the Python standard library. It reconstructs the exact rational polynomial \(Q\), verifies all 24 Bernstein coefficients and their minima, checks the negative eight-vertex rational upper bound, and compares the scalar positivity test with 234 independent Fourier reconstructions of the cycle-step matrices. It brackets both transition values for four representative cycle sizes, including \(n=8\), and verifies mass preservation numerically. These finite tests are supplementary; the universal assertions follow from Steps 1–6.

## Relationship to prior work
Bonaventura and Della Rocca [1] derive the L-stable TR-BDF2 stability function, its absolute monotonicity radius (approximately \(2.414\)), and conditional positivity sufficient conditions for general nonlinear problems. Their paper also contains numerical periodic advection–diffusion–reaction experiments; the analyzed method and published sufficient bounds do not give the exact cycle-by-cycle end-step positivity classification above. In particular, general SSP sufficiency does not imply unconditional positivity on seven-vertex cycles or positivity recovery after an intermediate negative window.

The publicly available lattice note [2] proves unconditional positivity for the *different* backward-Euler-filtered Crank–Nicolson map \(2G^2-G\) on one-dimensional lattices. Here the TR-BDF2 map is \((1+\sqrt2)G^2-\sqrt2G\); the coefficient of the signed correction is larger. That prior positivity theorem does not imply this one, and the seven-versus-eight cutoff shows the two maps behave differently.

The classical fourth-order diagonal Padé/Gauss scheme has a different rational stability function and stiff limit, so its cycle positivity behavior does not dominate this L-stable TR-BDF2 result. An equivalent historical result in work not fully retrievable or not indexed under these formulations cannot be excluded.

## Limitations
This is an exact final-step result for symmetric unit-rate nearest-neighbor cycles and the standard \(\gamma=2-\sqrt2\) TR-BDF2 parameter only. It does not assert positivity of intermediate stages, preservation for arbitrary Markov generators, asymmetric rates, other boundaries, or floating-point implementations. Large-step positivity recovery does **not** imply acceptable time-integration accuracy or monotonicity for arbitrary nonlinear models. Historical priority is assessed from accessible sources, not certified independently.

## References
1. L. Bonaventura and A. Della Rocca, *Monotonicity, positivity and strong stability of the TR-BDF2 method and of its SSP extensions*, arXiv:1510.04303v1, publicly posted October 14, 2015. https://arxiv.org/abs/1510.04303
2. *Unconditional lattice positivity from backward-Euler-filtered Crank–Nicolson*, publicly available mathematical note (2026). https://github.com/published-finding corpus/2026/blob/main/2026/9/20/SCOPE-backward-euler-filtered-cn-lattice-positivity--1f6f56bd0eac/RESULT.md
