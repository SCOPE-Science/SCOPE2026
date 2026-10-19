# Pascal translation stabilizers and exact finite-field orbit counts for the canonical extremal Rota–Baxter operator

## Finding

For every field \(K\) and integer \(n\ge2\), let \(E_{ij}\) be matrix units of \(M_n(K)\). Define \(B_0\) on matrix units by
\[
B_0(E_{ij})=\begin{cases}
\sum_{r\ge0} E_{i+r,j+r+1},& i\le j,\\
-\sum_{r\ge1} E_{i-r,j-r+1},& i>j,
\end{cases}
\]
with out-of-range matrix units interpreted as zero. This is the canonical extremal weight-zero Rota–Baxter operator appearing in Gubarev [1].

For \(t\in K\), set \(P_t\in\operatorname{GL}_n(K)\) by
\[
(P_t)_{ij}=\begin{cases}\binom{j-1}{i-1}t^{j-i},&1\le i\le j\le n,\\0,&i>j.\end{cases}
\]
The full stabilizer of \(B_0\) under conjugation by **inner algebra automorphisms** equals
\[
\operatorname{Stab}_{\operatorname{PGL}_n(K)}(B_0)
=\{\operatorname{Ad}_{P_t}:t\in K\}\cong(K,+).
\]
In particular, the Pascal matrices satisfy \(P_tP_u=P_{t+u}\) and \(P_t=I\) exactly when \(t=0\). Every nonzero scalar multiple of \(B_0\) is already inner-conjugate to \(B_0\).

Define the transpose-dual \(B_0^\top(X)=(B_0(X^\top))^\top\). Its inner-conjugacy orbit is disjoint from that of \(B_0\). When \(K=\mathbb F_q\), the respective orbit cardinalities and their disjoint union are exactly
\[
\left|\operatorname{PGL}_n(q)\cdot B_0\right|=
\left|\operatorname{PGL}_n(q)\cdot B_0^\top\right|=
\frac{|\operatorname{GL}_n(q)|}{q(q-1)},
\quad
\left|\mathcal O_0\sqcup\mathcal O_0^\top\right|
=\frac{2|\operatorname{GL}_n(q)|}{q(q-1)},
\]
where \(|\operatorname{GL}_n(q)|=\prod_{j=0}^{n-1}(q^n-q^j)\).

Finally, \(B_0\) is a weight-zero Rota–Baxter operator with \(B_0^{2n-1}=0\) and \(B_0^{2n-2}\ne0\) over *every* field, including all positive characteristics.

## Assumptions and scope

The action is \(\operatorname{Ad}_U(X)=UXU^{-1}\) for \(U\in\operatorname{GL}_n(K)\), viewed as an algebra automorphism of \(M_n(K)\). Two conjugating matrices differing by a nonzero scalar define the same inner automorphism. The transpose-dual is obtained by conjugating the linear operator by matrix transpose, which is an antiautomorphism of the associative algebra. No restriction on characteristic or field cardinality is imposed for the stabilizer. The finite orbit formula assumes \(K\) is a finite field. The result counts two **explicit canonical orbits**, not all weight-zero Rota–Baxter operators in positive characteristic.

## Proof

