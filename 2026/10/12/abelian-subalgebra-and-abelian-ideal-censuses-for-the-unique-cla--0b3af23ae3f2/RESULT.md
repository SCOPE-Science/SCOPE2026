# Abelian-subalgebra and abelian-ideal censuses for the unique class-three breadth family

## Finding
For every odd prime power \(q\) and every integer \(m\ge1\), let \(K=\mathbf F_{q^m}\) and put \(Q=q^m\). For the explicit class-three Lie algebra below, all maximal abelian \(\mathbf F_q\)-Lie subalgebras form a projective-plane family of size \(Q^2+Q+1\); distinct members meet in the center. The exact numbers of abelian subalgebras and abelian ideals of each dimension are, respectively,
\[
A_d=\binom{2m}{d}_q+(Q^2+Q+1)\left(\binom{3m}{d}_q-\binom{2m}{d}_q\right),
\]
\[
J_d=\binom{2m}{d}_q+\binom{m}{d-2m}_q-\mathbf 1_{d=2m}.
\]
These formulas apply to every integer \(0\le d\le5m\). The second formula follows from a complete classification: an abelian ideal is exactly a subspace of the center or a subspace between the center and the derived algebra. Thus the derived algebra is the unique maximal abelian ideal, whereas the maximal abelian subalgebras form a projective plane.

## Assumptions and scope
Fix \(q\) odd and \(m\ge1\). All subalgebras and ideals are \(\mathbf F_q\)-linear, not necessarily \(K\)-linear. On \(L=K^5\), define
\[
[(a,b,c,d,e),(x,y,z,s,t)]=(0,0,ay-bx,ay-bx+2cx-2az,ay-bx+2bz-2cy).
\]
This is the five-coordinate Lie algebra of Kundu–Naik–Singh [1]; their construction proves the Jacobi identity and establishes that it is the unique class-three stem Lie algebra of breadth type \((0,2m)\) over \(\mathbf F_q\). Define
\[
Z=\{(0,0,0,d,e):d,e\in K\},\qquad
L'=\{(0,0,c,d,e):c,d,e\in K\}.
\]
These are the center and the derived algebra, of \(\mathbf F_q\)-dimensions \(2m\) and \(3m\). We write \(\binom{r}{s}_q\) for the number of \(s\)-dimensional \(\mathbf F_q\)-subspaces of \(\mathbf F_q^r\), with value zero when \(s\notin[0,r]\). The zero algebra is counted as an abelian subalgebra and an abelian ideal.

## Proof
**Lie-law and structure check.** The bracket is alternating. To check Jacobi directly, write \(h_{uv}=ay-bx\), \(h_{vw}=xs-yr\), and \(h_{wu}=rb-sa\) for three vectors with first triples \((a,b,c)\), \((x,y,z)\), and \((r,s,t)\). The potentially nonzero Jacobi coordinates are the fourth and fifth, respectively proportional to \(r h_{uv}+a h_{vw}+x h_{wu}\) and \(s h_{uv}+b h_{vw}+y h_{wu}\); both vanish by expansion. By choosing entries supported in the first three coordinates, the bracket spans all of \(L'\), while \([L,L']=Z\) and \([L',L']=0\). An element centralizing all coordinate vectors must have its first three entries zero, so the center is exactly \(Z\).

**Commutator-minor lemma.** For \(u=(a,b,c,d,e)\) and \(v=(x,y,z,s,t)\), set \(h=ay-bx\), \(\alpha=cx-az\), and \(\beta=bz-cy\). The last three bracket coordinates are \((h,h+2\alpha,h+2\beta)\). Since the characteristic is odd, \([u,v]=0\) if and only if all three \(2\times2\) minors of
\[
\begin{pmatrix}a&b&c\\x&y&z\end{pmatrix}
\]
vanish. Equivalently, the triples \((a,b,c)\) and \((x,y,z)\) are \(K\)-linearly dependent.

**Maximal abelian subalgebras.** Let \(\pi:L\to K^3\) be projection onto the first three coordinates. For any \(u\notin Z\), the lemma yields
\[
C_L(u)=\pi^{-1}(K\pi(u))=Z+K(a,b,c,0,0).
\]
This is abelian, since all its projected triples are \(K\)-proportional. It is maximal abelian: any abelian subalgebra containing it must centralize \(u\), hence lies within \(C_L(u)\). Any abelian subalgebra \(U\not\subseteq Z\) contains such a \(u\), and \(U\subseteq C_L(u)\). The line \(K\pi(u)\) is independent of the choice of noncentral \(u\in U\). In particular \(U\) belongs to exactly one maximal abelian subalgebra. The maximal ones are indexed by \(\mathbf P^2(K)\), hence number \(Q^2+Q+1\); each has dimension \(2m+m=3m\), and distinct ones intersect precisely in \(Z\).

**Abelian-subalgebra census.** Exactly \(\binom{2m}{d}_q\) abelian \(d\)-subalgebras lie in \(Z\). For each maximal abelian subalgebra, the number of \(d\)-subspaces not lying in \(Z\) is \(\binom{3m}{d}_q-\binom{2m}{d}_q\). By the unique containment just proved, these sets are pairwise disjoint across the \(Q^2+Q+1\) maximal subalgebras. Adding both contributions gives \(A_d\), including the boundary cases \(d=0\) and \(d>3m\).

