# Quadratic-residue geometry of commutators in the five-element dihedral quandle algebra

## Finding
Let \(K\) be an arbitrary field of characteristic \(5\). In the five-dimensional algebra \(A=K[R_5]\) defined by \(e_i\star e_j=e_{2j-i}\) (indices modulo \(5\)), identify the *underlying vector space* with the ordinary cyclic group algebra \(B=K[X]/(X^5-1)\), sending \(e_i\) to \(X^i\). Put
\[
t=\log X=\sum_{j=1}^{4}\frac{(-1)^{j+1}}{j}(X-1)^j.
\]
Then \(B=K[t]/(t^5)\). The displayed products and powers in \(B\) are associative group-algebra products, not quandle-algebra products.

**Theorem.** The set \(\mathcal C_1=\{u\star v-v\star u:u,v\in A\}\) consists *exactly* of the vectors
\[
b=b_1t+b_2t^2+b_3t^3+b_4t^4
\]
such that
\[
b_1\ne 0\quad\text{or}\quad b_3^2-2b_2b_4\in K^2,
\]
where \(K^2=\{z^2:z\in K\}\), including \(0\). The linear span of \(\mathcal C_1\) is the whole augmentation ideal \(\Delta=\operatorname{span}_K\{t,t^2,t^3,t^4\}\). Every element of \(\Delta\) is a sum of at most two commutators. The least uniform bound is \(1\) precisely when every element of \(K\) is a square, and \(2\) otherwise.

For each finite field \(K=\mathbb F_q\) with \(q=5^e\), \(e\ge1\), the number of vectors of commutator length exactly \(2\) is
\[
\#(\Delta\setminus\mathcal C_1)=\frac{q(q-1)^2}{2}.
\]
Thus the number of single commutator values, including zero, is \(q^4-q(q-1)^2/2\). At \(q=5\) the count of length-two vectors is \(40\), agreeing with an earlier exhaustive computation; at \(q=25\) it is \(7200\).

## Assumptions and scope
The coefficient ring is a **field of characteristic five**, finite or infinite. The notion of commutator is the *additive* operation \([u,v]=u\star v-v\star u\), even though \(A\) is nonassociative. A linear scalar multiple of a commutator is itself a commutator because the multiplication is bilinear. The commutator length of \(b\in\Delta\) is the least number of additive commutators summing to \(b\); the zero vector has length \(0\). No statement is made for coefficient characteristics other than five, for other dihedral quandle orders, or for multiplicative commutators.

## Proof
**1. Group-algebra coordinates.** The map \(X\mapsto e^t=\sum_{j=0}^4t^j/j!\) is an isomorphism \(K[X]/(X^5-1)\cong K[t]/(t^5)\), because \(X-1\) and \(t\) differ by a higher-order nilpotent term. The quandle multiplication is
\[
U(t)\star V(t)=U(-t)V(2t),
\]
where the product on the right is ordinary commutative multiplication in \(B\). Indeed \(X^i\star X^j=X^{2j-i}\), and the truncated exponential satisfies \(\exp(at)\exp(bt)=\exp((a+b)t)\) modulo \(t^5\).

**2. Exact coefficient map.** Write \(U=\sum_{i=0}^4u_it^i\), \(V=\sum_{i=0}^4v_it^i\), and \(d_{ij}=u_iv_j-u_jv_i\) for \(0\le i<j\le3\). The coefficients of \([U,V]\) are
\[
(b_1,b_2,b_3,b_4)=
(3d_{01},\;3d_{02},\;4(d_{03}+d_{12}),\;-d_{13}).
\]
The fourth-order coefficients \(u_4,v_4\) do not contribute. The six minors of a \(2\times4\) matrix obey the Plücker identity
\[
d_{01}d_{23}-d_{02}d_{13}+d_{03}d_{12}=0.
\]
Conversely, every six-tuple satisfying this identity comes from such a matrix over **any field**. A direct proof: for a nonzero minor \(d_{ij}=z\), extend the minors antisymmetrically, put \(u_i=1,v_i=0,u_j=0,v_j=z\) and, for each remaining index \(\ell\), put \(v_\ell=d_{i\ell}\), \(u_\ell=-d_{j\ell}/z\). The Plücker identity verifies all remaining minors. For all-zero minors, take \(U=V=0\).

