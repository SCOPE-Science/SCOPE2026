# Exact conjugacy-class-size spectra for four-block unipotent radicals with two scalar blocks

## Finding

Let \(q\) be any prime power and let \(a,c\geq1\). The four-block unipotent radical \(G_{a,c}(q)\) of \(\operatorname{GL}_{a+c+2}(\mathbb F_q)\) has block dimensions \((a,1,1,c)\). For every \(s\geq0\), write \(A_s\) for the number of its elements whose conjugacy class has cardinality \(q^s\). The following explicit polynomial simultaneously determines **all** numbers \(A_s\), not only their sum weighted by inverse class size.

Define \(n_d(i,\epsilon)\), with \(i\in\{0,1,2\}\) and \(\epsilon\in\{0,1\}\), by
\[
\begin{aligned}
n_d(0,0)&=1,\\
n_d(1,0)&=q^d-1,\\
n_d(1,1)&=q(q^d-1),\\
n_d(2,1)&=(q^d-1)(q^d-q),
\end{aligned}
\]
with all other values zero. Then \(A_s=[z^s]F_{a,c,q}(z)\), where
\[
\begin{aligned}
F_{a,c,q}(z)=q^{ac}\Bigg[&
\sum_{i,j=0}^{2}\sum_{\epsilon,\delta=0}^{1}
n_a(i,\epsilon)n_c(j,\delta)
 z^{\mathbf1_{\epsilon+\delta>0}+ic+aj-ij}\\
&+(q-1)q^{a+c}
\sum_{\epsilon,\delta=0}^{1}
(q^a-1)^\epsilon(q^c-1)^\delta
z^{a+c+\epsilon c+\delta a-\epsilon\delta}\Bigg].
\end{aligned}
\]
In particular, the number of conjugacy classes **of size** \(q^s\) is exactly \(q^{-s}[z^s]F_{a,c,q}(z)\), and the total class number is \(F_{a,c,q}(q^{-1})\). The formula holds uniformly in both outer block dimensions and in every field characteristic. It specializes to the classical four-by-four unitriangular group when \(a=c=1\); its new intended scope is the complete element class-size spectrum throughout the two-parameter family, not the already-known total class count in small cases.

## Assumptions and scope

Fix an arbitrary finite field \(k=\mathbb F_q\), vector spaces \(U=k^a\) and \(W=k^c\), and let \(J\) be the nilpotent algebra of strict upper-block matrices with block dimensions \((a,1,1,c)\). Identify its six nonzero blocks, in order \((12),(23),(34),(13),(24),(14)\), with
\[
J=U\oplus k\oplus W\oplus U\oplus W\oplus(U\otimes W).
\]
Multiplication is ordinary block-matrix multiplication, and \(G_{a,c}(q)=1+J\). Thus \(\dim_k J=1+2a+2c+ac\), and \(|G_{a,c}(q)|=q^{1+2a+2c+ac}\). The same radical is the positive-length path algebra of the four-vertex directed chain with \(a\) parallel arrows on the first edge and \(c\) on the last edge. No restriction is imposed on the ratio of \(a\) and \(c\), and the statement counts elements of each class size, rather than individual orbit representatives.

## Proof

Write \(x=(u,b,w,p,t,r)\in J\), with \(u,p\in U\), \(w,t\in W\), \(b\in k\) and \(r\in U\otimes W\), and likewise \(y=(u',b',w',p',t',r')\). The only possibly nonzero components of the additive commutator \([x,y]=xy-yx\) are
\[
\begin{aligned}
[x,y]_{13}&=ub'-bu',\\
[x,y]_{24}&=bw'-b'w,\\
[x,y]_{14}&=u\otimes t'+p\otimes w'-u'\otimes t-p'\otimes w.
\end{aligned}
\]
The top block \(r\) is central. For every \(x\), the map \(\operatorname{ad}_x:y\mapsto[x,y]\) is \(k\)-linear, and \((1+x)(1+y)=(1+y)(1+x)\) exactly when \(\operatorname{ad}_x(y)=0\). Consequently
\[
|(1+x)^{G_{a,c}(q)}|=\frac{|G_{a,c}(q)|}{|C_{G_{a,c}(q)}(1+x)|}=q^{\operatorname{rank}(\operatorname{ad}_x)}.
\]

**Case \(b\ne0\).** The first two displayed components yield a surjective linear map from \(U\oplus k\oplus W\) to \(U\oplus W\), of rank \(a+c\). Its kernel consists of scalar multiples of \((u,b,w)\). On this kernel and on freely varying \((p',t')\), the final commutator component has image exactly
\[
u\otimes W+U\otimes w;
\]
the possible extra vector arising from a scalar multiple of \((u,b,w)\) is \(p\otimes w-u\otimes t\), which already lies in that space. If \(\epsilon=\mathbf1_{u\ne0}\) and \(\delta=\mathbf1_{w\ne0}\), the latter space has dimension \(\epsilon c+\delta a-\epsilon\delta\). Therefore
\[
\operatorname{rank}(\operatorname{ad}_x)
=a+c+\epsilon c+\delta a-\epsilon\delta.
\]
There are \(q-1\) choices for \(b\), \(q^{a+c}\) choices for \((p,t)\), \((q^a-1)^\epsilon(q^c-1)^\delta\) choices for \((u,w)\) with this zero/nonzero status, and \(q^{ac}\) choices for \(r\), yielding the second sum in \(F_{a,c,q}\).

