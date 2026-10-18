# Sharp global directional-derivative remainder for rank-one real Hilbert tensors

## Finding
Let \(H_1,H_2\) be nonzero real Hilbert spaces, finite- or infinite-dimensional, and let \(S_1(H_1,H_2)\) be the trace-class operators with nuclear norm \(\|\cdot\|_1\). For unit vectors \(u\in H_2\) and \(v\in H_1\), write \(P=u\otimes v\), meaning \(Px=\langle x,v\rangle u\). Define the exact one-sided norm derivative
\[D_P(A)=\lim_{h\downarrow0}\frac{\|P+hA\|_1-1}{h}.\]
For every \(A\in S_1(H_1,H_2)\),
\[D_P(A)=\langle Av,u\rangle+\|(I-uu^*)A(I-vv^*)\|_1.\]
The global deviation modulus, with a unit trace-class perturbation constraint, is
\[\Omega_P(t)=\sup_{\|A\|_1\le1}\left\{\frac{\|P+tA\|_1-1}{t}-D_P(A)\right\},\qquad t>0.\]
If at least one Hilbert space has dimension at least two, then
\[\boxed{\Omega_P(t)=\begin{cases}t/2,&0<t\le2,\\ 2-2/t,&t\ge2.\end{cases}}\]
If both spaces have dimension one, then
\[\boxed{\Omega_P(t)=\begin{cases}0,&0<t\le1,\\ 2-2/t,&t\ge1.\end{cases}}\]
In particular the non-scalar sharp uniform remainder for the unscaled norm is \(t^2/2\) throughout \(0<t\le2\). All constants are attained by rank-one perturbations.

## Assumptions and scope
All Hilbert spaces and operators are **real**; no separability or dimension bound is imposed. \(H_1\) is the operator domain, \(H_2\) its codomain. The tensor product \(H_2\widehat\otimes_\pi H_1\) is identified isometrically with \(S_1(H_1,H_2)\). Rank-one tensors \(u\otimes v\) are normalized with both factors of norm one. The dual of the real trace class is the space of bounded operators \(B(H_1,H_2)\), paired by \(\langle B,A\rangle=\operatorname{Tr}(B^*A)\), and the trace norm is its support function over contractions.

## Proof
**1. Derivative.** Set \(Q_u=I-uu^*\) and \(Q_v=I-vv^*\). The supporting contraction face at \(P\) is
\[J(P)=\{B:\|B\|\le1,\ \langle Bv,u\rangle=1\}.\]
By equality in Cauchy--Schwarz and in the contraction bound, each \(B\in J(P)\) satisfies \(Bv=u\) and \(B^*u=v\), hence relative to \(\mathbb Rv\oplus v^\perp\) and \(\mathbb Ru\oplus u^\perp\), it is \(1\oplus B_0\), where \(\|B_0\|\le1\). Thus
\[\sup_{B\in J(P)}\langle B,A\rangle=\langle Av,u\rangle+\|Q_uAQ_v\|_1.\]
The right derivative of the continuous convex trace norm is this support function: indeed dual maximizers for \(P+hA\) have weak-operator cluster points as \(h\downarrow0\), all in \(J(P)\); alternatively this is the standard support-function directional-derivative formula. This proves the expression for \(D_P(A)\).

**2. A sharp contraction-completion lemma.** Given a real contraction \(B:H_1\to H_2\), put \(s=\langle Bv,u\rangle\in[-1,1]\). There exists \(C\in J(P)\) such that
\[\|B-C\|\le\sqrt{2(1-s)}.\]
To prove it, use the Julia (Halmos) orthogonal dilation
\[U=\begin{pmatrix}B&(I-BB^*)^{1/2}\\ (I-B^*B)^{1/2}&-B^*\end{pmatrix}:H_1\oplus H_2\longrightarrow H_2\oplus H_1.\]
The defect-operator intertwining identity makes \(U\) a surjective isometry. Let \(x=(v,0)\) in the domain and \(y=(u,0)\) in the codomain. Both \(Ux,y\) are unit vectors and \(\langle Ux,y\rangle=s\). There is an orthogonal operator \(W\) on the codomain carrying \(Ux\) to \(y\) and satisfying
\[\|W-I\|=\|Ux-y\|=\sqrt{2(1-s)}.\]
For non-collinear vectors take their planar rotation; if they are equal take the identity; if opposite take the reflection on their line. Now \(V=WU\) is an isometry carrying \(x\) to \(y\), so \(V^*y=x\). The compression \(C=P_{H_2}V|_{H_1}\) is a contraction satisfying \(Cv=u\) and \(C^*u=v\), hence belongs to \(J(P)\). By compression, \(\|B-C\|\le\|U-V\|=\|I-W\|\). This proves the lemma, including the one-dimensional and infinite-dimensional cases.

