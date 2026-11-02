# Square-zero derivations of free class-two Lie algebras: a rank census and a modular threshold

## Finding

Let \(k=\mathbb F_q\) be any finite field, let \(n\ge3\), put \(V=k^n\), and let \(W=\bigwedge^2_kV\), of dimension \(N=\binom n2\). Equip \(L_n=V\oplus W\) with the alternating Lie bracket \([v+w,v'+w']=v\wedge v'\). A derivation here means an **ordinary** \(k\)-linear Lie derivation, with no specified restricted \(p\)-operation. We count operators \(D\in\operatorname{Der}_k(L_n)\) with \(D^2=0\) as linear maps.

Every derivation has a unique block form
\[
D=\begin{pmatrix}A&0\\B&\rho(A)\end{pmatrix},\qquad
\rho(A)(u\wedge v)=Au\wedge v+u\wedge Av,
\]
where \(A\in\operatorname{End}_k(V)\) and \(B\in\operatorname{Hom}_k(V,W)\).

For \(0\le r\le\lfloor n/2\rfloor\), define
\[
\rho_r=r(n-r-1),\qquad
E_{n,r}=rN+(n-2r)(N-\rho_r),
\]
and
\[
M_{n,r}(q)={n\brack r}_q{n-r\brack r}_q
\prod_{j=0}^{r-1}(q^r-q^j),
\]
with empty products equal to \(1\). The Gaussian coefficient \({a\brack b}_q\) is the number of \(b\)-dimensional subspaces of \(k^a\).

**Exact rank census.** The number of square-zero derivations for which the induced map on \(L_n/[L_n,L_n]\cong V\) has rank exactly \(r\) is
\[
\boxed{M_{n,r}(q)q^{E_{n,r}}}
\]
when \(q\) is even; when \(q\) is odd, this formula applies only for \(r=0,1\), and the number is zero for every \(r\ge2\). Thus the complete count is
\[
\boxed{Z_n(q)=\begin{cases}
\displaystyle\sum_{r=0}^{\lfloor n/2\rfloor}M_{n,r}(q)q^{E_{n,r}},&q\text{ even},\\[4pt]
\displaystyle q^{nN}+M_{n,1}(q)q^{E_{n,1}},&q\text{ odd}.
\end{cases}}
\]

**Modular threshold.** In odd characteristic every such derivation has induced rank at most \(1\), whereas in characteristic \(2\) every rank from \(0\) through \(\lfloor n/2\rfloor\) occurs. Hence an induced rank at least \(2\) is possible if and only if the characteristic is \(2\) and \(n\ge4\).

**Geometry.** For each admissible \(r\), the reduced locally closed rank-\(r\) stratum of square-zero derivations is smooth and geometrically irreducible. It is the total space of a vector bundle of rank \(E_{n,r}\) over the nilpotent matrix orbit of Jordan type \((2^r,1^{n-2r})\); its dimension is
\[
\boxed{2r(n-r)+E_{n,r}.}
\]
This is a statement about the reduced strata, not a claim that the entire square-zero equation scheme is reduced or irreducible.

For example, \(Z_3(2)=1184\), \(Z_3(3)=44955\), \(Z_3(4)=584704\), and \(Z_4(2)=19357696\). The last figure includes \(210\cdot2^{12}=860160\) derivations whose quotient map has rank \(2\); this branch does not exist in odd characteristic.

## Assumptions and scope

The field is finite of arbitrary prime-power cardinality, including extension fields and characteristic \(2\). The number \(n\) of free generators is at least \(3\). The Lie bracket is alternating and bilinear in all characteristics; the central exterior-square summand is the full derived ideal. The square-zero condition concerns composition of the underlying linear operator, not the bracket of derivations, a restricted derivation condition, or a nilpotency condition of unspecified index. Counts are of individual labeled \(k\)-linear derivation operators, not of conjugacy classes. The separately familiar rank-two Heisenberg case \(n=2\) is intentionally excluded from the new theorem.

## Proof

**1. Derivation normal form.** Since \([L_n,L_n]=W\), every derivation preserves \(W\) and induces an endomorphism \(A\) of \(V\). The derivation identity applied to \([u,v]=u\wedge v\) forces its action on \(W\) to be \(\rho(A)\), with no condition on the map \(B:V\to W\). Conversely, the displayed block map satisfies the derivation identity, because \(W\) is central. The uniqueness and all field characteristics follow without division.

**2. The quotient rank restriction.** Squaring the block matrix gives \(A^2=0\), \(\rho(A)^2=0\), and \(BA+\rho(A)B=0\). Directly,
\[
\rho(A)^2(u\wedge v)=A^2u\wedge v+2Au\wedge Av+u\wedge A^2v.
\]
When \(A^2=0\), this is \(2\bigwedge^2A\). Over odd characteristic its vanishing is equivalent to \(\operatorname{rank}A\le1\); over characteristic \(2\) it vanishes for every square-zero \(A\). In either case a square-zero \(A\) has rank \(r\le\lfloor n/2\rfloor\).

**3. Rank of the exterior-square differential.** For any square-zero \(A\) of rank \(r\), choose a basis \(x_1,\ldots,x_r,y_1,\ldots,y_r,z_1,\ldots,z_s\), where \(s=n-2r\), with \(Ay_i=x_i\) and \(Ax_i=Az_j=0\). The images of \(y_i\wedge z_j\) span an \(rs\)-dimensional space of \(x_i\wedge z_j\). The images of \(y_i\wedge y_j\) span a \(\binom r2\)-dimensional space in \(X\wedge Y\). The images of \(x_i\wedge y_j\) span \(\bigwedge^2X\), of dimension \(\binom r2\). These three image subspaces are independent, and all other exterior-basis images vanish. Therefore
\[
\operatorname{rank}\rho(A)=rs+2\binom r2=r(n-r-1)=\rho_r.
\]
This computation is valid in all characteristics.

**4. Exact lifting-fiber dimension.** Suppose \(A^2=\rho(A)^2=0\). The equation \(BA+\rho(A)B=0\) says \(Bx_i=-\rho(A)By_i\) for \(1\le i\le r\), and \(Bz_j\in\ker\rho(A)\) for \(1\le j\le s\). The remaining equations on \(x_i\) hold automatically because \(\rho(A)^2=0\). Thus the \(r\) vectors \(By_i\in W\) can be chosen freely and the \(s\) vectors \(Bz_j\) from an \((N-\rho_r)\)-dimensional kernel; the \(Bx_i\) are then forced. This gives exactly \(q^{rN+s(N-\rho_r)}=q^{E_{n,r}}\) lifts over each eligible \(A\).

**5. Count quotient operators.** A square-zero \(A\) of rank \(r\) is determined by a flag \(U=\operatorname{im}A\subseteq K=\ker A\), with dimensions \(r\) and \(n-r\), and an isomorphism \(V/K\xrightarrow{\sim}U\). Choosing \(U\), then \(K/U\), then the isomorphism gives precisely \(M_{n,r}(q)\). Summing the nonoverlapping rank strata completes the census and the modular threshold.

**6. Geometry.** For each \(r\), the square-zero quotient maps of rank \(r\) form the \(\operatorname{GL}(V)\)-orbit of the Jordan type \((2^r,1^{n-2r})\). Its centralizer is an open subset of a linear commutant, so the orbit is smooth and geometrically irreducible; its dimension is \(2r(n-r)\) by the centralizer/Jordan-block formula. The lifting equation is a constant-rank linear bundle map on this orbit, with kernel dimension \(E_{n,r}\). Its kernel is consequently a vector bundle. This proves the geometric assertion for reduced rank strata, without inferring scheme-theoretic reducedness of the full equation locus.

## Verification

The standalone `check_square_zero_derivations.py` implements finite-field addition and multiplication for \(\mathbb F_2\), \(\mathbb F_3\), and the genuine extension field \(\mathbb F_4\). It builds \(\rho(A)\) from its coefficient formula and independently row-reduces the linear equations \(BA+\rho(A)B=0\).

For \((n,q)=(2,2),(2,3),(2,4),(3,2),(3,3),(3,4),(4,2)\), it enumerates **every** quotient matrix \(A\) with \(A^2=0\) and checks the expected allowed ranks, exterior-map ranks and lifting-fiber dimensions. The \(n=2\) tests serve only as boundary controls, not originality claims. For \((2,2),(2,3),(3,2)\), it additionally exhaustively enumerates all lifting matrices \(B\) and directly evaluates the square-zero block equations. A rank-two example in dimension \(4\) separately checks both the characteristic-two branch and its failure in characteristic \(3\). The output is in `checker_output.txt` and terminates with `SQUARE_ZERO_FREE_TWO_STEP_DERIVATIONS_OK`. These finite tests do not constitute the proof for arbitrary \(n\) and \(q\).

To reproduce using Python 3, run `python3 check_square_zero_derivations.py` in a directory containing the standalone script; no third-party packages are needed.

## Relationship to prior work

Feldvoss–Siciliano–Weigel (2011), building on Tôgô's existence theorem, study the existence of outer **restricted** square-zero derivations. Their results do not count all ordinary square-zero derivations of the present free class-two family. Benito–de-la-Concepción (2014) and Benito–Roldán-López (2019) describe derivations and automorphisms of free nilpotent Lie algebras, supplying the general structural setting; their inspected derivation descriptions do not state this rank-stratified finite-field census or the characteristic-two quotient-rank threshold. La Rosa–Mancini (2023) analyze derivation algebras and almost-inner derivations for two-step nilpotent Leibniz families under characteristic different from two; that work neither supplies a characteristic-two count nor covers this all-rank free-family census.

A previously analyzed rank-two Heisenberg example yields \(q^3+q^2-q\) square-zero derivations and is not asserted to be new here. The closest separate results for the same free class-two family concern local derivations, rank-one Nijenhuis operators, and fixed-point-free automorphisms; none determines the square-zero ordinary-derivation census above. Non-identification of an equivalent published count is not a guarantee of historical priority.

## Limitations

The theorem counts ordinary derivations, not restricted derivations, conjugacy orbits or derivations of arbitrary nilpotent quotients. Its geometric assertion covers reduced locally closed rank strata only, not the possible nonreduced structure, number of global irreducible components, or singularities of the full equation scheme. The extension-field tests are finite checks; the full characteristic-free arithmetic conclusion rests on the proof. A broader preexisting enumeration of square-zero elements in derivation representations could imply this formula; such historical coverage remains a residual risk, and independent scientific validation has not been performed.

## References

1. J. Feldvoss, S. Siciliano, T. Weigel, *Outer restricted derivations of nilpotent restricted Lie algebras*, arXiv:1102.2629v1 (first posted 2011-02-13), https://arxiv.org/abs/1102.2629.
2. P. Benito, D. de-la-Concepción, *An overview of free nilpotent Lie algebras*, Commentationes Mathematicae Universitatis Carolinae **55** (2014), 325–339, https://dml.cz/handle/10338.dmlcz/143811.
3. P. Benito, J. Roldán-López, *Derivations and automorphisms of free nilpotent Lie algebras and their quotients*, arXiv:1911.01897v1 (2019-11-05), https://arxiv.org/abs/1911.01897.
4. G. La Rosa, M. Mancini, *Derivations of two-step nilpotent algebras*, Communications in Algebra **51** (2023), 4928–4948, https://doi.org/10.1080/00927872.2023.2222415.
