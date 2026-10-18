# Complete Gabor-projector spectra of parabola indicators over odd prime-power rings

## Finding

Fix an odd prime \(p\) and an integer \(k\ge2\). Put \(N=p^k\), \(R=\mathbb Z/N\mathbb Z\), \(G=R^2\) and \(D=|G|=p^{2k}\). Let \(g=N^{-1/2}\mathbf1_C\in\ell^2(G)\), where \(C=\{(t,t^2):t\in R\}\). For every translation \(u\in G\) and character frequency \(v\in G\), write \(W_{u,v}=M_vT_u\), \(P_{u,v}=|W_{u,v}g\rangle\langle W_{u,v}g|\), and form the full \(D^2\)-by-\(D^2\) real Gram matrix
\[
K_{(u,v),(u',v')}=\operatorname{tr}(P_{u,v}P_{u',v'})=|\langle W_{u,v}g,W_{u',v'}g\rangle|^2.
\]

**Exact spectrum.** For every \(0\le j<k\) and \(1\le s\le k\), define the positive integers
\[
L_j=\begin{cases}
(p-1)p^{4k-3j-1},&2j\le k,\\
(p-1)p^{5k-5j-1},&2j>k,
\end{cases}
\qquad
Q_s=(p-1)p^{2s+\lceil s/2\rceil-2}.
\]
The eigenvalue \(p^{2k}\) has multiplicity exactly one. For every integer \(0\le e<2k\), the eigenvalue \(p^e\) occurs with multiplicity
\[
\boxed{m_e=\sum_{\substack{0\le j<k\\2j=e}}L_j+
\sum_{\substack{1\le s\le k\\2k-s=e}}Q_s.}
\]
All other eigenvalues are zero, with multiplicity
\[
\boxed{m_{\mathrm{zero}}=p^{4k}-1-\sum_{j=0}^{k-1}L_j-\sum_{s=1}^kQ_s.}
\]
Thus the exact complex rank of the corresponding complete Gabor intensity-lifting operator on \(\operatorname{End}(\ell^2(G))\) is
\[
\boxed{\mathcal R(p,k)=1+\sum_{j=0}^{k-1}L_j+\sum_{s=1}^kQ_s.}
\]
The distinct positive eigenvalue exponents are **exactly**
\[
\boxed{\{0,2,4,\ldots,2\lfloor(k-1)/2\rfloor\}\ \cup\ \{k,k+1,\ldots,2k\}.}
\]
In particular, the smallest positive Gram eigenvalue is \(1\), its largest is \(p^{2k}\), and the nonzero-eigenspace condition number is \(p^{2k}\). With the natural Hilbert--Schmidt lifting analysis operator (whose squared singular values are these Gram eigenvalues), the corresponding positive-singular-value condition number is \(p^k\).

For each fixed odd prime \(p\), as the ring depth \(k\) grows,
\[
\boxed{\lim_{k\to\infty}\frac{\mathcal R(p,k)}{p^{4k}}=
\frac{p^2}{p^2+p+1}.}
\]
This is a nonzero, strictly subunit identifiable fraction for complete **linear** matrix tomography, not a claim about nonlinear pure-state phase retrieval.

## Assumptions and scope

All moduli are odd prime powers with \(k\ge2\). Translation is \((T_u f)(x)=f(x-u)\), and modulation is \((M_v f)(x)=\exp(2\pi i\,v\cdot x/N)f(x)\) using the standard pairing on \(R^2\). Norm and inner product are the counting-measure \(\ell^2(G)\) conventions, so \(\|g\|_2=1\). Every pair \((u,v)\in G\times G\) is sampled once, including both zero coordinates. Eigenvalues refer to the raw Gram matrix of unscaled unit-trace projectors; multiplying measurements by another normalization factor changes eigenvalues accordingly. Rank is over the complex Hilbert--Schmidt operator space; the corresponding real rank on Hermitian matrices is the same, but an operator-rank deficiency alone does not classify nonlinear phase-retrieval ambiguities. Valuations \(\nu_p\) on nonzero residues range from \(0\) to \(k-1\), and \(\nu_p(0)=k\).

## Proof

