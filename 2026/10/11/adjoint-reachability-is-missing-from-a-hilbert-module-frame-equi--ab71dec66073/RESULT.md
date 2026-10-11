# Adjoint reachability is missing from a Hilbert-module frame equivalence

## Finding
Rossafi--Kabbaj prove that a sequence in
\[
End_{\mathcal A}^*(\mathcal H,\mathcal K)
\]
is a frame for that operator Hilbert module if and only if it is a \(g\)-frame for \(\mathcal H\) with respect to \(\mathcal K\). The statement is Theorem 3.4 in the first public preprint and Theorem 2 in the published article. Its converse is false for general Hilbert \(C^*\)-modules.

Let
\[
\mathcal A=\mathbb C\oplus\mathbb C,\qquad
p=(1,0),\qquad
q=(0,1).
\]
Take
\[
\mathcal H=\mathcal A,\qquad
\mathcal K=\mathcal A p,
\]
with the standard left Hilbert-\(\mathcal A\) module inner products
\[
\langle x,y\rangle_{\mathcal A}=xy^*.
\]
Define
\[
P:\mathcal H\to\mathcal K,\qquad P(a)=pa.
\]
The adjoint
\[
P^*:\mathcal K\to\mathcal H
\]
is the inclusion. Hence
\[
Q:=P^*P
\]
is the orthogonal module projection given by multiplication by \(p\).

For every
\[
T\in End_{\mathcal A}^*(\mathcal H,\mathcal K)
\]
one has
\[
TQ=T.
\]
Indeed, \(T(ph)=pT(h)=T(h)\), because \(T(h)\in\mathcal A p\) and \(p\) acts as the identity on \(\mathcal A p\). Therefore
\[
\langle T,P\rangle\langle P,T\rangle
=
TP^*PT^*
=
TQT^*
=
TT^*
=
\langle T,T\rangle.
\]
Thus the singleton \(\{P\}\) is a Parseval frame for the operator module under the source's Definition 3.1.

But it is not a \(g\)-frame for \(\mathcal H\) with respect to \(\mathcal K\). At the nonzero vector \(q\),
\[
Pq=pq=0,
\qquad
\langle q,q\rangle_{\mathcal A}=q.
\]
Consequently no positive scalar \(C\) can satisfy
\[
C\langle q,q\rangle_{\mathcal A}
\le
\langle Pq,Pq\rangle_{\mathcal A}.
\]

The source's forward implication from \(g\)-frames to operator-module frames survives. The failure is in the converse, where the proof takes an arbitrary \(y\in\mathcal H\) and then chooses \(T\) and \(x\) satisfying \(T^*x=y\) without establishing that such a pair exists.

## Assumptions and scope
The \(C^*\)-algebra \(\mathcal A=\mathbb C\oplus\mathbb C\) is unital. Both \(\mathcal H=\mathcal A\) and \(\mathcal K=\mathcal A p\) satisfy the Hilbert-module definition used in the source; that definition does not impose fullness.

The operator module is nonzero: it contains \(P\). The counterexample therefore does not rely on declaring a sequence a frame in the zero module.

The conclusion concerns the converse direction of the stated frame/\(g\)-frame equivalence. It does not dispute the implication obtained by multiplying a \(g\)-frame operator inequality on the left and right by \(T\) and \(T^*\).

## Proof
For \(k\in\mathcal K\) and \(h\in\mathcal H\),
\[
\langle Ph,k\rangle_{\mathcal A}
=
(ph)k^*
=
hk^*
=
\langle h,k\rangle_{\mathcal A},
\]
because \(k=pk\). Thus \(P^*\) is the inclusion \(\mathcal K\hookrightarrow\mathcal H\), and
\[
P^*P=Q,\qquad Qh=ph.
\]

If \(T:\mathcal H\to\mathcal K\) is adjointable, it is \(\mathcal A\)-linear. Hence
\[
TQh=T(ph)=pT(h)=T(h).
\]
Using the source's operator-module inner product
\[
\langle T,S\rangle=TS^*,
\]
we obtain
\[
\langle T,P\rangle\langle P,T\rangle
=
(TP^*)(PT^*)
=
T(P^*P)T^*
=
TQT^*
=
TT^*
=
\langle T,T\rangle.
\]
This is exactly the frame inequality with both frame bounds equal to \(1\).

