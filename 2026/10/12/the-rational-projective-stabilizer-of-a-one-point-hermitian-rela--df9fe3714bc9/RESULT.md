# The rational projective stabilizer of a one-point Hermitian-relative curve

## Finding

Let \(s\ge 2\) be a prime power, \(k=\mathbb F_{s^2}\), and choose \(\eta\in k\setminus\mathbb F_s\). Let \(C_\eta\subset\mathbb P^2_k\) be the smooth plane curve
\[
X^{s+1}+\eta Y^{s+1}+Y^sZ+YZ^s=0.
\]
Its **full projective stabilizer over \(k\)** is exactly the set of transformations
\[
[X:Y:Z]\longmapsto
[\alpha X+\beta Y:Y:Z-\alpha\beta^sX+vY],
\qquad \alpha^{s+1}=1,\quad
v+v^s=-\beta^{s+1},
\]
with \(\alpha\in k^\times\) and \(\beta,v\in k\). In particular, this stabilizer has order
\[
\bigl|\operatorname{Stab}_{\mathrm{PGL}_3(k)}(C_\eta)\bigr|=s^3(s+1).
\]
More precisely, it is \(H_s\rtimes\mu_{s+1}\), where
\[
H_s=\{(\beta,v)\in k^2:v+v^s=-\beta^{s+1}\},\qquad
(\beta,v)(\gamma,w)=(\beta+\gamma,v+w-\beta^s\gamma),
\]
and the norm-one group \(\mu_{s+1}\) acts on \(H_s\) by \((\beta,v)\mapsto(\alpha\beta,v)\).
The group \(H_s\) has order \(s^3\), has center of order \(s\), and is nonabelian. When \(s=2\), it is the quaternion group \(Q_8\), so the complete stabilizer is \(Q_8\rtimes C_3\) of order \(24\).

## Assumptions and scope

All projectivities have entries in \(k=\mathbb F_{s^2}\), and \(\operatorname{Stab}_{\mathrm{PGL}_3(k)}\) denotes the projective transformations **defined over that field** that carry the indicated embedded curve onto itself. The conclusion does not identify the larger geometric projective group over \(\overline{k}\), the abstract automorphism group of the curve, or a group scheme. The parameter \(\eta\) is required to lie outside \(\mathbb F_s\); no characteristic restriction beyond \(s\) being a prime power is used.

The source of this family is Homma and Kim's classification of Hermitian-relative curves with precisely one \(\mathbb F_{s^2}\)-rational point. A verified public presentation of that source occurred on June 11, 2026; this is the earliest dated public evidence used for the source. A later arXiv posting is not used as its first public date.

## Proof

Write \(F=X^{s+1}+\eta Y^{s+1}+Y^sZ+YZ^s\). Because the characteristic divides \(s\) but not \(s+1\),
\[
F_X=X^s,\qquad F_Y=\eta Y^s+Z^s,\qquad F_Z=Y^s.
\]
These derivatives cannot vanish simultaneously at a projective point; hence \(C_\eta\) is smooth and geometrically integral.

For \((X,Y,Z)\in k^3\), the expressions \(X^{s+1}\), \(Y^{s+1}\), and \(Y^sZ+YZ^s\) belong to \(\mathbb F_s\). Thus \(F=0\) implies \(\eta Y^{s+1}\in\mathbb F_s\). Since \(\eta\notin\mathbb F_s\), necessarily \(Y=0\), then \(X=0\). Therefore
\[
C_\eta(k)=\{P\},\qquad P=[0:0:1].
\]
The tangent at \(P\) is \(Y=0\).

Let \(T\in\mathrm{PGL}_3(k)\) preserve the curve. It fixes the unique rational point \(P\), and necessarily preserves its tangent line \(Y=0\). Choosing a representative and scaling its second row, \(T\) has the unique form
\[
(X,Y,Z)\mapsto(aX+bY,\;Y,\;uX+vY+wZ),
\qquad a,w\in k^\times,\quad b,u,v\in k.
\]
Geometric integrality and equal degrees imply \(F\circ T=\lambda F\) for some \(\lambda\in k^\times\). Expanding the two Frobenius-binomial products, coefficient comparison in the six potentially nonzero monomials gives
\[
\begin{aligned}
a^{s+1}&=\lambda,& w&=\lambda,& w^s&=\lambda,\\
a^s b+u^s&=0,& ab^s+u&=0,\\
b^{s+1}+\eta+v+v^s&=\lambda\eta.
\end{aligned}
\]
The first line implies \(\lambda=a^{s+1}\in\mathbb F_s^\times\). On the final line the quantities \(b^{s+1}\), \(v+v^s\), and \(\lambda\) lie in \(\mathbb F_s\). Hence \((\lambda-1)\eta\in\mathbb F_s\), forcing \(\lambda=1\). The equations now give \(w=1\), \(a^{s+1}=1\), \(u=-ab^s\), and \(v+v^s=-b^{s+1}\); the remaining equation follows by taking the \(s\)-th power. Conversely, these conditions make every coefficient equation hold, proving both necessity and sufficiency.

