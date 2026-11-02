# Arithmetic universality and pure-point spectral laws for monomial cross-composition sections

## Finding
Let \(H^2_0=zH^2(\mathbb D)\), with orthonormal basis \(e_n(z)=z^n\), \(n\ge1\). For **distinct integers** \(p,q\ge2\), let \(C_{z^p}f=f(z^p)\), let \(P_N\) project onto \(\operatorname{span}\{e_1,\ldots,e_N\}\), and set
\[
T_N^{p,q}=P_N C_{z^p}C_{z^q}^{*}P_N\big|_{P_NH^2_0}.
\]
Write \(g=\gcd(p,q)\) and \(M=\max(p,q)/g\ge2\). The following assertions hold simultaneously for every \(N\ge1\).

**Exact ranks and complete unitary model.** For \(j\ge1\),
\[
 r_j(N):=\operatorname{rank}((T_N^{p,q})^j)
   =\left\lfloor\frac{N}{gM^j}\right\rfloor,
 \qquad r_0(N)=N.
\]
Here the finitely many nonzero Jordan blocks are *orthogonal unweighted shift blocks*: the number of blocks of length exactly \(k\ge1\) is
\[
 b_k(N)=r_{k-1}(N)-2r_k(N)+r_{k+1}(N).
\]
With \(L=\lfloor N/g\rfloor\), there is a unitary equivalence
\[
 T_N^{p,q}\ \simeq\ 
 0_{\mathbb C^{N-L}}\oplus
  \bigl(P_L C_{z^M}P_L\bigr)\big|_{\operatorname{span}\{e_1,\ldots,e_L\}},
\]
where the last summand is absent if \(L=0\). Thus the smaller normalized exponent has **no effect on any finite-section unitary invariant**. Moreover, two unequal-exponent pairs have unitarily equivalent sections at **every** positive cutoff \(N\) if and only if their greatest common divisors and their larger exponents are both equal.

**Complete Hermitian eigenvalues and limit law.** Put \(H_N=(T_N^{p,q}+(T_N^{p,q})^*)/2\). Its eigenvalues, counted with multiplicity, are
\[
 \cos\left(\frac{j\pi}{k+1}\right),
 \quad 1\le j\le k,
 \quad\text{each repeated }b_k(N)\text{ times},\quad k\ge1.
\]
In particular its characteristic polynomial is \(\prod_{k\ge1}[2^{-k}U_k(x)]^{b_k(N)}\), where \(U_k\) is the Chebyshev polynomial of the second kind. Its empirical eigenvalue measures converge weakly to the **purely atomic probability measure with dense support** \([-1,1]\):
\[
 \mu_{g,M}=
  \left(1-\frac1g\right)\delta_0
  +\frac1g\sum_{k=1}^{\infty}
     \frac{(M-1)^2}{M^{k+1}}
     \sum_{j=1}^{k}\delta_{\cos(j\pi/(k+1))}.
\]
For coprime exponents, the limit is independent of the smaller exponent and depends only on the larger one. For example, the sections associated to \((p,q)=(5,2),(5,3),(5,4)\) have identical eigenvalues (indeed are unitarily equivalent) for **every** \(N\), and all three share \(\mu_{1,5}\). For the concrete cutoff \(N=100\), each has exactly 64 blocks of length one, 12 of length two, and 4 of length three.

**Sharp numerical-radius edge.** Define \(J_N=\max(\{0\}\cup\{j\ge1:gM^j\le N\})\). The numerical range of \(T_N^{p,q}\) is the closed disk of radius
\[
 w(T_N^{p,q})=\cos\left(\frac{\pi}{J_N+2}\right),
\]
and the edge has the exact scale
\[
 \lim_{N\to\infty}(\log N)^2\bigl(1-w(T_N^{p,q})\bigr)
 =\frac{\pi^2(\log M)^2}{2}.
\]
The elementary numerical-radius formula for an individual Jordan shift is classical; the new assertions concern the arithmetic *multiset of blocks*, simultaneous unitary equivalences, and the induced empirical spectral law for these canonical finite sections.

