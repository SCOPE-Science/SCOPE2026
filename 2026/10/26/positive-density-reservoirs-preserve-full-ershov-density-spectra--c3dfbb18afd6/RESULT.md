# Positive-density reservoirs preserve full Ershov density spectra

## Finding

Let \(f:\omega\to\omega\) be computable, let \(S\subseteq\omega\) be computable with rational asymptotic density \(d\in(0,1)\), and enumerate \(S=\{s_0<s_1<\cdots\}\). Assume \(f(n)\ge1\) for every \(n\notin S\) and that \(g(j)=f(s_j)\) is computable, nondecreasing, and unbounded. Then the set of asymptotic densities of \(f\)-c.e. sets is exactly the set of asymptotic densities of \(\Delta^0_2\) sets.

Here, a set \(A\) is \(f\)-c.e. if it has a computable approximation \(a(n,s)\in\{0,1\}\) with \(a(n,0)=0\), \(\lim_s a(n,s)=\mathbf 1_A(n)\), and at most \(f(n)\) changes at each coordinate \(n\).

A concrete instance is \(f(2j)=j+1\) and \(f(2j+1)=1\). This bound is not globally nondecreasing; for every \(k\ge2\), the set of coordinates with allowance at least \(k\) has density exactly \(1/2\). Nevertheless, its \(f\)-c.e. sets realize every density realized by a \(\Delta^0_2\) set.

## Assumptions and scope

Write \(\rho(A)=\lim_{n\to\infty}|A\cap[0,n)|/n\) whenever this limit exists. The density spectrum of a class is the set of all such limits for members of that class. The set \(S\) has rational density strictly between zero and one; its increasing enumeration and the increasing enumeration of its complement are computable. The condition \(f(n)\ge1\) off \(S\) allows any computable baseline subset of the complement to be encoded with at most one change per coordinate. No necessary-and-sufficient characterization for arbitrary nonmonotone bounds is claimed.

## Proof

Let \(r\) be the density of some \(\Delta^0_2\) set. By the density characterization stated as Theorem 2.1 in Downey–Jockusch–McNicholl–Schupp, \(r\) is a \(\Delta^0_3\) real, and every \(\Delta^0_3\) real in \([0,1]\) is the density of a \(\Delta^0_2\) set.

Choose a rational number \(a\) in
\[
[\max(0,r-d),\,\min(r,1-d)].
\]
This interval is nonempty. For \(r=0\), take \(a=0\); for \(r=1\), take \(a=1-d\); for \(0<r<1\), it has positive length and therefore contains a rational. Set \(u=(r-a)/d\). The choice of \(a\) ensures \(0\le u\le1\), and since \(a,d\) are rational, \(u\) is also a \(\Delta^0_3\) real.

Let \(h\) be the increasing computable enumeration of \(S\), and let \(e\) be the increasing computable enumeration of \(\omega\setminus S\). Choose a computable set \(E\) of rational density \(a/(1-d)\), for example a periodic set. Then \(C=e(E)\) is a computable subset of \(\omega\setminus S\) and has density \(a\). The density-scaling identity used in Lemma 3.4 of the cited paper says that if \(h\) is increasing and both \(X\) and the range of \(h\) have densities, then
\[
\rho(h(X))=\rho(\operatorname{range}(h))\rho(X).
\]
It follows directly by comparing the counts below \(n\) with the counts below the number of elements of the range below \(n\).

Because \(u\) is \(\Delta^0_3\), Theorem 2.1 supplies a \(\Delta^0_2\) set with density \(u\). Apply Theorem 5.1 of the same paper to the computable, nondecreasing, unbounded function \(g(j)=f(s_j)\). There is a \(g\)-c.e. set \(D\) with density \(u\). Put \(B=h(D)\subseteq S\). The approximation for \(B(s_j)\) is the approximation for \(D(j)\), so it changes at most \(g(j)=f(s_j)\) times; outside \(S\), \(B\) is constantly zero. Hence \(B\) is \(f\)-c.e. and, by density scaling, \(\rho(B)=du=r-a\).

The sets \(B\) and \(C\) are disjoint. Their union \(A=B\cup C\) is \(f\)-c.e.: on \(S\) it uses the approximation to \(B\), and off \(S\) it is the computable set \(C\), requiring at most one change where \(f(n)\ge1\). Its density is
\[
\rho(A)=\rho(B)+\rho(C)=(r-a)+a=r.
\]
Thus every density of a \(\Delta^0_2\) set is attained by an \(f\)-c.e. set. Conversely, every \(f\)-c.e. set is \(\Delta^0_2\), so the density spectra are equal. The argument includes the endpoint cases \(r=0\) and \(r=1\).

For the concrete example, take \(S=2\omega\), \(d=1/2\), and \(s_j=2j\). Then \(g(j)=j+1\) is nondecreasing and unbounded, while \(f(2j+1)=1\) off \(S\). For each \(k\ge2\), all sufficiently large even numbers and no odd numbers satisfy \(f(n)\ge k\), giving density \(1/2\).

## Verification

The proof uses only the cited density-spectrum theorem, the cited density-scaling identity, and computable periodic sets of rational density. It does not infer an infinite theorem from a finite experiment. The change bound is checked coordinatewise on the disjoint sets \(S\) and its complement. The rational interval for \(a\) handles \(r=0\) and \(r=1\) explicitly. No external computation is needed for the proof.

## Relationship to prior work

Downey, Jockusch, McNicholl, and Schupp prove that a globally nondecreasing unbounded computable change bound preserves the density spectrum of \(\Delta^0_2\) sets (Theorem 5.1 of *Asymptotic density and the Ershov hierarchy*). Their Lemma 3.4 supplies the density-scaling identity used here. The present statement allows the global bound to oscillate: only its restriction to one computable positive-density reservoir must be nondecreasing and unbounded, while one change per coordinate suffices off that reservoir. The paper states neither this reservoir criterion nor the alternating example. This is a structural extension of its construction, not a classification of every nonmonotone change bound.

## Limitations

The condition is sufficient, not necessary. Bounds for which every high-change threshold set has irregular or vanishing density are not classified here. The proof is a derived extension of established theorems; an unindexed equivalent observation in the broader computability literature remains a residual originality risk. Independent audit has not been performed.

## References

- R. Downey, C. G. Jockusch Jr., T. H. McNicholl, and P. E. Schupp, *Asymptotic density and the Ershov hierarchy*, arXiv:1309.0137v1, first publicly posted 2013-08-31; primary MSC 03D25, secondary MSC 03D78. Relevant material: Theorem 2.1, Lemma 3.4, and Theorem 5.1.
- R. Downey, C. G. Jockusch Jr., and P. E. Schupp, *Asymptotic density and computably enumerable sets*, arXiv:1307.0040, first publicly posted 2013-06-28; primary MSC 03D25. Background on the complexity of asymptotic densities.