**Case \(b=0\).** The first two components, as a joint map of \(b'\), have rank \(\eta=\mathbf1_{u\ne0\text{ or }w\ne0}\). If \(\eta=1\), their joint kernel forces \(b'=0\); if \(\eta=0\), arbitrary \(b'\) contributes nothing to the final component. Put \(i=\dim\langle u,p\rangle\) and \(j=\dim\langle w,t\rangle\). The final component's image is exactly
\[
\langle u,p\rangle\otimes W+U\otimes\langle w,t\rangle,
\]
of dimension \(ic+aj-ij\) by the elementary intersection identity for tensor product subspaces. Thus
\[
\operatorname{rank}(\operatorname{ad}_x)=\eta+ic+aj-ij.
\]
For \(d\ge1\), the number of ordered pairs \((v_1,v_2)\in k^d\oplus k^d\) with \(\dim\langle v_1,v_2\rangle=i\) and \(\mathbf1_{v_1\ne0}=\epsilon\) is precisely \(n_d(i,\epsilon)\): the nonzero first vector gives \(q^d-1\) possibilities; the second vector has \(q\) possibilities in its span and \(q^d-q\) outside it. Multiplying independent choices for \((u,p)\) and \((w,t)\), along with \(q^{ac}\) free central blocks, gives the first sum. The cases exhaust \(J\), proving the theorem. Burnside's identity gives the displayed class-number specialization. All steps use field-linear dimension and elementary counting, hence apply to nonprime finite fields as well.

## Verification

The standalone script `artifacts/check.py` constructs a path-multiplication table independently from the formula, forms every adjoint matrix over selected prime fields, computes its rank by modular Gaussian elimination, and compares every rank coefficient to the closed form. It examines \(10\) configurations, including outer dimensions up to \((3,2)\), with \(10963\) independently computed adjoint matrices; it also directly counts commuting ordered pairs in three of the cases, independently testing Burnside's class-number identity. Replay with `python3 artifacts/check.py`; expected terminal marker: `FOUR_VERTEX_QUIVER_CLASS_SPECTRA_CHECKS_PASSED cases=10 independent_adjoint_matrices=10963`. Full finite output is in `artifacts/checker_output.txt`. These enumerations are not substitutes for the all-prime-power proof.

## Relationship to prior work

Hennecart and Perry, *A Quiver Analogue of Higman's Conjecture*, arXiv:2208.07738v1 (16 August 2022), give explicit radical commuting-pair counts for quivers with no oriented path longer than two; see Sections 3–5 and their treatment of path-length-two configurations. The family here is the first four-vertex directed chain, with oriented paths of length three, and this result supplies its elementwise class-size distribution rather than only the number of commuting pairs.

For the four-by-four unitriangular specialization, earlier work of Vera-López and Arregi (as reviewed in Hennecart–Perry) already counts conjugacy classes, and Pak–Soffer provide recursive methods for pattern-group class numbers. Their counts are not claimed as new. Yang Yang, *A Geometric Approach to Polynomial Property for Pattern Subgroups in* \(\mathrm U_{a,b,c,d}\), DOI 10.1017/S1446788725101328 (online 19 November 2025), states character-number formulae by irreducible degree for all four-block pattern subgroups, including this four-block radical. Those character counts already address class-number information, but irreducible character degrees are not element conjugacy-class sizes; the present claim is exclusively about the full latter spectrum. The article's accessible abstract was examined, but its full paper could not be obtained in this review; possible indirect deductions or overlap remain a source-risk.

## Limitations

The result is a family-specific elementary count; it does not assert a general formula for arbitrary four-block dimensions, arbitrary pattern subgroups, or higher nilpotency class. The connection to earlier character-degree counts is not an equivalence of invariants. No priority or uniqueness claim is made for \(a=c=1\) or for the total class number alone. Sources outside the available full-text corpus could contain an equivalent element-spectrum formula. Mathematical verification here is the finite mathematical proof and self-review; independent audit has not been performed.

## References

1. L. Hennecart and N. Perry, *A Quiver Analogue of Higman's Conjecture*, arXiv:2208.07738v1, 16 August 2022. https://arxiv.org/abs/2208.07738.
2. Y. Yang, *A Geometric Approach to Polynomial Property for Pattern Subgroups in* \(\mathrm U_{a,b,c,d}\), *J. Aust. Math. Soc.* 120 (2026), 287–304; published online 19 November 2025. DOI: 10.1017/S1446788725101328.
3. I. Pak and A. Soffer, pattern-group recursive class enumeration, as described in Hennecart–Perry, Introduction (reference [PS15]).
4. A. Vera-López and J. M. Arregi, classifications and counts for small unitriangular groups, as described in Hennecart–Perry, Introduction (references [VLA92], [VLA95], [VLA03]).
