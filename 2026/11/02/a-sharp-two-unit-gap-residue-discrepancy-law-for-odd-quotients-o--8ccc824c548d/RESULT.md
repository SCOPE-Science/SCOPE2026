# A sharp two-unit gap-residue discrepancy law for odd quotients of consecutive coin semigroups

## Finding
For every odd integer \(p\ge3\) and integer \(t\ge1\), define \(a=pt+1\) and the numerical semigroup
\[Q_{p,t}=\{x\in\mathbb N_0:px\in\langle a,a+1\rangle\}.\]
Write \(h=(p-1)/2\), \(E=\lfloor h/2\rfloor+1\), and \(O=\lceil h/2\rceil\). Define \([z]_p\in\{0,\ldots,p-1\}\) as the least nonnegative residue and \(u\in\mathbb Z\) by \(2u\equiv1\pmod p\). For each \(0\le j<p\), let \(C_j\) be the number of positive gaps of \(Q_{p,t}\) congruent to \(j\pmod p\). Then
\[
C_j=\frac{t(t-1)}2+\left\lfloor\frac{tE}{p}\right\rfloor+\left\lfloor\frac{tO}{p}\right\rfloor+\mathbf1_{[u(j-1)]_p<[tE]_p}+\mathbf1_{[u(j-1-t)]_p<[tO]_p}.
\]
In particular, \(\max_{0\le j<p} C_j-\min_{0\le j<p} C_j\le2\). This is sharp simultaneously for every odd \(p\ge5\) at \(t=2\), while for \(p=3\) the difference never exceeds one. The genus is \(g(Q_{p,t})=t(pt+1)/2\).

## Assumptions and scope
The odd modulus \(p\) is **not required to be prime**; \(t\) is any positive integer. The semigroup quotient is defined by membership \(px\in\langle pt+1,pt+2\rangle\). Gap means a nonnegative integer excluded from this semigroup; hence zero is never a gap. The formula counts each distinct gap exactly once, without asymptotics or coprimality assumptions on \(p\) and \(t\).

## Proof
**Exact parameterization.** Every nonnegative integer \(n\) has a unique expression \(n=ak+y\) with \(0\le y<a\). One has \(n\in\langle a,a+1\rangle\) if and only if \(y\le k\): the forward implication follows by reducing the number of copies of \(a+1\) modulo \(a\); the reverse direction is \(n=(k-y)a+y(a+1)\). Thus \(x\notin Q_{p,t}\) if and only if \(px=ak+y\) with \(y>k\). Since \(a=pt+1\), divisibility by \(p\) gives \(k+y\equiv0\pmod p\). We may therefore uniquely write \(k=pq+r\), \(0\le r<p\), and \(y=pt-ps-r\). Both \(q,s\) are nonnegative integers. The inequality \(y>k\) becomes \(p(t-q-s)>2r\). Accordingly, for \(0\le r\le h\) it is exactly \(q+s\le t-1\), whereas for \(h<r<p\) it is \(q+s\le t-2\). The corresponding gap is
\[x=t(pq+r)+q+t-s.\]
These conditions ensure \(0<y<a\) and give a bijection with all gaps.

**Uniform interior contribution.** Separate the parameter triples with \(q+s\le t-2\) and \(q+s=t-1\). The interior has all \(p\) values of \(r\) available. Its gap residue is \(tr+t+q-s\pmod p\). Let \(d=\gcd(p,t)\), which is odd. For each residue modulo \(d\), the number of pairs \((q,s)\) satisfying \(q,s\ge0\), \(q+s\le t-2\), and a prescribed residue of \(q-s\pmod d\) is exactly \(t(t-1)/(2d)\). To see this, start with the \(t\)-by-\(t\) square of pairs, where all differences are equally distributed modulo \(d\). The middle diagonal \(q+s=t-1\) is also equidistributed since \(d\mid t\) and \(2\) is invertible modulo \(d\). Reflection \((q,s)\mapsto(t-1-s,t-1-q)\) preserves \(q-s\) and bijects the two remaining triangles. Each triangle therefore contains \((t^2/d-t/d)/2\) pairs per residue. As \(r\) ranges over \(0,\ldots,p-1\), its multiples \(tr\pmod p\) run through the residues divisible by \(d\) exactly \(d\) times each. Thus every class modulo \(p\) receives exactly \(t(t-1)/2\) interior gaps.

