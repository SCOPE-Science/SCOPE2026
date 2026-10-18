# Phase-alphabet tomography ranks for binary Sidon supports

## Finding
Let \(G\cong(\mathbb Z/2\mathbb Z)^n\) have cardinality \(N\), and let \(S\subset G\) have odd size \(k\ge3\). The **binary Sidon property** means that the sums of distinct unordered pairs of points of \(S\) are all distinct. For phases \(u_x\in\mathbb T\), form the unit window \(g(x)=k^{-1/2}u_x\mathbf1_S(x)\). The complete complex-linear operator-tomography measurements are
\[\mathcal L_g(X)=\bigl(\operatorname{tr}(X P_{a,\beta})\bigr)_{a\in G,\,\beta\in\widehat G},\quad P_{a,\beta}=|M_\beta T_ag\rangle\langle M_\beta T_ag|.\]
Here \(T_af(x)=f(x-a)\) and \(M_\beta f(x)=\beta(x)f(x)\). Define the **resonant-pair count**
\[B(u)=\#\{\{x,y\}\subset S:x\ne y,\ u_x/u_y\in\mu_4\},\qquad\mu_4=\{1,-1,i,-i\}.\]
Then, with \(H=\binom{k}{2}\),
\[\boxed{\operatorname{rank}_{\mathbb C}\mathcal L_g=N(1+H-B(u)/2).}\]
Every lost Weyl operator direction is specified exactly in the proof. All zero-shift directions survive.

For an alphabet of \(L\)-th roots of unity, let \(r=L/\gcd(L,4)\) and write \(k=ar+s\) with \(0\le s<r\). The **sharp maximal rank for this alphabet** is
\[\boxed{N\left[1+H-\frac12\left((r-s)\binom a2+s\binom{a+1}2\right)\right].}\]
It reaches the unrestricted fixed-support ceiling \(N(1+H)\) exactly when \(r\ge k\).

For each \(q=2^m\ge4\), the inverse hyperbola \(S_q=\{(t,t^{-1}):t\in\mathbb F_q^\times\}\subset G=\mathbb F_q^2\) satisfies the Sidon condition and has \(k=q-1\) odd. Its **flat** and **optimally phase-coded** ranks are respectively
\[\boxed{q^2\left(1+\frac{(q-1)(q-2)}4\right),\qquad q^2\left(1+\frac{(q-1)(q-2)}2\right).}\]
The least root-of-unity alphabet order realizing the latter rank is exactly \(L=q-1\). An explicit optimizer assigns the distinct \((q-1)\)-th roots of unity to the \((q-1)\) support points.

## Assumptions and scope
The result concerns complex-linear lifting on the full matrix space \(\mathrm{End}(\ell^2(G))\), not nonlinear pure-state phase retrieval. All characters of a binary group take values \(\pm1\). The theorem assumes **equal nonzero coefficient moduli** for its exact \(B(u)\) formula, but the asserted maximum \(N(1+H)\) is an upper bound for *arbitrary* complex windows supported on \(S\). There are \(N^2\) intensity measurements and \(N^2\) complex matrix coordinates.

## Proof
**1. Weyl diagonalization.** The \(N^2\) Weyl operators \(W_{h,\xi}=M_\xi T_h\), indexed by \((h,\xi)\in G\times\widehat G\), are an orthogonal basis of the complex matrix space. Their conjugation under \(M_\beta T_a\) is multiplication by the distinct Fourier characters of \(G\times\widehat G\). Therefore the columns of \(\mathcal L_g\) in the normalized Weyl basis are mutually orthogonal; the column labelled \((h,\xi)\) is nonzero exactly when the ambiguity coefficient
\[A_g(h,\xi)=\langle g,M_\xi T_hg\rangle\]
is nonzero. Consequently the complex rank equals the number of nonzero ambiguity coefficients, and the kernel is the span of the Weyl basis elements with zero coefficient (conjugate labels give the same zero set).

**2. Zero shift.** Since \(|g(x)|^2=k^{-1}\) for \(x\in S\), we have
\[A_g(0,\xi)=k^{-1}\sum_{x\in S}\xi(x).\]
This is an odd integer divided by \(k\), since \(k\) is odd and each summand equals \(\pm1\). Thus all \(N\) zero-shift modes survive.

**3. Pair shifts.** For \(h\ne0\), the intersection \(S\cap(S+h)\) is empty or consists of exactly the two points \(x,y\) in the unique unordered pair with \(x+y=h\). This uses the binary Sidon property and \(x+h=y\). In the empty case, \(A_g(h,\xi)=0\) for every \(\xi\). In the pair case, an irrelevant global phase aside,
\[kA_g(h,\xi)=\xi(x)\,\overline{u_x}u_y+\xi(y)\,\overline{u_y}u_x.\]
As \(\xi(y)=\xi(x)\xi(h)\), this can vanish only if \((u_x/u_y)^2=\pm1\), or equivalently \(u_x/u_y\in\mu_4\). For a nonresonant pair, all \(N\) characters survive; for a resonant pair, the exact cancellation equation picks one sign of \(\xi(h)\), giving exactly \(N/2\) zero modes because \(h\ne0\). There are \(H=\binom{k}{2}\) distinct pair shifts. Hence the rank is \(N+N(H-B)+\tfrac N2B=N(1+H-B/2)\). The preceding cases explicitly classify all kernel modes.

**4. Alphabet optimum and unrestricted ceiling.** Two elements of \(\mu_L\) have a resonant ratio exactly when they lie in the same coset modulo \(\mu_L\cap\mu_4\). There are \(r=L/\gcd(L,4)\) cosets. If \(n_j\) support phases occupy coset \(j\), then \(B=\sum_{j=1}^r\binom{n_j}{2}\). Under \(\sum n_j=k\), elementary convexity of the binomial coefficient makes this smallest when the occupancies differ by at most one, giving \((r-s)\binom a2+s\binom{a+1}2\). Every such allocation is realizable. Each pair shift can support at most \(N\) coefficients, while the zero shift supports at most \(N\), so \(N(1+H)\) is a universal bound even without equal coefficient moduli. It is attained by choosing one phase in each of at least \(k\) cosets, and not if \(r<k\) in the phase-only alphabet class.

**5. Binary inverse hyperbola.** For distinct \(s,t\in\mathbb F_q^\times\), their sum is a nonzero element \(a=s+t\), and the sum of inverses is \(b=s^{-1}+t^{-1}=a/(st)\). Thus the vector \((a,b)\) uniquely determines both \(a=s+t\) and \(st=a/b\), hence the unordered roots \(\{s,t\}\) of \(X^2+aX+a/b\). Therefore \(S_q\) is binary Sidon, and substitution of \(N=q^2\), \(k=q-1\), and \(B=H\) or \(B=0\) proves the two displayed ranks. Because \(k\ge3\) is odd, \(L=k\) gives \(r=k\), while every positive integer \(L<k\) has \(L/\gcd(L,4)\le L<k\); hence the alphabet threshold is sharp.

## Verification
Run `python verify.py` with standard Python 3. The standalone exact finite-field implementation checks pair-sum uniqueness, character-halfspace sizes, zero-shift oddness, and both predicted rank counts for \(q=4,8,16\). The reproduced output is in `verify_output.txt`. These tests corroborate the proof; the proof itself covers every binary group with odd-cardinality Sidon support and every \(q=2^m\ge4\).

## Relationship to prior work
Führ and Oussa (2022, arXiv:2201.08654) discuss phase retrieval for nilpotent-group representation orbits and the standard ambiguity-function nonvanishing criterion, but do not give the sharp phase-alphabet rank optimization for arbitrary binary Sidon supports. Redman, Rose, and Walker (2021, arXiv:2109.00292) study Sidon-set geometry and constructions in binary vector spaces, not rank-one Gabor tomography. Li, Juste, Brennan, Cheng, and Han (first publicly available online October 2017) characterize general projective representation frame vectors, without a statement of this binary Sidon phase-rank census. The novelty assessment is best-knowledge rather than exhaustive.

## Limitations
No nonlinear phase-retrieval assertion follows from the complex-linear rank. The phase-alphabet optimum is over equal-modulus windows, and the universal ceiling only bounds windows with the same support. Rank does not alone determine nonzero singular values or conditioning. Older equivalent calculations under alternative Gabor/Sidon terminology may exist and would require independent bibliographic review.

## References
- H. Führ and V. Oussa, *Phase retrieval for nilpotent groups*, arXiv:2201.08654v1 (21 January 2022), relevant introduction and finite-group sections. https://arxiv.org/html/2201.08654v2
- M. Redman, L. Rose and R. Walker, *A Small Maximal Sidon Set in Z_2^n*, arXiv:2109.00292v1 (1 September 2021), especially Definition 1.1 and Sections 2–3. https://arxiv.org/html/2109.00292v3
- L. Li, T. Juste, J. Brennan, C. Cheng and D. Han, *Phase Retrievable Projective Representation Frames for Finite Abelian Groups*, J. Fourier Anal. Appl., online 16 October 2017, DOI 10.1007/s00041-017-9570-6. A publisher preview and bibliographic statement were available; full text was not reviewed.
