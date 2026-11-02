# Discrete-Gaussian ranks and exponentially rare homology among zero-product matrix pairs

## Finding

Fix a prime power \(q\ge2\). For every integer \(n\ge1\), choose an **ordered pair** \((A,B)\) uniformly from the finite set of pairs in \(M_n(\mathbb F_q)^2\) satisfying \(AB=0\). This is a *joint-uniform* law, not the law obtained by first choosing \(A\) uniformly from all matrices and then choosing a compatible \(B\).

Let \(R=\operatorname{rank}A\), \(T=\operatorname{rank}B\), and \(H=n-R-T\), the homology dimension of the three-term complex \(\mathbb F_q^n\xrightarrow{B}\mathbb F_q^n\xrightarrow{A}\mathbb F_q^n\) at its middle term. Put \(n=2m+\varepsilon\), where \(m=\lfloor n/2\rfloor\) and \(\varepsilon\in\{0,1\}\). Define
\[
Q_j(q)=\prod_{i=1}^{j}(1-q^{-i}),\qquad Q_\infty(q)=\prod_{i=1}^\infty(1-q^{-i}),\qquad
\Theta_\varepsilon(q)=\sum_{j\in\mathbb Z}q^{-j^2+\varepsilon j}.
\]

**Exact finite law.** For \(0\le r,s\le n\), the number \(N_{n;r,s}\) of admissible pairs with \(R=r,T=s\) equals zero when \(r+s>n\). Otherwise
\[
N_{n;r,s}={n\brack r}_q^2\,|\operatorname{GL}_r(q)|\,{n-r\brack s}_q\,{n\brack s}_q\,|\operatorname{GL}_s(q)|.
\tag{1}
\]
The cardinality \(Z_n\) of all admissible pairs satisfies the parity-sensitive asymptotic
\[
Z_n=q^{n^2+\lfloor n^2/4\rfloor}\left(\frac{\Theta_\varepsilon(q)}{Q_\infty(q)}+o(1)\right).
\tag{2}
\]

**Joint rank law.** For each fixed parity \(\varepsilon\), as \(n\to\infty\) through \(n\equiv\varepsilon\pmod2\), the distribution of \((R-m,T-m)\) converges in *total variation on \(\mathbb Z^2\)* to the law of \((J,\varepsilon-J)\), where
\[
\Pr(J=j)=\frac{q^{-j^2+\varepsilon j}}{\Theta_\varepsilon(q)},\qquad j\in\mathbb Z.
\tag{3}
\]
In particular, the middle homology is zero with probability tending to one, and the complete leading asymptotic for its failure is
\[
\Pr(H\ge1)=\frac{\Theta_{1-\varepsilon}(q)}{(q-1)\Theta_\varepsilon(q)}q^{-m}+o(q^{-m}),
\qquad \Pr(H\ge2)=O_q(q^{-2m}).
\tag{4}
\]
Thus \(\Pr(H=1)\) has the same leading term as \(\Pr(H\ge1)\). These statements hold for every fixed prime-power field size, including characteristic two.

## Assumptions and scope

All products and ranks refer to ordinary matrices over \(\mathbb F_q\). Each *pair* satisfying \(AB=0\) receives the same probability. Zero matrices are included, and the two factors are ordered. The Gaussian binomial coefficient \({a\brack b}_q\) counts \(b\)-dimensional subspaces of \(\mathbb F_q^a\), with \({a\brack b}_q=0\) for \(b\notin[0,a]\). Also \(|\operatorname{GL}_0(q)|=1\). Total variation on a discrete space means half the \(\ell^1\)-distance of the probability masses. The asymptotics keep \(q\) fixed while \(n\) grows, separately along even and odd dimensions; no simultaneous growing-field limit is asserted. Constants hidden in \(O_q\) may depend on \(q\), not on \(n\).

## Proof

**Step 1: count every rank pair.** The number of rank-\(r\) endomorphisms of an \(n\)-dimensional vector space is \({n\brack r}_q^2|\operatorname{GL}_r(q)|\): choose image and kernel, then the induced isomorphism from quotient to image. For fixed \(A\) of rank \(r\), the condition \(AB=0\) means precisely \(\operatorname{im}B\subseteq\ker A\), which has dimension \(n-r\). Rank-\(s\) maps from \(\mathbb F_q^n\) into the fixed \((n-r)\)-space number \({n-r\brack s}_q {n\brack s}_q|\operatorname{GL}_s(q)|\). Multiplication gives (1), including boundary cases.

