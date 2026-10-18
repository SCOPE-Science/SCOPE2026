# The three nuclei and characteristic jumps of finite Alexander quandle algebras
## Finding
Let \(G\) be a finite abelian group, \(\phi\in\operatorname{Aut}(G)\), and \(k\) any field. The Alexander quandle \(Q=\operatorname{Alex}(G,\phi)\) has operation \(x*y=\phi(x)+(1-\phi)y\). Write \(A=k[Q]\) for its (generally nonassociative and nonunital) quandle algebra.

Let \(H=(1-\phi)G\) and \(H_2=(1-\phi)H\), both subgroups of \(G\), and let \(B=k[G]\) be the *ordinary associative* group algebra, with basis \(X^g\). Define the linear map \(\beta:B\to B\) by \(\beta(X^g)=X^{(1-\phi)g}\). For any coset \(g+H\) set \(\Omega_{g+H}=\sum_{h\in H}X^{g+h}\), \(\Omega_H=\Omega_{0+H}\), and
\[
U_H=\operatorname{span}_k\{\Omega_{g+H}:g+H\in G/H\}.
\]
Let \(N_l,N_m,N_r\) be the three nuclei of \(A\), defined by vanishing of the associator when an element occupies respectively the first, second, or third slot. Then, under the vector-space identification \(A=B\),
\[
\boxed{N_l=U_H,\qquad N_m=\beta^{-1}(k\Omega_H),\qquad
N_r=\begin{cases}\beta^{-1}(k\Omega_H),&H_2=H,\\
\ker\beta,&H_2\ne H.\end{cases}}
\]
Consequently,
\[
\dim_kN_l=\frac{|G|}{|H|},\quad
\dim_kN_m=|G|-|H|+1,\quad
\dim_kN_r=|G|-|H|+\mathbf1_{H_2=H}.
\]
Put \(a=|G|/|H|\) and \(b=|H|/|H_2|\). The *full nucleus* \(N=N_l\cap N_m\cap N_r\) is
\[
N=\begin{cases}
U_H,&H_2=H,\\
U_H\cap\ker\beta,&H_2\ne H,
\end{cases}
\quad
\dim_kN=\begin{cases}
a,&H_2=H\text{ or }\operatorname{char}k\mid b,\\
a-b,&H_2\ne H\text{ and }\operatorname{char}k\nmid b.
\end{cases}
\]
Here characteristic zero is understood not to divide any positive integer. These formulas include disconnected, non-Latin Alexander quandles, and they are valid without semisimplicity assumptions on the coefficient group ring. The connected case is included for completeness but not asserted to be new.

## Assumptions and scope
All groups are written additively. \(\phi\) is invertible but \(1-\phi\) need not be. The algebra multiplication is bilinear and need not be associative. The associator is \([u,v,w]=(u\star v)\star w-u\star(v\star w)\); the definitions of nuclei require its vanishing against *all* elements in the other two slots. The symbol \(1=X^0\) below denotes the unit of \(B\), not a two-sided unit of \(A\). The symbol \(\mathbf1_{H_2=H}\) denotes the indicator of subgroup equality.

## Proof
**Step 1 (transport and associator).** Let \(\alpha(X^g)=X^{\phi g}\). The standard group-ring transport gives \(u\star v=\alpha(u)\beta(v)\), with juxtaposition on the right referring solely to the ordinary associative product of \(B\). Since \(\alpha\) and \(\beta\) commute, a direct expansion gives
\[
[u,v,w]=\alpha\beta(v)\bigl(\alpha^2(u)\beta(w)-\alpha(u)\beta^2(w)\bigr).
\tag{1}
\]
Define the subgroup ideal \(L_H=\langle X^h-1:h\in H\rangle_B\). It is the kernel of the quotient map \(B\to k[G/H]\). Its annihilator is exactly \(U_H\): multiplication by every \(X^h-1\) forces coefficient constancy on each \(H\)-coset, and this also suffices. Furthermore, both families \(\alpha^2(u)-\alpha(u)\) and \(\beta(w)-\beta^2(w)\), as \(u,w\) vary, lie in \(L_H\). The shifts in the second family range over \(\beta\phi(G)=H\), hence its elements generate \(L_H\) as an ideal of \(B\). Likewise, the shifts in the first family range over \(\phi(\phi-1)G=H\).

**Step 2 (left nucleus).** If \(u\in N_l\), taking \(v=w=1\) in (1) yields \(\alpha^2(u)=\alpha(u)\). Since \(\alpha\) is invertible, \(\alpha(u)=u\). Now taking \(v=1\) and letting \(w\) vary shows that \(u\) annihilates every \(\beta(w)-\beta^2(w)\), hence \(u\in U_H\). Conversely \(\alpha\) fixes \(U_H\) pointwise: \(\phi(g)-g\in H\), and \(\phi\) permutes each \(H\)-coset. Thus for \(u\in U_H\), equation (1) reduces to \(\alpha\beta(v)u(\beta(w)-\beta^2(w))=0\). Therefore \(N_l=U_H\).

**Step 3 (middle nucleus).** If \(v\in N_m\), put \(u=1\) in (1). Then \(\alpha\beta(v)\) annihilates the generating family \(\beta(w)-\beta^2(w)\), so \(\alpha\beta(v)\in U_H\). As \(\alpha(U_H)=U_H\), this says \(\beta(v)\in U_H\). But \(\beta(B)=k[H]\), and \(U_H\cap k[H]=k\Omega_H\). Conversely, if \(\beta(v)\in k\Omega_H\), then \(\alpha\beta(v)\in k\Omega_H\subseteq\operatorname{Ann}_B L_H\), and the parenthesized factor in (1) lies in \(L_H\). Thus \(N_m=\beta^{-1}(k\Omega_H)\). Since \(\beta:B\twoheadrightarrow k[H]\), its nullity is \(|G|-|H|\); the preimage of a one-dimensional subspace has dimension \(|G|-|H|+1\).

