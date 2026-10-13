# Prime-gap rigidity for arithmetic subderivative cycles

## Finding
For every pair of distinct primes \(p<q\) satisfying \(q\le p^p\), define the arithmetic subderivative
\[
D_{\{p,q\}}(n)=n\left(\frac{\nu_p(n)}{p}+\frac{\nu_q(n)}{q}\right)
\]
on positive integers, where \(\nu_r(n)\) is the exponent of the prime \(r\) in \(n\). If any positive integer \(n\) is periodic, meaning \(D_{\{p,q\}}^L(n)=n\) for some integer \(L\ge1\), then it is already fixed. Its complete positive periodic set is
\[
\{p^p m:\gcd(m,pq)=1\}\;\cup\;\{q^q m:\gcd(m,pq)=1\}.
\]

Equivalently, for arbitrary distinct primes \(p<q\), the existence of any positive cycle of length greater than one would force the quantitative gap \(q>p^p\). This necessary obstruction is an implication of the theorem; no assertion that cycles exist beyond the threshold is made.

## Assumptions and scope
Extend the map by \(D_{\{p,q\}}(0)=0\) to make every iterate defined. The cycles considered contain only positive integers, and the usual integer valuations apply to those integers. The case \(D_{\{p,q\}}(n)=0\) is not a positive periodic orbit. Primes not in \(\{p,q\}\) may divide \(n\); they are accounted for without being assumed absent. The prime gap condition \(q\le p^p\) is imposed only on the nonexistence conclusion, not on the monotonic-valuation lemma below.

## Proof
Fix distinct primes \(p<q\). Write any positive integer uniquely as \(n=m p^a q^b\) with \(a,b\ge0\) and \(\gcd(m,pq)=1\). Directly from the definition,
\[
D_{\{p,q\}}(n)=\frac{n}{pq}(aq+bp).
\]
In particular, for every prime \(r\notin\{p,q\}\), when the derivative is positive,
\[
\nu_r(D_{\{p,q\}}(n))=\nu_r(n)+\nu_r(aq+bp).
\]
The valuation of every outside prime is therefore nondecreasing along an orbit. If a positive orbit is periodic, every outside valuation must return to its starting value. Consequently, **at every point of that orbit the positive integer \(aq+bp\) has no prime factors outside \(\{p,q\}\)**; call this the smoothness condition. The cofactor \(m\) is also unchanged throughout the orbit.

Choose a largest integer in any purported positive periodic orbit and denote it \(n_*=m p^a q^b\). Since its successor cannot exceed it,
\[
\frac ap+\frac bq\le1,
\qquad 0\le a\le p,\quad 0\le b\le q.
\]
At least one of \(a,b\) is positive; otherwise the next derivative is zero.

**Both exponents positive.** If \(a,b>0\), the preceding bound implies \(1\le a<p\) and \(1\le b<q\). Hence \(aq+bp\) is coprime to \(p\) (because \(p\nmid a\)) and to \(q\) (because \(q\nmid b\)). It is greater than one and therefore violates the smoothness condition. Thus the maximal orbit element must lie on one of the two coordinate axes.

**Only the smaller prime divides the maximal orbit element.** If \(a>0,b=0\), then \(1\le a\le p\) and \(aq+bp=aq\). The smoothness condition, along with \(a\le p<q\), forces \(a=1\) or \(a=p\). At \(a=1\), differentiation sends \(mp\) to the \(\{p,q\}\)-free integer \(m\), whose next derivative is zero, ruling out a positive period. At \(a=p\), the point \(mp^p\) is fixed.

**Only the larger prime divides the maximal orbit element.** If \(a=0,b>0\), then \(1\le b\le q\) and \(aq+bp=bp\). The smoothness condition forces
\[
b=1,\qquad b=q,\qquad\text{or}\qquad b=p^k<q\quad(k\ge1).
\]
At \(b=1\), the point differentiates to \(m\), then to zero. At \(b=q\), the point \(mq^q\) is fixed. It remains to exclude \(b=p^k<q\) under \(q\le p^p\).

