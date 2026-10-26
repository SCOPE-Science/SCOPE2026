# An exact \(2p-4\) Dedekind-sum fiber at every odd prime cube

## Finding
For every odd prime \(p\), the exact set of reduced residues \(a\) modulo \(p^3\) satisfying
\[
S(a,p^3)=3-\frac{p^2+2}{p^3}
\]
is the union of two explicitly disjoint progressions
\[
\{p-1+jp^2:1\le j\le p-2\}\quad\text{and}\quad
\{p^2-p-1+jp^2:0\le j\le p-3\}.
\]
In particular this nonzero value has precisely \(2p-4\) preimages. These are all nontrivial units; it is a complete fiber, not merely a construction of coincident values. The normalized Dedekind sum is \(S(a,b)=12s(a,b)\).

## Assumptions and scope
Throughout, \(p\ge3\) is prime, \(b>0\), \(\gcd(a,b)=1\), and
\[
s(a,b)=\sum_{r=1}^{b-1}\bigl((r/b)\bigr)\bigl((ar/b)\bigr),
\qquad ((x))=\begin{cases}x-\lfloor x\rfloor-1/2,&x\notin\mathbb Z,\\0,&x\in\mathbb Z.\end{cases}
\]
Residues \(a\) are represented by integers in \(1,\dots,p^3-1\). We use the standard identity \(S(a,b)=S(a^*,b)\) when \(aa^*\equiv1\pmod b\), and \(S(-a,b)=-S(a,b)\).

## Proof
**The three-term identity.** We use the classical Rademacher–Dieter relation in the following explicit orientation. For integers \(A,C\), positive \(B,D\), \(\gcd(A,B)=\gcd(C,D)=1\), and \(Q=AD-BC>0\), choose integers \(J,K\) such that \(-CJ+DK=1\), and set \(R=AJ-BK\). Then
\[
S(A,B)=S(C,D)+S(R,Q)+\frac{B^2+D^2+Q^2}{BDQ}-3.\tag{1}
\]
The second argument of each Dedekind sum is positive; a negative first argument is allowed. This is the three-term relation written in Girstmair's 2021 Proposition 1 proof and in the 2014 paper's derivation.

**Step 1: an auxiliary relation over \(\mathbb F_p\).** Fix \(j\) with \(1\le j\le p-2\). Put \(k\equiv-(j+1)j^{-1}\pmod p\). In (1) take \(A=j+1\), \(B=p\), \(C=j\), \(D=p\); then \(Q=p\) and \(R\equiv k\pmod p\). Thus
\[
S(j,p)+S(k,p)-S(j+1,p)=3-\frac3p.\tag{2}
\]
All three residues are units modulo \(p\), including \(k\).

**Step 2: a bridge through \(p(p-1)\).** Write \(H=p(p-1)\). By CRT choose \(r\pmod H\) with \(r\equiv j^{-1}\pmod p\) and \(r\equiv-1\pmod{p-1}\); choose \(0<r<H\). Put \(h=(r+1)/(p-1)\). We have \(h\equiv k\pmod p\), so \(\gcd(h,p)=1\). Apply (1) with \(A=-r\), \(B=H\), \(C=-h\), \(D=p\): now \(Q=p\). The associated \(R\) is congruent to \((j+1)^{-1}\pmod p\) (use \(J\equiv h^{-1}\pmod p\) from \(hJ+pK=1\)). Taking the sign of \(S(-r,H)\) into account and using inversion invariance gives
\[
S(r,H)=S(k,p)-S(j+1,p)+3-\frac{p-1}{p}-\frac{2}{p(p-1)}.
\]
Combine this with (2) to obtain the constant identity
\[
S(j,p)+S(r,H)=5-\frac{2}{p-1}.\tag{3}
\]

**Step 3: the constant prime-cube value.** Put \(a_j=p-1+jp^2\). Apply (1) with \(A=a_j\), \(B=p^3\), \(C=j\), \(D=p\). Now \(Q=p(p-1)=H\); the associated numerator \(R=a_jJ-p^3K\), where \(-jJ+pK=1\), satisfies \(R\equiv j^{-1}\pmod p\) and \(R\equiv-1\pmod{p-1}\). Consequently \(S(R,H)=S(r,H)\). Equations (1) and (3) yield
\[
\begin{aligned}
S(a_j,p^3)
&=5-\frac2{p-1}+\frac{p^6+p^2+p^2(p-1)^2}{p^5(p-1)}-3\\
&=3-\frac{p^2+2}{p^3}.\tag{4}
\end{aligned}
\]
Moreover a direct modular multiplication gives
\[
a_j^{-1}\equiv p^2-p-1+(p-2-j)p^2\pmod{p^3}.
\]
For \(1\le j\le p-2\), the right side runs over exactly the second displayed progression. Hence all \(2(p-2)\) candidate residues share the value by (4) and inversion invariance. The two progressions are disjoint modulo \(p^2\) because their residues are \(p-1\) and \(-p-1\), distinct for odd \(p\).