**1. Weyl-coordinate diagonalization.** The \(D^2\) Weyl operators \(W_{a,b}\), with \((a,b)\in G\times G\), form an orthogonal basis of \(\operatorname{End}(\ell^2(G))\) with Hilbert--Schmidt squared norm \(D\). The projector frame superoperator is
\[
\mathcal S(X)=\sum_{u,v\in G}\operatorname{tr}(P_{u,v}X)P_{u,v}.
\]
Conjugation of a Weyl basis element by \(W_{u,v}\) multiplies it by a phase-space character. Character orthogonality then diagonalizes \(\mathcal S\) in that basis. Explicitly, for every \((a,b)\),
\[
\mathcal S(W_{a,b})=D|\langle g,W_{a,b}g\rangle|^2W_{a,b}.
\]
The nonzero spectra of the Gram matrix \(K\) and this frame superoperator coincide, with multiplicities (they are the analysis/adjoint-analysis products). Both act on spaces of dimension \(D^2\), so their zero multiplicities also coincide. Therefore it suffices to enumerate \(D|\langle g,W_{a,b}g\rangle|^2\).

**2. Translated parabola intersections.** Write spatial shift \(a=(A,B)\) and modulation \(b=(C,E)\). A point \((t,t^2)\) of the parabola also lies on its translate by \(a\) if and only if
\[
2At\equiv B+A^2\pmod{N}.
\]
Its unnormalized ambiguity sum is
\[
S(A,B,C,E)=\sum_{\substack{t\bmod N\\2At=B+A^2\bmod N}}
\exp\!\left(\frac{2\pi i}{N}(Ct+Et^2)\right),
\]
and \(D|\langle g,W_{a,b}g\rangle|^2=|S(A,B,C,E)|^2\), since \(g\) has amplitude \(N^{-1/2}\) on its support and \(D=N^2\).

If \(A=0\) and \(B\ne0\), the intersection is empty and the eigenvalue is zero. If \(A=B=0\), then \(S\) is the full quadratic Gauss sum modulo \(N\). The unique \((C,E)=(0,0)\) gives \(|S|^2=N^2=p^{2k}\). For \(\ell=\nu_p(E)<k\), the sum is nonzero precisely when \(\nu_p(C)\ge\ell\), in which case
\[
|S|^2=p^{k+\ell}.
\]
There are \((p-1)p^{2k-2\ell-1}\) such frequency pairs \((C,E)\). For \(E=0\) and \(C\ne0\), the sum is zero.

**3. Exact quadratic Gauss-sum criterion.** For an odd prime and \(j\ge1\), let
\[
G_j(\gamma,\beta)=\sum_{s\bmod p^j}\exp\!\left(\frac{2\pi i}{p^j}(\gamma s+\beta s^2)\right).
\]
If \(\beta=0\pmod{p^j}\), this equals \(p^j\) if \(\gamma=0\pmod{p^j}\), and zero otherwise. When \(\alpha=\nu_p(\beta)<j\), translation by \(p^{j-\alpha}\) shows that \(G_j=0\) unless \(\gamma\) is divisible by \(p^\alpha\). If both coefficients are divisible by \(p^\alpha\), factoring through reduction modulo \(p^{j-\alpha}\) yields \(p^\alpha\) times a quadratic Gauss sum with unit quadratic coefficient. Completing the square works because \(2\) is invertible. The bijection \((u,v)=(s-t,s+t)\) proves that a primitive unit-coefficient quadratic Gauss sum has squared magnitude \(p^{j-\alpha}\); thus in the nonzero case
\[
\boxed{|G_j(\gamma,\beta)|^2=p^{j+\alpha}.}
\]
These are exact identities, without numerical approximations or unresolved Gauss-sum phases.

**4. Shifts with nonzero first coordinate.** Take \(A\ne0\) and \(j=\nu_p(A)<k\). There are
\[
\mathcal A_j=(p-1)p^{k-j-1}
\]
such first coordinates. The intersection condition in Step 2 is solvable if and only if \(B+A^2\equiv0\pmod{p^j}\). For each \(A\) this gives exactly \(p^{k-j}\) choices of \(B\), and for each such spatial shift there are \(p^j\) intersection points
\[
t=t_0+p^{k-j}s,\qquad s\bmod p^j.
\]
Expanding the phase, and discarding an irrelevant unimodular factor, shows
\[
\boxed{|S(A,B,C,E)|=|G_j(C+2Et_0,\ p^{k-j}E)|.}
\]
For \(j=0\), interpret the right-hand side as the single term of magnitude one.

