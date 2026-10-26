# Retraction spectra and maximal-rank fluctuations of finite-field Heisenberg groups

## Finding

Let \(p\) be an odd prime, \(e\ge 2\), \(q=p^e\), and \(H_q=\operatorname{UT}_3(\mathbb F_q)\). All group retractions (idempotent endomorphisms) of \(H_q\) are classified below. Besides the trivial endomorphism and the identity, their images are precisely the graphs of \(\mathbb F_p\)-linear maps \(\beta:U\to\mathbb F_q\), where \(0\ne U\le\mathbb F_q^2\) is an \(\mathbb F_p\)-subspace contained in a one-dimensional \(\mathbb F_q\)-subspace. The graph is taken in the central-coordinate model in the next section. In particular, every proper nontrivial retract is elementary abelian of order \(p^r\) for some \(1\le r\le e\); no nontrivial proper retract is normal.

For \(1\le r\le e\), the numbers of distinct retract subgroups of order \(p^r\) and of idempotent endomorphisms with image order \(p^r\) are, respectively,
\[
S_{p,e}(r)=(p^e+1){e\brack r}_p p^{er},\qquad
R_{p,e}(r)=(p^e+1){e\brack r}_p p^{r(3e-r)}.
\]
The Gaussian coefficient \({e\brack r}_p\) counts \(r\)-dimensional \(\mathbb F_p\)-subspaces of \(\mathbb F_p^e\). The complete idempotent image-rank polynomial and total count are
\[
\mathcal E_{p,e}(t)=1+\sum_{r=1}^{e}R_{p,e}(r)t^r+t^{3e},\qquad
|\operatorname{Idem}(\operatorname{End}H_q)|=2+\sum_{r=1}^{e}R_{p,e}(r).
\]
Here the exponent of \(t\) is the base-\(p\) logarithm of the image order, so the identity contributes \(t^{3e}\).

There is also a nondegenerate growing-field limit. Choose an idempotent endomorphism uniformly among those with proper nontrivial image, write its image order as \(p^R\), and let \(D=e-R\). For each fixed integer \(s\ge0\), as \(e\to\infty\) with \(p\) fixed,
\[
\Pr(D=s)\longrightarrow \frac{w_p(s)}{\sum_{j=0}^{\infty}w_p(j)},\qquad
w_p(s)=\frac{p^{-2s^2}}{\prod_{j=1}^{s}(1-p^{-j})}.
\]
An empty product is one. Thus the rank defect remains tight and has an explicit discrete limiting law.

## Assumptions and scope

The field order is a **nonprime** odd prime power \(q=p^e\) with \(e\ge2\). The full group \(H_q\) has order \(p^{3e}\), and its derived subgroup equals its center, of order \(p^e\). To work in convenient coordinates, identify \(H_q\) with \(V\oplus Z\), where \(V=\mathbb F_q^2\) and \(Z=\mathbb F_q\), under the product
\[
(v,z)\cdot(w,t)=(v+w,z+t+\tfrac12\det(v,w)).
\]
This is isomorphic to the usual upper-unitriangular-matrix group by a central-coordinate change. The factor \(\tfrac12\) is defined because \(p\) is odd. A retraction means a group endomorphism \(F\) satisfying \(F^2=F\). Its image is a retract subgroup, and different retraction maps may have the same image. The subgroup graph of \(\beta:U\to Z\) means \(\{(u,\beta(u)):u\in U\}\). All linearity of \(U\), \(\beta\), and the maps in the proof is over \(\mathbb F_p\), unless specified otherwise.

## Proof

**Endomorphism coordinates.** The center and derived subgroup are both \(\{(0,z):z\in Z\}\), hence every endomorphism sends them into themselves. In a group of exponent \(p\) and nilpotency class two, with \(p\) odd, the underlying additive operation in these Baker–Campbell–Hausdorff coordinates is recovered group-theoretically by \(x+y=xy[x,y]^{-1/2}\). Therefore a homomorphism is \(\mathbb F_p\)-linear in additive coordinates and has the unique form
\[
F(v,z)=(Av,Bv+Tz),
\]
where \(A:V\to V\), \(B:V\to Z\), and \(T:Z\to Z\) are \(\mathbb F_p\)-linear. Preservation of commutators is equivalent to
\[
T(\det(v,w))=\det(Av,Aw)\quad\text{for all }v,w\in V.
\tag{1}
\]
Conversely, all such triples define group endomorphisms by the multiplication rule. Direct composition gives the exact retraction conditions
\[
A^2=A,\qquad T^2=T,\qquad BA+TB=B.
\tag{2}
\]

**Nonzero central action forces the identity.** Suppose \(F^2=F\) and \(T\ne0\). If \(0\ne v\in\ker A\), equation (1) gives \(T(\det(v,w))=0\) for all \(w\). But \(w\mapsto\det(v,w)\) surjects onto \(Z=\mathbb F_q\), forcing \(T=0\), a contradiction. Thus \(A\) is injective, hence invertible. Equations (2) yield \(A=I_V\). Equation (1), and surjectivity of the determinant pairing onto \(Z\), imply \(T=I_Z\). Finally \(BA+TB=B\) becomes \(2B=B\), so \(B=0\). The only such retraction is the identity.