Here the gap bound forces \(1\le k<p\). The first successor of \(m q^{p^k}\) is
\[
D_{\{p,q\}}(m q^{p^k})=m p^k q^{p^k-1}.
\]
For this new point the integer appearing in the smoothness condition is
\[
w=kq+p(p^k-1).
\]
Because \(0<k<p\), reduction modulo \(p\) gives \(w\equiv kq\not\equiv0\pmod p\). Because \(0<p^k-1<q\) and \(p\ne q\), reduction modulo \(q\) gives \(w\equiv p(p^k-1)\not\equiv0\pmod q\). Thus \(w>1\) is coprime to \(pq\), contradicting the smoothness condition at this second point. No such maximal element can occur.

We have shown that the maximal element of every positive periodic orbit must be one of the fixed points \(mp^p\) or \(mq^q\), with \(\gcd(m,pq)=1\). An orbit containing a fixed point is constant, proving that no longer positive cycle exists. Conversely, direct substitution verifies that both displayed families are fixed. This completes the classification for every \(p<q\) with \(q\le p^p\).

The proof also shows why the cutoff arises: an arbitrary nonconstant two-prime cycle would have to reach a maximal point of the form \(m q^{p^k}\) with \(k\ge p\), hence would require \(q>p^p\). The cutoff is necessary, not claimed sufficient, for a nontrivial cycle.

## Verification
The standalone Python 3 program `verify.py` uses only the standard library. Run `python verify.py` in the directory containing that file. It independently computes direct integer subderivatives, derives valuation-exponent transitions by factoring the integer \(aq+bp\), and checks the transition formula, fixed-point examples, and the two-step obstruction for all candidate maxima in a specified finite prime/exponent box. The accompanying `verification_output.txt` records an actual successful run.

All numerical tests are finite regression checks. The mathematical proof above, not an exhaustion of the integers or primes, supplies the unbounded quantifiers.

## Relationship to prior work
Merikoski, Haukkanen, and Tossavainen introduced arithmetic subderivatives for sets of primes in their 2019 paper. Emmons and Xiao's 2022 study classifies dynamics for a single prime and explicitly identifies finite-set subderivatives as a natural next dynamical question. Talukdar and Saikia's 2026 study classifies fixed points for arbitrary sets of primes but treats nontrivial periodic points as a further direction. A public 2026 mathematical note establishes the no-nontrivial-cycle result for the particular set \(\{2,3\}\); that instance is already covered and is not claimed to be new here.

The distinction is that the present argument proves a uniform **quantitative necessary prime gap** and rules out nontrivial periodic behavior for **every** pair of primes \(p<q\le p^p\). Existing fixed-point classifications do not themselves imply that all periodic points are fixed. This work does not claim to classify all prime pairs or to give a positive cycle beyond the threshold.

## Limitations
For \(q>p^p\), the proof supplies a structural necessary condition for a nontrivial cycle but no existence or nonexistence theorem. It does not address three or more supported primes. Independent mathematical and bibliographic auditing has not been carried out, and unindexed equivalent results may exist. The published fixed-point classification and the special case \(\{2,3\}\) are prior work; only the uniform absence of nontrivial cycles across the stated prime-gap range is proposed as new.

## References
1. J. K. Merikoski, P. Haukkanen, T. Tossavainen, “Arithmetic Subderivatives and Leibniz-Additive Functions,” arXiv:1901.02216v1, first public 2019-01-08, https://arxiv.org/html/1901.02216v1; Annales Mathematicae et Informaticae 50 (2019), 145–157.
2. B. Emmons, X. Xiao, “The Arithmetic Partial Derivative,” arXiv:2201.12453v1, first public 2022-01-28, https://arxiv.org/html/2201.12453v2; Journal of Integer Sequences 25 (2022).
3. C. Talukdar, H. K. Saikia, “Arithmetic Differential Equations Defined by Generalized Subderivatives,” International Journal of Mathematics Trends and Technology 72 (2026), 21–27, DOI:10.14445/22315373/IJMTT-V72I1P104, https://ijmttjournal.org/public/assets/volume-72/issue-1/IJMTT-V72I1P104.pdf.
4. C. Talukdar, H. K. Saikia, “Prime-Supported Leibniz-Additive Functions and Integer Eigenpoints of Generalized Arithmetic Subderivatives,” Far East Journal of Mathematical Sciences 143 (2026), 1057–1071, DOI:10.17654/0972087126061, https://pphmjopenaccess.com/fejms/article/download/4408.
5. “No nontrivial positive cycles for the \(\{2,3\}\)-arithmetic subderivative,” publicly available mathematical note, 2026-10-04, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-no-nontrivial-positive-cycles-for-the-2-3-arithmetic-subderivati--19603ae53ef5.
