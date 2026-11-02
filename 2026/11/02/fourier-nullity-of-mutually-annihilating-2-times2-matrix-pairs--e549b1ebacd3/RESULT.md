# Fourier nullity of mutually annihilating \(2\times2\) matrix pairs

## Finding
For every finite field \(F=\mathbb F_q\), the additive Fourier transform of the set
\[
\mathcal Z_q=\{(X,Y)\in M_2(F)^2:XY=YX=0\}
\]
is integer-valued and has an exact frequency-by-frequency zero criterion. For \(A,B\in M_2(F)\), set
\[
N_r(A,B)=\#\{t\in F^\times:\operatorname{rank}(A+t\operatorname{adj}B)=r\},\qquad r\in\{0,1\}.
\]
With any nontrivial additive character \(\psi\) of \(F\) and unnormalized Fourier transform,
\[
\widehat{\mathbf1}_{\mathcal Z_q}(A,B)=q^2\left[q^2\mathbf1_{A=0}+q^2\mathbf1_{B=0}-1+N_1(A,B)+(q+1)N_0(A,B)\right]. \tag{1}
\]
Thus a Fourier coefficient vanishes **precisely** when \(A\ne0\), \(B\ne0\), \(N_0=0\), and \(N_1=1\). On the additive group of order \(q^8\), convolution by \(\mathbf1_{\mathcal Z_q}\) has
\[
\boxed{\dim\ker T_q=q(q-1)^3(q+1)^2(3q-1)+36\mathbf1_{\{q=2\}},}\tag{2}
\]
\[
\boxed{\operatorname{rank}T_q=q^8-q(q-1)^3(q+1)^2(3q-1)-36\mathbf1_{\{q=2\}}.}\tag{3}
\]
In particular, the exact nullities at field orders \(2,3,4,5\) are \(126,3072,29700,161280\). The proportion of null Fourier frequencies is \(3/q+O(q^{-2})\) as \(q\to\infty\) over prime powers.

## Assumptions and scope
The field order \(q\) is any prime power at least two, including all characteristics and nonprime fields. Matrices are \(2\times2\), \(\operatorname{adj}\begin{psmallmatrix}a&b\\c&d\end{psmallmatrix}=\begin{psmallmatrix}d&-b\\-c&a\end{psmallmatrix}\), and the frequency pairing is \(\operatorname{tr}(AX+BY)\). For \(f,g:G\to\mathbb C\), unnormalized convolution is \((f*g)(z)=\sum_{w\in G}f(w)g(z-w)\), where \(G=M_2(F)^2\) is considered **additively**. The results do not assume or assert analogous formulas for higher-dimensional matrix pairs.

## Proof
**1. Decomposing the annihilation relation.** For invertible \(X\), the only admissible \(Y\) is zero; for \(X=0\), every \(Y\) is admissible. For nonzero rank-one \(X\), the two conditions are \(\operatorname{im}Y\subseteq\ker X\) and \(\operatorname{im}X\subseteq\ker Y\). Both lines are one-dimensional, so the space of admissible \(Y\) is exactly \(F\,\operatorname{adj}X\). Indeed the nonzero adjugate has image \(\ker X\) and kernel \(\operatorname{im}X\). Consequently, as disjoint portions,
\[
\mathcal Z_q=\{(X,0):X\in M_2(F)\}\cup\{(0,Y):Y\in M_2(F)\}\cup\{(X,t\operatorname{adj}X):\operatorname{rank}X=1,\ t\in F^\times\},
\]
where the two coordinate subspaces overlap only at \((0,0)\). Since there are \((q-1)(q+1)^2\) rank-one matrices, \(\lvert\mathcal Z_q\rvert=2q^4-1+(q-1)^2(q+1)^2=3q^4-2q^2\).

**2. Exact rank-one transform.** Let \(S(C)=\sum_{\operatorname{rank}X=1}\psi(\operatorname{tr}(CX))\). The map \((u,v)\mapsto uv^{\mathsf T}\) from \(F^2\times F^2\) represents each nonzero rank-one matrix exactly \(q-1\) times and represents zero exactly \(2q^2-1\) times. If \(r=\operatorname{rank}C\), character orthogonality gives
\[
\sum_{u,v\in F^2}\psi(v^{\mathsf T}Cu)=q^2\lvert\ker C\rvert=q^{4-r},\qquad
S(C)=\frac{q^{4-r}-2q^2+1}{q-1}
=\begin{cases}(q-1)(q+1)^2&r=0,\\q^2-q-1&r=1,\\-(q+1)&r=2.\end{cases}
\]
This calculation uses only additive-character orthogonality and applies in characteristic two and to extension fields. Since \(\operatorname{tr}(B\operatorname{adj}X)=\operatorname{tr}((\operatorname{adj}B)X)\), Step 1 gives
\[
\widehat{\mathbf1}_{\mathcal Z_q}(A,B)=q^4\mathbf1_{A=0}+q^4\mathbf1_{B=0}-1+\sum_{t\in F^\times}S(A+t\operatorname{adj}B).
\]
Substituting the three values of \(S\) yields (1). If one frequency matrix vanishes, the bracket in (1) is strictly positive because it is at least \(q^2-1\). If both are nonzero but \(N_0>0\), the bracket is at least \(q\). Otherwise the bracket equals \(N_1-1\); therefore the stated zero criterion is necessary and sufficient.

