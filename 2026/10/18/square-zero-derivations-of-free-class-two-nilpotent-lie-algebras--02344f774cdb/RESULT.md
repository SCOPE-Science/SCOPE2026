# Square-zero derivations of free class-two nilpotent Lie algebras over finite fields

## Finding

For every prime power \(q\) and integer \(n\ge3\), define the free class-two nilpotent Lie algebra
\[
 L_n=V\oplus W,\qquad V=\mathbb F_q^n,\qquad W=\bigwedge^2V,\qquad [u,v]=u\wedge v.
\]
Write \(m=\binom n2\), and for integers \(0\le r\le\lfloor n/2\rfloor\) set
\[
 s_r=r(n-r-1),\qquad h_r=nm-ns_r-mr+2rs_r.
\]
The number of ordinary derivations \(D\in\operatorname{Der}_{\mathbb F_q}(L_n)\) with \(D^2=0\), **by the rank \(r\) of the induced map on \(L_n/[L_n,L_n]\)**, is
\[
 N_{n,r}(q)={n\brack r}_q{n-r\brack r}_q|\mathrm{GL}_r(\mathbb F_q)|\,q^{h_r}
\]
when the rank is permitted, and zero otherwise. The permitted ranks are all \(0\le r\le\lfloor n/2\rfloor\) in characteristic two, and only \(r=0,1\) in odd characteristic. The zero-rank summand is exactly \(q^{nm}\), accounting for all central-image derivations.

Consequently
\[
 N_n(q)=\sum_{r\in I_q(n)}{n\brack r}_q{n-r\brack r}_q|\mathrm{GL}_r(\mathbb F_q)|\,q^{nm-ns_r-mr+2rs_r},
\]
where \(I_q(n)\) is the permitted set of ranks above. Here \({a\brack b}_q\) counts \(b\)-dimensional subspaces of \(\mathbb F_q^a\), and \(|\mathrm{GL}_r(\mathbb F_q)|=\prod_{j=0}^{r-1}(q^r-q^j)\), including \(|\mathrm{GL}_0|=1\).

There is an asymptotic transition: among these square-zero derivations, the proportion inducing zero on \(L_n/[L_n,L_n]\) tends to \(1/2\) for \(n=3\), and tends to \(1\) for every fixed \(n\ge4\), as \(q\to\infty\) through prime powers. Both assertions hold in either characteristic regime. The counts and transition are characteristic-uniform except for the extra permitted ranks in characteristic two.

## Assumptions and scope

The Lie bracket is bilinear and alternating, including in characteristic two. The derivations are ordinary Lie derivations satisfying the Leibniz rule, not restricted derivations. The square-zero condition means equality of endomorphisms of the entire \(n+\binom n2\)-dimensional vector space, not merely of the abelianization. The theorem covers every prime power and all \(n\ge3\); no assumptions of algebraic closure are made. In particular, exterior powers and all Gaussian coefficients are taken over the field \(\mathbb F_q\). The formulas count actual labeled endomorphisms, not conjugacy classes.

## Proof

**Block form.** Every derivation preserves the derived ideal \(W=[L_n,L_n]\), which is central. Any linear maps \(A:V\to V\) and \(B:V\to W\) extend uniquely to a derivation, whose matrix relative to \(V\oplus W\) is
\[
 D=\begin{pmatrix}A&0\\ B&T_A\end{pmatrix},\qquad T_A(u\wedge v)=Au\wedge v+u\wedge Av.
\]
This follows directly by applying the derivation rule to \([u,v]=u\wedge v\); conversely these matrices all satisfy it, since \(W\) is central. Therefore
\[
 D^2=0\iff A^2=0,\quad T_A^2=0,\quad T_AB+BA=0.
\]

**Permitted ranks.** If \(A^2=0\) has rank \(r\), choose a basis \(e_1,\dots,e_r,f_1,\dots,f_r,g_1,\dots,g_{n-2r}\) with \(Ae_i=f_i\) and \(Af_i=Ag_j=0\). On decomposable wedges,
\[
 T_A^2(u\wedge v)=A^2u\wedge v+2Au\wedge Av+u\wedge A^2v=2Au\wedge Av.
\]
In characteristic two this vanishes for every square-zero \(A\). In odd characteristic it vanishes exactly when \(\operatorname{im}A\) has dimension at most one: if \(r\ge2\) then evaluating at \(e_1\wedge e_2\) gives the nonzero vector \(2f_1\wedge f_2\). Thus the rank sets are exactly as stated.

**Rank of the induced action.** For each \(g_j\), the independent vectors \(T_A(e_i\wedge g_j)=f_i\wedge g_j\) contribute \(r(n-2r)\) to the image rank. For each pair \(i<j\le r\), the images of wedges involving the corresponding two length-two Jordan chains span precisely
\[
 \langle f_i\wedge e_j+e_i\wedge f_j,\; f_i\wedge f_j\rangle,
\]
a two-dimensional space, and different pairs lie in disjoint exterior-basis supports. Wedges involving only kernel generators contribute no additional image. Hence
\[
 \operatorname{rank}T_A=r(n-2r)+2\binom r2=r(n-r-1)=s_r.
\]
For permitted ranks \(T_A^2=0\), so \(W\) is a module for the dual-number algebra \(R=\mathbb F_q[\varepsilon]/(\varepsilon^2)\) with \(s_r\) Jordan blocks of length two and \(m-2s_r\) blocks of length one.

