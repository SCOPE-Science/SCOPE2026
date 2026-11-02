# Twenty lines on a twelve-nodal symmetric quartic in characteristic two

## Finding

Let \(k=\overline{\mathbb F}_2\), write \(\sigma_j\) for the elementary symmetric polynomial of degree \(j\) in four projective coordinates, and set
\[
X=V\bigl(\sigma_4+(\sigma_1^2+\sigma_2)^2\bigr)\subset\mathbb P^3_{\mathbb F_2}.
\]
The **complete geometric set of projective lines contained in \(X_k\) consists of exactly twenty lines**, in two explicitly described families: eight coordinate-plane lines and twelve paired-coordinate lines. The surface is normal, and its twelve singularities are ordinary double points; each node belongs to exactly four of these lines, whereas every coordinate-plane line passes through three nodes and every paired-coordinate line through two.

Among the \(\binom{20}{2}=190\) pairs of distinct lines, exactly seventy-two meet at nodes and twenty-two meet at smooth points. At each node four lines concur, and the twenty-two smooth intersection points each lie on exactly two lines. Four of these smooth intersections are \(\mathbb F_2\)-rational and the other eighteen are defined over \(\mathbb F_4\setminus\mathbb F_2\).

Every geometric line is defined over \(\mathbb F_4\), none over \(\mathbb F_2\). The **reduced** line-Hilbert scheme therefore has the exact arithmetic description
\[
F_1(X)_{\mathrm{red}}\;\cong_{\mathbb F_2}\;\coprod_{j=1}^{10}\operatorname{Spec}\mathbb F_4,
\qquad Z(F_1(X)_{\mathrm{red}}/\mathbb F_2,T)=(1-T^2)^{-10}.
\]
In particular, for all integers \(n\ge1\), there are twenty \(\mathbb F_{2^n}\)-rational projective lines when \(n\) is even and none when \(n\) is odd.

## Assumptions and scope

All geometric line and intersection claims are over the algebraic closure of \(\mathbb F_2\). The surface is the fixed, symmetric, prime-field member \(\sigma_4+(\sigma_1^2+\sigma_2)^2=0\) of the normal-quartic construction \(\ell_1\ell_2\ell_3\ell_4+Q^2=0\). No genericity assumption is made. The symbol \(F_1(X)_{\mathrm{red}}\) denotes the reduced subscheme of the Hilbert scheme of closed subschemes with Hilbert polynomial \(t+1\); no statement is made about the possible infinitesimal thickening of the unreduced Hilbert scheme.

Fix \(\omega\in\mathbb F_4\) with \(\omega^2+\omega+1=0\), so \(\omega^2=\omega+1\). A *coordinate-plane line* lies in one of the four coordinate planes, whereas a *paired-coordinate line* is specified by one of the three partitions of the four coordinate indices into two unordered pairs.

## Proof

**1. Singular points.** Write \(Q=\sigma_1^2+\sigma_2=\sum_i x_i^2+\sum_{i<j}x_ix_j\) and \(F=x_1x_2x_3x_4+Q^2\). In characteristic two, \(\partial F/\partial x_i=\prod_{j\ne i}x_j\). Hence all four derivatives vanish exactly when at least two coordinates are zero. If three coordinates vanish, the nonzero remaining coordinate gives \(Q\ne0\), so such a point is not on \(X\). If precisely coordinates \(x_i,x_j\) vanish, and \(x_r,x_s\) do not, then \(F=0\) becomes \(x_r^2+x_rx_s+x_s^2=0\). This gives exactly two points for each of six edges: their nonzero coordinate ratio is \(\omega\) or \(\omega^2\). There are precisely twelve singular points, all defined over \(\mathbb F_4\) and none over \(\mathbb F_2\).

At a singular point with \(x_1=x_2=0\), \(x_4=1\), \(x_3\in\{\omega,\omega^2\}\), the derivative of \(Q\) with respect to the local coordinate \(x_3\) is \(1\). Thus \(w=Q\), \(u=x_1\), \(v=x_2x_3\) are regular local parameters, and the local equation is exactly \(w^2+uv=0\). All twelve singularities are \(A_1\) rational double points. In particular, because \(X\) is a hypersurface with only isolated singularities, it is geometrically integral and normal.

**2. Lines in coordinate planes.** If a line \(L\) is contained in \(x_1=0\), then \(F|_L=Q|_L^2\). On that plane the conic \(Q=0\) factors into two distinct lines:
\[
Q|_{x_1=0}=(x_2+\omega x_3+\omega^2x_4)
(x_2+\omega^2x_3+\omega x_4).
\]
Consequently \(L\) is one of these two lines. Permuting the coordinates gives two lines per coordinate plane, eight in all. None lies in two coordinate planes: on a coordinate edge the restriction \(x_r^2+x_rx_s+x_s^2\) is nonzero as a polynomial.

**3. All remaining lines.** Let \(L\subset X_k\) be a line not contained in any coordinate plane. Each of the four coordinate restrictions \(\ell_i=x_i|_L\) is a nonzero linear form on \(L\cong\mathbb P^1_k\). From \(\prod_i\ell_i=Q|_L^2\), the divisor of \(\prod_i\ell_i\) on \(L\) has even multiplicity at every point. Hence the four forms split into two proportional pairs. They cannot all be proportional, because the induced inclusion of \(L\) into \(\mathbb P^3\) would then be constant. After reindexing, the line therefore has coordinates
\[
[x_1:x_2:x_3:x_4]=[as:s:bt:t],
\qquad a,b\in k^\times.
\]
On this line,
\[
Q=(a^2+a+1)s^2+(b^2+b+1)t^2+(a+1)(b+1)st.
\]
Comparison of the coefficients of \(s^4\) and \(t^4\) in \(F|_L=0\) forces \(a^2+a+1=b^2+b+1=0\), so \(a,b\in\{\omega,\omega^2\}\). Conversely, for these roots \((a+1)^2=a\) and \((b+1)^2=b\), making \(Q|_L^2=ab s^2t^2\). Thus all four choices of \((a,b)\) work for each of the three pair partitions. These twelve lines are pairwise distinct, and none is a coordinate-plane line. This proves geometric completeness and the number twenty **without relying on a finite-field experiment**.

