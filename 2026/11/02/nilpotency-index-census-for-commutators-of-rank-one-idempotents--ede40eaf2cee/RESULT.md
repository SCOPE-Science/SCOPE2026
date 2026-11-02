# Nilpotency-index census for commutators of rank-one idempotents over finite fields

## Finding
Let \(n\ge2\) and let \(\mathbb F_q\) be any finite field. Write \(\mathcal P_n(q)=\{P\in M_n(\mathbb F_q):P^2=P,\operatorname{rank}P=1\}\). For an ordered pair \((P,Q)\in\mathcal P_n(q)^2\), put \(C=PQ-QP\). The Lie commutator has only four possible types: \(C=0\); \(C\ne0\) with \(C^2=0\); \(C^2\ne0\) with \(C^3=0\); or \(C\) not nilpotent. These four types have the exact counts below.

Set \(m=n-1\), \(H=(q^m-1)q^{m-1}\), \(J=H/(q-1)\) and \(V=q^{m}(q^n-1)/(q-1)=|\mathcal P_n(q)|\). Among the \(V\) choices for \(Q\), with a fixed \(P\), their counts in the displayed order are
\[
\boxed{1+J,\quad 2H+2q^m-2,\quad (q^m-1)(q^{m-1}-1),\quad (q-2)H.}
\]
For ordered pairs \((P,Q)\), multiply all four numbers by \(V\). In particular, \(C\) has exact nilpotency index three for some such pair if and only if \(n\ge3\), in every characteristic, and its count is \(V(q^{n-1}-1)(q^{n-2}-1)\).

There is also a field-independent polynomial identity and exact nilpotency criterion. For every field \(k\) and every rank-one idempotent pair over \(k\), with \(a=\operatorname{tr}(PQ)\),
\[
\boxed{C^3=a(a-1)C.}
\]
Consequently \(C\) is nilpotent if and only if \(a\in\{0,1\}\). The dimension-three threshold for possible nilpotency index three holds over arbitrary fields.

## Assumptions and scope
All matrices are labelled; no simultaneous-conjugacy quotient is taken. A rank-one idempotent is an \(n\)-square matrix of rank one satisfying \(P^2=P\). Nilpotency index is the least positive integer \(r\) with \(C^r=0\); for \(C=0\), zero is classified separately. The formulas hold for all integers \(n\ge2\), all prime powers \(q\), including nonprime fields and characteristic two. The polynomial identity works over arbitrary fields. The rational quantities \(J\) and \(V\) are integers by geometric-series identities.

## Proof
Conjugation acts transitively on rank-one idempotents, so fix \(P=\operatorname{diag}(1,0,\ldots,0)\). Every rank-one idempotent \(Q\) is \(uv^{\mathsf T}\) with \(v^{\mathsf T}u=1\), uniquely modulo \((u,v)\mapsto(\lambda u,\lambda^{-1}v)\) for \(\lambda\in k^\times\). Decompose \(u=(s,w)\), \(v=(t,z)\), where \(s,t\in k\), \(w,z\in k^m\). Write \(a=st=\operatorname{tr}(PQ)\). The idempotence equation is
\[
st+z^{\mathsf T}w=1.\]
The commutator and its square have block form
\[
C=\begin{pmatrix}0&sz^{\mathsf T}\\-tw&0\end{pmatrix},\qquad
C^2=\begin{pmatrix}-a(1-a)&0\\0&-a\,wz^{\mathsf T}\end{pmatrix}.
\]
A further multiplication gives \(C^3=-a(1-a)C=a(a-1)C\). If \(a\notin\{0,1\}\), then \(C\ne0\) and repeated application of the cubic identity prevents nilpotence. If \(a=0\), then \(st=0\), hence \(C^2=0\). If \(a=1\), then \(s,t\ne0\); \(C^2=0\) precisely when \(w=0\) or \(z=0\), since the matrix \(wz^{\mathsf T}\) is nonzero if and only if both factors are nonzero. Thus an index-three example requires and, for \(m\ge2\), admits nonzero orthogonal \(w,z\).

