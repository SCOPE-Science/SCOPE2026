# An idempotent Drazin inverse needs a squared norm in the \(K\)-\(g\)-fusion lower bound

## Finding
Corollary 3.10 of Huang--Yang states that if \(S\) is a nonzero idempotent Drazin inverse of \(K\), then a \(K\)-\(g\)-fusion frame with lower bound \(A\) is an \(SKS^r\)-\(g\)-fusion frame with lower bound
\[
\frac{A}{\|S\|}
\]
for every positive integer \(r\).

The claimed denominator is too small. The valid universal norm bound is
\[
\frac{A}{\|S\|^2},
\]
and the exponent \(2\) is sharp.

Let
\[
H=\mathbb C^3,
\qquad
S=
\begin{pmatrix}
1&1&0\\
0&0&0\\
0&0&0
\end{pmatrix},
\qquad
K=
\begin{pmatrix}
1&1&0\\
0&0&0\\
0&1&0
\end{pmatrix}.
\]
Then
\[
S^2=S,\qquad
SK=KS=S,\qquad
K^2=S.
\]
Consequently \(S\) is a nonzero idempotent Drazin inverse of \(K\).

Take a one-component \(g\)-fusion system with
\[
W=H,\qquad v=1,\qquad \Lambda=K^*.
\]
For every \(f\in H\),
\[
\|\Lambda f\|^2=\|K^*f\|^2,
\]
so the family has exact \(K\)-lower bound \(A=1\).

Since \(S\) is idempotent and \(SK=S\),
\[
SKS^r=S
\]
for every positive integer \(r\). But
\[
\|S\|=\sqrt2.
\]
For
\[
f=(1,0,-1),
\]
one has
\[
K^*f=(1,0,0),
\qquad
S^*f=(1,1,0).
\]
Thus the coefficient energy is \(1\), whereas the printed lower bound demands
\[
\frac{1}{\sqrt2}\,2=\sqrt2\le1,
\]
which is false.

## Assumptions and scope
The example is finite dimensional and uses one fusion component equal to the whole Hilbert space. Hence there are no convergence, measurability, closure, or domain issues.

The Drazin inverse is used exactly in the sense defined by the source: \(S\) must satisfy
\[
SKS=S,\qquad SK=KS,
\]
and
\[
KSK^k=K^k
\]
for some positive integer \(k\). Here \(k=2\) works.

The corrected statement concerns the universal lower bound that follows from \(A\), \(K\), and the idempotent Drazin inverse \(S\). It does not claim that every individual frame has no better lower bound.

## Proof
First,
\[
S^2=S.
\]
Direct multiplication also gives
\[
SK=S
\]
and
\[
KS=S.
\]
Therefore
\[
SKS=S^2=S.
\]
Moreover,
\[
K^2=S,
\]
so
\[
KSK^2
=
KS^2
=
KS
=
S
=
K^2.
\]
Thus all three Drazin identities hold.

For the one-component family,
\[
W=H
\]
implies that the orthogonal projection onto \(W\) is the identity. With
\[
\Lambda=K^*
\]
and weight \(1\), its \(g\)-fusion coefficient energy is
\[
E(f)=\|\Lambda f\|^2=\|K^*f\|^2.
\]
Hence
\[
\|K^*f\|^2\le E(f)
\]
holds with equality.

Because
\[
S^r=S
\]
for every positive integer \(r\), and because \(SK=S\),
\[
SKS^r=S.
\]
The target lower inequality in Corollary 3.10 is therefore an \(S\)-lower inequality.

The operator norm is obtained from
\[
SS^*=
\begin{pmatrix}
2&0&0\\
0&0&0\\
0&0&0
\end{pmatrix},
\]
so
\[
\|S\|=\sqrt2.
\]
At
\[
f=(1,0,-1),
\]
the exact values are
\[
\|K^*f\|^2=1
\]
and
\[
\|S^*f\|^2=2.
\]
Therefore the claimed bound \(1/\|S\|\) fails.

For the corrected estimate, the Drazin and idempotence identities imply
\[
KS=S.
\]
Taking adjoints gives
\[
S^*=S^*K^*.
\]
Hence
\[
\|S^*f\|
=
\|S^*K^*f\|
\le
\|S\|\,\|K^*f\|.
\]
If a general \(K\)-\(g\)-fusion frame has lower bound \(A\), then
\[
E(f)\ge A\|K^*f\|^2
\ge
\frac{A}{\|S\|^2}\|S^*f\|^2.
\]
Since \(SKS^r=S\), the family is an \(SKS^r\)-\(g\)-fusion frame with lower bound
\[
\frac{A}{\|S\|^2}.
\]

To prove sharpness in the example, write
\[
f=(x,y,z).
\]
Then
\[
K^*f=(x,x+z,0)
\]
and
\[
S^*f=(x,x,0).
\]
Thus
\[
\frac{E(f)}{\|S^*f\|^2}
=
\frac{|x|^2+|x+z|^2}{2|x|^2}
\]
when \(x\ne0\). The ratio is at least \(1/2\), and equality occurs for \(z=-x\). Therefore the optimal \(S\)-lower bound is
\[
\frac12=\frac{1}{\|S\|^2}.
\]

## Verification
The full open-access source was inspected at Definition 2.9, Theorem 3.9, and Corollary 3.10.

Definition 2.9 gives the three Drazin identities used above. Theorem 3.9 obtains the general lower bound
\[
\frac{A}{\|S\|^{2r+2}}.
\]
Corollary 3.10 then states that idempotence improves this to
\[
\frac{A}{\|S\|}.
\]
The matrix example verifies that this latter exponent is incorrect.

The corrected estimate is derived independently from
\[
S^*=S^*K^*
\]
and not from numerical experimentation. The sharpness calculation is an exact minimization with equality attained at \(z=-x\).

## Relationship to prior work
Theorem 3.9 in the same source gives a weaker but valid norm estimate for an arbitrary Drazin inverse. Idempotence removes the dependence on \(r\), because
\[
SKS^r=S.
\]
It does not, however, remove the square that appears after comparing squared Hilbert norms.

The corrected bound
\[
A/\|S\|^2
\]
is stronger than the general Theorem 3.9 bound for every positive integer \(r\), while remaining valid and sharp.

Targeted searches for the exact corollary, Drazin-inverse \(K\)-\(g\)-fusion bounds, idempotent variants, and errata did not locate an indexed correction of the exponent.

## Limitations
The result corrects the lower-bound constant in Corollary 3.10. It does not challenge the qualitative conclusion that the family remains an \(SKS^r\)-\(g\)-fusion frame.

The sharpness statement is for the universal norm-only exponent: particular frames or particular idempotent Drazin inverses may admit larger lower bounds.

A nonindexed erratum, thesis remark, or informal correction may contain the same exponent repair.

## References
1. Y. Huang and Y. Yang, *\(K\)-\(g\)-fusion frames in Hilbert spaces*, Journal of Inequalities and Applications 2020, Article 57, published 28 February 2020, DOI 10.1186/s13660-020-02320-0.
2. Q. Huang, L. Zhu, W. Geng and J. Yu, *Perturbation and expression for inner inverses in Banach spaces and its applications*, Linear Algebra and its Applications 436(9) (2012), 3721--3735.