If \(2j\le k\), the quadratic coefficient vanishes modulo \(p^j\) for every \(E\). Exactly \(p^{k-j}\) values of \(C\) satisfy \(C+2Et_0\equiv0\pmod{p^j}\), for each of the \(p^k\) values of \(E\). Therefore \(|S|^2=p^{2j}\) occurs
\[
\mathcal A_j\,p^{k-j}\,p^k\,p^{k-j}
=(p-1)p^{4k-3j-1}=L_j
\]
times.

If \(2j>k\), set \(h=2j-k>0\). Frequencies \(E\) divisible by \(p^h\) again have zero quadratic coefficient modulo \(p^j\). Counting \(p^{k-h}\) such values of \(E\) and \(p^{k-j}\) admissible values of \(C\), the eigenvalue \(p^{2j}\) occurs
\[
\mathcal A_j\,p^{k-j}\,p^{k-h}\,p^{k-j}
=(p-1)p^{5k-5j-1}=L_j
\]
times.

For the remaining frequencies, write \(\ell=\nu_p(E)<h\). Then the quadratic coefficient of the reduced Gauss sum has valuation \(\alpha=k-j+\ell<j\). By Step 3 it is nonzero exactly for
\[
C+2Et_0\equiv0\pmod{p^\alpha},
\qquad\text{and then}\qquad |S|^2=p^{j+\alpha}=p^{k+\ell}.
\]
At each such spatial shift, the number of frequencies of valuation \(\ell\) satisfying that congruence is
\[
(p-1)p^{k-\ell-1}\,p^{j-\ell}
=(p-1)p^{k+j-2\ell-1}.
\]
Multiplying by the \(p^{k-j}\) valid choices of \(B\), each eligible \(A\) therefore contributes \((p-1)p^{2k-2\ell-1}\) occurrences. The inequality \(\ell<2j-k\) is equivalent to \(j>\frac{k+\ell}{2}\).

**5. Complete multiplicity count.** Fix \(0\le\ell<k\). In Step 2 the zero spatial shift contributes \((p-1)p^{2k-2\ell-1}\) copies of \(p^{k+\ell}\). Step 4 contributes the same factor multiplied by the total number of nonzero \(A\)'s satisfying \(\nu_p(A)>\frac{k+\ell}{2}\). Writing \(j_0=\lfloor(k+\ell)/2\rfloor+1\), this gives
\[
1+\sum_{j=j_0}^{k-1}(p-1)p^{k-j-1}=p^{k-j_0}=p^{\lceil(k-\ell)/2\rceil-1}.
\]
Thus the total multiplicity of this *stratum's* eigenvalue \(p^{k+\ell}\) is
\[
(p-1)p^{2k-2\ell-1}\,p^{\lceil(k-\ell)/2\rceil-1}
=Q_{k-\ell}.
\]
The other nonzero strata are exactly the \(L_j\) already counted. If an eigenvalue receives both contributions, the multiplicities add; this is why the theorem sums both families rather than claiming all levels distinct. The only remaining Weyl directions have zero ambiguity and hence zero Gram eigenvalue. Since there are exactly \(p^{4k}\) Weyl directions, subtraction gives the stated zero multiplicity and rank. Every positive-power stratum in the theorem is nonempty, yielding the exact exponent list and the two condition numbers.

**6. Limiting rank density.** Divide the expression for \(\mathcal R(p,k)\) by \(p^{4k}\). For each fixed \(j\), eventually \(2j\le k\), and the corresponding term is \((p-1)p^{-3j-1}\). The remaining large-\(j\) tail and the \(Q_s\) terms are negligible uniformly as \(k\to\infty\), since their maximal exponents are at most \(5k/2+O(1)\), strictly below \(4k\). Hence the limit is the absolutely convergent geometric sum
\[
\sum_{j=0}^{\infty}(p-1)p^{-3j-1}
=\frac{(p-1)p^2}{p^3-1}
=\frac{p^2}{p^2+p+1}.
\]
This proves every asserted statement.

## Verification

Run `python3 checks/verify.py` from the directory containing this document (Python 3 and NumPy). The standalone program constructs the normalized parabola indicator directly, evaluates all spatially shifted autocorrelations through two-dimensional discrete Fourier transforms, and independently diagonalizes their full four-dimensional projector Gram convolution using a four-dimensional FFT. It compares **every spectral multiplicity**, including zero, against the closed formulas for \((p,k)=(3,1),(5,1),(3,2),(5,2),(3,3)\). The test covers 531441 eigenvalues in its largest case.

