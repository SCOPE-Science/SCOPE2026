# Paired-domination polynomials reconstruct finite local total graphs

## Finding

Let \(R\) be a finite commutative local ring that is not a field, with maximal ideal \(M\), \(q=|R/M|\), and \(s=|M|\). Let \(T_\Gamma(R)\) be the total graph, and let \(D_{\mathrm{pr}}(T_\Gamma(R),x)\) count paired dominating sets by cardinality. Define
\[A_s(x)=\sum_{j\ge1}\binom{s}{2j}x^{2j}\]
and
\[B_s(x)=\sum_{j=1}^{s}\binom{s}{j}^2x^{2j}.\]
Then
\[D_{\mathrm{pr}}(T_\Gamma(R),x)=A_s(x)^q\]
when \(\operatorname{char}(R/M)=2\), while
\[D_{\mathrm{pr}}(T_\Gamma(R),x)=A_s(x)B_s(x)^{(q-1)/2}\]
when \(\operatorname{char}(R/M)\) is odd. Consequently
\[\gamma_{\mathrm{pr}}(T_\Gamma(R))=\gamma_t(T_\Gamma(R))=\begin{cases}2q,&\operatorname{char}(R/M)=2,\\q+1,&\operatorname{char}(R/M)\text{ odd}.\end{cases}\]
Moreover the paired-domination polynomial alone recovers \(q\), \(s\), and the residue-characteristic parity, and hence determines \(T_\Gamma(R)\) up to graph isomorphism within the class of finite commutative local nonfields.

This also classifies every paired dominating set. In residue characteristic \(2\), each residue coset is a clique and a paired dominating set chooses an even, nonzero number of at least two vertices from every coset. In odd residue characteristic, the maximal ideal is a clique while every pair of opposite nonzero residue cosets forms a complete bipartite component; a paired dominating set chooses an even subset of size at least two in the maximal-ideal clique and chooses the same positive number of vertices from the two sides of every bipartite component.

## Assumptions and scope

The total graph \(T_\Gamma(R)\) has vertex set \(R\), with distinct \(x,y\) adjacent exactly when \(x+y\in Z(R)\). For a finite local ring, \(Z(R)=M\). Since \(R\) is finite local, it has finite composition length and its unique simple module is \(R/M\); hence \(|R|=q^\ell\) and \(s=|M|=q^{\ell-1}\) for some \(\ell\ge2\). In particular, \(s\) is even exactly when the residue characteristic is \(2\).

A paired dominating set is a dominating set whose induced subgraph contains a perfect matching. The polynomial \(D_{\mathrm{pr}}(G,x)=\sum_k d_{\mathrm{pr}}(G,k)x^k\) records the number of paired dominating sets of each size.

## Proof

Anderson and Badawi's structure theorem for the total graph when \(Z(R)\) is an ideal gives, in the present local case,
\[
T_\Gamma(R)\cong
egin{cases}
qK_s,&2\in M,\
K_s\sqcup \dfrac{q-1}2K_{s,s},&2
otin M.
\end{cases}
	ag{1}
\]
The first condition is equivalent to residue characteristic \(2\).

For a disjoint union, a paired dominating set must restrict to a paired dominating set in every component: domination cannot cross components, and neither can an edge of a perfect matching. Thus paired-domination polynomials multiply over components.

In \(K_s\), every nonempty vertex set dominates, and its induced clique has a perfect matching exactly when its cardinality is positive and even. Therefore
\[
D_{\mathrm{pr}}(K_s,x)
=\sum_{j\ge1}inom{s}{2j}x^{2j}
=A_s(x).
	ag{2}
\]

For \(K_{s,s}\), suppose a selected set contains \(a\) vertices in one part and \(b\) in the other. A perfect matching in the induced graph exists exactly when \(a=b\). Paired domination excludes \(a=b=0\), so precisely the choices with \(a=b=j\ge1\) qualify. Hence
\[
D_{\mathrm{pr}}(K_{s,s},x)
=\sum_{j=1}^sinom{s}{j}^2x^{2j}
=B_s(x).
	ag{3}
\]
Combining (1)--(3) proves the two displayed product formulas.

