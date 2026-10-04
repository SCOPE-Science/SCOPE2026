# A uniform three-quarter abundance bound for weird numbers of form \(2^k p q\)
## Finding
Let \(k\ge 1\), let \(p<q\) be odd primes, and suppose \(n=2^k p q\) is weird. Define
\[
M=2^{k+1}-1,\qquad a=\sigma(n)-2n.
\]
Then
\[
M<a<\frac{3}{4}M^2+M.
\]
Equivalently, writing \(x=p-M\) and \(y=q-M\), one has \(xy>M^2/4\).

The established literature gives \(M<a<M(M+1)\) and conjectures the sharper upper bound \(a<(M+1)(M+2)/3\). The bound above is a uniform improvement of the proved upper bound; it does not prove the conjectured one-third-scale constant.

## Assumptions and scope
A positive integer is weird if it is abundant but is not a sum of distinct proper divisors. The claim concerns only weird integers with exactly the factorization \(n=2^k p q\), where \(k\ge1\) and \(p<q\) are odd primes. Such weird numbers are automatically primitive in this factorization class.

For this family, set \(M=2^{k+1}-1\) and let \(a=\sigma(n)-2n\) be the abundance. Iannucci proves the necessary relations
\[
a>M,\qquad M<p<2M,
\]
and
\[
(p-M)(q-M)=M(M+1)-a.
\]
He also proves that weirdness is equivalent, under these conditions, to the absence of positive integers \(r,s,t\le M\) satisfying
\[
pq=r+sp+tq.
\]

## Proof
Put
\[
x=p-M,\qquad y=q-M.
\]
Then \(x\) and \(y\) are positive even integers, \(x<y\), and
\[
a=M(M+1)-xy.
\]
We prove \(xy>M^2/4\).

First rewrite Iannucci's forbidden representation. Put \(u=M-s\) and \(v=M-t\). Then \(0\le u,v\le M-1\), and using
\[
pq=M+Mp+Mq-a,
\]
the equality \(pq=r+sp+tq\) is equivalent to
\[
r=M-a+up+vq.
\]
Thus weirdness implies that there are no \(u,v\in\{0,1,\ldots,M-1\}\) for which
\[
a-M+1\le up+vq\le a. \tag{1}
\]

Assume first that \(q\le a\), and put \(h=\lfloor a/q\rfloor\). For each \(v=0,1,\ldots,h\), let
\[
b_v=a-vq\ge0.
\]
Because \(a<M(M+1)\) and \(p\ge M+2\), one has \(a<Mp\), so \(u_v=\lfloor b_v/p\rfloor\) lies in \(\{0,\ldots,M-1\}\). If the residue \(b_v-u_vp\) were at most \(M-1\), then
\[
u_vp+vq=a-(b_v-u_vp)
\]
would satisfy (1), a contradiction. Hence every residue
\[
(a-vq)\bmod p
\]
lies in \(\{M,M+1,\ldots,p-1\}\), a set of exactly \(p-M=x\) residue classes.

These residues are distinct for \(0\le v\le h\). Indeed, \(q\not\equiv0\pmod p\), while
\[
h\le \frac{a}{q}<M<p,
\]
so two such indices cannot differ by a positive multiple of \(p\). Therefore
\[
h+1\le x.
\]
Since \(a<(h+1)q\), it follows that
\[
a<xq=x(M+y)=xM+xy.
\]
Combining this with \(a=M(M+1)-xy\) gives
\[
2xy>M(M+1-x). \tag{2}
\]
If \(x<M/2\), then (2) yields
\[
xy>\frac{M}{2}\left(M+1-\frac{M}{2}\right)>\frac{M^2}{4}.
\]
If \(x\ge M/2\), then \(y>x\), so
\[
xy>x^2\ge\frac{M^2}{4}.
\]
Thus \(xy>M^2/4\) whenever \(q\le a\).

Now assume \(q>a\). Since \(q=M+y\) and \(a=M(M+1)-xy\), the inequality \(q>a\) gives
\[
y(x+1)>M^2.
\]
Because \(x\) is a positive even integer, \(x\ge2\), and therefore
\[
xy=y(x+1)\frac{x}{x+1}>M^2\frac{x}{x+1}\ge\frac{2M^2}{3}>\frac{M^2}{4}.
\]
This completes both cases. Finally,
\[
a=M(M+1)-xy<M(M+1)-\frac{M^2}{4}=\frac{3}{4}M^2+M.
\]

## Verification
A standalone exact-integer checker re-enumerates every candidate prime pair for \(1\le k\le8\) using Iannucci's necessary-and-sufficient criterion in the equivalent interval form (1). It reproduces the published counts
\[
1,1,5,3,10,23,29,53
\]
and checks the new inequality for every enumerated weird pair. The replay reports `VERIFY_OK` after checking 29,490 candidate prime pairs.

This finite replay is corroborative only. The theorem is proved by the argument above for all \(k\ge1\); the computation is not used to pass from a finite range to the infinite statement.

## Relationship to prior work
Iannucci derives the identity \((p-M)(q-M)=M(M+1)-a\), proves \(M<a<M(M+1)\), gives the exact forbidden-representation criterion used here, and conjectures
\[
a<\frac{(M+1)(M+2)}{3}.
\]
The present argument uses the same exact criterion but adds a residue-packing step: for \(q\le a\), the residues \((a-vq)\bmod p\) must occupy the short terminal interval of length \(p-M\). This forces a quantitative lower bound on \((p-M)(q-M)\) and hence the stated three-quarter upper bound for abundance.

Melfi gives a substantial sufficient family of primitive weird numbers \(2^k p q\) and studies conditional infinitude. That construction controls primes near a specified scale but does not state a universal abundance upper bound for all weird numbers in the family. The 2016 extension by Amato, Hasler, Melfi, and Parton develops sufficient constructions with more prime factors; it likewise does not supply the bound claimed here.

## Limitations
The coefficient \(3/4\) is not asserted to be optimal. In particular, the proof does not establish Iannucci's conjectured coefficient asymptotic to \(1/3\). It also does not address weird numbers outside the factorization \(2^k p q\), nor does it prove existence or infinitude of such numbers for new values of \(k\).

Focused literature and database searches found no equivalent three-quarter bound. A differently phrased unpublished or hard-to-index argument could still exist; this is the principal residual originality risk.

## References
1. D. E. Iannucci, “On primitive weird numbers of the form \(2^k p q\),” arXiv:1504.02761v1, first posted 7 April 2015.
2. G. Melfi, “On the conditional infiniteness of primitive weird numbers,” Journal of Number Theory 147 (2015), 508–514, DOI 10.1016/j.jnt.2014.07.024; available online 16 September 2014.
3. G. Amato, M. F. Hasler, G. Melfi, and M. Parton, “Primitive weird numbers having more than three distinct prime factors,” Rivista di Matematica della Università di Parma 7(1) (2016), 153–163.
