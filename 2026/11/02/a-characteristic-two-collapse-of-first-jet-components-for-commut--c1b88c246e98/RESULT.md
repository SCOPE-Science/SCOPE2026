# A characteristic-two collapse of first-jet components for commuting square-zero matrices

## Finding

Let \(k\) be any field and \(m\geq1\). Define \(\mathscr S_m\) to be the **scheme** of ordered \(m\)-tuples of \(2\times2\) matrices with equations \(A_i^2=0\) and \([A_i,A_j]=0\) for all distinct indices. We retain its defining equation scheme, rather than replacing it by its reduction. Its first jet scheme \(J_1(\mathscr S_m)\) parametrizes tuples
\[
 X_i=A_i+\varepsilon B_i\in M_2(k[\varepsilon]/(\varepsilon^2))
\]
with \(X_i^2=0\) and pairwise commutation. Let \(\mathscr Y_m=(J_1(\mathscr S_m))_{\mathrm{red}}\).

**Component classification.** Every geometrically irreducible component of \(\mathscr Y_m\) is defined over \(k\). If \(\operatorname{char}k\ne2\), there are exactly \(2^m\) components: the affine \(4m\)-space \(Z_0=\{A_1=\cdots=A_m=0\}\), and one component \(Z_S\) for every nonempty support \(S\subseteq\{1,\ldots,m\}\). Each \(Z_S\) has dimension \(2m+2\). If \(\operatorname{char}k=2\), there are exactly two components, \(Z_0\) of dimension \(4m\) and a second component of dimension \(3m+1\). Hence \(\mathscr Y_m\) is equidimensional precisely for \(m=1\), in either characteristic.

