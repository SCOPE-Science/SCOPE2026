# Six-line characteristic-five reduction of Bring's curve and its exceptional six-point symmetry

## Finding
Let \(k\) be an algebraic closure of \(\mathbb F_5\). In \(\mathbb P^4_k\), write \(e_j\) for the degree-\(j\) elementary symmetric polynomial in five homogeneous coordinates \(x_1,\ldots,x_5\), and define the complete-intersection curve
\[
 B_5=V(e_1,e_2,e_3)\subset\mathbb P^4_k.
\]
This is the characteristic-five reduction of the classical elementary-symmetric canonical model of Bring's curve. By Newton's identities (with \(2\) and \(3\) invertible in characteristic \(5\)), the equations are equivalent to the first three vanishing power sums, which are used in some existing presentations. **The entire scheme \(B_5\) is reduced and equals exactly six distinct \(\mathbb F_5\)-defined lines through \(P=[1:1:1:1:1]\).** They are the spans of the diagonal vector and the \(120\) ordered permutations of \((0,1,2,3,4)\), with permutations identified when related by an affine transformation of \(\mathbb F_5\). There are precisely \(120/(5\cdot4)=6\) distinct spans.

The point \(P\) is the **only** singular point. It has six smooth branches, multiplicity \(6\), and delta invariant \(9\). The normalization is the disjoint union of six copies of \(\mathbb P^1_k\), and \(B_5\) has arithmetic genus \(4\). Furthermore the coordinate-permutation group \(S_5\) acts faithfully and transitively on its six lines; the component stabilizer is \(\operatorname{AGL}_1(\mathbb F_5)\) of order \(20\). Its six-point action is the standard projective action under the exceptional isomorphism
\[
S_5\ \cong\ \operatorname{PGL}_2(\mathbb F_5).
\]
This statement identifies the action of the **coordinate-permutation subgroup**, not the full automorphism group of the reducible curve.

## Assumptions and scope
All equations and assertions concern the full closed subscheme, not just its geometric support, over an algebraically closed field of characteristic \(5\). No smoothness is assumed. For \(\mathbf r=(r_1,\ldots,r_5)\) an ordering of the five field elements, let
\[
 L_{\mathbf r}=\big\{[S+r_1T:\cdots:S+r_5T]:[S:T]\in\mathbb P^1_k\big\}.
\]
This is a projective line because the constant diagonal vector and \(\mathbf r\) are linearly independent. The fields of definition and counts refer to the displayed model; no claim about an abstract stable model or its automorphism group is made.

