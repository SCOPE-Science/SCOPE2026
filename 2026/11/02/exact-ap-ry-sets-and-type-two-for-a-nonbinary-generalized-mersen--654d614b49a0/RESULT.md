# Exact Apéry sets and type two for a nonbinary generalized-Mersenne family

## Finding

For integers \(h\ge3\), \(m\ge1\), and \(d\ge1\), put
\[
 b=h^2-h+1,\qquad c=h^3-h+1,\qquad a=mc,
\]
and assume \(\gcd(a,d)=1\). Consider the numerical semigroup
\[
 S=\langle a,\;ha+d,\;h^2a+bd,\;h^3a+cd\rangle.
\]
For \(0\le r<a\), write uniquely \(r=jc+qb+u\), where \(j=\lfloor r/c\rfloor\), \(0\le qb+u<c\), \(q=\lfloor(r-jc)/b\rfloor\), and \(0\le u<b\). Define \(w(r)=h^3j+h^2q+hu\). The entire Apéry set, indexed by residues modulo \(a\), is
\[
 \operatorname{Ap}(S,a)=\{aw(r)+dr:0\le r<a\},
 \quad aw(r)+dr\equiv dr\pmod a.
\]
Set \(T=(m-1)h^3+2h^2(h-1)\). Then the Frobenius number, genus, and pseudo-Frobenius set are **exactly**
\[
 F(S)=a(T-1)+d(a-1),
\]
\[
 g(S)=\frac{mc h^3(m-1)}2
  +\frac{m h^2(h-1)(2h^3+h^2-3h+2)}2
  +\frac{(d-1)(a-1)}2,
\]
\[
 \operatorname{PF}(S)=\{F(S)-d(h-1)^2,\ F(S)\},\qquad
 \operatorname{type}(S)=2.
\]
In particular, the two pseudo-Frobenius numbers are separated by exactly \(d(h-1)^2\), independently of \(m\). The four displayed generators need not form a minimal generating set when \(m=1\); the formulas still hold.

## Assumptions and scope

All semigroups are additive submonoids of \(\mathbb N_0\). The genus counts all missing nonnegative integers (equivalently all positive gaps). The Frobenius number is the largest gap. A pseudo-Frobenius number is an integer \(f\notin S\) for which \(f+s\in S\) for every nonzero \(s\in S\). The Apéry set with respect to \(a\in S\) consists of the least semigroup element in each residue class modulo \(a\). The condition \(\gcd(a,d)=1\) ensures that the residues \(dr\) run through all classes. There is no restriction on the relative sizes of \(m\) and \(d\) beyond the hypotheses. The separate binary specialization \(h=2\) is not presented as a new result.

## Proof

**1. Exact weighted change-making.** For \(M\in\mathbb N_0\), consider all \((x,y,z)\in\mathbb N_0^3\) with \(M=x+by+cz\), and minimize \(hx+h^2y+h^3z\). Put \(t=(h-1)^2\). Direct calculation gives
\[
 hb+t=c,\qquad (h+1)b=c+h,\qquad b-t=h.
\]
There are three legal exchanges: replace \(b\) unit coins by one \(b\)-coin (strict cost decrease of \(h(h-1)^2\)); replace \(h+1\) \(b\)-coins by one \(c\)-coin and \(h\) unit coins (cost unchanged); replace \(h\) \(b\)-coins and \(t\) unit coins by one \(c\)-coin (strict cost decrease of \(ht\)). Repeatedly apply these exchanges whenever possible. Termination follows by lexicographically decreasing the integer pair (total weighted cost, negative number of \(c\)-coins); this pair is bounded on representations of a fixed \(M\). At termination \(x<b\), \(y\le h\), and \(y=h\) forces \(x<t\). Hence \(by+x<c\), so necessarily \(z=\lfloor M/c\rfloor\), \(y=\lfloor (M-zc)/b\rfloor\), and \(x=M-zc-by\). The terminal representation is the unique greedy one and is no more expensive than the starting representation. Thus the minimum is
\[
 w(M)=h^3\left\lfloor\frac M c\right\rfloor
 +h^2\left\lfloor\frac{M\bmod c}{b}\right\rfloor
 +h\bigl((M\bmod c)\bmod b\bigr).
\]
In particular \(w(M+qc)=w(M)+qh^3\) for every integer \(q\ge0\).