**Exact counts.** For \(k=\mathbb F_q\), write \(N_m(q)=\#\mathscr Y_m(\mathbb F_q)\). Then for all \(m\geq1\),
\[
\boxed{N_m(q)=\begin{cases}
 q^{4m}+(q+1)q^{m+1}\big((2q-1)^m-q^m\big),&q\text{ odd},\\
 q^{4m}+(q+1)(q^m-1)q^{2m},&q\text{ even}.
\end{cases}}
\]
In particular \(N_1(q)=2q^4-q^2\) in both characteristics, but the geometric component count jumps from \(2^m\) to \(2\) in characteristic two for \(m\ge2\).

The result also determines the Grothendieck class. Writing \(\mathbb L=[\mathbb A_k^1]\),
\[
 [\mathscr Y_m]=\begin{cases}
 \mathbb L^{4m}+(\mathbb L+1)\displaystyle\sum_{r=1}^m\binom mr(\mathbb L-1)^r\mathbb L^{2m-r+1},&\operatorname{char}k\ne2,\\
 \mathbb L^{4m}+(\mathbb L+1)(\mathbb L^m-1)\mathbb L^{2m},&\operatorname{char}k=2.
 \end{cases}
\]
These formulas hold in the Grothendieck ring of reduced \(k\)-varieties; they assert neither reducedness nor complete-intersection properties of the **unreduced** jet scheme.

## Assumptions and scope

All fields, including nonperfect fields and characteristic two, are permitted. The matrices are labeled, not classified modulo simultaneous conjugation. The first jets concern the defining square-zero **equations**, not the reduced nilpotent cone: changing the scheme before taking jets changes the answer. This distinction is essential already for one matrix.

Set \(R=k[\varepsilon]/(\varepsilon^2)\). Matrix multiplication gives the exact coefficient conditions
\[
 A_i^2=0,\qquad A_iB_i+B_iA_i=0,\qquad
 [A_i,A_j]=0,\qquad [A_i,B_j]+[B_i,A_j]=0.
\]
There is no condition on \(B_i^2\), because \(\varepsilon^2=0\). The two elementary linear equations involving \(B\) are the full infinitesimal lifting conditions.

## Proof

**Step 1: nonzero constant terms share a nilpotent line.** Every nonzero square-zero \(2\times2\) matrix over a field has rank one. Its centralizer is \(kI+kA\). A square-zero matrix in that centralizer must be a scalar multiple of \(A\) (also in characteristic two, since a scalar \(cI+dA\) has square with scalar part \(c^2I\)). Thus either all \(A_i=0\), or there is a unique projective line \(L=kN\) of nonzero nilpotent matrices and scalars \(t_i\) with \(A_i=t_iN\) and not all \(t_i\) zero. The projective variety of such nilpotent lines is the split smooth conic \(\mathscr Q\simeq\mathbb P_k^1\), since a nonzero nilpotent matrix has equal image and kernel, a line in \(k^2\).

**Step 2: solve all linearized equations.** After a change of basis take
\[
N=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad
B_i=\begin{pmatrix}a_i&b_i\\c_i&d_i\end{pmatrix}.
\]
Then
\[
NB_i+B_iN=\begin{pmatrix}c_i&a_i+d_i\\0&c_i\end{pmatrix},\qquad
[N,B_i]=\begin{pmatrix}c_i&d_i-a_i\\0&-c_i\end{pmatrix}.
\]
Let \(S=\{i:t_i\ne0\}\), with \(r=|S|>0\).

In characteristic different from two, for \(i\in S\) one has \(c_i=0\) and \(d_i=-a_i\); for \(j\notin S\), commutation with an active constant term forces \(c_j=0\) and \(d_j=a_j\). Comparing two active indices yields \(t_ia_j=t_ja_i\) for \(i,j\in S\). The complete normal form is therefore
\[
 B_i=\begin{cases}
 t_i u\begin{pmatrix}1&0\\0&-1\end{pmatrix}+b_iN,&i\in S,\\
 a_iI+b_iN,&i\notin S,
 \end{cases}
\]
with independent parameters \(u\), all \(b_i\), and the \(a_j\) for \(j\notin S\). Thus the infinitesimal fiber is an affine space of dimension \(2m-r+1\).

In characteristic two, the equations \(NB_i+B_iN=0\) and \([N,B_i]=0\) agree. One active index forces every \(B_j\) into \(kI+kN\), and this condition is also sufficient. The infinitesimal fiber is an affine \(2m\)-space, independent of \(S\).

**Step 3: geometry of the strata and components.** For fixed nonempty support \(S\), the constant terms form a Zariski-locally trivial \((\mathbb G_m)^r\)-bundle over \(\mathscr Q\simeq\mathbb P^1\). Step 2 gives Zariski-locally trivial affine-bundle fibers of respective ranks \(2m-r+1\) and \(2m\). Hence the stratum \(U_S\) is geometrically irreducible, of dimension \(2m+2\) in odd characteristic, or \(2m+r+1\) in characteristic two. The zero-constant-term locus \(Z_0\) is \(\mathbb A^{4m}\), since all \(B_i\) are then unrestricted.

In odd characteristic the closure \(Z_S=\overline{U_S}\) is a component for every nonempty \(S\). Indeed, \(A_i=0\) identically on \(Z_T\) for \(i\notin T\). If \(S\subsetneq T\), every \(B_j\) for \(j\in T\) is traceless throughout \(Z_T\), whereas \(U_S\) permits \(B_j=I\) for \(j\in T\setminus S\). Since \(\operatorname{tr}I=2\ne0\), neither stratum closure contains the other. The same trace witness shows that \(Z_0\) is not contained in any \(Z_S\), while \(Z_S\not\subseteq Z_0\) because some \(A_i\) is generically nonzero. These finitely many irreducible closed sets cover \(\mathscr Y_m\), proving there are exactly \(1+(2^m-1)=2^m\) components.

In characteristic two consider the incidence variety over the proper curve \(\mathscr Q\) whose fiber over \(L=kN\) consists of all \(A_i\in L\) and \(B_i\in kI+kN\). This is an affine-vector bundle of rank \(3m\) and thus irreducible of dimension \(3m+1\). Its projection to \(\mathscr Y_m\) has closed image (properness of \(\mathscr Q\)), and is generically injective because any nonzero constant term determines \(L\). All points with some \(A_i\ne0\) belong to this image and are dense there, so it is their single irreducible closure. This closed image does not contain the entire \(Z_0\): choose \(A_i=0\), \(B_1=\operatorname{diag}(0,1)\) and all other \(B_i=0\). No nonzero square-zero matrix can centralize \(B_1\), whose centralizer is diagonal. Consequently the image and \(Z_0\) are the two components. The displayed dimensions give equidimensionality exactly when \(m=1\).

**Step 4: point counts and motivic class.** Over \(\mathbb F_q\), the nilpotent-line conic has \(q+1\) points. For a chosen support \(S\) of size \(r\), each \(A_i\) with \(i\in S\) has \(q-1\) possible nonzero values on its line; the \(B\)-fiber has \(q^{2m-r+1}\) elements in odd characteristic, or \(q^{2m}\) elements in characteristic two. Add the \(q^{4m}\) zero-base points and sum over supports. The binomial theorem gives the two boxed formulas. Replacing \(q\), \(q+1\), \(q-1\) by their respective Zariski-locally trivial variety classes gives the displayed Grothendieck identities. No interpolation or finite extrapolation enters the proof.

## Verification

Run `python3 checker.py` with the Python standard library. The checker builds matrices and their products over prime fields and over the genuine degree-two field of four elements, solves the original coefficient equations by independent finite-field Gaussian elimination, and compares fiber sizes with the theorem across 15 configurations. It also directly exhausts the complete dual-number matrix space for \((q,m)=(2,2)\) and \((3,1)\). Expected final output:

`DUAL_JETS_COMMUTING_SQUARE_ZERO_OK 15 RANK_CASES 2 BRUTE_CASES`

The actual reproducible run output is embedded as `checker_output.txt`; finite tests provide corroboration, not a proof for arbitrary fields and arities.

## Relationship to prior work

Sethuraman and Šivic, arXiv:0902.3467 (first public version 2009-02-19), study jets of **unrestricted commuting-pair schemes** and prove the order-one and higher commuting \(2\times2\) pair jets irreducible. Their conclusion does not imply irreducibility after imposing the square-zero equations: the latter give a different, nonreduced representation scheme.

Ngo and Šivic, arXiv:1308.4438 (2013-08-20), study the **ordinary reduced varieties** of commuting nilpotent matrices over fields. These control the constant-term geometry but not the jets of the specific square-zero equation scheme. Moreau and Yu, arXiv:1411.6427 (2014-11-24), discuss jets of **reduced nilpotent orbit closures**; those have different defining ideals. For example, in odd characteristic \(A=0,B=I\) yields the square-zero dual-number matrix \(\varepsilon I\), which is not a first jet of the reduced nilpotent cone because its infinitesimal trace is nonzero.

The general representation-scheme framework, including the scheme defined by a single matrix square-zero equation, appears in D'Alesio, *Derived representation schemes and Nakajima quiver varieties* (2021). The cited work does not calculate the component count or complete point census of the present all-arity first-jet family. The claimed novelty is the explicit support-indexed geometric classification, sharp characteristic-two collapse and uniform finite-field/motivic formulas, not the general definition of jets, basic centralizer facts or base-field nilpotent commuting irreducibility.

## Limitations

The theorem is specifically for size-two matrices and the **first** jet of the original equation scheme. It does not determine higher-order jets, larger matrix sizes, full nonreduced jet-scheme structure, intersection multiplicities, simultaneous-conjugacy orbits, or the analogous jets after first reducing the base scheme. The literature checks do not prove global historical priority; a more general inaccessible source might subsume the calculation. Independent mathematical audit has not been performed.

## References

1. B. A. Sethuraman and K. Šivic, *Jet Schemes of the Commuting Matrix Pairs Scheme*, arXiv:0902.3467v1 (2009-02-19), https://arxiv.org/html/0902.3467v1.
2. N. V. Ngo and K. Šivic, *On varieties of commuting nilpotent matrices*, arXiv:1308.4438v1 (2013-08-20), https://arxiv.org/abs/1308.4438.
3. A. Moreau and R. W. T. Yu, *Jet schemes of the closure of nilpotent orbits*, arXiv:1411.6427v1 (2014-11-24), https://arxiv.org/html/1411.6427v3.
4. S. D'Alesio, *Derived representation schemes and Nakajima quiver varieties*, Selecta Mathematica 28 (2022), article 20, first online 2021-12-22, https://doi.org/10.1007/s00029-021-00724-4.
