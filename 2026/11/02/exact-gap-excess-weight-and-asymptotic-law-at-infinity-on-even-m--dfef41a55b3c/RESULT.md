# Exact gap-excess weight and asymptotic law at infinity on even Ma–Wang maximal curves

## Finding

Let \(q>2\) be a prime power, let \(n\ge4\) be even, and write \(d=q^n\), \(N=d+1\), \(r=(q^{n-1}-1)/(q-1)\), and \(b=q(q-1)\). On the normalization of the Kummer curve
\[
z^N=c(u^q-u)\bigl(1+(u^q-u)^{q-1}\bigr)^r,\qquad c\ne0,
\]
let \(P_\infty\) be its unique point over \(u=\infty\). For the ordered positive gaps \(\ell_1<\dots<\ell_g\) of the Weierstrass semigroup at this point, define the **gap-excess weight** \(W(P_\infty)=\sum_{i=1}^g(\ell_i-i)\). Set
\[
\begin{aligned}
 A(q)&=q^5-q^4+2q^2-3q-1,\\
 B(q)&=2q^6+2q^5-2q^4-8q^3-10q^2+10q+10,\\
 C(q)&=2q^6-2q^5-2q^4.
\end{aligned}
\]
Then the **exact closed polynomial evaluation** is
\[
\boxed{W(P_\infty)=\frac{A(q)q^{2n}+B(q)q^n+C(q)}{24(q+1)}.}
\]
In particular, for each fixed \(q>2\) the normalized gap-excess \(W(P_\infty)/g^2\) is strictly decreasing through even \(n\ge4\), and
\[
\boxed{\lim_{\substack{n\to\infty\\n\ \mathrm{even}}}
\frac{W(P_\infty)}{g^2}=
\frac{A(q)}{6(q+1)(q^2-1)^2}>0.}
\]
The limiting proportion approaches \(1/6\) as \(q\to\infty\) through prime powers. The underlying explicit gap-sequence calculation also yields the conductor
\[
\mathfrak c(P_\infty)=(q^2-1)q^n-q(q-1)\left\lfloor\frac{qr}{q+1}\right\rfloor.
\]
The conductor and semigroup are included for context, not claimed as independent discoveries beyond existing arbitrary-Kummer gap formulas.

## Assumptions and scope

All function-field valuations and gaps are taken on the smooth projective normalization over an algebraic closure of \(\mathbb F_{q^{2n}}\). The constant \(c\) is any nonzero constant; choosing \(c^{q^n}=-c\) gives the rational maximal model of Ma–Wang. The point \(P_\infty\) is rational over that field. The characteristic divides \(q\) but does not divide \(N\), so the Kummer extension is tame. The quantity \(W\) is the intrinsic integer defined from the gap sequence. In small positive characteristic, it is **not** asserted to equal a canonical Wronskian ramification coefficient or to satisfy the characteristic-zero global total-weight formula.

## Proof

**1. Valuations and the pole-order permutation.** Put \(A_0(u)=u^q-u\) and \(B_0(u)=1+(u^q-u)^{q-1}\). The first polynomial has \(q\) distinct roots; the second has \(b=q^2-q\) distinct roots disjoint from the first. Because \(n\) is even, \(r\equiv1\pmod{q+1}\), while
\[
N=br+(q+1),\qquad \gcd(r,N)=1,\qquad \deg(A_0B_0^r)=q+br=N-1=d.
\]
Thus the extension has a unique point over infinity, with \(v_{P_\infty}(u)=-N\) and \(v_{P_\infty}(z)=-d\). At a root of \(B_0\), the corresponding point is totally ramified and \(v(B_0)=N\), \(v(z)=r\); at a root of \(A_0\), \(v(z)=1\). For every \(0\le j<N\), the function
\[
\phi_j=z^j B_0(u)^{-\lfloor jr/N\rfloor}
\]
has no finite pole. Its only possible pole is at infinity, of order
\[
w_j=jd-Nb\left\lfloor\frac{jr}{N}\right\rfloor
=qj+b(jr\bmod N).
\]
Since \(w_j\equiv-j\pmod N\), the \(N\) values \(w_0,\ldots,w_{N-1}\) occupy all residue classes modulo \(N\), and \(w_j+Nt\) are nongaps for all \(t\ge0\). Their union has gap count
\[
\frac1N\sum_{j=0}^{N-1}w_j-\frac{N-1}{2}
=\frac{(q^2-1)(N-1)}2=g,
\]
because multiplication by \(r\) permutes all residues. The genus of the curve is \(g=(q^2-1)q^n/2\), independently established by the Kummer ramification formula. Every point of a smooth curve has exactly \(g\) gaps, so this explicit nongap union is the **entire** Weierstrass semigroup and these are its Apéry representatives with respect to \(N\). This proves completeness without extrapolating a finite enumeration.

**2. Exact gap-sum identity.** For any Apéry representatives \(w_j\) modulo \(N\), their gap sum is
\[
\sum_{i=1}^g\ell_i=
\frac{1}{2N}\sum_{j=0}^{N-1}w_j^2
-\frac12\sum_{j=0}^{N-1}w_j+\frac{N^2-1}{12}.
\]
Indeed, if \(a_j=w_j\bmod N\) and \(h_j=(w_j-a_j)/N\), the gaps in that residue class are \(a_j,a_j+N,\ldots,a_j+(h_j-1)N\). Summing these arithmetic progressions and using that the \(a_j\) permute the residues gives the identity.