**4. The incidence geometry.** At a node on a coordinate edge, two coordinate-plane lines occur (one in each plane containing the edge), and two paired-coordinate lines occur (the pairing using that edge, with two choices for the other parameter). Thus each node lies on four lines. Each coordinate-plane line meets the three coordinate edges in its plane at exactly one node per edge; each paired-coordinate line meets its two paired edges at one node per edge. Therefore the seventy-two nodal pairs are exactly \(12\binom42=72\).

For completeness, the finite remaining intersection computation is exhausted explicitly: all twenty lines were proved to be \(\mathbb F_4\)-defined, and the verifier enumerates their five \(\mathbb F_4\)-points, compares all 190 line pairs, and obtains the following complete counts:

| Pair types | Meet at a node | Meet at a smooth point |
| --- | ---: | ---: |
| Coordinate / coordinate | 12 | 4 |
| Coordinate / paired | 48 | 0 |
| Paired / paired | 12 | 18 |

No two distinct projective lines meet at two points. The program checks that the twenty-two smooth intersections are pairwise different, that each is on exactly two lines, and that exactly four are Frobenius-fixed. They are the four coordinate permutations of \([0:1:1:1]\). The other eighteen form nine Frobenius pairs. The independent finite computation here establishes an exact finite incidence fact, not an inference about unenumerated lines.

**5. Frobenius and the reduced line scheme.** Frobenius interchanges \(\omega\) and \(\omega^2\). It exchanges the two coordinate-plane lines in each coordinate plane and sends the paired line specified by \((a,b)\) to the distinct paired line specified by \((a^2,b^2)\). All twenty lines therefore occur in ten degree-two Frobenius orbits. Their geometric set is finite, so the reduced line-Hilbert scheme is zero-dimensional; a finite reduced scheme over the perfect field \(\mathbb F_2\) is finite étale. The stated decomposition, zeta function, and rational-line counts follow.

## Verification

Run `python3 verify_12node_lines.py` from the directory containing this document. It uses only the Python standard library and implements exact arithmetic in \(\mathbb F_4=\mathbb F_2[\omega]/(\omega^2+\omega+1)\). It independently constructs all 85 projective points and all 357 projective lines in \(\mathbb P^3(\mathbb F_4)\), tests the quartic on every point of every line, and finds twenty contained lines. It separately constructs the predicted eight-plus-twelve lines and checks equality with the exhaustive list. It then checks all twelve singular points, the 190 line pairs, incidence counts, smoothness of the crossings, and Frobenius actions. The final output is `SYMMETRIC_12_NODE_QUARTIC_20_LINES_ALL_CHECKS_PASS`.

The exhaustive \(\mathbb F_4\) check independently verifies the finite configuration; the algebraic-closure completeness in Step 3 is an algebraic proof and is not inferred from the finite-field enumeration.

## Relationship to prior work

Catanese's *Singularities of normal quartic surfaces I (char=2)* (arXiv:2106.09988, initial public submission June 18, 2021), especially its Section 4, establishes the symmetric quartic families and their singular-point strata. Catanese and Schütt's *Singularities of normal quartic surfaces III (char=2, non-supersingular)* (arXiv:2206.03295, initial submission June 7, 2022), especially Example 19 and Remark 20, gives the construction \(\ell_1\ell_2\ell_3\ell_4+Q^2\) and relates it to symmetric twelve-nodal quartics. Their *Part II* (arXiv:2110.03078, initially October 6, 2021) studies singularities and Gauss maps. The existence and classification of the twelve nodes, and their arithmetic splitting, are established or implied by prior work and are not the priority claim here.

The new, separately proved assertion concerns the complete **line-Hilbert support**, its twenty-line decomposition, pairwise incidence, and Frobenius orbit structure for the specified prime-field member. These do not follow just from the twelve-node singularity classification. Literature searches for this exact line configuration and its equivalent formulations did not reveal a covering theorem; historical priority in unindexed line-configuration literature is a residual risk.

## Limitations

The computation determines only the **reduced** line-Hilbert scheme. It does not determine tangent spaces or possible nonreduced infinitesimal structure of the full Hilbert scheme, the Picard lattice of the minimal K3 resolution, or all automorphisms of the surface. The twenty-line count applies to this specified symmetric quartic and is not a generic claim for every twelve-nodal quartic. No independent external mathematical validation has been performed.

## References

1. F. Catanese, *Singularities of normal quartic surfaces I (char=2)*, arXiv:2106.09988, initial version June 18, 2021, Section 4. https://arxiv.org/html/2106.09988v3
2. F. Catanese and M. Schütt, *Singularities of normal quartic surfaces II (char=2)*, arXiv:2110.03078, initial version October 6, 2021. https://arxiv.org/abs/2110.03078
3. F. Catanese and M. Schütt, *Singularities of normal quartic surfaces III (char=2, non-supersingular)*, arXiv:2206.03295, initial version June 7, 2022, Example 19 and Remark 20. https://arxiv.org/html/2206.03295v1
