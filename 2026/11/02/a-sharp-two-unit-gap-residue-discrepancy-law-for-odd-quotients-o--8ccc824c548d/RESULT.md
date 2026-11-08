# A sharp two-unit gap-residue discrepancy law for odd quotients of consecutive coin semigroups

## Finding

For an odd integer \(p\ge3\) and an integer \(t\ge1\), let \(a=pt+1\) and
\[
Q_{p,t}=\{x\in\mathbb N_0:px\in\langle a,a+1\rangle\}.
\]
Put \(h=(p-1)/2\), \(E=\lfloor h/2\rfloor+1\), and \(O=\lceil h/2\rceil\). Write \([z]_p\in\{0,\ldots,p-1\}\) for the least residue and choose \(u\) with \(2u\equiv1\pmod p\). If \(C_j\) is the number of positive gaps of \(Q_{p,t}\) congruent to \(j\pmod p\), then for every \(0\le j<p\),
\[
\boxed{C_j=\frac{t(t-1)}2+\left\lfloor\frac{tE}{p}\right\rfloor+\left\lfloor\frac{tO}{p}\right\rfloor
+\mathbf1_{[u(j-1)]_p<[tE]_p}+\mathbf1_{[u(j-1-t)]_p<[tO]_p}.}
\]
Consequently, \(\max_j C_j-\min_j C_j\le2\). The difference equals two for \(t=2\) and every odd \(p\ge5\), while for \(p=3\) it never exceeds one. The genus is \(g(Q_{p,t})=t(pt+1)/2\).

## Assumptions and scope

The odd integer \(p\) need not be prime; there is no coprimality restriction between \(p\) and \(t\). Gaps are nonnegative integers outside the semigroup, so zero is not a gap. Each gap is counted once. The result concerns only the indicated consecutive-generator quotient and residues modulo its odd quotient parameter, not arbitrary semigroup quotients or even moduli.

## Proof

**1. Unique gap parameters.** Every nonnegative integer \(n\) has a unique decomposition \(n=ak+y\), with \(0\le y<a\). Since \(a+1\) and \(a\) are consecutive, \(n\in\langle a,a+1\rangle\) if and only if \(y\le k\): if \(y\le k\), write \(n=(k-y)a+y(a+1)\); conversely, any nonnegative generating expression reduces modulo \(a\) to a residue whose least representative cannot exceed the quotient \(k\). For a gap \(x\) of \(Q_{p,t}\), write \(px=ak+y\), where \(y>k\). Divisibility by \(p\), together with \(a=pt+1\), forces \(k+y\equiv0\pmod p\). Thus uniquely write
\[
k=pq+r,\quad 0\le r<p,\qquad y=p(t-s)-r
\]
with \(q,s\ge0\). The inequality \(y>k\) is equivalent to \(p(t-q-s)>2r\), which gives \(q+s\le t-1\) for \(0\le r\le h\), and \(q+s\le t-2\) for \(h<r<p\). These conditions also ensure \(0<y<a\). The gap itself is
\[
x=t(pq+r)+q+t-s.
\]
This is a bijective parameterization of all positive gaps.

**2. Uniform interior.** First count \(q,s\ge0\) with \(q+s\le t-2\), allowing every \(r\in\{0,\ldots,p-1\}\). Their residues are \(tr+t+q-s\pmod p\). Put \(d=\gcd(p,t)\), necessarily odd. The full square \(0\le q,s<t\) has exactly \(t^2/d\) points with each prescribed \(q-s\pmod d\). On the diagonal \(q+s=t-1\), differences \(q-s=2q-(t-1)\) occupy each class modulo \(d\) exactly \(t/d\) times because \(d\mid t\) and \(2\) is invertible modulo \(d\). The reflection \((q,s)\mapsto(t-1-s,t-1-q)\) preserves \(q-s\) and swaps the two triangles on either side of the diagonal. Each class therefore has exactly \(t(t-1)/(2d)\) interior pairs. As \(r\) ranges over all \(p\) values, the residues \(tr\pmod p\) cover every multiple of \(d\) exactly \(d\) times. Consequently each residue class of the gaps receives precisely \(t(t-1)/2\) interior contributions.

