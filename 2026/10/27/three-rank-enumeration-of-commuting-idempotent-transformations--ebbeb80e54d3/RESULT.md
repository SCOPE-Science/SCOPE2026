# Three-rank enumeration of commuting idempotent transformations

## Finding
For every integer \(n\ge0\), let \(T_n\) be the full transformation monoid of the labeled set \([n]\), and define \(N_{n;a,b,k}\) to be the number of **ordered** pairs \((e,f)\in T_n^2\) such that \(e^2=e\), \(f^2=f\), \(ef=fe\), and the three image sizes \(\lvert\operatorname{im}e\rvert\), \(\lvert\operatorname{im}f\rvert\), \(\lvert\operatorname{im}(ef)\rvert\) equal \(a,b,k\), respectively. Multiplication means function composition.

Define the formal trivariate-rank exponential generating function
\[
F(z;u,v,w)=\sum_{n\ge0}\frac{z^n}{n!}\sum_{a,b,k\ge0}N_{n;a,b,k}u^av^bw^k.
\]
Its exact value is
\[
\boxed{F(z;u,v,w)=\exp\!\left(wzu v\sum_{p,q\ge0}
  \frac{(uz)^p(vz)^q}{p!q!}\exp\bigl((p+1)(q+1)z\bigr)\right).}
\]
All series are formal in \(z\), so each coefficient involves finitely many terms. Moreover, for \(n\ge1\), the support is **exactly**
\[
\boxed{N_{n;a,b,k}>0\quad\Longleftrightarrow\quad
1\le k\le\min(a,b),\qquad a+b-k\le n.}
\]
At \(n=0\), the unique empty map pair contributes \(N_{0;0,0,0}=1\). Setting \(u=v=w=1\) gives the exact total sequence for \(n=1,\ldots,8\):
\[
1,\ 7,\ 58,\ 601,\ 7616,\ 113989,\ 1963060,\ 38178193.
\]
The formula is a complete joint distribution of the two generator ranks and their meet rank, not only a count of commuting pairs.

## Assumptions and scope
A transformation is an arbitrary function from the finite labeled set to itself, without order-preservation, injectivity, or linearity hypotheses. An idempotent transformation is a retraction to its image. The result counts ordered pairs, including \(e=f\); it is not an orbit count up to relabeling. All ranks mean image cardinalities, not matrix ranks. The variables \(u,v,w\) are formal markers, while \(z\) counts labeled points.

## Proof
**Common retraction.** Since \(e\) and \(f\) commute and are idempotent, \(h=ef\) is idempotent, and
\[
\operatorname{im}h=\operatorname{im}e\cap\operatorname{im}f=:C.
\]
Indeed every output of \(h\) is fixed by both maps, and every point fixed by both is in the image of \(h\). For each \(c\in C\), the fiber \(B_c=h^{-1}(c)\) is preserved by both maps, because \(he=eh\) and \(hf=fh\), while \(e(c)=f(c)=c\). Thus the pair splits uniquely over these nonempty, disjoint fibers; each fiber has one marked common fixed point \(c\).

**A single fiber.** In a fiber \(B\) with common fixed point \(c\), put
\[
P=(\operatorname{im}e\cap B)\setminus\{c\},\qquad
Q=(\operatorname{im}f\cap B)\setminus\{c\},\qquad
R=B\setminus(\{c\}\cup P\cup Q).
\]
The sets \(P,Q,R\) are disjoint: a point in both images would belong to \(C\), hence must equal \(c\). For every \(x\in P\), we have \(e(x)=x\) and \(f(x)=h(x)=c\); for every \(y\in Q\), we have \(f(y)=y\) and \(e(y)=c\). For each \(z\in R\), the only restrictions are
\[
e(z)\in P\cup\{c\},\qquad f(z)\in Q\cup\{c\}.
\]
Conversely, after choosing \(P,Q,R\), every independent choice of these two images for each \(z\in R\), together with the preceding forced values, defines commuting idempotents. Indeed both composites are constantly \(c\) on \(B\), and both individual maps fix every point of their own images.

Write \(p=|P|\), \(q=|Q|\), \(r=|R|\). Then \(|B|=1+p+q+r\), and each such fiber has \((p+1)^r(q+1)^r\) independent image assignments after its points have been partitioned into \(P,Q,R\). Its contributions to the two ranks are \(p+1\) and \(q+1\), and its contribution to the composite rank is one.

