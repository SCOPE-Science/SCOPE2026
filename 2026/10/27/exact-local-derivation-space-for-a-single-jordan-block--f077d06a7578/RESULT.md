# Exact local-derivation space for a single Jordan block

## Finding

Let \(K\) be a field of characteristic zero, let \(k\geq 1\), and choose \(\lambda\in K\setminus\{0\}\). Let \(L=Kx\oplus N\), where \(N=\operatorname{span}_K\{e_1,\ldots,e_k\}\) is abelian and the nonzero brackets are
\[
[e_i,x]=\lambda e_i+e_{i+1}\quad(1\leq i<k),\qquad [e_k,x]=\lambda e_k.
\]
Define \(S(e_i)=e_{i+1}\) for \(i<k\) and \(S(e_k)=0\), and set \(F_j=\operatorname{span}_K\{e_j,\ldots,e_k\}\).

A linear map \(\Delta:L\to L\) is a local derivation if and only if it has the form
\[
\Delta(x)=u,\quad \Delta|_N=B,\quad u\in N,\quad B(F_j)\subseteq F_j\ (1\leq j\leq k).
\]
In contrast, it is a derivation if and only if \(\Delta(x)=u\in N\) and \(\Delta|_N=p(S)\) for a polynomial \(p\in K[t]\) of degree less than \(k\). Consequently,
\[
\dim_K\operatorname{LocDer}(L)=k+\frac{k(k+1)}2,\qquad
\dim_K\operatorname{Der}(L)=2k,
\]
and the dimension of the quotient space \(\operatorname{LocDer}(L)/\operatorname{Der}(L)\) is exactly \(k(k-1)/2\).

## Assumptions and scope

The field has characteristic zero and \(\lambda\neq0\). The nilradical \(N\) is abelian, the complementary space is one-dimensional, and the action on \(N\) is a single Jordan block with eigenvalue \(\lambda\). Local derivations are linear maps, as in the cited solvable-Lie-algebra literature. No statement is made here for multiple Jordan blocks, zero eigenvalue, or positive characteristic.

## Proof

Write \(A=\lambda I+S\), so \([v,x]=Av\) for \(v\in N\), and \(A\) is invertible. For a derivation \(d\), let \(\phi:N\to K\) be the coefficient of \(x\) in \(d(v)\). Applying \(d\) to \([v,x]=Av\) and comparing the \(x\)-components gives \(\phi(Av)=0\). Since \(A\) is invertible, \(\phi=0\), hence \(d(N)\subseteq N\). Write \(d(x)=a x+u\) and \(d|_N=B\). The same derivation identity gives
\[
BA=AB+aA.
\]
Taking traces yields \(0=a\operatorname{tr}(A)=ak\lambda\). Characteristic zero and \(\lambda\neq0\) imply \(a=0\). Thus \(B\) commutes with \(A\), equivalently with \(S\). The centralizer of a single Jordan block is \(K[S]=\{p(S):\deg p<k\}\). Conversely, every pair \(d(x)=u\in N\), \(d|_N=p(S)\) satisfies the derivation identity because \(N\) is abelian and \(p(S)A=Ap(S)\). This proves the asserted description of \(\operatorname{Der}(L)\).

Every derivation has image in \(N\), so any local derivation \(\Delta\) also has image in \(N\). Write \(\Delta(x)=u\) and \(\Delta|_N=B\). Locality on each \(v\in N\) says that \(Bv=p_v(S)v\) for some polynomial \(p_v\). In particular, \(Be_j\in F_j\) for each basis vector, so \(B(F_j)\subseteq F_j\) for every \(j\).

Conversely, suppose \(B\) preserves every \(F_j\). For nonzero \(v=\sum_i v_i e_i\), let \(j\) be the least index with \(v_j\neq0\). Then \(v,Sv,\ldots,S^{k-j}v\) is a basis of \(F_j\). Since \(Bv\in F_j\), some polynomial \(p_v\) of degree at most \(k-j\) satisfies \(Bv=p_v(S)v\). For \(y=\alpha x+v\), if \(\alpha=0\), choose a derivation with value zero on \(x\) and restriction \(p_v(S)\) to \(N\). If \(\alpha\neq0\), choose the derivation \(d_y\) with \(d_y|_N=0\) and \(d_y(x)=\Delta(y)/\alpha\in N\). In either case \(d_y(y)=\Delta(y)\). Thus \(\Delta\) is local, proving the characterization.

The endomorphisms preserving the complete flag \(F_1\supset F_2\supset\cdots\supset F_k\supset0\) are triangular and have dimension \(k(k+1)/2\). Adding the arbitrary value \(u=\Delta(x)\) contributes \(k\) dimensions. The polynomial centralizer has dimension \(k\), so derivations have dimension \(2k\); subtraction gives the quotient dimension \(k(k-1)/2\).

## Verification

The argument is symbolic and holds for every integer \(k\geq1\); it does not infer an infinite-family statement from finite experiments. The accompanying standard-library script checks, for \(1\leq k\leq8\), the centralizer dimension of a single nilpotent Jordan block, the dimensions of the flag-preserving and polynomial subspaces, and rational examples of the polynomial representation \(Bv=p_v(S)v\). For each \(k\geq2\), the diagonal map with entries \(1,\ldots,1,2\) preserves the flag but does not commute with \(S\), giving a concrete non-derivation local derivation. These finite checks corroborate the proof; they are not its substitute.

## Relationship to prior work

Ayupov and Khudoyberdiyev prove that for a solvable Lie algebra with abelian nilradical and one-dimensional complement, every local derivation is a derivation exactly when the action of the complement is diagonalizable. For a nontrivial Jordan block they construct a particular local derivation that is not a derivation. Their displayed derivation matrices provide the centralizer description used here, but their theorem does not state the full space of local derivations or its dimension. The present result gives that complete space for the canonical single-block family and quantifies the failure of rigidity by \(k(k-1)/2\). Related results for solvable Leibniz algebras concern a different bracket identity and do not imply this Lie-algebra classification.

## Limitations

This is a classification for a single nonzero-eigenvalue Jordan block over a characteristic-zero field. It does not classify local derivations for arbitrary Jordan forms or prove a positive-characteristic analogue. The comparison is based on the inspected primary papers and semantic literature searches; an exhaustive search of every publication or database is not claimed.

## References

[1] Sh. A. Ayupov and A. Kh. Khudoyberdiyev, “Local derivations on solvable Lie algebras,” arXiv:1803.06668v1 (first posted 18 March 2018); journal version, *Linear and Multilinear Algebra* 69(7) (2021), 1286–1301, DOI 10.1080/03081087.2019.1626336.

[2] Sh. A. Ayupov, A. Kh. Khudoyberdiyev, and B. B. Yusupov, “Local and 2-local derivations of solvable Leibniz algebras,” arXiv:1911.03733v1 (first posted 9 November 2019), used only as adjacent literature.
