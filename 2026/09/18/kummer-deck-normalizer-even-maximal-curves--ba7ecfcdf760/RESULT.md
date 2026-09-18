# Normalizer rigidity for the Kummer deck group of the even Ma–Wang maximal curves

## Statement

Let \(q\) be a prime power, let \(n\ge 4\) be even, put
\[
k=\mathbb F_{q^{2n}},\qquad m=q^n+1,\qquad
r=\frac{q^{n-1}-1}{q-1},
\]
and choose \(c\in k^\times\) with \(c^{q^n}=-c\).  Let \(X_{q,n}\) be the smooth projective curve with function field
\[
F=k(u,z),\qquad
z^m=f(u):=
c(u^q-u)\left(1+(u^q-u)^{q-1}\right)^r.
\]
Let
\[
C=\{\tau_\zeta:\ u\mapsto u,\ z\mapsto \zeta z\ :\ \zeta^m=1\}
\cong C_m
\]
be the deck group of the Kummer cover \(F/k(u)\).  Let \(G_{q,n}\) denote the subgroup constructed by Ma and Wang in Proposition 5.1: its elements are represented by
\[
u\longmapsto\frac{\alpha u+\beta}{\gamma u+\delta},
\qquad
z\longmapsto\frac{\lambda z}{\gamma u+\delta},
\]
where \(M=\begin{pmatrix}\alpha&\beta\\ \gamma&\delta\end{pmatrix}\in
\mathrm{GL}_2(q)\) and \(\lambda^m=\det M\).

Then
\[
\boxed{
N_{\operatorname{Aut}_k(X_{q,n})}(C)
=
C_{\operatorname{Aut}_k(X_{q,n})}(C)
=
G_{q,n}.
}
\]
Consequently,
\[
\boxed{
|N_{\operatorname{Aut}_k(X_{q,n})}(C)|
=(q^n+1)q(q^2-1)
}
\]
and there is a central exact sequence
\[
1\longrightarrow C_m\longrightarrow G_{q,n}
\longrightarrow \operatorname{PGL}_2(q)\longrightarrow 1.
\]
Moreover
\[
\boxed{Z(G_{q,n})=C.}
\]

Ma and Wang show that all automorphisms of \(X_{q,n}\) are defined over \(k\), so the same normalizer and centralizer statements hold inside the full geometric automorphism group.

A useful reformulation is: the Ma–Wang subgroup is not merely an explicit subgroup of the automorphism group; it is the complete subgroup preserving the distinguished degree-\(q^n+1\) Kummer structure.  Hence any automorphism outside \(G_{q,n}\), if one exists for even \(n\), must carry \(C\) to a different cyclic subgroup and cannot preserve the quotient field \(k(u)\).

## Proof

Write
\[
A(T)=T^q-T,\qquad
B(T)=1+(T^q-T)^{q-1}=\frac{T^{q^2}-T}{T^q-T}.
\]
Ma and Wang compute the Kummer ramification of
\[
z^m=cA(u)B(u)^r.
\]
For even \(n\),
\[
\gcd(r,m)=1.
\]
The branch locus on the \(u\)-line is exactly
\[
\mathbb P^1(\mathbb F_{q^2}),
\]
and every branch point is totally ramified.  Reduce the valuation of \(f\) at a branch point modulo \(m\).  The resulting nonzero Kummer exponent is
\[
e(Q)=
\begin{cases}
1,&Q\in S_0:=\mathbb P^1(\mathbb F_q),\\
r,&Q\in S_1:=\mathbb P^1(\mathbb F_{q^2})\setminus
\mathbb P^1(\mathbb F_q).
\end{cases}
\]
Indeed the finite \(\mathbb F_q\)-points have valuation \(1\), the points of
\(\mathbb F_{q^2}\setminus\mathbb F_q\) have valuation \(r\), and infinity has valuation \(-q^n\equiv1\pmod m\).
The two label classes have cardinalities
\[
|S_0|=q+1,\qquad |S_1|=q^2-q,
\]
which are unequal for every prime power \(q\ge2\).

Now let \(\sigma\in N_{\operatorname{Aut}_k(F)}(C)\).  Choose a primitive
\(m\)-th root of unity \(\zeta\) and write
\(\tau(z)=\zeta z\).
Since \(\sigma\) normalizes \(C\), the fixed field \(F^C=k(u)\) is preserved by
\(\sigma\).  Therefore
\[
\sigma(u)=M(u)
\]
for some \(M\in\operatorname{PGL}_2(k)\).

Conjugation by \(\sigma\) induces an automorphism of \(C\).  Since
\[
F=\bigoplus_{j=0}^{m-1} k(u)z^j
\]
is the eigenspace decomposition for \(C\), there are
\(t\in(\mathbb Z/m\mathbb Z)^\times\) and \(h(u)\in k(u)^\times\) such that
\[
\sigma(z)=h(u)z^t.
\]
Applying \(\sigma\) to \(z^m=f(u)\) gives
\[
f(M(u))=h(u)^m f(u)^t.
\]
Taking valuations at a point \(Q\in\mathbb P^1(\bar k)\) and reducing modulo
\(m\) yields
\[
e(M(Q))\equiv t\,e(Q)\pmod m
\]
on the branch locus (with the harmless inverse convention for \(M\) giving the same permutation conclusion).