**The free central block.** The remaining equation \(T_AB+BA=0\) states that \(B\) is an \(R\)-module homomorphism from \((V,-A)\) to \((W,T_A)\). Since \((-A)^2=0\) and \(-A\) is similar to \(A\), its dual-number module is \(R^r\oplus (R/\varepsilon)^{n-2r}\). Likewise \(W\cong R^{s_r}\oplus (R/\varepsilon)^{m-2s_r}\). The four blockwise homomorphism spaces have dimensions
\[
 2rs_r,\quad r(m-2s_r),\quad (n-2r)s_r,\quad (n-2r)(m-2s_r).
\]
Their sum is exactly \(h_r=nm-ns_r-mr+2rs_r\). There are therefore \(q^{h_r}\) choices for \(B\) for each admissible \(A\).

**Counting \(A\).** A square-zero \(A\) of rank \(r\) is specified by \(U=\operatorname{im}A\), a subspace \(K=\ker A\) of dimension \(n-r\) containing \(U\), and an isomorphism \(V/K\to U\). The three numbers of choices are \({n\brack r}_q\), \({n-r\brack r}_q\), and \(|\mathrm{GL}_r(\mathbb F_q)|\). Multiplication by the count for \(B\), followed by summation over permitted \(r\), proves the exact statements.

**Asymptotic transition.** The rank-\(r\) count for \(A\) is monic of degree \(2r(n-r)\) as a polynomial in \(q\). Relative to the exponent \(nm\) of the zero-rank term, the leading-degree difference of the rank-\(r\) summand is
\[
 \Delta_{n,r}=r\bigl(2(n-r)-m-(n-2r)(n-r-1)\bigr).
\]
For \(n=3\), only \(r=1\) is nonzero and \(\Delta_{3,1}=0\); both allowed summands have leading coefficient one, giving limiting zero-rank proportion \(1/2\). For \(n\ge4\), \(m=\binom n2\ge2(n-1)\), \(2(n-r)\le2(n-1)\), and \((n-2r)(n-r-1)\ge0\). At least one inequality is strict whenever \(r\ge1\), so \(\Delta_{n,r}<0\). The zero-rank summand then dominates, giving limit one in every characteristic.

## Verification

The standalone `verify.py` independently constructs induced exterior-square matrices, computes ranks of the linear equations for \(B\), exhaustively enumerates square-zero \(A\) over prime fields, and compares with the algebraic formulas. It returns `VERIFY_OK` after asserting every checked identity. Actual reproducible examples include
\[
 N_3(2)=1184,\qquad N_3(3)=44955,\qquad N_4(2)=19357696.
\]
The \(n=4,q=2\) check enumerates all \(2^{16}=65536\) four-by-four matrices \(A\), rejects nonsquare-zero matrices, and computes the \(B\)-fiber dimensions from independent Gaussian elimination; it does **not** enumerate all \(B\), because each fiber size follows exactly from its checked linear kernel dimension. Smaller \(n=2\) tests act only as sanity checks of the method and are not part of the claimed novelty.

## Relationship to prior work

The structural fact that derivations of a free nilpotent Lie algebra extend arbitrary maps on its generators is developed by Benito and Roldán-López, *Derivations and automorphisms of free nilpotent Lie algebras and their quotients* (arXiv:1911.01897, Proposition 1 and Corollary 1). That treatment assumes characteristic zero and does not provide square-zero counts, their abelianization-rank distribution, or the characteristic-two distinction. Drensky and Fındık (arXiv:1003.0350) analyze automorphism groups of free metabelian nilpotent Lie algebras in characteristic zero, rather than this derivation locus. La Rosa and Mancini (arXiv:2301.11058) study derivations of specific two-step Heisenberg and Leibniz families and assume characteristic different from two; their one-dimensional commutator spaces differ from \(\dim[L_n,L_n]=\binom n2\) here. General Gaussian-subspace and dual-number-module enumeration methods underlie the proof; those standard inputs are not asserted as new.

## Limitations

The result counts square-zero derivations, not all nilpotent derivations, orbit classes, or finite-field group-scheme geometry. It does not classify conjugacy orbits under Lie automorphisms. The method does not by itself generalize to nilpotency indices greater than two. The computation is an auxiliary finite check and is not a proof for arbitrary \(n\) or \(q\); arbitrary-parameter validity rests on the algebraic argument above. The scholarly comparisons identify no dominating general point-count theorem in the inspected sources, but literature completeness cannot be certified; a specialized enumeration of nilpotent derivation varieties remains a residual priority for independent verification.

## References

1. V. Drensky and Ş. Fındık, *Inner and Outer Automorphisms of Free Metabelian Nilpotent Lie Algebras*, arXiv:1003.0350v1, 1 March 2010; https://arxiv.org/abs/1003.0350.
2. P. Benito and J. Roldán-López, *Derivations and Automorphisms of Free Nilpotent Lie Algebras and Their Quotients*, arXiv:1911.01897v2, Proposition 1 and Corollary 1; https://arxiv.org/html/1911.01897v2.
3. G. La Rosa and M. Mancini, *Derivations of Two-Step Nilpotent Algebras*, arXiv:2301.11058v3, especially Sections 1–2; https://arxiv.org/html/2301.11058v3.
