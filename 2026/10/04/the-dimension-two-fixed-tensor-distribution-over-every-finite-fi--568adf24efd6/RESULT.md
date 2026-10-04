# The dimension-two fixed-tensor distribution over every finite field

## Finding

Let \(q\) be a prime power and, for
\[
M\in\operatorname{GL}_2(\mathbf F_q),
\]
define
\[
d(M)
=
\dim_{\mathbf F_q}
\operatorname{Eig}_1
\left(
M^T\otimes M^T\otimes M^{-1}
\right).
\]
Write
\[
\epsilon_2=
\begin{cases}
1,&\operatorname{char}\mathbf F_q\ne2,\\
0,&\operatorname{char}\mathbf F_q=2,
\end{cases}
\]
and
\[
\epsilon_+=
\begin{cases}
1,&q\equiv1\pmod3,\\
0,&\text{otherwise},
\end{cases}
\qquad
\epsilon_-=
\begin{cases}
1,&q\equiv2\pmod3,\\
0,&\text{otherwise}.
\end{cases}
\]

Put
\[
N_k(q)
=
\left|
\left\{
M\in\operatorname{GL}_2(\mathbf F_q):d(M)=k
\right\}
\right|.
\]
Then
\[
N_k(q)=0
\]
for every
\[
k\notin\{0,1,2,3,4,8\},
\]
while
\[
\boxed{N_8(q)=1,}
\]
\[
\boxed{
N_4(q)
=
(1-\epsilon_2)(q^2-1)
+
\epsilon_2q(q+1),
}
\]
\[
\boxed{
N_3(q)
=
\epsilon_2(q^2-1)
+
(q-2-\epsilon_2)q(q+1),
}
\]
\[
\boxed{
N_2(q)
=
\epsilon_+q(q+1)
+
\epsilon_-q(q-1),
}
\]
\[
\boxed{
N_1(q)
=
(q-2-\epsilon_2-2\epsilon_+)q(q+1),
}
\]
and
\[
\boxed{
\begin{aligned}
N_0(q)
={}&
(q-2)q^2\\
&+
q(q+1)
\left(
\frac{(q-2)(q-5)}2+\epsilon_2+\epsilon_+
\right)\\
&+
q(q-1)
\left(
\frac{q(q-1)}2-\epsilon_-
\right).
\end{aligned}
}
\]

This is a closed formula for the complete dimension-two slice of the fixed-tensor counting question posed by Verhulst.

As a consistency consequence, Verhulst's Burnside formula becomes
\[
\frac{1}{|\operatorname{GL}_2(\mathbf F_q)|}
\sum_k N_k(q)q^k.
\]
Substitution gives exactly
\[
\boxed{
q^4+q^3+4q^2+3q+6
}
\]
in characteristic \(2\),
\[
\boxed{
q^4+q^3+4q^2+4q+6
}
\]
in characteristic \(3\), and
\[
\boxed{
q^4+q^3+4q^2+4q+7
}
\]
in every other characteristic, agreeing with the classical enumeration of Petersson and Scherer.

## Assumptions and scope

The field \(\mathbf F_q\) is arbitrary and finite. The tensor product and eigenspace are taken over \(\mathbf F_q\).

The result concerns the distribution of the fixed-space dimension
\[
d(M)
\]
for invertible \(2\times2\) matrices. It does not give the corresponding distribution for larger matrix sizes.

The algebra-counting interpretation uses arbitrary bilinear algebra structures: associativity and a unit are not assumed.

## Proof

The quantity \(d(M)\) is constant on similarity classes. Indeed, replacing \(M\) by
\[
SMS^{-1}
\]
conjugates
\[
M^T\otimes M^T\otimes M^{-1}
\]
by an invertible Kronecker-product matrix. We therefore count the four rational-canonical types in
\[
\operatorname{GL}_2(\mathbf F_q).
\]

There are four types:

1. scalar matrices;
2. nonsemisimple matrices with one eigenvalue in \(\mathbf F_q\);
3. split semisimple matrices with two distinct eigenvalues in \(\mathbf F_q^\times\);
4. nonsplit semisimple matrices with irreducible quadratic characteristic polynomial.

Their similarity-class sizes are respectively
\[
1,\qquad
q^2-1,\qquad
q(q+1),\qquad
q(q-1).
\]

