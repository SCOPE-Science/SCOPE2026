# Rigidity of the remaining thirteen-line \(8,16,2,1\) multiplicity type

## Finding

A precise projective-rigidity statement eliminates one of the eight numerical possibilities left open by the generalized Terao analysis of Dimca and Pokora. Let \(\mathcal A\) be an arrangement of thirteen distinct complex projective lines with exactly eight double points, sixteen triple points, two quadruple points, and one quintuple point. Assume that (i) every line passes through at least one quadruple or quintuple point and (ii) every line contains at most six distinct intersection points of the arrangement. Then \(\mathcal A\) is projectively equivalent to the single cyclotomic arrangement
\[
  P_5(X,Z)P_5(Y,Z)(X^5-Y^5)=0,
  \qquad P_5(U,V)=U^4+U^3V+U^2V^2+UV^3+V^4.
\]
Thus the space of complex projective realizations with those properties consists of one projective equivalence class. In particular, no pair contradicting the generalized Terao conjecture can have the numerical type \((n_2,n_3,n_4,n_5)=(8,16,2,1)\) among the possible thirteen-line, maximal-multiplicity-five counterexamples isolated in arXiv:2609.33584v2, Proposition 5.6.

## Assumptions and scope

The ground field is \(\mathbb C\), and all lines are distinct in \(\mathbb P^2_{\mathbb C}\). An \(m\)-fold point lies on exactly \(m\) arrangement lines; \(n_m\) is the number of these points. For an arrangement line \(L\), the number \(r_L\) counts **distinct** singular points lying on \(L\), not pairwise line incidences. A projective equivalence is induced by \(\mathrm{PGL}_3(\mathbb C)\). The classification requires both explicit hypotheses (i) and (ii); their availability in the counterexample application follows from Proposition 5.8 and Proposition 5.1 of Dimca--Pokora, respectively. No assertion is made here about all arrangements having the same four raw multiplicity counts without these two additional hypotheses.

## Proof

**1. Three disjoint pencils.** Name the two quadruple points \(p_1,p_2\), and the quintuple point \(q\). The union of the three pencils of arrangement lines through them contains every line by (i), while the sum of the respective pencil sizes is \(4+4+5=13\), the total number of lines. Consequently the three pencils are disjoint as sets of lines, and no arrangement line contains two of the three centers. Two lines from the same pencil meet only at its center. Every triple point therefore lies on exactly one line from each pencil. There are sixteen pairs consisting of a line through \(p_1\) and a line through \(p_2\), and their intersection points are distinct: otherwise two lines within one pencil would also meet away from its center. Since there are exactly sixteen triple points, all sixteen such pairwise intersections are triple points and each lies on one line of the \(q\)-pencil.

**2. The centers are not collinear.** If the three distinct centers were collinear, make their common line the line at infinity. The first two pencils would be four lines \(y=a\) and four lines \(x=b\), with \(a\in A\), \(b\in B\), and \(|A|=|B|=4\); the third would be five parallel lines \(x-\lambda y=c\), where \(\lambda\ne0\) is fixed. All sixteen grid points lie on these five parallel lines, so \(|B-\lambda A|\le5\). This contradicts the elementary sumset bound \(|U+V|\ge |U|+|V|-1\) for finite nonempty subsets of \((\mathbb C,+)\): choose a real-linear functional injective on the finite sets in question and order the projected summands, obtaining at least seven distinct consecutive sums. Thus \(p_1,p_2,q\) are noncollinear.

**3. A five-element multiplicative quotient set.** Place the three centers at \([1:0:0]\), \([0:1:0]\), and \([0:0:1]\), in that order. Because no arrangement line joins two centers, the three pencils have equations
\[
 Y=aZ\ (a\in A),\qquad X=bZ\ (b\in B),\qquad X=cY\ (c\in C),
\]
with \(A,B,C\subset\mathbb C^*\) consisting of respectively four, four, and five distinct elements. The sixteen triple points are exactly \([b:a:1]\), with \(a\in A\), \(b\in B\), and each forces \(b/a\in C\). For \(c\in C\), put \(t(c)=|\{(a,b)\in A\times B:b=ca\}|\). Because one value of \(a\) determines at most one \(b\), \(0\le t(c)\le4\). On \(X=cY\), aside from the quintuple center \(q\), the four first-pencil and four second-pencil lines contribute eight incidences. Each triple grid point identifies two of these into one singular point; all remaining incidences are distinct double points. Hence
\[
 r_{\{X=cY\}}=1+t(c)+(8-2t(c))=9-t(c).
\]
Hypothesis (ii) gives \(t(c)\ge3\). As the sixteen grid points occur on exactly one \(q\)-line, \(\sum_{c\in C}t(c)=16\), and therefore the five multiplicities are \((4,3,3,3,3)\) in some order. Every \(q\)-line meets the grid, so
\[
 S:=BA^{-1}=\{b/a:a\in A,b\in B\}=C,\qquad |S|=5.
\]