**Exponential formula.** A labeled connected fiber contributes
\[
L(z;u,v)=zuv\sum_{p,q,r\ge0}
 \frac{(uz)^p(vz)^qz^r}{p!q!r!}(p+1)^r(q+1)^r
=zuv\sum_{p,q\ge0}\frac{(uz)^p(vz)^q}{p!q!}
\exp\bigl((p+1)(q+1)z\bigr).
\]
The initial factor \(z\) singles out the marked fixed point. Each pair is a **set** of independently labeled such fibers, and its composite rank is the number of fibers. The labeled exponential formula therefore gives \(F(z;u,v,w)=\exp(wL(z;u,v))\), as claimed.

**Sharp support.** If \(k=|C|\), let \(p_c,q_c,r_c\) be the sizes of the three auxiliary subsets in the fiber above \(c\). Then \(a=k+\sum_cp_c\), \(b=k+\sum_cq_c\), and \(n=k+\sum_c(p_c+q_c+r_c)\). This proves the three necessary inequalities. Conversely, whenever the inequalities hold, choose \(k-1\) singleton fibers and one fiber with \(p=a-k\), \(q=b-k\), \(r=n-a-b+k\) and any valid images; all quantities are nonnegative, yielding an actual pair. This proves exact support, including boundary equality.

For reproduction without symbolic formal exponentials, define
\[
B_m(u,v)=m\sum_{p+q+r=m-1}\binom{m-1}{p,q,r}
 (p+1)^r(q+1)^r u^{p+1}v^{q+1},\quad m\ge1.
\]
If \(A_n(u,v,w)=\sum_{a,b,k}N_{n;a,b,k}u^av^bw^k\), then \(A_0=1\) and
\[
A_n(u,v,w)=w\sum_{m=1}^n\binom{n-1}{m-1}
 B_m(u,v)A_{n-m}(u,v,w).
\]
This integer-polynomial recurrence follows by selecting the component containing label one, and is sufficient to compute every joint-rank coefficient exactly.

## Verification
Run `python3 verify.py` with Python 3 and no external dependencies. The script independently enumerates all idempotent maps and all commuting ordered pairs for \(1\le n\le5\), records every triple of image cardinalities, then compares each rank cell with the integer-polynomial component recurrence. For these five sizes there are respectively \(1,3,10,41,196\) idempotent maps and \(1,7,58,601,7616\) commuting pairs. The script also checks that the support criterion is both necessary and sufficient for every candidate rank triple in the tested ranges. This is finite corroboration; the proof above establishes all \(n\).

## Relationship to prior work
Araújo and Konieczny (2010, arXiv:1007.4845) establish a commuting criterion for arbitrary transformations relative to a fixed idempotent and classify the **largest subsemilattices** of \(T_n\). Their criterion is compatible with the common-fiber analysis, but their maximal-family theorem and criteria do not state the joint rank enumerator. Dolinka and East (2014, arXiv:1407.3312) enumerate **individual idempotents** in partition-preserving transformation monoids; taking one block recovers the classical one-idempotent rank count but does not supply this ordered commuting-pair distribution. André, Araújo and Konieczny (2010/2011) describe idempotent-generated subsemigroups of regular centralizers, rather than these rank-refined fibers. The older paper of Konieczny (2002) describes transformation centralizers of fixed idempotents; its complete text could not be obtained for decisive detailed comparison, so an implicit precursor remains possible.

## Limitations
This is a count on a finite labeled set; it does not classify commuting pairs up to conjugation, enumerate maximal semilattices, or provide asymptotic formulas. The structural decomposition is elementary, and related centralizer literature may contain implicit specializations; historical-priority uncertainty remains. The finite verifier does not constitute an independent proof or validation for all sizes.

## References
1. J. Araújo and J. Konieczny, *The Largest Subsemilattices of the Semigroup of Transformations on a Finite Set*, arXiv:1007.4845v1 (submitted 2010-07-27), https://arxiv.org/html/1007.4845v1.
2. I. Dolinka and J. East, *Idempotent generation in the endomorphism monoid of a uniform partition*, arXiv:1407.3312 (first posted 2014-07-11), https://arxiv.org/pdf/1407.3312.
3. J. André, J. Araújo and J. Konieczny, *Regular centralizers of idempotent transformations*, Semigroup Forum 82 (2011), 307–318, DOI:10.1007/s00233-010-9274-6, https://repositorioaberto.uab.pt/bitstream/10400.2/2001/1/AndreAraujoKoniecznyPublishedVersion.pdf.
4. J. Konieczny, *Semigroups of transformations commuting with idempotents*, Algebra Colloquium 9 (2002), 121–134 (full text not inspected).