**1. A characteristic-free inverse-derivation description.** Let \(W=\langle e_1,\ldots,e_{n-1}\rangle\), \(\mathcal B=\{X\in M_n(K):\operatorname{im}X\subset W\}\), \(\mathcal K=\{v e_n^\top:v\in K^n\}\), and \(S=\sum_{i=1}^{n-1}E_{i+1,i}\). Directly from the defining formula, \(B_0(\mathcal K)=0\) and \(B_0(M_n(K))\subset\mathcal B\). For every matrix unit \(E_{ij}\in\mathcal B\), the telescoping identity gives
\[
B_0(E_{ij}S-SE_{ij})=E_{ij}.
\]
Indeed for \(j=1\) the argument is \(-E_{i+1,1}\), and for \(j>1\) it is \(E_{i,j-1}-E_{i+1,j}\); the two displayed sums cancel except for \(E_{ij}\). Thus \(\operatorname{im}B_0=\mathcal B\) and, by dimension, \(\ker B_0=\mathcal K\). The map
\[
\delta:\mathcal B\longrightarrow M_n(K)/\mathcal K,
\qquad \delta(b)=bS-Sb+\mathcal K
\]
is the inverse of the induced bijection \(\overline{B_0}:M_n(K)/\mathcal K\to\mathcal B\). As \(\mathcal B\mathcal K\subset\mathcal K\) and \(\mathcal K\mathcal B=0\), the quotient is a \(\mathcal B\)-bimodule; \(\delta(bc)=b\delta(c)+\delta(b)c\). For arbitrary \(x,y\), put \(b=B_0(x),c=B_0(y)\). Reduction modulo \(\mathcal K\) gives
\[
B_0(x)\,y+x\,B_0(y)\equiv b\delta(c)+\delta(b)c=\delta(bc).
\]
Applying \(B_0\) proves \(B_0(x)B_0(y)=B_0(B_0(x)y+xB_0(y))\). The proof uses only integer coefficients and therefore works in every characteristic.

**2. Stabilizer reduction.** If \(\operatorname{Ad}_U\) commutes with \(B_0\), then \(\operatorname{Ad}_U\) preserves \(\mathcal B\), hence \(UW=W\). It then preserves \(\mathcal K=\{X:XW=0\}\) as well. Since \(B_0\) and \(\delta\) are mutually inverse on the quotient, commutation is equivalent to
\[
[b,USU^{-1}-S]\in\mathcal K\quad\text{for every }b\in\mathcal B.
\]
The elementary matrix-unit centralizer lemma is
\[
\{D\in M_n(K):[b,D]\in\mathcal K\ \forall b\in\mathcal B\}
=KI+\mathcal K.
\]
To prove it, insert \(b=E_{ij}\) for \(i<n\), first with \(j<n\). Vanishing of commutator columns \(1,\ldots,n-1\) forces the upper-left \((n-1)\)-square block of \(D\) to be a scalar matrix and the bottom-left row to vanish; its final column is arbitrary. The converse follows because \(\mathcal B\mathcal K\subset\mathcal K\) and \(\mathcal K\mathcal B=0\). Therefore stabilizing \(U\) must satisfy
\[
UW=W,\qquad USU^{-1}-S=aI+v e_n^\top
\]
for some \(a\in K\), \(v\in K^n\), and conversely these conditions imply stabilization.

**3. Exact Pascal rigidity.** Set \(w=Ue_1\). Applying the preceding identity to \(Ue_j\in W\) for \(j<n\) yields
\[
Ue_{j+1}=(S+aI)Ue_j,
\quad Ue_j=(S+aI)^{j-1}w.
\]
For \(0\le k\le n-2\), the vector \((S+aI)^k w\) belongs to \(W\). Reading their last coordinates successively at \(k=0,1,\ldots,n-2\) gives \(w_n=w_{n-1}=\cdots=w_2=0\). Thus \(w=c e_1\) with \(c\ne0\) because \(U\) is invertible. It follows that
\[
U=cP_a,\qquad (P_a)_{ij}=\binom{j-1}{i-1}a^{j-i}\quad(i\le j).
\]
Conversely \(P_aW=W\) and \((P_aSP_a^{-1}-S)|_W=aI|_W\), hence \(P_aSP_a^{-1}-S\in aI+\mathcal K\); every \(P_a\) stabilizes \(B_0\). The binomial identity gives \(P_aP_b=P_{a+b}\); their distinct \(\operatorname{PGL}\)-classes are detected by the \((1,2)\)-entry. This proves exactness over any field, including characteristics dividing binomial coefficients.

**4. Scalar absorption, disjointness, and counts.** For \(c\in K^\times\), set \(D_c=\operatorname{diag}(1,c,c^2,\ldots,c^{n-1})\). Each nonzero summand of \(B_0(E_{ij})\) raises diagonal degree \(j-i\) by one; hence \(\operatorname{Ad}_{D_c}\circ B_0\circ\operatorname{Ad}_{D_c}^{-1}=c^{-1}B_0\). Thus scalar multiplication contributes no further orbit.

