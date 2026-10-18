# A characteristic-two deficit for restricted Rota–Baxter operators on toral almost-abelian Lie algebras

## Finding
Let \(K\) be any field of characteristic \(p>0\). Let \(V\) have finite dimension \(n\ge1\), and let \(T\in\mathrm{GL}(V)\) satisfy \(T^p=T\). The split almost-abelian Lie algebra \(L_T=Ke\ltimes_T V\) has \([e,v]=Tv\) and \([V,V]=0\). Since \(T\) is invertible, its derived ideal is intrinsically \(V=[L_T,L_T]\).

The canonical restricted structure is \(e^{[p]}=e\) and \(v^{[p]}=0\) for \(v\in V\), with the \(p\)-map on sums determined by the restricted Lie axioms. For any linear \(R:L_T\to V\), write uniquely \(R(e)=u\) and \(R(v)=Sv\), where \(u\in V\) and \(S\in\operatorname{End}_K(V)\).

**Theorem.** The operator \(R\) satisfies the weight-zero Rota–Baxter identity exactly when \(STS=0\). It is restricted in the graph sense exactly when
\[
STS=0\quad\text{and}\quad\begin{cases}STu=0,&p=2,\\\text{no additional condition},&p>2.\end{cases}
\]
With \(F=ST\), these conditions are \(F^2=0\) and, in characteristic two only, \(Fu=0\).

Over \(K=\mathbb F_q\), define \(N_{n,r}(q)={n\brack r}_q{n-r\brack r}_q|\mathrm{GL}_r(\mathbb F_q)|\) for \(0\le r\le\lfloor n/2\rfloor\), where \({a\brack b}_q\) is the Gaussian binomial coefficient. Then
\[
|\operatorname{RB}_V(L_T)|=q^n\sum_{r=0}^{\lfloor n/2\rfloor}N_{n,r}(q),
\]
while the number of graph-restricted operators is
\[
|\operatorname{RRB}_V(L_T)|=\begin{cases}
q^n\sum_r N_{n,r}(q),&p>2,\\
\sum_r q^{n-r}N_{n,r}(q),&p=2.
\end{cases}
\]
Thus both counts are independent of the admissible operator \(T\). For \(n\ge2\), the characteristic-two restricted class is strictly smaller. For instance, at \(n=2\) there are \(q^4\) ordinary operators but only \(q^3+q^2-q\) restricted ones when \(q\) is even.

## Assumptions and scope
The exponent \(p\) is the characteristic of \(K\), not necessarily its cardinality. The condition \(T^p=T\) together with invertibility makes \(T\) semisimple with eigenvalues in the prime field's nonzero elements. The corresponding restricted Lie structure exists: embed \(L_T\) into the associative matrix Lie algebra by sending \(ae+v\) to \(\begin{psmallmatrix}aT&v\\0&0\end{psmallmatrix}\). The \(p\)-th matrix power stays in this subalgebra because \(T^p=T\) and \(T^{p-1}=I\). In particular all of \(V\) has zero restricted \(p\)-power.

A *weight-zero Rota–Baxter operator* obeys \([Rx,Ry]=R([Rx,y]+[x,Ry])\) for all \(x,y\). The exact restricted convention is: its graph \(\Gamma_R=\{(x,Rx):x\in L_T\}\) is a restricted Lie subalgebra of \(L_T^{\rm ab}\rtimes_{\operatorname{ad}}L_T\), where the first copy is abelian with zero \(p\)-map. This convention is essential; other restricted-operator conventions occur in the literature. The theorem classifies only operators with image inside \(V\), rather than all linear operators on \(L_T\).

## Proof
**Ordinary identity.** Every \(Rx\) lies in the abelian ideal \(V\), so \([Rx,Ry]=0\). Since \([R(e),v]=0\) and \([e,R(v)]=TSv\), evaluation at \((e,v)\) requires \(R(TSv)=STS v=0\). All other basis pairs impose nothing new. Bilinearity proves the equivalence \(R\in\operatorname{RB}_V(L_T)\Longleftrightarrow STS=0\).

**Restricted graph condition.** The restricted semidirect product has the \(p\)-map
\[
(x,z)^{[p]}=\big((\operatorname{ad}z)^{p-1}x,\ z^{[p]}\big)
\]
when the first Lie ideal is abelian with zero \(p\)-map; this follows by the usual restricted-semilinear action formula, or by taking \(p\)-th powers of upper block-triangular matrices for the action. For a graph element \((x,Rx)\), closure is therefore equivalent to
\[
R\big((\operatorname{ad}Rx)^{p-1}x\big)=(Rx)^{[p]}.
\]
The right-hand side is zero because \(Rx\in V\). If \(y\in V\), then \(\operatorname{ad}y\) sends \(e\) to \(-Ty\) and kills \(V\), so \((\operatorname{ad}y)^2=0\). When \(p>2\), the graph is consequently always closed under the \(p\)-map once the ordinary Rota–Baxter identity holds.

