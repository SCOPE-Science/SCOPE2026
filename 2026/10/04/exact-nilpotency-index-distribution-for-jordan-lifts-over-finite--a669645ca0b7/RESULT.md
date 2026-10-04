# Exact nilpotency-index distribution for Jordan lifts over finite dual numbers
## Finding
Let \(q\) be a prime power and
\[
R_q=\mathbb F_q[\varepsilon]/(\varepsilon^2).
\]
Let \(J_n\in M_n(\mathbb F_q)\) be the nilpotent Jordan block with ones on the superdiagonal. For every \(B\in M_n(\mathbb F_q)\), put
\[
N_B=J_n+\varepsilon B\in M_n(R_q).
\]
Then the nilpotency index of \(N_B\) is always one of \(n,n+1,\ldots,2n\), and its complete distribution as \(B\) varies is
\[
\#\{B:\operatorname{ind}(N_B)=n\}=q^{n^2-n},
\]
and, for every \(1\le j\le n\),
\[
\#\{B:\operatorname{ind}(N_B)=n+j\}=(q-1)q^{n^2-n+j-1}.
\]
In particular, exactly \((q-1)q^{n^2-1}\) lifts have the maximal possible index \(2n\), so a uniformly random dual part attains the doubled index with probability \(1-q^{-1}\).

## Assumptions and scope
The statement is for the finite dual-number ring \(R_q\) over an arbitrary finite field \(\mathbb F_q\). No restriction on the characteristic is needed. The Jordan block convention is
\[
J_ne_i=e_{i-1}\quad(2\le i\le n),\qquad J_ne_1=0,
\]
which corresponds to ones on the superdiagonal in the standard matrix convention. The nilpotency index is the least positive \(m\) for which \(N_B^m=0\).

The result refines the qualitative fact that a dual matrix is nilpotent exactly when its real part is nilpotent, and it gives the full index distribution in the canonical one-block fiber over \(J_n\).

## Proof
For every integer \(m\ge1\), the square-zero relation \(\varepsilon^2=0\) gives
\[
N_B^m=J_n^m+\varepsilon\sum_{i=0}^{m-1}J_n^i B J_n^{m-1-i}.
\]
Since \(J_n^n=0\), define
\[
S(B)=\sum_{i=0}^{n-1}J_n^i B J_n^{n-1-i}.
\]
Then
\[
N_B^n=\varepsilon S(B),
\]
and for every \(j\ge0\),
\[
N_B^{n+j}=\varepsilon S(B)J_n^j.
\]
The matrix \(S(B)\) commutes with \(J_n\), because
\[
J_nS(B)-S(B)J_n=J_n^nB-BJ_n^n=0.
\]
The centralizer of a single Jordan block consists of the upper-triangular Toeplitz matrices, so there are unique coefficients \(c_0,\ldots,c_{n-1}\in\mathbb F_q\) such that
\[
S(B)=c_0I+c_1J_n+\cdots+c_{n-1}J_n^{n-1}.
\]
The linear map
\[
\Phi:M_n(\mathbb F_q)\longrightarrow\mathbb F_q[J_n],\qquad B\longmapsto S(B),
\]
is surjective. Indeed, if \(E_{ab}\) denotes the matrix unit, then for \(0\le k\le n-1\), choosing \(B=E_{n,k+1}\) gives
\[
S(B)=J_n^k.
\]
Hence \(\Phi\) has rank \(n\), and every coefficient vector \((c_0,\ldots,c_{n-1})\) has exactly \(q^{n^2-n}\) preimages.

If all \(c_k\) vanish, then \(N_B^n=0\), while the real part of \(N_B^{n-1}\) is \(J_n^{n-1}\ne0\). Thus the index is exactly \(n\), giving \(q^{n^2-n}\) such lifts.

Otherwise let \(d\) be the least index with \(c_d\ne0\). Then
\[
S(B)J_n^j=c_dJ_n^{d+j}+c_{d+1}J_n^{d+1+j}+\cdots,
\]
which is nonzero exactly for \(0\le j\le n-1-d\), and vanishes at \(j=n-d\). Therefore
\[
\operatorname{ind}(N_B)=2n-d.
\]
For fixed \(d\), the number of coefficient vectors whose first nonzero coordinate is \(c_d\) equals
\[
(q-1)q^{n-1-d}.
\]
Multiplying by the common fiber size \(q^{n^2-n}\) yields
\[
(q-1)q^{n^2-d-1}.
\]
Writing \(j=n-d\) gives the asserted count \((q-1)q^{n^2-n+j-1}\) for index \(n+j\). Summing the counts gives \(q^{n^2}\), as required.

## Verification
A standalone verifier exhaustively enumerates all dual parts in four small cases and computes powers directly in the dual matrix ring. It reproduces the predicted distributions:

- \(n=1,q=2\): counts \(1,1\) at indices \(1,2\);
- \(n=2,q=2\): counts \(4,4,8\) at indices \(2,3,4\);
- \(n=3,q=2\): counts \(64,64,128,256\) at indices \(3,4,5,6\);
- \(n=2,q=3\): counts \(9,18,54\) at indices \(2,3,4\).

These finite checks are only sanity tests. The theorem is proved symbolically for every prime power \(q\) and every \(n\ge1\).

## Relationship to prior work
Özbay's February 2026 conference abstract on algebraic properties of dual matrices states that nilpotency is determined by the real part and that the dual part can increase the nilpotency index. The accessible abstract does not give an exact index criterion or a finite-field distribution.

Şentürk and Özbay subsequently proved in arXiv:2609.29468v1 that a real dual matrix \(A+\varepsilon B\) is nilpotent exactly when \(A\) is nilpotent. Their Theorem 2.5 shows, when \(A\) has index \(k\), that the \(2k\)-th power vanishes by the square-zero expansion. The theorem above sharpens that bound in the canonical one-Jordan-block fiber and, over finite fields, determines every possible lifted index and its exact multiplicity.

Targeted searches of the published-result database and the public mathematical literature did not locate the same all-index distribution for \(J_n+\varepsilon B\). The closest database hits concerned Jordan phenomena or nilpotency in different operator-theoretic settings and do not imply this finite dual-matrix count.

## Limitations
The exact distribution is proved here only for a single nilpotent Jordan block as the real part; a general nilpotent real part with several Jordan blocks may have a more intricate distribution. The structural power expansion is field-independent, but the counting formula uses finiteness of \(\mathbb F_q\). The February 2026 conference presentation itself was not available for full-text inspection; its abstract explicitly mentions nilpotency-index growth, so there is residual originality risk if the unavailable presentation contained a stronger formula than the abstract records.

## References
1. Neslihan Ayşen Özbay, *On the Algebraic Properties of Matrices over Dual Numbers*, in *2nd International Congress on Natural Sciences and Applied Mathematics Abstracts Book*, p. 52, DOI 10.5281/zenodo.18640991, published 2026-02-14.
2. Berrin Şentürk and Neslihan Ayşen Özbay, *On the Regularity and Clean Properties of Matrices over Dual Numbers*, arXiv:2609.29468v1, submitted 2026-09-24.