For \((3,2)\) and \((5,2)\), the program also directly enumerates every translated intersection and independently checks that all their squared quadratic Fourier magnitudes are either zero or integral powers of \(p\), covering respectively \(6561\) and \(390625\) Weyl coefficients. Exact-integer multiplicity and trace identities are additionally checked for three odd primes and depths up to seven. Executed output is preserved as `checks/output.txt`. Numerical Fourier tolerances are used only to corroborate the general algebraic proof; no infinite assertion is inferred from finite experiments.

## Relationship to prior work

Alaifari and Wellershoff [1] prove discrete Gabor phase-retrieval reconstruction and stability statements and exhibit the general ambiguity-function mechanism. Führ and Oussa [2] examine phase retrieval for nilpotent groups and their representations. Neither result classifies the full projector Gram eigenvalue multiset for this fixed parabola indicator over \(\mathbb Z/p^k\mathbb Z\). Iosevich and collaborators [3] study Gabor orthonormal bases over prime fields with different translation/modulation arrangements. Bojarovska and Flinth [4] develop general discrete Gabor injectivity criteria; their criteria are methodological, not this valuation-refined spectrum.

A publicly available *Complete exponential spectra of the parabola over odd prime-power rings* [5] explicitly classifies orthonormal additive-character bases restricted to exactly the same parabola, relying on the vanishing criterion for complete quadratic exponential sums. That is a different operator: a restricted frequency-character matrix, not the projector Gram of the **full time-frequency orbit of its normalized indicator**. In particular its statements do not imply this spectrum or its multiplicities. A publicly available *Exact Gabor tomography rank for hyperbolic quadratic shells over odd finite fields* [6] does analyze Weyl-projector ranks, but its support is a level-one quadric over fields rather than a parabola over nonreduced prime-power rings; its result does not supply these valuation-dependent multiplicities. The contribution here is the full explicit arithmetic multiplicity law and limiting tomography rank fraction, not classical Gauss-sum evaluation or the general Weyl diagonalization by themselves.

## Limitations

The theorem requires an odd prime and a cyclic ring of prime-power modulus with depth at least two; it does not cover modulus powers of two, arbitrary finite chain rings, perturbed graph windows, weighted supports, or higher polynomial curves. The Gram spectrum of linear Hilbert--Schmidt tomography does not by itself settle pure-state phase retrieval. The conditioning figures refer to the nonzero spectral subspace and the stated raw normalization. Small-modulus Fourier computations only corroborate the exact proof. A historical equivalent result in older finite-Heisenberg, Gauss-sum, or association-scheme literature remains a priority risk; lack of a matching indexed source does not prove novelty.

## References

1. Rima Alaifari and Matthias Wellershoff, *Stability Estimates for Phase Retrieval from Discrete Gabor Measurements*, arXiv:1901.05296v1, first posted 2019-01-12, https://arxiv.org/abs/1901.05296 ; full open-access version: https://link.springer.com/article/10.1007/s00041-020-09802-1.
2. Hartmut Führ and Vignon Oussa, *Phase Retrieval for Nilpotent Groups*, arXiv:2201.08654v1, first posted 2022-01-21, https://arxiv.org/abs/2201.08654 ; open-access article: https://link.springer.com/article/10.1007/s00041-023-10031-5.
3. Alex Iosevich, Mihalis Kolountzakis, Yurii Lyubarskii, Azita Mayeli, Jonathan Pakianathan, *On Gabor Orthonormal Bases over Finite Prime Fields*, arXiv:1712.09120v1, first posted 2017-12-25, https://arxiv.org/abs/1712.09120.
4. Irena Bojarovska and Axel Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800v1, first posted 2015-03-19, https://arxiv.org/abs/1503.05800.
5. *Complete exponential spectra of the parabola over odd prime-power rings*, publicly indexed scientific report, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-complete-exponential-spectra-of-the-parabola-over-odd-prime-powe--2cf08dd7e325.
6. *Exact Gabor tomography rank for hyperbolic quadratic shells over odd finite fields*, publicly indexed scientific report, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-gabor-tomography-rank-for-hyperbolic-quadratic-shells-over--b9e240edb677.