For the \(g\)-frame inequality, choose \(q=(0,1)\). Then
\[
Pq=0
\]
but
\[
\langle q,q\rangle_{\mathcal A}=q>0.
\]
The required lower inequality would read
\[
Cq\le0
\]
for some scalar \(C>0\), which is impossible.

The failed reachability step can also be seen directly. For every \(T\) and every \(k\in\mathcal K\),
\[
qT^*k=T^*(qk)=0,
\]
because \(qk=0\). Therefore
\[
R(T^*)\subseteq\mathcal A p
\]
for every adjointable \(T:\mathcal H\to\mathcal K\), so the vector \(q\) can never have the form \(T^*k\).

A sufficient repair is the adjoint-reachability property
\[
\forall y\in\mathcal H\ \exists T,\ k
\quad
T^*k=y.
\]
Under that assumption, the source's operator inequality can legitimately be evaluated at a representation of each \(y\), yielding the \(g\)-frame bounds.

There is a simple checkable condition implying reachability. Suppose \(\mathcal K\) contains \(e\) with
\[
\langle e,e\rangle_{\mathcal A}=1_{\mathcal A}.
\]
For \(y\in\mathcal H\), define
\[
R_y(h)=\langle h,y\rangle_{\mathcal A}e.
\]
Then
\[
R_y^*k=\langle k,e\rangle_{\mathcal A}y.
\]
Indeed,
\[
\langle R_yh,k\rangle_{\mathcal A}
=
\langle h,y\rangle_{\mathcal A}\langle e,k\rangle_{\mathcal A}
=
\langle h,R_y^*k\rangle_{\mathcal A}.
\]
Consequently
\[
R_y^*e=y.
\]
Thus the theorem's converse is valid whenever the coefficient module has such a unit vector.

## Verification
The first public full text was inspected at the Hilbert-module convention, the definition of \(g\)-frames, the definition of frames for \(End_{\mathcal A}^*(\mathcal H,\mathcal K)\), and the complete proof of Theorem 3.4. The proof explicitly introduces an arbitrary \(y\in\mathcal H\) and then assumes a representation \(T^*x=y\).

The published open-access article retains the same statement as Theorem 2 and the same converse step. The article also states that it generalizes an earlier result for \(B(H,K)\), where \(H\) and \(K\) are Hilbert spaces.

Every identity in the counterexample is exact. No finite experiment, numerical approximation, or unproved computational certificate is used.

## Relationship to prior work
Askarizadeh--Dehghan prove the corresponding equivalence for the special Hilbert \(C^*\)-module \(B(H,K)\) built from ordinary Hilbert spaces. That setting has the reachability property used implicitly in the later proof: if \(e\in K\) is a unit vector, rank-one operators can be chosen so that \(T^*e=y\) for any \(y\in H\).

The later source advertises its result as a Hilbert-\(C^*\)-module generalization of that special case. The counterexample shows that the rank-one reachability mechanism is not automatic for arbitrary Hilbert modules.

Exact-title, theorem, operator-module, adjoint-range, and Hilbert-module searches did not locate an indexed correction giving this counterexample or adding the missing reachability condition.

## Limitations
The unit-vector condition on \(\mathcal K\) is sufficient, not claimed necessary. More general pairs \((\mathcal H,\mathcal K)\) may satisfy adjoint reachability without containing such a vector.

The finding does not classify all module pairs for which the frame/\(g\)-frame equivalence holds, and it does not assess the paper's other generalized equivalence theorems. An unindexed erratum, thesis remark, or informal correction may contain the same observation.

The full text of the 2013 precursor could not be retrieved from the journal endpoint during this check; its publisher abstract and metadata were inspected, and no whole-document negative claim about that paper is used.

## References
1. M. Rossafi and S. Kabbaj, *Some Generalizations of Frames in Hilbert Modules*, arXiv:1805.11655v1, 29 May 2018; International Journal of Mathematics and Mathematical Sciences 2021, article 5522671, DOI 10.1155/2021/5522671.
2. A. Askarizadeh and M. A. Dehghan, *G-frames as special frames*, Turkish Journal of Mathematics 37 (2013), 60--70, DOI 10.3906/mat-1011-533.