**Zero central action.** If \(T=0\), equation (1) says \(\det(Av,Aw)=0\) for all \(v,w\). Therefore the \(\mathbb F_p\)-space \(U=\operatorname{im}A\) is contained in a single \(\mathbb F_q\)-line: any two nonzero elements of \(U\) must be \(\mathbb F_q\)-proportional. For \(U\ne0\), this \(\mathbb F_q\)-line is unique. Hence \(r=\dim_{\mathbb F_p}U\) satisfies \(1\le r\le e\). Condition \(A^2=A\) means that \(A\) is a projection onto \(U\), equivalently the choice of a direct-sum complement \(K=\ker A\) of \(U\) in \(V\). Condition \(BA=B\) means exactly that \(B=\beta A\) for a unique \(\mathbb F_p\)-linear map \(\beta:U\to Z\). Its image is \(\{(u,\beta(u)):u\in U\}\). Conversely, every such \(U,K,\beta\) satisfies (1) and (2), so this describes **all** nontrivial proper retractions. If \(U=0\), then \(A=0\), and (2) forces \(B=0\); this is the trivial endomorphism.

**Counting.** There are \(q+1=p^e+1\) projective \(\mathbb F_q\)-lines in \(V\). Inside one such line are \({e\brack r}_p\) choices for \(U\), counted once because the containing \(\mathbb F_q\)-line is unique for \(U\ne0\). For any such \(U\), the number of complementary \(\mathbb F_p\)-subspaces \(K\) in the \(2e\)-dimensional \(\mathbb F_p\)-space \(V\) is \(p^{r(2e-r)}\): once a complement is fixed, every other complement is the graph of a linear map from that complement to \(U\). Finally there are \(p^{er}\) maps \(\beta:U\to Z\). Their independent product gives \(R_{p,e}(r)\). Omitting the choice of complement gives \(S_{p,e}(r)\). Since every proper nontrivial image is disjoint from the center, but the commutators of any noncentral element with the whole group sweep out the center, such an image cannot be normal. The trivial subgroup and the full group are the only normal retracts.

**Limiting law.** Put \(s=e-r\). On dividing the \(r\)-th summand by \((p^e+1)p^{2e^2}\), the Gaussian-product identity gives exactly
\[
\frac{R_{p,e}(e-s)}{(p^e+1)p^{2e^2}}
=p^{-2s^2}\frac{\prod_{j=e-s+1}^{e}(1-p^{-j})}{\prod_{j=1}^{s}(1-p^{-j})},
\qquad 0\le s\le e-1.
\]
For fixed \(s\), the numerator product tends to one. All summands are dominated by \(p^{-2s^2}/\prod_{j=1}^{\infty}(1-p^{-j})\), a summable sequence because its denominator is positive. Dominated convergence for the normalized finite sums yields the stated limiting distribution. This also proves tightness of \(D\).

## Verification

Run `python3 verify.py` using only the standard library. Direct generator-image enumeration of every endomorphism of the prime-field groups in characteristics \(3\), \(5\), and \(7\) provides boundary checks outside the stated nonprime-field scope. Their idempotent image-order histograms are \(\{1:1,3:36,27:1\}\), \(\{1:1,5:150,125:1\}\), and \(\{1:1,7:392,343:1\}\).

For the in-scope field \(\mathbb F_9\), independently represent it as \(\mathbb F_3[\xi]/(\xi^2+1)\). The verifier constructs all \(\mathbb F_3\)-linear projections to subspaces contained in \(\mathbb F_9\)-lines, deduplicates these projections by their images on a fixed \(\mathbb F_3\)-basis, and checks \(1080\) rank-one projections and \(810\) rank-two projections. Including their central graph maps yields exactly \(9720\) and \(65610\) proper retractions of respective image orders \(3\) and \(9\); adding the trivial and identity maps gives \(75332\). A deterministic sample of \(20000\) group-product and idempotence checks uses actual \(\mathbb F_9\) multiplication. The verifier prints `VERIFY_OK`. These finite checks corroborate but do not prove the unrestricted theorem.

## Relationship to prior work

Anil Kumar and Pradhan (2019, Theorem \(\Omega\) and Section 5) determine the endomorphisms and their total number for extraspecial exponent-\(p\) groups, including the Heisenberg group over the **prime** field. In particular, their explicit endomorphism parametrization subsumes the prime-field special case of the present counting approach. Their Example 6.2 specifically identifies Heisenberg groups over extension fields as a setting for further endomorphism-semigroup questions. Here the center has size \(p^e>p\), so the group is not extraspecial. The new assertion is a **retraction-specific** classification with a Gaussian rank census and growing-extension-degree law, not an enumeration of all endomorphisms and not a solution of all their questions.

Research on *strong retracts* concerns a distinct universal condition involving all containing groups; it does not classify retractions of this fixed finite group. Centralizer and commutativity invariants of finite Heisenberg groups likewise do not, without an additional implication, determine idempotent endomorphism counts or their images. An equivalent classification elsewhere under nonstandard terminology remains a residual publication-priority risk.

## Limitations

The theorem requires odd characteristic and extension degree at least two. It does not assert any formula for characteristic two or any higher-dimensional Heisenberg group \(H_{2n+1}(\mathbb F_q)\) with \(n>1\). For prime fields the displayed counting argument specializes to a case already implicit in the 2019 endomorphism parametrization; it is used only for computational calibration. The result concerns retracts, not the complete endomorphism monoid. The proof is self-contained; computational checks alone do not certify every finite field. Publication priority has not been independently audited.

## References

1. C. P. Anil Kumar and S. S. Pradhan, *On the Endomorphism Semigroups of Extra-special \(p\)-groups and Automorphism Orbits*, arXiv:1908.00331v1 (first public August 1, 2019); later *International Journal of Group Theory* 11 (2022), 201–220. https://arxiv.org/abs/1908.00331 ; https://arxiv.org/html/1908.00331v2 . Relevant passages: Theorem \(\Omega\), Theorem 5.3, Example 6.2.
2. *Finite normal subgroups of strongly verbally closed groups*, *Journal of Group Theory*, DOI 10.1515/jgth-2023-0015. https://doi.org/10.1515/jgth-2023-0015 . The different notion of strong retract is distinguished from an ordinary retract.
