# Sharp real-window Gabor tomography rank on finite abelian groups

## Finding
Let \(G\) be a finite abelian group of order \(N\ge2\), let \(\widehat G\) be its character group, and let \(\varnothing\ne S\subseteq G\). Define the difference set \(D=S-S\) and the two-torsion subgroup \(T=G[2]=\{a\in G:2a=0\}\). For each real window \(g\in\mathbb R^G\) with support exactly \(S\), take the full time-frequency orbit \(v_{u,\eta}=M_\eta T_u g\), where \(u\in G\), \(\eta\in\widehat G\), \((T_u g)(x)=g(x-u)\), and \((M_\eta g)(x)=\eta(x)g(x)\). Its rank-one projectors are \(P_{u,\eta}=v_{u,\eta}v_{u,\eta}^*\).

**Sharp all-support rank theorem.** The maximum complex-linear matrix-span dimension of these projectors, over all real windows supported exactly on \(S\), is
\[
\boxed{R_{\max}(G,S)=N|D|-\frac N2\bigl|(D\cap T)\setminus\{0\}\bigr|.}
\]
The bound is attained by strictly positive integer entries on \(S\), and by a relatively open dense, full-Lebesgue-measure set of positive windows on \(S\). Precisely, there exists a single explicit such window whose ambiguity function has zeros at **exactly** the forced positions
\[
\boxed{A_g(a,\chi)=0\ \Longleftrightarrow\ a\notin D\quad\text{or}\quad
       \bigl(a\in T\setminus\{0\},\ \chi(a)=-1\bigr),}
\]
where \(A_g(a,\chi)=\sum_{x\in G}g(x)g(x-a)\chi(x)\). For every real window supported on \(S\), all positions on the right are necessarily zero. The invisible matrix directions at an attaining window are exactly the Weyl operators indexed by these positions.

For full support \(S=G\) one obtains the sharp capacity law
\[
\boxed{\max_{g\in\mathbb R^G}\operatorname{rank}\operatorname{span}\{P_{u,\eta}\}
=N^2-\frac N2(|G[2]|-1).}
\]
Thus a real window can be informationally complete for complex matrices exactly when \(N\) is odd. For the three abelian groups of order eight, the sharp real-window ranks are respectively \(60\) on \(\mathbb Z_8\), \(52\) on \(\mathbb Z_4\times\mathbb Z_2\), and \(36\) on \((\mathbb Z_2)^3\). For any elementary two-group, the full-support maximum equals \(N(N+1)/2\), the dimension of real symmetric matrices.

## Assumptions and scope
All groups are finite abelian and written additively; \(0\) is the identity. A window is supported exactly on \(S\) when it is zero off \(S\) and nonzero at every site in \(S\). The rank refers to the complex span in \(M_N(\mathbb C)\), or equivalently to the real span dimension of these Hermitian projectors inside the real vector space of Hermitian matrices. No normalization is needed: scaling a nonzero window does not change the span rank. ``Informationally complete'' means the linear measurement map is injective on all complex matrices, **not merely on rank-one signal matrices**. When \(S\ne G\), the sharp rank can be smaller because \(D\ne G\).

The explicit attaining window is as follows. Choose any enumeration \(S=\{s_0,\ldots,s_{m-1}\}\), put \(B=2N+1\), and define \(g(s_i)=B^{2^i}\) and \(g(x)=0\) for \(x\notin S\). The very large integer entries are only an existence certificate; normalization or generic bounded positive choices also attain the same rank.

