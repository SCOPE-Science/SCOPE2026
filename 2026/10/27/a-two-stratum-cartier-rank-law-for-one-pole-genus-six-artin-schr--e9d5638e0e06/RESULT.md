# A two-stratum Cartier-rank law for one-pole genus-six Artin–Schreier curves in characteristic three

## Finding
Let \(k\) be algebraically closed of characteristic \(3\), and let \(a,b,c,d\in k\). Define \(C_{a,b,c,d}\) to be the smooth projective curve with function field
\[
k(x,y),\qquad y^3-y=x^7+a x^5+b x^4+c x^2+d x.
\]
Then \(C_{a,b,c,d}\) has genus \(6\), Jacobian 3-rank \(0\), and
\[
\bigl(\operatorname{rank}\mathcal C,\operatorname{rank}\mathcal C^2,
\operatorname{rank}\mathcal C^3\bigr)
=\begin{cases}(3,1,0),&a\ne0,\\ (2,1,0),&a=0.\end{cases}
\]
Consequently its Jacobian has a-number
\[
a(C_{a,b,c,d})=\begin{cases}3,&a\ne0,\\4,&a=0.\end{cases}
\]
The locus with a-number \(4\) in this four-parameter monic reduced coefficient space is exactly the reduced irreducible hypersurface \(V(a)\). All other three coefficients are unconstrained. Both values occur; neither a-number \(5\) nor \(6\) occurs in this one-pole genus-six family. These statements concern the natural marked coefficient chart and do not assert the scheme-theoretic equation of a stratum in the unmarked moduli stack.

## Assumptions and scope
The base field \(k\) is algebraically closed of characteristic \(3\). The pole order of the right-hand side at \(x=\infty\) is exactly \(7\) for every coefficient choice. The Artin–Schreier cover \(x:C\to\mathbb P^1\) has its sole ramification point above infinity. The affine equation is smooth because its partial derivative with respect to \(y\) is \(-1\). Moreover, a degree-seven pole cannot arise from a function of the form \(h^3-h\), since such a pole has order divisible by \(3\). Thus the Artin–Schreier polynomial is irreducible over \(k(x)\) and its smooth projective normalization is connected.

Any one-pole Artin–Schreier cover with pole order \(7\) admits a monic reduced affine presentation of the indicated form over an algebraically closed field: translate and rescale \(x\), remove monomials of degree divisible by \(3\) by an Artin–Schreier change of \(y\), and remove the constant term. The theorem is stated for all displayed presentations; the assertion \(V(a)\) refers to this coefficient chart rather than to a canonical normalization of the coarse moduli space.

## Proof
By the one-pole Artin–Schreier genus and Deuring–Shafarevich formulas, the genus is
\[
g=\frac{(3-1)(7-1)}2=6,
\]
and the 3-rank is \(0\). Write \(P\) for the unique point above infinity. The valuations are \(v_P(x)=-3\) and \(v_P(y)=-7\). The different exponent of the covering at \(P\) equals \((3-1)(7+1)=16\), whence
\[
\operatorname{div}(dx)=(16-2\cdot 3)P=10P.
\]
Thus the differentials
\[
\mathcal B=(dx,\ x\,dx,\ x^2dx,\ x^3dx,\ y\,dx,\ xy\,dx)
\]
are regular, because the corresponding pole weights \(3i+7j\) do not exceed \(10\). They have pairwise distinct pole orders and, as their number is \(g=6\), constitute a basis of \(H^0(C,\Omega_C^1)\).

The modified Cartier operator \(\mathcal C\) is additive and \(1/3\)-linear, satisfies \(\mathcal C(h^3\omega)=h\mathcal C(\omega)\), and acts on rational monomial differentials by
\[
\mathcal C(x^m dx)=
\begin{cases}x^{(m-2)/3}dx,&m\equiv2\pmod3,\\0,&m\not\equiv2\pmod3.\end{cases}
\]
Set \(f(x)=x^7+a x^5+b x^4+c x^2+d x\). Since \(y=y^3-f(x)\), the Cartier identities on the chosen basis are
\[
\begin{aligned}
&\mathcal C(dx)=\mathcal C(xdx)=\mathcal C(x^3dx)=0,\\
&\mathcal C(x^2dx)=dx,\\
&\mathcal C(y\,dx)=-a^{1/3}x\,dx-c^{1/3}dx,\\
&\mathcal C(xy\,dx)=-x^2dx-b^{1/3}x\,dx-d^{1/3}dx.
\end{aligned}
\]
Here the cube roots are uniquely determined because \(k\) is perfect. The image always contains \(dx\) and a vector with a nonzero \(x^2dx\) coefficient. It also contains a third independent \(x\,dx\) direction exactly when \(a\ne0\). Therefore \(\operatorname{rank}\mathcal C=3\) for \(a\ne0\) and \(2\) for \(a=0\).