**4. Kneser rigidity.** Let \(H=\{h\in\mathbb C^*:hS=S\}\). It is a finite subgroup, and its order divides \(|S|=5\), since multiplication by \(H\) partitions \(S\) into free orbits. Kneser's addition theorem in the multiplicative abelian group \(\mathbb C^*\) states
\[
 |BA^{-1}|\ge |BH|+|A^{-1}H|-|H|.
\]
If \(H\) were trivial, this would give \(5\ge4+4-1=7\), impossible. Thus \(|H|=5\), and \(H=\mu_5\), the group of fifth roots of unity. Since \(|S|=|H|\), the quotient set is a single coset of \(\mu_5\). Fixing \(b_0\in B\) shows that every \(a\in A\) belongs to the coset \(b_0S^{-1}\); similarly fixing \(a_0\in A\) shows \(B\subset Sa_0\). Therefore \(A\) and \(B\) are four-element subsets of cosets of \(\mu_5\), hence each is such a coset with exactly one element deleted. Independently rescaling \(X/Z\) and \(Y/Z\) by a diagonal projectivity sends both missing elements to \(1\). Their ratio set becomes \(\mu_5\). The three pencils consequently become precisely the thirteen lines in the displayed equation. This proves classification up to projectivity.

**5. Existence and the counterexample exclusion.** For the displayed arrangement, \(A=B=\mu_5\setminus\{1\}\) and \(C=\mu_5\). The direction \(c=1\) occurs at four of the sixteen grid points; each other \(c\) occurs at three. The two quadruple points and the quintuple point are the three pencil centers, and the other intersections consist of sixteen triple and eight double points. Each first- or second-pencil line has one quadruple point, four triple points, and one double point, hence six singular points. The five \(q\)-lines have respectively five and six singular points. This validates the hypotheses and establishes nonemptiness.

Now suppose a lattice-isomorphic pair contradicted the generalized Terao conjecture in the thirteen-line, maximal-multiplicity-five case and had this numerical type. Proposition 5.1 of arXiv:2609.33584v2 gives at most six singular points on each line of the smaller-Jacobian-relation-degree arrangement; Proposition 5.8 shows that every such line passes through a point of multiplicity at least four. Both properties, including the multiplicity counts, are determined by the intersection lattice and thus hold for the other arrangement. The classification just proved makes both arrangements projectively equivalent. Minimal Jacobian syzygy degree is invariant under projective changes of coordinates, contradicting the assumed difference. Therefore this numerical type cannot support a generalized Terao counterexample.

## Verification

The accompanying standalone `verify.py` computes the entire projective incidence lattice of the cyclotomic normal form in characteristics \(11\), \(31\), and \(41\). It verifies the counts \((8,16,2,1)\), all thirteen linewise singular-point counts, and the five direction multiplicities \((4,3,3,3,3)\). It returns `THIRTEEN_LINE_INCIDENCE_OK`. These reductions verify the displayed example; they do not substitute for the characteristic-zero projective classification, which is proved symbolically above using Kneser's theorem. To reproduce: `python verify.py` with Python 3.8 or later, without third-party packages.

## Relationship to prior work

Dimca and Pokora (arXiv:2609.33584v2, Proposition 5.6 and Proposition 5.8, especially the sentence following Proposition 5.8) leave eight multiplicity types for thirteen-line generalized-Terao counterexamples, explicitly including \((8,16,2,1)\). They derive the two linewise constraints used here but do not give the projective rigidity theorem or eliminate this type. Their Section 5.3 suggests extending a combinatorial enumeration of block systems; here the key additional ingredient is multiplicative small-set structure applied to the forced three-pencil decomposition. Dimca, Ibadula and Măcinic (arXiv:1305.5092v3) classify certain \((3,4)\)-nets and study Milnor monodromy of small arrangements; their stated results neither classify this unequal \((4,4,5)\)-pencil configuration nor rule out this thirteen-line numerical type. The classical Kneser theorem supplies the finite-set rigidity lemma, but not the geometric incidence reduction.

## Limitations

The statement removes exactly the \((8,16,2,1)\) type from the eight possibilities in the cited 2026 analysis; the other seven types are not addressed. Without the hypotheses that every line passes through a quadruple/quintuple point and has at most six singular points, the theorem does not assert unique projective realization. It does not prove the generalized Terao conjecture for all thirteen-line arrangements. The projective classification is over \(\mathbb C\); the included finite-field computations are checks of the explicit example, not extension theorems in positive characteristic.

## References

1. A. Dimca and P. Pokora, *On a generalized Terao Conjecture for line arrangements*, arXiv:2609.33584v2 (2026), especially Theorem 1.3, Propositions 5.1, 5.6, and 5.8. First posted September 27, 2026. https://arxiv.org/html/2609.33584v2
2. A. Dimca, D. Ibadula and D. A. Măcinic, *Pencil type line arrangements of low degree: classification and monodromy*, arXiv:1305.5092v3 (2013), Sections 2--3. https://arxiv.org/html/1305.5092v3
3. M. DeVos, *A short proof of Kneser's addition theorem for abelian groups*, arXiv:1303.3539 (2013). https://arxiv.org/abs/1303.3539