## Assumptions and scope
All spaces are complex Hilbert spaces and the coefficient basis of \(H^2\) has its usual normalization. The zero-constant subspace matters: on all of \(H^2\), the constant basis vector is an invariant identity summand, making a direct numerical-radius comparison trivial. We restrict to integer \(p,q\ge2\) with \(p\ne q\), and to cutoffs by **polynomial degree** \(1,\ldots,N\), not by enumerating chains or by a spectrally optimized finite-dimensional subspace. The convention \(\lfloor N/g\rfloor=0\) gives a zero-dimensional last summand when \(N<g\). The Chebyshev polynomials satisfy \(U_k(\cos\theta)=\sin((k+1)\theta)/\sin\theta\).

## Proof
**1. Partial-permutation graph.** Composition by a power map sends \(e_n\mapsto e_{pn}\). Its adjoint sends \(e_{qk}\mapsto e_k\) and annihilates indices not divisible by \(q\). Therefore
\[
 T_N^{p,q}e_{qk}=e_{pk}\quad\text{if }\max(pk,qk)\le N,
\]
and all other basis vectors go to zero. Every retained vertex has at most one incoming and at most one outgoing arrow. Since the index is multiplied by the fixed ratio \(p/q\ne1\), there is no directed cycle. Each connected component is consequently a path, and the standard monomial basis, permuted along the paths, gives an **orthogonal direct sum** of nilpotent Jordan shifts with every nonzero edge weight exactly one. This stronger fact, rather than general similarity of nilpotent matrices, gives unitary equivalence.

**2. Exact ranks of powers.** Reduce \(p=ga\) and \(q=gb\), with \(\gcd(a,b)=1\), and put \(M=\max(a,b)\). For each integer \(j\ge1\), the nonzero action of the \(j\)-th power is precisely
\[
 e_{g b^j s}\longmapsto e_{g a^j s},\qquad
 1\le s\le\left\lfloor\frac{N}{gM^j}\right\rfloor.
\]
To see necessity, an input allowing \(j\) successive arrows must be divisible by \(gb^j\), because consecutive divisibility by \(gb\) and coprimality of \(a,b\) force one additional factor \(b\) at each step. Conversely, every indicated input follows the stated chain, whose intermediate indices are \(g a^i b^{j-i}s\) for \(0\le i\le j\). They all lie between its two endpoints when \(a\ne b\), so the endpoint bound \(g M^j s\le N\) is both necessary and sufficient. Distinct \(s\) give orthogonal outputs. This proves the rank identity for every \(j\), including beyond the nilpotency index.

**3. Block multiplicities and universality.** For a nilpotent Jordan block of length \(k\), its \(j\)-th power has rank \(\max(k-j,0)\). Thus \(r_j=\sum_{k\ge1}b_k\max(k-j,0)\); taking the second forward difference gives the formula for \(b_k\). For the truncated single composition \(P_L C_{z^M}P_L\), the same argument gives power ranks \(\lfloor L/M^j\rfloor=\lfloor N/(gM^j)\rfloor\). Padding by \(N-L\) zero blocks matches the rank at \(j=0\) as well. Because both finite operators are orthogonal sums of unweighted Jordan paths, identical power ranks determine their full *unitary* block decompositions.

If two families have equivalent sections for all \(N\), the smallest \(N\) for which the first-power rank becomes nonzero must agree. This smallest cutoff is \(gM=\max(p,q)\). The analogous smallest cutoff for the second-power rank is \(gM^2\). Their ratio determines \(M\), and then their quotient determines \(g\). Conversely, these two parameters already determine all power ranks and hence all the unitary block structures. This proves the stated **if and only if**, not merely sufficient universality.

**4. Hermitian spectrum.** The symmetrized length-\(k\) shift is the tridiagonal path matrix with entries \(1/2\) directly above and below the diagonal. The sine vectors with components \(\sin(\ell j\pi/(k+1))\), \(1\le\ell\le k\), diagonalize it, with eigenvalues \(\cos(j\pi/(k+1))\). This establishes the full finite eigenvalue list and its characteristic polynomial.