**3. Two-step Dedekind reciprocity.** Write \(a_j=jr\bmod N\), and define
\[
s(r,N)=\sum_{j=1}^{N-1}\left(\frac jN-\frac12\right)
\left(\frac{a_j}N-\frac12\right).
\]
Then
\[
\sum_{j=0}^{N-1}ja_j=N^2\left(s(r,N)+\frac{N-1}{4}\right).
\]
The two Euclidean divisions \(N=br+(q+1)\) and \(r\equiv1\pmod{q+1}\), together with the classical Dedekind reciprocity identity and
\(s(1,q+1)=q(q-1)/(12(q+1))\), give
\[
12s(r,N)=b+\frac rN-\frac r{q+1}
+\frac{1}{Nr}-\frac{1}{(q+1)r}
+\frac{q(q-1)}{q+1}.
\]
Now expand \(w_j=qj+ba_j\), use \(\sum j^2=\sum a_j^2=N(N-1)(2N-1)/6\), substitute the displayed Dedekind value into the gap-sum identity, and subtract \(g(g+1)/2\). Collecting the coefficients of \(d^2\), \(d\) and \(1\), where \(d=N-1=q^n\), yields exactly the polynomial \((A(q)d^2+B(q)d+C(q))/(24(q+1))\).

**4. Strict normalized law.** Since \(g=(q^2-1)d/2\),
\[
\frac{W(P_\infty)}{g^2}
=\frac{A(q)}{6(q+1)(q^2-1)^2}
+\frac{B(q)}{6(q+1)(q^2-1)^2d}
+\frac{C(q)}{6(q+1)(q^2-1)^2d^2}.
\]
For \(q\ge3\), all three numerator polynomials are strictly positive: \(A=q^4(q-1)+2q^2-3q-1\), \(C=2q^4(q^2-q-1)\), and
\(B=2[q^4(q^2+q-1)-q^2(4q+5)+5q+5]\). Consequently the ratio decreases strictly as the even integer \(n\) increases. The two stated limits follow from this identity and comparison of the leading powers of \(q\).

**5. Conductor.** Let \(k=\lfloor jr/N\rfloor\). On each fixed-\(k\) block, \(w_j\) increases in \(j\) and reaches its maximum at \(j_k=\lceil(k+1)N/r\rceil-1\). Put \(s=\lceil(k+1)(q+1)/r\rceil\), so \(1\le s\le q+1\). Then
\[
w_{j_k}=b(d-k)+d(s-1).
\]
For each \(s\), this is largest at the smallest permitted \(k=\lfloor(s-1)r/(q+1)\rfloor\). As \(s\) increases, these maxima increase strictly because \(b\lceil r/(q+1)\rceil<d\) (using \(N>q^2-1\)). Thus the largest Apéry representative is \(dq^2-b\lfloor qr/(q+1)\rfloor\). Subtracting \(N-1=d\) gives the conductor stated above. Its defect from the symmetric-semigroup conductor \(2g\) is exactly \(b\lfloor qr/(q+1)\rfloor>0\).

## Verification

The included standalone Python 3 program `verify.py` performs exact integer checks of the Apéry residues, gap genus, gap-excess weight, conductor, and symmetry defect on eleven distinct parameter pairs. For smaller pairs it also evaluates both sides of the Dedekind reciprocity expression using exact rational arithmetic. It checks the examples \((q,n)=(3,4)\), \((4,4)\), \((5,4)\), whose triples \((g,\mathfrak c,W)\) are respectively \((324,594,12906)\), \((1920,3648,449280)\), and \((7500,14500,7026250)\). These finite checks do not replace the universal valuation, Riemann–Roch and reciprocity proof.

## Relationship to prior work

Ma and Wang (2026) introduced the even-exponent Kummer family and computed its genus and branch ramification; their explicit Riemann–Roch functions already provide some nongaps. General theorems of Mendoza (2023), Cotterill–Mendoza–Speziali (2025), and Zhang–Zhao (2026) describe one-point gap sets for arbitrary Kummer extensions; therefore the *existence of an algorithm to obtain this semigroup* is previously known. The present specialized contribution is the **fully evaluated closed polynomial for the gap-excess weight** and its strict all-parameter normalized asymptotic law, obtained by exploiting the unusual two-step Euclidean structure of the branch exponents. Cotterill–Mendoza–Speziali additionally study total ramification-point weight asymptotics for classical curves, which do not directly evaluate this particular positive-characteristic one-point sequence. The closed polynomial should not be confused with a new generic semigroup algorithm.

## Limitations

The theorem covers even \(n\ge4\) and prime-power \(q>2\) only. It concerns the gap-defined weight of the point over infinity, not all points or a complete Weierstrass locus. It does not assert that the curve is classical in characteristic \(p\) or that the classical global Wronskian weight formula applies. The generic Kummer gap theorem already implies an unevaluated sum for this weight; historical originality is limited to the explicit evaluated formula and strict normalized behavior. Independent validation has not been performed.

## References

1. L. Ma and Y. Wang, *A new family of maximal curves not covered by the Hermitian curve*, arXiv:2609.19546 (first posted 2026-09-17), especially Sections 2 and 4. https://arxiv.org/abs/2609.19546
2. E. A. R. Mendoza, *On Kummer extensions with one place at infinity*, arXiv:2208.09729 (2022), published in Finite Fields and Their Applications (2023). https://arxiv.org/abs/2208.09729
3. E. Cotterill, E. A. R. Mendoza, P. Speziali, *On gap sets in arbitrary Kummer extensions of K(x)*, arXiv:2506.19169 (2025), Sections 3–4. https://arxiv.org/abs/2506.19169
4. H. Zhang and C.-A. Zhao, *Weierstrass semigroups at totally ramified places of degree one on Kummer extensions*, arXiv:2605.14583 (2026), Section 3. https://arxiv.org/abs/2605.14583
5. C. M. Shor, *Higher-order Weierstrass weights of branch points on superelliptic curves*, arXiv:1612.02730 (2016), for related weight questions on different branch multiplicities. https://arxiv.org/abs/1612.02730