**Step 4 (right nucleus).** If \(w\in N_r\), take \(u=v=1\) in (1) to obtain \(\beta(w)=\beta^2(w)\). Next let \(u\) vary with \(v=1\), obtaining \((\alpha^2(u)-\alpha(u))\beta(w)=0\). The generating property above forces \(\beta(w)\in U_H\cap k[H]=k\Omega_H\). These two conditions are also sufficient for vanishing of (1). Now
\[
\beta(\Omega_H)=b\,\Omega_{H_2},\qquad b=|H|/|H_2|.
\tag{2}
\]
If \(H_2=H\), then \(b=1\) and each scalar multiple of \(\Omega_H\) is fixed by \(\beta\). If \(H_2\subsetneq H\), equality \(c\Omega_H=cb\Omega_{H_2}\) forces \(c=0\), because the left side has coefficient \(c\) on every element of \(H\setminus H_2\), while the right side has zero there; this argument works in every characteristic. Hence the two displayed alternatives for \(N_r\), with the dimension formula.

**Step 5 (full nucleus and characteristic jump).** For each \(g+H\),
\[
\beta(\Omega_{g+H})=b\,\Omega_{\beta(g)+H_2}.
\tag{3}
\]
The induced map of coset sets \(G/H\to H/H_2\), \(g+H\mapsto\beta(g)+H_2\), is surjective. If \(H_2=H\) then equation (3) gives \(U_H\subseteq N_m\cap N_r\), so \(N=U_H\). Otherwise \(N_r=\ker\beta\subseteq N_m\), hence \(N=U_H\cap\ker\beta\). In the latter case, equation (3) has image rank \(b\) on \(U_H\) when \(b\ne0\) in \(k\), because the target coset sums are linearly independent and all occur. If \(b=0\) in \(k\), equation (3) vanishes identically on \(U_H\). Rank-nullity now yields the asserted formula for \(\dim_kN\). Notice that surjectivity also implies \(b\le a\), so all displayed dimensions are nonnegative.

## Verification
The separate reproducible Python 3 program `verify.py` constructs each finite Alexander quandle multiplication table without using equations (1)–(3), generates every basis associator, and computes the four nuclear dimensions as nullities of modular matrices. It exhaustively tests all unit multipliers for cyclic groups of sizes \(1\) through \(12\) in coefficient characteristics \(2,3,5,7\), and all invertible matrices defining automorphisms of the two-dimensional vector groups over \(\mathbb F_2\) and \(\mathbb F_3\), in coefficient characteristics \(2,3,5\). All \(346\) cases agree with the formulas and the program reports `VERIFY_OK`. These computations are finite consistency checks; the unrestricted field-and-group assertion is proved symbolically above.

For a concrete jump take \(G=\mathbb Z/4\mathbb Z\), \(\phi(g)=-g\), hence \(H=\{0,2\}\), \(H_2=\{0\}\), and \(a=b=2\). Then
\[
(\dim N_l,\dim N_m,\dim N_r,\dim N)=
\begin{cases}(2,3,2,0),&\operatorname{char}k\ne2,\\(2,3,2,2),&\operatorname{char}k=2.\end{cases}
\]
The algebra has the *same* quandle multiplication table in both cases; only the coefficient characteristic changes. For every prime \(p\), take \(G=(\mathbb Z/p\mathbb Z)^2\) and \(\phi(x,y)=(x+y,y)\). Then \(H=\{(x,0):x\in\mathbb F_p\}\) and \(H_2=0\), so \(a=b=p\). The full nucleus has dimension \(0\) over every field of characteristic different from \(p\), and dimension \(p\) over every field of characteristic \(p\). Hence the characteristic-controlled nuclear jump can be arbitrarily large.

## Relationship to prior work
Zhang, *Group-ring methods for Alexander quandle rings* (arXiv:2610.08204v1), Proposition 2.1, establishes the group-ring transport used in Step 1. Its main results describe augmentation products, commutator subalgebras, integral idempotents, and Peirce spectra, not the three nuclei. The transport itself is not asserted to be new. Sangare and Ta, *Idempotents, automorphism groups, and commutator widths of quandle algebras* (arXiv:2608.01550), Proposition 4.7, establishes the left nucleus for odd dihedral quandles; that known Latin case is credited. The connected-quandle left-nucleus result and the finite Latin three-nucleus case also precede the present analysis; these are recovered as special cases. The new assertion assessed here is the complete simultaneous classification for arbitrary **nonconnected** finite Alexander quandles, particularly the right-nucleus transition and coefficient-characteristic jump of the full nucleus.

## Limitations
The proof assumes \(G\) finite abelian, \(\phi\) invertible, and \(k\) a field. It does not classify nuclei for nonabelian generalized Alexander quandles, infinite underlying groups, or arbitrary coefficient rings. It determines vector spaces and dimensions; no claim is made about their unitality. Equivalent descriptions in older literature on twisted group-ring multiplications remain a possible historical overlap. Finite computation does not provide independent validation of the general theorem.

## References
1. Z.-L. Zhang, *Group-ring methods for Alexander quandle rings*, arXiv:2610.08204v1, October 6, 2026; especially Proposition 2.1 and Sections 2–5.
2. B. Sangare and L. Ta, *Idempotents, automorphism groups, and commutator widths of quandle algebras*, arXiv:2608.01550v2 (2026), especially Proposition 4.7.
