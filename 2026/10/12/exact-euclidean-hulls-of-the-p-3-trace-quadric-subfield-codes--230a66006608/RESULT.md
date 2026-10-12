# Exact Euclidean hulls of the \(p^3\) trace-quadric subfield codes
## Finding

Let
\[
p\equiv3\pmod4
\]
be prime, let
\[
\operatorname{Tr}=\operatorname{Tr}_{p^3/p},
\]
and define
\[
S=
\{(x,y)\in\mathbb F_{p^3}^2:
\operatorname{Tr}(x^2+y^2)=0\}.
\]

Consider the punctured code
\[
C^*
=
\left\{
\bigl(a+\operatorname{Tr}(bx+cy)\bigr)_{(x,y)\in S}:
a\in\mathbb F_p,\ b,c\in\mathbb F_{p^3}
\right\}.
\]
This is the punctured Section 4 family of Liu, Liu, and Yu. Their Theorem 4.4 gives dimension \(7\).

Then
\[
C^*\subseteq (C^*)^\perp,
\]
so its Euclidean hull is the whole code:
\[
\operatorname{Hull}(C^*)=C^*,
\qquad
\dim \operatorname{Hull}(C^*)=7.
\]

For the corresponding unpunctured source code
\[
C=
\left\{
\left(
\operatorname{Tr}(b),
\bigl(a+\operatorname{Tr}(bx+cy)\bigr)_{(x,y)\in S}
\right):
a\in\mathbb F_p,\ b,c\in\mathbb F_{p^3}
\right\},
\]
the Euclidean hull is exactly
\[
\operatorname{Hull}(C)
=
\{c_{a,b,c}\in C:\operatorname{Tr}(b)=0\}.
\]
Consequently
\[
\dim\operatorname{Hull}(C)=6.
\]

Thus puncturing the first coordinate raises the hull dimension from \(6\) to \(7\) and turns the entire seven-dimensional family into a self-orthogonal family.

## Assumptions and scope

The construction is exactly the one in Section 4 of the source, where
\[
f(x,y)=\operatorname{Tr}(x^2+y^2)
\]
over \(\mathbb F_{p^3}\) and \(p\equiv3\pmod4\).

The source gives
\[
|S|=p^5-p^3+p^2,
\]
so the punctured code has length
\[
n=p^5-p^3+p^2,
\]
dimension \(7\), and minimum distance
\[
p^5-p^4-p^3+p^2.
\]
The unpunctured code has length \(n+1\) and dimension \(7\).

The Euclidean inner product is used throughout:
\[
\langle u,v\rangle=\sum_i u_iv_i.
\]

## Proof

First suppose
\[
p>3.
\]
The defining set \(S\) is invariant under multiplication by any scalar
\[
\lambda\in\mathbb F_p^\times,
\]
because
\[
\operatorname{Tr}((\lambda x)^2+(\lambda y)^2)
=
\lambda^2\operatorname{Tr}(x^2+y^2).
\]

Let
\[
\ell,\mu:\mathbb F_{p^3}^2\longrightarrow\mathbb F_p
\]
be arbitrary \(\mathbb F_p\)-linear forms.

For the first moment,
\[
A=\sum_{z\in S}\ell(z).
\]
Scalar invariance gives
\[
A
=
\sum_{z\in S}\ell(\lambda z)
=
\lambda A.
\]
Choosing \(\lambda\ne1\) gives \(A=0\).

For the second moment,
\[
B=\sum_{z\in S}\ell(z)\mu(z).
\]
Again,
\[
B
=
\sum_{z\in S}\ell(\lambda z)\mu(\lambda z)
=
\lambda^2B.
\]
Because \(p>3\), there is a scalar with \(\lambda^2\ne1\), so \(B=0\).

