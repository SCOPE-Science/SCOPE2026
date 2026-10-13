# A second linear phase for generalized Frobenius numbers of arithmetic triples

## Finding
For an odd integer \(a=2h+1\ge3\), an integer \(d\) with \(1\le d\le h\) and \(\gcd(a,d)=1\), and any integer \(p\) in the interval \(h+1\le p\le a+d\), let \(D_{a,d}(N)\) count the ordered triples \((x,y,z)\in\mathbb Z_{\ge0}^3\) satisfying
\[
 ax+(a+d)y+(a+2d)z=N.
\]
Then the greatest nonnegative integer having at most \(p\) representations is
\[
\boxed{g_p(a,a+d,a+2d)=a(a+d+p-h-2)+d(a-1).}
\]
The boundary integer \(G\) on the right has **exactly** \(p\) representations. Every integer \(N>G\) has at least \(p+1\) representations. Thus the stated interval supplies a second, slope-\(a\) linear phase beyond the published range \(0\le p\le h\).

For example, with \(a=11\), \(d=2\), and \(6\le p\le13\), the exact answer is \(g_p(11,13,15)=11p+86\). The bound \(d\le h\) matters: for \((a,d,p)=(5,3,8)\), the displayed expression would give \(72\), but the actual value is \(74\).

## Assumptions and scope
The coefficients \(a\), \(a+d\), \(a+2d\) are fixed positive integers with \(a\) odd, \(a\ge3\), \(\gcd(a,d)=1\), and \(1\le d\le(a-1)/2\). Representations distinguish coefficient triples; there is no upper bound on any coefficient. The integer \(p\) is the representation threshold, not a prime. All quantifiers in the finding are unrestricted within these ranges.

## Proof
**1. Exact representation count.** Write \(t=x+y+z\) and \(s=y+2z\). The representation equation is \(N=at+ds\). At fixed nonnegative \(s,t\), the possible values of \(z\) are exactly
\[
\max(0,s-t)\le z\le\lfloor s/2\rfloor,
\]
so their number is
\[
R(s,t)=\max\left(0,\lfloor s/2\rfloor-\max(0,s-t)+1\right).
\]
For any \(N\), let \(s_0\in[0,a-1]\cap\mathbb Z\) be the unique residue with \(ds_0\equiv N\pmod a\), and set \(m=(N-ds_0)/a\). As every allowed \(s\) equals \(s_0+ka\) for an integer \(k\ge0\), there is the finite identity
\[
D_{a,d}(N)=\sum_{k\ge0}R(s_0+ka,m-dk),
\]
where a term with negative \(m-dk\) is understood to vanish. This is an identity for every integer \(N\), not an asymptotic approximation.

**2. The proposed last exceptional integer.** Set
\[
u=a+d+p-h-2,\qquad G=au+d(a-1).
\]
Since \(s_0=a-1=2h\), the \(k=0\) contribution at \(G\) equals \(h+1\). At \(k=1\), the arguments are \(s=4h+1\) and \(t=h+p-1\). The bounds \(h+1\le p\le a+d\), \(d\le h\) give the contribution \(p-h-1\). At \(k=2\), one has \(s=6h+2\) and \(t=h+p-d-1\le3h\), so there is no contribution, nor from larger \(k\). Consequently
\[
D_{a,d}(G)=(h+1)+(p-h-1)=p.
\]

**3. The next complete residue window.** Each of the integers \(G+1,\ldots,G+a-1\) is uniquely expressible as \(G+aj-dv\) with \(1\le v\le a-1\) and \(j=\lceil dv/a\rceil\). The coprimality hypothesis makes \(1\le aj-dv\le a-1\); also \(1\le j\le d\). For such \(v,j\), choose \(s_0=a-1-v\) and \(m=u+j\) in the preceding counting formula. The contribution with \(k=0\) is
\[
R_0=h+1-\lceil v/2\rceil.
\]
For \(k=1\), put \(s_1=4h+1-v\) and \(t_1=h+p-1+j\). Define \(\delta=\max(0,t_1-s_1)=\max(0,p+j+v-3h-2)\). The exact count is
\[
R_1=p-h-1+j+\lceil v/2\rceil-\delta,
\]
where the nonnegative first terms account for the lower endpoint and \(\delta\) is precisely the possible saturation correction. Thus
\[
R_0+R_1=p+j-\delta.
\]
If \(\delta=0\), this is already at least \(p+1\).