**Abelian-ideal classification.** Let \(I\) be an abelian ideal. If \(I\) contained \(u=(a,b,c,d,e)\) with \((a,b)\ne(0,0)\), choose \(v=(x,y,z,s,t)\) with \(h=ay-bx\ne0\). Since \(I\) is an ideal, \(w=[u,v]\in I\), and the first three coordinates of \(w\) equal \((0,0,h)\). But
\[
[u,w]=(0,0,0,-2ah,2bh)\ne0,
\]
contradicting \([I,I]=0\). Thus \(I\subseteq L'\). If \(I\) contains an element \(u=(0,0,c,d,e)\) with \(c\ne0\), the commutators \([L,u]\) fill \(Z\): explicitly, varying \((x,y)\in K^2\) in the first two coordinates yields \((0,0,0,-2cx,2cy)\), whose span is all \(Z\). Hence \(Z\subseteq I\). If there is no such \(u\), then \(I\subseteq Z\).

Conversely, every \(\mathbf F_q\)-subspace of \(Z\) is a central ideal, and every \(\mathbf F_q\)-subspace \(I\) with \(Z\subseteq I\subseteq L'\) is an abelian ideal because \([L,L']=Z\) and \([L',L']=0\). The two families overlap exactly in the single subspace \(Z\). Counting their \(d\)-dimensional members gives \(J_d\) by the Gaussian count of subspaces of \(Z\) and of \(L'/Z\). Since every abelian ideal lies in \(L'\), the latter is the unique maximal abelian ideal. This completes all assertions.

## Verification
The accompanying self-contained script `verify.py` uses the stated bracket, enumerates every reduced-row-echelon \(\mathbf F_q\)-subspace of \(\mathbf F_q^5\) for \(q=3,5\), and tests abelianness and the ideal condition directly. The computed distributions for dimensions \(0,1,2,3,4,5\) are:

- \(q=3\): abelian subalgebras \((1,121,157,13,0,0)\), abelian ideals \((1,4,1,1,0,0)\).
- \(q=5\): abelian subalgebras \((1,781,931,31,0,0)\), abelian ideals \((1,6,1,1,0,0)\).

The script additionally checks the centralizer criterion against every pair of vectors over \(\mathbf F_3\). It uses \(\mathbf F_9=\mathbf F_3[t]/(t^2+1)\) to independently check all nonzero triples in the extension-field case \(q=3,m=2\), finding \(91\) projective lines and exactly \(9\) commuting triples per nonzero triple. Run `python3 verify.py` from the directory containing the script; expected last line: `VERIFY_OK`. The finite calculations supplement but do not replace the general proof.

## Relationship to prior work
Kundu, Naik and Singh [1], especially Theorem 1.3 and Proposition 3.2, construct the algebra, identify its center and derived algebra, and calculate centralizer dimensions and their linear equations. Those ingredients are prior results: the commutator-minor condition is already implicit in their Proposition 3.2. The finding here is the **complete dimension-by-dimension census** of all abelian subalgebras and abelian ideals for every extension degree, together with the unique-containment/projective-incidence and ideal classification needed for the counting formulas.

Sriwongsa [2] studies general noncommuting graphs and establishes a relationship between graph colorings and abelian covers; that does not specify the families or the \(A_d,J_d\) distributions here. Šnobl and Winternitz [3] give structural lists of low-dimensional nilpotent Lie algebras and maximal abelian ideals, which may subsume some special-case qualitative observations when \(m=1\), but do not by themselves provide the displayed uniform finite-field Gaussian distributions. Unrecognized equivalent presentations remain possible.

## Limitations
The result is a theorem about this explicit class-three stem algebra and its isomorphic copies, not all nilpotent Lie algebras or all abelian subalgebras of arbitrary central extensions. Odd characteristic is used in the commutator-minor equivalence and in the abelian-ideal proof; characteristic two is not covered. Counting is by literal \(\mathbf F_q\)-linear subspaces, not up to automorphism or isomorphism. The algebra and elementary centralizer equations originate in [1]; only the complete classification/census assembled here is assessed. A self-review is not independent certification.

## References
[1] R. Kundu, T. K. Naik, A. Singh, “Nilpotent Lie algebras with two centralizer dimensions over a finite field,” arXiv:2208.07676v1, publicly posted 2022-08-16, Theorem 1.3 and Proposition 3.2. https://arxiv.org/html/2208.07676v1

[2] S. Sriwongsa, “Non-commuting graphs of projective spaces over central quotients of Lie algebras,” arXiv:2505.00726v1, 2025-04-27, Theorem 2.18. https://arxiv.org/html/2505.00726v1

[3] L. Šnobl and P. Winternitz, *Classification and Identification of Lie Algebras*, CRM Monograph Series 33, American Mathematical Society, 2014, especially its five-dimensional classification and maximal-abelian-ideal discussion, ISBN 9780821843550. https://doi.org/10.1090/crmm/033
