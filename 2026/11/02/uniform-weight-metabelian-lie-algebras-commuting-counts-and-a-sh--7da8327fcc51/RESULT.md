# Uniform-weight metabelian Lie algebras: commuting counts and a sharp reducibility threshold

## Finding

Let \(H\) and \(E\) be abelian spaces of dimensions \(d\) and \(m\), with \(1\le d\le m\). Let nonzero weights \(\alpha_1,\ldots,\alpha_m\in H^*\) form a representation of the uniform matroid \(U_{d,m}\): every at most \(d\) weights are independent. Form the split metabelian Lie algebra \(L=H\ltimes E\), with basis \(e_i\) of \(E\) and \([h,e_i]=\alpha_i(h)e_i\).

**Arithmetic theorem.** Over any finite field \(\mathbb F_q\) admitting these weights, for every integer \(r\ge1\), the number of ordered, pairwise commuting \(r\)-tuples in \(L\) is
\[
\boxed{C_L(r;q)=q^m\sum_{s=0}^{m}\binom ms (q^{r-1}-1)^s q^{r(d-\min\{s,d\})}.}
\]
More generally, for any nonzero (not necessarily uniform) weight configuration spanning \(H^*\), the corresponding exact formula is \(q^m\sum_{S\subseteq[m]}(q^{r-1}-1)^{|S|}q^{r(d-\operatorname{rank}\{\alpha_i:i\in S\})}\). Thus the whole commuting-tuple census depends only on the represented matroid, not the actual weight coefficients.

**Geometric theorem.** Over an algebraically closed field \(k\) (of arbitrary characteristic), the reduced commuting-pair variety \(\mathcal C(L)=\{(x,y)\in L^2:[x,y]=0\}_{\mathrm{red}}\) is irreducible of dimension \(2d+m\) if \(m<2d\). If \(m\ge 2d\), it has exactly two irreducible components: the closure of the locus where the \(H\)-coordinates have no vanishing weight row, of dimension \(2d+m\), and the coordinate space \(E^2\) of dimension \(2m\). They have equal dimension precisely when \(m=2d\), and unequal dimensions when \(m>2d\).

## Assumptions and scope

The ground field is arbitrary for the geometric theorem, with irreducible components understood after passing to an algebraic closure. Uniformity requires that \(\operatorname{rank}\{\alpha_i:i\in S\}=\min(|S|,d)\) for every subset \(S\). Such weights need not exist over every finite field for every parameter pair; all statements are conditional on their existence. The finite-field formula concerns actual \(\mathbb F_q\)-rational commuting tuples of length \(r\ge1\), and the geometric theorem concerns the underlying reduced pair variety, not its scheme structure. The proof uses only determinant identities and linear algebra and is characteristic-independent.

## Proof

**Step 1: bracket equations.** Write the two input elements as \((h_a,u_a)\), \(a\in\{1,2\}\), where \(h_a\in H\) and \(u_a=(u_{ia})_{i=1}^m\in E\). Their bracket is zero exactly when
\[
\alpha_i(h_1)u_{i2}-\alpha_i(h_2)u_{i1}=0\quad(1\le i\le m).
\]
For \(r\) tuple entries, these equations assert that the \(r\)-tuple of radical coefficients in row \(i\) is proportional to \((\alpha_i(h_a))_{a=1}^r\), unless that latter row is zero, in which case all \(q^r\) choices are permitted.

**Step 2: exact arithmetic count.** Fix the \(H\)-coordinates. There are \(q\) radical-row choices when the weight row is nonzero, and \(q^r\) when it is zero. This equals \(q(1+(q^{r-1}-1)\mathbf1_{\{\alpha_i(h_a)=0\ \forall a\}})\). Multiply over the \(m\) weights, expand the product over \(S\subseteq[m]\), and sum the \(H\)-coordinates. The number annihilating the span of weights indexed by \(S\) is \(q^{r(d-\operatorname{rank}S)}\). The general matroid formula follows. Uniformity makes the rank \(\min(|S|,d)\) and grouping subsets by size proves the displayed binomial expression. At \(r=1\) it gives \(q^{m+d}\), as necessary.