**3. Eliminate hidden coordinates.** Set \(a=b_1/3\), \(b=b_2/3=2b_2\), \(c=b_3\), \(d=b_4\). The specified minors force
\[
d_{01}=a,\quad d_{02}=b,\quad d_{13}=-d,\quad d_{03}+d_{12}=4c.
\]
Writing \(s=d_{03}\), the Plücker identity is
\[
a d_{23}+bd+s(4c-s)=0.
\]
If \(a\ne0\), choose \(s=0\), \(d_{12}=4c\), and \(d_{23}=-bd/a\); there is no obstruction. If \(a=0\), the unspecified minor \(d_{23}\) is irrelevant, and the quadratic equation
\[
s^2-4cs-bd=0
\]
has a root precisely when its discriminant \((4c)^2+4bd=c^2-bd=c^2-2b_2b_4\) is a square in \(K\). This remains valid when \(b=0\) or the discriminant vanishes; characteristic five makes \(2\) invertible. The converse decomposability construction yields actual elements \(U,V\) for each permitted target.

**4. Span, sharp width and counts.** The element \(1_B=X^0\) is not asserted to be a multiplicative identity for \(A\). Directly from the product formula,
\[
[1_B,t]=3t,\quad[1_B,t^2]=3t^2,\quad
[1_B,t^3]=4t^3,\quad[t,t^3]=-t^4.
\]
Thus the commutator span equals \(\Delta\). Any \(b\in\Delta\) with \(b_1=0\) splits as \(b=t+(b-t)\); both summands have nonzero linear coefficient, hence both are individual commutators by the criterion. This proves width at most \(2\). If \(K\) has a nonsquare \(\eta\), the target \(b_2=1\), \(b_3=0\), \(b_4=-\eta/2\), \(b_1=0\) has discriminant \(\eta\) and requires two; conversely if every scalar is a square, all targets are individual commutators.

For \(K=\mathbb F_q\), the failure condition forces \(b_1=0\) and \(b_2\ne0\). For every choice of the \(q-1\) nonzero \(b_2\) and any of the \(q\) values of \(b_3\), the map \(b_4\mapsto b_3^2-2b_2b_4\) is a bijection of \(\mathbb F_q\). Exactly \((q-1)/2\) field elements are nonsquares, yielding \(q(q-1)^2/2\) exceptional commutators. This counts all possibilities without omitting the zero discriminant.

## Verification
The standalone pure-Python verifier `verify.py` checks the full \(25\)-entry quandle multiplication table against the truncated-logarithm multiplication, exhaustively enumerates the \(5^8\) effective ordered pairs over \(\mathbb F_5\), compares their image to the discriminant criterion for all \(5^4\) targets, and reconstructs explicit wedges for every permitted target. It independently counts exceptions over \(\mathbb F_{25}=\mathbb F_5[s]/(s^2-3)\), verifies \(7200\) failures of the criterion, and reconstructs \(1419\) sample factorizations plus additional nonzero-linear cases. Run `python3 verify.py`; the final line must read `VERIFY_OK`. Enumeration checks finite fields only: the proof above supplies the arbitrary-field theorem.

## Relationship to prior work
Sangare–Ta, *Idempotents, automorphism groups, and commutator widths of quandle algebras* (first posted August 3, 2026), Theorem 5.4 and the discussion afterward, established by exhaustive computation that \(\mathbb F_5[R_5]\) has width \(2\) and **40** vectors of length \(2\). Those already-known facts are recovered, not claimed as new. The contribution here is a pointwise square-discriminant characterization **over every characteristic-five field**, the intrinsic Plücker explanation, the all-extension-field enumeration, and the sharp arbitrary-field criterion for width \(1\) versus \(2\).

Bardakov–Passi–Singh study general quandle rings and earlier width-one cases. Zhang's October 6, 2026 abstract describes group-algebra ideals for commutator *subalgebras* of Alexander quandles, but its full text was unavailable for comparison, and that abstract does not resolve whether it also characterizes individual additive commutator values. A possible equivalent historical statement in other language remains a limitation; a failed search alone cannot establish absolute novelty.

## Limitations
The statement is specific to characteristic \(5\) and the five-element dihedral quandle. The ordinary group-algebra logarithm is unavailable with the same denominators in characteristic dividing smaller factorials, and no extrapolation is made. The finite-field counts require \(q=5^e\). This is a mathematical derivation with finite computational cross-checks, not a substitute for an independent expert proof review. Relevant inaccessible literature, particularly the full version of Zhang's recent related work, leaves residual historical-overlap risk.

## References
1. B. Sangare and L. Ta, *Idempotents, automorphism groups, and commutator widths of quandle algebras*, arXiv:2608.01550v1 (2026), Theorem 5.4, especially the computation of 40 length-two vectors: https://arxiv.org/abs/2608.01550 .
2. V. G. Bardakov, I. B. S. Passi, and M. Singh, *Zero-divisors and idempotents in quandle rings*, Osaka Journal of Mathematics 59 (2022), 611–637, Sections 7.2–7.4.
3. Z.-L. Zhang, *Group-ring methods for Alexander quandle rings*, arXiv:2610.08204v1, first posted October 6, 2026: https://arxiv.org/abs/2610.08204 . Full-text comparison unresolved.