**2. Apéry formula.** Any element obtained from the last three generators without using \(a\) has the form \(a(hx+h^2y+h^3z)+dM\), with \(M=x+by+cz\). In residue class \(dr\pmod a\), \(0\le r<a\), the nonnegative integers \(M\) must be \(M=r+\ell a\), \(\ell\ge0\). Because \(a=mc\), the minimum over coin representations with fixed \(M\) equals \(a[w(r)+\ell mh^3]+d(r+\ell a)\), which increases strictly with \(\ell\). Adding a positive number of \(a\)-coins cannot improve a minimum. Thus the least element in residue \(dr\) is \(aw(r)+dr\), proving the Apéry formula.

**3. The two maxima.** Write \(r=jc+v\) with \(0\le j<m\), \(0\le v<c\), and \(v=qb+u\). The equality \(c=hb+t\), \(1\le t<b\), shows that \(q=0,\ldots,h-1\) each give a full block \(0\le u<b\), while \(q=h\) gives \(0\le u<t\). The quantity \(h^2q+hu\) increases within each block. Its full-block endpoints increase with \(q\) and its largest full-block endpoint is at \(v=hb-1\), with value \(2h^2(h-1)\). The final partial-block endpoint \(v=c-1\) has exactly the same value; all other \(v\) have strictly smaller value. Consequently \(w(r)\) has exactly two global maxima on \([0,a-1]\), at
\[
 r_1=(m-1)c+hb-1,\qquad r_2=a-1,
\]
where both weights equal \(T\). Since \(d>0\) and \(r_2>r_1\), the unique largest Apéry element is \(aT+d(a-1)\). Subtracting \(a\) yields the asserted \(F(S)\).

**4. Genus.** The standard Apéry identity is
\[
 g(S)=\frac1a\sum_{r=0}^{a-1}(aw(r)+dr)-\frac{a-1}{2}
 =\sum_{r=0}^{a-1}w(r)+\frac{(d-1)(a-1)}2.
\]
The sum of the weights over the first \(c\) arguments can be evaluated blockwise:
\[
 \sum_{v=0}^{c-1}w(v)
 =\sum_{q=0}^{h-1}\sum_{u=0}^{b-1}(h^2q+hu)
 +\sum_{u=0}^{t-1}(h^3+hu)
 =\frac{h^2(h-1)(2h^3+h^2-3h+2)}2.
\]
As \(w(jc+v)=jh^3+w(v)\), summing over \(0\le j<m\) proves the genus formula. The displayed fraction is an integer under the hypotheses, since either \(a-1\) or \(d-1\) is even.

**5. All pseudo-Frobenius numbers.** Write \(W_{dr}=aw(r)+dr\). An Apéry element is maximal in the semigroup order precisely when adding none of the non-\(a\) generators yields another Apéry element. Indeed, once a generator step leaves the Apéry set, any further nonnegative generator sum also remains outside it. If \(r<(m-1)c\), the \(c\)-generator takes \(W_{dr}\) to \(W_{d(r+c)}\), so such \(r\) is not maximal. Now let \(r=(m-1)c+v\). If \(v<c-b\), addition of the \(b\)-generator takes \(W_{dr}\) to \(W_{d(r+b)}\), by the greedy formula. Thus a maximal element requires \(v\ge c-b\).