**Step 3: the generic pair component.** Let \(X\subseteq\mathcal C(L)\) be the open subvariety where every weight row \(t_i=(\alpha_i(h_1),\alpha_i(h_2))\) is nonzero. For any choice of \((h_1,h_2)\) in the nonempty complement of the finitely many codimension-two linear subspaces \(t_i=0\), all radical rows have the unique form \(u_i=\lambda_i t_i\). Hence \(X\) is a trivial rank-\(m\) vector bundle over that irreducible open subset of \(H^2\), and \(Y=\overline X\) is irreducible of dimension \(2d+m\).

**Step 4: points with nonzero toral coordinate.** Suppose \((h_1,h_2)\ne(0,0)\) and let \(F=\{i:t_i=0\}\). If \(|F|\ge d\), uniformity forces both \(h_a=0\), a contradiction; thus \(|F|<d\) and the weights in \(F\) are independent. Choose \(v_1,v_2\in H\) with \((\alpha_i(v_1),\alpha_i(v_2))=u_i\) whenever \(i\in F\) and \(u_i\ne0\), while choosing a nonzero pair for any \(i\in F\) with \(u_i=0\). Such a choice exists by independence. Set \(h_a(\varepsilon)=h_a+\varepsilon v_a\). For \(i\in F\) with \(u_i\ne0\), keep \(u_i\) fixed, so \(u_i=\varepsilon^{-1}t_i(h(\varepsilon))\); for zero rows keep \(u_i(\varepsilon)=0\). For \(i\notin F\), choose the fixed scalar \(\lambda_i\) such that \(u_i=\lambda_i t_i(h)\), and set \(u_i(\varepsilon)=\lambda_i t_i(h(\varepsilon))\). Every resulting pair commutes, lies in \(X\) for generic nonzero \(\varepsilon\), and specializes to the original pair. Consequently \(\mathcal C(L)=Y\cup E^2\) set-theoretically. This also proves there can be at most two irreducible components.

**Step 5: closure criterion for the central space.** Let \(A\in k^{m\times d}\) have rows \(\alpha_i\), choose a full-row-rank matrix \(B\in k^{(m-d)\times m}\) satisfying \(BA=0\), and write \(t=m-d\). For \(U=(u_{ia})\in E^2\), let
\[
K(U)=\begin{pmatrix}B\operatorname{diag}(u_{*1})\\B\operatorname{diag}(u_{*2})\end{pmatrix},
\]
a \(2t\times m\) matrix. The column matroid of \(B\) is dual to that of \(A\), so it is uniform \(U_{t,m}\); in particular any \(t\) columns of \(B\) are independent.

If \(m<2d\), then \(2t\le m-1\). For each column index \(i\), partition \([m]\setminus\{i\}\) into two sets each containing at least \(t\) indices. Specializing \(u_{j1}=1,u_{j2}=0\) on one part and \(u_{j1}=0,u_{j2}=1\) on the other gives \(\operatorname{rank}K(U)_{\widehat i}=2t\). Thus for generic \(U\), deleting any one column leaves full row rank. The kernel of \(K(U)\) is then a positive-dimensional subspace not contained in any coordinate hyperplane. As \(k\) is infinite, it contains a vector \(s=(s_i)\) with all \(s_i\ne0\). Since \(K(U)s=0\), each vector \((s_i u_{ia})_{i=1}^m\) lies in the image of \(A\); choose \(v_a\in H\) with \(A v_a=(s_i u_{ia})_i\). Then \(h_a(\varepsilon)=\varepsilon v_a\), \(u_a(\varepsilon)=u_a\) gives a commuting pair whose weight rows are \(\varepsilon s_i u_i\), nonzero for generic \(U\) and \(\varepsilon\ne0\). It approaches the central pair \((0,U)\). Therefore a Zariski-dense open subset of \(E^2\) lies in \(Y\), so \(E^2\subseteq Y\): the variety is irreducible.