The norm-one equation \(a^{s+1}=1\) has exactly \(s+1\) solutions. There are \(s^2\) choices of \(b\), and, for each, exactly \(s\) solutions of the trace equation \(v+v^s=-b^{s+1}\), because \(\operatorname{Tr}_{k/\mathbb F_s}:k\to\mathbb F_s\) is surjective with kernel of size \(s\). This proves the claimed cardinality.

Writing \(U_{\beta,v}\) for the matrices with \(a=1\), direct multiplication gives
\[
U_{\beta,v}U_{\gamma,w}=U_{\beta+\gamma,\,v+w-\beta^s\gamma}.
\]
The diagonal matrices \(D_\alpha=\operatorname{diag}(\alpha,1,1)\) act by \(D_\alpha U_{\beta,v}D_\alpha^{-1}=U_{\alpha\beta,v}\). Every stabilizer uniquely factors as an element of \(H_s\) followed by an element of \(\mu_{s+1}\), establishing the semidirect product.

For \(\beta=0\), the trace-zero elements \(v\) form a central subgroup of order \(s\). The commutator of \((\beta,v)\) and \((\gamma,w)\) has central coordinate \(\gamma^s\beta-\beta^s\gamma\). If \(\beta\ne0\), choosing \(\gamma/\beta\notin\mathbb F_s\) makes it nonzero. Hence this is the entire center, and \(H_s\) is nonabelian. For \(s=2\), all six noncentral elements square to the unique nonidentity central element, so \(H_2\cong Q_8\). This completes the proof.

## Verification

The standalone `verify_stabilizer.py` computes in \(\mathbb F_4\) and \(\mathbb F_9\), exhaustively enumerates the normalized five-parameter projectivities fixing the unique rational point and its tangent, and independently compares all homogeneous polynomial coefficients. It finds exactly \(24\) and \(108\) stabilizers, respectively, matching \(s^3(s+1)\). It also checks the unipotent group law and the quaternion element orders in the smallest case. Run it with `python verify_stabilizer.py`; it prints `HERMITIAN_STABILIZER_EXACT_OK` on success. These finite calculations check examples but are not the proof for arbitrary prime powers; that proof is above.

## Relationship to prior work

Homma and Kim's conference article *Rational points and inflexions on Hermitian-relative curves*, Theorem 1.1, introduces and characterizes this one-rational-point normal form. Its subject is rational-point and inflexion classifications, and it does not give the exact rational projective stabilizer, its matrix parametrization, group law, or order. Their earlier *Relatives of the Hermitian curve* treats the more general relative-curve construction and equivalence over the algebraic closure, which does not by itself determine rational projective stabilizers of this newly isolated form. In particular, conjugacy over \(\overline{k}\) does not determine the subgroup of projectivities defined over \(k\).

A related chapter, *Classification of Hermitian-Relative Curves up to Projective Equivalence* (first online May 31, 2026), explicitly treats equivalence classes of all relative curves, including the one-point type, according to its publisher abstract. That abstract does not specify rational stabilizer orders or their group laws; its full text was not accessible for complete comparison. In particular, classifying which curves are equivalent does not alone determine the automorphism groups of representatives. This remains a specific priority for independent bibliographic checking, not an assertion that the chapter omits this result. No previously located published statement was found to imply the exact rational stabilizer classification.

## Limitations

The result is restricted to \(\mathrm{PGL}_3(\mathbb F_{s^2})\) for the one-point form and is independent of \(\eta\) only within the stipulated non-subfield range. It neither classifies stabilizers over larger coefficient fields nor asserts that different parameters define inequivalent curves. Unexamined portions of specialized projective-equivalence literature could include equivalent calculations. The exact formula follows from coefficient comparison; finite checker runs alone would not establish it.

## References

1. M. Homma and S. J. Kim, *Rational points and inflexions on Hermitian-relative curves*, Workshop on Coding and Cryptography (WCC 2026) proceedings, dated April 30, 2026, Theorem 1.1. https://wcc2026.inria.fr/assets/final_versions/WCC2026_paper_17.pdf . Public conference session: June 11, 2026, https://wcc2026.inria.fr/ .
2. M. Homma and S. J. Kim, *Relatives of the Hermitian curve*, 2024 preprint https://arxiv.org/abs/2402.14192 ; Journal of Geometry 117:11 (2026), DOI 10.1007/s00022-026-00795-8.
3. M. Homma and S. J. Kim, *Classification of Hermitian-Relative Curves up to Projective Equivalence*, Springer WAIFI proceedings (2026), DOI 10.1007/978-3-032-27574-5_7. Full text not examined.