**Two boundary intervals.** On \(q+s=t-1\) only \(0\le r\le h\) are allowed, and the gap residue reduces to \(tr+2q+1\pmod p\). Split into even indices \(r=2i\) and odd indices \(r=2i+1\). There are exactly \(E\) even choices and \(O\) odd choices. For the even choices, the integers \(ti+q\), with \(0\le i<E\) and \(0\le q<t\), run through the complete interval \(0,1,\ldots,tE-1\) exactly once. The associated residues are \(2z+1\pmod p\). Similarly the odd indices give \(z=0,\ldots,tO-1\) with associated residues \(2z+t+1\pmod p\). Since \(2\) is invertible modulo the odd number \(p\), any interval \(0,\ldots,L-1\) has \(\lfloor L/p\rfloor\) representatives of each prescribed residue, plus one more precisely when that residue is less than \([L]_p\). Adding the two intervals to the interior contribution yields the asserted formula and establishes discrepancy at most two.

**Sharpness and genus.** For \(t=2\), the two boundary-interval lengths are \(2E\) and \(2O\), both smaller than \(p\) when \(p\ge5\). The first interval has residues \(2z+1\) for \(0\le z<2E\); the second has residues \(2z+3\) for \(0\le z<2O\). They overlap (at least at residue \(3\)), but their union has only \(h+2<p\) residues. Therefore one residue receives two extra boundary gaps and another receives zero, proving sharpness. For \(p=3\), \(O=0\), so there is only one indicator and discrepancy at most one. Finally, summing the interior and boundary counts gives \(pt(t-1)/2+t(E+O)=(pt^2+t)/2\), because \(E+O=h+1=(p+1)/2\).

## Verification
The self-contained verifier `verify.py` independently enumerates quotient membership from the ordinary two-generator criterion and checks every residue histogram against the exact closed formula. It checks every odd \(p\) from \(3\) to \(79\) and every \(t\) from \(1\) to \(34\), altogether \(1326\) instances. It also verifies the universal discrepancy bound and witnesses sharpness at \(t=2\). Run with `python3 verify.py` from the extracted package directory. This finite test supplements, rather than proves, the universally quantified theorem.

## Relationship to prior work
Shor's 2021 preprint, later published in 2022, studies exact equidistribution of numerical-semigroup gaps, especially when a nonzero Apéry set forms an arithmetic progression. The present quotient family for general \(t\) is distinct from the characterized arithmetic-Apéry family; the claim here is a quantitative all-residue histogram with uniform discrepancy, not merely an equidistribution yes/no condition. Cabanillas' 2019 work computes standard invariants of arbitrary quotients of two-generated numerical semigroups (including genus, Frobenius number, type, and generators), but its examined theorems do not state this sharp residue-by-residue estimate. Liu's 2023 preprint, subsequently published in 2024, develops representation-generating functions for quotient semigroups and generator descriptions, not this residue-discrepancy theorem. The exact genus of the present family is not claimed independently novel. The existing general membership and generating-function methods could potentially derive this formula, but no earlier equivalent or stronger statement was identified in the materially inspected portions and searches.

## Limitations
No assertion is made for even \(p\), for quotients of nonconsecutive two-generated numerical semigroups, or for arbitrary residue moduli unrelated to the quotient parameter. The result is a new explicit family consequence and does not assert a universal discrepancy bound for all numerical semigroups. Independent external mathematical audit and exhaustive bibliographic verification are not performed.

## References
1. Caleb M. Shor, *Equidistribution of numerical semigroup gaps modulo m*, arXiv:2101.01760 (first posted 2021-01-05), https://arxiv.org/abs/2101.01760.
2. Emmanuel Cabanillas, *Quotients of numerical semigroups generated by two numbers*, arXiv:1904.08240 (2019-04-17), https://arxiv.org/abs/1904.08240.
3. Feihu Liu, *Generating functions for the quotients of numerical semigroups*, arXiv:2312.10889 (first posted 2023-12-18), https://arxiv.org/abs/2312.10889.
