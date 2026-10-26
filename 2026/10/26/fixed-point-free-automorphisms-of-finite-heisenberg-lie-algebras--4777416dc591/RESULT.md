# Fixed-point-free automorphisms of finite Heisenberg Lie algebras

## Finding
Let \(q\) be any prime power and let \(n\ge1\). Let \(V\) be a \(2n\)-dimensional vector space over \(\mathbb F_q\) with a nondegenerate alternating form \(\omega\), and define the Heisenberg Lie algebra
\[
\mathfrak h_{2n+1}(q)=V\oplus \mathbb F_q z,\qquad [v,w]=\omega(v,w)z,\quad [z,\mathfrak h_{2n+1}(q)]=0.
\]
Write \(F_n(q)\) for the number of \(\mathbb F_q\)-linear Lie algebra automorphisms with no nonzero fixed vector. Then
\[
\boxed{F_n(q)=q^{n^2+2n}(q-2)\left(\prod_{j=1}^{n}(q^{2j}-1)\right)\left(\sum_{r=0}^{n}\frac{(-1)^r}{\prod_{k=1}^{r}(q^k-1)}\right),}
\]
where an empty product equals \(1\). In particular, \(F_n(2)=0\). The proportion among all automorphisms is
\[
\boxed{\frac{F_n(q)}{|\operatorname{Aut}(\mathfrak h_{2n+1}(q))|}=\frac{q-2}{q-1}\sum_{r=0}^{n}\frac{(-1)^r}{\prod_{k=1}^{r}(q^k-1)}.}
\]
For each fixed \(q\), this proportion converges as \(n\to\infty\) to
\[
\frac{q-2}{q-1}\prod_{k=1}^{\infty}(1-q^{-k}).
\]
At \(n=1\), the count reduces to \(q^3(q+1)(q-2)^2\).

## Assumptions and scope
The field is finite with cardinality \(q\); no restriction is placed on its characteristic. The Lie algebra is the two-step Heisenberg algebra defined above, not a finite Heisenberg group. “Fixed-point-free” means that the only vector fixed by the linear automorphism is \(0\); it does not mean that the induced projective transformation has no invariant line. The formula counts automorphisms themselves, not conjugacy classes.

## Proof
Let \(Z=\mathbb F_qz\). Since \(Z=[\mathfrak h,\mathfrak h]\), every automorphism has the form
\[
\phi(v+tz)=g(v)+(\ell(v)+ct)z,
\]
where \(\ell\in V^*\), \(c\in\mathbb F_q^\times\), and \(g\in\operatorname{GL}(V)\) satisfies \(\omega(gv,gw)=c\omega(v,w)\). Thus \(g\in\operatorname{GSp}_{2n}(q)\) has multiplier \(c\), and every such pair \((g,c)\) admits exactly \(q^{2n}\) choices of \(\ell\). Also
\[
|\operatorname{Aut}(\mathfrak h_{2n+1}(q))|=q^{2n}(q-1)|\operatorname{Sp}_{2n}(q)|.
\]
The fixed-vector equations are \((g-I)v=0\) and \(\ell(v)+(c-1)t=0\). If \(c=1\), then \(z\) is fixed. If \(c\ne1\) and \(g\) has a nonzero fixed vector \(v\), a unique \(t\) makes \(v+tz\) fixed. Conversely, if \(c\ne1\) and \(g-I\) is invertible, the only fixed vector is zero. Hence \(\phi\) is fixed-point-free exactly when \(c\ne1\) and \(g-I\) is invertible.

Fix \(c\ne1\). If \(g\) has multiplier \(c\) and fixes a subspace \(U\) pointwise, then \(U\) is totally isotropic: for \(u,v\in U\), \(\omega(u,v)=\omega(gu,gv)=c\omega(u,v)\), so \(\omega(u,v)=0\). Let
\[
I_{n,r}=\prod_{i=0}^{r-1}\frac{q^{2(n-i)}-1}{q^{r-i}-1}
\]
be the number of totally isotropic \(r\)-subspaces of a \(2n\)-dimensional symplectic space. For a fixed such subspace \(U\), the number of similitudes with multiplier \(c\) that fix every vector of \(U\) is
\[
C_{n,r}=q^{r(2n-r)-\binom r2}|\operatorname{Sp}_{2(n-r)}(q)|.
\]
To count this pointwise parabolic stabilizer, choose a symplectic basis adapted to \(U\). Its unipotent block data consist of an arbitrary \(r\times 2(n-r)\) block and a symmetric \(r\times r\) block, giving \(2r(n-r)+r(r+1)/2=r(2n-r)-\binom r2\) free field entries. The induced similitude on \(U^\perp/U\) has fixed multiplier \(c\); each such multiplier fibre has \(|\operatorname{Sp}_{2(n-r)}(q)|\) elements. Thus \(C_{n,r}=q^{r(2n-r)-\binom r2}|\operatorname{Sp}_{2(n-r)}(q)|\), also when \(r=n\), where the symmetric block alone contributes \(q^{n(n+1)/2}\).