For \(c-b\le v<c-1\), addition of the unit-offset generator remains below \(a\) and is an Apéry step exactly when \(v\not\equiv b-1\pmod b\); at a block endpoint, the greedy weight jump is strictly less than \(h\). In the range \(c-b\le v<c-1\), the unique block endpoint is \(v=hb-1\). Addition of the \(b\)-generator already wraps modulo \(a\) in this range and does not preserve Apéry minimality: for \(u=v+b-c\in[0,b)\), its distance above the least semigroup element of residue \(du\) is \(a[w(r)+h^2-w(u)+d]\ge a\), since \(w(r)\ge h u=w(u)\). The \(c\)-generator also wraps, with positive distance \(a[mh^3+d]\). At \(v=c-1\), all three additions wrap modulo \(a\), and the corresponding differences above their Apéry representatives are at least \(a\) by the same formulas (for the unit offset the difference is \(a[T+h+d]\)). Therefore the only maximal Apéry elements are those indexed by \(r_1\) and \(r_2\). Subtracting \(a\) and using \(r_2-r_1=c-hb=t\) proves \(\operatorname{PF}(S)=\{F(S)-dt,F(S)\}\), and the type is two.

## Verification

The standalone standard-library Python program `checker.py` independently computes weighted coin-change optima by dynamic programming and all Apéry residue minima by Dijkstra's algorithm. It compares those independent values with the proposed formulas and extracts pseudo-Frobenius numbers directly from the computed residue minima. The recorded execution passed 6,342 weighted change-making comparisons, 271,591 residue comparisons, and 242 complete parameter-family checks with \(3\le h\le10\), \(1\le m\le6\) and several coprime \(d\) values; it additionally includes the known \(h=2\) boundary as a regression check. The finite checks are not a proof for unrestricted parameters. The symbolic proof above supplies that step.

## Relationship to prior work

Liu, Xin, Ye and Yin's June 2023 generalized-Mersenne study [1] handles the binary coefficient pattern and explicitly highlights the difficulty of the higher-base pattern with offsets \(h^i-h+1\): the greedy-weight monotonicity used in the binary case fails in general. The present theorem handles the natural cubic truncation \(k=3\) for every \(h\ge3\) when the first generator is a multiple of \(h^3-h+1\), giving all Apéry elements, not only the largest one. Their companion generalized-repunit paper [2] uses offsets \((h^i-1)/(h-1)\), which differ already at \(i=2\) for \(h\ge3\). Their uniform-coefficient paper [3] assigns the same coefficient of \(a\) to each nontrivial generator, unlike the powers here. Classical Apéry-genus and maximal-Apéry principles are used as established tools. This work does not assert novelty for the binary case or for general algorithms to compute these invariants.

## Limitations

The result treats only a particular cubic truncation and the divisible first-generator subfamily; it does not solve the unrestricted higher-base problem or longer sequences. Existing general algorithms and unrelated numerical-semigroup classification theorems may imply parts of the result after specialization. The originality assessment is limited to identifiable and inspected literature; a previously published implicit equivalent remains possible. No independent validation has been performed.

## References

[1] F. Liu, G. Xin, S. Ye, J. Yin, *A Generalization of Mersenne and Thabit Numerical Semigroups*, arXiv:2306.03459, first posted 2023-06-06, especially Section 6. https://arxiv.org/abs/2306.03459

[2] F. Liu, G. Xin, S. Ye, J. Yin, *A Note on Generalized Repunit Numerical Semigroups*, arXiv:2306.10738, first posted 2023-06-19. https://arxiv.org/abs/2306.10738

[3] F. Liu, G. Xin, S. Ye, J. Yin, *The Frobenius Formula for A=(a,ha+d,ha+b₂d,...)*, arXiv:2304.09039, first posted 2023-04-18. https://arxiv.org/abs/2304.09039

[4] M. B. Branco, I. Colaço, I. Ojeda, *The Frobenius Problem for Generalized Repunit Numerical Semigroups*, Mediterranean Journal of Mathematics 20 (2023), article 16, published online 2022-12-03, DOI 10.1007/s00009-022-02233-w. https://doi.org/10.1007/s00009-022-02233-w
