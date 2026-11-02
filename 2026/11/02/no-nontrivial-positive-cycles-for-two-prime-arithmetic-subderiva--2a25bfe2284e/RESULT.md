# No nontrivial positive cycles for two-prime arithmetic subderivatives

## Finding

**Theorem.** Let \(p\) and \(q\) be any distinct primes. Define, for positive integers \(n\),
\[
D_{\{p,q\}}(n)=n\left(\frac{\nu_p(n)}p+\frac{\nu_q(n)}q\right),
\]
where \(\nu_s(n)\) is the exponent of prime \(s\) in \(n\). For every \(n\ge1\) and \(k\ge1\),
\[
D_{\{p,q\}}^{\,k}(n)=n\quad\Longrightarrow\quad D_{\{p,q\}}(n)=n.
\]
The complete set of positive periodic points is
\[
\left\{p^p m:\ m\ge1,\ \gcd(m,pq)=1\right\}
\;\cup\;
\left\{q^q m:\ m\ge1,\ \gcd(m,pq)=1\right\}.
\]
Thus no two-prime arithmetic subderivative has a positive cycle of least period greater than one. This statement includes every pair of distinct primes, not merely a selected pair.

## Assumptions and scope

All primes and integers are ordinary positive rational integers; \(p\neq q\), \(n\ge1\), and the iterate count \(k\ge1\) are arbitrary. The arithmetic subderivative is integer-valued: the two terms \(n\nu_p(n)/p\) and \(n\nu_q(n)/q\) are integers separately whenever their corresponding exponents are nonzero. The theorem addresses *positive* periodic points. Zero is fixed under the usual convention \(D_{\{p,q\}}(0)=0\), but is not included in the displayed positive classification. No assertion is made for supports of three or more primes or for nonperiodic trajectories.

## Proof

Put \(P=pq\). Suppose \(n_0,n_1,\dots,n_{L-1}\), with cyclic indexing, is any positive periodic orbit. Let
\[
a_i=\nu_p(n_i),\qquad b_i=\nu_q(n_i),\qquad U_i=q a_i+p b_i.
\]
Then \(U_i\) is a positive integer because \(n_{i+1}=D_{\{p,q\}}(n_i)>0\). By the defining equation,
\[
n_{i+1}=\frac{n_i U_i}{P}.
\]
Multiplying these \(L\) equalities around the orbit gives the **exact multiplier identity**
\[
\prod_{i=0}^{L-1}U_i=P^L.
\tag{1}
\]
Consequently *every* \(U_i\) has no prime factors except \(p\) and \(q\): each divides \(P^L\). This restriction is essential; it is not asserted for general nonperiodic trajectories.

For all successive terms, the prime exponents satisfy
\[
a_{i+1}=a_i+\nu_p(U_i)-1,\qquad
b_{i+1}=b_i+\nu_q(U_i)-1,
\]
so the multiplier evolves by
\[
U_{i+1}=T(U_i),\qquad
T(U)=U-(p+q)+q\nu_p(U)+p\nu_q(U).
\tag{2}
\]

**Threshold lemma.** If \(U>P\) is a positive integer whose prime factors lie in \(\{p,q\}\), then \(T(U)>P\).

Write \(U=p^a q^b\), with \(a,b\ge0\). If \(a,b\ge1\), equation (2) gives
\[
T(U)=U+q(a-1)+p(b-1)\ge U>P.
\]
If \(b=0\), then \(U=p^a>P\) forces \(a\ge2\), and \(p^{a-1}>q\) gives \(U-P\ge p\). Therefore
\[
T(U)-P=(U-P)+q(a-1)-p\ge q(a-1)>0.
\]
If \(a=0\), the symmetric argument gives \(b\ge2\), \(U-P\ge q\), and
\[
T(U)-P=(U-P)+p(b-1)-q\ge p(b-1)>0.
\]
These three cases prove the lemma. There is no case \(a=b=0\) with \(U>P\).

Now suppose one multiplier on the cycle satisfies \(U_i>P\). It is \(\{p,q\}\)-smooth by (1), and the threshold lemma with (2) yields \(U_{i+1}>P\). Repeating cyclically shows that *all* multipliers exceed \(P\), contrary to (1). Therefore every \(U_i\le P\). Their product equals \(P^L\), so each \(U_i=P\). The original orbit equation implies \(n_{i+1}=n_i\). Every positive periodic orbit is a fixed point.

