# Parity and moduli of cyclic maximal-contact conic arrangements

## Finding
Let \(k\) be any algebraically closed field and \(n\geq3\). Consider ordered, pairwise distinct smooth conics \(C_0,\ldots,C_{n-1}\subset\mathbb P_k^2\), indexed cyclically. Require that \(C_i\) and \(C_{i+1}\) have a unique intersection \(p_i\), of intersection multiplicity four; that the \(n\) points \(p_i\) are distinct and collinear on a line \(M\); and that their common tangent lines \(T_{p_i}C_i=T_{p_i}C_{i+1}\) concur at a point \(P\notin M\). Then such a configuration exists **if and only if** \(n\) is even or \(\operatorname{char}(k)=2\). For each fixed ordered configuration of points \(p_i\in M\) and fixed \(P\notin M\), the conics are uniquely determined up to projective equivalence preserving the marked points and pencil center. The moduli of ordered configurations modulo projective automorphisms is the configuration space \(M_{0,n}(k)\) of \(n\) ordered distinct points of a projective line, up to \(\operatorname{PGL}_2(k)\). In characteristic two, **every pair** of distinct conics in the resulting tuple, including nonadjacent pairs, meets at one point with intersection multiplicity four (but the extra contact points need not lie on \(M\)).

## Assumptions and scope
All fields are algebraically closed. The incidence conditions are part of the theorem; no statement is made for arbitrary conic arrangements lacking collinearity or concurrence. A contact of order four means a single intersection point with local intersection multiplicity exactly four; Bézout then excludes any second intersection between that pair. Projective equivalences preserve the cyclic indexing. The claim does not classify singularity schemes of the full union away from the specified contacts, nor its freeness.

## Proof
Choose projective coordinates \([x:y:z]\) with \(M=\{y=0\}\) and \(P=[0:1:0]\). Write \(p_i=[a_i:0:b_i]\) and \(L_i=b_ix-a_iz\); the \(L_i=0\) are the distinct lines \(Pp_i\). Their evaluations \(L_i(p_j)=b_ia_j-a_ib_j\) are nonzero for \(i\neq j\) and satisfy \(L_i(p_j)=-L_j(p_i)\).

Because \(C_i\cap M\) consists of the two distinct points \(p_{i-1}\) and \(p_i\), any homogeneous equation for it has the form
\[F_i=A_iy^2+yB_i(x,z)+D_i L_{i-1}L_i.\]
Both tangent lines at these contacts belong to the pencil through \(P\); hence the coefficient of \(dy\) in the tangent-line equation vanishes at both contacts, i.e. \(B_i(p_{i-1})=B_i(p_i)=0\). Since \(B_i\) is linear, \(B_i=0\). Smooth irreducibility forces \(A_iD_i\neq0\). After rescaling each equation, the required normal form is
\[F_i=y^2+c_iL_{i-1}L_i,\qquad c_i\in k^*.\tag{1}\]
These conics are smooth in every characteristic: the independent linear forms \(L_{i-1},L_i\) give coordinates \(u,v\), making (1) \(y^2+c_iuv=0\); its projective gradient cannot vanish at any point on it, also when the characteristic equals two.

For consecutive conics, subtraction gives
\[F_{i+1}-F_i=L_i(c_{i+1}L_{i+1}-c_iL_{i-1}).\tag{2}\]
The order of \(L_i\) along the smooth curve \(C_i\) at \(p_i\) is exactly two, because it is its tangent line. Consequently (2) has intersection order four at \(p_i\) precisely when the second linear factor also vanishes there, equivalently when
\[c_{i+1}L_{i+1}(p_i)=c_iL_{i-1}(p_i).\tag{3}\]
In that case the parenthesized factor is a nonzero scalar multiple of \(L_i\): otherwise the two conics coincide, impossible as their traces on \(M\) have different unordered zero pairs. Thus \(F_{i+1}-F_i=u_iL_i^2\), with \(u_i\neq0\), and the contact is exactly order four.