Thus multiplication by \(t\) carries the two Kummer labels \(\{1,r\}\) to themselves.  Since \(t\) is a unit modulo \(m\), distinct labels remain distinct, so \(M\) either preserves the two label classes or swaps them.  A swap is impossible because
\[
q+1\ne q^2-q.
\]
Hence \(M(S_0)=S_0\), and the label \(1\) is fixed.  Therefore
\[
t\equiv1\pmod m.
\]
It follows that every element of the normalizer centralizes \(C\).

We have also shown that the induced fractional linear transformation \(M\) stabilizes
\(\mathbb P^1(\mathbb F_q)\).  Its stabilizer inside
\(\operatorname{PGL}_2(k)\) is exactly \(\operatorname{PGL}_2(q)\):
a transformation preserving \(\mathbb P^1(\mathbb F_q)\) sends
\(0,1,\infty\) to three \(\mathbb F_q\)-rational points; composing with the unique element of \(\operatorname{PGL}_2(q)\) having the same action on that ordered triple leaves a projective transformation fixing \(0,1,\infty\), hence the identity.

Therefore the map
\[
N_{\operatorname{Aut}_k(F)}(C)\longrightarrow\operatorname{PGL}_2(q)
\]
has kernel \(C\), so each projective transformation has at most \(m\) lifts.
Ma and Wang's Proposition 5.1 explicitly supplies lifts of every element of
\(\operatorname{PGL}_2(q)\), and their subgroup has order
\[
m|\operatorname{PGL}_2(q)|=m q(q^2-1).
\]
Consequently the normalizer equals their subgroup:
\[
N_{\operatorname{Aut}_k(F)}(C)=G_{q,n}.
\]
Since every normalizing element was shown to centralize \(C\),
\[
N_{\operatorname{Aut}_k(F)}(C)=C_{\operatorname{Aut}_k(F)}(C).
\]

Finally \(C\subseteq Z(G_{q,n})\).  The quotient
\(G_{q,n}/C\cong\operatorname{PGL}_2(q)\) has trivial center for every
\(q\ge2\).  The image of \(Z(G_{q,n})\) in the quotient is therefore trivial, so
\(Z(G_{q,n})\subseteq C\), proving \(Z(G_{q,n})=C\).

## Stress tests and boundary cases

The parity restriction is essential to this argument.  For \(n=2\) one has
\(r=1\), so the two Kummer labels collapse; \(X_{q,2}\) is Hermitian and its automorphism group is much larger.  For odd \(n\), Ma and Wang compute
\(\gcd(r,q^n+1)=q+1\), so the \(\mathbb F_{q^2}\setminus\mathbb F_q\) branch points are not totally ramified and the two-label unit argument above does not apply.

The proof does include \(q=2\): then the two label classes have sizes \(3\) and
\(2\), still forcing preservation.  This does not assert that
\(G_{2,n}\) is the full automorphism group; it identifies exactly the normalizer of the displayed Kummer deck group.

## Relation to prior work

Ma and Wang, *A new family of maximal curves not covered by the Hermitian curve*,
arXiv:2609.19546v1 (submitted 17 September 2026), introduce the above Kummer model.  For every \(n\ge4\) they construct the subgroup \(G_{q,n}\) of order
\((q^n+1)q(q^2-1)\).  Their Theorem A and Proposition 5.1 state the existence and size of this subgroup; the paper does not identify it as the normalizer or centralizer of the Kummer deck group.  The paper also notes that the full automorphism group is known for the odd-\(n\) Beelen–Montanucci curves.

Beelen and Montanucci, *A new family of maximal curves*, J. London Math. Soc.
98 (2018), 573–592, determine the full automorphism group for the earlier odd-\(n\) family, with the same numerical group order.  That result concerns odd \(n\ge5\) and does not determine the even-\(n\) curves newly introduced in arXiv:2609.19546.

General literature on superelliptic and cyclic covers contains normalizer and uniqueness results under various hypotheses, but the searched sources did not give the finite-characteristic, branch-label normalizer statement above for this new even-\(n\) family.

## Originality and limitations

To the best of our knowledge, the exact normalizer/centralizer identification above is new.  Searches using the defining family, the source arXiv identifier, Kummer deck groups, cyclic-cover normalizers, \(\operatorname{PGL}_2(q)\), and equivalent automorphism-group terminology found the Ma–Wang subgroup construction and older automorphism results for BM/GGS and other maximal curves, but no statement that the subgroup is the full normalizer of \(C\) for even \(n\).

The motivating preprint is extremely recent, so unindexed contemporaneous work is a residual originality risk.  No inaccessible source was identified whose title, abstract, or metadata specifically indicates the same even-\(n\) normalizer theorem.  The result does **not** determine the full automorphism group for even \(n\); it shows that any additional automorphism must move the distinguished Kummer deck group.

## References

1. L. Ma and Y. Wang, *A new family of maximal curves not covered by the Hermitian curve*, arXiv:2609.19546v1, 2026.  
   https://arxiv.org/abs/2609.19546  
   https://arxiv.org/html/2609.19546v1

2. P. Beelen and M. Montanucci, *A new family of maximal curves*, J. London Math. Soc. (2) 98 (2018), no. 3, 573–592.  
   https://doi.org/10.1112/jlms.12144  
   https://arxiv.org/abs/1711.02894

3. R. A. Hidalgo, S. Quispe, and T. Shaska, *Generalized superelliptic Riemann surfaces*, arXiv:1609.09576, 2016.  
   https://arxiv.org/abs/1609.09576
