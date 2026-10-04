# Exact subalgebra commutativity degree after a one-dimensional central stabilization of the Heisenberg algebra

## Finding
For every prime power \(q\), let \(L_q\) be the four-dimensional Lie algebra over \(\mathbb F_q\) with basis \(x,y,z,c\), where \([x,y]=z\) and all other brackets between basis elements vanish. Then
\[
|\mathcal L(L_q)|=2q^3+4q^2+3q+5,
\]
and the number of ordered nonpermutable pairs in \(\mathcal L(L_q)^2\) is
\[
q^4(q+1)(3q+1).
\]
Consequently
\[
\operatorname{sd}(L_q)=1-\frac{q^4(q+1)(3q+1)}{(2q^3+4q^2+3q+5)^2}
=\frac{q^6+12q^5+27q^4+44q^3+49q^2+30q+25}{(2q^3+4q^2+3q+5)^2},
\]
and \(\operatorname{sd}(L_q)\to 1/4\) as \(q\to\infty\).

## Assumptions and scope
The field is an arbitrary finite field \(\mathbb F_q\), with no restriction on characteristic. The algebra is
\[
L_q=V\oplus Z,
\qquad V=\langle x,y\rangle,
\qquad Z=\langle z,c\rangle=Z(L_q),
\]
with derived algebra \([L_q,L_q]=\langle z\rangle\). Two subalgebras \(A,B\) are called permutable when \(A+B\) is a subalgebra; equivalently, \([A,B]\subseteq A+B\). The subalgebra commutativity degree is the proportion of ordered pairs of subalgebras that are permutable.

## Proof
Let \(\pi:L_q\to V=L_q/Z\) be the quotient map. For a subalgebra \(A\), put \(U=\pi(A)\) and \(C=A\cap Z\).

If \(\dim U=0\), then \(A=C\) is an arbitrary subspace of the two-dimensional center. There are \(q+3\) such subalgebras.

If \(\dim U=1\), closure is automatic because the bracket of two elements with proportional images in \(V\) is zero. For each line \(U\le V\), each central subspace \(C\le Z\), and each linear map \(U\to Z/C\), one obtains one subalgebra, and every subalgebra with one-dimensional image arises uniquely this way. Summing over \(\dim C=0,1,2\) gives
\[
(q+1)\bigl(q^2+(q+1)q+1\bigr)
=2q^3+3q^2+2q+1.
\]

If \(U=V\), closure forces \(z\in C\), because the alternating bracket \(\Lambda^2V\to\langle z\rangle\) is onto. For \(C=\langle z\rangle\), graphs are parametrized by the \(q^2\) maps \(V\to Z/C\); for \(C=Z\) there is one subalgebra. Thus this case contributes \(q^2+1\). Adding the three cases yields
\[
|\mathcal L(L_q)|=(q+3)+(2q^3+3q^2+2q+1)+(q^2+1)
=2q^3+4q^2+3q+5.
\]

Now take subalgebras \(A,B\), with images \(U=\pi(A)\) and \(W=\pi(B)\). If either image is zero, then \([A,B]=0\). If one image is all of \(V\), that subalgebra contains \(z\), so \([A,B]\subseteq\langle z\rangle\subseteq A+B\). If \(U=W\) is a line, then again \([A,B]=0\). Therefore failure of permutability is possible only when \(U\) and \(W\) are distinct lines. There are \(q(q+1)\) ordered pairs of distinct lines.

For distinct lines, \([A,B]=\langle z\rangle\), while
\[
(A+B)\cap Z=(A\cap Z)+(B\cap Z)=C+D.
\]
Hence \(A,B\) fail to permute exactly when \(z\notin C+D\). The admissible ordered central pairs are \((0,0)\), \((0,F)\), \((F,0)\), and \((F,F)\), where \(F\) is one of the \(q\) lines of \(Z\) different from \(\langle z\rangle\). The numbers of graph choices give the weighted total
\[
q^4+q\,q^3+q\,q^3+q\,q^2=q^3(3q+1)
\]
for each ordered pair of distinct projection lines. Multiplying by \(q(q+1)\) proves that the number of ordered nonpermutable pairs is \(q^4(q+1)(3q+1)\), and the displayed formula for \(\operatorname{sd}(L_q)\) follows.

Finally, the leading terms are \(3q^6\) in the nonpermutable-pair count and \(4q^6\) in \(|\mathcal L(L_q)|^2\), giving the limit \(1/4\).

## Verification
The standalone checker `artifacts/verify.py` enumerates every vector subspace of \(\mathbb F_q^4\) in reduced row-echelon form for \(q=2\) and \(q=3\), tests Lie closure, and then tests every ordered pair by the criterion \([A,B]\subseteq A+B\). It obtains \(43\) subalgebras and \(336\) nonpermutable ordered pairs for \(q=2\), and \(104\) subalgebras and \(3240\) nonpermutable ordered pairs for \(q=3\), exactly matching the formulas. It also checks the polynomial identities for \(q=5,7,11\). The run ends with `CHECK_OK`. These finite computations corroborate the proof but are not used as a proof for arbitrary \(q\).

## Relationship to prior work
Muhie, Otera, and Russo introduced the subalgebra commutativity degree for finite-dimensional Lie algebras over finite fields and proved the permutability criterion \([A,B]\subseteq A+B\) in the form used here, citing Amayo. Their Theorem 1.2 computes the degree for the three-dimensional Heisenberg algebra \(\mathfrak h_3(\mathbb F_p)\), obtaining a quantity that tends to \(0\) as \(p\to\infty\). Their paper defines Heisenberg algebras with one-dimensional center and does not treat the four-dimensional central stabilization \(\mathfrak h_3\oplus \mathbb F_q\) in the inspected text. A later exact computation for finite Heisenberg algebras covers the nondegenerate one-dimensional-center family; it does not include this degenerate two-dimensional-center algebra. The present count therefore isolates the effect of a single central stabilization: the limiting degree becomes \(1/4\).

For odd prime \(q=p\), Lazard correspondence identifies this class-two exponent-\(p\) Lie algebra with the group-side central stabilization of the order-\(p^3\) Heisenberg group. Searches for subgroup-commutativity formulas under that equivalent description did not locate the displayed formula; this remains a literature-risk channel rather than evidence of uniqueness.

## Limitations
The result concerns exactly the one-dimensional central stabilization of the three-dimensional Heisenberg algebra. It does not give a formula for arbitrary degenerate alternating Lie algebras, for higher central stabilization dimension, or for noncentral direct sums. The originality comparison cannot exclude terminology-hidden coverage in older subgroup-lattice literature, especially through Lazard correspondence for odd prime fields.

## References
1. S. K. Muhie, D. E. Otera, F. G. Russo, *On the number of modular pairs in finite dimensional Lie algebras on finite fields*, arXiv:2609.19086v1, first public 2026-09-16.
2. M. Tărnăuceanu, *The subgroup commutativity degree of finite P-groups*, arXiv:1312.0296; Bulletin of the Australian Mathematical Society 93 (2016), 37–41.