**Step 4: exhaustive exclusion of other residues.** Choose \(c=a_1\) as a witness to (4), and suppose that another reduced residue \(a\) has the same normalized Dedekind sum. The known fractional-part criterion (Girstmair 2013, Theorem 1) implies
\[
(a-c)(ac-1)\equiv0\pmod{p^3}.\tag{5}
\]
Reducing (5) modulo \(p\), where \(c\equiv-1\pmod p\), forces \(a\equiv-1\pmod p\). Write \(a=-1+pu\); similarly \(c=-1+p(1+p)\). After dividing (5) by \(p^2\) and reducing modulo \(p\), one finds \((u-1)(u+1)\equiv0\pmod p\). Since \(p\) is odd, the complete candidate set comprises exactly the \(2p\) residues \(a\equiv-1+p\pmod{p^2}\) or \(a\equiv-1-p\pmod{p^2}\).

Of these \(2p\) residues, the two proven progressions contain \(2p-4\). The remaining four form two inversion pairs: the endpoints \(e_0=p-1\) and \(e_1=p^3-p^2+p-1\) and their inverses. Classical reciprocity
\[
S(v,w)+S(w,v)=\frac{v^2+w^2+1}{vw}-3,
\quad S(1,w)=\frac{(w-1)(w-2)}{w}
\]
gives, using \(p^3\equiv1\pmod{p-1}\),
\[
S(e_0,p^3)=\left(3-\frac{p^2+2}{p^3}\right)+(p^2-1).
\]
Since \(e_1^{-1}\equiv-p-1\pmod{p^3}\), and \(p^3\equiv-1\pmod{p+1}\), reciprocity similarly gives
\[
S(e_1,p^3)=\left(3-\frac{p^2+2}{p^3}\right)-(p^2-1).
\]
Neither endpoint, nor its inverse, takes the target value. This exhausts all candidates from (5) and proves the exact fiber.

## Verification
The bundled `verify.py` computes Dedekind sums by exact-rational reciprocity independently of the three-term proof. It reconstructs the complete claimed fiber for odd primes through 43 and checks the endpoint gaps. Its output is `VERIFY_OK` when the checks pass. These finite computations are corroboration only; the proof above treats every odd prime. The script requires Python 3 and no third-party modules: `python3 verify.py`.

## Relationship to prior work
Girstmair (2014, arXiv:1404.4428) proves families of equal Dedekind sums from Rademacher's formula and gives a complete account of the depth-\(r\ge k/2\) strata at prime-power moduli. Its text explicitly identifies the shallower \(r<k/2\) strata as lacking an analogous classification. The present theorem treats a **particular entire equality fiber** at the first shallower prime-power layer, modulus \(p^3\), with residues \(-1\pm p\pmod{p^2}\), and determines its exact cardinality. The displayed value is different from the \(\pm(p-3+2/p^3)\) values in that paper's Rademacher branch at depth two. The 2013 fractional-part theorem supplies a necessary congruence, not this exact equality classification. The 2021 three-term treatment contains the identity used as a proof tool but no stated formula for this full prime-cube fiber. The theorem is a special case of the general subject, not a new general criterion for equality of arbitrary Dedekind sums.

## Limitations
No claim is made about maximal fiber size among all Dedekind sums at modulus \(p^3\), the complete partition into all fibers, or higher prime powers. Historical studies and unpublished work could contain an equivalent special value; absence from the searches is not a proof of priority. No independent audit is claimed.

## References
- Girstmair, *On Dedekind sums with equal values*, arXiv:1404.4428v1, 2014-04-17; sections 1 and 3, including its three-term proof and the explicitly unresolved lower-depth issue.
- Girstmair, *The number of Dedekind sums with equal fractional parts*, arXiv:1309.4226v1, 2013-09-17; Theorem 1.
- Girstmair, *On the equality of Dedekind sums*, arXiv:2102.06374v1, 2021-02-12; Proposition 1 and its derivation from the three-term identity.
- H. Rademacher, *Zur Theorie der Dedekindschen Summen*, Math. Z. 63 (1956), 445–463.
