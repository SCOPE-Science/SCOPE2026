# Linear-window harmonic bias for factorial prime valuations
## Finding
Fix integers \(h\ge 2\), \(c\in\mathbb Z/h\mathbb Z\), and real numbers \(0<\alpha<\beta\le 1\). Define
\[
\Psi_{h,c}(n;\alpha,\beta)
=
\sum_{\substack{\alpha n<p\le \beta n\\ p\ \mathrm{prime}\\ v_p(n!)\equiv c\pmod h}}
v_p(n!)\log p.
\]
Then
\[
\Psi_{h,c}(n;\alpha,\beta)=nC_{h,c}(\alpha,\beta)+o(n),
\]
where
\[
C_{h,c}(\alpha,\beta)
=
\sum_{\substack{j\ge 1\\ j\equiv c\pmod h}}
j\left(\min\!\left\{\beta,\frac1j\right\}
-
\max\!\left\{\alpha,\frac1{j+1}\right\}\right)_+,
\]
and \((x)_+=\max\{x,0\}\). The sum is finite because a positive summand requires \(j<1/\alpha\).

For the aligned top window \(n/(K+1)<p\le n\), with fixed integer \(K\ge1\), this simplifies to
\[
\Psi_{h,c}\!\left(n;\frac1{K+1},1\right)
=
n\sum_{\substack{1\le j\le K\\ j\equiv c\pmod h}}\frac1{j+1}+o(n).
\]
Its total weighted mass is
\[
\left(H_{K+1}-1\right)n+o(n).
\]
Consequently, for \(h=2\), the odd-valuation class has strictly larger first-order mass than the even-valuation class for every fixed \(K\ge2\): pairing \(j=2r-1\) with \(j=2r\) gives \(1/(2r)>1/(2r+1)\), with an additional positive odd term when \(K\) is odd. At \(K=2\), the odd and even coefficients are \(1/2\) and \(1/3\), so their limiting shares are exactly \(3/5\) and \(2/5\).

## Assumptions and scope
The parameters \(h,c,\alpha,\beta\) are fixed while \(n\to\infty\). The statement concerns the weighted prime mass \(v_p(n!)\log p\) only on a linear window \((\alpha n,\beta n]\). It makes no simultaneous-uniformity claim as \(\alpha\downarrow0\), \(h\to\infty\), or \(K\to\infty\) with \(n\).

The motivating result of Ma proves residue-class equidistribution on fixed power bands \((n^a,n^b]\) at the \(\log(n!)\asymp n\log n\) scale. A fixed linear window corresponds to a power-band width of order \(1/\log n\) and has mass only of order \(n\), so that theorem does not determine its first-order residue profile.

## Proof
For fixed \(\alpha>0\), once \(n>\alpha^{-2}\), every prime \(p>\alpha n\) satisfies \(p>\sqrt n\). Legendre's formula therefore collapses exactly to
\[
v_p(n!)=\left\lfloor\frac np\right\rfloor,
\]
because \(p^2>n\).

For each integer \(j\ge1\), the condition \(\lfloor n/p\rfloor=j\) is equivalent to
\[
\frac{n}{j+1}<p\le\frac nj.
\]
Intersecting this cell with \((\alpha n,\beta n]\) gives
\[
nL_j<p\le nU_j,
\qquad
L_j=\max\!\left\{\alpha,\frac1{j+1}\right\},
\qquad
U_j=\min\!\left\{\beta,\frac1j\right\}.
\]
Only finitely many cells have \(U_j>L_j\). Writing \(\vartheta(x)=\sum_{p\le x}\log p\), the definition of \(\Psi_{h,c}\) therefore gives the exact finite decomposition
\[
\Psi_{h,c}(n;\alpha,\beta)
=
\sum_{\substack{j\ge1\\j\equiv c\pmod h\\U_j>L_j}}
j\bigl(\vartheta(nU_j)-\vartheta(nL_j)\bigr)
\]
for all sufficiently large \(n\). The prime number theorem in the form \(\vartheta(x)=x+o(x)\) implies, for every fixed positive \(L_j,U_j\),
\[
\vartheta(nU_j)-\vartheta(nL_j)=n(U_j-L_j)+o(n).
\]
There are only finitely many contributing \(j\), so summation yields
\[
\Psi_{h,c}(n;\alpha,\beta)
=
n\sum_{\substack{j\ge1\\j\equiv c\pmod h}}
j(U_j-L_j)_+ +o(n),
\]
which is the claimed formula.