**Step 2: rank weighting and partition function.** For fixed \(A\), there are exactly \(q^{n(n-r)}\) compatible \(B\)'s. Therefore the number of zero-product pairs with \(R=r\) is
\[
W_n(r)={n\brack r}_q^2|\operatorname{GL}_r(q)|q^{n(n-r)}
=q^{n^2+r(n-r)}\frac{Q_n(q)^2}{Q_r(q)Q_{n-r}(q)^2},\quad 0\le r\le n.
\tag{5}
\]
Set \(r=m+j\), so \(-m\le j\le m+\varepsilon\) and \(r(n-r)=m(m+\varepsilon)+\varepsilon j-j^2\). Since \(0<Q_\infty(q)\le Q_j(q)\le1\) for every \(j\), after extracting \(q^{n^2+m(m+\varepsilon)}\), the summands in (5) are uniformly bounded by \(Q_\infty(q)^{-3}q^{-j^2+\varepsilon j}\). For each fixed \(j\), their coefficient \(Q_n^2/(Q_{m+j}Q_{m+\varepsilon-j}^2)\) tends to \(1/Q_\infty(q)\). Dominated convergence over \(j\in\mathbb Z\) proves (2), because \(m(m+\varepsilon)=\lfloor n^2/4\rfloor\), and also gives total-variation convergence of \(R-m\) to (3). Moreover the same Gaussian majorant bounds \(\mathbb E[q^{\ell(m-R)}]\) uniformly in \(n\), for each fixed nonnegative integer \(\ell\).

**Step 3: saturation of the compatible map.** Conditional on \(R=r\) under the pair-uniform law, \(B\) is uniform among all \((n-r)\times n\) matrices (after choosing bases). Its rank equals \(n-r\) with probability
\[
P_\mathrm{full}(n,r)=\prod_{i=r+1}^{n}(1-q^{-i})=\frac{Q_n(q)}{Q_r(q)}.
\tag{6}
\]
The union bound gives
\[
0\le1-P_\mathrm{full}(n,r)\le\sum_{i=r+1}^{n}q^{-i}\le\frac{q^{-r}}{q-1}.
\tag{7}
\]
By the tight discrete-Gaussian law of \(R-m\), the right side has expectation \(O_q(q^{-m})\). On the event \(H=0\), the relation \(T=n-R\) is exact. Couple \((R-m,T-m)\) to \((R-m,\varepsilon-(R-m))\) using the same \(R\); the probability they differ equals \(\Pr(H>0)\). Combined with the total-variation convergence from Step 2, this proves the joint law (3).

**Step 4: first homology defect.** For each fixed \(j\), putting \(r=m+j\) and taking \(n\to\infty\) along the chosen parity gives
\[
q^r\left(1-\frac{Q_n(q)}{Q_r(q)}\right)\longrightarrow\frac1{q-1}.
\tag{8}
\]
Indeed, the sum \(\sum_{i=r+1}^nq^{-i}\) tends, after multiplying by \(q^r\), to \(1/(q-1)\), while the difference between this sum and \(1-\prod_{i=r+1}^n(1-q^{-i})\) is bounded by its square, negligible after that scaling. The bound (7) yields \(q^r(1-P_\mathrm{full})\le1/(q-1)\), so Step 2 supplies the summable dominating function \(C_q q^{-j^2+(\varepsilon-1)j}\). Consequently
\[
\lim_{n\to\infty\atop n\equiv\varepsilon\ (2)}q^m\Pr(H\ge1)
=\frac1{(q-1)\Theta_\varepsilon(q)}\sum_{j\in\mathbb Z}q^{-j^2+(\varepsilon-1)j}
=\frac{\Theta_{1-\varepsilon}(q)}{(q-1)\Theta_\varepsilon(q)},
\tag{9}
\]
where the last equality follows by \(j\mapsto-j\) for \(\varepsilon=0\), and is immediate for \(\varepsilon=1\).

**Step 5: defects of dimension at least two.** If the random \((n-r)\times n\) matrix \(B\) has rank at most \(n-r-2\), then the kernel of its transpose contains a two-dimensional subspace. For each fixed two-dimensional subspace \(U\) of the \((n-r)\)-dimensional dual space, the probability that every column annihilates \(U\) is \(q^{-2n}\). A union bound, together with \({n-r\brack2}_q\le C_q q^{2(n-r-2)}\), gives \(\Pr(H\ge2\mid R=r)\le C_q q^{-2r}\). After averaging and using the bounded \(\mathbb E[q^{2(m-R)}]\) from Step 2, this is \(O_q(q^{-2m})\). Equation (4) follows. \(\square\)