**3. Universal upper bound.** For any \(A\) with \(\|A\|_1\le1\) and any dual contraction \(B\), apply the preceding lemma and \(D_P(A)\ge\langle C,A\rangle\):
\[\langle B,P+tA\rangle-1-tD_P(A)\le s-1+t\|B-C\|\|A\|_1\le s-1+t\sqrt{2(1-s)}.\]
Take the supremum over \(B\). With \(r=\sqrt{2(1-s)}\in[0,2]\), the upper bound is
\[\|P+tA\|_1-1-tD_P(A)\le\max_{0\le r\le2}\big(tr-r^2/2\big)=\begin{cases}t^2/2,&0<t\le2,\\2t-2,&t\ge2.\end{cases}\]
Division by \(t\) gives the claimed upper bounds.

**4. Sharp perturbations for non-scalar spaces.** If \(\dim H_1\ge2\), choose \(w\perp v\), \(\|w\|=1\). For each \(0<t\le2\), let
\[A_t=u\otimes\big(-\tfrac t2v+\sqrt{1-t^2/4}\,w\big).\]
This is rank one of trace norm one, its off-corner block \(Q_uA_tQ_v\) vanishes, and \(D_P(A_t)=-t/2\). Moreover
\[\|P+tA_t\|_1^2=(1-t^2/2)^2+t^2(1-t^2/4)=1.\]
Therefore the remainder divided by \(t\) is exactly \(t/2\). If \(\dim H_1=1\) and \(\dim H_2\ge2\), interchange the roles: take \(A_t=(-tu/2+\sqrt{1-t^2/4}\,z)\otimes v\), with \(z\perp u\). For every \(t\ge2\), take \(A=-P\), giving \(\|P+tA\|_1=t-1\), \(D_P(A)=-1\), and exact deviation \(2-2/t\).

**5. Scalar exception.** When both dimensions equal one, identify \(P\) with \(1\) and \(A\) with a scalar \(a\in[-1,1]\). Then \(D_P(A)=a\). For \(t\le1\), \(|1+ta|=1+ta\), so the deviation is zero. For \(t>1\), the largest deviation is obtained at \(a=-1\) and equals \(2-2/t\). This finishes all cases.

## Verification
The accompanying standalone program `verify.py` checks rational sharpness witnesses, the scalar boundary case, unit-norm dilation/completion identities in finite real matrices, and numerical upper bounds against randomly chosen trace-norm-unit matrices with multiple rectangular shapes and parameters. Its experiments are **not** the proof of the infinite-dimensional theorem: that proof is the contraction-completion argument and duality above.

## Relationship to prior work
Dantas, Jung, Mazzitelli and Rodríguez (arXiv:2209.01767v1, first public 2022-09-05), Theorem C(iii), prove uniform strong subdifferentiability at elementary tensors of Hilbert-space projective tensor products. Their proof invokes qualitative Bishop--Phelps--Bollobás and micro-transitivity arguments (Proposition 4.3 and Theorem 4.5). The present calculation quantifies the **complete, all-scale optimal directional-derivative remainder** for two factors, includes rectangular and infinite-dimensional cases, exhibits rank-one extremizers, and distinguishes the scalar exception. The antecedent qualitative assertion does not itself state this optimal profile. Dantas, Kim, Lee and Mazzitelli (arXiv:1905.08483) study related local properties for other tensor norms; only their abstract was accessible for this comparison.

## Limitations
Only the real Hilbert setting and the trace/projective norm are asserted; neither complex scalar behavior nor higher-order tensor powers is established here. The numerical verifier samples finite dimensions and cannot certify an infinite-dimensional theorem. Related unpublished or insufficiently indexed sharp perturbation estimates might already imply this result; this bibliographic possibility remains open. Independent external validation has not been performed.

## References
1. S. Dantas, M. Jung, M. Mazzitelli, J. T. Rodríguez, *On the strong subdifferentiability of the homogeneous polynomials and (symmetric) tensor products*, arXiv:2209.01767v1 (2022), especially Theorem C(iii), Proposition 4.3, Section 4.2. https://arxiv.org/pdf/2209.01767
2. S. Dantas, S. K. Kim, H. J. Lee, M. Mazzitelli, *Strong subdifferentiability and local Bishop--Phelps--Bollobás properties*, arXiv:1905.08483 (2019), background. https://arxiv.org/abs/1905.08483