For \(p=2\), take \(x=te+v\), so \(Rx=tu+Sv\). Then
\[
R([Rx,x])=-t\,ST(tu+Sv)=-t^2STu-t\,STS v.
\]
The second term vanishes by the ordinary condition. The remaining expression is zero for all \(t,v\) precisely when \(STu=0\), as seen by choosing \(t=1\). This proves the characteristic dichotomy without assuming \(K\) is finite, perfect, or algebraically closed.

**Finite-field enumeration.** Since \(T\) is invertible, put \(F=ST\). The equation \(STS=0\) is equivalent to \(F^2=0\), and the extra characteristic-two condition is exactly \(Fu=0\). A square-zero \(F\) has rank \(r\le\lfloor n/2\rfloor\). To count rank \(r\), choose its image \(W\) in \({n\brack r}_q\) ways, its kernel \(U\supset W\) of dimension \(n-r\) in \({n-r\brack r}_q\) ways, and the induced isomorphism \(V/U\xrightarrow{\sim}W\) in \(|\mathrm{GL}_r(\mathbb F_q)|\) ways. This proves the factor \(N_{n,r}(q)\). For each such \(F\), there are \(q^n\) choices of \(u\) ordinarily and for odd \(p\), but just \(|\ker F|=q^{n-r}\) choices when \(p=2\). Summing proves both formulas and independence of \(T\). When \(n\ge2\) and \(q\) is even, rank-one square-zero maps exist, and their positive contribution to the difference is \((q^n-q^{n-1})N_{n,1}(q)>0\).

## Verification
The standalone `verify.py` is dependency-free and reconstructs the Lie brackets and graph closure equation independently of the counting formula. It enumerates every ideal-valued linear operator in dimensions \(n=1,2,3\) over \(\mathbb F_2\), in dimension \(n=2\) over \(\mathbb F_4\), and in dimension \(n=2\) over \(\mathbb F_3\) and \(\mathbb F_5\). The latter examples use toral operators with distinct eigenvalues. It checks the original Rota–Baxter identity on basis pairs, graph \(p\)-closure on every Lie-algebra element for candidate operators, and compares the independently enumerated counts to the Gaussian-binomial formulas.

The verified totals are: \(n=2,q=2\), ordinary/restricted \(16/10\); \(n=3,q=2\), \(176/92\); \(n=2,q=4\), \(256/76\); \(n=2,q=3\), \(81/81\); and \(n=2,q=5\), \(625/625\). The full arbitrary-field statements are proved symbolically and are not inferred from the finite tests.

## Relationship to prior work
Li and Ou's 2026 work develops restricted Rota–Baxter Lie algebras of arbitrary weight and the graph-subalgebra characterization that motivates the precise definition here. It does not assert the above image-in-derived-ideal parametrization or rank-resolved finite-field census in the accessible abstract. The full preprint was not accessible for complete comparison; possible overlap inside that source remains a residual risk. Mao and Chen's 2024 treatment of restricted Rota–Baxter operators in characteristic two concerns Nijenhuis/Kupershmidt structures and gives a restricted identity, but does not present this natural-family classification or finite-field counts in the materially inspected sections. The counting of square-zero matrices by image, kernel and quotient is classical and is used as an ingredient rather than claimed as novel.

## Limitations
This concerns the specified graph-restricted convention and the canonical restricted structure for \(T^p=T\). It does not classify operators whose image is not contained in the derived ideal, singular \(T\), or other restricted structures on other Lie algebras. The source comparison is not an independent priority determination, and some potentially relevant full texts were inaccessible. The enumeration is exact for the stated family and does not establish a general classification for arbitrary almost-abelian Lie algebras.

## References
1. Yunnan Li and Ke Ou, *On restricted Rota-Baxter Lie algebras of arbitrary weight*, arXiv:2606.19244, first posted 17 June 2026, https://arxiv.org/abs/2606.19244.
2. Dan Mao and Liangyun Chen, *Restricted Kupershmidt-(dual-)Nijenhuis structures on ResLieRep pairs in characteristic 2*, author-shared manuscript (2024), Definition 2.3; https://www.researchgate.net/publication/382335995_RESTRICTED_HOM-KUPERSHMIDT-NIJENHUIS_STRUCTURES_ON_RESHLIEREP_PAIRS_IN_CHARACTERISTIC_2.