The nonzero quantities in (3) imply
\[\frac{c_{i+1}}{c_i}=\frac{L_{i-1}(p_i)}{L_{i+1}(p_i)}.\]
Multiplying over all cyclic indices and using skew symmetry of the \(2\times2\) determinants yields
\[1=\prod_{i=0}^{n-1}\frac{L_{i-1}(p_i)}{L_{i+1}(p_i)}=(-1)^n.\tag{4}\]
Thus odd \(n\) is impossible outside characteristic two. Conversely, for even \(n\) in any characteristic, or all \(n\geq3\) in characteristic two, (4) makes the recurrence consistent. Starting with arbitrary \(c_0\neq0\) determines all coefficients uniquely and gives distinct smooth conics satisfying (3), so existence follows. A different initial \(c_0\) multiplies every \(c_i\) by the same nonzero scalar; since \(k\) is algebraically closed, scaling the coordinate \(y\) by a square root identifies the configurations. Any transformation preserving \(P\) and \(M\) induces a projectivity of \(M\), and all projectivities of \(M\) lift; hence the moduli claim is exactly \(M_{0,n}(k)\).

Finally, in characteristic two each adjacent difference \(F_{i+1}-F_i=u_iL_i^2\) has no mixed \(xz\) term. Every difference \(F_j-F_i\) is then a sum of binary squares and therefore a single binary square \(H_{ij}(x,z)^2\). It is nonzero since the conics are distinct. Their common mixed \(xz\) coefficient is nonzero because each \(c_iL_{i-1}L_i\) has distinct linear factors. Restricting \(F_i\) to the line \(H_{ij}=0\) through \(P\) leaves a nonzero quadratic of the form \(y^2+d s^2=(y+\sqrt d\,s)^2\), with exactly one point counted twice; since \(F_j-F_i=H_{ij}^2\), the two conics meet there with intersection multiplicity four. This proves the all-pairs assertion.

## Verification
An accompanying pure-Python `verify.py` computes the normal-form coefficients in exact rational arithmetic for lengths \(4,6,8\), checks that every adjacent quadratic difference is a nonzero scalar times the prescribed line squared, and finds an incompatible final recurrence for odd lengths \(3,5,7\) in characteristic zero. It also checks a characteristic-two triple over \(\mathbb F_2\) and the lengths \(5,7\) over \(\mathbb F_8\), including smoothness, cyclic contact, distinctness, and the all-pairs square-difference condition. The program prints `VERIFY_OK`. These finite calculations are *checks of the algebra* and do not replace the arbitrary-length proof above.

## Relationship to prior work
Zieliński (2023), especially Theorem 1.1 and Section 4.1, established numerical bounds on \(A_7\) conic contacts and recalled Persson's three-conic arrangement. Pokora (2023), especially Theorem B and Example 2.6, addressed freeness and exhibited a four-conic configuration with four \(A_7\) contacts. An earlier complete classification of the ordered four-conic concurrent-tangent case already handles that individual complex case; novelty is **not** claimed for \(n=4\) in characteristic zero. The present theorem concerns the characteristic-dependent all-length obstruction, moduli identification, and complete pairwise-contact jump in characteristic two; these are not consequences of the cited finite-case statements or freeness bounds. Merta–Zieliński–Zieliński (2025) classify free three-conic arrangements over \(\mathbb C\), not these incidence configurations across characteristics.

## Limitations
Only the stated collinearity, concurrence, and fourth-order pair-contact constraints are classified. The theorem is geometric over algebraically closed fields; there is no assertion that an arbitrary choice of points defined over a nonclosed field yields the same rational-coordinate classification. In characteristic two the additional nonadjacent contact points can lie off the specified line. No further incidence or freeness assertions are made.

## References
1. M. Zieliński, *On plane conic arrangements with \(A_5\) and \(A_7\) singularities*, Rendiconti del Circolo Matematico di Palermo (2023 first online), doi:10.1007/s12215-023-00890-8, https://link.springer.com/article/10.1007/s12215-023-00890-8.
2. P. Pokora, *On free and nearly free arrangements of conics admitting certain ADE singularities*, Annali dell'Università di Ferrara (2023 first online), doi:10.1007/s11565-023-00481-6, https://link.springer.com/article/10.1007/s11565-023-00481-6.
3. Ł. Merta, M. Zieliński, F. Zieliński, *On free arrangements of three conics* (2025), arXiv:2505.20025, https://arxiv.org/abs/2505.20025.