For a scalar matrix
\[
M=\lambda I,
\]
the tensor operator equals
\[
\lambda I_8.
\]
Thus the identity has \(d(M)=8\), while the other \(q-2\) nonidentity scalars have \(d(M)=0\).

For the nonsemisimple type write
\[
M=\lambda U,
\qquad
U=
\begin{pmatrix}
1&1\\
0&1
\end{pmatrix}.
\]
Every eigenvalue of the tensor operator is \(\lambda\), so \(d(M)=0\) when
\[
\lambda\ne1.
\]
For \(\lambda=1\), direct row reduction of
\[
U^T\otimes U^T\otimes U^{-1}-I_8
\]
gives rank \(5\) outside characteristic \(2\), and rank \(4\) in characteristic \(2\). One integer \(5\times5\) minor is \(-2\), while a \(4\times4\) minor is \(-1\), and direct row reduction gives the corresponding upper rank bounds. Hence the unipotent class has
\[
d(U)=3
\]
when the characteristic is odd and
\[
d(U)=4
\]
in characteristic \(2\).

Now let \(M\) be split semisimple with distinct eigenvalues
\[
\alpha,\beta\in\mathbf F_q^\times.
\]
Over an eigenbasis the tensor eigenvalues are
\[
\alpha,\alpha,\alpha,
\quad
\beta,\beta,\beta,
\quad
\frac{\alpha^2}{\beta},
\quad
\frac{\beta^2}{\alpha}.
\]
Therefore
\[
d(M)
=
3[\alpha=1]+3[\beta=1]
+
[\alpha^2=\beta]
+
[\beta^2=\alpha].
\]

We count unordered pairs
\[
\{\alpha,\beta\}.
\]
There are \(q-2\) pairs containing \(1\). If the characteristic is odd, the single pair
\[
\{1,-1\}
\]
has \(d=4\); all other pairs containing \(1\) have \(d=3\). Thus the split contributions are
\[
\epsilon_2
\]
classes with \(d=4\) and
\[
q-2-\epsilon_2
\]
classes with \(d=3\).

For pairs not containing \(1\), the extra relations arise from
\[
\beta=\alpha^2.
\]
The map
\[
\alpha\longmapsto\{\alpha,\alpha^2\}
\]
has one exceptional duplication exactly when \(\alpha\) is a nontrivial cube root of unity. Hence there is one pair satisfying both directed squaring relations exactly when
\[
q\equiv1\pmod3;
\]
this pair has \(d=2\). The number of pairs satisfying exactly one directed squaring relation and not containing \(1\) is
\[
q-2-\epsilon_2-2\epsilon_+.
\]
All remaining split pairs have \(d=0\), and their number is
\[
\frac{(q-2)(q-5)}2+\epsilon_2+\epsilon_+.
\]
Multiplying these class counts by the split class size
\[
q(q+1)
\]
gives all split-semismiple terms in the formulas.

Finally let \(M\) have irreducible quadratic characteristic polynomial. Over
\[
\mathbf F_{q^2}
\]
its eigenvalues are
\[
\alpha,\alpha^q
\]
with
\[
\alpha\notin\mathbf F_q.
\]
The only possible eigenvalue \(1\) in the tensor representation comes from
\[
\alpha^2/\alpha^q
\]
and its Frobenius conjugate. Thus
\[
d(M)=2
\]
exactly when
\[
\alpha^{q-2}=1.
\]
But
\[
\gcd(q-2,q^2-1)=\gcd(q-2,3).
\]
Therefore this happens exactly when
\[
q\equiv2\pmod3,
\]
and then the two nontrivial cube roots form one irreducible quadratic conjugacy class. Hence there is exactly one nonsplit class with \(d=2\) when \(\epsilon_-=1\), and none otherwise. Every other nonsplit class has \(d=0\).

There are
\[
\frac{q(q-1)}2
\]
irreducible monic quadratics over \(\mathbf F_q\), and every associated similarity class has size
\[
q(q-1).
\]
Combining the four rational-canonical types yields the stated formulas.