Now take two punctured codewords
\[
u=(a+\ell(z))_{z\in S},
\qquad
v=(a'+\mu(z))_{z\in S}.
\]
Their inner product is
\[
\langle u,v\rangle
=
aa'|S|
+
a\sum_{z\in S}\mu(z)
+
a'\sum_{z\in S}\ell(z)
+
\sum_{z\in S}\ell(z)\mu(z).
\]
Since
\[
|S|=p^5-p^3+p^2
\]
is divisible by \(p\), and the first and second moments vanish, every term is zero. Hence
\[
C^*\subseteq(C^*)^\perp
\]
for every \(p>3\) with \(p\equiv3\pmod4\).

It remains to handle \(p=3\). The source's Example 4.5 gives the punctured ternary code
\[
[225,7,144]_3
\]
with weight enumerator
\[
1+952z^{144}+1008z^{153}+224z^{162}+2z^{225}.
\]
Every nonzero weight is divisible by \(3\). Over \(\mathbb F_3\), every nonzero scalar has square \(1\), so for every codeword \(u\),
\[
\langle u,u\rangle
=
\operatorname{wt}(u)
\equiv0\pmod3.
\]
Thus every codeword is isotropic. Since \(2\) is invertible in \(\mathbb F_3\), polarization gives
\[
2\langle u,v\rangle
=
\langle u+v,u+v\rangle-\langle u,u\rangle-\langle v,v\rangle
=
0.
\]
Therefore \(\langle u,v\rangle=0\) for all \(u,v\in C^*\), proving self-orthogonality also for \(p=3\).

The source gives \(\dim C^*=7\), so
\[
\operatorname{Hull}(C^*)=C^*
\]
has dimension \(7\).

For the unpunctured code, the source trace representation shows that the extra first coordinate of \(c_{a,b,c}\) is
\[
\operatorname{Tr}(b).
\]
The punctured parts are mutually orthogonal by the result just proved. Hence
\[
\langle c_{a,b,c},c_{a',b',c'}\rangle
=
\operatorname{Tr}(b)\operatorname{Tr}(b').
\]

The finite-field trace map
\[
\operatorname{Tr}_{p^3/p}:\mathbb F_{p^3}\longrightarrow\mathbb F_p
\]
is surjective. Therefore a codeword \(c_{a,b,c}\) is orthogonal to every codeword in \(C\) if and only if
\[
\operatorname{Tr}(b)=0.
\]
This proves
\[
\operatorname{Hull}(C)
=
\{c_{a,b,c}:\operatorname{Tr}(b)=0\}.
\]
Because this is one nonzero linear condition on the seven-dimensional source parameter space,
\[
\dim\operatorname{Hull}(C)=6.
\]

## Verification

`artifacts/verify.py` uses only the Python standard library.

It constructs cubic extensions of \(\mathbb F_3\) and \(\mathbb F_7\) from irreducible monic cubic polynomials, implements the field trace, reconstructs \(S\), and forms the seven natural generator rows: the constant row, three \(b\)-trace rows, and three \(c\)-trace rows.

For \(p=3\) and \(p=7\), the script checks
\[
|S|=p^5-p^3+p^2,
\]
rank \(7\), and a zero punctured Gram matrix.

For \(p=3\), it enumerates all \(3^7\) codewords and independently recovers
\[
1+952z^{144}+1008z^{153}+224z^{162}+2z^{225}.
\]

For the unpunctured generators, the script appends the first coordinate prescribed by the source and verifies that the Gram matrix is the rank-one outer product of the trace-coordinate functional with itself. Its radical therefore has dimension \(6\).

Successful replay prints `VERIFY_OK`.

## Relationship to prior work

Liu, Liu, and Yu determine the complete weight distributions of these punctured and unpunctured Section 4 codes. Their Theorems 4.2 and 4.4 give dimensions, minimum distances, and dual minimum distance \(3\), and Example 4.5 gives the ternary \([225,7,144]\) instance. The article does not state Euclidean self-orthogonality or compute the Euclidean hull of either version.

General recent hull literature develops hull-prescription methods for other families such as generalized Reed--Solomon, Roth--Lempel, and transformed linear codes. No inspected result identifies the present trace-quadric family or implies the exact \(7\)- and \(6\)-dimensional hulls above.

Focused searches for the source title together with hull or self-orthogonality terminology, for the length formula
\[
p^5-p^3+p^2,
\]
and for the exact ternary parameters
\[
[225,7,144]_3
\]
found no prior statement of these hulls.

## Limitations

The theorem concerns the Section 4 family with extension degree \(3\), quadratic trace function
\[
\operatorname{Tr}(x^2+y^2),
\]
and primes \(p\equiv3\pmod4\). It does not classify hulls of every family in the source.

For \(p=3\), the proof uses the complete source weight enumerator. For \(p>3\), the proof is structural and uses scalar invariance of the defining set.

No claim is made that stabilizer codes formed through standard self-orthogonal-code constructions have new optimal quantum parameters.

## References

1. Shanshan Liu, Yan Liu, and Xiaoyu Yu, *Weight distributions of subfield codes from special functions*, AIMS Mathematics 11 (2026), 2797--2815, DOI 10.3934/math.2026112.
2. V. K. Wei, *Generalized Hamming weights for linear codes*, IEEE Transactions on Information Theory 37 (1991), 1412--1418.