**3. Intersections with the rank-one quadric.** The linear adjugate map \(B\mapsto\operatorname{adj}B\) is a bijection, so count frequency pairs as \((A,C)\) with \(C=\operatorname{adj}B\). If \(A,C\ne0\) are proportional, exactly one \(t\in F^\times\) makes \(A+tC=0\), so \(N_0>0\) and there is no Fourier zero. For independent \(A,C\), their projectivizations give ordered distinct endpoints on the projective line \(\mathbb P(\operatorname{span}(A,C))\) in \(\mathbb P(M_2(F))\cong\mathbb P^3(F)\). Its \(q-1\) interior projective points are represented exactly by \(A+tC\), \(t\in F^\times\). Rank-one matrices constitute the nonsingular hyperbolic quadric \(Q:\det=0\), with \((q+1)^2\) points. The zero condition becomes: exactly one interior point of this projective line belongs to \(Q\).

**4. Counting lines and ordered endpoints.** The Segre description \(Q\cong\mathbb P^1(F)\times\mathbb P^1(F)\) shows that \(Q\) has exactly \(2(q+1)\) generator lines, one per fiber of each ruling. Every \(P\in Q\) lies on two generators, each with \(q\) other points, leaving \(q^2\) points of \(Q\) not sharing a generator with \(P\). Thus the number of secants with exactly two quadric points is
\[
L_s=\frac{(q+1)^2q^2}{2}.
\]
The tangent plane to \(Q\) at \(P\) contains \(q+1\) lines through \(P\), two being the generators; the other \(q-1\) meet \(Q\) only at \(P\). Hence the number of nongenerator tangent lines is
\[
L_t=(q+1)^2(q-1).
\]
On each secant, the ordered distinct endpoints have exactly one interior quadric point in \(4(q-1)\) ways: select which of the two quadric points is an endpoint, select the other endpoint among the \(q-1\) off-quadric points, and choose the endpoint order. On each nongenerator tangent, this occurs in \(q(q-1)\) ways, by selecting both endpoints off \(Q\). A generator line has every one of its \(q+1\) points in \(Q\), so its interior contains exactly one quadric point **only** if \(q=2\), when each of the six generators supplies six ordered endpoint choices. All other lines have no interior quadric point or two such points and cannot contribute.

Each ordered pair of distinct projective endpoints has \((q-1)^2\) nonzero matrix lifts. Therefore the exact number of Fourier zeros is
\[
(q-1)^2\left[4(q-1)\frac{(q+1)^2q^2}{2}+q(q-1)(q+1)^2(q-1)+36\mathbf1_{\{q=2\}}\right]
=q(q-1)^3(q+1)^2(3q-1)+36\mathbf1_{\{q=2\}},
\]
proving (2). Fourier characters diagonalize every additive convolution operator, giving rank (3). The asymptotic estimate follows by expanding the polynomial.

## Verification
The accompanying standalone script `mutual_annihilation_check.py` tests the exact frequency formula against direct character sums at **all** frequencies for \(q=2,3\); it additionally compares 213 deterministic raw Fourier sums over \(\mathbb F_4\), and independently enumerates all frequency pairs to verify the nullity polynomial at \(q=2,3,4,5\). The finite-field arithmetic for \(\mathbb F_4\) uses \(\mathbb F_2[z]/(z^2+z+1)\) with its canonical additive trace. Run `python3 mutual_annihilation_check.py`; successful output ends with `ALL_EXACT_MUTUAL_ANNIHILATION_CHECKS_OK`. These finite checks do **not** replace the argument for arbitrary \(q\).

## Relationship to prior work
Bondarenko–Gerasimova–Sergeichuk classify mutually annihilating operator pairs up to simultaneous similarity, over arbitrary fields, but their results do not give the additive Fourier transform of the entire solution set or its convolution-nullity polynomial. Huang counts these pairs in every dimension and derives a Cohen–Lenstra series, but a point count is just the zero-frequency Fourier coefficient and does not determine the remaining Fourier-zero pattern. Britnell–Wildon provide a related classification of commuting matrix types, again without the frequency-sensitive convolution invariant. The familiar rank-one matrix character sum used in Step 2 is not itself asserted to be new. The new statement is the assembled full Fourier-null classification, its projective secant/tangent mechanism, and the exact binary-field correction.

## Limitations
The theorem is specific to \(2\times2\) mutually annihilating pairs over finite fields. It does not determine convolution ranks for larger matrices, local rings, or variants imposing nilpotence. It does not claim that the underlying orbit classifications or the rank-one character-sum calculation are new. A published equivalent result in matrix association schemes or character-sum literature could remain undetected. Scientific review of this result has not been independently replicated.

## References
1. V. M. Bondarenko, T. G. Gerasimova, and V. V. Sergeichuk, *Pairs of mutually annihilating operators*, arXiv:0812.2155 (first publicly posted 2008-12-11), https://arxiv.org/abs/0812.2155 .
2. Y. Huang, *Mutually annihilating matrices, and a Cohen–Lenstra series for the nodal singularity*, arXiv:2110.15566 (first publicly posted 2021-10-29), https://arxiv.org/abs/2110.15566 .
3. J. R. Britnell and M. Wildon, *On types and classes of commuting matrices over finite fields*, arXiv:1001.0811 (first publicly posted 2010-01-06), https://arxiv.org/abs/1001.0811 .