For the Burnside check, substitute the six nonzero \(N_k(q)\) into
\[
\frac{N_0+qN_1+q^2N_2+q^3N_3+q^4N_4+q^8}{q(q-1)^2(q+1)}.
\]
Elementary simplification gives the three displayed characteristic-dependent algebra counts.

## Verification

The included replay constructs
\[
M^T\otimes M^T\otimes M^{-1}
\]
directly for every
\[
M\in\operatorname{GL}_2(\mathbf F_q)
\]
for
\[
q=2,3,4,5,7.
\]
The field \(\mathbf F_4\) is implemented as
\[
\mathbf F_2[t]/(t^2+t+1).
\]

For every matrix it computes the rank of
\[
M^T\otimes M^T\otimes M^{-1}-I_8
\]
by finite-field Gaussian elimination and hence obtains \(d(M)\) independently of the conjugacy-type proof.

The exact enumerated distributions are

\[
q=2:
\quad
(N_2,N_4,N_8)=(2,3,1),
\]
\[
q=3:
\quad
(N_0,N_3,N_4,N_8)=(27,8,12,1),
\]
\[
q=4:
\quad
(N_0,N_2,N_3,N_4,N_8)=(104,20,40,15,1),
\]
\[
q=5:
\quad
(N_0,N_1,N_2,N_3,N_4,N_8)=(285,60,20,84,30,1),
\]
and
\[
q=7:
\quad
(N_0,N_1,N_2,N_3,N_4,N_8)=(1519,112,56,272,56,1).
\]

The replay checks these against the closed formulas, checks that the counts sum to
\[
|\operatorname{GL}_2(\mathbf F_q)|,
\]
and checks that the weighted Burnside sum reproduces the classical number of two-dimensional algebras for every tested field.

The replay returns `VERIFY_OK`.

Finite enumeration is not used to prove the general formulas.

## Relationship to prior work

Verhulst proves that the number of isomorphism classes of \(n\)-dimensional algebras over \(\mathbf F_q\) is
\[
\frac{1}{|\operatorname{GL}_n(\mathbf F_q)|}
\sum_{M\in\operatorname{GL}_n(\mathbf F_q)}
q^{\dim\operatorname{Eig}_1(M^T\otimes M^T\otimes M^{-1})}.
\]
For dimension two, the paper describes the possible Jordan forms, computes the unipotent fixed-space dimension, and works out only the field \(\mathbf F_2\). Its Outlook then explicitly asks for a closed formula counting matrices by the fixed-space dimension for general \(q\) and \(n\).

The theorem here answers that question completely for
\[
n=2
\]
and every finite field. The new information is the entire distribution
\[
N_k(q),
\]
not merely the weighted Burnside sum.

Petersson and Scherer had already obtained the final number of two-dimensional algebra isomorphism classes by classification methods. Their total count is therefore a consistency check, not part of the originality claim. A weighted sum such as Burnside's formula does not determine the individual \(N_k(q)\).

A 2026 clarification by Bekbaev again studies the classification and total number of two-dimensional algebras. Its inspected text contains no tensor-eigenspace distribution and does not address Verhulst's fixed-space counting question.

Searches using the exact tensor expression, fixed-space language, the \(\operatorname{GL}_2(q)\) formulation, and the algebra-enumeration formulation did not locate the displayed distribution.

## Limitations

The result solves only the matrix-dimension-two case of Verhulst's general question. For larger matrix size, rational canonical types and tensor resonances become substantially more complicated.

The proof uses the standard similarity-class classification and centralizer sizes in \(\operatorname{GL}_2(\mathbf F_q)\).

An equivalent formula could exist in invariant-tensor or representation-theoretic terminology not captured by the searches.

Failed searches do not prove novelty.

## References

1. N. D. Verhulst, “Counting finite-dimensional algebras over finite fields,” arXiv:1909.03717v1, first public version 9 September 2019; *Results in Mathematics* 75 (2020), article 153, DOI 10.1007/s00025-020-01281-6.
2. H. P. Petersson and M. Scherer, “The Number of Nonisomorphic Two-dimensional Algebras over a Finite Field,” *Results in Mathematics* 45 (2004), 137–152, DOI 10.1007/BF03323003. Primary MSC 17A01.
3. U. Bekbaev, “On the Classification of Two-Dimensional Algebras,” arXiv:2603.15148v3, 2026.