For fixed \(k\ge2\), the floor identities yield
\[
 \frac{b_k(N)}N\longrightarrow \frac{(M-1)^2}{gM^{k+1}}.
\]
For \(k=1\), the limit is \(1-2/(gM)+1/(gM^2)\), which equals the \(k=1\) weight of the proposed measure plus \(1-1/g\). To justify convergence of measures rather than only coefficientwise convergence, observe that the number of coordinates in Jordan blocks of size at least \(K\ge2\) obeys
\[
 \sum_{k\ge K} k b_k(N)
 \le K\,r_{K-1}(N)
 \le \frac{KN}{gM^{K-1}}.
\]
The right side divided by \(N\) tends uniformly to zero as \(K\to\infty\). Consequently the finite eigenvalue measures converge against every bounded continuous test function to the displayed pure-point measure. Its total mass is one because
\[
 \sum_{k\ge1}\frac{k(M-1)^2}{M^{k+1}}=1.
\]
Every value \(\cos(j\pi/(k+1))\) occurs with positive mass, and these values are dense in \([-1,1]\). Thus the limit is purely atomic while its topological support is the full interval. No absolutely continuous component is implicit.

**5. Numerical radius.** The largest nonzero Jordan block has length \(1+J_N\), because the \(j\)-th power is nonzero exactly when \(gM^j\le N\). Rotating the basis along a path shows that its numerical range is a disk. The path's largest symmetrized eigenvalue is \(\cos(\pi/(k+1))\), which is its numerical radius. Taking the direct sum selects the longest path, giving the exact formula. Finally \(J_N=(\log N)/(\log M)+O(1)\) for fixed \(g,M\), and \(1-\cos u\sim u^2/2\) gives the asserted logarithmic edge constant.

## Verification
A standalone, standard-library Python checker constructs all arrows and independently enumerates all Jordan paths for every distinct parameter pair \(2\le p,q\le18\) and twenty-three degree cutoffs through \(600\). It compares path multiplicities, power ranks, largest block, exact second moments, and parameter-universality fingerprints against the arithmetic formulas. Running `python3 checker.py` produces `PASS 61661 exact assertions`. These tests include noncoprime and reverse-order pairs and use only integer arithmetic or exact rational arithmetic. The all-parameter conclusions and convergence theorem follow from the preceding proof rather than those finite tests.

## Relationship to prior work
Clifford, Dabkowski, and Wiggins (2021), Section 2.3 and Theorem 6, give the underlying monomial-basis action and qualitative point-spectrum and numerical-range information for composition–adjoint products. Their reported results do not provide the **degree-cutoff rank sequence, full finite-cutoff unitary-equivalence classification, exact Hermitian multiplicity profile, or the limiting dense-support pure-atomic measure**. Leng and Zhao (2026), Theorem 3.24, address Schatten-class membership for composition–adjoint products with inner symbols, not the present finite cutoff invariant. The single-block cosine numerical radius is standard and is explicitly credited to the classical nilpotent-shift literature. Thus neither a general finite-rank Jordan theory nor a classical cosine formula is presented here as an independent discovery. The scope of the asserted new contribution is the complete arithmetic **degree-truncation and spectral-statistics package**.

## Limitations
Only unweighted Hardy-space monomial power maps and polynomial-degree cutoffs are covered. These sections do **not** approximate the uncompressed operator in operator norm. The limiting measure concerns eigenvalues of the Hermitian parts, not singular-value distributions or spectral measures of the nonnormal infinite operators. A more general historical theorem about finite compressions of weighted partial permutations might imply this specific formula and remains a publication-priority risk. Originality is a best-knowledge assessment, not proof of global novelty; no independent mathematical audit or publication validation has occurred.

## References
1. Q. Leng and X. Zhao, *Schatten class membership of products of composition operators and their adjoints*, arXiv:2610.15472v1, first public 2026-10-11, especially Theorem 3.24. https://arxiv.org/abs/2610.15472 .
2. J. Clifford, M. Dabkowski, and A. Wiggins, *The Numerical Range of \(C_\psi^*C_\varphi\) and \(C_\varphi C_\psi^*\)*, *Concrete Operators* **8** (2021), 13–23, especially Section 2.3 and Theorem 6. https://doi.org/10.1515/conop-2020-0108 .
3. U. Haagerup and P. de la Harpe, *The numerical radius of a nilpotent operator on a Hilbert space*, *Proc. Amer. Math. Soc.* **115** (1992), 371–379. https://doi.org/10.1090/S0002-9939-1992-1072339-6 .