Finally, \(D_{\{p,q\}}(n)=n\) holds precisely when
\[
q\nu_p(n)+p\nu_q(n)=pq.
\]
Set \(a=\nu_p(n)\), \(b=\nu_q(n)\). Reducing \(qa+pb=pq\) modulo \(p\), using \(\gcd(p,q)=1\), yields \(p\mid a\). Since \(0\le a\le p\), either \((a,b)=(p,0)\) or \((a,b)=(0,q)\). Prime factors other than \(p,q\) are unrestricted, so \(n=p^p m\) or \(n=q^q m\) with \(\gcd(m,pq)=1\). Conversely both forms satisfy the fixed-point equation. This proves all assertions. \(\square\)

## Verification

The independent finite arithmetic tests implemented in `proof_check.py` check the threshold lemma on 120 distinct prime pairs with \(p<q\le53\) and \(38,212\) smooth multipliers above the threshold; they compare the fixed-point characterization in 70,000 bounded positive cases and sample bounded trajectories. The script also checks that smoothness cannot be dropped from the threshold lemma: for \(p=2,q=3\), the nonsmooth multiplier \(U=7>6\) has \(T(U)=2\). All tests passed. Their finite scope is explicitly separate from the infinite proof above, which uses equations (1), (2), and the threshold lemma for arbitrary primes and orbit lengths. The script uses only Python's standard library.

## Relationship to prior work

Merikoski, Haukkanen and Tossavainen (2019) introduce arithmetic subderivatives for prime sets, defining the object of this theorem. Emmons and Xiao (2022) analyze iterates for a *single-prime* arithmetic partial derivative. Talukdar and Saikia (2025) examine general subderivative identities, and their 2026 paper studies differential equations and determines fixed points for general prime sets. Knowing all fixed points alone does not rule out cycles of larger period. The 2019 paper on discontinuity addresses analytic behavior and the single-step eigenvalue equation rather than classification of positive periodic orbits.

An accessible prior public mathematical record, titled *No nontrivial positive cycles for the \(\{2,3\}\) arithmetic subderivative* (record identifier `19603ae53ef5`), establishes the analogous statement for the *single pair* \(\{2,3\}\). Its theorem is exactly subsumed by the present arbitrary-prime-pair result. Its full proof text was unavailable for inspection; the comparison is grounded in its accessible statement, not claimed full-text noncoverage. Searches of accessible records did not uncover a theorem encompassing **every** pair of distinct primes. The contribution is the arbitrary-pair generality and the prime-smooth threshold argument, not the previously known single-pair case or fixed-point equation.

## Limitations

The argument uses the fact that \(\{p,q\}\)-smooth multiplier dynamics have an invariant strict region above \(pq\); it does not establish an analogous property for prime sets of size three or more. No claim is made about convergence, eventual behavior of arbitrary positive starting integers, or periodic rational points. Literature searches and comparison cannot guarantee that an unindexed equivalent result does not exist. A separate independent mathematical audit has not been performed.

## References

1. J. K. Merikoski, P. Haukkanen, T. Tossavainen, *Arithmetic Subderivatives and Leibniz-Additive Functions*, arXiv:1901.02216v1, 8 January 2019, https://arxiv.org/abs/1901.02216.
2. B. Emmons, X. Xiao, *The Arithmetic Partial Derivative*, arXiv:2201.12453v1, 28 January 2022, https://arxiv.org/abs/2201.12453.
3. P. Haukkanen, J. K. Merikoski, T. Tossavainen, *Arithmetic Subderivatives: Discontinuity and Continuity*, Journal of Integer Sequences 22 (2019), Article 19.7.4, https://cs.uwaterloo.ca/journals/JIS/VOL22/Merikoski/meri6.html.
4. C. Talukdar, H. K. Saikia, *Arithmetic Subderivatives Relative to Subsets of Primes* (2025), https://www.rgnpublications.com/journals/index.php/cma/article/download/3430/1865/12614.
5. C. Talukdar, H. K. Saikia, *Arithmetic Differential Equations Defined by Generalized Subderivatives*, International Journal of Mathematics Trends and Technology 72 (2026), 21–27, DOI:10.14445/22315373/IJMTT-V72I1P104.
6. *No nontrivial positive cycles for the \(\{2,3\}\) arithmetic subderivative*, publicly indexed mathematical finding, identifier `19603ae53ef5` (accessible statement; full text unavailable).
