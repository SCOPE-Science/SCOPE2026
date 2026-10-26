# Sharp initial-rank tomography of alternating-adjoint nilpotent paths

## Finding

**Theorem.** Fix integers \(m\ge2\), \(d\ge1\) and an arbitrary complex matrix \(T\in M_d(\mathbb C)\). Form the block-nilpotent path \(N_m(T)\in M_{md}(\mathbb C)\) with zero blocks except the first superdiagonal, whose blocks alternate \(T,T^*,T,T^*,\ldots\), beginning with \(T\). For \(1\le k\le md\), let the rank-\(k\) numerical range be

\[
\Lambda_k(A)=\{z\in\mathbb C:\text{some orthogonal rank-}k\text{ projection }P\text{ satisfies }PAP=zP\}.
\]

Write the singular values of \(T\) in nonincreasing order as \(s_1\ge\cdots\ge s_d\ge0\). Let \(q=\lfloor m/2\rfloor\), \(c_j=\cos(j\pi/(m+1))>0\) for \(1\le j\le q\), and let \(v_1\ge\cdots\ge v_{qd}\ge0\) be the decreasing rearrangement, with multiplicity, of the products \(s_ic_j\). Then

\[
\boxed{\Lambda_k(N_m(T))=\{z\in\mathbb C:|z|\le v_k\},\quad 1\le k\le qd.}
\]

More generally, if \(h_1\ge\cdots\ge h_{md}\) is the ordered multiset \(\{s_i\cos(j\pi/(m+1)):1\le i\le d,\ 1\le j\le m\}\), then for **every** rank \(1\le k\le md\),

\[
\boxed{\Lambda_k(N_m(T))=\begin{cases}\{z:|z|\le h_k\},&h_k\ge0,\\\varnothing,&h_k<0.\end{cases}}
\]

Consequently, with \(m,d\) known and the first consecutive higher-rank numerical ranges observed exactly, the smallest universally sufficient number of ranks to recover **all** singular values of \(T\), including multiplicities and zeros, is precisely

\[
\boxed{K_{m,d}=(d-1)\lfloor m/2\rfloor+1.}
\]

No initial segment of fewer than \(K_{m,d}\) ranks distinguishes every singular-value multiset (interpreting an empty segment when \(d=1\) and \(K_{m,d}=1\)).

## Assumptions and scope

All spaces are complex, finite-dimensional Hilbert spaces with their standard inner products. The matrix \(T\) may be singular, zero, nonsymmetric or nonnormal. The path length \(m\ge2\) and block dimension \(d\ge1\) are known and fixed in the inverse question. A disk of radius zero means the singleton \(\{0\}\); an empty range means no rank-\(k\) scalar compression exists. Recovery uses exact set data, with no stability guarantee against noise. It identifies singular values, not singular vectors or the original matrix.

## Proof

**1. Singular-value splitting.** Take a singular-value decomposition \(T=U\operatorname{diag}(s_1,\ldots,s_d)V^*\). Conjugate \(N_m(T)\) by the block-diagonal unitary having vertex blocks \(U,V,U,V,\ldots\). Every odd superdiagonal edge becomes \(U^*TV=\operatorname{diag}(s_i)\); every even edge becomes \(V^*T^*U=\operatorname{diag}(s_i)\). Permuting coordinates by singular-vector index gives the exact unitary equivalence

\[
N_m(T)\ \simeq\ \bigoplus_{i=1}^d s_iJ_m,
\]

where \(J_m\) is the scalar nilpotent upper Jordan shift with unit superdiagonal. This is valid even for repeated or zero singular values.

**2. All compression disks.** For every real \(\theta\), a diagonal phase unitary conjugates \(e^{i\theta}J_m\) to \(J_m\); hence \(\operatorname{Re}(e^{i\theta}J_m)\) is unitarily equivalent to the real symmetric Jacobi matrix with off-diagonal entries \(1/2\). Its simple eigenvalues are \(\cos(j\pi/(m+1))\), \(1\le j\le m\), with sine eigenvectors. Therefore the ordered eigenvalues of \(\operatorname{Re}(e^{i\theta}N_m(T))\) are exactly \(h_1,\ldots,h_{md}\), independently of \(\theta\). The Li–Sze half-plane characterization asserts

\[
\Lambda_k(A)=\bigcap_{\theta\in\mathbb R}\{z\in\mathbb C:\operatorname{Re}(e^{i\theta}z)\le\lambda_k(\operatorname{Re}(e^{i\theta}A))\}.
\]

