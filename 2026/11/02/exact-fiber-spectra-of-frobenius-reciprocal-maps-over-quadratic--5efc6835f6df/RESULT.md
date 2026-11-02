# Exact fiber spectra of Frobenius--reciprocal maps over quadratic finite-field extensions

## Finding
For a prime power \(q\), put \(K=\mathbb F_q\), \(L=\mathbb F_{q^2}\), and let \(a\in L^\times\). Consider
\[
F_a:L^\times\longrightarrow L,\qquad F_a(x)=x^q+\frac a x.
\]
Let \(m_j(a)=\#\{y\in L:\#F_a^{-1}(y)=j\}\). The **complete fiber spectrum**, with every unlisted multiplicity zero, is given below. Zero entries may be suppressed. In the small cases where the labels \(2\) and \(q+1\) coincide, no collision occurs since \(q\ge2\).

**Odd field order.** Write \(N(a)=a^{q+1}\in K^\times\), and \(\chi\) for the quadratic character of \(K^\times\). Then
\[
\begin{array}{c|cccc|c}
\text{coefficient condition}&m_0&m_1&m_2&m_{q+1}&|F_a(L^\times)|\\ \hline
 a\in K^\times &(q^2-1)/2&q+1&(q+1)(q-3)/2&1&(q^2+1)/2\\
 a\notin K,\ \chi(N(a))=1 &(q^2-2q-1)/2&2(q+1)&(q+1)(q-3)/2&0&(q+1)^2/2\\
 a\notin K,\ \chi(N(a))=-1 &(q^2+1)/2&0&(q^2-1)/2&0&(q^2-1)/2
\end{array}
\]
The three coefficient classes have respectively \(q-1\), \((q-1)^2/2\), and \((q^2-1)/2\) members.

**Even field order.** The two classes are
\[
\begin{array}{c|cccc|c}
\text{coefficient condition}&m_0&m_1&m_2&m_{q+1}&|F_a(L^\times)|\\ \hline
 a\in K^\times&q(q+1)/2&0&(q+1)(q-2)/2&1&q(q-1)/2\\
 a\notin K&q(q-1)/2&q+1&(q+1)(q-2)/2&0&q(q+1)/2
\end{array}
\]
These two coefficient classes have \(q-1\) and \(q(q-1)\) members.

For every \(a\in K^\times\), the exceptional fiber is precisely \(F_a^{-1}(0)\), a norm fiber of size \(q+1\); for \(a\notin K\), zero is not in the image. The restriction \(F_a:L^\times\to L^\times\) is a bijection if and only if either \(q=2\) and \(a\notin K\), or \(q=3\), \(a\notin K\), and \(N(a)\) is square.

## Assumptions and scope
All fields are finite. There is no assumption that \(q\) is prime, and the parameter \(a\) runs through **every nonzero element of the quadratic extension**, rather than only the base field. The domain excludes zero, at which the rational expression is undefined. Fiber spectra count targets throughout \(L\), including the non-image target zero for coefficients outside the base field.

## Proof
**Norm reduction and converse.** For \(x\in L^\times\) put \(r=N(x)=x^{q+1}\in K^\times\). Then \(F_a(x)=(r+a)/x\). For a specified nonzero target \(y\), the relation \(yx=r+a\), after taking norms, becomes
\[
 z r = r^2+\operatorname{Tr}_{L/K}(a)\,r+N(a),\qquad z=N(y)\in K^\times.
\]
Consequently admissible \(r\) are the roots in \(K\) of
\[
P_{a,z}(R)=R^2+(\operatorname{Tr}(a)-z)R+N(a).
\]
Its constant coefficient is nonzero, hence each root is nonzero. Also \(r+a\ne0\) for \(z\ne0\), since \(r=-a\) would make the original equation force \(zr=0\). Conversely, given a root \(r\) of this polynomial, define \(x=(r+a)/y\). The root relation gives \(N(x)=r\) and therefore \(F_a(x)=y\). Thus **every root gives exactly one preimage, and there are no other preimages**. Each nonzero \(z\in K\) is the norm of exactly \(q+1\) nonzero targets \(y\in L\). For \(y=0\), the original equation is \(r=-a\); this holds precisely for \(a\in K^\times\), when all \(q+1\) elements in the norm fiber of \(-a\) are preimages.

**Odd characteristic.** Let \(t=\operatorname{Tr}(a)\) and \(n=N(a)\). The discriminant is \(D(z)=(z-t)^2-4n\). If \(a\in K^\times\), then \(D(z)=z(z-4a)\). The discriminant vanishes for exactly one nonzero norm value \(z=4a\), and the elementary identity \(\sum_{z\in K}\chi(z(z-4a))=-1\) gives \((q-3)/2\) two-root norm values and \((q-1)/2\) zero-root norm values. If \(a\notin K\), then \(X^2-tX+n\) is irreducible over \(K\), and hence \(\chi(D(0))=-1\). The identity \(\sum_{z\in K}\chi((z-t)^2-4n)=-1\) yields \(\sum_{z\ne0}\chi(D(z))=0\). There are two nonzero discriminant zeros exactly when \(n\) is a square, and none otherwise: the candidates \(z=t\pm2\sqrt n\) are distinct, and neither can be zero because \(D(0)\) is a nonsquare. Thus in the square-norm case the \(q-3\) nonzero-discriminant norm values split evenly between positive and negative square characters; in the nonsquare case the \(q-1\) values split evenly. Multiplication by \(q+1\) and inclusion of the zero target yields all odd-order rows.

**Even characteristic.** If \(a\in K^\times\), the root equation is \(R^2+zR+a^2=0\). For \(z\ne0\), writing \(R=zu\) shows there are two distinct roots exactly when \(\operatorname{Tr}_{K/\mathbb F_2}(a/z)=0\). As \(z\) ranges through \(K^\times\), this occurs \(q/2-1\) times. If \(a\notin K\), its trace \(t=\operatorname{Tr}(a)\) is nonzero and the irreducibility of its minimal polynomial implies \(\operatorname{Tr}_{K/\mathbb F_2}(n/t^2)=1\). At \(z=t\), the quadratic \(P_{a,z}\) has exactly one root (the Frobenius square root of \(n\)). At other \(z\), put \(w=z+t\ne0\). The equation has two roots exactly when \(\operatorname{Tr}_{K/\mathbb F_2}(\sqrt n/w)=0\). This happens for \(q/2-1\) of the \(q-2\) allowed values \(w\in K^\times\setminus\{t\}\), because the excluded value \(w=t\) has absolute trace one after squaring. Each such root-count datum multiplies by \(q+1\) target values, yielding the even-order rows.

**Coefficient census and bijectivity.** The norm map has \(q+1\) elements per nonzero norm. In odd characteristic every base-field coefficient has square norm, so among all extension coefficients the square-norm class outside \(K\) has \((q-1)^2/2\) members, while the nonsquare class has \((q^2-1)/2\). Even characteristic has no nonzero nonsquares. The image and permutation statements follow directly from the tables and the exceptional zero-fiber condition; only \(q=2\) and \(q=3\) permit an all-singleton nonzero fiber spectrum.

## Verification
The standalone executable `verify_frobenius_reciprocal.py` constructs explicit polynomial-basis models of \(\mathbb F_{p^{2m}}\) using standard-library finite-field arithmetic and independent polynomial irreducibility tests. It computes \(F_a(x)\) directly for every nonzero input in selected finite fields, then compares the full histogram of fiber cardinalities against each formula. Tested base-field orders: \(2,4,8,16,3,9,27,5,25,7,49,11,13,17\); the test covered \(173\) coefficient instances and \(70549\) directly evaluated nonzero inputs. Output:

```
VERIFY_OK fields=14 coefficient_cases=173 direct_nonzero_inputs=70549 types=['base', 'outside_nonsquare', 'outside_square'] all_fibers=PASS
```

This finite verification is corroboration, not a proof for all prime powers. The universal argument is the norm-root equivalence and the quadratic-character or absolute-trace census proved above.

## Relationship to prior work
Ugolini's archival work on maps \(x\mapsto k(x+x^{-1})\) studies finite-field rational-map dynamics and motivates the finite-fiber question. The present family twists one term by field Frobenius, permits an arbitrary extension-field coefficient, and classifies **all** coefficient regimes uniformly across odd and even characteristic. The base-field coefficient case can also be seen through norm-one-torus addition; its value-set size alone is not claimed as a separate novelty. The distinguishing assertion is the complete extension-coefficient fiber distribution and its exact norm-square dichotomy. General reciprocal-map results may overlap and remain a literature risk.

## Limitations
The theorem concerns a quadratic extension and a nonzero coefficient. It does not provide a dynamical functional graph or generalize unchanged to higher extension degrees. The archival source comparison and available result searches do not establish universal historical priority; a systematic independent literature audit has not been performed.

## References
1. S. Ugolini, *On the iterations of certain maps \(x\mapsto k(x+x^{-1})\) over finite fields of odd characteristic*, arXiv:1304.3283, first public 2013-04-11, https://arxiv.org/abs/1304.3283 .