If \(\alpha=1/(K+1)\) and \(\beta=1\), the contributing cells are exactly \(1\le j\le K\), and
\[
j\left(\frac1j-\frac1{j+1}\right)=\frac1{j+1}.
\]
This proves the aligned-window formula, its harmonic total, and the parity comparison stated above.

## Verification
The standalone verifier implements Legendre's formula directly, sieves all primes through \(2{,}000{,}000\), and checks \(250\) independent finite cases of the exact cell regrouping across several values of \(n\), \(K\), \(h\), and \(c\). It also evaluates the \(h=2\), \(K=2\) profile at four increasing values of \(n\). The observed normalized masses track the proved coefficients \(1/2\) and \(1/3\), and the odd share tracks \(3/5\).

These finite computations corroborate the exact partition and normalization. They are not used to establish the asymptotic, which follows from the symbolic reduction and the prime number theorem.

## Relationship to prior work
Ma, arXiv:2609.37460v1, defines the same weighted observable and proves that for fixed \(h\), fixed residue class, and fixed \(0\le a<b\le1\), the mass on \((n^a,n^b]\) is \(((b-a)/h+o(1))\log(n!)\). The paper explicitly states that its error is not asserted uniform when the endpoints vary with \(n\). The present linear window has moving logarithmic endpoint \(1+\log(\alpha)/\log n\), and its entire mass is one order smaller, so Ma's theorem does not imply the constant \(C_{h,c}(\alpha,\beta)\).

Older work of Luca--Stănică and Berend--Kolesnik studies residue patterns of \(v_p(n!)\) for fixed primes while \(n\) varies. That quantifier structure is different from the present regime, where \(n\) is fixed inside each sum and the prime \(p\) ranges through a moving interval of size comparable to \(n\). Liu--Chen likewise treats a fixed prime in its modulo-three counting problem.

The boundary-scale effect is substantive: equal residue density need not survive at order \(n\). The exact \(3/5\) versus \(2/5\) split for \(n/3<p\le n\) gives a concrete obstruction to extrapolating fixed-power-band equidistribution uniformly all the way to linear endpoint scales.

## Limitations
The result is an iterated fixed-parameter asymptotic. It does not quantify an error term beyond \(o(n)\), does not treat windows whose lower endpoint is \(o(n)\), and does not prove any uniform transition law when \(K\), \(h\), or \(1/\alpha\) grows with \(n\). The originality comparison is necessarily literature-limited: because the proof uses classical Legendre and prime-number-theorem ingredients, an equivalent boundary formula could exist under different terminology even though targeted searches did not locate one.

## References
1. Ma Yicen, *Weighted equidistribution of factorial prime valuations in fixed power bands*, arXiv:2609.37460v1, 2026.
2. F. Luca and P. Stănică, *On the prime power factorization of n!*, Journal of Number Theory 102 (2003), 298–305; arXiv:math/0304272.
3. D. Berend and G. Kolesnik, *Regularity of patterns in the factorization of n!*, Journal of Number Theory 124 (2007), 181–192, DOI 10.1016/j.jnt.2006.08.010.
4. W. Liu and Y.-G. Chen, *On the exponents modulo 3 in the standard factorisation of n!*, Bulletin of the Australian Mathematical Society 73 (2006), 329–334, DOI 10.1017/S000497270003536X.