The image algebra \(\mathcal B\) of \(B_0\) has zero common kernel \(\bigcap_{b\in\mathcal B}\ker b=0\), whereas \(\operatorname{im}B_0^\top=\{X:X e_n=0\}\) has the one-dimensional common kernel \(K e_n\). The common-kernel dimension is invariant under inner conjugation, so the two orbits cannot meet. In \(\mathbb F_q\), the stabilizing subgroup inside \(\operatorname{GL}_n(q)\) consists exactly of \(\{cP_t:c\in\mathbb F_q^\times,t\in\mathbb F_q\}\), of order \(q(q-1)\); orbit-stabilizer gives both displayed counts.

**5. Nilpotency index in all characteristics.** Since \(B_0(E_{ij})\) raises \(j-i\) by one, \(B_0^{2n-1}=0\). For \(1\le k\le n-1\), one has \(B_0^k(E_{n1})=(-1)^kE_{n-k,1}\). Furthermore, for \(0\le k\le n-1\), the coefficient of \(E_{1,k+1}\) in \(B_0^k(E_{11})\) is exactly one: in this progression the only way to retain row index one is to choose the zero-shift summand at each step. Therefore \(B_0^{2n-2}(E_{n1})=(-1)^{n-1}E_{1n}\ne0\), with no characteristic restriction.

## Verification

Run `python3 verify.py` with a standard Python 3 interpreter. The standalone checker tests the weight-zero Rota–Baxter identity on every pair of matrix units for dimensions two through five over the prime fields of orders two, three and five; checks the Pascal stabilizing operators and scalar conjugacies; exhaustively enumerates all invertible matrices and stabilizers in \(\operatorname{GL}_2(2)\), \(\operatorname{GL}_3(2)\), \(\operatorname{GL}_2(3)\), and \(\operatorname{GL}_3(3)\); and verifies the nonzero top nilpotent power. The respective exhaustive stabilizer orders are \(2,2,6,6\), exactly \(q(q-1)\). Finite checks are not used as a substitute for the universal proof.

## Relationship to prior work

Gubarev [1, equation (2), §4] introduced the explicit canonical form and characterized extremal weight-zero Rota–Baxter operators over characteristic-zero fields **up to inner conjugation, transpose, and nonzero scalar multiplication**. The image/kernel and inverse-derivation ideas also appear in [1]; they are credited and reused here. The independent contribution is the precise, characteristic-free inner stabilizer group \((K,+)\) realized by Pascal translations, its explicit orbit count over every finite field, and the disjointness of the two canonical inner orbits. Gubarev's characteristic-zero theorem together with scalar absorption implies that those two orbits exhaust characteristic-zero extremal operators; this text does **not** extend that exhaustion assertion to positive characteristic. Earlier work by Ogievetsky and Popov [2] gave Bézout-operator constructions related to \(B_0\). Its detailed symmetry content was not fully verified here; any equivalent pre-existing stabilizer statement would affect novelty.

## Limitations

The finite-field formula counts only the two displayed canonical orbits, not every extremal Rota–Baxter operator over positive-characteristic fields. A complete positive-characteristic classification is not proved. Independent mathematical auditing has not been performed. Earlier Bézout or associative Yang–Baxter literature could contain an equivalent stabilizer description not indexed by these search terms.

## References

[1] V. Gubarev, *Extremal Rota–Baxter operators on matrix algebras*, arXiv:2609.05647v1, first submitted 4 September 2026, especially equation (2), Theorem 1.1 and §4. https://arxiv.org/html/2609.05647v1

[2] O. Ogievetsky and T. Popov, *R-matrices in rime*, Advances in Theoretical and Mathematical Physics 14 (2010), §5 (Bézout operators), DOI:10.4310/ATMP.2010.v14.n2.a3. (The relevant full text could not be inspected completely.)