**3. Boundary intervals.** On the boundary \(q+s=t-1\), only \(0\le r\le h\) occur. The gap residue is \(tr+2q+1\pmod p\). Even \(r=2i\), for \(0\le i<E\), give \(2(ti+q)+1\), with \(0\le q<t\); every integer \(z=ti+q\) in \([0,tE)\) occurs once. Odd \(r=2i+1\), for \(0\le i<O\), similarly give \(2z+t+1\) for \(z\in[0,tO)\). Since \(2\) is invertible modulo odd \(p\), the number of solutions \(0\le z<L\) to \(2z+b\equiv j\pmod p\) equals \(\lfloor L/p\rfloor+\mathbf1_{[u(j-b)]_p<[L]_p}\). Adding the two boundary contributions to the common interior contribution proves the boxed histogram formula and the discrepancy bound two.

**4. Sharpness for \(p\ge5\).** Set \(t=2\). Both boundary interval lengths \(2E,2O\) are strictly smaller than \(p\). The two boundary supports are the residues \(2z+1\) for \(0\le z<2E\) and \(2z+3\) for \(0\le z<2O\). Their intersection contains residue \(3\); their union has exactly \(h+2<p\) residues. Indeed, when \(h\) is even, the second support is contained in the first; when \(h\) is odd, it extends the first by precisely one residue. Therefore one class receives two boundary counts while another receives none. The common interior count does not affect the difference, proving discrepancy exactly two.

**5. The exceptional modulus \(p=3\).** Here \(h=1\) and, importantly, **\(E=O=1\)**: there are two boundary indicators, not one. If \(t\equiv0\pmod3\), both remainder intervals have length divisible by three and both indicators vanish. If \(t\equiv1\pmod3\), each remainder interval has length one, and the two indicators select different classes \(j\equiv1\) and \(j\equiv2\pmod3\). If \(t\equiv2\pmod3\), each remainder interval has length two; their missing classes are different (respectively \(j\equiv2\) and \(j\equiv1\pmod3\)). Thus in every case the sum of the two indicators differs by at most one between any two classes. This proves the sharper bound one for \(p=3\), without the incorrect assertion that \(O=0\).

**6. Genus.** There are \(p\binom t2=pt(t-1)/2\) interior gaps and \(t(E+O)=t(h+1)=t(p+1)/2\) boundary gaps, giving \(g(Q_{p,t})=(pt^2+t)/2\).

## Verification

The accompanying `verify.py` enumerates quotient membership independently of the gap-parameter proof and checks residue histograms, genus and sharpness on a finite grid of odd \(p\) and positive \(t\). Independently checked cases include composite odd moduli. These computations corroborate only their finite ranges; the arguments above prove the all-parameter statement.

## Relation to prior work and limitations

Shor (2022; arXiv:2101.01760) characterizes exact equidistribution of semigroup gaps, particularly for arithmetic Apéry configurations. Cabanillas (2019; arXiv:1904.08240) develops algorithms for genus, type, Frobenius number and generators of two-generated semigroup quotients. Liu (2023; arXiv:2312.10889) supplies generating functions and generator descriptions of quotient semigroups. Those known general tools provide context and may furnish alternate derivations; the present claim is the explicit every-residue histogram and its sharp discrepancy for this constrained family, not the known genus formula or an assertion of new quotient-semigroup theory. Earlier equivalent specializations remain a historical-priority risk.

No conclusion is asserted for even quotient parameters, nonconsecutive original generators, or unrelated residue moduli. The finite verifier is not a proof for infinitely many parameters, and bibliographic comparison does not guarantee exhaustive priority.

## References

1. C. M. Shor, *Equidistribution of numerical semigroup gaps modulo m*, arXiv:2101.01760, 2021; Discrete Mathematics 345 (2022), 112995. https://arxiv.org/abs/2101.01760
2. E. Cabanillas, *Quotients of numerical semigroups generated by two numbers*, arXiv:1904.08240, 2019. https://arxiv.org/abs/1904.08240
3. F. Liu, *Generating functions for the quotients of numerical semigroups*, arXiv:2312.10889, 2023. https://arxiv.org/abs/2312.10889