## Verification

The standalone script `verify.py` enumerates actual finite-field matrix pairs for \((q,n)=(2,1),(2,2),(2,3),(3,1),(3,2)\), computes products and both ranks by direct matrix arithmetic, and compares each rank-pair multiplicity with (1). It separately compares both exact ways of counting \(Z_n\) for four values of \(q\) and all \(1\le n\le12\), using integer arithmetic rather than numerical approximation. Invoke `python3 verify.py` from the directory containing this file. A successful execution prints `VERIFY_OK`. These finite tests corroborate the exact formulas; the infinite asymptotics follow from the analytic estimates in the proof, not from finite enumeration.

## Relationship to prior work

Đurić, Jevđenić and Stopar [1] define a compressed zero-product digraph of finite matrix rings. Their Proposition 3.1 counts adjacency between image–kernel classes by Gaussian binomial coefficients, a precursor for the finite rank-pair count (1) when each class is correctly weighted by its number of matrices. They study degrees, graph reconstruction and automorphisms, not the pair-uniform measure or its fixed-field asymptotic ranks and homology tail. Gould, Johnson and Naz [2] describe the rank/Green-stratum geometry of finite-field matrix monoids, which motivates studying multiplication-zero pairs across matrix rank strata; their article does not give the pair-uniform joint rank law or the fixed-field theta limit. Catanzaro and Zabka [3] count compatible differentials and study a *sequentially chosen* uniform random chain complex, deriving its homology distribution and investigating \(q\to\infty\), not the jointly uniform pair law at fixed \(q\) with \(n\to\infty\). For instance, a sequentially uniform first matrix has rank \(n-O_{\Pr}(1)\), whereas the first matrix under our globally pair-uniform conditioning has rank \(n/2+O_{\Pr}(1)\). Their finite-rank counting lemma is an ingredient but does not imply this sampling contrast or the parity-dependent formula (4) without a new normalization and limiting analysis.

Huang [4] studies pairs satisfying **both** \(AB=0\) and \(BA=0\), where a fixed rank-\(r\) first matrix has \(q^{(n-r)^2}\) second-matrix choices; our one-sided constraint has \(q^{n(n-r)}\). The distinction changes the rank weights substantially. Ginzburg and Pasechnik [5] treat a **single** square-zero differential \(D^2=0\) and obtain a nondegenerate fixed-field limiting distribution for homology; the present two-map jointly uniform complex instead has zero homology with exponentially high probability. These comparisons separate sampling spaces, not merely terminology.

## Limitations

The novelty comparison is based on inspected primary literature and semantic searching, not a proof of bibliographic uniqueness. An equivalent fixed-field, growing-dimension result may exist in work on representations of the length-two-zero quiver, zero-product varieties, or asymptotic enumeration of chain complexes. No rates for the total-variation convergence in (3), no limit with \(q=q(n)\), and no multistage complex theorem are asserted. The verifier cannot certify the infinite-dimensional statements. Nothing here claims mathematical independent validation or independent publication priority.

## References

[1] A. Đurić, S. Jevđenić and N. Stopar, *Compressed zero-divisor graphs of noncommutative rings* (later *Compressed zero-divisor graphs of matrix rings over finite fields*), arXiv:1810.02776, first public October 5, 2018; 2010 primary MSC 16U99. https://arxiv.org/abs/1810.02776.

[2] V. Gould, M. Johnson and M. Naz, *Matrix semigroups over semirings*, arXiv:1907.12518, first public July 29, 2019; 2010 primary MSC 20M10. https://arxiv.org/abs/1907.12518.

[3] M. J. Catanzaro and M. J. Zabka, *A Model for Random Chain Complexes*, arXiv:1901.00964, first public January 4, 2019. https://arxiv.org/abs/1901.00964.

[4] Y. Huang, *Mutually annihilating matrices, and a Cohen--Lenstra series for the nodal singularity*, arXiv:2110.15566, first public October 29, 2021. https://arxiv.org/abs/2110.15566.

[5] V. Ginzburg and D. V. Pasechnik, *Random Chain Complexes*, arXiv:1602.08538, first public February 27, 2016. https://arxiv.org/abs/1602.08538.