Both \(A_s\) and \(B_s\) have lowest nonzero degree \(2\). Therefore the least exponent occurring in the full polynomial is \(2q\) in residue characteristic \(2\), and \(q+1\) in odd residue characteristic. This gives the paired-domination number. Each clique \(K_s\) and each \(K_{s,s}\) has total-domination number \(2\) for \(s\ge2\), so the same component decomposition gives the identical total-domination values.

It remains to prove reconstruction. Let \(P(x)=D_{\mathrm{pr}}(T_\Gamma(R),x)\), let \(e\) be its least nonzero exponent, let \(d=\deg P\), and let \(c\) be its leading coefficient. If the residue characteristic is \(2\), then \(s\) is even, \(A_s\) has degree \(s\) and leading coefficient \(1\), so
\[
c=1,\qquad e=2q,\qquad d=qs.
\]
Thus \(q=e/2\) and \(s=d/q\).

If the residue characteristic is odd, then \(s\) is odd. Now \(A_s\) has degree \(s-1\) and leading coefficient \(s\), while \(B_s\) has degree \(2s\) and leading coefficient \(1\). Hence
\[
c=s>1,\qquad e=q+1,\qquad d=qs-1.
\]
Thus \(s=c\) and \(q=e-1\). The polynomial therefore distinguishes the parity case and reconstructs \((q,s)\). Equation (1) shows that these data determine the total graph up to isomorphism.

## Verification

The accompanying `verify.py` independently constructs the total graphs of \(\mathbb Z_4\), \(\mathbb Z_8\), and \(\mathbb Z_9\), enumerates all vertex subsets, tests domination and exact perfect matching, and compares the resulting coefficient vectors with the formulas above. It also tests the reconstruction rule on five additional structural profiles.

Exact output:

```text
VERIFY_OK
actual_rings=Z4,Z8,Z9
bruteforce_subsets=16,256,512
additional_profiles=(4,4,char2),(8,8,char2),(3,9,odd),(5,5,odd),(7,7,odd)
reconstruction_from_lowest_degree_and_leading_coefficient=passed
```

The computation is corroborative only; the theorem is proved symbolically from the component decomposition and matching classification.

## Relationship to prior work

Anderson and Badawi introduced the total graph and proved the clique/complete-bipartite decomposition when the zero divisors form an ideal. Tamizh Chelvam and Asir later studied domination in total graphs and, in the same structural regime, obtained the corresponding total-domination number. Their paper does not study paired dominating sets or the paired-domination polynomial.

Haynes and Slater introduced paired domination in 1998. A 2016 conference paper introduced the paired-domination polynomial for general graphs and reports formulas for some standard graph families. The result here is ring-specific: it classifies all paired dominating sets in finite local total graphs, gives the complete polynomial, proves equality with total domination, and shows that the polynomial reconstructs the residue-field size, maximal-ideal size, and total-graph isomorphism type.

Targeted searches under total-graph, finite-local-ring, paired-domination, paired-domination-polynomial, complete-bipartite-component, residue-coset, and reconstruction formulations found no source stating this ring-specific polynomial or reconstruction theorem.

## Limitations

The reconstruction statement is restricted to finite commutative local nonfields. If \(R\) is a field, its total graph has isolated vertices, so no paired dominating set exists and the paired-domination polynomial is zero; it therefore cannot recover the field order.

The polynomial determines the total graph within the stated local class, not the ring isomorphism type. Distinct finite local rings can share the same \(q\) and \(s\).

No claim is made for finite nonlocal rings, where \(Z(R)\) need not be an ideal and the component structure can be substantially more complicated.

## References

1. D. F. Anderson and A. Badawi, “The total graph of a commutative ring,” *Journal of Algebra* 320 (2008), 2706–2719. DOI: 10.1016/j.jalgebra.2008.06.028. Available online 26 July 2008.
2. T. Tamizh Chelvam and T. Asir, “Domination in the Total Graph of a Commutative Ring,” *Journal of Combinatorial Mathematics and Combinatorial Computing* 87 (2013), 147–158.
3. T. W. Haynes and P. J. Slater, “Paired-domination in graphs,” *Networks* 32 (1998), 199–206. DOI: 10.1002/(SICI)1097-0037(199810)32:3<199::AID-NET4>3.0.CO;2-F.
4. Puttaswamy, Anwar Alwardi, and S. R. Nayaka, “Introduction to Paired Domination Polynomial of a Graph,” *International Journal of Physical and Mathematical Sciences* 10(9) (2016), conference dates 26–27 September 2016.