Suppose \(\delta>0\). At \(k=2\), \(s_2=6h+2-v\ge4h+2\) whereas
\[
t_2=h+p-d-1+j\le3h+d\le4h,
\]
so there is no upper-end saturation. The contribution is exactly
\[
R_2=\max\left(0,\,p-(a+d)+j+\lfloor v/2\rfloor\right).
\]
Since \(d\le h\), for \(T=a-v\) one has \(dT/a<T/2\). It follows that
\[
d-j=\lfloor d(a-v)/a\rfloor
\le\lfloor(a-v-1)/2\rfloor
=h-\lceil v/2\rceil.
\]
The unsaturated expression inside the maximum for \(R_2\), minus \(\delta-j+1\), is therefore
\[
\bigl(p-(a+d)+j+\lfloor v/2\rfloor\bigr)
-(\delta-j+1)=h-d+j-\lceil v/2\rceil\ge0.
\]
Whether \(\delta-j+1\) is positive or not, \(R_2\ge\delta-j+1\). Hence
\[
D_{a,d}(G+aj-dv)\ge R_0+R_1+R_2\ge p+1.
\]
The remaining successor is \(G+a\), and injecting every representation of \(G\) by increasing \(x\) by one already gives \(p\) representations; in fact the exact counting formula at \(s_0=a-1\), \(m=u+1\) increases the \(k=1\) contribution from \(p-h-1\) to \(p-h\), while the \(k=0\) contribution stays \(h+1\). Thus \(D_{a,d}(G+a)\ge p+1\).

**4. All larger integers.** Adding one coin of denomination \(a\) injects the representations of \(N\) into those of \(N+a\), so \(D_{a,d}(N+a)\ge D_{a,d}(N)\). Every integer larger than \(G\) is obtained from one of \(G+1,\ldots,G+a\) by adding a nonnegative multiple of \(a\). Hence every such integer has more than \(p\) representations, while \(G\) has exactly \(p\). This proves the formula for \(g_p\).

## Verification
The accompanying standalone Python program `verify.py` computes denumerants in two mathematically different ways: by the finite residue-lattice formula above and, for small parameters, by three-coin dynamic programming. It checked all \(30{,}750\) admissible triples \((a,d,p)\) with odd \(3\le a\le83\), all \(1{,}940{,}622\) successor inequalities, and \(291{,}790\) cross-method comparisons. It also checked the out-of-domain example \((a,d,p)=(5,3,8)\). These are finite diagnostics, not proof of the unrestricted theorem; the preceding exact argument proves the general statement. Run `python verify.py` with Python 3.8 or newer.

## Relationship to prior work
Komatsu and Ying, *The \(p\)-numerical semigroup of the triple of arithmetic progressions* (first publicly posted 27 June 2022; subsequently *Symmetry* **15** (2023), 1328), consider exactly the generator triple \(\{a,a+d,a+2d\}\). Their Theorem 1 proves
\[
g_p=(a+2d)p+\lfloor(a-2)/2\rfloor a+(a-1)d
\quad (0\le p\le\lfloor a/2\rfloor).
\]
The first phase has slope \(a+2d\). The new theorem establishes a **different** phase for \(h+1\le p\le a+d\) under the explicit conditions \(a=2h+1\) and \(d\le h\), with slope \(a\); it is not a special case of the previously proved formula. The source itself notes that the pattern becomes more complicated after the first phase. Subsequent work on Pell triples and longer blocks of consecutive odd generators concerns different generating sets and does not establish this fixed-three-generator formula. No priority or independent verification beyond the reviewed sources is asserted.

## Limitations
The formula is not claimed for even \(a\), for \(d>h\), or for \(p>a+d\). The example \((5,3,8)\) shows that deleting the restriction on \(d\) can break the stated formula. The proof gives the maximal exceptional integer, not the entire \(p\)-Apéry set or the generalized genus. The literature comparison cannot exclude unindexed equivalent results; independent audit has not been performed.

## References
1. T. Komatsu and H. Ying, *The \(p\)-numerical semigroup of the triple of arithmetic progressions*, arXiv:2206.13052, first posted 2022-06-27; *Symmetry* **15** (2023), article 1328, DOI: 10.3390/sym15071328. Full preprint: https://arxiv.org/pdf/2206.13052.
2. T. Komatsu and J. Mu, *\(p\)-Numerical semigroups of Pell triples*, *Journal of the Ramanujan Mathematical Society* **40** (2025), 5–22. Different generating family.
3. T. Komatsu, S. Hyun, and K. Song, *\(p\)-numerical semigroup of the sequence of consecutive odd integers*, arXiv:2608.14053 (2026). Different variable-length generating families.