If \(m\ge2d\), then \(m\le2t\). Partition \([m]\) into two sets each of size at most \(t\), and assign row values \(u_i=(1,0)\) or \((0,1)\) accordingly. Uniformity of \(B\) makes the resulting \(K(U)\) full column rank \(m\). Thus full column rank holds on a nonempty open subset \(\Omega\subset E^2\), which can be chosen with all \(u_i\ne0\). At any commuting pair with \((h_1,h_2)\ne0\) and every radical row \(u_i\ne0\), the commutator equations give scalars \(s_i\) with \((\alpha_i(h_a))_{a=1,2}=s_i(u_{ia})_{a=1,2}\), setting \(s_i=0\) for vanishing weight rows. At least one \(s_i\) is nonzero because the weights span \(H^*\). The relations \(BA=0\) then imply \(K(U)s=0\). Thus \(K(U)\) cannot be full column rank at such a pair or any specialization with every radical row nonzero. In particular \(Y\cap\Omega=\varnothing\), so \(E^2\not\subseteq Y\). It is the second component. Dimensions from Step 3 and \(\dim E^2=2m\) give the equidimensionality boundary \(m=2d\). This exhausts all components.

## Verification

The companion standalone `verify.py` independently enumerates weight values and all radical row choices by testing the actual determinant equations in small finite fields. It checks nineteen parameter/arity configurations with dimensions both below and at/above the threshold. Run `python3 verify.py`; the exact success marker is `UNIFORM_METABELIAN_COMMUTING_OK 19`. The script's row-by-row enumeration is independent of the formula's subset expansion. The geometric proof is symbolic and works over algebraic closures; finite enumeration is not offered as a proof of geometric irreducibility.

## Relationship to prior work

Cagliero and Szechtman, arXiv:1408.2166v1 (public 2014-08-09; primary MSC 17B10), study indecomposable admissible uniserial modules for one-dimensional diagonal extensions of abelian Lie algebras. Its introduction, Proposition 3.1, Theorem 3.4, Theorem 3.8 and conclusion were inspected: those are classification statements about modules, not the algebra's intrinsic commuting-pair variety or all-arity rational-point count. The present theorem uses potentially higher-dimensional diagonal toral factors and a uniform-matroid condition. Goodwin and Röhrle, arXiv:1209.1289, concern nilradicals of Borel algebras, not this diagonal semidirect family. Matroid rank-generating identities themselves are classical; the contribution claimed here is the exact Lie-algebra arithmetic interpretation together with the geometric transition at \(m=2d\). The prior-work comparison does not certify historical priority.

## Limitations

The two-component classification is proved only when the weights realize the uniform matroid; it is not asserted for general weight matroids or for schemes with nilpotent structure. The all-arity formula counts ordered pairwise commuting tuples, not conjugacy orbits. Over a small finite field some uniform matroids are not representable, so those parameter choices have no corresponding algebra in this family. Unlocated literature on commuting varieties of solvable or arrangement Lie algebras could potentially imply a stronger version of this result. Independent mathematical validation has not been performed.

## References

1. L. Cagliero and F. Szechtman, *Indecomposable modules of 2-step solvable Lie algebras in arbitrary characteristic*, arXiv:1408.2166v1, 9 August 2014. https://arxiv.org/pdf/1408.2166
2. S. Goodwin and G. Röhrle, *On commuting varieties of nilradicals of Borel subalgebras of reductive Lie algebras*, arXiv:1209.1289v1, 7 September 2012. https://arxiv.org/abs/1209.1289
3. Standard facts on dual matroids, rank functions and uniform matroids are used only through their elementary linear-algebra formulations.