## Proof
**1. Six explicit lines.** For every ordering \(\mathbf r\) of \(\mathbb F_5\), the monic polynomial with roots \(S+r_iT\) equals
\[
 \prod_{i=1}^5(U-S-r_iT)=(U-S)^5-T^4(U-S)
\]
in characteristic \(5\). Its coefficients of degrees \(4,3,2\) in \(U\) vanish. Thus \(e_1=e_2=e_3=0\) identically on \(L_{\mathbf r}\). Two such spans coincide precisely when their ordered residue vectors are related by \(\mathbf r' =u\mathbf r+v(1,\ldots,1)\) for some \(u\in\mathbb F_5^\times\), \(v\in\mathbb F_5\): indeed, a projective equality of their \(k\)-linear spans forces \(u,v\in\mathbb F_5\) by subtracting two distinct residue coordinates. The affine group has order \(20\), acts freely on orderings, and gives six distinct lines.

**2. Scheme-theoretic exhaustion.** Eliminate the linear equation \(e_1=0\) by writing
\[
(x_1,x_2,x_3,x_4,x_5)=(z+a,z+b,z+c,z,z-a-b-c).
\]
A direct computation over \(\mathbb F_5\) gives
\[
 e_2=-q,\qquad e_3=2zq-h,
\]
where
\[
\begin{aligned}
 q&=a^2+b^2+c^2+ab+ac+bc,\\
 h&=a^2b+a^2c+ab^2+2abc+ac^2+b^2c+bc^2.
\end{aligned}
\]
Thus \(B_5\) is the projective cone, with vertex \([a:b:c:z]=[0:0:0:1]\), over \(V(q,h)\subset\mathbb P^2_{\mathbb F_5}\). The Hessian matrix of \(q\) has diagonal entries \(2\) and off-diagonal entries \(1\), with determinant \(4\ne0\) in \(\mathbb F_5\), so \(q=0\) is a smooth, geometrically irreducible conic. The cubic \(h\) is not a multiple of \(q\): if \(h=q(\alpha a+\beta b+\gamma c)\), comparing the pure-cube coefficients forces \(\alpha=\beta=\gamma=0\), contrary to \(h\ne0\).

The following six distinct points satisfy both equations:
\[
(1:2:3),\ (1:2:4),\ (1:3:2),\ (1:3:4),\ (1:4:2),\ (1:4:3).
\]
By Bézout, the intersection of a smooth conic and a cubic without a common component has total scheme length \(6\), so these six reduced points exhaust the full intersection scheme, with intersection multiplicity \(1\) each. The cone is therefore the **reduced scheme-theoretic union** of the six indicated lines. Every pair of distinct generator lines meets only at the vertex; away from it the curve is smooth.

**3. Local ring, multiplicity, and delta invariant.** In the affine chart \(z=1\), with the vertex at the origin, the complete local ring is exactly
\[
 \widehat{\mathcal O}_{B_5,P}
 =k[[a,b,c]]/(q,h).
\]
The homogeneous regular sequence \((q,h)\) has degrees \(2\) and \(3\), so the Hilbert–Samuel multiplicity at the vertex is \(2\cdot3=6\). As a complete intersection of type \((2,3)\) in \(\mathbb P^3\), the curve has arithmetic genus
\[
 p_a(B_5)=1+\frac{2\cdot3(2+3-4)}2=4.
\]
Its normalization is \(\coprod_{i=1}^{6}\mathbb P^1_k\). The normalization exact sequence, supported at the single singular point, gives
\[
 1-p_a(B_5)=\chi(\mathcal O_{B_5})
 =6-\delta_P,
 \qquad\text{hence}\qquad\delta_P=9.
\]
In particular this is a six-branch *space-curve* singularity, not a planar ordinary sixfold point.

**4. The exceptional six-point action.** Coordinate permutations preserve each \(e_j\) and hence permute the six lines. The stabilizer of one line is exactly the group of affine permutations \(r\mapsto ur+v\) of its five distinct coordinate residues; it has order \(20\), proving transitivity. The induced action on the conic of directions is a homomorphism \(S_5\to\operatorname{Aut}_{\mathbb F_5}(V(q))\cong\operatorname{PGL}_2(\mathbb F_5)\). It is faithful: its kernel is normal in \(S_5\), and a three-cycle changes, for instance, the direction \((1:2:3)\), so its kernel cannot contain \(A_5\). Since the only nontrivial proper normal subgroup of \(S_5\) is \(A_5\), the kernel is trivial. Both groups have order \(120\), giving the claimed isomorphism and its action on the six \(\mathbb F_5\)-points of the conic.

## Verification
Run `python3 verify_bring.py` in the directory containing this document. The exact, standard-library-only verifier reconstructs \(e_1,e_2,e_3\) and \(q,h\) by polynomial arithmetic modulo \(5\); enumerates all \(31\) projective points of \(\mathbb P^2(\mathbb F_5)\); confirms the six conic/cubic intersection directions; checks all \(120\) permutations induce distinct permutations of those six directions; and checks the genus/delta arithmetic. It prints `BRING_CHAR5_SIX_LINES_CONIC_OUTER_S5_DELTA9_OK`. The general scheme-theoretic conclusion is established by the regular-sequence and Bézout argument above, not by finite-field enumeration alone.

## Relationship to prior work
Korchmáros, Lia, and Timpanella, *A generalization of Bring's curve in any characteristic*, first made public on 20 December 2021, study the same family of symmetric power-sum complete intersections but explicitly impose \(p\ge7\), and in positive characteristic \(m\le p-1\). Their smooth-curve statements therefore exclude this characteristic-five boundary. Braden and Disney-Hogg, *Bring's curve: old and new* (arXiv first posted 29 August 2022; journal 2023), give the classical complex geometry; their introduction expressly excludes positive-characteristic extensions from its scope. Conca, Krattenthaler, and Watanabe study regular sequences of symmetric power sums chiefly over the complex field, not this six-line special fibre. The six-line Winger pencil in characteristic zero is a separate plane-sextic degeneration; its occurrence does not state the characteristic-five reduction of the elementary-symmetric Bring model. The claims here concern the **explicit full special fibre**, its local delta invariant, and the induced exceptional six-point symmetry, not a new general classification of Bring curves.

## Limitations
The result applies only to the displayed elementary-symmetric projective model in characteristic \(5\). It does not classify possible semistable models, compute a Jacobian's Néron model, assign a stable reduction type, or determine the full abstract/projective automorphism group of the reducible special fibre. The literature comparison may miss unindexed earlier computations; no claim of independent external certification is made.

## References
1. G. Korchmáros, S. Lia, M. Timpanella, *A generalization of Bring's curve in any characteristic*, arXiv:2112.10886 (first posted 2021-12-20), https://arxiv.org/abs/2112.10886 ; full preprint https://arxiv.org/pdf/2112.10886 .
2. H. W. Braden, L. Disney-Hogg, *Bring's curve: old and new*, arXiv:2208.13692 (first posted 2022-08-29), https://arxiv.org/abs/2208.13692 ; *European Journal of Mathematics* 10 (2024), article 3, https://doi.org/10.1007/s40879-023-00706-0 (online 2023-12-18).
3. A. Conca, C. Krattenthaler, J. Watanabe, *Regular sequences of symmetric polynomials*, *Rend. Sem. Mat. Univ. Padova* 121 (2009), 179–199, https://doi.org/10.4171/RSMUP/121-11 .
4. E. Looijenga, Y. Zi, *Monodromy and period map of the Winger pencil*, arXiv:2109.01810 (2021), https://arxiv.org/abs/2109.01810 (a different complex six-line pencil).
