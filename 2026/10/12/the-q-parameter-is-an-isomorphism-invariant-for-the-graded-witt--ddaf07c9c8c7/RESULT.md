# The \(q\)-parameter is an isomorphism invariant for the graded Witt \(q\)-pre-Lie family
## Finding
For \(q\in\mathbb C^\times\setminus\{1\}\) and \(\lambda\in\mathbb C\), write \(S(q,\lambda)\) for the algebra on the Witt basis \(\{W_n:n\in\mathbb Z\}\) with
\[
W_n\circ W_m=\frac{1}{q}\bigl(\lambda+m+(1-q)n\bigr)W_{n+m}.
\]
For \(q,q'\in\mathbb C^\times\setminus\{1\}\), the underlying nonassociative algebras \(S(q,\lambda)\) and \(S(q',\mu)\) are isomorphic exactly when
\[
q=q'\quad\text{and}\quad \mu\in\{\lambda,-\lambda\}.
\]
Consequently the parameter \(q\) is recoverable up to algebra isomorphism from the multiplication itself, even after one forgets which \(q\)-pre-Lie identity was used to obtain it. The global isomorphism space of the Lu--Hong non-pre-Lie branch is
\[
(\mathbb C^\times\setminus\{1\})\times\bigl(\mathbb C/\{\lambda\sim-\lambda\}\bigr).
\]
The automorphism group has a symmetry jump at the unique fixed point of the sign involution:
\[
\operatorname{Aut}S(q,\lambda)\cong
\begin{cases}
\mathbb C^\times,&\lambda\ne0,\\
\mathbb C^\times\rtimes C_2,&\lambda=0,
\end{cases}
\]
where \(C_2\) acts on \(\mathbb C^\times\) by inversion.

## Assumptions and scope
The ground field is \(\mathbb C\). The statement concerns the graded Witt-compatible family classified by Lu and Hong for \(q\ne0,1\). It compares the resulting binary algebras across *different* values of \(q\); the isomorphism is not required a priori to preserve the grading or the displayed basis. No claim is made here about the separate \(q=1\) pre-Lie classification, the nonexistent \(q=0\) branch, ungraded products, or Virasoro extensions.

## Proof
First, every member of the family has the same commutator. Indeed,
\[
W_n\circ W_m-W_m\circ W_n=(m-n)W_{m+n},
\]
so the sub-adjacent Lie algebra is the classical Witt algebra \(\mathcal W\), independently of \(q\) and \(\lambda\). Hence every algebra isomorphism \(S(q,\lambda)\to S(q',\mu)\) is automatically a Lie automorphism of \(\mathcal W\).

Bavula's determination of \(\operatorname{Aut}_{\mathrm{Lie}}(\mathcal W)\), together with the standard identification \(\mathcal W=\operatorname{Der}\mathbb C[t,t^{-1}]\), gives every Lie automorphism in the form
\[
\Phi_{\varepsilon,a}(W_n)=\varepsilon a^n W_{\varepsilon n},
\qquad \varepsilon\in\{1,-1\},\quad a\in\mathbb C^\times.
\]
Substituting this into the multiplicativity condition \(\Phi(W_n\circ W_m)=\Phi(W_n)\circ'\Phi(W_m)\) and cancelling \(a^{n+m}\) gives, for all \(m,n\in\mathbb Z\),
\[
\frac{\varepsilon}{q}\bigl(\lambda+m+(1-q)n\bigr)
=
\frac{1}{q'}\bigl(\mu+\varepsilon m+\varepsilon(1-q')n\bigr).
\]
Comparison of the coefficient of \(m\) forces \(q=q'\). Comparison of the constant term then forces \(\mu=\varepsilon\lambda\); after \(q=q'\), the coefficient of \(n\) agrees automatically. Conversely, when \(q=q'\) and \(\mu=\varepsilon\lambda\), every \(\Phi_{\varepsilon,a}\) with that choice of \(\varepsilon\) is an algebra isomorphism. This proves the cross-\(q\) classification.

For automorphisms one sets \(\mu=\lambda\). If \(\lambda\ne0\), the equality \(\lambda=\varepsilon\lambda\) forces \(\varepsilon=1\), leaving exactly the maps \(W_n\mapsto a^nW_n\), hence \(\mathbb C^\times\). If \(\lambda=0\), both signs occur. Composition gives the usual semidirect product law, with the sign-reversing element conjugating \(a\) to \(a^{-1}\).

## Verification
The accompanying `verify.py` performs exact rational regression checks of the commutator identity and of the coefficient comparison for many values of \(q,q',\lambda,\mu\), and it checks the automorphism sign condition and semidirect-product action. These finite checks are supplementary. The infinite quantifiers and completeness of the isomorphism classification are supplied by the symbolic coefficient comparison above together with the published classification of Witt Lie automorphisms.

## Relationship to prior work
Lu and Hong classify the graded compatible \(q\)-pre-Lie structures on the Witt algebra for each fixed \(q\ne0,1\), obtaining exactly the displayed one-parameter family. Their Proposition 3.10 and Theorem 3.11 then classify isomorphisms **for a fixed value of \(q\)**, giving \(\lambda\sim-\lambda\). The new point here is the comparison across different scaling parameters: after forgetting the \(q\)-label, the multiplication still determines \(q\), so no additional identifications occur between the fixed-\(q\) moduli spaces. The same argument also records the full automorphism-group jump at \(\lambda=0\).

The predecessor of Bai and Gao treats only the anti-pre-Lie slice \(q=-1\) and already identifies its single parameter up to sign. Bavula's automorphism theorem is used as prior structural input for the Witt Lie algebra; it does not address the \(q\)-pre-Lie products.

## Limitations
The proof uses the characteristic-zero complex Witt automorphism theorem and the Lu--Hong graded family. It does not classify all possible isomorphisms for unrelated \(q\)-pre-Lie algebras, and it does not assert that \(q\) is recoverable for arbitrary finite-dimensional or ungraded examples. The motivating preprint is very recent; a later revision could explicitly add the cross-\(q\) comparison, although the inspected version and web-indexed descriptions did not contain it.

## References
1. Chengyang Lu and Yanyong Hong, *On \(q\)-pre-Lie algebras*, arXiv:2607.08389v1 (first public 2026-07-09), especially Theorem 3.8, Proposition 3.10, and Theorem 3.11.
2. Chengming Bai and Dongfang Gao, *Graded anti-pre-Lie algebraic structures on Witt and Virasoro algebras*, arXiv:2507.09293v1; Journal of Geometry and Physics 214 (2025), 105525.
3. V. V. Bavula, *The groups of automorphisms of the Witt \(W_n\) and Virasoro Lie algebras*, Czechoslovak Mathematical Journal 66 (2016), 1129--1141.