Apply Möbius inversion in the lattice of subspaces. Its Möbius value at an \(r\)-dimensional subspace is \((-1)^rq^{\binom r2}\). Since the fixed space of a multiplier-\(c\ne1\) similitude is isotropic, the number \(N_n(q)\) of such similitudes with no nonzero fixed vector is
\[
N_n(q)=\sum_{r=0}^{n}(-1)^r q^{\binom r2}I_{n,r}C_{n,r}
=\sum_{r=0}^{n}(-1)^r I_{n,r}q^{r(2n-r)}|\operatorname{Sp}_{2(n-r)}(q)|.
\]
The expression is independent of the particular \(c\ne1\). Using
\[
|\operatorname{Sp}_{2m}(q)|=q^{m^2}\prod_{j=1}^{m}(q^{2j}-1)
\]
and the displayed product for \(I_{n,r}\), each summand simplifies to
\[
q^{n^2}\frac{\prod_{j=1}^{n}(q^{2j}-1)}{\prod_{k=1}^{r}(q^k-1)}.
\]
There are \(q-2\) choices of multiplier different from \(1\), and each contributes \(q^{2n}\) central shears. This proves the formula for \(F_n(q)\). Dividing by the automorphism-group order gives the proportion formula. Finally, the Euler \(q\)-binomial identity gives
\[
\sum_{r=0}^{\infty}\frac{(-1)^r}{\prod_{k=1}^{r}(q^k-1)}=\prod_{k=1}^{\infty}(1-q^{-k}),
\]
with absolute convergence, proving the limit.

## Verification
The proof reduces the count to the subspace-lattice Möbius function, the number of isotropic subspaces, and the pointwise parabolic stabilizer order. The bundled standard-library verifier independently enumerates all \(2\times2\) similitudes over prime fields \(\mathbb F_2,\mathbb F_3,\mathbb F_5\), and the multiplier-\(2\) coset in \(\operatorname{GSp}_4(3)\) by enumerating symplectic bases. It checks the resulting counts against the formula. These finite checks corroborate the group-counting proof; they are not the proof of the all-\(n\), all-prime-power statement.

## Relationship to prior work
Neumann and Praeger studied eigenvalue-free elements in finite classical groups and their derangement applications. Fulman and Guralnick later established uniform and asymptotic results for derangements in subspace actions, including cosets of classical groups. Fisher, Gray, and Hydon tabulated automorphisms of real Lie algebras of dimension at most five. These works supply nearby group-theoretic and automorphism context, but the statements inspected do not give the exact fixed-vector-free automorphism count for \(\mathfrak h_{2n+1}(q)\) for arbitrary \(n\) and \(q\). A separate published mathematical record gives the \(n=1\) case; the formula here extends the count to every higher Heisenberg dimension and yields its limiting proportion. The inaccessible full text of the 1998 eigenvalue-free-elements paper remains a bibliographic risk, recorded in the review.

## Limitations
The proof assumes the standard symplectic form is nondegenerate and uses the finite-field parabolic stabilizer order. The closed expression is a finite sum; no claim is made that the sum has a simpler product form for each finite \(n\). The asymptotic statement fixes \(q\) and lets \(n\) grow. Independent mathematical and priority audits have not been performed.

## References
1. P. M. Neumann and C. E. Praeger, “Derangements and Eigenvalue-Free Elements in Finite Classical Groups,” *Journal of the London Mathematical Society* 58 (1998), 564–586. DOI: 10.1112/S0024610798006772. First public date used here: 1998-12-01.
2. J. Fulman and R. Guralnick, “Derangements in Subspace Actions of Finite Classical Groups,” arXiv:1303.5480 (2013).
3. D. J. Fisher, R. J. Gray, and P. E. Hydon, “Automorphisms of Real Lie Algebras of Dimension Five or Less,” *Journal of Physics A: Mathematical and Theoretical* 46 (2013), 225204. DOI: 10.1088/1751-8113/46/22/225204.