Count rank-one idempotents by the nonzero pairs \((u,v)\) with \(v^{\mathsf T}u=1\), modulo \(q-1\) scalings. This gives \(V=(q^n-1)q^{n-1}/(q-1)\). The number of \((w,z)\) with \(z^{\mathsf T}w=1\) is \(H=(q^m-1)q^{m-1}\). When \(a=0\), either exactly one of \(s,t\) vanishes, giving \(H\) choices in each of two cases after scaling, or both vanish, giving \(J=H/(q-1)\) commuting choices with \(C=0\). Thus the \(a=0\) sector comprises \(2H+J\) choices, \(2H\) of them with \(C\ne0\) and \(C^2=0\).

When \(a=1\), normalize \(s=t=1\). The equation becomes \(z^{\mathsf T}w=0\). Taking \(w=0\) gives \(q^m\) choices, and taking \(w\ne0\) gives \(H\), hence a total of \(q^m+H\). Exactly \(2q^m-1\) have \(w=0\) or \(z=0\), including the unique \(Q=P\), where \(C=0\). The remaining \((q^m-1)(q^{m-1}-1)\) have nonzero \(w,z\) orthogonal and produce index-three commutators.

Finally, for each \(a\in k\setminus\{0,1\}\), normalize \(s=1,t=a\), so \(z^{\mathsf T}w=1-a\ne0\), giving exactly \(H\) choices. Thus \((q-2)H\) choices are not nilpotent. Adding the cases produces the four stated counts, which sum to \(V\). Multiplying by the number \(V\) of first projectors gives all ordered-pair counts. For \(m=1\), nonzero orthogonal vectors do not exist; for \(m\ge2\), choose distinct coordinate directions for nonzero orthogonal \(w,z\). This proves the sharp threshold over any field.

## Verification
A standalone Python program `verify.py` constructs every rank-one idempotent independently from the defining matrix conditions, forms all ordered pairs, multiplies their matrices directly and classifies the commutators by exact powers, without using the proof's block classification. It checks the predicted counts over \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5\) in dimension two, over \(\mathbb F_2,\mathbb F_3,\mathbb F_4\) in dimension three, and over \(\mathbb F_2\) in dimension four. The output is `RANK_ONE_IDEMPOTENT_COMMUTATOR_OK 8 exhaustive pair enumerations`. For instance, over \(\mathbb F_2\) in dimension three, the four ordered-pair counts are \(196,504,84,0\), summing to \(784\). These finite calculations check instances and do not replace the general proof.

## Relationship to prior work
The finite-field matrix centralizer and commuting-class literature provides a natural motivation for classifying commutators by their nilpotence properties; for example, Britnell and Wildon, *On types and classes of commuting matrices over finite fields* (arXiv:1001.0811, first public version 6 January 2010), concerns which similarity classes have commuting representatives and the structure of nilpotent centralizers. Its principal results, including the classification of commuting nilpotent types, do not give an ordered-pair count of rank-one idempotents classified by the nilpotency index of their **commutator**. Radjavi and Rosenthal, *On Commutators of Idempotents* (2002), establish implications from nilpotent commutators to triangularizability, rather than the finite-field rank-one census. Drnovšek, Radjavi and Rosenthal, *A characterization of commutators of idempotents* (2002), give characterization criteria for possible commutator operators; no assertion is made that those general existence criteria are new here. The present result is a finite-field **multiplicity** and index-stratification theorem, not a characterization of all realizable commutators.

## Limitations
The result treats rank-one idempotents and ordered labelled pairs, not arbitrary-rank idempotents or simultaneous similarity orbits. It counts nilpotency-index categories, not full conjugacy-class profiles of commutators. The literature comparison is not exhaustive; the two older idempotent-commutator papers were not available in full text during this investigation, leaving a residual implicit-coverage risk. The independently executed finite enumerations are not independent mathematical peer review.

## References
1. J. R. Britnell and M. Wildon, *On types and classes of commuting matrices over finite fields*, arXiv:1001.0811v1 (6 January 2010), https://arxiv.org/abs/1001.0811 ; https://doi.org/10.1112/jlms/jdq088.
2. H. Radjavi and P. Rosenthal, *On Commutators of Idempotents*, Linear and Multilinear Algebra 50 (2002), 121–124, https://doi.org/10.1080/03081080290019540.
3. R. Drnovšek, H. Radjavi and P. Rosenthal, *A characterization of commutators of idempotents*, Linear Algebra and its Applications 347 (2002), 91–99, https://doi.org/10.1016/S0024-3795(01)00533-X.