## Proof
**1. Weyl diagonalization of the lifted measurements.** Define \(W_{a,\chi}=M_\chi T_a\), for \(a\in G\) and \(\chi\in\widehat G\). Orthogonality of characters shows that these \(N^2\) operators form an orthogonal Hilbert--Schmidt basis of \(M_N(\mathbb C)\). Conjugation by \(M_\eta T_u\) multiplies each \(W_{a,\chi}\) by a distinct character of \(G\times\widehat G\). Directly,
\[
\operatorname{tr}(W_{a,\chi}P_{u,\eta})
=\chi(u)\overline{\eta(a)}\,A_g(a,\chi).
\]
The \(N^2\)-by-\(N^2\) character table is invertible, so the lifted linear map \(H\mapsto(\operatorname{tr}(HP_{u,\eta}))_{u,\eta}\) has rank exactly \(\#\{(a,\chi):A_g(a,\chi)\ne0\}\). Its kernel is the span of those \(W_{a,\chi}\) for which \(A_g(a,\chi)=0\). This is the standard finite Weyl/ambiguity diagonalization; the new content below is the complete sharp zero-pattern classification for arbitrary real support masks.

**2. Forced zeros.** If \(a\notin D\), there is no \(x\) with \(x,x-a\in S\), so all coefficients vanish. Suppose instead \(a\in T\setminus\{0\}\). Translation by \(a\) pairs each \(x\in G\) with the distinct point \(x-a\). For real \(g\), their contributions to \(A_g(a,\chi)\) add to
\[
g(x)g(x-a)\chi(x)\bigl(1+\chi(a)^{-1}\bigr).
\]
Because \(a\) has order two, \(\chi(a)\in\{1,-1\}\), and the pair cancels whenever \(\chi(a)=-1\), for **every** choice of real amplitudes. For each nonzero involution, exactly \(N/2\) characters take the value \(-1\), since characters separate points and evaluation at \(a\) is a surjective homomorphism onto \(\{1,-1\}\).

**3. One explicit window avoids every other zero.** For the given integer window, each nonzero summand of \(A_g(a,\chi)\) has the form \(B^{2^i+2^j}\chi(s_i)\) for an ordered pair \((s_i,s_j)\) with \(s_i-s_j=a\). If \(a=0\), every pair has \(i=j\); the exponents \(2^{i+1}\) are distinct, and each coefficient has modulus one. If \(a\ne0\) but \(2a\ne0\), every unordered pair occurs at most once for that fixed oriented difference, so again all exponents are distinct and coefficients have modulus one. If \(a\ne0\) and \(2a=0\), each unordered pair occurs twice and its combined coefficient is \(\chi(s_i)(1+\chi(a)^{-1})\), which is zero in the forced case and has modulus two otherwise. Distinct unordered pairs of distinct indices give distinct binary sums \(2^i+2^j\). Thus, whenever \(a\in D\) and \((a,\chi)\) is not forced, the resulting sum consists of at most \(N\) terms with **pairwise distinct nonnegative integer exponents** and coefficients of modulus between one and two. Choose the term having the largest exponent \(E\). The total modulus of every lower-exponent term is at most \(2N B^{E-1}<B^E\), since \(B=2N+1\). The leading term cannot cancel. Hence precisely the stated forced positions vanish.

**4. Sharp rank and genericity.** There are \(N\) characters for each allowed difference \(a\in D\). For each nonzero involution in \(D\) exactly half are necessarily lost, and step 3 shows there are no further losses for the displayed window. Therefore the sharp rank is \(N|D|-(N/2)|(D\cap T)\setminus\{0\}|\). Each nonforced ambiguity coefficient is a nonzero polynomial in the \(|S|\) real amplitudes, as certified by step 3. The zero locus of a nonzero real or complex polynomial has measure zero and empty interior. A finite union of these loci cannot cover the strictly positive orthant and its complement is relatively open dense and full measure. This proves the genericity claim. Taking \(D=G\) gives the full-support capacity and the group-order consequences: \(T=\{0\}\) exactly when \(N\) is odd, and when \(N\) is even the unavoidable defect is at least \(N/2\).

## Verification
The standalone standard-library script `verify_real_gabor.py` computes exact character sums as integer polynomials in a root of unity, reduces them modulo the corresponding cyclotomic polynomial, and checks the predicted zero sets and rank for **every nonempty support** on ten test groups: \(\mathbb Z_n\) for \(n\in\{2,3,4,5,6,8\}\), \(\mathbb Z_2^2\), \(\mathbb Z_2\times\mathbb Z_4\), \(\mathbb Z_2^3\), and \(\mathbb Z_3^2\). The script passed all \(1410\) support patterns. These finite tests do not replace the all-group proof. Run `python3 verify_real_gabor.py` using Python 3 and no third-party packages.

## Relationship to prior work
Feichtinger, Kozek and Luef [1] develop Weyl/spreading analysis over finite abelian groups; the Weyl basis used above is classical. Bojarovska and Flinth [2] prove Gabor ambiguity-based linear lifting and phase-retrieval results; the Weyl/rank criterion is prior mathematics. Goldberger, Kang and Okoudjou [3] identify Gabor-projector rank with ambiguity support and classify several special cyclic families. The present result **does not** claim novelty for that equivalence, for standard character cancellation, or for special examples obtained from previously studied windows.

The published result *Arithmetic rigidity of prime-cyclic Gabor tomography for positive rational windows* already gives, for every positive rational window on an odd prime group with proper support, rank equal to prime order times the difference-set size; this **stronger prime-arithmetic special case is prior coverage**. *Exact operator-span rank and arithmetic thresholds for cyclic boxcar Gabor measurements* gives exact ranks for all cyclic interval-indicator windows, including an even-order obstruction; those boxcar ranks are also prior coverage. The finding here instead optimizes over **all real windows with every prescribed support**, for **every finite abelian group**, and supplies a simultaneous constructive sharpness witness, a complete universal ambiguity-zero classification, and the exact two-torsion correction. *Exact matrix-recovery ranks for one-frequency deletion frames on finite abelian groups* concerns a different family of measurements, not the Gabor orbits considered here. These comparisons are by mathematical implication; residual risk of an unindexed equivalent generic-rank theorem remains.

## Limitations
The result addresses exact, noiseless **linear matrix tomography**. It does not claim that the failure of linear informational completeness prevents nonlinear phase retrieval of pure signals, nor does it give a stability bound or conditioning optimum. The integer witness can have enormous dynamic range and is not a practical robust sensing design. Realness is essential: complex-valued windows do not share the involution cancellation mechanism. The basic Weyl-diagonal rank fact and prime-rational and boxcar special cases are known. Originality of the all-real-mask sharp rank theorem requires independent literature review; no independent audit or external certification has been conducted.

## References
[1] H. G. Feichtinger, W. Kozek and F. Luef, *Gabor analysis over finite Abelian groups*, arXiv:math/0703228, first public 2007-03-08. https://arxiv.org/abs/math/0703228

[2] I. Bojarovska and A. Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800, first public 2015-03-19. https://arxiv.org/abs/1503.05800

[3] A. Goldberger, S. Kang and K. A. Okoudjou, *Towards a classification of incomplete Gabor POVMs in \(\mathbb C^d\)*, arXiv:2106.01509, first public 2021-06-02. https://arxiv.org/abs/2106.01509

[4] *Arithmetic rigidity of prime-cyclic Gabor tomography for positive rational windows*, publicly available mathematical result (2026), consulted in complete text.

[5] *Exact operator-span rank and arithmetic thresholds for cyclic boxcar Gabor measurements*, publicly available mathematical result (2026), consulted in complete text.

[6] *Exact matrix-recovery ranks for one-frequency deletion frames on finite abelian groups*, publicly available mathematical result (2026), consulted in complete text.