When \(h_k\ge0\) the intersection is the closed disk of radius \(h_k\); for \(h_k<0\), using opposite phases shows that it is empty. The first \(qd\) eigenvalues are exactly the \(qd\) nonnegative products \(s_ic_j\): in the presence of zero singular values, any additional zero eigenvalues have the same value and cause no ambiguity. This proves both disk formulas.

**3. Exact inverse from a short initial segment.** In each observed disk recover its radius, obtaining the first \(K=(d-1)q+1\) entries of the nonincreasing multiset of products \(s_ic_j\). The constants \(c_1>\cdots>c_q>0\) are known. Recover \(s_1=v_1/c_1\); delete, with multiplicity, from the observed list every occurrence arising from \(s_1c_j\) that is present. In decreasing order, the greatest undeleted observed entry is \(s_2c_1\), provided \(s_2>0\). Indeed, among all products of the first \(i-1\) singular values there are at most \((i-1)q\) products ahead of \(s_ic_1\); thus its position in the complete ordered product multiset is at most \((i-1)q+1\le K\). By induction this peeling step determines \(s_i\) for each \(1\le i\le d\). Equal products may be deleted using multiplicities, since only their values matter. If the greatest undeleted entry is zero, all remaining singular values are zero. This proves universal sufficiency.

**4. Sharpness of the measurement count.** If \(d\ge2\), choose distinct scalars \(0<t<t'<c_q/c_1\) and set

\[
T_t=\operatorname{diag}(\underbrace{1,\ldots,1}_{d-1},t),\qquad
T_{t'}=\operatorname{diag}(\underbrace{1,\ldots,1}_{d-1},t').
\]

In both cases the first \((d-1)q\) products are exactly the multiset consisting of each \(c_1,\ldots,c_q\) repeated \(d-1\) times, because \(t'c_1<c_q\). Their first \((d-1)q\) higher-rank numerical ranges therefore agree despite unequal smallest singular values. At rank \((d-1)q+1\), their radii differ. When \(d=1\), no rank data cannot determine the single singular value, while the first disk has radius \(c_1s_1\). The lower and upper bounds coincide in every case.

## Verification

A standalone Python-standard-library script, `verify.py`, performs finite exact-data recovery and sharpness tests for \(2\le m\le10\), \(1\le d\le6\), including repeated and zero singular values. It also tests a nontrivial complex singular-value decomposition for the alternating-edge unitary splitting. Execute `python verify.py` after extracting the file. These finite tests corroborate, but do not establish, the all-size theorem; the preceding argument is the proof.

## Relationship to prior work

Audeh, Kittaneh and Moradi [1, Corollary 2.1] gave the exact ordinary numerical radius \(\|T\|\cos(\pi/(m+1))\) of this same alternating-adjoint block path. That rank-one identity corresponds to the \(k=1\) case of the disk formula, but does not recover the other singular values or provide the sharp inverse cutoff. Gaaya [2, Theorems 2.1 and 2.3] computed higher-rank disks for one Jordan shift and an upper bound for general nilpotent contractions; distinct singular-value-scaled direct sums and minimum-rank recovery are not stated there. Gau and Wu [3, Theorem 1] showed that a sufficiently long initial chain of higher-rank ranges determines the Kippenhahn polynomial of an arbitrary matrix; its general cutoff \(\lfloor md/2\rfloor+1\) does not imply the shorter sharp cutoff above without the specific product-factorization and peeling argument. Argerami and Mustafa [4, Sections 3–4] analyze Jordan-like block families with a scalar summand, not the singular-value family and inverse problem here.

## Limitations

The result is restricted to finite-dimensional alternating-adjoint paths and exact rank-range measurements. It does not recover the singular directions, establish stability under perturbations, or assert an infinite-dimensional inverse theorem. Priority remains subject to unindexed equivalent presentations, especially possible specialized higher-rank numerical-range inverse results; the sources checked below do not certify absolute novelty. No independent audit has been performed.

## References

[1] W. Audeh, F. Kittaneh, H. R. Moradi, *Integral Representations and Sharp Numerical Radius Inequalities for Hilbert Space Operators*, arXiv:2610.15242v1 (first public 2026-10-11), https://arxiv.org/html/2610.15242v1.

[2] H. Gaaya, *On the higher rank numerical range of the shift operator*, arXiv:1004.3751v1 (2010), https://arxiv.org/html/1004.3751v1.

[3] H.-L. Gau and P. Y. Wu, *Higher-rank Numerical Ranges and Kippenhahn Polynomials*, arXiv:1208.1333v1 (2012), https://arxiv.org/html/1208.1333v1.

[4] M. Argerami and S. Mustafa, *Higher Rank Numerical Ranges of Jordan-Like Matrices*, arXiv:1908.05692v3 (2019), https://arxiv.org/abs/1908.05692.