Every image lies in \(\langle dx,x\,dx,x^2dx\rangle\); another Cartier application kills the first two generators and takes \(x^2dx\) to \(dx\). The image of \(\mathcal C^2\) is exactly \(\langle dx\rangle\), since \(\mathcal C(xy\,dx)\) has coefficient \(-1\) at \(x^2dx\). The third iterate is zero. The a-number is \(g-\operatorname{rank}\mathcal C\), giving the stated complete classification.

Finally, \(k[a,b,c,d]\) is a polynomial ring; the equation \(a=0\) cuts out a reduced irreducible divisor, with both sides populated by coefficient choices. This is a statement about the monic reduced presentation space, not a computation of stack-theoretic multiplicity.

## Verification
The accompanying standalone script `verify_cartier.py` uses exact arithmetic in \(\mathbb F_3\) and \(\mathbb F_9\). It constructs all six Cartier images directly from the monomial congruence rule and the equation, forms the semilinear iterates, and checks their ranks for every \((a,b,c,d)\) over those fields. All \(3^4=81\) and \(9^4=6561\) coefficient tuples pass, with a-number counts \((54,27)\) over \(\mathbb F_3\) and \((5832,729)\) over \(\mathbb F_9\) for a-numbers \((3,4)\), respectively. These computations are reproducibility checks; the preceding symbolic identities prove the universal statement over algebraically closed fields.

## Relationship to prior work
Farnell–Pries [1] prove coefficient-independent a-numbers in the regime \(p\equiv1\pmod L\), where \(L\) is the least common multiple of ramification pole orders. That theorem does not apply here, because the only pole order is \(7\) and the characteristic is \(3\). Zhou [2, Proposition 2.5] bounds the genus and possible polynomial degree when the a-number equals the genus minus two; the statement permits, but does not compute, the entire degree-seven genus-six family or the exact jumping equation. Pries–Zhu [3] classify components of Artin–Schreier moduli by p-rank; the p-rank-zero conclusion here is already classical and is not claimed as new. Farnell's dissertation [4] describes the general differential and Cartier framework, with its main coefficient-independent theorem under pole-order divisibility conditions not met here.

The distinct point here is the full coefficientwise characteristic-three degree-seven a-number stratification together with the ranks of every Cartier iterate. These calculations use classical identities; they do not assert a new general formula for all Artin–Schreier curves.

## Limitations
The finding concerns the one-pole genus-six Artin–Schreier family and a chosen monic reduced coefficient space. It does not classify all characteristic-three genus-six curves or all Artin–Schreier ramification partitions. The Cartier rank profile is not claimed to be a complete Ekedahl–Oort or Newton-polygon classification. No external independent mathematical audit has been performed. Published equivalent computations in specialized theses or tables under different notation remain a possible source-overlap risk.

## References
[1] S. Farnell and R. Pries, *Families of Artin–Schreier curves with Cartier–Manin matrix of constant rank*, arXiv:1202.4183 (first public preprint 2012-02-19), https://arxiv.org/pdf/1202.4183.

[2] Z. Zhou, *On the existence of curves with prescribed a-number*, arXiv:1901.08375 (2019), https://arxiv.org/pdf/1901.08375.

[3] R. Pries and H. J. Zhu, *The p-rank stratification of Artin–Schreier curves*, Ann. Inst. Fourier 62 (2012), 707–726, https://www.numdam.org/item/10.5802/aif.2692.pdf.

[4] S. Farnell, *Artin–Schreier Curves*, doctoral dissertation (2010), https://mountainscholar.org/bitstreams/b29bf91f-4848-4aca-b33f-e67f23037554/download.
