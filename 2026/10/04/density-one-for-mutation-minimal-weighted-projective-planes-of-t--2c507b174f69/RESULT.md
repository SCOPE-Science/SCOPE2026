# Density one for mutation-minimal weighted projective planes of type \(\mathbb P(1,a,b)\)
## Finding
For \(N\ge 1\), define
\[
\mathcal W_N=\{(a,b):1\le a\le b\le N,\ \gcd(a,b)=1\}.
\]
The pair \((a,b)\) represents the well-formed weighted projective plane \(\mathbb P(1,a,b)\). Use the height \(h=1+a+b\), and call the weights minimal in the sense of Akhtar--Kasprzyk: no sequence of one-step mutations reaches weights of smaller height.

A member of \(\mathcal W_N\) is non-minimal exactly when
\[
b\ge a+2\qquad\text{and}\qquad b\mid(a+1)^2.
\]
If \(D(N)\) denotes the number of non-minimal members, then the exact identity
\[
D(N)=\sum_{\substack{s\le N\\ s\ \mathrm{squarefree}}}\binom{\lfloor\sqrt{N/s}\rfloor}{2}
\]
holds. Therefore
\[
D(N)=\frac{3}{\pi^2}N\log N+O(N).
\]
Since
\[
|\mathcal W_N|=\sum_{m\le N}\varphi(m)=\frac{3}{\pi^2}N^2+O(N\log N),
\]
the non-minimal proportion satisfies
\[
\frac{D(N)}{|\mathcal W_N|}=\frac{\log N}{N}+O\!\left(\frac1N\right).
\]
Thus, in the natural height box \(1\le a\le b\le N\), asymptotically almost every well-formed plane \(\mathbb P(1,a,b)\) is already height-minimal under one-step mutation.

## Assumptions and scope
Weights are positive, ordered as \(1\le a\le b\), and well formed; for this family well-formedness is equivalent to \(\gcd(a,b)=1\). Minimality is the height-minimality of Akhtar--Kasprzyk, where height is the sum of the three weights. The count concerns ordinary weighted projective planes, not fake weighted projective planes with a nontrivial finite quotient.

The literature input is the one-step mutation criterion for weighted projective planes and the fact that mutation is geometrically realized by a toric deformation. The new statement is the exact enumeration and its asymptotic density in the two-parameter family \(\mathbb P(1,a,b)\).

## Proof
Akhtar--Kasprzyk show that replacing a weight \(\lambda_0\) in \(\mathbb P(\lambda_0,\lambda_1,\lambda_2)\) by a one-step mutation is possible exactly when the corresponding cyclic quotient is a \(T\)-singularity, and in that case the new weight is
\[
\frac{(\lambda_1+\lambda_2)^2}{\lambda_0}.
\]
For an isolated cyclic quotient \(\frac1r(u,v)\), their Lemma 3.8 gives the equivalent criterion \(r\mid(u+v)^2\). Applied to \(\mathbb P(1,a,b)\), a mutation replacing \(b\) exists exactly when \(b\mid(a+1)^2\), and then the new weights are
\[
\left(1,a,\frac{(a+1)^2}{b}\right).
\]
This mutation strictly lowers height exactly when \((a+1)^2/b<b\), equivalently \(b>a+1\). A mutation replacing \(1\) always raises height. If a mutation replacing \(a\) exists, its new weight is \((b+1)^2/a>b\), so it also raises height. Akhtar--Kasprzyk's height lemma gives at most one non-increasing mutation from any weight triple and identifies a unique minimal weight in each mutation tree. Hence \(\mathbb P(1,a,b)\) is non-minimal exactly when \(b\ge a+2\) and \(b\mid(a+1)^2\).

