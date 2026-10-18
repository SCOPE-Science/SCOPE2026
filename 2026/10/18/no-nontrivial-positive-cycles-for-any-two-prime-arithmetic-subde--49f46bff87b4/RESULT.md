# No nontrivial positive cycles for any two-prime arithmetic subderivative

## Finding
Let \(p<q\) be arbitrary distinct primes, \(\nu_p\) the \(p\)-adic valuation on positive integers, and
\[
D_{\{p,q\}}(n)=n\left(\frac{\nu_p(n)}p+\frac{\nu_q(n)}q\right).
\]
For every positive integer \(n\) and every integer \(L\ge1\),
\[
D_{\{p,q\}}^L(n)=n\quad\Longrightarrow\quad D_{\{p,q\}}(n)=n.
\]
The complete positive periodic-point set is
\[
\{p^p m:\gcd(m,pq)=1\}\ \cup\ \{q^q m:\gcd(m,pq)=1\}.
\]

## Assumptions and scope
The two primes \(p<q\) are arbitrary and fixed; \(n\) and the period \(L\) are positive integers. A positive periodic orbit has all iterates positive. If the map is extended by \(D(0)=0\), zero is a further fixed point, excluded from this result. The theorem makes no assertion that arbitrary orbits converge, or that larger prime supports admit nontrivial cycles.

## Proof
Suppose \(n_0,\dots,n_{L-1}\) is a positive periodic orbit, indexed modulo \(L\). Write
\[
n_i=m_i p^{a_i}q^{b_i},\qquad \gcd(m_i,pq)=1,\qquad a_i,b_i\ge0.
\]
Define the positive integer \(c_i=q a_i+p b_i\). The recurrence has the exact ratio
\[
\frac{n_{i+1}}{n_i}=\frac{c_i}{pq}.
\]
Multiplying around the orbit yields
\[
\prod_{i=0}^{L-1}c_i=(pq)^L.
\]
Therefore every \(c_i\) is supported only at \(p\) and \(q\); write \(c_i=p^{u_i}q^{v_i}\) with \(u_i,v_i\ge0\). Taking valuations in the displayed ratio gives the exact updates
\[
a_{i+1}=a_i+u_i-1,\qquad b_{i+1}=b_i+v_i-1,
\]
and hence
\[
c_{i+1}-c_i=q(u_i-1)+p(v_i-1). \tag{1}
\]

**Threshold lemma.** On such a positive orbit, \(c_i<pq\) is impossible, and whenever \(c_i\ge pq\) one has \(c_{i+1}\ge pq\).

To prove this, first suppose \(c_i<pq\). Because \(c_i\) is a positive \(\{p,q\}\)-smooth integer, it is either \(p^u\) for \(u\ge1\) or \(q\): both prime factors already contribute at least \(pq\), and \(q^2>pq\). If \(c_i=p\) or \(c_i=q\), (1) gives \(c_{i+1}=0\), impossible on a positive periodic orbit. If instead \(c_i=p^u\) with \(u\ge2\), (1) yields
\[
c_{i+1}-c_i=q(u-1)-p\ge q-p>0.
\]
Now assume \(c_i\ge pq\). If \(u_i,v_i\ge1\), equation (1) makes \(c_{i+1}\ge c_i\). If \(v_i=0\), then necessarily \(u_i\ge2\), so the same strict increase holds. The remaining case \(u_i=0\) has \(v_i\ge2\), and equation (1) gives
\[
c_{i+1}=q^{v_i}-q+p(v_i-1)\ge q^2-q+p\ge pq,
\]
where the last inequality follows from \(q^2-q+p-pq=q(q-p-1)+p\ge p>0\), since \(q>p\). This proves forward invariance of the range \([pq,\infty)\) and strict increase at any allowed step below \(pq\). A finite positive periodic orbit cannot remain forever strictly increasing below \(pq\), nor can it cross into a forward-invariant upper range and return. The lemma follows.

Since every \(c_i\ge pq\) and their product is \((pq)^L\), all must equal \(pq\). The exact ratio then forces \(n_{i+1}=n_i\). Finally, solving \(q a+p b=pq\) in nonnegative integers: reduction modulo \(p\) shows \(p\mid a\); as \(0\le a\le p\), either \((a,b)=(p,0)\) or \((a,b)=(0,q)\). Conversely both exponent pairs give \(D(n)=n\). The theorem follows. \(\square\)

## Verification
The standalone `verify.py` implements the derivative with integer arithmetic, checks the valuation-transition identity, the threshold lemma on thousands of smooth exponent states for 45 prime pairs, and scans finite positive orbits and fixed-point equations. It prints a successful completion message when run with Python 3. These computations are regression checks; the universal statement follows from the proof for arbitrary primes and periods, not from finite enumeration.

## Relationship to prior work
Merikoski, Haukkanen, and Tossavainen introduced arithmetic subderivatives for sets of primes in 2019. Emmons and Xiao studied iteration for one-prime partial derivatives in 2022. Talukdar and Saikia (2026, Theorem 3.4) classified fixed points for all supports and explicitly named periodic points of least period greater than one as a further direction; thus the formula for the fixed families above is **not** claimed original. A published 2026 result already excludes nontrivial positive cycles for the one pair \(\{2,3\}\), using a small-smoothness argument. The present finding extends the exclusion simultaneously to **every** two-prime support using an invariant threshold and a multiplicative product constraint, which is not implied by the single-pair theorem.

## Limitations
No result is proved here about periodic cycles for supports of cardinality at least three, about unbounded orbits, or about convergence rates. Novelty assessments are relative to the inspected literature and searchable mathematical records; an unindexed general two-prime theorem could exist. The fixed-point families themselves are known from the 2026 paper; the new part is their exhaustiveness among positive periodic orbits for all two-prime supports.

## References
1. J. K. Merikoski, P. Haukkanen, and T. Tossavainen, “Arithmetic Subderivatives and Leibniz-Additive Functions,” arXiv:1901.02216v1 (first public 8 January 2019), *Annales Mathematicae et Informaticae* 50 (2019), 145–157, DOI:10.33039/ami.2019.03.003; primary MSC 11A25.
2. B. Emmons and X. Xiao, “The Arithmetic Partial Derivative,” arXiv:2201.12453v1 (28 January 2022), *Journal of Integer Sequences* 25 (2022).
3. C. Talukdar and H. K. Saikia, “Arithmetic Differential Equations Defined by Generalized Subderivatives,” *International Journal of Mathematics Trends and Technology* 72 (2026), 21–27, DOI:10.14445/22315373/IJMTT-V72I1P104; especially Theorem 3.4 and Section 5.
4. “No nontrivial positive cycles for the \(\{2,3\}\)-arithmetic subderivative,” 2026 public result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-no-nontrivial-positive-cycles-for-the-2-3-arithmetic-subderivati--19603ae53ef5.