Set \(n=a+1\). The preceding characterization gives
\[
D(N)=\sum_{n=2}^{N-1}\#\{d:d\mid n^2,\ n<d\le N\}.
\]
For a counted divisor \(d\), put \(m=n^2/d\). Then \(m<d\le N\) and \(md\) is a square. Conversely every pair \(m<d\le N\) whose product is a square determines \(n=\sqrt{md}\) and hence one counted pair \((a,b)=(n-1,d)\). The condition that \(md\) be a square means that \(m\) and \(d\) have the same squarefree part. Thus uniquely
\[
m=sv^2,\qquad d=su^2,
\]
with \(s\) squarefree and \(1\le v<u\). For fixed \(s\), the bound \(d\le N\) is \(u\le\lfloor\sqrt{N/s}\rfloor\). Choosing \(v<u\) gives exactly
\[
\binom{\lfloor\sqrt{N/s}\rfloor}{2},
\]
which proves the exact identity.

Write \(q_s=\lfloor\sqrt{N/s}\rfloor\). Then
\[
D(N)=\frac12\sum_{s\le N}\mu^2(s)(q_s^2-q_s)
     =\frac N2\sum_{s\le N}\frac{\mu^2(s)}s+O(N).
\]
The standard identity \(\mu^2(n)=\sum_{d^2\mid n}\mu(d)\), followed by harmonic summation, gives
\[
\sum_{s\le N}\frac{\mu^2(s)}s=\frac6{\pi^2}\log N+O(1).
\]
Therefore \(D(N)=\frac3{\pi^2}N\log N+O(N)\). Finally, \(|\mathcal W_N|=\sum_{m\le N}\varphi(m)\), and the classical summatory-totient estimate yields \(|\mathcal W_N|=\frac3{\pi^2}N^2+O(N\log N)\). Division gives the stated density.

## Verification
The standalone script `verify.py` performs three independent finite checks using exact integer arithmetic. First, for every \(2\le N<80\), and additionally \(N\in\{100,200,500\}\), it compares: (i) direct enumeration of well-formed \((a,b)\) satisfying the descending-mutation condition; (ii) the divisor count \(\sum_n\#\{d:d\mid n^2,\ n<d\le N\}\); and (iii) the squarefree-part formula. Second, for every well-formed \(\mathbb P(1,a,b)\) with \(b<120\), it directly computes the height change for every allowed coordinate mutation and verifies that a strict decrease occurs exactly under the stated criterion. Third, it prints sample exact counts, including \(D(100)=105\), \(D(1000)=1672\), and \(D(10000)=23648\).

The finite checks are regression tests only; the infinite statement is proved by the divisor/squarefree bijection and the classical summatory estimates above.

## Relationship to prior work
Ilten established that the relevant mutations of Laurent-polynomial/toric data give flat families with toric fibers, placing mutation in the algebraic-geometric deformation setting. Akhtar--Kasprzyk give the complete one-step mutation criterion for weighted projective planes, the weight transformation formula, and the height-minimal mutation-tree structure. Kasprzyk--Nill--Prince subsequently develop a broader theory of minimal Fano polygons and mutation-equivalence.

Those sources provide the local mutation rule and the general minimality framework. They do not state the exact squarefree-part enumeration above, nor the resulting density-one theorem for the natural two-parameter family \(\mathbb P(1,a,b)\). The present calculation therefore quantifies how sparse strictly height-descending toric mutations are inside this family.

## Limitations
The result concerns the box ordering \(1\le a\le b\le N\); a different probability model on weights can have a different density. It uses height-minimality for weighted-projective-plane mutation trees, not every notion of minimality for arbitrary Fano polygons. The asymptotic invokes standard estimates for squarefree harmonic sums and the summatory totient function rather than improving their error terms. No claim is made about mutation classes of fake weighted projective planes with nontrivial multiplicity.

## References
1. N. O. Ilten, *Mutations of Laurent Polynomials and Flat Families with Toric Fibers*, SIGMA 8 (2012), 047; arXiv:1205.4664. First public version: 2012-05-21. MSC includes 14M25.
2. M. E. Akhtar and A. M. Kasprzyk, *Mutations of Fake Weighted Projective Planes*, Proc. Edinb. Math. Soc. 59 (2016), 271--285; arXiv:1302.1152. See Proposition 1.1, Lemma 3.8, Definition 3.15, and Lemma 3.16.
3. A. M. Kasprzyk, B. Nill, and T. Prince, *Minimality and Mutation-Equivalence of Polygons*, Forum Math. Sigma 5 (2017), e18; arXiv:1501.05335.
